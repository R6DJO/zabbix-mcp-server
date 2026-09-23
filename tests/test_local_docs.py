"""Unit tests for the offline docs provider (zabbix_mcp_server.local_docs).

Run with the stdlib test runner (no external test dependencies):

    python -m unittest tests.test_local_docs -v
"""

import json
import sys
import tempfile
import unittest
from pathlib import Path

# Make the package importable when run from a repo checkout without installation.
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from zabbix_mcp_server import local_docs as ld


def _make_snapshot(docs_dir, version: str, sections: dict[str, str],
                   missing: list[str] | None = None) -> Path:
    """Build a version snapshot (docs.md + manifest.json) and return its base.

    ``sections`` maps method name -> section body, mirroring what
    scripts/fetch_zabbix_docs.py writes.
    """
    base = Path(docs_dir)
    vdir = base / version
    vdir.mkdir(parents=True, exist_ok=True)

    header = "<!-- test snapshot -->\n"
    chunks = [header]
    for name in sorted(sections):
        chunks.append(f"<!-- method: {name} -->\n{sections[name].strip()}\n")
    (vdir / "docs.md").write_text("".join(chunks), encoding="utf-8")

    manifest = {
        "zabbix_version": version,
        "context7_library": "/websites/zabbix_current_en",
        "docs_source": "https://www.zabbix.com/documentation/current/en/manual/api",
        "fetched_at": "2026-01-01T00:00:00+00:00",
        "method_count": len(sections),
        "methods": sorted(sections),
        "missing": sorted(missing or []),
    }
    (vdir / "manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True),
                                        encoding="utf-8")
    return base


# Shared fixture content for the search tests.
_SNAP_SHOTS = {
    "host.get": "## host.get\nRetrieves hosts. Use proxy items to poll data.\n",
    "host.create": "## host.create\nCreates a new host.\n",
    "proxy.get": "## proxy.get\nRetrieves Zabbix proxy servers.\n",
    "item.get": "## item.get\nRetrieves items. Can search by proxy association.\n",
}


class NormalizeVersionTests(unittest.TestCase):
    def test_minor_version_passthrough(self):
        self.assertEqual(ld.normalize_version("7.4"), "7.4")

    def test_patch_version_collapsed(self):
        self.assertEqual(ld.normalize_version("7.4.14"), "7.4")
        self.assertEqual(ld.normalize_version("6.4.0"), "6.4")

    def test_whitespace_tolerated(self):
        self.assertEqual(ld.normalize_version("  7.4 "), "7.4")

    def test_garbage_rejected(self):
        for bad in ("", ".", "7", "abc", "7x4"):
            with self.assertRaises(ld.LocalDocsError, msg=bad):
                ld.normalize_version(bad)


class SplitDocsTextTests(unittest.TestCase):
    def test_round_trip(self):
        text = "header\n<!-- method: a.b -->\nbody ab\n\n<!-- method: a.c -->\nbody ac\n"
        sections = ld.split_docs_text(text)
        self.assertEqual(sections, {"a.b": "body ab", "a.c": "body ac"})

    def test_no_markers_yields_empty(self):
        self.assertEqual(ld.split_docs_text("plain text, no markers"), {})

    def test_duplicate_marker_last_wins(self):
        text = ("<!-- method: a.b -->\nfirst\n<!-- method: a.b -->\nsecond\n")
        self.assertEqual(ld.split_docs_text(text), {"a.b": "second"})


class AvailableVersionsTests(unittest.TestCase):
    def test_missing_dir_yields_empty(self):
        tmp = tempfile.TemporaryDirectory()
        self.assertEqual(ld.available_versions(tmp.name + "/nope"), [])
        tmp.cleanup()

    def test_only_version_dirs_with_manifests_count(self):
        tmp = tempfile.TemporaryDirectory()
        base = _make_snapshot(tmp.name + "/zabbix", "7.4", {"host.get": "## host.get\n"})
        for decoy in ("notes", "7.4.14", "bad"):
            (base / decoy).mkdir()
        self.assertEqual(ld.available_versions(base), ["7.4"])
        tmp.cleanup()

    def test_sorted_numerically_not_lexicographically(self):
        tmp = tempfile.TemporaryDirectory()
        for ver in ("6.4", "7.4", "7.10"):
            _make_snapshot(tmp.name + "/zabbix", ver, {"a.b": "## a.b\n"})
        self.assertEqual(ld.available_versions(Path(tmp.name + "/zabbix")),
                         ["6.4", "7.4", "7.10"])
        tmp.cleanup()


class ListMethodsTests(unittest.TestCase):
    def setUp(self):
        self._td = tempfile.TemporaryDirectory()
        self.base = _make_snapshot(
            self._td.name + "/zabbix",
            "7.4",
            {
                "host.get": "## host.get\n",
                "host.create": "## host.create\n",
                "item.get": "## item.get\n",
            },
        )

    def tearDown(self):
        self._td.cleanup()

    def test_grouped_by_object(self):
        result = ld.list_methods("7.4", self.base)
        self.assertEqual(result["host"], ["create", "get"])
        self.assertEqual(result["item"], ["get"])

    def test_unknown_version_raises(self):
        with self.assertRaises(ld.LocalDocsError):
            ld.list_methods("6.0", self.base)


