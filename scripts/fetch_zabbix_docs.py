#!/usr/bin/env python3
"""
Fetch a local Zabbix API docs snapshot for the MCP server.

One-time, dev-time tool: run it WITH internet access. The MCP server itself
never touches the internet — it serves the snapshot produced by this script.

Two doc sources:

  --source zabbix      (default) Scrape the official zabbix.com API reference
      HTML pages directly. No Context7 quota involved. Coverage is the full
      official method list for the version; parameter tables are carried over
      verbatim.

  --source context7     Fetch per-method docs from the Context7 REST API
      (GET https://context7.com/api/v2/context), pinned to a library that
      indexes the Zabbix manual. Costs API calls (free plan: 1000/month,
      https://context7.com/plans).

How it works (both sources):
  1. Bootstrap: list the Zabbix API methods for the target version from the
     official docs index page (zabbix.com) — method NAMES only, no content.
  2. For each missing method, fetch its documentation from the chosen source.
  3. Assemble everything into ONE file <out>/<version>/docs.md
     (sections delimited by '<!-- method: object.action -->' markers) plus a
     manifest.json describing the snapshot. Re-runs only fetch what is
     missing (resume), then rebuild the file atomically.

If an existing snapshot on disk was built from a different source, its
sections are ignored and the snapshot is rebuilt from scratch (content
styles must not be mixed inside one docs.md).

Dependencies:
  - zabbix source: beautifulsoup4 (dev dependency: `uv sync` installs it).
  - context7 source: Python standard library only.
  HTTP(S) proxy env vars (http_proxy/https_proxy) are honored.

Usage:
    uv run python scripts/fetch_zabbix_docs.py --version 7.4
    uv run python scripts/fetch_zabbix_docs.py --version 7.4 --limit 5   # smoke test
    uv run python scripts/fetch_zabbix_docs.py --version 7.4 --source context7 --library /websites/zabbix_current_en
    CONTEXT7_API_KEY=ctx7sk-... uv run python scripts/fetch_zabbix_docs.py --source context7

The Context7 API can be used without a key (IP rate-limited, testing only).
An API key (free plan: 1000 calls/month) raises the limits:
    https://context7.com/plans
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

try:
    from bs4 import BeautifulSoup, Tag
except ImportError:  # bare checkout without dev dependencies
    BeautifulSoup = None
    Tag = None

CONTEXT7_API = "https://context7.com/api/v2/context"
ZABBIX_INDEX = "https://www.zabbix.com/documentation/{version}/en/manual/api/reference/"
DOCS_SOURCE_CONTEXT7 = "https://www.zabbix.com/documentation/current/en/manual/api"
DEFAULT_CONTEXT7_LIBRARY = "/websites/zabbix_current_en"
USER_AGENT = "zabbix-mcp-server-docs-fetcher (stdlib)"

_METHOD_LINK_RE = re.compile(
    r"manual/api/reference/([a-z][a-z0-9_]*)/([a-z][a-z0-9_]*)"
)

SOURCE_ZABBIX = "zabbix"
SOURCE_CONTEXT7 = "context7"

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger("fetch_zabbix_docs")


def _is_retryable(exc: urllib.error.HTTPError) -> bool:
    """HTTP errors worth a backoff retry: 429 (rate limit) and 5xx."""
    return exc.code == 429 or exc.code >= 500


# Only these URL schemes are permitted for the doc fetcher (defense-in-depth:
# both build sites use hardcoded https constants, but reject any other scheme
# explicitly so the URL-open surface stays http/https-only).
_ALLOWED_URL_SCHEMES = frozenset({"http", "https"})

# Host allowlist for every URL this script opens: URLs are built from the
# hardcoded ZABBIX_INDEX / CONTEXT7_API constants, and each open site re-checks
# scheme + host so no drift (env-manipulated URL, future code change) can
# steer the opener at an unlisted target.
_ALLOWED_TARGETS: frozenset[tuple[str, int]] = frozenset({
    ("www.zabbix.com", 443),
    ("context7.com", 443),
})


def _check_url_allowed(url: str) -> None:
    """Scheme + host allowlist guard to run at every URL open site."""
    parts = urllib.parse.urlsplit(url)
    if parts.scheme not in _ALLOWED_URL_SCHEMES:
        raise ValueError(
            f"Unsupported URL scheme {parts.scheme!r} for {url!r}; "
            f"only http/https are allowed"
        )
    host = parts.hostname or ""
    port = parts.port or (443 if parts.scheme == "https" else 80)
    if (host, port) not in _ALLOWED_TARGETS:
        raise ValueError(
            f"Refusing to open {host!r}:{port} for {url!r}; allowed targets: "
            f"{sorted(h for h, _ in _ALLOWED_TARGETS)}"
        )


def http_get(url: str, api_key: str | None = None, timeout: int = 60) -> bytes:
    """GET with proxy env support and retries on 429/5xx.

    Both URL open sites are guarded by the scheme + host allowlist check
    (_check_url_allowed) so no file:/custom-scheme or off-allowlist target
    can reach the opener.
    """
    _check_url_allowed(url)
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    if api_key:
        req.add_header("Authorization", f"Bearer {api_key}")

    last_err: Exception | None = None
    for attempt in range(6):
        try:
            # Scheme + host guard at the open site: req.full_url comes from
            # the two hardcoded https constants in this script; reject drift.
            _check_url_allowed(req.full_url)
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


def bootstrap_methods(version: str, api_key: str | None = None) -> list[str]:
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


# ---------------------------------------------------------------------------
# zabbix.com source
# ---------------------------------------------------------------------------


def _method_url(method: str, version: str) -> str:
    obj, _, action = method.partition(".")
    return ZABBIX_INDEX.format(version=version) + f"{obj}/{action}"


def _find_heading(soup, *names: str):
    """First h2/h3 whose text contains any of the given (lowercase) names."""
    for h in soup.find_all(["h2", "h3"]):
        text = h.get_text(strip=True).lower()
        if any(n in text for n in names):
            return h
    return None


def _section_elements(heading) -> list:
    """Siblings after the heading, up to the next h2/h3."""
    out = []
    for sib in heading.find_next_siblings():
        if Tag is not None and isinstance(sib, Tag) and sib.name in ("h2", "h3"):
            break
        out.append(sib)
    return out


def _section_text(elements: list) -> str:
    """Join p/li text of a section's elements as paragraphs/lines."""
    parts: list[str] = []
    for el in elements:
        if el.name == "p":
            text = el.get_text(" ", strip=True)
            if text:
                parts.append(text)
        elif el.name in ("ul", "ol"):
            for li in el.find_all("li", recursive=False):
                text = li.get_text(" ", strip=True)
                if text:
                    parts.append(f"- {text}")
    return "\n".join(parts)


