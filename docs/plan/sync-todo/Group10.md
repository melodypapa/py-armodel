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

- [ ] `ApiPrincipleEnum` — AREnum — R23-11 markdown · Table 5.18 (CP_TPS_BSWModuleDescriptionTemplate)
  - module: M2/AUTOSARTemplates/CommonStructure/InternalBehavior.py
  - note: deviation-tracked in method_deviation_by_class.md + method_deviation_by_class_v2.md — review entries at Step 1
  - [x] Step 1 — Sync members & description from spec (Table 5.18, p.83; literals common/perExecutable, indices 0-1 = XSD doc order; SWC TPS Table 7.29 p.557 renders the same enum; found: paraphrased class docstring, `__init__` docstring present, literal comments have spurious trailing period vs spec, old 4-column checklist)
  - [x] Step 2 — Write model class unit test (Red) (6 tests: literals/values+order/setValue round-trip+chaining/None no-op/validateEnumValue/spec Note; Red confirmed 1st run — test_spec_note failed on the paraphrased docstring "Represents the ability…" vs spec "This enumeration represents…", 5 behavior tests already green)
  - [x] Step 3 — Implement model class (Green) (no production change: values `common`/`perExecutable`, index order 0-1 and no-arg `__init__` already spec-correct; Green = 6/6 after Step 4's verbatim docstring)
  - [x] Step 4 — Sync docstrings (wipe + rewrite) (paraphrased class docstring, `__init__` docstring and both wrapped literal comments wiped; class Note rewritten verbatim from Table 5.18; both literal comments rewritten verbatim — removed spurious trailing period after "Module", single-line `Tags: atp.EnumerationLiteralIndex=N` form; no `__init__` docstring; mirror file 57/57)
  - [x] Step 5 — Write reader/writer round-trip test (Red) (N/A: standalone enum — the value form is serialized by the consuming `apiPrinciple` attributes; consumer coverage verified PRESENT for both: parser `readSwcInternalBehaviorExclusiveAreaPolicies` (arxml_parser.py:3752) + `getBswExclusiveAreaPolicy` (arxml_parser.py:4114); reader test asserts `perExecutable` in test_arxml_parser_handlers.py)
  - [x] Step 6 — Update parser & writer (Green) (N/A: standalone enum — no parser/writer code added for the enum itself; writer verified: `writeSwcInternalBehaviorExclusiveAreaPolicies` (arxml_writer.py:5715) + `setBswExclusiveAreaPolicy` (arxml_writer.py:7116) emit `API-PRINCIPLE` via `setChildElementOptionalLiteral`; writer test asserts `perExecutable` in test_writer_swc_behavior.py)
  - [x] Step 7 — Update checklist comment (6-column format, single `__init__` row, release R23-11; NO `# Spec verified:` — deferred to batch confirmation)
  - [x] Step 8 — Deviations (fixed+recorded in step notes: paraphrased class docstring → Note verbatim, `__init__` docstring removed, wrapped literal comments rewritten verbatim; no open deviations — tracker mentions are stale intake appendix listings)
  - [ ] Step 9 — Verify (9a) + confirm (9b)  [9a: 10940 unit tests + flake8 + ruff + black green; **stamp deferred to batch confirmation (user instruction 2026-09-24)**]

- [ ] `ReentrancyLevelEnum` — AREnum — R23-11 markdown · Table 5.5 (CP_TPS_BSWModuleDescriptionTemplate)
  - module: M2/AUTOSARTemplates/CommonStructure/InternalBehavior.py
  - note: deviation-tracked in method_deviation_by_class_v2.md — reviewed at Step 1: only an Appendix intake listing ("classes without a spec attribute table" — stale artifact, Table 5.5 exists; no deviation rows)
  - [x] Step 1 — Sync members & description from spec (Table 5.5, p.73; literals multicoreReentrant/nonReentrant/singleCoreReentrant, indices 0-2 = XSD doc order; found: markdown renders `singleCore Reentrant` via column wrap — XSD `mmt.qualifiedName` + constr_4077 prose confirm `singleCoreReentrant`; old 4-column checklist, `__init__` docstring present, literal comments line-wrapped)
  - [x] Step 2 — Write model class unit test (Red) (6 tests: literals/values+order/setValue round-trip+chaining/None no-op/validateEnumValue/spec Note; 6/6 green on first run — no behavioral Red: wire values, index order and no-arg `__init__` already spec-correct, remaining deltas are form-only and fixed in Steps 4/7)
  - [x] Step 3 — Implement model class (Green) (no production change: values `multicoreReentrant`/`nonReentrant`/`singleCoreReentrant`, index order 0-2 and no-arg `__init__` already spec-correct; Green = 6/6)
  - [x] Step 4 — Sync docstrings (wipe + rewrite) (`__init__` docstring wiped; all three multi-line literal comments rewritten verbatim in single-line `Tags: atp.EnumerationLiteralIndex=N` form; class Note verified verbatim from Table 5.5, kept; no `__init__` docstring)
  - [x] Step 5 — Write reader/writer round-trip test (Red) (N/A: standalone enum — the value form is serialized by `ExecutableEntity.reentrancyLevel`; consumer coverage verified PRESENT: parser `readExecutableEntity` → `setReentrancyLevel(getChildElementOptionalLiteral(element, "REENTRANCY-LEVEL"))` (arxml_parser.py:1935); reader test asserts `multicoreReentrant` in test_arxml_parser_bsw_handlers.py)
  - [x] Step 6 — Update parser & writer (Green) (N/A: standalone enum — no parser/writer code added for the enum itself; writer verified: `writeExecutableEntity` emits `REENTRANCY-LEVEL` via `setChildElementOptionalLiteral` (arxml_writer.py:6678); writer tests assert `multicoreReentrant` in test_writer_bsw_module.py)
  - [x] Step 7 — Update checklist comment (6-column format, single `__init__` row, `# Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 5.5, p.73`, release R23-11; NO `# Spec verified:` — deferred to batch confirmation)
  - [x] Step 8 — Deviations (fixed+recorded in step notes: `__init__` docstring removed, old 4-column checklist → 6-column with release column, multi-line literal comments → single-line verbatim + inline `Tags:` form; no open deviations — tracker v2 mention is a stale intake appendix listing only, consumer parser/writer coverage PRESENT so nothing deferred)
  - [ ] Step 9 — Verify (9a) + confirm (9b)  [9a: 10943 unit tests + flake8 + ruff + black green; **stamp deferred to batch confirmation (user instruction 2026-09-24)**]

- [ ] `ImplementationProps` — Referrable — R23-11 markdown · Table 5.20 (CP_TPS_SoftwareComponentTemplate)
  - module: M2/AUTOSARTemplates/CommonStructure/Implementation.py
  - note: deviation-tracked in method_deviation_by_class.md — reviewed at Step 1: no ImplementationProps rows (only historical SymbolicNameProps subclass write-ups — stale artifacts)
  - [x] Step 1 — Sync members & description from spec (Table 5.20, p.287 SWC TPS; identical twin Table 5.21, p.86 BSW TPS; abstract Class, Base = ARObject, Referrable → Referrable correct; one attr `symbol` CIdentifier 0..1 attr; XSD group IMPLEMENTATION-PROPS (00052 line 71960) matches 1:1 + doc texts verbatim; constr_1909 targets symbol; found: class docstring "Define" ≠ spec "Defines", `__init__` docstring present, getter/setter docstrings paraphrased, old 4-column checklist; reader/writer helpers already correct — readImplementationProps owns readReferrable + SYMBOL, writeImplementationProps owns writeReferrable + SYMBOL)
  - [x] Step 2 — Write model class unit test (Red) (6 tests: verbatim spec Notes / base shape + bare-name return annotation pin / abstract guard / init defaults / get-set round-trip + chaining / None no-op; Red confirmed — test_spec_notes_are_verbatim failed on "Define" ≠ "Defines" + paraphrased getter/setter docstrings, test_base_and_inheritance_shape failed on quoted `'ImplementationProps'` return annotation with embedded quotes)
  - [x] Step 3 — Implement model class (Green) (production change: setter return annotation de-quoted `"ImplementationProps"` → bare `ImplementationProps` (Rule 0003 — PEP 563 stores quotes verbatim; 3.8 get_type_hints would return str); field `symbol: Optional[CIdentifier]`, base `Referrable, ABC`, None no-op and chaining already spec-correct; Green = 5/6 — test_spec_notes_are_verbatim intentionally Red pending Step 4)
  - [x] Step 4 — Sync docstrings (wipe + rewrite) (`__init__` docstring wiped; class docstring rewritten verbatim from Table 5.20 Note — fixed "Define" → "Defines", single line; getter docstring = symbol Note + [constr_1909] verbatim; setter docstring = symbol Note + [constr_1909] + None-no-op sentence; wrapped 2-line inline comment rewritten single-line verbatim; no `__init__` docstring; mirror file 101/101)
  - [x] Step 5 — Write reader/writer round-trip test (Red) (new matched pair tests/test_armodel/parser/test_implementation_props.py + tests/test_armodel/writer/test_implementation_props.py, 2+2 tests: SYMBOL field value populated/emitted, absent-SYMBOL leaves None / emits no SYMBOL element (0..1 analog of the empty-wrapper case); no behavioral Red — readImplementationProps/writeImplementationProps already correct, 4/4 green on first run, tests pin the field-value contract at the class's own level)
  - [x] Step 6 — Update parser & writer (Green) (no production change — verified present: parser `readImplementationProps` (arxml_parser.py:8158) = readReferrable + setSymbol(SYMBOL), writer `writeImplementationProps` (arxml_writer.py:7569) = writeReferrable + getSymbol→SYMBOL; Rule 0013.1 leveling verified for call sites 1913/2123→8163/4234 reader and 6648/4892/7231 writer; no chained mutators introduced; REPORTED UNFIXED consumer gap: `readSectionNamePrefixes`/`writeSectionNamePrefixes` (arxml_parser.py:4668, arxml_writer.py:5961) call readReferrable/writeReferrable directly on the ImplementationProps subclass SectionNamePrefix — inherited SYMBOL dropped on round-trip; no fixture carries SECTION-NAME-PREFIX; fix belongs to the SectionNamePrefix/ResourceConsumption row)
  - [x] Step 7 — Update checklist comment (6-column format with release column: `# Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.20, p.287`; `__init__` [—]/[—], getSymbol writer [x] (writeImplementationProps calls it), setSymbol reader [x] (readImplementationProps calls it) — verified against arxml_parser.py:8158-8160 / arxml_writer.py:7569-7571; release R23-11; set-based checklist==methods check green; NO `# Spec verified:` — deferred to batch confirmation)
  - [x] Step 8 — Deviations (fixed+recorded in step notes: class docstring "Define" → Note verbatim "Defines", `__init__` docstring wiped, paraphrased getter/setter docstrings → symbol Note verbatim + [constr_1909] (+ None-no-op sentence on setter), wrapped 2-line inline comment → single-line verbatim, old 4-column checklist → 6-column R23-11, quoted return annotation → bare name (Rule 0003); no open deviations for the class itself — tracker method_deviation_by_class.md has no ImplementationProps rows (SymbolicNameProps mentions are historical subclass write-ups, stale artifacts); REPORTED UNFIXED: consumer SectionNamePrefix reader/writer gap (see Step 6) — fix belongs to its own row)
  - [ ] Step 9 — Verify (9a) + confirm (9b) [9a: 10949 unit tests + flake8 + ruff + black green; **stamp deferred to batch confirmation (user instruction 2026-09-24)**]

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
