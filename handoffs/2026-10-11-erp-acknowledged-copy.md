# Mission Receipt copy: the external system acknowledged the write

Owner: claude
Branch: claude/erp-acknowledged
Date: 2026-10-11

## What changed

`spaces.receipt.erpAcknowledged` in `locales/cloud/{en,zh-TW,zh-CN}/spaceOperations.json`,
next to `spaces.receipt.erpAckMissing`. flyto-cloud's Mission Receipt shows it
when the evidence package's `external_writeback.status` is `ACKNOWLEDGED`:
the system of record's own signed read-back (`flyto.record-readback.v1`,
flyto-cloud `docs/record-readback.md`) holds every field the AI wrote.
`{record}` is the record id. dist and manifest rebuilt; the cumulative Cloud
key count in `tests/test_cloud_runtime_cumulative_keys.py` is 13,961.

## Verified

- `python3 scripts/validate.py --strict`: PASS, 0 errors.
- `python3 scripts/build-dist.py`, `python3 -m pytest tests -q`: 132 passed.

## Not verified

- Other locales fall back to English, like `erpAckMissing`.
