# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

py-armodel is a Python library for parsing, manipulating, and writing AUTOSAR XML (ARXML) files. It provides comprehensive support for AUTOSAR model processing with various tools and CLI utilities for handling AUTOSAR data structures.

**Current Version**: 1.9.0  
**Python Requirements**: >= 3.5  
**License**: MIT  
**Repository**: http://github.com/melodypapa/py-armodel

## Architecture

The project is organized into the following key modules:

- **models**: Contains all AUTOSAR data model classes organized according to AUTOSAR XML schema (M2 structure)
  - M2/MSR: Meta-model metadata
  - M2/AUTOSARTemplates: Core AUTOSAR template models organized by domain
    - AutosarTopLevelStructure: AUTOSAR singleton and root model
    - ECUCDescriptionTemplate: ECUC configuration models
    - ECUCParameterDefTemplate: ECUC parameter definitions
    - CommonStructure: Common AUTOSAR elements (ARObject, Referrable, Identifiable, ServiceNeeds)
    - SWComponentTemplate: Software component models (AtomicSwComponentType, CompositionSwComponentType, etc.)
    - SystemTemplate: System-level models (SystemSignal, ECU-INSTANCE, etc.)
    - BswModuleTemplate: Basic Software module models (BswModuleDescription, BswBehavior, BswImplementation, BswInterfaces, BswOverview)
    - EcuResourceTemplate: ECU resource models
    - GenericStructure: Generic structure elements
    - DiagnosticExtract: Diagnostic models
  - utils: Utility classes (UUID management, etc.)

- **parser**: ARXML parsing functionality
  - arxml_parser.py: Main parser class for reading ARXML files
  - abstract_arxml_parser.py: Abstract base parser
  - connector_xlsx_parser.py: Excel connector parsing
  - excel_parser.py: Generic Excel parsing
  - file_parser.py: File parsing utilities

- **writer**: ARXML writing functionality
  - arxml_writer.py: Main writer class for writing ARXML files
  - abstract_arxml_writer.py: Abstract base writer

- **cli**: Command-line interface tools (10 tools total)
  - arxml_dump_cli.py: Dump ARXML data to screen
  - arxml_format_cli.py: Format ARXML files
  - connector2xlsx_cli.py: Export connectors to Excel
  - connector_update_cli.py: Update connectors from Excel
  - swc_list_cli.py: List software components
  - system_signal_cli.py: List system signals
  - memory_section_cli.py: Memory section operations
  - file_list_cli.py: File listing
  - uuid_checker_cli.py: UUID validation
  - format_xml_cli.py: XML formatting

- **data_models**: Additional data models
  - sw_connector.py: Software connector model

- **lib**: Library functions
  - cli_args_parser.py: CLI argument parsing
  - sw_component.py: Software component utilities
  - system_signal.py: System signal utilities

- **transformer**: Data transformation utilities
  - abstract.py: Abstract transformer base
  - admin_data.py: Admin data transformation

- **report**: Report generation
  - connector_xls_report.py: Connector Excel reports
  - excel_report.py: Generic Excel reports

## Development Commands

### Testing

Test files are located in `tests/test_armodel/` and `src/armodel/tests/` directories.

- Run all tests: `pytest`
- Run tests with coverage: `pytest --cov=armodel --cov-report term-missing`
- Run specific test file: `pytest tests/test_armodel/parser/test_arxml_parser.py`
- Run specific test method: `pytest tests/test_armodel/parser/test_arxml_parser.py::TestClass::test_method`
- Run with verbose output: `pytest -v`
- Run with print output: `pytest -s`

Using package.json scripts:
- `npm run pytest` - Run all tests
- `npm run pytest-cov` - Run tests with coverage
- `npm run flake8` - Run linting with flake8
- `npm run bswm-test` - Run BSW module test

### Linting

- Run Flake8: `npm run flake8` (or `flake8 --select=E9,F63,F7,F82 .`)
- CI runs both syntax checks and complexity checks

### Building

- Create distribution: `python setup.py bdist_wheel`
- Create source and wheel: `python setup.py sdist bdist_wheel --universal`
- Check distribution: `twine check dist/*`
- Upload to PyPI: `twine upload dist/*`

### Documentation

The project supports both Sphinx and MkDocs documentation:

**Sphinx:**
```bash
cd docs
make html
```

**MkDocs:**
```bash
mkdocs build
mkdocs serve
```

## Key CLI Tools

All CLI tools are registered as console_scripts in setup.py:

