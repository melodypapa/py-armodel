# Mypy Baseline Drain — Small Tail (35 modules, ≤5 errors each)

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Drain the 35 smallest modules from the `[[tool.mypy.overrides]]` baseline in `pyproject.toml` (~110 errors), keeping `uv run mypy` green after every commit.

**Architecture:** Each task fixes one error cluster (cast sites, Optional field declarations, misc singles), then deletes exactly that cluster's module lines from the baseline list, then verifies green (`uv run mypy`, targeted pytest, `npm run lint`) and commits. The three giants (`arxml_parser.py` 1143, `arxml_writer.py` 1071, `ARPackage.py` 338) and the 6–10 error middle tier are explicitly OUT of scope — separate plans.

**Tech Stack:** Python 3.8 typing ONLY (`typing.Optional[T]`, `typing.List[T]`, `typing.cast`, `typing.Union`, `typing.Dict`, `typing.Any` — never `T | None`), mypy (uv), pytest (uv), Black 200 chars, npm lint.

---

## Global conventions (apply to every task)

1. **Error inventory source of truth:** `uv run mypy --config-file /tmp/mypy-drain.ini 2>&1 | grep "error:"` (config exists at `/tmp/mypy-drain.ini`; recreate with `printf '[mypy]\nfiles = src/armodel\nignore_missing_imports = True\nwarn_redundant_casts = True\nwarn_unused_ignores = True\n' > /tmp/mypy-drain.ini` if missing). Regenerate this after each task to confirm the fixed modules disappeared.
2. **Baseline edits:** `pyproject.toml` L125+ — one `"armodel....",` line per module inside the single `module = [...]` list. Delete lines with the Edit tool; never reorder the remaining lines.
3. **Module name from file path:** `src/armodel/a/b/X.py` → `armodel.a.b.X`; `src/armodel/a/b/__init__.py` → `armodel.a.b`.
4. **cast imports:** when adding `cast(...)` to a file, extend its existing `from typing import ...` line (do NOT create a second typing import; do NOT re-sort). If the file has no typing import, add `from typing import cast` (plus whatever the fix needs) adjacent to the existing stdlib imports.
5. **Verification per task (in order):**
   - `uv run mypy` → `Success: no issues found in 268 source files`
   - `uv run pytest tests/test_armodel -x -q` → all pass
   - `npm run lint` → `All checks passed!`
   - `uv run black --check <files touched in this task>` → all clean (fix with `uv run black <files>` if not)
6. **Commit format:** `fix(mypy): drain <cluster> from baseline` — one commit per task. Never add AI attribution.
7. **Do NOT touch** `src/armodel/parser/arxml_parser.py`, `src/armodel/writer/arxml_writer.py`, `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/ARPackage.py` (out of scope giants).

## The two fix recipes

**Recipe A — cast on lookup return (error: `Incompatible return value type (got "Referrable | None", expected "X")`):**
wrap the returned expression, `X` = the expected type from the mypy message:

```python
# before
return self.getReferrableElement(short_name, X)
# after
return cast(X, self.getReferrableElement(short_name, X))
```

**Recipe B — Optional field declaration (error: `Incompatible types in assignment (expression has type "None", variable has type "X")` in `__init__`):**
make the declared type Optional; align the getter's return type to `Optional[X]` if it is annotated non-Optional:

```python
# before                          # after
self.offset: TimeValue = None     self.offset: Optional[TimeValue] = None
```

---

### Task 1: Cast cluster — CommonStructure + Timing (6 files, 16 sites)

**Files (all Modify only):**
- `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingCondition.py:380,392,404`
- `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/ExecutionOrderConstraint.py:299,307,315`
- `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ImplementationDataTypes.py:172,326,352`
- `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/FlatMap.py:222`
- `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingExtensions.py:96,108,162`
- `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ModeDeclaration.py:319,328,392`

- [ ] **Step 1: Apply Recipe A** at every line above except `ModeDeclaration.py:328`. Expected types per mypy: TimingCondition → `AutosarOperationArgumentInstance` / `TimingModeInstance` / `AutosarVariableInstance`; ExecutionOrderConstraint → `EOCEventRef` / `EOCExecutableEntityRef` / `EOCExecutableEntityRefGroup`; ImplementationDataTypes → `ImplementationDataTypeElement` (172, 326) / `SymbolProps` (352 — return is `self.symbolProps`, a field, cast the field access); FlatMap → `FlatInstanceDescriptor`; TimingExtensions → `TimingClockSyncAccuracy` / `TimingCondition` / `ExecutionOrderConstraint`; ModeDeclaration → `ModeDeclaration` (319) / `ModeTransition` (392). For each file, add `cast` to the typing import.

