# SPM improvement-loop copy — 2026-09-30

Flyto2 Code's Posture `Improve` view now has source-owned translation keys for:

- discover / measure / prioritize / remediate / verify / re-observe stages;
- canonical external-rating forecast;
- measured rating-improvement opportunities;
- optional Footprint / Pentest / Red Team enrichment state;
- fail-soft copy when optional module status is unavailable.

English, Traditional Chinese, Simplified Chinese, and Japanese are populated.
Other locales intentionally retain empty source entries so the runtime uses the
English fallback rather than stale or fabricated translations.

`python3 scripts/validate.py --strict` and `python3 scripts/build-dist.py` are
the release checks for this change.
