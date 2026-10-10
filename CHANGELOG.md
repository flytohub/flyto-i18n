# Changelog

## 2026-10-10 — Clear private Space data after access revocation

- Added `spaces.ops.spaceAccessLost` to the canonical Cloud catalog in English, Traditional Chinese and Simplified Chinese. A Mission Station whose task or registry read loses authorization no longer keeps the previous user's mission, resource or evidence details visible.
- Rebuilt the tracked locale distributions from source. This is source/contract verification, not a production deployment or App/HMI implementation.
- Added `spaces.ops.send.goalOutcomeUnknown` in all three official Cloud locales: after an ambiguous task-submit timeout/server error, the operator is instructed to inspect existing tasks before attempting a new send. A definitive refusal keeps its existing wording. This prevents misleading "just retry" copy while the server-side durable submit-idempotency contract remains a separate P0.

## 2026-10-10 — i18n lint and official Cloud parity on the current main

- Brought the latest-main Ruff baseline from 221 issues to zero while keeping Python 3.9 support and preserving established hyphenated CLI names.
- Added the Editor saved/saving/unsaved states and Ollama/OpenAI-compatible source labels in English, Traditional Chinese and Simplified Chinese, increasing the cumulative English source-key count from 13,945 to 13,950.
- Regenerated the Cloud, aggregate and SEO manifests from source. Three official Cloud dictionaries now match approved Cloud runtime bundles exactly, without reviving historical or experimental UI labels.
- Main/remote branch cleanup requires verified fast-forward and audit evidence; this change does not claim production/CDN acceptance.

## 2026-10-09 — The Mission Station's simple view: receipt, progress, "Needs you"

- 12 cloud keys added in en, zh-TW and zh-CN for flyto-cloud's simple Mission
  Station view (other locales fall back to English): the Mission Receipt
  (`spaces.receipt.title`, `requested`, `observed`, `rule`, `executedBy`,
  `duration`, `viewEvidence`, `viewDecisions`, `outcomeUnknown`), the progress
  stepper label (`spaces.lifecycle.label`), the "?" hint button
  (`spaces.hud.moreInfo`) and the paused-for-reply line that now points at
  the "Needs you" card (`spaces.narrative.continuation.awaitingReplyNeedsYou`).
  The older `awaitingReply` key stays for released clients.
- The cumulative key count moves from 13,933 to 13,945.

## 2026-10-08 — What a self-hosted edition says about a feature it does not offer

- 4 cloud keys added in en, zh-TW and zh-CN for flyto-cloud's self-host
  WP15 (other locales fall back to English):
  `spaces.editionRefusal.edition_capability_absent` and
  `spaces.editionRefusal.unavailable_in_this_edition` (the two typed edition
  refusals a Space or device route answers with),
  `spaces.triggers.events.routeNotInEdition` (a subscription whose delivery
  route has no sender in this edition) and
  `spaces.triggers.events.refused.ROUTE_UNAVAILABLE_IN_EDITION` (saving one is
  refused for that reason).
- The cumulative key count moves from 13,929 to 13,933.

## 2026-10-07 — A step held until its computer guarantees one action per resource

- 1 cloud key added in en, zh-TW and zh-CN, copied verbatim from the
  flyto-cloud `claude/host-guarantees` bundled locales (other locales fall
  back to English): `spaces.ops.dispatchRefusal.host_single_actuation_required`,
  the Start refusal for a step whose job can send two actions to one resource
  at once while its computer's release does not guarantee one action at a time
  per resource.
- The cumulative key count moves from 13,922 to 13,923.

## 2026-10-07 — flyto-cloud sweep 1007: every key the code reads, none it dropped

- 428 cloud keys added in en and zh-TW (429 in zh-CN), copied verbatim from
  the flyto-cloud `claude/sweep-1007` bundled locales (other locales fall back
  to English). A new `cloud.messaging` category holds the messaging
  integration screen (`messaging.*`, including `messaging.testFailure.*`, one
  sentence per stable Test connection failure code); the rest extend
  existing categories: `accessibility.*`, `spaces.timeline.*`, `spaces.ops.*`, `spaces.guide.*`,
  `variables.credentialTypes.*`, `lineage.*`, `templateCollaboration.*`,
  `workflowCanvas.node.*`, `aiSpace.*`, `spaces.narrative.task.reviewRunning`
  (a done task whose independent review is still checking) and smaller
  screens.
- 50 en, 47 zh-TW and 115 zh-CN values replaced: English left in the Chinese
  catalogs and labels generated from their own keys.
- 5 zh-TW and zh-CN Discord/Slack/Telegram parameter descriptions in the
  modules scope (`locales/modules/*/notification.json`) say Bot instead of
  機器人, which flyto-cloud's check-i18n reads as equipment vocabulary.
- 75 keys removed from every locale, with no consumer left in any repository:
  71 key-shaped `admin.*` leaves, `dashboard.evolution.subtitle` and the
  interpolated fragments `scheduler.{lastRun,runs,times}`.
- The cumulative key count moves from 13,569 to 13,922.

## 2026-10-07 — Triggers & events: both directions, and a route nothing is sending

- 1 cloud key added and 2 changed in en, zh-TW and zh-CN, copied verbatim from
  the flyto-cloud bundled locales (other locales fall back to English):
  - `spaces.triggers.events.cloudWaiting` (new): a subscription sent by Cloud
    while no Cloud sender has asked for its events in the last 2 minutes.
  - `spaces.triggers.events.computerWaiting`: now says no computer of the Space
    has asked in the last 2 minutes and names the Desktop release
    (`{release}`) that sends them.
  - `spaces.triggers.description`: the tab now holds inbound triggers and
    event subscriptions, so its description names both.
- The cumulative key count moves from 13,568 to 13,569.

## 2026-10-07 — A Space's task lifecycle events sent to another system

- 62 cloud keys added in en, zh-TW and zh-CN, copied verbatim from the
  flyto-cloud `claude/space-events` bundled locales (other locales fall back
  to English):
  - `spaces.triggers.events.*`: event subscriptions (receiver URL, events,
    the route derived from the URL, the computer-route allowlist hint and the
    wait for a Desktop that can send, typed refusals, the secret shown once).
  - `spaces.triggers.delivery.*`: each delivery and its attempts, Redeliver,
    and the delivery states.
  - `spaces.tasks.{eventDelivered,eventDeliveries}`: the receipts line in a
    task's detail.
