# Software Requirements Specification

## py-armodel Requirements

This document contains all software requirements extracted from the current implementation of the py-armodel package.

## Maturity Levels

Each requirement has a maturity level that indicates its status:

- **draft**: Newly created requirement, under review, or not yet implemented
- **accept**: Accepted requirement, implemented in the codebase
- **invalid**: Deprecated requirement, superseded, or no longer applicable

All existing requirements in this document are currently at maturity level **accept**.

---

## 1. Model

### 1.1 Core AUTOSAR Model

#### SWR_MODEL_00001
**Title**: AUTOSAR Singleton Pattern

**Maturity**: accept

**Description**: The system shall provide a singleton pattern for the AUTOSAR model with the following methods:
- `AUTOSAR.getInstance()`: Retrieve the singleton instance
- `AUTOSAR.new()`: Clear and create a new instance
- `AUTOSAR.setARRelease(version)`: Set the AUTOSAR release version

---

#### SWR_MODEL_00002
**Title**: AUTOSAR Version Support

**Maturity**: accept

**Description**: The system shall support the following AUTOSAR release versions:
- 4.0.3, 4.1.0, 4.2.1, 4.3.0, 4.3.1, 4.4.0
- R19-11, R20-11, R21-11, R22-11, R23-11, R24-11

---

#### SWR_MODEL_00003
**Title**: ARPackage Hierarchy

**Maturity**: accept

**Description**: The system shall provide a hierarchical ARPackage structure for organizing AUTOSAR elements with support for:
- Nested packages through parent-child relationships
- Adding and retrieving subpackages
- Organizing elements by AUTOSAR M2 schema structure

---

#### SWR_MODEL_00004
**Title**: ARObject Base Class

**Maturity**: accept

**Description**: The system shall provide a base ARObject class that all AUTOSAR elements inherit from, providing common attributes and methods for:
- UUID management
- Admin data handling
- Parent reference tracking
- String representation

---

#### SWR_MODEL_00005
**Title**: UUID Management

**Maturity**: accept

**Description**: The system shall provide built-in UUID management with the following capabilities:
- Automatic UUID generation for new elements
- Duplicate UUID detection and reporting
- UUID validation tools

---

### 1.2 M2 MSR Models

#### SWR_MODEL_00006
**Title**: AsamHdo Base Types

**Maturity**: accept

**Description**: The system shall provide support for ASAM HDO base types including:
- SwBaseType: Software base type definitions
- BaseTypeDirectDefinition: Direct base type definitions

---

#### SWR_MODEL_00007
**Title**: Computation Methods

**Maturity**: accept

**Description**: The system shall support computation methods for data conversion including:
- CompuMethod: Computation method definitions
- CompuConst: Constant value mappings
- CompuScale: Scale value mappings
- CompuRationalCoefficients: Rational coefficient computations

---

#### SWR_MODEL_00008
**Title**: Units and Physical Dimensions

**Maturity**: accept

**Description**: The system shall provide support for units and physical dimensions including:
- Unit: Unit definitions with names and display names
- PhysicalDimension: Physical dimension definitions

---

#### SWR_MODEL_00009
**Title**: Data Constraints

**Maturity**: accept

**Description**: The system shall support data constraint definitions including:
- DataConstr: Data constraint definitions
- InternalConstrs: Internal constraint rules
- PhysConstrs: Physical constraint rules
- Upper and lower limit constraints

---

#### SWR_MODEL_00010
**Title**: Data Dictionary

**Maturity**: accept

**Description**: The system shall provide data dictionary support including:
- SwDataDefProps: Software data definition properties
- SwPointerTargetProps: Pointer target properties
- SwCalprmAxis: Calibration parameter axis
- SwCalprmAxisSet: Calibration parameter axis sets
- SwRecordLayout: Record layout definitions
- SwServiceArg: Service argument definitions

---

#### SWR_MODEL_00011
**Title**: Documentation Model

**Maturity**: accept

**Description**: The system shall provide documentation model support including:
- DocumentationBlock: Documentation block elements
- MultilanguageParagraph: Multi-language text paragraphs
- MultiLanguageLongName: Multi-language long names
- ARList: AR list elements
- Figure: Figure elements

---

### 1.3 M2 AUTOSARTemplates

#### SWR_MODEL_00012A
**Title**: AUTOSAR Class Mapping Compliance

