# Sync queue: FlexrayCluster + FlexrayCommunicationController

Input classes: `FlexrayCluster`, `FlexrayCommunicationController` (user request).
Closure gate: user confirmed **"Also re-sync base classes"** — bases `CommunicationCluster`,
`CommunicationController` are queued; missing member types `FlexrayFifoRange`,
`FlexrayFifoConfiguration` are implemented from spec (both have full PDF/markdown tables,
no Skip/XSD resolution needed).

Spec source: `autosar/markdown/AUTOSAR_CP_TPS_SystemTemplate.md` (+ `autosar/pdf/AUTOSAR_CP_TPS_SystemTemplate.pdf` for page numbers only).

Queue order (dependency-first, deepest ancestors first, inputs last):

| # | Class | Role | Spec | Status |
|---|-------|------|------|--------|
| 1 | CommunicationCluster | base (of FlexrayCluster) | Table 3.6, p.57 | [x] done (feat: bc4f9ede) |
| 2 | CommunicationController | base (of FlexrayCommunicationController) | Table 3.3, p.53 | [x] done (feat: 3d58717f) |
| 3 | FlexrayFifoRange | member (FlexrayFifoConfiguration.fifoRange) | Table 3.32, p.87 | [x] done (feat: 468c3416) |
| 4 | FlexrayFifoConfiguration | member (FlexrayCommunicationController.flexrayFifo) | Table 3.31, p.87 | [ ] pending |
| 5 | FlexrayCommunicationController | input | Table 3.30, p.86 | [ ] pending |
| 6 | FlexrayCluster | input | Table 3.29 (+preceding block), p.81 | [ ] pending |

Known gaps to fix during sync:

- CommunicationCluster: `baudrate` typed `ARFloat` but spec says `PositiveUnlimitedInteger`;
  `getPhysicalChannels*` filter the elements registry instead of the dedicated `physicalChannel`
  list (Rule 0004); docstrings are paraphrases; no `# Spec:` block.
- CommunicationController: single attr `wakeUpByControllerSupported` exists; needs docstrings
  (spec Note), checklist, tests, reader/writer coverage (currently none).
- FlexrayCluster: reader/writer drop `symbolWindow`, `symbolWindowActionPointOffset`,
  `tranceiverStandbyDelay`; `# type:` comments instead of PEP 526; docstrings paraphrased.
- FlexrayCommunicationController: `flexrayFifos` aggr has no model class, reader, or writer;
  `# type:`-style members vs PEP 526; docstrings paraphrased.

## 1. CommunicationCluster — Table 3.6, p.57

- [x] Step 1 — Sync members & description from spec
- [x] Step 2 — Write the model class unit test (Red)
- [x] Step 3 — Implement the model class (Green)
- [x] Step 4 — Sync docstrings (wipe & rewrite from markdown)
- [x] Step 5 — Write the reader/writer round-trip test (Red)
- [x] Step 6 — Update the parser (reader) & writer (Green)
- [x] Step 7 — Update checklist comment (`# Spec:` + rows)
- [x] Step 8 — Deviations check (referenced classes, placeholders)
- [ ] Step 9 — Verify (9a automated) + confirm (9b gate) & stamp

## 2. CommunicationController — Table 3.3, p.53

- [ ] Step 1 — Sync members & description from spec
- [ ] Step 2 — Write the model class unit test (Red)
- [ ] Step 3 — Implement the model class (Green)
- [ ] Step 4 — Sync docstrings (wipe & rewrite from markdown)
- [ ] Step 5 — Write the reader/writer round-trip test (Red)
- [ ] Step 6 — Update the parser (reader) & writer (Green)
- [ ] Step 7 — Update checklist comment (`# Spec:` + rows)
- [ ] Step 8 — Deviations check (referenced classes, placeholders)
- [ ] Step 9 — Verify (9a automated) + confirm (9b gate) & stamp

## 3. FlexrayFifoRange — Table 3.32, p.87

- [ ] Step 1 — Sync members & description from spec
- [ ] Step 2 — Write the model class unit test (Red)
- [ ] Step 3 — Implement the model class (Green)
- [ ] Step 4 — Sync docstrings (wipe & rewrite from markdown)
- [ ] Step 5 — Write the reader/writer round-trip test (Red)
- [ ] Step 6 — Update the parser (reader) & writer (Green)
- [ ] Step 7 — Update checklist comment (`# Spec:` + rows)
- [ ] Step 8 — Deviations check (referenced classes, placeholders)
- [ ] Step 9 — Verify (9a automated) + confirm (9b gate) & stamp

## 4. FlexrayFifoConfiguration — Table 3.31, p.87

- [ ] Step 1 — Sync members & description from spec
- [ ] Step 2 — Write the model class unit test (Red)
- [ ] Step 3 — Implement the model class (Green)
- [ ] Step 4 — Sync docstrings (wipe & rewrite from markdown)
- [ ] Step 5 — Write the reader/writer round-trip test (Red)
- [ ] Step 6 — Update the parser (reader) & writer (Green)
- [ ] Step 7 — Update checklist comment (`# Spec:` + rows)
- [ ] Step 8 — Deviations check (referenced classes, placeholders)
- [ ] Step 9 — Verify (9a automated) + confirm (9b gate) & stamp

## 5. FlexrayCommunicationController — Table 3.30, p.86

- [ ] Step 1 — Sync members & description from spec
- [ ] Step 2 — Write the model class unit test (Red)
- [ ] Step 3 — Implement the model class (Green)
- [ ] Step 4 — Sync docstrings (wipe & rewrite from markdown)
- [ ] Step 5 — Write the reader/writer round-trip test (Red)
- [ ] Step 6 — Update the parser (reader) & writer (Green)
- [ ] Step 7 — Update checklist comment (`# Spec:` + rows)
- [ ] Step 8 — Deviations check (referenced classes, placeholders)
- [ ] Step 9 — Verify (9a automated) + confirm (9b gate) & stamp

## 6. FlexrayCluster — Table 3.29, p.81

- [ ] Step 1 — Sync members & description from spec
- [ ] Step 2 — Write the model class unit test (Red)
- [ ] Step 3 — Implement the model class (Green)
- [ ] Step 4 — Sync docstrings (wipe & rewrite from markdown)
- [ ] Step 5 — Write the reader/writer round-trip test (Red)
- [ ] Step 6 — Update the parser (reader) & writer (Green)
- [ ] Step 7 — Update checklist comment (`# Spec:` + rows)
- [ ] Step 8 — Deviations check (referenced classes, placeholders)
- [ ] Step 9 — Verify (9a automated) + confirm (9b gate) & stamp
