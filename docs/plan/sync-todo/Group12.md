# Sync todo: Group 12 — SwcInternalBehavior & measurement refs

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

- [ ] `ParameterAccess` — AbstractAccessPoint — R23-11 CP_TPS_SoftwareComponentTemplate Table 7.40, p.586
  - module: M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/DataElements/__init__.py
  - note (Step 1): Base chain ARObject/AbstractAccessPoint/AtpClassifier/AtpFeature/AtpStructureElement/Identifiable/MultilanguageReferrable/Referrable — most-derived base AbstractAccessPoint (stamped `# Spec verified: R23-11`, BSWModuleDescriptionTemplate Table 4.24, p.57 — no blocker). Attrs (displayed order): accessedParameter (AutosarParameterRef, 0..1, aggr), swDataDefProps (SwDataDefProps, 0..1, aggr). BSW appendix Table D.48 verified identical reproduction. XSD PARAMETER-ACCESS group (AUTOSAR_00052.xsd:87809) element order ACCESSED-PARAMETER, SW-DATA-DEF-PROPS, VARIATION-POINT; class docstring Note renders "ParameterData Prototype" in markdown (line-wrap artifact; XSD documentation + VariableAccess precedent join it as "ParameterDataPrototype"). Existing reader/writer drop SW-DATA-DEF-PROPS (genuine Red pending).
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red) (note: Red via None-no-op + get_type_hints pins; `test_initialization` passed immediately — defaults were already correct)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red) (note: Red on all three SW-DATA-DEF-PROPS gaps — reader, writer, populated round-trip; empty round-trip + optional-children-omitted passed immediately, already correct)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - note (Step 8): no in-scope deviations remain (both Table 7.40 attributes modeled, typed `Optional[T]`, reader+writer covered; no naming/type/missing rows). Observations (out of scope, not blockers): (1) `AbstractAccessPoint.returnValueProvision` (RETURN-VALUE-PROVISION) has no reader/writer coverage anywhere — inherited-base gap (Rule 0001.7) for a future AbstractAccessPoint drift pass; no fixture carries the element. (2) `RunnableEntity.getParameterAccesses` still filters the `elements` registry (`sorted(filter(...))`) although `self.parameterAccesses` exists (Rule 0004 to-fix shape) — aggregator row, not this class. (3) Writer emits VARIATION-POINT via `writeIdentifiable` (IDENTIFIABLE-group position) rather than the XSD group tail position — generic pre-existing behavior, round-trip lossless. (4) Adding `from __future__ import annotations` (bare-name pins, Rule 0003/0005) made this module a PEP 563 module and tripped `test_no_top_level_quoted_annotations_in_pep563_modules`: 6 pre-existing top-level quoted return annotations in `VariableAccess` (setAccessedVariableRef, setScope) and `ArVariableInImplementationDataInstanceRef` (4 setters) were mechanically unquoted to bare same-module names to keep the suite green — no runtime behavior change, row 2's spec state untouched (nested quotes left for row 2's own pass).
  - [x] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-24: touched tests 467 passed (model DataElements/test___init__.py + parser/test_arxml_parser_orchestrators.py + writer/test_writer_swc_behavior.py); full suite 11534 passed / 0 failed (`uv run python scripts/run_tests.py --no-coverage`, baseline 11527 + 7 new); `uv run ruff check src tests scripts` clean; black clean on all 6 touched files (23 unrelated pre-existing files at HEAD fail repo-wide black --check — not touched); set-based checklist==methods + coverage audit OK; verbatim docstring/`# type:`/blank-line/export/get_type_hints pin audits OK; integration round-trip 11/11. 9b deferred to batch confirmation (user instruction 2026-09-24)

