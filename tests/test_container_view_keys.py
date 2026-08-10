"""Contract tests for the container view, module wizard, and domain row copy.

These keys drive progressive disclosure in the Warroom container panel
(diagnostics toggles, "show more/less" affordances, truncation counters), the
module-confirmation hint in the project wizard, and the per-domain row label in
the external engineer view. Every authored locale must ship a non-empty value
with the exact English placeholder set, and both published dist shapes must be
a faithful rebuild of the authored catalogs.

Assertion style: catalogs here hold tens of thousands of entries, so no
assertion may pass a whole catalog to unittest. Membership is always checked
before indexing, and every failure message carries only locale / origin / key /
value metadata.
"""

import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "locales" / "code"
SCOPED_DIST_DIR = ROOT / "dist" / "code"
FULL_DIST_DIR = ROOT / "dist"

STALE_DIST_HINT = (
    "copy differs between locales/ and dist/ — "
    "run `python3 scripts/build-dist.py` to rebuild the published bundles"
)
MISSING_HINT = (
    "every authored code locale must define this key with a non-empty value"
)
PLACEHOLDER_RE = re.compile(r"\{\{?([A-Za-z_][A-Za-z0-9_.-]*)\}?\}")
HAN_RE = re.compile(r"[一-鿿]")

# key -> the exact placeholder names the English source declares.
REQUIRED_KEYS = {
    "code.projects.modules.confirmRequiredHint": frozenset(),
    "code.external.engineerDomainRowAria": frozenset({"domain"}),
    "code.warroom.containerConnectionFailedGeneric": frozenset(),
    "code.warroom.containerHideDiagnostics": frozenset(),
    "code.warroom.containerShowDiagnostics": frozenset(),
    "code.warroom.containerDiagnostics": frozenset(),
    "code.warroom.containerRunFailedGeneric": frozenset(),
    "code.warroom.containerShowLessImages": frozenset(),
    "code.warroom.containerShowMoreImages": frozenset({"count"}),
    "code.warroom.containerImagesShownOfTotal": frozenset({"shown", "total"}),
    "code.warroom.containerShowLessFindingsFor": frozenset({"image"}),
    "code.warroom.containerShowMoreFindingsFor": frozenset({"count", "image"}),
    "code.warroom.containerShowLessFindings": frozenset(),
    "code.warroom.containerShowMoreFindings": frozenset({"count"}),
    "code.warroom.containerFindingsShownOfTotal": frozenset({"shown", "total"}),
    "code.warroom.containerShowLessSources": frozenset(),
    "code.warroom.containerShowMoreSources": frozenset({"count"}),
    "code.warroom.containerSourcesShownOfTotal": frozenset({"shown", "total"}),
}

CHINESE_LOCALES = ("zh-TW", "zh-CN")
GATE_PREFIX = "code.gate."
# The regression this suite guards against: the feature-gate namespace once
# shipped raw English (or nothing at all) to Chinese readers.
GATE_REGRESSION_HINT = (
    "Chinese feature-gate copy regressed to the English source or an empty "
    "string — restore the reviewed translation and rebuild dist/"
)


def authored_locales():
    """List every authored locale directory for the code project."""
    return sorted(path.name for path in SOURCE_DIR.iterdir() if path.is_dir())


def flatten(obj, prefix=""):
    """Flatten a nested dist bundle back to dotted catalog keys."""
    result = {}
    for key, value in obj.items():
        full_key = prefix if key == "_self" else (
            f"{prefix}.{key}" if prefix else key
        )
        if isinstance(value, dict):
            result.update(flatten(value, full_key))
        else:
            result[full_key] = value
    return result


def load_source(locale):
    """Read the authored code catalog for one locale."""
    path = SOURCE_DIR / locale / "code.json"
    return json.loads(path.read_text(encoding="utf-8"))["translations"]


def load_dist(directory, locale):
    """Read and flatten one published bundle."""
    path = directory / f"{locale}.json"
    return flatten(json.loads(path.read_text(encoding="utf-8"))["translations"])


