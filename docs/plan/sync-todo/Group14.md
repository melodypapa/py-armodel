# Sync todo: Group 14 — ServiceNeeds & Diagnostics

Input: full-repo orphan audit 2026-09-23 (unstamped ∧ untracked, M2 only) · Queue order = row order
(resume = first class row still `[ ]`; all class rows `[x]` = sync finished — Rule 0017.3)
> **Rule — already-verified short-circuit (added 2026-09-04):** before running the 9-step
> sync for a row, check whether the class already carries `# Spec verified: <RELEASE>` or
> `# XSD verified: <xsd-file>` in its own class body (verify the marker in the source — a
> row in this todo is not proof). If it does **and** a quick deviation check finds nothing
> new (base vs the spec `Base` closure, member types vs its table, verbatim docstrings,
> reader/writer coverage, checklist shape per Rules 0002/0012), **skip the 9 steps**: mark
> the row `- [x] <Class> — already verified (<marker>, <file>)` and move on. If the check
> finds a new deviation, do **not** mark it verified — keep the row queued, run the steps
> for the deviation only, and record it in Step 8 (Rule 0012.3: an existing marker is not
> proof).

> **Parent-dependency audit 2026-09-26 (all Group1-20 pending rows, spec-table Base chains):** every pending row's Base row extracted from the R23-11/R4.3.1 markdown (260/293 found; 33 = enums/XSD-only/user-arbitrated) and every parent classified against src stamps + the queue. Findings: DiagnosticEnvCompareCondition (Group14) and MixedContentForUnitNames (Group8) queued NEW above their children; DiagnosticEnvModeElement row-header Base corrected. ESTABLISHED SKIPS (no rows, per precedent): UploadableDesignElement / UploadablePackageElement (attribute-less abstract bases, empty XSD groups — most-derived-base collapse, Group5-audit precedent; appear in Base cells of the DiagnosticExtract family this file queues); AREnum leaf classes (no Base row by construction); the Firewall member-rule family (user arbitration 2026-08-31: no Class table in either corpus → skipped, see Group1 FirewallRule Done row); ARList (resolved under "List", FO GST Table 9.8, Group9 row).

## Queue (dependency-first)

