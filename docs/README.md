# Documentation Index

## Contracts

- [Feature and ownership reference](FEATURES.md)
- [Locale source and fallback contract](LOCALE_CONTRACT.md)
- [Generated distribution contract](DISTRIBUTION.md)
- [Multilingual SEO contract](SEO_CONTRACT.md)
- [Script and side-effect reference](TOOLING.md)
- [Generated Python declaration reference](generated/python-symbols.md)

## Generated Artifacts

- `../dist/locale-meta.json` contains locale-picker, `hreflang`, Open Graph,
  direction, region, and flag metadata.
- `../dist/seo-manifest.json` contains the landing/docs/blog SEO contract built
  from `../seo/public-surfaces.json`.
- `../dist/{scope}/{locale}.json` contains merged runtime translations.
- `generated/python-symbols.md` contains all documented Python classes,
  functions, nested functions, methods, and tests with source line links.

Architecture and current maintainer truth live in [ARCHITECTURE.md](../ARCHITECTURE.md),
[STATE.md](../STATE.md), [ROADMAP.md](../ROADMAP.md), and
[DECISIONS.md](../DECISIONS.md). Generated files identify their owning builder
in [DISTRIBUTION.md](DISTRIBUTION.md); do not edit them directly.
