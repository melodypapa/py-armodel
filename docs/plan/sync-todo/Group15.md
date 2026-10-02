# Sync todo: Group 15 — FibexCore communication & topology

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

> **Parent-dependency audit 2026-09-26 (all Group1-20 pending rows, spec-table Base chains):** every pending row's Base row extracted from the R23-11/R4.3.1 markdown (260/293 found; 33 = enums/XSD-only/user-arbitrated) and every parent classified against src stamps + the queue. Findings: DiagnosticEnvCompareCondition (Group14) and MixedContentForUnitNames (Group8) queued NEW above their children; DiagnosticEnvModeElement row-header Base corrected. ESTABLISHED SKIPS (no rows, per precedent): UploadableDesignElement / UploadablePackageElement (attribute-less abstract bases, empty XSD groups — most-derived-base collapse, Group5-audit precedent; appear in Base cells of DynamicPart / MultiplexedIPdu / SecuredIPdu / UserDefinedIPdu rows below); AREnum leaf classes (no Base row by construction); the Firewall member-rule family (user arbitration 2026-08-31: no Class table in either corpus → skipped, see Group1 FirewallRule Done row); ARList (resolved under "List", FO GST Table 9.8, Group9 row).

## Queue (dependency-first)

- [ ] `CommunicationDirectionType` — AREnum — R23-11 markdown · Table 6.33 (CP_TPS_SystemTemplate), p.351 — commit 3378eb624
  - commit: 3378eb624 (feat; steps 1-8; literals renamed ENUM_IN/ENUM_OUT → IN/OUT, verbatim Note + literal descriptions, 6-col checklist; 7 stale test refs updated)
  - note: deviation-tracked entries reviewed (md:2553 = DataMapping member row; v2:1890 package misfile) — informational only, no code deviation
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red) — N/A standalone enum (value form on consuming classes)
  - [x] Step 6 — Update parser & writer (Green) — N/A standalone enum
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations — none new
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-27 (212 passed / 0 failed targeted, lint clean, black-check clean); 9b deferred to batch confirmation (user instruction)

- [x] `TransferPropertyEnum` — AREnum — R23-11 markdown · Table 6.15 (CP_TPS_SystemTemplate), p.327 — **finished, stamped `# Spec verified: R23-11`** (sync commit f3a9dc08d; steps 1-8 commit e6baac031)
  - commit: e6baac031 (feat; steps 1-8; class body already spec-faithful — added mirror test + 6-col checklist)
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red) — class already conformant; mirror test green on first run
  - [x] Step 3 — Implement model class (Green) — no change needed
  - [x] Step 4 — Sync docstrings (wipe + rewrite) — already verbatim, verified vs table
  - [x] Step 5 — Write reader/writer round-trip test (Red) — N/A standalone enum
  - [x] Step 6 — Update parser & writer (Green) — N/A standalone enum
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations — none
  - [x] Step 9 — Verify (9a) + confirm (9b) — 9a re-run 2026-10-02 (1128 Fibex tests passed incl. dedicated TestTransferPropertyEnum, lint clean, black-check clean); 9b user-confirmed 2026-10-02 — Note + 5 literals verbatim in displayed order (de-split 'triggeredOnChange WithoutRepetition'), 6-col AREnum checklist canonical; no deviations; `# Spec verified: R23-11` written after the `# Spec:` line

- [x] `MultiplexedPart` — ARObject — R23-11 markdown · Table 6.76 (CP_TPS_SystemTemplate), p.411 — **finished, stamped `# Spec verified: R23-11`** (sync commit 9ed9d7878; steps 1-8 commit 66512d060)
  - commit: 66512d060 (feat; steps 1-8; verbatim Note + constr_9181, PEP 526 typed list, typed accessors, 6-col checklist; abstract guard kept)
  - note: v2 tracker entry (line 1447) is about StaticPart — informational only
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red) — 2 failed / 4 passed (fabricated docstrings)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red) — covered by existing parser tests (readMultiplexedPartSegmentPositions value-level) via concrete subclasses
  - [x] Step 6 — Update parser & writer (Green) — helpers already complete (readMultiplexedPart/writeMultiplexedPart)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations — none (abstract per table)
  - [x] Step 9 — Verify (9a) + confirm (9b) — 9a re-run 2026-10-02 (51 targeted passed, lint clean, black-check clean); 9b user-confirmed 2026-10-02 — Note + constr_9181 verbatim, Base = ARObject, abstract guard, segmentPosition *→List[SegmentPosition] with Note verbatim, rw via concrete subclasses; no deviations; `# Spec verified: R23-11` written after the `# Spec:` line

