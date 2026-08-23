# Sync todo — IPduPort

Input class: `IPduPort`
Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.3, p.304
Release: R23-11

## Confirmed closure (user gate: "Only IPduPort")
- **IPduPort** — input, unstamped. Sync from beginning.
- IPduSignalProcessingEnum — member type consumed by `IPduPort.iPduSignalProcessing`; **explicitly excluded by user** (left unstamped).
- CommConnectorPort — base, stamped `R23-11`, skipped.
- ARObject / Identifiable / MultilanguageReferrable / Referrable — std base classes, stamped, skipped.
- Boolean / TimeValue — primitive member types, stamped, skipped.

## Queue (dependency-first)
1. [x] IPduPort  (input) — commit 738043f

---

## IPduPort — 9-step sub-checklist
- [x] Step 1 — Sync members & description from spec
- [x] Step 2 — Write the model class unit test (Red)
- [x] Step 3 — Implement the model class (Green)
- [x] Step 4 — Sync description — wipe & rewrite docstrings verbatim from markdown
- [x] Step 5 — Write the reader/writer round-trip test (Red)
- [x] Step 6 — Update the parser (reader) & writer
- [x] Step 7 — Update checklist comment (`# Spec:` + rows; marker deferred)
- [x] Step 8 — Deviations ⇒ no `# Spec verified:` stamp
- [x] Step 9 — Verify (9a) + confirm (9b) ⇒ write `# Spec verified:`
