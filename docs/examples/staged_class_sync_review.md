# Staged Class Sync Review — Manual Confirmation Sheet

- **Date:** 2026-08-21
- **Scope:** all changes currently staged vs `HEAD` (sync-autosar-class staged-mode pass)
- **Verification state:** 6722 unit tests PASS, integration round-trip PASS, flake8 clean
  (`black-check` flags only a pre-existing file `BswModuleTemplate/BswBehavior/__init__.py` from an earlier commit, untouched here)

## 1. Model classes — summary

| # | Class | File | Spec | Kind of change | `# Spec verified` |
|---|-------|------|------|----------------|-------------------|
| 1 | ApplicationArrayDataType | Datatypes.py | CP_SwCompTemplate, Table 5.8, p.252 | Full sync | **NOT stamped** |
| 2 | ArraySizeHandlingEnum *(new)* | Datatypes.py | CP_SwCompTemplate, Table 5.11, p.253 | New AREnum | **NOT stamped** |
| 3 | ApplicationArrayElement | DataPrototypes.py | CP_SwCompTemplate, Table 5.9, p.252 | Full sync + new attr | **NOT stamped** |
| 4 | ArraySizeSemanticsEnum | ImplementationDataTypes.py | CP_SwCompTemplate, Table 5.10, p.253 | Literal-value fix | **NOT stamped** |
| 5 | SectionInitializationPolicyType *(new)* | PrimitiveTypes.py | CP_SwCompTemplate, Table 5.93, p.417 | New AREnum | R23-11 |
| 6 | SwAddrMethod | AuxillaryObjects.py | CP_SwCompTemplate, Table 5.92, p.414 | Retyped accessors | R23-11 |
| 7 | MemoryAllocationKeywordPolicyType *(new)* | AuxillaryObjects.py | CP_SwCompTemplate, Table 5.95, p.418 | New AREnum | R23-11 |
| 8 | MemorySectionType *(new)* | AuxillaryObjects.py | CP_SwCompTemplate, Table 5.94, p.418 | New AREnum | R23-11 |
| 9 | SwServiceArg | ServiceProcessTask.py | CP_BSWModuleDesc, Table 4.6, p.38 | Full sync | **NOT stamped** |
| 10 | VariationPointProxy | VariantHandling.py | CP_SwCompTemplate, Table 7.61, p.613 | Full sync + new reader/writer | **NOT stamped** (deviation) |

## 2. Model classes — details

### 2.1 ApplicationArrayDataType — [Datatypes.py](../../src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Datatype/Datatypes.py)
- Spec verbatim docstrings (class Note, member comments, getter/setter) from Table 5.8.
- PEP 526 annotated members: `dynamicArraySizeProfile: Optional[String]`, `element: Optional[ApplicationArrayElement]`.
- **Accessor rename:** `getElement()` → `getApplicationArrayElement()` — the old name collided with the `ARObject` element-registry `getElement(short_name, type)`; rename documented in the docstring.
- `createApplicationArrayElement` keeps duplicate-returns-existing semantics.
- 5-column checklist all `[x]` (reader via `readApplicationArrayDataType`, writer via `writeApplicationArrayDataType`).
- Round-trip test asserts `dynamicArraySizeProfile` + all 4 element attributes.
- **Stamp withheld** per user decision (Step 9b not confirmed).

### 2.2 ArraySizeHandlingEnum (new) — [Datatypes.py](../../src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Datatype/Datatypes.py)
- Literals per Table 5.11: `allIndicesDifferentArraySize` (0), `allIndicesSameArraySize` (1), `inheritedFromArrayElementTypeSize` (2).
- No own XML element — serialized as value on `ApplicationArrayElement.arraySizeHandling`, `ImplementationDataTypeElement.arraySizeHandling`.
- Checklist `(no methods)`, all `[x]`. **Not stamped.**

### 2.3 ApplicationArrayElement — [DataPrototypes.py](../../src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Datatype/DataPrototypes.py)
- Spec verbatim docstrings + typed annotations per Table 5.9.
- **New attribute:** `indexDataTypeRef: Optional[RefType]` with `get/setIndexDataTypeRef` — was missing entirely (ref to ApplicationPrimitiveDataType for TEXTTABLE CompuMethod).
- Reader/writer coverage added: `INDEX-DATA-TYPE-REF` (parser `readApplicationArrayElement`, writer `setApplicationArrayElement`).
- Checklist all `[x]`. **Not stamped.**

