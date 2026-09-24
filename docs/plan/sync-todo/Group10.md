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

- [ ] `SwcImplementation` — Implementation — R23-11 markdown · Table 8.7 (CP_TPS_SoftwareComponentTemplate)
  - module: M2/AUTOSARTemplates/SWComponentTemplate/SwcImplementation.py
  - [x] Step 1 — Sync members & description from spec (Table 8.7, p.623 SWC TPS; concrete Class; Base most-derived = `Implementation` (exists in src, CommonStructure/Implementation.py, stamped R23-11); 3 attrs: behavior (SwcInternalBehavior 0..1 ref) / perInstanceMemorySize (PerInstanceMemorySize * aggr) / requiredRTEVendor (String 0..1 attr); XSD group SWC-IMPLEMENTATION (00052 line 117039) order BEHAVIOR-REF → PER-INSTANCE-MEMORY-SIZES → REQUIRED-RTE-VENDOR; member type PerInstanceMemorySize NOT in src → Rule 0001.10 placeholder, reader/writer for PER-INSTANCE-MEMORY-SIZES deferred; found: paraphrased docstrings, untyped accessors, old 4-column checklist, REQUIRED-RTE-VENDOR missing in reader+writer)
  - [x] Step 2 — Write model class unit test (Red) (6 tests: verbatim spec Notes / base shape + bare-name setter return annotations / init defaults / behaviorRef get-set + chaining + None no-op / perInstanceMemorySizes add-get + chaining + None no-op / requiredRTEVendor get-set + chaining + None no-op; Red confirmed 1st run — 5 failed on paraphrased docstrings, missing annotations and unguarded setters, 1 passed on defaults already None/[])
  - [x] Step 3 — Implement model class (Green) (production change: base kept `Implementation` (most-derived, stamped), `from __future__ import annotations` + typing imports added, PEP 526 members `behaviorRef: Optional[RefType]` / `perInstanceMemorySizes: List["PerInstanceMemorySize"]` (Rule 0001.10 placeholder — class not in src) / `requiredRTEVendor: Optional[String]`, typed accessors, setters return self, None no-ops; docstrings wiped pending Step 4; Green = 5/6 — test_spec_notes_are_verbatim intentionally Red pending Step 4)
  - [x] Step 4 — Sync docstrings (wipe + rewrite) (all old docstrings wiped in Step 3; class docstring = Table 8.7 Note verbatim incl. `Tags: atp.recommendedPackage=SwcImplementations` tail; behavior comment/getter/setter = Note verbatim + [constr_1969] (+ None-no-op sentence on setter); perInstanceMemorySize Note verbatim — markdown column-wrap `PerInstanceMemory Size` fixed to `PerInstanceMemorySize` per XSD doc, `Stereotypes:`/`Tags:` tail dropped; requiredRTEVendor Note verbatim; no `__init__` docstring; mirror file 6/6)
  - [x] Step 5 — Write reader/writer round-trip test (Red) (new matched pair tests/test_armodel/parser/test_swc_implementation.py + tests/test_armodel/writer/test_swc_implementation.py, 3+3 tests: BEHAVIOR-REF value+DEST read / REQUIRED-RTE-VENDOR String value read / absent-element leaves None; BEHAVIOR-REF+REQUIRED-RTE-VENDOR emitted in XSD order / unset fields emit no elements incl. no PER-INSTANCE-MEMORY-SIZES / full save→reload field values; Red confirmed 1st run — 3 failed on REQUIRED-RTE-VENDOR missing in reader+writer+round-trip, 3 passed on BEHAVIOR-REF and absent cases)
  - [x] Step 6 — Update parser & writer (Green) (production change: `readSwcImplementation` adds `impl.setRequiredRTEVendor(getChildElementOptionalString(element, "REQUIRED-RTE-VENDOR"))` (spec-typed String pair, arxml_parser.py:5079); `writeSwcImplementation` adds `setChildElementOptionalString(child_element, "REQUIRED-RTE-VENDOR", impl.getRequiredRTEVendor())` after BEHAVIOR-REF (XSD order, arxml_writer.py:6438); no chained mutators; Rule 0013.1 leveling unchanged — readSwcImplementation calls readImplementation only, no extra readReferrable; PER-INSTANCE-MEMORY-SIZES deferred with the placeholder member; Green = 6/6 model + 3/3 parser + 3/3 writer + 11 pre-existing implementation parser/writer tests)
  - [x] Step 7 — Update checklist comment (6-column format with release column: `# Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 8.7, p.623`; `__init__` [—]/[—]; getBehaviorRef writer [x] / setBehaviorRef reader [x] — verified against arxml_parser.py:5079-5086 / arxml_writer.py:6438-6444; getRequiredRTEVendor writer [x] / setRequiredRTEVendor reader [x]; getPerInstanceMemorySizes writer [ ] / addPerInstanceMemorySize reader [ ] — pending PerInstanceMemorySize class (Rule 0001.10); rows in source order; NO `# Spec verified:` — deferred to batch confirmation)
  - [x] Step 8 — Deviations (fixed+recorded in step notes: whole-class stub (Rule 0001.3 shape-3) — no `# Spec:` line, paraphrased docstrings, untyped bare-`T` 0..1 members, unguarded setters, old 4-column checklist — all replaced from Table 8.7; REQUIRED-RTE-VENDOR silently dropped on round-trip (absent from readSwcImplementation AND writeSwcImplementation) — added both sides via spec-typed String pair; `from __future__ import annotations` added for bare-name annotations (Rule 0003); no entries in method_deviation_by_class.md / _v2.md; REPORTED UNFIXED: member type `PerInstanceMemorySize` (own Table 8.8, p.624, same spec package) not in src — Rule 0001.10 placeholder `List["PerInstanceMemorySize"]`, reader/writer for PER-INSTANCE-MEMORY-SIZES deferred (checklist reader/writer `[ ]`), fix belongs to a future PerInstanceMemorySize queue row)
  - [ ] Step 9 — Verify (9a) + confirm (9b) [9a: 10960 unit tests + integration 11 round-trips + flake8 + ruff + black green; **stamp deferred to batch confirmation (user instruction 2026-09-24)**]

