"""Regression tests for deletion-safe Core module synchronization."""

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


SCRIPT_PATH = Path(__file__).resolve().parents[1] / "scripts" / "sync-from-core.py"


def load_core_sync_module():
    """Load the hyphenated Core sync script as an isolated module."""
    spec = importlib.util.spec_from_file_location("sync_from_core", SCRIPT_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


class CoreSyncDeletionTests(unittest.TestCase):
    """Verify Core synchronization preserves values unless deletion is explicit."""

    def setUp(self):
        """Redirect Core synchronization output to temporary directories."""
        self.module = load_core_sync_module()
        self.tmpdir = tempfile.TemporaryDirectory()
        root = Path(self.tmpdir.name)
        self.module.MODULES_EN_DIR = root / "modules" / "en"
        self.module.SHARED_EN_DIR = root / "shared" / "en"
        self.path = self.module.MODULES_EN_DIR / "api.json"

    def tearDown(self):
        """Remove the temporary Core synchronization tree."""
        self.tmpdir.cleanup()

    def test_preserves_existing_values_by_default(self):
        """Merge scanned values while retaining unscanned existing entries."""
        grouped = {"api": {"modules.api.keep": "Updated"}}
        existing = {
            "api": {
                "modules.api.keep": "Old",
                "modules.api.stale": "Preserve me",
            }
        }
        stats = self.module.write_locale_files(grouped, existing)
        translations = json.loads(self.path.read_text(encoding="utf-8"))["translations"]

        self.assertEqual(translations["modules.api.keep"], "Updated")
        self.assertEqual(translations["modules.api.stale"], "Preserve me")
        self.assertEqual(stats["preserved"], 1)
        self.assertEqual(stats["deleted"], 0)

    def test_deletes_only_when_no_delete_is_false(self):
        """Drop unscanned values only in explicit destructive mode."""
        grouped = {"api": {"modules.api.keep": "Updated"}}
        existing = {"api": {"modules.api.keep": "Old", "modules.api.stale": "Delete me"}}
        stats = self.module.write_locale_files(grouped, existing, no_delete=False)
        translations = json.loads(self.path.read_text(encoding="utf-8"))["translations"]

        self.assertEqual(translations, {"modules.api.keep": "Updated"})
        self.assertEqual(stats["deleted"], 1)


if __name__ == "__main__":
    unittest.main()
