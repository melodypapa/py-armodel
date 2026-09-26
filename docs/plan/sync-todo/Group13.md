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

## Queue (dependency-first)

- [ ] `BswApiOptions` — ARObject — source TBC (locate table at Step 1)
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
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-25 (11997 passed / 0 failed, npm run lint clean, black-check clean); 9b deferred to batch confirmation (user instruction)

- [ ] `BswModuleCallPoint` — Referrable — source TBC (locate table at Step 1)
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
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-26 (12014 passed / 0 failed, lint clean, black-check clean); 9b deferred to batch confirmation (user instruction)

- [ ] `BswDirectCallPoint` — BswModuleCallPoint — source TBC (locate table at Step 1)
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
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-26 (12018 passed / 0 failed, lint clean, black-check clean); 9b deferred to batch confirmation (user instruction)

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
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `BswModeManagerErrorEvent` — BswScheduleEvent — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior.py
  - note: deviation-tracked in method_deviation_by_class.md — review entries at Step 1
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `BswModeSwitchedAckEvent` — BswScheduleEvent — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior.py
  - note: deviation-tracked in method_deviation_by_class.md — review entries at Step 1
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `BswTimingEvent` — BswScheduleEvent — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior.py
  - note: deviation-tracked in method_deviation_by_class.md — review entries at Step 1
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `BswEntryRelationshipEnum` — AREnum — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/BswModuleTemplate/BswInterfaces.py
  - note: deviation-tracked in method_deviation_by_class.md + method_deviation_by_class_v2.md — review entries at Step 1
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `BswEntryRelationship` — ARObject — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/BswModuleTemplate/BswInterfaces.py
  - note: deviation-tracked in method_deviation_by_class.md + method_deviation_by_class_v2.md — review entries at Step 1
  - after `BswEntryRelationshipEnum`
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `BswEntryRelationshipSet` — Identifiable — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/BswModuleTemplate/BswInterfaces.py
  - note: deviation-tracked in method_deviation_by_class.md — review entries at Step 1
  - after `BswEntryRelationship`
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `BswModuleClientServerEntry` — Referrable — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/BswModuleTemplate/BswInterfaces.py
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `BswModuleDependency` — Identifiable — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/BswModuleTemplate/BswInterfaces.py
  - note: deviation-tracked in method_deviation_by_class.md — review entries at Step 1
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `SwcBswRunnableMapping` — ARObject — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/CommonStructure/SwcBswMapping.py
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `SwcBswSynchronizedModeGroupPrototype` — ARObject — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/CommonStructure/SwcBswMapping.py
  - note: deviation-tracked in method_deviation_by_class.md — review entries at Step 1
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `SwcBswSynchronizedTrigger` — ARObject — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/CommonStructure/SwcBswMapping.py
  - note: deviation-tracked in method_deviation_by_class.md — review entries at Step 1
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
