# 2026-09-21 — External Intelligence quality and learning copy

## Scope

Flyto2 Code now exposes an External Intelligence Quality / Learning surface
backed by Engine evidence. This catalog update provides the reviewed runtime
copy for that surface; it does not create or change detector verdicts.

## Copy contract

Added 23 source-owned Code keys covering:

- the Quality & Learning tab;
- coverage and uncertainty metrics;
- versioned detector-quality tables;
- reviewed precision and labeled recall labels;
- recent observation history;
- measurement limitations and empty/error/loading states.

English, Traditional Chinese and Simplified Chinese have reviewed copy. The
other Code locales use the established explicit English-fallback pattern for
these additive keys.

## Truth boundary

The copy deliberately avoids claiming global detector accuracy. Reviewed
precision and labeled recall are described as metrics over explicitly reviewed
or verified labels only. Missing labels, stale evidence and unavailable sources
must not be interpreted as a clean result.

## Verification

- Strict catalog validation passed for all 4,854 source files.
- Code and aggregate distributions were regenerated for all supported locales.
- Consumer TypeScript, component tests and browser acceptance remain owned by
  flyto-code and are recorded in its paired release work.
