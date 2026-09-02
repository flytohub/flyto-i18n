"""Pin owner-first AI Space identity and local-voice localization."""

from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE_ROOT = ROOT / "locales" / "cloud"
LOCALES = tuple(sorted(path.name for path in SOURCE_ROOT.iterdir() if path.is_dir()))
NEW_SUFFIXES = {
    "aliases",
    "aliasesHint",
    "aliasesPlaceholder",
    "displayName",
    "displayNameHint",
    "displayNamePlaceholder",
    "identity",
    "voice",
    "voiceExtend",
    "voiceExtendHint",
    "voiceHint",
    "voiceLocale",
    # The empty option of the locale menu. The field stopped being free text --
    # the platform answers `language-not-supported` to a tag it does not know,
    # and the detector records that the error will not become supported by
    # asking again, so a typo was a Space that never woke with a valid-looking
    # value saved. The empty option is the default and means "listen in the
    # language this machine is set to", which is the whole reason the locale is
    # not hardcoded: whoever installs this on a second computer may not speak
    # the language the Space was set up in.
    "voiceLocaleDevice",
    "voiceOnDevice",
    "voiceSafety",
    "voiceTimeout",
    "wakeWords",
    "wakeWordsHint",
    "wakeWordsPlaceholder",
    "wakeWordsRequired",
}
EXISTING_SUFFIXES = {
    "advanced",
    "advancedHint",
    "automatic",
    "custom",
    "safety",
    "sourceMode",
    "subtitle",
    "title",

    # The wake-word panel's runtime states. They landed in `aiSpace.json`
    # without a line here, so `test_source_ownership_and_localization` has
    # been failing on main since -- the same commit range that left the
    # cumulative seal in `test_cloud_runtime_cumulative_keys.py` short by
    # 32 keys. A catalogue allowed to drift from the file it describes is
    # not a catalogue, so this is recorded rather than absorbed silently.
    #
    # EXISTING and not NEW, deliberately. NEW_SUFFIXES is what the
    # reviewed-values and single-source-owner rules run over, and these are
    # keys that already shipped rather than part of a batch anyone reviewed
    # here. Listing them as new would claim a review that did not happen.
    "voiceArmedLabel",
    "voiceArmedSpaces",
    "voiceCannotEnable",
    "voiceChecking",
    "voiceDownloadAction",
    "voiceDownloadable",
    "voiceDownloading",
    "voiceHeardLabel",
    "voiceHeardNothing",
    "voiceInstallFailed",
    "voiceListening",
    "voiceLocaleConflict",
    "voiceMatchedLabel",
    "voiceMicRefused",
    "voiceNetworkRefused",
    "voiceNoMatch",
    "voiceProblem",
    "voiceReady",
    "voiceRecheck",
    "voiceSpaceNotArmed",
    "voiceSpaceNotArmedDefault",
    "voiceTestHint",
    "voiceTestStart",
    "voiceTestStop",
    "voiceUnavailable",
    "voiceUnsaved",
    "voiceUnsupported",
    "voiceWakeWordTaken",
}
REVIEWED = {
    "en": {
        "identity": "Identity",
        "displayName": "Display name",
        "displayNamePlaceholder": "Operations Space",
        "displayNameHint": "Shown on this Space everywhere. Up to 80 characters.",
        "aliases": "Aliases",
        "aliasesPlaceholder": "ops\nnight shift",
        "aliasesHint": "One alias per line. Up to 8 aliases, 80 characters each.",
        "voice": "Local voice",
        "voiceHint": "Say a wake word to open this Space. Detection stays on this device.",
        "wakeWords": "Wake words",
        "wakeWordsPlaceholder": "hey ops, night shift",
        "wakeWordsHint": "One phrase per line or separated by commas. Up to 8 phrases, 64 characters each.",
        "wakeWordsRequired": "Add at least one wake phrase, or turn local voice off.",
        "voiceLocale": "Recognition locale",
        "voiceTimeout": "Active timeout (ms)",
        "voiceExtend": "Extend while speaking",
        "voiceExtendHint": "Keep listening until the speaker stops, then close the window.",
        "voiceOnDevice": "On-device detection / configuration only",
        "voiceSafety": "Wake words only route you to this Space. They never grant permission, and never bypass approval.",
    },
    "zh-TW": {
        "identity": "身分",
        "displayName": "顯示名稱",
        "displayNamePlaceholder": "作業 Space",
        "displayNameHint": "此名稱會顯示在這個 Space 的所有位置。最多 80 個字元。",
        "aliases": "別名",
        "aliasesPlaceholder": "作業\n夜班",
        "aliasesHint": "每行一個別名。最多 8 個，每個最多 80 個字元。",
        "voice": "本機語音",
        "voiceHint": "說出喚醒詞即可開啟這個 Space。偵測只會在此裝置上進行。",
        "wakeWords": "喚醒詞",
        "wakeWordsPlaceholder": "嘿，作業；夜班",
        "wakeWordsHint": "每行一個詞組，也可以用逗號分隔。最多 8 個，每個最多 64 個字元。",
        "wakeWordsRequired": "請至少新增一個喚醒詞，否則請關閉本機語音。",
        "voiceLocale": "辨識語言",
        "voiceTimeout": "啟用逾時（毫秒）",
        "voiceExtend": "說話時延長",
        "voiceExtendHint": "持續聆聽到說話者停止，再關閉視窗。",
        "voiceOnDevice": "僅限裝置端偵測／設定",
        "voiceSafety": "喚醒詞只會將您導向這個 Space，不會授予權限，也不會略過核准。",
    },
    "zh-CN": {
        "identity": "身份",
        "displayName": "显示名称",
        "displayNamePlaceholder": "作业 Space",
        "displayNameHint": "此名称会显示在这个 Space 的所有位置。最多 80 个字符。",
        "aliases": "别名",
        "aliasesPlaceholder": "作业\n夜班",
        "aliasesHint": "每行一个别名。最多 8 个，每个最多 80 个字符。",
        "voice": "本地语音",
        "voiceHint": "说出唤醒词即可打开这个 Space。检测只会在此设备上进行。",
        "wakeWords": "唤醒词",
        "wakeWordsPlaceholder": "嘿，作业；夜班",
        "wakeWordsHint": "每行一个短语，也可以用逗号分隔。最多 8 个，每个最多 64 个字符。",
        "wakeWordsRequired": "请至少添加一个唤醒词，否则请关闭本地语音。",
        "voiceLocale": "识别语言",
        "voiceTimeout": "启用超时（毫秒）",
        "voiceExtend": "说话时延长",
        "voiceExtendHint": "持续监听直到说话者停止，再关闭窗口。",
        "voiceOnDevice": "仅限设备端检测／配置",
        "voiceSafety": "唤醒词只会将您引导到这个 Space，不会授予权限，也不会绕过审批。",
    },
}


