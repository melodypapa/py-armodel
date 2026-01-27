# Agent Guidelines for py-armodel

## Project Overview
Python library for AUTOSAR model support - ARXML parser and writer for automotive ECU software development.
**Version**: 1.9.0 | **Python**: >= 3.5 | **License**: MIT | **Repository**: http://github.com/melodypapa/py-armodel

## Build, Lint, and Test Commands

### Testing
- Run all tests: `pytest` or `npm run pytest`
- Run tests with coverage: `pytest --cov=armodel --cov-report term-missing` or `npm run pytest-cov`
- Run specific test file: `pytest tests/test_armodel/parser/test_arxml_parser.py`
- Run specific test method: `pytest tests/test_armodel/parser/test_arxml_parser.py::TestClass::test_method`
- Run tests with verbose output: `pytest -v`
- Run tests with print output: `pytest -s`

### Linting
- Run flake8: `npm run flake8` (or `flake8 --select=E9,F63,F7,F82 .`)
- CI runs both syntax checks and complexity checks with max-line-length=127

### Building
- Create distribution: `python setup.py bdist_wheel`
- Create source and wheel: `python setup.py sdist bdist_wheel --universal`
- Check distribution: `twine check dist/*`
- Upload to PyPI: `twine upload dist/*`

## Code Style Guidelines

### Imports
- Standard library first (typing, xml, os, logging, getopt, re)
- Third-party next (colorama, openpyxl, lxml)
- Local imports using relative notation (e.g., `from ..models.M2...`)
- Alphabetical within groups

### Naming Conventions
- Classes: PascalCase (e.g., `ARXMLParser`, `AUTOSAR`, `RoleBasedDataAssignment`)
- Methods: camelCase (e.g., `getShortName`, `setRole`, `getUsedDataElement`)
- Variables: camelCase or lowercase_with_underscores
- Constants: UPPER_CASE (e.g., `CATEGORY_TYPE_REFERENCE`)
- Private attributes: underscore prefix (e.g., `_appl_impl_type_maps`)
- Test classes: `Test` prefix (e.g., `TestRoleBasedDataAssignment`)
- Test methods: lowercase_with_underscores

### Type Hints
- Use typing module (List, Dict, Optional, etc.)
- Comments like `# type: List[Sdg]` for complex types
- When adding type annotations, only reference classes that exist in the codebase
- Add proper imports for existing types or remove annotations for non-existent types to avoid F821 errors

### Formatting
- Indentation with spaces
- Max line length: 127 characters
- Docstrings optional but follow standard format when used
- Method chaining: setters return `self`
- Comment style: `# inline comments` (not doc comments)

### Error Handling
- Raise `ValueError`, `NotImplementedError`, `TypeError`, `Exception`
- Use descriptive error messages
- Abstract classes raise TypeError in `__init__`
- Error logging via `self.logger.error()` when warning mode enabled
- Use `self.raiseError()`, `self.notImplemented()`, `self.raiseWarning()` parser methods

### Abstract Base Classes
- Use `ABC` (Abstract Base Class) from `abc` module for abstract base classes
- Use `@abstractmethod` decorator for abstract methods
- Migrated from `ABCMeta` metaclass to `ABC` for better Python 3 compatibility
- Example: `class MyAbstractClass(ABC):` instead of `class MyAbstractClass(metaclass=ABCMeta):`

## Architecture

### Project Structure
```
src/armodel/
├── cli/                    # Command line tools
├── data_models/            # Data model definitions
├── lib/                    # Library functions
├── models/                 # AUTOSAR model definitions (M2 structure)
│   └── M2/
│       ├── AUTOSARTemplates/  # AUTOSAR templates
│       └── utils/             # Utility classes
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

### Supported Elements
- Components: ApplicationSwComponentType, CompositionSwComponentType, ServiceSwComponentType, etc.
- Port Interfaces: SenderReceiverInterface, ClientServerInterface, ModeSwitchInterface, ParameterInterface, etc.
- Data Types: ApplicationDataType, ImplementationDataType, SwBaseType, CompuMethod, DataConstr, Unit, PhysicalDimension
- Communication: AssemblySwConnector, DelegationSwConnector, CAN/LIN/FlexRay/Ethernet communication
- Behavior: RunnableEntity, InitEvent, DataReceiveEvent, InternalBehavior, SwcImplementation
- System: SystemSignal, SWC-TO-ECU-MAPPING, ECU-INSTANCE, ROOT-SOFTWARE-COMPOSITIONS
- BSW: BswModuleDescription, BswInternalBehavior, BswModuleEntity, BswEvent
- ECUC: EcucValueCollection, EcucModuleConfigurationValues, EcucContainerValue, EcucParameterValue
- Resource: MemorySection, StackUsage, HeapUsage, ExecutionTime

## Important Notes
- Python >= 3.5 required, CI supports 3.8, 3.9, 3.10, 3.11, 3.12
- Do NOT add comments unless asked
- Follow PEP 8 coding conventions
- When modifying code, check that flake8 passes (especially E9,F63,F7,F82 errors)
- Run tests after changes to ensure no regressions
- Test folder structure must match source folder structure
- Use singleton pattern for AUTOSAR class
- Abstract base classes use `ABC` from `abc` module (migrated from ABCMeta)
- UUID checking is enabled to detect duplicate UUIDs in ARXML files
- Same short names with different types can be added and located
- Float numbers in scientific notation are properly handled
- Boolean type values should not contain spaces

## Recent Version History
- **1.9.0**: Current version
- **1.8.7**: Correct the base class of the BswEvent, Export the RunnableEntity class
- **1.8.6**: Support NvProvideComSpec and NvRequireComSpec, Improve ParameterAccess
- **1.8.5**: Reorganize the SwConnector class, Raise error if short name of rootSwCompositionPrototype is invalid
- **1.8.4**: Support BSW-SYNCHRONOUS-SERVER-CALL-POINT and RETURN-TYPE, Add armodel-uuid-checker CLI tool