- [ ] **Step 2: Fix `ModeDeclaration.py:328`** — replace the `filter(lambda ...)` with an `isinstance`-narrowing generator expression:

```python
# before (L328)
return list(sorted(filter(lambda a: isinstance(a, ModeDeclaration), self.referrableElements), key=lambda o: o.short_name))
# after
return list(sorted((a for a in self.referrableElements if isinstance(a, ModeDeclaration)), key=lambda o: o.short_name))
```

- [ ] **Step 3: Verify** (conventions step 5).
- [ ] **Step 4: Delete baseline lines** for: `armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingCondition`, `...CommonStructure.Timing.TimingConstraint.ExecutionOrderConstraint`, `...CommonStructure.ImplementationDataTypes`, `...CommonStructure.FlatMap`, `...CommonStructure.Timing.TimingExtensions`, `...CommonStructure.ModeDeclaration`. Re-run `uv run mypy` → green.
- [ ] **Step 5: Commit** — `fix(mypy): drain CommonStructure cast sites from baseline`

### Task 2: Cast cluster — SWComponentTemplate (5 files, 12 sites)

**Files:**
- `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/NvBlockComponent.py:176,344,356,368` → `VariableDataPrototype` / `NvBlockNeeds` / `VariableDataPrototype` / `ParameterDataPrototype`
- `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/ImplicitCommunicationBehavior/__init__.py:257,289` → `DataPrototypeGroup`; `:321,353` → `RunnableEntityGroup`
- `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/RPTScenario.py:275` → `DiagnosticParameterElement`
- `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/EndToEndProtection.py:416` → `EndToEndProtection`
- `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Datatype/Datatypes.py:202,227` → `ApplicationArrayElement` / `ApplicationRecordElement`

