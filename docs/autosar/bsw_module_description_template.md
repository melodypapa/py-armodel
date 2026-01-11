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
  - Attributes:
    - `moduleId: PositiveInteger [0..1]` (attr) - Refers to the BSW Module Identifier defined by the AUTOSAR standard
    - `expectedEntry: BswModuleEntry [*]` (ref) - Indicates an entry which is required by this module
    - `implementedEntry: BswModuleEntry [*]` (ref) - Specifies an entry provided by this module which can be called by other modules
    - `internalBehavior: BswInternalBehavior [*]` (aggr) - The various BswInternalBehaviors associated with a BswModuleDescription
    - `providedClientServerEntry: BswModuleClientServerEntry [*]` (aggr) - Specifies that this module provides a client server entry which can be called from another partition or core
    - `providedData: VariableDataPrototype [*]` (aggr) - Specifies a data prototype provided by this module in order to be read from another partition or core
    - `providedModeGroup: ModeDeclarationGroupPrototype [*]` (aggr) - A set of modes which is owned and provided by this module or cluster
    - `releasedTrigger: Trigger [*]` (aggr) - A Trigger released by this module or cluster
    - `requiredClientServerEntry: BswModuleClientServerEntry [*]` (aggr) - Specifies that this module requires a client server entry which can be implemented on another partition or core
    - `requiredData: VariableDataPrototype [*]` (aggr) - Specifies a data prototype required by this module in oder to be provided from another partition or core
    - `requiredModeGroup: ModeDeclarationGroupPrototype [*]` (aggr) - Specifies that this module or cluster depends on a certain mode group
    - `requiredTrigger: Trigger [*]` (aggr) - Specifies that this module or cluster reacts upon an external trigger
    - `bswModuleDependency: BswModuleDependency [*]` (aggr) - Describes the dependency to another BSW module
    - `bswModuleDocumentation: SwComponentDocumentation [0..1]` (aggr) - This adds a documentation to the BSW module
  - Category values:
    - `BSW_MODULE` - Specifies a single BSW module (ICC3 granularity)
    - `BSW_CLUSTER` - Specifies a BSW module cluster (ICC2 granularity)
    - `LIBRARY` - Specifies a Library (not restricted to be used within the BSW)
- `BswModuleDependency` - (M2::AUTOSARTemplates::BswModuleTemplate::BswOverview)
  - Attributes:
    - `targetModuleId: PositiveInteger [0..1]` (attr) - AUTOSAR identifier of the target module of which the dependencies are defined
    - `targetModuleRef: BswModuleDescription [0..1]` (ref) - Reference to the target module. It is an <<atpUriDef>> because the reference shall be used to identify the target module without actually needing the description of that target module
  - Note: Contains dependency information for BSW modules, including interfaces and dependencies to other modules

### BSW Interfaces Classes
- `BswModuleEntry` - (M2::AUTOSARTemplates::BswModuleTemplate::BswInterfaces)
  - Attributes:
    - `bswEntryKind: BswEntryKindEnum [0..1]` (attr) - This describes whether the entry is concrete or abstract
    - `callType: BswCallType [0..1]` (attr) - The type of call associated with this service
    - `executionContext: BswExecutionContext [0..1]` (attr) - Specifies the execution context which is required or guaranteed for this service
    - `functionPrototypeEmitter: NameToken [0..1]` (attr) - Used to control the generation of function prototypes
    - `isReentrant: Boolean [0..1]` (attr) - Reentrancy from the viewpoint of function callers
    - `isSynchronous: Boolean [0..1]` (attr) - Synchronicity from the viewpoint of function callers
    - `role: Identifier [0..1]` (attr) - Specifies the role of the entry in the given context
    - `serviceId: PositiveInteger [0..1]` (attr) - Refers to the service identifier of the Standardized Interfaces of AUTOSAR basic software
    - `swServiceImplPolicy: SwServiceImplPolicyEnum [0..1]` (attr) - Denotes the implementation policy as a standard function call, inline function or macro
    - `argument: SwServiceArg [*]` (aggr) - An argument belonging to this BswModuleEntry
    - `returnType: SwServiceArg [0..1]` (aggr) - The return type belonging to this BswModuleEntry
- `BswModuleClientServerEntry` - (M2::AUTOSARTemplates::BswModuleTemplate::BswInterfaces)
  - Attributes:
    - `encapsulatedEntry: BswModuleEntry [0..1]` (ref) - The underlying BswModuleEntry
    - `isReentrant: Boolean [0..1]` (attr) - Reentrancy from the viewpoint of clients invoking the service via the BSW Scheduler
    - `isSynchronous: Boolean [0..1]` (attr) - Synchronicity from the viewpoint of clients invoking the service via the BSW Scheduler
- `BswEntryRelationshipSet` - (M2::AUTOSARTemplates::BswModuleTemplate::BswInterfaces)
  - Attributes:
    - `bswEntryRelationship: BswEntryRelationship [*]` (aggr) - Relationship between two BswModuleEntrys
- `BswEntryRelationship` - (M2::AUTOSARTemplates::BswModuleTemplate::BswInterfaces)
  - Attributes:
    - `bswEntryRelationshipType: BswEntryRelationshipEnum [0..1]` (attr) - Denotes the type of the relationship
    - `from: BswModuleEntry [0..1]` (ref) - Type of relationship that refers to the abstract BswModuleEntry
    - `to: BswModuleEntry [0..1]` (ref) - Type of relationship that refers to the concrete BswModuleEntry
