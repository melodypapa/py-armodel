# Sync todo: Group 10 — SWC communication & datatypes

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

- [ ] `DependencyUsageEnum` — AREnum — R23-11 markdown · Table 7.4 (CP_TPS_BSWModuleDescriptionTemplate)
  - module: M2/AUTOSARTemplates/CommonStructure/Implementation.py
  - note: deviation-tracked in method_deviation_by_class_v2.md — reviewed at Step 1: only an Appendix intake listing (no deviation rows); Table 7.4 exists, so the appendix entry is a stale intake artifact
  - [x] Step 1 — Sync members & description from spec (Table 7.4, p.132; literals build/codegeneration/compile/execute/link, indices 0-4 = XSD doc order; found: CODEGENERATION comment has spurious trailing period vs spec, old 4-column checklist, no `Tags:` prefix)
  - [x] Step 2 — Write model class unit test (Red) (6 tests: literals/values+order/setValue round-trip+chaining/None no-op/validateEnumValue/spec Note; Red confirmed 1st run — fresh-unset `getValue()` is `""` per the ARLiteral base contract, not `None`)
  - [x] Step 3 — Implement model class (Green) (no production change: values, index order and no-arg `__init__` already spec-correct; Green = 6/6 after Step 2 expectation fix)
  - [x] Step 4 — Sync docstrings (wipe + rewrite) (class Note already verbatim, kept; 5 literal comments rewritten verbatim — removed spurious period on `codegeneration`, added `Tags: atp.EnumerationLiteralIndex=N` form)
  - [x] Step 5 — Write reader/writer round-trip test (Red) (N/A: standalone enum — the value form is serialized by `DependencyOnArtifact.usage`; consumer coverage verified: parser `readDependencyOnArtifact` USAGES/USAGE → `DependencyUsageEnum().setValue` + `addUsage` (arxml_parser.py:4477), reader test asserts values BUILD/LINK/CODEGENERATION in test_arxml_parser_implementation.py)
  - [x] Step 6 — Update parser & writer (Green) (N/A: standalone enum — writer verified: `writeDependencyOnArtifact` emits `USAGES` wrapper only when non-empty + one `USAGE` per entry (arxml_writer.py:6427); consumer class checklist already reader/writer `[x]`)
  - [x] Step 7 — Update checklist comment (6-column format, single `__init__` row, release R23-11; NO `# Spec verified:` — deferred to batch confirmation)
  - [x] Step 8 — Deviations (fixed+recorded in step notes: CODEGENERATION comment trailing period removed (spec has none), `Tags:` prefix format applied, 4-col checklist → 6-col, set-based order test → exact order; no open deviations — tracker v2 mention is a stale intake appendix listing only)
  - [ ] Step 9 — Verify (9a) + confirm (9b) [9a: 10933 unit tests + flake8 + ruff + black green; **stamp deferred to batch confirmation (user instruction 2026-09-24)**]