def _fallback_description(soup) -> str:
    """Description extraction when the page has no Description heading."""
    h1 = soup.find("h1")
    if h1:
        for sibling in h1.find_next_siblings():
            if sibling.name == "p":
                text = sibling.get_text(separator=" ", strip=True)
                if text:
                    return text
    for p in soup.find_all("p"):
        text = p.get_text(separator=" ", strip=True)
        if len(text) > 40:
            return text
    return ""


def _parse_parameters_table(table) -> list[dict]:
    """Parse one Zabbix parameter/property table into a list of parameter dicts.

    Column locations come from the header row; if a Mandatory/Required column
    exists it is used, otherwise the '(mandatory)'/'(required)' markers in the
    description text are honored. Zabbix 7.x tables carry neither and the
    docs simply do not mark mandatory-ness there — in that case 'required'
    is left unset and the renderer must not invent a split.
    """
    rows = table.find_all("tr")
    if len(rows) < 2:
        return []
    headers = [th.get_text(strip=True).lower() for th in rows[0].find_all(["th", "td"])]
    col = {
        "name": next(
            (i for i, h in enumerate(headers) if "parameter" in h or "name" in h), 0
        ),
        "type": next((i for i, h in enumerate(headers) if "type" in h), 1),
        "required": next(
            (i for i, h in enumerate(headers) if "mandatory" in h or "required" in h),
            None,
        ),
        "desc": next((i for i, h in enumerate(headers) if "description" in h), -1),
    }

    def cell_text(row_cells, idx) -> str:
        if idx is None or idx >= len(row_cells):
            return ""
        return row_cells[idx].get_text(" ", strip=True)

    params: list[dict] = []
    for row in rows[1:]:
        cells = row.find_all(["td", "th"])
        if len(cells) < 2:
            continue
        name = cell_text(cells, col["name"])
        if not name:
            continue
        desc = cell_text(cells, col["desc"])
        p: dict[str, str | bool] = {
            "name": name,
            "type": cell_text(cells, col["type"]) or "unknown",
            "desc": desc,
        }
        if col["required"] is not None:
            p["required"] = cell_text(cells, col["required"]).lower() in (
                "yes", "true", "1", "mandatory",
            )
        else:
            desc_l = desc.lower()
            if "(mandatory)" in desc_l or "(required)" in desc_l:
                p["required"] = True
        params.append(p)
    return params