- `SwServiceArg` - (M2::AUTOSARTemplates::BswModuleTemplate::BswInterfaces)
  - Attributes:
    - `direction: ArgumentDirectionEnum [0..1]` (attr) - Specifies the direction of the data transfer
    - `swArraysize: ValueList [0..1]` (aggr) - This turns the argument of the service to an array
    - `swDataDefProps: SwDataDefProps [0..1]` (aggr) - Data properties of this SwServiceArg
- `SwPointerTargetProps` - (M2::AUTOSARTemplates::BswModuleTemplate::BswInterfaces)
  - Attributes:
    - `functionPointerSignature: BswModuleEntry [0..1]` (ref) - The referenced BswModuleEntry serves as the signature of a function pointer definition
    - `swDataDefProps: SwDataDefProps [0..1]` (aggr) - The properties of the target data type
    - `targetCategory: Identifier [0..1]` (attr) - This specifies the category of the target
  - Note: Related to BSW module interfaces, mode declarations, trigger declarations, and module dependencies as described in chapter 4 of the specification

### BSW Behavior Classes
- `BswInternalBehavior` - (M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior)
  - Attributes:
    - `arTypedPerInstanceMemory: VariableDataPrototype [*]` (aggr) - Defines an AUTOSAR typed memory-block that needs to be available for each instance of the Basic Software Module
    - `bswPerInstanceMemoryPolicy: BswPerInstanceMemoryPolicy [*]` (aggr) - Policy for a arTypedPerInstanceMemory. The policy selects the options of the Schedule Manager API generation
    - `clientPolicy: BswClientPolicy [*]` (aggr) - Policy for a requiredClientServerEntry. The policy selects the options of the Schedule Manager API generation
    - `distinguishedPartition: BswDistinguishedPartition [*]` (aggr) - Indicates an abstract partition context in which the enclosing BswModuleEntity can be executed
    - `entity: BswModuleEntity [*]` (aggr) - A code entity for which the behavior is described
    - `event: BswEvent [*]` (aggr) - An event required by this module behavior
    - `exclusiveAreaPolicy: BswExclusiveAreaPolicy [*]` (aggr) - Policy for an ExclusiveArea in this BswInternalBehavior. The policy selects the options of the Schedule Manager API generation
    - `includedDataTypeSet: IncludedDataTypeSet [*]` (aggr) - The includedDataTypeSet is used by a basic software module for its implementation
    - `includedModeDeclarationGroupSet: IncludedModeDeclarationGroupSet [*]` (aggr) - This aggregation represents the included Mode DeclarationGroups
    - `internalTriggeringPoint: BswInternalTriggeringPoint [*]` (aggr) - An internal triggering point
    - `internalTriggeringPointPolicy: BswInternalTriggeringPointPolicy [*]` (aggr) - Policy for an internalTriggeringPoint in this BswInternalBehavior. The policy selects the options of the Schedule Manager API generation
    - `modeReceiverPolicy: BswModeReceiverPolicy [*]` (aggr) - Implementation policy for the reception of mode switches
    - `modeSenderPolicy: BswModeSenderPolicy [*]` (aggr) - Implementation policy for providing a mode group
    - `parameterPolicy: BswParameterPolicy [*]` (aggr) - Policy for a perInstanceParameter in this BswInternalBehavior. The policy selects the options of the Schedule Manager API generation
    - `perInstanceParameter: ParameterDataPrototype [*]` (aggr) - Describes a read only memory object containing characteristic value(s) needed by this BswInternalBehavior
    - `receptionPolicy: BswDataReceptionPolicy [*]` (aggr) - Data reception policy for inter-partition and/or inter-core communication
    - `releasedTriggerPolicy: BswReleasedTriggerPolicy [*]` (aggr) - Policy for a releasedTrigger. The policy selects the options of the Schedule Manager API generation
    - `schedulerNamePrefix: BswSchedulerNamePrefix [*]` (aggr) - Optional definition of one or more prefixes to be used for the BswScheduler
    - `sendPolicy: BswDataSendPolicy [*]` (aggr) - Policy for a providedData. The policy selects the options of the Schedule Manager API generation
    - `serviceDependency: BswServiceDependency [*]` (aggr) - Defines the requirements on AUTOSAR Services for a particular item
    - `triggerDirectImplementation: BswTriggerDirectImplementation [*]` (aggr) - Specifies a trigger to be directly implemented via OS calls
    - `variationPointProxy: VariationPointProxy [*]` (aggr) - Proxy of a variation points in the C/C++ implementation
  - Note: Specifies the behavior of a BSW module or a BSW cluster w.r.t. the code entities visible by the BSW Scheduler. It is possible to have several different BswInternalBehaviors referring to the same BswModuleDescription
