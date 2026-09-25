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
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `BswSynchronousServerCallPoint` — BswModuleCallPoint — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior.py
  - after `BswModuleCallPoint`
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `BswInternalTriggeringPoint` — Identifiable — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior.py
  - note: deviation-tracked in method_deviation_by_class_v2.md — review entries at Step 1
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `BswInterruptEntity` — BswModuleEntity — source TBC (locate table at Step 1)
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

- [ ] `BswModeSwitchAckRequest` — ARObject — source TBC (locate table at Step 1)
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

- [ ] `BswQueuedDataReceptionPolicy` — BswDataReceptionPolicy — source TBC (locate table at Step 1)
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

- [ ] `BswAsynchronousServerCallReturnsEvent` — BswScheduleEvent — source TBC (locate table at Step 1)
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

- [ ] `BswDataReceivedEvent` — BswScheduleEvent — source TBC (locate table at Step 1)
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
