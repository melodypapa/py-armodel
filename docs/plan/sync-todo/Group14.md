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
- [x] `DiagnosticRoutineTypeEnum` — AREnum — R23-11 markdown · Table 12.25 (CP_TPS_BSWModuleDescriptionTemplate), p.247 — commit f9dc536d5 (stamped 2026-10-02, # Spec verified: R23-11)
- [x] `DiagnosticServiceRequestCallbackTypeEnum` — AREnum — R23-11 markdown · Table 13.35 (CP_TPS_SoftwareComponentTemplate), p.780 — commit 77c7312cc (stamped 2026-10-02, # Spec verified: R23-11)
- [x] `DiagnosticValueAccessEnum` — AREnum — R23-11 markdown · Table 12.22 (CP_TPS_BSWModuleDescriptionTemplate), p.246 — commit 85e9c3f3b (stamped 2026-10-02, # Spec verified: R23-11)
- [x] `DtcFormatTypeEnum` — AREnum — R4.3.1 markdown · Table 13.30 (AUTOSAR_TPS_SoftwareComponentTemplate), p.770 (R4.3.1 fallback — no R23-11 table) — commit f376d8339 (stamped 2026-10-02, # Spec verified: R4.3.1; 2026-10-02 re-check ADDED the missed page-split literal uds(2))
- [x] `DtcKindEnum` — AREnum — R4.3.1 markdown · Table 13.16 (AUTOSAR_TPS_SoftwareComponentTemplate), p.760 (R4.3.1 fallback — no R23-11 table) — commit 8b62eec62 (stamped 2026-10-02, # Spec verified: R4.3.1)
- [x] `ServiceDiagnosticRelevanceEnum` — AREnum — R23-11 markdown · Table 7.58 (CP_TPS_SoftwareComponentTemplate), p.609 — commit da3a2d353 (stamped 2026-10-02, # Spec verified: R23-11)
- [x] `DiagnosticCapabilityElement` — ServiceNeeds — R23-11 markdown · Table 13.15 (CP_TPS_SoftwareComponentTemplate), p.754 — commit caf7dc341 (stamped 2026-10-02, # Spec verified: R23-11; 2026-10-02 re-check fixed Spec page p.753→p.754)
- [x] `DiagnosticCommunicationManagerNeeds` — DiagnosticCapabilityElement — R23-11 markdown · Table 13.34 (CP_TPS_SoftwareComponentTemplate), p.779 — commit 8c487102b (stamped 2026-10-02, # Spec verified: R23-11; 2026-10-02 re-check fixed Spec page p.777→p.779)
- [x] `DiagnosticEventInfoNeeds` — DiagnosticCapabilityElement — R23-11 markdown · Table 13.23 (CP_TPS_SoftwareComponentTemplate), p.761 — commit 99f3db39c (stamped 2026-10-02, # Spec verified: R23-11; 2026-10-02 re-check completed dual Spec lines + added accepted-legacy dtcKind tracker row)
- [x] `DiagnosticRoutineNeeds` — DiagnosticCapabilityElement — R23-11 markdown · Table 13.36 (CP_TPS_SoftwareComponentTemplate), p.780 — commit 9f1a4310b (stamped 2026-10-02, # Spec verified: R23-11; 2026-10-02 re-check fixed Spec pages p.778→p.780 + R4.3.1 Table 13.33 id, added accepted-legacy ridNumber tracker row)
- [ ] `DiagnosticValueNeeds` — DiagnosticCapabilityElement — R23-11 markdown · Table 13.39 (CP_TPS_SoftwareComponentTemplate), p.780
  - module: M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py
  - note (Step 1): R23-11 attrs: dataLength (PositiveInteger), diagnosticValueAccess (DiagnosticValueAccessEnum), fixedLength (Boolean), processingStyle (DiagnosticProcessingStyleEnum), all 0..1. didNumber ABSENT from R23-11 table, present in R4.3.1 → Rule 0019 legacy member. Field renamed DidNumber → didNumber; type corrected Integer → PositiveInteger (R4.3.1 row).
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - note (Steps 5/6): DIAGNOSTIC-VALUE-ACCESS + PROCESSING-STYLE converted to typed enum tokens; writer tests updated from fabricated 'read'/'asynchronous' to spec tokens.
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - note (Step 8): ONE accepted legacy deviation (didNumber — Rule 0019); DidNumber→didNumber rename + type fix recorded
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-26 (12335 passed / 0 failed, lint clean, black-check clean); 9b deferred to batch confirmation (user instruction)
- [ ] `DtcStatusChangeNotificationNeeds` — DiagnosticCapabilityElement — R23-11 markdown · Table 13.32 (CP_TPS_SoftwareComponentTemplate), p.776
  - module: M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py
  - note (Step 1): R23-11 attr: notificationTime (DiagnosticClearDtcNotificationEnum, 0..1; wire NOTIFICATION-TIME). dtcFormatType ABSENT from R23-11 table, present in R4.3.1 → Rule 0019 legacy member (j1939/obd). Writer was MISSING NOTIFICATION-TIME emission entirely — added.
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - note (Steps 5/6): rw converted to typed enums (DTC-FORMAT-TYPE, NOTIFICATION-TIME); NOTIFICATION-TIME coverage added both directions.
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - note (Step 8): ONE accepted legacy deviation (dtcFormatType — Rule 0019) — subject to 9b batch confirmation
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-26 (12335 passed / 0 failed, lint clean, black-check clean); 9b deferred to batch confirmation (user instruction)
- [ ] `CryptoServiceNeeds` — ServiceNeeds — R23-11 markdown · Table 13.9 (CP_TPS_SoftwareComponentTemplate), p.733
  - module: M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py
  - note (Step 1): Four attrs: algorithmFamily (String), algorithmMode (String), cryptoKeyDescription (String), maximumKeyLength (PositiveInteger), all 0..1; wire ALGORITHM-FAMILY/ALGORITHM-MODE/CRYPTO-KEY-DESCRIPTION/MAXIMUM-KEY-LENGTH. Drift: fabricated docstring, bare-typed fields, untyped accessors, old checklist; reader covered only MAXIMUM-KEY-LENGTH, writer likewise — 3 String attrs added to both.
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - note (Steps 5/6): ALGORITHM-FAMILY/ALGORITHM-MODE/CRYPTO-KEY-DESCRIPTION added both directions (getChildElementOptionalString/setChildElementOptionalString)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - note (Step 8): no deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-26 (12335 passed / 0 failed, lint clean, black-check clean); 9b deferred to batch confirmation (user instruction)
- [ ] `DiagEventDebounceCounterBased` — DiagEventDebounceAlgorithm — R23-11 markdown · Table 12.33 (CP_TPS_BSWModuleDescriptionTemplate), p.260
  - module: M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py
  - note (Step 1): Nine attrs (0..1 each): counterBasedFdcThresholdStorageValue (Integer), counterDecrementStepSize (Integer), counterFailedThreshold (Integer), counterIncrementStepSize (Integer), counterJumpDown (Boolean — src wrongly Integer), counterJumpDownValue (Integer), counterJumpUp (Boolean — src wrongly Integer), counterJumpUpValue (Integer), counterPassedThreshold (Integer); wire names = UPPER-KEBAB per XSD group DIAG-EVENT-DEBOUNCE-COUNTER-BASED (INTEGER-VALUE-VARIATION-POINT/BOOLEAN-VALUE-VARIATION-POINT types — only the plain value path is modeled; the VP-bearing variant is not, see Step 8). Drift: fabricated docstring, bare-typed fields, untyped accessors, old checklist; reader read NOTHING of the 9 attrs, writer had NO implementation (empty helper).
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - note (Steps 5/6): reader: all 9 elements added; writer: all 9 elements added in XSD order.
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - note (Step 8): model limitation recorded — XSD wires these attrs as INTEGER-/BOOLEAN-VALUE-VARIATION-POINT (value XOR value+VARIATION-POINT); the model stores the plain value and rw covers that path only (consistent with repo-wide handling); subject to 9b batch review
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-26 (12335 passed / 0 failed, lint clean, black-check clean); 9b deferred to batch confirmation (user instruction)
- [ ] `SignalServiceTranslationElementProps` — Identifiable — R23-11 markdown · Table 6.342 (CP_TPS_SystemTemplate), p.735
  - module: M2/AUTOSARTemplates/CommonStructure/SignalServiceTranslation.py
  - note (Step 1): Three attrs: element (DataPrototypeReference, 0..1, aggr — wire ELEMENT wrapper with choice DATA-PROTOTYPE-IN-PORT-INTERFACE-REF / IMPLEMENTATION-DATA-TYPE-ELEMENT-IN-PORT-INTERFACE-REF), filter (DataFilter, 0..1, aggr), transmissionTrigger (Boolean, 0..1, attr). Placeholder RESOLVED: DataPrototypeReference family now exists — element typed as DataPrototypeInPortInterfaceRef (TYPE_CHECKING import, nested-quoted annotations); ELEMENT rw added both directions via the existing DataPrototypeInPortInterfaceRef helpers (the ImplDataTypeElement variant hits notImplemented). Drift: class Note + checklist were glued INSIDE the docstring — split; checklist lacked release column; setElement lacked return annotation.
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - note (Steps 5/6): ELEMENT coverage added (parser + writer via writeDataPrototypeInPortInterfaceRef); filter/transmissionTrigger rw pre-existed.
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - note (Step 8): model limitation — only the DATA-PROTOTYPE-IN-PORT-INTERFACE-REF choice of the ELEMENT wrapper is supported; the IMPLEMENTATION-DATA-TYPE-ELEMENT variant hits notImplemented; subject to 9b batch review
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-26 (12335 passed / 0 failed, lint clean, black-check clean); 9b deferred to batch confirmation (user instruction)
- [x] `DiagnosticServiceClass` — DiagnosticCommonElement — already verified (R23-11 · Table 4.25, p.69; short-circuit 2026-09-26; source/stamp commit `6b514727f`)
  - module: M2/AUTOSARTemplates/DiagnosticExtract/CommonService.py
  - note (short-circuit 2026-09-26): class body already matches the spec — verbatim Note docstring, 6-col checklist with only __init__ (abstract, ZERO attribute rows — spec Attribute row is \-\), abstract guard, Base most-derived = DiagnosticCommonElement (already correct), concrete subclasses not queued (Group7 precedent). Deviation check found nothing new; marker deferred to batch confirmation like the other rows. No code change needed — row flipped without a class commit.
- [ ] `DiagnosticJumpToBootLoaderEnum` — AREnum — R23-11 markdown · Table 4.31 (CP_TPS_DiagnosticExtractTemplate), p.74
  - module: M2/AUTOSARTemplates/DiagnosticExtract/Dcm.py
  - note (Step 1): Note = "This enumeration contains the options for jumping to a boot loader." 5 literals in DISPLAYED order noBoot(0), oemBoot(1), oemBootRespApp(3), systemSupplierBoot(2), systemSupplierBootRespApp(4) — src already matches incl. values (XSD kebab tokens NO-BOOT etc.) and __init__; already-verified short-circuit applied: only the Spec page number drifted (p.75 → p.74 per pdf_page) and the checklist lacked the marker row.
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - note (Steps 5/6): N/A — standalone AREnum, serialized as attribute value on DiagnosticSession.jumpToBootLoader (Rules 0010-0011)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - note (Step 8): no deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-26 (12333 passed / 0 failed, lint clean, black-check clean); 9b deferred to batch confirmation (user instruction)
- [ ] `DiagnosticLogicalOperatorEnum` — AREnum — R23-11 markdown · Table 4.37 (CP_TPS_DiagnosticExtractTemplate), p.80
  - module: M2/AUTOSARTemplates/DiagnosticExtract/EnvironmentalCondition.py
  - note (Step 1): Note = "Logical AND and OR operation (&&, ||)" (markdown HTML-entity &#124;&#124; de-escaped). Literals: logicalAnd(0), logicalOr(1) — src already matches incl. values and __init__; already-verified short-circuit applied: only the Spec page drifted (p.81 → p.80 per pdf_page).
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - note (Steps 5/6): N/A — standalone AREnum, serialized as attribute value on DiagnosticEnvConditionFormula.op (Rules 0010-0011)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - note (Step 8): no deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-26 (12333 passed / 0 failed, lint clean, black-check clean); 9b deferred to batch confirmation (user instruction)
- [x] `DiagnosticEnvConditionFormulaPart` — ARObject — already verified (R23-11 · Table 4.38, p.81; short-circuit 2026-09-26)
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
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-26 (12339 passed / 0 failed, lint clean, black-check clean); 9b deferred to batch confirmation (user instruction)
- [ ] `DiagnosticEnvConditionFormula` — DiagnosticEnvConditionFormulaPart — R23-11 markdown · Table 4.36 (CP_TPS_DiagnosticExtractTemplate), p.80
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
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-26 (12339 passed / 0 failed, lint clean, black-check clean); 9b deferred to batch confirmation (user instruction)
- [ ] `DiagnosticEnvCompareCondition` — DiagnosticEnvConditionFormulaPart (abstract) — R23-11 markdown · Table 4.39 (CP_TPS_DiagnosticExtractTemplate), p.82
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
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-26 (12339 passed / 0 failed, lint clean, black-check clean); 9b deferred to batch confirmation (user instruction)
- [ ] `DiagnosticEnvModeElement` — Referrable (abstract) — R23-11 markdown · Table 4.44 (CP_TPS_DiagnosticExtractTemplate), p.89
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
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-26 (12339 passed / 0 failed, lint clean, black-check clean); 9b deferred to batch confirmation (user instruction)