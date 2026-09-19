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

All standard AUTOSAR OS R23-11 Chapter 10 fields are first-class model members — including `OsStacksize`, which IS a standard SWS OS `OsTask` parameter and is collected like any other field. Only genuinely vendor-specific parameters (e.g. the fixture's `OsVendorSpecificParam`) are ignored by the strict converter, and the ignored set is explicit in the converter tests.

The model identity member is `name`, exposed through `getName()` and `setName()` (accepted deviation from the M2 `shortName` accessor; see "Accepted Deviations").

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
- `OsStacksize: Optional[int]`
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
OsEcucParser().load(path, document=None, warning=False)
OsEcucParser().parseEcuc(document, warning=False)
```

`load` performs the required AUTOSAR release setup and invokes the existing `ARXMLParser` to construct ECUC model objects, then delegates to `parseEcuc`. `parseEcuc` accepts the already parsed ECUC document and populates standalone OS model classes. With `warning=True`, unresolved standard references are logged as warnings instead of raising conversion errors (the CLI `-w/--warning` flag feeds this). `OsOs.from_file` and `OsOs.from_ecuc` may remain convenience delegates, but conversion ownership belongs to `OsEcucParser`.

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
- `getName()` identity behavior.
- Typed boolean, integer, float, and enumeration conversion.
- Repeated application/task references.
- Bidirectional application/task resolution without duplicate task objects.
- Flattened autostart and timing-protection conversion into `OsTask`.
- Ordered resource-lock budget/reference pairs.
- Collection of the standard `OsStacksize` parameter.
- Ignoring of genuinely vendor-specific parameters (the fixture's `OsVendorSpecificParam`).
- Missing optional values and unresolved references (error mode and `warning=True` mode).
- File entry point delegation through `OsEcucParser`.

## CLI Export

Add a new dedicated CLI command for converting an ECUC ARXML OS configuration into an export file containing the semantic `OsApplication` and `OsTask` data.

The command follows the existing CLI house pattern (`connector2xlsx_cli.py`, `file_list_cli.py`): argparse with `-v/--verbose` and `-w/--warning` store-true flags, positional `INPUT` (`nargs="+"`) and `OUTPUT`, the shared `[%(levelname)s] : %(message)s` logging format with a stderr stream handler plus a `FileHandler` writing `os_config_export.log` next to `OUTPUT`, file handler at DEBUG and stdout at INFO (DEBUG with `--verbose`), the work inside `try/except`, and the `if __name__ == "__main__"` guard.

The command accepts one format selector:

```text
os-config-export [-v] [-w] INPUT... OUTPUT [--format {xlsx,yaml}]
```

`--format` defaults to `xlsx`. The command shall:

1. Parse the input ARXML into the existing ECUC model.
2. Convert the ECUC model into `OsOs` model objects, forwarding `-w/--warning` to `OsEcucParser.load(..., warning=True)`.
3. Export the model objects using the selected format.

The command shall return a non-zero exit status for invalid input, conversion errors (except when downgraded by `--warning`), unsupported formats, or output failures. It shall not silently overwrite the input file. The output extension may be validated against `--format` or generated from the requested format according to the existing CLI conventions.

### YAML Output

YAML shall represent the semantic model structure, including:

- `OsApplication` objects
- `OsTask` objects
- exact AUTOSAR Chapter 10 field names
- `name` as the identity member of each object
- flattened standard fields from the `OsTaskAutostart`, `OsTaskTimingProtection`, and `OsTaskResourceLock` containers
- application/task references represented consistently by `name` values or serialized reference paths, without Python object identity details

### Excel Output

The default XLSX export shall provide separate worksheets for the primary semantic objects and nested repeated structures:

- `OsApplication`
- `OsTask`
- flattened `OsTask` autostart and timing-protection fields

Each worksheet shall use `name` as the object identity column and exact AUTOSAR field names for exported attributes. Repeated references shall be represented in a stable, readable form, preserving their order. The workbook shall be suitable for inspection and downstream spreadsheet processing.

The CLI export layer must consume `OsOs` model objects and must not read ECUC model internals directly.

## Accepted Deviations

These deviations from the general repo conventions are deliberate for the OS collector and must not be "corrected" by later sync or refactoring passes:

1. **PascalCase semantic field names.** OS model members and accessor suffixes keep the verbatim ECUC parameter names (`OsTaskPriority`, `OsAppTaskRef`, ...) instead of the repo's camelCase model-field convention, because the collector's contract is exact Chapter 10 naming.
2. **`name` identity instead of M2 `shortName`.** The standalone OS classes do not inherit from M2 `Identifiable`, so the identity member is `name` with `getName()`/`setName()`; YAML and XLSX exports use `name` as the identity column.
3. **`OsStacksize` is collected.** It is a standard SWS OS `OsTask` parameter, not a vendor extension; the strict mapping includes it. Only genuinely vendor-specific parameters are ignored.
4. **Exporters live in `armodel.report`** (`src/armodel/report/os_export.py`), the repo's home for report/export writers, not under `models`; they are exported through the package `__init__.py` (`from armodel.report import write_xlsx, write_yaml`) exactly like `ConnectorXlsReport`.
5. **`pyyaml` is not a runtime dependency.** `write_yaml` imports it lazily and raises an actionable `ImportError` (`pip install pyyaml`) when absent; pyyaml remains in the `pytest` extra for tests.
6. **The CLI follows the house pattern** (`-v/--verbose`, `-w/--warning`, INPUT/OUTPUT positionals, `[%(levelname)s] : %(message)s` logging with `os_config_export.log` next to the output) rather than a bespoke argparse setup, and `-w` maps to the converter's `warning=True` mode.
7. **The demo fixture joins the integration corpus.** `Os_ECUC.arxml` lives in `tests/integration_tests/test_files/` and is therefore round-trip tested by the integration suite; Task 0 of the implementation plan verifies this stays green.

## Alternatives Considered

### Converter over existing ECUC objects

Recommended. It preserves the generic ECUC parser boundary and makes the output actual OS objects.

### OS-aware ECUC parser

Rejected for the first version because it couples generic ECUC parsing to one module's semantics.

### Intermediate normalized ECUC model

Deferred. It would ease support for both legacy and modern ECUC XML forms but adds scope before the legacy demo is supported.
