"""Contract coverage for the cumulative Cloud runtime localization import."""

import importlib.util
import hashlib
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LOCALES = ("en", "zh-TW", "zh-CN")
PLACEHOLDER_RE = re.compile(r"\{\{?([A-Za-z_][A-Za-z0-9_.-]*)\}?\}")

AI_SPACE_KEYS = frozenset(
    f"aiSpace.memory.{key}"
    for key in """
approve approvedAt approvedBy approvedState contentHash createLifecycle creator
editInvalidatesApproval indexVersion keepStatus revoke revokedAt revokedBy revokedState
source sourceReference
""".split()
) | frozenset(
    f"aiSpace.missions.{key}"
    for key in """
activeMissions approvalRequired calibrateNext calibration calibrationUnavailable
catalogCountLabels catalogCounts configurationComplete configurationError
configurationHealth configurationHealthAriaLabel configurationLoadError configure
configureNext configured evidenceRequirements loadingConfiguration
loadingConfigurationDetail missing missionHint missionNext missions
missionsNotConfigured monitorNext nextAction noConfigurationData noData noMissionData
notConfigured openSetup overviewLabel overviewSubtitle partialConfiguration
refreshingConfiguration refreshingConfigurationDetail retryConfiguration revision
taskCount unknownStatus zoneSummary zones zonesNotConfigured
""".split()
) | {"aiSpace.workspace.missionSpaceChanged"}

MY_TEMPLATES_KEYS = {"myTemplates.join.close"} | frozenset(
    f"myTemplates.warroomImport.{key}"
    for key in """
action approveBundle assetCount baseUrl checking close credentialsPolicy description
dryRun folderPlan importRecipes imported importing metrics.folders metrics.recipeAssets
metrics.scenarios pendingBundle projectSlug scan scanning scenarios signedInbox title
unknownProducer
""".split()
)

TEMPLATE_BUILDER_KEYS = frozenset(
    f"templateBuilder.missionSetup.{key}"
    for key in """
addObjective addZone cancel description discard discardAriaLabel discardMessage
discardTitle duplicateObjective duplicateZone entryApproval evidenceRequirements
invalidCapability invalidEndpoint invalidEvidence invalidObjective invalidStationKind
invalidZone keepEditing markerId moveDown moveUp noObjectives noZones notes objectiveId
objectiveNumber objectiveTitle objectiveVocabularyUnavailable objectives objectivesHint
promptTemplate removeObjective removeZone requiredCapabilities resourceEndpoint save
saveError saving stationKind summary title unbound unsaved zoneId zoneLabel zoneNumber
zoneVocabularyUnavailable zones zonesHint
""".split()
)

RUNTIME_KEYS = AI_SPACE_KEYS | MY_TEMPLATES_KEYS | TEMPLATE_BUILDER_KEYS
SOURCE_OWNERS = {
    "aiSpace.json": AI_SPACE_KEYS,
    "myTemplates.json": MY_TEMPLATES_KEYS,
    "templateBuilder.json": TEMPLATE_BUILDER_KEYS,
}
RUNTIME_VALUE_DIGESTS = {
    "en": "a6017cb49e38bdec0db279eaa30d783ec25155db69b43fd25cb691ab6d00b1f8",
    "zh-TW": "baaa0d66e7ebe1e00906d397348638019975b05a4b54ce61040ee842fdd964ce",
    "zh-CN": "eebf889d426c58c192309d79af1f41113f2f3526dfa1c50a3a1cb22f794d775b",
}
SPACE_OPERATIONS_KEYS = frozenset(
    f"spaces.draw.{key}"
    for key in """
choose empty explain incomplete loading objective requires retry title zone
""".split()
) | frozenset(
    f"spaces.voice.{key}"
    for key in """
blocked goal listening micDenied micFailed noSpeech placeholder placeholderTyped send
startListening stopListening
""".split()
)


def _flatten(value: dict, prefix: str = "") -> dict[str, str]:
    """Flatten a generated nested translation object."""
    flattened = {}
    for key, child in value.items():
        path = f"{prefix}.{key}" if prefix else key
        if isinstance(child, dict):
            flattened.update(_flatten(child, path))
        else:
            flattened[path] = child
    return flattened


