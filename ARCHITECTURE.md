# Architecture

`flyto-i18n` is the Flyto2 source of truth for localization bundles and public
multilingual SEO metadata.

Boundaries:

- `locales/{scope}/{locale}/*.json` owns translation source data.
- `scripts/build-dist.py` owns generated runtime bundles under `dist/`.
- `scripts/i18n_contract.py` owns shared project directories, locale metadata,
  `hreflang`, Open Graph locale, region, direction, and flag mapping.
- `seo/public-surfaces.json` owns the landing/docs/blog SEO contract, including
  sitemap URLs, required signals, keyword intent, long-tail terms, and observed
  search metrics.
- `scripts/build-seo-manifest.py` turns that SEO source into
  `dist/seo-manifest.json` for public sites.

Consumer surfaces:

- Product bundles: Flyto2 Cloud, Code, Console, Data, Engine, App, Landing.
- Public SEO surfaces: `flyto2.com`, `docs.flyto2.com`, `blog.flyto2.com`.

This repo must not bypass shared `flyto-core` runtime boundaries, must not store
credentials, and must keep SaaS, enterprise, community, and internal-only
behavior explicit.

Update this file when package exports, generated dist shape, SEO contract
shape, deployment mode, provider boundaries, or cross-repo dependencies change.
