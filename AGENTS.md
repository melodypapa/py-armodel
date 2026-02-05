# Agent Guidelines for py-armodel

## Project Overview
Python library for AUTOSAR model support - ARXML parser and writer for automotive ECU software development.
**Version**: 1.9.2 | **Python**: >= 3.5 (CI supports 3.8-3.13) | **License**: MIT | **Repository**: http://github.com/melodypapa/py-armodel

**Current Git Branch**: feat/v2-coding-rules-compliance
**Latest Commit**: 9e58876 - feat(v2): Apply V2 coding rules compliance and fix imports

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

#### Type Checking: MyPy
```bash
# Run mypy type checking
mypy src/armodel/v2/models/

# Run mypy with specific configuration
mypy --config-file pyproject.toml src/armodel/v2/models/
```

#### Legacy Linter: Flake8
```bash
# Run flake8 for critical errors only
flake8 --select=E9,F63,F7,F82 .
```

**Note**: CI runs ruff and mypy with comprehensive rules. Line length is 79 characters (PEP 8 standard), with CI warnings at 127.

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

### Development Scripts
The `scripts/` directory contains utility scripts for development:
- `run_tests.py`: Comprehensive test runner with colored output
- `scan_existing_classes.py`: Scan and catalog existing classes
- `compare-package-implementation.py`: Compare package structure
- `deviation-class-hierarchy.py`: Generate class hierarchy deviation reports
- `deviation-package.py`: Generate package structure deviation reports
- `fix-package-implementation.py`: Fix package structure issues
- `check_v2_coding_rules.py`: Check V2 models against coding rules
- `fix_v2_coding_rules.py`: Auto-fix V2 coding rule violations
- `validate_v2.py`: Validate V2 model structure
- `refactor_commonstructure_v2.py`: Refactor CommonStructure for V2
- `add_all_declarations.py`: Add __all__ declarations
- `add_init_all.py`: Add __init__.py files
- `fix_models_v2_imports.py`: Fix imports in V2 models
- `fix_relative_imports.py`: Fix relative imports
- `create_v2_structure.py`: Create V2 directory structure
- `lib/`: Support library for scripts (code_generator, code_utils, package_loader, test_generator, type_resolver)

## Code Style Guidelines

### Comprehensive Reference
For detailed coding standards, see: `docs/development/coding_rules.md`

### V2-Specific Coding Rules

The project is migrating to a V2 model structure with enhanced coding standards. Key differences:

#### V2 Model Structure
- **Location**: `src/armodel/v2/models/`
- **Purpose**: Refactored AUTOSAR M2 model with improved code organization
- **Status**: Active development on `feat/v2-coding-rules-compliance` branch
- **Key Features**:
  - Enhanced type hints with strict mypy checking
  - Improved import organization
  - Better separation of concerns
  - Comprehensive deviation tracking

#### V2 Coding Rules (CODING_RULE_V2_*)
- **CODING_RULE_V2_00001**: V2 models must use strict type hints
- **CODING_RULE_V2_00002**: V2 models must pass mypy checks
- **CODING_RULE_V2_00003**: V2 models must follow ruff configuration
- See `docs/development/coding_rules.md` for complete V2-specific rules

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

### Package Structure (CRITICAL)
Follow AUTOSAR M2 model hierarchy with strict conventions:

**Leaf Packages (no subdirectories):**
- Classes defined in a single `.py` file
- Package name = filename (without `.py` extension)
- File name typically matches the primary class name or package concept
- Import path includes the filename as the package name

```python
# File: src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ImplementationDataTypes.py
# This is a leaf package (no subdirectories)

from abc import ABCMeta
from typing import List

class AbstractImplementationDataTypeElement(Identifiable):
    """Base class for implementation data type elements."""
    pass

class ImplementationDataTypeElement(AbstractImplementationDataTypeElement):
    """Implementation data type element class."""
    pass

class ImplementationDataType(AbstractImplementationDataType):
    """Implementation data type class."""
    pass

# Import statement:
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ImplementationDataTypes import ImplementationDataType
```