def _source(locale: str) -> dict[str, str]:
    """Merge one official Cloud source locale."""
    merged = {}
    for path in sorted((ROOT / "locales" / "cloud" / locale).glob("*.json")):
        merged.update(json.loads(path.read_text(encoding="utf-8"))["translations"])
    return merged


def _catalogs(locale: str) -> dict[str, dict[str, str]]:
    """Load each official Cloud source catalog without merge shadowing."""
    catalogs = {}
    for path in sorted((ROOT / "locales" / "cloud" / locale).glob("*.json")):
        catalogs[path.name] = json.loads(path.read_text(encoding="utf-8"))[
            "translations"
        ]
    return catalogs


def _runtime_digest(source: dict[str, str]) -> str:
    """Hash the canonical sorted 134-key runtime value map."""
    values = {key: source[key] for key in RUNTIME_KEYS}
    payload = json.dumps(
        values, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def _dist(locale: str) -> dict[str, str]:
    """Load and flatten one generated Cloud bundle."""
    path = ROOT / "dist" / "cloud" / f"{locale}.json"
    return _flatten(json.loads(path.read_text(encoding="utf-8"))["translations"])


def _placeholders(value: str) -> set[str]:
    """Return the named interpolation placeholders in a translation."""
    return set(PLACEHOLDER_RE.findall(value))


def test_exact_cumulative_runtime_namespace_contract_and_counts() -> None:
    """Pin the reviewed 134-key import contract by namespace."""
    assert len(AI_SPACE_KEYS) == 59
    assert len(MY_TEMPLATES_KEYS) == 25
    assert len(TEMPLATE_BUILDER_KEYS) == 50
    assert len(RUNTIME_KEYS) == 134


def test_runtime_keys_have_one_designated_source_catalog_owner() -> None:
    """Reject imported keys duplicated or shadowed across source catalogs."""
    for locale in LOCALES:
        catalogs = _catalogs(locale)
        for owner, keys in SOURCE_OWNERS.items():
            for key in keys:
                actual_owners = {
                    catalog for catalog, values in catalogs.items() if key in values
                }
                assert actual_owners == {owner}, (locale, key, actual_owners)


def test_runtime_values_match_accepted_cloud_provenance() -> None:
    """Pin official-locale values to the accepted bundled Cloud provenance."""
    for locale in LOCALES:
        assert _runtime_digest(_source(locale)) == RUNTIME_VALUE_DIGESTS[locale]


def test_official_sources_and_dist_publish_non_empty_placeholder_safe_union() -> None:
    """Require three-locale parity, source-to-dist identity, and placeholders."""
    sources = {locale: _source(locale) for locale in LOCALES}
    generated = {locale: _dist(locale) for locale in LOCALES}

    for locale in LOCALES:
        assert RUNTIME_KEYS <= sources[locale].keys(), locale
        assert RUNTIME_KEYS <= generated[locale].keys(), locale
        assert all(str(sources[locale][key]).strip() for key in RUNTIME_KEYS), locale
        assert {key: generated[locale][key] for key in RUNTIME_KEYS} == {
            key: sources[locale][key] for key in RUNTIME_KEYS
        }
        assert sources[locale]["accessibility.modal"].strip()
        assert generated[locale]["accessibility.modal"] == sources[locale][
            "accessibility.modal"
        ]
        assert SPACE_OPERATIONS_KEYS <= sources[locale].keys(), locale
        assert SPACE_OPERATIONS_KEYS <= generated[locale].keys(), locale
        assert all(sources[locale][key].strip() for key in SPACE_OPERATIONS_KEYS)

    for key in RUNTIME_KEYS:
        expected = _placeholders(sources["en"][key])
        assert all(_placeholders(sources[locale][key]) == expected for locale in LOCALES)


def test_generated_cloud_union_is_current_and_deterministic() -> None:
    """Keep tracked Cloud output equal to two deterministic source builds."""
    script = ROOT / "scripts" / "build-dist.py"
    spec = importlib.util.spec_from_file_location("cloud_cumulative_build", script)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)

    for locale in LOCALES:
        first = module.build_locale(locale, "cloud")
        second = module.build_locale(locale, "cloud")
        tracked = json.loads(
            (ROOT / "dist" / "cloud" / f"{locale}.json").read_text(encoding="utf-8")
        )
        assert first == second
        assert tracked == first
