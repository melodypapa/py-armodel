# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

py-armodel is a Python library for parsing, manipulating, and writing AUTOSAR XML (ARXML) files. It follows the AUTOSAR standard specifications and supports versions from 4.0.3 to R24-11, with particular focus on CP R23-11 standard compliance.

**Current Version**: 1.9.2
**Python Requirements**: >= 3.5 (CI tests on 3.8-3.13)
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

**V2 Models Architecture (2025):**
- **Clean Import Architecture**: V2 models (`armodel.v2.models`) provide improved structure with absolute imports only
- **Abstract Base Class Pattern**: Properly implemented ABC with `@abstractmethod` decorator across all 101 concrete subclasses
- **Ruff Error Reduction**: Reduced V2 linting errors from 932 to 113 (88% reduction) through automated refactoring
- **Block Import Style**: Explicit class imports with multi-line block format for better readability and git diffs
- **Type Safety**: Enhanced type hints with string annotations for forward references (no TYPE_CHECKING blocks)
- **100% V1 API Compatibility**: V2 maintains full backward compatibility with V1 models
- **Migration Guide**: Comprehensive documentation for migrating from V1 to V2 (see `docs/development/v2_migration_guide.md`)

### V2 Models Key Improvements

**Abstract Base Class Pattern:**
- All abstract base classes use `@abstractmethod` decorator from `abc` module
- Concrete subclasses implement `_validate_abstract()` method to prove they're instantiable
- ARObject and ARType serve as foundation abstract classes for the M2 model hierarchy
- Runtime validation prevents instantiation of abstract classes with clear error messages

**V2 vs V1 Architecture:**
| Aspect | V1 | V2 |
|--------|----|----|
| Import path | `armodel.models` | `armodel.v2.models` |
| Imports | Relative allowed | Absolute only |
| TYPE_CHECKING | Used | Prohibited (use string annotations) |
| __all__ | Optional | Required (explicit exports) |
| Import style | Wildcard/mixed | Block-style explicit imports |
| Abstract classes | ABCMeta/informal | Proper @abstractmethod |
| Ruff errors | 932 | 113 (intentional patterns) |

**V2 Coding Standards:**
- CODING_RULE_V2_00001: Absolute imports only
- CODING_RULE_V2_00002: No TYPE_CHECKING blocks
- CODING_RULE_V2_00003: Explicit __all__ exports
- CODING_RULE_V2_00005: String annotations for forward references
- CODING_RULE_V2_00012: Explicit class imports (no wildcards)
- CODING_RULE_V2_00013: Block import style (multi-line with parentheses)

See `docs/development/coding_rules_v2.md` for complete V2 coding rules.

## Module Organization