### 2.4 ArraySizeSemanticsEnum — [ImplementationDataTypes.py](../../src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ImplementationDataTypes.py)
- **Literal fix (breaking):** `FIXED_SIZE` `"fixed-size"` → `"fixedSize"`, `VARIABLE_SIZE` `"variable-size"` → `"variableSize"` to match spec Table 5.10.
- Spec Note docstring replaced the paraphrase; checklist upgraded to 5-column, all `[x]`.
- All consuming tests updated (`ImplementationDataTypeElement`, `SwTextProps`, `ApplicationArrayElement` round-trips). **Not stamped.**

### 2.5 SectionInitializationPolicyType (new) — [PrimitiveTypes.py](../../src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/PrimitiveTypes.py)
- AREnum per Table 5.93: `INIT`, `CLEARED`, `POWER-ON-CLEARED` with spec descriptions.
- Consumed by `SwAddrMethod.sectionInitializationPolicy`. **Stamped R23-11.**

### 2.6 SwAddrMethod — [AuxillaryObjects.py](../../src/armodel/models/M2/MSR/DataDictionary/AuxillaryObjects.py)
- Accessors retyped from loose `ARLiteral` to spec enums per Table 5.92:
  - `memoryAllocationKeywordPolicy` → `MemoryAllocationKeywordPolicyType`
  - `sectionInitializationPolicy` → `SectionInitializationPolicyType`
  - `sectionType` → `MemorySectionType`
  - `options` → `List[Identifier]` (typed list, addOption appends)
- Reader/writer updated to convert literal ↔ enum. **Stamped R23-11.**

### 2.7 / 2.8 MemoryAllocationKeywordPolicyType, MemorySectionType (new) — [AuxillaryObjects.py](../../src/armodel/models/M2/MSR/DataDictionary/AuxillaryObjects.py)
- New AREnums per Tables 5.95 / 5.94 with spec Notes and literal comments. **Stamped R23-11.**

### 2.9 SwServiceArg — [ServiceProcessTask.py](../../src/armodel/models/M2/MSR/DataDictionary/ServiceProcessTask.py)
- Full sync per BSW Module Description Template Table 4.6: spec verbatim docstrings, typed annotations (`direction: Optional[ArgumentDirectionEnum]`, `swArraysize: Optional[ValueList]`, `swDataDefProps: Optional[SwDataDefProps]`), member order per `xml.sequenceOffset` 10/20/30.
- **Reader/writer gap fixed:** `SW-ARRAYSIZE` now read (`readSwServiceArg`) and written (`setSwServiceArg`).
- Round-trip test asserts direction, swArraysize.v, swDataDefProps.swImplPolicy. Checklist all `[x]`. **Not stamped** (Step 9b not confirmed).

### 2.10 VariationPointProxy — [VariantHandling.py](../../src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/VariantHandling.py)
- Full docstring/checklist sync per Table 7.61 (p.613).
- **New reader/writer** (did not exist before): `readVariationPointProxy`, `readSwcInternalBehaviorVariationPointProxies` (parser), `writeVariationPointProxy`, `writeSwcInternalBehaviorVariationPointProxies` (writer); `writeConditionByFormula` gained a `key` parameter (reused for `CONDITION-ACCESS`).
- **Deviation (unstamped):** `valueAccess` spec type is abstract `AttributeValueVariationPoint`, not yet implemented — carried as `ARObject` placeholder; reader calls `notImplemented` on `VALUE-ACCESS`. Checklist honestly shows `[ ]` for valueAccess reader/writer.

### 2.11 Supporting touch-ups (same staged files)
- `DataPrototype`, `AutosarDataPrototype`, `ParameterDataPrototype` (DataPrototypes.py): signatures typed (`getSwDataDefProps`, `getTypeTRef`, `getInitValue` chains), docstrings refreshed — all three remain stamped.
- `ApplicationCompositeElementDataPrototype`, `ApplicationRecordElement`: docstring/comment refresh only.
- `writeApplicationCompositeElementDataPrototype` now uses `prototype.getTypeTRef()` instead of direct attribute access.

