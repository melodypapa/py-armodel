# AUTOSAR Package and Class Reference

This document contains all class and package references extracted from AUTOSAR specification.

* AUTOSARTemplates
  * AutosarTopLevelStructure
      * AUTOSAR
  * BswModuleTemplate
    * BswBehavior
        * BswInternalBehavior
        * ExecutableEntity (abstract)
        * BswModuleEntity (abstract)
        * BswSchedulableEntity
        * BswInterruptEntity
        * BswModuleCallPoint (abstract)
        * BswDirectCallPoint
        * BswSynchronousServerCallPoint
        * BswAsynchronousServerCallPoint
        * BswAsynchronousServerCallResultPoint
        * BswVariableAccess
        * ExclusiveArea
        * BswExclusiveAreaPolicy
        * ImplementationProps (abstract)
        * BswScheduleEvent (abstract)
        * BswInterruptEvent
        * BswTimingEvent
        * BswBackgroundEvent
        * BswOsTaskExecutionEvent
        * BswInternalTriggeringPoint
        * BswInternalTriggerOccurredEvent
        * BswExternalTriggerOccurredEvent
        * BswModeSwitchEvent
        * BswModeSwitchedAckEvent
        * BswModeManagerErrorEvent
        * BswAsynchronousServerCallReturnsEvent
        * BswDataReceivedEvent
        * BswTriggerDirectImplementation
        * BswModeSenderPolicy
        * BswModeSwitchAckRequest
        * BswModeReceiverPolicy
        * BswDataReceptionPolicy (abstract)
        * BswQueuedDataReceptionPolicy
        * ParameterDataPrototype
        * BswImplementation
        * RoleBasedBswModuleEntryAssignment
        * RoleBasedDataAssignment
    * BswImplementation
        * Implementation (abstract)
    * BswInterfaces
        * BswModuleEntry
        * BswModuleDependency
        * BswEntryRelationshipSet
        * BswEntryRelationship
        * BswModuleClientServerEntry
        * AccessCountSet
    * BswOverview
        * BswModuleDescription
        * BswModuleEntry
  * CommonStructure
    * Constants
        * ApplicationRuleBasedValueSpecification
        * ArgumentDataPrototype
        * ArrayValueSpecification
        * AsynchronousServerCallResultPoint
        * DataPrototype (abstract)
        * NumericalOrText
        * NumericalValueSpecification
        * ObdInfoServiceNeeds
        * Referrable (abstract)
        * RuleBasedValueCont
        * RuleBasedValueSpecification
        * RunnableEntity
    * FlatMap
        * AliasNameAssignment
        * McDataInstance
        * FlatInstanceDescriptor
        * FlatMap
        * FunctionInhibitionAvailabilityNeeds
    * Implementation
        * BswEvent (abstract)
        * Implementation (abstract)
        * Code
        * DependencyOnArtifact
        * AutosarEngineeringObject
        * Linker
        * BuildActionManifest
    * ImplementationDataTypes
        * ImplementationDataType
        * ImplementationDataTypeElement
        * InternalTriggeringPoint
    * InternalBehavior
        * InternalBehavior (abstract)
        * BswInternalBehavior
        * BswModuleEntity (abstract)
        * BswCalledEntity
        * BswExclusiveAreaPolicy
        * ExclusiveAreaNestingOrder
        * BswSchedulerNamePrefix
        * ExternalTriggeringPoint
    * McGroups
        * McGroup
        * McDataAccessDetails
    * MeasurementCalibrationSupport
      * RptSupport
          * McGroup
          * RptSwPrototypingAccess
          * RptComponent
          * RptExecutableEntity
          * RptExecutableEntityEvent
          * RptImplPolicy
          * RptExecutableEntityProperties
          * RptServicePoint
          * ServiceDependency (abstract)
        * AliasNameSet
        * McDataInstance
        * McSwEmulationMethodSupport
        * McParameterElementGroup
        * ImplementationElementInParameterInstanceRef
        * McFunction
        * RptSupportData
        * RoleBasedPortAssignment
    * ModeDeclaration
        * ModeDeclarationGroup
        * ModeDeclaration
        * ModeTransition
        * ModeErrorBehavior
        * ModeRequestTypeMap
        * Trigger
        * BswOperationInvokedEvent
    * ResourceConsumption
      * ExecutionTime
          * ExecutionTime (abstract)
          * HardwareConfiguration
          * SoftwareContext
          * MultidimensionalTime
          * SimulatedExecutionTime
          * RoughEstimateOfExecutionTime
          * McSupportData
      * HeapUsage
          * WorstCaseHeapUsage
          * MeasuredHeapUsage
          * RoughEstimateHeapUsage
          * ExecutionTime (abstract)
      * MemorySectionUsage
          * MemorySection
          * StackUsage (abstract)
      * StackUsage
          * WorstCaseStackUsage
          * MeasuredStackUsage
          * RoughEstimateStackUsage
          * HeapUsage (abstract)
        * ResourceConsumption
        * MemorySection
        * MemorySectionLocation
        * AnalyzedExecutionTime
    * ServiceNeeds
        * BswServiceDependency
        * RoleBasedDataAssignment
        * RoleBasedDataTypeAssignment
        * ServiceNeeds (abstract)
        * NvBlockNeeds
        * SupervisedEntityNeeds
        * ComMgrUserNeeds
        * EcuStateMgrUserNeeds
        * CryptoServiceNeeds
        * DltUserNeeds
        * SyncTimeBaseMgrUserNeeds
        * DiagnosticCapabilityElement (abstract)
        * FunctionInhibitionNeeds
        * DoIpServiceNeeds (abstract)
        * DiagnosticValueNeeds
        * DiagnosticRoutineNeeds
        * DiagnosticIoControlNeeds
        * DiagnosticsCommunicationSecurityNeeds
        * DiagnosticCommunicationManagerNeeds
        * DiagnosticUploadDownloadNeeds
        * SupervisedEntityCheckpointNeeds
        * DiagnosticEventNeeds
        * DiagEventDebounceAlgorithm (abstract)
        * DiagEventDebounceCounterBased
        * DiagEventDebounceTimeBased
        * DiagEventDebounceMonitorInternal
        * ErrorTracerNeeds
        * TracedFailure (abstract)
        * DevelopmentError
        * RuntimeError
        * HardwareTestNeeds
        * ARElement (abstract)
        * DiagnosticEventInfoNeeds
        * EcuAbstractionSwComponentType (abstract)
        * GlobalSupervisionNeeds
        * Identifiable (abstract)
        * ObdPidServiceNeeds
        * OperationInvokedEvent
    * SignalServiceTranslation
    * StandardizationTemplate
      * AbstractBlueprintStructure
          * AutosarDataPrototype (abstract)
    * SwcBswMapping
        * SwcBswRunnableMapping
        * SwcBswSynchronizedModeGroupPrototype
        * SwcBswSynchronizedTrigger
        * BswDistinguishedPartition
    * TriggerDeclaration
        * Trigger
        * BswModuleDependency
  * ECUCDescriptionTemplate
      * EcucModuleConfigurationValues
      * EcucModuleDef
  * ECUCParameterDefTemplate
      * EcucModuleDef
      * ExecutableEntityActivationReason
  * GenericStructure
    * BuildActionManifest
        * BuildActionManifest
        * ResourceConsumption
    * GeneralTemplateClasses
      * ARPackage
          * ARPackage
          * AUTOSAR
      * EngineeringObject
          * EngineeringObject (abstract)
          * Compiler
      * Identifiable
          * DiagnosticComponentNeeds
          * Identifiable (abstract)
          * ImplementationDataType
          * RoleBasedMcDataAssignment
      * MultidimensionalTime
          * MultidimensionalTime
          * MeasuredExecutionTime
      * PrimitiveTypes
          * ModeDeclarationGroupPrototype
          * SwAddrMethod
          * SwBaseType
    * VariantHandling
        * ApplicationDataType (abstract)
        * ClientServerInterface
  * SWComponentTemplate
    * Components
        * AtomicSwComponentType (abstract)
        * AtpBlueprint (abstract)
        * CompuMethod
        * EcucModuleConfigurationValues
        * ParameterAccess
        * RTEEvent (abstract)
        * SignalServiceTranslationProps
    * Datatype
      * DataPrototypes
          * VariableDataPrototype
          * SwcBswMapping
          * AutosarDataType (abstract)
          * DataTypeMappingSet
      * Datatypes
          * ApplicationRuleBasedValueSpecification
          * AutosarParameterRef
          * Describable (abstract)
    * NvBlockComponent
    * PortInterface
        * ArrayValueSpecification
        * ClientServerInterface
        * ClientServerOperation
        * ComplexDeviceDriverSwComponentType
        * ServerCallPoint (abstract)
    * RPTScenario
        * RptExecutionContext
        * RecordValueSpecification
    * SoftwareComponentDocumentation
        * SwComponentDocumentation
    * SwcImplementation
        * SwcImplementation
        * SwcInternalBehavior
    * SwcInternalBehavior
      * AccessCount
          * AccessCount
          * AbstractAccessPoint (abstract)
          * InternalBehavior (abstract)
      * DataElements
          * AutosarParameterRef
          * AutosarVariableRef
          * ParameterAccess
          * PortDefinedArgumentValue
      * ModeDeclarationGroup
          * ModeSwitchPoint
          * NumericalOrText
      * PortAPIOptions
          * PortPrototype (abstract)
      * RTEEvents
          * PRPortPrototype
          * RapidPrototypingScenario
      * ServerCall
          * AtomicSwComponentType (abstract)
          * ServiceSwComponentType
      * ServiceMapping
          * ServiceNeeds (abstract)
      * Trigger
          * ExternalTriggeringPoint
          * FlatInstanceDescriptor
          * ModeAccessPoint
        * RunnableEntity
        * SenderReceiverInterface
        * SwcInternalBehavior
        * System
  * SystemTemplate
      * System
* MSR
  * AsamHdo
    * BaseTypes
    * ComputationMethod
        * ConstantSpecification
  * DataDictionary
    * AuxillaryObjects
        * SwAddrMethod
        * SectionNamePrefix
    * DataDefProperties
        * SwComponentDocumentation
        * SwSystemconst
        * SwTextProps
        * SwcImplementation
        * VariableAccess
    * ServiceProcessTask
        * SwServiceArg
        * SwPointerTargetProps
    * SystemConstant
        * SwTextProps