def _parse_method_page(html: str) -> dict:
    """Parse a zabbix.com API method page into a structured dict."""
    if BeautifulSoup is None:
        raise RuntimeError(
            "beautifulsoup4 is required for the zabbix source — "
            "install dev dependencies (`uv sync`)"
        )
    soup = BeautifulSoup(html, "html.parser")

    desc_heading = _find_heading(soup, "description")
    if desc_heading is not None:
        description = _section_text(_section_elements(desc_heading))
    else:
        description = _fallback_description(soup)

    prose: list[str] = []
    params: list[dict] = []
    param_heading = _find_heading(soup, "parameters")
    if param_heading is not None:
        for el in _section_elements(param_heading):
            if el.name == "p":
                text = el.get_text(" ", strip=True)
                if text:
                    prose.append(text)
            elif el.name in ("ul", "ol"):
                for li in el.find_all("li", recursive=False):
                    text = li.get_text(" ", strip=True)
                    if text:
                        prose.append(f"- {text}")
            for table in ([el] if el.name == "table" else []) + el.find_all("table"):
                header_row = table.find("tr")
                if not header_row:
                    continue
                header_text = header_row.get_text(strip=True).lower()
                if "parameter" not in header_text and "name" not in header_text:
                    continue
                params.extend(_parse_parameters_table(table))

    ret_heading = _find_heading(soup, "return")
    returns = _section_text(_section_elements(ret_heading)) if ret_heading else ""

    return {
        "description": description,
        "prose": prose,
        "params": params,
        "returns": returns,
    }


def _param_line(p: dict) -> str:
    desc = p["desc"].replace("\n", " ").strip()
    line = f"- **{p['name']}** ({p['type']})"
    if desc:
        line += f": {desc}"
    return line


def zabbix_method_markdown(method: str, url: str, parsed: dict) -> str:
    """Render a parsed zabbix.com method page as the docs.md section body."""
    lines = [f"## {method}", "", "### Description"]
    lines += [parsed["description"].strip() or "Not available.", ""]

    has_required = any("required" in p for p in parsed["params"])
    if parsed["prose"] or parsed["params"]:
        lines.append("### Parameters")
        if parsed["prose"]:
            lines += parsed["prose"]
            lines.append("")
        if parsed["params"]:
            if has_required:
                required = [p for p in parsed["params"] if p["required"]]
                optional = [p for p in parsed["params"] if not p.get("required")]
                if required:
                    lines += ["**Required:**"] + [_param_line(p) for p in required]
                if optional:
                    lines += [""] + ["**Optional:**"] + [_param_line(p) for p in optional]
            else:
                # 7.x-style docs: no mandatory markers on the page; render the
                # full parameter list verbatim without inventing a split.
                lines += [_param_line(p) for p in parsed["params"]]
            lines.append("")

    if parsed["returns"].strip():
        lines += ["### Return value", parsed["returns"].strip(), ""]

    lines += [f"Source: {url}"]
    return "\n".join(lines) + "\n"


