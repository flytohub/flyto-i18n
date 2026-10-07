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
        self.module.LOCALES_DIR = Path(self.tmpdir.name)
        self.module.CLOUD_DIR = self.module.LOCALES_DIR / "cloud"
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

    def test_leaves_a_catalog_without_key_changes_byte_for_byte(self):
        """A sync that adds and removes nothing must not restyle the file."""
        original = json.dumps(
            {"translations": {"common.keep": "Keep", "common.stale": "Stale"}},
            indent=4,
        )
        self.path.write_text(original, encoding="utf-8")

        self.module.generate_locale_file("common", {"common.keep"}, "en")

        self.assertEqual(self.path.read_text(encoding="utf-8"), original)

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

    def test_skips_keys_owned_by_another_catalog_across_locales(self):
        """Use English catalog ownership even before another locale is translated."""
        owner_path = self.module.LOCALES_DIR / "modules" / "en" / "crypto.json"
        owner_path.parent.mkdir(parents=True)
        owner_path.write_text(
            json.dumps(
                {
                    "locale": "en",
                    "translations": {"modules.crypto.totp.label": "TOTP Code"},
                }
            ),
            encoding="utf-8",
        )

        self.module.generate_locale_file(
            "modules",
            {"modules.crypto.totp.label", "modules.crypto.new.label"},
            "de",
        )

        generated_path = self.module.CLOUD_DIR / "de" / "modules.json"
        translations = json.loads(generated_path.read_text(encoding="utf-8"))[
            "translations"
        ]
        self.assertNotIn("modules.crypto.totp.label", translations)
        self.assertEqual(translations["modules.crypto.new.label"], "")


class CloudSyncRuntimeKeyTests(unittest.TestCase):
    """A key is the key the runtime resolves: `cloud.a.b` in a catalog is `a.b`.

    flyto-cloud 2026-10-07: `templateDebugger.logs.duration`,
    `templateBuilder.settings.label` and `userSettings.changeAvatar` were held
    as `cloud.`-prefixed keys in template.json and settings.json, which
    build-dist strips. The sync compared raw keys, wrote each a second time as
    an empty string and created `templateDebugger.json`, so the catalog grew a
    266th namespace file and "Validate Cloud Keys for i18n" failed.
    """

    def setUp(self):
        """Hold one key under the stripped prefix in another English catalog."""
        self.module = load_cloud_sync_module()
        self.tmpdir = tempfile.TemporaryDirectory()
        self.module.LOCALES_DIR = Path(self.tmpdir.name)
        self.module.CLOUD_DIR = self.module.LOCALES_DIR / "cloud"
        owner = self.module.CLOUD_DIR / "en" / "template.json"
        owner.parent.mkdir(parents=True)
        owner.write_text(
            json.dumps({"locale": "en", "translations": {"cloud.templateDebugger.logs.duration": "{time}s"}}),
            encoding="utf-8",
        )

    def tearDown(self):
        """Remove the temporary catalog tree."""
        self.tmpdir.cleanup()

    def test_a_key_held_with_the_stripped_prefix_creates_no_namespace_file(self):
        """Write no new namespace file for a key another catalog already holds."""
        for locale in ("en", "de"):
            _, new, _ = self.module.generate_locale_file(
                "templateDebugger", {"templateDebugger.logs.duration"}, locale,
            )
            self.assertEqual(new, 0)
            self.assertFalse((self.module.CLOUD_DIR / locale / "templateDebugger.json").exists())

    def test_a_key_held_with_the_prefix_in_its_own_file_is_not_written_twice(self):
        """Keep a prefixed key as it is instead of adding its unprefixed twin."""
        own = self.module.CLOUD_DIR / "en" / "userSettings.json"
        own.write_text(
            json.dumps({"locale": "en", "translations": {"cloud.userSettings.changeAvatar": "Change Avatar"}}),
            encoding="utf-8",
        )
        self.module.generate_locale_file("userSettings", {"userSettings.changeAvatar"}, "en")
        translations = json.loads(own.read_text(encoding="utf-8"))["translations"]
        self.assertEqual(translations, {"cloud.userSettings.changeAvatar": "Change Avatar"})

    def test_check_names_only_keys_no_catalog_resolves(self):
        """Report only keys no English catalog resolves."""
        missing = self.module.missing_catalog_keys(
            {"templateDebugger": {"templateDebugger.logs.duration", "templateDebugger.logs.absent"}}
        )
        self.assertEqual(missing, {"templateDebugger": {"templateDebugger.logs.absent"}})

    def test_build_dist_and_the_sync_share_one_rule(self):
        """Strip the prefix by the one contract rule in both tools."""
        contract = importlib.util.spec_from_file_location(
            "i18n_contract", SCRIPT_PATH.parent / "i18n_contract.py",
        )
        module = importlib.util.module_from_spec(contract)
        contract.loader.exec_module(module)
        self.assertEqual(module.runtime_key("cloud.a.b"), "a.b")
        self.assertEqual(module.runtime_key("a.cloud.b"), "a.cloud.b")
        build_dist = (SCRIPT_PATH.parent / "build-dist.py").read_text(encoding="utf-8")
        self.assertIn("normalized_key = runtime_key(key)", build_dist)
        self.assertNotIn("key[6:]", build_dist)


if __name__ == "__main__":
    unittest.main()
