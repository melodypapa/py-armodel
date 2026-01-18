# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

py-armodel is a Python library for parsing, manipulating, and writing AUTOSAR XML (ARXML) files. It follows the AUTOSAR standard specifications and supports versions from 4.0.3 to R24-11, with particular focus on CP R23-11 standard compliance.

**Current Version**: 1.9.0
**Python Requirements**: >= 3.5 (CI tests on 3.8-3.12)
**License**: MIT
**Repository**: http://github.com/melodypapa/py-armodel

## Critical Architecture Concepts

### M2 Schema Structure
The codebase is organized according to the AUTOSAR M2 meta-model:
- `src/armodel/models/M2/MSR/` - Meta-model semantic rules (AsamHdo, DataDictionary, Documentation, CalibrationData)
- `src/armodel/models/M2/AUTOSARTemplates/` - AUTOSAR template models organized by domain

**Wildcard Import Pattern:**
- All model classes use wildcard imports in `__init__.py` files (e.g., `from .my_class import *`)
- When adding new model classes, ensure they are exported from the appropriate `__init__.py`
- This allows imports like `from armodel.models.M2.AUTOSARTemplates import SwcInternalBehavior`
- Each module's `__init__.py` re-exports all classes from its submodules for convenience

### AUTOSAR Singleton Pattern
`AUTOSAR` class uses singleton pattern:
- `AUTOSAR.getInstance()` - Get/create the singleton instance
- `AUTOSAR.new()` - Clear and create fresh instance
- `AUTOSAR.setARRelease(version)` - MUST be called before parsing/writing to select correct XML schema

### Parent-Child Object Graph
AUTOSAR model objects maintain bi-directional references:
- Every object has a `parent` attribute pointing to its container
- Parents hold collections of children
- ARPackage hierarchy is the primary containment structure
- When manipulating models, maintain parent-child relationships carefully

