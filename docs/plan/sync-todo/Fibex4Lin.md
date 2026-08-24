# Sync queue: Fibex4Lin Lin-related classes (deviation doc batch)

Input classes (user request): all Lin-related entries in
`docs/examples/method_deviation_by_class_v2.md`.
Closure gate: user confirmed **all 5 classes + drift fix on LinTpConfig**.
Member/base classes (`ScheduleTableEntry`, `TpConfig`, `TpAddress`, `LinTpConnection`,
`LinTpNode`) exist — not queued except `LinTpNode` (touched for writer drift fix +
docstring sync, stamped like any touched member type). Ref targets `LinSlave`
(missing from codebase) / `LinSlaveConfigIdent` stay plain `RefType` fields per
project convention — **no new classes needed**.

Spec source: `autosar/R23-11/markdown/AUTOSAR_CP_TPS_SystemTemplate.md`
(+ PDF for page numbers only).

Queue order (dependency-first, inputs last):

| # | Class | Role | Spec | Status |
|---|-------|------|------|--------|
| 1 | LinFrame | base (of LinUnconditionalFrame) | Table 6.87, p.428 | [ ] pending stamp |
| 2 | LinUnconditionalFrame | input | Table 6.90, p.429 | [ ] pending stamp |
| 3 | FreeFormatEntry | input | Table 6.98, p.434 | [ ] pending stamp |
| 4 | LinConfigurationEntry | input | Table 6.99, p.434 | [ ] pending 9b re-gate (reader/writer now implemented) |
| 5 | LinTpNode | member (LinTpConfig.tpNode; writer drift fix) | Table 6.260, p.615 | [ ] pending stamp |
| 6 | LinTpConfig | input | Table 6.259, p.614 | [ ] pending stamp |
| 7 | FramePid | member (AssignFrameIdRange.framePid) | Table 6.103, p.437 | [ ] pending 9b |
| 8 | AssignFrameId | concrete subclass (unlocks refs serialization) | Table 6.100, p.436 | [ ] pending 9b |
| 9 | UnassignFrameId | concrete subclass | Table 6.101, p.436 | [ ] pending 9b |
| 10 | AssignFrameIdRange | concrete subclass | Table 6.102, p.437 | [ ] pending 9b |
| 11 | AssignNad | concrete subclass | Table 6.104, p.438 | [ ] pending 9b |
| 12 | ConditionalChangeNad | concrete subclass | Table 6.105, p.438 | [ ] pending 9b |
| 13 | SaveConfigurationEntry | concrete subclass | Table 6.106, p.439 | [ ] pending 9b |
| 14 | DataDumpEntry | concrete subclass | Table 6.107, p.439 | [ ] pending 9b |
| 15 | FreeFormat | concrete subclass (of FreeFormatEntry) | Table 6.108, p.439 | [ ] pending 9b |

Rows 7-15 added mid-sync: at the row-4 9b gate the user ruled **"reader/writer shall
be fixed first"** for LinConfigurationEntry — per Rule 0001.10 that requires its
concrete subclasses (the XSD serializes ASSIGNED-CONTROLLER-REF /
ASSIGNED-LIN-SLAVE-CONFIG-REF only inside concrete entry elements), so the whole
Table 6.100-6.108 family was implemented in this session. `messageId` on
AssignFrameId/UnassignFrameId carries `atp.Status="removed"` in the XSD → not
modeled (Rule 1.3).

Known gaps resolved / remaining:

- RESOLVED LinFrame/LinUnconditionalFrame/FreeFormatEntry: no own attributes
  (`-` rows); verbatim Note docstrings; checklists = self-defined methods only
  (`CanFrame` precedent).
- RESOLVED LinUnconditionalFrame reader/writer dispatch verified.
- LinConfigurationEntry: refs implemented (`assignedControllerRef`,
  `assignedLinSlaveConfigRef`) with verbatim Notes + model tests. Reader/writer
  deferred — XSD group `LIN-CONFIGURATION-ENTRY` serializes inside concrete
  subclass elements only → stamp withheld until that family lands.
- RESOLVED LinTpNode writer parent-element bug (DROP-NOT-REQUESTED-NAD) +
  missing MAX-NUMBER-OF-RESP-PENDING-FRAMES round-trip; docstrings verbatim.
- RESOLVED LinTpConfig stale tracker rows removed; docstrings verbatim;
  empty-wrapper round-trip test added.

Deviation tracker updates applied:
`docs/examples/method_deviation_by_class_v2.md` — LinConfigurationEntry,
LinTpConfig, LinFrame, LinUnconditionalFrame, FreeFormatEntry rows rewritten.

## 1. LinFrame — Table 6.87, p.428

