# Multilingual SEO Source

`public-surfaces.json` is the reviewed source contract for Flyto2 landing,
documentation, and blog search metadata. It records canonical origins,
sitemaps, route templates, required signals, keyword intent, long-tail terms,
and dated evidence.

Edit the source, run `python3 scripts/build-seo-manifest.py`, and review
`dist/seo-manifest.json`. The generator rejects missing surfaces, signals,
evidence sources, locale metadata, and `x-default` alternates.
