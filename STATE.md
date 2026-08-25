# State

Current state on 2026-08-26:

- All 16 Code locale catalogs include the additive 131-key manager-surface
  contract. It includes the Agent Firewall telemetry, policy posture, AI
  registry, audit report, discovery, blocking, prompt/paste, file-upload, and
  code-to-AI labels, plus the CTEM sampled-priority notice and the rest of the
  intended Code catalog delta.
- Existing catalog keys and values from `origin/main` remain authoritative;
  the restored keys retain the locale-specific values from the intended
  source commit. Tracked Code and aggregate bundles and manifests are generated
  only from the merged source catalogs by `scripts/build-dist.py`.

Current state on 2026-08-24:

- Every `ui_label_key` exposed by the current 475-module Core registry resolves
  in the English, Traditional Chinese, and Simplified Chinese module catalogs.
  The 42-key closure covers AI, API, OAuth, browser detection, data, HTTP,
  output, reverse engineering, MCP, test, verification, and Warroom nodes.
- Focused regression coverage pins reviewed values, single source ownership,
  and source-to-Cloud-distribution identity for all 42 labels. Canvas and node
  picker consumers can now share one resolver without locale-dependent English
  leaks.
- `spaces.ops.management` is owned by `spaces.json` and
  `spaces.ops.noReplans` by `spaceOperations.json`, with no duplicate source
  keys. Repository verification runs pytest, which includes both unittest
  classes and function-style source-ownership contracts. The Cloud manifest
  contract reflects 12,046 keys across 262 source files after the six new
  module catalogs and 42 labels.

Current state on 2026-08-23:

- Space Operations owns a 40-key verification-loop copy contract in the
  English, Traditional Chinese, and Simplified Chinese `spaceOperations.json`
  catalogs. The contract names acceptance, execution, evidence, verdict,
  every backend-projected stage state and overall status, plus the explicit
  next action.
- Completed execution remains visibly different from verified acceptance.
  Focused regression coverage pins the exact key set, reviewed copy, unique
  source ownership, non-empty placeholder-free values, and equality between
  source, Cloud distribution, and aggregate distribution bundles.

Current state on 2026-08-22:

- The Operations Room output wall and management entry now source their 11
  visible labels from the reviewed English, Traditional Chinese, and Simplified
  Chinese catalogs. The canonical Cloud and aggregate bundles publish the same
  values, so syncing a consumer from `dist/cloud` cannot remove copy that the
  live `wt()` surfaces still require.
- Focused regression coverage pins sole non-empty catalog ownership, exact
  values, placeholder parity, and source-to-Cloud-to-aggregate identity for the
  11-key control contract.

Current positioning on 2026-08-14:

- The public role is: "Fix a translation once and share it across every Flyto2
  product, docs, and website surface."
- The README now leads with the cross-repository copy-drift problem and an
  existing-catalog edit followed by strict validation and distribution build.
  Architecture, ecosystem scope, SEO, and secondary workflows remain documented
  below that first result.
- Package and repository manifest descriptions use the same narrow role. Public
  discovery keywords no longer imply that this repository is an AI framework or
  workflow automation product.

- Cloud synchronization is now owned by this repository. An hourly or manual
  workflow pulls a selected `flyto-cloud` ref, synchronizes catalogs, rebuilds
  generated artifacts, runs the complete verification suite, and opens a
  review-required PR only when the deterministic working tree changes. Private
  Cloud source is never committed here.

Current state on 2026-08-14:

- AI Space identity and local-voice settings are source-owned under the exact
  19-key `aiSpace.settings.*` contract in every Cloud locale. English,
  Traditional Chinese, and Simplified Chinese use reviewed copy; the other 13
  locales carry native-language copy rather than a full English fallback.
  Generated Cloud and aggregate bundles expose the same values. Wake-word copy
  states that detection remains on-device and routing never grants permission
  or bypasses approval.
- War Room camera copy now describes a local, near-real-time image surface
  truthfully. The room status is connection state rather than a camera-live
  claim; delayed, disconnected, permission-denied, and starting states are
  explicit; and the privacy label says camera images stay on the device.
- The cumulative Cloud runtime regression pins the reviewed English,
  Traditional Chinese, and Simplified Chinese camera values, their unique
  `spaceOperations.json` ownership, `{fps}` / `{seconds}` placeholder parity,
  non-empty source-to-Cloud-to-aggregate equality, and rejection of continuous
  video, live-camera, inference, or recording claims.

Current state on 2026-08-13:

