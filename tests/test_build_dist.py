"""Regression tests for aggregate distribution and root-manifest parity."""

import contextlib
import importlib.util
import io
import json
import tempfile
import unittest
from pathlib import Path


SCRIPT_PATH = Path(__file__).resolve().parents[1] / "scripts" / "build-dist.py"

FIXTURE_TRANSLATIONS = {
    "cloud": {"cloud.common.ok": "OK"},
    "modules": {"modules.http.name": "HTTP"},
    "landing": {"landing.hero.title": "Automate everything"},
    "shared": {"common.action.save": "Save"},
}


def load_build_module():
    """Load the hyphenated distribution builder as an isolated module."""
    spec = importlib.util.spec_from_file_location("build_dist", SCRIPT_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def write_fixture_tree(root: Path, locales: tuple) -> None:
    """Create a minimal locales/ tree covering several project directories."""
    for project, translations in FIXTURE_TRANSLATIONS.items():
        for locale in locales:
            locale_dir = root / project / locale
            locale_dir.mkdir(parents=True, exist_ok=True)
            payload = {"translations": {key: f"{value} ({locale})" for key, value in translations.items()}}
            (locale_dir / "catalog.json").write_text(json.dumps(payload), encoding="utf-8")


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


class SelectionArgumentTests(unittest.TestCase):
    """Verify the closed-set, repeatable --scope/--locale filters."""

    def setUp(self):
        """Load a fresh builder module for each test."""
        self.module = load_build_module()

    def test_defaults_select_every_scope_and_locale(self):
        """No arguments means the full build, exactly as before."""
        args = self.module.parse_args([], ["en", "ja"])

        self.assertIsNone(args.scopes)
        self.assertIsNone(args.locales)
        self.assertEqual(
            self.module.select_ordered(args.scopes, self.module.available_scopes()),
            list(self.module.SCOPES) + ["all"],
        )
        self.assertEqual(self.module.select_ordered(args.locales, ["en", "ja"]), ["en", "ja"])

    def test_flags_are_repeatable(self):
        """Repeat --scope/--locale to accumulate several selections."""
        args = self.module.parse_args(
            ["--scope", "landing", "--scope", "app", "--locale", "en", "--locale", "ja"],
            ["en", "ja", "zh-TW"],
        )

        self.assertEqual(args.scopes, ["landing", "app"])
        self.assertEqual(args.locales, ["en", "ja"])

    def test_selection_is_deduplicated_and_canonically_ordered(self):
        """Repeated or out-of-order values collapse to the canonical order."""
        selected = self.module.select_ordered(["app", "landing", "app"], list(self.module.SCOPES))

        self.assertEqual(selected, [scope for scope in self.module.SCOPES if scope in {"landing", "app"}])
        self.assertLess(selected.index("landing"), selected.index("app"))

    def test_rejects_unknown_scope(self):
        """An unknown scope aborts the build instead of silently building all."""
        stderr = io.StringIO()
        with contextlib.redirect_stderr(stderr), self.assertRaises(SystemExit) as caught:
            self.module.parse_args(["--scope", "nope"], ["en"])

        self.assertEqual(caught.exception.code, 2)
        self.assertIn("--scope", stderr.getvalue())

    def test_rejects_unknown_locale(self):
        """An unknown locale aborts the build instead of emitting nothing."""
        stderr = io.StringIO()
        with contextlib.redirect_stderr(stderr), self.assertRaises(SystemExit) as caught:
            self.module.parse_args(["--locale", "xx-YY"], ["en", "ja"])

        self.assertEqual(caught.exception.code, 2)
        self.assertIn("--locale", stderr.getvalue())

    def test_aggregate_scope_is_selectable(self):
        """`all` names the aggregate dist/{locale}.json bundle."""
        args = self.module.parse_args(["--scope", "all"], ["en"])

        self.assertEqual(args.scopes, ["all"])
        self.assertIn("all", self.module.available_scopes())


class FilteredBuildTests(unittest.TestCase):
    """Verify filtered builds emit fewer files but complete manifests."""

    def setUp(self):
        """Point a fresh builder module at a temporary locales/dist tree."""
        self.module = load_build_module()
        self._temp = tempfile.TemporaryDirectory()
        self.addCleanup(self._temp.cleanup)
        root = Path(self._temp.name)
        self.locales_dir = root / "locales"
        self.dist_dir = root / "dist"
        self.repository_manifest = root / "manifest.json"
        write_fixture_tree(self.locales_dir, ("en", "ja"))
        self.repository_manifest.write_text(
            json.dumps({"name": "flyto-i18n", "locales": {"en": {"coverage": 0, "status": "official"}}}),
            encoding="utf-8",
        )
        self.module.LOCALES_DIR = self.locales_dir
        self.module.DIST_DIR = self.dist_dir
        self.module.REPOSITORY_MANIFEST = self.repository_manifest

    def run_build(self, argv):
        """Run the builder quietly and return its captured stdout."""
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            exit_code = self.module.main(argv)
        self.assertEqual(exit_code, 0)
        return stdout.getvalue()

    def read_json(self, relative: str):
        """Read one JSON document from the temporary dist tree."""
        return json.loads((self.dist_dir / relative).read_text(encoding="utf-8"))

    def test_no_arguments_builds_every_scope_and_locale(self):
        """The unfiltered build still writes every bundle it always wrote."""
        self.run_build([])

        for scope in self.module.SCOPES:
            for locale in ("en", "ja"):
                self.assertTrue((self.dist_dir / scope / f"{locale}.json").exists())
            self.assertTrue((self.dist_dir / scope / "manifest.json").exists())
        self.assertTrue((self.dist_dir / "en.json").exists())
        self.assertTrue((self.dist_dir / "ja.json").exists())
        self.assertTrue((self.dist_dir / "manifest.json").exists())
        self.assertTrue((self.dist_dir / "locale-meta.json").exists())

    def test_scope_filter_emits_only_requested_scopes(self):
        """A scoped build skips other scope directories and the aggregate."""
        self.run_build(["--scope", "landing"])

        self.assertTrue((self.dist_dir / "landing" / "en.json").exists())
        self.assertTrue((self.dist_dir / "landing" / "ja.json").exists())
        self.assertFalse((self.dist_dir / "cloud").exists())
        self.assertFalse((self.dist_dir / "en.json").exists())

    def test_locale_filter_emits_only_requested_locales(self):
        """A locale-filtered build writes bundles only for those locales."""
        self.run_build(["--locale", "en"])

        self.assertTrue((self.dist_dir / "landing" / "en.json").exists())
        self.assertFalse((self.dist_dir / "landing" / "ja.json").exists())
        self.assertTrue((self.dist_dir / "en.json").exists())
        self.assertFalse((self.dist_dir / "ja.json").exists())

    def test_filtered_build_keeps_global_manifests_complete(self):
        """Manifests and coverage cover every locale even when filtered."""
        self.run_build(["--scope", "landing", "--locale", "en"])

        scope_manifest = self.read_json("landing/manifest.json")
        root_manifest = self.read_json("manifest.json")
        locale_meta = self.read_json("locale-meta.json")
        repository_manifest = json.loads(self.repository_manifest.read_text(encoding="utf-8"))

        self.assertEqual(sorted(scope_manifest["locales"]), ["en", "ja"])
        self.assertEqual(sorted(root_manifest["locales"]), ["en", "ja"])
        self.assertEqual(sorted(locale_meta["locales"]), ["en", "ja"])
        self.assertEqual(repository_manifest["locales"]["en"]["coverage"], 100.0)

    def test_filtered_manifests_match_the_full_build(self):
        """Filtering bundles never changes manifest content."""
        self.run_build([])
        full_root = self.read_json("manifest.json")
        full_landing = self.read_json("landing/manifest.json")

        self.run_build(["--scope", "landing", "--locale", "ja"])

        self.assertEqual(self.read_json("manifest.json"), full_root)
        self.assertEqual(self.read_json("landing/manifest.json"), full_landing)

    def test_filtered_run_reports_the_active_selection(self):
        """The filtered run states which scopes and locales it emitted."""
        output = self.run_build(["--scope", "landing", "--locale", "en"])

        self.assertIn("filters", output)
        self.assertIn("landing", output)
        self.assertNotIn("→ dist/landing/ja.json", output)
