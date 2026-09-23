"""
Local Zabbix API docs provider.

Serves pre-downloaded Zabbix API method documentation from a local docs
directory (see scripts/fetch_zabbix_docs.py). No network access is used
at runtime: the content is a snapshot of the Zabbix manual as indexed
by Context7, pinned per Zabbix version.

Layout expected on disk:
    <docs_dir>/<version>/manifest.json
    <docs_dir>/<version>/api/<object>/<action>.md

The docs directory is located by:
    1. ZABBIX_DOCS_DIR environment variable (explicit override)
    2. <repo root>/docs/zabbix (default)
"""

import json
import logging
import re
from pathlib import Path
from typing import Any

from .config import EnvVars, get_env

logger = logging.getLogger(__name__)

MANIFEST_NAME = "manifest.json"
VERSION_DIR_RE = re.compile(r"^\d+\.\d+$")


def _version_sort_key(version: str) -> tuple[str, ...]:
    """Total sort key for a 'major.minor' version directory name.

    Zero-padding makes lexicographic comparison equivalent to numeric
    comparison for digit-only parts ('7.10' after '7.4', '10.0' after
    '7.x'), so no int() conversion and no possible ValueError — the key is
    total over any directory name.
    """
    return tuple(part.zfill(6) for part in version.split("."))


class LocalDocsError(Exception):
    """Raised when local documentation cannot be resolved or is missing."""


def _default_docs_dir() -> Path:
    """Repo-local docs directory: <repo root>/docs/zabbix."""
    return Path(__file__).resolve().parent.parent.parent / "docs" / "zabbix"


def get_docs_dir() -> Path:
    """Resolve the docs directory from the environment or default location."""
    override = get_env(EnvVars.ZABBIX_DOCS_DIR)
    if override:
        return Path(override)
    return _default_docs_dir()


def _resolve_docs_dir(docs_dir: Path | str | None) -> Path:
    """Normalize a caller-supplied docs dir (str or Path) or the default."""
    return Path(docs_dir) if docs_dir else get_docs_dir()


def available_versions(docs_dir: Path | str | None = None) -> list[str]:
    """List Zabbix versions that have a docs snapshot on disk."""
    base = _resolve_docs_dir(docs_dir)
    if not base.is_dir():
        return []
    versions: list[str] = []
    try:
        for child in base.iterdir():
            if child.is_dir() and VERSION_DIR_RE.match(child.name) and (
                child / MANIFEST_NAME
            ).is_file():
                versions.append(child.name)
    except OSError:
        # A directory that exists but cannot be listed (permissions, race)
        # yields "no versions" instead of a crash.
        return []
    return sorted(versions, key=_version_sort_key)


def _load_manifest(version: str, docs_dir: Path | str | None = None) -> dict[str, Any]:
    base = _resolve_docs_dir(docs_dir)
    manifest_path = base / version / MANIFEST_NAME
    if not manifest_path.is_file():
        raise LocalDocsError(
            f"No docs snapshot for Zabbix version '{version}' at '{manifest_path}'. "
            f"Available versions: {', '.join(available_versions(docs_dir)) or '(none)'}"
        )
    try:
        with open(manifest_path, encoding="utf-8") as fh:
            manifest = json.load(fh)
    except (OSError, json.JSONDecodeError) as exc:
        raise LocalDocsError(
            f"Failed to read docs manifest '{manifest_path}': {exc}"
        ) from exc
    if not isinstance(manifest, dict):
        raise LocalDocsError(f"Malformed docs manifest: '{manifest_path}'")
    return manifest


def normalize_version(version: str) -> str:
    """Normalize a Zabbix version to major.minor form (e.g. '7.4.14' -> '7.4')."""
    parts = [p for p in version.strip().split(".") if p.isdigit()]
    if len(parts) < 2:
        raise LocalDocsError(
            f"Unrecognized Zabbix version '{version}' (expected e.g. '7.4' or '7.4.14')"
        )
    return f"{parts[0]}.{parts[1]}"


def _server_version() -> str | None:
    """Best-effort Zabbix server version from the API client, or None."""
    try:
        from .client import get_zabbix_client

        version = str(get_zabbix_client().version)
        return normalize_version(version)
    except Exception as exc:  # noqa: BLE001 - any failure falls back to next source
        logger.debug(f"Could not resolve Zabbix version from server: {exc}")
        return None


