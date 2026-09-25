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

- [ ] `ModeDeclarationGroupPrototypeMapping` — ARObject — R23-11 markdown · Table 4.27 (CP_TPS_SoftwareComponentTemplate)
  - module: M2/AUTOSARTemplates/CommonStructure/ModeDeclaration.py
  - [x] Step 1 — Sync members & description from spec (Table 4.27, p.130; concrete Class; Base most-derived = ARObject — row confirmed; 3 attrs, all 0..1 ref → Optional[RefType] + Ref suffix, names already spec-correct; XSD element order FIRST-MODE-GROUP-REF / MODE-DECLARATION-MAPPING-SET-REF / SECOND-MODE-GROUP-REF matches reader/writer; found: fabricated class docstring, bare-RefType 0..1 annotations, `__init__` docstring present, old 4-column checklist without `# Spec:`/release column)
  - [x] Step 2 — Write model class unit test (Red) (7 tests: initialization/base shape/3 get-set round-trip+chaining+None no-op/accessor get_type_hints pins/spec Note verbatim incl. `__init__.__doc__ is None` + inline comment source asserts; Red confirmed — test_accessor_annotations KeyError + test_spec_note failed, 5 behavior tests already green)
  - [x] Step 3 — Implement model class (Green) (no behavior change: base ARObject, 3 ref fields + get/set pairs already present; fixes = PEP 526 `Optional[RefType]` annotations on fields/getter returns/setter params (0..1 per Mult.), setters return `"ModeDeclarationGroupPrototypeMapping"`; Green = 67/67 after Step 4's verbatim docstrings + test attr-name derivation fix)
  - [x] Step 4 — Sync docstrings (wipe + rewrite) (whole class block replaced — fabricated class docstring → Table 4.27 Note verbatim single-line; `__init__` docstring removed; 3 fields re-commented with per-attr Notes verbatim (incl. spec's "context ot" typo and markdown space artifacts); getter/setter docstrings = Note verbatim, setters append None-no-op sentence with field name; old 4-column checklist removed — 6-column written at Step 7)
  - [x] Step 5 — Write reader/writer round-trip test (Red) (6 new tests in the paired feature files: parser `TestReadModeInterfaceMappingModeMapping` — 3 refs value+DEST / absent refs → None / no MODE-MAPPING → None; writer `TestWriteModeInterfaceMappingModeMapping` — 3 refs value+DEST in XSD order / absent refs emit nothing + no MODE-MAPPING when mapping absent / write→read round-trip value+DEST; green after fixing test harness only — writer nests the tag under the passed parent and parser needs the xmlns root, no production bug)
  - [x] Step 6 — Update parser & writer (Green) (N/A: no parser/writer change — coverage verified PRESENT and spec-correct: reader `readModeInterfaceMappingModeMapping` calls the three setters via `getChildElementOptionalRefType`, writer `writeModeInterfaceMappingModeMapping` calls the three getters via `setChildElementOptionalRefType`, matched name pairs per Rule 0013.2, element order = XSD sequenceOffset, no chained mutators)
  - [x] Step 7 — Update checklist comment (6-column format with release column, source-order rows; `# Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 4.27, p.130`; reader [x] on setter rows / writer [x] on getter rows verified against `readModeInterfaceMappingModeMapping`/`writeModeInterfaceMappingModeMapping` call sites; NO `# Spec verified:` — deferred to batch confirmation)
  - [x] Step 8 — Deviations (fixed+recorded in step notes: fabricated class docstring → Table 4.27 Note verbatim; `__init__` docstring removed; bare-RefType 0..1 fields + untyped accessors → PEP 526 `Optional[RefType]` typed accessors; paraphrased member docstrings + placeholder inline comments → spec Notes verbatim incl. "context ot" typo; old 4-column checklist → 6-column with `# Spec:` line + release column; no pre-existing `# Spec verified:`/`# XSD verified:` marker to invalidate; deviation trackers have NO entries for this class — nothing stale; no open deviations, no placeholders — RefType is the spec type for all three `ref` rows)
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `ModeRequestTypeMap` — ARObject — R23-11 markdown · Table 4.18 (CP_TPS_SoftwareComponentTemplate)
  - module: M2/AUTOSARTemplates/CommonStructure/ModeDeclaration.py
  - [x] Step 1 — Sync members & description from spec (Table 4.18, p.115; concrete Class; Base most-derived = ARObject — row confirmed; 2 attrs, both 0..1 ref → Optional[RefType] + Ref suffix, names already spec-correct; also rendered by CP_TPS_BSWModuleDescriptionTemplate Table 4.15 p.45 (same content — page-split); XSD element order IMPLEMENTATION-DATA-TYPE-REF / MODE-GROUP-REF matches reader/writer; found: fabricated class docstring, bare-RefType 0..1 annotations, setters lack the None no-op guard despite docstring claiming it, `__init__` docstring present, old 4-column checklist without `# Spec:`/release column, reader assigns fields directly instead of via setters)
  - [x] Step 2 — Write model class unit test (Red) (6 tests: initialization/base shape/2 get-set round-trip+chaining+None no-op/accessor get_type_hints pins/spec Note verbatim incl. `__init__.__doc__ is None` + inline comment source asserts; Red confirmed — test_accessor_annotations KeyError + test_spec_note + both None no-op tests failed, initialization and base shape already green)
  - [x] Step 3 — Implement model class (Green) (behavior fixes: PEP 526 `Optional[RefType]` annotations on fields/getter returns/setter params (0..1 per Mult.), setters gained the None no-op guard (`if value is not None`) the old docstring claimed but code lacked, setters return `"ModeRequestTypeMap"` (module has no `from __future__ import annotations` — quoted self-reference matches the sibling `ModeDeclarationGroupPrototypeMapping` pattern in this file); Green = 5/6, spec-note test stays Red until Step 4's verbatim docstrings — same shape as the sibling row)
  - [x] Step 4 — Sync docstrings (wipe + rewrite) (whole class block replaced — fabricated class docstring → Table 4.18 Note verbatim + class/attr-level constr rows 1166/1871/1872/1167 (ClientIdRange precedent: attr-existence constr live in the class docstring); `__init__` docstring removed; 2 fields re-commented with per-attr Notes verbatim (markdown mid-word splits de-split per the XSD doc wording: "AbstractImplementationData Type." → "AbstractImplementationDataType."); getter/setter docstrings = Note verbatim, setters append None-no-op sentence with field name; old 4-column checklist removed — 6-column written at Step 7; test_spec_note updated to containment + constr asserts since the class docstring now carries Note + constr rows; Green = 67/67)
  - [x] Step 5 — Write reader/writer round-trip test (Red) (8 new tests in new paired feature files: parser `TestReadModeRequestTypeMaps` (test_data_type_mapping_set_mode_request_type_map.py) — refs value+DEST / multiple maps in document order / absent ref → None / no MODE-REQUEST-TYPE-MAPS → []; writer `TestWriteModeRequestTypeMaps` (test_data_type_mapping_set_mode_request_type_map.py) — refs value+DEST in XSD order / absent refs emit map with no children / no wrapper when empty / write→read round-trip value+DEST; NOT Red-able — all 8 green on first run because coverage already existed and behaved spec-correctly (same outcome as the sibling row: harness-only, no production bug); existing handler tests test_arxml_parser_handlers.py + test_writer_impl_types_ports.py still green)
  - [x] Step 6 — Update parser & writer (Green) (writer N/A: coverage verified PRESENT and spec-correct — `writeModeRequestTypeMaps` reads via the two getters via `setChildElementOptionalRefType`, XSD element order, wrapper only when non-empty, matched name pairs per Rule 0013.2; reader FIXED: `readModeRequestTypeMaps` assigned the two fields directly (`map.implementationDataTypeRef = ...`) — migrated to the mutators `setImplementationDataTypeRef`/`setModeGroupRef` so the checklist reader [x] on the setter rows is honest (Rule 0002); no chained mutators; 5508 parser/writer tests green after the fix)
  - [x] Step 7 — Update checklist comment (6-column format with release column, source-order rows; `# Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 4.18, p.115`; reader [x] on setter rows verified against `readModeRequestTypeMaps` call site (arxml_parser.py:7599-7600 now calling the setters), writer [x] on getter rows verified against `writeModeRequestTypeMaps` (arxml_writer.py:7924-7925); NO `# Spec verified:` — deferred to batch confirmation)
  - [x] Step 8 — Deviations (fixed+recorded in step notes: fabricated class docstring → Table 4.18 Note verbatim + constr rows; `__init__` docstring removed; bare-RefType 0..1 fields + untyped accessors → PEP 526 `Optional[RefType]`; setters lacked the None no-op guard the old docstring claimed → guard added; paraphrased member docstrings + placeholder inline comments → spec Notes verbatim; old 4-column checklist → 6-column with `# Spec:` line + release column; reader direct field assignment → mutators; no pre-existing `# Spec verified:`/`# XSD verified:` marker to invalidate; deviation trackers method_deviation_by_class.md + v2 have NO entries for this class — nothing stale; no open deviations, no placeholders — RefType is the spec type for both `ref` rows)
  - [ ] Step 9 — Verify (9a) + confirm (9b) [9a: 11917 unit tests + 3 integration + flake8 + ruff + black green; **stamp deferred to batch confirmation (user instruction 2026-09-24)**]

- [ ] `ClientServerApplicationErrorMapping` — ARObject — R23-11 markdown · Table 4.25 (CP_TPS_SoftwareComponentTemplate)
  - module: M2/AUTOSARTemplates/SWComponentTemplate/PortInterface/__init__.py
  - [x] Step 1 — Sync members & description from spec (Table 4.25, p.129; concrete Class; Base most-derived = ARObject — row confirmed; 2 attrs, both 0..1 ref → Optional[RefType] + Ref suffix, names already spec-correct; class-level constr_1238 belongs in the class docstring — its title says "ClientServerOperationMapping" but the body constrains this class's firstApplicationError/secondApplicationError roles (spec typo); XSD element order FIRST-APPLICATION-ERROR-REF / SECOND-APPLICATION-ERROR-REF matches reader/writer; reader/writer coverage MISSING — no ERROR-MAPPINGS branch in readClientServerInterfaceMapping/writeClientServerInterfaceMapping (arxml_parser.py:13722 / arxml_writer.py:11943) → Step 6 adds it; found: bare-RefType 0..1 annotations, untyped accessors, setters lack the None no-op guard, old 4-column checklist without `# Spec:`/release column, no class docstring)
  - [x] Step 2 — Write model class unit test (Red) (6 tests in the mirrored test_PortInterface.py: initialization/base shape/2 get-set round-trip+chaining+None no-op/accessor get_type_hints pins/spec Note + constr_1238 verbatim incl. `__init__.__doc__ is None` + inline comment source asserts; Red confirmed — both None no-op tests + test_accessor_annotations (KeyError) + test_spec_note (AttributeError on None doc) failed, initialization and base shape already green)
  - [x] Step 3 — Implement model class (Green) (behavior fixes: PEP 526 `Optional[RefType]` annotations on fields/getter returns/setter params (0..1 per Mult.), setters gained the None no-op guard (`if value is not None`), setters return `"ClientServerApplicationErrorMapping"` (module has no `from __future__ import annotations` — quoted self-reference matches the sibling pattern in CommonStructure/ModeDeclaration.py); stale 4-column checklist removed — 6-column written at Step 7; Green = 5/6, spec-note test stays Red until Step 4's verbatim docstrings — same shape as the sibling row)
  - [x] Step 4 — Sync docstrings (wipe + rewrite) (class had no docstrings/member comments to wipe beyond the stale checklist already removed at Step 3 — wipe trivially complete; class docstring = Table 4.25 Note verbatim + class-level constr_1238 rows (title keeps the spec's "ClientServerOperationMapping" typo, body de-splits markdown mid-word spaces: "ApplicationError s" → "ApplicationErrors"); 2 fields commented with per-attr Notes verbatim; getter/setter docstrings = Note verbatim, setters append None-no-op sentence with field name; Green = 40/40 in test_PortInterface.py)
  - [x] Step 5 — Write reader/writer round-trip test (Red) (7 new tests in the paired feature files: parser `TestReadClientServerInterfaceMappingErrorMappings` (test_ar_package_port_interface_mapping_set.py) — refs value+DEST / multiple maps in document order / absent ref → None / no ERROR-MAPPINGS → []; writer `TestWriteClientServerInterfaceMappingErrorMappings` (same file pair) — refs value+DEST in XSD order / absent refs emit no elements + no ERROR-MAPPINGS when list empty / write→read round-trip value+DEST; Red confirmed — 6 failed (all value-carrying tests), 13 passed (pre-existing + the absent-element no-op cases))
  - [x] Step 6 — Update parser & writer (Green) (coverage ADDED: reader `readClientServerApplicationErrorMapping` (two setters via `getChildElementOptionalRefType`) + `readClientServerInterfaceMappingErrorMappings` (iterates `ERROR-MAPPINGS/*`, dispatches on tag, `mapping.addErrorMapping`) called from `readClientServerInterfaceMapping` BEFORE operation mappings per XSD sequenceOffset; writer `writeClientServerApplicationErrorMapping` (two getters via `setChildElementOptionalRefType`) + `writeClientServerInterfaceMappingErrorMappings` (wrapper only when non-empty, isinstance dispatch) called from `writeClientServerInterfaceMapping` before operation mappings; matched name pairs per Rule 0013.2, no chained mutators; imports extended in both files; 5515 parser/writer tests green)
  - [x] Step 7 — Update checklist comment (6-column format with release column, 5 rows in accessor source order: __init__ [—/—], getters writer [x], setters reader [x] verified against the new read/writeClientServerApplicationErrorMapping call sites; NO # Spec verified: — deferred to batch confirmation)
  - [x] Step 8 — Deviations (fixed+recorded: bare-T 0..1 members → PEP 526 Optional[RefType]; untyped accessors → typed; setters lacked the None no-op their docstring claimed → guard + verbatim Note + no-op sentence; reader/writer coverage was ENTIRELY MISSING → new read/writeClientServerApplicationErrorMapping helpers + ERROR-MAPPINGS wrapper dispatch in readClientServerInterfaceMapping (arxml_parser.py) / writeClientServerInterfaceMapping (arxml_writer.py); no open deviations — dispatch of the wrapper belongs to the ClientServerInterfaceMapping row, whose helper call sites are already wired and test-pinned here)
  - [ ] Step 9 — Verify (9a) + confirm (9b)  [9a: 11930 unit tests + 3 integration + flake8 + ruff + black green; **stamp deferred to batch confirmation (user instruction 2026-09-24)**]

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