**Non-Leaf Packages (have subdirectories):**
- Classes defined in `__init__.py` of the directory
- Package name = directory name
- May contain multiple subdirectories with their own classes

```python
# File: src/armodel/models/M2/AUTOSARTemplates/CommonStructure/__init__.py
# This is a non-leaf package (has subdirectories)

from abc import ABCMeta
from typing import List

class ValueSpecification(ARObject, metaclass=ABCMeta):
    """Value specification base class."""
    pass

class ConstantSpecification(ARElement):
    """Constant specification class."""
    pass

# Import statement:
from armodel.models.M2.AUTOSARTemplates.CommonStructure import ValueSpecification
```

**Package Structure Decision Tree:**
```
Does the package contain subdirectories?
│
├── YES → Non-Leaf Package
│   - Create directory with __init__.py
│   - Define classes in __init__.py
│   - Package name = directory name
│
└── NO  → Leaf Package
    - Create single .py file
    - Define all classes in that .py file
    - Package name = filename (without .py)
```

**CODING_RULE_STYLE_00008: Class Location and Package Structure**

**Maturity**: accept

**Rule**: Classes must be located in the correct package according to AUTOSAR M2 model hierarchy.

**Key Principles:**
- **Leaf Package Pattern**: When a package contains only a single primary class (or a small set of closely related classes), create a leaf package with a `.py` file named after the class
- **Non-Leaf Package Pattern**: When a package contains multiple subdirectories or serves as a namespace for multiple classes, define classes in `__init__.py`
- **Module Naming**: Leaf package modules should NOT use the class name as a subdirectory; the class should be defined directly in the module file

**Examples:**

**Correct - Leaf Package:**
```
src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ImplementationDataTypes.py
# Defines: ImplementationDataType, AbstractImplementationDataTypeElement, etc.
# Import: from armodel.models.M2.AUTOSARTemplates.CommonStructure.ImplementationDataTypes import ImplementationDataType
```

**Incorrect - Avoid double nesting:**
```
src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ImplementationDataTypes/ImplementationDataTypes.py
# This creates unnecessary nesting and violates the leaf package pattern
```

**CODING_RULE_STYLE_00009: Class Export and Module Organization**

**Maturity**: accept

**Rule**: Classes must be properly exported from their modules and be importable via the expected AUTOSAR M2 path.

**Key Principles:**
- **Proper Export**: All classes defined in a module must be exportable via `__all__` or direct import
- **Duplicate Detection**: No duplicate class names should exist across the codebase (enforced by deviation tracking)
- **Mapping Compliance**: Classes MUST be importable from the module path specified in `docs/requirements/mapping.json`

**Module Export Pattern:**

```python
# File: src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ImplementationDataTypes.py

from abc import ABCMeta
from typing import List

class AbstractImplementationDataTypeElement(Identifiable):
    """Base class for implementation data type elements."""
    pass

class ImplementationDataTypeElement(AbstractImplementationDataTypeElement):
    """Implementation data type element class."""
    pass

class ImplementationDataType(AbstractImplementationDataType):
    """Implementation data type class."""
    pass

# Export all classes
__all__ = [
    'AbstractImplementationDataTypeElement',
    'ImplementationDataTypeElement',
    'ImplementationDataType',
]
```

**Package Export Pattern (for non-leaf packages):**

```python
# File: src/armodel/models/M2/AUTOSARTemplates/CommonStructure/__init__.py

from abc import ABCMeta
from typing import List

class ValueSpecification(ARObject, metaclass=ABCMeta):
    """Value specification base class."""
    pass

# Import and re-export from submodules
from .ImplementationDataTypes import ImplementationDataType
from .SwDataDefProps import SwDataDefProps

__all__ = [
    'ValueSpecification',
    'ImplementationDataType',
    'SwDataDefProps',
]
```

**Class Mapping Compliance:**
- Classes MUST be importable from the module path specified in `docs/requirements/mapping.json`
- Run `test_class_mapping.py` integration test to verify compliance
- Deviation reports are generated in `reports/deviation_*.md`

