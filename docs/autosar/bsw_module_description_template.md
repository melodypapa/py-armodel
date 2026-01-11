# AUTOSAR BSW Module Description Template - Class and Package Reference

This document provides a comprehensive listing of classes and packages from the AUTOSAR BSW Module Description Template as documented in the AUTOSAR CP R23-11 Basic Software Module Description Template specification.

## Table of Contents
- [Abstract Classes](#abstract-classes)
- [Packages](#packages)
- [Classes](#classes)
- [Enumerations](#enumerations)

## Abstract Classes

The following classes are abstract classes in the AUTOSAR BSW Module Description Template, meaning they serve as base classes that cannot be instantiated directly but provide a common interface for derived concrete classes.

### BSW Behavior Package (M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior)
- `AbstractEvent` - Base class for various event types (page 86-87)
- `BswApiOptions` - Base class for API options (page 82)
- `BswDataReceptionPolicy` - Base class for data reception policies (page 104)
- `BswModuleCallPoint` - Base class for module call points (page 76-77)

### BSW Interfaces Package (M2::AUTOSARTemplates::BswModuleTemplate::BswInterfaces)
- `BswEntryRelationshipEnum` - Enum with abstract values (page 51)

### Common Structure Implementation Package (M2::AUTOSARTemplates::CommonStructure::Implementation)
- `Implementation` - Base class for implementation (page 126)

### Common Structure ImplementationDataTypes Package (M2::AUTOSARTemplates::CommonStructure::ImplementationDataTypes)
- `AbstractImplementationDataType` - Base class for abstract implementation data types (page 320)
- `AbstractImplementationDataTypeElement` - Base class for abstract implementation data type elements (page 321)

### Common Structure Internal Behavior Package (M2::AUTOSARTemplates::CommonStructure::InternalBehavior)
- `InternalBehavior` - Base class for internal behavior (page 64)
- `ExecutableEntity` - Base class for executable entities (page 69)
- `ImplementationProps` - Base class for implementation properties (page 85)

### Common Structure Service Needs Package (M2::AUTOSARTemplates::CommonStructure::ServiceNeeds)
- `ServiceNeeds` - Base class for service needs (page 227)

### SW Component Template SwcInternalBehavior AccessCount Package (M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::AccessCount)
- `AbstractAccessPoint` - Base class for access points (page 57)

### SW Component Template Datatype Datatypes Package (M2::AUTOSARTemplates::SWComponentTemplate::Datatype::Datatypes)
- `ApplicationDataType` - Base class for application data types (page 305)
- `AutosarDataType` - Base class for AUTOSAR data types (page 305)

### SW Component Template Datatype DataPrototypes Package (M2::AUTOSARTemplates::SWComponentTemplate::Datatype::DataPrototypes)
- `AutosarDataPrototype` - Base class for AUTOSAR data prototypes (page 305)
- `DataPrototype` - Base class for data prototypes (page 305)

### Common Structure SwcBswMapping Package (M2::AUTOSARTemplates::CommonStructure::SwcBswMapping)
- `SwcBswMapping` - Base class for SWC/BSW mapping (page 109)

### Generic Structure GeneralTemplateClasses Package
- `ARObject` - Base class for all AUTOSAR objects (page 318)
- `Identifiable` - Base class for identifiable elements (page 318)
- `Referrable` - Base class for referrable elements (page 328)
- `MultilanguageReferrable` - Base class for multilanguage referrable elements (page 318)
- `AtpBlueprint` - Base class for blueprint elements (page 318)
- `AtpClassifier` - Base class for classifier elements (page 318)
- `AtpFeature` - Base class for feature elements (page 318)
- `AtpStructureElement` - Base class for structure elements (page 318)
- `CollectableElement` - Base class for collectable elements (page 318)
- `PackageableElement` - Base class for packageable elements (page 318)
- `UploadableDesignElement` - Base class for uploadable design elements (page 318)
- `UploadablePackageElement` - Base class for uploadable package elements (page 318)

### MSR Base Types Package (M2::MSR::AsamHdo::BaseTypes)
- `BaseType` - Base class for base types (page 336)

## Packages

### BSW Template Packages
- `M2::AUTOSARTemplates::BswModuleTemplate::BswOverview`
- `M2::AUTOSARTemplates::BswModuleTemplate::BswInterfaces`
- `M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior`
- `M2::AUTOSARTemplates::BswModuleTemplate::BswImplementation`

### Common Structure Packages
- `M2::AUTOSARTemplates::CommonStructure::ModeDeclaration`
- `M2::AUTOSARTemplates::CommonStructure::TriggerDeclaration`
- `M2::AUTOSARTemplates::CommonStructure::InternalBehavior`
- `M2::AUTOSARTemplates::CommonStructure::SwcBswMapping`
- `M2::AUTOSARTemplates::CommonStructure::ResourceConsumption`
- `M2::AUTOSARTemplates::CommonStructure::ResourceConsumption::MemorySectionUsage`
- `M2::AUTOSARTemplates::CommonStructure::ResourceConsumption::StackUsage`
- `M2::AUTOSARTemplates::CommonStructure::ResourceConsumption::HeapUsage`
- `M2::AUTOSARTemplates::CommonStructure::ResourceConsumption::ExecutionTime`
- `M2::AUTOSARTemplates::CommonStructure::MeasurementCalibrationSupport`
- `M2::AUTOSARTemplates::CommonStructure::McGroups`
- `M2::AUTOSARTemplates::CommonStructure::ServiceNeeds`
- `M2::AUTOSARTemplates::CommonStructure::Implementation`
- `M2::AUTOSARTemplates::CommonStructure::ImplementationDataTypes`

### SW Component Template Packages
- `M2::AUTOSARTemplates::SWComponentTemplate::Components`
- `M2::AUTOSARTemplates::SWComponentTemplate::PortInterface`
- `M2::AUTOSARTemplates::SWComponentTemplate::Datatype::DataPrototypes`
- `M2::AUTOSARTemplates::SWComponentTemplate::Datatype::Datatypes`
- `M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior`
- `M2::AUTOSARTemplates::SWComponentTemplate::SwcImplementation`
- `M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::ServerCall`
- `M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::DataElements`
- `M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::RTEEvents`
- `M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::ModeDeclarationGroup`
- `M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::Trigger`
- `M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::PortAPIOptions`
- `M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::AccessCount`

### MSR Packages
- `M2::MSR::DataDictionary::ServiceProcessTask`
- `M2::MSR::DataDictionary::DataDefProperties`
- `M2::MSR::DataDictionary::AuxillaryObjects`
- `M2::MSR::AsamHdo::ComputationMethod`
- `M2::MSR::AsamHdo::BaseTypes`
- `M2::MSR::AsamHdo::Units`

### Generic Structure Packages
- `M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::ARPackage`
- `M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::Identifiable`
- `M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::Referrable`
- `M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::MultilanguageReferrable`
- `M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::ARObject`
- `M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::AtpBlueprint`
- `M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::AtpClassifier`
- `M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::AtpFeature`
- `M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::AtpPrototype`
- `M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::AtpStructureElement`
- `M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::CollectableElement`
- `M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::PackageableElement`
- `M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::UploadableDesignElement`
- `M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::UploadablePackageElement`
- `M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::PrimitiveTypes`
- `M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::MultilanguageOverviewParagraph`
- `M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::DocumentationBlock`
- `M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::MultiLanguageOverviewParagraph`
- `M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::SingleLanguageOverviewParagraph`
- `M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::EngineeringObject`
- `M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::MultidimensionalTime`
- `M2::AUTOSARTemplates::GenericStructure::BuildActionManifest`
- `M2::AUTOSARTemplates::GenericStructure::VariantHandling`

### ECUC Packages
- `M2::AUTOSARTemplates::ECUCDescriptionTemplate`
- `M2::AUTOSARTemplates::ECUCParameterDefTemplate`

### System Template Packages
- `M2::AUTOSARTemplates::SystemTemplate`

### Top Level Packages
- `M2::AUTOSARTemplates::AutosarTopLevelStructure`

## Classes

### BSW Overview Classes
- `BswModuleDescription` - (M2::AUTOSARTemplates::BswModuleTemplate::BswOverview)
- `BswModuleDependency` - (M2::AUTOSARTemplates::BswModuleTemplate::BswOverview)

### BSW Interfaces Classes
- `BswModuleEntry` - (M2::AUTOSARTemplates::BswModuleTemplate::BswInterfaces)
- `BswModuleClientServerEntry` - (M2::AUTOSARTemplates::BswModuleTemplate::BswInterfaces)
- `BswEntryRelationshipSet` - (M2::AUTOSARTemplates::BswModuleTemplate::BswInterfaces)
- `BswEntryRelationship` - (M2::AUTOSARTemplates::BswModuleTemplate::BswInterfaces)
- `SwServiceArg` - (M2::AUTOSARTemplates::BswModuleTemplate::BswInterfaces)
- `SwPointerTargetProps` - (M2::AUTOSARTemplates::BswModuleTemplate::BswInterfaces)

### BSW Behavior Classes
- `BswInternalBehavior` - (M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior)
- `BswModuleEntity` - (M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior)
- `BswCalledEntity` - (M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior)
- `BswSchedulableEntity` - (M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior)
- `BswInterruptEntity` - (M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior)
- `BswModuleCallPoint` - (M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior)
- `BswDirectCallPoint` - (M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior)
- `BswSynchronousServerCallPoint` - (M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior)
- `BswAsynchronousServerCallPoint` - (M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior)
- `BswAsynchronousServerCallResultPoint` - (M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior)
- `BswVariableAccess` - (M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior)
- `BswEvent` - (M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior)
- `BswScheduleEvent` - (M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior)
- `BswTimingEvent` - (M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior)
- `BswBackgroundEvent` - (M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior)
- `BswInternalTriggerOccurredEvent` - (M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior)
- `BswExternalTriggerOccurredEvent` - (M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior)
- `BswModeSwitchEvent` - (M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior)
- `BswModeSwitchedAckEvent` - (M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior)
- `BswModeManagerErrorEvent` - (M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior)
- `BswOperationInvokedEvent` - (M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior)
- `BswAsynchronousServerCallReturnsEvent` - (M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior)
- `BswDataReceivedEvent` - (M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior)
- `BswInterruptEvent` - (M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior)
- `BswOsTaskExecutionEvent` - (M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior)
- `BswInternalTriggeringPoint` - (M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior)
- `BswModeReceiverPolicy` - (M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior)
- `BswModeSenderPolicy` - (M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior)
- `BswDataReceptionPolicy` - (M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior)
- `BswQueuedDataReceptionPolicy` - (M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior)
- `BswTriggerDirectImplementation` - (M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior)
- `BswModeSwitchAckRequest` - (M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior)

### BSW Implementation Classes
- `BswImplementation` - (M2::AUTOSARTemplates::BswModuleTemplate::BswImplementation)

### Common Structure Classes
- `InternalBehavior` - (M2::AUTOSARTemplates::CommonStructure::InternalBehavior)
- `ExecutableEntity` - (M2::AUTOSARTemplates::CommonStructure::InternalBehavior)
- `AbstractEvent` - (M2::AUTOSARTemplates::CommonStructure::InternalBehavior)
- `ExclusiveArea` - (M2::AUTOSARTemplates::CommonStructure::InternalBehavior)
- `ExclusiveAreaNestingOrder` - (M2::AUTOSARTemplates::CommonStructure::InternalBehavior)
- `SwcBswMapping` - (M2::AUTOSARTemplates::CommonStructure::SwcBswMapping)
- `SwcBswRunnableMapping` - (M2::AUTOSARTemplates::CommonStructure::SwcBswMapping)
- `SwcBswSynchronizedModeGroupPrototype` - (M2::AUTOSARTemplates::CommonStructure::SwcBswMapping)
- `SwcBswSynchronizedTrigger` - (M2::AUTOSARTemplates::CommonStructure::SwcBswMapping)
- `ResourceConsumption` - (M2::AUTOSARTemplates::CommonStructure::ResourceConsumption)
- `MemorySection` - (M2::AUTOSARTemplates::CommonStructure::ResourceConsumption::MemorySectionUsage)
- `StackUsage` - (M2::AUTOSARTemplates::CommonStructure::ResourceConsumption::StackUsage)
- `WorstCaseStackUsage` - (M2::AUTOSARTemplates::CommonStructure::ResourceConsumption::StackUsage)
- `MeasuredStackUsage` - (M2::AUTOSARTemplates::CommonStructure::ResourceConsumption::StackUsage)
- `RoughEstimateStackUsage` - (M2::AUTOSARTemplates::CommonStructure::ResourceConsumption::StackUsage)
- `HeapUsage` - (M2::AUTOSARTemplates::CommonStructure::ResourceConsumption::HeapUsage)
- `WorstCaseHeapUsage` - (M2::AUTOSARTemplates::CommonStructure::ResourceConsumption::HeapUsage)
- `MeasuredHeapUsage` - (M2::AUTOSARTemplates::CommonStructure::ResourceConsumption::HeapUsage)
- `RoughEstimateHeapUsage` - (M2::AUTOSARTemplates::CommonStructure::ResourceConsumption::HeapUsage)
- `ExecutionTime` - (M2::AUTOSARTemplates::CommonStructure::ResourceConsumption::ExecutionTime)
- `AnalyzedExecutionTime` - (M2::AUTOSARTemplates::CommonStructure::ResourceConsumption::ExecutionTime)
- `MeasuredExecutionTime` - (M2::AUTOSARTemplates::CommonStructure::ResourceConsumption::ExecutionTime)
- `SimulatedExecutionTime` - (M2::AUTOSARTemplates::CommonStructure::ResourceConsumption::ExecutionTime)
- `RoughEstimateOfExecutionTime` - (M2::AUTOSARTemplates::CommonStructure::ResourceConsumption::ExecutionTime)
- `McSupportData` - (M2::AUTOSARTemplates::CommonStructure::MeasurementCalibrationSupport)
- `McDataInstance` - (M2::AUTOSARTemplates::CommonStructure::MeasurementCalibrationSupport)
- `McSwEmulationMethodSupport` - (M2::AUTOSARTemplates::CommonStructure::MeasurementCalibrationSupport)
- `McParameterElementGroup` - (M2::AUTOSARTemplates::CommonStructure::MeasurementCalibrationSupport)
- `ImplementationElementInParameterInstanceRef` - (M2::AUTOSARTemplates::CommonStructure::MeasurementCalibrationSupport)
- `McFunction` - (M2::AUTOSARTemplates::CommonStructure::McGroups)
- `McGroup` - (M2::AUTOSARTemplates::CommonStructure::McGroups)
- `BswServiceDependency` - (M2::AUTOSARTemplates::CommonStructure::ServiceNeeds)
- `ServiceDependency` - (M2::AUTOSARTemplates::CommonStructure::ServiceNeeds)
- `ServiceNeeds` - (M2::AUTOSARTemplates::CommonStructure::ServiceNeeds)
- `NvBlockNeeds` - (M2::AUTOSARTemplates::CommonStructure::ServiceNeeds)
- `SupervisedEntityNeeds` - (M2::AUTOSARTemplates::CommonStructure::ServiceNeeds)
- `ComMgrUserNeeds` - (M2::AUTOSARTemplates::CommonStructure::ServiceNeeds)
- `EcuStateMgrUserNeeds` - (M2::AUTOSARTemplates::CommonStructure::ServiceNeeds)
- `CryptoServiceNeeds` - (M2::AUTOSARTemplates::CommonStructure::ServiceNeeds)
- `DltUserNeeds` - (M2::AUTOSARTemplates::CommonStructure::ServiceNeeds)
- `SyncTimeBaseMgrUserNeeds` - (M2::AUTOSARTemplates::CommonStructure::ServiceNeeds)
- `DiagnosticCapabilityElement` - (M2::AUTOSARTemplates::CommonStructure::ServiceNeeds)
- `FunctionInhibitionNeeds` - (M2::AUTOSARTemplates::CommonStructure::ServiceNeeds)
- `DoIpServiceNeeds` - (M2::AUTOSARTemplates::CommonStructure::ServiceNeeds)
- `DiagnosticEventNeeds` - (M2::AUTOSARTemplates::CommonStructure::ServiceNeeds)
- `DiagEventDebounceAlgorithm` - (M2::AUTOSARTemplates::CommonStructure::ServiceNeeds)
- `DiagEventDebounceCounterBased` - (M2::AUTOSARTemplates::CommonStructure::ServiceNeeds)
- `DiagEventDebounceTimeBased` - (M2::AUTOSARTemplates::CommonStructure::ServiceNeeds)
- `DiagEventDebounceMonitorInternal` - (M2::AUTOSARTemplates::CommonStructure::ServiceNeeds)
- `ErrorTracerNeeds` - (M2::AUTOSARTemplates::CommonStructure::ServiceNeeds)
- `HardwareTestNeeds` - (M2::AUTOSARTemplates::CommonStructure::ServiceNeeds)

### SW Component Template Classes
- `SwcServiceDependency` - (M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::ServiceMapping)
- `SwComponentType` - (M2::AUTOSARTemplates::SWComponentTemplate::Components)
- `AtomicSwComponentType` - (M2::AUTOSARTemplates::SWComponentTemplate::Components)
- `ApplicationSwComponentType` - (M2::AUTOSARTemplates::SWComponentTemplate::Components)
- `ComplexDeviceDriverSwComponentType` - (M2::AUTOSARTemplates::SWComponentTemplate::Components)
- `EcuAbstractionSwComponentType` - (M2::AUTOSARTemplates::SWComponentTemplate::Components)
- `SensorActuatorSwComponentType` - (M2::AUTOSARTemplates::SWComponentTemplate::Components)
- `ServiceSwComponentType` - (M2::AUTOSARTemplates::SWComponentTemplate::Components)
- `ServiceProxySwComponentType` - (M2::AUTOSARTemplates::SWComponentTemplate::Components)
- `NvBlockSwComponentType` - (M2::AUTOSARTemplates::SWComponentTemplate::Components)
- `SwcInternalBehavior` - (M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior)
- `SwcImplementation` - (M2::AUTOSARTemplates::SWComponentTemplate::SwcImplementation)
- `RunnableEntity` - (M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior)
- `RTEEvent` - (M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::RTEEvents)
- `OperationInvokedEvent` - (M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::RTEEvents)
- `TimingEvent` - (M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::RTEEvents)
- `DataReceivedEvent` - (M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::RTEEvents)
- `DataSendCompletedEvent` - (M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::RTEEvents)
- `DataWriteCompletedEvent` - (M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::RTEEvents)
- `DataReceiveErrorEvent` - (M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::RTEEvents)
- `ExternalTriggerOccurredEvent` - (M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::RTEEvents)
- `InternalTriggerOccurredEvent` - (M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::RTEEvents)
- `ModeSwitchedAckEvent` - (M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::RTEEvents)
- `SwcModeSwitchEvent` - (M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::RTEEvents)
- `SwcModeManagerErrorEvent` - (M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::RTEEvents)
- `BackgroundEvent` - (M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::RTEEvents)
- `OsTaskExecutionEvent` - (M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::RTEEvents)
- `TransformerHardErrorEvent` - (M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::RTEEvents)
- `ServerCallPoint` - (M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::ServerCall)
- `SynchronousServerCallPoint` - (M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::ServerCall)
- `AsynchronousServerCallPoint` - (M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::ServerCall)
- `AsynchronousServerCallResultPoint` - (M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::ServerCall)
- `VariableAccess` - (M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::DataElements)
- `ParameterAccess` - (M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::DataElements)
- `ModeSwitchPoint` - (M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::ModeDeclarationGroup)
- `ModeAccessPoint` - (M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::ModeDeclarationGroup)
- `InternalTriggeringPoint` - (M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::Trigger)
- `ExternalTriggeringPoint` - (M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::Trigger)

### Data Type and Data Prototype Classes
- `AutosarDataType` - (M2::AUTOSARTemplates::SWComponentTemplate::Datatype::Datatypes)
- `ApplicationDataType` - (M2::AUTOSARTemplates::SWComponentTemplate::Datatype::Datatypes)
- `ImplementationDataType` - (M2::AUTOSARTemplates::CommonStructure::ImplementationDataTypes)
- `ImplementationDataTypeElement` - (M2::AUTOSARTemplates::CommonStructure::ImplementationDataTypes)
- `AbstractImplementationDataType` - (M2::AUTOSARTemplates::CommonStructure::ImplementationDataTypes)
- `AbstractImplementationDataTypeElement` - (M2::AUTOSARTemplates::CommonStructure::ImplementationDataTypes)
- `DataPrototype` - (M2::AUTOSARTemplates::SWComponentTemplate::Datatype::DataPrototypes)
- `AutosarDataPrototype` - (M2::AUTOSARTemplates::SWComponentTemplate::Datatype::DataPrototypes)
- `VariableDataPrototype` - (M2::AUTOSARTemplates::SWComponentTemplate::Datatype::DataPrototypes)
- `ParameterDataPrototype` - (M2::AUTOSARTemplates::SWComponentTemplate::Datatype::DataPrototypes)
- `ArgumentDataPrototype` - (M2::AUTOSARTemplates::SWComponentTemplate::PortInterface)

### Port Interface Classes
- `PortInterface` - (M2::AUTOSARTemplates::SWComponentTemplate::PortInterface)
- `ClientServerInterface` - (M2::AUTOSARTemplates::SWComponentTemplate::PortInterface)
- `SenderReceiverInterface` - (M2::AUTOSARTemplates::SWComponentTemplate::PortInterface)
- `ModeSwitchInterface` - (M2::AUTOSARTemplates::SWComponentTemplate::PortInterface)
- `ParameterInterface` - (M2::AUTOSARTemplates::SWComponentTemplate::PortInterface)
- `NvDataInterface` - (M2::AUTOSARTemplates::SWComponentTemplate::PortInterface)
- `TriggerInterface` - (M2::AUTOSARTemplates::SWComponentTemplate::PortInterface)
- `ServiceInterface` - (M2::AUTOSARTemplates::SWComponentTemplate::PortInterface)
- `DiagnosticDataElementInterface` - (M2::AUTOSARTemplates::SWComponentTemplate::PortInterface)
- `DiagnosticRoutineInterface` - (M2::AUTOSARTemplates::SWComponentTemplate::PortInterface)
- `ClientServerOperation` - (M2::AUTOSARTemplates::SWComponentTemplate::PortInterface)
- `ApplicationInterface` - (M2::AUTOSARTemplates::SWComponentTemplate::PortInterface)
- `DiagnosticServiceInterface` - (M2::AUTOSARTemplates::SWComponentTemplate::PortInterface)

### Generic Structure Classes
- `ARPackage` - (M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::ARPackage)
- `AUTOSAR` - (M2::AUTOSARTemplates::AutosarTopLevelStructure)
- `Identifiable` - (M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::Identifiable)
- `Referrable` - (M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::Referrable)
- `MultilanguageReferrable` - (M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::MultilanguageReferrable)
- `ARObject` - (M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::ARObject)
- `AtpBlueprint` - (M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::AtpBlueprint)
- `AtpClassifier` - (M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::AtpClassifier)
- `AtpFeature` - (M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::AtpFeature)
- `AtpPrototype` - (M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::AtpPrototype)
- `AtpStructureElement` - (M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::AtpStructureElement)
- `CollectableElement` - (M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::CollectableElement)
- `PackageableElement` - (M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::PackageableElement)
- `UploadableDesignElement` - (M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::UploadableDesignElement)
- `UploadablePackageElement` - (M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::UploadablePackageElement)

### Mode Declaration Classes
- `ModeDeclarationGroup` - (M2::AUTOSARTemplates::CommonStructure::ModeDeclaration)
- `ModeDeclarationGroupPrototype` - (M2::AUTOSARTemplates::CommonStructure::ModeDeclaration)
- `ModeDeclaration` - (M2::AUTOSARTemplates::CommonStructure::ModeDeclaration)
- `ModeTransition` - (M2::AUTOSARTemplates::CommonStructure::ModeDeclaration)
- `ModeErrorBehavior` - (M2::AUTOSARTemplates::CommonStructure::ModeDeclaration)

### Trigger Declaration Classes
- `Trigger` - (M2::AUTOSARTemplates::CommonStructure::TriggerDeclaration)

### Implementation Classes
- `Implementation` - (M2::AUTOSARTemplates::CommonStructure::Implementation)
- `Code` - (M2::AUTOSARTemplates::CommonStructure::Implementation)
- `DependencyOnArtifact` - (M2::AUTOSARTemplates::CommonStructure::Implementation)
- `Compiler` - (M2::AUTOSARTemplates::CommonStructure::Implementation)
- `Linker` - (M2::AUTOSARTemplates::CommonStructure::Implementation)
- `BuildActionManifest` - (M2::AUTOSARTemplates::GenericStructure::BuildActionManifest)

### MSR Classes
- `SwBaseType` - (M2::MSR::AsamHdo::BaseTypes)
- `CompuMethod` - (M2::MSR::AsamHdo::ComputationMethod)
- `Unit` - (M2::MSR::AsamHdo::Units)
- `UnitGroup` - (M2::MSR::AsamHdo::Units)
- `DataConstr` - (M2::MSR::AsamHdo::ComputationMethod)
- `SwAddrMethod` - (M2::MSR::DataDictionary::AuxillaryObjects)
- `SwDataDefProps` - (M2::MSR::DataDictionary::DataDefProperties)
- `SwTextProps` - (M2::MSR::DataDictionary::DataDefProperties)
- `SwBitRepresentation` - (M2::MSR::DataDictionary::DataDefProperties)

### ECUC Classes
- `EcucModuleDef` - (M2::AUTOSARTemplates::ECUCParameterDefTemplate)
- `EcucModuleConfigurationValues` - (M2::AUTOSARTemplates::ECUCDescriptionTemplate)

### System Template Classes
- `System` - (M2::AUTOSARTemplates::SystemTemplate)

## Enumerations

### BSW Module Enumerations
- `BswCallType` - (M2::AUTOSARTemplates::BswModuleTemplate::BswInterfaces)
- `BswExecutionContext` - (M2::AUTOSARTemplates::BswModuleTemplate::BswInterfaces)
- `BswEntryKindEnum` - (M2::AUTOSARTemplates::BswModuleTemplate::BswInterfaces)
- `BswEntryRelationshipEnum` - (M2::AUTOSARTemplates::BswModuleTemplate::BswInterfaces)
- `BswInterruptCategory` - (M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior)
- `ReentrancyLevelEnum` - (M2::AUTOSARTemplates::CommonStructure::InternalBehavior)
- `ApiPrincipleEnum` - (M2::AUTOSARTemplates::CommonStructure::InternalBehavior)

### MSR Enumerations
- `SwServiceImplPolicyEnum` - (M2::MSR::DataDictionary::ServiceProcessTask)
- `SwCalibrationAccessEnum` - (M2::MSR::DataDictionary::DataDefProperties)
- `SwImplPolicyEnum` - (M2::MSR::DataDictionary::DataDefProperties)
- `MemorySectionType` - (M2::MSR::DataDictionary::AuxillaryObjects)
- `MemoryAllocationKeywordPolicyType` - (M2::MSR::DataDictionary::AuxillaryObjects)
- `SectionInitializationPolicyType` - (M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::PrimitiveTypes)

### Common Structure Enumerations
- `ArgumentDirectionEnum` - (M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::PrimitiveTypes)
- `ModeErrorReactionPolicyEnum` - (M2::AUTOSARTemplates::CommonStructure::ModeDeclaration)
- `ModeActivationKind` - (M2::AUTOSARTemplates::CommonStructure::ModeDeclaration)
- `DependencyUsageEnum` - (M2::AUTOSARTemplates::CommonStructure::Implementation)
- `ProgramminglanguageEnum` - (M2::AUTOSARTemplates::CommonStructure::Implementation)
- `EcucConfigurationVariantEnum` - (M2::AUTOSARTemplates::ECUCDescriptionTemplate)
- `RptAccessEnum` - (M2::AUTOSARTemplates::CommonStructure::MeasurementCalibrationSupport::RptSupport)
- `RptPreparationEnum` - (M2::AUTOSARTemplates::CommonStructure::MeasurementCalibrationSupport::RptSupport)
- `RptEnablerImplTypeEnum` - (M2::AUTOSARTemplates::CommonStructure::MeasurementCalibrationSupport::RptSupport)
- `RptExecutionControlEnum` - (M2::AUTOSARTemplates::SWComponentTemplate::RPTScenario)
- `RptServicePointEnum` - (M2::AUTOSARTemplates::SWComponentTemplate::RPTScenario)
- `AdditionalBindingTimeEnum` - (M2::AUTOSARTemplates::GenericStructure::VariantHandling)
- `BindingTimeEnum` - (M2::AUTOSARTemplates::GenericStructure::VariantHandling)
- `ArrayImplPolicyEnum` - (M2::AUTOSARTemplates::CommonStructure::ImplementationDataTypes)
- `ArraySizeHandlingEnum` - (M2::AUTOSARTemplates::CommonStructure::ImplementationDataTypes)
- `ArraySizeSemanticsEnum` - (M2::AUTOSARTemplates::CommonStructure::ImplementationDataTypes)

### Service Needs Enumerations
- `NvBlockNeedsReliabilityEnum` - (M2::AUTOSARTemplates::CommonStructure::ServiceNeeds)
- `NvBlockNeedsWritingPriorityEnum` - (M2::AUTOSARTemplates::CommonStructure::ServiceNeeds)
- `RamBlockStatusControlEnum` - (M2::AUTOSARTemplates::SWComponentTemplate::NvBlockComponent)
- `MaxCommModeEnum` - (M2::AUTOSARTemplates::CommonStructure::ServiceNeeds)
- `DiagnosticValueAccessEnum` - (M2::AUTOSARTemplates::CommonStructure::ServiceNeeds)
- `DiagnosticProcessingStyleEnum` - (M2::AUTOSARTemplates::CommonStructure::ServiceNeeds)
- `DiagnosticRoutineTypeEnum` - (M2::AUTOSARTemplates::CommonStructure::ServiceNeeds)
- `DiagnosticAudienceEnum` - (M2::AUTOSARTemplates::CommonStructure::ServiceNeeds)
- `EventAcceptanceStatusEnum` - (M2::AUTOSARTemplates::CommonStructure::ServiceNeeds)
- `StorageConditionStatusEnum` - (M2::AUTOSARTemplates::CommonStructure::ServiceNeeds)
- `OperationCycleTypeEnum` - (M2::AUTOSARTemplates::CommonStructure::ServiceNeeds)
- `DiagnosticClearDtcNotificationEnum` - (M2::AUTOSARTemplates::CommonStructure::ServiceNeeds)
- `VerificationStatusIndicationModeEnum` - (M2::AUTOSARTemplates::CommonStructure::ServiceNeeds)
- `ObdRatioConnectionKindEnum` - (M2::AUTOSARTemplates::CommonStructure::ServiceNeeds)

## Additional Classes

### System Constants and Documentation
- `SwSystemconst` - (M2::MSR::DataDictionary::SystemConstant)
- `SwcToImplMapping` - (M2::AUTOSARTemplates::SWComponentTemplate::Components)
- `SwcToEcuMapping` - (M2::AUTOSARTemplates::SWComponentTemplate::Components)
- `SwcToApplicationPartitionMapping` - (M2::AUTOSARTemplates::SWComponentTemplate::Components)
- `ECUMapping` - (M2::AUTOSARTemplates::SWComponentTemplate::Components)
- `ComManagementMapping` - (M2::AUTOSARTemplates::SWComponentTemplate::Components)
- `NvBlockDescriptor` - (M2::AUTOSARTemplates::SWComponentTemplate::Components)
- `PortPrototype` - (M2::AUTOSARTemplates::SWComponentTemplate::Components)
- `PPortPrototype` - (M2::AUTOSARTemplates::SWComponentTemplate::Components)
- `RPortPrototype` - (M2::AUTOSARTemplates::SWComponentTemplate::Components)
- `PrPortPrototype` - (M2::AUTOSARTemplates::SWComponentTemplate::Components)
- `DataTypeMappingSet` - (M2::AUTOSARTemplates::SWComponentTemplate::Datatype::Datatypes)
- `ConstantSpecification` - (M2::AUTOSARTemplates::CommonStructure::Constants)
- `ConstantSpecificationMappingSet` - (M2::AUTOSARTemplates::CommonStructure::Constants)

### Value Specification Classes
- `ValueSpecification` - (M2::AUTOSARTemplates::CommonStructure::Constants)
- `NumericalValueSpecification` - (M2::AUTOSARTemplates::CommonStructure::Constants)
- `ArrayValueSpecification` - (M2::AUTOSARTemplates::CommonStructure::Constants)
- `RecordValueSpecification` - (M2::AUTOSARTemplates::CommonStructure::Constants)
- `ApplicationRuleBasedValueSpecification` - (M2::AUTOSARTemplates::CommonStructure::Constants)
- `RuleBasedValueSpecification` - (M2::AUTOSARTemplates::CommonStructure::Constants)
- `RuleBasedValueCont` - (M2::AUTOSARTemplates::CommonStructure::Constants)
- `RuleArguments` - (M2::AUTOSARTemplates::CommonStructure::Constants)
- `NumericalOrText` - (M2::AUTOSARTemplates::CommonStructure::Constants)
- `ValueList` - (M2::MSR::DataDictionary::DataDefProperties)

### Data Access and Reference Classes
- `AutosarVariableRef` - (M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::DataElements)
- `AutosarParameterRef` - (M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::DataElements)
- `SwVariableRefProxy` - (M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::DataElements)
- `SwCalprmRefProxy` - (M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::DataElements)

### Data Type Classes
- `SwAxisType` - (M2::AUTOSARTemplates::SWComponentTemplate::Datatype::Datatypes)
- `SwRecordLayout` - (M2::AUTOSARTemplates::SWComponentTemplate::Datatype::Datatypes)
- `SwAxisCont` - (M2::AUTOSARTemplates::SWComponentTemplate::Datatype::Datatypes)
- `SwValueCont` - (M2::AUTOSARTemplates::SWComponentTemplate::Datatype::Datatypes)
- `SwCalprmAxisSet` - (M2::AUTOSARTemplates::SWComponentTemplate::Datatype::Datatypes)
- `SwGenericAxisParamType` - (M2::AUTOSARTemplates::SWComponentTemplate::Datatype::Datatypes)
- `InstantiationDataDefProps` - (M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior)

### Complex Data Types
- `ApplicationCompositeDataType` - (M2::AUTOSARTemplates::SWComponentTemplate::Datatype::Datatypes)
- `ApplicationPrimitiveDataType` - (M2::AUTOSARTemplates::SWComponentTemplate::Datatype::Datatypes)
- `ApplicationArrayElement` - (M2::AUTOSARTemplates::SWComponentTemplate::Datatype::Datatypes)
- `ApplicationRecordElement` - (M2::AUTOSARTemplates::SWComponentTemplate::Datatype::Datatypes)
- `ApplicationCompositeElementDataPrototype` - (M2::AUTOSARTemplates::SWComponentTemplate::Datatype::DataPrototypes)

### Mapping and Configuration Classes
- `DataTypeMap` - (M2::AUTOSARTemplates::SWComponentTemplate::Datatype::Datatypes)
- `ModeRequestTypeMap` - (M2::AUTOSARTemplates::CommonStructure::ModeDeclaration)
- `DataTypeMappingSet` - (M2::AUTOSARTemplates::SWComponentTemplate::Datatype::Datatypes)
- `IncludedDataTypeSet` - (M2::AUTOSARTemplates::SWComponentTemplate::Datatype::Datatypes)
- `IncludedModeDeclarationGroupSet` - (M2::AUTOSARTemplates::SWComponentTemplate::Datatype::Datatypes)
- `ApplicationError` - (M2::AUTOSARTemplates::SWComponentTemplate::PortInterface)

### Implementation Properties
- `ImplementationProps` - (M2::AUTOSARTemplates::CommonStructure::Implementation)
- `SymbolProps` - (M2::AUTOSARTemplates::CommonStructure::Implementation)
- `SymbolicNameProps` - (M2::AUTOSARTemplates::CommonStructure::Implementation)
- `SectionNamePrefix` - (M2::AUTOSARTemplates::CommonStructure::ResourceConsumption::MemorySectionUsage)
- `ExecutableEntityActivationReason` - (M2::AUTOSARTemplates::CommonStructure::InternalBehavior)
- `SwComponentDocumentation` - (M2::AUTOSARTemplates::SWComponentTemplate::SoftwareComponentDocumentation)

### Service Mapping Classes
- `RoleBasedMcDataAssignment` - (M2::AUTOSARTemplates::CommonStructure::MeasurementCalibrationSupport)
- `RoleBasedPortAssignment` - (M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::ServiceMapping)
- `RoleBasedBswModuleEntryAssignment` - (M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior)
- `RoleBasedDataAssignment` - (M2::AUTOSARTemplates::CommonStructure::ServiceNeeds)
- `RoleBasedDataTypeAssignment` - (M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::ServiceMapping)

### Resource Management
- `HardwareConfiguration` - (M2::AUTOSARTemplates::CommonStructure::ResourceConsumption)
- `SoftwareContext` - (M2::AUTOSARTemplates::CommonStructure::ResourceConsumption)
- `MemorySectionLocation` - (M2::AUTOSARTemplates::CommonStructure::ResourceConsumption::ExecutionTime)
- `TimeValue` - (M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::PrimitiveTypes)
- `MultidimensionalTime` - (M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::MultidimensionalTime)

This comprehensive list includes all the major classes and packages from the AUTOSAR BSW Module Description Template. These components together form the foundation for describing and configuring Basic Software Modules in the AUTOSAR standard.