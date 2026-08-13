# FeatureGate i18n

Owner: claude
Branch: working tree only (nothing staged, committed, or pushed)

Flyto2 FeatureGate blocking states now carry reviewed Traditional and Simplified
Chinese copy. The nine existing `code.gate.*` keys were unusable in both Chinese
locales: eight were empty strings and `capabilitiesUnavailableDesc` held a
verbatim copy of the English source, so gated pages rendered blank buttons or
English prose to Chinese operators.

No keys were added, renamed, or removed. No consumer was touched, so nothing is
hardcoded outside the catalog. No other namespace was modified.

## Changed

- `locales/code/zh-TW/code.json`: nine `code.gate.*` values translated
- `locales/code/zh-CN/code.json`: nine `code.gate.*` values translated
- `tests/test_feature_gate_keys.py`: new focused contract test
- `docs/generated/python-symbols.md`: regenerated for the new declarations
- `dist/`: rebuilt deterministically from source by `scripts/build-dist.py`

Terminology follows existing catalog precedent: 儀表板/仪表板, 工作區/工作区,
計費/计费, 模組/模块, 預覽/预览, 重試/重试.

### Wording of the blocked-capability state

The two `capabilitiesUnavailable*` keys were the sharpest part of the regression.
Chinese operators saw either nothing or the English source, and that English
source is written in internal engineering language: "Capabilities unavailable" /
"Flyto2 could not verify this workspace capability snapshot. Access stays closed
until the policy check succeeds." *Capability snapshot* and *policy check* name
implementation objects a Warroom reader has no way to act on.

The Chinese copy is therefore product language about permissions rather than a
literal translation. The headline is 「無法確認功能權限」/「无法确认功能权限」, and the
description says Flyto2 cannot currently confirm whether this workspace may use
the feature, and that the feature stays off until confirmation succeeds. The
retry action is plain 「重試」/「重试」. No key, English source string, or consumer
changed — only the Chinese values.

## Contract

The focused test asserts, for zh-TW and zh-CN, across both the `locales/` source
and the published `dist/code/` bundle:

1. the gate namespace key set matches the English catalog exactly
2. every gate value is non-empty
3. no gate value equals its English source string, and every value contains CJK
   — this is the English-fallback guard
4. no gate value carries internal engineering vocabulary — 能力快照, 快照,
   政策/策略檢查, `capabilit`, `snapshot`, `policy`, `fallback`, raw catalog keys
   — and no Latin-script run other than the brand token `Flyto2` survives
5. the reviewed wording is pinned against silent drift, including the exact
   blocked-capability headline in both locales
6. the published `dist/` gate namespace is byte-identical to the authored
   `locales/` gate namespace for `en`, `zh-TW`, and `zh-CN` — this is the
   freshly-rebuilt-from-source contract, and it is the only assertion that also
   covers the English bundle

Assertions covering the published bundle carry a failure hint pointing at
`python3 scripts/build-dist.py`, because the usual cause of a mismatch is an
un-rebuilt distribution rather than bad copy.

`code.gate` resolves to a plain nine-key leaf object in the code scope, with no
`_self` parent collision, so the exact-key-set assertion is stable under
`build-dist.py`'s flat-to-nested conversion.

## Verification

Ran and passed:

- the declared `build-dist` project action (`.flyto/coding.yaml` →
  `python3 scripts/build-dist.py`), exit 0. All nine scopes plus the aggregate
  bundle and `dist/locale-meta.json` were regenerated; the `code` scope built
  9,264 keys per locale at 96.9% zh-TW and 95.7% zh-CN.
- read-back of the authored catalogs: both Chinese gate namespaces carry the
  reviewed product copy verbatim, headline 「無法確認功能權限」/「无法确认功能权限」
  included. Coverage of the published bundles comes from the focused test's
  source↔dist equality and jargon assertions rather than a separate manual read.
- `npm run verify`, exit 0 — compileall, Ruff, generated-reference freshness,
  strict schema validation (4,592 files, 0 errors), the unit suite (47 tests,
  including this change's focused `tests/test_feature_gate_keys.py`), and the
  configured distribution build, which succeeded.
- the configured strict `flyto-indexer` check
  (`flyto-index verify . --strict --json`), the remaining required check declared
  in `.flyto/coding.yaml`, run by the service route and passed. This handoff
  records only the outcome; the detailed metrics remain in the route evidence.

`dist/` is rebuilt and current — it is not pending, not stale, and was not
hand-edited. Both required checks in `.flyto/coding.yaml` have now run and
passed: project checks are green; independent Codex audit remains the release
gate.

`build_locale` derives each `version` from a
SHA-256 of the flat catalog and `build_manifest` derives its version from the
per-locale versions, so distributions are only ever regenerated from source;
editing them by hand would desynchronize those hashes and defeat the
determinism that `check-dist-fresh` gates on. Rebuilding raises
`translated_keys` and `completion` for zh-TW and zh-CN in the `code` scope
manifest and the aggregate manifest, since eight previously empty values per
locale become non-empty.

The unrelated report-export / PPTX working-tree changes were left untouched and
are swept into the same deterministic rebuild.
