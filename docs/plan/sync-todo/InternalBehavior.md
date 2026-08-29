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

- [x] ExclusiveArea (markdown · Table 5.16 · p.82 · source CommonStructure/InternalBehavior.py · member type of InternalBehavior.exclusiveArea — synced first per Rule 0016.5)
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations (none)
  - [x] Step 9 — Verify (9a) ✓ · confirm (9b) ✓ · stamp R23-11 written · commit 610ad11cacb57120b6d65dd1b90117fe463972b3
- [x] InternalBehavior (markdown · Table 5.1 · p.65 · source CommonStructure/InternalBehavior.py · depends on ExclusiveArea above; adds missing constantMemory / constantValueMapping / exclusiveArea / exclusiveAreaNestingOrder members; member classes all exist)
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations (none; constantValueMapping reader/writer gap closed)
  - [x] Step 9 — Verify (9a) ✓ · confirm (9b) ✓ · stamp R23-11 written · commit 6f254bbe8c9c93cdeb6a4f797b453cb056dbc151
- [x] RoleBasedDataTypeAssignment (markdown · Table 12.5 · p.227 · source CommonStructure/ServiceNeeds.py · member type of ServiceDependency.assignedDataType — synced first per Rule 0016.5)
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations (none; setter None-guard added, writer now uses getters)
  - [x] Step 9 — Verify (9a) ✓ · confirm (9b) ✓ · stamp R23-11 written · commit d28752b5382ac1acea8c81d55dfe701f87f75ea9
- [x] ServiceDependency (markdown · Table 12.1 · p.225 · source CommonStructure/ServiceNeeds.py · depends on RoleBasedDataTypeAssignment above; fixes `assigneddatatype` → `assignedDataType`; ServiceDiagnosticRelevanceEnum stub filled with isNotRelevant/isRelevant; DIAGNOSTIC-RELEVANCE reader/writer added)
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations (assignedDataType multiplicity corrected to 0..1 in 9b)
  - [x] Step 9 — Verify (9a) ✓ · confirm (9b) ✓ · stamp R23-11 written · commit c990532058437c2b995e06ba29b11573f54736e1

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
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations (none; ctor fixed to (parent, short_name); BSW-INTERRUPT-EVENT reader/writer dispatch + factory added)
  - [ ] Step 9 — Verify (9a) ✓ · confirm (9b) deferred — stamp pending batch confirmation
- [ ] BswBackgroundEvent (markdown · Table 5.26 · p.89 · source BswModuleTemplate/BswBehavior/__init__.py · base chain out of scope)
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations (none; I/O dispatch already existed)
  - [ ] Step 9 — Verify (9a) ✓ · confirm (9b) deferred — stamp pending batch confirmation
- [ ] BswOsTaskExecutionEvent (markdown · Table 5.27 · p.89 · source BswModuleTemplate/BswBehavior/__init__.py · base chain out of scope)
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations (none; BSW-OS-TASK-EXECUTION-EVENT reader/writer dispatch + factory added)
  - [ ] Step 9 — Verify (9a) ✓ · confirm (9b) deferred — stamp pending batch confirmation
