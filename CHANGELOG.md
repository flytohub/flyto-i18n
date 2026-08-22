# Changelog

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