class GetMethodDocsTests(unittest.TestCase):
    def setUp(self):
        # Per-test snapshot so destructive tests cannot leak into others.
        self._td = tempfile.TemporaryDirectory()
        self.base = _make_snapshot(
            self._td.name + "/zabbix", "7.4",
            {"host.get": "## host.get\n\nDescription of host.get.\n"},
        )

    def tearDown(self):
        self._td.cleanup()

    def test_returns_documentation_with_metadata(self):
        out = ld.get_method_docs("host.get", "7.4", self.base)
        self.assertIn("Zabbix API method: host.get", out)
        self.assertIn("Docs version: 7.4 (local snapshot)", out)
        self.assertIn("Description of host.get.", out)
        self.assertIn("Context7 library: /websites/zabbix_current_en", out)
        self.assertIn("Snapshot fetched: 2026-01-01T00:00:00+00:00", out)

    def test_method_name_case_insensitive(self):
        out = ld.get_method_docs("HOST.GET", "7.4", self.base)
        self.assertIn("Zabbix API method: host.get", out)

    def test_missing_method_raises_value_error(self):
        with self.assertRaises(ValueError):
            ld.get_method_docs("problem.get", "7.4", self.base)

    def test_missing_method_notes_snapshot_missing_set(self):
        # Rebuild the snapshot with 'problem.get' listed in the manifest's
        # missing set; the error message must say so.
        base2 = _make_snapshot(
            self._td.name + "/zabbix", "7.4",
            {"host.get": "## host.get\n"},
            missing=["problem.get"],
        )
        with self.assertRaises(ValueError) as cm:
            ld.get_method_docs("problem.get", "7.4", base2)
        self.assertIn("'missing'", str(cm.exception))

    def test_missing_docs_file_raises_local_docs_error(self):
        (self.base / "7.4" / "docs.md").unlink()
        with self.assertRaises(ld.LocalDocsError):
            ld.get_method_docs("host.get", "7.4", self.base)

    def test_invalid_method_format_raises_value_error(self):
        for bad in ("", "host", "host.get.extra", ".get", "host."):
            with self.assertRaises(ValueError, msg=bad):
                ld.get_method_docs(bad, "7.4", self.base)


class SearchDocsTests(unittest.TestCase):
    def setUp(self):
        self._td = tempfile.TemporaryDirectory()
        self.base = _make_snapshot(self._td.name + "/zabbix", "7.4", _SNAP_SHOTS)

    def tearDown(self):
        self._td.cleanup()

    def test_search_finds_hits_with_snippets(self):
        out = ld.search_docs("proxy", "7.4", self.base)
        # proxy.get has the most hits (heading + body) and must rank first
        self.assertIn("3 method(s) mention \"proxy\"", out)
        self.assertIn("## proxy.get", out)
        self.assertIn("## host.get", out)
        self.assertIn("## item.get", out)
        self.assertIn(">> L1:", out)  # snippet marker on the hit line
        self.assertIn("zabbix_api_docs", out)  # pointer to the full-text tool

    def test_search_case_insensitive(self):
        out = ld.search_docs("PROXY", "7.4", self.base)
        self.assertIn("3 method(s) mention \"PROXY\"", out)

    def test_search_ranked_by_hit_count(self):
        out = ld.search_docs("proxy", "7.4", self.base)
        self.assertLess(out.index("## proxy.get"), out.index("## host.get"))

    def test_search_respects_limit(self):
        out = ld.search_docs("proxy", "7.4", self.base, limit=1)
        self.assertIn("## proxy.get", out)
        self.assertNotIn("## host.get", out)
        self.assertIn("Showing top 1 of 3", out)

    def test_search_object_name_lists_methods(self):
        out = ld.search_docs("host", "7.4", self.base)
        self.assertIn("Object 'host' has 2 method(s): create, get", out)

    def test_search_no_match_is_honest(self):
        out = ld.search_docs("quantum flux", "7.4", self.base)
        self.assertIn('No method docs in Zabbix 7.4 mention "quantum flux"', out)
        self.assertIn("zabbix_api_list", out)

    def test_search_partial_snapshot_notes_missing(self):
        base2 = _make_snapshot(self._td.name + "/zabbix", "7.4",
                               {"host.get": "## host.get\nmentions proxy"},
                               missing=["proxy.get", "item.get"])
        out = ld.search_docs("proxy", "7.4", base2)
        self.assertIn("snapshot is partial — 2 method(s) not downloaded yet", out)

    def test_search_empty_query_raises(self):
        for bad in ("", "   "):
            with self.assertRaises(ValueError, msg=bad):
                ld.search_docs(bad, "7.4", self.base)


if __name__ == "__main__":
    unittest.main(verbosity=2)