- The tab label and title (`aiSpace.workspace.tabs.triggers`,
  `spaces.triggers.title`) are the inbound-triggers copy's keys.
- The cumulative key count moves from 13,506 to 13,568.

## 2026-10-07 — Another system hands a Space a goal

- 56 cloud keys added in en, zh-TW and zh-CN, copied verbatim from the
  flyto-cloud space-triggers bundled locales (other locales fall back to English):
  - `spaces.triggers.*`: the Space dialog's Triggers & events tab, its inbound
    triggers (create, rotate, disable, delete, recent events) and the signing
    secret shown once.
  - `spaces.tasks.submittedBy.*` and `spaces.tasks.holdUnattended`: who
    submitted a task when it was not the operator, and why its step waits.
  - `aiSpace.workspace.tabs.triggers`, and
    `auth.oauthConsent.scopes.{spacesSubmit,spacesRead}.*` for the two new
    MCP scopes on the consent page.

## 2026-10-06 — A goal sent as the Space changed, and Send's refusals in operator words

- 31 cloud keys added in en, zh-TW and zh-CN, copied verbatim from the
  flyto-cloud bundled locales (other locales fall back to English):
  - `spaces.registryChange.*`: what changed in a Space between the page's read
    and a goal (resource added/removed/renamed, simulation vs physical
    equipment, revoked/restored, command added/removed/changed), with the
    summary shown when the goal was therefore not started.
  - `spaces.narrative.task.registryMoved`, `spaces.narrative.problem.registry_snapshot_stale`,
    `spaces.timeline.{stage,plain}.registry_moved`.
  - `spaces.ops.send.*`: every refusal the Mission Station's Send and Test raise
    (the raw English 「No command has that exact label」 among them).

## 2026-10-06 — Reconnect for equipment a computer no longer serves, refused Space reads

- 4 cloud keys added in en, zh-TW and zh-CN, copied verbatim from the
  flyto-cloud bundled locales (other locales fall back to English):
  `spaces.equipment.connection.notServed` and
  `spaces.readFailure.{signedOut,forbidden,notFound}`.

## 2026-10-06 — Equipment presence states

- 4 cloud keys added in en, zh-TW and zh-CN, copied verbatim from the
  flyto-cloud bundled locales (other locales fall back to English):
  `spaces.resources.presence.{unreachable,unreported,unreportedHint,dormant}`.

## 2026-10-06 — Closure 1006b: evidence time, provider-neutral names, retired copy

- 30 cloud keys added in en, zh-TW and zh-CN, copied verbatim from the
  flyto-cloud bundled locales (other locales fall back to English, as with the
  earlier Mission Station copy):
  - Evidence time on the task timeline: `spaces.timeline.stage.{evidence_admission,evidence_not_current}`,
    `spaces.timeline.evidence.{admitted,missing,notCurrent,refused}` and
    `spaces.timeline.evidence.reason.{expired,undated,historical_kind,undeclared_kind,observed_after_use,no_clock,not_recorded}`.
  - Skipped steps: `spaces.narrative.step.{skipped,skippedUnobserved}`, `spaces.narrative.stepState.skipped`.
  - `spaces.narrative.adapterReason.resourceBusy`.
  - Provider-neutral renames: `orchestrator.robots.*` -> `orchestrator.runners.*`,
    `orchestrator.stats.totalRobots` -> `totalRunners`, `enterprise.robotsOnline` -> `runnersOnline`,
    `spaces.capability.family.robot` -> `equipment`,
    `spaces.narrative.adapterReason.travelled` -> `stoppedAfter`. Other locales
    drop the old robot-named key and fall back to English.
- 10 values reworded to match flyto-cloud: `orchestrator.register.{title,name,namePlaceholder}`
  (runner, not robot), `aiSpace.resources.coveragePlaceholder` (`zone-b, floor-2`),
  `spaces.hud.sweep.{before,after}` (range scan, not a sensor brand) and
  `spaces.narrative.adapterReason.{localizationError,noEscapeRoom,nearest,nearestSide}`.
  Stale translations of these in other locales are removed so they fall back
  to the new English.
- 96 cloud keys removed from every locale, with no consumer left in flyto-cloud
  or any other workspace repository: `aiSpace.delivery.*` (retired
  guarded-delivery panel), `aiSpace.controls.runtime*`, `spaces.kind.robot`,
  `spaces.hud.evidenceKind.robot.arrival` and the renamed keys above.
  `locales/landing/` copies of the orchestrator and enterprise keys are untouched.

## 2026-10-06 — Readable adapter failure copy

- 16 cloud keys flyto-cloud now uses, in en, zh-TW and zh-CN (other locales
  fall back to English, as with the earlier Mission Station copy):
  - Why equipment stopped, in the operator's words:
    `spaces.narrative.adapterReason.{noPath,obstacleBlocked,sensorStale,timeout,localizationError,noProgress,abortedByServer,cancelled,noEscapeRoom}`.
  - Stop confirmation: `spaces.narrative.adapterReason.{safeStopUnconfirmed,stoppedSafely,stopUnconfirmed}`.
  - What it did before stopping: `spaces.narrative.adapterReason.{travelled,nearestSide,nearest}`.
  - The collapsed raw-detail disclosure: `spaces.narrative.technicalDetails`.

## 2026-10-06 — Mission Station replans, equipment Reconnect and device presence copy

- 101 cloud keys flyto-cloud now uses, in en, zh-TW and zh-CN (other locales
  fall back to English, as with the earlier Mission Station copy):
  - AI routing refusals in the operator's words: `spaces.narrative.routing.*`,
    `spaces.narrative.need.*`, `spaces.narrative.result.*`,
    `spaces.narrative.task.routeRefused`, and the timeline stages
    `spaces.timeline.{stage,plain}.{routing_refused,goal_contract_frozen,follows}`.
  - Follow-up goals: `spaces.voice.follow*` and `spaces.followLinks.*`.
  - Reserved tool names: `aiSpace.selection.reservedTitle` and
    `aiSpace.selection.reservedBy.*`.
  - Device presence and removal: `dashboardPage.devices.presence.*` and
    `dashboardPage.devices.confirmRemoveMessage`.
  - Replans in words: `spaces.hud.replanTrigger.*`, `spaces.hud.replanPlanner.*`,
    `spaces.hud.replanSuperseded.recovery_rule` and the plan-record labels.
  - Equipment Reconnect: `spaces.equipment.connection.*` (states and errors).
  - Adapter refusal reasons: `spaces.narrative.adapterReason.*`,
    `spaces.narrative.side.*`, `spaces.narrative.sideName.*`.