def catalogs(locale):
    """Yield the authored catalog plus both published dist shapes."""
    return (
        ("source", load_source(locale)),
        ("dist/code", load_dist(SCOPED_DIST_DIR, locale)),
        ("dist", load_dist(FULL_DIST_DIR, locale)),
    )


def placeholders(value):
    """Extract the placeholder names used by one translation value."""
    return frozenset(PLACEHOLDER_RE.findall(str(value)))


class BoundedCatalogAssertions(unittest.TestCase):
    """Assertion helpers that never render a whole catalog on failure."""

    def assert_keys_present(self, catalog, keys, locale, origin, hint):
        """Fail with a sorted key list — never with the catalog itself."""
        missing = sorted(key for key in keys if key not in catalog)
        self.assertEqual(
            [],
            missing,
            f"[{locale}/{origin}] missing {len(missing)} key(s): {missing} — {hint}",
        )

    def present_items(self, catalog, keys):
        """Yield only the (key, value) pairs that exist, so indexing is safe."""
        for key in keys:
            if key in catalog:
                yield key, catalog[key]


class ContainerViewKeyTests(BoundedCatalogAssertions):
    """Pin the container/module/domain copy across locales and bundles."""

    def test_english_source_declares_the_expected_placeholders(self):
        """English is the placeholder contract every locale must match."""
        english = load_source("en")
        self.assert_keys_present(
            english, REQUIRED_KEYS, "en", "source", MISSING_HINT
        )
        for key, value in self.present_items(english, REQUIRED_KEYS):
            with self.subTest(key=key):
                self.assertTrue(str(value).strip(), f"[en] {key} is blank")
                self.assertEqual(
                    REQUIRED_KEYS[key],
                    placeholders(value),
                    f"[en] {key} placeholder drift: {value!r}",
                )

    def test_every_authored_locale_defines_non_empty_values(self):
        """No authored locale may leave one of these keys blank or missing."""
        for locale in authored_locales():
            catalog = load_source(locale)
            self.assert_keys_present(
                catalog, REQUIRED_KEYS, locale, "source", MISSING_HINT
            )
            blank = sorted(
                key
                for key, value in self.present_items(catalog, REQUIRED_KEYS)
                if not str(value).strip()
            )
            with self.subTest(locale=locale):
                self.assertEqual(
                    [], blank, f"[{locale}/source] blank values: {blank}"
                )

    def test_every_authored_locale_matches_english_placeholders(self):
        """Placeholder drift silently breaks interpolation at runtime."""
        for locale in authored_locales():
            catalog = load_source(locale)
            for key, value in self.present_items(catalog, REQUIRED_KEYS):
                with self.subTest(locale=locale, key=key):
                    self.assertEqual(
                        REQUIRED_KEYS[key],
                        placeholders(value),
                        f"[{locale}/source] {key} placeholder drift: {value!r}",
                    )

    def test_both_dist_shapes_match_the_authored_source(self):
        """Scoped and full CDN bundles must both be rebuilt from locales/."""
        for locale in authored_locales():
            source = load_source(locale)
            for origin, catalog in catalogs(locale):
                self.assert_keys_present(
                    catalog, REQUIRED_KEYS, locale, origin, STALE_DIST_HINT
                )
                for key, value in self.present_items(catalog, REQUIRED_KEYS):
                    with self.subTest(locale=locale, origin=origin, key=key):
                        self.assertEqual(
                            source.get(key),
                            value,
                            f"[{locale}/{origin}] {key}: "
                            f"{value!r} != {source.get(key)!r} — {STALE_DIST_HINT}",
                        )

    def test_both_dist_shapes_keep_placeholders_and_stay_non_empty(self):
        """Published bundles are what consumers read — check them directly."""
        for locale in authored_locales():
            for origin, catalog in catalogs(locale):
                self.assert_keys_present(
                    catalog, REQUIRED_KEYS, locale, origin, STALE_DIST_HINT
                )
                for key, value in self.present_items(catalog, REQUIRED_KEYS):
                    with self.subTest(locale=locale, origin=origin, key=key):
                        self.assertTrue(
                            str(value).strip(),
                            f"[{locale}/{origin}] {key} is blank",
                        )
                        self.assertEqual(
                            REQUIRED_KEYS[key],
                            placeholders(value),
                            f"[{locale}/{origin}] {key} placeholder drift: {value!r}",
                        )

    def test_chinese_copy_is_translated_not_the_english_source(self):
        """zh-TW and zh-CN must read as Chinese in source and both bundles."""
        english = load_source("en")
        for locale in CHINESE_LOCALES:
            for origin, catalog in catalogs(locale):
                self.assert_keys_present(
                    catalog, REQUIRED_KEYS, locale, origin, STALE_DIST_HINT
                )
                for key, value in self.present_items(catalog, REQUIRED_KEYS):
                    with self.subTest(locale=locale, origin=origin, key=key):
                        text = str(value)
                        self.assertNotEqual(
                            str(english.get(key, "")).strip(),
                            text.strip(),
                            f"[{locale}/{origin}] {key} is the English source: "
                            f"{text!r}",
                        )
                        self.assertRegex(
                            text,
                            HAN_RE,
                            f"[{locale}/{origin}] {key} has no Han script: {text!r}",
                        )

    def test_traditional_and_simplified_chinese_are_distinct(self):
        """Simplified copy must be converted, not copied from Traditional."""
        traditional = load_source("zh-TW")
        simplified = load_source("zh-CN")
        differing = [
            key
            for key in REQUIRED_KEYS
            if str(traditional.get(key, "")).strip()
            != str(simplified.get(key, "")).strip()
        ]
        self.assertTrue(differing, "zh-CN copy looks identical to zh-TW")

    def test_simplified_chinese_domain_label_uses_mainland_vocabulary(self):
        """zh-CN says 域名/工程详情; zh-TW keeps 網域/工程細節."""
        key = "code.external.engineerDomainRowAria"
        expected = {
            "zh-TW": "開啟網域 {domain} 的工程細節",
            "zh-CN": "打开域名 {domain} 的工程详情",
        }
        for locale, wanted in expected.items():
            for origin, catalog in catalogs(locale):
                with self.subTest(locale=locale, origin=origin):
                    self.assertTrue(
                        key in catalog,
                        f"[{locale}/{origin}] {key} missing — {STALE_DIST_HINT}",
                    )
                    self.assertEqual(
                        wanted,
                        catalog.get(key),
                        f"[{locale}/{origin}] {key}: {catalog.get(key)!r}",
                    )

    def test_chinese_feature_gate_copy_is_not_english_or_empty(self):
        """Regression guard for the feature-gate work these keys ship beside."""
        english = {
            key: value
            for key, value in load_source("en").items()
            if key.startswith(GATE_PREFIX)
        }
        self.assertTrue(english, "the English gate namespace disappeared")
        for locale in CHINESE_LOCALES:
            for origin, catalog in catalogs(locale):
                self.assert_keys_present(
                    catalog, english, locale, origin, GATE_REGRESSION_HINT
                )
                for key, value in self.present_items(catalog, english):
                    with self.subTest(locale=locale, origin=origin, key=key):
                        text = str(value)
                        self.assertTrue(
                            text.strip(),
                            f"[{locale}/{origin}] {key} is empty — "
                            f"{GATE_REGRESSION_HINT}",
                        )
                        self.assertNotEqual(
                            str(english[key]).strip(),
                            text.strip(),
                            f"[{locale}/{origin}] {key} is the English source: "
                            f"{text!r} — {GATE_REGRESSION_HINT}",
                        )
                        self.assertRegex(
                            text,
                            HAN_RE,
                            f"[{locale}/{origin}] {key} has no Han script: "
                            f"{text!r} — {GATE_REGRESSION_HINT}",
                        )


if __name__ == "__main__":
    unittest.main()
