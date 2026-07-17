# 2026-07-18 Multilingual SEO Contract

## Summary

`flyto-i18n` now owns a generated multilingual SEO contract for the three public
Flyto2 surfaces:

- `https://flyto2.com`
- `https://docs.flyto2.com`
- `https://blog.flyto2.com`

The source file is `seo/public-surfaces.json`; the generated CDN artifact is
`dist/seo-manifest.json`.

## Changed

- Added `scripts/i18n_contract.py` for shared locale metadata, project dirs,
  `hreflang`, `og_locale`, direction, region, and flag mapping.
- Updated build, validate, coverage, and add-locale tooling to use the shared
  contract.
- Added `scripts/build-seo-manifest.py` with `--check`.
- Added `seo/public-surfaces.json` with landing/docs/blog sitemap references,
  required SEO signals, route templates, keyword clusters, long-tail keywords,
  and search-metric evidence.
- Generated `dist/locale-meta.json` from the shared contract.
- Generated `dist/seo-manifest.json`.
- Fixed generated manifest completion math to count unique merged keys instead
  of double-counting duplicated source keys.
- Updated README, project memory, changelog, decisions, tasks, and docs index.

## Verification

Run before handoff:

```bash
python3 -m compileall -q scripts tests
python3 -m unittest discover -s tests
python3 scripts/build-dist.py
python3 scripts/build-seo-manifest.py
```

Additional final verification should run:

```bash
npm run verify
python3 scripts/build-seo-manifest.py --check
python3 scripts/validate.py --strict
flyto-indexer verify --full-scan
```

## Remaining Work

- Landing/docs/blog still need to consume `dist/seo-manifest.json` in their
  metadata/sitemap generation.
- Add CI stale check for `python3 scripts/build-seo-manifest.py --check`.
- Continue closing `code` scope translation gaps; it is the main non-public
  coverage weakness.
- Refresh keyword evidence when new SEO research is done.