- `BswModuleEntity` - (M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior)
  - Attributes:
    - `accessedModeGroup: ModeDeclarationGroupPrototype [*]` (ref) - A mode group which is accessed via API call by this entity. It shall be a ModeDeclarationGroupPrototype required by this module or cluster
    - `activationPoint: BswInternalTriggeringPoint [*]` (ref) - Activation point used by the module entity to activate one or more internal triggers
    - `callPoint: BswModuleCallPoint [*]` (aggr) - A call point used in the code of this entity
    - `dataReceivePoint: BswVariableAccess [*]` (aggr) - The data is received via the BSW Scheduler
    - `dataSendPoint: BswVariableAccess [*]` (aggr) - The data is sent via the BSW Scheduler
    - `implementedEntry: BswModuleEntry [0..1]` (ref) - The entry which is implemented by this module entity
    - `issuedTrigger: Trigger [*]` (ref) - A trigger issued by this entity via BSW Scheduler API call. It shall be a BswTrigger released (i.e. owned) by this module or cluster
    - `managedModeGroup: ModeDeclarationGroupPrototype [*]` (ref) - A mode group which is managed by this entity. It shall be a ModeDeclarationGroupPrototype provided by this module or cluster
    - `schedulerNamePrefix: BswSchedulerNamePrefix [0..1]` (ref) - A prefix to be used in generated names for the BswModuleScheduler in the context of this BswModuleEntity
  - Note: Specifies the smallest code fragment which can be described for a BSW module or cluster within AUTOSAR
- `BswCalledEntity` - (M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior)
  - Note: BSW module entity which is designed to be called from another BSW module or cluster
- `BswSchedulableEntity` - (M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior)
  - Note: BSW module entity, which is designed for control by the BSW Scheduler. It may for example implement a so-called "main" function
- `BswInterruptEntity` - (M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior)
  - Attributes:
    - `interruptCategory: BswInterruptCategory [0..1]` (attr) - Category of the interrupt
    - `interruptSource: String [0..1]` (attr) - Allows a textual documentation of the intended interrupt source
  - Note: BSW module entity, which is designed to be triggered by an interrupt
- `BswModuleCallPoint` - (M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior)
  - Attributes:
    - `contextLimitation: BswDistinguishedPartition [*]` (ref) - The existence of this reference indicates that the call point is used only in the context of the referred BswDistinguishedPartitions
  - Note: Represents a point at which a BswModuleEntity handles a procedure call into a BswModuleEntry, either directly or via the BSW Scheduler
- `BswDirectCallPoint` - (M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior)
  - Attributes:
    - `calledEntry: BswModuleEntry [0..1]` (ref) - The BswModuleEntry called at this point
    - `calledFromWithinExclusiveArea: ExclusiveAreaNestingOrder [0..1]` (ref) - This indicates that the call point is located at the deepest level inside one or more ExclusiveAreas that are nested in the given order
  - Note: Represents a concrete point in the code from where a BswModuleEntry is called directly, i.e. not via the BSW Scheduler
- `BswSynchronousServerCallPoint` - (M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior)
  - Attributes:
    - `calledEntry: BswModuleClientServerEntry [0..1]` (ref) - The entry to be called
    - `calledFromWithinExclusiveArea: ExclusiveAreaNestingOrder [0..1]` (ref) - This indicates that the call point is located at the deepest level inside one or more ExclusiveAreas that are nested in the given order
  - Note: Represents a synchronous procedure call point via the BSW Scheduler
- `BswAsynchronousServerCallPoint` - (M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior)
  - Attributes:
    - `calledEntry: BswModuleClientServerEntry [0..1]` (ref) - The entry to be called
  - Note: Represents an asynchronous procedure call point via the BSW Scheduler
- `BswAsynchronousServerCallResultPoint` - (M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior)
  - Attributes:
    - `asynchronousServerCallPoint: BswAsynchronousServerCallPoint [0..1]` (ref) - The call point invoking the call to which the result belongs
  - Note: The callback point for an BswAsynchronousServerCallPoint i.e. the point at which the result can be retrieved from the BSW Scheduler
- `BswVariableAccess` - (M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior)
  - Attributes:
    - `accessedVariable: VariableDataPrototype [0..1]` (ref) - The data accessed via the BSW Scheduler
    - `contextLimitation: BswDistinguishedPartition [*]` (ref) - The existence of this reference indicates that the variable is received resp. sent only in the context of the referred BswDistinguishedPartitions
- `BswEvent` - (M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior)
  - Attributes:
    - `contextLimitation: BswDistinguishedPartition [*]` (ref) - The existence of this reference indicates that the usage of the event is limited to the context of the referred BswDistinguishedPartitions
    - `disabledInMode: ModeDeclaration [*]` (iref) - The modes, in which this event is disabled
    - `startsOnEvent: BswModuleEntity [0..1]` (ref) - The entity which is started by the event
  - Note: Base class of various kinds of events which are used to trigger a BswModuleEntity of this BSW module or cluster. The event is local to the BSW module or cluster. The short name of the meta-class instance is intended as an input to configure the required API of the BSW Scheduler
  - Constraints:
    - [constr_10328] For each BswEvent, the reference in the role startsOnEvent shall exist at the time when the configuration of the BSW module is finished
- `BswScheduleEvent` - (M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior)
  - Note: BswEvent that is able to start a BswSchedulabeEntity. Base classes: ARObject, AbstractEvent, BswEvent, Identifiable, MultilanguageReferrable, Referrable
  - Constraints:
    - [constr_1275] The reference BswScheduleEvent.startsOnEvent shall only refer to a BswSchedulableEntity
