import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CLOUD_LOCALES = ROOT / "locales" / "cloud"
BROWSER_KEYS = {
    "browserEngine.compReady",
    "browserEngine.compWorking",
    "browserEngine.degradedFallback",
    "browserEngine.degradedTitle",
    "browserEngine.provisioningHint",
    "browserEngine.provisioningTitle",
    "browserEngine.retry",
    "browserEngine.retrying",
}


def _translations(locale: str, category: str) -> dict[str, str]:
    payload = json.loads(
        (CLOUD_LOCALES / locale / f"{category}.json").read_text(encoding="utf-8")
    )
    return payload["translations"]


def test_cloud_runtime_copy_is_complete_for_bundled_locales() -> None:
    for locale in ("en", "zh-TW", "zh-CN"):
        browser = _translations(locale, "browserEngine")
        assert BROWSER_KEYS <= browser.keys()
        assert all(
            isinstance(browser[key], str) and browser[key].strip()
            for key in BROWSER_KEYS
        )

        template_categories = _translations(locale, "templateCategory")
        tool_categories = _translations(locale, "toolCategory")
        assert template_categories["templateCategory.connector"].strip()
        assert tool_categories["toolCategory.connector"].strip()
