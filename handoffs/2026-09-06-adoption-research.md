# Adoption research copy handoff

Status: Active. No release is claimed.

Source: `locales/code/*/research.json`, 137 keys per locale. English and the two
Chinese locales have reviewed values; the remaining locales use the existing
English fallback policy. Keep this as the sole source owner, then rebuild
tracked Code and aggregate distributions. Consumer: flyto-code's private
Adoption research workspace. No CE publication is part of this work.

Run `npm run verify`, `flyto-index verify . --strict --full-scan --json`, and
`flyto-index task validate` before merge. Consumer CI and deployment pins must
reference the merged locale revision, not a private worktree copy.