- `BswTimingEvent` - (M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior)
  - Attributes:
    - `period: TimeValue [0..1]` (attr) - Requirement for the time period (in seconds) by which this event is triggered
  - Note: A recurring BswEvent driven by a time period. Base classes: ARObject, AbstractEvent, BswEvent, BswScheduleEvent, Identifiable, MultilanguageReferrable, Referrable
  - Constraints:
    - [constr_10281] For each BswTimingEvent, the attribute period shall exist at the time when the configuration of the BSW module is finished
    - [constr_4043] BswTimingEvent.period shall be greater than 0
- `BswBackgroundEvent` - (M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior)
  - Note: A recurring BswEvent which is used to perform background activities. It is similar to a BswTimingEvent but has no fixed time period and is activated only with low priority. Base classes: ARObject, AbstractEvent, BswEvent, BswScheduleEvent, Identifiable, MultilanguageReferrable, Referrable
- `BswInternalTriggerOccurredEvent` - (M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior)
  - Attributes:
    - `eventSource: BswInternalTriggeringPoint [0..1]` (ref) - The activation point is the source of this event
  - Note: A BswEvent, which can happen sporadically. The event is activated by explicit calls from the module to the BSW Scheduler. The main purpose for such an event is to cause a context switch, e.g. from an ISR context into a task context. Activation and switching are handled within the same module or cluster only. Base classes: ARObject, AbstractEvent, BswEvent, BswScheduleEvent, Identifiable, MultilanguageReferrable, Referrable
  - Constraints:
    - [constr_10282] For each BswInternalTriggerOccurredEvent, the reference in the role eventSource shall exist at the time when the configuration of the BSW module is finished
- `BswExternalTriggerOccurredEvent` - (M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior)
  - Attributes:
    - `trigger: Trigger [0..1]` (ref) - The trigger associated with this event. The trigger is external to this module
  - Note: A BswEvent resulting from a trigger released by another module or cluster. Base classes: ARObject, AbstractEvent, BswEvent, BswScheduleEvent, Identifiable, MultilanguageReferrable, Referrable
  - Constraints:
    - [constr_10283] For each BswExternalTriggerOccurredEvent, the reference in the role trigger shall exist at the time when the configuration of the BSW module is finished
    - [constr_4023] A BswExternalTriggerOccurredEvent shall refer to a Trigger that is declared via BswModuleDescription.requiredTrigger for the same module
- `BswModeSwitchEvent` - (M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior)
  - Attributes:
    - `activation: ModeActivationKind [0..1]` (attr) - Kind of activation w.r.t. to the referred mode
    - `mode (ordered): ModeDeclaration [0..2]` (iref) - Reference to one or two Modes that initiate the Mode Switch Event. InstanceRef implemented by: ModeInBswModuleDescriptionInstanceRef
  - Note: A BswEvent resulting from a mode switch. Base classes: ARObject, AbstractEvent, BswEvent, BswScheduleEvent, Identifiable, MultilanguageReferrable, Referrable
  - Constraints:
    - [constr_10284] For each BswModeSwitchEvent, the attribute activation shall exist at the time when the configuration of the BSW module is finished
    - [constr_4024] If BswModeSwitchEvent.activation has the value onTransition BswModeSwitchEvent shall refer to two different modes belonging to the same instance of ModeDeclarationGroup, their order defining the direction of the transition. In all other cases, BswModeSwitchEvent shall refer to exactly one mode
    - [constr_4066] For each pair of ModeDeclaration's referenced by a BswModeSwitchEvent with attribute activation set to onTransition a ModeTransition shall be defined in the corresponding direction (i.e. from exitedMode to enteredMode). This constraint shall only apply if the respective ModeDeclarationGroup defines at least one modeTransition
    - [constr_4025] The ModeDeclaration used by BswModeSwitchEvent shall belong to the ModeDeclarationGroupPrototype referred as BswInternalBehavior.entity.accessedModeGroup of the enclosing BswInternalBehavior
- `BswModeSwitchedAckEvent` - (M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior)
  - Attributes:
    - `modeGroup: ModeDeclarationGroupPrototype [0..1]` (ref) - A mode group provided by this module. The acknowledgement of a switch of this group raises this event
  - Note: The event is raised after a switch of the referenced mode group has been acknowledged or an error occurs. The referenced mode group shall be provided by this module. Base classes: ARObject, AbstractEvent, BswEvent, BswScheduleEvent, Identifiable, MultilanguageReferrable, Referrable
  - Constraints:
- `BswDistinguishedPartition` - (M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior)
  - Note: Each instance of this meta-class represents an abstract partition in which context the code of the enclosing BswModuleBehavior can be executed. The intended use case is to distinguish between several partitions in order to implement different behavior per partition, for example to behave either as a master or satellite in a multicore ECU with shared BSW code. Base classes: ARObject, Referrable
  - Aggregated by: BswInternalBehavior.distinguishedPartition
  - Constraints:
    - [constr_4083] BswDistinguishedPartition shall be used only in the context of a particular BswInternalBehavior - All instances of BswEvent, BswModuleCallPoint and BswVariableAccess which refer to a BswDistinguishedPartition shall belong to the same BswInternalBehavior that also aggregates the referred BswDistinguishedPartition
    - [constr_10285] For each BswModeSwitchedAckEvent, the reference in the role modeGroup shall exist at the time when the configuration of the BSW module is finished
    - [constr_4026] The ModeDeclarationGroupPrototype used by BswModeSwitchedAckEvent shall be referred as BswModuleDescription.providedModeGroup by the same module
