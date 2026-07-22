# Tasks

- [x] Add MCP Studio source catalogs, include them in Cloud and Flow scopes,
  and synchronize the generated bundles to both consuming frontends.
- [ ] Define a canonical source catalog and `SCOPES` mapping for the tracked
  `dist/cortex` compatibility bundle, then add freshness coverage.

- [ ] Wire landing/docs/blog to consume `dist/seo-manifest.json`.
- [x] Add CI freshness coverage for the generated SEO manifest and root
  distribution coverage metadata.
- [ ] Confirm flyto-engine accepts `X-Flyto2-API-Key` before removing legacy
  API-key fallback references anywhere else.
- [ ] Continue closing `code` scope coverage gaps, especially community
  languages below 90%.
- [ ] Reduce the measured 577 placeholder-set mismatches by reviewed project
  and locale batches, then enable scoped strict gates.
- [ ] Keep product-line, public-surface, and `flyto-core` boundaries documented.
- [ ] Review the current Core `+272/-241` and Cloud `+133/-1915` scanner drift
  in focused PRs before advancing the last-full-sync marker.
- [ ] Update handoff notes for unresolved release risks.
- [x] Add Product Verification cockpit and scheduler i18n keys for
  `flyto-code`.
- [x] Add shared locale metadata contract for `hreflang`, `og_locale`, region,
  direction, and flags.
- [x] Add landing/docs/blog multilingual SEO source and generated
  `dist/seo-manifest.json`.
- [x] Normalize public locale values to Flyto2 branding and preferred
  `X-Flyto2-API-Key` wording.
- [x] Add package metadata, backlinks, and SEO keywords for i18n discoverability.
- [x] Fix generated manifest completion percentages to use unique merged keys.
- [x] Require docstrings and generated references for every Python declaration.
- [x] Execute locale and repository manifest Draft-07 schemas in strict validation.
