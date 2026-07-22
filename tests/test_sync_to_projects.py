"""Regression tests for generated-bundle delivery to sibling projects."""

import importlib.util
import tempfile
import unittest
from pathlib import Path


SCRIPT_PATH = Path(__file__).resolve().parents[1] / "scripts" / "sync-to-projects.py"


def load_sync_module():
    """Load the hyphenated consumer-sync script as an isolated module."""
    spec = importlib.util.spec_from_file_location("sync_to_projects", SCRIPT_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


class SyncToProjectsTests(unittest.TestCase):
    """Verify consumer writes, deletions, manifests, and dry-run isolation."""

    def setUp(self):
        """Redirect generated and consumer paths to a temporary fixture."""
        self.module = load_sync_module()
        self.tmpdir = tempfile.TemporaryDirectory()
        self.root = Path(self.tmpdir.name)
        self.dist_dir = self.root / "dist"
        self.module.DIST_DIR = self.dist_dir

    def tearDown(self):
        """Remove the temporary distribution and consumer fixture."""
        self.tmpdir.cleanup()

    def write_dist_file(self, scope: str, filename: str, value: str) -> Path:
        """Write one generated bundle fixture and return its path."""
        path = self.dist_dir / scope / filename
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(value, encoding="utf-8")
        return path

    def test_sync_single_scope_dry_run_does_not_write_or_delete(self):
        """Report additions and deletions without mutating consumer files."""
        self.write_dist_file("cloud", "en.json", '{"ok": true}\n')
        dest_dir = self.root / "target"
        dest_dir.mkdir()
        stale_file = dest_dir / "ja.json"
        stale_file.write_text('{"stale": true}\n', encoding="utf-8")

        stats = self.module.sync_single_scope("cloud", dest_dir, dry_run=True)

        self.assertEqual(stats["added"], 1)
        self.assertEqual(stats["deleted"], 1)
        self.assertFalse((dest_dir / "en.json").exists())
        self.assertTrue(stale_file.exists())

    def test_sync_single_scope_writes_updates_and_deletes_stale_locale(self):
        """Update changed bundles and remove only stale locale files."""
        self.write_dist_file("cloud", "en.json", '{"version": 2}\n')
        dest_dir = self.root / "target"
        dest_dir.mkdir()
        (dest_dir / "en.json").write_text('{"version": 1}\n', encoding="utf-8")
        (dest_dir / "ja.json").write_text('{"stale": true}\n', encoding="utf-8")
        (dest_dir / "manifest.json").write_text('{"keep": true}\n', encoding="utf-8")

        stats = self.module.sync_single_scope("cloud", dest_dir, dry_run=False)

        self.assertEqual(stats["updated"], 1)
        self.assertEqual(stats["deleted"], 1)
        self.assertEqual((dest_dir / "en.json").read_text(encoding="utf-8"), '{"version": 2}\n')
        self.assertFalse((dest_dir / "ja.json").exists())
        self.assertTrue((dest_dir / "manifest.json").exists())

    def test_sync_manifest_updates_when_source_differs(self):
        """Replace a consumer manifest only when generated content differs."""
        source_dir = self.dist_dir / "code"
        dest_dir = self.root / "public" / "i18n" / "code"
        source_dir.mkdir(parents=True)
        dest_dir.mkdir(parents=True)
        (source_dir / "manifest.json").write_text('{"version": "new"}\n', encoding="utf-8")
        (dest_dir / "manifest.json").write_text('{"version": "old"}\n', encoding="utf-8")

        changed = self.module.sync_manifest(source_dir, dest_dir, dry_run=False)

        self.assertTrue(changed)
        self.assertEqual(
            (dest_dir / "manifest.json").read_text(encoding="utf-8"),
            '{"version": "new"}\n',
        )

    def test_flow_target_uses_static_flow_scope_and_manifest(self):
        target = self.module.SYNC_TARGETS["flow"]

        self.assertEqual(target["repo"], "flyto-flow")
        self.assertEqual(target["targets"], [{
            "scope": "flow",
            "dest": "src/ui/web/frontend/src/i18n/bundled",
            "locales": None,
            "mode": "single-scope-with-manifest",
        }])


if __name__ == "__main__":
    unittest.main()