- `BswModeManagerErrorEvent` - (M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior)
  - Attributes:
    - `modeGroup: ModeDeclarationGroupPrototype [0..1]` (ref) - This represents the ModeDeclarationGroupPrototype for which the error behavior of the mode manager applies
  - Note: This represents the ability to react on errors occurring during mode handling. Base classes: ARObject, AbstractEvent, BswEvent, BswScheduleEvent, Identifiable, MultilanguageReferrable, Referrable
  - Constraints:
    - [constr_10286] For each BswModeManagerErrorEvent, the reference in the role modeGroup shall exist at the time when the configuration of the BSW module is finished
    - [constr_4081] The ModeDeclarationGroupPrototype used by BswModeManagerErrorEvent shall be referred as BswModuleDescription.providedModeGroup by the same module
- `BswOperationInvokedEvent` - (M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior)
  - Attributes:
    - `entry: BswModuleClientServerEntry [0..1]` (ref) - The providedClientServerEntry invoked by this event
  - Note: This event is thrown on operation invocation in Client-Server-Communication via the BSW Scheduler. Its "entry" reference provides the BswClientServerEntry that is called subsequently. Note this event is not needed in case of direct function calls. Base classes: ARObject, AbstractEvent, BswEvent, Identifiable, MultilanguageReferrable, Referrable
  - Constraints:
    - [constr_10287] For each BswOperationInvokedEvent, the reference in the role entry shall exist at the time when the configuration of the BSW module is finished
    - [constr_4078] The BswCalledEntity referred by the attribute BswOperationInvokedEvent.startsOnEvent shall refer to the same BswModuleEntry (via its attribute implementedEntry) as the BswOperationInvokedEvent (via its attribute entry.encapsulatedEntry)
    - [constr_4098] A BswOperationInvokedEvent shall not have a reference to a ModeDeclaration in the role disabledInMode
- `BswAsynchronousServerCallReturnsEvent` - (M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior)
  - Attributes:
    - `eventSource: BswAsynchronousServerCallResultPoint [0..1]` (ref) - The call point to be used for retrieving the result
  - Note: This is the "callback" event for asynchronous Client-Server-Communication via the BSW Scheduler which is thrown after completion of the asynchronous Client-Server call. Its eventSource specifies the call point to be used for retrieving the result
  - Constraints:
    - [constr_10288] For each BswAsynchronousServerCallReturnsEvent, the reference in the role eventSource shall exist at the time when the configuration of the BSW module is finished
- `BswDataReceivedEvent` - (M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior)
  - Attributes:
    - `data: VariableDataPrototype [0..1]` (ref) - The received data
  - Note: This event is thrown on reception of the referenced data via Sender-Receiver-Communication over the BSW Scheduler
  - Constraints:
    - [constr_10289] For each BswDataReceivedEvent, the reference in the role data shall exist at the time when the configuration of the BSW module is finished
- `BswInterruptEvent` - (M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior)
  - Note: This meta-class represents an event triggered by an interrupt. Base classes: ARObject, AbstractEvent, BswEvent, Identifiable, MultilanguageReferrable, Referrable
- `BswOsTaskExecutionEvent` - (M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior)
  - Note: This BswEvent is supposed to execute BswSchedulableEntitys which have to react on the execution of specific OsTasks. Therefore, this event is unconditionally raised whenever the OsTask on which it is mapped is executed. The main use case for this event is scheduling of Runnables of Complex Drivers which have to react on task executions. Base classes: ARObject, AbstractEvent, BswEvent, BswScheduleEvent, Identifiable, MultilanguageReferrable, Referrable
- `BswInternalTriggeringPoint` - (M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior)
  - Attributes:
    - `swImplPolicy: SwImplPolicyEnum [0..1]` (attr) - This attribute, when set to value queued, specifies a queued processing of the internal trigger event
  - Note: Represents the activation point for one or more BswInternalTriggerOccurredEvents
  - Constraints:
    - [constr_4065] The only allowed values for the attribute BswInternalTriggeringPoint.swImplPolicy are either STANDARD (in which case the internal trigger processing does not use a queue) or QUEUED (in which case the internal trigger processing uses a queue)
- `BswExclusiveAreaPolicy` - (M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior)
  - Attributes:
    - `apiPrinciple: ApiPrincipleEnum [0..1]` (attr) - Specifies for this ExclusiveArea if either one common set of Enter and Exit APIs for the whole BSW module is requested from the SchM or if the set of Enter and Exit APIs is expected per BswModuleEntity
    - `exclusiveArea: ExclusiveArea [0..1]` (ref) - The ExclusiveArea for which the BSW Scheduler using this policy
  - Attributes:
    - `apiPrinciple: ApiPrincipleEnum [0..1]` (attr) - Specifies for this ExclusiveArea if either one common set of Enter and Exit APIs for the whole BSW module is requested from the SchM or if the set of Enter and Exit APIs is expected per BswModuleEntity
    - `exclusiveArea: ExclusiveArea [0..1]` (ref) - The ExclusiveArea for which the BSW Scheduler using this policy