- [x] Step 1 — Sync members & description from spec
- [x] Step 2 — Write the model class unit test (existing tests cover abstract guard + concrete subclass)
- [x] Step 3 — Implement the model class (verified against spec)
- [x] Step 4 — Sync docstrings (wipe & rewrite from markdown)
- [x] Step 5 — Reader/writer round-trip test (N/A: abstract, no own XML tag)
- [x] Step 6 — Parser/writer (N/A: same reason)
- [x] Step 7 — Update checklist comment (`# Spec:` + rows)
- [x] Step 8 — Deviations check (tracker row rewritten)
- [ ] Step 9 — Verify (9a automated) + confirm (9b gate) & stamp

## 2. LinUnconditionalFrame — Table 6.90, p.429

- [x] Step 1 — Sync members & description from spec
- [x] Step 2 — Write the model class unit test (existing)
- [x] Step 3 — Implement the model class (verified)
- [x] Step 4 — Sync docstrings (wipe & rewrite from markdown)
- [x] Step 5 — Reader/writer round-trip test (existing dispatch verified by suite)
- [x] Step 6 — Parser/writer (existing dispatch verified)
- [x] Step 7 — Update checklist comment (`# Spec:` + rows)
- [x] Step 8 — Deviations check
- [ ] Step 9 — Verify (9a automated) + confirm (9b gate) & stamp

## 3. FreeFormatEntry — Table 6.98, p.434

- [x] Step 1 — Sync members & description from spec
- [x] Step 2 — Write the model class unit test (existing)
- [x] Step 3 — Implement the model class (verified)
- [x] Step 4 — Sync docstrings (wipe & rewrite from markdown)
- [x] Step 5 — Reader/writer round-trip test (N/A: abstract, no own XML tag)
- [x] Step 6 — Parser/writer (N/A: same reason)
- [x] Step 7 — Update checklist comment (`# Spec:` + rows)
- [x] Step 8 — Deviations check (concrete FreeFormat subclass deferred; table id corrected 6.99→6.98)
- [ ] Step 9 — Verify (9a automated) + confirm (9b gate) & stamp

## 4. LinConfigurationEntry — Table 6.99, p.434

- [x] Step 1 — Sync members & description from spec
- [x] Step 2 — Write the model class unit test (TestLinConfigurationEntry: defaults/chaining/None-no-op/type annotations)
- [x] Step 3 — Implement the model class (assignedControllerRef/assignedLinSlaveConfigRef)
- [x] Step 4 — Sync docstrings (wipe & rewrite from markdown)
- [x] Step 5 — Reader/writer round-trip test (deferred: needs concrete subclasses)
- [x] Step 6 — Parser/writer (deferred, same reason)
- [x] Step 7 — Update checklist comment (`# Spec:` + rows)
- [x] Step 8 — Deviations check (recorded deferred reader/writer; stamp withheld)
- [ ] Step 9 — Verify (9a automated) + confirm (9b gate)

## 5. LinTpNode — Table 6.260, p.615

- [x] Step 1 — Sync members & description from spec
- [x] Step 2 — Write the model class unit test (existing + round-trip field asserts)
- [x] Step 3 — Implement the model class (Optional-typed fields, verbatim notes)
- [x] Step 4 — Sync docstrings (wipe & rewrite from markdown)
- [x] Step 5 — Write the reader/writer round-trip test (MAX-NUMBER-OF-RESP-PENDING-FRAMES + DROP-NOT-REQUESTED-NAD parent fix; empty-fields case)
- [x] Step 6 — Update the parser (reader) & writer
- [x] Step 7 — Update checklist comment (`# Spec:` + rows)
- [x] Step 8 — Deviations check
- [ ] Step 9 — Verify (9a automated) + confirm (9b gate) & stamp

## 6. LinTpConfig — Table 6.259, p.614

- [x] Step 1 — Sync members & description from spec
- [x] Step 2 — Write the model class unit test (existing)
- [x] Step 3 — Implement the model class (verified: dedicated typed lists)
- [x] Step 4 — Sync docstrings (wipe & rewrite from markdown)
- [x] Step 5 — Write the reader/writer round-trip test (+ empty-wrapper case)
- [x] Step 6 — Update the parser (reader) & writer (verified existing)
- [x] Step 7 — Update checklist comment (`# Spec:` + rows)
- [x] Step 8 — Deviations check (stale tpAddress/tpNode tracker rows removed)
- [ ] Step 9 — Verify (9a automated) + confirm (9b gate) & stamp

## Future queue (out of this batch)

- `ScheduleTableEntry` (Table 6.96): XSD group also carries `INTRODUCTION` before
  `DELAY`; model has the field but parser/writer do not serialize it yet
  (pre-existing gap, outside this batch's confirmed scope).