- [x] `DynamicPart` — MultiplexedPart — R23-11 markdown · Table 6.74 (CP_TPS_SystemTemplate), p.410 — **finished, stamped `# Spec verified: R23-11`** (sync commit 82138518f; steps 1-8 commit 4211085bc)
  - commit: 4211085bc (feat; steps 1-8; verbatim Note, PEP 526 typed list, typed accessors, 6-col checklist)
  - note: kept `MultiplexedPart, VariationPointCapable` — Base row "ARObject, MultiplexedPart" but DYNAMIC-PART XSD group has VARIATION-POINT (StaticPart precedent, accepted deviation)
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red) — authored test-first (verbatim-docstring asserts fail on old fabricated wording)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red) — covered by parser tests (readDynamicPartDelegates, readMultiplexedIPdu_full) + writer TestWriteDynamicPartAlternative
  - [x] Step 6 — Update parser & writer (Green) — helpers already complete
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations — VariationPointCapable mixin XSD-justified (see note)
  - [x] Step 9 — Verify (9a) + confirm (9b) — 9a re-run 2026-10-02 (30 targeted tests passed, lint clean, black-check clean); 9b user-confirmed 2026-10-02 — Note verbatim, Base = MultiplexedPart, dynamicPartAlternative *→List with Note verbatim, VP mixin XSD-justified (VARIATION-POINT in DYNAMIC-PART group, Rule 0020); no open deviations; `# Spec verified: R23-11` written after the `# Spec:` line

- [x] `SegmentPosition` — ARObject — R23-11 markdown · Table 6.77 (CP_TPS_SystemTemplate), p.412 — **finished, stamped `# Spec verified: R23-11`** (sync commit 6c2d8befb; steps 1-8 commit 9546cf291)
  - commit: 9546cf291 (feat; steps 1-8; verbatim Note + 3 attr notes incl. long segmentPosition note, Optional[T] PEP 526 replacing bare `: ByteOrderEnum = None`, typed accessors + None-no-op, 6-col checklist)
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red) — 2 failed / 2 passed (fabricated docstrings)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red) — covered by parser test readMultiplexedPartSegmentPositions_with_segment (value-level, 3 fields)
  - [x] Step 6 — Update parser & writer (Green) — readSegmentPosition/writeSegmentPosition already complete (all 3 elements)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations — none
  - [x] Step 9 — Verify (9a) + confirm (9b) — 9a re-run 2026-10-02 (model + parser segment tests passed, lint clean, black-check clean); 9b user-confirmed 2026-10-02 — Note + 3 attr Notes verbatim in displayed order (segmentByteOrder/segmentLength/segmentPosition 0..1→Optional), rw coverage; no deviations; `# Spec verified: R23-11` written after the `# Spec:` line

- [ ] `ISignalPort` — CommConnectorPort — R23-11 markdown · Table 6.5 (CP_TPS_SystemTemplate), p.306 — commit b5f92f4b2
  - commit: b5f92f4b2 (feat; steps 1-8; page-split table reconstructed (rows above caption 6.5); verbatim Note + 5 attr notes; Optional[T] PEP 526; handleInvalid now typed HandleInvalidEnum; ddsQosProfile (spec, ref kind) already correctly named ddsQosProfileRef; NEW reader/writer coverage for DATA-FILTER/DDS-QOS-PROFILE-REF/FIRST-TIMEOUT/HANDLE-INVALID (only TIMEOUT was wired); parser+writer tests incl. XSD-order + round-trip)
  - note: HandleInvalidEnum import via TYPE_CHECKING (PEP 563 module; runtime import broke normal load path — circular via Communication.py→RTEEvents→ClientComSpec)
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red) — 3 failed / 1 passed
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red) — parser value-level ×2 + writer full/empty/round-trip
  - [x] Step 6 — Update parser & writer (Green) — readISignalPort/writeISignalPort extended to all 5 attrs in XSD order
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations — none (dataFilter aggr / ddsQosProfile ref→Ref suffix both per rule)
  - [x] Step 9 — Verify (9a) + confirm (9b) — 9a re-run 2026-10-02 (12 targeted tests passed, lint clean, black-check clean); 9b user-confirmed 2026-10-02 — Note + 5 attr Notes verbatim, Base = CommConnectorPort, ddsQosProfile→ddsQosProfileRef ref-suffix naming, dataFilter aggr→Optional[DataFilter], handleInvalid typed HandleInvalidEnum, rw covers all 5 attrs in XSD order; no deviations; `# Spec verified: R23-11` written after the `# Spec:` line

