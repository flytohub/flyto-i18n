# Historical execution output copy

Two `spaces.ops` keys are owned by `spaceOperations.json`: `previousAttempt`
and `previousAttemptHint`. They distinguish saved output from an earlier
execution from the current task status. The consumer reuses the existing
`spaces.schedule.attempt` heading rather than creating a duplicate label.

English, Traditional Chinese and Simplified Chinese are reviewed. The other
thirteen Cloud locales intentionally contain English fallback for these two
additions. Source ownership and generated Cloud bundle equality are asserted by
the existing operations runtime-key contract. The cumulative English Cloud
inventory increases from 12,474 to 12,476 without weakening the manifest check.
Cloud and aggregate distributions were regenerated, and Cloud's three bundled
locales were synchronized from the generated files.

`npm run verify` passed: strict validation of 4,816 catalogs, zero errors and
120 tests. This includes build reproducibility and source-to-distribution
contracts. The Cloud consumer's focused translation/result tests passed 43
cases; its complete frontend suite passed all 4,295 cases across 300 files.

This catalog change does not itself deploy Cloud or prove live AI task
completion. Cloud keeps the historical execution read model and acceptance
receipts in its own software acceptance change.
