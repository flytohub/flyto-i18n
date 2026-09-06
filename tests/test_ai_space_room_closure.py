"""Keep computer task copy canonical, uniquely owned and safe to synchronize."""

import json
import re
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
LOCALES = ("en", "zh-TW", "zh-CN")
OWNED_KEYS = {
    "templateBuilder.json": {
        "templateBuilder.aiChat.welcomeMessageComputer",
        "templateBuilder.aiChat.toolsUnavailableHint",
        "templateBuilder.aiChat.toolsPending",
    },
    "aiSpace.json": {
        "aiSpace.chatResult.browserCleanupFailed",
        "aiSpace.chatResult.reviewUnavailable",
        "aiSpace.chatResult.goalUnverified",
        "aiSpace.resources.dispatchRules.aiTaskMaxSecondsHint",
        "aiSpace.resources.dispatchRules.aiTaskMaxRoundsHint",
        "aiSpace.resources.dispatchRules.aiTaskMaxSeconds",
        "aiSpace.resources.dispatchRules.aiTaskMaxRounds",
        "aiSpace.resources.dispatchRules.keepBrowserHint",
        "aiSpace.workspace.basicSafetyHint",
        "aiSpace.workspace.workflowSummary",
        "aiSpace.workspace.basicScopeHint",
        "aiSpace.workspace.scopeSubtitle",
        "aiSpace.selection.spaceRegistry",
    },
    "spaceOperations.json": {
        "spaces.guide.outcomeReplanned",
        "spaces.guide.outcomeReassigned",
        "spaces.guide.outcomeRetried",
    },
    "productJourney.json": {
        f"productJourney.{name}"
        for name in (
            "workflowsHint", "aiSpaceHint", "warRoomHint", "workflows",
            "aiSpace", "warRoom", "label",
        )
    },
}


def _translations(path: Path) -> dict:
    """Read a source catalog or generated translation object."""
    return json.loads(path.read_text(encoding="utf-8"))["translations"]


def _nested_value(translations: dict, key: str) -> str:
    """Resolve a canonical dotted key in a generated nested bundle."""
    value = translations
    for part in key.split("."):
        value = value[part]
    return value


@pytest.mark.parametrize("locale", LOCALES)
def test_task_copy_has_one_source_owner_and_placeholder_parity(locale):
    """Reject duplicate ownership, empty values and mismatched placeholders."""
    catalogs = {
        path.name: _translations(path)
        for path in (ROOT / "locales/cloud" / locale).glob("*.json")
    }
    for owner, keys in OWNED_KEYS.items():
        english = _translations(ROOT / "locales/cloud/en" / owner)
        for key in keys:
            owners = {
                name for name, values in catalogs.items()
                if key in values or f"cloud.{key}" in values
            }
            assert owners == {owner}, (locale, key, owners)
            value = catalogs[owner][key]
            assert isinstance(value, str) and value.strip()
            assert re.findall(r"\{[^{}]+\}", value) == re.findall(
                r"\{[^{}]+\}", english[key]
            )


@pytest.mark.parametrize("locale", LOCALES)
def test_task_copy_survives_cloud_and_aggregate_distribution(locale):
    """Keep synchronized runtime copy identical to the reviewed source."""
    for scope in ("cloud", ""):
        output = _translations(ROOT / "dist" / scope / f"{locale}.json")
        for owner, keys in OWNED_KEYS.items():
            source = _translations(ROOT / "locales/cloud" / locale / owner)
            for key in keys:
                assert _nested_value(output, key) == source[key], (locale, scope, key)


def test_task_copy_distinguishes_computer_execution_and_verification():
    """Pin computer-local authority and honest verification wording."""
    english = _translations(ROOT / "locales/cloud/en/aiSpace.json")
    chinese = _translations(ROOT / "locales/cloud/zh-TW/templateBuilder.json")
    assert english["aiSpace.resources.dispatchRules.aiTaskMaxRounds"] == "AI response rounds per task"
    assert "still unverified" in english["aiSpace.resources.dispatchRules.aiTaskMaxRoundsHint"]
    assert "verification service was unavailable" in english["aiSpace.chatResult.reviewUnavailable"]
    assert "電腦" in chinese["templateBuilder.aiChat.welcomeMessageComputer"]
    assert sum(map(len, OWNED_KEYS.values())) == 26
