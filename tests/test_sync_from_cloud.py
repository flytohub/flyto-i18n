"""Regression tests for deletion-safe Cloud key synchronization."""

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


SCRIPT_PATH = Path(__file__).resolve().parents[1] / "scripts" / "sync-from-cloud.py"


def load_cloud_sync_module():
    """Load the hyphenated Cloud sync script as an isolated module."""
    spec = importlib.util.spec_from_file_location("sync_from_cloud", SCRIPT_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


class CloudSyncDeletionTests(unittest.TestCase):
    """Verify Cloud scanner omissions do not delete catalog keys by default."""

    def setUp(self):
        """Redirect Cloud locale output to a temporary catalog tree."""
        self.module = load_cloud_sync_module()
        self.tmpdir = tempfile.TemporaryDirectory()
        self.module.CLOUD_DIR = Path(self.tmpdir.name)
        self.path = self.module.CLOUD_DIR / "en" / "common.json"
        self.path.parent.mkdir(parents=True)
        self.path.write_text(
            json.dumps({"translations": {"common.keep": "Keep", "common.stale": "Stale"}}),
            encoding="utf-8",
        )

    def tearDown(self):
        """Remove the temporary Cloud catalog tree."""
        self.tmpdir.cleanup()

    def test_preserves_unscanned_keys_by_default(self):
        """Merge scanned keys without deleting an existing scanner omission."""
        self.module.generate_locale_file("common", {"common.keep", "common.new"}, "en")
        translations = json.loads(self.path.read_text(encoding="utf-8"))["translations"]

        self.assertEqual(translations["common.keep"], "Keep")
        self.assertEqual(translations["common.stale"], "Stale")
        self.assertEqual(translations["common.new"], "")

    def test_deletes_only_with_explicit_flag(self):
        """Remove an unscanned key only when destructive mode is explicit."""
        self.module.generate_locale_file(
            "common",
            {"common.keep"},
            "en",
            delete_stale=True,
        )
        translations = json.loads(self.path.read_text(encoding="utf-8"))["translations"]

        self.assertEqual(translations, {"common.keep": "Keep"})


if __name__ == "__main__":
    unittest.main()
