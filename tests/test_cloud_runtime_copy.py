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
    """Load one Cloud locale category's translation mapping."""
    payload = json.loads(
        (CLOUD_LOCALES / locale / f"{category}.json").read_text(encoding="utf-8")
    )
    return payload["translations"]


def test_cloud_runtime_copy_is_complete_for_bundled_locales() -> None:
    """Require complete reviewed runtime copy in each bundled Cloud locale."""
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


def test_needs_you_start_has_an_in_flight_word() -> None:
    """The Start button says it is starting while its request is in flight."""
    expected = {"en": "Starting\u2026", "zh-TW": "\u555f\u52d5\u4e2d\u2026", "zh-CN": "\u542f\u52a8\u4e2d\u2026"}
    for locale, word in expected.items():
        narrative = _translations(locale, "spaceOperations")
        assert narrative["spaces.narrative.action.starting"] == word


def test_recording_upload_names_the_first_published_desktop() -> None:
    """Recording upload needs Desktop 0.7.13: v0.7.12 was tagged and never published."""
    for locale in ("en", "zh-TW", "zh-CN"):
        hint = _translations(locale, "aiSpace")[
            "aiSpace.resources.dispatchRules.uploadRecordingsRequires"
        ]
        assert "Desktop 0.7.13" in hint
        assert "0.7.12" not in hint
