Changelog
=========

Version 1.9.0 (Current)
------------------------

* Current stable version

Version 1.8.7
-------------

* Corrected the base class of BswEvent
* Exported RunnableEntity class
* Added more class support for getDestType

Version 1.8.6
-------------

* Added support for NvProvideComSpec and NvRequireComSpec
* Improved ParameterAccess

Version 1.8.5
-------------

* Reorganized SwConnector class
* Raise error if short name of rootSwCompositionPrototype is invalid
* Added support for NvProvideComSpec
* Fixed duplicate short name of ARPackage and Other ARElements

Version 1.8.4
-------------

* Added support for BSW-SYNCHRONOUS-SERVER-CALL-POINT and RETURN-TYPE
* Added armodel-uuid-checker CLI tool
* Removed spaces in boolean type

Version 1.8.3
-------------

* Added support for SHORT-LABEL for VALUE
* Added support for MAX-DELTA-COUNTER-INIT, MAX-NO-NEW-OR-REPEATED-DATA, USER-DEFINED-TRANSFORMATION-COM-SPEC-PROPS, MASK

Version 1.8.2
-------------

* Fixed AUTOSAR XML schema issue

Version 1.8.1
-------------

* Added support for MODE-DECLARATION-MAPPING-SET, MODE-INTERFACE-MAPPING
* Added support for ECUC-MODULE-DEF, DOC-REVISION
* Added support for ECUC parameter definitions (Boolean, String, Integer, Float, Enumeration)
* Enabled same short name with different type to be added and located

Version 1.8.0
-------------

* Added support for DLT-USER-NEEDS
* Improved UUID check
* Improved find method of AbstractAUTOSAR to support validation of dest
* Added findXXX methods: findAtomicSwComponentType, findSystemSignal, findSystemSignalGroup, findPort, findVariableDataPrototype, findImplementationDataType

Version 1.7.9
-------------

* Improved BSW-MODULE-DESCRIPTION, BSW-INTERNAL-BEHAVIOR, LIFE-CYCLE-INFO-SET, PHYSICAL-DIMENSION
* Added support for ACTIVATION-POINTS, CALL-POINTS, LIFE-CYCLE-INFO, COLLECTION, KEYWORD-SET, FIGURE
* Added support for CLIENT-SERVER-INTERFACE-MAPPING, DTC-STATUS-CHANGE-NOTIFICATION-NEEDS
* Added test case for AUTOSAR_MOD_AISpecification_BaseTypes_Standard.arxml
* Added API to set AUTOSAR release version and correct schema will be set (AUTOSAR::setARRelease())
* Fixed conversion for float number in scientific notation

Version 1.7.8
-------------

* Added support for STATIC-MEMORYS, RECEPTION-POLICYS, VENDOR-API-INFIX, INCLUDED-MODE-DECLARATION-GROUP-SET, HW-ELEMENT
* Added support for FLEXRAY-FRAME, TYPE-MAPPING, DATA-TRANSFORMATION-SET
* Added support for FLEXRAY-COMMUNICATION-CONTROLLER, FLEXRAY-COMMUNICATION-CONNECTOR, FLEXRAY-PHYSICAL-CHANNEL, FLEXRAY-CLUSTER
* Added support for BSW-OPERATION-INVOKED-EVENT
* Improved SW-DATA-DEF-PROPS, SW-RECORD-LAYOUT-GROUP, BSW-MODULE-DESCRIPTION, BSW-CALLED-ENTITY
* Improved BSW-SCHEDULABLE-ENTITY, SW-SERVICE-ARG, RUNNABLE-ENTITY, I-SIGNAL-GROUP
* Improved END-TO-END-PROTECTION, BSW-INTERNAL-TRIGGER-OCCURRED-EVENT
* Fixed PROVIDED-MODE-GROUPS, MANAGED-MODE-GROUPS
* Enabled Flake8 and fixed Flake8 issues
* Added CompositionSwComponentType in AUTOSAR root model (getCompositionSwComponentTypes, getCompositionSwComponentType, addCompositionSwComponentType)
* Added duplicate UUID check

Version 1.7.7
-------------

* Added support for UDP-NM-CLUSTER, UDP-NM-CLUSTER-COUPLING, NM-IF-ECUS, UDP-NM-ECU
* Added support for TRANSMISSION-MODE-FALSE-TIMING, SECURED-I-PDU, MULTIPLEXED-I-PDU
* Added support for NM-PDU, SECURE-COMMUNICATION-PROPS-SET, SO-AD-ROUTING-GROUP
* Added support for ECU-RESOURCE-MAPPINGS, SW-IMPL-MAPPINGS, CAN-TP-CONFIG, DO-IP-TP-CONFIG
* Added support for LIN-TP-CONFIG, BSW-BACKGROUND-EVENT, BSW-DATA-RECEIVED-EVENT
* Added support for BSW-EXTERNAL-TRIGGER-OCCURRED-EVENT, MODE-SWITCHED-ACK-EVENT, BACKGROUND-EVENT
* Improved ETHERNET-COMMUNICATION-CONNECTOR, ECU-INSTANCE, CAN-NM-NODE, NM-NODE
* Improved SDG, DATA-FILTER, USER-DEFINED-PDU, APPLICATION-ARRAY-DATA-TYPE
* Improved MODE-SWITCH-SENDER-COM-SPEC
* Access RootSwCompositionPrototype directly from AUTOSAR instance
* Created mapping for Implementation and InternalBehavior (AUTOSAR::getBehavior(), AUTOSAR::getImplementation())
* Improved Identifiable::setCategory with Raw String

