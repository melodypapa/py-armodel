# OS Application and Task Collector Design

## Goal

Convert parsed ECUC model objects into actual AUTOSAR OS semantic model classes, specifically `OsApplication` and `OsTask`, using the AUTOSAR CP R23-11 OS specification as the source of truth. Store these classes under `src/armodel/models/extended/os` and follow the class conventions used by `src/armodel/models/M2`.

The existing generic ECUC parser remains responsible for reading ARXML. The new conversion layer reads ECUC objects and fills OS model classes. Consumers receive OS-domain objects rather than ECUC container objects.

## Reference Inputs

- `tests/integration_tests/test_files/Os_ECUC.arxml` is the committed OS integration fixture and demo input.
- `data/AUTOSAR_CP_SWS_OS.pdf`, Chapter 10, defines the configuration containers and parameters.
- The demo uses the legacy ECUC structure: `MODULE-CONFIGURATION`, `CONTAINERS`, `CONTAINER`, `PARAMETER-VALUES`, and `REFERENCE-VALUES`.
- The demo contains one `OsApplication` and four `OsTask` containers. Application task membership is expressed by `OsAppTaskRef`; task access is expressed by `OsTaskAccessingApplication`.

## Scope

The first implementation supports the legacy ECUC model represented by `tests/integration_tests/test_files/Os_ECUC.arxml`.

Only standard AUTOSAR OS R23-11 Chapter 10 fields are first-class model members. Vendor-specific fields are ignored by the strict converter. In particular, the demo's `OsStacksize` is not mapped because it is not an R23-11 standard `OsTask` parameter.

The model identity member follows the existing `Identifiable` convention, exposed through `getShortName()` and the inherited `short_name` member.

## Semantic Model Classes

The OS classes follow the existing M2 accessor style without inheriting from M2 classes:

- do not inherit from `Identifiable` or another M2 class
- do not contain a `parent` field
- initialize with no constructor arguments
- use `name` as the identity member
- expose `getName()` and `setName()` for the identity member
- use mutable member fields initialized in `__init__`
- expose `getXxx()` and `setXxx()` methods for scalar members
- have setters return `self` for method chaining
- expose `getXxx()` and `addXxx()` methods for repeated members
- preserve exact AUTOSAR parameter names in the public semantic member and method suffixes
- use `Optional[...]` and `List[...]` annotations compatible with Python 3.8

`OsOs` is the aggregate root and follows the same accessor style.

### `OsApplication`

The class uses the exact Chapter 10 parameter names as public members and accessor suffixes. It is initialized with no arguments and exposes project-style getters, setters, and adders:

- `name: str`
- `OsTrusted: Optional[bool]`
- `OsTrustedApplicationDelayTimingViolationCall: Optional[bool]`
- `OsTrustedApplicationWithProtection: Optional[bool]`
- `OsAppAlarmRef: List[str]`
- `OsAppCounterRef: List[str]`
- `OsAppEcucPartitionRef: Optional[str]`
- `OsAppIsrRef: List[str]`
- `OsAppScheduleTableRef: List[str]`
- `OsAppTaskRef: List[OsTask]`
- `OsMemoryMappingCodeLocationRef: Optional[str]`
- `OsRestartTask: Optional[OsTask]`

The class also holds standard nested semantic members for application hooks and trusted functions, using Chapter 10 names. Application runtime state is represented as an OS semantic value and defaults to `APPLICATION_ACCESSIBLE` when modeled; it is not read from ECUC because the configuration input does not define runtime state.

### `OsTask`

The class uses the exact Chapter 10 parameter names as public members and accessor suffixes. It is initialized with no arguments and exposes project-style getters, setters, and adders:

- `name: str`
- `OsTaskActivation: Optional[int]`
- `OsTaskPeriod: Optional[float]`
- `OsTaskPriority: Optional[int]`
- `OsTaskSchedule: Optional[str]`
- `OsMemoryMappingCodeLocationRef: Optional[str]`
- `OsTaskAccessingApplication: List[OsApplication]`
- `OsTaskEventRef: List[str]`
- `OsTaskResourceRef: List[str]`

The fields from the Chapter 10 `OsTaskAutostart`, `OsTaskTimingProtection`, and `OsTaskResourceLock` containers are flattened into `OsTask`; these are not separate dataclasses. The additional `OsTask` members are:

- `OsTaskAppModeRef: List[str]`
- `OsTaskAllInterruptLockBudget: Optional[float]`
- `OsTaskExecutionBudget: Optional[float]`
- `OsTaskOsInterruptLockBudget: Optional[float]`
- `OsTaskTimeFrame: Optional[float]`
- `OsTaskResourceLockBudget: List[float]`
- `OsTaskResourceLockResourceRef: List[str]`

The two resource-lock lists preserve matching order: item `n` in `OsTaskResourceLockBudget` belongs to item `n` in `OsTaskResourceLockResourceRef`.

Absent optional ECUC values become `None` or empty lists. Repeated references remain ordered lists.

## Conversion API

Provide a semantic OS configuration aggregate class:

```python
class OsOs:
    def __init__(self):
        ...

    def getName(self) -> str:
        ...

    def setName(self, value: str) -> "OsOs":
        ...

    def getOsApplications(self) -> List[OsApplication]:
        ...

    def addOsApplication(self, value: OsApplication) -> "OsOs":
        ...

    def getOsTasks(self) -> List[OsTask]:
        ...

    def addOsTask(self, value: OsTask) -> "OsOs":
        ...
```