**Maturity**: accept

**Description**: The system shall ensure all AUTOSAR model classes are importable from the module path specified in `docs/requirements/mapping.json`. Each class MUST be defined in the module file that corresponds to its AUTOSAR package path as specified in the mapping.

**Rationale**: The AUTOSAR standard defines a specific package hierarchy (M2 model) for each class. To maintain alignment with the AUTOSAR standard, classes must be importable from their mapped locations. This enables:
- Compliance with AUTOSAR specifications
- Predictable import paths for all users
- Automated verification through integration tests

**Verification**: Run the class mapping integration test to verify all classes are at their correct locations:
```bash
pytest tests/integration_tests/test_class_mapping.py::TestClassMapping::test_all_types_combined -v
```

---

#### SWR_MODEL_00012
**Title**: CommonStructure Elements

**Maturity**: accept

**Description**: The system shall provide common structure elements used across all AUTOSAR templates including:
- ARObject: Base object for all AUTOSAR objects
- Referrable: Elements that can have unique short names
- Identifiable: Elements with unique identifiers and categories

---

#### SWR_MODEL_00013
**Title**: Implementation Support

**Maturity**: accept

**Description**: The system shall support implementation definitions including:
- Implementation: Implementation definitions
- ImplementationProps: Implementation properties
- Code: Code generation properties

---

#### SWR_MODEL_00014
**Title**: Internal Behavior

**Maturity**: accept

**Description**: The system shall support internal behavior specifications including:
- InternalBehavior: Base internal behavior class
- ExecutableEntity: Executable entity definitions
- DataReceivePoint: Data receive point definitions
- OperationInvokedEvent: Operation invoked event definitions

---

#### SWR_MODEL_00015
**Title**: Resource Consumption

**Maturity**: accept

**Description**: The system shall support resource consumption specifications including:
- MemorySectionUsage: Memory section usage specifications
- StackUsage: Stack usage specifications
- HeapUsage: Heap usage specifications
- ExecutionTime: Execution time specifications
- ResourceConsumption: Resource consumption definitions

---

#### SWR_MODEL_00016
**Title**: Service Needs

**Maturity**: accept

**Description**: The system shall support AUTOSAR service needs including:
- DiagnosticEventNeeds: Diagnostic event requirements
- DiagnosticRoutineNeeds: Diagnostic routine requirements
- DiagnosticCapabilityElement: Diagnostic capability elements
- FunctionInhibitionNeeds: Function inhibition requirements
- CryptoServiceNeeds: Cryptographic service requirements
- ComMgrUserNeeds: Communication manager user needs
- EcuStateMgrUserNeeds: ECU state manager user needs
- DltUserNeeds: Diagnostic log and trace user needs
- DoIpServiceNeeds: Diagnostics over IP service needs

---

#### SWR_MODEL_00017
**Title**: SwcBswMapping

**Maturity**: accept

**Description**: The system shall support software component to BSW mapping including:
- SwcBswMapping: SWC to BSW mapping definitions
- SwcBswRunnableMapping: Runnable entity mapping definitions

---

#### SWR_MODEL_00018
**Title**: Implementation Data Types

**Maturity**: accept

**Description**: The system shall support implementation data type definitions including:
- ImplementationDataType: Implementation data type definitions
- AbstractImplementationDataTypeElement: Abstract implementation data type elements
- ImplementationDataTypeType: Type definitions for implementation data types

---

#### SWR_MODEL_00019
**Title**: Mode Declaration

**Maturity**: accept

**Description**: The system shall support mode declaration specifications including:
- ModeDeclaration: Mode declaration definitions
- ModeDeclarationGroup: Mode declaration groups
- ModeSwitch: Mode switch specifications

---

#### SWR_MODEL_00020
**Title**: Timing Specifications

**Maturity**: accept

**Description**: The system shall support timing specifications including:
- TimingConstraint: Timing constraint definitions
- ExecutionOrder: Execution order specifications
- TimingExtension: Timing extension elements

---

### 1.4 SWComponentTemplate

#### SWR_MODEL_00021
**Title**: Software Component Types

**Maturity**: accept