## 2026-10-04 — Project wizard catalog fallback copy

- Added `code.projects.wizard.catalogFallback` to canonical Code locale source.
- Rebuilt Code and aggregate distributions so flyto-code can pin a source-owned
  translation instead of carrying an i18n orphan exception.

## 2026-10-04 — Module catalog names for every module

- `code.projects.feature.{core,coreDesc,vrm,vrmDesc,supplyChain,supplyChainDesc}`
  in en, zh-TW and zh-CN. flyto-engine's module catalog now requires a
  `title_key` / `description_key` on every module; these were the six the
  catalog named with no copy here, which is why Warroom showed raw module keys.
- Japanese copy for every catalog `title_key` / `description_key`. `ja` is a
  primary locale in flyto-engine's i18n check, so it is part of the contract.
- `code.projects.feature.{thirdPartyMonitoring,codeSecurityAutofix}` (+ `Desc`)
  in en, zh-TW, zh-CN and ja, matching the catalog `display_name` /
  `description` of `continuous_monitoring` and `autofix`.
- Removed `code.projects.feature.supply` / `supplyDesc` from every locale. No
  catalog module or consumer referenced it, and it described vendor risk under
  a "Supply Chain" name, beside the catalog's own VRM and supply-chain copy.
- `tests/test_module_catalog_copy.py` reads the engine catalog itself and fails
  when any of its keys has no copy in en, zh-TW, zh-CN or ja. It no longer
  skips in CI: `validate.yml` sparse-checks out flyto-engine's catalog and sets
  `FLYTO_ENGINE_CATALOG`, and with `CI=true` a missing catalog fails the run.
  Agent worktrees find the workspace's `flyto-engine` clone through any
  ancestor directory. The English-derived pair check is gone; the catalog is
  the only source of which keys must exist.

## 2026-10-04 — Module Marketplace (模組商城)

- New `modulePacks.json` namespace (165 keys with `plugins.tabs.modulePacks`)
  in en, zh-TW and zh-CN for flyto-cloud `claude/module-marketplace`: browse
  and search packs, install on this computer, publish a private or public
  pack, Ed25519 signing keys, the administrator review queue, and one
  sentence for every stable refusal code the marketplace and the Desktop
  installer return. Other locales carry the keys empty, as usual.
- No price, checkout, entitlement or trial wording: the marketplace has none.
- The Cloud seal is 13,290 (13,152 when this copy was written alone) and the merged file count 264.

## 2026-10-04 — Workflows bind to capabilities, not to a resource

- 42 new Cloud keys (en, zh-TW, zh-CN) for flyto-cloud
  `claude/capability-binding`: the Space settings overview of resources,
  module packs and capabilities (`aiSpace.capabilityOverview.*`), what each
  workflow needs and which resources match, the optional limits on automatic
  choice (only simulation resources, only these resources),
  `aiSpace.resources.addToSpace`, and two refusal words on candidate chips
  (`spaces.hud.refusal.outside_resource_constraint`, `.simulation_only`).
- Five values reworded so the Resources tab no longer asks the operator to
  pick an adapter for workflows: `aiSpace.workspace.resourceRegistry`
  (Resources in this Space / 此 Space 的資源), `resourceRegistryHint`,
  `allowedInSpace`, `aiSpace.resources.equipmentHint`, and
  `aiSpace.resources.noPolicyHint` (a workflow with no policy now uses its own
  declared capabilities instead of failing closed). Domain-neutral wording.
- The Cloud seal is re-pinned at 13,125 (after the provider-neutral copy).

## 2026-10-04 — Mission Station demo-path polish

- 82 new Cloud keys (en, zh-TW, zh-CN) for flyto-cloud `claude/demo-polish`:
  the result check's plain name (`spaces.ops.verificationLoopPlain`), what
  each decision-timeline entry means in the operator's words
  (`spaces.timeline.plain.*`), a machine's question read as a wait rather
  than a failure (`spaces.timeline.view.*`), Yes/No quick replies and a
  quieter secrets hint (`spaces.schedule.*`), the error codes a computer's AI
  reports (`spaces.narrative.errorCode.*`), capability words in place of ids
  (`spaces.capability.*`, domain-neutral), the top bar's loading state and
  labelled counts, acceptance-check labels, and the explicit desktop-alert
  buttons (`spaces.ops.desktopAlerts`, `notifications.desktopAlerts*`).
- `spaces.history.group.*` were empty placeholders in every locale, which the
  Cloud build drops, so the history filters read All / Running / Done in
  English. They now have words. `spaces.timeline.readAll` reads View all /
  查看全部.
- `spaces.capability.sensing_map` and `spaces.capability.family.sensing`, so a
  map step reads as a word instead of the generic "A capability of this
  Space" (flyto-cloud #470 review finding 5).
- Pinned counts re-pinned: the verification-loop key set is 42 and the Cloud
  seal is 13,076.

## 2026-10-03 — Second UI sweep: editor, chat, navigation, settings, Mission Station

- 272 new Cloud keys (en, zh-TW, zh-CN) for flyto-cloud `claude/ui-sweep-2`:
  the workflow editor, the global AI chat and direct messages, navigation and
  global pages, account settings and billing, Mission Station, and the
  execution detail page. Each one replaces an English fallback a component
  already passed to `t()`.
- 167 existing values corrected: users read "workflow / 工作流程", never
  模板/範本; Mission Station replaces "room"; the zh-TW confirm verb is 啟動.
  `cloud.`-prefixed overrides of the same keys in `template.json`,
  `issues.json` and `settings.json` carry the same words.
- The "Warroom" product name is shown as "Code security scan / 程式碼安全掃描 /
  代码安全扫描" in `myTemplates.warroomImport.*` and the six
  `modules.warroom.*.label` values, so it is not confused with the reserved
  War Room. Key names and module ids are unchanged.
- Pinned test values re-pinned for those changes; the Cloud seal is 12,987.

