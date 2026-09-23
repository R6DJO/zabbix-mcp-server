#!/usr/bin/env python3
"""
Fetch a local Zabbix API docs snapshot from Context7.

One-time, dev-time tool: run it WITH internet access. The MCP server itself
never touches the internet — it serves the snapshot produced by this script.

How it works:
  1. Bootstrap: list the Zabbix API methods for the target version from the
     official docs index page (zabbix.com) — method NAMES only, no content.
  2. For each missing method, fetch its documentation from the Context7 REST
     API (GET https://context7.com/api/v2/context), pinned to a library that
     indexes the Zabbix manual for that version.
  3. Assemble everything into ONE file <out>/<version>/docs.md
     (sections delimited by '<!-- method: object.action -->' markers) plus a
     manifest.json describing the snapshot. Re-runs only fetch what is
     missing (resume), then rebuild the file atomically.

Only the Python standard library (plus the repo's own local_docs module for
the shared section format) is used. HTTP(S) proxy env vars
(http_proxy/https_proxy) are honored.

Usage:
    python scripts/fetch_zabbix_docs.py --version 7.4
    python scripts/fetch_zabbix_docs.py --version 7.4 --limit 5    # smoke test
    CONTEXT7_API_KEY=ctx7sk-... python scripts/fetch_zabbix_docs.py

The Context7 API can be used without a key (IP rate-limited, testing only).
An API key (free plan: 1000 calls/month) raises the limits:
    https://context7.com (Plans & Pricing)
"""

import argparse
import concurrent.futures
import json
import logging
import os
import random
import re
import sys
import threading
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

# Use the installed package when available (venv); fall back to the repo's
# src/ so the script also works from a bare checkout without installation.
_REPO_ROOT = Path(__file__).resolve().parent.parent
try:
    from zabbix_mcp_server.local_docs import DOCS_NAME, split_docs_text
except ImportError:
    sys.path.insert(0, str(_REPO_ROOT / "src"))
    from zabbix_mcp_server.local_docs import DOCS_NAME, split_docs_text

CONTEXT7_API = "https://context7.com/api/v2/context"
ZABBIX_INDEX = "https://www.zabbix.com/documentation/{version}/en/manual/api/reference/"
DOCS_SOURCE = "https://www.zabbix.com/documentation/current/en/manual/api"
DEFAULT_LIBRARY = "/websites/zabbix_current_en"
USER_AGENT = "zabbix-mcp-server-docs-fetcher (stdlib)"

_METHOD_LINK_RE = re.compile(
    r"manual/api/reference/([a-z][a-z0-9_]*)/([a-z][a-z0-9_]*)"
)

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger("fetch_zabbix_docs")


def _is_retryable(exc: urllib.error.HTTPError) -> bool:
    """HTTP errors worth a backoff retry: 429 (rate limit) and 5xx."""
    return exc.code == 429 or exc.code >= 500


# Only these URL schemes are permitted for the doc fetcher (defense-in-depth:
# both build sites use hardcoded https constants, but reject any other scheme
# explicitly so the URL-open surface stays http/https-only).
_ALLOWED_URL_SCHEMES = frozenset({"http", "https"})


def _validate_url_scheme(url: str) -> None:
    """Reject URLs whose scheme is not http/https (no file:, no custom schemes)."""
    parsed = urllib.parse.urlparse(url)
    if parsed.scheme not in _ALLOWED_URL_SCHEMES:
        raise ValueError(
            f"Unsupported URL scheme {parsed.scheme!r} for {url!r}; "
            f"only http/https are allowed"
        )


def http_get(url: str, api_key: str | None, timeout: int = 60) -> bytes:
    """GET with proxy env support and retries on 429/5xx."""
    _validate_url_scheme(url)
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    if api_key:
        req.add_header("Authorization", f"Bearer {api_key}")

    last_err: Exception | None = None
    for attempt in range(6):
        try:
            # Scheme guard at the open site: req.full_url comes from the two
            # hardcoded https constants in this script; reject any drift.
            opened = urllib.parse.urlsplit(req.full_url)
            if opened.scheme not in _ALLOWED_URL_SCHEMES:
                raise ValueError(f"Refusing to open non-http(s) URL: {req.full_url!r}")
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return resp.read()
        except urllib.error.HTTPError as exc:
            if _is_retryable(exc):
                last_err = exc
                wait = min(60, 2 ** attempt + random.random())
                log.warning("HTTP %s, retrying in %.1fs (%d/6): %s", exc.code, wait, attempt + 1, url)
                time.sleep(wait)
                continue
            raise
        except (urllib.error.URLError, TimeoutError, OSError) as exc:
            last_err = exc
            if attempt < 5:
                time.sleep(2 * (attempt + 1))
                continue
            raise
    raise RuntimeError(f"Failed to fetch {url}: {last_err}")


