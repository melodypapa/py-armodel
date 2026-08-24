# Sync queue: Fibex4Lin Lin-related classes (deviation doc batch)

> RESET (2026-08-24): all classes unchecked by user request — the whole queue is
> re-synced from scratch. Prior step-completion annotations were dropped with the
> reset; findings survive in the notes below. During the review the queue was
> re-analyzed dependency-first and extended with the previously missing
> dependent base **ScheduleTableEntry** (now #1).

Input classes (user request): all Lin-related entries in
`docs/examples/method_deviation_by_class_v2.md`.
Closure gate: user confirmed **all 5 classes + drift fix on LinTpConfig**;
extended in review with **ScheduleTableEntry** — direct `Base` of BOTH
`FreeFormatEntry` and `LinConfigurationEntry`, previously misclassified as
"exists, skip": it carries no `# Spec verified:` marker, a stale checklist,
trailing `# type:` comments, and the known INTRODUCTION reader/writer gap
(Rule 0016.5 — "exists" is not a stamp). Member/base classes (`TpConfig`,
`TpAddress`, `LinTpConnection`, `LinTpNode`) exist — not queued except
`LinTpNode` (touched for writer drift fix + docstring sync, stamped like any
touched member type). Ref targets `LinSlave` (missing from codebase) /
`LinSlaveConfigIdent` stay plain `RefType` fields per project convention —
**no new classes needed**.

Dependency analysis (code:
`src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Lin/LinCommunication.py`,
`.../SystemTemplate/TransportProtocols.py`; spec markdown Base rows):

- `ScheduleTableEntry` ← `FreeFormatEntry` ← `FreeFormat`
- `ScheduleTableEntry` ← `LinConfigurationEntry` ← {`AssignFrameId`,
  `UnassignFrameId`, `AssignFrameIdRange` (+ `FramePid` member), `AssignNad`,
  `ConditionalChangeNad`, `SaveConfigurationEntry`, `DataDumpEntry`}
- `LinFrame` ← `LinUnconditionalFrame`
- `LinTpNode` = member of `LinTpConfig.tpNode`

Spec source: `autosar/R23-11/markdown/AUTOSAR_CP_TPS_SystemTemplate.md`
(+ PDF for page numbers only).

Queue order (dependency-first, inputs last):

| # | Class | Role | Spec | Status |
|---|-------|------|------|--------|
| 1 | ScheduleTableEntry | base (of FreeFormatEntry + LinConfigurationEntry) | Table 6.96, p.433 | [x] done — commit `938590e` |
| 2 | LinFrame | base (of LinUnconditionalFrame) | Table 6.87, p.428 | [x] done — commit `f69950a` |
| 3 | LinUnconditionalFrame | input | Table 6.90, p.429 | [x] done — re-synced, commit `05b97c7`; stamped R23-11 in batch review |
| 4 | FreeFormatEntry | input | Table 6.98, p.434 | [x] done — re-synced, commit `05b97c7`; stamped R23-11 in batch review |
| 5 | LinConfigurationEntry | input | Table 6.99, p.434 | [x] done — re-synced, commit `05b97c7`; stamped R23-11 in batch review |
| 6 | LinTpNode | member (LinTpConfig.tpNode) | Table 6.260, p.615 | [x] done — re-synced, commit `05b97c7`; stamped R23-11 in batch review |
| 7 | LinTpConfig | input | Table 6.259, p.614 | [x] done — re-synced, commit `05b97c7`; stamped R23-11 in batch review |
| 8 | FramePid | member (AssignFrameIdRange.framePid) | Table 6.103, p.437 | [x] done — re-synced, commit `05b97c7`; stamped R23-11 in batch review |
| 9 | AssignFrameId | concrete subclass (unlocks refs serialization) | Table 6.100, p.436 | [x] done — re-synced, commit `05b97c7`; stamped R23-11 in batch review |
| 10 | UnassignFrameId | concrete subclass | Table 6.101, p.436 | [x] done — re-synced, commit `05b97c7`; stamped R23-11 in batch review |
| 11 | AssignFrameIdRange | concrete subclass | Table 6.102, p.437 | [x] done — re-synced, commit `05b97c7`; stamped R23-11 in batch review |
| 12 | AssignNad | concrete subclass | Table 6.104, p.438 | [x] done — re-synced, commit `05b97c7`; stamped R23-11 in batch review |
| 13 | ConditionalChangeNad | concrete subclass | Table 6.105, p.438 | [x] done — re-synced, commit `05b97c7`; stamped R23-11 in batch review |
| 14 | SaveConfigurationEntry | concrete subclass | Table 6.106, p.439 | [x] done — re-synced, commit `05b97c7`; stamped R23-11 in batch review |
| 15 | DataDumpEntry | concrete subclass | Table 6.107, p.439 | [x] done — re-synced, commit `05b97c7`; stamped R23-11 in batch review |
| 16 | FreeFormat | concrete subclass (of FreeFormatEntry) | Table 6.108, p.439 | [x] done — re-synced, commit `05b97c7`; stamped R23-11 in batch review |

History: rows 9-16 (former 8-15) added mid-sync of a previous pass: at the
then-row-4 9b gate the user ruled **"reader/writer shall be fixed first"** for
LinConfigurationEntry — per Rule 0001.10 that requires its concrete subclasses
(the XSD serializes ASSIGNED-CONTROLLER-REF / ASSIGNED-LIN-SLAVE-CONFIG-REF only
inside concrete entry elements), so the whole Table 6.100-6.108 family was
implemented. `messageId` on AssignFrameId/UnassignFrameId carries
`atp.Status="removed"` in the XSD → not modeled (Rule 1.3).

Known gaps carried into the reset (code state persists even though progress
is unchecked):

- ScheduleTableEntry: model has `introduction` (DocumentationBlock) but parser/
  writer do not serialize it yet — main reason row 1 is queued.
- LinConfigurationEntry refs implemented (`assignedControllerRef`,
  `assignedLinSlaveConfigRef`) with verbatim Notes + model tests; their
  reader/writer serialization lives in concrete subclass elements → covered by
  rows 9-15; stamp gates on that family landing.
- LinFrame/LinUnconditionalFrame/FreeFormatEntry: no own attributes (`-` rows);
  verbatim Note docstrings; checklists = self-defined methods only
  (`CanFrame` precedent).
- LinTpNode writer parent-element bug (DROP-NOT-REQUESTED-NAD) +
  missing MAX-NUMBER-OF-RESP-PENDING-FRAMES round-trip fixed in previous pass —
  re-verify during re-sync.
- LinTpConfig empty-wrapper round-trip test added in previous pass — re-verify.

Deviation tracker: `docs/examples/method_deviation_by_class_v2.md` rows for
LinConfigurationEntry, LinTpConfig, LinFrame, LinUnconditionalFrame,
FreeFormatEntry were rewritten in the previous pass — re-check against the
re-synced classes.

## 1. ScheduleTableEntry — Table 6.96, p.433

- [x] Step 1 — Sync members & description from spec
- [x] Step 2 — Write the model class unit test
- [x] Step 3 — Implement the model class
- [x] Step 4 — Sync docstrings (wipe & rewrite from markdown)
- [x] Step 5 — Write the reader/writer round-trip test
- [x] Step 6 — Update the parser (reader) & writer
- [x] Step 7 — Update checklist comment (`# Spec:` + rows)
- [x] Step 8 — Deviations check
- [x] Step 9 — Verify (9a automated) + confirm (9b gate) & stamp

## 2. LinFrame — Table 6.87, p.428

- [x] Step 1 — Sync members & description from spec
- [x] Step 2 — Write the model class unit test
- [x] Step 3 — Implement the model class (verified: no own attributes, guard present)
- [x] Step 4 — Sync docstrings (wipe & rewrite from markdown; already verbatim Note)
- [x] Step 5 — Reader/writer round-trip test (N/A: abstract, no own XML tag)
- [x] Step 6 — Parser/writer (N/A: same reason)
- [x] Step 7 — Update checklist comment (`# Spec:` + rows)
- [x] Step 8 — Deviations check
- [x] Step 9 — Verify (9a automated) + confirm (9b gate) & stamp

## 3. LinUnconditionalFrame — Table 6.90, p.429

- [x] Step 1 — Sync members & description from spec
- [x] Step 2 — Write the model class unit test
- [x] Step 3 — Implement the model class
- [x] Step 4 — Sync docstrings (wipe & rewrite from markdown; already verbatim Note, no own attributes)
- [x] Step 5 — Write the reader/writer round-trip test (dispatch tests exist in parser/writer folders)
- [x] Step 6 — Update the parser (reader) & writer (read/writeLinUnconditionalFrame → read/writeFrame)
- [x] Step 7 — Update checklist comment (`# Spec:` + rows)
- [x] Step 8 — Deviations check (none)
- [x] Step 9 — Verify (9a automated) + confirm (9b gate) & stamp (stamp DEFERRED to batch gate)

## 4. FreeFormatEntry — Table 6.98, p.434

- [x] Step 1 — Sync members & description from spec (no own attrs; Note = XSD group doc verbatim)
- [x] Step 2 — Write the model class unit test
- [x] Step 3 — Implement the model class
- [x] Step 4 — Sync docstrings (wipe & rewrite from markdown)
- [x] Step 5 — Write the reader/writer round-trip test (N/A: abstract, no own XML tag; round-trips via FreeFormat)
- [x] Step 6 — Parser/writer (N/A: same reason)
- [x] Step 7 — Update checklist comment (`# Spec:` + rows)
- [x] Step 8 — Deviations check (none)
- [x] Step 9 — Verify (9a automated) + confirm (9b gate) & stamp (stamp DEFERRED to batch gate)

## 5. LinConfigurationEntry — Table 6.99, p.434

- [x] Step 1 — Sync members & description from spec
- [x] Step 2 — Write the model class unit test
- [x] Step 3 — Implement the model class
- [x] Step 4 — Sync docstrings (wipe & rewrite from markdown)
- [x] Step 5 — Write the reader/writer round-trip test (refs serialize via concrete subclass dispatch, rows 9-15)
- [x] Step 6 — Parser/writer (same as Step 5)
- [x] Step 7 — Update checklist comment (`# Spec:` + rows)
- [x] Step 8 — Deviations check (none; ref targets stay RefType per Phase 0 decision)
- [x] Step 9 — Verify (9a automated) + confirm (9b gate) & stamp (stamp DEFERRED to batch gate)

## 6. LinTpNode — Table 6.260, p.615

- [x] Step 1 — Sync members & description from spec
- [x] Step 2 — Write the model class unit test
- [x] Step 3 — Implement the model class
- [x] Step 4 — Sync docstrings (wipe & rewrite from markdown)
- [x] Step 5 — Write the reader/writer round-trip test
- [x] Step 6 — Update the parser (reader) & writer
- [x] Step 7 — Update checklist comment (`# Spec:` + rows)
- [x] Step 8 — Deviations check (none)
- [x] Step 9 — Verify (9a automated) + confirm (9b gate) & stamp (stamp DEFERRED to batch gate)

## 7. LinTpConfig — Table 6.259, p.614

- [x] Step 1 — Sync members & description from spec
- [x] Step 2 — Write the model class unit test
- [x] Step 3 — Implement the model class
- [x] Step 4 — Sync docstrings (wipe & rewrite from markdown)
- [x] Step 5 — Write the reader/writer round-trip test (incl. empty-wrapper cases)
- [x] Step 6 — Update the parser (reader) & writer
- [x] Step 7 — Update checklist comment (`# Spec:` + rows)
- [x] Step 8 — Deviations check (none; addTpConnection shape correct — TpConnection non-Referrable)
- [x] Step 9 — Verify (9a automated) + confirm (9b gate) & stamp (stamp DEFERRED to batch gate)

## 8. FramePid — Table 6.103, p.437

- [x] Step 1 — Sync members & description from spec
- [x] Step 2 — Write the model class unit test
- [x] Step 3 — Implement the model class
- [x] Step 4 — Sync docstrings (wipe & rewrite from markdown)
- [x] Step 5 — Write the reader/writer round-trip test
- [x] Step 6 — Update the parser (reader) & writer
- [x] Step 7 — Update checklist comment (`# Spec:` + rows)
- [x] Step 8 — Deviations check
- [x] Step 9 — Verify (9a automated) + confirm (9b gate) & stamp

## 9. AssignFrameId — Table 6.100, p.436

- [x] Step 1 — Sync members & description from spec
- [x] Step 2 — Write the model class unit test
- [x] Step 3 — Implement the model class
- [x] Step 4 — Sync docstrings (wipe & rewrite from markdown)
- [x] Step 5 — Write the reader/writer round-trip test
- [x] Step 6 — Update the parser (reader) & writer
- [x] Step 7 — Update checklist comment (`# Spec:` + rows)
- [x] Step 8 — Deviations check
- [x] Step 9 — Verify (9a automated) + confirm (9b gate) & stamp

## 10. UnassignFrameId — Table 6.101, p.436

- [x] Step 1 — Sync members & description from spec
- [x] Step 2 — Write the model class unit test
- [x] Step 3 — Implement the model class
- [x] Step 4 — Sync docstrings (wipe & rewrite from markdown)
- [x] Step 5 — Write the reader/writer round-trip test
- [x] Step 6 — Update the parser (reader) & writer
- [x] Step 7 — Update checklist comment (`# Spec:` + rows)
- [x] Step 8 — Deviations check
- [x] Step 9 — Verify (9a automated) + confirm (9b gate) & stamp

## 11. AssignFrameIdRange — Table 6.102, p.437

- [x] Step 1 — Sync members & description from spec
- [x] Step 2 — Write the model class unit test
- [x] Step 3 — Implement the model class
- [x] Step 4 — Sync docstrings (wipe & rewrite from markdown)
- [x] Step 5 — Write the reader/writer round-trip test
- [x] Step 6 — Update the parser (reader) & writer
- [x] Step 7 — Update checklist comment (`# Spec:` + rows)
- [x] Step 8 — Deviations check
- [x] Step 9 — Verify (9a automated) + confirm (9b gate) & stamp

## 12. AssignNad — Table 6.104, p.438

- [x] Step 1 — Sync members & description from spec
- [x] Step 2 — Write the model class unit test
- [x] Step 3 — Implement the model class
- [x] Step 4 — Sync docstrings (wipe & rewrite from markdown)
- [x] Step 5 — Write the reader/writer round-trip test
- [x] Step 6 — Update the parser (reader) & writer
- [x] Step 7 — Update checklist comment (`# Spec:` + rows)
- [x] Step 8 — Deviations check
- [x] Step 9 — Verify (9a automated) + confirm (9b gate) & stamp

## 13. ConditionalChangeNad — Table 6.105, p.438

- [x] Step 1 — Sync members & description from spec
- [x] Step 2 — Write the model class unit test
- [x] Step 3 — Implement the model class
- [x] Step 4 — Sync docstrings (wipe & rewrite from markdown)
- [x] Step 5 — Write the reader/writer round-trip test
- [x] Step 6 — Update the parser (reader) & writer
- [x] Step 7 — Update checklist comment (`# Spec:` + rows)
- [x] Step 8 — Deviations check
- [x] Step 9 — Verify (9a automated) + confirm (9b gate) & stamp

## 14. SaveConfigurationEntry — Table 6.106, p.439

- [x] Step 1 — Sync members & description from spec
- [x] Step 2 — Write the model class unit test
- [x] Step 3 — Implement the model class
- [x] Step 4 — Sync docstrings (wipe & rewrite from markdown)
- [x] Step 5 — Write the reader/writer round-trip test
- [x] Step 6 — Update the parser (reader) & writer
- [x] Step 7 — Update checklist comment (`# Spec:` + rows)
- [x] Step 8 — Deviations check
- [x] Step 9 — Verify (9a automated) + confirm (9b gate) & stamp

## 15. DataDumpEntry — Table 6.107, p.439

- [x] Step 1 — Sync members & description from spec
- [x] Step 2 — Write the model class unit test
- [x] Step 3 — Implement the model class
- [x] Step 4 — Sync docstrings (wipe & rewrite from markdown)
- [x] Step 5 — Write the reader/writer round-trip test
- [x] Step 6 — Update the parser (reader) & writer
- [x] Step 7 — Update checklist comment (`# Spec:` + rows)
- [x] Step 8 — Deviations check
- [x] Step 9 — Verify (9a automated) + confirm (9b gate) & stamp

## 16. FreeFormat — Table 6.108, p.439

- [x] Step 1 — Sync members & description from spec
- [x] Step 2 — Write the model class unit test
- [x] Step 3 — Implement the model class
- [x] Step 4 — Sync docstrings (wipe & rewrite from markdown)
- [x] Step 5 — Write the reader/writer round-trip test
- [x] Step 6 — Update the parser (reader) & writer
- [x] Step 7 — Update checklist comment (`# Spec:` + rows)
- [x] Step 8 — Deviations check
- [x] Step 9 — Verify (9a automated) + confirm (9b gate) & stamp

## Future queue (out of this batch)

- `ApplicationEntry` (concrete subclass of ScheduleTableEntry, sibling of the
  queued entries): once row 1 lands DELAY/INTRODUCTION/POSITION-IN-TABLE
  reader/writer coverage, APPLICATION-ENTRY serializes the same XSD
  SCHEDULE-TABLE-ENTRY group → expect drift fix there. Not in this batch's
  confirmed closure — queue separately if the user confirms.
