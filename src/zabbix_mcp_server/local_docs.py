"""
Local Zabbix API docs provider.

Serves pre-downloaded Zabbix API method documentation from a local docs
directory (see scripts/fetch_zabbix_docs.py). No network access is used
at runtime: the content is a snapshot of the Zabbix manual as indexed
by Context7, pinned per Zabbix version.

Layout on disk (one file per version, built by scripts/fetch_zabbix_docs.py):
    <docs_dir>/<version>/manifest.json   snapshot metadata + method lists
    <docs_dir>/<version>/docs.md        all method docs, one file,
                                         sections delimited by
                                         <!-- method: object.action -->

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
DOCS_NAME = "docs.md"
VERSION_DIR_RE = re.compile(r"^\d+\.\d+$")

# Section delimiter inside docs.md. Method names are lowercase
# [a-z0-9_.] pairs, so the marker form is unambiguous in markdown content.
SECTION_MARKER_RE = re.compile(r"^<!-- method: (\w+\.\w+) -->[ \t]*\n?", re.MULTILINE)

# Snippet rendering for search results.
_SNIPPET_MAX_LEN = 160
_SNIPPET_CONTEXT = 1  # lines of context around each hit
_MAX_SNIPPETS_PER_METHOD = 3
_SEARCH_LIMIT_CAP = 50


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


def split_docs_text(text: str) -> dict[str, str]:
    """Split a docs.md snapshot into {method: section body}.

    Sections are delimited by '<!-- method: object.action -->' markers.
    Content before the first marker (file header) and duplicate markers
    (later ones win) are dropped.
    """
    sections: dict[str, str] = {}
    parts = SECTION_MARKER_RE.split(text)
    # re.split with one capture group yields: [header, name1, body1, name2, body2, ...]
    # so the name/body slices are always equal-length — strict=True makes that invariant explicit.
    for name, body in zip(parts[1::2], parts[2::2], strict=True):
        sections[name.strip()] = body.strip()
    return sections


class _Snapshot:
    """Parsed docs.md for one version, cached and invalidation-checked."""

    __slots__ = ("mtime", "sections", "size", "text")

    def __init__(self, mtime: float, size: int, text: str, sections: dict[str, str]) -> None:
        self.mtime = mtime
        self.size = size
        self.text = text
        self.sections = sections


_SNAPSHOT_CACHE: dict[str, _Snapshot] = {}


def _load_snapshot(version: str, docs_dir: Path | str | None = None) -> _Snapshot:
    """Load and parse the docs.md snapshot for a version (cached by mtime/size)."""
    path = _resolve_docs_dir(docs_dir) / version / DOCS_NAME
    key = str(path)
    try:
        st = path.stat()
    except OSError as exc:
        raise LocalDocsError(
            f"No docs snapshot for Zabbix version '{version}': '{path}' is missing. "
            f"Download it with: python scripts/fetch_zabbix_docs.py --version {version}"
        ) from exc
    cached = _SNAPSHOT_CACHE.get(key)
    if cached is not None and (cached.mtime, cached.size) == (st.st_mtime, st.st_size):
        return cached
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        raise LocalDocsError(
            f"Failed to read docs snapshot '{path}': {exc}. "
            f"Re-download it with: python scripts/fetch_zabbix_docs.py --version {version}"
        ) from exc
    snapshot = _Snapshot(st.st_mtime, st.st_size, text, split_docs_text(text))
    _SNAPSHOT_CACHE[key] = snapshot
    return snapshot


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
        logger.debug(f"Could not resolve Zabbix server version: {exc}")
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
    """Build {object: [actions]} from a manifest ('methods' is a list of names)."""
    methods: dict[str, list[str]] = {}
    for method in sorted(manifest.get("methods", [])):
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
    snapshot = _load_snapshot(resolved_version, docs_dir)

    body = snapshot.sections.get(full_method)
    if body is None:
        known = _methods_for(manifest)
        available_objects = ", ".join(sorted(known)) or "(none)"
        in_missing = full_method in manifest.get("missing", [])
        missing_note = " It is listed in the snapshot's 'missing' set." if in_missing else ""
        raise ValueError(
            f"Method '{full_method}' is not available in the local docs snapshot "
            f"for Zabbix {resolved_version}.{missing_note} Known objects: {available_objects}. "
            f"Re-download the snapshot to add it (scripts/fetch_zabbix_docs.py)."
        )

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
    lines += ["", body]
    return "\n".join(lines)


def _method_snippets(section: str, hit_lines: list[int]) -> list[str]:
    """Render up to 3 hit lines with context as 'L<n>: text' snippet lines."""
    lines = section.splitlines()
    wanted: list[tuple[int, bool]] = []
    for idx in hit_lines[:_MAX_SNIPPETS_PER_METHOD]:
        for j in range(idx - _SNIPPET_CONTEXT, idx + _SNIPPET_CONTEXT + 1):
            if 0 <= j < len(lines):
                wanted.append((j, j == idx))
    seen: set[int] = set()
    out: list[str] = []
    for j, is_hit in wanted:
        if j in seen:
            continue
        seen.add(j)
        text = lines[j].strip()
        if not text:
            continue
        if len(text) > _SNIPPET_MAX_LEN:
            text = text[: _SNIPPET_MAX_LEN - 1] + "…"
        prefix = ">> " if is_hit else "   "
        out.append(f"{prefix}L{j + 1}: {text}")
    return out


def search_docs(
    query: str,
    version: str | None = None,
    docs_dir: Path | str | None = None,
    limit: int = 10,
) -> str:
    """Search all local method docs; return a report of matching methods.

    Case-insensitive substring search across every method doc in the
    snapshot. Matches are grouped per method and rendered as short
    snippets. If the query matches an API object name exactly (e.g.
    'host'), that object's method list is included as well.

    Args:
        query: Search term, e.g. 'proxy' or 'sla'.
        version: Zabbix version. If None, resolved automatically.
        docs_dir: Override the docs directory (testing).
        limit: Maximum number of matching methods to show (default 10).

    Returns:
        A plain-text report: matching methods with snippets, or an honest
        'no matches' answer with hints.

    Raises:
        ValueError: If the query is empty.
    """
    q = (query or "").strip()
    if not q:
        raise ValueError("Search query must not be empty")
    needle = q.lower()
    shown_limit = max(1, min(limit, _SEARCH_LIMIT_CAP))

    resolved_version = resolve_version(version, docs_dir)
    manifest = _load_manifest(resolved_version, docs_dir)
    snapshot = _load_snapshot(resolved_version, docs_dir)

    # Group matches per method, ranked by hit count (desc), then name.
    results: list[tuple[str, list[int]]] = []
    for method, section in snapshot.sections.items():
        hit_lines = [i for i, line in enumerate(section.splitlines()) if needle in line.lower()]
        if hit_lines:
            results.append((method, hit_lines))
    results.sort(key=lambda r: (-len(r[1]), r[0]))

    out: list[str] = [
        (f'Docs search: "{q}" — Zabbix {resolved_version} '
         f"(local snapshot, {len(snapshot.sections)} methods)")
    ]
    missing_count = len(manifest.get("missing", []))
    if missing_count:
        out.append(f"Note: snapshot is partial — {missing_count} method(s) not downloaded yet.")

    objects = _methods_for(manifest)
    if "." not in needle and needle in objects:
        out.append("")
        out.append(f"Object '{needle}' has {len(objects[needle])} method(s): "
                   + ", ".join(objects[needle]))

    shown = results[:shown_limit]
    if not shown:
        out += [
            "",
            f'No method docs in Zabbix {resolved_version} mention "{q}".',
            ("List available methods with zabbix_api_list() or fetch missing docs "
             "with scripts/fetch_zabbix_docs.py."),
        ]
        return "\n".join(out)

    out.append("")
    out.append(f"{len(results)} method(s) mention \"{q}\":")
    for method, hit_lines in shown:
        out.append("")
        out.append(f"## {method} ({len(hit_lines)} hit(s))")
        out.extend(_method_snippets(snapshot.sections[method], hit_lines))
    out.append("")
    if len(results) > shown_limit:
        out.append(
            f"Showing top {shown_limit} of {len(results)} matched method(s). "
            f"Use zabbix_api_docs('<method>') for full text."
        )
    else:
        out.append('Use zabbix_api_docs("<method>") for full text.')
    return "\n".join(out)
