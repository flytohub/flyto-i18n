# Multilingual SEO Contract

## Source Of Truth

`seo/public-surfaces.json` covers three origins: `https://flyto2.com`,
`https://docs.flyto2.com`, and `https://blog.flyto2.com`. Each surface declares
its sitemap, localized route template, primary search intent, and keyword
clusters.

Each keyword cluster records a primary term, intent, long-tail variants, and an
evidence object with source, country, language, observed date, search volume,
SEO difficulty, paid difficulty, and CPC. These are dated observations, not
live guarantees. Update the evidence date and source whenever research changes;
do not silently treat zero-valued internal topic maps as measured demand.

## Generated Contract

`build-seo-manifest.py`:

1. validates required signals, origins, sitemaps, route patterns, keywords, and
   evidence fields;
2. discovers shipped locales from source catalogs;
3. generates localized URL prefixes and `hreflang` alternates;
4. adds `x-default` and Open Graph locale metadata;
5. emits a stable source hash in `dist/seo-manifest.json`.

Run `python3 scripts/build-seo-manifest.py --check` in read-only validation.

## Consumer Requirements

The manifest is planning and generation input. Landing, docs, and blog remain
responsible for rendering and validating:

- one self-referencing canonical URL per indexable page;
- reciprocal `hreflang` links and `x-default`;
- localized title, description, and visible page copy;
- sitemap entries that match canonical, status-200 routes;
- correct Open Graph locale and alternates;
- page-appropriate structured data;
- crawlable internal links and intentional robots directives.

Keyword inclusion must read naturally and answer the page intent. The contract
does not authorize keyword stuffing, doorway pages, duplicate translations, or
claims unsupported by product behavior.