def bootstrap_methods(version: str, api_key: str | None) -> list[str]:
    """List API methods for a Zabbix version from the official index page."""
    url = ZABBIX_INDEX.format(version=version)
    log.info("Bootstrapping method list from %s", url)
    page = http_get(url, api_key).decode("utf-8", errors="replace")
    methods: list[str] = []
    for obj, action in _METHOD_LINK_RE.findall(page):
        if action == "object":
            continue
        method = f"{obj}.{action}"
        if method not in methods:
            methods.append(method)
    if not methods:
        raise RuntimeError(
            f"Bootstrap failed: no methods found at {url} "
            f"(check the version, or that zabbix.com is reachable)"
        )
    log.info("Found %d methods", len(methods))
    return methods


def pick_snippet(method: str, data: dict) -> dict | None:
    """Pick the best snippet for a method from a Context7 response.

    Preference:
      1. snippet whose source URL is the dedicated method page
         (…/manual/api/reference/<obj>/<action>)
      2. snippet titled with the method name (sections of the object page)
    Among ties, the largest content wins.
    """
    obj, _, action = method.partition(".")
    method_page = f"/manual/api/reference/{obj}/{action}"
    object_page = f"/manual/api/reference/{obj}"
    snippets = data.get("codeSnippets") or []

    def content_len(snip: dict) -> int:
        return sum(len(c.get("code", "")) for c in snip.get("codeList") or [])

    best: dict | None = None
    for rank_match in (lambda s: s.get("codeId", "").endswith(method_page),
                       lambda s: s.get("codeTitle") == method):
        candidates = [s for s in snippets if rank_match(s)]
        if candidates:
            best = max(candidates, key=content_len)
            break
        # fall through to next preference level
    if best is None:
        # last resort: object-page section mentioning the method title
        candidates = [s for s in snippets if s.get("codeId", "").endswith(object_page)
                      and method in (s.get("codeTitle") or "")]
        if candidates:
            best = max(candidates, key=content_len)
    return best


def snippet_markdown(method: str, snip: dict) -> str:
    parts = [c.get("code", "") for c in snip.get("codeList") or []]
    body = "\n\n".join(p.strip() for p in parts if p.strip())
    title = snip.get("codeTitle") or method
    # Ensure the section starts with a stable heading for the method
    if not body.startswith(f"## {method}") and not body.startswith(f"## {title}"):
        body = f"## {method}\n\n" + body
    return body + "\n"


def fetch_method(
    method: str, library: str, api_key: str | None
) -> tuple[str, str | None, str | None]:
    """Fetch docs for one method. Returns (method, markdown|None, error|None)."""
    obj, _, action = method.partition(".")
    del obj, action  # method string is the only identifier the caller needs

    query = f"Zabbix API {method} parameters"
    params = urllib.parse.urlencode({"libraryId": library, "query": query, "type": "json"})
    url = f"{CONTEXT7_API}?{params}"
    try:
        data = json.loads(http_get(url, api_key).decode("utf-8"))
    except Exception as exc:  # noqa: BLE001 - per-method errors must not kill the run
        return method, None, f"request failed: {exc}"

    snip = pick_snippet(method, data)
    if snip is None or not snippet_has_content(snip):
        return method, None, "no matching snippet in Context7 response"
    return method, snippet_markdown(method, snip), None


def snippet_has_content(snip: dict) -> bool:
    return sum(len(c.get("code", "")) for c in snip.get("codeList") or []) > 50


def load_existing_manifest(out_version: Path) -> dict:
    manifest_path = out_version / "manifest.json"
    if not manifest_path.is_file():
        return {}
    try:
        return json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        log.warning("Ignoring unreadable manifest %s: %s", manifest_path, exc)
        return {}


def existing_methods(manifest: dict) -> list[str]:
    """Method names from an old manifest (list) or legacy one (dict keys)."""
    methods = manifest.get("methods", [])
    if isinstance(methods, dict):
        return sorted(methods)
    return list(methods)


def load_existing_sections(out_version: Path) -> dict[str, str]:
    """Parse an existing docs.md into {method: section} (resume base)."""
    docs_path = out_version / DOCS_NAME
    if not docs_path.is_file():
        return {}
    try:
        return split_docs_text(docs_path.read_text(encoding="utf-8"))
    except OSError as exc:
        log.warning("Ignoring unreadable %s: %s", docs_path, exc)
        return {}