**Description**: The system shall support the following software component types:
- ApplicationSwComponentType: Application software components
- CompositionSwComponentType: Composition software components
- SensorActuatorSwComponentType: Sensor/actuator software components
- ServiceSwComponentType: Service software components
- ComplexDeviceDriverSwComponentType: Complex device driver components
- EcuAbstractionSwComponentType: ECU abstraction components
- ServiceProxySwComponentType: Service proxy components
- NvBlockSwComponentType: Non-volatile block components

---

#### SWR_MODEL_00022
**Title**: SwcInternalBehavior

**Maturity**: accept

**Description**: The system shall support software component internal behavior including:
- SwcInternalBehavior: SWC internal behavior definitions
- RunnableEntity: Runnable entity definitions with data access points
- DataReceiveEvent: Data receive event definitions
- InitEvent: Initialization event definitions
- SwcModeSwitchEvent: Mode switch event definitions
- TimingEvent: Timing event definitions
- DataTriggeredOperationInvokedEvent: Data triggered operation events

---

#### SWR_MODEL_00023
**Title**: Port Interfaces

**Maturity**: accept

**Description**: The system shall support the following port interface types:
- SenderReceiverInterface: Sender-receiver interfaces for data transmission
- ClientServerInterface: Client-server interfaces for service operations
- ParameterInterface: Parameter interfaces for parameter access
- ModeSwitchInterface: Mode switch interfaces for mode management
- NvDataInterface: Non-volatile data interfaces
- TriggerInterface: Trigger interfaces for event triggering
- ServiceInterface: Service interfaces for AUTOSAR services

---

#### SWR_MODEL_00024
**Title**: Port Interface Operations

**Maturity**: accept

**Description**: The system shall support port interface operations including:
- Operation: Client-server operation definitions
- DataElement: Data element definitions for sender-receiver interfaces

---

#### SWR_MODEL_00025
**Title**: Data Types

**Maturity**: accept

**Description**: The system shall support application data type definitions including:
- ApplicationDataType: Application data type definitions
- ApplicationRecordElement: Application record element definitions
- ApplicationArrayElement: Application array element definitions
- DataTypeMap: Data type mapping between application and implementation types

---

#### SWR_MODEL_00026
**Title**: SwcImplementation

**Maturity**: accept

**Description**: The system shall support software component implementation definitions including:
- SwcImplementation: SWC implementation definitions
- ImplementationProperty: Implementation property definitions

---

### 1.5 SystemTemplate

#### SWR_MODEL_00027
**Title**: System Signal Support

**Maturity**: accept

**Description**: The system shall support system signal definitions including:
- SystemSignal: System signal definitions
- SystemSignalGroup: System signal group definitions

---

#### SWR_MODEL_00028
**Title**: ECU and System Mapping

**Maturity**: accept

**Description**: The system shall support ECU and system mapping including:
- EcuInstance: ECU instance definitions
- SwcToEcuMapping: Software component to ECU mapping
- RootSoftwareComposition: Root software composition definitions
- SwMappings: Software mapping definitions

---

#### SWR_MODEL_00029
**Title**: Data Mapping

**Maturity**: accept

**Description**: The system shall support system-level data mapping including:
- DataMapping: Data mapping definitions
- Mapping: Mapping element definitions

---

#### SWR_MODEL_00030
**Title**: Diagnostic Connection

**Maturity**: accept

**Description**: The system shall support diagnostic connection definitions including:
- DiagnosticConnection: Diagnostic connection definitions
- DiagnosticServiceTable: Diagnostic service table definitions

---

#### SWR_MODEL_00031
**Title**: Network Management

**Maturity**: accept

**Description**: The system shall support network management configurations including:
-NmConfig: Network management configuration
-NmNode: Network management node
-NmCluster: Network management cluster
- CanNmMode: CAN network management mode
- UdpNmCluster: UDP network management cluster

---

#### SWR_MODEL_00032
**Title**: Secure Communication

**Maturity**: accept

**Description**: The system shall support secure communication elements including:
- SecureCommunication: Secure communication definitions

---

#### SWR_MODEL_00033
**Title**: Transport Protocols

**Maturity**: accept

**Description**: The system shall support transport protocol definitions for various communication protocols.

---

#### SWR_MODEL_00034
**Title**: Fibex CAN Communication

**Maturity**: accept

**Description**: The system shall support Fibex CAN communication elements including:
- CanFrame: CAN frame definitions
- CanFrameTriggering: CAN frame triggering specifications

---