**Current Deviation Status (as of v1.9.2):**
- ✓ **Match**: 610 classes correctly implemented
- ✗ **Missing**: 1189 classes documented but not found
- ⚠ **Path Mismatch**: 87 classes in wrong location
- + **Extra**: 207 undocumented classes
- See `reports/deviation_package.md` for detailed deviation tracking

## Architecture

### Project Structure
```
src/armodel/
├── cli/                    # Command line tools (10 CLI utilities)
├── data_models/            # Data model definitions
├── lib/                    # Library functions
├── models/                 # AUTOSAR model definitions (V1 - legacy)
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
├── v2/                     # V2 package (refactored architecture)
│   └── models/              # AUTOSAR model definitions (V2 - refactored)
│       ├── M2/
│       │   ├── AUTOSARTemplates/  # AUTOSAR templates (V2 structure)
│       │   ├── MSR/              # Meta-model semantic rules (V2)
│       │   └── N/                # Naming conventions (V2)
│       └── utils/                # Utility classes (V2)
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
- V2 models represent a refactored architecture with improved code organization

### Core Modules
- **parser.arxml_parser**: Main ARXML parser, based on `AbstractARXMLParser`
- **models.M2.AUTOSARTemplates.AutosarTopLevelStructure**: `AUTOSAR` class (singleton root), `AbstractAUTOSAR` class
- **v2.models.M2.AUTOSARTemplates**: Refactored AUTOSAR templates (in development)
- **writer.arxml_writer**: ARXML file writer
- **models/**: Contains all AUTOSAR data model classes (V1 - legacy)
- **v2/models/**: Contains refactored AUTOSAR data model classes (V2 - active development)

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
- Python >= 3.5 required, CI supports 3.8, 3.9, 3.10, 3.11, 3.12, 3.13
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
- Package structure migration is ongoing (see docs/plans/2026-02-01-package-structure-migration-design.md)
- **Enum Usage**: Use AREnum base class instead of Python enum.Enum for AUTOSAR compliance
- **Class Location**: Follow CODING_RULE_STYLE_00008 for proper class placement in package structure
- **Class Export**: Follow CODING_RULE_STYLE_00009 for proper class exports and module organization
- **Duplicate Detection**: Run deviation tracking to identify duplicate class names before committing
- **V2 Development**: Currently developing V2 models on `feat/v2-coding-rules-compliance` branch with enhanced coding standards

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

### Recent Refactoring Activities

#### V2 Model Development (Current - 2026)
**Purpose**: Refactor AUTOSAR M2 model structure with enhanced coding standards and better organization.

**Status**: Active development on `feat/v2-coding-rules-compliance` branch

**Key Features**:
- Enhanced type hints with strict mypy checking
- Improved import organization following ruff configuration
- Better separation of concerns
- Comprehensive deviation tracking
- Automated coding rule validation

**Related Files**:
- `src/armodel/v2/models/`: V2 model structure
- `docs/development/coding_rules.md`: V2-specific coding rules
- `scripts/check_v2_coding_rules.py`: Validate V2 against coding rules
- `scripts/fix_v2_coding_rules.py`: Auto-fix V2 coding rule violations
- `scripts/validate_v2.py`: Validate V2 model structure

**Recent Commits**:
- 9e58876: feat(v2): Apply V2 coding rules compliance and fix imports
- 9c18565: style(v2): Auto-fix ruff import formatting in V2 models
- f251580: docs(v2): Add V2-specific coding rules to coding_rules.md

#### Enum to AREnum Conversion (v1.9.2)
**Purpose**: Improve AUTOSAR compliance by replacing Python's standard `enum.Enum` with a custom `AREnum` base class.

**Benefits**:
- Better alignment with AUTOSAR M2 model specifications
- Enhanced serialization and deserialization for ARXML files
- Improved type safety and validation
- Consistent enum handling across the codebase

**Impact**:
- All enum definitions migrated to use `AREnum` base class
- Parser and writer updated to handle AREnum instances
- Test suite updated to validate enum conversions
- Backward compatibility maintained where possible

**Example**:
```python
# Before (Python Enum)
from enum import Enum

class BswEntryKindEnum(Enum):
    PROVIDED = "PROVIDED"
    REQUIRED = "REQUIRED"

