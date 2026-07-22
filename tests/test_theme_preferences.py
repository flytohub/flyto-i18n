"""Regression coverage for Warroom CE appearance preference copy."""

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
THEME_KEYS = (
    "code.theme.light",
    "code.theme.dark",
    "code.theme.system",
)


class ThemePreferenceTranslationTests(unittest.TestCase):
    """Require every supported code locale to label all theme choices."""

    def test_theme_preference_labels_are_non_empty_in_every_code_locale(self):
        """Prevent language switching from producing blank theme menu items."""
        locale_files = sorted((ROOT / "locales" / "code").glob("*/code.json"))
        self.assertGreater(len(locale_files), 0)

        for path in locale_files:
            payload = json.loads(path.read_text(encoding="utf-8"))
            translations = payload["translations"]
            for key in THEME_KEYS:
                with self.subTest(locale=path.parent.name, key=key):
                    value = translations.get(key)
                    self.assertIsInstance(value, str)
                    self.assertTrue(value.strip())


if __name__ == "__main__":
    unittest.main()