#### SWR_MODEL_00035
**Title**: Fibex Ethernet Communication

**Maturity**: accept

**Description**: The system shall support Fibex Ethernet communication elements including:
- SocketConnection: Socket connection definitions
- SocketConnectionBundle: Socket connection bundle definitions

---

#### SWR_MODEL_00036
**Title**: Fibex FlexRay Communication

**Maturity**: accept

**Description**: The system shall support Fibex FlexRay communication elements.

---

#### SWR_MODEL_00037
**Title**: Fibex LIN Communication

**Maturity**: accept

**Description**: The system shall support Fibex LIN communication elements including:
- LinCluster: LIN cluster definitions
- LinUnconditionalFrame: LIN unconditional frame definitions
- LinMaster: LIN master definitions

---

#### SWR_MODEL_00038
**Title**: Fibex Core Communication

**Maturity**: accept

**Description**: The system shall support Fibex core communication and topology elements.

---

#### SWR_MODEL_00039
**Title**: Fibex Multiplatform Communication

**Maturity**: accept

**Description**: The system shall support Fibex multiplatform communication elements.

---

#### SWR_MODEL_00040
**Title**: DoIP Support

**Maturity**: accept

**Description**: The system shall support Diagnostics over IP (DoIP) including:
- DoIpServiceNeeds: DoIP service needs definitions
- DoIpConfiguration: DoIP configuration definitions

---

### 1.6 BswModuleTemplate

#### SWR_MODEL_00041
**Title**: BSW Module Description

**Maturity**: accept

**Description**: The system shall support BSW module description definitions including:
- BswModuleDescription: BSW module description definitions

---

#### SWR_MODEL_00042
**Title**: BSW Behavior

**Maturity**: accept

**Description**: The system shall support BSW behavior specifications including:
- BswInternalBehavior: BSW internal behavior definitions
- BswModuleEntity: BSW module entity definitions
- BswSchedulableEntity: BSW schedulable entity definitions
- BswCalledEntity: BSW called entity definitions
- BswInterruptEntity: BSW interrupt entity definitions

---

#### SWR_MODEL_00043
**Title**: BSW Implementation

**Maturity**: accept

**Description**: The system shall support BSW implementation definitions including:
- BswImplementation: BSW implementation definitions

---

#### SWR_MODEL_00044
**Title**: BSW Interfaces

**Maturity**: accept

**Description**: The system shall support BSW interface definitions including:
- BswModuleEntry: BSW module entry definitions
- BswModuleClientServerEntry: BSW module client-server entry definitions
- BswModuleDependency: BSW module dependency definitions

---

#### SWR_MODEL_00045
**Title**: BSW Events

**Maturity**: accept

**Description**: The system shall support BSW event definitions including:
- BswBackgroundEvent: BSW background event definitions
- BswDataReceivedEvent: BSW data received event definitions
- BswExternalTriggerOccurredEvent: BSW external trigger event definitions
- BswModeSwitchedAckEvent: BSW mode switch acknowledgement event definitions
- BswOperationInvokedEvent: BSW operation invoked event definitions
- BswAsynchronousServerCallReturnsEvent: BSW asynchronous server call returns event definitions

---

#### SWR_MODEL_00046
**Title**: BSW Call Points

**Maturity**: accept

**Description**: The system shall support BSW call point definitions including:
- BswDirectCallPoint: BSW direct call point definitions
- BswSynchronousServerCallPoint: BSW synchronous server call point definitions
- BswAsynchronousServerCallPoint: BSW asynchronous server call point definitions
- BswAsynchronousServerCallResultPoint: BSW asynchronous server call result point definitions

---

### 1.7 ECUCDescriptionTemplate

#### SWR_MODEL_00047
**Title**: ECUC Configuration Values

**Maturity**: accept

**Description**: The system shall support ECUC configuration values including:
- EcucValueCollection: ECUC value collection definitions
- EcucModuleConfigurationValues: ECUC module configuration values
- EcucContainerValue: ECUC container value definitions

---

#### SWR_MODEL_00048
**Title**: ECUC Parameter Values

**Maturity**: accept

**Description**: The system shall support ECUC parameter value definitions including:
- EcucParameterValue: ECUC parameter value base class
- EcucBooleanParameterValue: Boolean parameter values
- EcucIntegerParameterValue: Integer parameter values
- EcucFloatParameterValue: Float parameter values
- EcucStringParameterValue: String parameter values
- EcucEnumerationParameterValue: Enumeration parameter values

