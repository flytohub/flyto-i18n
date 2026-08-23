# Complete Core module labels

Owner: codex
Branch: codex/convergence-closure
Date: 2026-08-24

## What changed

Added the 42 label keys missing from the current Core registry to their
category-owned English, Traditional Chinese, and Simplified Chinese source
catalogs, rebuilt aggregate, Flow, and Cloud bundles, and added a contract test
for source ownership and distribution identity. The repository test command now
uses pytest. The newly collected contracts keep `spaces.ops.management` in
`spaces.json`, `spaces.ops.noReplans` in `spaceOperations.json`, and pin the
expanded Cloud manifest at 12,046 keys across 262 source files.

## Why

The canvas and node picker now use the same resolver. That resolver can only be
consistent when every official-locale registry key has one upstream owner and
the generated Cloud bundle carries the same value.

## Verified

- Current 475-module Core registry audit: zero missing keys in all three
  official locales.
- `npm run verify`: strict validation of 4,674 files with zero errors; 100 tests
  and 2,702 subtests passed; generated distributions rebuilt before their
  contracts ran.

## Not verified

Unsupported locales continue to use the registry English fallback for these
new labels. Native review for those locales was not claimed.

## Follow-ups

Add native translations when a locale owner reviews them; keep the official
three-locale registry contract as the release gate.
