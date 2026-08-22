# Sync queue: LinCluster + LinMaster

Input classes: `LinCluster`, `LinMaster` (user request).
Closure gate: user confirmed **"Core 4 + LinSlaveConfig members"** — bases `LinCommunicationController`
(unstamped stub) and missing member type `LinSlaveConfig` plus its members `LinSlaveConfigIdent`,
`LinErrorResponse`, `LinConfigurableFrame`, `LinOrderedConfigurableFrame` are queued.
`CommunicationCluster` / `CommunicationController` skipped (stamped R23-11). Primitives
(`TimeValue`, `Integer`, `PositiveInteger`, `String`) and ref targets (`ISignalTriggering`,
`LinFrame`) exist — not queued. No missing-spec classes → no Skip/XSD resolution needed.

Placement decision: **LinCluster moves from `FibexCore/CoreTopology.py` to
`Fibex4Lin/LinTopology.py`** (spec package exact match; user chose Move). Requires updating
imports in `ARPackage.py`, `parser/arxml_parser.py`, `writer/arxml_writer.py`.
`LinErrorResponse` spec package is `Fibex4Lin::LinCommunication` (Table 3.42) — decide its
file placement at its own sync session.

Spec source: `autosar/markdown/AUTOSAR_CP_TPS_SystemTemplate.md` (+ `autosar/pdf/AUTOSAR_CP_TPS_SystemTemplate.pdf` for page numbers only).

Queue order (dependency-first, deepest ancestors first, inputs last):

| # | Class | Role | Spec | Status |
|---|-------|------|------|--------|
| 1 | LinCommunicationController | base (of LinMaster) | Table 3.37, p.93 | [x] done |
| 2 | LinSlaveConfigIdent | member (LinSlaveConfig.ident) | Table 3.40, p.95 | [x] done |
| 3 | LinErrorResponse | member (LinSlaveConfig.linErrorResponse) | Table 3.42, p.97 | [x] done |
| 4 | LinConfigurableFrame | member (LinSlaveConfig.linConfigurableFrame) | Table 3.44, p.99 | [x] done |
| 5 | LinOrderedConfigurableFrame | member (LinSlaveConfig.linOrderedConfigurableFrame) | Table 3.45, p.99 | [ ] pending |
| 6 | LinSlaveConfig | member (LinMaster.linSlave) | Table 3.39, p.95 | [ ] pending |
| 7 | LinCluster | input | Table 3.36, p.93 | [ ] pending |
| 8 | LinMaster | input | Table 3.38, p.94 | [ ] pending |

Known gaps to fix during sync:

- LinCommunicationController: exists unstamped; docstrings paraphrased; no `# Spec:` line; no
  model tests; parser/writer already cover PROTOCOL-VERSION (verify during session).
- LinMaster: `linSlaves` is an untyped list, `addLinSlaves` misnamed (spec attr `linSlave` `*`
  aggr → dedicated `List[LinSlaveConfig]`, `getLinSlaves`/`addLinSlave`); LIN-SLAVE elements
  are dropped by parser and writer entirely; docstrings paraphrased.
- LinSlaveConfig + members: classes missing from model entirely; no reader/writer coverage.
- LinCluster: no own attributes; unstamped; must move to `LinTopology.py` per placement
  decision.
- LinErrorResponse: `responseError` is a `ref` to ISignalTriggering (Kind-suffix naming:
  `getResponseErrorRef`/`setResponseErrorRef`).
- LinConfigurableFrame / LinOrderedConfigurableFrame: `frame` is a `ref` to LinFrame; note
  LinCommunicationConnector (Table 3.43, out of closure) also aggregates these classes.

## 1. LinCommunicationController — Table 3.37, p.93

- [x] Step 1 — Sync members & description from spec
- [x] Step 2 — Write the model class unit test (Red)
- [x] Step 3 — Implement the model class (Green)
- [x] Step 4 — Sync docstrings (wipe & rewrite from markdown)
- [x] Step 5 — Write the reader/writer round-trip test (Red)
- [x] Step 6 — Update the parser (reader) & writer (Green)
- [x] Step 7 — Update checklist comment (`# Spec:` + rows)
- [x] Step 8 — Deviations check (referenced classes, placeholders)
- [x] Step 9 — Verify (9a automated) + confirm (9b gate) & stamp

## 2. LinSlaveConfigIdent — Table 3.40, p.95

