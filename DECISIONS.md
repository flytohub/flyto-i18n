# Decisions

## 2026-08-22 - Operations Room controls are upstream-owned

Decision: keep the output-wall labels, target-selection errors, optional
mission input label, protocol/status labels, and management entry in the
reviewed Cloud source catalogs, then generate both Cloud and aggregate runtime
bundles from those values.

Reason: Flyto2 Cloud still renders these keys through its `wt()` helper. A
consumer-side bundled copy is not an alternate source of truth and must remain
safe to replace from `flyto-i18n/dist/cloud` without deleting live UI copy.

## 2026-08-14 - Public positioning starts with one shared translation fix

Decision: present `flyto-i18n` with one public role: "Fix a translation once
and share it across every Flyto2 product, docs, and website surface." Lead with
an existing locale-catalog edit and the real validation/build commands. Keep
architecture, SEO, product inventory, and synchronization detail below that
first result.

Reason: the user problem is duplicate product copy drifting across repositories
and locales. Broad ecosystem and AI-oriented discovery language obscured the
repository's narrow ownership boundary and could be confused with Flyto2 Core,
AI, Cloud, or Warroom product capabilities.
## 2026-08-14 - AI Space identity and local voice are locale-owner first

Decision: own the 19 identity and local-voice settings keys in every Cloud
locale's `aiSpace.json` source catalog and publish them through the generated
Cloud and aggregate bundles. Keep wake-word detection on-device and describe
wake words as routing only, with no permission grant or approval bypass.

Reason: identity and voice controls are visible product and safety copy.
Source presence in every locale prevents consumer-side English fallback from
becoming the localization strategy or weakening the voice safety boundary.

## 2026-08-14 - War Room camera copy states the local image contract

Decision: describe the War Room camera surface as local and near-real-time,
with explicit delayed, disconnected, permission-denied, and starting states.
Treat `spaces.ops.live` as room connection state, describe the surface as
mission operations and evidence, and state that camera images remain on the
device.

Reason: the current surface presents local camera images and does not establish
continuous video, a live-camera stream, inference, or recording. Product copy
must communicate only capabilities and privacy properties the runtime provides.

## 2026-08-13 - Operations room copy follows the accepted Cloud UI

Decision: publish `aiSpace.workspace.openOperations` exactly as `Operations
room`, `作戰室`, and `作战室` in the three official locales, with exact
source-to-distribution regression coverage.

Reason: these user-approved labels are the product contract. The earlier
open-console wording was stale and must not override the accepted Cloud UI.

## 2026-08-13 - Cloud bundled runtime copy migrates additively

Decision: import the reviewed Cloud-bundled runtime gap into the three official
Cloud source locales as an additive migration. Preserve all existing i18n keys,
pin the exact imported namespace contract, and generate the runtime union from
this repository after migration.

Reason: the Cloud bundle contained 134 runtime keys absent from the published
i18n bundle, while i18n already contained newer cumulative Space Operations
copy. An additive, tested merge makes i18n authoritative without losing either
side and prevents the consumer bundle from becoming a competing catalog.

## 2026-08-09 - Report export format copy is catalog-owned

Decision: keep the Reports export selector and PowerPoint format name in the
additive `code.reports.*` catalog. English, Traditional Chinese, and Simplified
Chinese are reviewed together; every other supported Code locale carries the
deterministic English fallback until native review.

Reason: the export control is visible product and accessibility copy. Keeping
it in `flyto-i18n` avoids a hard-coded frontend label while preserving one
translation source for generated and bundled Code locales.

## 2026-08-08 - Cloud copy converges from workflows upward

Decision: name the three product levels `Workflows -> AI Space -> AI Workflow
War Room`. Keep device, robot, camera, gateway, and MCP language inside optional
adapter and resource controls instead of using it to define the AI Space.

Reason: Flyto2 starts from reusable software workflows and must remain useful
without physical hardware. AI Space is the composition boundary, while the War
Room is the execution and evidence surface; hardware is one possible adapter.

