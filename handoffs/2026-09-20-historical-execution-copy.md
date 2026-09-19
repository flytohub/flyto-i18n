# Historical execution and learning result copy

Two `spaces.ops` keys are owned by `spaceOperations.json`: `previousAttempt`
and `previousAttemptHint`. They distinguish saved output from an earlier
execution from the current task status. The consumer reuses the existing
`spaces.schedule.attempt` heading rather than creating a duplicate label.
Two further labels, `learningSaved` and `learningNotSaved`, distinguish an
acknowledged saved reusable workflow from an explicit not-saved receipt.
They do not change the execution's independently verified completion state.
The consumer omits this note when learning was disabled or no receipt exists.

English, Traditional Chinese and Simplified Chinese are reviewed. The other
thirteen Cloud locales intentionally contain English fallback for these four
additions. Source ownership and generated Cloud bundle equality are asserted by
the existing operations runtime-key contract. The cumulative English Cloud
inventory increases from 12,474 to 12,478 without weakening the manifest check.
Cloud and aggregate distributions were regenerated, and Cloud's three bundled
locales were synchronized from the generated files.

`npm run verify` passed: strict validation of 4,854 catalogs, zero errors and
120 tests. This includes build reproducibility and source-to-distribution
contracts. The Cloud consumer's focused translation/result tests passed 49
cases. Four 390px browser fixtures cover saved, not saved, disabled and absent
learning receipts; all passed and the screenshots were visually inspected.
These are rendering contracts, not proof of live AI learning.
The final complete Cloud frontend suite passed 4,301 tests across 300 files.

This catalog change does not itself deploy Cloud or prove live AI task
completion. Cloud keeps the historical execution read model and acceptance
receipts in its own software acceptance change.

Strict Indexer verification passed all 21 checks. Aggregate task validation
passed Ruff, all 120 tests and the complete 57-path intent ledger. Its host-
captured path manifest uses the supported current-state interface because the
minified generated diff exceeds the built-in byte limit; generated files are
included. Validation invokes the same Indexer CLI source with both its own root
and the tested repository on Python's import path, since the shell wrapper
otherwise hides the top-level translation test module.

The integration preserves upstream CTEM translations from `origin/main` and
regenerates aggregate distributions from both catalogs rather than selecting
one side of a generated-file merge conflict.