## 2026-10-02 — Ratings Tree access-state labels

- Added canonical Code keys for `Subscription`, `Access`, and `Control` on the
  company Ratings Tree.
- English, Traditional Chinese, and Simplified Chinese are reviewed; other
  locales retain explicit fallback values until translated.
- Rebuilt `dist/code` and aggregate distributions so flyto-code's i18n sync
  gate no longer reports these Ratings Tree labels as orphaned keys.

## 2026-10-02 — A robot turn is said in radians

- `spaces.hud.sweep.turned` (en, zh-TW, zh-CN): the robot motion view says
  how far a turn went against what was asked, instead of "moved 0.000 m".

## 2026-10-02 — The robot motion view on the output wall

- `spaces.hud.sweep.*` (en, zh-TW, zh-CN): the picture of a robot motion says
  what the LiDAR saw before moving and once stopped, where the robot was asked
  to go, the safety distance, and how far it went against what was asked, in
  the page language rather than the backend's English sentence.

## 2026-10-02 — Mission Station records in words, and the Agents tab

- The Mission Station names what it used to print as identifiers, keyed by the
  identifier the backend serves:
  - assignment gates and their skip reasons, for example 租用 · 這個 Space 的規則沒有開啟這項檢查;
  - refusal chips on rejected candidates and the two order bases;
  - evidence states, reasons with their arithmetic, what a waiting item waits
    on, and the three conclusions;
  - the decision source on each timeline badge.
- `spaces.timeline.originalNote`: the full decision record says its detail
  lines are the system's original sentences.
- The AI Space Agents tab (`aiSpace.agents.*`, `aiSpace.workspace.tabs.agents`)
  is translated. It reuses the agent hub's role names.
- `aiSpace.resources.inertMachines*` explains why a computer does not belong
  in the adapter list and how to remove it.
- `templateToolbar.search*` says workflows rather than templates.

## 2026-10-02 — Demo-path copy: no rooms, no mixed-language labels

- The Mission Station's own copy no longer calls it a "room". The help button,
  the connection badge, the information panel and one failure reason now say
  Mission Station / 任務站點 / 任务站点.
- The Mission cards switch reads **任務卡 / 任务卡 / Mission cards**, not
  "任務卡 Adapter". Its setup dialog is **Mission cards setup**, and it asks for
  a **zone kind / 區域類型 / 区域类型** instead of a "station kind", which read as
  a kind of Mission Station.
- The Mission Station information dialog labels its facts Connection / 連線,
  Open tasks / 進行中任務 and Space ID.
- The Warroom module labels in zh-TW and zh-CN say "Warroom", like their
  English labels, instead of 戰情室 / 战情室.
- `templateFolders.allTemplates` is "All workflows / 所有工作流程 / 所有工作流",
  matching the page it labels.
- New key `aiSpace.resources.machineBindings.noRunnableWorkflows`: a machine
  card says that the Space's workflows cannot run there, instead of asking for
  a workflow when the Space already has one.

## 2026-10-02 — Each Space has a Mission Station; War Room is reserved