- [x] `ISignalIPduGroup` — FibexElement — R23-11 markdown · Table 6.32 (CP_TPS_SystemTemplate), p.351 — commit 1e758bd44
  - commit: 1e758bd44 (feat; steps 1-8; verbatim Note incl. Tags, PEP 526 types (Optional[CommunicationDirectionType]/Optional[String]/List[RefType]), None-no-op setters + None-guarded adds; NEW NM-PDUS reader+writer coverage (was dropped — silent round-trip loss); XSD order COMMUNICATION-DIRECTION→COMMUNICATION-MODE→CONTAINED-...-REFS→I-SIGNAL-I-PDUS→NM-PDUS)
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red) — 4 failed / 2 passed
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red) — parser NM-PDUS read ×2 new + writer test_nm_pdu_refs + NM-PDUS-empty assert added
  - [x] Step 6 — Update parser & writer (Green) — readISignalIPduGroup + writeISignalIPduGroup extended with NM-PDUS wrapper (NM-PDU-REF-CONDITIONAL/NM-PDU-REF)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations — none
  - [x] Step 9 — Verify (9a) + confirm (9b) — 9a re-run 2026-10-02 (19 targeted tests passed, lint clean, black-check clean); 9b user-confirmed 2026-10-02 — Note (incl. Tags) verbatim, Base = FibexElement, 5 members in displayed order (communicationDirection/communicationMode/containedISignalIPduGroupRefs/iSignalIPduRefs/nmPduRefs) with correct quota shapes, NM-PDUS rw coverage added in prior pass; no deviations; `# Spec verified: R23-11` written after the `# Spec:` line

- [x] `MultiplexedIPdu` — IPdu — R23-11 markdown · Table 6.72 (CP_TPS_SystemTemplate), p.410 — **finished, stamped `# Spec verified: R23-11`** (sync commit 2c2e10293; steps 1-8 commit eba346cb5)
  - commit: eba346cb5 (feat; steps 1-8; verbatim Note + 7 attr notes incl. markdown wrap-spaces ("variation Point"/"short Label" per raw cells), PEP 526 Optional[T] replacing `# type:` comments, triggerMode now typed Optional[TriggerMode]; reader/writer already complete — no change)
  - note: markdown cells carry PDF-wrap spaces verbatim (raw-byte verified per row); test NOTES matched by diff loop
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red) — 2 failed / 2 passed (fabricated docstrings)
  - [x] Step 3 — Implement model class (Green) — class block generated from extracted cells (byte-exact)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red) — covered by parser test_readMultiplexedIPdu_full
  - [x] Step 6 — Update parser & writer (Green) — already complete (7/7 attrs incl. dynamic/static part helpers)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations — TriggerMode class was missing (Rule 0001.10): created, see new row below
  - [x] Step 9 — Verify (9a) + confirm (9b) — 9a re-run 2026-10-02 (Fibex + user-defined tests green, lint clean, black-check clean); 9b user-confirmed 2026-10-02 — 7 attr Notes verbatim (markdown wrap-spaces kept), triggerMode typed Optional[TriggerMode], rw 7/7 pre-existing; no open deviations; `# Spec verified: R23-11` written after the `# Spec:` line

- [x] `TriggerMode` — AREnum — NEW row (discovered 2026-09-27 as missing MultiplexedIPdu.triggerMode member type, Rule 0001.10/0016.4) — R23-11 markdown · Table 6.71 (CP_TPS_SystemTemplate), p.408 — **finished, stamped `# Spec verified: R23-11`** (sync commit 2c2e10293; steps 1-8 commit cc609f42a)
  - commit: cc609f42a (feat; steps 1-8; 4 literals dynamicPartTrigger/none/staticOrDynamicPartTrigger/staticPartTrigger with verbatim descriptions + EnumerationLiteralIndex tags)
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red) — ImportError (class absent)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite) — new class, verbatim from start
  - [x] Step 5 — Write reader/writer round-trip test (Red) — N/A standalone enum (TRIGGER-MODE element round-tripped via MultiplexedIPdu)
  - [x] Step 6 — Update parser & writer (Green) — N/A standalone enum
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations — none
  - [x] Step 9 — Verify (9a) + confirm (9b) — 9a re-run 2026-10-02 (Fibex + user-defined tests green, lint clean, black-check clean); 9b user-confirmed 2026-10-02 — 4 literals verbatim with EnumerationLiteralIndex tags, dedicated mirror test; no open deviations; `# Spec verified: R23-11` written after the `# Spec:` line

- [x] `SecuredIPdu` — IPdu — R23-11 markdown · Table 6.42 (CP_TPS_SystemTemplate), p.368 — **finished, stamped `# Spec verified: R23-11`** (sync commit 2c2e10293; steps 1-8 commit 0a98655a0)
  - commit: 0a98655a0 (feat; steps 1-8; verbatim Note + 7 attr notes (class+test generated from single extraction), PEP 526 types, useSecuredPduHeader now Optional[SecuredPduHeaderEnum]; NEW reader/writer coverage for DYNAMIC-RUNTIME-LENGTH-HANDLING + USE-SECURED-PDU-HEADER per XSD order)
  - note: SecuredPduHeaderEnum was missing (Rule 0001.10) — created, see new row below
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red) — 2 failed / 2 passed (fabricated docstrings)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red) — parser read ×2 new fields + writer XSD-order test
  - [x] Step 6 — Update parser & writer (Green) — readSecuredIPdu/writeSecuredIPdu extended to all 7 attrs
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations — SecuredPduHeaderEnum created (see new row)
  - [x] Step 9 — Verify (9a) + confirm (9b) — 9a re-run 2026-10-02 (Fibex + user-defined tests green, lint clean, black-check clean); 9b user-confirmed 2026-10-02 — 7 attr Notes verbatim, useSecuredPduHeader typed Optional[SecuredPduHeaderEnum], DYNAMIC-RUNTIME-LENGTH-HANDLING + USE-SECURED-PDU-HEADER rw added; no open deviations; `# Spec verified: R23-11` written after the `# Spec:` line

