# Sync todo: Group 13 — BSW behavior, interfaces & SwcBswMapping

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

> **Parent-dependency audit 2026-09-26 (all Group1-20 pending rows, spec-table Base chains):** every pending row's Base row extracted from the R23-11/R4.3.1 markdown (same-table identity rule; 238/293 found; the rest = enums/XSD-only/user-arbitrated) and every parent classified against src stamps + the queue. Findings in THIS file: BswDataReceptionPolicy queued NEW above its child BswQueuedDataReceptionPolicy. ESTABLISHED SKIPS (no rows, per precedent): UploadableDesignElement / UploadablePackageElement (attribute-less abstract bases, empty XSD groups — most-derived-base collapse, Group5-audit precedent); AREnum leaf classes (no Base row by construction); the Firewall member-rule family (user arbitration 2026-08-31); ARList (resolved under "List", FO GST Table 9.8).

## Queue (dependency-first)

- [x] `BswApiOptions` — ARObject — XSD-only (Step 1: no own table in either corpus; group BSW-API-OPTIONS AUTOSAR_00052.xsd L9379, R4.3.1 00044.xsd L7279) — **finished, stamped `# XSD verified: AUTOSAR_00052.xsd`** (sync commit 816c64f3d)
  - module: M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior.py
  - note: deviation-tracked in method_deviation_by_class_v2.md — review entries at Step 1
  - note (Step 1): XSD-only class — no table in either corpus (R23-11/R4.3.1 markdown
    greps + full pdf_page.py scan negative; only Base-column mentions). Group-only class:
    `<xsd:group name="BSW-API-OPTIONS">` AUTOSAR_00052.xsd L9379 (R4.3.1 00044.xsd L7279
    identical). One attr `enableTakeAddress` (BOOLEAN, 0..1, element ENABLE-TAKE-ADDRESS).
    Drift found: bare `Boolean` field annotation (→ Optional[Boolean]), untyped accessors,
    paraphrased docstrings, `__init__` docstring, old 4-col checklist. Base ARObject+ABC
    correct (abstract guard, 8 concrete policy subclasses). Not VP-capable (no
    VARIATION-POINT in the group). Reader/writer helpers readBswApiOptions/writeBswApiOptions
    already exist with matched set/get pairs.
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - [x] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-25 (11997 passed / 0 failed, npm run lint clean, black-check clean); 9a re-run 2026-10-01 on feature/g13-9b-confirm (post PR #876 merge): full suite 15,346 passed / 1 failed (= the pre-existing 8× `*SystemMapping.arxml` round-trip file_compare set, documented Group11.md:292 — unrelated to this class) + `npm run lint` (flake8 + ruff) clean + `black --check` clean on BswBehavior.py; 9b user-confirmed 2026-10-01 (XSD-only): group BSW-API-OPTIONS AUTOSAR_00052.xsd L9379 (R4.3.1 00044.xsd L7279 identical), sole attr enableTakeAddress (BOOLEAN, 0..1, `Optional[Boolean]`) with typed get/set, setter None no-op + chaining, abstract guard ARObject+ABC intact (8 concrete subclasses), reader/writer via read/writeBswApiOptions (ENABLE-TAKE-ADDRESS), checklist 3/3 in source order, no deviations remain; `# XSD verified: AUTOSAR_00052.xsd` written after the `# Spec:` line

- [x] `BswModuleCallPoint` — Referrable — R23-11 markdown · Table 5.10 (CP_TPS_BSWModuleDescriptionTemplate), p.77 — **finished, stamped `# Spec verified: R23-11`** (sync commit 879aacf8c)
  - module: M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior.py
  - note (Step 1): R23-11 markdown Table 5.10, p.77 (AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate).
    Abstract Class; Base most-derived = `Referrable`; VP-capable (VARIATION-POINT in
    BSW-MODULE-CALL-POINT group, AUTOSAR_00052.xsd L11283 — mixin base kept, Rule 0020).
    One attr `contextLimitation` (BswDistinguishedPartition, *, ref → `contextLimitationRefs`
    List[RefType]). XSD XML order: CONTEXT-LIMITATION-REFS wrapper / CONTEXT-LIMITATION-REF
    items, then VARIATION-POINT. Drift: old 4-col checklist, untyped accessors, missing
    None no-op on addContextLimitationRef, paraphrased docstrings, shared
    read/writeBswModuleCallPoint helpers lacked wrapper + VARIATION-POINT coverage.
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - [x] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-26 (12014 passed / 0 failed, lint clean, black-check clean); 9a re-run 2026-10-01 on feature/g13-9b-confirm (post PR #876 merge): full suite 15,346 passed / 1 failed (= the pre-existing 8× `*SystemMapping.arxml` round-trip file_compare set, documented Group11.md:292 — unrelated to this class) + `npm run lint` (flake8 + ruff) clean + `black --check` clean on BswBehavior.py; 9b user-confirmed 2026-10-01: abstract, Table 5.10 p.77, Base most-derived = `Referrable` (already correct), VP-capable mixin kept (Rule 0020 — VARIATION-POINT in BSW-MODULE-CALL-POINT group L11283), sole attr contextLimitation → `contextLimitationRefs` `List[RefType]` (XSD CONTEXT-LIMITATION-REFS wrapper / REF items) with add/get (None no-op on add, no set — Rule 0001.6 List shape), reader/writer round-trip incl. wrapper + VARIATION-POINT, checklist 3/3 in source order, no deviations remain; `# Spec verified: R23-11` written after the `# Spec:` line

- [x] `BswDirectCallPoint` — BswModuleCallPoint — R23-11 markdown · Table 5.11 (CP_TPS_BSWModuleDescriptionTemplate), p.78 — **finished, stamped `# Spec verified: R23-11`** (sync commit 518ebf6a0)
  - module: M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior.py
  - after `BswModuleCallPoint`
  - note (Step 1): R23-11 markdown Table 5.11, p.78 (AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate).
    Concrete Class; Base most-derived = `BswModuleCallPoint` (already correct in src).
    Two attrs, both 0..1 ref → `calledEntryRef` (BswModuleEntry), `calledFromWithinExclusiveAreaRef`
    (ExclusiveAreaNestingOrder), both `Optional[RefType]`. VP capability inherited from base
    (no VARIATION-POINT in BSW-DIRECT-CALL-POINT group, AUTOSAR_00052.xsd L9901 — base group
    ref L9950; Rule 0020). XSD XML order after base groups: CALLED-ENTRY-REF then
    CALLED-FROM-WITHIN-EXCLUSIVE-AREA-REF. Drift: bare `RefType = None` fields, untyped
    accessors, `__init__` docstring, paraphrased docstrings, glued `__init__` member blocks,
    old 4-col checklist; NO reader/writer coverage (no read/writeBswDirectCallPoint, no
    dispatch branch, no createBswDirectCallPoint factory on BswModuleEntity).
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - [x] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-26 (12018 passed / 0 failed, lint clean, black-check clean); 9a re-run 2026-10-01 on feature/g13-9b-confirm (post PR #876 merge): full suite 15,346 passed / 1 failed (= the pre-existing 8× `*SystemMapping.arxml` round-trip file_compare set, documented Group11.md:292 — unrelated to this class) + `npm run lint` (flake8 + ruff) clean + `black --check` clean on BswBehavior.py; 9b user-confirmed 2026-10-01: concrete, Table 5.11 p.78, Base most-derived = `BswModuleCallPoint` (already correct), VP capability inherited (no own VARIATION-POINT, group L9901/base group ref L9950 — Rule 0020), two 0..1 refs (calledEntryRef → BswModuleEntry, calledFromWithinExclusiveAreaRef → ExclusiveAreaNestingOrder) both `Optional[RefType]` with typed get/set + None no-op, reader/writer + parser dispatch + `createBswDirectCallPoint` factory added at Step 6 (XSD order CALLED-ENTRY-REF → CALLED-FROM-WITHIN-EXCLUSIVE-AREA-REF), checklist 5/5 in source order, no deviations remain; `# Spec verified: R23-11` written after the `# Spec:` line

- [ ] `BswSynchronousServerCallPoint` — BswModuleCallPoint — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior.py
  - after `BswModuleCallPoint`
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-26 (12027 passed / 0 failed, lint clean, black-check clean); 9b deferred to batch confirmation (user instruction)

- [ ] `BswInternalTriggeringPoint` — Identifiable — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior.py
  - note: deviation-tracked in method_deviation_by_class_v2.md — review entries at Step 1
  - note (Step 1): R23-11 markdown Table 5.28, p.91 (AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate).
    Concrete Class; Base most-derived = `Identifiable` (already correct in src); VP-capable
    (VARIATION-POINT in BSW-INTERNAL-TRIGGERING-POINT group, AUTOSAR_00052.xsd L10773 —
    mixin base kept, Rule 0020). One attr `swImplPolicy` (SwImplPolicyEnum, 0..1, attr).
    XSD XML order: SW-IMPL-POLICY then VARIATION-POINT. Drift: fabricated class docstring,
    bare `SwImplPolicyEnum = None` field, untyped accessors, `__init__` docstring,
    paraphrased docstrings, old 4-col checklist; read/writeBswInternalTriggeringPoint
    exist but only cover Identifiable (no SW-IMPL-POLICY / VARIATION-POINT).
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-26 (12041 passed / 0 failed, lint clean, black-check clean); 9b deferred to batch confirmation (user instruction)

- [ ] `BswInterruptEntity` — BswModuleEntity — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior.py
  - note (Step 1): R23-11 markdown Table 5.8, p.75 (AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate).
    Concrete Class; Base most-derived = `BswModuleEntity` (already correct in src). Two attrs,
    both 0..1 attr → `interruptCategory` (BswInterruptCategory), `interruptSource` (String).
    No own VARIATION-POINT (capability inherited from base group, Rule 0020). XSD XML order
    after base groups: INTERRUPT-CATEGORY (enum tokens CAT-1/CAT-2) then INTERRUPT-SOURCE
    (AR:STRING). Drift: old 4-col checklist, `__init__` docstring, bare-typed fields,
    untyped accessors, no None no-op, paraphrased docstrings; reader reads generic ARLiteral
    (not spec types), writer named `setBswInterruptEntity` (unmatched pair) via
    setChildElementOptionalLiteral.
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-26 (12043 passed / 0 failed, lint clean, black-check clean); 9b deferred to batch confirmation (user instruction)

- [ ] `BswModeSwitchAckRequest` — ARObject — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior.py
  - note: deviation-tracked in method_deviation_by_class.md — review entries at Step 1
  - note (Step 1): R23-11 markdown Table 5.40, p.103 (AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate).
    Concrete Class; Base most-derived = `ARObject` (already correct in src). One attr `timeout`
    (TimeValue, 0..1, attr). Not VP-capable (no VARIATION-POINT in BSW-MODE-SWITCH-ACK-REQUEST
    group, AUTOSAR_00052.xsd L11164/L11180). XSD XML order: TIMEOUT only. Drift: fabricated
    class docstring, `__init__` docstring, bare `Float` field (→ Optional[TimeValue]), untyped
    accessors, no None no-op, old 4-col checklist; get/setBswModeSwitchAckRequest reader/writer
    helpers already exist with TIMEOUT coverage.
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - note (Step 6): N/A — get/setBswModeSwitchAckRequest already covered TIMEOUT (AR:TIME-VALUE)
    with matched names; new tests passed immediately, no parser/writer edit.
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-26 (12051 passed / 0 failed, lint clean, black-check clean); 9b deferred to batch confirmation (user instruction)

- [ ] `BswDataReceptionPolicy` — (abstract; Table 5.42 renders no Base row — src intake bases BswApiOptions + VariationPointCapable, XSD group-only) — R23-11 markdown · Table 5.42 (CP_TPS_BSWModuleDescriptionTemplate)
  - module: M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior.py (class EXISTS in src, unstamped — queued per Rule 0016.4 "exists is not a stamp")
  - note (2026-09-26, parent-dependency audit): QUEUED BEFORE its queued child `BswQueuedDataReceptionPolicy` (Rule 0016.5) — Table 5.43 Base row names this class, which was missing from the queue; abstract, group-only in XSD 00052 (group BSW-DATA-RECEPTION-POLICY L9727, single member RECEIVED-DATA-REF → VariableDataPrototype 0..1 ref, constr_10296 existence constr); Table 5.42 has ONE attribute row (receivedData) and renders no Base row — verify Base (incl. whether BswApiOptions belongs per the src intake) at Step 1 against the XSD complexType composition
  - note (Step 1): Table 5.42 body renders BEFORE its caption (page-split render,
    md L2648-2663): Class = BswDataReceptionPolicy (abstract); Package =
    M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior; Note = "Specifies the
    reception policy for the referred data in sender-receiver communication over the
    BSW Scheduler. To be used for inter-partition and/or inter-core communication.";
    Base = "ARObject, BswApiOptions" → most-derived = BswApiOptions (XSD-only class,
    group BSW-API-OPTIONS L9379); Subclasses = BswQueuedDataReceptionPolicy;
    Aggregated by = BswInternalBehavior.receptionPolicy. Attribute rows (after
    caption): receivedData (VariableDataPrototype, 0..1, ref → receivedDataRef
    Optional[RefType]), constr_10296. R4.3.1 Table 6.41 p.106 agrees (Mult 1 there;
    R23-11 0..1 wins). XSD: group-only BSW-DATA-RECEPTION-POLICY L9727 =
    RECEIVED-DATA-REF (0..1) + VARIATION-POINT (sequenceOffset 10000) → VP-capable,
    mixin kept (Rule 0020); no complexType of its own — child complexType L12400
    composes BSW-API-OPTIONS + BSW-DATA-RECEPTION-POLICY + own group, confirming the
    Base and BswApiOptions intake. Drift: fabricated class docstring, __init__
    docstring, bare `RefType = None` field, untyped accessors, paraphrased docstrings,
    stale 3-col checklist, redundant ABC in bases (siblings use
    `(BswApiOptions, VariationPointCapable)`); read/writeBswDataReceptionPolicy exist
    and are called by the child helpers but lack VARIATION-POINT coverage.
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - note (Steps 5/6): read/writeBswDataReceptionPolicy had RECEIVED-DATA-REF +
    ENABLE-TAKE-ADDRESS (via read/writeBswApiOptions) but lacked VARIATION-POINT
    (group member 2, sequenceOffset 10000) — added readVariationPoint/writeVariationPoint
    to both helpers (sibling readBswPerInstanceMemoryPolicy idiom); new VP
    parser tests + value-asserting full round-trip (enableTakeAddress/receivedDataRef/
    queueLength/variationPoint short label) pass.
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - note (Step 8): no open deviations — all Step-1 drift items fixed (docstrings
    verbatim, Optional[RefType] field + typed accessors, 6-col checklist); abstract
    guard kept (ABC); Rule 0020 VP mixin is established convention, not a deviation;
    R23-11 Mult 0..1 wins over R4.3.1 Table 6.41 Mult 1; constr_10296 is a
    config-time existence constraint (not a model invariant), recorded here only.
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-26 (12296 passed / 0 failed, lint clean, black-check clean); 9b deferred to batch confirmation (user instruction)

- [ ] `BswQueuedDataReceptionPolicy` — BswDataReceptionPolicy — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior.py
  - note (Step 1): R23-11 markdown Table 5.43, p.105 (AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate).
    Concrete Class; Base most-derived = `BswDataReceptionPolicy` (already correct in src).
    One attr `queueLength` (PositiveInteger, 0..1, attr). Not VP-capable directly —
    VARIATION-POINT lives in base group BSW-DATA-RECEPTION-POLICY (AUTOSAR_00052.xsd
    L9727), capability inherited from base mixin (Rule 0020). Own XSD group
    BSW-QUEUED-DATA-RECEPTION-POLICY L12385: QUEUE-LENGTH (AR:POSITIVE-INTEGER, 0..1);
    XML order after base groups. Drift: fabricated class docstring, `__init__` docstring,
    bare `PositiveInteger` field (→ Optional[PositiveInteger]), untyped accessors, fake
    4-col checklist (removed). read/writeBswQueuedDataReceptionPolicy already cover
    QUEUE-LENGTH. Base `BswDataReceptionPolicy` itself unstamped/drifted — not this row.
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - note (Steps 5/6): read/writeBswQueuedDataReceptionPolicy + wrapper dispatch already
    covered QUEUE-LENGTH with matched set/get names (XSD wire names verified); new
    value-asserting + full round-trip tests passed immediately, no parser/writer edit.
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-26 (12057 passed / 0 failed, lint clean, black-check clean); 9b deferred to batch confirmation (user instruction)

- [ ] `BswAsynchronousServerCallReturnsEvent` — BswScheduleEvent — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior.py
  - note: deviation-tracked in method_deviation_by_class.md — review entries at Step 1
  - note (Step 1): R23-11 markdown Table 5.36, p.98 (AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate).
    Concrete Class; Base most-derived = `BswScheduleEvent` (already correct in src). One attr
    `eventSource` (BswAsynchronousServerCallResultPoint, 0..1, ref → `eventSourceRef`
    Optional[RefType]). Not directly VP-capable — VARIATION-POINT lives in ancestor BSW-EVENT
    group (AUTOSAR_00052.xsd), capability inherited via BswEvent mixin (Rule 0020). Wire
    element EVENT-SOURCE-REF (AR:REF + DEST BSW-ASYNCHRONOUS-SERVER-CALL-RESULT-POINT--SUBTYPES-ENUM).
    Drift: old 5-col checklist (no release/Columns line), `__init__` docstring, paraphrased
    docstrings, setter param bare `RefType` (not Optional). Reader/writer helpers + dispatch
    + consumer factory already exist with matched set/get names.
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - note (Steps 5/6): read/writeBswAsynchronousServerCallReturnsEvent + EVENTS dispatch +
    createBswAsynchronousServerCallReturnsEvent already cover EVENT-SOURCE-REF with matched
    set/get names (XSD wire name verified, AUTOSAR_00052.xsd L9481); new value-asserting +
    full round-trip + empty tests passed immediately, no parser/writer edit. Empty round-trip
    shows no inherited normally-None element emission (SWC-sibling disease absent here).
    Base drift noted (not this row): readBswEvent lacks readIdentifiable while
    writeBswEvent calls writeIdentifiable (BswEvent/BswScheduleEvent base-owned).
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-26 (12062 passed / 0 failed, lint clean, black-check clean); 9b deferred to batch confirmation (user instruction)

- [ ] `BswDataReceivedEvent` — BswScheduleEvent — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior.py
  - note (Step 1): R23-11 markdown Table 5.37, p.99 (AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate).
    Concrete Class; Base most-derived = `BswScheduleEvent` (already correct in src). One attr
    `data` (VariableDataPrototype, 0..1, ref → `dataRef` Optional[RefType]). Not directly
    VP-capable — VARIATION-POINT lives in ancestor BSW-EVENT group (AUTOSAR_00052.xsd),
    capability inherited via BswEvent mixin (Rule 0020). Wire element DATA-REF (AR:REF + DEST
    VARIABLE-DATA-PROTOTYPE--SUBTYPES-ENUM; group L9684, complexType L9707). Drift: fabricated
    class docstring, `__init__` docstring, paraphrased docstrings, bare `RefType` field (not
    Optional), untyped accessors, no None no-op, stale 4-col checklist with unchecked
    getDataRef row. Reader/writer helpers + dispatch + consumer factory already exist with
    matched set/getDataRef names; writer reads via getter (SWC-sibling disease absent).
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - note (Steps 5/6): read/writeBswDataReceivedEvent + EVENTS dispatch + createBswDataReceivedEvent
    already cover DATA-REF with matched set/getDataRef names (XSD wire name verified,
    AUTOSAR_00052.xsd L9684); new value-asserting + full round-trip + empty tests passed
    immediately, no parser/writer edit. Writer reads via getter (SWC-sibling disease absent).
    Empty round-trip shows no inherited normally-None element emission.
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-26 (12068 passed / 0 failed, lint clean, black-check clean); 9b deferred to batch confirmation (user instruction)

- [ ] `BswInternalTriggerOccurredEvent` — BswScheduleEvent — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior.py
  - note (Step 1): R23-11 markdown Table 5.29, p.91 (AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate).
    Concrete Class; Base most-derived = `BswScheduleEvent` (already correct in src). One attr
    `eventSource` (BswInternalTriggeringPoint, 0..1, ref → `eventSourceRef` Optional[RefType]),
    constr_10282. Not directly VP-capable — VARIATION-POINT lives in ancestor BSW-EVENT group
    (AUTOSAR_00052.xsd), capability inherited via BswEvent mixin (Rule 0020). Wire element
    EVENT-SOURCE-REF (AR:REF + DEST BSW-INTERNAL-TRIGGERING-POINT--SUBTYPES-ENUM; group L10730,
    complexType L10753). Drift: fabricated class docstring, `__init__` docstring, paraphrased
    docstrings, bare `RefType` field (not Optional), untyped accessors, no None no-op, stale
    3-col checklist with unchecked getEventSourceRef row. Reader/writer helpers + dispatch +
    consumer factory already exist with matched set/getEventSourceRef names; writer reads via
    getter (SWC-sibling disease absent).
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - note (Steps 5/6): read/writeBswInternalTriggerOccurredEvent + EVENTS dispatch +
    createBswInternalTriggerOccurredEvent already cover EVENT-SOURCE-REF with matched
    set/getEventSourceRef names (XSD wire name verified, AUTOSAR_00052.xsd L10730); new
    value-asserting + dest/absent + full round-trip + empty tests passed immediately,
    no parser/writer edit. Writer reads via getter (SWC-sibling disease absent). Empty
    round-trip shows no inherited normally-None element emission.
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-26 (12074 passed / 0 failed, lint clean, black-check clean); 9b deferred to batch confirmation (user instruction)

- [ ] `BswModeManagerErrorEvent` — BswScheduleEvent — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior.py
  - note: deviation-tracked in method_deviation_by_class.md — review entries at Step 1
  - note (Step 1): R23-11 markdown Table 5.33, p.95 (AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate).
    Concrete Class; Base most-derived = `BswScheduleEvent` (already correct in src). One attr
    `modeGroup` (ModeDeclarationGroupPrototype, 0..1, ref → `modeGroupRef` Optional[RefType]),
    constr_10286. Not directly VP-capable — VARIATION-POINT lives in ancestor BSW-EVENT group
    (AUTOSAR_00052.xsd), capability inherited via BswEvent mixin (Rule 0020). Wire element
    MODE-GROUP-REF (AR:REF + DEST MODE-DECLARATION-GROUP-PROTOTYPE--SUBTYPES-ENUM; group
    L11003, complexType L11026). Drift: fabricated class docstring (constr_4081 text not in
    this table), `__init__` docstring, paraphrased docstrings, bare `RefType` setter param
    (not Optional), old 4-col checklist. Reader/writer helpers + dispatch + consumer factory
    already exist with matched set/getModeGroupRef names.
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - note (Steps 5/6): read/writeBswModeManagerErrorEvent + EVENTS dispatch +
    createBswModeManagerErrorEvent already cover MODE-GROUP-REF with matched
    set/getModeGroupRef names (XSD wire name verified, AUTOSAR_00052.xsd L11003); new
    dest/absent + full round-trip + empty tests passed immediately (after adding the
    missing BswModeManagerErrorEvent import to the writer test file), no parser/writer
    edit. Writer reads via getter (SWC-sibling disease absent). Empty round-trip shows
    no inherited normally-None element emission.
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-26 (12079 passed / 0 failed, lint clean, black-check clean); 9b deferred to batch confirmation (user instruction)

- [ ] `BswModeSwitchedAckEvent` — BswScheduleEvent — R23-11 markdown · Table 5.32 (CP_TPS_BSWModuleDescriptionTemplate), p.95
  - module: M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior.py
  - note (Step 1): R23-11 markdown Table 5.32, p.95. Concrete Class; Base most-derived =
    `BswScheduleEvent` (already correct in src). One attr `modeGroup`
    (ModeDeclarationGroupPrototype, 0..1, ref → `modeGroupRef` Optional[RefType]),
    constr_10285. Not directly VP-capable — VARIATION-POINT lives in ancestor BSW-EVENT
    group (AUTOSAR_00052.xsd), capability inherited via BswEvent mixin (Rule 0020). Own
    group BSW-MODE-SWITCHED-ACK-EVENT L11240 = MODE-GROUP-REF only (DEST
    MODE-DECLARATION-GROUP-PROTOTYPE--SUBTYPES-ENUM; complexType L11263). Drift:
    fabricated class docstring (constr_4026 text not in this table), `__init__`
    docstring, paraphrased docstrings, bare `RefType` setter param (not Optional), old
    3-col checklist. Reader/writer helpers + EVENTS dispatch + createBswModeSwitchedAckEvent
    factory already exist with matched set/getModeGroupRef names.
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - note (Steps 5/6): read/writeBswModeSwitchedAckEvent + EVENTS dispatch + factory already
    cover MODE-GROUP-REF with matched set/getModeGroupRef names (XSD wire name verified,
    AUTOSAR_00052.xsd L11240); new type-hint pin + dest/absent full-document round-trip +
    empty tests passed immediately, no parser/writer edit. Writer reads via getter
    (SWC-sibling disease absent).
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - note (Step 8): no open deviations — all Step-1 drift fixed; `modeGroupRef` naming is
    the Rule 0001.5 ref-suffix convention (tracker row stays "ok"); constr_10285 is a
    config-time existence constraint (inline comment only), recorded in the tracker note.
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-26 (12299 passed / 0 failed, lint clean, black-check clean); 9b deferred to batch confirmation (user instruction)

- [ ] `BswTimingEvent` — BswScheduleEvent — R23-11 markdown · Table 5.25 (CP_TPS_BSWModuleDescriptionTemplate), p.89
  - module: M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior.py
  - note (Step 1): R23-11 markdown Table 5.25, p.89. Concrete Class; Base most-derived =
    `BswScheduleEvent` (already correct in src). One attr `period` (TimeValue, 0..1, attr;
    Note "Requirement for the time period (in seconds) by which this event is
    triggered."), constr_10281 (existence) + constr_4043 (>0). Not directly VP-capable —
    VARIATION-POINT lives in ancestor BSW-EVENT group, capability inherited via BswEvent
    mixin (Rule 0020). Own group BSW-TIMING-EVENT (PERIOD, AR:TIME-VALUE, 0..1) only.
    Drift: fabricated class docstring extension, `__init__` docstring, paraphrased
    docstrings, bare `TimeValue` setter param (not Optional), old 3-col checklist.
    `periodMs` property = tracker-recorded convenience extra (not in spec, kept).
    Reader/writer helpers + dispatch + factory already exist with matched set/getPeriod.
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - note (Steps 5/6): read/writeBswTimingEvent + EVENTS dispatch + createBswTimingEvent
    already cover PERIOD with matched set/getPeriod names; new type-hint pin +
    full-document round-trip (value + empty) tests passed immediately, no parser/writer
    edit. Writer reads via getter (SWC-sibling disease absent).
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - note (Step 8): no new deviations — `periodMs` stays as the tracker-recorded
    convenience property (checklist row marked); constr_10281/constr_4043 recorded in
    the inline member comment + tracker note.
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-26 (12302 passed / 0 failed, lint clean, black-check clean); 9b deferred to batch confirmation (user instruction)

- [ ] `BswEntryRelationshipEnum` — AREnum — R23-11 markdown · Table 4.20 (CP_TPS_BSWModuleDescriptionTemplate), p.52
  - module: M2/AUTOSARTemplates/BswModuleTemplate/BswInterfaces.py
  - note (Step 1): R23-11 markdown Table 4.20, p.52. Enumeration; Package
    M2::AUTOSARTemplates::BswModuleTemplate::BswInterfaces; Note = "Define the type of
    relationship between two BswModuleEntrys." (spec grammar kept verbatim); Aggregated
    by = BswEntryRelationship.bswEntryRelationshipType. ONE literal: derivedFrom
    ("Describes that the BswModuleEntry referenced as \"to\" needs to have the same
    signature as the \"abstract\" BswModuleEntry referenced as \"from\".",
    atp.EnumerationLiteralIndex=0). XSD BSW-ENTRY-RELATIONSHIP-ENUM --SIMPLE token
    "derivedFrom" agrees. Drift: fabricated 2-sentence class docstring, NO __init__
    (AREnum.__init__ requires enum_values → the enum could not be instantiated at all),
    literal comment wrapped, no Spec/checklist header.
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - note (Steps 5/6): N/A for a standalone AREnum — no own XML element; serialized as
    the attribute value of the consuming class (BswEntryRelationship, next row) and
    round-tripped there (Rules 0010–0011).
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - note (Step 8): no deviations — single literal matches XSD token; the v2 tracker
    bullet-list mention is a type-list reference, not a deviation row.
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-26 (12305 passed / 0 failed, lint clean, black-check clean); 9b deferred to batch confirmation (user instruction)

- [ ] `BswEntryRelationship` — ARObject — R23-11 markdown · Table 4.19 (CP_TPS_BSWModuleDescriptionTemplate), p.51
  - module: M2/AUTOSARTemplates/BswModuleTemplate/BswInterfaces.py
  - after `BswEntryRelationshipEnum`
  - note (Step 1): R23-11 markdown Table 4.19, p.51. Concrete Class; Base = ARObject
    (already correct in src). Aggregated by = BswEntryRelationshipSet.bswEntryRelationship.
    Three attrs in displayed order: bswEntryRelationshipType (BswEntryRelationshipEnum,
    0..1, attr, xml.sequenceOffset=5), from (BswModuleEntry, 0..1, ref → fromRef), to
    (BswModuleEntry, 0..1, ref → toRef). XSD wire order: FROM-REF, TO-REF,
    BSW-ENTRY-RELATIONSHIP-TYPE (token DERIVED-FROM vs literal value "derivedFrom" →
    BSW_ENTRY_RELATIONSHIP_XML_MAP, SW_IMPL_POLICY idiom). Note: spec/from Note carries
    the spec's own "drivedFrom" typo — kept verbatim per Rule 0001.4. Drift: `__init__`
    docstring, paraphrased docstrings, src inline comment had "drivenFrom" (wrong),
    old 4-col checklist; NO reader/writer coverage (no read/writeBswEntryRelationship).
    Tracker `missing` rows were stale (audited against non-existent leaf files).
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - note (Steps 5/6): ADDED readBswEntryRelationship (parser: FROM-REF/TO-REF via
    getChildElementOptionalRefType + BSW-ENTRY-RELATIONSHIP-TYPE token map) and
    writeBswEntryRelationship (writer: XSD order, token map); new value-asserting
    parser tests (refs+token, absent) and writer tests (element order, unset omits,
    full round-trip) pass.
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - note (Step 8): tracker `missing` rows RESOLVED (stale audit against non-existent
    leaf files) — retyped as ok rows (fromRef/toRef = Rule 0001.5 ref-suffix naming);
    "drivedFrom" spec typo kept verbatim in docstrings.
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-26 (12310 passed / 0 failed, lint clean, black-check clean); 9b deferred to batch confirmation (user instruction)

- [ ] `BswEntryRelationshipSet` — ARElement — R23-11 markdown · Table 4.18 (CP_TPS_BSWModuleDescriptionTemplate), p.51
  - module: M2/AUTOSARTemplates/BswModuleTemplate/BswInterfaces.py
  - after `BswEntryRelationship`
  - note (Step 1): R23-11 markdown Table 4.18, p.51. Concrete Class; spec Base chain
    ARObject..Identifiable..CollectableElement..PackageableElement..ARElement (+ AtpBlueprint /
    AtpBlueprintable, both empty groups — collapsed per the attribute-less-abstract-base
    precedent) → RE-BASED src `Identifiable` → `ARElement`. Aggregated by ARPackage.element.
    One attr: bswEntryRelationship (BswEntryRelationship, 0..*, aggr → typed-list field
    bswEntryRelationships). XSD: BSW-ENTRY-RELATIONSHIPS wrapper (0..1) + unbounded
    BSW-ENTRY-RELATIONSHIP items after base groups. Drift: `__init__` docstring,
    paraphrased docstrings, old 4-col checklist; NO reader/writer coverage (no factory,
    no dispatch, no read/write helpers); tracker `missing` row stale (leaf-file audit).
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - note (Steps 5/6): ADDED createBswEntryRelationshipSet factory + getBswEntryRelationshipSets
    getter on ARPackage (bottom late-binding import, createSwcBswMapping pattern);
    read/writeBswEntryRelationshipSet helpers (wrapper + items via read/writeBswEntryRelationship);
    ARPackage element dispatch both directions; value-asserting helper tests + full-document
    round-trip via the factory pass.
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - note (Step 8): tracker `missing` row RESOLVED (stale leaf-file audit) → ok row
    (Rule 0001.5 plural naming); base re-base recorded (Identifiable → ARElement);
    AtpBlueprint/AtpBlueprintable collapse noted for 9b review.
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-26 (12319 passed / 0 failed, lint clean, black-check clean); 9b deferred to batch confirmation (user instruction)

- [ ] `BswModuleClientServerEntry` — Referrable — R23-11 markdown · Table 4.21 (CP_TPS_BSWModuleDescriptionTemplate), p.54
  - module: M2/AUTOSARTemplates/BswModuleTemplate/BswInterfaces.py
  - note (Step 1): R23-11 markdown Table 4.21, p.54. Concrete Class; Base most-derived =
    `Referrable` (already correct in src); VP-capable — VARIATION-POINT is in the OWN XSD
    group BSW-MODULE-CLIENT-SERVER-ENTRY (AUTOSAR_00052.xsd L11320: ENCAPSULATED-ENTRY-REF,
    IS-REENTRANT, IS-SYNCHRONOUS, VARIATION-POINT). R23-11 table attrs: encapsulatedEntry
    (BswModuleEntry, 0..1, ref → encapsulatedEntryRef, seq 5), isReentrant (Boolean, 0..1,
    attr, seq 10). isSynchronous ABSENT from the R23-11 table but present in R4.3.1 Table
    5.22 p.56 AND the R23-11 XSD → Rule 0019 legacy member kept (R4.3.1 Note verbatim,
    release column R4.3.1, dual # Spec: lines). Drift: fabricated class docstring,
    `__init__` docstring, bare-typed fields (`RefType = None`, `Boolean = None`),
    untyped accessors, paraphrased docstrings, old 4-col checklist; reader/writer lacked
    VARIATION-POINT.
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - note (Steps 5/6): read/writeBswModuleClientServerEntry already covered
    ENCAPSULATED-ENTRY-REF/IS-REENTRANT/IS-SYNCHRONOUS with matched names; ADDED
    VARIATION-POINT to both (readVariationPoint/writeVariationPoint); new type-hint pin +
    value-asserting document round-trips (attrs + VP short label) pass.
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - note (Step 8): ONE accepted legacy deviation (isSynchronous — Rule 0019 combine case,
    dual # Spec: lines, mixed release columns) — subject to 9b batch confirmation;
    encapsulatedEntryRef/isReentrant rows ok.
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-26 (12322 passed / 0 failed, lint clean, black-check clean); 9b deferred to batch confirmation (user instruction)

- [ ] `BswModuleDependency` — Identifiable — R23-11 markdown · Table 4.17 (CP_TPS_BSWModuleDescriptionTemplate), p.48
  - module: M2/AUTOSARTemplates/BswModuleTemplate/BswInterfaces.py
  - note (Step 1): R23-11 markdown Table 4.17, p.48. Concrete Class; Base most-derived =
    `Identifiable` (already correct in src); NOT VP-capable — the complexType has no
    class-level VARIATION-POINT group (atpVariation is attribute-level on targetModuleRef via
    the REF-CONDITIONAL wrapper); src mixin VariationPointCapable REMOVED. Two attrs:
    targetModuleId (PositiveInteger, 0..1, attr, seq 5), targetModuleRef (BswModuleDescription,
    0..1, ref, seq 7). R23-11 XSD wire = TARGET-MODULE-REFS wrapper + unbounded
    BSW-MODULE-DESCRIPTION-REF-CONDITIONAL (markdown 0..1 wins for the model; wire per XSD).
    requiredEntry/expectedCallback/serviceItem are atp.Status="removed" — not modeled.
    Drift: fabricated class docstring, `__init__` docstring, paraphrased docstrings, old
    4-col checklist; reader used generic NumericalValue (not PositiveInteger) and a bare
    TARGET-MODULE-REF element that does not exist in the R23-11 XSD.
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - note (Steps 5/6): reader REWIRED (PositiveInteger helper + TARGET-MODULE-REFS wrapper
    path, first item wins); writer REWIRED (wrapper + conditional item + DEST); new
    type-hint pins, wrapper-path parser test, and document round-trips (value + empty)
    pass. No fixture/test used the old wire element.
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - note (Step 8): ONE accepted model-vs-wire deviation (targetModuleRef "wire many vs py
    single" — Rule 0015 markdown-wins, tracker row updated); mixin removal + removed-element
    handling recorded in the tracker note.
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-26 (12326 passed / 0 failed, lint clean, black-check clean); 9b deferred to batch confirmation (user instruction)

- [ ] `SwcBswRunnableMapping` — ARObject — R23-11 markdown · Table 5.47 (CP_TPS_BSWModuleDescriptionTemplate), p.110
  - module: M2/AUTOSARTemplates/CommonStructure/SwcBswMapping.py
  - note (Step 1): R23-11 markdown Table 5.47, p.110. Concrete Class; Base = ARObject
    (already correct); VP-capable — VARIATION-POINT in OWN XSD group
    SWC-BSW-RUNNABLE-MAPPING (seq 10000, atpVariation), mixin kept (Rule 0020). Two attrs:
    bswEntity (BswModuleEntity, 0..1, ref → bswEntityRef, DEST BSW-MODULE-ENTITY--SUBTYPES-ENUM),
    swcRunnable (RunnableEntity, 0..1, ref → swcRunnableRef, DEST
    RUNNABLE-ENTITY--SUBTYPES-ENUM); wire order refs then VP. Aggregated by
    SwcBswMapping.runnableMapping (parent SwcBswMapping stamped). Drift: `__init__`
    docstring, bare `RefType = None` fields, untyped accessors, setBswEntityRef/
    setSwcRunnableRef had NO None no-op guard, old 4-col checklist; reader/writer existed
    with matched names but lacked VARIATION-POINT.
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - note (Steps 5/6): read/write helpers existed with matched wire names; ADDED
    VARIATION-POINT to both (parser per-item read in the RUNNABLE-MAPPINGS loop, writer
    writeVariationPoint); new None no-op + type-hint pin + VP helper round-trip tests pass.
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - note (Step 8): no deviations — missing None no-op guards were drift, now fixed.
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-26 (12329 passed / 0 failed, lint clean, black-check clean); 9b deferred to batch confirmation (user instruction)

- [ ] `SwcBswSynchronizedModeGroupPrototype` — ARObject — R23-11 markdown · Table 5.48 (CP_TPS_BSWModuleDescriptionTemplate), p.111
  - module: M2/AUTOSARTemplates/CommonStructure/SwcBswMapping.py
  - note (Step 1): R23-11 markdown Table 5.48, p.111. Concrete Class; Base = ARObject
    (already correct); VP-capable — VARIATION-POINT in OWN XSD group
    SWC-BSW-SYNCHRONIZED-MODE-GROUP-PROTOTYPE (seq 10000, atpVariation), mixin kept
    (Rule 0020). Two attrs: bswModeGroup (ModeDeclarationGroupPrototype, 0..1, ref →
    BSW-MODE-GROUP-REF, constr_10336), swcModeGroup (ModeDeclarationGroupPrototype, 0..1,
    iref → SWC-MODE-GROUP-IREF / PModeGroupInAtomicSwcInstanceRef, constr_10337); wire
    order refs/irefs then VP. Old checklist page claim "p.162" was WRONG (pdf_page: p.111).
    Drift: `__init__` docstring, untyped-old checklists, paraphrased docstrings; rw
    helpers existed with matched names but lacked VARIATION-POINT.
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - note (Steps 5/6): read/writeSwcBswSynchronizedModeGroupPrototype existed with matched
    names; ADDED VARIATION-POINT to both; new None no-op + type-hint pin tests pass.
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - note (Step 8): no deviations — tracker rows already "—"; constr_10336/10337 kept in
    the inline comments (config-time existence constraints).
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-26 (12331 passed / 0 failed, lint clean, black-check clean); 9b deferred to batch confirmation (user instruction)

- [ ] `SwcBswSynchronizedTrigger` — ARObject — R23-11 markdown · Table 5.49 (CP_TPS_BSWModuleDescriptionTemplate), p.111
  - module: M2/AUTOSARTemplates/CommonStructure/SwcBswMapping.py
  - note (Step 1): R23-11 markdown Table 5.49, p.111. Concrete Class; Base = ARObject
    (already correct); VP-capable — VARIATION-POINT in OWN XSD group
    SWC-BSW-SYNCHRONIZED-TRIGGER (seq 10000, atpVariation), mixin kept (Rule 0020). Two
    attrs: bswTrigger (Trigger, 0..1, ref → BSW-TRIGGER-REF, DEST TRIGGER--SUBTYPES-ENUM,
    constr_10300), swcTrigger (Trigger, 0..1, iref → SWC-TRIGGER-IREF /
    PTriggerInAtomicSwcTypeInstanceRef, constr_10301); wire order refs/irefs then VP.
    Drift: `__init__` docstring, paraphrased docstrings, bare `PTriggerInAtomicSwcTypeInstanceRef = None`
    field (not Optional), old 4-col checklist; rw helpers existed with matched names but
    lacked VARIATION-POINT. InstanceRef imports promoted TYPE_CHECKING → runtime
    (repo cycle-breaker pattern; needed for typing.get_type_hints resolution).
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - note (Steps 5/6): read/writeSwcBswSynchronizedTrigger existed with matched names;
    ADDED VARIATION-POINT to both; new type-hint pin test passes.
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - note (Step 8): no deviations — tracker rows already "—"; constr_10300/10301 kept in
    the inline comments (config-time existence constraints).
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-26 (12332 passed / 0 failed, lint clean, black-check clean); 9b deferred to batch confirmation (user instruction)