def resolve_version(
    version: str | None = None, docs_dir: Path | str | None = None
) -> str:
    """Resolve which docs snapshot to use.

    Resolution order:
      1. explicitly requested version (normalized to major.minor)
      2. running Zabbix server version
      3. ZABBIX_DOCS_VERSION environment variable
      4. newest snapshot on disk
    """
    if version:
        requested = normalize_version(version)
        available = available_versions(docs_dir)
        if requested not in available:
            raise LocalDocsError(
                f"No docs snapshot for Zabbix version '{requested}'. "
                f"Available versions: {', '.join(available) or '(none)'}"
            )
        return requested

    candidate = _server_version()
    if candidate:
        logger.debug(f"Using docs version '{candidate}' from Zabbix server")
        return candidate

    env_version = get_env(EnvVars.ZABBIX_DOCS_VERSION)
    if env_version:
        candidate = normalize_version(env_version)
        if candidate in available_versions(docs_dir):
            logger.debug(f"Using docs version '{candidate}' from {EnvVars.ZABBIX_DOCS_VERSION}")
            return candidate

    versions = available_versions(docs_dir)
    if not versions:
        raise LocalDocsError(
            f"No local Zabbix docs found at '{get_docs_dir()}'. "
            f"Download them with: python scripts/fetch_zabbix_docs.py --version <ver>"
        )
    candidate = versions[-1]
    logger.warning(
        f"Could not determine Zabbix version; falling back to newest "
        f"local docs version '{candidate}'"
    )
    return candidate


def _methods_for(manifest: dict[str, Any]) -> dict[str, list[str]]:
    """Build {object: [actions]} from a manifest."""
    methods: dict[str, list[str]] = {}
    for method in sorted(manifest.get("methods", {})):
        obj, _, action = method.partition(".")
        if not obj or not action:
            continue
        methods.setdefault(obj, [])
        if action not in methods[obj]:
            methods[obj].append(action)
    return methods


def list_methods(
    version: str | None = None, docs_dir: Path | str | None = None
) -> dict[str, list[str]]:
    """Return {object: [actions]} available in the local docs snapshot.

    Args:
        version: Zabbix version, e.g. '7.4'. If None, resolved automatically.
        docs_dir: Override the docs directory (testing).

    Returns:
        {"host": ["create", "delete", "get", ...], "item": [...], ...}
    """
    resolved = resolve_version(version, docs_dir)
    manifest = _load_manifest(resolved, docs_dir)
    return _methods_for(manifest)


def get_method_docs(
    method: str, version: str | None = None, docs_dir: Path | str | None = None
) -> str:
    """Return local documentation for a Zabbix API method.

    Args:
        method: Zabbix method in 'object.action' format, e.g. 'host.get'.
        version: Zabbix version, e.g. '7.4'. If None, resolved automatically.
        docs_dir: Override the docs directory (testing).

    Returns:
        The method documentation as structured text (description, parameters,
        return value) read from the local docs snapshot.

    Raises:
        ValueError: If the method format is invalid or the method is not
            present in the local snapshot.
    """
    parts = method.strip().lower().split(".", 1)
    if len(parts) != 2 or not parts[0] or not parts[1]:
        raise ValueError(
            f"Invalid format: '{method}'. Expected 'object.action' (e.g. host.get)"
        )
    obj, action = parts
    full_method = f"{obj}.{action}"

    resolved_version = resolve_version(version, docs_dir)
    manifest = _load_manifest(resolved_version, docs_dir)
    base = _resolve_docs_dir(docs_dir)

    rel_path = manifest.get("methods", {}).get(full_method)
    if rel_path is None:
        known = _methods_for(manifest)
        available_objects = ", ".join(sorted(known)) or "(none)"
        raise ValueError(
            f"Method '{full_method}' is not available in the local docs snapshot "
            f"for Zabbix {resolved_version}. Known objects: {available_objects}. "
            f"Re-download the snapshot to add it (scripts/fetch_zabbix_docs.py)."
        )

    doc_path = base / resolved_version / rel_path
    try:
        body = doc_path.read_text(encoding="utf-8")
    except OSError as exc:
        raise LocalDocsError(
            f"Docs file missing for '{full_method}': '{doc_path}' ({exc}). "
            f"Re-download the snapshot (scripts/fetch_zabbix_docs.py)."
        ) from exc

    source = manifest.get("docs_source") or ""
    library = manifest.get("context7_library") or ""
    fetched_at = manifest.get("fetched_at", "")
    lines = [
        f"Zabbix API method: {full_method}",
        f"Docs version: {resolved_version} (local snapshot)",
    ]
    if library:
        lines.append(f"Context7 library: {library}")
    if source:
        lines.append(f"Docs source: {source}")
    if fetched_at:
        lines.append(f"Snapshot fetched: {fetched_at}")
    lines += ["", body.strip()]
    return "\n".join(lines)