- [ ] **Step 1: Apply Recipe A** at each site (add `cast` to each file's typing import).
- [ ] **Step 2: Verify** (conventions step 5).
- [ ] **Step 3: Delete baseline lines** for: `armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent`, `...SWComponentTemplate.SwcInternalBehavior.ImplicitCommunicationBehavior`, `...SWComponentTemplate.RPTScenario`, `...SWComponentTemplate.EndToEndProtection`, `...SWComponentTemplate.Datatype.Datatypes`. Re-run `uv run mypy` → green.
- [ ] **Step 4: Commit** — `fix(mypy): drain SWComponentTemplate cast sites from baseline`

### Task 3: Cast cluster — remaining model files (12 files, 22 sites)

**Files (all Recipe A; expected cast type in parentheses):**
- `LogAndTraceExtract.py:139,282` (`DltArgument`), `:573` (`DltApplication`)
- `ECUCDescriptionTemplate.py:464,517` (`EcucContainerValue`), `:1016,1088` (`Container`)
- `SystemTemplate/Fibex/FibexCore/CoreCommunication/__init__.py` — none; skip (9 errors = out of scope)
- `SystemTemplate/Fibex/Fibex4Ethernet/ServiceInstances.py:736` (`ConsumedEventGroup`), `:1556` (`EventHandler`), `:1841` (`ApplicationEndpoint`)
- `SystemTemplate/Transformer/__init__.py:983` (`DataTransformation`), `:996` (`TransformationTechnology`)
- `SystemTemplate/Fibex/Fibex4Ethernet/TcpOptionFilterSet.py:73` (`TcpOptionFilterList`)
- `SystemTemplate/DoIP.py:257` (`DoIpRoutingActivation`)
- `SystemTemplate/DiagnosticConnection.py:58` (`TpConnectionIdent` — return is a field access `self.tpConnectionIdent`, cast it)
- `BswModuleTemplate/BswInterfaces.py:275,387` (`SwServiceArg`)
- `EcuResourceTemplate/HwElementCategory.py:212` (`HwAttributeLiteralDef`), `:291` (`HwAttributeDef`)
- `GenericStructure/ViewMapSet.py:167` (`ViewMap`)
- `CommonStructure/StandardizationTemplate/Keyword.py:111` (`Keyword`)
- `GenericStructure/GeneralTemplateClasses/Identifiable.py:979` (`DiagnosticParameterElement`) — **cast only here; do NOT delete Identifiable's baseline entry in this task** (its L83 attr-defined is fixed in Task 6, which deletes the entry)

- [ ] **Step 1: Apply Recipe A** at each site (add `cast` to each file's typing import).
- [ ] **Step 2: Verify** (conventions step 5).
- [ ] **Step 3: Delete baseline lines** for: `...LogAndTraceExtract`, `...ECUCDescriptionTemplate`, `...SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances`, `...SystemTemplate.Transformer`, `...SystemTemplate.Fibex.Fibex4Ethernet.TcpOptionFilterSet`, `...SystemTemplate.DoIP`, `...SystemTemplate.DiagnosticConnection`, `...BswModuleTemplate.BswInterfaces`, `...EcuResourceTemplate.HwElementCategory`, `...GenericStructure.ViewMapSet`, `...CommonStructure.StandardizationTemplate.Keyword` (11 entries — NOT Identifiable, NOT LinTopology; Identifiable's entry goes in Task 6, LinTopology's in Task 4). Re-run `uv run mypy` → green.
- [ ] **Step 4: Commit** — `fix(mypy): drain remaining model cast sites from baseline`

### Task 4: Optional field declarations + LinTopology cast (4 files)

**Files:**
- `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Lin/LinTopology.py:553` — `self.busIdleTimeoutPeriod: TimeValue = None` → `Optional[TimeValue] = None`; getter `getBusIdleTimeoutPeriod` (L556, currently unannotated) stays unannotated. **Plus Recipe A at L574** (`LinScheduleTable`) — this file's cast site lives in this task so its baseline entry is deleted exactly once, here.
- `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/RTEEvents.py:381,382` — `self.offset` / `self.period: TimeValue = None` → `Optional[TimeValue]`; `:506` — `self.eventSourceRef: RefType = None` → `Optional[RefType]`. Check the three getters (`getOffset`, `getPeriod`, `getEventSourceRef`) — if any is annotated `-> TimeValue` / `-> RefType`, change to `-> Optional[TimeValue]` / `-> Optional[RefType]`.
- `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/EndToEndProtection.py:315` — locate the `endToEndDescription` field declaration (`grep -n "endToEndDescription" <file>`) → `Optional[EndToEndDescription] = None`; align its getter if annotated non-Optional.
- `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/VariantHandling/__init__.py:37` — the RefType-typed field assigned None → `Optional[RefType] = None`; align getter if annotated non-Optional.

- [ ] **Step 1: Apply Recipe B** (add `Optional` to typing imports where missing) and the LinTopology L574 Recipe A cast.
- [ ] **Step 2: Verify** (conventions step 5).
- [ ] **Step 3: Delete baseline lines** for `...Fibex.Fibex4Lin.LinTopology`, `...SWComponentTemplate.SwcInternalBehavior.RTEEvents`, `...GenericStructure.VariantHandling` (3 entries — NOT EndToEndProtection; Task 2 already deleted its entry after fixing L416). Re-run `uv run mypy` → green.
- [ ] **Step 4: Commit** — `fix(mypy): drain Optional field declarations from baseline`

### Task 5: EnvironmentalCondition instance-ref getter/setter pairs (1 file, 4 sites)

`src/armodel/models/M2/AUTOSARTemplates/DiagnosticExtract/EnvironmentalCondition.py:303,312` and `:520,529`. The fields hold instance-ref objects (`ModeInBswModuleDescriptionInstanceRef` / `PModeInSystemInstanceRef`) while the public getter/setter use the `RefType` API — bridge with casts, runtime behavior unchanged:

```python
# L303 (inside getModeIRef, declared -> Optional[RefType])
return cast(Optional[RefType], self.modeIRef)
# L312 (inside setModeIRef, value: Optional[RefType])
self.modeIRef = cast(ModeInBswModuleDescriptionInstanceRef, value)
# L520 / L529 — same two casts with PModeInSystemInstanceRef for the pModeIRef pair
```

- [ ] **Step 1: Apply the four casts** (add `cast` to the typing import).
- [ ] **Step 2: Verify** (conventions step 5; the EnvironmentalCondition parse/write tests live under `tests/test_armodel/models/M2/AUTOSARTemplates/DiagnosticExtract/` — run them explicitly too: `uv run pytest tests/test_armodel/models/M2/AUTOSARTemplates/DiagnosticExtract -x -q`).
- [ ] **Step 3: Delete baseline line** for `...DiagnosticExtract.EnvironmentalCondition`. Re-run `uv run mypy` → green.
- [ ] **Step 4: Commit** — `fix(mypy): drain EnvironmentalCondition instance-ref pairs from baseline`

### Task 6: Misc singles — model files (2 files)

- [ ] **Step 1: `src/armodel/models/M2/MSR/Documentation/TextModel/LanguageDataModel.py:915`** — `Name "SlParagraph" already defined`. Run `grep -n "SlParagraph" <file>`. Delete the redundant earlier import/definition (keep the spec-synced class at L915 and its checklist block; if the earlier hit is an import, delete that import line only after confirming no use sits between it and L915).
- [ ] **Step 2: `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/Identifiable.py:83`** — `full_name` property does `self.parent.full_name + "/" + self.short_name` where `parent: ARObject` lacks `full_name`. Cast to preserve runtime behavior exactly:

```python
return cast(Identifiable, self.parent).full_name + "/" + self.short_name
```

- [ ] **Step 3: Verify** (conventions step 5).
- [ ] **Step 4: Delete baseline lines** for `armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel` and `armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable`. Re-run `uv run mypy` → green.
- [ ] **Step 5: Commit** — `fix(mypy): drain LanguageDataModel and Identifiable from baseline`

### Task 7: Misc singles — non-model files (4 files)

- [ ] **Step 1: `src/armodel/parser/file_parser.py:16`** — `self.file_list = []` → `self.file_list: List[str] = []` (getter at L19 already declares `List[str]`).
- [ ] **Step 2: `src/armodel/models/utils/uuid_mgr.py:29-31`** — `uuid = uuid.getValue()` may be None before dict indexing:

```python
uuid = uuid.getValue()
if uuid is not None and uuid not in self.uuid_object_mappings:
    self.uuid_object_mappings[uuid] = []
```

(L31's `self.uuid_object_mappings[uuid]` sits inside the guarded block → narrowed.)
- [ ] **Step 3: `src/armodel/lib/sw_component.py:15`** — add `from typing import List` to the imports (the `# type: List[...]` comment needs the name; mirrors commit 36bb3155d).
- [ ] **Step 4: `src/armodel/transformer/admin_data.py:34`** — `remove(self, root: AUTOSAR)` incompatible with `AbstractTransformer.remove(self)` (`src/armodel/transformer/abstract.py:9`). First `grep -rn "def remove" src/armodel/transformer/`; if every concrete `remove` takes the AUTOSAR root, change the abstract to `def remove(self, root: AUTOSAR) -> None:` (import `AUTOSAR` under `TYPE_CHECKING` with a string annotation if a circular import would trigger). If concrete signatures differ, instead declare the abstract as `def remove(self, *args, **kwargs) -> None:` and leave concretes untouched.
- [ ] **Step 5: Verify** (conventions step 5; also run `uv run pytest tests/test_armodel/models/utils -x -q` and `uv run pytest tests/test_armodel/transformer -x -q` if those dirs exist).
- [ ] **Step 6: Delete baseline lines** for `armodel.parser.file_parser`, `armodel.models.utils.uuid_mgr`, `armodel.lib.sw_component`, `armodel.transformer.admin_data`. Re-run `uv run mypy` → green.
- [ ] **Step 7: Commit** — `fix(mypy): drain parser/lib/transformer singles from baseline`

### Task 8: PrimitiveTypes value setters + models/__init__ shadowed imports (2 files)

- [ ] **Step 1: `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/PrimitiveTypes.py`** — the three subclass `value` setters (Numerical L202 `val: Optional[Union[int, str]]`, Float L~235, PositiveInteger L~551) are narrower than `ARLiteral.value`'s setter `val: Optional[Any]` (L37). Widen all three setter parameters to `val: Optional[Any]` — bodies unchanged (they already isinstance-check).

```python
# before (each of the three)
def value(self, val: Optional[Union[int, str]]):   # or Optional[float] / Optional[int]
# after
def value(self, val: Optional[Any]):
```

- [ ] **Step 2: `src/armodel/models/__init__.py:201`** — five `Diagnostic*` names are exported by BOTH `...GeneralTemplateClasses.ArObject` and `...GeneralTemplateClasses.ARPackage` wildcards, and mypy sees two distinct `type[...]` objects. Run `grep -rn "class DiagnosticEnableConditionPortMapping\|class DiagnosticParameterElementAccess\|class DiagnosticServiceMappingDiagTarget\|class DiagnosticServiceSwMapping\|class DiagnosticTroubleCodeJ1939" src/armodel/models/`. Delete the stale duplicate definitions from the module that only carries legacy copies (keep the module whose copy matches parser/writer usage — check with `grep -rn "<ClassName>" src/armodel/parser/ src/armodel/writer/ | head`), and if that module's `__all__` re-exported them, ensure the canonical module's wildcard still exposes all five names. **Never re-sort the import lines.**
- [ ] **Step 3: Verify** (conventions step 5; also `uv run python -c "from armodel.models import DiagnosticEnableConditionPortMapping, DiagnosticParameterElementAccess, DiagnosticServiceMappingDiagTarget, DiagnosticServiceSwMapping, DiagnosticTroubleCodeJ1939; print('ok')"`).
- [ ] **Step 4: Delete baseline lines** for `armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes` and `armodel.models`. Re-run `uv run mypy` → green.
- [ ] **Step 5: Commit** — `fix(mypy): drain PrimitiveTypes setters and models re-exports from baseline`

### Task 9: os_export (1 file)

**File:** `src/armodel/report/os_export.py`

- [ ] **Step 1: Optional mapper params** (L135, L151, L188): `def __init__(self, mapper: OsConfigModelMapper = None):` → `mapper: Optional[OsConfigModelMapper] = None` (add `Optional`, `Union`, `Dict` to the typing import as needed).
- [ ] **Step 2: Exporter registry** (L190): annotate the dict so `exporter.export(...)` at L200 type-checks:

```python
self._exporters: Dict[str, Union[OsConfigYamlExporter, OsConfigXlsxExporter]] = {"yaml": OsConfigYamlExporter(mapper), "xlsx": OsConfigXlsxExporter(mapper)}
```

If mypy then rejects `exporter.export(os_os, output_path)` because the two `export()` signatures disagree on `output_path`, widen BOTH `export()` declarations to `output_path: Union[str, os.PathLike]` (and inside them use `os.fspath(output_path)` where a `str` is required). If `OsConfigXlsxExporter` lives in another file, widen it there.
- [ ] **Step 3: L184 `ExcelReporter.save(...)`** arg-type — widen `ExcelReporter.save`'s path parameter to `Union[str, os.PathLike]` the same way (locate with `grep -rn "def save" src/armodel/report/`).
- [ ] **Step 4: Verify** (conventions step 5; plus `uv run pytest tests/test_armodel -x -q -k "os_export or excel"`.
- [ ] **Step 5: Delete baseline line** for `armodel.report.os_export`. Re-run `uv run mypy` → green.
- [ ] **Step 6: Commit** — `fix(mypy): drain os_export from baseline`

### Task 10: Final sweep

- [ ] **Step 1:** Regenerate the full inventory: `uv run mypy --config-file /tmp/mypy-drain.ini 2>&1 | grep "error:" | awk -F: '{print $1}' | sort | uniq -c | sort -rn` — confirm none of the 35 drained modules appear.
- [ ] **Step 2:** `grep -c '"armodel\.' pyproject.toml` → 65 − 35 = 30 remaining baseline lines.
- [ ] **Step 3:** Full gates: `uv run pytest tests/ -q` (unit + integration), `npm run lint`, `npm run black-check`.
- [ ] **Step 4:** Commit any straggler fixes (repeat the owning task's recipe if a fix regressed), else skip.
- [ ] **Step 5:** Report: modules drained, commits, remaining baseline (30 entries — giants + middle tier for follow-up plans).

---

## Self-review

- **Spec coverage:** all 35 tail modules appear in exactly one task's baseline-deletion step — T1:6, T2:5, T3:11, T4:3, T5:1, T6:2, T7:4, T8:2, T9:1 = 35 entries. Cross-task rules: Identifiable cast (L979, T3) but deletion in T6 (L83 fix); EndToEndProtection cast (L416, T2 deletes entry) but L315 Optional field in T4 (no deletion); LinTopology cast (L574) and Optional field (L553) both in T4, deletion in T4. Baseline 65 → 30 remaining.
- **Type consistency:** every cast type equals the "expected" type in the mypy message; all annotations are Python 3.8-compatible `typing.*`.
- **Execution order:** T3 before T6 (Identifiable), T2 before T4 (EndToEndProtection) — deletion rights are single-owner as listed above.
