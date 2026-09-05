"""Contract coverage for the cumulative Cloud runtime localization import."""

import contextlib
import hashlib
import importlib.util
import io
import json
import re
import tempfile
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
OPEN_OPERATIONS_VALUES = {
    "en": "Operations room",
    "zh-TW": "作戰室",
    "zh-CN": "作战室",
}
LOCAL_CAMERA_VALUES = {
    "en": {
        "spaces.ops.live": "Room connected",
        "spaces.ops.subtitle": "Mission operations and evidence",
        "spaces.ops.localNearRealtime": "Local camera · near-real-time · {fps} FPS",
        "spaces.ops.cameraDelayed": "Local camera images delayed",
        "spaces.ops.lastFrameAgo": "Last local camera image {seconds}s ago",
        "spaces.ops.cameraDisconnected": "Local camera disconnected",
        "spaces.ops.cameraPermissionDenied": "Local camera permission denied",
        "spaces.ops.cameraStarting": "Starting local camera…",
        "spaces.ops.cameraPrivacy": "Camera images stay on this device",
        "spaces.ops.cameraFrameAlt": "Local near-real-time camera image",
    },
    "zh-TW": {
        "spaces.ops.live": "房間已連線",
        "spaces.ops.subtitle": "任務操作與證據",
        "spaces.ops.localNearRealtime": "本機攝影機 · 近即時 · {fps} FPS",
        "spaces.ops.cameraDelayed": "本機攝影機影像延遲",
        "spaces.ops.lastFrameAgo": "上一張本機攝影機影像於 {seconds} 秒前取得",
        "spaces.ops.cameraDisconnected": "本機攝影機已中斷連線",
        "spaces.ops.cameraPermissionDenied": "本機攝影機權限遭拒",
        "spaces.ops.cameraStarting": "正在啟動本機攝影機…",
        "spaces.ops.cameraPrivacy": "攝影機影像只會留在此裝置上",
        "spaces.ops.cameraFrameAlt": "本機攝影機近即時影像",
    },
    "zh-CN": {
        "spaces.ops.live": "房间已连接",
        "spaces.ops.subtitle": "任务操作与证据",
        "spaces.ops.localNearRealtime": "本机摄像头 · 近实时 · {fps} FPS",
        "spaces.ops.cameraDelayed": "本机摄像头图像延迟",
        "spaces.ops.lastFrameAgo": "上一张本机摄像头图像于 {seconds} 秒前获取",
        "spaces.ops.cameraDisconnected": "本机摄像头已断开连接",
        "spaces.ops.cameraPermissionDenied": "本机摄像头权限被拒绝",
        "spaces.ops.cameraStarting": "正在启动本机摄像头…",
        "spaces.ops.cameraPrivacy": "摄像头图像只会留在此设备上",
        "spaces.ops.cameraFrameAlt": "本机摄像头近实时图像",
    },
}
LOCAL_CAMERA_KEYS = frozenset(LOCAL_CAMERA_VALUES["en"])
OPERATION_ROOM_CONTROL_VALUES = {
    "en": {
        "spaces.ops.available": "Available",
        "spaces.ops.configureSources": "Sources / Configure",
        "spaces.ops.management": "Management",
        "spaces.ops.missionInput": "Mission input (optional)",
        "spaces.ops.outputAmbiguous": "More than one output matches. Use the exact output label.",
        "spaces.ops.outputKind": "Kind",
        "spaces.ops.outputNoMatch": "No output matches that name.",
        "spaces.ops.outputSources": "Output sources",
        "spaces.ops.outputWall": "OUTPUT WALL",
        "spaces.ops.protocol": "Protocol",
        "spaces.ops.status": "Status",
    },
    "zh-TW": {
        "spaces.ops.available": "可用",
        "spaces.ops.configureSources": "來源 / 設定",
        "spaces.ops.management": "管理",
        "spaces.ops.missionInput": "任務輸入（選用）",
        "spaces.ops.outputAmbiguous": "有多個輸出符合。請使用完整輸出名稱。",
        "spaces.ops.outputKind": "類型",
        "spaces.ops.outputNoMatch": "找不到符合該名稱的輸出。",
        "spaces.ops.outputSources": "輸出來源",
        "spaces.ops.outputWall": "輸出牆",
        "spaces.ops.protocol": "協定",
        "spaces.ops.status": "狀態",
    },
    "zh-CN": {
        "spaces.ops.available": "可用",
        "spaces.ops.configureSources": "来源 / 配置",
        "spaces.ops.management": "管理",
        "spaces.ops.missionInput": "任务输入（可选）",
        "spaces.ops.outputAmbiguous": "有多个输出匹配。请使用完整输出名称。",
        "spaces.ops.outputKind": "类型",
        "spaces.ops.outputNoMatch": "找不到匹配该名称的输出。",
        "spaces.ops.outputSources": "输出来源",
        "spaces.ops.outputWall": "输出墙",
        "spaces.ops.protocol": "协议",
        "spaces.ops.status": "状态",
    },
}
OPERATION_ROOM_CONTROL_KEYS = frozenset(OPERATION_ROOM_CONTROL_VALUES["en"])
FALSE_CAMERA_LIVE_WORDING = re.compile(
    r"\b(?:continuous (?:video|stream)|live camera|camera (?:is )?live|"
    r"inference|recording)\b|"
    r"連續(?:視訊|串流)|即時攝影機|攝影機(?:正在)?直播|推論|錄影|"
    r"连续(?:视频|串流)|实时摄像头|摄像头(?:正在)?直播|推理|录像",
    re.IGNORECASE,
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


def _aggregate_dist(locale: str) -> dict[str, str]:
    """Load and flatten one generated repository aggregate bundle."""
    path = ROOT / "dist" / f"{locale}.json"
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


def test_open_operations_uses_pinned_product_copy_in_all_outputs() -> None:
    """Pin the accepted label across source, Cloud, and aggregate output."""
    key = "aiSpace.workspace.openOperations"
    for locale, expected in OPEN_OPERATIONS_VALUES.items():
        assert _source(locale)[key] == expected
        assert _dist(locale)[key] == expected
        assert _aggregate_dist(locale)[key] == expected


def test_local_camera_copy_is_truthful_owned_and_identical_in_all_outputs() -> None:
    """Pin reviewed local-camera truth across its sole source and outputs."""
    for locale, expected in LOCAL_CAMERA_VALUES.items():
        catalogs = _catalogs(locale)
        source = _source(locale)
        cloud_dist = _dist(locale)
        aggregate_dist = _aggregate_dist(locale)

        for key, value in expected.items():
            actual_owners = {
                catalog for catalog, values in catalogs.items() if key in values
            }
            assert actual_owners == {"spaceOperations.json"}, (
                locale,
                key,
                actual_owners,
            )
            assert value.strip()
            assert source[key] == value
            assert cloud_dist[key] == value
            assert aggregate_dist[key] == value
            assert not FALSE_CAMERA_LIVE_WORDING.search(value), (locale, key, value)

        room_connectivity = expected["spaces.ops.live"]
        assert room_connectivity == {
            "en": "Room connected",
            "zh-TW": "房間已連線",
            "zh-CN": "房间已连接",
        }[locale]
        assert not re.search(
            r"camera|攝影機|摄像头|live|即時|实时", room_connectivity, re.IGNORECASE
        ), (locale, room_connectivity)

    for key in LOCAL_CAMERA_KEYS:
        expected_placeholders = _placeholders(LOCAL_CAMERA_VALUES["en"][key])
        assert all(
            _placeholders(LOCAL_CAMERA_VALUES[locale][key]) == expected_placeholders
            for locale in LOCALES
        )


def test_operation_room_controls_are_reviewed_and_identical_in_all_outputs() -> None:
    """Keep visible output-wall controls localized through both bundles."""
    for locale, expected in OPERATION_ROOM_CONTROL_VALUES.items():
        catalogs = _catalogs(locale)
        source = _source(locale)
        cloud_dist = _dist(locale)
        aggregate_dist = _aggregate_dist(locale)

        for key, value in expected.items():
            owner = (
                "spaces.json"
                if key == "spaces.ops.management"
                else "spaceOperations.json"
            )
            actual_owners = {
                catalog
                for catalog, values in catalogs.items()
                if values.get(key, "").strip()
            }
            assert actual_owners == {owner}, (locale, key, actual_owners)
            assert value.strip()
            assert source[key] == value
            assert cloud_dist[key] == value
            assert aggregate_dist[key] == value

    for key in OPERATION_ROOM_CONTROL_KEYS:
        expected_placeholders = _placeholders(OPERATION_ROOM_CONTROL_VALUES["en"][key])
        assert all(
            _placeholders(OPERATION_ROOM_CONTROL_VALUES[locale][key])
            == expected_placeholders
            for locale in LOCALES
        )


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


def test_complete_cloud_manifest_survives_selective_build() -> None:
    """Seal the complete tracked Cloud manifest across a filtered build."""
    script = ROOT / "scripts" / "build-dist.py"
    spec = importlib.util.spec_from_file_location("cloud_manifest_build", script)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)

    locales = module.get_locales()
    locale_data = {
        locale: module.build_locale(locale, "cloud") for locale in locales
    }
    translated_counts = {
        locale: module.count_translated(locale, "cloud") for locale in locales
    }
    complete_manifest = module.build_manifest(locale_data, translated_counts)
    tracked_manifest = json.loads(
        (ROOT / "dist" / "cloud" / "manifest.json").read_text(encoding="utf-8")
    )
    assert complete_manifest == tracked_manifest

    english_total = locale_data["en"]["total_keys"]
    # +5: the operations room was rendering five sentences from code
    # fallbacks with no key behind them — `spaces.hud.capabilitiesPending`,
    # `spaces.hud.gatesUnenforceable`, `spaces.hud.evidencePending`,
    # `spaces.voice.micSendsAudio` and `spaces.ops.goalWaitingOnRegistry`.
    # +8: the war room could not answer `human.approval`. It is unschedulable
    # — no step is ever created to produce it — so it never arrived through a
    # step reporting an outcome, and a mission that required a supervisor's
    # approval was one nobody could complete. These are that panel's words.
    #
    # +31, and they arrived without a line here. `aiSpace.settings.voice*` —
    # the on-device wake-word panel — landed while the seal still said 12_082,
    # so this assertion has been failing on main since. It is written down now
    # rather than folded silently into the number below, because a seal whose
    # ledger skips an entry is a number nobody can check.
    # +1: `templateBuilder.header.saveOptions`, same commit range, same story.
    #
    # +1: `aiSpace.settings.voiceLocaleDevice`. The recognition locale stopped
    # being a free-text field and became a menu, and a menu needs a word for
    # its empty option. That option is the default and means "listen in the
    # language this machine is set to" -- which is the whole reason the field
    # is not hardcoded: the person who installs this on a second computer is
    # not necessarily the person who set the Space up, and may not speak the
    # same language.
    #
    # +6: `outcome.*` — the six words for how far a step's effect was followed.
    # Two of them are the reason this namespace exists rather than reusing
    # `status.*`: `dispatched` means an instruction left us and nobody
    # confirmed anything, and `indeterminate` means we cannot say. Neither is a
    # status, and rendering either as one is the thing the ladder exists to
    # stop.
    #
    # +8: `dashboardPage.devices.voice*` — the wake daemon on the devices page.
    # The daemon is one per machine and serves every AI Space, so its status is
    # a fact about the device, not about any Space; putting it here rather than
    # under `aiSpace.settings.*` is what keeps a user with many folders from
    # having the same machine-level control repeated into every one of them.
    # Four of the eight exist because presence alone cannot separate a daemon
    # that is running and armed nothing from one that is not running, nor a
    # daemon that stopped from one that was never installed — and the operator's
    # next move differs for each.
    #
    # +11: `aiSpace.resources.machines*`, `equipment*`, `infrastructure*` and
    # the two empty states — the Resources tab splitting one flat list into the
    # two relations it always held. A machine RUNS a workflow; a robot, a
    # camera or a lift is COMMANDED by one, and the tab showed both under one
    # heading with an OS string as the subtitle. `alsoEquipment` is the pair
    # that earns the split: the delivery robot is both, so it is labelled in
    # the machines list rather than made to choose.
    #
    # +2: `aiSpace.resources.inertMachines*`. The resource picker stopped
    # offering machines, because `device_ids` becomes `allowed_resources` and
    # is matched against an endpoint's `resource_id` -- which is never a
    # laptop, so a machine listed there opened nothing. A Space that already
    # listed one still does, and these two say so rather than hiding an entry
    # nobody could then remove.
    #
    # +5: `dashboardPage.devices.machines*` / `equipment*`. The same split on
    # the dashboard, which is where a robot or a camera is actually managed --
    # the AI Space tab only says which of them a Space may reach.
    #
    # -2: the two dashboard section hints. The heading and the count said it
    # already, and a line that restates its own heading is one more line
    # between the reader and the list.
    #
    # +1: `dashboardPage.devices.infrastructure`. The devices page folds away
    # rows that never said WHICH machine they are — a container the product
    # runs for you, a host that answered "localhost". The heading was written
    # against a key that was never added, so the fold rendered its own fallback
    # while the sync check called it an orphan.
    #
    # +5: `templateBuilder.aiChat.space*` / `*Tools`. The chat had no way to
    # say which AI Space it was bound to, let alone change it — the binding was
    # whichever folder happened to be selected on the page behind it. And a
    # Space can hold verified workflows while exposing none of them as callable
    # tools, which is the state that had the assistant answering "please
    # confirm what you want" with an empty registry.
    #
    # +5: `aiSpace.workspace.publishAsTool*`. A workflow becomes callable by
    # carrying an MCP trigger, and the only way to get one was to start a NEW
    # workflow from the MCP starter — so twenty verified workflows in a folder
    # could hand the assistant an empty registry, with the panel labelling them
    # "MCP" because it admitted on a tag the backend never reads.
    #
    # +7: `aiSpace.workspace.asksFirst*` / `runsDirectly*`. Whether a workflow
    # confirms before it runs was already a field on the trigger and was read
    # by nothing -- it defaulted to the string "workflow-defined", which looks
    # like a policy and means nobody chose. Unset now means ask, and this is
    # where an operator says otherwise.
    #
    # +1: `aiSpace.selection.elsewhere`. The selection panel's total now counts
    # the workflows the machine serving the turn was never offered -- ones whose
    # steps need motion, vision or sensing, so they belong to a robot, a camera
    # or another computer. That made "2 of 2" honest again by turning it into
    # "2 of 5", and on its own an honest number reads like an accusation against
    # the shortlist. This is the rest of the sentence.
    #
    # +23: workflow runner placement and War Room dispatch inventory. These
    # labels make the machine that RUNS a workflow an explicit relation rather
    # than conflating it with hardware or adapters the workflow COMMANDS. They
    # also distinguish automatic capability placement from a multi-machine
    # allowlist and expose refused workflows in the scheduler inventory.
    #
    # +2: `spaces.schedule.rejectedBy` / `holds`. The refusal an operator met
    # was "This Space cannot carry out that goal: plan_empty" -- never
    # translated, and untrue over a Space holding two working workflows the
    # goal had not named exactly. The second key is what it does hold, so the
    # next attempt is an exact match rather than a guess.
    #
    # +8: `aiSpace.resources.dispatchRules.*`. The War Room handed a goal to a
    # docker box that had not reported in for days and then waited for Start,
    # and the three Space policies that decide both had no screen. This is the
    # card that exposes them, on the Resources tab where the machines are.
    #
    # +4: two more dispatch rules. The War Room finished a job and left the
    # browser open; a failed step sat at "waiting" for good. Whether the machine
    # keeps the browser and whether the operator's AI may re-plan are the
    # Space's to set, and these are the words on those switches.
    #
    # +12: the dispatch rules that make the War Room a dispatcher and not a
    # runner. Whether a read-only workflow may be sent by name, whether a
    # machine's AI may assemble a missing tool, what the room does when a
    # machine reports a real block, and how many rounds and seconds a task
    # handed to a machine's AI may spend. All the Space's to set.
    #
    # +104: the War Room learned to speak to a first-time operator. A guided
    # rail (資源就緒 → 下達目標 → 看結果與決定), a welcome, navigation, and one
    # plain sentence per task and step in the operator's words; the section
    # titles that had fallen back to English get their Chinese at last.
    assert english_total == 12_317

    for locale in LOCALES:
        record = complete_manifest["locales"][locale]
        assert set(record) == {
            "name",
            "native",
            "region",
            "total_keys",
            "translated_keys",
            "completion",
            "files_merged",
        }
        assert record["total_keys"] <= english_total
        assert record["total_keys"] == locale_data[locale]["total_keys"]
        # 263, not 262: `outcome.json` is a new namespace rather than keys
        # added to an existing file. It is separate from `status.json` on
        # purpose -- a rung is not a status, and merging the two vocabularies
        # is what would let `dispatched` be read as a state a run passes
        # through rather than as "nobody confirmed anything".
        assert record["files_merged"] == 263

    with tempfile.TemporaryDirectory() as temp_dir:
        temp_root = Path(temp_dir)
        module.DIST_DIR = temp_root / "dist"
        module.REPOSITORY_MANIFEST = temp_root / "manifest.json"
        module.REPOSITORY_MANIFEST.write_text(
            (ROOT / "manifest.json").read_text(encoding="utf-8"), encoding="utf-8"
        )
        with contextlib.redirect_stdout(io.StringIO()):
            assert module.main(["--scope", "cloud", "--locale", "en"]) == 0

        filtered_manifest = json.loads(
            (module.DIST_DIR / "cloud" / "manifest.json").read_text(
                encoding="utf-8"
            )
        )
        assert filtered_manifest == complete_manifest
        assert (module.DIST_DIR / "cloud" / "en.json").is_file()
        assert not (module.DIST_DIR / "cloud" / "zh-TW.json").exists()
