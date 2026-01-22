# Agent Guidelines for py-armodel

## Project Overview

py-armodel is a Python library for AUTOSAR model support. AUTOSAR (AUTomotive Open System ARchitecture) is the standard architecture for automotive electronic control unit (ECU) software development.

This project provides a complete ARXML (AUTOSAR XML) file parser and writer, supporting parsing and generation of various AUTOSAR elements. It implements various data structures, interfaces, components, and communication patterns defined in the AUTOSAR standard.

**Current Version**: 1.9.0  
**Python Requirement**: >= 3.5  
**License**: MIT  
**Repository**: http://github.com/melodypapa/py-armodel

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
- Standard library imports first (typing, xml, os, logging, getopt, re)
- Third-party imports next (colorama, openpyxl, lxml)
- Local imports using relative notation (e.g., `from ..models.M2...`)
- Imports organized alphabetically within groups
- Long import lists are common due to extensive AUTOSAR model classes

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
- Type hints are used but not comprehensive
- Comments like `# type: List[Sdg]` for complex types
- When adding type annotations, only reference classes that exist in the codebase
- Add proper imports for existing types or remove annotations for non-existent types to avoid F821 errors

### Formatting
- Indentation with spaces
- Max line length: 127 characters (per CI flake8 config)
- Docstrings are optional but follow standard format when used
- Method chaining: setters return `self`
- Comment style: `# inline comments` (not doc comments)

### Error Handling
- Raise `ValueError`, `NotImplementedError`, `TypeError`, `Exception`
- Use descriptive error messages
- Abstract classes raise TypeError in `__init__`
- Error logging via `self.logger.error()` when warning mode enabled
- Use `self.raiseError()`, `self.notImplemented()`, `self.raiseWarning()` parser methods

## Architecture

### Project Structure

```
src/armodel/
├── cli/                    # Command line tools
│   ├── arxml_dump_cli.py      # ARXML data dump
│   ├── arxml_format_cli.py    # ARXML formatting
│   ├── connector2xlsx_cli.py  # Connector export to Excel
│   ├── connector_update_cli.py # Update connectors from Excel
│   ├── swc_list_cli.py        # Software component list
│   ├── system_signal_cli.py   # System signal list
│   ├── memory_section_cli.py  # Memory section management
│   ├── file_list_cli.py       # File list
│   ├── uuid_checker_cli.py    # UUID checker
│   └── format_xml_cli.py      # XML formatting
├── data_models/            # Data model definitions
│   └── sw_connector.py        # Software connector model
├── lib/                    # Library functions
│   ├── cli_args_parser.py     # CLI argument parser
│   ├── sw_component.py        # Software component utilities
│   └── system_signal.py       # System signal utilities
├── models/                 # AUTOSAR model definitions
│   ├── M2/                    # M2 model layer
│   │   ├── AUTOSARTemplates/  # AUTOSAR templates
│   │   │   ├── AutosarTopLevelStructure.py
│   │   │   ├── ECUCDescriptionTemplate.py
│   │   │   ├── ECUCParameterDefTemplate.py
│   │   │   ├── CommonStructure/    # Common structure
│   │   │   ├── BswModuleTemplate/  # BSW module template
│   │   │   ├── SWComponentTemplate/ # Software component template
│   │   │   ├── SystemTemplate/     # System template
│   │   │   ├── EcuResourceTemplate/ # ECU resource template
│   │   │   ├── GenericStructure/   # Generic structure
│   │   │   └── DiagnosticExtract/  # Diagnostic extract
│   │   └── MSR/                # MSR metadata
│   └── utils/                 # Utility classes
│       └── uuid_mgr.py         # UUID manager
├── parser/                 # Parser implementation
│   ├── arxml_parser.py          # ARXML parser
│   ├── abstract_arxml_parser.py # Abstract parser base class
│   ├── connector_xlsx_parser.py # Connector Excel parser
│   ├── excel_parser.py          # Excel parser
│   └── file_parser.py           # File parser
├── report/                 # Report generation
│   ├── connector_xls_report.py  # Connector Excel report
│   └── excel_report.py          # Excel report
├── transformer/            # Transformer
│   ├── abstract.py              # Abstract transformer
│   └── admin_data.py            # Admin data transformer
└── writer/                 # Writer implementation
    ├── arxml_writer.py          # ARXML writer
    └── abstract_arxml_writer.py # Abstract writer base class
```