## 2026-08-01 - Translation owners pull private consumer source

Decision: `flyto-i18n` owns the scheduled and manual Cloud-key import. It uses
the existing `FLYTO_CLOUD_TOKEN` only to read the private consumer and to open
a reviewed PR in this repository after complete source and distribution
verification. Flyto2 Cloud retains a credential-free validation projection.

Reason: localization catalogs and generated bundles are owned here. Pull
ownership removes an unnecessary cross-repository write secret from Cloud,
keeps source-to-dist validation in one trust boundary, and still provides an
hourly recovery path when a Cloud push cannot dispatch this private workflow.

## 2026-07-30 - AI Space product copy is catalog-owned

Decision: keep the complete `aiSpace.*` namespace in `locales/cloud`, with
reviewed non-empty English, Traditional Chinese, and Simplified Chinese source
catalogs. Flyto Cloud may keep an empty emergency override object, but normal
product copy must arrive through generated `dist/cloud` bundles.

Reason: folder-scoped Physical AI controls are safety- and workflow-facing
product text. A second catalog inside the consumer hides missing keys, prevents
normal translation review, and can silently fall back to embedded English.

## 2026-07-30 - Dependency labels summarize independent policy axes

Decision: localize the AI Space dependency editor as automatic or custom, then
describe safety response, task consequence, evidence, substitution, confidence,
freshness, recovery, retry, and active phases independently. Labels such as
mission critical, safety critical, required, assistive, and optional are derived
UI summaries only and are never a persisted dependency level.

Reason: one camera, microphone, speaker, elevator, or robot endpoint can be
optional in one workflow phase and safety-critical in another. A device-class
label or fixed severity ladder would hide that context and make translated UI
copy appear more authoritative than the execution contract.

## 2026-07-28 - Attack-validation safety copy is catalog-owned

Decision: keep the Red Team, Pulse, BYO, confidence, authorization mode,
owned/canary scope, TLS safety, and remediation/retest copy under the additive
`code.attackValidation.*` namespace. Review English and Traditional Chinese
directly, and synchronize deterministic English fallbacks to every other Code
locale until native translations are reviewed.

Reason: the attack-validation cockpit communicates authorization and safety
boundaries that must not disappear, drift, or become hard-coded when the
operator changes locale.

## 2026-07-29 - Safety-envelope and benchmark terms stay in one namespace

Decision: proof-of-control, proof-pack eligibility, allowlist, kill-switch,
audit-chain, hard-budget, cost-settlement, and tenant-local benchmark copy
remain additive members of `code.attackValidation.*`. English, Traditional
Chinese, and Simplified Chinese are reviewed together before rebuilding every
Code and aggregate distribution.

Reason: these labels determine whether an operator understands that an active
security test is authorized, bounded, auditable, and locally measured. Splitting
them into page-owned literals would let frontend and Engine safety contracts
drift across locales.

## 2026-07-23 - CE repository onboarding copy is bundled locally

Decision: keep the Community direct-repository URL form, supported-host hint,
validation errors, connect action, and scan-start state in the `code` locale
catalogs and generated distribution bundles.

Reason: first-run self-hosted CE must remain understandable without a network
translation service, including before any external provider connection exists.

## 2026-06-21 - Project memory bootstrapped

Decision: track Flyto2 product-line role, repo boundary, state, roadmap, tasks,
and handoffs in this repo.

Reason: `flyto-i18n` must be maintainable by future agents without relying on
conversation memory.

## 2026-07-18 - Public multilingual SEO contract lives in flyto-i18n

Decision: keep landing/docs/blog locale metadata, `hreflang` templates,
sitemap references, Open Graph locale mapping, and keyword-intent evidence in
`seo/public-surfaces.json`, then generate `dist/seo-manifest.json`.

Reason: the three public Flyto2 surfaces need the same multilingual SEO
contract. Keeping it here avoids stale per-site copies and lets translation,
locale metadata, and public SEO planning evolve together.