def _translations(path: Path) -> dict[str, object]:
    """Load translations from one source or generated catalog."""
    return json.loads(path.read_text(encoding="utf-8"))["translations"]


def _generated_flat_count(path: Path) -> int:
    """Read the generated pre-nesting flattened translation count."""
    return json.loads(path.read_text(encoding="utf-8"))["total_keys"]


def _flatten(value: object, prefix: str = "") -> dict[str, str]:
    """Flatten either supported generated distribution shape."""
    if not isinstance(value, dict):
        return {prefix: value}
    flattened: dict[str, str] = {}
    for key, child in value.items():
        child_prefix = f"{prefix}.{key}" if prefix else key
        flattened.update(_flatten(child, child_prefix))
    return flattened


def _identity_voice(translations: dict[str, object]) -> dict[str, str]:
    """Select the new settings contract and return suffix-keyed values."""
    prefix = "aiSpace.settings."
    return {
        key.removeprefix(prefix): value
        for key, value in translations.items()
        if key.startswith(prefix) and key.removeprefix(prefix) in NEW_SUFFIXES
    }


def test_identity_voice_has_one_source_owner_in_every_locale() -> None:
    """Require complete, non-empty, uniquely owned source copy in all locales."""
    english = _identity_voice(_translations(SOURCE_ROOT / "en" / "aiSpace.json"))

    for locale in LOCALES:
        owners: dict[str, list[str]] = {suffix: [] for suffix in NEW_SUFFIXES}
        for catalog_path in sorted((SOURCE_ROOT / locale).glob("*.json")):
            for key in _translations(catalog_path):
                prefix = "aiSpace.settings."
                if key.startswith(prefix) and key.removeprefix(prefix) in owners:
                    owners[key.removeprefix(prefix)].append(catalog_path.name)

        owner_errors = {
            suffix: names for suffix, names in owners.items() if names != ["aiSpace.json"]
        }
        assert not owner_errors, f"{locale}: invalid owners for {sorted(owner_errors)}"

        source = _translations(SOURCE_ROOT / locale / "aiSpace.json")
        settings_suffixes = {
            key.removeprefix("aiSpace.settings.")
            for key in source
            if key.startswith("aiSpace.settings.")
        }
        assert settings_suffixes == EXISTING_SUFFIXES | NEW_SUFFIXES, locale
        localized = _identity_voice(source)
        assert all(isinstance(value, str) and value.strip() for value in localized.values()), locale
        if locale != "en":
            assert localized != english, f"{locale}: full English fallback"


