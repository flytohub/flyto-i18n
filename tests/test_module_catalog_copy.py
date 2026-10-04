"""Module catalog copy contract.

flyto-engine's module catalog (internal/modulecatalog/catalog.yaml) is the
only module registry. Every module declares a ``title_key`` and a
``description_key`` under ``projects.feature.*``, and every surface renders
``code.<key>`` from this repository. A missing entry reaches users as a raw
module key, so these tests read the catalog itself rather than a copied list.
"""

import json
import os
import re
import unittest
from pathlib import Path
from typing import List, Optional


ROOT = Path(__file__).resolve().parents[1]
REVIEWED_LOCALES = ("en", "zh-TW", "zh-CN")
FEATURE_PREFIX = "code.projects.feature."
CATALOG_KEY_PATTERN = re.compile(r"^\s*(?:title_key|description_key):\s*(\S+)\s*$", re.MULTILINE)


def load_translations(locale: str) -> dict:
    """Return the flat code translations for one locale."""
    path = ROOT / "locales" / "code" / locale / "code.json"
    return json.loads(path.read_text(encoding="utf-8"))["translations"]


def find_engine_catalog() -> Optional[Path]:
    """Locate the engine module catalog from the environment or a sibling checkout."""
    candidates = []
    explicit = os.environ.get("FLYTO_ENGINE_CATALOG")
    if explicit:
        candidates.append(Path(explicit))
    candidates.append(ROOT.parent / "flyto-engine" / "internal" / "modulecatalog" / "catalog.yaml")
    for candidate in candidates:
        if candidate.is_file():
            return candidate
    return None


def catalog_copy_keys(text: str) -> List[str]:
    """Extract every title_key / description_key value from catalog YAML text."""
    return CATALOG_KEY_PATTERN.findall(text)


class ModuleCatalogCopyTests(unittest.TestCase):
    """Keep module names and descriptions resolvable in every reviewed locale."""

    def test_catalog_key_extraction(self):
        """Read both key kinds and ignore unrelated fields."""
        sample = (
            "modules:\n"
            "  - key: vrm\n"
            "    display_name: Vendor Risk Management\n"
            "    title_key: projects.feature.vrm\n"
            "    description_key: projects.feature.vrmDesc\n"
        )
        self.assertEqual(
            catalog_copy_keys(sample),
            ["projects.feature.vrm", "projects.feature.vrmDesc"],
        )

    def test_every_engine_catalog_key_has_copy(self):
        """Every catalog title_key / description_key resolves in en, zh-TW and zh-CN."""
        catalog = find_engine_catalog()
        if catalog is None:
            self.skipTest("flyto-engine catalog not found; set FLYTO_ENGINE_CATALOG")
        keys = catalog_copy_keys(catalog.read_text(encoding="utf-8"))
        self.assertGreater(len(keys), 0, f"no copy keys found in {catalog}")

        for locale in REVIEWED_LOCALES:
            translations = load_translations(locale)
            for key in keys:
                with self.subTest(locale=locale, key=key):
                    value = translations.get(f"code.{key}")
                    self.assertIsInstance(value, str)
                    self.assertTrue(value.strip())

    def test_feature_copy_is_complete_in_reviewed_locales(self):
        """A module title/description pair in English also exists in zh-TW and zh-CN."""
        english = load_translations("en")
        pairs = [
            key
            for key in english
            if key.startswith(FEATURE_PREFIX)
            and not key.endswith("Desc")
            and f"{key}Desc" in english
        ]
        self.assertGreater(len(pairs), 0)

        for locale in ("zh-TW", "zh-CN"):
            translations = load_translations(locale)
            for title_key in pairs:
                for key in (title_key, f"{title_key}Desc"):
                    with self.subTest(locale=locale, key=key):
                        value = translations.get(key)
                        self.assertIsInstance(value, str)
                        self.assertTrue(value.strip())


if __name__ == "__main__":
    unittest.main()