## 3. Parser (reader) changes — [arxml_parser.py](../../src/armodel/parser/arxml_parser.py)
- New: `readVariationPointProxy`, `readSwcInternalBehaviorVariationPointProxies` (+ hook into `readSwcInternalBehavior`).
- `readSwServiceArg`: + `SW-ARRAYSIZE`.
- `readApplicationArrayElement`: + `INDEX-DATA-TYPE-REF`.
- `readSwAddrMethod`: enum conversion for `MEMORY-ALLOCATION-KEYWORD-POLICY`, `SECTION-INITIALIZATION-POLICY`, `SECTION-TYPE`.
- Imports: `SectionInitializationPolicyType`, `VariationPointProxy`, `MemoryAllocationKeywordPolicyType`, `MemorySectionType`.

## 4. Writer changes — [arxml_writer.py](../../src/armodel/writer/arxml_writer.py)
- New: `writeVariationPointProxy`, `writeSwcInternalBehaviorVariationPointProxies` (+ hook).
- `writeConditionByFormula`: configurable element key (`CONDITION-ACCESS` reuse).
- `setSwServiceArg`: + `SW-ARRAYSIZE`.
- `setApplicationArrayElement`: + `INDEX-DATA-TYPE-REF`.
- `writeApplicationArrayDataType`: uses `getApplicationArrayElement()`.
- `writeApplicationCompositeElementDataPrototype`: `getTypeTRef()` accessor.

## 5. Test changes (11 files)

| File | New/changed tests |
|------|-------------------|
| test_ImplementationDataTypes.py | ArraySizeSemanticsEnum literal assertions (`fixedSize`/`variableSize`) |
| test_PrimitiveTypes.py | + `TestSectionInitializationPolicyType` |
| test_DataPrototypes.py | Typed-accessor tests (DataPrototype/AutosarDataPrototype/ParameterDataPrototype) |
| test_Datatypes.py | `TestApplicationArrayDataType` — `getApplicationArrayElement()`; `TestDataTypeMappingSet` |
| test_AuxillaryObjects.py | Enum-typed SwAddrMethod accessors + both new enums (+122 lines) |
| test_ServiceProcessTask.py | `TestSwServiceArg` incl. `swArraysize` set/get + None no-op |
| test_writer_bsw_module.py | + `TestSwServiceArgRoundTrip` (field-value assertions) |
| test_writer_data_types.py | + `TestApplicationArrayElementRoundTrip` (all attrs incl. `dynamicArraySizeProfile`, `INDEX-DATA-TYPE-REF` dest/value) |
| test_writer_sw_data_def_props.py | + `TestDataPrototypeSwDataDefPropsRoundTrip` (shared-parameter, with/without props) |
| test_writer_sw_text_props.py | `fixedSize` literal round-trip assertion |
| test_writer_variation_point.py | + `TestVariationPointProxyRoundTrip` (with/without proxy) |

## 6. Docs
- `docs/examples/method_deviation_by_class.md` — deviation report refresh (2 lines).

## 7. Manual confirmation checklist

| # | Class / area | Confirm |
|---|--------------|---------|
| 1 | ApplicationArrayDataType (incl. accessor rename) | ☐ |
| 2 | ArraySizeHandlingEnum | ☐ |
| 3 | ApplicationArrayElement (incl. new indexDataTypeRef) | ☐ |
| 4 | ArraySizeSemanticsEnum literal fix | ☐ |
| 5 | SectionInitializationPolicyType | ☐ |
| 6 | SwAddrMethod retyping | ☐ |
| 7 | MemoryAllocationKeywordPolicyType | ☐ |
| 8 | MemorySectionType | ☐ |
| 9 | SwServiceArg (+SW-ARRAYSIZE reader/writer) | ☐ |
| 10 | VariationPointProxy (valueAccess deviation accepted) | ☐ |
| 11 | Parser changes (§3) | ☐ |
| 12 | Writer changes (§4) | ☐ |
| 13 | Test changes (§5) | ☐ |