- [x] Step 1 — Sync members & description from spec
- [x] Step 2 — Write the model class unit test (Red)
- [x] Step 3 — Implement the model class (Green)
- [x] Step 4 — Sync docstrings (wipe & rewrite from markdown)
- [x] Step 5 — Write the reader/writer round-trip test (Red)  N/A: no own XML attributes; only aggregation LinSlaveConfig.ident is queued (#6)
- [x] Step 6 — Update the parser (reader) & writer (Green)  N/A deferred to LinSlaveConfig session
- [x] Step 7 — Update checklist comment (`# Spec:` + rows)
- [x] Step 8 — Deviations check (referenced classes, placeholders)
- [x] Step 9 — Verify (9a automated) + confirm (9b gate) & stamp

## 3. LinErrorResponse — Table 3.42, p.97

- [x] Step 1 — Sync members & description from spec
- [x] Step 2 — Write the model class unit test (Red)
- [x] Step 3 — Implement the model class (Green)
- [x] Step 4 — Sync docstrings (wipe & rewrite from markdown)
- [x] Step 5 — Write the reader/writer round-trip test (Red)  standalone getLinErrorResponse/setLinErrorResponse; aggregators (#6) not synced yet
- [x] Step 6 — Update the parser (reader) & writer (Green)  standalone helper for RefType
- [x] Step 7 — Update checklist comment (`# Spec:` + rows)
- [x] Step 8 — Deviations check (referenced classes, placeholders)
- [x] Step 9 — Verify (9a automated) + confirm (9b gate) & stamp

## 4. LinConfigurableFrame — Table 3.44, p.99

- [x] Step 1 — Sync members & description from spec
- [x] Step 2 — Write the model class unit test (Red)
- [x] Step 3 — Implement the model class (Green)
- [x] Step 4 — Sync docstrings (wipe & rewrite from markdown)
- [x] Step 5 — Write the reader/writer round-trip test (Red)  standalone getLinConfigurableFrame/setLinConfigurableFrame; aggregators (#6) not synced yet
- [x] Step 6 — Update the parser (reader) & writer (Green)  standalone helper for RefType + PositiveInteger
- [x] Step 7 — Update checklist comment (`# Spec:` + rows)
- [x] Step 8 — Deviations check (referenced classes, placeholders)
- [x] Step 9 — Verify (9a automated) + confirm (9b gate) & stamp

## 5. LinOrderedConfigurableFrame — Table 3.45, p.99

- [ ] Step 1 — Sync members & description from spec
- [ ] Step 2 — Write the model class unit test (Red)
- [ ] Step 3 — Implement the model class (Green)
- [ ] Step 4 — Sync docstrings (wipe & rewrite from markdown)
- [ ] Step 5 — Write the reader/writer round-trip test (Red)
- [ ] Step 6 — Update the parser (reader) & writer (Green)
- [ ] Step 7 — Update checklist comment (`# Spec:` + rows)
- [ ] Step 8 — Deviations check (referenced classes, placeholders)
- [ ] Step 9 — Verify (9a automated) + confirm (9b gate) & stamp

## 6. LinSlaveConfig — Table 3.39, p.95

- [ ] Step 1 — Sync members & description from spec
- [ ] Step 2 — Write the model class unit test (Red)
- [ ] Step 3 — Implement the model class (Green)
- [ ] Step 4 — Sync docstrings (wipe & rewrite from markdown)
- [ ] Step 5 — Write the reader/writer round-trip test (Red)
- [ ] Step 6 — Update the parser (reader) & writer (Green)
- [ ] Step 7 — Update checklist comment (`# Spec:` + rows)
- [ ] Step 8 — Deviations check (referenced classes, placeholders)
- [ ] Step 9 — Verify (9a automated) + confirm (9b gate) & stamp

## 7. LinCluster — Table 3.36, p.93

- [ ] Step 1 — Sync members & description from spec
- [ ] Step 2 — Write the model class unit test (Red)
- [ ] Step 3 — Implement the model class (Green)
- [ ] Step 4 — Sync docstrings (wipe & rewrite from markdown)
- [ ] Step 5 — Write the reader/writer round-trip test (Red)
- [ ] Step 6 — Update the parser (reader) & writer (Green)
- [ ] Step 7 — Update checklist comment (`# Spec:` + rows)
- [ ] Step 8 — Deviations check (referenced classes, placeholders)
- [ ] Step 9 — Verify (9a automated) + confirm (9b gate) & stamp

## 8. LinMaster — Table 3.38, p.94

- [ ] Step 1 — Sync members & description from spec
- [ ] Step 2 — Write the model class unit test (Red)
- [ ] Step 3 — Implement the model class (Green)
- [ ] Step 4 — Sync docstrings (wipe & rewrite from markdown)
- [ ] Step 5 — Write the reader/writer round-trip test (Red)
- [ ] Step 6 — Update the parser (reader) & writer (Green)
- [ ] Step 7 — Update checklist comment (`# Spec:` + rows)
- [ ] Step 8 — Deviations check (referenced classes, placeholders)
- [ ] Step 9 — Verify (9a automated) + confirm (9b gate) & stamp
