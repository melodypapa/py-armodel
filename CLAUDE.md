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

### Recent Architectural Improvements

**Package Structure Refactoring (2024):**
- Fixed case-sensitivity issues with Components/ vs Components directories
- Reorganized ECUC module imports to resolve ImportError
- Improved AnyInstanceRef and CompositionSwComponentType package structure
- Enhanced deviation tracking and documentation

**Test Coverage Enhancement:**
- Ongoing effort to increase test coverage across all modules
- Focus on M2 models, parser, writer, and library functions
- Added tests for SwcInternalBehavior and NetworkManagement
- Using test-driven development for new features

**Documentation Improvements:**
- Added comprehensive deviation documentation
- Enhanced class hierarchy documentation
- Improved coding rules documentation
- Added SpeckKit integration for feature specification

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
    - ECUCParameterDefTemplate - ECUC parameter definitions
    - EcuResourceTemplate - ECU resources
    - GenericStructure - Generic template classes, variant handling, lifecycle
    - DiagnosticExtract - Diagnostic contributions
  - utils/ - UUID management utilities

- **parser/** - ARXML parsing
  - arxml_parser.py - Main ARXML parser
  - abstract_arxml_parser.py - Abstract base parser
  - connector_xlsx_parser.py - Excel connector parsing
  - excel_parser.py - Generic Excel parsing
  - file_parser.py - File parsing utilities

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

- **data_models/** - Data model definitions
  - sw_connector.py - Software connector model (AssemblySwConnector, DelegationSwConnector)

- **transformer/** - Data transformation
  - abstract.py - Abstract transformer base
  - admin_data.py - Admin data transformation

- **report/** - Report generation
  - connector_xls_report.py - Connector Excel report
  - excel_report.py - Excel report utilities

### Source Layout
- Source code in `src/armodel/` directory (src layout)
- Install in development mode with: `pip install -e .`
- All imports are absolute: `from armodel.models import AUTOSAR`
- `.specify/` - SpeckKit directory for feature specification and development workflows
- `.claude/commands/` - Custom Claude Code slash commands for development automation

## Development Commands

### Testing
- `python scripts/run_tests.py` - Run all tests with colored output and summary (Recommended)
- `python scripts/run_tests.py --unit` - Run only unit tests
- `python scripts/run_tests.py --integration` - Run only integration tests
- `python scripts/run_tests.py --coverage` - Run with coverage reports
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
- `python -m build` - Create source and wheel distributions
- `python -m build --sdist` - Create source distribution only
- `python -m build --wheel` - Create wheel distribution only
- `twine check dist/*` - Check distribution
- `twine upload dist/*` - Upload to PyPI

### Installation
- `pip install -e .` - Install in editable mode for development

### Documentation
- `cd docs && make html` - Build with Sphinx
- `mkdocs build` or `mkdocs serve` - Build with MkDocs

### Common Development Tasks

**Adding a new AUTOSAR model class:**
1. Determine if it should be a leaf package (`.py` file) or non-leaf package (`__init__.py`)
2. Create the file in appropriate M2 location under `src/armodel/models/M2/AUTOSARTemplates/`
3. Add wildcard import in parent `__init__.py`: `from .my_class import *`
4. Add import to `src/armodel/models/__init__.py`
5. Create corresponding test in `tests/test_armodel/models/M2/`
6. Run tests and linting: `python scripts/run_tests.py`

**Debugging parser issues:**
- Use `options={"warning": True}` to get warnings instead of exceptions
- Check XML namespace mappings in `release_xsd_mappings`
- Verify element is in supported elements list
- Check parent-child relationships are maintained

**Working with test files:**
- Sample ARXML files in `tests/test_files/`
- Use existing files as templates for new test cases
- Ensure test files cover supported AUTOSAR versions

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
Many AUTOSAR classes use ABC (Abstract Base Class) from the `abc` module (migrated from ABCMeta metaclass). These raise TypeError if directly instantiated. Always check if a class is abstract before attempting to instantiate it (e.g., ARObject, AtpType, Identifiable).

**Pattern:**
```python
from abc import ABC

class MyAbstractClass(ABC):
    @abstractmethod
    def my_method(self):
        pass
```

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

### Common Pitfalls

**Import Errors:**
- Ensure proper package structure when adding new classes
- Check that wildcard imports in `__init__.py` files include new classes
- Leaf packages use `.py` files, non-leaf packages use `__init__.py`

**Package Structure:**
- Recent refactoring fixed issues with Components/ vs Components
- Always verify package exists before adding classes
- Use proper import paths: `from armodel.models.M2.AUTOSARTemplates...`

**UUID Management:**
- UUIDs are managed through `UUIDMgr` utility
- Duplicate UUIDs are checked and will raise errors
- Each AUTOSAR element should have a unique UUID

**Parent References:**
- Always maintain parent-child relationships
- Use `addElement()` methods rather than directly appending to lists
- Parent references are used for navigation and serialization

## Coding Standards

The project follows PEP 8 coding conventions. Key conventions include:

### Code Layout
- Indentation with 4 spaces (never tabs)
- Maximum line length: 79 characters per PEP 8 (CI warns at 127)
- Double quotes for strings (triple double quotes for docstrings)
- Blank lines: 2 between top-level definitions, 1 between class methods

### Import Organization
- Import order: Standard library → Third-party → Local (absolute paths)
- Section separation with blank lines, alphabetical ordering within sections

### Naming Conventions
- Classes: `PascalCase`
- AUTOSAR methods: `camelCase` (following AUTOSAR standard)
- New Python methods: `snake_case` (following PEP 8)
- Constants: `UPPER_CASE`
- Private attributes: `_leading_underscore`
- Test classes: `Test<ClassName>`
- Test methods: `test_<method_name>_<scenario>` or `test_<scenario>`

### Type Annotations
- Use Python 3.10+ union syntax: `str | None` instead of `Optional[str]`
- Use forward references with string literals for circular dependencies: `List["MyClass"]`
- Only reference classes that exist in the codebase to avoid F821 flake8 errors

### Documentation
- Google-style docstrings for public classes and methods (when present)
- Requirements section with requirement IDs in docstrings (when applicable)
- All docstrings in English

### Whitespace
- No extraneous whitespace in parentheses/brackets
- Operators surrounded by spaces: `x = 1`, `a + b`
- Keyword arguments use `arg=value` (no spaces around `=`)

### Style Guidelines
- Use `@dataclass` decorator for model classes (when applicable)
- Validate dataclass fields in `__post_init__`
- Compile regex patterns as class constants
- Use context managers (`with`) for resource management

**Important Package Structure Rule:**
- **Leaf packages** (no subdirectories): Classes defined in `.py` file with package name = filename
- **Non-leaf packages** (have subdirectories): Classes defined in `__init__.py` of the directory

### Error Handling
- Use `ValueError` for invalid arguments
- Validate inputs immediately
- Use `raise ... from e` for exception chaining
- Abstract base classes raise `TypeError` in `__init__`

### Testing
- Mirror source structure in `tests/` directory
- Test classes: `Test<ClassName>`
- Test methods: `test_<method_name>_<scenario>` or `test_<scenario>`
- Use `pytest.raises(ValueError, match="pattern")` for exception testing

### Programming Recommendations
- Use `isinstance()` for type comparisons
- Use `is` / `is not` for `None` comparisons
- Don't compare booleans to `True`/`False` using `==`
- Catch specific exceptions, not bare `except:`
- Use `with` statements for resource management

For comprehensive coding rules, see `docs/development/coding_rules.md`.

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
- BSW Call Points: BswDirectCallPoint, BswSynchronousServerCallPoint, BswAsynchronousServerCallPoint, BswAsynchronousServerCallResultPoint

### CommonStructure
ARObject, Referrable, Identifiable, ServiceNeeds (Diagnostic, Communication, etc.), Implementation, InternalBehavior, ResourceConsumption (MemorySection, StackUsage, HeapUsage, ExecutionTime), ModeDeclaration, SwcBswMapping
- Timing: TimingConstraints, ExecutionOrderConstraint, TimingExtensions
- TriggerDeclaration: Trigger
- Documentation: Documentation (DocumentationOnM1)
- Variant Handling: VariationPoint, PostBuildVariantCriterion, PostBuildVariantCriterionValue, PredefinedVariant, SwSystemconstantValueSet, NumericalValueVariationPoint
- LifeCycle: LifeCycleInfo, LifeCycleInfoSet, KeywordSet, Collection

### Diagnostics
DiagnosticConnection, DiagnosticServiceTable, DiagnosticEventNeeds, DiagnosticEventInfoNeeds, DCM Needs (DiagnosticCommunicationManagerNeeds, DiagnosticRoutineNeeds, DiagnosticValueNeeds), DoIP (DoIpServiceNeeds, DoIpConfiguration)
- Additional: MlFormula (MathML formulas)

### System
SystemSignal, SystemSignalGroup, SWC-TO-ECU-MAPPING, SW-MAPPINGS, ECU-INSTANCE, ROOT-SOFTWARE-COMPOSITIONS, DataMapping, NetworkManagement, SecureCommunication

### BSW Modules
BswModuleDescription, BswBehavior (BswInternalBehavior, BswModuleEntity, BswCalledEntity, BswSchedulableEntity, BswInterruptEntity), BswImplementation, BswInterfaces (BswModuleEntry, BswModuleClientServerEntry, BswModuleDependency), BSW Events, BSW Call Points (BswDirectCallPoint, BswSynchronousServerCallPoint, BswAsynchronousServerCallPoint, BswAsynchronousServerCallResultPoint)

### ECUC Configuration
EcucValueCollection, EcucModuleConfigurationValues, EcucContainerValue, EcucParameterValue, EcucModuleDef, EcucParamDef (Boolean, String, Integer, Float, Enumeration)
- Additional: EcucAddInfoParamDef, EcucConditionFormula, EcucDefinitionCollection, EcucDestinationUriDef, EcucDestinationUriDefSet, EcucDestinationUriPolicy, EcucLinkerSymbolDef, EcucMultilineStringParamDef, EcucParameterDerivationFormula, EcucQuery, EcucQueryExpression, EcucParamConfContainerDef

### Fibex (Field Bus Exchange Format)
Fibex4Can, Fibex4Ethernet, Fibex4Flexray, Fibex4Lin, FibexCore, Fibex4Multiplatform

### Transport Protocols
GenericTP, TCP-TP, UDP-TP, CAN-TP, LIN-TP, DO-IP-TP

### Data Transformation
DataTransformationSet, TypeMapping, Mask, UserDefinedTransformationComSpecProps

## Testing Structure

Tests in `tests/test_armodel/` mirror the source structure. Sample ARXML files in `test_files/` include AUTOSAR_Datatypes.arxml, SoftwareComponents.arxml, BswM_Bswmd.arxml organized by AUTOSAR modules.

**Test Data Location:**
- Sample ARXML files are in `tests/test_files/` directory
- Common test files: AUTOSAR_Datatypes.arxml, SoftwareComponents.arxml, BswM_Bswmd.arxml, CanSystem.arxml
- Use these files for parser/writer validation

**Test Coverage Goals:**
- Target high test coverage (current focus on increasing coverage)
- Test both success and error paths
- Include edge cases and boundary conditions
- **Integration tests**: 29 ARXML files validated through round-trip testing (parse → write → re-parse → compare)
- **Test runner script**: Use `python scripts/run_tests.py` for colored output and comprehensive summaries

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
from armodel.models import AUTOSAR
from armodel.parser.arxml_parser import ARXMLParser

# MUST set AUTOSAR version first
AUTOSAR.setARRelease('R23-11')

# Get singleton instance and clear
document = AUTOSAR.getInstance()
document.clear()

# Parse ARXML file
parser = ARXMLParser()
parser.load('example.arxml', document)

# Or with warning mode for development
parser = ARXMLParser(options={"warning": True})
parser.load('example.arxml', document)
```

### Writer Usage
```python
from armodel.models import AUTOSAR
from armodel.writer.arxml_writer import ARXMLWriter

# MUST set AUTOSAR version first
AUTOSAR.setARRelease('R23-11')

# Write to ARXML file
writer = ARXMLWriter()
writer.save('output.arxml', AUTOSAR.getInstance())
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

**Working with parent-child relationships:**
```python
# When adding elements, ensure proper parent references
pkg.addElement(element)
assert element.parent == pkg  # Parent is automatically set
```

**Getter/setter pattern:**
```python
# Most AUTOSAR classes follow getter/setter pattern
element.getShortName()
element.setShortName("NewName")  # Returns self for method chaining

# Method chaining example
pkg.setShortName("MyPackage").setUUID("12345").addARPackage(child_pkg)
```

**Working with collections:**
```python
# Add to collections
pkg.addARPackage(child_pkg)
behavior.addRunnableEntity(runnable)

# Get collections (returns list)
packages = pkg.getARPackages()
runnables = behavior.getRunnableEntities()
```

## CI/CD

GitHub Actions (`.github/workflows/python-package.yml`):
- Python versions: 3.8, 3.9, 3.10, 3.11, 3.12
- Linting: `flake8 --select=E9,F63,F7,F82` (syntax errors) and `--max-complexity=10 --max-line-length=127` (complexity warnings)
- Steps: Install dependencies → Lint → Test
- All lint and test checks must pass before merge

## Additional Documentation

### Hierarchy and Class Relationships
The project maintains detailed documentation of AUTOSAR class hierarchies:
- `docs/requirements/software_components_hierarchy.md` - Complete class hierarchy from ARObject down through all ARElement types
- Shows inheritance relationships (abstract classes marked with "abstract")
- Useful for understanding the AUTOSAR M2 meta-model structure

### Deviation Documentation
The project includes scripts and documentation for tracking deviations from the AUTOSAR standard:
- `scripts/deviation-package.py` - Generate deviation package documentation
- `scripts/deviation-class-hierarchy.py` - Generate class hierarchy documentation
- `reports/deviation_package.md` - Deviation package structure documentation
- `reports/deviation_class_hierarchy_summary.md` - Class hierarchy deviation summary
- `reports/deviation_class_hierarchy_mismatches.md` - Class hierarchy mismatches detail
- `reports/deviation_class_hierarchy_extra_classes.md` - Extra classes not in documentation
- `docs/requirements/software_components.md` - Software component requirements

### Coding Standards
- `docs/development/coding_rules.md` - Comprehensive coding rules and standards (maturity levels: accept/invalid/draft)
- Covers PEP 8 conventions, type hints, docstrings, testing, error handling
- Enforced through CI/CD pipeline with flake8 and pytest

### Agent Guidelines
- `AGENTS.md` - Additional guidelines for AI agents working with this codebase
- `CLAUDE.md` - This file, providing project guidance for Claude Code

### Slash Commands
The project includes custom Claude Code slash commands in `.claude/commands/` for development automation:

**Available Commands:**
- `/test` - Test runner with coverage reporting (all/unit/integration)
- `/quality` - Run quality checks (flake8, pytest coverage)
- `/gh-workflow` - Automate GitHub workflow (create issue, branch, commit, PR)
- `/merge-pr` - Merge pull requests via GitHub CLI (gh)
- `/req` - Requirement management and documentation

**Usage:**
```
/test                    # Run all tests
/test --unit            # Run only unit tests
/test --integration     # Run only integration tests
/quality                # Run all quality checks
/gh-workflow Add feature X
```

See `.claude/commands/README.md` for complete command documentation.

### Requirements Documentation
- `reports/deviation_package.md` - Deviations from AUTOSAR standard package structure
- `docs/requirements/software_components.md` - Software component requirements

## References

- AUTOSAR: https://www.autosar.org/
- GitHub: http://github.com/melodypapa/py-armodel
- PyPI: https://pypi.org/project/armodel/
- Docs: https://py-armodel.readthedocs.io/

## Language-Specific Documentation

- **IFLOW.md** - 项目指南 (Chinese language project guide with architecture overview)
- **AGENTS.md** - Agent Guidelines (English language guidelines for AI agents)
- **CLAUDE.md** - This file (Claude Code guidance in English)
