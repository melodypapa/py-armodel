# Sync todo: Group 18 — NetworkManagement, Dlt & system mappings

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

- [ ] `NmEcu` (input · R23-11 markdown · Table 6.300)
  - module: M2/AUTOSARTemplates/SystemTemplate/NetworkManagement.py
  - note: deviation-tracked in method_deviation_by_class.md + method_deviation_by_class_v2.md — reviewed at Step 1: v1 rows (busSpecificNmEcu/nmMultipleChannelsEnabled/nmPassiveModeEnabled missing) were stale pre-R23-11 findings, replaced; v2 gained the accepted nmCoordinator placeholder row
  - [x] Step 1 — Sync members & description from spec — Table 6.300, p.674; Note "ECU on which NM is running."; Base ARObject,Identifiable,MultilanguageReferrable,Referrable; 10 attrs in displayed order (busDependentNmEcu `*` aggr, ecuInstance 0..1 ref, nmBusSynchronizationEnabled/nmComControlEnabled 0..1 Boolean, nmCoordinator 0..1 aggr NmCoordinator, nmCycletimeMainFunction 0..1 TimeValue, nmPduRxIndicationEnabled/nmRemoteSleepIndEnabled/nmStateChangeIndEnabled/nmUserDataEnabled 0..1 Boolean); reader/writer XML order per XSD group NM-ECU (AUTOSAR_00052.xsd l.84602)
  - [x] Step 2 — Write model class unit test (Red) — tests/test_armodel/models/M2/AUTOSARTemplates/SystemTemplate/NetworkManagement/test_NmEcu.py: defaults, get/set + None no-op for all 10 attrs, addBusDependentNmEcu append/no-op
  - [x] Step 3 — Implement model class (Green) — removed fabricated nmNodeDetectionEnabled/nmNodeIdEnabled/nmRepeatMsgIndEnabled (NmCluster rows, absent from Table 6.300; no fixture carries the tags); PEP 526 typed fields, None-guarded setters returning self, mutator-first list accessors
  - [x] Step 4 — Sync docstrings (wipe + rewrite) — class docstring = Note verbatim; per-attr inline __init__ comments + getter/setter docstrings verbatim from markdown; __init__ has no docstring; blank line between every attribute block
  - [x] Step 5 — Write reader/writer round-trip test (Red) — tests/test_armodel/parser/test_nm_ecu.py (field values incl. NM-CYCLETIME-MAIN-FUNCTION, BUS-DEPENDENT-NM-ECUS dispatch, removed-attr rejection) + tests/test_armodel/writer/test_nm_ecu.py (XSD element order, dropped-tag asserts, full round-trip values)
  - [x] Step 6 — Update parser & writer (Green) — readNmEcu/writeNmEcu: removed the 3 stale elements, added NM-CYCLETIME-MAIN-FUNCTION (getChildElementOptionalTimeValue/setChildElementOptionalTimeValue); matched name pairs, no chained mutators
  - [x] Step 7 — Update checklist comment — 6-column, `# Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.300, p.674`, all rows R23-11; no marker written (unstamped batch)
  - [x] Step 8 — Deviations — nmCoordinator typed `Optional[ARObject]` placeholder with reader/writer deferred (aggregated child NmCoordinator, Table 6.302, not yet implemented — Rule 0001.10/0001.7), recorded in method_deviation_by_class.md + _v2.md; XSD-only BUS-SPECIFIC-NM-ECU group not modeled (Rule 0015, PDF authoritative); stale v1 NmEcu rows removed
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-29: 13554 passed / 0 failed, lint + black clean; 9b deferred to batch confirmation (user instruction)

- [ ] `CanNmCluster` — NmCluster — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/SystemTemplate/NetworkManagement.py
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

- [ ] `UdpNmCluster` — NmCluster — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/SystemTemplate/NetworkManagement.py
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

- [ ] `CanNmNode` — NmNode — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/SystemTemplate/NetworkManagement.py
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

- [ ] `UdpNmNode` — NmNode — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/SystemTemplate/NetworkManagement.py
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

- [ ] `CanNmClusterCoupling` — NmClusterCoupling — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/SystemTemplate/NetworkManagement.py
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `UdpNmClusterCoupling` — NmClusterCoupling — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/SystemTemplate/NetworkManagement.py
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

- [ ] `FlexrayNmClusterCoupling` — NmClusterCoupling — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/SystemTemplate/NetworkManagement.py
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

- [ ] `SecOcCryptoServiceMapping` — CryptoServiceMapping — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/SystemTemplate/SecureCommunication.py
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `EndToEndTransformationISignalProps` — TransformationISignalProps — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/SystemTemplate/Transformer/__init__.py
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

- [ ] `TpAddress` — Identifiable — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/SystemTemplate/TransportProtocols.py
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

- [ ] `LinTpConnection` — TpConnection — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/SystemTemplate/TransportProtocols.py
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

- [ ] `EndToEndProtectionISignalIPdu` — ARObject — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/SystemTemplate/EndToEndProtection.py
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `SwcToEcuMapping` — Identifiable — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/SystemTemplate/__init__.py
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

- [ ] `ApplicationPartitionToEcuPartitionMapping` — Identifiable — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/SystemTemplate/SWmapping.py
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `SwcToImplMapping` — Identifiable — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/SystemTemplate/SWmapping.py
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `AppOsTaskProxyToEcuTaskProxyMapping` — Identifiable — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/SystemTemplate/RteEventToOsTaskMapping.py
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