### Element Naming
- AUTOSAR elements use "short name" as primary identifier (not Python's `__name__`)
- Short names must be unique within their containing package/context
- Use `findXXX()` methods for lookups by short name; they return `None` if not found (not exceptions)
- Same short name can exist in different packages or with different types

## Module Organization

- **models/** - AUTOSAR data model classes following M2 schema structure
  - M2/MSR/ - Meta-model semantic rules (AsamHdo, DataDictionary, Documentation, CalibrationData)
  - M2/AUTOSARTemplates/ - AUTOSAR template models by domain
    - AutosarTopLevelStructure - AUTOSAR singleton
    - CommonStructure - ARObject, Referrable, Identifiable, ServiceNeeds, Implementation, InternalBehavior, ResourceConsumption
    - SWComponentTemplate - Component types, port interfaces, datatypes, behavior, implementation
    - SystemTemplate - System signals, ECU instances, communication (Fibex for CAN/Ethernet/FlexRay/LIN)
    - BswModuleTemplate - BSW module descriptions, behavior, implementation, interfaces
    - ECUCDescriptionTemplate - ECUC configuration values
    - EcuResourceTemplate - ECU resources
    - GenericStructure - Generic template classes
  - utils/ - UUID management utilities

- **parser/** - ARXML parsing
  - arxml_parser.py - Main ARXML parser
  - abstract_arxml_parser.py - Abstract base parser
  - connector_xlsx_parser.py - Excel connector parsing
  - excel_parser.py - Generic Excel parsing

- **writer/** - ARXML writing
  - arxml_writer.py - Main ARXML writer
  - abstract_arxml_writer.py - Abstract base writer

- **cli/** - Command-line interface tools
  - arxml_dump_cli.py - Dump ARXML data
  - arxml_format_cli.py - Format ARXML files
  - connector2xlsx_cli.py - Export connectors to Excel
  - connector_update_cli.py - Update connectors from Excel
  - swc_list_cli.py - List software components
  - system_signal_cli.py - List system signals
  - memory_section_cli.py - Memory section operations
  - file_list_cli.py - File listing
  - uuid_checker_cli.py - UUID validation
  - format_xml_cli.py - XML formatting

- **lib/** - Library utilities
  - cli_args_parser.py - CLI argument parsing
  - sw_component.py - Software component utilities
  - system_signal.py - System signal utilities

- **transformer/** - Data transformation
- **report/** - Report generation

### Source Layout
- Source code in `src/armodel/` directory (src layout)
- Install in development mode with: `pip install -e .`
- All imports are absolute: `from armodel.models import AUTOSAR`

## Development Commands

### Testing
- `pytest` - Run all tests
- `pytest --cov=armodel --cov-report term-missing` - Run with coverage
- `pytest tests/test_armodel/parser/test_arxml_parser.py` - Run specific test file
- `pytest tests/test_armodel/parser/test_arxml_parser.py::TestClass::test_method` - Run specific test method
- `pytest -v` - Verbose output
- `pytest -s` - Show print output

Or using npm scripts:
- `npm run pytest` - Run all tests
- `npm run pytest-cov` - Run tests with coverage

### Linting
- `npm run flake8` - Run syntax checks (E9, F63, F7, F82)
- CI also runs complexity checks: `--max-complexity=10 --max-line-length=127`
- Project uses 79-character line length (per PEP 8), not 127 (127 is just for CI warnings)

### Building
- `python setup.py bdist_wheel` - Create wheel distribution
- `python setup.py sdist bdist_wheel --universal` - Create source and wheel
- `twine check dist/*` - Check distribution
- `twine upload dist/*` - Upload to PyPI

### Installation
- `pip install -e .` - Install in editable mode for development

### Documentation
- `cd docs && make html` - Build with Sphinx
- `mkdocs build` or `mkdocs serve` - Build with MkDocs

## CLI Tools (console_scripts)

- `arxml-dump` - Dump ARXML data to screen
- `arxml-format` - Format ARXML files
- `armodel-component` - List SWComponentType
- `connector2xlsx` - Export SwConnector to Excel
- `connector-update` - Update SwConnector from Excel
- `armodel-system-signal` - List system signals
- `armodel-memory-section` - Memory section operations
- `armodel-file-list` - List files
- `armodel-uuid-checker` - UUID validation
- `format-xml` - XML formatting

## Important Implementation Details

### Abstract Base Classes
Many AUTOSAR classes use ABC metaclasses and raise TypeError if directly instantiated. Always check if a class is abstract before attempting to instantiate it (e.g., ARObject, AtpType, Identifiable).

### Parser Options
ARXMLParser accepts an `options` dict parameter:
- `{"warning": True}` - Enables warning mode instead of raising exceptions
- Parser uses lxml for XML processing and resolves namespace prefixes automatically

### Writer Pattern
ARXMLWriter serializes the AUTOSAR model back to ARXML format, respecting the AUTOSAR version set via `setARRelease()` for schema compliance. Writer preserves UUIDs, timestamps, and other metadata.

### Type Annotations
- Use Python 3.10+ union syntax: `str | None` instead of `Optional[str]`
- Use forward references with string literals for circular dependencies: `List["MyClass"]`
- Only reference classes that exist in the codebase to avoid F821 flake8 errors
- Add proper imports for existing types or remove annotations for non-existent types

### Test Structure
- Test folder structure mirrors source structure: `tests/test_armodel/` mirrors `src/armodel/`
- Test file per source file convention: e.g., `test_arxml_parser.py` for `arxml_parser.py`
- Test classes: `Test<ClassName>` for model classes
- Test methods: `test_<method_name>_<scenario>` or `test_<scenario>`
- Use `pytest.raises(ValueError, match="pattern")` for exception testing

## Coding Standards

The project follows comprehensive coding standards documented in `docs/development/coding_rules.md`. Key coding rule categories include:

### Code Layout (CODING_RULE_LAYOUT_00001 - CODING_RULE_LAYOUT_00007)
- Indentation, maximum line length, line breaking, binary operator placement
- Blank lines, source file encoding, string quotes

### Import Organization (CODING_RULE_IMPORT_00001 - CODING_RULE_IMPORT_00003)
- Import order, section separation, alphabetical ordering

### Naming Conventions (CODING_RULE_NAMING_00001 - CODING_RULE_NAMING_00005)
- Class names, function/method names, constant names
- Private attribute names, instance variable names

### Type Annotations (CODING_RULE_TYPE_00001 - CODING_RULE_TYPE_00005)
- Mandatory type annotations, union types, collection types
- Forward references, dataclass field types

### Documentation (CODING_RULE_DOC_00001 - CODING_RULE_DOC_00005)
- Google-style docstrings, class/method docstrings
- Requirements section, docstring language

### Whitespace (CODING_RULE_WS_00001 - CODING_RULE_WS_00006)
- Extraneous whitespace, operator spacing
- Keyword arguments, function annotations, trailing whitespace
- Compound statements

### Style Guidelines (CODING_RULE_STYLE_00001 - CODING_RULE_STYLE_00008)
- Dataclass usage, validation in `__post_init__`
- Regular expressions, context managers, string methods
- List comprehensions, dunder methods, **Python package structure**

### Error Handling (CODING_RULE_ERROR_00001 - CODING_RULE_ERROR_00004)
- Validation errors, immediate validation
- Exception chaining, import validation

### Testing (CODING_RULE_TEST_00001 - CODING_RULE_TEST_00003)
- Test structure, coverage goals, test patterns

### Logging (CODING_RULE_LOG_00001 - CODING_RULE_LOG_00003)
- Logging levels, configuration, CLI error handling

### Best Practices (CODING_RULE_BP_00001 - CODING_RULE_BP_00002)
- Query methods, path operations

### Programming Recommendations (CODING_RULE_PR_00001 - CODING_RULE_PR_00010)
- Type comparisons, sequence checks, string prefix/suffix checks
- None comparisons, boolean comparisons, exception handling
- Resource management, return statement consistency
- Use `def` instead of lambda assignment, exception classes

**Important:** When creating new classes or modules, always follow CODING_RULE_STYLE_00008 for package structure:
- **Leaf packages** (no subdirectories): Classes defined in `.py` file with package name = filename
- **Non-leaf packages** (have subdirectories): Classes defined in `__init__.py` of the directory

## Key Supported Elements

### Component Types
ApplicationSwComponentType, CompositionSwComponentType, SensorActuatorSwComponentType, ServiceSwComponentType, ComplexDeviceDriverSwComponentType, EcuAbstractionSwComponentType, ServiceProxySwComponentType, NvBlockSwComponentType

### Port Interfaces
SenderReceiverInterface, ClientServerInterface, ModeSwitchInterface, ParameterInterface, NvDataInterface, TriggerInterface, ServiceInterface, Diagnostic*Interface

### Data Types
ApplicationDataType, ImplementationDataType, ApplicationRecordElement, ApplicationArrayElement, CompuMethod, DataConstr, Unit, BaseTypes
- Additional: UnitGroup, SwTextProps, SwSystemconst

### Communication
AssemblySwConnector, DelegationSwConnector, ServerComSpec, ModeSwitchReceiverComSpec, NvProvideComSpec, NvRequireComSpec
- CAN: CAN-FRAME, CAN-COMMUNICATION-CONNECTOR, CAN-CONTROLLER
- LIN: LIN-CLUSTER, LIN-UNCONDITIONAL-FRAME, LIN-MASTER
- FlexRay: FLEXRAY-CLUSTER, FLEXRAY-COMMUNICATION-CONNECTOR, FLEXRAY-FRAME
- Ethernet: ETHERNET-COMMUNICATION-CONNECTOR, ETHERNET-PHYSICAL-CHANNEL, SO-AD-CONFIG
- Network Management: NM-CONFIG, NM-NODE, NM-CLUSTER, CAN-NM-MODE, UDP-NM-CLUSTER
- End-to-End Protection: EndToEndProtectionSet, EndToEndProtection

### Behavior
RunnableEntity, SwcInternalBehavior, BswInternalBehavior, SwcImplementation, BswImplementation
- Events: InitEvent, DataReceiveEvent, SwcModeSwitchEvent, BswBackgroundEvent, BswDataReceivedEvent, BswExternalTriggerOccurredEvent, BswModeSwitchedAckEvent, BswOperationInvokedEvent, BswAsynchronousServerCallReturnsEvent

### CommonStructure
ARObject, Referrable, Identifiable, ServiceNeeds (Diagnostic, Communication, etc.), Implementation, InternalBehavior, ResourceConsumption (MemorySection, StackUsage, HeapUsage, ExecutionTime), ModeDeclaration, SwcBswMapping
- Documentation: Documentation (DocumentationOnM1)
- Variant Handling: VariationPoint, PostBuildVariantCriterion, PostBuildVariantCriterionValue, PredefinedVariant, SwSystemconstantValueSet, NumericalValueVariationPoint

### Diagnostics
DiagnosticConnection, DiagnosticServiceTable, DiagnosticEventNeeds, DCM Needs, DoIP (DoIpServiceNeeds, DoIpConfiguration)
- Additional: MlFormula (MathML formulas)

### System
SystemSignal, SystemSignalGroup, SWC-TO-ECU-MAPPING, SW-MAPPINGS, ECU-INSTANCE, ROOT-SOFTWARE-COMPOSITIONS, DataMapping, NetworkManagement, SecureCommunication

### BSW Modules
BswModuleDescription, BswBehavior (BswInternalBehavior, BswModuleEntity, BswCalledEntity, BswSchedulableEntity, BswInterruptEntity), BswImplementation, BswInterfaces (BswModuleEntry, BswModuleClientServerEntry, BswModuleDependency), BSW Events, BSW Call Points (BswDirectCallPoint, BswSynchronousServerCallPoint, BswAsynchronousServerCallPoint, BswAsynchronousServerCallResultPoint)

### ECUC Configuration
EcucValueCollection, EcucModuleConfigurationValues, EcucContainerValue, EcucParameterValue, EcucModuleDef, EcucParamDef (Boolean, String, Integer, Float, Enumeration)
- Additional: EcucAddInfoParamDef, EcucConditionFormula, EcucDefinitionCollection, EcucDestinationUriDef, EcucDestinationUriDefSet, EcucDestinationUriPolicy, EcucLinkerSymbolDef, EcucMultilineStringParamDef, EcucParameterDerivationFormula, EcucQuery, EcucQueryExpression

### Fibex (Field Bus Exchange Format)
Fibex4Can, Fibex4Ethernet, Fibex4Flexray, Fibex4Lin, FibexCore, Fibex4Multiplatform

## Testing Structure

Tests in `tests/test_armodel/` mirror the source structure. Sample ARXML files in `test_files/` include AUTOSAR_Datatypes.arxml, SoftwareComponents.arxml, BswM_Bswmd.arxml organized by AUTOSAR modules.

## Dependencies

**Runtime:** colorama, openpyxl, lxml
**Development:** pytest, pytest-cov, flake8, sphinx

## Key AUTOSAR API Methods

### AUTOSAR Singleton
- `AUTOSAR.getInstance()` - Get singleton instance
- `AUTOSAR.new()` - Clear and create new instance
- `AUTOSAR.setARRelease(version)` - Set AUTOSAR release version (determines XML schema)
- `getAtomicSwComponentTypes()` - Get all atomic software component types
- `getCompositionSwComponentTypes()` - Get all composition software component types
- `getSystemSignals()` - Get all system signals
- `findAtomicSwComponentType(short_name)` - Find specific atomic component
- `findSystemSignal(short_name)` - Find specific system signal
- `findPort(short_name)` - Find specific port
- `findVariableDataPrototype(short_name)` - Find specific data prototype
- `findImplementationDataType(short_name)` - Find specific implementation data type
- `getBehavior(component)` - Get the InternalBehavior for a component
- `getImplementation(component)` - Get the Implementation for a component

### Parser Usage
```python
from armodel.parser.arxml_parser import ARXMLParser

parser = ARXMLParser(options={"warning": True})
autosar_model = parser.parse_from_file('example.arxml')
```

### Writer Usage
```python
from armodel.writer.arxml_writer import ARXMLWriter

writer = ARXMLWriter()
writer.write_to_file(autosar_model, 'output.arxml')
```

## Common Patterns

**Adding new elements:**
```python
from armodel.models import AUTOSAR, ARPackage

autosar = AUTOSAR.getInstance()
pkg = ARPackage('MyPackage')
autosar.addARPackage(pkg)
```

**Navigating package hierarchy:**
```python
parent_pkg = ARPackage('Parent')
child_pkg = ARPackage('Child')
parent_pkg.addARPackage(child_pkg)
```

**Setting AUTOSAR version before parsing/writing:**
```python
from armodel.models import AUTOSAR

# MUST call before parsing or writing
AUTOSAR.setARRelease('R23-11')  # or '4.0.3', 'R24-11', etc.
```

**Finding elements by short name:**
```python
from armodel.models import AUTOSAR

autosar = AUTOSAR.getInstance()

# Find returns None if not found (no exceptions)
component = autosar.findAtomicSwComponentType('MyComponent')
if component is not None:
    behavior = autosar.getBehavior(component)
```

## CI/CD

GitHub Actions (`.github/workflows/python-package.yml`):
- Python versions: 3.8, 3.9, 3.10, 3.11, 3.12
- Linting: `flake8 --select=E9,F63,F7,F82` (syntax errors) and `--max-complexity=10 --max-line-length=127` (complexity warnings)
- Steps: Install dependencies → Lint → Test
- All lint and test checks must pass before merge

## References

- AUTOSAR: https://www.autosar.org/
- GitHub: http://github.com/melodypapa/py-armodel
- PyPI: https://pypi.org/project/armodel/
- Docs: https://py-armodel.readthedocs.io/