- `BswModeReceiverPolicy` - (M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior)
- `BswModeSenderPolicy` - (M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior)
- `BswDataReceptionPolicy` - (M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior)
- `BswQueuedDataReceptionPolicy` - (M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior)
- `BswTriggerDirectImplementation` - (M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior)
- `BswModeSwitchAckRequest` - (M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior)

### BSW Implementation Classes
- `BswImplementation` - (M2::AUTOSARTemplates::BswModuleTemplate::BswImplementation)
  - Attributes:
    - `arReleaseVersion: RevisionLabelString [0..1]`
    - `vendorApiInfix: Identifier [0..1]`
  - Note: Bottom layer of BSWMDT three-layer approach, contains information on the individual code, may have several instances for the same BswInternalBehavior

### Common Structure Classes
- `InternalBehavior` - (M2::AUTOSARTemplates::CommonStructure::InternalBehavior)
  - Attributes:
    - `constantMemory: ParameterDataPrototype [*]` (aggr) - Describes a read only memory object containing characteristic value(s) implemented by this InternalBehavior
    - `constantValueMapping: ConstantSpecificationMappingSet [*]` (ref) - Reference to the ConstantSpecificationMapping to be applied for the particular InternalBehavior
    - `dataTypeMapping: DataTypeMappingSet [*]` (ref) - Reference to the DataTypeMapping to be applied for the particular InternalBehavior
    - `exclusiveArea: ExclusiveArea [*]` (aggr) - This specifies an ExclusiveArea for this InternalBehavior
    - `exclusiveAreaNestingOrder: ExclusiveAreaNestingOrder [*]` (aggr) - This represents the set of ExclusiveAreaNestingOrder owned by the InternalBehavior
    - `staticMemory: VariableDataPrototype [*]` (aggr) - Describes a read and writeable static memory object representing measurerment variables implemented by this software component
  - Note: Common base class (abstract) for the internal behavior of both software components and basic software modules/clusters
- `ExecutableEntity` - (M2::AUTOSARTemplates::CommonStructure::InternalBehavior)
  - Attributes:
    - `activationReason: ExecutableEntityActivationReason [*]` (aggr) - If the ExecutableEntity provides at least one activationReason element the RTE resp. BSW Scheduler shall provide means to read the activation vector of this executable entity execution. If no activationReason element is provided the feature of being able to determine the activating RTEEvent is disabled for this ExecutableEntity
    - `canEnter: ExclusiveArea [*]` (ref) - This means that the executable entity can enter/leave the referenced exclusive area through explicit API calls
    - `exclusiveAreaNestingOrder: ExclusiveAreaNestingOrder [*]` (ref) - This represents the set of ExclusiveAreaNestingOrders recognized by this ExecutableEntity
    - `minimumStartInterval: TimeValue [0..1]` (attr) - Specifies the time in seconds by which two consecutive starts of an ExecutableEntity are guaranteed to be separated
    - `reentrancyLevel: ReentrancyLevelEnum [0..1]` (attr) - The reentrancy level of this ExecutableEntity
    - `runsInside: ExclusiveArea [*]` (ref) - The executable entity runs completely inside the referenced exclusive area
    - `swAddrMethod: SwAddrMethod [0..1]` (ref) - Addressing method related to this code entity
  - Note: Abstraction of executable code
- `AbstractEvent` - (M2::AUTOSARTemplates::CommonStructure::InternalBehavior)
- `ExclusiveArea` - (M2::AUTOSARTemplates::CommonStructure::InternalBehavior)
  - Note: Prevents an executable entity running in the area from being preempted
  - Base classes: ARObject, Identifiable, MultilanguageReferrable, Referrable
- `ExclusiveAreaNestingOrder` - (M2::AUTOSARTemplates::CommonStructure::InternalBehavior)
  - Attributes:
    - `exclusiveArea (ordered): ExclusiveArea [*]` (ref) - This represents a specific scenario of how Exclusive Areas can be used in terms of the nesting order
    - `exclusiveArea: ExclusiveArea [*]` (ref) - This represents a specific scenario of how ExclusiveAreas can be used in terms of the nesting order
- `SwcBswMapping` - (M2::AUTOSARTemplates::CommonStructure::SwcBswMapping)
- `SwcBswRunnableMapping` - (M2::AUTOSARTemplates::CommonStructure::SwcBswMapping)
- `SwcBswSynchronizedModeGroupPrototype` - (M2::AUTOSARTemplates::CommonStructure::SwcBswMapping)
- `SwcBswSynchronizedTrigger` - (M2::AUTOSARTemplates::CommonStructure::SwcBswMapping)
- `ResourceConsumption` - (M2::AUTOSARTemplates::CommonStructure::ResourceConsumption)
  - Note: Related to resource consumption aspects as described in chapter 8 of the specification
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
  - Note: Related to measurement and calibration support as described in chapter 9 of the specification
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
  - Note: SW Component Template elements that are shared between BSW and SWC contexts

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
  - Attributes (from class table example in documentation):
    - `arPackages: ARPackage [0..*]` (aggr)
    - `adminData: AdminData [0..1]` (aggr)
    - `topLevelPackages: CollectableElement [0..*]` (aggr)
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
  - Attributes:
    - `initialMode: ModeDeclaration [0..1]` (ref) - The initial mode of the ModeDeclarationGroup. This mode is active before any mode switches occurred
    - `modeDeclaration: ModeDeclaration [*]` (aggr) - The ModeDeclarations collected in this ModeDeclarationGroup
    - `modeManagerErrorBehavior: ModeErrorBehavior [0..1]` (aggr) - This represents the ability to define the error behavior expected by the mode manager in case of errors on the mode user side
    - `modeTransition: ModeTransition [*]` (aggr) - This represents the avaliable ModeTransitions of the ModeDeclarationGroup
    - `modeUserErrorBehavior: ModeErrorBehavior [0..1]` (aggr) - This represents the definition of the error behavior expected by the mode user in case of errors on the mode manager side
    - `onTransitionValue: PositiveInteger [0..1]` (attr) - The value of this attribute shall be taken into account by the RTE generator for programmatically representing a value used for the transition between two statuses