- [ ] `ArrayImplPolicyEnum` — AREnum — R23-11 markdown · Table 5.18 (CP_TPS_SoftwareComponentTemplate)
  - module: M2/AUTOSARTemplates/CommonStructure/ImplementationDataTypes.py
  - note: deviation-tracked in method_deviation_by_class_v2.md — reviewed at Step 1: only an Appendix intake listing (no deviation rows); Table 5.18 exists, so the appendix entry is a stale intake artifact
  - [x] Step 1 — Sync members & description from spec (Table 5.18, p.276; literals payloadAsArray/payloadAsPointerToArray, indices 0-1 = XSD doc order; found: markdown renders `payloadAsPointerTo Array` via column wrap — XSD `mmt.qualifiedName` confirms `payloadAsPointerToArray`)
  - [x] Step 2 — Write model class unit test (Red) (6 tests: literals/values+order/setValue round-trip+chaining/None no-op/validateEnumValue/spec Note; Red confirmed 1st run — 6/6 failed on the fabricated DYNAMIC/STATIC stub members and paraphrased docstring)
  - [x] Step 3 — Implement model class (Green) (production change: fabricated DYNAMIC/STATIC stub literals replaced with spec PAYLOAD_AS_ARRAY/"payloadAsArray" + PAYLOAD_AS_POINTER_TO_ARRAY/"payloadAsPointerToArray" in index order, no-arg `__init__`; Green = 5/6 behavior tests pass — test_spec_note intentionally Red pending Step 4)
  - [x] Step 4 — Sync docstrings (wipe + rewrite) (paraphrased docstring "Enumeration for array implementation policy." wiped; class Note rewritten verbatim from Table 5.18; both literal comments rewritten verbatim with `Tags: atp.EnumerationLiteralIndex=N`; no `__init__` docstring; mirror file 53/53)
  - [x] Step 5 — Write reader/writer round-trip test (Red) (N/A: standalone enum — the value form is serialized by `ImplementationDataTypeElement.arrayImplPolicy`; consumer coverage verified MISSING: no `ARRAY-IMPL-POLICY` in parser/writer and no fixture/test carries it — recorded at Step 8 as consuming-class deviation, fix belongs to the queued ImplementationDataTypeElement row)
  - [x] Step 6 — Update parser & writer (Green) (N/A: standalone enum — no parser/writer code added for the enum itself; consumer gap reported, not fixed here — out of this row's per-class commit scope)
  - [x] Step 7 — Update checklist comment (6-column format, single `__init__` row, `# Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.18, p.276`, release R23-11; NO `# Spec verified:` — deferred to batch confirmation)
  - [x] Step 8 — Deviations (fixed+recorded in step notes: whole-enum stub — fabricated DYNAMIC/STATIC literals with no spec basis, paraphrased docstring, old 4-column checklist — all replaced from Table 5.18; REPORTED UNFIXED: consumer `ImplementationDataTypeElement.arrayImplPolicy` has no reader/writer coverage (`ARRAY-IMPL-POLICY` absent from read/writeImplementationDataTypeElement, arxml_parser.py:6532 / arxml_writer.py:7549; no fixture/test carries it) — fix belongs to the queued ImplementationDataTypeElement row in this file; tracker v2 mention is a stale intake appendix listing only)
  - [ ] Step 9 — Verify (9a) + confirm (9b) [9a: 10937 unit tests + flake8 + ruff + black green; **stamp deferred to batch confirmation (user instruction 2026-09-24)**]

- [ ] `ApiPrincipleEnum` — AREnum — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/CommonStructure/InternalBehavior.py
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

- [ ] `ReentrancyLevelEnum` — AREnum — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/CommonStructure/InternalBehavior.py
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

- [ ] `ImplementationProps` — Referrable — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/CommonStructure/Implementation.py
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

- [ ] `SwcImplementation` — Implementation — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/SWComponentTemplate/SwcImplementation.py
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `ImplementationDataTypeElement` — AbstractImplementationDataTypeElement — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/CommonStructure/ImplementationDataTypes.py
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `ReceptionComSpecProps` — ARObject — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/SWComponentTemplate/Communication.py
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `CompositeNetworkRepresentation` — ARObject — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/SWComponentTemplate/Communication.py
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `ModeSwitchedAckRequest` — ARObject — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/SWComponentTemplate/Communication.py
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `ModeSwitchReceiverComSpec` — RPortComSpec — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/SWComponentTemplate/Communication.py
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `ModeSwitchSenderComSpec` — PPortComSpec — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/SWComponentTemplate/Communication.py
  - after `ModeSwitchedAckRequest`
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `NvProvideComSpec` — PPortComSpec — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/SWComponentTemplate/Communication.py
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `NvRequireComSpec` — RPortComSpec — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/SWComponentTemplate/Communication.py
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `ParameterRequireComSpec` — RPortComSpec — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/SWComponentTemplate/Communication.py
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `QueuedReceiverComSpec` — ReceiverComSpec — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/SWComponentTemplate/Communication.py
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `DataTypeMap` — ARObject — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/SWComponentTemplate/Datatype/Datatypes.py
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `EndToEndDescription` — ARObject — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/SWComponentTemplate/EndToEndProtection.py
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `ModeSwitchEventTriggeredActivity` — ARObject — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/SWComponentTemplate/NvBlockComponent.py
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `AutosarVariableRef` — ARObject — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/DataElements/__init__.py
  - note: moved from Group12 — member type of `NvBlockDataMapping` (dependency priority)
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

- [ ] `RoleBasedPortAssignment` — ARObject — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/ServiceMapping.py
  - note: moved from Group12 — member type of `NvBlockDescriptor` (dependency priority)
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `AutosarParameterRef` — ARObject — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/DataElements/__init__.py
  - note: moved from Group12 — member type of `RoleBasedDataAssignment`, `InstantiationDataDefProps` (dependency priority)
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

- [ ] `NvBlockNeedsReliabilityEnum` — AREnum — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py
  - note: moved from Group14 — member type of `NvBlockNeeds` (dependency priority)
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

- [ ] `NvBlockNeedsWritingPriorityEnum` — AREnum — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py
  - note: moved from Group14 — member type of `NvBlockNeeds` (dependency priority)
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

- [ ] `RamBlockStatusControlEnum` — AREnum — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py
  - note: moved from Group14 — member type of `NvBlockNeeds` (dependency priority)
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

- [ ] `NvBlockDataMapping` — ARObject — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/SWComponentTemplate/NvBlockComponent.py
  - after `AutosarVariableRef`
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `BulkNvDataDescriptor` — AtpStructureElement — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/SWComponentTemplate/NvBlockComponent.py
  - after `NvBlockDataMapping`
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `RoleBasedDataAssignment` — ARObject — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py
  - note: moved from Group14 — member type of `NvBlockDescriptor` (dependency priority)
  - note: deviation-tracked in method_deviation_by_class.md — review entries at Step 1
  - after `AutosarVariableRef`
  - after `AutosarParameterRef`
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `InstantiationDataDefProps` — ARObject — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/InstantiationDataDefProps.py
  - note: moved from Group12 — member type of `NvBlockDescriptor` (dependency priority)
  - note: deviation-tracked in method_deviation_by_class.md — review entries at Step 1
  - after `AutosarVariableRef`
  - after `AutosarParameterRef`
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `NvBlockNeeds` — ServiceNeeds — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py
  - note: moved from Group14 — member type of `NvBlockDescriptor` (dependency priority)
  - after `NvBlockNeedsReliabilityEnum`
  - after `NvBlockNeedsWritingPriorityEnum`
  - after `RamBlockStatusControlEnum`
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `NvBlockDescriptor` — AtpStructureElement — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/SWComponentTemplate/NvBlockComponent.py
  - after `ModeSwitchEventTriggeredActivity`
  - after `RoleBasedPortAssignment`
  - after `NvBlockDataMapping`
  - after `RoleBasedDataAssignment`
  - after `InstantiationDataDefProps`
  - after `NvBlockNeeds`
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
