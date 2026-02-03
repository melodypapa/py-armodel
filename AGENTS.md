# Agent Guidelines for py-armodel

## Project Overview
Python library for AUTOSAR model support - ARXML parser and writer for automotive ECU software development.
**Version**: 1.9.2 | **Python**: >= 3.5 | **License**: MIT | **Repository**: http://github.com/melodypapa/py-armodel

## Build, Lint, and Test Commands

### Testing

#### Recommended Test Runner
Use the test runner script for colored output and comprehensive testing:
```bash
# Run all tests (unit + integration)
python scripts/run_tests.py

# Run only unit tests
python scripts/run_tests.py --unit

# Run only integration tests
python scripts/run_tests.py --integration

# Run with coverage reports
python scripts/run_tests.py --coverage

# Verbose output
python scripts/run_tests.py --verbose
```

#### Using pytest Directly
```bash
# Run all tests with coverage
pytest --cov=armodel --cov-report term-missing
npm run pytest-cov

# Run only unit tests
pytest tests/test_armodel/

# Run integration tests with progress output
pytest tests/integration_tests/ -s

# Run specific test file
pytest tests/test_armodel/parser/test_arxml_parser.py

# Run specific test method
pytest tests/test_armodel/parser/test_arxml_parser.py::TestClass::test_method

# Verbose output
pytest -v

# Show print output
pytest -s
```

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
npm run flake8
flake8 --select=E9,F63,F7,F82 .
```

**Note**: CI runs ruff with comprehensive rules. Line length is 79 characters (PEP 8 standard), with CI warnings at 127.

### Building
```bash
# Create distribution (source + wheel)
python -m build

# Create source distribution only
python -m build --sdist

# Create wheel distribution only
python -m build --wheel