Version 1.7.6
-------------

* Added support for PROVIDED-SERVICE-INSTANCE, MAC-MULTICAST-GROUP
* Added support for ASSOCIATED-COM-I-PDU-GROUP-REF, CAN-CONTROLLER-CONFIGURATION-REQUIREMENTS
* Added support for CAN-CONTROLLER-FD-REQUIREMENTS
* Improved AR-PACKAGE, LIN-TP-CONFIG, DIAGNOSTIC-SERVICE-TABLE, LIN-MASTER
* Improved IMPLEMENTATION-DATA-TYPE, ETHERNET-COMMUNICATION-CONTROLLER
* Improved I-SIGNAL-PORT, SYMBOL-PROPS, I-PDU-PORT
* Fixed I-PDU-MAPPING

Version 1.7.5
-------------

* Added support for DIAGNOSTIC-CONNECTION, DIAGNOSTIC-SERVICE-TABLE
* Added support for LIN-MASTER, LIN-COMMUNICATION-CONNECTOR, UDP-NM-CLUSTER, UDP-NM-NODE
* Added support for MULTIPLEXED-I-PDU, USER-DEFINED-I-PDU, USER-DEFINED-PDU
* Added support for GENERAL-PURPOSE-I-PDU, GENERAL-PURPOSE-PDU
* Added support for SECURE-COMMUNICATION-PROPS-SET, SO-AD-ROUTING-GROUP
* Added support for BUS-OFF-RECOVERY, SCHEDULE-TABLES, INFRASTRUCTURE-SERVICES
* Added support for GENERIC-TP, TCP-TP, UDP-TP, CONSUMED-SERVICE-INSTANCES
* Fixed SW-RECORD-LAYOUT-V-AXIS, SW-RECORD-LAYOUT-GROUP-AXIS
* Improved SOCKET-CONNECTION, SOCKET-ADDRESS

Version 1.7.4
-------------

* Added support for DIAGNOSTIC-EVENT-INFO-NEEDS, AR-TYPED-PER-INSTANCE-MEMORYS
* Added support for USED-DATA-ELEMENT, ETHERNET-COMMUNICATION-CONTROLLER
* Added support for ETHERNET-COMMUNICATION-CONNECTOR, ETHERNET-PHYSICAL-CHANNEL
* Added support for PHYSICAL-PROPS, SO-AD-CONFIG
* Improved MODE-SWITCH-RECEIVER-COM-SPEC, APPLICATION-ARRAY-DATA-TYPE

Version 1.7.3
-------------

* Added support for MEM-CLASS-SYMBOL, ASYNCHRONOUS-SERVER-CALL-RESULT-POINTS
* Added support for STEP-SIZE, BSW-INTERRUPT-ENTITY, FLAT-MAP
* Added support for VARIABLE-AND-PARAMETER-INTERFACE-MAPPING, PORT-INTERFACE-MAPPING-SET
* Added support for DATA-MAPPINGS, ECU-STATE-MGR-USER-NEEDS, STACK-USAGES
* Added support for ROUGH-ESTIMATE-STACK-USAGE
* Improved PARAMETER-INTERFACE

Version 1.7.2
-------------

* Fixed invalidationPolicy of SenderReceiverInterface cannot be written in ARXML
* Added support for SW-ADDR-METHOD, DIAGNOSTIC-COMMUNICATION-MANAGER-NEEDS
* Added support for DIAGNOSTIC-ROUTINE-NEEDS, DIAGNOSTIC-VALUE-NEEDS
* Added support for DIAGNOSTIC-EVENT-NEEDS, CRYPTO-SERVICE-NEEDS
* Added support for DIAG-EVENT-DEBOUNCE-MONITOR-INTERNAL, ROLE-BASED-DATA-TYPE-ASSIGNMENT
* Added support for ASYNCHRONOUS-SERVER-CALL-RETURNS-EVENT, PR-PORT-PROTOTYPE

Version 1.7.1
-------------

* Added support for INTRODUCTION, LIST, SW-INTENDED-RESOLUTION, REFERENCE-BASE

Version 1.7.0
-------------

* Added support for SWC-TO-ECU-MAPPING, SW-MAPPINGS, ROOT-SOFTWARE-COMPOSITIONS
* Added support for SPEED, ECU-INSTANCE, COMM-CONTROLLERS
* Added support for CAN-COMMUNICATION-CONNECTOR, I-PDU-TIMING, DATA-FILTER
* Added support for EVENT-CONTROLLED-TIMING

Version 1.6.4
-------------

* Refactored the Implementation
* Fixed the Binary value
* Refactored the SwComponentType

Version 1.6.3
-------------

