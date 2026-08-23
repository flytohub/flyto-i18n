"""Regression coverage for the reviewed Space device-pairing catalog."""

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

EXPECTED = {
    "en": ("Bound resources", "Pair device"),
    "zh-TW": ("已綁定資源", "配對設備"),
    "zh-CN": ("已绑定资源", "配对设备"),
}


def translations(locale: str, catalog: str) -> dict[str, str]:
    """Load one flat Cloud source catalog for a locale."""
    path = ROOT / "locales" / "cloud" / locale / f"{catalog}.json"
    return json.loads(path.read_text(encoding="utf-8"))["translations"]


class SpacePairingCatalogTest(unittest.TestCase):
    """Keep pairing labels localized and protected from legacy overrides."""

    def test_reviewed_labels_are_not_overridden_by_empty_legacy_values(self):
        """Reject stale empty legacy values that shadow reviewed labels."""
        for locale, (resources, pair_device) in EXPECTED.items():
            with self.subTest(locale=locale):
                operations = translations(locale, "spaceOperations")
                legacy = translations(locale, "spaces")

                self.assertEqual(operations["spaces.ops.resources"], resources)
                self.assertEqual(operations["spaces.ops.pairDevice"], pair_device)
                self.assertNotIn("spaces.ops.resources", legacy)
                self.assertNotIn("spaces.ops.pairDevice", legacy)

    def test_complete_pairing_dialog_is_translated(self):
        """Require the complete pairing dialog contract in official locales."""
        required = {
            "afterPairing",
            "copied",
            "copy",
            "enterOnDevice",
            "expires",
            "failed",
            "generate",
            "mostRegister",
            "pairWhen",
            "subtitle",
            "title",
        }

        for locale in EXPECTED:
            with self.subTest(locale=locale):
                operations = translations(locale, "spaceOperations")
                actual = {
                    key.removeprefix("spaces.pair."): value
                    for key, value in operations.items()
                    if key.startswith("spaces.pair.")
                }
                self.assertEqual(set(actual), required)
                self.assertTrue(all(value.strip() for value in actual.values()))


if __name__ == "__main__":
    unittest.main()