def write_snapshot(
    out_version: Path,
    version: str,
    library: str,
    sections: dict[str, str],
    all_methods: list[str],
) -> tuple[Path, Path]:
    """Write docs.md (atomic) + manifest.json for the assembled snapshot."""
    fetched_at = datetime.now(timezone.utc).isoformat(timespec="seconds")
    methods = sorted(sections)
    missing = sorted(set(all_methods) - set(methods))

    header = (
        f"<!-- Zabbix {version} API docs snapshot\n"
        f"     Context7 library: {library}\n"
        f"     Docs source: {DOCS_SOURCE}\n"
        f"     Fetched: {fetched_at}\n"
        f"-->\n"
    )
    chunks = [header]
    for method in methods:
        chunks.append(f"<!-- method: {method} -->\n{sections[method]}\n")
    docs_path = out_version / DOCS_NAME
    tmp_path = out_version / (DOCS_NAME + ".tmp")
    tmp_path.write_text("".join(chunks), encoding="utf-8")
    os.replace(tmp_path, docs_path)  # atomic on POSIX

    manifest = {
        "zabbix_version": version,
        "context7_library": library,
        "docs_source": DOCS_SOURCE,
        "fetched_at": fetched_at,
        "method_count": len(all_methods),
        "methods": methods,
        "missing": missing,
    }
    manifest_path = out_version / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n",
                             encoding="utf-8")
    return docs_path, manifest_path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                    formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--version", default="7.4",
                        help="Zabbix version to download docs for (default: 7.4)")
    parser.add_argument("--library", default=DEFAULT_LIBRARY,
                        help=f"Context7 library ID (default: {DEFAULT_LIBRARY})")
    parser.add_argument("--out", default=None,
                        help="output root dir (default: <repo>/docs/zabbix)")
    parser.add_argument("--api-key", default=os.environ.get("CONTEXT7_API_KEY"),
                        help="Context7 API key (default: $CONTEXT7_API_KEY, optional)")
    parser.add_argument("--workers", type=int, default=4, help="parallel downloads (default: 4)")
    parser.add_argument("--limit", type=int, default=None,
                        help="only fetch the first N methods (smoke testing)")
    parser.add_argument("--force", action="store_true",
                        help="re-fetch methods that already have local docs")
    args = parser.parse_args()

    version = ".".join(p for p in args.version.split(".") if p.isdigit())[:5]
    if not re.fullmatch(r"\d+\.\d+", version):
        log.error("Invalid --version '%s' (expected e.g. 7.4)", args.version)
        return 2

    out_version = _REPO_ROOT / "docs" / "zabbix" / version if args.out is None \
        else Path(args.out) / version
    out_version.mkdir(parents=True, exist_ok=True)

    # 1. Authoritative method list = bootstrap ∪ previously fetched, so a
    #    partial snapshot is completed on re-run.
    manifest = load_existing_manifest(out_version)
    methods = sorted(set(bootstrap_methods(version, args.api_key))
                     | set(existing_methods(manifest)))
    if args.limit:
        methods = methods[: args.limit]

    # 2. Resume base: sections already present in docs.md.
    existing = {} if args.force else load_existing_sections(out_version)

    # 3. Download only what is missing.
    to_do = [m for m in methods if m not in existing]
    log.info("Fetching %d of %d methods (have %d local, library=%s, workers=%d)",
             len(to_do), len(methods), len(existing), args.library, args.workers)

    new_bodies: dict[str, str] = {}
    errors: list[tuple[str, str]] = []
    if to_do:
        lock = threading.Lock()
        with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as pool:
            futures = {
                pool.submit(fetch_method, m, args.library, args.api_key): m
                for m in to_do
            }
            for i, fut in enumerate(concurrent.futures.as_completed(futures), 1):
                method, body, err = fut.result()
                if err is None:
                    # fetch_method returns body=None only when err is set,
                    # so here body is a str (narrowed for the type checker).
                    assert body is not None
                    with lock:
                        new_bodies[method] = body
                status = "ok" if err is None else f"MISS: {err}"
                print(f"  [{i}/{len(to_do)}] {method}: {status}", flush=True)
                if err:
                    errors.append((method, err))

    # 4. Assemble: existing sections + new downloads, written atomically.
    sections = dict(existing)
    sections.update(new_bodies)
    docs_path, manifest_path = write_snapshot(out_version, version, args.library,
                                              sections, methods)

    print(f"\nSnapshot: {out_version}")
    print(f"  docs.md: {docs_path} ({len(sections)} methods)")
    missing_now = sorted(set(methods) - set(sections))
    if missing_now:
        print(f"  missing: {len(missing_now)}")
        for m, err in errors:
            print(f"    - {m}: {err}")
    print(f"  manifest: {manifest_path}")
    print("\nNote: content is a snapshot of the Zabbix manual as indexed by "
          f"Context7 ({args.library}). Re-run this script to refresh.")
    return 0 if not missing_now else 1


if __name__ == "__main__":
    sys.exit(main())