- `arxml-dump`: Dump all ARXML data to screen
- `arxml-format`: Format ARXML files
- `armodel-component` (aliased as `arxml-swc`): List all SWComponentType in the autosar model
- `connector2xlsx`: Export all SwConnector to Excel file
- `connector-update`: Update SwConnector from Excel file
- `armodel-system-signal`: List system signals
- `armodel-memory-section`: Memory section operations
- `armodel-file-list`: File listing
- `armodel-uuid-checker`: UUID validation
- `format-xml`: XML formatting

## Core Concepts

- **AUTOSAR Singleton**: The `AUTOSAR.getInstance()` pattern provides a singleton instance for managing the entire AUTOSAR model
- **M2 Structure**: Models follow the AUTOSAR M2 schema structure (M2/MSR/..., M2/AUTOSARTemplates/...)
- **ARPackage**: The primary container for organizing AUTOSAR elements hierarchically
- **Parser/Writer**: Separate modules for reading and writing ARXML files
- **Referrable/Identifiable**: Core base classes implementing AUTOSAR object identification and referencing
- **UUID Management**: Built-in UUID manager with duplicate UUID checking support
- **Type Mapping**: Support for mapping between application data types and implementation data types

## Supported AUTOSAR Elements



### Component Types
- ApplicationSwComponentType
- CompositionSwComponentType
- SensorActuatorSwComponentType
- ServiceSwComponentType

### Port Interfaces
- SenderReceiverInterface
- ClientServerInterface
- ModeSwitchInterface
- ParameterInterface
- NvDataInterface

### Data Types
- ApplicationDataType
- ImplementationDataType
- ApplicationRecordElement
- ApplicationArrayElement
- CompuMethod
- DataConstr
- Unit
- BaseTypes

### Communication
- AssemblySwConnector, DelegationSwConnector
- ServerComSpec, ModeSwitchReceiverComSpec, NvProvideComSpec, NvRequireComSpec
- CAN: CAN-FRAME, CAN-COMMUNICATION-CONNECTOR, CAN-CONTROLLER
- LIN: LIN-CLUSTER, LIN-UNCONDITIONAL-FRAME, LIN-MASTER
- FlexRay: FLEXRAY-CLUSTER, FLEXRAY-COMMUNICATION-CONNECTOR, FLEXRAY-FRAME
- Ethernet: ETHERNET-COMMUNICATION-CONNECTOR, ETHERNET-PHYSICAL-CHANNEL, SO-AD-CONFIG
- Network Management: NM-CONFIG, NM-NODE, NM-CLUSTER, CAN-NM-MODE, UDP-NM-CLUSTER
- End-to-End Protection: EndToEndProtectionSet, EndToEndProtection

### Behavior
- RunnableEntity
- InternalBehavior: SwcInternalBehavior, BswInternalBehavior
- Implementation: SwcImplementation, BswImplementation
- Events: InitEvent, DataReceiveEvent, SwcModeSwitchEvent, BswBackgroundEvent, BswDataReceivedEvent

### CommonStructure
- ServiceNeeds: Support for various AUTOSAR service needs (Diagnostic, Communication, etc.)
- ARObject: Base object for all AUTOSAR objects
- Referrable: Elements that can have unique short names
- Identifiable: Elements with unique identifiers and categories
- Implementation: Implementation-related elements
- InternalBehavior: Internal behavior specifications for components
- ResourceConsumption: Resource usage specifications (memory, stack, heap)
- ModeDeclaration: Mode declaration and switch specifications
- SwcBswMapping: Software component and BSW mapping elements

### Diagnostics
- DiagnosticConnection
- DiagnosticServiceTable
- DiagnosticEventNeeds
- DCM Needs: DiagnosticCommunicationManagerNeeds, DiagnosticRoutineNeeds, DiagnosticValueNeeds

### System
- SystemSignal, SystemSignalGroup
- SWC-TO-ECU-MAPPING, SW-MAPPINGS
- ECU-INSTANCE
- ROOT-SOFTWARE-COMPOSITIONS

### BSW Modules
- BswModuleDescription
- BswBehavior
- BswImplementation
- BswInterfaces
- BswSchedulableEntity
- BswCalledEntity
- BswModuleClientServerEntry
- BswModuleEntry
- BswModuleDependency

### ECUC Configuration
- EcucValueCollection
- EcucModuleConfigurationValues
- EcucContainerValue
- EcucParameterValue
- EcucModuleDef
- EcucParamDef (Boolean, String, Integer, Float, Enumeration)

## Testing Structure

Tests are located in `tests/test_armodel/` and `src/armodel/tests/` directories:

```
tests/test_armodel/
├── cli/                    # CLI tool tests
├── models/                 # Model class tests
│   ├── test_ar_object.py
│   ├── test_ar_package.py
│   ├── test_ar_ref.py
│   ├── test_bsw_behavior.py
│   ├── test_bsw_implementation.py
│   ├── test_bsw_interfaces.py
│   ├── test_bsw_module_template.py
│   ├── test_bsw_overview.py
│   ├── test_common_structure.py
│   ├── test_data_dictionary.py
│   ├── test_data_prototype.py
│   ├── test_datatype.py
│   ├── test_ECUCParameterDefTemplate.py
│   ├── test_general_structure.py
│   ├── test_Identifiable.py
│   ├── test_implementation.py
│   ├── test_m2_msr.py
│   ├── test_port_interface.py
│   ├── test_port_prototype.py
│   └── test_resource_consumption.py
├── parser/                 # Parser tests
│   ├── test_arxml_parser.py
│   ├── test_bsw_module_descriiption.py
│   ├── test_implementation_data_type.py
│   ├── test_rte_event.py
│   ├── test_runnable_entity.py
│   ├── test_sw_components.py
│   └── test_system.py
├── writer/                 # Writer tests
│   ├── test_abstract_arxml_writer.py
│   └── test_arxml_writer.py
└── requirements.txt        # Test dependencies
```

Test files in `test_files/` directory contain sample ARXML files for validation.

## Code Organization

- Data models are organized according to AUTOSAR specification structure
- Parser and writer follow separation of concerns
- CLI tools provide specific functionality access points
- Test files use sample ARXML files from the test_files directory
- Transformer module provides data transformation capabilities
- Report module generates Excel-based reports

## Dependencies

### Runtime Dependencies
- colorama: Cross-platform colored terminal output
- openpyxl: Excel file processing
- lxml: XML processing library

### Development Dependencies
- pytest: Unit testing framework
- pytest-cov: Code coverage tool
- flake8: Code style checking
- sphinx: Documentation generation

## Development Practices

- Follow AUTOSAR standard specifications (supports versions from 4.0.3 to R24-11)
- Use layered architecture: model layer, parser layer, writer layer separation
- Use singleton pattern for AUTOSAR class
- Built-in UUID manager with duplicate UUID checking
- Support for type mapping between application and implementation data types
- Follow Python PEP 8 coding conventions
- Use pytest for unit testing with high code coverage requirement
- Use flake8 for code quality checking
- Continuous Integration with GitHub Actions (Python 3.8-3.12)

## Continuous Integration

Project uses GitHub Actions for CI/CD:

- Python versions: 3.8, 3.9, 3.10, 3.11, 3.12
- CI workflow: `.github/workflows/python-package.yml`
- Steps: Install dependencies → Lint with flake8 → Run tests with pytest

## Key API Methods

### AUTOSAR Singleton Methods

- `AUTOSAR.getInstance()`: Get singleton instance
- `AUTOSAR.new()`: Clear and create new instance
- `AUTOSAR.setARRelease(version)`: Set AUTOSAR release version
- `getAtomicSwComponentTypes()`: Get all atomic software component types
- `getCompositionSwComponentTypes()`: Get all composition software component types
- `getSystemSignals()`: Get all system signals
- `findAtomicSwComponentType(short_name)`: Find specific atomic component
- `findSystemSignal(short_name)`: Find specific system signal
- `findPort(short_name)`: Find specific port
- `findVariableDataPrototype(short_name)`: Find specific data prototype
- `findImplementationDataType(short_name)`: Find specific implementation data type

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

## Recent Changes (Version 1.7.0 - 1.9.0)

Key updates in recent versions:

- Added system modeling support (SWC-TO-ECU-MAPPING, ECU-INSTANCE)
- Added communication protocol support for CAN, LIN, FlexRay, Ethernet
- Added diagnostic functionality (DiagnosticConnection, DiagnosticServiceTable)
- Added end-to-end protection support
- Added UUID checking CLI tool
- Added transformer module for data transformation
- Improved BSW module description support
- Improved ECUC configuration support
- Fixed various XML schema issues
- Improved findXXX methods for element lookup
- Added duplicate UUID checking
- Enhanced BSW module template functionality with comprehensive type hints and documentation
- Enhanced ServiceNeeds support with increased test coverage
- Improved DiagnosticContribution functionality
- Extended HwElementCategory for ECU resource template
- Enhanced GenericStructure with improved abstract structure and lifecycle support

## References

- AUTOSAR Official Website: https://www.autosar.org/
- Project GitHub: http://github.com/melodypapa/py-armodel
- PyPI Package: https://pypi.org/project/armodel/
- Documentation: https://py-armodel.readthedocs.io/