- `ModeDeclarationGroupPrototype` - (M2::AUTOSARTemplates::CommonStructure::ModeDeclaration)
  - Attributes:
    - `swCalibrationAccess: SwCalibrationAccessEnum [0..1]` (attr) - This allows for specifying whether or not the enclosing ModeDeclarationGroupPrototype can be measured at run-time
    - `type: ModeDeclarationGroup [0..1]` (tref) - The "collection of ModeDeclarations" ( = ModeDeclarationGroup) supported by a component
- `ModeDeclaration` - (M2::AUTOSARTemplates::CommonStructure::ModeDeclaration)
  - Attributes:
    - `value: PositiveInteger [0..1]` (attr) - The RTE shall take the value of this attribute for generating the source code representation of this Mode Declaration
- `ModeTransition` - (M2::AUTOSARTemplates::CommonStructure::ModeDeclaration)
  - Attributes:
    - `enteredMode: ModeDeclaration [0..1]` (ref) - This represents the entered model of the ModeTransition
    - `exitedMode: ModeDeclaration [0..1]` (ref) - This represents the exited mode of the ModeTransition
- `ModeErrorBehavior` - (M2::AUTOSARTemplates::CommonStructure::ModeDeclaration)
  - Attributes:
    - `defaultMode: ModeDeclaration [0..1]` (ref) - This represents the ModeDeclaration that is considered the error mode in the context of the enclosing ModeDeclarationGroup
    - `errorReactionPolicy: ModeErrorReactionPolicyEnum [0..1]` (attr) - This represents the ability to define the policy in terms of which default model shall apply in case an error occurs

### Trigger Declaration Classes
- `Trigger` - (M2::AUTOSARTemplates::CommonStructure::TriggerDeclaration)
  - Attributes:
    - `swImplPolicy: SwImplPolicyEnum [0..1]` (attr) - This attribute, when set to value queued, allows for a queued processing of Triggers
    - `triggerPeriod: MultidimensionalTime [0..1]` (aggr) - Optional definition of a period in case of a periodically (time or angle) driven external trigger

### Implementation Classes
- `Implementation` - (M2::AUTOSARTemplates::CommonStructure::Implementation)
  - Note: Contains implementation description elements as described in chapter 7 of the specification
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
  - Values:
    - `callback` - Callback (i.e. the caller specifies the signature)
    - `callout` - Callout - provide defined means to extend the functionality of an existing module
    - `interrupt` - Interrupt routine
    - `regular` - Regular API call
    - `scheduled` - Called by the scheduler
- `BswExecutionContext` - (M2::AUTOSARTemplates::BswModuleTemplate::BswInterfaces)
  - Values:
    - `hook` - Context of an OS "hook" routine
    - `interruptCat1` - CAT1 interrupt context
    - `interruptCat2` - CAT2 interrupt context
    - `task` - Task context
    - `unspecified` - The execution context is not specified by the API
- `BswEntryKindEnum` - (M2::AUTOSARTemplates::BswModuleTemplate::BswInterfaces)
  - Values:
    - `abstract` - This BswModuleEntry specifies an abstract signature of C-functions
    - `concrete` - This BswModuleEntry specifies a concrete C-function with its signature
- `BswEntryRelationshipEnum` - (M2::AUTOSARTemplates::BswModuleTemplate::BswInterfaces)
  - Values:
    - `derivedFrom` - Describes that the BswModuleEntry referenced as "to" needs to have the same signature as the "abstract" BswModuleEntry referenced as "from"
- `BswInterruptCategory` - (M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior)
  - Literals:
    - `cat1` - Cat1 interrupt routines are not controlled by the OS and are only allowed to make a very limited selection of OS calls to enable and disable all interrupts. The BswInterruptEntity is implemented by the interrupt service routine, which is directly called from the interrupt vector (not via the OS)
    - `cat2` - Cat2 interrupt routines are controlled by the OS and they are allowed to make OS calls. The BswInterruptEntity is implemented by the interrupt handler, which is called from the OS
  - Note: Category of the interrupt service
- `ReentrancyLevelEnum` - (M2::AUTOSARTemplates::CommonStructure::InternalBehavior)
  - Literals:
    - `multicoreReentrant` - Unlimited concurrent execution of this entity is possible, including preemption and parallel execution on multi core systems
    - `nonReentrant` - Concurrent execution of this entity is not possible
    - `singleCoreReentrant` - Pseudo-concurrent execution (i.e. preemption) of this entity is possible on single core systems
  - Note: Specifies if and in which kinds of environments an entity is reentrant
