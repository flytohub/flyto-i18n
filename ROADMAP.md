# Roadmap

## P0

- Keep the public role centered on fixing translation drift across Flyto2
  repositories and locales; keep supporting SEO and architecture detail below
  the first translation result.
- Preserve the repo boundary described in `ARCHITECTURE.md`.
- Keep release-impacting changes covered by tests, guards, docs, or handoffs.
- Keep `dist/` and `dist/seo-manifest.json` generated from source, never edited
  by hand.
- Keep Python declaration documentation and Draft-07 validation in the closed
  verification loop.

## P1

- Raise or maintain health at target: B.
- Wire landing/docs/blog to consume the shared SEO manifest for canonical,
  alternate language, sitemap, and localized metadata generation.
- Keep product-line and public-surface mapping current with Flyto2 release
  gates.
- Remediate placeholder mismatches in reviewed locale batches before enabling
  repository-wide strict parity.

## P2

- Add quarterly keyword evidence refresh notes for the three public surfaces.
- Add contributor guidance for translating high-traffic public pages before
  broad long-tail expansion.
- Expand docs as the repo's Flyto2 role matures.
