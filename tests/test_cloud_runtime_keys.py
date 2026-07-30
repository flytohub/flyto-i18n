"""Contract tests for Cloud runtime translations that must never fall through."""

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REQUIRED_SOURCE_KEYS = {
    "browserEngine.json": {
        "browserEngine.provisioningHint",
        "browserEngine.provisioningTitle",
    },
    "templateCategory.json": {"templateCategory.connector"},
    "toolCategory.json": {"toolCategory.connector"},
}
REQUIRED_DIST_KEYS = set().union(*REQUIRED_SOURCE_KEYS.values())


def flatten(obj, prefix=""):
    """Flatten nested distribution translations to dotted runtime keys."""
    result = {}
    for key, value in obj.items():
        full_key = f"{prefix}.{key}" if prefix else key
        if isinstance(value, dict):
            result.update(flatten(value, full_key))
        else:
            result[full_key] = value
    return result


class CloudRuntimeTranslationTests(unittest.TestCase):
    """Keep dev and CDN consumers free from missing-key fallback warnings."""

    def test_required_source_keys_are_non_empty_in_every_cloud_locale(self):
        """Reject present-but-empty source values filtered out by the loader."""
        locale_dirs = sorted((ROOT / "locales" / "cloud").iterdir())
        self.assertGreater(len(locale_dirs), 0)

        for locale_dir in locale_dirs:
            if not locale_dir.is_dir():
                continue
            for filename, required_keys in REQUIRED_SOURCE_KEYS.items():
                path = locale_dir / filename
                translations = json.loads(path.read_text(encoding="utf-8"))[
                    "translations"
                ]
                for key in required_keys:
                    with self.subTest(
                        locale=locale_dir.name,
                        filename=filename,
                        key=key,
                    ):
                        value = translations.get(key)
                        self.assertIsInstance(value, str)
                        self.assertTrue(value.strip())

    def test_required_keys_are_non_empty_in_every_cloud_distribution(self):
        """Ensure generated CDN bundles preserve every required runtime key."""
        locale_names = sorted(
            path.name
            for path in (ROOT / "locales" / "cloud").iterdir()
            if path.is_dir()
        )
        dist_files = [
            ROOT / "dist" / "cloud" / f"{locale}.json"
            for locale in locale_names
        ]
        self.assertGreater(len(dist_files), 0)

        for path in dist_files:
            translations = flatten(
                json.loads(path.read_text(encoding="utf-8"))["translations"]
            )
            for key in REQUIRED_DIST_KEYS:
                with self.subTest(locale=path.stem, key=key):
                    value = translations.get(key)
                    self.assertIsInstance(value, str)
                    self.assertTrue(value.strip())


if __name__ == "__main__":
    unittest.main()