# After (AUTOSAR AREnum)
from armodel.models.base import AREnum

class BswEntryKindEnum(AREnum):
    PROVIDED = "PROVIDED"
    REQUIRED = "REQUIRED"
```

#### Class Relocation for Coding Rule Compliance (v1.9.2)
**Purpose**: Ensure all classes are properly located according to AUTOSAR M2 model hierarchy and coding rules.

**Affected Classes**:
- `CollectableElement`: Relocated to proper module location
- `EndToEndTransformationComSpecProps`: Fixed module path
- `FlexrayChannelName`, `CommunicationDirectionType`, `IPduSignalProcessingEnum`: Enumeration relocation
- `ExternalTriggeringPointIdent`, `AtpBlueprintMapping`: Class relocation
- `EcuInstance`, `SwcToEcuMapping`: Class relocation
- `PackageableElement`: Added to ARPackage module exports

**Process**:
1. Identify classes violating CODING_RULE_STYLE_00008 or CODING_RULE_STYLE_00009
2. Create new module structure following AUTOSAR M2 hierarchy
3. Move classes to correct locations
4. Update imports across the codebase
5. Run tests to ensure no regressions
6. Update deviation reports
7. Commit with descriptive message

**Verification**:
- Run `python scripts/deviation-package.py` to check for path mismatches
- Run `pytest tests/integration_tests/test_class_mapping.py` to verify class mapping
- Run `ruff check .` to ensure code quality

### Development Activities

#### V2 Model Development (Current)
- **Goal**: Refactor AUTOSAR M2 model with enhanced coding standards
- **Status**: Active development on `feat/v2-coding-rules-compliance` branch
- **Changes**:
  - Enhanced type hints with strict mypy checking
  - Improved import organization following ruff configuration
  - Better separation of concerns
  - Comprehensive deviation tracking
  - Automated coding rule validation
- **Related Commits**: 9e58876, 9c18565, f251580

#### Enum Refactoring (v1.9.2)
- **Goal**: Convert Python Enum to AUTOSAR AREnum for better AUTOSAR compliance
- **Status**: Completed
- **Changes**:
  - Replaced Python `enum.Enum` with custom `AREnum` base class
  - Updated all enum-related code to use AREnum
  - Improved compatibility with AUTOSAR standards
- **Related Commits**: 3c86ebf, 16fcd79

#### Package Structure Refactoring (Ongoing)
- **Design Document**: `docs/plans/2026-02-01-package-structure-migration-design.md`
- **Goal**: Align Python package structure with AUTOSAR M2 model hierarchy
- **Status**: Ongoing - addressing path mismatches and missing classes
- **Recent Changes**:
  - Relocated CollectableElement to comply with coding rules
  - Fixed EndToEndTransformationComSpecProps location
  - Fixed FlexrayChannelName, CommunicationDirectionType, IPduSignalProcessingEnum
  - Fixed ExternalTriggeringPointIdent and AtpBlueprintMapping
  - Fixed EcuInstance and SwcToEcuMapping
  - Added PackageableElement to ARPackage module exports
- **Tools**:
  - `scripts/scan_existing_classes.py`: Scan and catalog existing classes
  - `scripts/compare-package-implementation.py`: Compare package structure
  - `scripts/fix-package-implementation.py`: Fix package structure issues
- **Reports**: Generated in `reports/deviation_*.md`

#### Deviation Tracking
The project maintains comprehensive deviation tracking between documented AUTOSAR M2 model and actual implementation:
- **Package Deviations**: `reports/deviation_package.md` (610 match, 1189 missing, 87 path mismatch, 207 extra)
- **Class Hierarchy**: `reports/deviation_class_hierarchy_*.md`
- **Class Mapping**: `reports/class_mapping_report.md`
- Run `python scripts/deviation-package.py` to regenerate reports

#### AUTOSAR M2 Class Generation
- **Design Document**: `docs/plans/2025-01-31-autosar-m2-class-generation-design.md`
- **Implementation Document**: `docs/plans/2025-01-31-autosar-m2-class-generation-implementation.md`
- **Goal**: Automated generation of AUTOSAR M2 model classes from specification documents
- **Status**: Partially implemented - ongoing development

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
- **Enum Refactoring**
  - Convert Python Enum to AUTOSAR AREnum for better AUTOSAR compliance
  - Refactor all enum-related code to use AREnum base class
- **Package Structure Refactoring**
  - Relocate classes to comply with CODING_RULE_STYLE_00008 and CODING_RULE_STYLE_00009
  - Fix CollectableElement location in deviation report
  - Clarify connection between CODING_RULE_STYLE_00008 and CODING_RULE_STYLE_00009
- **Test Coverage Enhancement**
  - Ongoing test coverage enhancement across all modules
  - Enhanced class mapping validation and reporting
- **Documentation Improvements**
  - Updated AGENTS.md with detailed coding rules explanations
  - Improved deviation tracking and documentation
- **Development Tools**
  - Added duplicate detection for CODING_RULE_STYLE_00009 compliance
  - Development scripts added for package structure analysis and fixes

### Version 1.9.1
- **Package Structure Refactoring**
  - Fixed case-sensitivity issues with Components/ vs Components directories
  - Reorganized ECUC module imports to resolve ImportError
  - Improved AnyInstanceRef and CompositionSwComponentType package structure
- **Test Coverage Enhancement**
  - Ongoing effort to increase test coverage across all modules
  - Added tests for SwcInternalBehavior and NetworkManagement
- **Documentation Improvements**
  - Added comprehensive deviation documentation
  - Enhanced class hierarchy documentation
  - Improved coding rules documentation

### Version 1.9.0
- **Testing Infrastructure**
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

## V2 Migration Guide

The project is migrating to a V2 model structure with enhanced coding standards. This section provides guidance for working with V2 models.

### Key Differences

#### V1 Models (Legacy)
- **Location**: `src/armodel/models/`
- **Type Hints**: Basic, no strict checking
- **Import Organization**: Manual, less consistent
- **Linting**: Flake8 for critical errors only
- **Status**: Stable, in production use

#### V2 Models (In Development)
- **Location**: `src/armodel/v2/models/`
- **Type Hints**: Comprehensive, strict mypy checking
- **Import Organization**: Automated via ruff, highly consistent
- **Linting**: Ruff + mypy for comprehensive quality checks
- **Status**: Active development on `feat/v2-coding-rules-compliance` branch

### Working with V2 Models

#### Checking V2 Coding Rules
```bash
# Run V2 coding rules checker
python scripts/check_v2_coding_rules.py