- [x] `DiagnosticAudienceEnum` — AREnum — R23-11 markdown · Table 13.17 (CP_TPS_SoftwareComponentTemplate), p.754 — commit 80d64e8f1 (stamped 2026-10-02, # Spec verified: R23-11)
- [x] `DiagnosticClearDtcNotificationEnum` — AREnum — R23-11 markdown · Table 13.33 (CP_TPS_SoftwareComponentTemplate), p.776 — commit 2415d2157 (stamped 2026-10-02, # Spec verified: R23-11)
- [x] `DiagnosticProcessingStyleEnum` — AREnum — R23-11 markdown · Table 12.23 (CP_TPS_BSWModuleDescriptionTemplate), p.247 — commit d07b0d014 (stamped 2026-10-02, # Spec verified: R23-11)
- [x] `DiagnosticRoutineTypeEnum` — AREnum — R23-11 markdown · Table 12.25 (CP_TPS_BSWModuleDescriptionTemplate), p.247 — **finished, stamped
  - module: M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py
  - note (Step 1): Note = "This enumerator specifies the different types of diagnostic routines." Literals: asynchronous(0), synchronous(1) — values matched src. Drift: fabricated docstring/comments, __init__ docstring, old checklist.
  - note (2026-10-02 re-check): checklist re-formatted to the 6-column AREnum shape (Columns line + enum-form note + __init__ row)
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - note (Step 8): no deviations
  - [x] Step 9 — Verify (9a) + confirm (9b) — 9a re-run 2026-10-02 (full suite 16300 passed / 1 failed = the pre-existing unrelated integration round-trip on gitignored *SystemMapping.arxml fixtures, documented at session start; targeted tests + member-annotation gate + npm run lint + black-check clean); 9b user-confirmed 2026-10-02 (checklist re-formatted to 6-column AREnum shape)

- [x] `DiagnosticServiceRequestCallbackTypeEnum` — AREnum — R23-11 markdown · Table 13.35 (CP_TPS_SoftwareComponentTemplate), p.780 — **finished, stamped
  - module: M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py
  - note (Step 1): Note = "This represents the ability to define whether a Service Request Notification was used in the role of a manufacturer or a supplier." Literals: requestCallbackTypeManufacturer(0), requestCallbackTypeSupplier(1) — values matched src. Drift: fabricated docstring/comments, __init__ docstring, old checklist.
  - note (2026-10-02 re-check): checklist re-formatted to the 6-column AREnum shape
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - note (Step 8): no deviations
  - [x] Step 9 — Verify (9a) + confirm (9b) — 9a re-run 2026-10-02 (full suite 16300 passed / 1 failed = the pre-existing unrelated integration round-trip on gitignored *SystemMapping.arxml fixtures, documented at session start; targeted tests + member-annotation gate + npm run lint + black-check clean); 9b user-confirmed 2026-10-02

- [x] `DiagnosticValueAccessEnum` — AREnum — R23-11 markdown · Table 12.22 (CP_TPS_BSWModuleDescriptionTemplate), p.246 — **finished, stamped
  - module: M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py
  - note (Step 1): Note = "Defines the access of the configured diagnostic current values which will be used by the Dem or Dcm module." Literals: readOnly(0), readWrite(1), writeOnly(2 — spec Note cell itself ends with a stray comma before Tags; kept verbatim) — values matched src. Drift: fabricated docstring/comments, __init__ docstring, old checklist.
  - note (2026-10-02 re-check): checklist re-formatted to the 6-column AREnum shape
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - note (Step 8): no deviations
  - [x] Step 9 — Verify (9a) + confirm (9b) — 9a re-run 2026-10-02 (full suite 16300 passed / 1 failed = the pre-existing unrelated integration round-trip on gitignored *SystemMapping.arxml fixtures, documented at session start; targeted tests + member-annotation gate + npm run lint + black-check clean); 9b user-confirmed 2026-10-02

- [x] `DtcFormatTypeEnum` — AREnum — R4.3.1 markdown · Table 13.30 (AUTOSAR_TPS_SoftwareComponentTemplate), p.770 (R4.3.1 fallback — no R23-11 table) — **finished, stamped
  - module: M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py
  - note (Step 1): R4.3.1-only class (R23-11 markdown + pdf_page scan negative) → release R4.3.1. Note = "This enumeration specifies the DTC format." Literals: j1939(0), obd(1) (atp.EnumerationValue tags). src was an EMPTY stub — literals added; empty-pinning test updated to spec.
  - note (2026-10-02 re-check): THE 2026-10-02 RE-CHECK FOUND AND ADDED THE MISSED PAGE-SPLIT LITERAL uds(2) ('Defines the UDS DTC format. Tags: atp.EnumerationValue=2') — Red→Green (2 failed → 267 passed); table 13.30 body carries j1939/obd rows + a scattered uds text block before the caption
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - note (Step 8): no deviations; R4.3.1 provenance recorded in the Spec line
  - [x] Step 9 — Verify (9a) + confirm (9b) — 9a re-run 2026-10-02 (full suite 16300 passed / 1 failed = the pre-existing unrelated integration round-trip on gitignored *SystemMapping.arxml fixtures, documented at session start; targeted tests + member-annotation gate + npm run lint + black-check clean); 9b user-confirmed 2026-10-02 (missing uds(2) literal added)

- [x] `DtcKindEnum` — AREnum — R4.3.1 markdown · Table 13.16 (AUTOSAR_TPS_SoftwareComponentTemplate), p.760 (R4.3.1 fallback — no R23-11 table) — **finished, stamped
  - module: M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py
  - note (Step 1): R4.3.1-only class → release R4.3.1. Note = "This enumeration defines the possible kinds of diagnostic monitors regarding the OBD relevance." Literals: emissionRelatedDtc(0), nonEmmissionRelatedDtc(1) (de-split from "nonEmmis- sionRelated Dtc"; double-m spelling per spec). src was an EMPTY stub — literals added; empty-pinning test updated to spec.
  - note (2026-10-02 re-check): checklist re-formatted to the 6-column AREnum shape; NO scattered extra literals this time (table body clean)
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - note (Step 8): no deviations; R4.3.1 provenance recorded in the Spec line
  - [x] Step 9 — Verify (9a) + confirm (9b) — 9a re-run 2026-10-02 (full suite 16300 passed / 1 failed = the pre-existing unrelated integration round-trip on gitignored *SystemMapping.arxml fixtures, documented at session start; targeted tests + member-annotation gate + npm run lint + black-check clean); 9b user-confirmed 2026-10-02

- [x] `ServiceDiagnosticRelevanceEnum` — AREnum — R23-11 markdown · Table 7.58 (CP_TPS_SoftwareComponentTemplate), p.609 — **finished, stamped
  - module: M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py
  - note (Step 1): Note = "This enumeration provides values to describe the diagnostic relevance of a SwcServiceDependency (specifically if the aggregated ServiceNeeds itself does not indicate a relevance for diagnostics)." Literals: isNotRelevant(0), isRelevant(1) — values matched src. Drift: fabricated docstring/comments, __init__ docstring, old checklist.
  - note (2026-10-02 re-check): checklist re-formatted to the 6-column AREnum shape
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - note (Step 8): no deviations
  - [x] Step 9 — Verify (9a) + confirm (9b) — 9a re-run 2026-10-02 (full suite 16300 passed / 1 failed = the pre-existing unrelated integration round-trip on gitignored *SystemMapping.arxml fixtures, documented at session start; targeted tests + member-annotation gate + npm run lint + black-check clean); 9b user-confirmed 2026-10-02

- [x] `DiagnosticCapabilityElement` — ServiceNeeds — R23-11 markdown · Table 13.15 (CP_TPS_SoftwareComponentTemplate), p.754 — **finished, stamped
  - module: M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py
  - note (Step 1): R23-11 markdown Table 13.15, p.753. ABSTRACT Class; Base most-derived = `ServiceNeeds` (already correct); not VP-capable per own XSD group. Three attrs: audience (DiagnosticAudienceEnum, *, attr → AUDIENCES/AUDIENCE wrapper items, token map DIAGNOSTIC_AUDIENCE_XML_MAP), diagRequirement (DiagRequirementIdString, 0..1, attr), securityAccessLevel (PositiveInteger, 0..1, attr). Drift: fabricated class docstring, __init__ docstring, bare-typed fields, untyped accessors, old 4-col checklist; read/writeDiagnosticCapabilityElement covered ONLY the ServiceNeeds base — all three attrs were DROPPED on round-trip for the whole subclass family.
  - note (2026-10-02 re-check): Spec page corrected p.753 → p.754 per pdf_page (checklist header updated)
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - note (Step 8): no deviations
  - [x] Step 9 — Verify (9a) + confirm (9b) — 9a re-run 2026-10-02 (full suite 16300 passed / 1 failed = the pre-existing unrelated integration round-trip on gitignored *SystemMapping.arxml fixtures, documented at session start; targeted tests + member-annotation gate + npm run lint + black-check clean); 9b user-confirmed 2026-10-02 (Spec page fixed p.753→p.754)

- [x] `DiagnosticCommunicationManagerNeeds` — DiagnosticCapabilityElement — R23-11 markdown · Table 13.34 (CP_TPS_SoftwareComponentTemplate), p.779 — **finished, stamped
  - module: M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py
  - note (Step 1): One attr serviceRequestCallbackType (DiagnosticServiceRequestCallbackTypeEnum, 0..1, attr; wire SERVICE-REQUEST-CALLBACK-TYPE, token REQUEST-CALLBACK-TYPE-MANUFACTURER/SUPPLIER via DIAGNOSTIC_SERVICE_REQUEST_CALLBACK_TYPE_XML_MAP). Drift: fabricated docstring, __init__ docstring, bare-typed field, untyped accessors, old checklist; reader read generic Literal (not spec enum).
  - note (2026-10-02 re-check): Spec page corrected p.777 → p.779 per pdf_page (checklist header updated)
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - note (Step 8): no deviations
  - [x] Step 9 — Verify (9a) + confirm (9b) — 9a re-run 2026-10-02 (full suite 16300 passed / 1 failed = the pre-existing unrelated integration round-trip on gitignored *SystemMapping.arxml fixtures, documented at session start; targeted tests + member-annotation gate + npm run lint + black-check clean); 9b user-confirmed 2026-10-02 (Spec page fixed p.777→p.779)

- [x] `DiagnosticEventInfoNeeds` — DiagnosticCapabilityElement — R23-11 markdown · Table 13.23 (CP_TPS_SoftwareComponentTemplate), p.761 — **finished, stamped
  - module: M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py
  - note (Step 1): R23-11 attrs: obdDtcNumber, udsDtcNumber (PositiveInteger, 0..1). dtcKind (DtcKindEnum) ABSENT from R23-11 table, present in R4.3.1 → Rule 0019 legacy member kept (R4.3.1 Note verbatim, release column R4.3.1, dual Spec lines). Writer was MISSING OBD-DTC-NUMBER emission entirely — added.
  - note (2026-10-02 re-check): second `# Spec:` line completed to the Rule 0019 format (R4.3.1/AUTOSAR_TPS_SoftwareComponentTemplate.pdf, Table 13.22, p.767); accepted-legacy dtcKind tracker row ADDED to method_deviation_by_class_v2.md (was deferred)
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - note (Step 8): ONE accepted legacy deviation (dtcKind — Rule 0019, dual Spec lines) — 9b user-confirmed 2026-10-02
  - [x] Step 9 — Verify (9a) + confirm (9b) — 9a re-run 2026-10-02 (full suite 16300 passed / 1 failed = the pre-existing unrelated integration round-trip on gitignored *SystemMapping.arxml fixtures, documented at session start; targeted tests + member-annotation gate + npm run lint + black-check clean); 9b user-confirmed 2026-10-02 (accepted-legacy dtcKind deviation confirmed)

- [x] `DiagnosticRoutineNeeds` — DiagnosticCapabilityElement — R23-11 markdown · Table 13.36 (CP_TPS_SoftwareComponentTemplate), p.780 — **finished, stamped
  - module: M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py
  - note (Step 1): R23-11 attr: diagRoutineType (DiagnosticRoutineTypeEnum, 0..1; wire DIAG-ROUTINE-TYPE). ridNumber ABSENT from R23-11 table, present in R4.3.1 → Rule 0019 legacy member (Note verbatim incl. spec's 'the a function' typo). Field renamed RidNumber → ridNumber (lowerCamel per spec member name).
  - note (2026-10-02 re-check): Spec pages corrected: R23-11 p.778 → p.780; R4.3.1 `# Spec:` line completed (Table 13.33, p.780); accepted-legacy ridNumber tracker row ADDED
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - note (Step 8): ONE accepted legacy deviation (ridNumber — Rule 0019); RidNumber→ridNumber rename recorded — 9b user-confirmed 2026-10-02
  - [x] Step 9 — Verify (9a) + confirm (9b) — 9a re-run 2026-10-02 (full suite 16300 passed / 1 failed = the pre-existing unrelated integration round-trip on gitignored *SystemMapping.arxml fixtures, documented at session start; targeted tests + member-annotation gate + npm run lint + black-check clean); 9b user-confirmed 2026-10-02 (accepted-legacy ridNumber deviation confirmed + Spec pages fixed)

- [x] `DiagnosticValueNeeds` — DiagnosticCapabilityElement — R23-11 markdown · Table 13.39 (CP_TPS_SoftwareComponentTemplate), p.782 — **finished, stamped
  - module: M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py
  - note (Step 1): R23-11 attrs: dataLength (PositiveInteger), diagnosticValueAccess (DiagnosticValueAccessEnum), fixedLength (Boolean), processingStyle (DiagnosticProcessingStyleEnum), all 0..1. didNumber ABSENT from R23-11 table, present in R4.3.1 → Rule 0019 legacy member. Field renamed DidNumber → didNumber; type corrected Integer → PositiveInteger (R4.3.1 row).
  - note (2026-10-02 re-check): Spec pages corrected: R23-11 p.780 → p.782; R4.3.1 `# Spec:` line completed (Table 13.36, p.783); accepted-legacy didNumber tracker row ADDED
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - note (Step 8): ONE accepted legacy deviation (didNumber — Rule 0019); DidNumber→didNumber rename + type fix recorded — 9b user-confirmed 2026-10-02
  - [x] Step 9 — Verify (9a) + confirm (9b) — 9a re-run 2026-10-02 (full suite 16300 passed / 1 failed = the pre-existing unrelated integration round-trip on gitignored *SystemMapping.arxml fixtures, documented at session start; targeted tests + member-annotation gate + npm run lint + black-check clean); 9b user-confirmed 2026-10-02 (accepted-legacy didNumber deviation confirmed + Spec pages fixed)

- [x] `DtcStatusChangeNotificationNeeds` — DiagnosticCapabilityElement — R23-11 markdown · Table 13.32 (CP_TPS_SoftwareComponentTemplate), p.776 — **finished, stamped
  - module: M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py
  - note (Step 1): R23-11 attr: notificationTime (DiagnosticClearDtcNotificationEnum, 0..1; wire NOTIFICATION-TIME). dtcFormatType ABSENT from R23-11 table, present in R4.3.1 → Rule 0019 legacy member (j1939/obd). Writer was MISSING NOTIFICATION-TIME emission entirely — added.
  - note (2026-10-02 re-check): R4.3.1 `# Spec:` line completed (Table 13.29, p.769); accepted-legacy dtcFormatType tracker row ADDED
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - note (Step 8): ONE accepted legacy deviation (dtcFormatType — Rule 0019) — 9b user-confirmed 2026-10-02
  - [x] Step 9 — Verify (9a) + confirm (9b) — 9a re-run 2026-10-02 (full suite 16300 passed / 1 failed = the pre-existing unrelated integration round-trip on gitignored *SystemMapping.arxml fixtures, documented at session start; targeted tests + member-annotation gate + npm run lint + black-check clean); 9b user-confirmed 2026-10-02 (accepted-legacy dtcFormatType deviation confirmed)

- [x] `CryptoServiceNeeds` — ServiceNeeds — R23-11 markdown · Table 13.9 (CP_TPS_SoftwareComponentTemplate), p.733 — **finished, stamped
  - module: M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py
  - note (Step 1): Four attrs: algorithmFamily (String), algorithmMode (String), cryptoKeyDescription (String), maximumKeyLength (PositiveInteger), all 0..1; wire ALGORITHM-FAMILY/ALGORITHM-MODE/CRYPTO-KEY-DESCRIPTION/MAXIMUM-KEY-LENGTH. Drift: fabricated docstring, bare-typed fields, untyped accessors, old checklist; reader covered only MAXIMUM-KEY-LENGTH, writer likewise — 3 String attrs added to both.
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - note (Step 8): no deviations
  - [x] Step 9 — Verify (9a) + confirm (9b) — 9a re-run 2026-10-02 (full suite 16300 passed / 1 failed = the pre-existing unrelated integration round-trip on gitignored *SystemMapping.arxml fixtures, documented at session start; targeted tests + member-annotation gate + npm run lint + black-check clean); 9b user-confirmed 2026-10-02

- [x] `DiagEventDebounceCounterBased` — DiagEventDebounceAlgorithm — R23-11 markdown · Table 12.33 (CP_TPS_BSWModuleDescriptionTemplate), p.260 — **finished, stamped
  - module: M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py
  - note (Step 1): Nine attrs (0..1 each): counterBasedFdcThresholdStorageValue (Integer), counterDecrementStepSize (Integer), counterFailedThreshold (Integer), counterIncrementStepSize (Integer), counterJumpDown (Boolean — src wrongly Integer), counterJumpDownValue (Integer), counterJumpUp (Boolean — src wrongly Integer), counterJumpUpValue (Integer), counterPassedThreshold (Integer); wire names = UPPER-KEBAB per XSD group DIAG-EVENT-DEBOUNCE-COUNTER-BASED (INTEGER-VALUE-VARIATION-POINT/BOOLEAN-VALUE-VARIATION-POINT types — only the plain value path is modeled; the VP-bearing variant is not, see Step 8). Drift: fabricated docstring, bare-typed fields, untyped accessors, old checklist; reader read NOTHING of the 9 attrs, writer had NO implementation (empty helper).
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - note (Step 8): model limitation recorded — XSD wires these attrs as INTEGER-/BOOLEAN-VALUE-VARIATION-POINT (value XOR value+VARIATION-POINT); the model stores the plain value and rw covers that path only (consistent with repo-wide handling) — 9b user-ACCEPTED 2026-10-02
  - [x] Step 9 — Verify (9a) + confirm (9b) — 9a re-run 2026-10-02 (full suite 16300 passed / 1 failed = the pre-existing unrelated integration round-trip on gitignored *SystemMapping.arxml fixtures, documented at session start; targeted tests + member-annotation gate + npm run lint + black-check clean); 9b user-confirmed 2026-10-02 (VP-wiring model limitation accepted)

- [x] `SignalServiceTranslationElementProps` — Identifiable — R23-11 markdown · Table 6.342 (CP_TPS_SystemTemplate), p.735 — **finished, stamped
  - module: M2/AUTOSARTemplates/CommonStructure/SignalServiceTranslation.py
  - note (Step 1): Three attrs: element (DataPrototypeReference, 0..1, aggr — wire ELEMENT wrapper with choice DATA-PROTOTYPE-IN-PORT-INTERFACE-REF / IMPLEMENTATION-DATA-TYPE-ELEMENT-IN-PORT-INTERFACE-REF), filter (DataFilter, 0..1, aggr), transmissionTrigger (Boolean, 0..1, attr). Placeholder RESOLVED: DataPrototypeReference family now exists — element typed as DataPrototypeInPortInterfaceRef (TYPE_CHECKING import, nested-quoted annotations); ELEMENT rw added both directions via the existing DataPrototypeInPortInterfaceRef helpers (the ImplDataTypeElement variant hits notImplemented). Drift: class Note + checklist were glued INSIDE the docstring — split; checklist lacked release column; setElement lacked return annotation.
  - note (2026-10-02 re-check): 2026-10-02: setFilter return annotation added (setters return self); the user-arbitrated getElement shadowing conflict resolved by the Identifiable registry refactor to referrable* (commit 4fd223786) — the subclass keeps the spec-attr accessor getElement()/setElement() unshadowed
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - note (Step 8): model limitation — only the DATA-PROTOTYPE-IN-PORT-INTERFACE-REF choice of the ELEMENT wrapper is supported; the IMPLEMENTATION-DATA-TYPE-ELEMENT variant hits notImplemented — 9b user-ACCEPTED 2026-10-02
  - [x] Step 9 — Verify (9a) + confirm (9b) — 9a re-run 2026-10-02 (full suite 16300 passed / 1 failed = the pre-existing unrelated integration round-trip on gitignored *SystemMapping.arxml fixtures, documented at session start; targeted tests + member-annotation gate + npm run lint + black-check clean); 9b user-confirmed 2026-10-02 (ELEMENT-choice limitation accepted + Identifiable refactor resolved the getElement clash)

- [x] `DiagnosticServiceClass` — DiagnosticCommonElement — already verified (R23-11 · Table 4.25, p.69; short-circuit 2026-09-26; source/stamp commit `6b514727f`)
  - module: M2/AUTOSARTemplates/DiagnosticExtract/CommonService.py
  - note (short-circuit 2026-09-26): class body already matches the spec — verbatim Note docstring, 6-col checklist with only __init__ (abstract, ZERO attribute rows — spec Attribute row is \-\), abstract guard, Base most-derived = DiagnosticCommonElement (already correct), concrete subclasses not queued (Group7 precedent). Deviation check found nothing new; marker deferred to batch confirmation like the other rows. No code change needed — row flipped without a class commit.
- [x] `DiagnosticJumpToBootLoaderEnum` — AREnum — R23-11 markdown · Table 4.31 (CP_TPS_DiagnosticExtractTemplate), p.74 — **finished, stamped
  - module: M2/AUTOSARTemplates/DiagnosticExtract/Dcm.py
  - note (Step 1): Note = "This enumeration contains the options for jumping to a boot loader." 5 literals in DISPLAYED order noBoot(0), oemBoot(1), oemBootRespApp(3), systemSupplierBoot(2), systemSupplierBootRespApp(4) — src already matches incl. values (XSD kebab tokens NO-BOOT etc.) and __init__; already-verified short-circuit applied: only the Spec page number drifted (p.75 → p.74 per pdf_page) and the checklist lacked the marker row.
  - note (2026-10-02 re-check): test_Dcm.py module docstring page ref updated p.75 → p.74
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - note (Step 8): no deviations
  - [x] Step 9 — Verify (9a) + confirm (9b) — 9a re-run 2026-10-02 (full suite 16300 passed / 1 failed = the pre-existing unrelated integration round-trip on gitignored *SystemMapping.arxml fixtures, documented at session start; targeted tests + member-annotation gate + npm run lint + black-check clean); 9b user-confirmed 2026-10-02

- [x] `DiagnosticLogicalOperatorEnum` — AREnum — R23-11 markdown · Table 4.37 (CP_TPS_DiagnosticExtractTemplate), p.80 — **finished, stamped
  - module: M2/AUTOSARTemplates/DiagnosticExtract/EnvironmentalCondition.py
  - note (Step 1): Note = "Logical AND and OR operation (&&, ||)" (markdown HTML-entity &#124;&#124; de-escaped). Literals: logicalAnd(0), logicalOr(1) — src already matches incl. values and __init__; already-verified short-circuit applied: only the Spec page drifted (p.81 → p.80 per pdf_page).
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - note (Steps 5/6): N/A — standalone AREnum, serialized as attribute value on the consuming class (Rules 0010-0011)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - note (Step 8): OP literal-value choice (XSD wire tokens LOGICAL-AND/LOGICAL-OR as enum values, consistent with DiagnosticJumpToBootLoaderEnum) — 9b user-ACCEPTED 2026-10-02
  - [x] Step 9 — Verify (9a) + confirm (9b) — 9a re-run 2026-10-02 (full suite 16300 passed / 1 failed = the pre-existing unrelated integration round-trip on gitignored *SystemMapping.arxml fixtures, documented at session start; targeted tests + member-annotation gate + npm run lint + black-check clean); 9b user-confirmed 2026-10-02 (wire-token values accepted)

- [x] `DiagnosticEnvConditionFormulaPart` — ARObject — R23-11 markdown · Table 4.38 (CP_TPS_DiagnosticExtractTemplate), p.81 — **finished, stamped `# Spec verified: R23-11`** (sync commit 66e22b5a4; short-circuit 2026-09-26)
  - module: M2/AUTOSARTemplates/DiagnosticExtract/EnvironmentalCondition.py
  - note (short-circuit 2026-09-26): class body already matches the spec — verbatim Note docstring, 6-col checklist with only __init__ (abstract, ZERO attribute rows), abstract guard, Base = ARObject (already correct). Deviation check found nothing new; marker deferred to batch confirmation. No code change needed.
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - note (Steps 5/6): N/A — abstract, no own attributes and no own XML element
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - note (Step 8): no deviations
  - [x] Step 9 — Verify (9a) + confirm (9b) — 9a re-run 2026-10-02 (full suite 16300 passed / 1 failed = the pre-existing unrelated integration round-trip on gitignored *SystemMapping.arxml fixtures; targeted tests + npm run lint + black-check clean); 9b user-confirmed 2026-10-02 — abstract, Table 4.38 p.81, Note verbatim, Base = ARObject, ZERO attribute rows, abstract guard, checklist 1/1, no deviations; `# Spec verified: R23-11` written after the `# Spec:` line
- [x] `DiagnosticEnvConditionFormula` — DiagnosticEnvConditionFormulaPart — R23-11 markdown · Table 4.36 (CP_TPS_DiagnosticExtractTemplate), p.80
  - module: M2/AUTOSARTemplates/CommonStructure/../DiagnosticExtract/EnvironmentalCondition.py
  - note (Step 1): class was already largely synced in the Group7 pass — verbatim Note, typed fields, 6-col checklist. This pass: added missing setter return annotations (PEP 563 module — bare self-reference), verified OP wire values (DiagnosticLogicalOperatorEnum stores XSD tokens LOGICAL-AND/LOGICAL-OR as literal values — pre-existing decision, OP needs no token map; recorded for 9b review vs the markdown literal values logicalAnd/logicalOr).
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - note (Steps 5/6): rw helpers (NRC-VALUE/OP/PARTS + nested formula recursion) pre-existed and pass the new round-trip test.
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - note (Step 8): OP literal-value choice (wire tokens as values) predates this sync — flagged for 9b review, not changed
  - [x] Step 9 — Verify (9a) + confirm (9b) — 9a re-run 2026-10-02 (full suite 16300 passed / 1 failed = the pre-existing unrelated integration round-trip on gitignored *SystemMapping.arxml fixtures; targeted tests + npm run lint + black-check clean); 9b user-confirmed 2026-10-02 — Table 4.36 p.80, class Note + 3 attr Notes verbatim, Base = DiagnosticEnvConditionFormulaPart, attrs nrcValue/op/part(*) in displayed order with correct quota shapes, setter return annotations added, rw covers NRC-VALUE/OP/PARTS + formula recursion, OP wire-token values accepted (consistent with DiagnosticLogicalOperatorEnum 9b), no deviations; `# Spec verified: R23-11` written after the `# Spec:` line
- [x] `DiagnosticEnvCompareCondition` — DiagnosticEnvConditionFormulaPart (abstract) — R23-11 markdown · Table 4.39 (CP_TPS_DiagnosticExtractTemplate), p.82
  - module: M2/AUTOSARTemplates/DiagnosticExtract/EnvironmentalCondition.py
  - note (Step 1): abstract; Base most-derived = DiagnosticEnvConditionFormulaPart (created this pass — src class was MISSING, queued per the 2026-09-26 parent-dependency audit). One attr compareType (DiagnosticCompareTypeEnum, 0..1, attr; wire COMPARE-TYPE; Note cell carries the spec's own 'This attributes' typo, kept verbatim). New enum DiagnosticCompareTypeEnum created too (Table 4.40, p.83 — 6 literals isEqual..isGreaterOrEqual; wire tokens IS-EQUAL.. via DIAGNOSTIC_COMPARE_TYPE_XML_MAP). XSD formula PARTS choice wires only the CONCRETE condition elements — the abstract CompareCondition has no own element, so the reusable read/writeDiagnosticEnvCompareCondition helpers exist but are not dispatched from the formula loop (concrete subclasses DiagnosticEnvDataCondition/EnvDataElementCondition/EnvModeCondition are NOT queued/modeled — report at 9b).
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - note (Steps 5/6): reusable read/writeDiagnosticEnvCompareCondition helpers added (token map); helper-level round-trip test passes; formula-loop dispatch intentionally not added (abstract element never appears in valid XML).
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - note (Step 8): concrete-subclass gap (3 classes, not queued) + helper-not-dispatched recorded — subject to 9b batch review
  - [x] Step 9 — Verify (9a) + confirm (9b) — 9a re-run 2026-10-02 (full suite 16300 passed / 1 failed = the pre-existing unrelated integration round-trip on gitignored *SystemMapping.arxml fixtures; targeted tests + npm run lint + black-check clean); 9b user-confirmed 2026-10-02 — abstract, Table 4.39 p.82, class Note + compareType Note verbatim (spec 'This attributes' typo kept), Base = DiagnosticEnvConditionFormulaPart, compareType 0..1 Optional, reusable rw helper + COMPARE-TYPE token map; STALE STEP-8 NOTE CORRECTED: the concrete subclasses DiagnosticEnvDataCondition/EnvDataElementCondition/EnvModeCondition ARE modeled (EnvironmentalCondition.py:312/372/455) and the formula PARTS loop dispatches all of them (parser:10982-10997) — the abstract class itself correctly has no direct dispatch (only concrete conditions appear in valid XML); no deviations; `# Spec verified: R23-11` written after the `# Spec:` line
- [x] `DiagnosticEnvModeElement` — Referrable (abstract) — R23-11 markdown · Table 4.44 (CP_TPS_DiagnosticExtractTemplate), p.89
  - module: M2/AUTOSARTemplates/DiagnosticExtract/EnvironmentalCondition.py
  - note (Step 1): CORRECTION OF THE CORRECTION — the 2026-09-26 parent-audit note here claimed Table 4.44 Base = ARObject , DiagnosticEnvCompareCondition , DiagnosticEnvConditionFormulaPart, but those Base rows belong to the sibling DiagnosticEnvModeCondition (md L2383/2420/2511); the actual Table 4.44 Base cell (md L2533) = 'ARObject , Referrable' → most-derived = Referrable — the ORIGINAL src base was CORRECT; the audit's re-base instruction was the error and was NOT applied (a trial re-base broke the MRO/constructor contract and was reverted). Zero attribute rows. Checklist page fixed p.83 → p.89 (pdf_page). Concrete subclasses (DiagnosticEnvBswModeElement/EnvSwcModeElement) not queued/modeled — DiagnosticEnvironmentalCondition.modeElement aggregation rw remains unwired (pre-existing gap, out of queue scope) — report at 9b.
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - note (Steps 5/6): N/A — abstract, no own attributes and no own XML element
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - note (Step 8): no deviations in class scope; audit-claim correction + aggregation gap recorded for 9b
  - [x] Step 9 — Verify (9a) + confirm (9b) — 9a re-run 2026-10-02 (full suite 16300 passed / 1 failed = the pre-existing unrelated integration round-trip on gitignored *SystemMapping.arxml fixtures; targeted tests + npm run lint + black-check clean); 9b user-confirmed 2026-10-02 — abstract, Table 4.44 p.89, Note verbatim, Base = Referrable (audit re-base claim was the error; original src base correct), ZERO attribute rows, checklist 1/1; the former Step-8 gap (DiagnosticEnvironmentalCondition.modeElement aggregation rw) FIXED at 9b before stamping per user instruction: PModeInSystemInstanceRef added (XSD-only, 00052 l.87429, '# XSD verified: AUTOSAR_00052.xsd'), both mode elements' modeIRef retyped (RefType → typed InstanceRefs) with MODE-IREF rw wired both directions (R4.3.1 00044 structure verified identical); no deviations remain; `# Spec verified: R23-11` written after the `# Spec:` line