- `aiSpace.workspace.openOperations` now uses the accepted Cloud UI product
  copy exactly: `Operations room`, `作戰室`, and `作战室`. A focused regression
  pins all three source values and requires exact source-to-Cloud-dist equality.
- The Cloud PR156 cumulative runtime closure is source-owned here. The official
  English, Traditional Chinese, and Simplified Chinese catalogs additively
  include the 134 reviewed keys previously present only in Cloud's bundled
  runtime source: 59 `aiSpace.*`, 25 `myTemplates.*`, and 50
  `templateBuilder.missionSetup.*`. All earlier i18n keys remain present,
  including the 21 `spaces.draw.*` / `spaces.voice.*` additions.
- `accessibility.modal` is reviewed and non-empty in all three official locales.
  The focused cumulative contract pins all 134 imported key names and counts,
  their unique designated source-catalog ownership, and canonical sorted value
  map digests for each official locale against the accepted Cloud provenance,
  three-locale non-empty and placeholder parity, source-to-dist identity,
  deterministic generated Cloud output, the modal label, and the 21 Space
  Operations keys. The final integration regression also builds the complete
  Cloud manifest in memory through the selective distribution API, requires it
  to equal tracked `dist/cloud/manifest.json`, pins the complete official-locale
  records at 11,842 keys across 254 files, and proves a temporary filtered
  `--scope cloud --locale en` build cannot truncate the all-locale manifest.
- Fresh verification on branch `codex/i18n-cloud-runtime-20260813` completed
  successfully: the focused cumulative suite passed 6 tests;
  `python3 scripts/validate.py --strict` validated 4,598 files with zero errors;
  `npm run verify` passed compile/Ruff/generated-reference checks (299 Python
  declarations), strict validation, coverage, 68 unit tests, deterministic
  distribution generation, and SEO generation. The full build retained 11,842
  Cloud keys and 254 Cloud source files in each official locale without changing
  tracked generated bundles.
- `flyto-index verify . --strict --json` passed 19/19 checks with no warnings or
  failures. Its check fingerprint is
  `2d0b13986cdccdafda951e9484a04d0d065506a2d49b363c36e2fef271e2f4bb`.

Current state on 2026-08-12:

- Cloud deployments that do not serve the newer Space endpoints now have
  fail-closed copy instead of a silent empty panel. Four keys —
  `aiSpace.workspace.resourceInventoryUnavailable`,
  `aiSpace.workspace.resourceInventoryUnavailableHint`,
  `spaces.draw.catalogUnavailable`, and `spaces.draw.catalogUnavailableHint` —
  are reviewed and non-empty in English, Traditional Chinese, and Simplified
  Chinese. Each title now names the exact capability that is missing rather than
  a generic noun: the AI Space title reads "Registered-device inventory
  unavailable" / 「無法取得已註冊設備清單」/「无法获取已注册设备清单」 and the Space
  Operations title reads "Mission card catalog unavailable" /
  「無法取得任務卡目錄」/「无法获取任务卡目录」, so each title matches the endpoint
  named in its own hint. The AI Space pair states that the registered-device
  inventory endpoint is unavailable, that already selected workflows stay
  configured, and that the device list cannot be refreshed until Cloud is
  upgraded. The Space Operations pair states that the mission-card catalog
  endpoint is unavailable and that mission goal creation stays locked until
  Cloud is upgraded. None of the four values uses an interpolation placeholder.
- The Traditional and Simplified Chinese `templateBuilder.aiChat.inputPlaceholder`
  source values are now a concise action prompt —
  「請描述您想建立或調整的工作流程」/「请描述您想创建或调整的工作流」 — instead of an
  open greeting, keeping the polite 您 form used by the rest of that catalog.
  This is a source-only improvement: the generated bundles resolve the nested
  `templateBuilder.aiChat.inputPlaceholder` path from
  `locales/cloud/<locale>/template.json`'s `cloud.`-prefixed key instead, because
  `build-dist.flat_to_nested` strips the `cloud.` prefix and keeps the longest
  key as first writer. That pre-existing shadowing is out of scope for this
  change and remains open work.
- The Cloud `spaceOperations` catalog now owns the live Space operations zone
  drawing and voice goal surfaces: 10 `spaces.draw.*` and 11 `spaces.voice.*`
  keys are reviewed and non-empty in English, Traditional Chinese, and
  Simplified Chinese. None of the 21 values uses an interpolation placeholder,
  so placeholder parity holds by construction. `aiSpace.workspace.openOperations`
  gives the AI Space workspace a localized entry point into that console.
