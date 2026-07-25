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