---

#### SWR_MODEL_00049
**Title**: ECUC Definitions

**Maturity**: accept

**Description**: The system shall support ECUC definition classes including:
- EcucModuleDef: ECUC module definition
- EcucParamDef: ECUC parameter definition base class
- EcucContainerDef: ECUC container definition
- EcucBooleanParamDef: Boolean parameter definition
- EcucIntegerParamDef: Integer parameter definition
- EcucFloatParamDef: Float parameter definition
- EcucStringParamDef: String parameter definition
- EcucEnumerationParamDef: Enumeration parameter definition

---

### 1.8 EcuResourceTemplate

#### SWR_MODEL_00050
**Title**: ECU Resource Elements

**Maturity**: accept

**Description**: The system shall support ECU resource template elements including hardware element categories.

---

### 1.9 GenericStructure

#### SWR_MODEL_00051
**Title**: Generic Structure Elements

**Maturity**: accept

**Description**: The system shall support generic structure elements including abstract and template classes following AUTOSAR standardization patterns.

---

### 1.10 DiagnosticExtract

#### SWR_MODEL_00052
**Title**: Diagnostic Contribution

**Maturity**: accept

**Description**: The system shall support diagnostic contribution elements with enhanced diagnostic functionality.

---

## 2. Parser

### 2.1 Core Parser

#### SWR_PARSER_00001
**Title**: ARXML Parser Class

**Maturity**: accept

**Description**: The system shall provide an ARXMLParser class for parsing ARXML files with the following capabilities:
- XML parsing using lxml library
- AUTOSAR namespace resolution
- Support for all AUTOSAR versions (4.0.3 to R24-11)
- Warning mode option to continue parsing on errors

---

#### SWR_PARSER_00002
**Title**: Parser Configuration Options

**Maturity**: accept

**Description**: The system shall support parser configuration options including:
- warning: Boolean flag to enable warning mode instead of raising exceptions
- Support for continuing parsing on non-critical errors when warning mode is enabled

---

#### SWR_PARSER_00003
**Title**: Parse from File

**Maturity**: accept

**Description**: The system shall provide functionality to parse ARXML files from the file system and return a complete AUTOSAR model object.

---

#### SWR_PARSER_00004
**Title**: XML Namespace Handling

**Maturity**: accept

**Description**: The system shall automatically resolve and handle AUTOSAR XML namespaces during parsing, supporting different AUTOSAR versions.

---

#### SWR_PARSER_00005
**Title**: Element Finding

**Maturity**: accept

**Description**: The system shall provide helper methods for finding XML elements by name within the parsed document structure.

---

#### SWR_PARSER_00006
**Title**: Attribute Reading

**Maturity**: accept

**Description**: The system shall provide methods for reading XML attributes with proper type conversion (string, integer, boolean, etc.).

---

#### SWR_PARSER_00007
**Title**: Parent-Child Relationship Maintenance

**Maturity**: accept

**Description**: The system shall maintain parent-child relationships when building the object graph from XML, allowing bidirectional navigation.

---

### 2.2 Specialized Parsers

#### SWR_PARSER_00008
**Title**: File List Parser

**Maturity**: accept

**Description**: The system shall provide a FileListParser for parsing file listing operations.

---

#### SWR_PARSER_00009
**Title**: Excel Parser

**Maturity**: accept

**Description**: The system shall provide an ExcelParser for parsing generic Excel files.

---

#### SWR_PARSER_00010
**Title**: Connector Excel Parser

**Maturity**: accept

**Description**: The system shall provide a ConnectorXlsxParser for parsing Excel connector files specifically.

---

## 3. Writer

### 3.1 Core Writer

#### SWR_WRITER_00001
**Title**: ARXML Writer Class

**Maturity**: accept

**Description**: The system shall provide an ARXMLWriter class for writing AUTOSAR models to ARXML format.

---

#### SWR_WRITER_00002
**Title**: Write to File

**Maturity**: accept

**Description**: The system shall provide functionality to write AUTOSAR model objects to ARXML files on the file system.

---

#### SWR_WRITER_00003
**Title**: XML Generation

**Maturity**: accept

**Description**: The system shall generate well-formed XML files with proper indentation and formatting.

---