- The Traditional and Simplified Chinese `templateBuilder.aiChat.*` catalogs no
  longer leak English scaffold strings for `configureFirst`, `goToSettings`,
  `notConfigured`, `setupDesc`, `setupTitle`, or `welcomeMessageGeneral`. The
  English source values for those six keys are still unreviewed scaffolds and
  remain open work.

Current state on 2026-08-09:

- Repo status: internal tooling with public CDN artifacts.
- FeatureGate blocking states are fully localized in Traditional and Simplified
  Chinese. The nine `code.gate.*` keys — dashboard return, capability-snapshot
  failure, disabled module, preview lock, billing entry, and capability retry —
  are non-empty in source and in the tracked `dist/code` bundles, and none falls
  through to the English source string. The capability-snapshot title now uses
  the same noun as its description and retry action in both Chinese locales.
  `tests/test_feature_gate_keys.py` pins the key set against the English
  catalog, the non-empty requirement, the English-fallback guard, the reviewed
  wording, and source-to-dist parity for `en`, `zh-TW`, and `zh-CN`. The
  Current-tree `npm run verify` and strict Indexer verification now cover this
  cumulative dirty baseline, including the focused FeatureGate test.
- Report export format copy is catalog-owned under `code.reports`: all 16 Code
  locales publish a non-empty format-menu label and PowerPoint name. English,
  Traditional Chinese, and Simplified Chinese are reviewed; the other 13
  locales use the established deterministic English fallback until reviewed.
Current state on 2026-08-08:

- Repo status: internal tooling with public CDN artifacts.
- Canonical Cloud copy now exposes the product hierarchy as `Workflows -> AI
  Space -> AI Workflow War Room`. AI Space composes workflows, context, and
  policy; physical endpoints and MCP resources remain optional adapters rather
  than defining the product's top-level navigation.
- Flyto2 AI Space product copy now has a canonical `cloud.aiSpace` source
  catalog with 340 non-empty keys in English, Traditional Chinese, and
  Simplified Chinese. Flyto Cloud consumes the generated bundles without
  carrying a duplicate local catalog; other locales use the standard English
  runtime fallback until reviewed community translations are added.
- Every Cloud locale now has non-empty browser-engine provisioning copy and
  connector category labels. Source and generated-bundle contract tests keep
  these runtime keys from falling through to missing-key warnings.
- The 44-key `aiSpace.dependency.*` contract gives each workflow capability an
  automatic or operator-reviewed multi-axis dependency policy. Safety response,
  task consequence, evidence, substitution, confidence, freshness, recovery,
  retry, and active phases remain independent; mission/safety/required labels
  are UI summaries, not persisted execution levels.
- AI Space is described as a provider-neutral workflow, memory, permission, and
  policy scope. Reviewed copy makes workflow input/output schemas the common
  composition boundary for APIs, databases, cameras, speakers, robots, and
  other capabilities; endpoint leasing remains an optional adapter safeguard
  and is not presented as the AI planning surface.
- Product lines: cloud_apps_automation, security, data, zero_person_agent,
  big_data_intelligence.
- Health target: B.
- Shared locale metadata now lives in `scripts/i18n_contract.py` and is
  generated into `dist/locale-meta.json`.
- Public landing/docs/blog SEO source lives in `seo/public-surfaces.json` and is
  generated into `dist/seo-manifest.json`.
- Package metadata now includes homepage, repository, issues, and SEO keywords
  for GitHub/package-index discovery.
- Public locale values no longer expose standalone retired branding or the old
  API-key header copy; generated dist bundles now use Flyto2 wording.
- `scripts/build-dist.py` now reports completion from unique merged keys, so
  manifest percentages no longer exceed 100%.
- `scripts/coverage.py` and `scripts/add-locale.py` now include the `engine`
  scope through the shared contract.
- The Flyto2 Warroom CE deterministic product loop has source keys in every
  supported code locale, generated `dist/code` artifacts, and synchronized
  `flyto-code/public/i18n/code` bundles.
- The attack-validation cockpit has a canonical `code.attackValidation.*`
  namespace in all 16 Code locales. English and Traditional Chinese have
  reviewed copy for Red Team, Pulse, BYO, authorization modes, confidence,
  owned/canary safety scope, and remediation/retest states; other locales use
  the deterministic English fallback until reviewed translations land.
- All 16 Code locale catalogs and tracked distributions now include the 37-key
  `code.attackValidation.command.*` contract for the campaign-first Red Team,
  Pulse, and BYO decision surface. English, Traditional Chinese, and Simplified
  Chinese are reviewed; the other 13 catalogs use deterministic English
  fallbacks until native review.