* Changed the Package structure according to AUTOSAR standard

Version 1.6.2
-------------

* Changed the AUTOSAR.clear() to AUTOSAR.new()
* Fixed several refactor methods issue

Version 1.6.1
-------------

* Organized the armodel package
* Added the Get/Set method for several classes

Version 1.6.0
-------------

* Added annotation support for Identifiable class
* Added ECUC support (EcucValueCollection, EcucModuleConfigurationValues, EcucContainerValue, EcucParameterValue, EcucAbstractReferenceValue)
* Added support for I-SIGNAL-GROUP, I-SIGNAL-I-PDU-GROUP, NM-CONFIG, NM-NODE, NM-CLUSTER
* Added support for CAN-NM-MODE, NM-ECU, SECURED-I-PDU, MODE-SWITCH-POINTS
* Created CLI (armodel-system-signal) to list all system signals

Version 1.5.0
-------------

* Fixed old ARElement (InitEvent, SwcTiming, ConstantMemory, ModeSwitchReceiverComSpec, MODE-ACCESS-POINTS)
* Added timestamp to AUTOSAR-VARIABLE-IREF, MODE-REQUEST-TYPE-MAP
* Added timing extension (TIMING-REQUIREMENTS, EXECUTION-ORDER-CONSTRAINT, EOC-EXECUTABLE-ENTITY-REF)
* Added communication support (LIN-CLUSTER, NM-PDU, LIN-UNCONDITIONAL-FRAME, CAN-FRAME, GATEWAY, I-SIGNAL)

Version 1.4.3
-------------

* Added support for writing BswCalledEntity, BswSchedulableEntity, BswImplementation
* Added support for writing ServiceSwComponentType, DataTypeMappingSet, ModeRequestTypeMap, PortInterface, ModeInterface
* Added support for reading ServiceSwComponentType, ModeRequestTypeMap, PortInterface, ModeInterface
* Refactored base ARType (ARFloat, ARNumerical, ARLiteral)
* Fixed Issue #22 - raise wrong Exception: Invalid ResourceConsumption of Implementation

Version 1.4.2
-------------

* Added support for reading EndToEndProtectionSet, EndToEndProtection, EndToEndProtectionVariablePrototype
* Added support for reading EndToEndDescription, ApplicationArrayDataType, SwRecordLayout
* Added support for reading SwCalprmAxisSet, SwCalprmAxis, ApplicationArrayElement, SwRecordLayoutGroup
* Added support for reading SwRecordLayoutGroupContent
* Added support for writing EndToEndProtectionSet, EndToEndProtection, EndToEndProtectionVariablePrototype
* Added support for writing EndToEndDescription, ApplicationArrayDataType, SwRecordLayout
* Added support for writing SwCalprmAxisSet, SwCalprmAxis, ApplicationArrayElement, SwRecordLayoutGroup
* Added support for writing SwRecordLayoutGroupContent, ImplementationDataType

Version 1.4.1
-------------

* Added support for reading ServerComSpec, PerInstanceMemory, PortDefinedArgumentValue
* Added support for reading DataWriteAccesses, NvBlockNeeds, CompositeNetworkRepresentation, PortGroup
* Added support for writing ServerComSpec, PerInstanceMemory, ServerCallPoint, ReadLocalVariable
* Added support for writing WrittenLocalVariable, PortDefinedArgumentValue, RVariableInAtomicSwcInstanceRef
* Added support for writing DataWriteAccesses, NvBlockNeeds, RecordValueSpecification
* Added support for writing CompositeNetworkRepresentation, PortGroup
* Moved ARPackage from the Elements

Version 1.4.0
-------------

* Added support for writing AUTOSAR model to arxml file (ARPackage, CompositionSwComponentType, CompuMethod, DataConstr, Unit)
* Added support for reading AUTOSAR model from arxml file (ConstantSpecification, DataConstr, Unit)

Version 1.3.0
-------------

* Added support to list all SwComponentType
* Added support to parse DelegationSwConnector
* Corrected class definitions of PPortInCompositionInstanceRef and RPortInCompositionInstanceRef

Version 1.2.0
-------------

* Added SwcImplementation support
* Added integer value for memory section alignment
* Removed required attributes for Implementation according to AUTOSAR standard 23R-11
* Changed START-ON-EVENT-REF to optional according to AUTOSAR standard 23R-11
* Changed HANDLE-OUT-OF-RANGE to optional according to AUTOSAR standard 23R-11
* Added SensorActuatorSwComponentType support
* Changed CATEGORY of COMPU-METHOD to optional
* Changed CAN-BE-INVOKED-CONCURRENTLY to optional

Version 1.1.0
-------------

* Added InitEvent support
* Added DataReceiveEvent support
* Added SwcModeSwitchEvent support

Version 1.0.0
-------------

* Added logging support
* Added <warning> option to disable exception raised
* Added BswMD support

Version 0.1.3
-------------

* Fixed attribute intervalType of Limit is empty issue

Version 0.1.2
-------------

* Added AsynchronousServerCallPoint support for ARXML

Version 0.1.1
-------------

* Added ARRAY category support for ImplementationDataType