- **models/** - V1 AUTOSAR data model classes following M2 schema structure
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

- **v2/models/** - V2 AUTOSAR data model classes with improved architecture
  - **Clean Import Architecture**: Absolute imports only, explicit `__all__` exports
  - **Proper ABC Pattern**: `@abstractmethod` decorator with `_validate_abstract()` implementation
  - **Block Import Style**: Multi-line explicit class imports for better readability
  - **Type Safety**: String annotations for forward references (no TYPE_CHECKING)
  - **100% V1 API Compatible**: Drop-in replacement with improved code quality
  - Same M2 structure as V1 but with enhanced coding standards
  - See `docs/development/v2_migration_guide.md` for migration guide

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

#### Test Markers
Tests are organized with custom markers for selective execution:
- `integration`: Integration tests (slower, requires full parse/write cycle)
- `slow`: Slow-running tests (can be skipped with `-m "not slow"`)
- `datatypes`: Tests related to AUTOSAR data types
- `components`: Tests related to software components
- `bsw`: Tests related to BSW modules
- `system`: Tests related to system configuration
- `blueprint`: Tests for blueprint specification files
- `lifecycle`: Tests for lifecycle-related files

**Example:**
```bash
# Run only integration tests
pytest -m integration

# Run tests but skip slow ones
pytest -m "not slow"

# Run datatype-related tests
pytest -m datatypes
```

Or using npm scripts (from package.json):
- `npm run pytest` - Run all tests
- `npm run pytest-cov` - Run tests with coverage report
- `npm run flake8` - Run flake8 for critical errors only
- `npm run bswm-test` - Test BSW module with sample ARXML file

### Linting

#### Primary Linter: Ruff
```bash
# Run ruff (configured in pyproject.toml)
ruff check .

# Auto-fix issues
ruff check --fix .

# Show detailed rule violations
ruff check --show-source .
```

#### Legacy Linter: Flake8
```bash
# Run flake8 for critical errors only
flake8 --select=E9,F63,F7,F82 .
```

**Note**: CI runs ruff with comprehensive rules. Line length is 79 characters (PEP 8 standard), with CI warnings at 127.

### Type Checking: MyPy

For V2 models, run mypy to validate type annotations:
```bash
# Run mypy on V2 modules
mypy src/armodel/v2/

# Run mypy with specific configuration
mypy --config-file pyproject.toml src/armodel/v2/

# Run mypy on specific V2 submodules
mypy src/armodel/v2/models/
mypy src/armodel/v2/reader/
mypy src/armodel/v2/writer/
```

**Current Status**: V2 models show 6348 mypy errors (mostly missing type annotations).
This is acceptable for gradual type annotation adoption. Focus on new code and critical paths first.

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

### Development Scripts

**Package Structure Analysis:**
- `python scripts/deviation-package.py` - Generate package deviation reports
- `python scripts/deviation-class-hierarchy.py` - Generate class hierarchy reports
- `python scripts/scan_existing_classes.py` - Scan and catalog existing classes
- `python scripts/compare-package-implementation.py` - Compare package structure

**ABC Automation (V2 Models):**
- `python scripts/add_validate_abstract.py` - Add `_validate_abstract()` method to concrete classes
- `python scripts/remove_validate_abstract.py` - Remove `_validate_abstract()` method from classes

**Test Runner:**
- `python scripts/run_tests.py` - Run all tests with colored output and summary
- `python scripts/run_tests.py --unit` - Run only unit tests
- `python scripts/run_tests.py --integration` - Run only integration tests
- `python scripts/run_tests.py --coverage` - Run with coverage reports

### Common Development Tasks

**Adding a new AUTOSAR model class:**

**For V1 models:**
1. Determine if it should be a leaf package (`.py` file) or non-leaf package (`__init__.py`)
   - **Leaf package**: Single `.py` file when package has no subdirectories
   - **Non-leaf package**: Directory with `__init__.py` when package has subdirectories
2. Create the file in appropriate M2 location under `src/armodel/models/M2/AUTOSARTemplates/`
3. Add wildcard import in parent `__init__.py`: `from .my_class import *`
4. Add import to `src/armodel/models/__init__.py`
5. Create corresponding test in `tests/test_armodel/models/M2/`
6. Run tests and linting: `python scripts/run_tests.py`
7. Verify package structure compliance: `python scripts/deviation-package.py`

**For V2 models:**
1. Determine if it should be a leaf package (`.py` file) or non-leaf package (`__init__.py`)
2. Create the file in appropriate M2 location under `src/armodel/v2/models/M2/AUTOSARTemplates/`
3. Use **absolute imports** and **block import style**:
   ```python
   from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
       ARObject,
   )
   ```
4. Add explicit `__all__` export in parent `__init__.py` (after all imports):
   ```python
   from armodel.v2.models.M2.AUTOSARTemplates.MyModule import MyClass

   __all__ = ["MyClass"]
   ```
5. If creating abstract class, use `@abstractmethod`:
   ```python
   from abc import ABC, abstractmethod

   class MyAbstractClass(ABC):
       @abstractmethod
       def _validate_abstract(self) -> None:
           pass
   ```
6. If creating concrete class, implement `_validate_abstract()`:
   ```python
   class MyConcreteClass(ARObject):
       def _validate_abstract(self) -> None:
           """Validate this is a concrete class."""
           pass
   ```
7. Create corresponding test in `tests/test_armodel/models_v2/M2/`
8. Run V2-specific checks:
   ```bash
   ruff check src/armodel/v2/models/
   pytest tests/test_armodel/models_v2/
   ```

**Class relocation for coding rule compliance:**
When moving classes to comply with CODING_RULE_STYLE_00008 or CODING_RULE_STYLE_00009:
1. Identify the correct AUTOSAR M2 package location
2. Move class to proper module (leaf package `.py` or non-leaf `__init__.py`)
3. Update all imports across the codebase
4. Run `ruff check .` to verify no import errors
5. Run `python scripts/deviation-package.py` to verify path compliance
6. Run tests to ensure no regressions

**Debugging parser issues:**
- Use `options={"warning": True}` to get warnings instead of exceptions
- Check XML namespace mappings in `release_xsd_mappings`
- Verify element is in supported elements list
- Check parent-child relationships are maintained

**Working with test files:**
- Sample ARXML files in `tests/test_files/`
- Use existing files as templates for new test cases
- Ensure test files cover supported AUTOSAR versions
- Integration tests auto-detect version from XSD schema (4.0.3 to R24-11)

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

## Claude Code Slash Commands

The project includes custom slash commands in `.claude/commands/` for development automation. These commands provide shortcuts for common workflows and are invoked with `/` prefix.

### `/test` - Test Runner with Coverage
Run tests with colored output and comprehensive summaries.
```bash
/test                    # Run all tests
/test --unit            # Run only unit tests
/test --integration     # Run only integration tests
/test --coverage        # Run with coverage reports
```

### `/quality` - Quality Check Automation
Run all quality checks (ruff, mypy, pytest) to ensure code meets standards.
```bash
/quality                # Run all quality checks
/quality --fix          # Auto-fix linting issues
```

**Quality Gates:**
- Ruff linting: No errors
- Mypy type checking: No issues (for V2 models)
- Pytest: All tests pass
- Coverage: Maintained or improved

### `/gh-workflow` - GitHub Workflow Automation
Automate the complete GitHub workflow for creating issues, feature branches, commits, and pull requests.
```bash
/gh-workflow
/gh-workflow Implement new parser for AUTOSAR models
/gh-workflow feature: Add support for base class extraction
```

**Workflow Steps:**
1. Run quality checks (flake8, ruff, mypy, pytest)
2. Analyze current changes with git status and diff
3. Create GitHub issue with detailed description
4. Create or verify feature branch
5. Stage and commit changes
6. Push to GitHub only (not gitee)
7. Create pull request with comprehensive description

**Important:** Never commits directly to main branch. If commits exist on main, the workflow moves them to a feature branch and resets main to origin/main.

### `/merge-pr` - Merge Pull Requests
Safely merge PRs via GitHub CLI with validation.
```bash
/merge-pr
```

### `/req` - Requirement Management
Manage AUTOSAR project requirements with traceability.
```bash
/req add SWR_WRITER_00007 "Add support for custom templates"
/req update SWR_WRITER_00006 maturity accept
/req check traceability
/req list draft
/req search parser
```

**See `.claude/commands/README.md` for complete command documentation.**

## Important Implementation Details

### Abstract Base Classes
AUTOSAR uses proper Python ABC (Abstract Base Class) pattern with `@abstractmethod` decorator. This ensures abstract classes cannot be instantiated directly.

**V2 Implementation (Proper ABC Pattern):**
```python
from abc import ABC, abstractmethod

# Abstract base class with @abstractmethod
class ARObject(ABC):
    @abstractmethod
    def _validate_abstract(self) -> None:
        """Abstract method to enforce abstract base class pattern."""
        pass

    def __init__(self) -> None:
        if type(self) is ARObject:
            raise TypeError("ARObject is an abstract class.")
        self._validate_abstract()

# Concrete subclass must implement abstract method
class SwComponentType(ARObject):
    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass
```

**Key Points:**
- **V2 models** use proper `@abstractmethod` decorator (101 concrete subclasses implement `_validate_abstract()`)
- **V1 models** may use informal ABC or ABCMeta metaclass (being migrated)
- Runtime validation in `__init__` prevents direct instantiation of abstract classes
- Always check if a class is abstract before attempting to instantiate it (e.g., ARObject, AtpType, Identifiable)

### Enum Usage: AREnum vs Python Enum
**CRITICAL**: Use `AREnum` base class instead of Python's `enum.Enum` for AUTOSAR compliance.

```python
# Correct - Use AREnum for AUTOSAR enums
from armodel.models.base import AREnum

class BswEntryKindEnum(AREnum):
    PROVIDED = "PROVIDED"
    REQUIRED = "REQUIRED"

# Incorrect - Do NOT use Python Enum
from enum import Enum  # Don't do this
class MyEnum(Enum):   # Violates AUTOSAR compliance
    VALUE = "value"
```

**Why AREnum?**
- Better alignment with AUTOSAR M2 model specifications
- Enhanced serialization and deserialization for ARXML files
- Improved type safety and validation
- Consistent enum handling across the codebase

**Recent Migration (v1.9.2)**: All enum definitions have been migrated from Python `enum.Enum` to `AREnum`. When adding new enums, always use `AREnum` as the base class.

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

**Package Structure (CODING_RULE_STYLE_00008):**
- **Leaf packages**: Create `.py` file (e.g., `ImplementationDataTypes.py`)
- **Non-leaf packages**: Create directory with `__init__.py`
- **Never** create double nesting like `ImplementationDataTypes/ImplementationDataTypes.py`
- Recent refactoring fixed issues with Components/ vs Components
- Always verify package exists before adding classes
- Use proper import paths: `from armodel.models.M2.AUTOSARTemplates...`

**Class Export (CODING_RULE_STYLE_00009):**
- All classes must be properly exported from their modules
- Use `__all__` lists in modules for explicit exports
- Run `python scripts/deviation-package.py` to verify compliance
- Check for duplicate class names before committing
- Classes MUST be importable from paths in `docs/requirements/mapping.json`

**Enum Usage:**
- Always use `AREnum` base class, never Python's `enum.Enum`
- Import from `armodel.models.base import AREnum`
- Parser and writer expect AREnum instances for proper serialization

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
- **V2 models**: Use string annotations for forward refs instead of TYPE_CHECKING blocks

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

## Error Handling and Debugging

### Parser Error Modes

The ARXMLParser supports two error handling modes:

**Strict Mode (default):**
```python
parser = ARXMLParser()
# Raises exceptions on errors
parser.load("file.arxml", document)
```

**Warning Mode (for development):**
```python
parser = ARXMLParser(options={"warning": True})
# Logs warnings instead of raising exceptions
parser.load("file.arxml", document)
```

### Common Parser Issues

**Issue**: "Element not supported"
- **Cause**: ARXML element not in supported elements list
- **Solution**: Check XML namespace mappings in `release_xsd_mappings`
- **Debug**: Use warning mode to see all unsupported elements

**Issue**: "Parent-child relationship error"
- **Cause**: Parent references not maintained when adding elements
- **Solution**: Use `addElement()` methods instead of directly appending to lists
- **Example**: `pkg.addElement(element)` instead of `pkg.elements.append(element)`

**Issue**: "Circular import error"
- **Cause**: Type annotations with forward references not using string literals
- **Solution**: Use string annotations: `List["MyClass"]` instead of `List[MyClass]`
- **V2 Note**: Use string annotations per CODING_RULE_V2_00005 (no TYPE_CHECKING blocks)

**Issue**: "Package not found" error
- **Cause**: Class not properly exported from `__init__.py`
- **Solution**: Ensure class is in wildcard import or `__all__` list
- **V1 Models**: Use `from .my_class import *` in `__init__.py`
- **V2 Models**: Add to `__all__` list with explicit imports

**Issue**: Tests failing on Python 3.8/3.9
- **Cause**: Using Python 3.10+ union syntax without `from __future__ import annotations`
- **Solution**: Add `from __future__ import annotations` at top of file, or use `Union[...]` syntax
- **Note**: V1 models should use `Union`, V2 models use string annotations

### Debugging Tips

**Enable verbose logging:**
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

**Check AUTOSAR version:**
```python
from armodel.models import AUTOSAR
AUTOSAR.setARRelease('R23-11')  # MUST be set before parsing/writing
```

**Validate object graph:**
```python
# Check parent references
assert element.parent is expected_parent

# Check children exist
assert len(pkg.getARPackages()) > 0
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
- Python versions: 3.8, 3.9, 3.10, 3.11, 3.12, 3.13
- Linting: `ruff check .` with comprehensive rules (E, W, F, I, N, B, C4, SIM)
- Ignores: F403/F405 (wildcard imports), N802 (AUTOSAR camelCase), N999 (AUTOSAR PascalCase modules)
- Steps: Install dependencies → Lint → Test
- All lint and test checks must pass before merge

### V2 Quality Status
- **V2 Linting**: 113 ruff errors (all intentional patterns: AUTOSAR naming, circular dependencies)
  - Reduced from 932 errors (88% reduction) through automated refactoring
  - All B024 (abstract base class) errors fixed with proper `@abstractmethod` pattern
  - All 101 concrete subclasses implement `_validate_abstract()` method
- **V2 Type Checking**: MyPy shows 6348 errors (mostly missing type annotations)
  - Acceptable for gradual type annotation adoption
  - Focus on new code and critical paths first
- **V2 Tests**: All 2357 tests passing (unit + integration)

### Ruff Configuration
- Line length: 79 characters (PEP 8 standard)
- Max docstring length: 72 characters
- Import order: Standard library → Third-party → Local
- Wildcard imports allowed for M2 model structure (intentional per coding rules)
- AUTOSAR camelCase methods exempt from snake_case naming convention
- **V2 specific**: Block import style enforced (CODING_RULE_V2_00013)

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
- `docs/development/coding_rules_v2.md` - V2-specific coding rules (13 rules defined)
  - Absolute imports, no TYPE_CHECKING, explicit __all__, block import style
  - String annotations for forward references
  - Proper ABC pattern with @abstractmethod
- Covers PEP 8 conventions, type hints, docstrings, testing, error handling
- Enforced through CI/CD pipeline with ruff and pytest

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

## Recent Version History

### Version 2.0.0 (Upcoming - V2 Models)
- **V2 Architecture Launch**: New V2 models with improved code quality and cleaner imports
  - Absolute imports only (CODING_RULE_V2_00001)
  - Proper ABC pattern with `@abstractmethod` (101 concrete subclasses)
  - Block import style for better readability (CODING_RULE_V2_00013)
  - Explicit `__all__` exports (CODING_RULE_V2_00003)
  - String annotations for forward references (CODING_RULE_V2_00005)
- **Ruff Error Reduction**: Reduced V2 linting errors from 932 to 113 (88% reduction)
- **Automated Refactoring**: Script-based implementation of abstract methods across 101 files
- **Quality Gates**: All 2357 tests passing, V2-specific linting and type checking established
- **Migration Support**: Comprehensive V1 to V2 migration guide and backward compatibility
- **Documentation**: V2 coding rules (13 rules), migration guide, design documents

### Version 1.9.2 (Current - V1 Models)
- **Enum Refactoring**: Converted Python `enum.Enum` to `AREnum` for better AUTOSAR compliance
- **Package Structure Refactoring**: Relocated classes to comply with CODING_RULE_STYLE_00008 and CODING_RULE_STYLE_00009
  - Fixed CollectableElement, EndToEndTransformationComSpecProps, FlexrayChannelName
  - Fixed CommunicationDirectionType, IPduSignalProcessingEnum, ExternalTriggeringPointIdent
  - Fixed AtpBlueprintMapping, EcuInstance, SwcToEcuMapping
  - Added PackageableElement to ARPackage module exports
- **Test Coverage Enhancement**: Ongoing effort to increase test coverage across all modules
- **Documentation Improvements**: Updated AGENTS.md with detailed coding rules explanations

### Version 1.9.1
- **Package Structure Refactoring**: Fixed case-sensitivity issues, reorganized ECUC module imports
- **Test Coverage Enhancement**: Added tests for SwcInternalBehavior and NetworkManagement
- **Documentation Improvements**: Enhanced deviation tracking and documentation

### Version 1.9.0
- **Testing Infrastructure**: Added comprehensive integration test suite with round-trip validation
- **Test Runner**: Added `scripts/run_tests.py` with colored output and comprehensive summaries
- **Pytest Configuration**: Added `pytest.ini` with custom markers for test organization
- **Coverage Reporting**: Support for 2205+ unit tests and 29 integration test files