- All 16 Code locale catalogs and tracked distributions include the 33-key
  attack-validation benchmark v2 contract for measurable outcome funnels,
  time-to-proof percentiles, source/mode/proof-stage coverage, and closure gap
  queues. English, Traditional Chinese, and Simplified Chinese are reviewed;
  the other 13 catalogs preserve the runtime English fallback policy.
- All 16 Code locale catalogs and their generated distributions include the
  five canonical `code.scoring.*` labels for cloud posture, container images,
  and MCP Runtime Guardian, keeping the frontend scoring surface aligned with
  the Engine scoring domains.
- Warroom CE one-time administrator setup copy is translated in English,
  Traditional Chinese, and Simplified Chinese, present in all code locale
  catalogs, and synchronized into the consuming frontend bundles. Its password
  guidance matches the enforced 8-character, 72 UTF-8 byte, three-of-four
  character-class policy.
- All 16 Code locale catalogs now carry the canonical
  `auth.localBootstrap.passwordClasses` and
  `auth.localBootstrap.passwordMaxBytes` keys. The 13 fallback locales and the
  tracked Code/aggregate distribution bundles were regenerated after a real
  Cloud-owned synchronization run exposed the stale catalog state.
- Warroom CE appearance controls now have non-empty light, dark, and
  system-following labels in all 16 supported code locales; generated
  `dist/code` and aggregate bundles carry the same keys.
- Warroom CE direct public-repository onboarding copy is translated in English
  and Traditional Chinese and has synchronized fallback keys in every supported
  code locale and generated distribution bundle.
- Cloud synchronization is owned by the private `flyto-cloud` workflow. It
  runs this repository's scanner beside the private source and opens a reviewed
  i18n pull request without granting this public repository Cloud read access.
- MCP Studio now has a canonical Cloud source catalog for English, Traditional
  Chinese, and Simplified Chinese. The catalog is included in both Cloud and
  Flow distribution scopes, with other Flow locales using the English fallback.
- The public i18n checkout is isolated under Cloud's `.sync-target/` workspace,
  so generated localization pull requests cannot include private Cloud source.
- `code.communityLoop.*` is a critical non-empty namespace for Traditional and
  Simplified Chinese validation.
- Draft-07 locale and repository-manifest schemas are executed by strict
  validation across 4,560 recognized catalog files.
- Every one of 212 Python classes, functions, nested functions, methods, and
  tests has a docstring and a freshness-checked generated source reference.
- Root manifest coverage is synchronized from the deterministic aggregate
  build; it no longer drifts from `dist/manifest.json`.
- Placeholder parity is measurable through `audit-placeholders.py`; the
  current non-blocking legacy baseline is 577 mismatches.
- The historical Thai batch no longer writes during import or uses an absolute
  workstation path; its CLI supports repository-relative and dry-run use.
- Core and Cloud synchronization preserve scanner omissions by default. The
  pre-fix dry-run exposed Core `-241` and Cloud `-1915` deletion candidates;
  after the fix, current safe dry-runs report Core `+272/~241 preserved` and
  Cloud `+133/0 removed`. The upstream changes were not applied.

Verification evidence captured on 2026-08-08:

- Workflow-first hierarchy regression coverage passed for English, Traditional
  Chinese, and Simplified Chinese, including the mirrored legacy namespace.
- Strict catalog validation passed across 4,576 source files with zero errors;
  Cloud, Flow, and aggregate tracked distributions were rebuilt successfully.

Known release work:

- Wire `dist/seo-manifest.json` into landing/docs/blog metadata generation.
- Keep Flyto2 API-key header compatibility aligned with flyto-engine before
  downstream apps rely only on `X-Flyto2-API-Key`.
- Keep keyword evidence in `seo/public-surfaces.json` current when new SEO
  research is done.
- Continue translating the `code` scope; it is the main remaining coverage gap.
- Review current Core and Cloud scanner drift before changing the recorded
  `flyto-core@2.0.0` last-full-sync marker.
- Remediate placeholder parity by project and locale before enabling the
  repository-wide strict placeholder gate.
- Migrate the tracked `dist/cortex` compatibility bundle to a named source
  catalog and generator scope before treating it as fresh output.
- Resolve the `cloud.`-prefixed key shadowing in `build-dist.flat_to_nested`.
  Any legacy `cloud.<path>` key silently wins over the unprefixed `<path>` key
  because keys are applied longest-first and the first writer wins, so reviewed
  edits to the shorter key never reach the published bundles.
  `templateBuilder.aiChat.inputPlaceholder` is the currently known instance.