def fetch_method_zabbix(method: str, version: str) -> tuple[str, str | None, str | None]:
    """Fetch docs for one method from zabbix.com.

    Returns (method, markdown|None, error|None).
    """
    if BeautifulSoup is None:
        return method, None, (
            "zabbix source needs beautifulsoup4 — install dev dependencies "
            "(`uv sync`) and re-run"
        )
    url = _method_url(method, version)
    try:
        html = http_get(url).decode("utf-8", errors="replace")
    except urllib.error.HTTPError as exc:
        return method, None, f"HTTP {exc.code} for {url}"
    except Exception as exc:  # noqa: BLE001 - per-method errors must not kill the run
        return method, None, f"request failed: {exc}"
    parsed = _parse_method_page(html)
    if not parsed["description"].strip() and not parsed["params"] and not parsed["prose"]:
        return method, None, "page parsed but no content found (check the URL)"
    return method, zabbix_method_markdown(method, url, parsed), None


# ---------------------------------------------------------------------------
# context7 source
# ---------------------------------------------------------------------------


def pick_snippet(method: str, data: dict) -> dict | None:
    """Pick the best snippet for a method from a Context7 response.

    Preference:
      1. snippet whose source URL is the dedicated method page
         (…/manual/api/reference/<obj>/<action>)
      2. snippet titled with the method name (sections of the object page)
    Among ties, the largest content wins.
    """
    obj, _, _ = method.partition(".")
    method_page = f"/manual/api/reference/{obj}/" + method.partition(".")[2]
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


def snippet_has_content(snip: dict) -> bool:
    return sum(len(c.get("code", "")) for c in snip.get("codeList") or []) > 50


def fetch_method_context7(
    method: str, library: str, api_key: str | None
) -> tuple[str, str | None, str | None]:
    """Fetch docs for one method from the Context7 API.

    Returns (method, markdown|None, error|None).
    """
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


# ---------------------------------------------------------------------------
# snapshot assembly (shared)
# ---------------------------------------------------------------------------


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


def docs_source_for(source: str, version: str, library: str) -> str:
    if source == SOURCE_CONTEXT7:
        return DOCS_SOURCE_CONTEXT7
    return f"https://www.zabbix.com/documentation/{version}/en/manual/api"


