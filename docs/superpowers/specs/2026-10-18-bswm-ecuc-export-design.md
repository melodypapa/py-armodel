# Design: BswM ECUC export (SWS BSW Mode Manager §10.2 → XLSX)

Date: 2026-10-18 · Status: proposed (design gate) · Branch: `main`

## Problem

The AUTOSAR CP SWS *BSW Mode Manager* document
(`autosar/ECUC/markdown/ModeManagement/AUTOSAR_CP_SWS_BSWModeManager.md`, Document ID 313,
R23-11) carries the complete BswM ECUC configuration specification in Chapter 10.2:
91 container/choice definitions and 135 configuration parameters, described across
structured markdown tables.

Consumers want that configuration as a spreadsheet — one sheet per container, filterable
per parameter — without hand-copying the tables. The existing `os-ecuc-export` CLI reads an
ECUC **ARXML** model, not this markdown, so it cannot be reused directly.

## Goals

1. A **BswM configuration model**, built in the same style as the existing OS model
   (`src/armodel/data_models/ecuc/os.py`): plain classes with camelCase getters/setters that
   return `self`, a root aggregator that holds the containers and offers a `from_file`
   classmethod.
2. A parser that extracts §10.2 into that model. Containers and parameters are **classified
   according to the ECUC metamodel** defined in
   `autosar/R23-11/markdown/AUTOSAR_CP_TPS_ECUConfiguration.md`
   (`EcucModuleDef` / `EcucParamConfContainerDef` / `EcucChoiceContainerDef` /
   `Ecuc*ParamDef` / `Ecuc*ReferenceDef` / `EcucEnumerationLiteralDef` / multiplicity and
   configuration classes).
3. An XLSX exporter, built on `ExcelReporter` like `src/armodel/report/os_export.py`, writing
   **one sheet per container**, ordered with `BswMAction` and `BswMActionList` first, then the
   remaining containers in document order.
4. A console script `bswm-ecuc-export` (INPUT `.md`, OUTPUT `.xlsx`), wired like
   `os-ecuc-export`.

## Non-goals

- Reading or writing ECUC ARXML; the existing `EcucParser` / `OsEcucParser` / `EcucParser`
  base are untouched.
- Instantiating the M2 metamodel classes in
  `models/M2/AUTOSARTemplates/ECUCParameterDefTemplate.py`; the metamodel is the
  classification reference, the model is our own (per "same as current OS").
- Semantic modelling of runtime behaviour: no reference resolution beyond the targets named
  in the tables.
- Publication details (§10.3), diagrams, and images.

## Source facts (measured on the R23-11 document)

- §10.2 body spans lines ~2707–6301; sections are `## 10.2.N <ContainerName>` headings.
- 91 sections = 91 containers; 1 uses `Module Name` (`BswM`, no parent), 4 use
  `Choice Container Name`, 86 use `Container Name`. Heading text equals the declared
  container name for every section.
- 135 parameters; each carries one `Multiplicity`, one `Type`, one
  `Post-Build Variant Value`, and one `Scope / Dependency` row. 59 `Range` rows (repeatable,
  one per enum value), 38 `Default value` rows, 6 `Regular Expression` rows.
  Configuration classes are repeated rows (`Pre-compile time` / `Link time` /
  `Post-build time`).
- 92 included-container entries across the containers' `Included Containers` /
  `Container Choices` tables.
- 4 container names exceed Excel's 31-character sheet-name limit
  (`BswMDcmApplicationUpdatedIndication`, `BswMEthIfSwitchPortGroupRequestMode`,
  `BswMSdConsumedEventGroupModeRequest` at 35; `BswMSdConsumedEventGroupCurrentState` at 36).
  No duplicate names and no invalid sheet characters.

### Parameter `Type` → ECUC metamodel classification

The `Type` column already names ECUC metamodel classes. 47 distinct strings collapse to:

| SWS `Type` string                    | Model kind   | Classification              | Count |
|--------------------------------------|--------------|-----------------------------|-------|
| `EcucBooleanParamDef`                | parameter    | `EcucBooleanParamDef`       | 25    |
| `EcucEnumerationParamDef`            | parameter    | `EcucEnumerationParamDef`   | 20    |
| `EcucStringParamDef`                 | parameter    | `EcucStringParamDef`        | 6     |
| `EcucIntegerParamDef` (+ variant note)| parameter   | `EcucIntegerParamDef`       | 4     |
| `EcucFloatParamDef`                  | parameter    | `EcucFloatParamDef`         | 2     |
| `Reference to X`                     | reference    | `EcucReferenceDef`          |       |
| `Symbolic name reference to X`       | reference    | `EcucSymbolicNameReferenceDef` |    |
| `Choice reference to [ A, B ]`       | reference    | `EcucChoiceReferenceDef`    |       |
| `Foreign reference to X`             | reference    | `EcucForeignReferenceDef`   |       |
| `Instance reference to X context: …` | reference    | `EcucInstanceReferenceDef`  |       |

`X` (and `A`/`B`) become the reference targets; `Range` rows become enumeration literals.
An unrecognised `Type` is kept as a parameter with the raw type string and reported as a
warning rather than dropped.

