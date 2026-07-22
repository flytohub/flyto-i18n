# State

Current state on 2026-07-22:

- Repo status: internal tooling with public CDN artifacts.
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
- Warroom CE one-time administrator setup copy is translated in English,
  Traditional Chinese, and Simplified Chinese, present in all code locale
  catalogs, and synchronized into the consuming frontend bundles.
- Warroom CE appearance controls now have non-empty light, dark, and
  system-following labels in all 16 supported code locales; generated
  `dist/code` and aggregate bundles carry the same keys.
- The Cloud synchronization workflow prefers the repository-wide cross-repo
  token and retains the older Cloud-specific token only as a compatibility
  fallback; secret values are never stored in the repository.
- MCP Studio now has a canonical Cloud source catalog for English, Traditional
  Chinese, and Simplified Chinese. The catalog is included in both Cloud and
  Flow distribution scopes, with other Flow locales using the English fallback.
- The private Cloud checkout is isolated under ignored `.sync-source/`, so a
  generated localization PR cannot stage the nested repository as a gitlink.
- `code.communityLoop.*` is a critical non-empty namespace for Traditional and
  Simplified Chinese validation.
- Draft-07 locale and repository-manifest schemas are executed by strict
  validation across 4,531 recognized catalog files.
- Every one of 192 Python classes, functions, nested functions, methods, and
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

Verification evidence captured on 2026-07-22:

- MCP Studio source catalogs passed strict validation across 4,531 files; the
  Flow-scope regression test and deterministic distribution build passed, and
  the generated Cloud and Flow bundles were synchronized to both consumers.

- `npm run verify`: passed compilation, Ruff, generated-reference freshness,
  strict schema validation of 4,531 catalogs plus the root manifest, 23 unit
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
- `Sync from Cloud` still requires an authorized GitHub Actions secret with
  read access to the private `flyto-cloud` repository; a manual dispatch is
  the final remote authorization check.
