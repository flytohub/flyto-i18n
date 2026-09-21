"""Regression coverage for Space Operations runtime-key ownership."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {
    "en": {
        "spaces.ops.management": "Management",
        "spaces.schedule.block": "Report a blocker",
        "spaces.ops.noReplans": "No replans",
        "spaces.ops.previousAttempt": "Previous attempt",
        "spaces.ops.previousAttemptHint": "Previous attempt. This saved output does not change the current task status.",
        "spaces.ops.learningSaved": "Reusable workflow saved.",
        "spaces.ops.learningNotSaved": "No new reusable workflow was saved from this execution.",
        "spaces.ops.learningReused": "Reused a saved workflow.",
    },
    "zh-TW": {
        "spaces.ops.management": "管理",
        "spaces.schedule.block": "回報阻礙",
        "spaces.ops.noReplans": "尚無重新規劃",
        "spaces.ops.previousAttempt": "先前執行",
        "spaces.ops.previousAttemptHint": "這是先前執行留下的結果，不會改變目前任務的狀態。",
        "spaces.ops.learningSaved": "已保存為可重複使用的工作流程。",
        "spaces.ops.learningNotSaved": "這次執行沒有新增可重複使用的工作流程。",
        "spaces.ops.learningReused": "已復用既有工作流程。",
    },
    "zh-CN": {
        "spaces.ops.management": "管理",
        "spaces.schedule.block": "报告阻碍",
        "spaces.ops.noReplans": "暂无重新规划",
        "spaces.ops.previousAttempt": "先前执行",
        "spaces.ops.previousAttemptHint": "这是先前执行留下的结果，不会改变当前任务的状态。",
        "spaces.ops.learningSaved": "已保存为可重复使用的工作流程。",
        "spaces.ops.learningNotSaved": "这次执行没有新增可重复使用的工作流程。",
        "spaces.ops.learningReused": "已复用现有工作流程。",
    },
}
OWNERS = {
    "spaces.schedule.block": "spaceOperations.json",
    "spaces.ops.management": "spaces.json",
    "spaces.ops.noReplans": "spaceOperations.json",
    "spaces.ops.previousAttempt": "spaceOperations.json",
    "spaces.ops.previousAttemptHint": "spaceOperations.json",
    "spaces.ops.learningSaved": "spaceOperations.json",
    "spaces.ops.learningNotSaved": "spaceOperations.json",
    "spaces.ops.learningReused": "spaceOperations.json",
}


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


def _catalogs(locale: str) -> dict[str, dict[str, str]]:
    """Load every Cloud source catalog for one locale."""
    catalogs = {}
    for path in sorted((ROOT / "locales" / "cloud" / locale).glob("*.json")):
        catalogs[path.name] = json.loads(path.read_text(encoding="utf-8"))[
            "translations"
        ]
    return catalogs


def _cloud_dist(locale: str) -> dict[str, str]:
    """Load one generated Cloud bundle as a flat map."""
    path = ROOT / "dist" / "cloud" / f"{locale}.json"
    return _flatten(json.loads(path.read_text(encoding="utf-8"))["translations"])


def test_operations_runtime_keys_have_reviewed_unique_source_ownership() -> None:
    """Keep runtime labels reviewed and owned by one canonical catalog."""
    for locale, expected in EXPECTED.items():
        catalogs = _catalogs(locale)
        for key, value in expected.items():
            owners = {name for name, catalog in catalogs.items() if key in catalog}
            assert owners == {OWNERS[key]}
            assert catalogs[OWNERS[key]][key] == value


def test_operations_runtime_keys_match_generated_cloud_bundles() -> None:
    """Publish the exact reviewed values in generated Cloud bundles."""
    for locale, expected in EXPECTED.items():
        cloud_dist = _cloud_dist(locale)
        assert {key: cloud_dist[key] for key in expected} == expected