The converter exposes two entry points:

```python
OsOs.from_ecuc(document)
OsOs.from_file(path)
```

The primary loader is `armodel.parser.OsEcucParser`:

```python
OsEcucParser().load(path, document=None)
OsEcucParser().parseEcuc(document)
```

`load` performs the required AUTOSAR release setup and invokes the existing `ARXMLParser` to construct ECUC model objects, then delegates to `parseEcuc`. `parseEcuc` accepts the already parsed ECUC document and populates standalone OS model classes. `OsOs.from_file` and `OsOs.from_ecuc` may remain convenience delegates, but conversion ownership belongs to `OsEcucParser`.

## Conversion Flow

1. Locate ECUC module configuration containers whose definition references resolve to `OsApplication` and `OsTask`.
2. Index all relevant ECUC containers by their normalized ECUC value path.
3. Create every `OsTask` model object from its standard parameter and nested-container values.
4. Create every `OsApplication` model object from its standard parameter, reference, and nested-container values.
5. Resolve application/task references to the corresponding model objects. Preserve references to OS classes outside this scope as normalized ECUC paths in the exact model fields.
6. Reconcile application/task membership from both `OsAppTaskRef` and `OsTaskAccessingApplication` without duplicating objects.
7. Resolve `OsRestartTask` to the task identity while retaining the declared reference value.
8. Return `OsOs` containing actual semantic model objects.

Unresolved standard references are reported as conversion errors or warnings according to the converter policy; the converter must not silently fabricate OS objects.

## Relationship Rules

- `OsApplication.OsAppTaskRef` is the configured membership list.
- `OsTask.OsTaskAccessingApplication` is the configured access list and may contain multiple applications.
- The demo's application ownership relationship is represented by both sides and must produce one shared `OsTask` instance per task.
- Missing `OsAppEcucPartitionRef` remains `None`; no core is inferred from application or task names.
- No relationship is inferred from container short-name substrings.

## Error Handling

- Missing optional parameters are accepted.
- Missing required values are represented according to the project's parser/converter error policy.
- Invalid typed values are rejected rather than silently coerced.
- References to non-existent ECUC containers are surfaced as unresolved-reference diagnostics.
- Vendor-specific ECUC parameters are ignored by the strict standard mapper.

## Testing

Tests will use `tests/integration_tests/test_files/Os_ECUC.arxml` as the integration reference and focused in-memory ECUC fixtures for edge cases.

Required coverage includes:

- Conversion of `OsApplication_QM` into `OsApplication`.
- Conversion of all four demo tasks into `OsTask`.
- Exact Chapter 10 parameter names and model member names.
- Existing `getShortName()` identity behavior.
- Typed boolean, integer, float, and enumeration conversion.
- Repeated application/task references.
- Bidirectional application/task resolution without duplicate task objects.
- Flattened autostart and timing-protection conversion into `OsTask`.
- Ordered resource-lock budget/reference pairs.
- Omission of vendor-only `OsStacksize` from the strict semantic mapping.
- Missing optional values and unresolved references.
- File entry point delegation through `OsEcucParser`.

## CLI Export

Add a new dedicated CLI command for converting an ECUC ARXML OS configuration into an export file containing the semantic `OsApplication` and `OsTask` data.

The command accepts one format selector:

```text
os-config-export INPUT OUTPUT [--format {xlsx,yaml}]
```

`--format` defaults to `xlsx`. The command shall:

1. Parse the input ARXML into the existing ECUC model.
2. Convert the ECUC model into `OsOs` model objects.
3. Export the model objects using the selected format.

The command shall return a non-zero exit status for invalid input, conversion errors, unsupported formats, or output failures. It shall not silently overwrite the input file. The output extension may be validated against `--format` or generated from the requested format according to the existing CLI conventions.

### YAML Output

YAML shall represent the semantic model structure, including:

- `OsApplication` objects
- `OsTask` objects
- exact AUTOSAR Chapter 10 field names
- `ShortName`
- flattened standard fields from the `OsTaskAutostart`, `OsTaskTimingProtection`, and `OsTaskResourceLock` containers
- application/task references represented consistently by `ShortName` or serialized reference paths, without Python object identity details

### Excel Output

The default XLSX export shall provide separate worksheets for the primary semantic objects and nested repeated structures:

- `OsApplication`
- `OsTask`
- flattened `OsTask` autostart and timing-protection fields

Each worksheet shall use `ShortName` as the object identity column and exact AUTOSAR field names for exported attributes. Repeated references shall be represented in a stable, readable form, preserving their order. The workbook shall be suitable for inspection and downstream spreadsheet processing.

The CLI export layer must consume `OsOs` model objects and must not read ECUC model internals directly.

## Alternatives Considered

### Converter over existing ECUC objects

Recommended. It preserves the generic ECUC parser boundary and makes the output actual OS objects.

### OS-aware ECUC parser

Rejected for the first version because it couples generic ECUC parsing to one module's semantics.

### Intermediate normalized ECUC model

Deferred. It would ease support for both legacy and modern ECUC XML forms but adds scope before the legacy demo is supported.
