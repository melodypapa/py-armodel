# Sync todo: InternalBehavior + BswBehavior cluster (BSW Module Description Template)

Input scope: 10 classes of `AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate` (R23-11),
selected by user from `docs/examples/method_deviation_by_class_v2.md` ("alternates mix").
Generated: 2026-08-24 · Queue reordered 2026-08-24 per user direction: member types
synced BEFORE their dependents (Rule 0016.5).
(resume = first class row still `[ ]`; all class rows `[x]` = sync finished)

Closure confirmed by user 2026-08-24 (framework bases ARObject…Identifiable,
ARElement, ARPackage, AUTOSAR excluded per standing project decision).

Promoted into the queue 2026-08-24 (unstamped stubs referenced by queued classes,
Rule 0016.4/0016.5):
- `ExclusiveArea` — member of InternalBehavior.exclusiveArea
- `RoleBasedDataTypeAssignment` — member of ServiceDependency.assignedDataType
- `BswAsynchronousServerCallPoint` — ref target of BswAsynchronousServerCallResultPoint.asynchronousServerCallPoint

Already stamped, therefore NOT queued (Rule 0012.3): `ExclusiveAreaNestingOrder`
(Table 5.19, p.84).

Out-of-scope stubs deliberately NOT queued (user selected alternates mix over entity/event
bases): `ExecutableEntity`, `AbstractEvent`, `BswScheduleEvent`, `BswModuleCallPoint`,
`BswModuleEntity`, `BswEvent`, `ServiceNeeds`. If a class below turns out to require
restructuring of one of these, add it interactively per Rule 0016.4.

Spec markdown: `autosar/R23-11/markdown/AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.md`
(page numbers via `.claude/skills/sync-autosar-class/pdf_page.py <ClassName>`).
No spec-missing classes → no Rule 0016.4 Skip/XSD decisions required.
Workflow per user instruction: commit each class WITHOUT the stamp after 9a;
stamps written in batch after user confirmation rounds.

## Queue (dependency-first)

### CommonStructure

- [ ] ExclusiveArea (markdown · Table 5.16 · p.82 · source CommonStructure/InternalBehavior.py · member type of InternalBehavior.exclusiveArea — synced first per Rule 0016.5)
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations (none)
  - [ ] Step 9 — Verify (9a) ✓ · confirm (9b) deferred — stamp pending batch confirmation
- [ ] InternalBehavior (markdown · Table 5.1 · p.65 · source CommonStructure/InternalBehavior.py · depends on ExclusiveArea above; adds missing constantMemory / constantValueMapping / exclusiveArea / exclusiveAreaNestingOrder members; member classes all exist)
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations (none; constantValueMapping reader/writer gap closed)
  - [ ] Step 9 — Verify (9a) ✓ · confirm (9b) deferred — stamp pending batch confirmation
- [ ] RoleBasedDataTypeAssignment (markdown · Table 12.5 · p.227 · source CommonStructure/ServiceNeeds.py · member type of ServiceDependency.assignedDataType — synced first per Rule 0016.5)
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations (none; setter None-guard added, writer now uses getters)
  - [ ] Step 9 — Verify (9a) ✓ · confirm (9b) deferred — stamp pending batch confirmation
- [ ] ServiceDependency (markdown · Table 12.1 · p.225 · source CommonStructure/ServiceNeeds.py · depends on RoleBasedDataTypeAssignment above; fixes `assigneddatatype` → `assignedDataType`; ServiceDiagnosticRelevanceEnum stub filled with isNotRelevant/isRelevant; DIAGNOSTIC-RELEVANCE reader/writer added)
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations (none)
  - [ ] Step 9 — Verify (9a) ✓ · confirm (9b) deferred — stamp pending batch confirmation

### BswBehavior leaves

- [ ] BswAsynchronousServerCallPoint (markdown · Table 5.13 · p.80 · source BswModuleTemplate/BswBehavior/__init__.py · ref target of BswAsynchronousServerCallResultPoint — synced first per Rule 0016.5)
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations (none)
  - [ ] Step 9 — Verify (9a) ✓ · confirm (9b) deferred — stamp pending batch confirmation
- [ ] BswAsynchronousServerCallResultPoint (markdown · Table 5.14 · p.80 · source BswModuleTemplate/BswBehavior/__init__.py · depends on BswAsynchronousServerCallPoint above; adds missing asynchronousServerCallPointRef accessors; reader/writer dispatch for BSW-ASYNCHRONOUS-SERVER-CALL-RESULT-POINT added)
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations (none)
  - [ ] Step 9 — Verify (9a) ✓ · confirm (9b) deferred — stamp pending batch confirmation
- [ ] BswSchedulerNamePrefix (markdown · Table 5.20 · p.86 · source BswModuleTemplate/BswBehavior/BswSchedulerNamePrefix.py · leaf)
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations (base fixed ARObject→ImplementationProps; fabricated prefix/getPrefix/setPrefix removed per Rule 0001.3; SCHEDULER-NAME-PREFIXS reader/writer wiring + createSchedulerNamePrefix factory added)
  - [ ] Step 9 — Verify (9a) ✓ · confirm (9b) deferred — stamp pending batch confirmation
- [ ] BswDistinguishedPartition (markdown · Table 5.50 · p.118 · source BswModuleTemplate/BswBehavior/__init__.py · leaf)
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations (none; DISTINGUISHED-PARTITIONS reader/writer wiring + createDistinguishedPartition factory added)
  - [ ] Step 9 — Verify (9a) ✓ · confirm (9b) deferred — stamp pending batch confirmation

### BswBehavior entities/events (bases out of scope, see note above)

- [ ] BswCalledEntity (markdown · Table 5.6 · p.74 · source BswModuleTemplate/BswBehavior/__init__.py · base BswModuleEntity out of scope)
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations (none; no own attributes, I/O via BswInternalBehavior entity dispatch already covered)
  - [ ] Step 9 — Verify (9a) ✓ · confirm (9b) deferred — stamp pending batch confirmation
- [ ] BswSchedulableEntity (markdown · Table 5.7 · p.75 · source BswModuleTemplate/BswBehavior/__init__.py · base BswModuleEntity out of scope)
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations (none; no own attributes, I/O via BswInternalBehavior entity dispatch already covered)
  - [ ] Step 9 — Verify (9a) ✓ · confirm (9b) deferred — stamp pending batch confirmation
- [ ] BswInterruptEvent (markdown · Table 5.24 · p.88 · source BswModuleTemplate/BswBehavior/BswInterruptEvent.py · base chain out of scope)
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] BswBackgroundEvent (markdown · Table 5.26 · p.89 · source BswModuleTemplate/BswBehavior/__init__.py · base chain out of scope)
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] BswOsTaskExecutionEvent (markdown · Table 5.27 · p.89 · source BswModuleTemplate/BswBehavior/__init__.py · base chain out of scope)
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