- [x] `SecuredPduHeaderEnum` — AREnum — NEW row (discovered 2026-09-27 as missing SecuredIPdu.useSecuredPduHeader member type, Rule 0001.10/0016.4) — R23-11 markdown · Table 6.43 (CP_TPS_SystemTemplate), p.369 — **finished, stamped `# Spec verified: R23-11`** (sync commit 2c2e10293; steps 1-8 commit 3d5cb55db)
  - commit: 3d5cb55db (feat; steps 1-8; 4 literals noHeader/securedPduHeader08Bit/16Bit/32Bit with verbatim descriptions + EnumerationLiteralIndex tags)
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red) — ImportError (class absent)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite) — new class, verbatim from start
  - [x] Step 5 — Write reader/writer round-trip test (Red) — N/A standalone enum (USE-SECURED-PDU-HEADER round-tripped via SecuredIPdu)
  - [x] Step 6 — Update parser & writer (Green) — N/A standalone enum
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations — none
  - [x] Step 9 — Verify (9a) + confirm (9b) — 9a re-run 2026-10-02 (Fibex + user-defined tests green, lint clean, black-check clean); 9b user-confirmed 2026-10-02 — 4 literals verbatim (noHeader/08Bit/16Bit/32Bit) with EnumerationLiteralIndex tags, dedicated mirror test; no open deviations; `# Spec verified: R23-11` written after the `# Spec:` line

- [x] `UserDefinedIPdu` — IPdu — R23-11 markdown · Table 6.28 — **finished, stamped `# Spec verified: R23-11`** (sync commit 2c2e10293; steps 1-8 commit 78ff524a7)
  - module: M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreCommunication/__init__.py
  - Note: own table = AUTOSAR_CP_TPS_SystemTemplate Table 6.28, p.346 (markdown L9188, caption L9198; R4.3.1 Table 6.32 p.229 exists but R23-11 wins); concrete Class (XSD complexType USER-DEFINED-I-PDU 00052.xsd L128888 abstract="false"); Base most-derived = `IPdu` (Base cell closure ARElement/ARObject/CollectableElement/FibexElement/IPdu/Identifiable/MultilanguageReferrable/PackageableElement/Pdu/Referrable/UploadableDesignElement/UploadablePackageElement; class IPdu(Pdu, ABC) stamped in-file) → current Python base already correct; class NOT VP-capable — complexType sequence = base groups (…PDU, I-PDU) + own group USER-DEFINED-I-PDU (L128872), NO VARIATION-POINT anywhere; aggregated by ARPackage.element; 1 own attribute in displayed order — cddType (String, 0..1, attr; XSD element CDD-TYPE); orphan-intake drift found (unstamped partial sync, queue row still source-TBC): class + verbatim docstrings + 6-column checklist + mirrored model test + parser readUserDefinedIPdu + writer writeUserDefinedIPdu + ARPackage dispatch ALL pre-existed — the only gap was reader/writer TEST coverage (added at Step 5); member type String native — no Rule 0001.10 work; no integration fixture carries USER-DEFINED-I-PDU (self-built round-trip per CryptoServiceCertificate ARPackage-aggregate precedent); docs/plan/deviation/ does not exist, docs/examples/method_deviation_by_class.md + _v2.md have NO entries for this class
  - [x] Step 1 — Sync members & description from spec — Table 6.28 located (markdown L9188; PDF p.346 via pdf_page.py); Class header + Note + Base + Aggregated-by + 1 Attribute row (cddType) extracted in displayed order; Base IPdu + no-VP verified against whole XSD group + complexType (L128872-L128910)
  - [x] Step 2 — Write model class unit test (Red) — N/A red (orphan intake): mirrored test_UserDefinedIPdu.py pre-existed and already matches the SecuredIPdu exemplar shape (defaults, get/set + None no-op, class + accessor docstring pins verbatim); verified 4 passed as-is, no edit
  - [x] Step 3 — Implement model class (Green) — pre-existing impl verified in-spec, no change: most-derived base IPdu; PEP 526 `Optional[String]` field; guarded self-returning setCddType with None no-op; member order = displayed row order
  - [x] Step 4 — Sync docstrings (wipe + rewrite) — pre-existing class docstring + getter/setter docstrings verified verbatim against Table 6.28 Note + cddType Note column; no change
  - [x] Step 5 — Write reader/writer round-trip test (Red) — new tests/test_armodel/parser/test_user_defined_ipdu.py (4 tests: dispatch creates class on ARPackage via readARPackageElements, field values LENGTH + CDD-TYPE, absent CDD-TYPE → None, write→reparse round-trip) + tests/test_armodel/writer/test_user_defined_ipdu.py (3 tests: XSD order LENGTH → CDD-TYPE with values, None cddType omitted, write→reparse round-trip); 11 passed incl. model test — green on first run (impl pre-existed; drift, not red-green)
  - [x] Step 6 — Update parser & writer (Green) — pre-existing impl verified in-spec, no change: readUserDefinedIPdu calls readIPdu base helper exactly once then CDD-TYPE via getChildElementOptionalLiteral; writeUserDefinedIPdu emits USER-DEFINED-I-PDU → writeIPdu once → CDD-TYPE via setChildElementOptionalLiteral (XSD order); dispatch routes USER-DEFINED-I-PDU in readARPackageElements (parser L14683) + writeARPackageElement (writer L14292) — same path as SecuredIPdu; matched name pairs, no chained mutators
  - [x] Step 7 — Update checklist comment — pre-existing checklist verified: 6 columns + release column, rows in source order (getter-first scalar pair), `# Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.28, p.346 (R23-11)`, reader [x] on setCddType row / writer [x] on getCddType row matches call sites; NO `# Spec verified:` — deferred to batch confirmation
  - [x] Step 8 — Deviations — none open (orphan-intake drift recorded in Note: impl/model-test/reader/writer pre-existed unstamped, reader/writer tests were the only gap, added at Step 5; no tracker entries in docs/examples/method_deviation_by_class.md + _v2.md — nothing stale)
  - [x] Step 9 — Verify (9a) + confirm (9b) — 9a re-run 2026-10-02 (Fibex + user-defined tests green, lint clean, black-check clean); 9b user-confirmed 2026-10-02 — cddType 0..1 String verbatim, Base = IPdu, reader/writer tests added at Step 5 (orphan intake); no open deviations; `# Spec verified: R23-11` written after the `# Spec:` line

