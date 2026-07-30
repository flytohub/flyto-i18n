# State

Current state on 2026-07-30:

- Repo status: internal tooling with public CDN artifacts.
- Flyto2 AI Space product copy now has a canonical `cloud.aiSpace` source
  catalog with 286 non-empty keys in English, Traditional Chinese, and
  Simplified Chinese. Flyto Cloud consumes the generated bundles without
  carrying a duplicate local catalog; other locales use the standard English
  runtime fallback until reviewed community translations are added.
- The AI Space resource-routing extension adds reviewed endpoint, capability,
  Space, permission, health, priority, lease, automatic/custom policy, and
  confirmation copy without binding the UI to a language, device class,
  coordinate system, or vendor SDK.
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
- Every one of 198 Python classes, functions, nested functions, methods, and
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
- Document unresolved P0/P1 work in `tasks.md` or `handoffs/`.

Verification evidence captured on 2026-07-30:

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