- Each Space's control room is now **Mission Station / 任務站點 / 任务站点**
  (78 strings, which said War Room / 戰情室 / 战情室 after #162). "War Room" is
  reserved for the planned layer above all Spaces and no longer appears in the
  Cloud UI.
- The legacy Mission Stations feature (venue calibration and judge-card tasks)
  is now **Mission cards / 任務卡 / 任务卡**, so it no longer shares a name with
  the room.
- The Warroom recipe import reads "Warroom" in zh-TW and zh-CN as well, where it
  used to say 戰情室 / 战情室.
- Tests pinning the old copy are updated, including the zh-TW and zh-CN runtime
  value digests.

## 2026-10-02 — One name for the War Room, one for Mission Stations

- The Space's control room is called **War Room / 戰情室 / 战情室** everywhere.
  zh-TW used 作戰室 (25 strings) and zh-CN used 作战室 for the same room. English
  also called it "Operations room" or "Operations Room" in three places.
- The Space settings tab that configures Mission Stations, and the Mission
  Stations panel title, are now **Mission Stations / 任務站點 / 任务站点**.
  They were "AI War Room" and "AI Workflow War Room", which collided with the
  room itself.
- `test_cloud_runtime_cumulative_keys.py`: the English key count is updated
  for the 13 Agent Hub keys added in #160, which had left it failing on `main`.

## 2026-10-01 — War Room Agent Hub copy

- Added source-owned Cloud translations for Planner, Recovery, Reviewer,
  agent phases and statuses, and the read-only execution-authority disclosure
  used by the Operations Room Agent Hub.
- English and both Chinese locales are reviewed; the remaining Cloud locales
  use explicit English fallback values until native review.
- Rebuilt Cloud and aggregate runtime bundles from the canonical catalogs.

## 2026-10-01 — SPM material-change activity copy

- Added reviewed English, Traditional Chinese, and Simplified Chinese labels
  for material-change counts and high-impact materiality review notices in the
  Exposure activity feed.
- Rebuilt tracked Code and aggregate CDN bundles so Flyto2 Code CI no longer
  treats the new activity keys as orphaned.

## 2026-10-01 — SPM attribution evidence

- Added source-owned Code labels for optional Footprint attribution evidence in
  Posture Quality: confirmed entities, relationship count, and Engine-authored
  entity/relationship confidence summaries.
- Reviewed English, Traditional Chinese, Simplified Chinese, and Japanese
  wording; other Code locales use deterministic English fallback for the new
  keys.
- Rebuilt tracked Code and aggregate CDN bundles.

## 2026-10-01 — CI import-path hardening

- Made the repository `scripts` directory an explicit Python package so clean
  CI environments cannot resolve a third-party `scripts` package before
  `scripts.validate`.
- Load the validation regression target by repository path so pytest remains
  deterministic even when the runner has already imported another `scripts`
  module.

## 2026-09-30 — SPM improvement loop

- Added Flyto2 Code strings for the first-party Posture improvement loop and
  canonical external-rating forecast.
- Added reviewed `en`, `zh-TW`, `zh-CN`, and `ja` copy and rebuilt CDN output.

## 2026-09-29 — Posture English copy and company Ratings Tree

- Replaced literal Unicode escape strings in English Posture labels with reviewed English copy.
- Added Domain detail diagnostics/readiness labels in English and Traditional Chinese.
- Added company-hierarchy Ratings Tree labels and kept them semantically separate from the SPM Rating Breakdown risk-vector explanation.

## 2026-09-28 — SPM rating explanation copy

- Added source-owned Rating Tree labels for SPM rating, risk vectors, findings, latest score change and remediation projections.
- Added reviewed English and Traditional Chinese wording for unavailable states and the domain-level penalty boundary.
- Rebuilt tracked Code and aggregate bundles; no consumer-side scoring logic or authority changed.

## 2026-09-24 — SPM infrastructure attribution copy

- Added source-owned Code labels for Domain, IP, CIDR and ASN attribution controls, authority evidence, end-attribution and review-required removal states.
- English, Traditional Chinese and Simplified Chinese are reviewed; other Code locales use deterministic English fallback for the new keys.
- Wording preserves the SPM authority boundary: independent ownership evidence cannot be represented as directly removable by an operator.

## 2026-09-24 — Posture operator telemetry labels

- Added the six missing Posture Overview telemetry/scope labels to the canonical Code catalogs.
- Reviewed English, Traditional Chinese, and Simplified Chinese copy; other locales use explicit English fallback.
- Rebuilt tracked Code and aggregate bundles, removing the orphan-key CI failure in flyto-code.

## 2026-09-21 — External Intelligence quality and learning copy

- Added 23 source-owned labels for the External Intelligence Quality / Learning workspace.
- Reviewed English, Traditional Chinese and Simplified Chinese distinguish reviewed precision and labeled recall from population-wide accuracy claims.
- Regenerated Code and aggregate distributions; other Code locales use explicit English fallback for the additive keys.

## 2026-09-21 — Report and assessment library copy

- Added source-owned Report Library, Assessment Library and CTEM compliance-dialog copy for Code.
- English, Traditional Chinese and Simplified Chinese are reviewed; other Code locales use explicit English fallback for the additive keys.
- Assessment language preserves the Engine truth boundary: missing evidence remains not assessed and is never labelled as a pass.
- Rebuilt tracked Code and aggregate distributions for all supported Code locales.
- Added the missing Compliance Review labels and status guidance so the new report/assessment release no longer depends on orphaned runtime keys.

## 2026-09-20 — Historical execution and learning result labels

- Label retained output from an earlier execution separately from the current
  task status, with reviewed English and Chinese copy and generated bundles.
- Distinguish a saved reusable workflow from an execution whose procedure was
  not saved, independently of the execution's verified completion status.

## 2026-09-19 — Approved CTEM design

Add source-owned English and Traditional Chinese labels for the approved CTEM layout, missing lifecycle statistics, evidence dialogs and linked-alert tools. Other locales explicitly use English fallback for these new keys. Existing translations remain unchanged.

## CTEM action queue copy — 2026-09-19

Add source-owned queue purpose, loaded-window counts, priority context, review dialogs and explicit remediation-versus-verification language. English and Traditional Chinese are reviewed; other locales use explicit English fallback. This does not establish a frontend deployment.


## 2026-09-17 — Audit review and score history

- Add English and Traditional Chinese audit-review, report-scope and recorded-score history copy.
- Regenerate the canonical distribution; no existing keys are replaced.

## 2026-09-06 — Clear verification and priority states

- Distinguished verified target ownership from verified Red Team results in
  English and Traditional Chinese. Ready ownership is not attack evidence.
- Shortened the priority window disclosure and restored its missing
  Traditional Chinese translation, preserving both count placeholders.

## 2026-09-06 — Adoption research workspace copy

- Added source-owned research navigation, exact-commit case inputs, evidence
  provenance, advisory-candidate, AI hypothesis and report/disclosure wording.
- Kept evidence assertions distinct from executing repository code.
- Generated Code and aggregate bundles for all supported Code locales.

## 2026-09-04 — AI Space runner placement and War Room dispatch copy

- Added reviewed English, Traditional Chinese, and Simplified Chinese labels
  for automatic or multi-machine workflow placement, runner availability,
  save states, and the War Room's dispatchable-workflow inventory.
- Kept workflow runners separate from hardware and adapter resources, and made
  the copy explicit that War Room schedules while AI Space executes locally.
- Rebuilt Cloud and aggregate runtime bundles and added source-ownership,
  placeholder-parity, and generated-bundle regression coverage.

## 2026-08-26 — Code manager key prefix and Vendor Posture repair

- Removed the erroneous leading `code.` from exactly the 131 Code manager
  source keys introduced by `7df5f69f0` in all 16 locales, preserving every
  locale-specific value and leaving unrelated historical keys unchanged.
- Added the 32 current SPM, CM, and TPRM Vendor Posture UI keys with reviewed
  English, Traditional Chinese, and Simplified Chinese copy; other locales use
  the established deterministic English fallback.
- Rebuilt the tracked Code and aggregate bundles and catalog manifests without
  changing the orphan allowlist.

## 2026-08-26 — Pytest tmpdir security update

- Upgraded pytest to 9.0.3 and aligned CI with the patched pytest 9 release
  line, closing GHSA-6w46-j5rx-g56g.

## 2026-08-26 — Code manager catalog keys restored

- Added the complete 131-key Code catalog delta from the intended manager-
  surface change to all 16 supported Code locales. A later repair recorded
  above removed the accidental extra source-level `code.` prefix while
  preserving these values.
- Restored Agent Firewall manager rails and inputs, CTEM sample disclosure,
  domain-manager labels, repository connection errors, and the remaining Code
  surface copy carried by that additive delta.
- Regenerated the tracked Code and aggregate distribution bundles and
  manifests from the source catalogs.

## 2026-08-24 — Every current Core module has an official label

- Added the 42 missing Core registry label keys to the category-owned English,
  Traditional Chinese, and Simplified Chinese module catalogs.
- Added exact source-ownership and generated Cloud-bundle coverage so the node
  picker and workflow canvas can share one resolver without English leaks.
- Rebuilt aggregate, Flow, and Cloud distribution bundles.
- Removed duplicate source ownership for `spaces.ops.management` and
  `spaces.ops.noReplans`, refreshed the pinned Cloud inventory for the new
  module catalogs, and made pytest the repository test runner so function-style
  contracts cannot be silently skipped by unittest discovery.

## 2026-08-23 — Space Operations exposes a verification loop

- Added reviewed English, Traditional Chinese, and Simplified Chinese copy for
  acceptance, execution, evidence, verdict, and the backend-selected next action.
- Kept completed-but-unverified missions distinct from verified outcomes in
  source catalogs and generated Cloud bundles.
- Added the missing management and no-replan labels so Cloud's orphan-key scan
  closes without frontend-only fallback copy.

## 2026-08-21 — AI Space device pairing is fully localized

- The bound-resource heading, pairing action, and complete pairing-code dialog
  now have reviewed English, Traditional Chinese, and Simplified Chinese copy.
- Removed stale empty duplicates that overrode the reviewed operations-room
  translations during bundle generation.

## 2026-08-22 — Operations Room control copy is source-owned

- Added reviewed English, Traditional Chinese, and Simplified Chinese copy for
  the 10 output-wall and mission-entry keys previously present only in Flyto2
  Cloud's bundled baseline.
- Filled the `spaces.ops.management` source value in the same three locales and
  added source-to-Cloud-to-aggregate regression coverage for the complete
  11-key control contract.

## 2026-08-18 — Telling a quiet machine from an idle room

- `spaces.ops.noSignalYet` and `spaces.ops.noSignalYetHint` in all sixteen
  cloud locales.
- The operations room's stage had one idle message — "Standby / Waiting for the
  next mission" — for two different facts, so a screenshot with a task running,
  two robots on the wall and steps in flight still had the largest panel on
  screen announcing that nothing was happening.

## 2026-08-18 — The refused-feed label

- `spaces.ops.refused` in all sixteen cloud locales.
- The operations room already renders it — `wt('refused', 'Feed refused')` — but
  it had only ever been written into cloud's bundled baseline, never landed
  here. Cloud's sync check reports it as a deleted key, and the orphan scan
  does not catch it because `wt()` builds the key from a prefix at runtime.

## 2026-08-18 — The operations room's deadline and evidence producer

- Four `spaces.hud.*` keys in all sixteen cloud locales: `deadline`,
  `projectedPastDeadline`, `provenBy` and `showOnWall`.
- They belong to the war room saying the time a task was promised in, and
  naming the machine that produced a piece of evidence. Cloud's `i18n Sync
  Check` fails on a key referenced in code that does not exist here, which is
  the right way round: the vocabulary lands upstream first.

## Unreleased

### Changed

- Repositioned the public README, package metadata, docs index, and project
  memory around one role: fixing a translation once and sharing it across every
  Flyto2 product, docs, and website surface. The README now demonstrates a real
  locale-source edit, strict validation, and distribution rebuild before
  architecture and ecosystem detail. Removed unrelated AI/framework discovery
  keywords and refreshed stale README coverage values from the tracked manifest.
- Replaced ambiguous War Room live-camera wording with reviewed local,
  near-real-time image copy in English, Traditional Chinese, and Simplified
  Chinese. Room connection, delayed images, last-image age, disconnection,
  permission denial, startup, on-device privacy, and image alt text are now
  explicit and synchronized into Cloud and aggregate runtime bundles.
- Corrected `aiSpace.workspace.openOperations` to the accepted Cloud UI labels
  `Operations room`, `作戰室`, and `作战室`, with exact source-to-runtime bundle
  regression coverage for all three official locales.

### Added

- Added 19 catalog-owned AI Space identity and local-voice settings keys to all
  16 Cloud locales and regenerated Cloud and aggregate runtime bundles. The
  copy preserves display-name and alias limits, device-local wake-word
  detection, routing-only behavior, and the permission and approval boundary.
- Added focused regression coverage for exact reviewed English and Chinese
  values, the exact settings key set, unique source ownership across locale
  catalogs, non-empty native locale copy, rejection of full English fallback,
  and parity with both generated distribution shapes.
- Extended the cumulative Cloud runtime regression to pin the War Room camera
  values, unique source ownership, placeholder parity, non-empty
  source-to-Cloud-to-aggregate equality, and absence of false continuous-video,
  live-camera, inference, or recording claims.
- Added the reviewed 134-key Cloud runtime migration for English, Traditional
  Chinese, and Simplified Chinese: 59 `aiSpace.*`, 25 `myTemplates.*`, and 50
  `templateBuilder.missionSetup.*` keys. Added `accessibility.modal` in the same
  three locales and focused coverage for exact key/count contracts, non-empty
  locale and placeholder parity, deterministic source-to-dist union, and
  preservation of the existing 21 Space Operations keys.

- Added four fail-closed keys for Cloud deployments that do not serve the newer
  Space endpoints, in reviewed English, Traditional Chinese, and Simplified
  Chinese. `aiSpace.workspace.resourceInventoryUnavailable` and its `…Hint`
  explain that the registered-device inventory endpoint is missing, that already
  selected workflows stay configured, and that the device list cannot be
  refreshed until Cloud is upgraded. `spaces.draw.catalogUnavailable` and its
  `…Hint` explain that the mission-card catalog endpoint is missing and that
  creating a mission goal stays locked until Cloud is upgraded. None of the four
  values uses an interpolation placeholder, so placeholder parity holds by
  construction.
- Added 21 `spaces.draw.*` and `spaces.voice.*` keys to the Cloud
  `spaceOperations` catalog so the live Space operations surface can localize
  zone drawing (title, explanation, loading, retry, empty, zone, objective,
  objective picker, resource requirement, incomplete state) and voice goal
  entry (listen toggles, goal label, send, both composer placeholders,
  policy-blocked state, listening state, no-speech, and the two microphone
  failures). English, Traditional Chinese, and Simplified Chinese are reviewed
  and carry no interpolation placeholders, so placeholder parity holds.
- Added `aiSpace.workspace.openOperations` to the Cloud AI Space catalog in
  English, Traditional Chinese, and Simplified Chinese for the entry point that
  opens the Space operations console from the AI Space workspace.
- Added catalog-owned report export format copy for all 16 Code locales,
  including reviewed English, Traditional Chinese, and Simplified Chinese
  labels for the format selector and PowerPoint `.pptx` option.
- Added source/generated-bundle regression coverage requiring both report
  export keys to remain present and non-empty in every supported Code locale.
- Added an i18n-owned hourly and manual Flyto2 Cloud key pull. It validates the
  complete repository and opens a review-required synchronization PR without
  copying private Cloud source or requiring Cloud to hold an i18n write token.

- Added non-empty browser-engine provisioning and connector-category runtime
  copy to every Cloud locale, with source and generated-bundle contract tests
  that reject missing or empty values.
- Added 33 `code.attackValidation.benchmark.*` keys for the measurable
  effectiveness command center: authorized outcome funnel, time-to-proof
  percentiles, Red Team/Pulse/BYO and active-mode coverage, all seven proof
  stages, and explicit remediation/retest gap queues. English, Traditional
  Chinese, and Simplified Chinese are reviewed; the other 13 Code locales
  retain the established deterministic runtime fallback contract.
- Added regression coverage requiring the benchmark v2 catalog in every source
  and generated Code locale, with reviewed primary-locale copy pins for the
  outcome funnel, effectiveness coverage, and tamper-evident audit stage.
- Added 37 `code.attackValidation.command.*` keys for the campaign-first Red
  Team, Pulse, and BYO decision surface across all 16 Code locales. English,
  Traditional Chinese, and Simplified Chinese are reviewed; the remaining 13
  locales use deterministic English fallbacks.
- Added regression coverage that requires every campaign command-center key in
  source and generated Code bundles and pins the three reviewed locale titles
  and subtitles.
- Added five `code.scoring.*` labels for cloud posture, container images, and
  MCP Runtime Guardian across all 16 Code locales, with regression coverage
  for the Engine-aligned scoring surface.
- Added 65 `code.attackValidation.*` keys for proof-of-control, proof-pack
  eligibility, tenant-local benchmark accounting, exact allowlists,
  tamper-evident audit state, three-level hard budgets, cost settlement, and
  emergency-stop controls. English, Traditional Chinese, and Simplified
  Chinese are reviewed; all Code locales and generated distributions are
  synchronized.
- Added the canonical 286-key `cloud.aiSpace` catalog with reviewed English,
  Traditional Chinese, and Simplified Chinese copy, plus regression coverage
  requiring locale parity and non-empty official translations.
- Added reviewed AI Space endpoint and workflow-routing copy for arbitrary
  adapter, capability, Space, permission, freshness, priority, confirmation,
  lease, and automatic/custom policy settings without exposing raw JSON.
- Added the `code.attackValidation.*` catalog for the Red Team + Pulse + BYO
  authorized attack-validation closure. English and Traditional Chinese are
  reviewed; all 16 Code locales carry a deterministic fallback catalog.
- Added attack-effectiveness denominators, evidence freshness/provenance,
  Red Team/Pulse/BYO source filters, and tenant-owned dark-web canary guidance
  to the attack-validation catalog; English, Traditional Chinese, and
  Simplified Chinese are reviewed and all 16 Code locales remain synchronized.
- Added localized copy for confidence bands, validation modes, owned/canary
  safety scope, error/empty/retry states, and remediation/retest progress.
- Added regression coverage that requires the full catalog in every Code
  locale and pins the reviewed English and Traditional Chinese safety boundary.
- Added English and Traditional Chinese copy plus synchronized locale fallbacks
  for credential-free public repository onboarding in Warroom CE.
- Added a shared MCP Studio catalog for English, Traditional Chinese, and
  Simplified Chinese, including navigation, tools, connection, audit, status,
  action, and accessibility copy.
- Added regression coverage that keeps `mcpStudio.json` in the self-hosted Flow
  distribution scope.
- Added localized light, dark, and system-following appearance labels for all
  16 `flyto-code` locales used by Warroom CE.
- Added English, Traditional Chinese, and Simplified Chinese copy for the
  one-time Warroom CE administrator setup flow, with synchronized placeholders
  in every supported code locale.
- Added the Flyto2 Warroom CE deterministic product-loop copy for all supported
  `flyto-code` locale catalogs, including loading, error, evidence, surface,
  metric, safe-mode, and Enterprise-boundary states.
- Added validation coverage that prevents the critical
  `code.communityLoop.*` namespace from regressing to empty Traditional or
  Simplified Chinese values.
- Added package metadata, backlink fields, and SEO-focused keywords so the
  i18n source is clearer on GitHub and package indexes.
- Added `scripts/i18n_contract.py` as the shared locale/project metadata source
  for build, validation, coverage, and add-locale tooling.
- Added `seo/public-surfaces.json` and generated `dist/seo-manifest.json` for
  landing/docs/blog multilingual SEO, `hreflang`, sitemap, `og_locale`, and
  long-tail keyword planning.
- Added unittest coverage for the SEO manifest builder and wired unittest
  discovery into `npm test` / `make test`.
- Added Product Verification cockpit and scheduler translations for `flyto-code`
  plus the shared `common.running` key used by action buttons.
- Added unittest coverage for `scripts/sync-to-projects.py` dry-run, stale
  locale deletion, manifest sync behavior, and `scripts/add-locale.py` locale
  coverage status calculation.
- Added project memory files, workflow docs, and handoff registry.
- Added feature, locale, distribution, multilingual SEO, and full tooling
  references plus a machine-readable feature-to-source manifest.
- Added an AST-enforced generated reference for all 188 Python declarations.
- Added Draft-07 locale and repository manifest validation plus regression tests.
- Added a non-mutating placeholder parity audit with JSON and scoped strict modes.
- Added regression coverage for root manifest synchronization and the safe Thai
  historical batch CLI.

### Changed

- Refined the two reviewed fail-closed titles so each names the exact capability
  the deployment is missing instead of a generic noun.
  `aiSpace.workspace.resourceInventoryUnavailable` is now "Registered-device
  inventory unavailable" / 「無法取得已註冊設備清單」/「无法获取已注册设备清单」, and
  `spaces.draw.catalogUnavailable` is now "Mission card catalog unavailable" /
  「無法取得任務卡目錄」/「无法获取任务卡目录」. Both titles now match the endpoint
  named in their own hint. The two `…Hint` values are unchanged, so the panels
  still state that already selected workflows stay configured and the device
  list cannot be refreshed until Cloud is upgraded, and that creating a mission
  goal stays locked until Cloud is upgraded. No key was added, renamed, or
  removed, and no value gained an interpolation placeholder.
- Refined the Traditional and Simplified Chinese
  `templateBuilder.aiChat.inputPlaceholder` from a casual open greeting into a
  concise action prompt: 「請描述您想建立或調整的工作流程」/
  「请描述您想创建或调整的工作流」. The composer now tells the operator what to
  type instead of asking what the assistant can help with, and keeps the polite
  您 form and the workflow noun already used by every other reviewed string in
  the same `templateBuilder.aiChat.*` catalog. This stays a source-only
  improvement: the generated bundles still publish
  `locales/cloud/<locale>/template.json`'s longer
  `cloud.templateBuilder.aiChat.inputPlaceholder` for this path, because
  `flat_to_nested` strips the `cloud.` prefix and keeps the first writer; that
  pre-existing shadowing was not changed here.
- Replaced the six broken English scaffold values in the Traditional and
  Simplified Chinese `templateBuilder.aiChat.*` catalogs — `configureFirst`,
  `goToSettings`, `notConfigured`, `setupDesc`, `setupTitle`, and
  `welcomeMessageGeneral` — with reviewed product copy. Chinese operators
  previously saw literal strings such as `Setup Title` and `GoTo設定` in the
  workflow builder AI assistant. No key was added, renamed, or removed.
- Translated the nine existing `code.gate.*` FeatureGate keys into Traditional
  and Simplified Chinese. Eight were empty and `capabilitiesUnavailableDesc`
  carried the English source verbatim, so gated pages showed blank buttons or
  English prose to Chinese operators. No key was added, renamed, or removed, and
  no consumer copy was hardcoded.
- Added focused coverage requiring the whole `code.gate` namespace to stay
  non-empty in zh-TW and zh-CN across source and generated bundles, to keep its
  key set matched to the English catalog, and to reject values that are still
  the English fallback.
- Refined the Traditional and Simplified Chinese `code.gate.capabilitiesUnavailable`
  title to name the capability snapshot, matching the noun already used by its own
  description and by the retry action instead of the vaguer 「能力資訊」/「能力信息」.
- Extended the FeatureGate regression test with a source-to-dist parity assertion
  covering `en`, `zh-TW`, and `zh-CN`, so a stale published bundle fails even for
  the English catalog, which no other assertion checked in `dist/`.

- Converged the canonical English, Traditional Chinese, and Simplified Chinese
  Cloud copy on `Workflows -> AI Space -> AI Workflow War Room`; resource copy
  now treats robots, cameras, gateways, and MCP endpoints as optional workflow
  adapters instead of the product's top-level structure.

- Reframed AI Space copy around composable workflow input/output contracts for
  both software and hardware. Added reviewed English, Traditional Chinese, and
  Simplified Chinese labels for typed outputs, open inputs, missing contracts,
  and optional adapter safeguards without changing existing locale keys.
- Rebuilt the tracked Code and aggregate distribution bundles with 9,246 Code
  keys so every benchmark v2 label, proof stage, duration, and gap state is
  available from the CDN contract.
- Migrated the remaining Cloud common/status/AI Space save labels into the
  shared source, rebuilt tracked Cloud/Flow/aggregate bundles, and closed all
  Flyto Cloud orphan translation references.
- Rebuilt the tracked Code and aggregate distribution bundles with 9,208 Code
  keys. Strict validation passed across all 4,560 source catalogs, and the
  focused Code UI/distribution suite passed 9 tests.
- Rebuilt the tracked Code and aggregate distribution bundles with the
  Engine-aligned scoring labels.
- Synchronized the two missing Warroom CE administrator password-policy keys
  into all fallback Code locale catalogs and rebuilt the tracked Code,
  aggregate, and manifest distribution artifacts.
- Rebuilt the tracked Code and aggregate distribution bundles so the
  attack-validation cockpit never depends on hard-coded UI copy.
- Aligned Warroom CE administrator-registration copy with the enforced
  8-character, 72 UTF-8 byte, three-of-four character-class password policy;
  added reviewed English, Traditional Chinese, and Simplified Chinese messages
  plus regression coverage and rebuilt the tracked Code/aggregate bundles.
- Rebuilt and synchronized the Cloud and Flow locale bundles so both editions
  consume the same MCP Studio copy from `flyto-i18n`.
- Updated Cloud-sync authentication to prefer the existing repository-wide
  cross-repository secret, with the legacy Cloud-specific secret as fallback.
- Isolated and ignored the workflow's private Cloud checkout so generated
  localization PRs contain locale sources and distribution artifacts only.
- Filled the previously empty light and dark appearance labels in non-English
  code catalogs and rebuilt the tracked `dist/code` plus aggregate bundles.
- Rebuilt and synchronized `dist/code` bundles for first-run CE onboarding.
- Rebuilt distribution bundles and synchronized the CE product-loop catalog to
  the consuming `flyto-code` package.
- Updated public locale values to use the Flyto2 brand and the preferred
  `X-Flyto2-API-Key` header text.
- Corrected the README license badge to match the MIT license file and refreshed
  generated coverage numbers.
- `scripts/build-dist.py` now generates `dist/locale-meta.json` from the shared
  contract and reports translated completion from unique merged keys instead of
  double-counting duplicated source keys.
- `scripts/coverage.py` and `scripts/add-locale.py` now include the `engine`
  scope through the shared contract.
- Updated root project memory and manifest coverage numbers for the current
  Flyto2 localization and public SEO role.
- Reduced `scripts/sync-to-projects.py` complexity by extracting locale,
  manifest, deletion, app-build, and summary helpers without changing locale
  data.
- Reduced `scripts/add-locale.py` list complexity by extracting locale coverage
  counting and status formatting helpers.
- Extended generated-artifact freshness and build triggers to SEO source and
  locale contract changes; cache purge now includes Engine and metadata files.
- Replaced the outdated CI timing/consumer claim with the actual workflow and
  external-state contract.
- Synchronized root locale coverage from deterministic aggregate build evidence
  and extended freshness automation to cover `manifest.json`.
- Replaced the Thai batch's absolute workstation path and import-time writes
  with an explicit repository-relative, dry-run-aware CLI.
- Changed Core and Cloud key synchronization to preserve scanner-omitted values
  by default, with destructive deletion available only through
  `--delete-stale`; added regression tests for both paths.
- Unified operational project-scope lists through `i18n_contract.PROJECT_DIRS`.
