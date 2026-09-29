# Posture English copy and company Ratings Tree — 2026-09-29

## Scope

- Repair English Posture Overview values that were persisted in the canonical
  catalog as literal `\\uXXXX` escape sequences.
- Move remaining Domain-detail status/readiness copy out of frontend literals.
- Add copy for a real company-hierarchy Ratings Tree while retaining the
  separate SPM Rating Breakdown explanation.

## Authority boundary

Ratings Tree labels describe parent/subsidiary company hierarchy. A child
company without an independent score must remain `Unrated`; consumer code must
not copy the parent score or derive one from relationship confidence.

The existing `ratingTree*` labels continue to belong to the Engine-authored
SPM Rating Breakdown (risk vector → finding explanation). They are not renamed
into company hierarchy semantics.

## Verification

- Source catalog contains no literal Unicode escape values under the repaired
  English `code.external.engineer*` keys.
- Code/aggregate distributions rebuilt from source.
- Consumer synchronization and release/deployment evidence are recorded in
  flyto-code.
