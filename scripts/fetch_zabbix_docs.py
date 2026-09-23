#!/usr/bin/env python3
"""
Fetch a local Zabbix API docs snapshot from Context7.

One-time, dev-time tool: run it WITH internet access. The MCP server itself
never touches the internet — it serves the snapshot produced by this script.

How it works:
  1. Bootstrap: list the Zabbix API methods for the target version from the
     official docs index page (zabbix.com) — method NAMES only, no content.
  2. For each method, fetch its documentation from the Context7 REST API
     (GET https://context7.com/api/v2/context), pinned to a library that
     indexes the Zabbix manual for that version.
  3. Save the markdown under <out>/<version>/api/<object>/<action>.md and a
     manifest.json describing the snapshot.

Only the Python standard library is used. HTTP(S) proxy env vars
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

CONTEXT7_API = "https://context7.com/api/v2/context"
ZABBIX_INDEX = "https://www.zabbix.com/documentation/{version}/en/manual/api/reference/"
DEFAULT_LIBRARY = "/websites/zabbix_current_en"
USER_AGENT = "zabbix-mcp-server-docs-fetcher (stdlib)"

_METHOD_LINK_RE = re.compile(
    r"manual/api/reference/([a-z][a-z0-9_]*)/([a-z][a-z0-9_]*)"
)

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger("fetch_zabbix_docs")


def http_get(url: str, api_key: str | None, timeout: int = 60) -> bytes:
    """GET with proxy env support and retries on 429/5xx."""
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    if api_key:
        req.add_header("Authorization", f"Bearer {api_key}")

    last_err: Exception | None = None
    for attempt in range(6):
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return resp.read()
        except urllib.error.HTTPError as exc:
            if exc.code == 429 or exc.code >= 500:
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
    # Ensure the file starts with a stable heading for the method
    if not body.startswith(f"## {method}") and not body.startswith(f"## {title}"):
        body = f"## {method}\n\n" + body
    return body + "\n"


def fetch_method(
    method: str, library: str, api_key: str | None, out_version: Path, manifest: dict, lock
) -> tuple[str, str | None]:
    """Fetch docs for one method. Returns (method, error|None).

    Resume filtering (which methods to fetch at all) is done by the caller;
    this function only writes files and updates the shared manifest.
    """
    obj, _, action = method.partition(".")
    target = out_version / "api" / obj / f"{action}.md"

    query = f"Zabbix API {method} parameters"
    params = urllib.parse.urlencode({"libraryId": library, "query": query, "type": "json"})
    url = f"{CONTEXT7_API}?{params}"
    try:
        data = json.loads(http_get(url, api_key).decode("utf-8"))
    except Exception as exc:  # noqa: BLE001 - per-method errors must not kill the run
        return method, f"request failed: {exc}"

    snip = pick_snippet(method, data)
    if snip is None or not content_len_safe(snip):
        return method, "no matching snippet in Context7 response"

    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(snippet_markdown(method, snip), encoding="utf-8")
    with lock:
        manifest.setdefault("methods", {})[method] = f"api/{obj}/{action}.md"
        if method in manifest.get("missing", []):
            manifest["missing"].remove(method)
    return method, None


def content_len_safe(snip: dict) -> bool:
    return sum(len(c.get("code", "")) for c in snip.get("codeList") or []) > 50


def write_manifest(out_version: Path, version: str, library: str,
                   methods: list[str], missing: list[str], resumed: bool) -> dict:
    manifest = {
        "zabbix_version": version,
        "context7_library": library,
        "docs_source": "https://www.zabbix.com/documentation/current/en/manual/api",
        "fetched_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "resumed": resumed,
        "method_count": len(methods),
        "missing": sorted(missing),
        "methods": {},
    }
    for method in methods:
        obj, _, action = method.partition(".")
        rel = f"api/{obj}/{action}.md"
        if (out_version / rel).is_file():
            manifest["methods"][method] = rel
    manifest_path = out_version / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return manifest


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
                        help="re-fetch methods that already have a local file")
    args = parser.parse_args()

    version = ".".join(p for p in args.version.split(".") if p.isdigit())[:5]
    if not re.fullmatch(r"\d+\.\d+", version):
        log.error("Invalid --version '%s' (expected e.g. 7.4)", args.version)
        return 2

    repo_root = Path(__file__).resolve().parent.parent
    out_root = Path(args.out) if args.out else repo_root / "docs" / "zabbix"
    out_version = out_root / version
    out_version.mkdir(parents=True, exist_ok=True)

    # 1. bootstrap the authoritative method list, then merge with any
    #    previously fetched methods so a partial snapshot is completed.
    manifest_path = out_version / "manifest.json"

    def load_manifest() -> dict:
        try:
            return json.loads(manifest_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            log.warning("Ignoring unreadable manifest %s: %s", manifest_path, exc)
            return {}

    manifest = load_manifest() if manifest_path.is_file() else {}
    methods = sorted(set(bootstrap_methods(version, args.api_key)) | set(manifest.get("methods", {})))

    if args.limit:
        methods = methods[: args.limit]

    # 2. init manifest fields
    manifest.setdefault("zabbix_version", version)
    manifest.setdefault("context7_library", args.library)
    manifest.setdefault("methods", {})
    manifest["missing"] = list(methods)

    lock = threading.Lock()

    # 3. download
    to_do = list(methods)
    if not args.force:
        to_do = [m for m in to_do if not (out_version / manifest.get("methods", {}).get(m, "")).is_file()]
    log.info("Fetching %d of %d methods (library=%s, workers=%d)",
             len(to_do), len(methods), args.library, args.workers)

    errors: list[tuple[str, str]] = []
    if to_do:
        with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as pool:
            futures = {
                pool.submit(fetch_method, m, args.library, args.api_key, out_version,
                            manifest, lock): m
                for m in to_do
            }
            for i, fut in enumerate(concurrent.futures.as_completed(futures), 1):
                method, err = fut.result()
                status = "ok" if err is None else f"MISS: {err}"
                print(f"  [{i}/{len(to_do)}] {method}: {status}", flush=True)
                if err:
                    errors.append((method, err))

    # 4. final manifest
    write_manifest(out_version, version, args.library, methods,
                   [m for m, _ in errors], resumed=bool(manifest.get("methods") and not args.force))
    print(f"\nSnapshot: {out_version}")
    print(f"  methods: {len(manifest['methods'])} / {len(methods)}")
    if errors:
        print(f"  missing: {len(errors)}")
        for m, err in errors:
            print(f"    - {m}: {err}")
    print(f"  manifest: {out_version / 'manifest.json'}")
    print("\nNote: content is a snapshot of the Zabbix manual as indexed by "
          f"Context7 ({args.library}). Re-run this script to refresh.")
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
