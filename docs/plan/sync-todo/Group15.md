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
  - [—] Step 5 — Write reader/writer round-trip test (Red) — N/A standalone enum (value form on consuming classes)
  - [—] Step 6 — Update parser & writer (Green) — N/A standalone enum
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations — none new
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-27 (212 passed / 0 failed targeted, lint clean, black-check clean); 9b deferred to batch confirmation (user instruction)

- [x] `ContainedIPduCollectionSemanticsEnum` — AREnum — already verified (R23-11 · Table 6.40, p.357; short-circuit 2026-09-27)
  - module: M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreCommunication/__init__.py
  - note (short-circuit 2026-09-27): class body already carries `# Spec verified: R23-11 (2026-09-26, user 9b confirmation)` — verbatim Note docstring, both literals (lastIsBest idx 0 / queued idx 1) with verbatim literal descriptions + EnumerationLiteralIndex tags, 6-col checklist with only `__init__` (enum value form, reader/writer [—]). Deviation check found nothing new. No code change needed — row flipped without a class commit.

- [ ] `TransferPropertyEnum` — AREnum — R23-11 markdown · Table 6.15 (CP_TPS_SystemTemplate), p.327 — commit e6baac031
  - commit: e6baac031 (feat; steps 1-8; class body already spec-faithful — added mirror test + 6-col checklist)
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red) — class already conformant; mirror test green on first run
  - [x] Step 3 — Implement model class (Green) — no change needed
  - [x] Step 4 — Sync docstrings (wipe + rewrite) — already verbatim, verified vs table
  - [—] Step 5 — Write reader/writer round-trip test (Red) — N/A standalone enum
  - [—] Step 6 — Update parser & writer (Green) — N/A standalone enum
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations — none
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-27 (206 passed / 0 failed, lint clean, black-check clean); 9b deferred to batch confirmation (user instruction)

- [ ] `MultiplexedPart` — ARObject — R23-11 markdown · Table 6.76 (CP_TPS_SystemTemplate), p.411 — commit 66512d060
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
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-27 (256 passed / 0 failed, lint clean, black-check clean); 9b deferred to batch confirmation (user instruction)

- [ ] `DynamicPart` — MultiplexedPart — R23-11 markdown · Table 6.74 (CP_TPS_SystemTemplate), p.410 — commit 4211085bc
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
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-27 (313 passed / 0 failed, lint clean, black-check clean); 9b deferred to batch confirmation (user instruction)

- [ ] `SegmentPosition` — ARObject — R23-11 markdown · Table 6.77 (CP_TPS_SystemTemplate), p.412 — commit 9546cf291
  - commit: 9546cf291 (feat; steps 1-8; verbatim Note + 3 attr notes incl. long segmentPosition note, Optional[T] PEP 526 replacing bare `: ByteOrderEnum = None`, typed accessors + None-no-op, 6-col checklist)
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red) — 2 failed / 2 passed (fabricated docstrings)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red) — covered by parser test readMultiplexedPartSegmentPositions_with_segment (value-level, 3 fields)
  - [x] Step 6 — Update parser & writer (Green) — readSegmentPosition/writeSegmentPosition already complete (all 3 elements)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations — none
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-27 (329 passed / 0 failed, lint clean, black-check clean); 9b deferred to batch confirmation (user instruction)

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
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-27 (504 passed / 0 failed, lint clean, black-check clean); 9b deferred to batch confirmation (user instruction)