def write_snapshot(
    out_version: Path,
    version: str,
    source: str,
    library: str,
    sections: dict[str, str],
    all_methods: list[str],
) -> tuple[Path, Path]:
    """Write docs.md (atomic) + manifest.json for the assembled snapshot."""
    fetched_at = datetime.now(timezone.utc).isoformat(timespec="seconds")
    methods = sorted(sections)
    missing = sorted(set(all_methods) - set(methods))

    if source == SOURCE_CONTEXT7:
        header = (
            f"<!-- Zabbix {version} API docs snapshot\n"
            f"     Source: Context7 ({library})\n"
            f"     Docs source: {DOCS_SOURCE_CONTEXT7}\n"
            f"     Fetched: {fetched_at}\n"
            "-->\n"
        )
    else:
        header = (
            f"<!-- Zabbix {version} API docs snapshot\n"
            f"     Source: zabbix.com official documentation\n"
            f"     Docs source: {docs_source_for(source, version, library)}\n"
            f"     Fetched: {fetched_at}\n"
            "-->\n"
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
        "source": source,
        "docs_source": docs_source_for(source, version, library),
        "fetched_at": fetched_at,
        "method_count": len(all_methods),
        "methods": methods,
        "missing": missing,
    }
    if source == SOURCE_CONTEXT7:
        # Keep the legacy key so old readers stay compatible.
        manifest["context7_library"] = library
    manifest_path = out_version / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n",
                             encoding="utf-8")
    return docs_path, manifest_path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                    formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--version", default="7.4",
                        help="Zabbix version to download docs for (default: 7.4)")
    parser.add_argument("--source", choices=[SOURCE_ZABBIX, SOURCE_CONTEXT7],
                        default=SOURCE_ZABBIX,
                        help="doc source (default: zabbix — official zabbix.com pages)")
    parser.add_argument("--library", default=DEFAULT_CONTEXT7_LIBRARY,
                        help=f"Context7 library ID, context7 source only "
                             f"(default: {DEFAULT_CONTEXT7_LIBRARY})")
    parser.add_argument("--out", default=None,
                        help="output root dir (default: <repo>/docs/zabbix)")
    parser.add_argument("--api-key", default=os.environ.get("CONTEXT7_API_KEY"),
                        help="Context7 API key, context7 source only "
                             "(default: $CONTEXT7_API_KEY, optional)")
    parser.add_argument("--workers", type=int, default=4, help="parallel downloads (default: 4)")
    parser.add_argument("--limit", type=int, default=None,
                        help="only fetch the first N methods (smoke testing)")
    parser.add_argument("--force", action="store_true",
                        help="re-fetch methods that already have local docs")
    args = parser.parse_args()

    if args.source == SOURCE_ZABBIX and args.api_key:
        log.warning("--api-key is only used by the context7 source; ignoring it")

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

    # 2. Resume base: sections already present in docs.md — but only when the
    #    snapshot was built from the SAME source (content styles must not mix).
    #    An empty manifest means no snapshot existed: nothing to warn about.
    prev_source = manifest.get("source", SOURCE_CONTEXT7)
    existing = {}
    if not args.force and manifest and prev_source == args.source:
        existing = load_existing_sections(out_version)
    elif not args.force and manifest:
        log.warning("Existing snapshot was built from source '%s'; requested '%s' "
                    "— rebuilding from scratch (existing sections ignored).",
                    prev_source, args.source)

    # 3. Download only what is missing.
    to_do = [m for m in methods if m not in existing]
    log.info("Fetching %d of %d methods (have %d local, source=%s, workers=%d)",
             len(to_do), len(methods), len(existing), args.source, args.workers)

    new_bodies: dict[str, str] = {}
    errors: list[tuple[str, str]] = []
    if to_do:
        lock = threading.Lock()
        with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as pool:
            if args.source == SOURCE_CONTEXT7:
                def worker(m):
                    return fetch_method_context7(m, args.library, args.api_key)
            else:
                def worker(m):
                    return fetch_method_zabbix(m, version)

            futures = {pool.submit(worker, m): m for m in to_do}
            for i, fut in enumerate(concurrent.futures.as_completed(futures), 1):
                method, body, err = fut.result()
                if err is None:
                    # fetch_* returns body=None only when err is set,
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
    docs_path, manifest_path = write_snapshot(out_version, version, args.source,
                                               args.library, sections, methods)

    print(f"\nSnapshot: {out_version}")
    print(f"  docs.md: {docs_path} ({len(sections)} methods)")
    missing_now = sorted(set(methods) - set(sections))
    if missing_now:
        print(f"  missing: {len(missing_now)}")
        for m, err in errors:
            print(f"    - {m}: {err}")
    print(f"  manifest: {manifest_path}")
    note_lib = f" ({args.library})" if args.source == SOURCE_CONTEXT7 else ""
    print(f"\nNote: content is a snapshot of the Zabbix manual from "
          f"{args.source}{note_lib}. Re-run this script to refresh.")
    return 0 if not missing_now else 1


if __name__ == "__main__":
    sys.exit(main())
