"""Contract tests for the Flyto2 FeatureGate copy."""

import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
GATE_PREFIX = "code.gate."
STALE_DIST_HINT = (
    "gate copy differs between locales/ and dist/ — "
    "run `python3 scripts/build-dist.py` to rebuild the published bundles"
)
PINNED_LOCALES = ("en", "zh-TW", "zh-CN")
REQUIRED_KEYS = {
    "code.gate.backToDashboard",
    "code.gate.capabilitiesUnavailable",
    "code.gate.capabilitiesUnavailableDesc",
    "code.gate.moduleUnavailable",
    "code.gate.moduleUnavailableDesc",
    "code.gate.openBilling",
    "code.gate.previewLocked",
    "code.gate.previewLockedDesc",
    "code.gate.retryCapabilities",
}
REVIEWED_COPY = {
    "zh-TW": {
        "code.gate.backToDashboard": "回到儀表板",
        "code.gate.capabilitiesUnavailable": "無法確認功能權限",
        "code.gate.capabilitiesUnavailableDesc": (
            "Flyto2 目前無法確認這個工作區是否可以使用這項功能。"
            "在確認成功之前，這項功能會維持關閉。"
        ),
        "code.gate.moduleUnavailable": "模組未啟用",
        "code.gate.moduleUnavailableDesc": (
            "這個工作區目前沒有開通這個頁面的功能。"
            "畫面會停留在這裡，而不是直接跳到其他頁面，讓你清楚看到它已被停用。"
        ),
        "code.gate.openBilling": "開啟計費設定",
        "code.gate.previewLocked": "預覽已鎖定",
        "code.gate.previewLockedDesc": (
            "此頁面以預覽形式顯示，但主要工作流程需要升級後才能使用。"
        ),
        "code.gate.retryCapabilities": "重試",
    },
    "zh-CN": {
        "code.gate.backToDashboard": "回到仪表板",
        "code.gate.capabilitiesUnavailable": "无法确认功能权限",
        "code.gate.capabilitiesUnavailableDesc": (
            "Flyto2 目前无法确认这个工作区是否可以使用这项功能。"
            "在确认成功之前，这项功能会保持关闭。"
        ),
        "code.gate.moduleUnavailable": "模块未启用",
        "code.gate.moduleUnavailableDesc": (
            "这个工作区目前没有开通这个页面的功能。"
            "界面会停留在这里，而不是直接跳到其他页面，让你清楚看到它已被停用。"
        ),
        "code.gate.openBilling": "打开计费设置",
        "code.gate.previewLocked": "预览已锁定",
        "code.gate.previewLockedDesc": (
            "此页面以预览形式显示，但主要工作流程需要升级后才能使用。"
        ),
        "code.gate.retryCapabilities": "重试",
    },
}
UNAVAILABLE_HEADLINE_KEY = "code.gate.capabilitiesUnavailable"
UNAVAILABLE_DESC_KEY = "code.gate.capabilitiesUnavailableDesc"
# The production regression: the blocked-capability state shipped internal
# engineering wording to end users instead of product copy.
REVIEWED_HEADLINES = {
    "zh-TW": "無法確認功能權限",
    "zh-CN": "无法确认功能权限",
}
# Brand tokens are the only Latin-script runs allowed in Chinese gate copy.
ALLOWED_LATIN_TOKENS = {"Flyto2"}
LATIN_RUN = re.compile(r"[A-Za-z][A-Za-z0-9]*")
# Internal vocabulary that must never reach a Warroom reader.
BANNED_JARGON = (
    "能力快照",
    "政策檢查",
    "策略检查",
    "政策检查",
    "策略檢查",
    "快照",
    "code.gate",
    "capabilit",
    "snapshot",
    "policy",
    "fallback",
)
JARGON_HINT = (
    "gate copy must read as product language — no capability-snapshot / "
    "policy-check wording, raw catalog keys, or untranslated English"
)


def flatten(obj, prefix=""):
    """Flatten a generated translation object to dotted catalog keys."""
    result = {}
    for key, value in obj.items():
        full_key = f"{prefix}.{key}" if prefix else key
        if isinstance(value, dict):
            result.update(flatten(value, full_key))
        else:
            result[full_key] = value
    return result


def load_source(locale):
    """Read the authored catalog for one code locale."""
    path = ROOT / "locales" / "code" / locale / "code.json"
    return json.loads(path.read_text(encoding="utf-8"))["translations"]


def load_published(locale):
    """Read the built dist bundle for one code locale."""
    path = ROOT / "dist" / "code" / f"{locale}.json"
    return flatten(json.loads(path.read_text(encoding="utf-8"))["translations"])


def gate_entries(catalog):
    """Select every gate namespace entry from a catalog."""
    return {key: value for key, value in catalog.items() if key.startswith(GATE_PREFIX)}


def catalogs(locale):
    """Yield the authored and published catalogs for one locale."""
    return (("source", load_source(locale)), ("dist", load_published(locale)))