- [ ] `ISignalIPduGroup` — FibexElement — R23-11 markdown · Table 6.32 (CP_TPS_SystemTemplate), p.351 — commit 1e758bd44
  - commit: 1e758bd44 (feat; steps 1-8; verbatim Note incl. Tags, PEP 526 types (Optional[CommunicationDirectionType]/Optional[String]/List[RefType]), None-no-op setters + None-guarded adds; NEW NM-PDUS reader+writer coverage (was dropped — silent round-trip loss); XSD order COMMUNICATION-DIRECTION→COMMUNICATION-MODE→CONTAINED-...-REFS→I-SIGNAL-I-PDUS→NM-PDUS)
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red) — 4 failed / 2 passed
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red) — parser NM-PDUS read ×2 new + writer test_nm_pdu_refs + NM-PDUS-empty assert added
  - [x] Step 6 — Update parser & writer (Green) — readISignalIPduGroup + writeISignalIPduGroup extended with NM-PDUS wrapper (NM-PDU-REF-CONDITIONAL/NM-PDU-REF)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations — none
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-27 (538 passed / 0 failed, lint clean, black-check clean); 9b deferred to batch confirmation (user instruction)

- [ ] `MultiplexedIPdu` — IPdu — R23-11 markdown · Table 6.72 (CP_TPS_SystemTemplate), p.410 — commit eba346cb5
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
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-27 (283 passed / 0 failed, lint clean, black-check clean); 9b deferred to batch confirmation (user instruction)

- [ ] `TriggerMode` — AREnum — NEW row (discovered 2026-09-27 as missing MultiplexedIPdu.triggerMode member type, Rule 0001.10/0016.4) — R23-11 markdown · Table 6.71 (CP_TPS_SystemTemplate), p.408 — commit cc609f42a
  - commit: cc609f42a (feat; steps 1-8; 4 literals dynamicPartTrigger/none/staticOrDynamicPartTrigger/staticPartTrigger with verbatim descriptions + EnumerationLiteralIndex tags)
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red) — ImportError (class absent)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite) — new class, verbatim from start
  - [—] Step 5 — Write reader/writer round-trip test (Red) — N/A standalone enum (TRIGGER-MODE element round-tripped via MultiplexedIPdu)
  - [—] Step 6 — Update parser & writer (Green) — N/A standalone enum
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations — none
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-27 (3 passed / 0 failed, lint clean, black-check clean); 9b deferred to batch confirmation (user instruction)

- [ ] `SecuredIPdu` — IPdu — R23-11 markdown · Table 6.42 (CP_TPS_SystemTemplate), p.368 — commit 0a98655a0
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
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-27 (343+ passed / 0 failed, lint clean, black-check clean); 9b deferred to batch confirmation (user instruction)

- [ ] `SecuredPduHeaderEnum` — AREnum — NEW row (discovered 2026-09-27 as missing SecuredIPdu.useSecuredPduHeader member type, Rule 0001.10/0016.4) — R23-11 markdown · Table 6.43 (CP_TPS_SystemTemplate), p.369 — commit 3d5cb55db
  - commit: 3d5cb55db (feat; steps 1-8; 4 literals noHeader/securedPduHeader08Bit/16Bit/32Bit with verbatim descriptions + EnumerationLiteralIndex tags)
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red) — ImportError (class absent)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite) — new class, verbatim from start
  - [—] Step 5 — Write reader/writer round-trip test (Red) — N/A standalone enum (USE-SECURED-PDU-HEADER round-tripped via SecuredIPdu)
  - [—] Step 6 — Update parser & writer (Green) — N/A standalone enum
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations — none
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-27 (3 passed / 0 failed, lint clean, black-check clean); 9b deferred to batch confirmation (user instruction)

- [ ] `UserDefinedIPdu` — IPdu — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreCommunication/__init__.py
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `UserDefinedPdu` — Pdu — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreCommunication/__init__.py
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

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

- [x] `ClientIdRange` — ARObject — already verified (R23-11 · Table 3.2, p.52; short-circuit 2026-09-27)
  - module: M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py
  - note (short-circuit 2026-09-27): class body already carries `# Spec verified: R23-11` — Base ARObject correct, lowerLimit/upperLimit (Limit, 0..1, attr) with verbatim member notes + None-no-op setters, constraints 3116/5396/5397 verbatim in class docstring, full reader/writer coverage, 6-col checklist all [x]. Deviation check found nothing new. No code change needed — row flipped without a class commit.

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