def test_reviewed_identity_voice_values_are_exact() -> None:
    """Pin the owner-reviewed English and Chinese copy exactly."""
    for locale, expected in REVIEWED.items():
        actual = _identity_voice(_translations(SOURCE_ROOT / locale / "aiSpace.json"))
        assert actual == expected, locale


def test_identity_voice_matches_both_generated_dist_shapes() -> None:
    """Keep Cloud and aggregate runtime bundles identical to their source owner."""
    for locale in LOCALES:
        source = _identity_voice(_translations(SOURCE_ROOT / locale / "aiSpace.json"))
        cloud = _identity_voice(
            _flatten(_translations(ROOT / "dist" / "cloud" / f"{locale}.json"))
        )
        aggregate = _identity_voice(
            _flatten(_translations(ROOT / "dist" / f"{locale}.json"))
        )
        assert cloud == source, f"{locale}: cloud dist mismatch"
        assert aggregate == source, f"{locale}: aggregate dist mismatch"


def test_generated_manifests_match_flattened_distribution_counts() -> None:
    """Keep both generated manifests and repository coverage synchronized."""
    cloud_manifest = json.loads(
        (ROOT / "dist" / "cloud" / "manifest.json").read_text(encoding="utf-8")
    )
    aggregate_manifest = json.loads(
        (ROOT / "dist" / "manifest.json").read_text(encoding="utf-8")
    )
    repository_manifest = json.loads(
        (ROOT / "manifest.json").read_text(encoding="utf-8")
    )

    failures: dict[str, dict[str, object]] = {}
    for locale in LOCALES:
        cloud_count = _generated_flat_count(
            ROOT / "dist" / "cloud" / f"{locale}.json"
        )
        aggregate_count = _generated_flat_count(ROOT / "dist" / f"{locale}.json")
        expected = {
            "cloud_total": cloud_count,
            "aggregate_total": aggregate_count,
            "repository_coverage": aggregate_manifest["locales"][locale]["completion"],
        }
        actual = {
            "cloud_total": cloud_manifest["locales"][locale]["total_keys"],
            "aggregate_total": aggregate_manifest["locales"][locale]["total_keys"],
            "repository_coverage": repository_manifest["locales"][locale]["coverage"],
        }
        if actual != expected:
            failures[locale] = {"expected": expected, "actual": actual}

    assert not failures, f"manifest mismatches: {failures}"


class IdentityVoiceCatalogTests(unittest.TestCase):
    """Expose the focused contract through the repository's unittest runner."""

    def test_source_ownership_and_localization(self) -> None:
        """Exercise exact suffixes, ownership, and localized source values."""
        test_identity_voice_has_one_source_owner_in_every_locale()

    def test_reviewed_values(self) -> None:
        """Exercise the exact reviewed English and Chinese values."""
        test_reviewed_identity_voice_values_are_exact()

    def test_generated_distribution_shapes(self) -> None:
        """Exercise source equality in Cloud and aggregate distributions."""
        test_identity_voice_matches_both_generated_dist_shapes()

    def test_generated_manifest_counts(self) -> None:
        """Exercise generated totals and repository coverage synchronization."""
        test_generated_manifests_match_flattened_distribution_counts()