#### SWR_WRITER_00004
**Title**: Namespace Handling

**Maturity**: accept

**Description**: The system shall properly handle XML namespaces in the generated ARXML files according to the AUTOSAR version specified.

---

#### SWR_WRITER_00005
**Title**: Version Compliance

**Maturity**: accept

**Description**: The system shall generate ARXML files that comply with the schema for the specified AUTOSAR version.

---

#### SWR_WRITER_00006
**Title**: Metadata Preservation

**Maturity**: accept

**Description**: The system shall preserve all metadata from the model including:
- UUIDs
- Timestamps
- Admin data
- Other AUTOSAR-specific metadata

---

#### SWR_WRITER_00007
**Title**: Object Graph Serialization

**Maturity**: accept

**Description**: The system shall serialize the complete AUTOSAR object graph back to XML format, maintaining all relationships and hierarchies.

---

## 4. CLI

### 4.1 Core CLI Tools

#### SWR_CLI_00001
**Title**: arxml-dump Tool

**Maturity**: accept

**Description**: The system shall provide a command-line tool `arxml-dump` for dumping the complete hierarchical structure of an ARXML file to the console.

---

#### SWR_CLI_00002
**Title**: arxml-format Tool

**Maturity**: accept

**Description**: The system shall provide a command-line tool `arxml-format` for formatting ARXML files with proper indentation and structure.

---

#### SWR_CLI_00003
**Title**: connector2xlsx Tool

**Maturity**: accept

**Description**: The system shall provide a command-line tool `connector2xlsx` for exporting SwConnector data from ARXML files to Excel format. Usage: `connector2xlsx <arxml_file> <excel_file>`

---

#### SWR_CLI_00004
**Title**: connector-update Tool

**Maturity**: accept

**Description**: The system shall provide a command-line tool `connector-update` for updating SwConnector data in ARXML files from Excel files. Usage: `connector-update <arxml_file> <excel_file>`

---

#### SWR_CLI_00005
**Title**: armodel-component Tool

**Maturity**: accept

**Description**: The system shall provide a command-line tool `armodel-component` for listing software components in ARXML files. The tool shall support:
- Filtering by component type (e.g., CompositionSwComponent)
- Multiple output formats (long, short)
- Usage: `armodel-component <arxml_file> [--filter <type>] [--format <format>]`

---

#### SWR_CLI_00006
**Title**: armodel-system-signal Tool

**Maturity**: accept

**Description**: The system shall provide a command-line tool `armodel-system-signal` for listing system signals in ARXML files. Usage: `armodel-system-signal <arxml_file>`

---

#### SWR_CLI_00007
**Title**: armodel-memory-section Tool

**Maturity**: accept

**Description**: The system shall provide a command-line tool `armodel-memory-section` for displaying memory section usage from ARXML files. Usage: `armodel-memory-section <arxml_file>`

---

#### SWR_CLI_00008
**Title**: armodel-file-list Tool

**Maturity**: accept

**Description**: The system shall provide a command-line tool `armodel-file-list` for listing project files. Usage: `armodel-file-list`

---

#### SWR_CLI_00009
**Title**: armodel-uuid-checker Tool

**Maturity**: accept

**Description**: The system shall provide a command-line tool `armodel-uuid-checker` for validating UUID uniqueness in ARXML files. Usage: `armodel-uuid-checker <arxml_file>`

---

#### SWR_CLI_00010
**Title**: format-xml Tool

**Maturity**: accept

**Description**: The system shall provide a command-line tool `format-xml` for formatting generic XML files with proper indentation. Usage: `format-xml <xml_file>`

---

### 4.2 CLI Common Features

#### SWR_CLI_00011
**Title**: CLI Error Handling

**Maturity**: accept

**Description**: All CLI tools shall provide appropriate error handling with:
- User-friendly error messages
- Proper exit codes (0 for success, 1 for error)
- Error output to stderr

---

#### SWR_CLI_00012
**Title**: CLI Help Messages

**Maturity**: accept

**Description**: All CLI tools shall provide help messages accessible via `-h` or `--help` flags showing usage and available options.

---

## 5. Data Models

### 5.1 Connector Models

#### SWR_DM_00001
**Title**: SwConnectorData Base Class

**Maturity**: accept

**Description**: The system shall provide a SwConnectorData base class for connector data management.

---