### Architecture Principles
- Follow AUTOSAR M2 schema structure for model organization
- Layered architecture: models/ (M2 structure), parser/, writer/, cli/, lib/, data_models/, transformer/, report/
- Test structure mirrors source structure (tests/models/ mirrors src/models/)
- Use singleton pattern for `AUTOSAR` class via `getInstance()`
- Abstract base classes use ABCMeta metaclass
- Separation of concerns between parser and writer modules

### Core Modules
- **parser.arxml_parser**: Main ARXML parser, based on `AbstractARXMLParser`
- **models.M2.AUTOSARTemplates.AutosarTopLevelStructure**: 
  - `AUTOSAR` class: Singleton root object
  - `AbstractAUTOSAR` class: Provides basic AUTOSAR functionality
- **writer.arxml_writer**: ARXML file writer
- **models/**: Contains all AUTOSAR data model classes

## AUTOSAR Specifics

### AUTOSAR Versions
- XML namespace: `http://autosar.org/schema/r4.0`
- Supported versions: 4.0.3 to R24-11 (especially R23-11)
- XSD mappings in `release_xsd_mappings` dictionary
- Follow AUTOSAR XML schema definitions
- Use proper AUTOSAR element types and references

### Supported AUTOSAR Elements

#### Component Types
- **Atomic Components**: ApplicationSwComponentType, SensorActuatorSwComponentType, ComplexDeviceDriverSwComponentType, EcuAbstractionSwComponentType
- **Composition Components**: CompositionSwComponentType
- **Service Components**: ServiceSwComponentType, ServiceProxySwComponentType
- **NV Block Components**: NvBlockSwComponentType

#### Port Interfaces
- **Sender-Receiver Interface**: SenderReceiverInterface
- **Client-Server Interface**: ClientServerInterface
- **Mode Switch Interface**: ModeSwitchInterface
- **Parameter Interface**: ParameterInterface
- **NV Data Interface**: NvDataInterface
- **Trigger Interface**: TriggerInterface
- **Service Interface**: ServiceInterface
- **Diagnostic Interfaces**: DiagnosticDataElementInterface, DiagnosticRoutineInterface, DiagnosticServiceInterface

#### Data Types
- **Application Data Types**: ApplicationDataType, ApplicationArrayDataType, ApplicationCompositeDataType, ApplicationPrimitiveDataType
- **Implementation Data Types**: ImplementationDataType, AbstractImplementationDataType
- **Base Types**: SwBaseType, BaseType
- **Record and Array Types**: ApplicationRecordElement, ApplicationArrayElement
- **Computation Methods**: CompuMethod
- **Data Constraints**: DataConstr
- **Units**: Unit, UnitGroup
- **Physical Dimensions**: PhysicalDimension

#### Communication
- **Port Connectors**: AssemblySwConnector, DelegationSwConnector
- **Communication Specifications**: ServerComSpec, ModeSwitchReceiverComSpec, NvProvideComSpec, NvRequireComSpec
- **Network Management**: NM-CONFIG, NM-NODE, NM-CLUSTER, CAN-NM-MODE, UDP-NM-CLUSTER
- **CAN Communication**: CAN-FRAME, CAN-COMMUNICATION-CONNECTOR, CAN-CONTROLLER, CAN-TP-CONFIG
- **LIN Communication**: LIN-CLUSTER, LIN-UNCONDITIONAL-FRAME, LIN-MASTER, LIN-TP-CONFIG
- **FlexRay Communication**: FLEXRAY-CLUSTER, FLEXRAY-COMMUNICATION-CONNECTOR, FLEXRAY-FRAME, FLEXRAY-PHYSICAL-CHANNEL
- **Ethernet Communication**: ETHERNET-COMMUNICATION-CONNECTOR, ETHERNET-PHYSICAL-CHANNEL, SO-AD-CONFIG
- **End-to-End Protection**: EndToEndProtectionSet, EndToEndProtection
- **Secure Communication**: SECURED-I-PDU, SECURE-COMMUNICATION-PROPS-SET

#### Behavior
- **Runnable Entities**: RunnableEntity
- **Events**: InitEvent, DataReceiveEvent, SwcModeSwitchEvent, BswBackgroundEvent, BswDataReceivedEvent, BswExternalTriggerOccurredEvent, BswInternalTriggerOccurredEvent, BswModeSwitchEvent, BswModeSwitchedAckEvent, BswOperationInvokedEvent, BswAsynchronousServerCallReturnsEvent, BswInterruptEvent, BswOsTaskExecutionEvent
- **Internal Behavior**: InternalBehavior, SwcInternalBehavior, BswInternalBehavior
- **Implementation**: SwcImplementation, BswImplementation
- **BSW Entities**: BswCalledEntity, BswSchedulableEntity, BswInterruptEntity
- **Call Points**: ServerCallPoint, SynchronousServerCallPoint, AsynchronousServerCallPoint, BswDirectCallPoint, BswSynchronousServerCallPoint, BswAsynchronousServerCallPoint

#### Diagnostic
- **Diagnostic Connection**: DiagnosticConnection
- **Service Table**: DiagnosticServiceTable
- **Event Needs**: DiagnosticEventNeeds, DiagnosticEventInfoNeeds
- **DCM Needs**: DiagnosticCommunicationManagerNeeds, DiagnosticRoutineNeeds, DiagnosticValueNeeds
- **Debounce Algorithms**: DiagEventDebounceAlgorithm, DiagEventDebounceCounterBased, DiagEventDebounceTimeBased, DiagEventDebounceMonitorInternal

#### System
- **System Signal**: SystemSignal, SystemSignalGroup
- **System Mapping**: SWC-TO-ECU-MAPPING, SW-MAPPINGS, ECU-RESOURCE-MAPPINGS, SW-IMPL-MAPPINGS
- **ECU Instance**: ECU-INSTANCE
- **Root Software Composition**: ROOT-SOFTWARE-COMPOSITIONS

#### BSW Modules
- **BSW Module Description**: BswModuleDescription, BswModuleDependency
- **BSW Entries**: BswModuleEntry, BswModuleClientServerEntry
- **BSW Behavior**: BswInternalBehavior, BswModuleEntity, BswEvent, BswScheduleEvent, BswTimingEvent, BswBackgroundEvent
- **BSW Policies**: BswExclusiveAreaPolicy, BswModeReceiverPolicy, BswModeSenderPolicy, BswDataReceptionPolicy, BswQueuedDataReceptionPolicy

#### ECUC Configuration
- **ECUC Collection**: EcucValueCollection
- **ECUC Module Configuration**: EcucModuleConfigurationValues
- **ECUC Container Values**: EcucContainerValue
- **ECUC Parameter Values**: EcucParameterValue
- **ECUC Module Definitions**: EcucModuleDef, EcucParamDef (Boolean, String, Integer, Float, Enumeration)

#### Resource Consumption
- **Memory Sections**: MemorySection, MemorySectionLocation
- **Stack Usage**: StackUsage, WorstCaseStackUsage, MeasuredStackUsage, RoughEstimateStackUsage
- **Heap Usage**: HeapUsage, WorstCaseHeapUsage, MeasuredHeapUsage, RoughEstimateHeapUsage
- **Execution Time**: ExecutionTime, AnalyzedExecutionTime, MeasuredExecutionTime, SimulatedExecutionTime, RoughEstimateOfExecutionTime

#### Measurement and Calibration
- **MC Support**: McSupportData, McDataInstance, McSwEmulationMethodSupport, McParameterElementGroup
- **MC Groups**: McGroup, McFunction

#### Service Needs
- **General Service Needs**: ServiceNeeds, ServiceDependency, BswServiceDependency
- **Specific Needs**: NvBlockNeeds, SupervisedEntityNeeds, ComMgrUserNeeds, EcuStateMgrUserNeeds, CryptoServiceNeeds, DltUserNeeds, SyncTimeBaseMgrUserNeeds, DiagnosticCapabilityElement, FunctionInhibitionNeeds, DoIpServiceNeeds, ErrorTracerNeeds, HardwareTestNeeds

#### Miscellaneous
- **Mode Declaration**: ModeDeclarationGroup, ModeDeclaration, ModeTransition, ModeErrorBehavior
- **Trigger Declaration**: Trigger, MultidimensionalTime, BswInternalTriggeringPoint
- **Value Specifications**: ValueSpecification, NumericalValueSpecification, ArrayValueSpecification, RecordValueSpecification
- **Calibration**: SwAxisType, SwRecordLayout, SwAxisCont, SwValueCont, SwCalprmAxisSet, SwGenericAxisParamType
- **Data Properties**: SwDataDefProps, SwTextProps, SwBitRepresentation, SwAddrMethod
- **Constants**: ConstantSpecification, ConstantSpecificationMappingSet

## CLI Tools

### arxml-dump
Dump all ARXML data to screen
```bash
arxml-dump --arxml <file1.arxml> --arxml <file2.arxml>
```

### arxml-format
Format ARXML files
```bash
arxml-format <input.arxml> <output.arxml>
```

### armodel-component
List all software component types
```bash
armodel-component <arxml_folder>
armodel-component --format long --filter CompositionSwComponent <arxml_folder>
```

### connector2xlsx
Export connectors to Excel file
```bash
connector2xlsx <input.arxml> <output.xlsx>
```

### connector-update
Update connectors from Excel file
```bash
connector-update <input.arxml> <excel_file.xlsx> <output.arxml>
```

### armodel-system-signal
List all system signals
```bash
armodel-system-signal <arxml_folder>
```

### armodel-memory-section
Manage memory sections
```bash
armodel-memory-section <arxml_folder>
```

### armodel-file-list
List file information
```bash
armodel-file-list <arxml_folder>
```

### armodel-uuid-checker
UUID checker tool
```bash
armodel-uuid-checker <arxml_folder>
```

### format-xml
Format XML files
```bash
format-xml <input.xml> <output.xml>
```

## Testing

### Test Framework
- Use pytest framework
- Test files mirror source structure
- Test methods are small and focused
- Use sample ARXML files from `tests/test_files/` for validation
- Run flake8 linting before committing

### Test Structure
```
tests/test_armodel/
├── cli/                    # CLI tool tests
├── data_models/            # Data model tests
├── lib/                    # Library function tests
├── models/                 # Model class tests
│   ├── M2/                 # M2 model tests
│   └── utils/              # Utility tests
├── parser/                 # Parser tests
├── transformer/            # Transformer tests
└── writer/                 # Writer tests
```

### Test Data
Test uses ARXML files from `test_files/` directory:
- AUTOSAR_Datatypes.arxml
- AUTOSAR_MOD_AISpecification_ApplicationDataType_Blueprint.arxml
- AUTOSAR_MOD_AISpecification_BaseTypes_Standard.arxml
- BswM_Bswmd.arxml
- CanSystem.arxml
- SoftwareComponents.arxml
- And many more...

## Important Notes

- Python >= 3.5 required
- Do NOT add comments unless asked
- Follow PEP 8 coding conventions
- When modifying code, check that flake8 passes (especially E9,F63,F7,F82 errors)
- Run tests after changes to ensure no regressions
- Test folder structure must match source folder structure
- CI supports Python 3.8, 3.9, 3.10, 3.11, and 3.12
- Use singleton pattern for AUTOSAR class
- Abstract base classes use ABCMeta metaclass
- Separation of concerns between parser and writer modules
