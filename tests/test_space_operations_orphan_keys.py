"""Regression coverage for Space Operations runtime-key ownership."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {
    "en": {
        "spaces.ops.management": "Management",
        "spaces.ops.noReplans": "No replans",
    },
    "zh-TW": {
        "spaces.ops.management": "管理",
        "spaces.ops.noReplans": "尚無重新規劃",
    },
    "zh-CN": {
        "spaces.ops.management": "管理",
        "spaces.ops.noReplans": "暂无重新规划",
    },
}
OWNERS = {
    "spaces.ops.management": "spaces.json",
    "spaces.ops.noReplans": "spaceOperations.json",
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
