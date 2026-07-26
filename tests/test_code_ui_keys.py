import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REQUIRED_CODE_UI_KEYS = {
    "code.agentFirewall.downloadBrowserExtension",
    "code.agentFirewall.downloadIntro",
    "code.agentFirewall.downloadReleaseNotes",
    "code.agentFirewall.downloadTitle",
    "code.agentFirewall.downloadUnavailable",
    "code.sidebar.pulseAllReporting",
    "code.sidebar.pulseNoDataYet",
    "code.sidebar.pulseTagline",
    "auth.localBootstrap.passwordClasses",
    "auth.localBootstrap.passwordMaxBytes",
}


class CodeUIKeyContractTests(unittest.TestCase):
    """Keep release-critical Code copy present in primary supported locales."""

    def test_primary_locales_publish_reviewed_code_ui_copy(self):
        """Require reviewed, non-empty UI copy for each primary locale."""
        for locale in ("en", "zh-TW", "zh-CN"):
            with self.subTest(locale=locale):
                path = ROOT / "locales" / "code" / locale / "code.json"
                translations = json.loads(path.read_text(encoding="utf-8"))["translations"]
                missing = REQUIRED_CODE_UI_KEYS - translations.keys()
                empty = {
                    key
                    for key in REQUIRED_CODE_UI_KEYS
                    if not str(translations.get(key, "")).strip()
                }
                self.assertEqual(set(), missing)
                self.assertEqual(set(), empty)

    def test_local_admin_password_copy_matches_runtime_policy(self):
        """Keep registration copy aligned with the 8-character/72-byte policy."""
        expected = {
            "en": {
                "auth.localBootstrap.passwordLength": "Use at least 8 characters",
                "auth.localBootstrap.passwordMaxBytes": "Use no more than 72 UTF-8 bytes",
            },
            "zh-TW": {
                "auth.localBootstrap.passwordLength": "請使用至少 8 個字元",
                "auth.localBootstrap.passwordMaxBytes": "請勿超過 72 個 UTF-8 位元組",
            },
            "zh-CN": {
                "auth.localBootstrap.passwordLength": "请使用至少 8 个字符",
                "auth.localBootstrap.passwordMaxBytes": "请勿超过 72 个 UTF-8 字节",
            },
        }
        for locale, policy_copy in expected.items():
            with self.subTest(locale=locale):
                path = ROOT / "locales" / "code" / locale / "code.json"
                translations = json.loads(path.read_text(encoding="utf-8"))["translations"]
                for key, value in policy_copy.items():
                    self.assertEqual(value, translations[key])