- [x] `UserDefinedPdu` — Pdu — R23-11 markdown · Table 6.27 — **finished, stamped `# Spec verified: R23-11`** (sync commit 2c2e10293; steps 1-8 commit 78ff524a7)
  - module: M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreCommunication/__init__.py
  - Note: own table = AUTOSAR_CP_TPS_SystemTemplate Table 6.27, p.345 (markdown L9177, caption L9175; R4.3.1 Table 6.31 p.228 exists but R23-11 wins); concrete Class (XSD complexType USER-DEFINED-PDU 00052.xsd L128955 abstract="false"); Base most-derived = `Pdu` (Base cell closure ARElement/ARObject/CollectableElement/FibexElement/Identifiable/MultilanguageReferrable/PackageableElement/Pdu/Referrable/UploadableDesignElement/UploadablePackageElement — NO IPdu; class Pdu(FibexElement, ABC) stamped in-file) → current Python base already correct; class NOT VP-capable — complexType sequence = base groups (…PDU) + own group USER-DEFINED-PDU (L128940), NO VARIATION-POINT anywhere; aggregated by ARPackage.element; 1 own attribute in displayed order — cddType (String, 0..1, attr; XSD element CDD-TYPE); orphan-intake drift found (unstamped partial sync, queue row still source-TBC): class + verbatim docstrings + 6-column checklist + mirrored model test + parser readUserDefinedPdu + writer writeUserDefinedPdu + ARPackage dispatch ALL pre-existed — the only gap was reader/writer TEST coverage (added at Step 5); spec quirk kept verbatim: the Table 6.27 cddType Note itself says "the UserDefinedIPdu" (cross-reference present in R23-11 markdown + XSD documentation); member type String native — no Rule 0001.10 work; no integration fixture carries USER-DEFINED-PDU (self-built round-trip per UserDefinedIPdu precedent); docs/plan/deviation/ does not exist, docs/examples/method_deviation_by_class.md + _v2.md have NO entries for this class
  - [x] Step 1 — Sync members & description from spec — Table 6.27 located (markdown L9177; PDF p.345 via pdf_page.py); Class header + Note + Base + Aggregated-by + 1 Attribute row (cddType) extracted in displayed order; Base Pdu + no-VP verified against whole XSD group (L128940) + complexType (L128955)
  - [x] Step 2 — Write model class unit test (Red) — N/A red (orphan intake): mirrored test_UserDefinedPdu.py pre-existed and already matches the SecuredIPdu exemplar shape (defaults, get/set + None no-op, class + accessor docstring pins verbatim); verified 4 passed as-is, no edit
  - [x] Step 3 — Implement model class (Green) — pre-existing impl verified in-spec, no change: most-derived base Pdu; PEP 526 `Optional[String]` field; guarded self-returning setCddType with None no-op; member order = displayed row order
  - [x] Step 4 — Sync docstrings (wipe + rewrite) — pre-existing class docstring + getter/setter docstrings verified verbatim against Table 6.27 Note + cddType Note column; no change
  - [x] Step 5 — Write reader/writer round-trip test (Red) — new tests/test_armodel/parser/test_user_defined_pdu.py (4 tests: dispatch creates class on ARPackage via readARPackageElements, field values LENGTH + CDD-TYPE, absent CDD-TYPE → None, write→reparse round-trip) + tests/test_armodel/writer/test_user_defined_pdu.py (3 tests: XSD order LENGTH → CDD-TYPE with values, None cddType omitted, write→reparse round-trip); 7 passed green on first run (impl pre-existed; drift, not red-green)
  - [x] Step 6 — Update parser & writer (Green) — pre-existing impl verified in-spec, no change: readUserDefinedPdu calls readPdu base helper exactly once then CDD-TYPE via getChildElementOptionalLiteral; writeUserDefinedPdu emits USER-DEFINED-PDU → writePdu once → CDD-TYPE via setChildElementOptionalLiteral (XSD order); dispatch routes USER-DEFINED-PDU in readARPackageElements (parser L14686) + writeARPackageElement (writer L14293); matched name pairs, no chained mutators
  - [x] Step 7 — Update checklist comment — pre-existing checklist verified: 6 columns + release column, rows in source order (getter-first scalar pair), `# Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.27, p.345 (R23-11)`, reader [x] on setCddType row / writer [x] on getCddType row matches call sites; NO `# Spec verified:` — deferred to batch confirmation
  - [x] Step 8 — Deviations — none open (orphan-intake drift recorded in Note: impl/model-test/reader/writer pre-existed unstamped, reader/writer tests were the only gap, added at Step 5; no tracker entries in docs/examples/method_deviation_by_class.md + _v2.md — nothing stale)
  - [x] Step 9 — Verify (9a) + confirm (9b) — 9a re-run 2026-10-02 (Fibex + user-defined tests green, lint clean, black-check clean); 9b user-confirmed 2026-10-02 — cddType 0..1 String verbatim (spec 'the UserDefinedIPdu' cross-ref kept), Base = Pdu, reader/writer tests added at Step 5 (orphan intake); no open deviations; `# Spec verified: R23-11` written after the `# Spec:` line

