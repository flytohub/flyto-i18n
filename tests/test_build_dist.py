"""Regression tests for aggregate distribution and root-manifest parity."""

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


SCRIPT_PATH = Path(__file__).resolve().parents[1] / "scripts" / "build-dist.py"


def load_build_module():
    """Load the hyphenated distribution builder as an isolated module."""
    spec = importlib.util.spec_from_file_location("build_dist", SCRIPT_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


class RepositoryManifestSyncTests(unittest.TestCase):
    """Verify root coverage follows aggregate distribution evidence."""

    def setUp(self):
        """Load a fresh builder module for each test."""
        self.module = load_build_module()

    def test_updates_known_locale_coverage_and_preserves_metadata(self):
        """Update derived coverage without replacing hand-maintained fields."""
        root = {
            "name": "flyto-i18n",
            "locales": {
                "en": {"coverage": 10, "status": "official"},
                "ja": {"coverage": 20, "status": "community"},
            },
        }
        distribution = {
            "locales": {
                "en": {"completion": 99.8},
                "ja": {"completion": 92.9},
                "unknown": {"completion": 100},
            },
        }
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "manifest.json"
            path.write_text(json.dumps(root), encoding="utf-8")
            changed = self.module.sync_repository_manifest(distribution, path)
            actual = json.loads(path.read_text(encoding="utf-8"))

        self.assertTrue(changed)
        self.assertEqual(actual["locales"]["en"]["coverage"], 99.8)
        self.assertEqual(actual["locales"]["ja"]["coverage"], 92.9)
        self.assertEqual(actual["locales"]["en"]["status"], "official")
        self.assertNotIn("unknown", actual["locales"])

    def test_flow_scope_includes_mcp_studio_catalog(self):
        """Keep the shared MCP surface available to the self-hosted UI."""
        distribution = self.module.build_locale("en", "flow")

        self.assertEqual(distribution["translations"]["mcpStudio"]["title"], "MCP Studio")