# Check distribution
twine check dist/*

# Upload to PyPI
twine upload dist/*
```

## Code Style Guidelines

### Comprehensive Reference
For detailed coding standards, see: `docs/development/coding_rules.md`

### Imports
- Standard library first (typing, xml, os, logging, getopt, re)
- Third-party next (colorama, openpyxl, lxml)
- Local imports using absolute paths (e.g., `from armodel.models.M2...`)
- Alphabetical within groups

### Naming Conventions
- Classes: PascalCase (e.g., `ARXMLParser`, `AUTOSAR`, `RoleBasedDataAssignment`)
- Methods: camelCase (AUTOSAR standard, e.g., `getShortName`, `setRole`, `getUsedDataElement`)
- Functions: snake_case (e.g., `parse_xml`, `validate_input`)
- Variables: snake_case
- Constants: UPPER_CASE (e.g., `CATEGORY_TYPE_REFERENCE`)
- Private attributes: underscore prefix (e.g., `_appl_impl_type_maps`)
- Test classes: `Test` prefix (e.g., `TestRoleBasedDataAssignment`)
- Test methods: lowercase_with_underscores

### Type Hints
- Use Python 3.10+ union syntax with `|` (e.g., `str | None`)
- Use typing module for collection types (List, Dict, Optional, Set, Tuple)
- Use string literals for forward references
- Comments like `# type: List[Sdg]` for complex types (legacy)
- When adding type annotations, only reference classes that exist in the codebase
- Add proper imports for existing types or remove annotations for non-existent types to avoid F821 errors

### Formatting
- Indentation with spaces (4 spaces per level)
- Max line length: 79 characters (PEP 8 standard)
- Max docstring length: 72 characters
- Docstrings follow Google-style format
- Method chaining: setters return `self`
- Comment style: `# inline comments` (not doc comments)
- Use double quotes for strings, single quotes only when string contains double quotes

### Error Handling
- Raise `ValueError`, `NotImplementedError`, `TypeError`, `Exception`
- Use descriptive error messages
- Abstract classes raise TypeError in `__init__`
- Error logging via `self.logger.error()` when warning mode enabled
- Use `self.raiseError()`, `self.notImplemented()`, `self.raiseWarning()` parser methods
- Use exception chaining: `raise ... from e` to preserve context

### Abstract Base Classes
- Use `ABC` (Abstract Base Class) from `abc` module for abstract base classes
- Use `@abstractmethod` decorator for abstract methods
- Migrated from `ABCMeta` metaclass to `ABC` for better Python 3 compatibility
- Example: `class MyAbstractClass(ABC):` instead of `class MyAbstractClass(metaclass=ABCMeta):`

### Package Structure
Follow AUTOSAR M2 model hierarchy:
- **Leaf packages** (no subdirectories): Classes defined in single `.py` file
- **Non-leaf packages** (have subdirectories): Classes defined in `__init__.py`
- Classes MUST be importable from module path specified in `docs/requirements/mapping.json`

## Architecture

### Project Structure
```
src/armodel/
├── cli/                    # Command line tools (10 CLI utilities)
├── data_models/            # Data model definitions
├── lib/                    # Library functions
├── models/                 # AUTOSAR model definitions (M2 structure)
│   ├── M2/
│   │   ├── AUTOSARTemplates/  # AUTOSAR templates
│   │   │   ├── AbstractPlatform/
│   │   │   ├── AdaptivePlatform/
│   │   │   ├── AutosarTopLevelStructure/
│   │   │   ├── BswModuleTemplate/
│   │   │   ├── CommonStructure/
│   │   │   ├── DiagnosticExtract/
│   │   │   ├── ECUCDescriptionTemplate/
│   │   │   ├── ECUCParameterDefTemplate/
│   │   │   ├── EcuResourceTemplate/
│   │   │   ├── FeatureModelTemplate/
│   │   │   ├── GenericStructure/
│   │   │   ├── LogAndTraceExtract/
│   │   │   ├── SecurityExtractTemplate/
│   │   │   ├── SWComponentTemplate/
│   │   │   └── SystemTemplate/
│   │   ├── MSR/              # Meta-model semantic rules
│   │   └── N/                # Naming conventions
│   └── utils/                # Utility classes
├── parser/                 # Parser implementation
├── report/                 # Report generation
├── transformer/            # Transformer
└── writer/                 # Writer implementation
```

### Architecture Principles
- Follow AUTOSAR M2 schema structure for model organization
- Layered architecture: models/, parser/, writer/, cli/, lib/, data_models/, transformer/, report/
- Test structure mirrors source structure (tests/test_armodel/ mirrors src/armodel/)
- Use singleton pattern for `AUTOSAR` class via `getInstance()`
- Abstract base classes use `ABC` from `abc` module
- Separation of concerns between parser and writer modules

### Core Modules
- **parser.arxml_parser**: Main ARXML parser, based on `AbstractARXMLParser`
- **models.M2.AUTOSARTemplates.AutosarTopLevelStructure**: `AUTOSAR` class (singleton root), `AbstractAUTOSAR` class
- **writer.arxml_writer**: ARXML file writer
- **models/**: Contains all AUTOSAR data model classes

## AUTOSAR Specifics

### AUTOSAR Versions
- XML namespace: `http://autosar.org/schema/r4.0`
- Supported versions: 4.0.3 to R24-11 (especially R23-11)
- XSD mappings in `release_xsd_mappings` dictionary
- Follow AUTOSAR XML schema definitions
- MUST set AUTOSAR version before parsing/writing: `AUTOSAR.setARRelease("R23-11")`

### Supported Elements
- Components: ApplicationSwComponentType, CompositionSwComponentType, ServiceSwComponentType, SensorActuatorSwComponentType
- Port Interfaces: SenderReceiverInterface, ClientServerInterface, ModeSwitchInterface, ParameterInterface, NvDataInterface
- Data Types: ApplicationDataType, ImplementationDataType, SwBaseType, CompuMethod, DataConstr, Unit, PhysicalDimension, ApplicationArrayDataType
- Communication: AssemblySwConnector, DelegationSwConnector, CAN/LIN/FlexRay/Ethernet communication, SystemSignal, I-Signal
- Behavior: RunnableEntity, InitEvent, DataReceiveEvent, InternalBehavior, SwcImplementation, SwcModeSwitchEvent
- System: SystemSignal, SWC-TO-ECU-MAPPING, ECU-INSTANCE, ROOT-SOFTWARE-COMPOSITIONS
- BSW: BswModuleDescription, BswInternalBehavior, BswModuleEntity, BswEvent, BswCalledEntity, BswSchedulableEntity
- ECUC: EcucValueCollection, EcucModuleConfigurationValues, EcucContainerValue, EcucParameterValue
- Resource: MemorySection, StackUsage, HeapUsage, ExecutionTime, PerInstanceMemory
- End-to-End: EndToEndProtectionSet, EndToEndProtection, EndToEndDescription

## Important Notes

### Development Guidelines
- Python >= 3.5 required, CI supports 3.8, 3.9, 3.10, 3.11, 3.12
- Do NOT add comments unless asked
- Follow PEP 8 coding conventions
- When modifying code, check that ruff/flake8 passes (especially E9,F63,F7,F82 errors)
- Run tests after changes to ensure no regressions
- Test folder structure must match source folder structure
- Use singleton pattern for AUTOSAR class
- Abstract base classes use `ABC` from `abc` module (migrated from ABCMeta)
- UUID checking is enabled to detect duplicate UUIDs in ARXML files
- Same short names with different types can be added and located
- Float numbers in scientific notation are properly handled
- Boolean type values should not contain spaces

### AUTOSAR Singleton Management
```python
from armodel.models import AUTOSAR

# Get or create singleton instance
document = AUTOSAR.getInstance()

# Clear and create fresh instance
document = AUTOSAR.new()

# MUST set AUTOSAR version before parsing/writing
AUTOSAR.setARRelease("R23-11")  # or '4.0.3', 'R24-11', etc.
```

### Integration Tests
- 29 ARXML files tested with round-trip validation
- Parse → Write → Re-parse → Compare cycle
- Auto-detects AUTOSAR version from XSD schema (4.0.3 to R24-11)
- Extensible via `tests/integration_tests/config.yaml`

## CLI Tools

The library provides 10 command-line tools:

1. **format-xml**: Format XML files
2. **arxml-dump**: Dump all ARXML data to screen
3. **arxml-format**: Format ARXML files
4. **connector2xlsx**: Export SwConnector to Excel file
5. **connector-update**: Update SwConnector from Excel file
6. **armodel-component**: List all SwComponentType
7. **armodel-system-signal**: List all system signals
8. **armodel-memory-section**: Memory section operations
9. **armodel-file-list**: List files
10. **armodel-uuid-checker**: Validate UUIDs in ARXML files

## Recent Version History

### Version 1.9.2 (Current)
- Ongoing test coverage enhancement across all modules
- Package structure refactoring for case-sensitivity issues
- Improved deviation tracking and documentation

### Version 1.9.1
- Package Structure Refactoring
  - Fixed case-sensitivity issues with Components/ vs Components directories
  - Reorganized ECUC module imports to resolve ImportError
  - Improved AnyInstanceRef and CompositionSwComponentType package structure
- Test Coverage Enhancement
  - Ongoing effort to increase test coverage across all modules
  - Added tests for SwcInternalBehavior and NetworkManagement
- Documentation Improvements
  - Added comprehensive deviation documentation
  - Enhanced class hierarchy documentation
  - Improved coding rules documentation

### Version 1.9.0
- Testing Infrastructure
  - Added comprehensive integration test suite with round-trip validation
  - Added test runner script (`scripts/run_tests.py`) with colored output
  - Added pytest configuration (`pytest.ini`) with custom markers
  - Support for 2205+ unit tests and 29 integration test files
  - Added coverage reporting (HTML and terminal)

### Version 1.8.7
- Correct the base class of the BswEvent
- Export the RunnableEntity class
- Add more class support for getDestType

### Version 1.8.6
- Support NvProvideComSpec and NvRequireComSpec
- Improve ParameterAccess

### Version 1.8.5
- Reorganize the SwConnector class
- Raise error if short name of rootSwCompositionPrototype is invalid
- Support NvProvideComSpec
- Fix duplicate short name of ARPackage and Other ARElements

### Version 1.8.4
- Support BSW-SYNCHRONOUS-SERVER-CALL-POINT and RETURN-TYPE
- Add armodel-uuid-checker CLI tool
- Remove space in boolean type