# Run mypy type checking
mypy src/armodel/v2/models/

# Run ruff linting
ruff check src/armodel/v2/models/
```

#### Fixing V2 Coding Rules
```bash
# Auto-fix V2 coding rule violations
python scripts/fix_v2_coding_rules.py

# Auto-fix ruff issues
ruff check --fix src/armodel/v2/models/
```

#### Validating V2 Structure
```bash
# Validate V2 model structure
python scripts/validate_v2.py
```

### V2-Specific Coding Rules

See `docs/development/coding_rules.md` for complete V2-specific coding rules:

- **CODING_RULE_V2_00001**: V2 models must use strict type hints
- **CODING_RULE_V2_00002**: V2 models must pass mypy checks
- **CODING_RULE_V2_00003**: V2 models must follow ruff configuration

### Branch Management

- **Main Branch**: Contains V1 models (stable, production)
- **feat/v2-coding-rules-compliance Branch**: Contains V2 models (in development)

When working on V2 features:
1. Create feature branches from `feat/v2-coding-rules-compliance`
2. Follow V2 coding rules strictly
3. Run `check_v2_coding_rules.py` before committing
4. Ensure mypy and ruff checks pass
5. Update documentation as needed

### Future Plans

The V2 migration is ongoing. Key milestones:

- [ ] Complete V2 model structure refactoring
- [ ] Achieve 100% coding rules compliance in V2
- [ ] Migrate all tests to V2
- [ ] Merge V2 into main branch
- [ ] Deprecate V1 models

For detailed migration plans, see:
- `docs/plans/2026-02-01-package-structure-migration-design.md`
- `docs/development/coding_rules.md`