class FeatureGateTranslationTests(unittest.TestCase):
    """Keep the FeatureGate blocking states readable in Chinese locales."""

    def test_english_catalog_defines_the_expected_gate_keys(self):
        """Pin the gate namespace so new keys get reviewed translations too."""
        self.assertEqual(REQUIRED_KEYS, set(gate_entries(load_source("en"))))

    def test_published_gate_bundles_match_authored_source(self):
        """Require dist/ to be a faithful rebuild of locales/ for every pin."""
        for locale in PINNED_LOCALES:
            with self.subTest(locale=locale):
                self.assertEqual(
                    gate_entries(load_source(locale)),
                    gate_entries(load_published(locale)),
                    STALE_DIST_HINT,
                )

    def test_chinese_gate_namespaces_are_fully_translated(self):
        """Require every gate string to be non-empty in source and dist."""
        for locale in REVIEWED_COPY:
            for origin, catalog in catalogs(locale):
                with self.subTest(locale=locale, origin=origin):
                    entries = gate_entries(catalog)
                    self.assertEqual(REQUIRED_KEYS, set(entries), STALE_DIST_HINT)
                    self.assertEqual(
                        [],
                        sorted(
                            key
                            for key, value in entries.items()
                            if not str(value).strip()
                        ),
                        STALE_DIST_HINT,
                    )

    def test_chinese_gate_copy_is_not_the_english_fallback(self):
        """Catch copies of the English source leaking into Chinese catalogs."""
        english = gate_entries(load_source("en"))
        for locale in REVIEWED_COPY:
            for origin, catalog in catalogs(locale):
                with self.subTest(locale=locale, origin=origin):
                    entries = gate_entries(catalog)
                    self.assertEqual(
                        [],
                        sorted(
                            key
                            for key, value in entries.items()
                            if str(value).strip() == str(english[key]).strip()
                        ),
                        STALE_DIST_HINT,
                    )
                    self.assertEqual(
                        [],
                        sorted(
                            key
                            for key, value in entries.items()
                            if not any("一" <= char <= "鿿" for char in str(value))
                        ),
                        STALE_DIST_HINT,
                    )

    def test_chinese_gate_copy_has_no_untranslated_latin_words(self):
        """Only brand tokens may stay in Latin script once copy is localized."""
        for locale in REVIEWED_COPY:
            for origin, catalog in catalogs(locale):
                with self.subTest(locale=locale, origin=origin):
                    offenders = sorted(
                        (key, token)
                        for key, value in gate_entries(catalog).items()
                        for token in LATIN_RUN.findall(str(value))
                        if token not in ALLOWED_LATIN_TOKENS
                    )
                    self.assertEqual([], offenders, JARGON_HINT)

    def test_chinese_gate_copy_avoids_internal_engineering_jargon(self):
        """Keep capability-snapshot / policy-check vocabulary out of the UI."""
        for locale in REVIEWED_COPY:
            for origin, catalog in catalogs(locale):
                with self.subTest(locale=locale, origin=origin):
                    offenders = sorted(
                        (key, term)
                        for key, value in gate_entries(catalog).items()
                        for term in BANNED_JARGON
                        if term.lower() in str(value).lower()
                    )
                    self.assertEqual([], offenders, JARGON_HINT)

    def test_unavailable_gate_headline_uses_reviewed_product_copy(self):
        """Pin the exact headline that replaced the engineering wording."""
        for locale, headline in REVIEWED_HEADLINES.items():
            for origin, catalog in catalogs(locale):
                with self.subTest(locale=locale, origin=origin):
                    self.assertEqual(
                        headline, catalog[UNAVAILABLE_HEADLINE_KEY], STALE_DIST_HINT
                    )

    def test_unavailable_gate_description_explains_the_blocked_state(self):
        """The description must say what failed and that access stays closed."""
        for locale in REVIEWED_COPY:
            for origin, catalog in catalogs(locale):
                with self.subTest(locale=locale, origin=origin):
                    description = str(catalog[UNAVAILABLE_DESC_KEY])
                    self.assertIn("Flyto2", description)
                    self.assertNotEqual(
                        description.strip(),
                        catalog[UNAVAILABLE_HEADLINE_KEY].strip(),
                    )
                    self.assertGreater(len(description), len(REVIEWED_HEADLINES[locale]))

    def test_reviewed_chinese_gate_copy_does_not_drift(self):
        """Pin the reviewed Traditional and Simplified Chinese wording."""
        for locale, expected in REVIEWED_COPY.items():
            with self.subTest(locale=locale):
                source = load_source(locale)
                self.assertEqual(
                    expected, {key: source[key] for key in REQUIRED_KEYS}
                )
                published = load_published(locale)
                self.assertEqual(
                    expected,
                    {key: published[key] for key in REQUIRED_KEYS},
                    STALE_DIST_HINT,
                )


if __name__ == "__main__":
    unittest.main()
