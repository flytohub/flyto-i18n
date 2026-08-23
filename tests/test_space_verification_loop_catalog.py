"""Contract tests for the Space Operations verification-loop copy."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LOCALES = ("en", "zh-TW", "zh-CN")

VERIFICATION_KEYS = frozenset(
    {"spaces.ops.nextAction"}
    | {
        f"spaces.ops.verification{suffix}"
        for suffix in """
ActionContinue ActionDefine ActionNone ActionOpen ActionRepeat ActionResolve
ActionReview ActionShortfall ActionStart ActionWait Contract Empty Evidence
Execution Loop StateActive StateBlocked StateCancelled StateComplete
StateExecutionFailed StateFailed StateInsufficient StateMissing
StateNotConfigured StateNotProven StatePending StateReady StateRefused
StateUnverified StateVerified StatusBlocked StatusCancelled
StatusExecutionFailed StatusInProgress StatusNotProven StatusRefused
StatusUnverified StatusVerified Verdict
""".split()
    }
)

REVIEWED_VALUES = {
    "en": {
        "spaces.ops.nextAction": "Next",
        "spaces.ops.verificationLoop": "Verification loop",
        "spaces.ops.verificationContract": "Acceptance",
        "spaces.ops.verificationStateUnverified": "Completed without proof",
        "spaces.ops.verificationStatusUnverified": "Completed, not verified",
        "spaces.ops.verificationStatusVerified": "Acceptance verified",
        "spaces.ops.verificationActionDefine": "State what the mission must prove.",
        "spaces.ops.verificationActionOpen": "Define the result, then send a mission.",
    },
    "zh-TW": {
        "spaces.ops.nextAction": "下一步",
        "spaces.ops.verificationLoop": "驗證閉環",
        "spaces.ops.verificationContract": "驗收條件",
        "spaces.ops.verificationStateUnverified": "已完成但未驗證",
        "spaces.ops.verificationStatusUnverified": "已完成，但未驗證",
        "spaces.ops.verificationStatusVerified": "驗收已通過",
        "spaces.ops.verificationActionDefine": "請先說明任務必須證明什麼。",
        "spaces.ops.verificationActionOpen": "先定義結果，再送出任務。",
    },
    "zh-CN": {
        "spaces.ops.nextAction": "下一步",
        "spaces.ops.verificationLoop": "验证闭环",
        "spaces.ops.verificationContract": "验收条件",
        "spaces.ops.verificationStateUnverified": "已完成但未验证",
        "spaces.ops.verificationStatusUnverified": "已完成，但未验证",
        "spaces.ops.verificationStatusVerified": "验收已通过",
        "spaces.ops.verificationActionDefine": "请先说明任务必须证明什么。",
        "spaces.ops.verificationActionOpen": "先定义结果，再发送任务。",
    },
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


def _source_catalog(locale: str) -> dict[str, str]:
    """Load the owning Space Operations source catalog."""
    path = ROOT / "locales" / "cloud" / locale / "spaceOperations.json"
    return json.loads(path.read_text(encoding="utf-8"))["translations"]


def _source_owners(locale: str, key: str) -> set[str]:
    """Return every Cloud source catalog that declares one key."""
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


def test_verification_loop_contract_has_exact_additive_key_set() -> None:
    """Pin all states, statuses, actions, stages, and the next-action label."""
    assert len(VERIFICATION_KEYS) == 40
    for locale in LOCALES:
        actual = {
            key
            for key in _source_catalog(locale)
            if key == "spaces.ops.nextAction"
            or key.startswith("spaces.ops.verification")
        }
        assert actual == VERIFICATION_KEYS


def test_verification_loop_copy_is_reviewed_nonempty_and_uniquely_owned() -> None:
    """Keep visible proof language reviewed and source-owned in one catalog."""
    for locale in LOCALES:
        source = _source_catalog(locale)
        assert {key: source[key] for key in REVIEWED_VALUES[locale]} == REVIEWED_VALUES[locale]
        for key in VERIFICATION_KEYS:
            assert source[key].strip()
            assert "{" not in source[key]
            assert _source_owners(locale, key) == {"spaceOperations.json"}


def test_completed_without_proof_is_not_presented_as_verified() -> None:
    """Prevent a completed execution from collapsing into a verified verdict."""
    for locale in LOCALES:
        source = _source_catalog(locale)
        assert source["spaces.ops.verificationStateUnverified"] != source[
            "spaces.ops.verificationStateVerified"
        ]
        assert source["spaces.ops.verificationStatusUnverified"] != source[
            "spaces.ops.verificationStatusVerified"
        ]


def test_verification_loop_source_matches_cloud_and_aggregate_dist() -> None:
    """Publish exactly the reviewed source copy in both generated bundles."""
    for locale in LOCALES:
        source = _source_catalog(locale)
        cloud_dist = _dist(locale)
        aggregate_dist = _dist(locale, scope="")
        for key in VERIFICATION_KEYS:
            assert cloud_dist[key] == source[key]
            assert aggregate_dist[key] == source[key]
