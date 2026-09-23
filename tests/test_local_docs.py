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


def _make_snapshot(docs_dir, version: str, methods: dict[str, str]) -> Path:
    """Create a docs snapshot under docs_dir and return its base directory.

    Accepts a Path or str for docs_dir and returns the base as a Path, so
    callers never build Path objects themselves.
    """
    base = Path(docs_dir)
    vdir = base / version
    manifest = {
        "zabbix_version": version,
        "context7_library": "/websites/zabbix_current_en",
        "docs_source": "https://www.zabbix.com/documentation/7.4/en/manual/api",
        "fetched_at": "2026-01-01T00:00:00+00:00",
        "method_count": len(methods),
        "missing": [],
        "methods": methods,
    }
    try:
        for method, rel_path in methods.items():
            doc = vdir / rel_path
            doc.parent.mkdir(parents=True, exist_ok=True)
            doc.write_text(f"# {method}\n\nDescription of {method}.\n")
        (vdir / "manifest.json").write_text(json.dumps(manifest))
    except OSError as exc:
        # Surface fixture-creation failures with the snapshot path attached so
        # a test failure points at the fixture, not the production code.
        raise OSError(f"Could not build docs fixture under {vdir}") from exc
    return base


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


class AvailableVersionsTests(unittest.TestCase):
    def test_missing_dir_yields_empty(self):
        tmp = tempfile.TemporaryDirectory()
        self.assertEqual(ld.available_versions(tmp.name + "/nope"), [])
        tmp.cleanup()

    def test_only_version_dirs_with_manifests_count(self):
        tmp = tempfile.TemporaryDirectory()
        base = _make_snapshot(tmp.name + "/zabbix", "7.4", {"host.get": "api/host/get.md"})
        for decoy in ("notes", "7.4.14", "bad"):
            (base / decoy).mkdir()
        self.assertEqual(ld.available_versions(base), ["7.4"])
        tmp.cleanup()

    def test_sorted_numerically_not_lexicographically(self):
        tmp = tempfile.TemporaryDirectory()
        base = _make_snapshot(tmp.name + "/zabbix", "7.10", {"a.b": "api/a/b.md"})
        _make_snapshot(tmp.name + "/zabbix", "7.4", {"a.b": "api/a/b.md"})
        _make_snapshot(tmp.name + "/zabbix", "6.4", {"a.b": "api/a/b.md"})
        self.assertEqual(ld.available_versions(base), ["6.4", "7.4", "7.10"])
        tmp.cleanup()


class ListMethodsTests(unittest.TestCase):
    def setUp(self):
        self._td = tempfile.TemporaryDirectory()
        self.base = _make_snapshot(
            self._td.name + "/zabbix",
            "7.4",
            {
                "host.get": "api/host/get.md",
                "host.create": "api/host/create.md",
                "item.get": "api/item/get.md",
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
            self._td.name + "/zabbix", "7.4", {"host.get": "api/host/get.md"}
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

    def test_missing_doc_file_raises_local_docs_error(self):
        (self.base / "7.4" / "api" / "host" / "get.md").unlink()
        with self.assertRaises(ld.LocalDocsError):
            ld.get_method_docs("host.get", "7.4", self.base)

    def test_invalid_method_format_raises_value_error(self):
        for bad in ("", "host", "host.get.extra", ".get", "host."):
            with self.assertRaises(ValueError, msg=bad):
                ld.get_method_docs(bad, "7.4", self.base)


if __name__ == "__main__":
    unittest.main(verbosity=2)
