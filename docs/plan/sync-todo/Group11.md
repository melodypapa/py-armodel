# Sync todo: Group 11 — SWC ports & instance refs

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

- [ ] `ModeActivationKind` — AREnum — R23-11 markdown · Table 5.34 (CP_TPS_BSWModuleDescriptionTemplate)
  - module: M2/AUTOSARTemplates/CommonStructure/ModeDeclaration.py
  - note: deviation-tracked in method_deviation_by_class.md + method_deviation_by_class_v2.md — reviewed at Step 1: only intake listings (no deviation rows; `activation` row = ok)
  - [x] Step 1 — Sync members & description from spec (Table 5.34, p.96; SWC TPS Table 7.18 p.545 renders the same enum — both agree; literals onEntry/onExit/onTransition, indices 0-2 = XSD doc order; found: `__init__` docstring present, class Note line-wrapped, old 4-column checklist without release column)
  - [x] Step 2 — Write model class unit test (Red) (6 tests: literals/values+order/setValue round-trip+chaining/None no-op/validateEnumValue/spec Note; Red confirmed 1st run — test_spec_note failed on the line-wrapped class Note, 5 behavior tests already green)
  - [x] Step 3 — Implement model class (Green) (no production behavior change: values `onEntry`/`onExit`/`onTransition`, index order 0-2 and no-arg `__init__` already spec-correct; Green = 6/6 after Step 4's verbatim docstring)
  - [x] Step 4 — Sync docstrings (wipe + rewrite) (line-wrapped class Note rewritten single-line verbatim from Table 5.34; `__init__` docstring removed; wrapped ON_TRANSITION literal comment joined to the single-line `Tags: atp.EnumerationLiteralIndex=N` form; mirror file 71/71)
  - [x] Step 5 — Write reader/writer round-trip test (Red) (N/A: standalone enum — the value form is serialized by `BswModeSwitchEvent.activation` + `SwcModeSwitchEvent.activation`; consumer coverage verified PRESENT for both: parser `readBswModeSwitchEvent` (arxml_parser.py:1990) + `readSwcModeSwitchEvent` types via `ModeActivationKind().setValue` (arxml_parser.py:5615); writer test asserts ON_ENTRY/ON_EXIT round-trip in test_writer_swc_behavior.py)
  - [x] Step 6 — Update parser & writer (Green) (N/A: standalone enum — no parser/writer code added for the enum itself; writer verified: `writeBswModeSwitchEvent` (arxml_writer.py:6978) + `writeSwcModeSwitchEvent` (arxml_writer.py:3573) emit `ACTIVATION` via `setChildElementOptionalLiteral`/`getActivation`)
  - [x] Step 7 — Update checklist comment (6-column format, single `__init__` row with release R23-11, `# Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 5.34, p.96`; NO `# Spec verified:` — deferred to batch confirmation)
  - [x] Step 8 — Deviations (fixed+recorded in step notes: line-wrapped class Note → single-line verbatim, `__init__` docstring removed, wrapped ON_TRANSITION comment → single-line `Tags:` form, old 4-column checklist → 6-column with release column; no pre-existing `# Spec verified:`/`# XSD verified:` marker to invalidate; no open deviations — tracker mentions are intake listings only, `activation` row = ok)
  - [ ] Step 9 — Verify (9a) + confirm (9b) [9a: 11907 unit tests + flake8 + ruff + black green; **stamp deferred to batch confirmation (user instruction 2026-09-24)**]

- [ ] `ModeDeclarationGroupPrototypeMapping` — ARObject — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/CommonStructure/ModeDeclaration.py
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `ModeRequestTypeMap` — ARObject — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/CommonStructure/ModeDeclaration.py
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `ClientServerApplicationErrorMapping` — ARObject — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/SWComponentTemplate/PortInterface/__init__.py
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `ClientServerOperationMapping` — ARObject — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/SWComponentTemplate/PortInterface/__init__.py
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `ClientServerInterfaceMapping` — PortInterfaceMapping — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/SWComponentTemplate/PortInterface/__init__.py
  - after `ClientServerApplicationErrorMapping`
  - after `ClientServerOperationMapping`
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `ModeInterfaceMapping` — PortInterfaceMapping — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/SWComponentTemplate/PortInterface/__init__.py
  - after `ModeDeclarationGroupPrototypeMapping`
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `VariableAndParameterInterfaceMapping` — PortInterfaceMapping — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/SWComponentTemplate/PortInterface/__init__.py
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `Field` — AutosarDataPrototype — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/AdaptivePlatform/ApplicationDesign/PortInterface/__init__.py
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

- [ ] `AbstractProvidedPortPrototype` — PortPrototype — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/SWComponentTemplate/Components/__init__.py
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `AbstractRequiredPortPrototype` — PortPrototype — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/SWComponentTemplate/Components/__init__.py
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `ServiceProxySwComponentType` — AtomicSwComponentType — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/SWComponentTemplate/Components/__init__.py
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `ModeGroupInAtomicSwcInstanceRef` — AtpInstanceRef — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/SWComponentTemplate/Components/InstanceRefs.py
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `OperationInAtomicSwcInstanceRef` — AtpInstanceRef — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/SWComponentTemplate/Components/InstanceRefs.py
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `RModeInAtomicSwcInstanceRef` — AtpInstanceRef — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/SWComponentTemplate/Components/InstanceRefs.py
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

- [ ] `TriggerInAtomicSwcInstanceRef` — AtpInstanceRef — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/SWComponentTemplate/Components/InstanceRefs.py
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `PModeGroupInAtomicSwcInstanceRef` — ModeGroupInAtomicSwcInstanceRef — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/SWComponentTemplate/Components/InstanceRefs.py
  - note: deviation-tracked in method_deviation_by_class.md — review entries at Step 1
  - after `ModeGroupInAtomicSwcInstanceRef`
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `RModeGroupInAtomicSWCInstanceRef` — ModeGroupInAtomicSwcInstanceRef — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/SWComponentTemplate/Components/InstanceRefs.py
  - after `ModeGroupInAtomicSwcInstanceRef`
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `POperationInAtomicSwcInstanceRef` — OperationInAtomicSwcInstanceRef — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/SWComponentTemplate/Components/InstanceRefs.py
  - after `OperationInAtomicSwcInstanceRef`
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `ROperationInAtomicSwcInstanceRef` — OperationInAtomicSwcInstanceRef — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/SWComponentTemplate/Components/InstanceRefs.py
  - after `OperationInAtomicSwcInstanceRef`
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `RVariableInAtomicSwcInstanceRef` — VariableInAtomicSwcInstanceRef — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/SWComponentTemplate/Components/InstanceRefs.py
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `PTriggerInAtomicSwcTypeInstanceRef` — TriggerInAtomicSwcInstanceRef — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/SWComponentTemplate/Components/InstanceRefs.py
  - note: deviation-tracked in method_deviation_by_class.md — review entries at Step 1
  - after `TriggerInAtomicSwcInstanceRef`
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `PPortInCompositionInstanceRef` — PortInCompositionTypeInstanceRef — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/SWComponentTemplate/Composition/InstanceRefs.py
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `RPortInCompositionInstanceRef` — PortInCompositionTypeInstanceRef — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/SWComponentTemplate/Composition/InstanceRefs.py
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