### Parsing hazards (must be handled)

1. **Merged cells duplicated.** Header/metadata cells repeat across columns (e.g. a
   `Description` value fills columns 2–4). Values are taken as the first non-empty cell
   after the label, not concatenated.
2. **Page-break splits.** `glyph[triangleinv]`, `## glyph[triangle]`, and `![Image](...)`
   lines interrupt tables mid-row-set. Continuation rows may start with an **empty first
   cell** (`| | Link time | X | ... |`) and inherit the previous row's label. They must not
   be dropped (they carry `Link time` / `Post-build time` config classes and split `Range`
   enum rows with descriptions).
3. **Mangled included-container headers.** Three shapes occur: `Included Containers` header
   + `Container Name | Multiplicity | Scope / Dependency`; a single
   `Container Choices Container Name | Multiplicity | ...` header; and `Included Containers`
   with **no** `Container Name` header. Detection accepts any of them.
4. **`No Included Containers`** appears both as a plain text line and as a one-cell table row.
5. **Continuation tables** may repeat only a subset of a parameter's rows, so parameter
   fields accumulate across the whole section rather than reset per table block.

## Design

### 1. BswM configuration model — `src/armodel/data_models/ecuc/bswm.py`

Same style as `os.py`: plain classes, 3.8-compatible `typing` (`Optional`, `List`), field
comments, camelCase getters/setters returning `self`. Re-exported from
`src/armodel/data_models/ecuc/__init__.py`.

- `BswmConfigurationClass` — one configuration-class row:
  `configClass` (`Pre-compile time`/`Link time`/`Post-build time`),
  `configVariant` (e.g. `VARIANT-PRE-COMPILE`), `value` (`X`/`-`).
- `BswmEnumLiteral` — an enumeration literal: `name`, `description`.
- `BswmParameter` — a scalar/enum parameter definition: `name`, `parameterType`
  (ECUC class name), `parent`, `description`, `swsItem`, `lowerMultiplicity`,
  `upperMultiplicity`, `upperMultiplicityInfinite`, `scope`, `postBuildVariantMultiplicity`,
  `postBuildVariantValue`, `multiplicityConfigClasses`, `valueConfigClasses`,
  `ranges: List[BswmEnumLiteral]`, `defaults: List[str]`, `regularExpression`.
- `BswmReference` — a reference definition: `name`, `referenceType`, `targets: List[str]`,
  `parent`, `description`, `swsItem`, `lowerMultiplicity`, `upperMultiplicity`,
  `upperMultiplicityInfinite`, `scope`, `postBuildVariantMultiplicity`, `postBuildVariantValue`,
  `multiplicityConfigClasses`, `valueConfigClasses`.
- `BswmIncludedContainer` — a child entry in an included-containers table: `name`,
  `multiplicity`, `scope`.
- `BswmContainer` — a container definition: `name`, `containerType`
  (`EcucParamConfContainerDef`/`EcucChoiceContainerDef`), `parent`, `description`, `swsItem`,
  `lowerMultiplicity`, `upperMultiplicity`, `upperMultiplicityInfinite`,
  `postBuildVariantMultiplicity`, `multiplicityConfigClasses`, `parameters`,
  `references`, `includedContainers`.
- `BswmModule` — root aggregator: `name`, `postBuildVariantSupport`,
  `supportedConfigVariants: List[str]`, `containers: List[BswmContainer]` (document order);
  `getContainers` / `addBswmContainer` / `getContainer(name)`; and
  `from_file(path)` / `from_markdown(path)` classmethods delegating to the parser (mirroring
  `OsOs.from_file`).

Multiplicity strings (`0..1`, `1`, `1..*`, `n..m`) are parsed into
`lowerMultiplicity` / `upperMultiplicity` / `upperMultiplicityInfinite`, mirroring
`EcucDefinitionElement`.

### 2. Parser — `src/armodel/parser/bswm_ecuc_parser.py`

`BswmEcucParser.load(path) -> BswmModule` (and `parse(text)`); raises
`BswmEcucParseError` (`ValueError`) when the §10.2 chapter is absent.

Algorithm:

1. Read UTF-8; locate the §10.2 body (from the `## 10.2 ` heading to the next `## 10.3 `, or
   EOF); missing heading → `BswmEcucParseError`.
2. Split the body on `^## 10\.2\.(\d+)\s+(.*)$` into one block per container.
3. Per block, take all pipe rows in order; skip separator rows; ignore non-pipe lines; carry
   `last_label` so an empty first cell reuses the previous label.
