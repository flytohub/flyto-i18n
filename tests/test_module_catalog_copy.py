"""Module catalog copy contract.

flyto-engine's module catalog (internal/modulecatalog/catalog.yaml) is the
only module registry. Every module declares a ``title_key`` and a
``description_key`` under ``projects.feature.*``, and every surface renders
``code.<key>`` from this repository. A missing entry reaches users as a raw
module key, so these tests read the catalog itself rather than a copied list.

The catalog lives in flyto-engine, which is internal; this repository is
public, so its CI cannot read the catalog. The authoritative gate therefore
runs in flyto-engine's CI (``catalog-copy`` job), which reads this public
repository. Here the same check runs whenever a workspace checkout or
``FLYTO_ENGINE_CATALOG`` provides the catalog, so a contributor sees a gap
before the engine gate does; without it the suite skips.
"""

from __future__ import annotations

import json
import os
import re
import tempfile
import unittest
from collections.abc import Mapping
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
# The locales flyto-engine's scripts/check-i18n-keys.py treats as primary.
# Every other locale renders these keys through the consumer's English fallback.
REVIEWED_LOCALES = ("en", "zh-TW", "zh-CN", "ja")
CATALOG_ENV = "FLYTO_ENGINE_CATALOG"
CATALOG_RELATIVE = Path("flyto-engine") / "internal" / "modulecatalog" / "catalog.yaml"
CATALOG_KEY_PATTERN = re.compile(r"^\s*(?:title_key|description_key):\s*(\S+)\s*$", re.MULTILINE)


class CatalogNotFound(Exception):
    """The engine catalog is required here but could not be located."""


def load_translations(locale: str) -> dict:
    """Return the flat code translations for one locale."""
    path = ROOT / "locales" / "code" / locale / "code.json"
    return json.loads(path.read_text(encoding="utf-8"))["translations"]


def find_engine_catalog(env: Mapping[str, str], root: Path) -> Path | None:
    """Locate the engine module catalog.

    An explicit ``FLYTO_ENGINE_CATALOG`` must exist. Otherwise every ancestor of
    ``root`` is tried for a ``flyto-engine`` sibling, which covers both a
    workspace clone and an agent worktree nested under ``.claude/worktrees``.
    Returns None when no catalog is available (flyto-engine CI is the gate).
    """
    explicit = env.get(CATALOG_ENV, "").strip()
    if explicit:
        path = Path(explicit)
        if not path.is_file():
            raise CatalogNotFound(f"{CATALOG_ENV}={explicit} is not a file")
        return path
    for ancestor in (root, *root.parents):
        candidate = ancestor / CATALOG_RELATIVE
        if candidate.is_file():
            return candidate
    return None


def catalog_copy_keys(text: str) -> list[str]:
    """Extract every title_key / description_key value from catalog YAML text."""
    return CATALOG_KEY_PATTERN.findall(text)


class CatalogLocationTests(unittest.TestCase):
    """The catalog lookup fails loudly wherever enforcement is expected."""

    def setUp(self):
        """Create a fake workspace with an i18n worktree nested like an agent checkout."""
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.base = Path(self.tmp.name)
        self.repo = self.base / "flyto-i18n" / ".claude" / "worktrees" / "topic"
        self.repo.mkdir(parents=True)

    def write_catalog(self, base: Path) -> Path:
        """Write a minimal catalog where a workspace keeps flyto-engine."""
        path = base / CATALOG_RELATIVE
        path.parent.mkdir(parents=True)
        path.write_text("modules: []\n", encoding="utf-8")
        return path

    def test_missing_catalog_skips_even_under_ci(self):
        """This public repository's CI cannot read the internal engine; engine CI is the gate."""
        self.assertIsNone(find_engine_catalog({"CI": "true"}, self.repo))

    def test_missing_catalog_is_optional_outside_ci(self):
        """A contributor without flyto-engine can still run the suite locally."""
        self.assertIsNone(find_engine_catalog({}, self.repo))

    def test_explicit_path_must_exist(self):
        """A misconfigured FLYTO_ENGINE_CATALOG is an error, not a fallback."""
        with self.assertRaises(CatalogNotFound):
            find_engine_catalog({CATALOG_ENV: str(self.base / "missing.yaml")}, self.repo)

    def test_explicit_path_wins(self):
        """FLYTO_ENGINE_CATALOG takes precedence over a workspace sibling."""
        self.write_catalog(self.base)
        explicit = self.base / "explicit.yaml"
        explicit.write_text("modules: []\n", encoding="utf-8")
        self.assertEqual(find_engine_catalog({CATALOG_ENV: str(explicit)}, self.repo), explicit)

    def test_worktree_finds_workspace_sibling(self):
        """A worktree under .claude/worktrees finds the workspace's flyto-engine."""
        expected = self.write_catalog(self.base)
        self.assertEqual(find_engine_catalog({"CI": "true"}, self.repo), expected)


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
        """Every catalog title_key / description_key resolves in every reviewed locale."""
        catalog = find_engine_catalog(os.environ, ROOT)
        if catalog is None:
            self.skipTest(f"flyto-engine catalog not found outside CI; set {CATALOG_ENV}")
        keys = catalog_copy_keys(catalog.read_text(encoding="utf-8"))
        self.assertGreater(len(keys), 0, f"no copy keys found in {catalog}")

        for locale in REVIEWED_LOCALES:
            translations = load_translations(locale)
            for key in keys:
                with self.subTest(locale=locale, key=key):
                    value = translations.get(f"code.{key}")
                    self.assertIsInstance(value, str)
                    self.assertTrue(value.strip())


if __name__ == "__main__":
    unittest.main()