- [ ] `SystemSignal` — ARElement — R23-11 markdown · Table 5.23 (CP_TPS_SystemTemplate), p.218 — commit 7c5d9e9d8
  - commit: 7c5d9e9d8 (feat; steps 1-8; verbatim Note + attr notes, PEP 526 types, None-no-op accessors, 6-col checklist)
  - note (Step 8): — None-no-op setters replace overwrite; rw already complete
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations — see below
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-27/28 (6666 passed / 0 failed battery, lint clean, black-check clean); 9b deferred to batch confirmation (user instruction)

- [ ] `TimeRangeType` — ARObject — R23-11 markdown · Table 6.67 (CP_TPS_SystemTemplate), p.413 — commit dcbc6abdb
  - commit: dcbc6abdb (feat; steps 1-8; verbatim Note + attr notes, PEP 526 types, None-no-op accessors, 6-col checklist)
  - note (Step 8): — NEW TimeRangeTypeTolerance XSD-only empty-group class created (Rule 0016.4); TOLERANCE element not read/written (ABSOLUTE-/RELATIVE-TOLERANCE choice members not modeled) — deviation flagged
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations — see below
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-27/28 (6666 passed / 0 failed battery, lint clean, black-check clean); 9b deferred to batch confirmation (user instruction)

