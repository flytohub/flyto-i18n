# workflows/

Human workflow notes for recurring maintenance tasks. These files are operator
playbooks, not executable automation.

## Use

Read the matching workflow before making broad i18n changes:

- `bugfix.md`: small correction or missing-key repair.
- `implementation.md`: new capability or scope-level change.
- `refactor.md`: script or schema cleanup.
- `wrap-up.md`: verification and handoff checklist.

Automation lives in `scripts/`; long-lived state lives in `STATE.md`,
`DECISIONS.md`, and `handoffs/`.