- `ApiPrincipleEnum` - (M2::AUTOSARTemplates::CommonStructure::InternalBehavior)
  - Values:
    - `common` - The Rte or SchM API is provided for the whole software component / BSW Module. Tags: atp.EnumerationLiteralIndex=0
    - `perExecutable` - The Rte or SchM API is provided for a specific ExecutableEntity of a software component / BSW Module. Tags: atp.EnumerationLiteralIndex=1
  - Note: This enumeration represents the ability to control the granularity of API generation

### MSR Enumerations
- `SwServiceImplPolicyEnum` - (M2::MSR::DataDictionary::ServiceProcessTask)
  - Values:
    - `inline` - inline service definition
    - `inlineConditional` - The service is implemented in a way that it either resolves to an inline function or to a standard function depending on conditions
    - `macro` - macro service definition
    - `standard` - Standard service and default value, if nothing is defined
- `SwCalibrationAccessEnum` - (M2::MSR::DataDictionary::DataDefProperties)
- `SwImplPolicyEnum` - (M2::MSR::DataDictionary::DataDefProperties)
- `MemorySectionType` - (M2::MSR::DataDictionary::AuxillaryObjects)
- `MemoryAllocationKeywordPolicyType` - (M2::MSR::DataDictionary::AuxillaryObjects)
- `SectionInitializationPolicyType` - (M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::PrimitiveTypes)

### Common Structure Enumerations
- `ArgumentDirectionEnum` - (M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::PrimitiveTypes)
  - Values:
    - `in` - The argument value is passed to the callee
    - `inout` - The argument value is passed to the callee but also passed back from the callee to the caller
    - `out` - The argument value is passed from the callee to the caller
- `ModeErrorReactionPolicyEnum` - (M2::AUTOSARTemplates::CommonStructure::ModeDeclaration)
  - Values:
    - `defaultMode` - This represents the ability to switch to the defaultMode in case of a mode error
    - `lastMode` - This represents the ability to keep the last mode in case of a mode error
- `ModeActivationKind` - (M2::AUTOSARTemplates::CommonStructure::ModeDeclaration)
  - Values:
    - `onEntry` - On entering the referred mode. Tags: atp.EnumerationLiteralIndex=0
    - `onExit` - On exiting the referred mode. Tags: atp.EnumerationLiteralIndex=1
    - `onTransition` - On transition of the 1st referred mode to the 2nd referred mode. Tags: atp.EnumerationLiteralIndex=2
  - Note: Kind of mode switch condition used for activation of an event, as further described for each enumeration field
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
  - Values:
    - `fixed-size` - Fixed size array
    - `variable-size` - Variable size array

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
  - Attributes:
    - `implementationDataType: AbstractImplementationDataType [0..1]` (ref) - This is the corresponding AbstractImplementationDataType. It shall be modeled along the idea of an "unsigned integer-like" data type
    - `modeGroup: ModeDeclarationGroup [0..1]` (ref) - This is the corresponding ModeDeclarationGroup
- `DataTypeMappingSet` - (M2::AUTOSARTemplates::SWComponentTemplate::Datatype::Datatypes)
- `IncludedDataTypeSet` - (M2::AUTOSARTemplates::SWComponentTemplate::Datatype::Datatypes)
- `IncludedModeDeclarationGroupSet` - (M2::AUTOSARTemplates::SWComponentTemplate::Datatype::Datatypes)
- `ApplicationError` - (M2::AUTOSARTemplates::SWComponentTemplate::PortInterface)

### Implementation Properties
- `ImplementationProps` - (M2::AUTOSARTemplates::CommonStructure::Implementation)
  - Attributes:
    - `symbol: CIdentifier [0..1]` (attr) - The symbol to be used as (depending on the concrete case) either a complete replacement or a prefix
  - Subclasses: BswSchedulerNamePrefix, ExecutableEntityActivationReason, SectionNamePrefix, SymbolProps, SymbolicNameProps
- `SymbolProps` - (M2::AUTOSARTemplates::CommonStructure::Implementation)
- `SymbolicNameProps` - (M2::AUTOSARTemplates::CommonStructure::Implementation)
- `SectionNamePrefix` - (M2::AUTOSARTemplates::CommonStructure::ResourceConsumption::MemorySectionUsage)
- `AccessCountSet` - (M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::AccessCount)
  - Attributes:
    - `accessCount: AccessCount [*]` (aggr) - Count value for a AbstractAccessPoint
    - `countProfile: NameToken [0..1]` (attr) - This attribute defines the name of the count profile used to determine the AccessCount.value numbers
- `AccessCount` - (M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::AccessCount)
  - Attributes:
    - `accessPoint: AbstractAccessPoint [0..1]` (ref) - AbstractAccessPoint for which the count value is applicable
    - `value: PositiveInteger [0..1]` (attr) - This attribute represents the number of determined accesses
- `AbstractAccessPoint` - (M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::AccessCount)
  - Attributes:
    - `returnValueProvision: RteApiReturnValueProvisionEnum [0..1]` (attr) - This attribute controls the provision of return values for RTE APIs that correspond to the enclosing access point
- `ExecutableEntityActivationReason` - (M2::AUTOSARTemplates::CommonStructure::InternalBehavior)
  - Attributes:
    - `bitPosition: PositiveInteger [0..1]` (attr) - Bit position for activation reason representation
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