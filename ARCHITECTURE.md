# Architecture

`flyto-i18n` fixes cross-repository copy drift by owning reviewed translation
sources and the generated bundles shared with Flyto2 consumers. Locale metadata
and public multilingual SEO metadata are supporting contracts within that role.

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

Cross-repository synchronization is consumer-pull oriented. The i18n-owned
`sync-cloud.yml` workflow checks out private Cloud source with a repository
secret, runs the existing scanner and full deterministic verification, and
opens a review-required pull request only when catalogs or generated outputs
change. Flyto2 Cloud may validate the same projection, but it does not own an
i18n write credential.

Cloud's bundled runtime catalogs are accepted as read-only migration provenance,
not a second source of truth. Reviewed keys imported from that bundle are merged
into `locales/cloud/{en,zh-TW,zh-CN}` and thereafter owned here; deterministic
`dist/cloud` generation and source-to-dist contract tests prevent either source
keys or cumulative local additions from being replaced.

This repo must not bypass shared `flyto-core` runtime boundaries, must not store
credentials, and must keep SaaS, enterprise, community, and internal-only
behavior explicit.

Update this file when package exports, generated dist shape, SEO contract
shape, deployment mode, provider boundaries, or cross-repo dependencies change.

## Flyto Cloud workflow hierarchy

The canonical Cloud catalog presents the product from the software workflow
upward: `Workflows -> AI Space -> AI Workflow War Room`. AI Space composes
workflows, context, and policy. Cameras, robots, gateways, and MCP endpoints
remain optional adapters selected only through declared workflow contracts;
they do not define the top-level information architecture.

The authoritative public copy for this hierarchy lives in
`locales/cloud/{en,zh-TW,zh-CN}/{myTemplates,aiSpace,other}.json`. Consumer-side
fallback strings may preserve availability, but they must not replace the
catalog as the reviewed runtime source.

## Flyto2 Flow boundary

`dist/flow` is the static localization input for the open-source Flyto2 Flow
parent. It contains only shared/local UI groups plus module translations.
Hosted account, collaboration, marketplace, dashboard, settings, subscription,
and remote-agent groups are excluded.

The Flow Docker build copies this generated scope and its flag SVG files into
the frontend image. Flow never loads translations or flags from a CDN at
runtime. `scripts/sync-to-projects.py --project flow` is the supported
sync path; hand-maintained translation copies in Flow are not allowed.