- Document unresolved P0/P1 work in `tasks.md` or `handoffs/`.

Verification evidence captured on 2026-07-31:

- Cloud runtime translation closure passed strict validation across 4,563
  source catalogs, 36 unit tests, generated-reference freshness, Ruff, and a
  deterministic rebuild of Cloud plus aggregate CDN bundles.
- Every supported Cloud locale passed non-empty source and generated-bundle
  checks for browser provisioning and connector category runtime keys.
- The rebuilt aggregate bundles contain 22,318 keys in fallback locales and
  22,733 keys in English, Traditional Chinese, and Simplified Chinese.

Verification evidence captured on 2026-07-30:

- The AI Space dependency contract passed exact 44-key source and generated
  bundle parity tests for English, Traditional Chinese, and Simplified Chinese,
  strict validation across all 4,563 catalogs, and deterministic Cloud and
  aggregate distribution rebuilding.
- Deterministic distribution rebuilding completed with 9,246 Code keys after
  adding the measurable effectiveness benchmark v2 catalog.
- Strict validation passed across all 4,560 source catalogs after adding the
  campaign command-center contract.
- Deterministic distribution rebuilding completed with 9,208 Code keys and
  22,272 aggregate keys.
- The focused Code UI and distribution suites passed 9 tests, including
  all-locale source/generated parity and reviewed English, Traditional Chinese,
  and Simplified Chinese copy pins.

Verification evidence captured on 2026-07-28:

- The AI Space catalog migration passed strict validation across 4,563 source
  files, 27 tests, deterministic distribution rebuilding, Cloud bundle sync
  with zero orphan keys, and Flyto2 Indexer verification at 18/18.
- The expanded attack-validation efficacy, evidence-quality, source-health,
  filtering, and safe dark-web canary copy passed strict source validation and
  deterministic Code/aggregate distribution rebuilding across all 16 locales.
- Attack-validation catalogs passed strict validation across 4,560 source
  files, rebuilt all tracked Code and aggregate distribution bundles, and
  passed 27 tests with 72 locale-contract subtests.
- MCP Studio source catalogs passed strict validation across 4,544 files; the
  Flow-scope regression test and deterministic distribution build passed, and
  the generated Cloud and Flow bundles were synchronized to both consumers.
- The canonical locale synchronization added exactly two missing password
  policy keys to each of 13 fallback Code locales; strict validation and a
  second sync/build pass confirmed the generated locale, manifest, and
  distribution artifacts are deterministic.

- `npm run verify`: passed compilation, Ruff, generated-reference freshness,
  strict schema validation of 4,560 catalogs plus the root manifest, 27 unit
  tests, every configured distribution build, and SEO-manifest freshness.
- Shared documentation audit: passed all 6 source areas and 11 feature
  surfaces with no warnings.
- Flyto2 Indexer strict full scan: passed 18 of 18 checks; README, module,
  API, and Python declaration documentation coverage all score 100%.
- Repeated distribution builds produced identical hashes for all 183 tracked
  distribution files, including the root repository manifest.
- Placeholder audit: 577 known legacy mismatches; the default report is
  non-blocking until those strings are reviewed and corrected by locale.
- Core and Cloud real-checkout dry-runs completed without writing upstream
  changes and confirmed default preservation of scanner-omitted keys.
- Cloud-to-i18n synchronization no longer requires a private-Cloud read token
  in this public repository. The Cloud-owned workflow validates the generated
  i18n change before opening its reviewed pull request.

## 2026-07-29 - Attack validation safety and cost catalog closure

- Added 65 attack-validation keys covering proof-of-control, proof-pack state,
  tenant-local benchmark populations, exact allowlists, audit integrity,
  workspace/campaign/run budgets, cost settlement, and the emergency kill
  switch, including the full benchmark method, outcome populations, proof
  stages, audit hash context, and versioned control context.
- English, Traditional Chinese, and Simplified Chinese are reviewed for the new
  safety-critical copy. The remaining 13 Code locales carry synchronized empty
  fallbacks under the established locale policy.
- Strict validation passed across all 4,560 source catalogs. Code and aggregate
  distribution bundles were rebuilt deterministically with 9,166 Code keys.
- The five Engine-aligned scoring labels passed the focused Code UI and
  distribution tests (7 tests), strict validation across all 4,560 source
  catalogs, deterministic distribution rebuilding, and the Flyto2 Indexer
  strict full scan (18 of 18 checks).
- Cross-repository strict verification passed for Code, Engine, and i18n (3 of
  3 projects), with all 581 frontend API calls matched to backend routes and no
  product-loop closure gaps.