#### SWR_DM_00002
**Title**: DelegationSwConnectorData

**Maturity**: accept

**Description**: The system shall provide a DelegationSwConnectorData class for delegation connectors with inner and outer port mappings.

---

#### SWR_DM_00003
**Title**: AssemblySwConnectorData

**Maturity**: accept

**Description**: The system shall provide an AssemblySwConnectorData class for assembly connectors with provider and receiver mappings.

---

## 6. Library Functions

### 6.1 Software Component Analysis

#### SWR_LIB_00001
**Title**: SwComponentAnalyzer

**Maturity**: accept

**Description**: The system shall provide a SwComponentAnalyzer utility class with the following capabilities:
- Recursive package parsing for software component types
- Filtering by component type
- Formatted output options
- Support for all SWComponentType variants

---

### 6.2 CLI Arguments Parser

#### SWR_LIB_00002
**Title**: CLI Arguments Parser

**Maturity**: accept

**Description**: The system shall provide command-line argument parsing utilities for standardized argument handling across CLI tools.

---

### 6.3 System Signal Utilities

#### SWR_LIB_00003
**Title**: System Signal Utilities

**Maturity**: accept

**Description**: The system shall provide system signal manipulation utilities for working with SystemSignal elements.

---

## 7. Transformer

### 7.1 Base Transformer

#### SWR_TRANSFORMER_00001
**Title**: AbstractTransformer Base Class

**Maturity**: accept

**Description**: The system shall provide an AbstractTransformer base class for data transformation operations with a remove() method for cleanup operations.

---

#### SWR_TRANSFORMER_00002
**Title**: Admin Data Transformer

**Maturity**: accept

**Description**: The system shall provide admin data transformation utilities for handling administrative data transformations.

---

## 8. Report

### 8.1 Excel Report Generation

#### SWR_REPORT_00001
**Title**: ConnectorXlsReport

**Maturity**: accept

**Description**: The system shall provide a ConnectorXlsReport class for generating Excel reports for connector data.

---

#### SWR_REPORT_00002
**Title**: Generic Excel Report

**Maturity**: accept

**Description**: The system shall provide generic Excel report generation utilities for creating custom Excel reports.

---

## 9. Package

### 9.1 Package Configuration

#### SWR_PACKAGE_00001
**Title**: Package API Export

**Maturity**: accept

**Description**: The system shall export the following public API from the root package:
- All M2 model classes (MSR and AUTOSARTemplates)
- ARXMLParser class
- ARXMLWriter class
- CLI tool entry points
- Utility classes and functions
- Data models
- Transformer and report modules

---

#### SWR_PACKAGE_00002
**Title**: Python Version Support

**Maturity**: accept

**Description**: The system shall support Python versions 3.5 through 3.12.

---

#### SWR_PACKAGE_00003
**Title**: Package Metadata

**Maturity**: accept

**Description**: The system shall include appropriate package metadata including:
- Package name: armodel
- Version information
- Author and contact information
- Description and long description
- Project URL
- License classification (MIT)
- Python version requirements
- Runtime dependencies

---

#### SWR_PACKAGE_00004
**Title**: Console Scripts Registration

**Maturity**: accept

**Description**: The system shall register the following console scripts:
- arxml-dump
- arxml-format
- armodel-component
- connector2xlsx
- connector-update
- armodel-system-signal
- armodel-memory-section
- armodel-file-list
- armodel-uuid-checker
- format-xml

---

## 10. Dependencies

### 10.1 Runtime Dependencies

#### SWR_DEPS_00001
**Title**: colorama Dependency

**Maturity**: accept

**Description**: The system shall use colorama library for cross-platform colored terminal output.

---

#### SWR_DEPS_00002
**Title**: openpyxl Dependency

**Maturity**: accept

**Description**: The system shall use openpyxl library for Excel file processing.

---

#### SWR_DEPS_00003
**Title**: lxml Dependency

**Maturity**: accept

**Description**: The system shall use lxml library for XML processing and parsing.

---

### 10.2 Development Dependencies

#### SWR_DEPS_00004
**Title**: pytest Dependency

**Maturity**: accept

**Description**: The system shall use pytest framework for unit testing.

---

#### SWR_DEPS_00005
**Title**: pytest-cov Dependency

**Maturity**: accept

**Description**: The system shall use pytest-cov for code coverage reporting.

