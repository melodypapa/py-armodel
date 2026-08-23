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
1. [ ] IPduPort  (input)

---

## IPduPort — 9-step sub-checklist
- [ ] Step 1 — Sync members & description from spec
- [ ] Step 2 — Write the model class unit test (Red)
- [ ] Step 3 — Implement the model class (Green)
- [ ] Step 4 — Sync description — wipe & rewrite docstrings verbatim from markdown
- [ ] Step 5 — Write the reader/writer round-trip test (Red)
- [ ] Step 6 — Update the parser (reader) & writer
- [ ] Step 7 — Update checklist comment (`# Spec:` + rows; marker deferred)
- [ ] Step 8 — Deviations ⇒ no `# Spec verified:` stamp
- [ ] Step 9 — Verify (9a) + confirm (9b) ⇒ write `# Spec verified:`
