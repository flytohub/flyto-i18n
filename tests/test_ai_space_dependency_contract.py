"""Pin the reviewed AI Space dependency-contract copy and generated bundles."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REVIEWED_LOCALES = ("en", "zh-TW", "zh-CN")
DEPENDENCY_KEYS = {
    "aiSpace.dependency.activePhases",
    "aiSpace.dependency.activePhasesHint",
    "aiSpace.dependency.activePhasesPlaceholder",
    "aiSpace.dependency.automatic",
    "aiSpace.dependency.automaticHint",
    "aiSpace.dependency.automaticShort",
    "aiSpace.dependency.automaticTitle",
    "aiSpace.dependency.bandAssistive",
    "aiSpace.dependency.bandMissionCritical",
    "aiSpace.dependency.bandOptional",
    "aiSpace.dependency.bandRequired",
    "aiSpace.dependency.bandSafetyCritical",
    "aiSpace.dependency.custom",
    "aiSpace.dependency.derived",
    "aiSpace.dependency.evidenceNone",
    "aiSpace.dependency.evidenceRecord",
    "aiSpace.dependency.evidenceRequired",
    "aiSpace.dependency.evidenceRequirement",
    "aiSpace.dependency.maxAgeSeconds",
    "aiSpace.dependency.minimumConfidence",
    "aiSpace.dependency.mode",
    "aiSpace.dependency.outcomeAssistive",
    "aiSpace.dependency.outcomeMissionCritical",
    "aiSpace.dependency.outcomeOptional",
    "aiSpace.dependency.outcomeRequired",
    "aiSpace.dependency.outcomeSafetyCritical",
    "aiSpace.dependency.recoveryTimeout",
    "aiSpace.dependency.retryLimit",
    "aiSpace.dependency.safetyAbort",
    "aiSpace.dependency.safetyImpact",
    "aiSpace.dependency.safetyNone",
    "aiSpace.dependency.safetyPause",
    "aiSpace.dependency.safetyStop",
    "aiSpace.dependency.substituteAny",
    "aiSpace.dependency.substituteEquivalent",
    "aiSpace.dependency.substituteNone",
    "aiSpace.dependency.substituteValidated",
    "aiSpace.dependency.substitutionMode",
    "aiSpace.dependency.taskBlock",
    "aiSpace.dependency.taskDegrade",
    "aiSpace.dependency.taskImpact",
    "aiSpace.dependency.taskInvalidate",
    "aiSpace.dependency.taskNone",
    "aiSpace.dependency.title",
}


def _translations(path: Path) -> dict[str, str]:
    """Load flat source keys or flatten one generated nested runtime bundle."""
    translations = json.loads(path.read_text(encoding="utf-8"))["translations"]
    if any("." in key for key in translations):
        return translations

    flattened: dict[str, str] = {}

    def walk(value: object, prefix: str = "") -> None:
        """Collect nested runtime values under their dot-delimited key."""
        if isinstance(value, dict):
            for key, child in value.items():
                walk(child, f"{prefix}.{key}" if prefix else key)
            return
        flattened[prefix] = value

    walk(translations)
    return flattened


def test_reviewed_dependency_catalogs_are_complete_and_non_empty() -> None:
    """Keep all reviewed locales on the exact operator-facing contract."""
    for locale in REVIEWED_LOCALES:
        translations = _translations(
            ROOT / "locales" / "cloud" / locale / "aiSpace.json"
        )
        dependency = {
            key: value
            for key, value in translations.items()
            if key.startswith("aiSpace.dependency.")
        }

        assert set(dependency) == DEPENDENCY_KEYS
        assert all(isinstance(value, str) and value.strip() for value in dependency.values())


def test_dependency_copy_is_identical_in_cloud_and_aggregate_dist() -> None:
    """Prove generated runtime bundles contain the reviewed source values."""
    for locale in REVIEWED_LOCALES:
        source = _translations(
            ROOT / "locales" / "cloud" / locale / "aiSpace.json"
        )
        cloud = _translations(ROOT / "dist" / "cloud" / f"{locale}.json")
        aggregate = _translations(ROOT / "dist" / f"{locale}.json")

        for key in DEPENDENCY_KEYS:
            assert cloud[key] == source[key]
            assert aggregate[key] == source[key]