- [ ] `TimeRangeTypeTolerance` — ARObject — XSD-only · group TIME-RANGE-TYPE-TOLERANCE (00052.xsd L122919)
  - Note: NEW row (recorded 2026-09-28: TimeRangeType.tolerance member type class created in commit dcbc6abd without own queue row — Rule 0016.4/0017 row-parity; same pattern as the TriggerMode/SecuredPduHeaderEnum NEW rows) — XSD-only: group TIME-RANGE-TYPE-TOLERANCE is an EMPTY group (`<xsd:sequence/>`, atpObject, mmt.qualifiedName="TimeRangeTypeTolerance"), no own Class/Enumeration table in R23-11, R4.3.1 or R4.4.0 corpora; complexType TIME-RANGE-TYPE aggregates it only through the CONSUMING class (AR-OBJECT + TIME-RANGE-TYPE groups), so the class has no own members, no own XML element; Base `ARObject`, `__init__(self)` only.
  - [x] Step 1 — Sync members & description from spec — verified 2026-09-28 against AUTOSAR_00052.xsd group TIME-RANGE-TYPE-TOLERANCE (L122919, EMPTY sequence) + the consuming complexType TIME-RANGE-TYPE (L122908); no R23-11/R4.3.1/R4.4.0 table exists (XSD-only per Rule 0016.3 sweep)
  - [x] Step 2 — Write model class unit test (Red) — N/A new: class + mirrored tests pre-exist from the dcbc6abd pass; TestTimeRangeType (tests/.../FibexCore/CoreCommunication/test_TimeRangeType.py) instantiates TimeRangeTypeTolerance and round-trips it through TimeRangeType.setTolerance/getTolerance with None no-op — adequate for a member-less XSD-only class
  - [x] Step 3 — Implement model class (Green) — verified: `class TimeRangeTypeTolerance(ARObject)` with empty `__init__` matches the EMPTY XSD group exactly (nothing to add, nothing fabricated)
  - [x] Step 4 — Sync docstrings (wipe + rewrite) — verified: class docstring = the XSD group documentation "Maximum allowable deviation" verbatim
  - [x] Step 5 — Write reader/writer round-trip test (Red) — N/A: the class has no own XML element ([—] reader / [—] writer); serialization is owned by the consuming TimeRangeType (its checklist carries reader [x] on setTolerance / writer [x] on getTolerance, Rules 0010–0011)
  - [x] Step 6 — Update parser & writer (Green) — N/A: same reason — nothing to read or write for an empty group
  - [x] Step 7 — Update checklist comment — verified: checklist present in the XSD-only citation form `# Spec: XSD group TIME-RANGE-TYPE-TOLERANCE, AUTOSAR_00052.xsd line 122919 (XSD-only; empty group, no own table in repo corpus)` + `[x] __init__ ... R23-11` row
  - [x] Step 8 — Deviations — none: no members, no placeholders, nothing referenced; TimeRangeType (consumer) stamped R23-11 Table 6.67 in the same file
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-28: 13492 passed / 0 failed, lint + black clean; 9b deferred to batch confirmation (user instruction)
  - module: M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreCommunication/Timing.py
  - commit: dcbc6abd (class created alongside the TimeRangeType sync; steps below record the already-done work for row parity, not new code)
  - [x] Step 1 — Sync members & description from spec — XSD-only derivation: group TIME-RANGE-TYPE-TOLERANCE (xsd:122919) is EMPTY — zero child elements (the ABSOLUTE-/RELATIVE-TOLERANCE choice sits in the surrounding TIME-RANGE-TYPE context, not in this group, and is not modeled — parent-gap flagged on the TimeRangeType row); no spec Note exists in either corpus ⇒ docstring taken from the XSD annotation verbatim ("Maximum allowable deviation"); Base = ARObject (xsd:AR-OBJECT attributeGroup only), concrete, no-arg `__init__`
  - [x] Step 2 — Write model class unit test — 4 tests in test_TimeRangeType.py (initialization defaults / setters round-trip + None no-op via the TimeRangeType surface / class-docstring pin / accessor-docstring verbatim pin)
  - [x] Step 3 — Implement model class (Green) — concrete `ARObject` subclass, zero own members (empty group), abstract guard not required, no-arg `__init__`
  - [x] Step 4 — Sync docstrings (wipe + rewrite) — class docstring = XSD annotation text ("Maximum allowable deviation"); no member docstrings (no members); no `__init__` docstring
  - [—] Step 5 — Write reader/writer round-trip test (Red) — N/A: empty-group artifact class has no own XML serialization; the parent TOLERANCE element read/write gap is the TimeRangeType row's recorded deviation (not re-flagged here)
  - [—] Step 6 — Update parser & writer (Green) — N/A standalone empty class (no elements to read/write)
  - [x] Step 7 — Update checklist comment — 6-column format with release column, single `__init__` row `[x] impl [x] docstring [x] test [—] reader [—] writer R23-11`; citation `# Spec: XSD group TIME-RANGE-TYPE-TOLERANCE, AUTOSAR_00052.xsd line 122919 (XSD-only; empty group, no own table in repo corpus)`
  - [x] Step 8 — Deviations (fixed+recorded in step notes: row created for checklist/queue parity — the class itself carries NO deviations; OPEN OBSERVATIONS reported, not fixed here: (1) NO `# Spec verified:`/`# XSD verified:` stamp — an XSD-only class stamp would be `# XSD verified: AUTOSAR_00052.xsd`, deferred to 9b batch confirmation per batch instruction; (2) NOT exported top-level — Timing.py classes are imported selectively into CoreCommunication/__init__.py (only TransmissionModeDeclaration/TriggerIPduSendCondition) so `armodel.TimeRangeTypeTolerance` does not resolve; export-chain fix belongs to a CoreCommunication export pass (Rule 0007 observation); (3) parent TOLERANCE element not read/written — TimeRangeType row's deviation, out of scope here)
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `TransmissionModeCondition` — ARObject — R23-11 markdown · Table 6.60 (CP_TPS_SystemTemplate), p.393 — commit dcbc6abdb
  - commit: dcbc6abdb (feat; steps 1-8; verbatim Note + attr notes, PEP 526 types, None-no-op accessors, 6-col checklist)
  - note (Step 8): — class note completed ("In all other cases..." sentence added per table); None-no-op setters replace overwrite
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations — see below
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-27/28 (6666 passed / 0 failed battery, lint clean, black-check clean); 9b deferred to batch confirmation (user instruction)

- [ ] `TriggerIPduSendCondition` — ARObject — R23-11 markdown · Table 6.70 (CP_TPS_SystemTemplate), p.399 — commit dcbc6abdb
  - commit: dcbc6abdb (feat; steps 1-8; verbatim Note + attr notes, PEP 526 types, None-no-op accessors, 6-col checklist)
  - note (Step 8): — wrap-space "Com_Trigger IPDUSend" kept verbatim per markdown; checklist upgraded to 6-col; accessor names getModeDeclarationRefs/addModeDeclarationRef preserved (rw contract)
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations — see below
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-27/28 (6666 passed / 0 failed battery, lint clean, black-check clean); 9b deferred to batch confirmation (user instruction)

- [ ] `CyclicTiming` — Describable — R23-11 markdown · Table 6.65 (CP_TPS_SystemTemplate), p.408 — commit dcbc6abdb
  - commit: dcbc6abdb (feat; steps 1-8; verbatim Note + attr notes, PEP 526 types, None-no-op accessors, 6-col checklist)
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations — see below
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-27/28 (6666 passed / 0 failed battery, lint clean, black-check clean); 9b deferred to batch confirmation (user instruction)

- [ ] `EventControlledTiming` — Describable — R23-11 markdown · Table 6.66 (CP_TPS_SystemTemplate), p.409 — commit dcbc6abdb
  - commit: dcbc6abdb (feat; steps 1-8; verbatim Note + attr notes, PEP 526 types, None-no-op accessors, 6-col checklist)
  - note (Step 8): — note kept "a event driven" per table verbatim
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations — see below
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-27/28 (6666 passed / 0 failed battery, lint clean, black-check clean); 9b deferred to batch confirmation (user instruction)

- [ ] `FlexrayChannelName` — AREnum — R23-11 markdown · Table 3.35 (CP_TPS_SystemTemplate), p.89 — commit 7c137656f
  - commit: 7c137656f (feat; steps 1-8; verbatim Note + attr notes, PEP 526 types, None-no-op accessors, 6-col checklist)
  - note (Step 8): — literal renamed channel_B → CHANNEL_B (case fix, no external usages)
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations — see below
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-27/28 (6666 passed / 0 failed battery, lint clean, black-check clean); 9b deferred to batch confirmation (user instruction)

- [ ] `PncGatewayTypeEnum` — AREnum — R23-11 markdown · Table 3.5 (CP_TPS_SystemTemplate), p.55 — commit 7c137656f
  - commit: 7c137656f (feat; steps 1-8; verbatim Note + attr notes, PEP 526 types, None-no-op accessors, 6-col checklist)
  - note (Step 8): — literals renamed ENUM_ACTIVE/ENUM_NONE/ENUM_PASSIVE → ACTIVE/NONE/PASSIVE
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations — see below
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-27/28 (6666 passed / 0 failed battery, lint clean, black-check clean); 9b deferred to batch confirmation (user instruction)

- [ ] `TransmissionModeTiming` — ARObject — R23-11 markdown · Table 6.62 (CP_TPS_SystemTemplate), p.394 — commit dcbc6abdb
  - commit: dcbc6abdb (feat; steps 1-8; verbatim Note + attr notes, PEP 526 types, None-no-op accessors, 6-col checklist)
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations — see below
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-27/28 (6666 passed / 0 failed battery, lint clean, black-check clean); 9b deferred to batch confirmation (user instruction)

- [ ] `TransmissionModeDeclaration` — ARObject — R23-11 markdown · Table 6.59 (CP_TPS_SystemTemplate), p.392 — commit dcbc6abdb
  - commit: dcbc6abdb (feat; steps 1-8; verbatim Note + attr notes, PEP 526 types, None-no-op accessors, 6-col checklist)
  - note (Step 8): — accessor contract preserved (getModeDrivenFalseConditions/addModeDrivenFalseCondition etc. used by parser+writer); legacy test_Timing.py None-overwrite/None-append assertions updated to the None-guard contract
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations — see below
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-27/28 (6666 passed / 0 failed battery, lint clean, black-check clean); 9b deferred to batch confirmation (user instruction)
