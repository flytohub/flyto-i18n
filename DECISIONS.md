# Decisions

## 2026-07-23 - CE repository onboarding copy is bundled locally

Decision: keep the Community direct-repository URL form, supported-host hint,
validation errors, connect action, and scan-start state in the `code` locale
catalogs and generated distribution bundles.

Reason: first-run self-hosted CE must remain understandable without a network
translation service, including before any external provider connection exists.

## 2026-06-21 - Project memory bootstrapped

Decision: track Flyto2 product-line role, repo boundary, state, roadmap, tasks,
and handoffs in this repo.

Reason: `flyto-i18n` must be maintainable by future agents without relying on
conversation memory.

## 2026-07-18 - Public multilingual SEO contract lives in flyto-i18n

Decision: keep landing/docs/blog locale metadata, `hreflang` templates,
sitemap references, Open Graph locale mapping, and keyword-intent evidence in
`seo/public-surfaces.json`, then generate `dist/seo-manifest.json`.

Reason: the three public Flyto2 surfaces need the same multilingual SEO
contract. Keeping it here avoids stale per-site copies and lets translation,
locale metadata, and public SEO planning evolve together.