4. Walk rows with a small state machine, producing a `BswmContainer` plus its parameters,
   references, and included containers:
   - `Module Name`/`Container Name`/`Choice Container Name` → container name + kind;
     `Parent Container`, `Description`, `Post-Build Variant Support`,
     `Supported Config Variants` → container fields; `SWS Item` → stashed.
   - `Parameter Name` → finalise the previous parameter/reference; start a new one seeded
     with the stashed SWS item.
   - `Multiplicity` → parsed bounds; `Type` → kind classification (parameter vs reference and
     ECUC class); `Scope / Dependency` → scope text.
   - `Range` → `BswmEnumLiteral` (appended); `Default value` → appended;
     `Regular Expression` → set.
   - `Post-Build Variant Multiplicity` / `Post-Build Variant Value` → booleans.
   - `Multiplicity Configuration Class` / `Value Configuration Class` → a
     `BswmConfigurationClass` keyed by cell 1.
   - `Configuration Parameters` → ignorable sub-header.
   - Included-container header (cells include `Container Name` and a cell equal to
     `Multiplicity`), or a first cell of `Included Containers` / `Container Choices` → enter
     child mode; `No Included Containers` → none; child rows are `name | multiplicity | scope`.
5. Append containers in document order; the first block (BswM) names the `BswmModule` and
   supplies its post-build support / supported variants.

### 3. Exporter — `src/armodel/report/bswm_export.py`

`BswmConfigXlsxExporter(ExcelReporter)` with `export(module: BswmModule, output_path)`, and a
`BswmConfigExporter` dispatcher mirroring `OsConfigExporter` (XLSX for now; YAML optional and
out of the first cut unless trivial).

- **Sheet order:** `BswMAction`, `BswMActionList` first (in that order), then the remaining
  containers in document order; a missing priority name is skipped.
- **Sheet name:** container name sanitised (strip `\ / ? * [ ] :`, truncate to 31 chars,
  de-duplicate with a numeric suffix).
- **Sheet layout:** rows 1–4 a metadata block (`Container`, `Parent Container`, `SWS Item`,
  `Description`; label col A, value col B, wrapped); row 6 the header row; rows 7+ one row per
  included container (`Kind = Container`) then one per parameter/reference
  (`Kind = Parameter` / `Kind = Reference`), in document order.
- **Columns:** `Kind`, `SWS Item`, `Name`, `Parent Container`, `Multiplicity`, `Type`,
  `Range / Default`, `Post-Build Variant Multiplicity`, `Post-Build Variant Value`,
  `Multiplicity Config Class`, `Value Config Class`, `Scope / Dependency`, `Description`.
  - `Type` = the ECUC class name; for references it includes the target(s).
  - `Range / Default` joins enum literals then defaults (newline-separated).
  - Config-class cells render `Pre-compile time: <variants>; Link time: …; Post-build time: …`.
  - Free-text cells use `Alignment(wrap_text=True)`; `auto_width` per sheet.

### 4. CLI — `src/armodel/cli/bswm_ecuc_export_cli.py`

`main()` mirrors `os_config_export_cli.py`: positional `INPUT` (`.md`) and `OUTPUT`
(`.xlsx`), `-v/--verbose`, guard against overwriting the input, log to
`<output_dir>/bswm_ecuc_export.log`, print a stderr summary. Registered in `pyproject.toml`:

```toml
bswm-ecuc-export = "armodel.cli.bswm_ecuc_export_cli:main"
```

## Testing

Unit tests (small hand-written markdown fixtures):

- `tests/test_armodel/data_models/test_bswm.py` — model accessors: setters return `self`,
  add/get containers, `from_file` delegates to the parser.
- `tests/test_armodel/parser/test_bswm_ecuc_parser.py`
  - metadata: module vs container vs choice container, parent, description, SWS item;
  - merged-cell de-duplication;
  - page-break continuation with empty first cell (config-class row, split `Range` row);
  - `Range`/`Default value` accumulation, `Regular Expression`;
  - Type classification: each of the 10 kinds; multiplicity parsed to lower/upper/infinite;
  - reference targets for `Reference` / `Symbolic name` / `Choice` / `Foreign` / `Instance`;
  - included-container detection for all three header shapes and `No Included Containers`;
  - missing §10.2 → `BswmEcucParseError`.
- `tests/test_armodel/report/test_bswm_export.py`
  - sheet order has `BswMAction`/`BswMActionList` first;
  - metadata block, header row, `Kind`/name/multiplicity cells for a built model;
  - long container name truncated to ≤31 chars; unnamed/empty module still yields a header row.
- Integration over the real document
  (`tests/test_armodel/report/test_bswm_ecuc_export.py`):
  - parser finds 91 containers and 135 parameters; 92 included-container entries;
  - `BswM` has no parent and includes `BswMConfig` + `BswMGeneral`;
  - `BswMAvailableActions` is a choice container whose child count matches the spec table;
  - workbook's first two sheets are `BswMAction`, `BswMActionList`; sheet count equals the
    container count.

Quality gates: `python scripts/run_tests.py` (full suite) and `npm run lint` (ruff + mypy;
new code must be type-clean, 3.8-compatible typing).

## Risks / notes

- Docling output is a one-off artefact of this document; the parser targets the row shapes
  observed here. Unknown labels are ignored rather than fatal, and an unrecognised `Type` is
  kept with a warning. Exact expected counts (91 / 135 / 92) are asserted in the integration
  test as a canary for silent extraction drift.
- Sheet-name truncation cannot collide for the current names, but a de-duplicating suffix is
  used defensively.
- No model-layer or ARXML parser changes, so the model-parity and round-trip suites are
  unaffected.
