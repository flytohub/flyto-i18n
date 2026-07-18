# State

Current state on 2026-07-18:

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
- Public locale values no longer expose standalone `Flyto` branding or the old
  `X-Flyto-API-Key` copy; generated dist bundles now use Flyto2 wording.
- `scripts/build-dist.py` now reports completion from unique merged keys, so
  manifest percentages no longer exceed 100%.
- `scripts/coverage.py` and `scripts/add-locale.py` now include the `engine`
  scope through the shared contract.

Known release work:

- Wire `dist/seo-manifest.json` into landing/docs/blog metadata generation.
- Keep Flyto2 API-key header compatibility aligned with flyto-engine before
  downstream apps rely only on `X-Flyto2-API-Key`.
- Keep keyword evidence in `seo/public-surfaces.json` current when new SEO
  research is done.
- Continue translating the `code` scope; it is the main remaining coverage gap.
- Run repo-specific lint, tests, build, and release gates before production.
- Document unresolved P0/P1 work in `tasks.md` or `handoffs/`.