- [ ] `ImplementationDataTypeElement` — AbstractImplementationDataTypeElement — R23-11 markdown · Table 5.17 (CP_TPS_SoftwareComponentTemplate)
  - module: M2/AUTOSARTemplates/CommonStructure/ImplementationDataTypes.py
  - [x] Step 1 — Sync members & description from spec (Table 5.17, p.270 SWC TPS; concrete Class; Base most-derived = `AbstractImplementationDataTypeElement` (stamped R23-11, Table 5.16 p.269); VariationPointCapable mixin already on the class per Rule 0020 — subElement aggr row atpVariation, XSD VARIATION-POINT "Applicable for: ImplementationDataTypeElement.subElement"; 7 attrs displayed order: arrayImplPolicy/arraySize/arraySizeHandling/arraySizeSemantics (page 1) + isOptional/subElement (ordered)/swDataDefProps (page 2); XSD group IMPLEMENTATION-DATA-TYPE-ELEMENT (00052 line 71561) element order ARRAY-IMPL-POLICY → ARRAY-SIZE → ARRAY-SIZE-HANDLING → ARRAY-SIZE-SEMANTICS → IS-OPTIONAL → SUB-ELEMENTS → SW-DATA-DEF-PROPS → VARIATION-POINT; markdown column wraps fixed per XSD mmt.qualifiedName: arraySizeHandling/ArraySizeHandlingEnum, arraySizeSemantics/ArraySizeSemanticsEnum, subElement, "ImplementationDataTypeElement" in isOptional Note; found: model types loose (ARLiteral/ARNumerical vs spec enums/PositiveInteger), untyped accessors, no Optional annotations, quoted return annotations (module lacks `from __future__ import annotations`), paraphrased class docstring, no per-member docstrings, old 4-column checklist, ARRAY-IMPL-POLICY + IS-OPTIONAL missing in reader AND writer, writer ARRAY-SIZE loose cross pair (setChildElementOptionalLiteral vs reader getChildElementOptionalPositiveInteger))
  - [x] Step 2 — Write model class unit test (Red) (10 tests: verbatim spec Notes (class + all 7 attrs' accessor docstrings incl. None-no-op sentences) / base shape (AbstractImplementationDataTypeElement + VariationPointCapable) + bare-name PEP 563 return annotations / init defaults / typed get-set+chaining+None no-op ×5 (ArrayImplPolicyEnum PAYLOAD_AS_POINTER_TO_ARRAY, PositiveInteger "4", ArraySizeHandlingEnum, ArraySizeSemanticsEnum, Boolean, SwDataDefProps) / create+getSubElements incl. duplicate-returns-existing; Red confirmed 1st run — test_spec_notes_are_verbatim + test_base_and_inheritance_shape failed on paraphrased class docstring, missing member docstrings and missing return annotations, 8 passed pinning already-correct runtime behavior; fabricated ARRAY_SIZE_SEMANTICS_* constants removed with their 2 old tests)
  - [x] Step 3 — Implement model class (Green) (production change: `from __future__ import annotations` added (module lacked PEP 563 — bare-name annotations, Rule 0003); imports ArraySizeHandlingEnum (Datatypes.py, no cycle) + PositiveInteger, unused ARLiteral/ARNumerical dropped; PEP 526 members retyped to spec types `Optional[ArrayImplPolicyEnum]`/`Optional[PositiveInteger]`/`Optional[ArraySizeHandlingEnum]`/`Optional[ArraySizeSemanticsEnum]`/`Optional[Boolean]`/`List[ImplementationDataTypeElement]`/`Optional[SwDataDefProps]` (was ARLiteral/ARNumerical/bare — Rule 0001.3); all accessors typed `Optional[T]`/`List[T]` with bare-name `-> ImplementationDataTypeElement` setter returns, None no-ops kept; dedicated subElements typed list + createImplementationDataTypeElement (Referrable child factory) kept, duplicate-returns-existing verified; fabricated ARRAY_SIZE_SEMANTICS_FIXED_SIZE/VARIABLE_SIZE constants removed (no spec basis, no production consumers — Rule 0001.3); base kept (AbstractImplementationDataTypeElement, VariationPointCapable); Green = 38/38 except test_spec_notes_are_verbatim intentionally Red pending Step 4)
  - [x] Step 4 — Sync docstrings (wipe + rewrite) (all old docstrings wiped in Step 3 (paraphrased class docstring, old 4-column checklist, no per-member docstrings); class docstring = Table 5.17 Note verbatim incl. spec "fur" typo and • bullets; per-attr inline `__init__` comments + getter docstrings + setter docstrings = Note verbatim (Stereotypes/Tags tails dropped; markdown column wraps fixed per XSD docs: "ImplementationDataTypeElement" in arraySize/isOptional Notes, "a ImplementationDataType" in subElement Note; "ImplementionDataTypeElement" spec typo kept verbatim); setter docstrings carry the appended None-no-op sentence inline (queue precedent — joined into the same paragraph after a first-pass paragraph-split failed the verbatim test); createImplementationDataTypeElement + getSubElements = subElement Note verbatim; no `__init__` docstring; blank line between every attribute block; mirror file 39/39)
  - [x] Step 5 — Write reader/writer round-trip test (Red) (new matched pair tests/test_armodel/parser/test_implementation_data_type_element.py + tests/test_armodel/writer/test_implementation_data_type_element.py, 5+4 tests: reader ARRAY-IMPL-POLICY value / IS-OPTIONAL Boolean true / ARRAY-SIZE PositiveInteger 8 + HANDLING + SEMANTICS values / nested SUB-ELEMENTS recursion incl. child ARRAY-IMPL-POLICY / absent-elements leaves all None; writer ARRAY-IMPL-POLICY+IS-OPTIONAL emitted with values / 7 own elements in XSD group order / unset fields emit nothing incl. no SUB-ELEMENTS wrapper / full save→reload via ImplementationDataType dispatch asserting all field values incl. nested; Red confirmed 1st run — 6 failed (ARRAY-IMPL-POLICY + IS-OPTIONAL missing in reader AND writer, nested round-trip, XSD order), 3 passed on already-covered paths)
  - [x] Step 6 — Update parser & writer (Green) (production change: `readImplementationDataTypeElement` adds setArrayImplPolicy(ARRAY-IMPL-POLICY via getChildElementOptionalLiteral — enum value form, Rule 0010/0011 convention) + setIsOptional(IS-OPTIONAL via getChildElementOptionalBooleanValue), elements now in XSD group order; `writeImplementationDataTypeElement` adds setChildElementOptionalLiteral(ARRAY-IMPL-POLICY, getArrayImplPolicy) + setChildElementOptionalBooleanValue(IS-OPTIONAL, getIsOptional), and ARRAY-SIZE upgraded from loose setChildElementOptionalLiteral to spec-typed setChildElementOptionalPositiveInteger (matched pair with reader getChildElementOptionalPositiveInteger, Rule 0013.2) — closes the deferred ArrayImplPolicyEnum consumer gap; no chained mutators; Rule 0013.1 leveling unchanged (readAutosarDataType called once, no double base read; writeAbstractImplementationDataTypeElement owns writeARElement); Green = 162/162 across new parser+writer tests, mirrored model file, pre-existing test_implementation_data_type.py and test_writer_impl_types_ports.py)
  - [x] Step 7 — Update checklist comment (6-column format with release column: `# Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.17, p.270`; rows in source order == markdown displayed order (arrayImplPolicy → arraySize → arraySizeHandling → arraySizeSemantics → isOptional → subElement → swDataDefProps grouping); reader [x] on all 6 setter rows + createImplementationDataTypeElement, writer [x] on all 6 getter rows + getSubElements — verified against actual call sites arxml_parser.py:6533-6540 (readImplementationDataTypeElement incl. setSwDataDefProps via readAutosarDataType:6501) and arxml_writer.py:7550-7561 (writeImplementationDataTypeElement, setSwDataDefProps:7559); `__init__` [—]/[—]; set-based checklist==methods + source-order checks green; NO `# Spec verified:` — deferred to batch confirmation)
  - [x] Step 8 — Deviations (fixed+recorded in step notes: ARRAY-IMPL-POLICY missing in reader AND writer (the gap deferred from the ArrayImplPolicyEnum row) — CLOSED here; IS-OPTIONAL missing in reader AND writer — added both sides; writer ARRAY-SIZE cross pair setChildElementOptionalLiteral vs reader getChildElementOptionalPositiveInteger — upgraded to matched setChildElementOptionalPositiveInteger (Rule 0013.2); loose model types ARLiteral/ARNumerical vs spec ArrayImplPolicyEnum/PositiveInteger/ArraySizeHandlingEnum/ArraySizeSemanticsEnum — retyped (Rule 0001.3); untyped accessors + bare/quoted annotations — typed with PEP 563 bare names (Rule 0003); paraphrased class docstring, missing member docstrings, old 4-column checklist — verbatim rewrite + 6-column (Rules 0012/0002); fabricated ARRAY_SIZE_SEMANTICS_FIXED_SIZE/VARIABLE_SIZE class constants — removed (no spec basis, no production consumers, Rule 0001.3); VariationPointCapable mixin confirmed per Rule 0020 (subElement atpVariation row + XSD VARIATION-POINT anchor) — already on the class, no per-class rows; REPORTED UNFIXED: none for this class — readAutosarDataType reuse in readImplementationDataTypeElement noted as an observation (AutosarDataType is not in the model Base chain, but the call is single-level, correct-coverage and pre-existing; parser has no readAtpStructureElement/readAbstractImplementationDataTypeElement level to mirror — the abstract base's own table has no attributes, so its [—]/[—] checklist rows are correct); no entries in method_deviation_by_class.md / _v2.md for this class (v2's AbstractImplementationDataTypeElement "missing —" row is a stale intake artifact — Table 5.16 has no attributes); no integration fixture carries IMPLEMENTATION-DATA-TYPE-ELEMENT (verified) so no fixture interplay)
  - [ ] Step 9 — Verify (9a) + confirm (9b) [9a: 10955 unit tests + integration 3 round-trip suites + flake8 + ruff + black green; **stamp deferred to batch confirmation (user instruction 2026-09-24)**]

- [ ] `ReceptionComSpecProps` — ARObject — R23-11 markdown · Table 4.64 (CP_TPS_SoftwareComponentTemplate)
  - module: M2/AUTOSARTemplates/SWComponentTemplate/Communication.py
  - [x] Step 1 — Sync members & description from spec (Table 4.64, p.174 SWC TPS; concrete Class (atpObject); Base = ARObject confirmed; aggregated by ReceiverComSpec.receptionProps; 2 attrs displayed order dataUpdatePeriod → timeout, both TimeValue 0..1 attr; XSD group RECEPTION-COM-SPEC-PROPS (00052 line 96132) element order DATA-UPDATE-PERIOD → TIMEOUT; markdown column wrap "dataUpdate Period" fixed per XSD mmt.qualifiedName; found: quoted setter return annotations (module lacks PEP 563), paraphrased getter/setter docstrings, old 5-column checklist without release column; reader/writer coverage already present (getReceptionComSpecProps arxml_parser.py:6612 / writeReceptionComSpecProps arxml_writer.py:1688) but no parser/writer tests exist)
  - [x] Step 2 — Write model class unit test (Red) (5 tests appended to test_Communication.py: verbatim spec Notes (class + 4 accessor docstrings incl. None-no-op sentences) / base shape (ARObject) + bare-name PEP 563 return annotations / init defaults / typed get-set+chaining+None no-op ×2 (TimeValue 0.02, 2.5); Red confirmed 1st run — test_spec_notes_are_verbatim failed on the paraphrased "Gets the period…" docstrings, 4 passed pinning already-correct runtime behavior)
  - [x] Step 3 — Implement model class (Green) (production change: `from __future__ import annotations` added (module lacked PEP 563 — bare-name annotations, Rule 0003); my class's quoted setter returns `-> "ReceptionComSpecProps"` → bare `-> ReceptionComSpecProps`; 43 sibling quoted annotations left untouched (siblings' own sync passes fix theirs — ImplementationDataTypes.py precedent); field/accessor types, None no-ops, chaining, member order already spec-correct — no other change; Green = 61/62 behavior tests pass, test_spec_notes_are_verbatim intentionally Red pending Step 4)
  - [x] Step 4 — Sync docstrings (wipe + rewrite) (paraphrased getter/setter docstrings with "Gets/Sets the…" prefixes and Args/Returns boilerplate wiped; getter docstrings = Table 4.64 Notes verbatim; setter docstrings = Note verbatim + None-no-op sentence joined inline (queue precedent); class docstring and both `__init__` inline comments already Note-verbatim, kept identical after wipe-check; no `__init__` docstring; blank line between attribute blocks kept; mirror file 62/62)
  - [x] Step 5 — Write reader/writer round-trip test (Red) (new matched pair tests/test_armodel/parser/test_reception_com_spec_props.py (5 tests: both elements field values / TIMEOUT-only with DATA-UPDATE-PERIOD None / minimal empty wrapper / absent wrapper → None / aggregator wiring via getQueuedReceiverComSpec) + tests/test_armodel/writer/test_reception_com_spec_props.py (6 tests: field values / XSD order DATA-UPDATE-PERIOD→TIMEOUT / None props emit nothing / empty wrapper / comspec-level round-trip via writeNonqueuedReceiverComSpec → getNonqueuedReceiverComSpec asserting values / absent-props round-trip); BORN GREEN 1st run 11/11 — reader/writer coverage pre-exists and is spec-correct, so no Red was possible; tests pin previously-untested behavior (no RECEPTION-PROPS test existed anywhere))
  - [x] Step 6 — Update parser & writer (Green) (no production change: getReceptionComSpecProps (arxml_parser.py:6612) reads DATA-UPDATE-PERIOD/TIMEOUT via setDataUpdatePeriod/setTimeout with spec-typed getChildElementOptionalTimeValue, readARObject once (ARObject base, no Referrable); writeReceptionComSpecProps (arxml_writer.py:1688) emits via getDataUpdatePeriod/getTimeout with setChildElementOptionalTimeValue, writeARObject once, XSD order; aggregators verified by grep — getQueuedReceiverComSpec:6754 + getNonqueuedReceiverComSpec:6769 → readReceiverComSpec:6601 → helper; writeQueuedReceiverComSpec:1857 + writeNonqueuedReceiverComSpec:1871 → writeReceiverComSpec:1673 → helper; matched name pairs at every layer (Rule 0013.2), no chained mutators, Green = 11/11)
  - [x] Step 7 — Update checklist comment (6-column format with release column: `# Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 4.64, p.174`; rows in source order == markdown displayed order (dataUpdatePeriod → timeout, getter first per scalar shape); reader [x] on both setter rows — verified against getReceptionComSpecProps call sites arxml_parser.py:6618-6619; writer [x] on both getter rows — verified against writeReceptionComSpecProps arxml_writer.py:1690-1691; `__init__` [—]/[—]; set-based checklist==methods + coverage + source-order + no-marker checks green; NO `# Spec verified:` — deferred to batch confirmation)
  - [x] Step 8 — Deviations (fixed+recorded in step notes: quoted setter return annotations + module lacking PEP 563 (Rule 0003) — fixed in Step 3; paraphrased getter/setter docstrings with "Gets/Sets the…" prefixes and Args/Returns boilerplate (Rule 0001.4/0012) — wiped+rewritten verbatim in Step 4; old 5-column checklist without release column (Rule 0002) — rewritten 6-column in Step 7; missing reader/writer test coverage — no RECEPTION-PROPS test existed anywhere, 11 tests added in Step 5; markdown column wrap "dataUpdate Period" fixed per XSD mmt.qualifiedName at Step 1; no open deviations — no entries for this class in method_deviation_by_class.md / _v2.md; consumer observation: ReceiverComSpec itself (Table 4.60) remains unstamped but is not queued in this file — its receptionProps aggregation coverage exists and is now test-pinned)
  - [ ] Step 9 — Verify (9a) + confirm (9b) [9a: 10971 unit tests + integration 3 round-trip suites + flake8 + ruff + black green; **stamp deferred to batch confirmation (user instruction 2026-09-24)**]

- [ ] `CompositeNetworkRepresentation` — ARObject — R23-11 markdown · Table 4.74 (CP_TPS_SoftwareComponentTemplate)
  - module: M2/AUTOSARTemplates/SWComponentTemplate/Communication.py
  - [x] Step 1 — Sync members & description from spec (Table 4.74, p.181 SWC TPS; concrete Class (atpObject); Base = ARObject confirmed; aggregated by ReceiverComSpec/SenderComSpec .compositeNetworkRepresentation; 2 attrs displayed order leafElement (iref 0..1, InstanceRef implemented by ApplicationCompositeElementInPortInterfaceInstanceRef — markdown Type column names the pointed-to ApplicationCompositeElementDataPrototype) → networkRepresentation (aggr 0..1, SwDataDefProps, atpSplitable); XSD group COMPOSITE-NETWORK-REPRESENTATION (00052 line 20804) element order LEAF-ELEMENT-IREF → NETWORK-REPRESENTATION; markdown column wraps fixed per XSD ("network Representation", "CompositeNetwork Representation", "Application CompositeDataType"); not VP-capable (atpSplitable only, no variationPoint.shortLabel tag; XSD group has no VARIATION-POINT — Rule 0020); found: quoted setter return annotations (module HAS PEP 563), paraphrased getter/setter docstrings with Args/Returns boilerplate, Stereotypes/Tags tail left in networkRepresentation comment, dead duplicated assignment after `return self` in setNetworkRepresentation, old 5-column checklist without release column; reader/writer coverage already present (getCompositeNetworkRepresentation arxml_parser.py:6583 / writeCompositeNetworkRepresentation arxml_writer.py:1653)
  - [x] Step 2 — Write model class unit test (Red) (5 tests replacing the single old test in test_Communication.py's TestCompositeNetworkRepresentation (old test set a bare RefType on leafElementIRef — wrong spec type): verbatim spec Notes (class + 4 accessor docstrings incl. None-no-op sentences) / base shape (ARObject) + bare-name PEP 563 return annotations / init defaults / typed get-set+chaining+None no-op for leafElementIRef (ApplicationCompositeElementInPortInterfaceInstanceRef with root/target RefType values) and networkRepresentation (SwDataDefProps); Red confirmed 1st run — test_spec_notes_are_verbatim + test_base_and_inheritance_shape failed (paraphrased docstrings, quoted return annotation), 3 passed pinning already-correct runtime behavior)
  - [x] Step 3 — Implement model class (Green) (production change: my class's quoted setter returns `-> "CompositeNetworkRepresentation"` → bare `-> CompositeNetworkRepresentation` ×2 (module has PEP 563, Rule 0003); dead duplicated `self.networkRepresentation = value` after `return self` in setNetworkRepresentation removed; field/accessor types, None no-ops, chaining, member order already spec-correct — no other change; Green = 4/5, test_spec_notes_are_verbatim intentionally Red pending Step 4)
  - [x] Step 4 — Sync docstrings (wipe + rewrite) (all paraphrased getter/setter docstrings with "Gets/Sets the…" prefixes + Args/Returns boilerplate wiped; getter docstrings = Table 4.74 Notes verbatim; setter docstrings = Note verbatim + "." joiner + None-no-op sentence inline (stamped InstanceRefs.py precedent for Notes without trailing period); networkRepresentation comment/docstrings fixed to XSD wording — wrap-space "Application CompositeDataType" → "ApplicationCompositeDataType", "CompositeNetwork Representation" → "CompositeNetworkRepresentation", Stereotypes/Tags tail dropped (Rule 0012.2.5.2); class docstring already Note-verbatim, kept identical after wipe-check; no `__init__` docstring; blank line between attribute blocks kept; mirror file 66/66)
  - [x] Step 5 — Write reader/writer round-trip test (Red) (new matched pair tests/test_armodel/parser/test_composite_network_representation.py (5 tests: both elements incl. iref root/context×2/target ref values + SwDataDefProps BASE-TYPE-REF value / context list document order + NETWORK-REPRESENTATION None / LEAF-ELEMENT-IREF-only / minimal empty element → both None / aggregation via getQueuedReceiverComSpec asserting field values) + tests/test_armodel/writer/test_composite_network_representation.py (7 tests: field values incl. inner iref refs / XSD order LEAF-ELEMENT-IREF→NETWORK-REPRESENTATION / None emits nothing / unset fields emit empty element / full comspec-level round-trip via writeQueuedReceiverComSpec → getQueuedReceiverComSpec asserting all field values / ARObject S/T attribute round-trip / absent list → no wrapper + reload []); 1st run 3 failed — 2 were my wrong fixture (BASE-TYPE-REF placed directly under NETWORK-REPRESENTATION instead of SW-DATA-DEF-PROPS-VARIANTS/SW-DATA-DEF-PROPS-CONDITIONAL; fixture fixed, production coverage pre-exists and is correct) + writer BASE-TYPE-REF same fixture issue; after fixture fix 10/10 born green on own-elements coverage)
  - [x] Step 6 — Update parser & writer (Green) (production change: `getCompositeNetworkRepresentation` (arxml_parser.py:6583) gains `readARObject(element, representation)` and `writeCompositeNetworkRepresentation` (arxml_writer.py:1653) gains `writeARObject(child_element, representation)` — the AR-OBJECT attributeGroup S/T (checksum/timestamp) of the COMPOSITE-NETWORK-REPRESENTATION element were dropped on round-trip (Rule 0001.7 inherited-base-attribute gap; sibling ReceptionComSpecProps helper already had it); Red confirmed 1st run (new test_round_trip_ar_object_attributes failed), Green after the fix; own-element order already XSD-correct (LEAF-ELEMENT-IREF → NETWORK-REPRESENTATION); matched name pairs at every layer (setLeafElementIRef/getLeafElementIRef ↔ LEAF-ELEMENT-IREF via get/setApplicationCompositeElementInPortInterfaceInstanceRef; setNetworkRepresentation/getNetworkRepresentation ↔ NETWORK-REPRESENTATION via get/setSwDataDefProps), no chained mutators, readARObject/writeARObject called once (ARObject direct base — no double base read); Green = 78/78 across both new files + mirror file)
  - [x] Step 7 — Update checklist comment (6-column format with release column: `# Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 4.74, p.181`; rows in source order == markdown displayed order (leafElement → networkRepresentation, getter first per scalar shape); reader [x] on both setter rows — verified against getCompositeNetworkRepresentation call sites arxml_parser.py:6587-6588; writer [x] on both getter rows — verified against writeCompositeNetworkRepresentation arxml_writer.py:1658-1659; `__init__` [—]/[—]; set-based checklist==methods + source-order + coverage + no-marker checks green; NO `# Spec verified:` — deferred to batch confirmation)
  - [x] Step 8 — Deviations (fixed+recorded in step notes: quoted setter return annotations (Rule 0003) — fixed in Step 3; dead duplicated `self.networkRepresentation = value` after `return self` in setNetworkRepresentation — removed in Step 3; paraphrased getter/setter docstrings with "Gets/Sets the…" prefixes + Args/Returns boilerplate (Rule 0001.4/0012) — wiped+rewritten verbatim in Step 4; Stereotypes/Tags tail + markdown wrap-spaces ("Application CompositeDataType", "CompositeNetwork Representation") in networkRepresentation comment (Rule 0012.2.5.2) — fixed to XSD wording in Step 4; old 5-column checklist without release column (Rule 0002) — rewritten 6-column in Step 7; ARObject S/T (checksum/timestamp attributeGroup) dropped on round-trip in reader AND writer (Rule 0001.7 inherited-base-attribute gap) — readARObject/writeARObject added in Step 6; old model test set a bare RefType on leafElementIRef — replaced with spec-typed ApplicationCompositeElementInPortInterfaceInstanceRef in Step 2; no open deviations — no entries for this class in method_deviation_by_class.md / _v2.md; consumer observation: aggregators ReceiverComSpec/SenderComSpec (COMPOSITE-NETWORK-REPRESENTATIONS wrapper `*` aggregation) remain unstamped and are not queued in this file — their aggregation coverage exists and is now test-pinned)
  - [ ] Step 9 — Verify (9a) + confirm (9b) [9a: 10987 unit tests + integration 3 round-trip suites + flake8 + ruff + black green; **stamp deferred to batch confirmation (user instruction 2026-09-24)**]

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
