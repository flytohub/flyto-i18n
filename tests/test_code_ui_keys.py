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

ATTACK_VALIDATION_KEYS = {
    "code.attackValidation.awaiting",
    "code.attackValidation.canaryOnly",
    "code.attackValidation.closureProgress",
    "code.attackValidation.confidence.high",
    "code.attackValidation.confidence.low",
    "code.attackValidation.confidence.medium",
    "code.attackValidation.confidence.veryHigh",
    "code.attackValidation.emptyBody",
    "code.attackValidation.emptyTitle",
    "code.attackValidation.error",
    "code.attackValidation.mode.analystReview",
    "code.attackValidation.mode.canaryAuthCheck",
    "code.attackValidation.mode.controlledRedTeamReplay",
    "code.attackValidation.mode.controlledTlsProbe",
    "code.attackValidation.ownedScope",
    "code.attackValidation.ready",
    "code.attackValidation.retry",
    "code.attackValidation.safety",
    "code.attackValidation.source.byo",
    "code.attackValidation.source.pulse",
    "code.attackValidation.source.redTeam",
    "code.attackValidation.subtitle",
    "code.attackValidation.title",
}


def flatten(obj, prefix=""):
    """Flatten a nested distribution translation object to dotted keys."""
    result = {}
    for key, value in obj.items():
        full_key = f"{prefix}.{key}" if prefix else key
        if isinstance(value, dict):
            result.update(flatten(value, full_key))
        else:
            result[full_key] = value
    return result


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

    def test_every_code_locale_publishes_attack_validation_contract(self):
        """Keep every locale aligned so runtime English fallback can resolve."""
        locale_root = ROOT / "locales" / "code"
        for path in sorted(locale_root.glob("*/code.json")):
            with self.subTest(locale=path.parent.name):
                translations = json.loads(path.read_text(encoding="utf-8"))["translations"]
                missing = ATTACK_VALIDATION_KEYS - translations.keys()
                self.assertEqual(set(), missing)

                dist_path = ROOT / "dist" / "code" / f"{path.parent.name}.json"
                published = flatten(
                    json.loads(dist_path.read_text(encoding="utf-8"))["translations"]
                )
                self.assertEqual(set(), ATTACK_VALIDATION_KEYS - published.keys())

    def test_reviewed_attack_validation_safety_copy_does_not_drift(self):
        """Protect the explicit authorization boundary in reviewed locales."""
        expected = {
            "en": (
                "Attack validation closure",
                "Active checks require owned scope and unexpired authorization. "
                "Credential validation is canary-only; TLS uses controlled probes, "
                "never third-party interception.",
            ),
            "zh-TW": (
                "攻擊驗證閉環",
                "主動檢查必須限定在自有範圍且授權尚未到期。帳密驗證僅限金絲雀帳號；"
                "TLS 只執行受控探測，絕不攔截第三方流量。",
            ),
        }
        for locale, (title, safety) in expected.items():
            with self.subTest(locale=locale):
                path = ROOT / "locales" / "code" / locale / "code.json"
                translations = json.loads(path.read_text(encoding="utf-8"))["translations"]
                self.assertEqual(title, translations["code.attackValidation.title"])
                self.assertEqual(safety, translations["code.attackValidation.safety"])

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