---

#### SWR_DEPS_00006
**Title**: flake8 Dependency

**Maturity**: accept

**Description**: The system shall use flake8 for code style checking and linting.

---

#### SWR_DEPS_00007
**Title**: sphinx Dependency

**Maturity**: accept

**Description**: The system shall use sphinx for documentation generation.

---

## 11. Key Features

### 11.1 AUTOSAR Model Query

#### SWR_FEATURE_00001
**Title**: Finding Atomic Software Components

**Maturity**: accept

**Description**: The system shall provide methods to find atomic software component types by short name and retrieve all atomic components.

---

#### SWR_FEATURE_00002
**Title**: Finding Composition Software Components

**Maturity**: accept

**Description**: The system shall provide methods to find composition software component types by short name and retrieve all composition components.

---

#### SWR_FEATURE_00003
**Title**: Finding System Signals

**Maturity**: accept

**Description**: The system shall provide methods to find system signals by short name and retrieve all system signals.

---

#### SWR_FEATURE_00004
**Title**: Finding Ports

**Maturity**: accept

**Description**: The system shall provide methods to find ports by short name.

---

#### SWR_FEATURE_00005
**Title**: Finding Data Prototypes

**Maturity**: accept

**Description**: The system shall provide methods to find variable data prototypes by short name.

---

#### SWR_FEATURE_00006
**Title**: Finding Implementation Data Types

**Maturity**: accept

**Description**: The system shall provide methods to find implementation data types by short name.

---

#### SWR_FEATURE_00007
**Title**: Getting Component Behavior

**Maturity**: accept

**Description**: The system shall provide methods to retrieve the internal behavior for a software component.

---

#### SWR_FEATURE_00008
**Title**: Getting Component Implementation

**Maturity**: accept

**Description**: The system shall provide methods to retrieve the implementation for a software component.

---

### 11.2 Data Type Mapping

#### SWR_FEATURE_00009
**Title**: Type Mapping Support

**Maturity**: accept

**Description**: The system shall support mapping between application data types and implementation data types through DataTypeMap definitions.

---

### 11.3 Connector Support

#### SWR_FEATURE_00010
**Title**: Assembly Connector Support

**Maturity**: accept

**Description**: The system shall support assembly connectors for connecting ports between components.

---

#### SWR_FEATURE_00011
**Title**: Delegation Connector Support

**Maturity**: accept

**Description**: The system shall support delegation connectors for delegating ports through component hierarchies.

---

#### SWR_FEATURE_00012
**Title**: Communication Specification Support

**Maturity**: accept

**Description**: The system shall support various communication specifications including:
- ServerComSpec
- ModeSwitchReceiverComSpec
- NvProvideComSpec
- NvRequireComSpec

---

### 11.4 Event Support

#### SWR_FEATURE_00013
**Title**: RTE Events

**Maturity**: accept

**Description**: The system shall support RTE events including:
- InitEvent
- DataReceiveEvent
- SwcModeSwitchEvent
- TimingEvent
- DataTriggeredOperationInvokedEvent

---

#### SWR_FEATURE_00014
**Title**: BSW Events

**Maturity**: accept

**Description**: The system shall support BSW events including:
- BswBackgroundEvent
- BswDataReceivedEvent
- BswExternalTriggerOccurredEvent
- BswModeSwitchedAckEvent
- BswOperationInvokedEvent
- BswAsynchronousServerCallReturnsEvent

---

### 11.5 End-to-End Protection

#### SWR_FEATURE_00015
**Title**: End-to-End Protection Support

**Maturity**: accept

**Description**: The system shall support end-to-end protection including:
- EndToEndProtectionSet
- EndToEndProtection definitions

---

### 11.6 Testing Structure

#### SWR_FEATURE_00016
**Title**: Test Coverage

**Maturity**: accept

**Description**: The system shall include comprehensive test coverage with test files mirroring the source structure in tests/test_armodel/.

---

#### SWR_FEATURE_00017
**Title**: Test Files

**Maturity**: accept

**Description**: The system shall include sample ARXML files in test_files/ directory for validation and testing.

---

#### SWR_FEATURE_00018
**Title**: CI/CD Testing

**Maturity**: accept

**Description**: The system shall include GitHub Actions workflows for continuous integration testing across Python versions 3.8-3.12 with linting and coverage checks.
