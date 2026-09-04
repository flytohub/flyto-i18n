"""Contract tests for AI Space workflow-runner and War Room dispatch copy."""

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LOCALES = ("en", "zh-TW", "zh-CN")

RUNNER_BINDING_KEYS = frozenset(
    {
        "aiSpace.missions.dispatchable",
        "aiSpace.missions.dispatchableHint",
        "aiSpace.missions.dispatchableNone",
        "aiSpace.missions.dispatchableUnreadable",
        "aiSpace.missions.notDispatchable",
        "aiSpace.workspace.machineBindingAutomatic",
        "aiSpace.workspace.machineBindingSaveFailed",
        "aiSpace.workspace.machineBindingSaved",
    }
    | {
        f"aiSpace.resources.machineBindings.{suffix}"
        for suffix in (
            "automatic",
            "automaticHint",
            "hint",
            "loadError",
            "loading",
            "noMachines",
            "noWorkflows",
            "offline",
            "online",
            "retry",
            "saving",
            "title",
            "unavailable",
            "unnamed",
            "workflow",
        )
    }
)

REVIEWED_VALUES = {
    "en": {
        "aiSpace.missions.dispatchable": "Dispatchable workflows",
        "aiSpace.missions.dispatchableHint": (
            "War Room can schedule these workflows; AI Space executes them on an "
            "allowed capable machine."
        ),
        "aiSpace.resources.machineBindings.automatic": (
            "Automatic — any capable machine"
        ),
        "aiSpace.resources.machineBindings.hint": (
            "AI Space runs each workflow locally. War Room may dispatch it to any "
            "capable machine you allow here."
        ),
        "aiSpace.resources.machineBindings.title": "Workflow runners",
        "aiSpace.workspace.machineBindingSaved": "Workflow runners updated",
    },
    "zh-TW": {
        "aiSpace.missions.dispatchable": "可派送工作流程",
        "aiSpace.missions.dispatchableHint": (
            "作戰室可以排程這些工作流程；AI Space 會在獲准且能力相符的機器上執行。"
        ),
        "aiSpace.resources.machineBindings.automatic": (
            "自動配置 — 任何能力相符的機器"
        ),
        "aiSpace.resources.machineBindings.hint": (
            "AI Space 會在本地執行每個工作流程；作戰室可將任務派給您在此允許、且能力相符的任何機器。"
        ),
        "aiSpace.resources.machineBindings.title": "工作流程執行機器",
        "aiSpace.workspace.machineBindingSaved": "已更新工作流程執行機器",
    },
    "zh-CN": {
        "aiSpace.missions.dispatchable": "可派发工作流",
        "aiSpace.missions.dispatchableHint": (
            "作战室可以调度这些工作流；AI Space 会在获准且能力匹配的机器上执行。"
        ),
        "aiSpace.resources.machineBindings.automatic": (
            "自动配置 — 任何能力匹配的机器"
        ),
        "aiSpace.resources.machineBindings.hint": (
            "AI Space 会在本地执行每个工作流；作战室可将任务派给您在此允许且能力匹配的任何机器。"
        ),
        "aiSpace.resources.machineBindings.title": "工作流执行机器",
        "aiSpace.workspace.machineBindingSaved": "已更新工作流执行机器",
    },
}


def _flatten(value: dict, prefix: str = "") -> dict[str, str]:
    """Flatten one generated nested translation object."""
    flattened = {}
    for key, child in value.items():
        path = f"{prefix}.{key}" if prefix else key
        if isinstance(child, dict):
            flattened.update(_flatten(child, path))
        else:
            flattened[path] = child
    return flattened


def _source_catalog(locale: str) -> dict[str, str]:
    """Load the source-owned AI Space catalog for one locale."""
    path = ROOT / "locales" / "cloud" / locale / "aiSpace.json"
    return json.loads(path.read_text(encoding="utf-8"))["translations"]


def _source_owners(locale: str, key: str) -> set[str]:
    """Return each Cloud source catalog that declares one key."""
    owners = set()
    for path in sorted((ROOT / "locales" / "cloud" / locale).glob("*.json")):
        translations = json.loads(path.read_text(encoding="utf-8"))["translations"]
        if key in translations:
            owners.add(path.name)
    return owners


def _dist(locale: str, scope: str = "cloud") -> dict[str, str]:
    """Load one generated distribution bundle as a flat key map."""
    path = ROOT / "dist" / scope / f"{locale}.json" if scope else ROOT / "dist" / f"{locale}.json"
    return _flatten(json.loads(path.read_text(encoding="utf-8"))["translations"])


def _placeholders(value: str) -> set[str]:
    """Return the interpolation placeholders declared by one value."""
    return set(re.findall(r"\{[^{}]+\}", value))


def test_runner_binding_contract_has_exact_additive_key_set() -> None:
    """Pin every new placement, dispatch, and save-state key."""
    assert len(RUNNER_BINDING_KEYS) == 23
    for locale in LOCALES:
        source = _source_catalog(locale)
        actual = {
            key
            for key in source
            if key.startswith("aiSpace.resources.machineBindings.")
            or key.startswith("aiSpace.workspace.machineBinding")
            or key
            in {
                "aiSpace.missions.dispatchable",
                "aiSpace.missions.dispatchableHint",
                "aiSpace.missions.dispatchableNone",
                "aiSpace.missions.dispatchableUnreadable",
                "aiSpace.missions.notDispatchable",
            }
        }
        assert actual == RUNNER_BINDING_KEYS


def test_runner_binding_copy_is_reviewed_nonempty_and_uniquely_owned() -> None:
    """Keep visible copy reviewed, non-empty, and owned by AI Space."""
    for locale in LOCALES:
        source = _source_catalog(locale)
        assert {key: source[key] for key in REVIEWED_VALUES[locale]} == REVIEWED_VALUES[locale]
        for key in RUNNER_BINDING_KEYS:
            assert source[key].strip()
            assert _source_owners(locale, key) == {"aiSpace.json"}


def test_runner_binding_placeholder_parity_and_existing_elsewhere_copy() -> None:
    """Preserve placeholder parity and the prior remote-machine count label."""
    english = _source_catalog("en")
    for locale in LOCALES:
        source = _source_catalog(locale)
        assert source["aiSpace.selection.elsewhere"].strip()
        for key in RUNNER_BINDING_KEYS:
            assert _placeholders(source[key]) == _placeholders(english[key])


def test_runner_binding_source_matches_cloud_and_aggregate_dist() -> None:
    """Publish identical copy in Cloud and aggregate distributions."""
    for locale in LOCALES:
        source = _source_catalog(locale)
        cloud_dist = _dist(locale)
        aggregate_dist = _dist(locale, scope="")
        for key in RUNNER_BINDING_KEYS | {"aiSpace.selection.elsewhere"}:
            assert cloud_dist[key] == source[key]
            assert aggregate_dist[key] == source[key]