- [ ] `VariableAccess` — AbstractAccessPoint — R23-11 CP_TPS_SoftwareComponentTemplate Table 7.33, p.567
  - module: M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/DataElements/__init__.py
  - note (Step 1): Base chain ARObject/AbstractAccessPoint/AtpClassifier/AtpFeature/AtpStructureElement/Identifiable/MultilanguageReferrable/Referrable — most-derived base AbstractAccessPoint (stamped `# Spec verified: R23-11`; current `(AbstractAccessPoint, VariationPointCapable)` shape already matches the ParameterAccess convention). Attrs (displayed order): accessedVariable (AutosarVariableRef, 0..1, aggr; XSD mmt.qualifiedName "VariableAccess.accessedVariable" — existing field/accessors `accessedVariableRef`/`getAccessedVariableRef`/`setAccessedVariableRef` are a Rule 0001.5 naming mismatch → rename to accessedVariable/getAccessedVariable/setAccessedVariable, consumers parser:6662, writer:1728/3855, cli/arxml_dump_cli.py), scope (VariableAccessScopeEnum, 0..1 — enum class does not exist in the codebase; Rule 0001.10 placeholder `Optional[ARLiteral]` kept, reported at Step 8). Class Note renders "VariableData Prototype" in markdown (line-wrap artifact; XSD documentation joins it as "VariableDataPrototype"). BSW appendix D.78 + TimingExtensions D.67 verified identical; SystemTemplate F.142 is heading-only (no table body). XSD VARIABLE-ACCESS group (AUTOSAR_00052.xsd:129453) element order ACCESSED-VARIABLE, SCOPE, VARIATION-POINT. Consume-path gaps (genuine Red pending): writer `writeVariableAccess` drops SCOPE; parser `readVariableAccesses` (all 7 RunnableEntity roles) never reads SCOPE; `readVariableAccess` + `writeReceiverReplaceWith` already cover both elements.
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red) (note: Red via the Rule 0001.5 rename — `test_initialization` (no `accessedVariable` field) and `test_get_set_accessedVariable` (no `setAccessedVariable`) failed with AttributeError; `test_get_set_scope` passed immediately — scope accessors were already correct with None no-op + matching hints)
  - [x] Step 3 — Implement model class (Green) (note: rename tail per Rule 0001.5 — consumers switched to `accessedVariable`/`getAccessedVariable`/`setAccessedVariable`: parser dispatch ×7 + `readVariableAccess`, writer `writeReceiverReplaceWith` + `writeVariableAccess`, cli/arxml_dump_cli.py, one pre-existing writer test; BswVariableAccess's own `ACCESSED-VARIABLE-REF` pair untouched)
  - [x] Step 4 — Sync docstrings (wipe + rewrite) (note: class docstring = verbatim joined Note ("VariableDataPrototype" per XSD); inline `__init__` comments verbatim; getter docstrings verbatim Note; setter docstrings verbatim Note + None-no-op sentence; old "Gets/Sets the…" paraphrases removed)
  - [x] Step 5 — Write reader/writer round-trip test (Red) (note: Red on exactly the three SCOPE gaps — parser `readVariableAccesses` dispatch (`test_readRunnableEntity_with_dataReadAccess_full`), writer `writeVariableAccess` (`test_writeVariableAccess_full`), populated round-trip (`test_round_trip_populated`); `test_writeVariableAccess_optional_children_omitted` + `test_round_trip_empty` passed immediately — already correct)
  - [x] Step 6 — Update parser & writer (Green) (note: `readVariableAccesses` now delegates each created access to `readVariableAccess` (Identifiable + ACCESSED-VARIABLE + SCOPE, read exactly once — 7 duplicated `setAccessedVariable` lines removed); `writeVariableAccess` now emits SCOPE after ACCESSED-VARIABLE per XSD group order)
  - [x] Step 7 — Update checklist comment (note: `# Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 7.33, p.567` + 5 method rows in source order, 6-column format with release R23-11; marker withheld per batch instruction — see Step 8)
  - note (Step 8): one Rule 0001.10 placeholder remains — attribute `scope` is spec-typed `VariableAccessScopeEnum` (Table 7.34, same package M2::...::SwcInternalBehavior::DataElements; XSD VARIABLE-ACCESS-SCOPE-ENUM literals COMMUNICATION-INTER-ECU / COMMUNICATION-INTRA-PARTITION / INTER-PARTITION-INTRA-ECU) but the enum class does not exist in the codebase; per the Rule 0001.10 workflow relaxation the field stays `Optional[ARLiteral]` (XML text round-trips losslessly either way) and is reported here for a future pass. No other deviations: both Table 7.33 attributes modeled (`accessedVariable` renamed per Rule 0001.5, `scope` verbatim), field/getter/setter/parser/writer types agree, reader+writer covered for both, no naming/type/missing rows, no tracker entries for this class. Stamp decision: `# Spec verified:` withheld while the placeholder remains (Rule 0012.1) and per batch instruction (stamp deferred to batch confirmation). Observation (out of scope, not blockers): member types `AutosarVariableRef` and `ArVariableInImplementationDataInstanceRef` live in this module unstamped with all-`[ ]` checklists (orphan intake; `AutosarVariableRef` fields are bare-typed, setters lack None no-ops) — candidates for a future row; `BswVariableAccess` (BswBehavior.py) is a distinct class with its own `ACCESSED-VARIABLE-REF` pair, untouched.
  - [x] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-25: touched tests 473 passed (model DataElements/test___init__.py + parser/test_arxml_parser_orchestrators.py + writer/test_writer_swc_behavior.py) + test_runnable_entity.py 6 passed; full suite 11541 passed / 0 failed (`uv run python scripts/run_tests.py --no-coverage`, baseline 11534 + 7 net new); integration round-trip 11/11; `uv run ruff check src tests scripts` clean; black clean on all 8 touched files (repo-wide black --check NOT run — 23 unrelated pre-existing files at HEAD would fail; untouched); set-based checklist==methods + coverage audit OK; plain get_type_hints pin audit OK; bare-annotation / no-`# type:` / blank-line / verbatim-docstring / member-order / top-level-export audits OK. 9b deferred to batch confirmation (user instruction 2026-09-24)

- [ ] `InternalTriggeringPoint` — AbstractAccessPoint — R23-11 CP_TPS_SoftwareComponentTemplate Table 7.30, p.561
  - module: M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/Trigger.py
  - note (Step 1): Base chain ARObject/AbstractAccessPoint/AtpClassifier/AtpFeature/AtpStructureElement/Identifiable/MultilanguageReferrable/Referrable — most-derived base AbstractAccessPoint (stamped `# Spec verified: R23-11`; current `(AbstractAccessPoint, VariationPointCapable)` shape matches the ParameterAccess/VariableAccess convention; XSD complexType chain ends ABSTRACT-ACCESS-POINT → INTERNAL-TRIGGERING-POINT). Attrs (displayed order): swImplPolicy (SwImplPolicyEnum, 0..1, attr — sole attribute; member type exists as a synced AREnum, Table 5.45 p.336). BSW appendix D.39 + R4.3.1 Table 7.31 verified reproductions. Class Note + constr_1182 (STANDARD/QUEUED allowed values); attribute Note "This attribute, when set to value queued, allows for a queued processing of Triggers." Existing field bare-typed (`SwImplPolicyEnum = None`, Rule 0001.4/0003 → needs `Optional[SwImplPolicyEnum]`). XSD group element order SW-IMPL-POLICY, VARIATION-POINT. Consume-path gaps (genuine Red pending): parser `readRunnableEntityInternalTriggeringPoints` writes phantom `point.sw_impl_policy` (dropped) and skips readIdentifiable; writer has NO RunnableEntity INTERNAL-TRIGGERING-POINTS emission.
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red) (note: Red via the Rule 0001.4/0003 annotation drift — get_type_hints pins fail on bare `SwImplPolicyEnum` setter param / bare getter return / missing setter `-> InternalTriggeringPoint`; `test_initialization`, the None-no-op round-trip and the inherited returnValueProvision accessor passed immediately — behavior was already correct)
  - [x] Step 3 — Implement model class (Green) (note: `swImplPolicy` field/getter/setter re-typed `Optional[SwImplPolicyEnum]`, setter annotated `-> InternalTriggeringPoint`; touched test file 6 passed)
  - [x] Step 4 — Sync docstrings (wipe + rewrite) (note: fabricated class docstring replaced with the verbatim Table 7.30 Note + constr_1182; old "Gets/Sets the…" paraphrases wiped — getter docstring = Note verbatim, setter = Note verbatim + None-no-op sentence, inline `__init__` comment = Note verbatim; `__init__` carries no docstring)
  - [x] Step 5 — Write reader/writer round-trip test (Red) (note: Red on all 8 new tests — parser SW-IMPL-POLICY read (phantom `sw_impl_policy` field), 5 writer helper tests (no `writeRunnableEntityInternalTriggeringPoints`/`writeInternalTriggeringPoint` exist), populated round-trip and empty round-trip (wrapper dropped entirely so the point itself never reloads))
  - [x] Step 6 — Update parser & writer (Green) (note: parser — `readRunnableEntityInternalTriggeringPoints` now dispatches per child tag and delegates to new `readInternalTriggeringPoint` (readIdentifiable + SW-IMPL-POLICY via the existing `SW_IMPL_POLICY_XML_MAP` camel↔UPPER tokens, `SwImplPolicyEnum` instance stored — phantom `sw_impl_policy` line removed); writer — new `writeInternalTriggeringPoint` (writeIdentifiable + SW-IMPL-POLICY, wrapper `INTERNAL-TRIGGERING-POINTS` only when non-empty) and `writeRunnableEntityInternalTriggeringPoints`, called in `writeRunnableEntity` right after EXTERNAL-TRIGGERING-POINTS per XSD relative order; writer test accesses the filter-shaped aggregator getter via `list(...)` — getter shape itself left untouched (aggregator observation, Step 8))
  - [x] Step 7 — Update checklist comment (note: `# Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 7.30, p.561` + 3 method rows in source order (`__init__`, getSwImplPolicy, setSwImplPolicy), 6-column format with release R23-11; set-based checklist==methods + coverage audit OK; marker withheld per batch instruction — see Step 8)
  - [x] Step 8 — Deviations
  - note (Step 8): no in-scope deviations remain (sole Table 7.30 attribute swImplPolicy modeled with field + accessors typed `Optional[SwImplPolicyEnum]` per Mult. 0..1, member type = synced `SwImplPolicyEnum` Table 5.45 — no Rule 0001.10 placeholder, no naming/type/missing rows, reader+writer covered, no tracker entries for this class). Stamp decision: no deviation remains, so the stamp would be warranted at 9b — `# Spec verified:` withheld per batch instruction (stamp deferred to batch confirmation, user instruction 2026-09-24). Observations (out of scope, not blockers): (1) inherited `AbstractAccessPoint.returnValueProvision` (RETURN-VALUE-PROVISION) still has no reader/writer coverage anywhere — the AbstractAccessPoint inherited-base gap already recorded on the ParameterAccess row; applies equally here (Rule 0001.7, future AbstractAccessPoint drift pass). (2) Aggregator `RunnableEntity.getInternalTriggeringPoints` returns a bare `filter` object, not a `List` (aggregator shape; tests use `list(...)`; same family as the `getParameterAccesses` observation on the ParameterAccess row). (3) Pre-existing `writeRunnableEntity` wrapper order (MODE-ACCESS/MODE-SWITCH before EXTERNAL-TRIGGERING) does not match XSD order — generic pre-existing behavior, round-trip lossless (path-based findall); the new INTERNAL-TRIGGERING-POINTS emission keeps the XSD EXTERNAL→INTERNAL relative order.
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-25: touched tests 612 passed (model test_Trigger.py 6 + full SwcInternalBehavior model dir + parser/test_arxml_parser_orchestrators.py 285 + writer/test_writer_swc_behavior.py 196); full suite 11551 passed / 0 failed (`uv run python scripts/run_tests.py --no-coverage`, baseline 11541 + 10 net new; integration round-trip 11/11 included); `uv run ruff check src tests scripts` clean; black clean on all 6 touched Python files (parser import line exploded past 200 chars by black after adding InternalTriggeringPoint — order preserved, not a re-sort; repo-wide black NOT run — unrelated pre-existing failures at HEAD); set-based checklist==methods + coverage audit OK; plain get_type_hints pin audit OK (setter value/return + getter return); verbatim docstring diff audit OK (class Note, constr_1182, attribute Note x3, None-no-op sentence); no-`# type:` / blank-line / member-order / top-level-export (`armodel.InternalTriggeringPoint`) audits OK. 9b deferred to batch confirmation (user instruction 2026-09-24)

- [ ] `ModeAccessPoint` — ARObject — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/ModeDeclarationGroup.py
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `ModeSwitchPoint` — AbstractAccessPoint — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/ModeDeclarationGroup.py
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `AsynchronousServerCallReturnsEvent` — RTEEvent — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/RTEEvents.py
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `DataReceiveErrorEvent` — RTEEvent — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/RTEEvents.py
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `DataReceivedEvent` — RTEEvent — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/RTEEvents.py
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `DataSendCompletedEvent` — RTEEvent — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/RTEEvents.py
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `DataWriteCompletedEvent` — RTEEvent — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/RTEEvents.py
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `InternalTriggerOccurredEvent` — RTEEvent — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/RTEEvents.py
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `OperationInvokedEvent` — RTEEvent — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/RTEEvents.py
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `RteEventInEcuInstanceRef` — AtpInstanceRef — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/__init__.py
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

- [ ] `VariableAccessInEcuInstanceRef` — AtpInstanceRef — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/__init__.py
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
