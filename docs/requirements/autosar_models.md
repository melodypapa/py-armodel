* M2
  * AUTOSARTemplates
    * BswModuleTemplate
      * BswOverview
        * BswModuleDescription
        * InstanceRefs
          * ModeInBswModuleDescriptionInstanceRef
      * BswInterfaces
        * BswModuleEntry
        * BswEntryKindEnum
        * BswExecutionContext
        * BswCallType
        * BswModuleDependency
        * BswEntryRelationshipSet
        * BswEntryRelationship
        * BswEntryRelationshipEnum
        * BswModuleClientServerEntry
      * BswBehavior
        * BswInternalBehavior
        * BswModuleEntity (abstract)
        * BswCalledEntity
        * BswSchedulableEntity
        * BswInterruptEntity
        * BswInterruptCategory
        * BswModuleCallPoint (abstract)
        * BswDirectCallPoint
        * BswSynchronousServerCallPoint
        * BswAsynchronousServerCallPoint
        * BswAsynchronousServerCallResultPoint
        * BswVariableAccess
        * BswExclusiveAreaPolicy
        * BswSchedulerNamePrefix
        * BswEvent (abstract)
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
        * BswOperationInvokedEvent
        * BswAsynchronousServerCallReturnsEvent
        * BswDataReceivedEvent
        * BswTriggerDirectImplementation
        * BswModeSenderPolicy
        * BswModeSwitchAckRequest
        * BswModeReceiverPolicy
        * BswDataReceptionPolicy (abstract)
        * BswQueuedDataReceptionPolicy
        * BswDistinguishedPartition
        * BswServiceDependency
        * RoleBasedBswModuleEntryAssignment
      * BswImplementation
        * BswImplementation
    * GenericStructure
      * GeneralTemplateClasses
        * PrimitiveTypes
          * ArgumentDirectionEnum
          * ByteOrderEnum
          * IntervalTypeEnum
          * MonotonyEnum
        * EngineeringObject
          * AutosarEngineeringObject
          * EngineeringObject (abstract)
        * MultidimensionalTime
          * MultidimensionalTime
        * ARPackage
          * ARElement (abstract)
          * ARPackage
          * PackageableElement (abstract)
          * ReferenceBase
        * Identifiable
          * Describable (abstract)
          * Identifiable (abstract)
          * Referrable (abstract)
          * MultilanguageReferrable (abstract)
          * SingleLanguageReferrable (abstract)
          * ShortNameFragment
        * AnyInstanceRef
          * AnyInstanceRef
        * GeneralAnnotation
          * GeneralAnnotation (abstract)
        * TagWithOptionalValue
          * TagWithOptionalValue
        * ElementCollection
          * Collection
          * AutoCollectEnum
          * CollectableElement (abstract)
        * SpecialDataDef
          * SdgDef
          * SdgElementWithGid (abstract)
          * SdgClass
          * SdgAttribute (abstract)
          * SdgAbstractPrimitiveAttribute (abstract)
          * SdgPrimitiveAttribute
          * SdgPrimitiveAttributeWithVariation
          * SdgAggregationWithVariation
          * SdgReference
          * SdgAbstractForeignReference (abstract)
          * SdgForeignReference
          * SdgForeignReferenceWithVariation
        * ModelRestrictionTypes
          * AbstractValueRestriction (abstract)
          * AbstractVariationRestriction (abstract)
          * FullBindingTimeEnum
          * AbstractMultiplicityRestriction (abstract)
        * ArObject
          * ARObject (abstract)
      * BuildActionManifest
        * BuildActionManifest
        * BuildAction
        * BuildActionIoElement
        * BuildActionEnvironment
        * BuildActionEntity (abstract)
        * BuildActionInvocator
        * BuildEngineeringObject
        * GenericModelReference
      * VariantHandling
        * AdditionalBindingTimeEnum
        * BindingTimeEnum
        * PostBuildVariantCriterion
        * PostBuildVariantCriterionValue
        * PredefinedVariant
        * SwSystemconstantValueSet
        * VariationPoint
        * ConditionByFormula (interface)
        * PostBuildVariantCondition
        * PostBuildVariantCriterionValueSet
        * SwSystemconstDependentFormula (interface)
        * SwSystemconstValue
        * EvaluatedVariantSet
        * AttributeValueVariationPoints
          * NumericalValueVariationPoint (interface)
          * AttributeValueVariationPoint (interface)
          * AbstractNumericalVariationPoint (interface)
          * BooleanValueVariationPoint (interface)
          * FloatValueVariationPoint (interface)
          * IntegerValueVariationPoint (interface)
          * LimitValueVariationPoint (interface)
          * PositiveIntegerValueVariationPoint (interface)
          * UnlimitedIntegerValueVariationPoint (interface)
          * TimeValueValueVariationPoint (interface)
          * AbstractEnumerationValueVariationPoint (interface)
          * EnumerationMappingEntry
          * EnumerationMappingTable
      * DocumentationOnM1
        * StandardNameEnum
        * Documentation
        * DocumentationContext
      * AbstractStructure
        * AtpInstanceRef (abstract)
        * AtpClassifier (abstract)
        * AtpFeature (abstract)
        * AtpPrototype (abstract)
        * AtpStructureElement (abstract)
        * AtpType (abstract)
      * ViewMapSet
        * ViewMap
        * ViewMapSet
      * FormulaLanguage
        * FormulaExpression (interface)
      * RolesAndRights
        * AclPermission
        * AclObjectSet
        * AtpDefinition (abstract)
        * AclOperation
        * AclRole
        * AclScopeEnum
      * LifeCycles
        * LifeCycleStateDefinitionGroup
        * LifeCycleState
        * LifeCycleInfoSet
        * LifeCyclePeriod
        * LifeCycleInfo
      * ImpositionTimes
        * ImpositionTime
    * CommonStructure
      * ModeDeclaration
        * ModeDeclarationGroupPrototype
        * ModeDeclarationGroup
        * ModeDeclaration
        * ModeTransition
        * ModeErrorBehavior
        * ModeErrorReactionPolicyEnum
        * ModeRequestTypeMap
        * ModeActivationKind
        * ModeDeclarationGroupPrototypeMapping
      * TriggerDeclaration
        * Trigger
        * TriggerMapping
      * InternalBehavior
        * InternalBehavior (abstract)
        * ExecutableEntity (abstract)
        * ReentrancyLevelEnum
        * ExclusiveArea
        * ApiPrincipleEnum
        * ExclusiveAreaNestingOrder
        * ExecutableEntityActivationReason
        * AbstractEvent (abstract)
      * Implementation
        * ImplementationProps (abstract)
        * Implementation (abstract)
        * Code
        * DependencyOnArtifact
        * DependencyUsageEnum
        * Compiler
        * Linker
        * ProgramminglanguageEnum
      * SwcBswMapping
        * SwcBswMapping
        * SwcBswRunnableMapping
        * SwcBswSynchronizedModeGroupPrototype
        * SwcBswSynchronizedTrigger
      * ResourceConsumption
        * ResourceConsumption
        * HardwareConfiguration
        * SoftwareContext
        * MemorySectionUsage
          * MemorySection
          * SectionNamePrefix
        * StackUsage
          * StackUsage (abstract)
          * WorstCaseStackUsage
          * MeasuredStackUsage
          * RoughEstimateStackUsage
        * HeapUsage
          * HeapUsage (abstract)
          * WorstCaseHeapUsage
          * MeasuredHeapUsage
          * RoughEstimateHeapUsage
        * ExecutionTime
          * ExecutionTime (abstract)
          * MemorySectionLocation
          * AnalyzedExecutionTime
          * MeasuredExecutionTime
          * SimulatedExecutionTime
          * RoughEstimateOfExecutionTime
      * MeasurementCalibrationSupport
        * McSupportData
        * McDataInstance
        * McSwEmulationMethodSupport
        * McParameterElementGroup
        * ImplementationElementInParameterInstanceRef
        * McFunction
        * McDataAccessDetails
        * RoleBasedMcDataAssignment
        * RptSupport
          * McFunctionDataRefSet (interface)
          * RptSupportData
          * RptSwPrototypingAccess
          * RptComponent
          * RptExecutableEntity
          * RptExecutableEntityEvent
          * RptEnablerImplTypeEnum
          * RptPreparationEnum
          * RptExecutionControlEnum
          * RptExecutionContext
          * RptAccessEnum
          * RptServicePoint
      * FlatMap
        * AliasNameSet
        * AliasNameAssignment
        * FlatInstanceDescriptor
        * FlatMap
        * RtePluginProps
      * McGroups
        * McGroup
        * McGroupDataRefSet (interface)
      * ServiceNeeds
        * ServiceDependency (abstract)
        * RoleBasedDataAssignment
        * ServiceNeeds (abstract)
        * NvBlockNeeds
        * NvBlockNeedsReliabilityEnum
        * NvBlockNeedsWritingPriorityEnum
        * MaxCommModeEnum
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
        * DiagnosticValueAccessEnum
        * DiagnosticProcessingStyleEnum
        * DiagnosticRoutineNeeds
        * DiagnosticRoutineTypeEnum
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
        * DiagnosticComponentNeeds
        * DiagnosticEventInfoNeeds
        * FunctionInhibitionAvailabilityNeeds
        * GlobalSupervisionNeeds
        * ObdInfoServiceNeeds
        * ObdPidServiceNeeds
        * ObdControlServiceNeeds
        * ObdMonitorServiceNeeds
        * ServiceProviderEnum
        * VendorSpecificServiceNeeds
        * ServiceDiagnosticRelevanceEnum
        * SymbolicNameProps
        * BswMgrNeeds
        * CryptoServiceJobNeeds
        * CryptoKeyManagementNeeds
        * DiagnosticEventManagerNeeds
        * DiagnosticAudienceEnum
        * DiagnosticOperationCycleNeeds
        * OperationCycleTypeEnum
        * DiagnosticEnableConditionNeeds
        * EventAcceptanceStatusEnum
        * DiagnosticStorageConditionNeeds
        * StorageConditionStatusEnum
        * IndicatorStatusNeeds
        * DtcStatusChangeNotificationNeeds
        * DiagnosticClearDtcNotificationEnum
        * DiagnosticServiceRequestCallbackTypeEnum
        * DiagnosticRequestFileTransferNeeds
        * ObdRatioServiceNeeds
        * ObdRatioConnectionKindEnum
        * DiagnosticMonitorUpdateKindEnum
        * ObdRatioDenominatorNeeds
        * DiagnosticDenominatorConditionEnum
        * DoIpGidNeeds
        * DoIpGidSynchronizationNeeds
        * DoIpPowerModeStatusNeeds
        * DoIpRoutingActivationAuthenticationNeeds
        * DoIpRoutingActivationConfirmationNeeds
        * DoIpActivationLineNeeds
        * WarningIndicatorRequestedBitNeeds
        * FurtherActionByteNeeds
        * DiagnosticControlNeeds
        * SecureOnBoardCommunicationNeeds
        * VerificationStatusIndicationModeEnum
        * J1939RmOutgoingRequestServiceNeeds
        * J1939RmIncomingRequestServiceNeeds
        * J1939DcmDm19Support
        * V2xFacUserNeeds
        * V2xMUserNeeds
        * V2xDataManagerNeeds
        * IdsMgrNeeds
        * IdsMgrCustomTimestampNeeds
        * TransientFault
      * Constants
        * ApplicationRuleBasedValueSpecification
        * ArrayValueSpecification
        * ConstantSpecification
        * NumericalOrText
        * NumericalValueSpecification
        * RecordValueSpecification
        * RuleArguments (interface)
        * RuleBasedValueCont
        * RuleBasedValueSpecification
        * ApplicationValueSpecification
        * ValueSpecification (abstract)
        * CompositeValueSpecification (abstract)
        * TextValueSpecification
        * ReferenceValueSpecification
        * NotAvailableValueSpecification
        * ConstantReference
        * ConstantSpecificationMapping
        * ConstantSpecificationMappingSet
        * AbstractRuleBasedValueSpecification (abstract)
        * RuleBasedAxisCont
        * NumericalRuleBasedValueSpecification
        * CompositeRuleBasedValueSpecification
        * CompositeRuleBasedValueArgument (abstract)
      * StandardizationTemplate
        * AbstractBlueprintStructure
          * AtpBlueprint (abstract)
          * AtpBlueprintable (abstract)
          * AtpBlueprintMapping (abstract)
          * BlueprintPolicy (abstract)
          * BlueprintPolicyList
          * BlueprintPolicyNotModifiable
          * BlueprintPolicySingle
        * BlueprintDedicated
          * Port
            * PortPrototypeBlueprint
            * PortPrototypeBlueprintInitValue
          * Generic
            * BlueprintMapping
        * BlueprintMapping
          * BlueprintMappingSet
        * BlueprintGenerator
          * BlueprintGenerator
        * Keyword
          * Keyword
          * KeywordSet
        * ClientServerInterfaceToBsw
          * ClientServerOperationBlueprintMapping
          * ClientServerInterfaceToBswModuleEntryBlueprintMapping
        * DataExchangePoint
          * DataExchangePoint
          * Baseline
          * DataExchangePointKind
          * SeverityEnum
          * Common
            * SpecElementReference (abstract)
            * SpecElementScope (abstract)
            * RestrictionWithSeverity (abstract)
            * DataFormatElementReference (abstract)
          * Data
            * ValueRestrictionWithSeverity
            * MultiplicityRestrictionWithSeverity
            * VariationRestrictionWithSeverity
            * DataFormatElementScope (abstract)
            * AbstractClassTailoring (abstract)
            * AbstractCondition (abstract)
            * AggregationCondition
            * AttributeCondition (abstract)
            * ClassTailoring (abstract)
            * ClassContentConditional
            * ConcreteClassTailoring
            * InvertCondition
            * PrimitiveAttributeCondition
            * ReferenceCondition
            * TextualCondition
            * AttributeTailoring (abstract)
            * PrimitiveAttributeTailoring
            * DefaultValueApplicationStrategyEnum
            * AggregationTailoring
            * ReferenceTailoring
            * ConstraintTailoring
            * SdgTailoring
            * DataFormatTailoring
            * UnresolvedReferenceRestrictionWithSeverity
        * DataExchange
          * SpecificationScope
          * SpecificationDocumentScope
          * DocumentElementScope
        * BlueprintFormula
          * BlueprintFormula (interface)
        * Blueprint
          * ConsistencyNeedsBlueprintSet
      * ImplementationDataTypes
        * ImplementationDataType
        * ImplementationDataTypeElement
        * ArraySizeSemanticsEnum
        * AbstractImplementationDataType (abstract)
        * AbstractImplementationDataTypeElement (abstract)
        * ArrayImplPolicyEnum
      * SignalServiceTranslation
        * SignalServiceTranslationProps
        * SignalServiceTranslationPropsSet
        * SignalServiceTranslationEventProps
        * SignalServiceTranslationElementProps
        * SignalServiceTranslationControlEnum
      * Filter
        * DataFilter
        * DataFilterTypeEnum
      * Timing
        * TimingExtensions
          * VfbTiming
          * SwcTiming
          * SystemTiming
          * BswModuleTiming
          * BswCompositionTiming
          * EcuTiming
          * TimingExtension (abstract)
        * TimingCondition
          * TimingCondition
          * TimingConditionFormula (interface)
          * TimingExtensionResource
          * TimingModeInstance
          * ModeInBswInstanceRef
          * ModeInSwcInstanceRef
        * TimingDescription
          * TimingDescriptionEventChain
          * TimingDescription (abstract)
          * TimingDescriptionEvent (abstract)
          * TimingDescription
            * TDEventVfb (abstract)
            * TDEventVfbReference
            * TDEventVfbPort (abstract)
            * TDEventVariableDataPrototype
            * TDEventVariableDataPrototypeTypeEnum
            * TDEventOperation
            * TDEventOperationTypeEnum
            * TDEventModeDeclaration
            * TDEventModeDeclarationTypeEnum
            * TDEventTrigger
            * TDEventTriggerTypeEnum
            * TDEventSwc (abstract)
            * TDEventSwcInternalBehavior
            * TDEventSwcInternalBehaviorTypeEnum
            * TDEventSwcInternalBehaviorReference
            * TDEventCom (abstract)
            * TDEventISignal
            * TDEventISignalTypeEnum
            * TDEventIPdu
            * TDEventIPduTypeEnum
            * TDEventFrame
            * TDEventFrameTypeEnum
            * TDEventFrameEthernet
            * TDEventFrameEthernetTypeEnum
            * TDHeaderIdRange
            * TDEventCycleStart (abstract)
            * TDEventFrClusterCycleStart
            * TDEventTTCanCycleStart
            * TDEventBswInternalBehavior
            * TDEventBswInternalBehaviorTypeEnum
            * TDEventBswModule
            * TDEventBswModuleTypeEnum
            * TDEventBswModeDeclaration
            * TDEventBswModeDeclarationTypeEnum
            * TDEventComplex
            * TDEventSLLETPort
            * TDEventOccurrenceExpression
            * TDEventOccurrenceExpressionFormula (interface)
            * AutosarVariableInstance
            * AutosarOperationArgumentInstance
            * TDEventBsw (abstract)
            * TDEventSLLET (abstract)
        * TimingConstraint
          * TimingConstraint (abstract)
          * SynchronizationTiming
            * SynchronizationTimingConstraint
            * SynchronizationTypeEnum
            * EventOccurrenceKindEnum
          * LatencyTimingConstraint
            * LatencyTimingConstraint
            * LatencyConstraintTypeEnum
          * EventTriggeringConstraint
            * EventTriggeringConstraint (abstract)
            * PeriodicEventTriggering
            * SporadicEventTriggering
            * ConcretePatternEventTriggering
            * BurstPatternEventTriggering
            * ArbitraryEventTriggering
            * ConfidenceInterval
          * OffsetConstraint
            * OffsetTimingConstraint
          * AgeConstraint
            * AgeConstraint
          * ExecutionOrderConstraint
            * ExecutionOrderConstraint
            * ExecutionOrderConstraintTypeEnum
            * EOCExecutableEntityRefAbstract (abstract)
            * EOCExecutableEntityRefGroup
            * EOCExecutableEntityRef
            * EOCEventRef
            * LetDataExchangeParadigmEnum
          * ExecutionTimeConstraint
            * ExecutionTimeConstraint
            * ExecutionTimeTypeEnum
          * SynchronizationPointConstraint
            * SynchronizationPointConstraint
        * TimingCpSoftwareCluster
          * TDCpSoftwareClusterMappingSet
          * TDCpSoftwareClusterMapping
          * TDCpSoftwareClusterResourceMapping
        * TimingClock
          * TDLETZoneClock
          * TimingClock (abstract)
          * TimingClockSyncAccuracy
    * SWComponentTemplate
      * SwcInternalBehavior
        * RunnableEntity
        * SwcInternalBehavior
        * SwcExclusiveAreaPolicy
        * AccessCount
          * AccessCountSet
          * AccessCount
          * AbstractAccessPoint (abstract)
          * RteApiReturnValueProvisionEnum
        * ServiceMapping
          * RoleBasedDataTypeAssignment
          * RoleBasedPortAssignment
          * SwcServiceDependency
        * ServerCall
          * AsynchronousServerCallResultPoint
          * ServerCallPoint (abstract)
          * SynchronousServerCallPoint
          * AsynchronousServerCallPoint
        * DataElements
          * AutosarParameterRef
          * AutosarVariableRef
          * ParameterAccess
          * VariableAccess
          * ArVariableInImplementationDataInstanceRef
          * ArParameterInImplementationDataInstanceRef
          * VariableAccessScopeEnum
          * InstanceRefs
            * ParameterInAtomicSWCTypeInstanceRef
            * VariableInAtomicSWCTypeInstanceRef
        * Trigger
          * ExternalTriggeringPoint
          * InternalTriggeringPoint
        * ModeDeclarationGroup
          * ModeAccessPoint
          * ModeSwitchPoint
          * IncludedModeDeclarationGroupSet
        * RTEEvents
          * OperationInvokedEvent
          * RTEEvent (abstract)
          * TimingEvent
          * AsynchronousServerCallReturnsEvent
          * DataSendCompletedEvent
          * DataWriteCompletedEvent
          * DataReceivedEvent
          * DataReceiveErrorEvent
          * BackgroundEvent
          * SwcModeSwitchEvent
          * ModeSwitchedAckEvent
          * ExternalTriggerOccurredEvent
          * InternalTriggerOccurredEvent
          * InitEvent
          * TransformerHardErrorEvent
          * OsTaskExecutionEvent
          * WaitPoint
          * SwcModeManagerErrorEvent
        * PortAPIOptions
          * PortDefinedArgumentValue
          * PortAPIOption
          * DataTransformationErrorHandlingEnum
          * DataTransformationStatusForwardingEnum
          * SwcSupportedFeature (abstract)
          * CommunicationBufferLocking
          * SupportBufferLockingEnum
        * RunnableEntity
          * RunnableEntityArgument
        * InstantiationDataDefProps
          * InstantiationDataDefProps
        * PerInstanceMemory
          * PerInstanceMemory
        * IncludedDataTypes
          * IncludedDataTypeSet
        * VariantHandling
          * VariationPointProxy
      * Datatype
        * DataPrototypes
          * ParameterDataPrototype
          * VariableDataPrototype
          * AutosarDataPrototype (abstract)
          * DataPrototype (abstract)
          * ApplicationArrayElement
          * ApplicationRecordElement
          * ApplicationCompositeElementDataPrototype (abstract)
        * Datatypes
          * ApplicationDataType (abstract)
          * AutosarDataType (abstract)
          * DataTypeMappingSet
          * ApplicationPrimitiveDataType
          * DataTypeMap
          * ApplicationCompositeDataType (abstract)
          * ApplicationArrayDataType
          * ArraySizeHandlingEnum
          * ApplicationRecordDataType
      * RPTScenario
        * RptImplPolicy
        * RptExecutableEntityProperties
        * RptServicePointEnum
        * RapidPrototypingScenario
        * IdentCaption (abstract)
        * RptContainer
        * RptHook
        * ModeAccessPointIdent
        * ExternalTriggeringPointIdent
        * RptProfile
      * NvBlockComponent
        * RamBlockStatusControlEnum
        * NvBlockDescriptor
        * ModeSwitchEventTriggeredActivity
        * NvBlockDataMapping
        * BulkNvDataDescriptor
      * PortInterface
        * ArgumentDataPrototype
        * ClientServerInterface
        * ClientServerOperation
        * SenderReceiverInterface
        * DataInterface (abstract)
        * NvDataInterface
        * PortInterface (abstract)
        * ParameterInterface
        * InvalidationPolicy
        * MetaDataItem
        * MetaDataItemSet
        * ServerArgumentImplPolicyEnum
        * ApplicationError
        * TriggerInterface
        * ModeSwitchInterface
        * PortInterfaceMappingSet
        * PortInterfaceMapping (abstract)
        * VariableAndParameterInterfaceMapping
        * DataPrototypeMapping
        * ClientServerInterfaceMapping
        * ClientServerOperationMapping
        * ClientServerApplicationErrorMapping
        * ModeInterfaceMapping
        * ModeDeclarationMappingSet
        * ModeDeclarationMapping
        * TriggerInterfaceMapping
        * SubElementMapping
        * SubElementRef (abstract)
        * ImplementationDataTypeSubElementRef
        * ApplicationCompositeDataTypeSubElementRef
        * TextTableMapping
        * MappingDirectionEnum
        * TextTableValuePair
        * InstanceRefs
          * ApplicationCompositeElementInPortInterfaceInstanceRef
      * Components
        * AtomicSwComponentType (abstract)
        * ComplexDeviceDriverSwComponentType
        * EcuAbstractionSwComponentType
        * PRPortPrototype
        * PortPrototype (abstract)
        * ServiceSwComponentType
        * ApplicationSwComponentType
        * PPortPrototype
        * SwComponentType (abstract)
        * ParameterSwComponentType
        * AbstractRequiredPortPrototype (abstract)
        * AbstractProvidedPortPrototype (abstract)
        * RPortPrototype
        * PortGroup
        * SymbolProps
        * SensorActuatorSwComponentType
        * ServiceProxySwComponentType
        * NvBlockSwComponentType
        * InstanceRefs
          * VariableInAtomicSwcInstanceRef (abstract)
          * RVariableInAtomicSwcInstanceRef
          * RModeInAtomicSwcInstanceRef
          * InnerPortGroupInCompositionInstanceRef
          * TriggerInAtomicSwcInstanceRef (abstract)
          * RTriggerInAtomicSwcInstanceRef
          * PTriggerInAtomicSwcTypeInstanceRef
          * OperationInAtomicSwcInstanceRef (abstract)
          * ROperationInAtomicSwcInstanceRef
          * POperationInAtomicSwcInstanceRef
          * RModeGroupInAtomicSWCInstanceRef
          * PModeGroupInAtomicSwcInstanceRef
          * ModeGroupInAtomicSwcInstanceRef (abstract)
      * SoftwareComponentDocumentation
        * SwComponentDocumentation
      * SwcImplementation
        * SwcImplementation
        * PerInstanceMemorySize
      * Composition
        * CompositionSwComponentType
        * SwComponentPrototype
        * AssemblySwConnector
        * SwConnector (abstract)
        * DelegationSwConnector
        * PassThroughSwConnector
        * InstantiationTimingEventProps
        * InstantiationRTEEventProps (abstract)
        * InstanceRefs
          * ComponentInCompositionInstanceRef
          * PortInCompositionTypeInstanceRef (abstract)
          * PPortInCompositionInstanceRef
          * RPortInCompositionInstanceRef
          * InstanceEventInCompositionInstanceRef
      * Communication
        * HandleInvalidEnum
        * PPortComSpec (abstract)
        * RPortComSpec (abstract)
        * ReceiverComSpec (abstract)
        * HandleOutOfRangeStatusEnum
        * NonqueuedReceiverComSpec
        * QueuedReceiverComSpec
        * ReceptionComSpecProps
        * HandleTimeoutEnum
        * SenderComSpec (abstract)
        * QueuedSenderComSpec
        * NonqueuedSenderComSpec
        * TransmissionComSpecProps
        * TransmissionAcknowledgementRequest
        * HandleOutOfRangeEnum
        * TransmissionModeDefinitionEnum
        * CompositeNetworkRepresentation
        * ClientComSpec
        * ServerComSpec
        * ModeSwitchSenderComSpec
        * ModeSwitchedAckRequest
        * ModeSwitchReceiverComSpec
        * ParameterProvideComSpec
        * ParameterRequireComSpec
        * NvRequireComSpec
        * NvProvideComSpec
        * TransformationComSpecProps (abstract)
        * UserDefinedTransformationComSpecProps
      * ApplicationAttributes
        * SenderReceiverAnnotation (abstract)
        * SenderAnnotation
        * ReceiverAnnotation
        * ProcessingKindEnum
        * DataLimitKindEnum
        * ClientServerAnnotation
        * IoHwAbstractionServerAnnotation
        * FilterDebouncingEnum
        * PulseTestEnum
        * ParameterPortAnnotation
        * ModePortAnnotation
        * TriggerPortAnnotation
        * NvDataPortAnnotation
        * DelegatedPortAnnotation
        * SignalFanEnum
      * EndToEndProtection
        * EndToEndDescription
        * EndToEndProtectionSet
        * EndToEndProtection
        * EndToEndProtectionVariablePrototype
      * ImplicitCommunicationBehavior
        * ConsistencyNeeds
        * RunnableEntityGroup
        * DataPrototypeGroup
        * InstanceRef
          * InnerDataPrototypeGroupInCompositionInstanceRef
          * InnerRunnableEntityGroupInCompositionInstanceRef
          * RunnableEntityInCompositionInstanceRef
          * VariableDataPrototypeInCompositionInstanceRef
      * MeasurementAndCalibration
        * InterpolationRoutine
          * InterpolationRoutineMappingSet
          * InterpolationRoutineMapping
          * InterpolationRoutine
        * CalibrationParameter
          * CalibrationParameterValueSet
          * CalibrationParameterValue
    * AutosarTopLevelStructure
      * AUTOSAR
      * FileInfoComment
    * ECUCDescriptionTemplate
      * EcucModuleConfigurationValues
      * EcucValueCollection
      * EcucIndexableValue (abstract)
      * EcucContainerValue
      * EcucParameterValue (abstract)
      * EcucTextualParamValue
      * EcucNumericalParamValue
      * EcucAddInfoParamValue
      * EcucAbstractReferenceValue (abstract)
      * EcucReferenceValue
      * EcucInstanceReferenceValue
    * ECUCParameterDefTemplate
      * EcucModuleDef
      * EcucDefinitionCollection
      * EcucContainerDef (abstract)
      * EcucParamConfContainerDef
      * EcucChoiceContainerDef
      * EcucDefinitionElement (abstract)
      * EcucScopeEnum
      * EcucCommonAttributes (abstract)
      * EcucAbstractConfigurationClass (abstract)
      * EcucValueConfigurationClass
      * EcucMultiplicityConfigurationClass
      * EcucConfigurationClassEnum
      * EcucConfigurationVariantEnum
      * EcucParameterDef (abstract)
      * EcucBooleanParamDef
      * EcucIntegerParamDef
      * EcucFloatParamDef
      * EcucAbstractStringParamDef (interface)
      * EcucStringParamDef (interface)
      * EcucMultilineStringParamDef (interface)
      * EcucLinkerSymbolDef (interface)
      * EcucFunctionNameDef (interface)
      * EcucEnumerationParamDef
      * EcucEnumerationLiteralDef
      * EcucAddInfoParamDef
      * EcucAbstractReferenceDef (abstract)
      * EcucAbstractInternalReferenceDef (abstract)
      * EcucAbstractExternalReferenceDef (abstract)
      * EcucReferenceDef
      * EcucChoiceReferenceDef
      * EcucForeignReferenceDef
      * EcucInstanceReferenceDef
      * EcucUriReferenceDef
      * EcucDestinationUriDefSet
      * EcucDestinationUriDef
      * EcucDestinationUriPolicy
      * EcucDestinationUriNestingContractEnum
      * EcucDerivationSpecification
      * EcucParameterDerivationFormula (interface)
      * EcucQuery
      * EcucQueryExpression (interface)
      * EcucConditionSpecification
      * EcucConditionFormula (interface)
      * EcucValidationCondition
    * SystemTemplate
      * System
      * RootSwCompositionPrototype
      * ClientIdDefinitionSet
      * ClientIdDefinition
      * SystemMapping
      * ComManagementMapping
      * J1939SharedAddressCluster
      * PortElementToCommunicationResourceMapping
      * DiagnosticConnection
        * DiagnosticConnection
        * TpConnectionIdent
        * DoIpTpConnection
        * TpConnection (abstract)
      * Fibex
        * FibexCore
          * FibexElement (abstract)
          * CoreTopology
            * CommunicationCluster (interface)
            * EcuInstance
            * PhysicalChannel (abstract)
            * ClientIdRange
            * CommunicationController (interface)
            * CommunicationConnector (abstract)
            * PncGatewayTypeEnum
            * CommConnectorPort (abstract)
            * CommunicationCycle (abstract)
            * CycleCounter
            * CycleRepetition
            * CycleRepetitionType
          * CoreCommunication
            * ISignal
            * ISignalIPduGroup
            * J1939DcmIPdu
            * SystemSignal
            * Frame (abstract)
            * FrameTriggering (abstract)
            * NPdu
            * NmPdu
            * Pdu (abstract)
            * PduTriggering
            * UserDefinedPdu
            * ISignalGroup
            * ISignalIPdu
            * FramePort
            * IPduPort
            * IPduSignalProcessingEnum
            * ISignalPort
            * ISignalTypeEnum
            * ISignalProps
            * SystemSignalGroup
            * ISignalToIPduMapping
            * TransferPropertyEnum
            * ISignalTriggering
            * IPdu (abstract)
            * DcmIPdu
            * DiagPduType
            * GeneralPurposePdu
            * GeneralPurposeIPdu
            * UserDefinedIPdu
            * PduToFrameMapping (interface)
            * IPduTiming
            * CommunicationDirectionType
            * PdurIPduGroup
            * ContainerIPdu
            * ContainerIPduTriggerEnum
            * ContainerIPduHeaderTypeEnum
            * RxAcceptContainedIPduEnum
            * ContainedIPduProps
            * ContainedIPduCollectionSemanticsEnum
            * SecuredIPdu
            * SecuredPduHeaderEnum
            * SecureCommunicationProps
            * SecureCommunicationPropsSet
            * SecureCommunicationFreshnessProps
            * SecureCommunicationAuthenticationProps
            * TriggerMode
            * MultiplexedIPdu
            * StaticPart
            * DynamicPart
            * DynamicPartAlternative
            * MultiplexedPart (abstract)
            * SegmentPosition
            * Timing
              * TransmissionModeDeclaration
              * TransmissionModeCondition
              * ModeDrivenTransmissionModeCondition
              * TransmissionModeTiming
              * CyclicTiming
              * EventControlledTiming
              * TimeRangeType
              * RelativeTolerance
              * AbsoluteTolerance
              * TriggerIPduSendCondition
        * Fibex4Ethernet
          * EthernetTopology
            * EthernetPhysicalChannel
            * EthernetCluster (interface)
            * MacMulticastGroup
            * VlanConfig
            * CouplingElement
            * CouplingElementEnum
            * CouplingPort
            * EthernetConnectionNegotiationEnum
            * EthernetMacLayerTypeEnum
            * EthernetPhysicalLayerTypeEnum
            * EthernetSwitchVlanIngressTagEnum
            * VlanMembership
            * CouplingPortConnection
            * EthernetCommunicationController (interface)
            * EthernetCommunicationConnector
            * CouplingPortDetails
            * CouplingPortStructuralElement (abstract)
            * CouplingPortScheduler
            * EthernetCouplingPortSchedulerEnum
            * CouplingPortShaper
            * CouplingPortFifo
            * CouplingPortRatePolicy
            * CouplingPortRatePolicyActionEnum
            * EthernetPriorityRegeneration
            * CouplingPortTrafficClassAssignment
            * EthernetSwitchVlanEgressTaggingEnum
            * DhcpServerConfiguration
            * Ipv4DhcpServerConfiguration
            * Ipv6DhcpServerConfiguration
            * CouplingElementAbstractDetails (abstract)
            * CouplingElementSwitchDetails
            * SwitchStreamIdentification
            * SwitchStreamFilterRule
            * StreamFilterRuleDataLinkLayer
            * StreamFilterMACAddress
            * StreamFilterRuleIpTp
            * StreamFilterIpv4Address
            * StreamFilterIpv6Address
            * StreamFilterPortRange
            * StreamFilterIEEE1722Tp
            * SwitchStreamFilterActionDestPortModification
            * SwitchStreamFilterActionPortModificationEnum
            * SwitchStreamFilterEntry
            * SwitchAsynchronousTrafficShaperGroupEntry
            * SwitchStreamGateEntry
            * SwitchFlowMeteringEntry
            * FlowMeteringColorModeEnum
            * EthIpProps
            * Ipv4Props
            * Ipv4ArpProps
            * Ipv4AutoIpProps
            * Ipv4FragmentationProps
            * Ipv6Props
            * Ipv6FragmentationProps
            * Dhcpv6Props
            * Ipv6NdpProps
            * EthTcpIpProps
            * UdpProps
            * TcpProps
            * EthTcpIpIcmpProps
            * TcpIpIcmpv4Props
            * TcpIpIcmpv6Props
            * EthernetWakeupSleepOnDatalineConfig
            * EthernetWakeupSleepOnDatalineConfigSet
            * PlcaProps
            * ApplicationEndpoint
            * TransportProtocolConfiguration (abstract)
            * GenericTp
            * TcpUdpConfig (abstract)
            * UdpTp
            * TcpTp
            * RtpTp
            * Ieee1722Tp
            * HttpTp
            * TpPort
            * NetworkEndpoint
            * NetworkEndpointAddress (abstract)
            * Ipv4Configuration
            * Ipv4AddressSourceEnum
            * IpAddressKeepEnum
            * Ipv6Configuration
            * Ipv6AddressSourceEnum
            * MacMulticastConfiguration
            * InfrastructureServices
            * TimeSynchronization
            * TimeSyncClientConfiguration
            * TimeSyncServerConfiguration
            * OrderedMaster
            * TimeSyncTechnologyEnum
            * DoIpEntity
            * DoIpEntityRoleEnum
            * GlobalTimeCouplingPortProps
            * CouplingPortAsynchronousTrafficShaper
            * CouplingPortCreditBasedShaper
            * CouplingPortRoleEnum
          * ServiceInstances
            * ConsumedEventGroup
            * ConsumedServiceInstance
            * ProvidedServiceInstance
            * PduCollectionTriggerEnum
            * SoAdConfig
            * SocketAddress
            * UdpChecksumCalculationEnum
            * ServiceInstanceCollectionSet
            * AbstractServiceInstance (abstract)
            * PduActivationRoutingGroup
            * EventGroupControlTypeEnum
            * SoConIPduIdentifier
            * SocketConnectionIpduIdentifierSet
            * PduCollectionSemanticsEnum
            * EventHandler
            * SomeipSdServerServiceInstanceConfig
            * InitialSdDelayConfig
            * RequestResponseDelay
            * SomeipSdServerEventGroupTimingConfig
            * SomeipSdClientEventGroupTimingConfig
            * ConsumedProvidedServiceInstanceGroup
            * StaticSocketConnection
            * ServiceVersionAcceptanceKindEnum
            * SomeipSdClientServiceInstanceConfig
            * SomeipServiceVersion
            * TcpRoleEnum
          * Dds
            * DdsCpISignalToDdsTopicMapping
            * DdsCpServiceInstance (abstract)
            * DdsCpProvidedServiceInstance
            * DdsCpConsumedServiceInstance
            * DdsCpServiceInstanceEvent
            * DdsCpServiceInstanceOperation
            * DdsCpConfig
            * DdsCpDomain
            * DdsCpTopic
            * DdsCpPartition
            * DdsCpQosProfile
            * DdsTopicData
            * DdsDurability
            * DdsDurabilityKindEnum
            * DdsDurabilityService
            * DdsDurabilityServiceHistoryKindEnum
            * DdsDeadline
            * DdsLatencyBudget
            * DdsOwnership
            * DdsOwnershipKindEnum
            * DdsOwnershipStrength
            * DdsLiveliness
            * DdsLivenessKindEnum
            * DdsReliability
            * DdsReliabilityKindEnum
            * DdsTransportPriority
            * DdsLifespan
            * DdsDestinationOrder
            * DdsDestinationOrderKindEnum
            * DdsHistory
            * DdsHistoryKindEnum
            * DdsResourceLimits
          * IPv6HeaderFilterList
            * IPv6ExtHeaderFilterSet
            * IPv6ExtHeaderFilterList
          * TcpOptionFilterSet
            * TcpOptionFilterSet
            * TcpOptionFilterList
          * EthernetFrame
            * AbstractEthernetFrame (abstract)
            * EthernetFrameTriggering
            * GenericEthernetFrame
            * UserDefinedEthernetFrame
            * Ieee1722TpEthernetFrame
          * ObsoleteModel
            * SoAdRoutingGroup
            * SocketConnection
        * Fibex4Can
          * CanTopology
            * J1939Cluster (interface)
            * AbstractCanCluster (interface)
            * CanCluster (interface)
            * CanClusterBusOffRecovery
            * CanCommunicationController (interface)
            * AbstractCanCommunicationController (interface)
            * AbstractCanCommunicationControllerAttributes (abstract)
            * CanControllerConfiguration
            * CanControllerConfigurationRequirements
            * CanControllerFdConfiguration
            * CanControllerFdConfigurationRequirements
            * CanControllerXlConfiguration
            * CanControllerXlConfigurationRequirements
            * AbstractCanPhysicalChannel (abstract)
            * CanPhysicalChannel
            * AbstractCanCommunicationConnector (abstract)
            * CanCommunicationConnector
          * CanCommunication
            * CanFrame
            * CanFrameTriggering
            * CanAddressingModeType
            * RxIdentifierRange
            * CanFrameRxBehaviorEnum
            * CanFrameTxBehaviorEnum
            * CanXlFrameTriggeringProps
        * Fibex4Ttcan
          * TtcanTopology
            * TtcanCluster (interface)
            * TtcanCommunicationController (interface)
            * TtcanPhysicalChannel
            * TtcanCommunicationConnector
          * TtcanCommunication
            * TtcanAbsolutelyScheduledTiming
            * TtcanTriggerType
        * Fibex4Flexray
          * FlexrayTopology
            * FlexrayCluster (interface)
            * FlexrayCommunicationController (interface)
            * FlexrayFifoConfiguration
            * FlexrayFifoRange
            * FlexrayCommunicationConnector
            * FlexrayPhysicalChannel
            * FlexrayChannelName
          * FlexrayCommunication
            * FlexrayFrame
            * FlexrayFrameTriggering
            * FlexrayAbsolutelyScheduledTiming
        * Fibex4Lin
          * LinTopology
            * LinCluster (interface)
            * LinCommunicationController (interface)
            * LinMaster (interface)
            * LinSlaveConfig
            * LinSlaveConfigIdent
            * LinSlave (interface)
            * LinCommunicationConnector
            * LinConfigurableFrame
            * LinOrderedConfigurableFrame
            * LinPhysicalChannel
          * LinCommunication
            * LinErrorResponse
            * LinFrame (abstract)
            * LinFrameTriggering
            * LinChecksumType
            * LinUnconditionalFrame
            * LinSporadicFrame
            * LinEventTriggeredFrame
            * LinScheduleTable
            * RunMode
            * ResumePosition
            * ScheduleTableEntry (abstract)
            * ApplicationEntry
            * FreeFormatEntry (abstract)
            * LinConfigurationEntry (abstract)
            * AssignFrameId
            * UnassignFrameId
            * AssignFrameIdRange
            * FramePid
            * AssignNad
            * ConditionalChangeNad
            * SaveConfigurationEntry
            * DataDumpEntry
            * FreeFormat
        * CddSupport
          * UserDefinedCluster (interface)
          * UserDefinedPhysicalChannel
          * UserDefinedCommunicationConnector
          * UserDefinedCommunicationController (interface)
        * Fibex4Multiplatform
          * Gateway
          * FrameMapping
          * IPduMapping
          * TargetIPduRef
          * PduMappingDefaultValue
          * DefaultValueElement
          * ISignalMapping
      * SoftwareCluster
        * CpSoftwareClusterResource (abstract)
        * RoleBasedResourceDependency
        * CpSoftwareCluster
        * CpSoftwareClusterToEcuInstanceMapping
        * CpSoftwareClusterResourceToApplicationPartitionMapping
        * CpSoftwareClusterMappingSet
        * CpSoftwareClusterToApplicationPartitionMapping
        * SystemSignalToCommunicationResourceMapping
        * SystemSignalGroupToCommunicationResourceMapping
        * SwComponentPrototypeAssignment
        * CpSoftwareClusterResourcePool
        * CpSoftwareClusterCommunicationResource
        * CpSoftwareClusterCommunicationResourceProps (abstract)
        * DataComProps
        * DataConsistencyPolicyEnum
        * ClientServerOperationComProps
        * SendIndicationEnum
        * CpSoftwareClusterServiceResource
        * CpSoftwareClusterToResourceMapping
        * BinaryManifest
          * CpSoftwareClusterBinaryManifestDescriptor
          * BinaryManifestProvideResource
          * BinaryManifestResource (abstract)
          * BinaryManifestRequireResource
          * BinaryManifestResourceDefinition
          * BinaryManifestItem
          * BinaryManifestItemDefinition
          * BinaryManifestAddressableObject (abstract)
          * BinaryManifestItemValue (abstract)
          * BinaryManifestItemNumericalValue
          * BinaryManifestItemPointerValue
          * BinaryManifestMetaDataField
      * SecureCommunication
        * CryptoServiceCertificate
        * MacSecProps
        * MacSecLocalKayProps
        * MacSecGlobalKayProps
        * MacSecParticipantSet
        * MacSecKayParticipant
        * MacSecCryptoAlgoConfig
        * MacSecCipherSuiteConfig
        * MacSecConfidentialityOffsetEnum
        * MacSecCapabilityEnum
        * MacSecRoleEnum
        * MacSecFailPermissiveModeEnum
        * CryptoServiceMapping (abstract)
        * SecOcCryptoServiceMapping
        * CryptoServicePrimitive
        * CryptoServiceKey
        * CryptoServiceKeyGenerationEnum
        * CryptoServiceQueue
        * TlsCryptoServiceMapping
        * TlsCryptoCipherSuite
        * TlsVersionEnum
        * TlsPskIdentity
        * TlsCryptoCipherSuiteProps
        * CryptoEllipticCurveProps
        * CryptoSignatureScheme
        * CryptoCertificateAlgorithmFamilyEnum
        * CryptoCertificateFormatEnum
        * IPSecConfig
        * IPSecRule
        * IPSecConfigProps
        * IPsecIpProtocolEnum
        * IPsecPolicyEnum
        * IPsecModeEnum
        * IPsecHeaderTypeEnum
        * IPsecDpdActionEnum
      * NetworkManagement
        * J1939NmNode
        * NmConfig
        * NmCluster (abstract)
        * NmEcu
        * BusspecificNmEcu (abstract)
        * NmCoordinator
        * NmNode (abstract)
        * NmCoordinatorRoleEnum
        * NmClusterCoupling (abstract)
        * FlexrayNmCluster
        * FlexrayNmEcu
        * FlexrayNmClusterCoupling
        * FlexrayNmNode
        * FlexrayNmScheduleVariant
        * CanNmCluster
        * CanNmEcu
        * CanNmClusterCoupling
        * CanNmNode
        * UdpNmCluster
        * UdpNmEcu
        * UdpNmClusterCoupling
        * UdpNmNode
        * J1939NmCluster
        * J1939NodeName
        * J1939NmAddressConfigurationCapabilityEnum
        * J1939NmEcu
      * Transformer
        * DataTransformation
        * DataTransformationKindEnum
        * TransformationTechnology
        * BufferProperties
        * TransformationDescription (abstract)
        * TransformerClassEnum
        * EndToEndTransformationComSpecProps
        * E2EProfileCompatibilityProps
        * EndToEndTransformationDescription
        * DataTransformationSet
        * UserDefinedTransformationDescription
        * TransformationISignalProps (interface)
        * CSTransformerErrorReactionEnum
        * SOMEIPTransformationDescription
        * SOMEIPTransformationISignalProps (interface)
        * SOMEIPMessageTypeEnum
        * TransformationPropsSet
        * TransformationProps (abstract)
        * SOMEIPTransformationProps
        * DataPrototypeTransformationProps
        * DataPrototypeReference (abstract)
        * DataPrototypeInPortInterfaceRef
        * DataIdModeEnum
        * EndToEndProfileBehaviorEnum
        * EndToEndTransformationISignalProps (interface)
        * UserDefinedTransformationISignalProps (interface)
        * UserDefinedTransformationProps
        * TlvDataIdDefinitionSet
        * TlvDataIdDefinition
        * InstanceRef
          * DataPrototypeInSenderReceiverInterfaceInstanceRef
          * DataPrototypeInClientServerInterfaceInstanceRef
          * ImplementationDataTypeElementInPortInterfaceRef
          * DataPrototypeInPortInterfaceInstanceRef (abstract)
      * DataMapping
        * DataMapping (abstract)
        * SenderReceiverToSignalMapping
        * SenderReceiverToSignalGroupMapping
        * SenderRecCompositeTypeMapping (abstract)
        * SenderRecArrayTypeMapping
        * SenderRecRecordTypeMapping
        * SenderRecRecordElementMapping
        * SenderRecArrayElementMapping
        * IndexedArrayElement
        * ClientServerToSignalMapping
        * SenderReceiverCompositeElementToSignalMapping
        * TriggerToSignalMapping
        * DataTypePolicyEnum
      * EndToEndProtection
        * EndToEndProtectionISignalIPdu
      * ECUResourceMapping
        * ECUMapping
        * CommunicationControllerMapping
        * HwPortMapping
      * SWmapping
        * SwcToEcuMapping
        * SwcToImplMapping
        * SwcToApplicationPartitionMapping
        * ApplicationPartition
        * ApplicationPartitionToEcuPartitionMapping
        * EcuPartition
        * MappingConstraint (abstract)
        * ComponentClustering
        * MappingScopeEnum
        * ComponentSeparation
        * J1939ControllerApplicationToJ1939NmNodeMapping
        * J1939ControllerApplication
        * EcuResourceEstimation
      * RteEventToOsTaskMapping
        * OsTaskProxy
        * OsTaskPreemptabilityEnum
        * AppOsTaskProxyToEcuTaskProxyMapping
        * RteEventInCompositionToOsTaskProxyMapping
        * RteEventInCompositionSeparation
        * RteEventInSystemToOsTaskProxyMapping
        * RteEventInSystemSeparation
      * SignalPaths
        * CommonSignalPath
        * SwcToSwcSignal
        * SwcToSwcOperationArguments
        * SwcToSwcOperationArgumentsDirectionEnum
        * ForbiddenSignalPath
        * PermissibleSignalPath
        * SeparateSignalPath
        * SignalPathConstraint (abstract)
      * PncMapping
        * PncMapping
        * PncMappingIdent
      * GeneralPurposeConnection
        * GeneralPurposeConnection
      * DoIP
        * DoIpConfig
        * DoIpInterface
        * DoIpRoutingActivation
        * AbstractDoIpLogicAddressProps (abstract)
        * DoIpLogicTargetAddressProps
        * DoIpLogicTesterAddressProps
      * TransportProtocols
        * DoIpTpConfig
        * DoIpLogicAddress
        * TpConfig (abstract)
        * TpAddress
        * FlexrayTpConfig
        * FlexrayTpConnectionControl
        * FlexrayTpConnection
        * FlexrayTpPduPool
        * FlexrayTpNode
        * FlexrayTpEcu
        * FlexrayArTpConfig
        * FlexrayArTpChannel
        * FlexrayArTpNode
        * FlexrayArTpConnection
        * FrArTpAckType
        * MaximumMessageLengthType
        * CanTpConfig
        * CanTpChannel
        * CanTpConnection
        * CanTpAddressingFormatType
        * CanTpAddress
        * CanTpEcu
        * CanTpNode
        * NetworkTargetAddressType
        * LinTpConfig
        * LinTpNode
        * LinTpConnection
        * EthTpConfig
        * EthTpConnection
        * SomeipTpConfig
        * SomeipTpConnection
        * SomeipTpChannel
        * J1939TpConfig
        * J1939TpConnection
        * J1939TpPg
        * J1939TpNode
        * IEEE1722Tp
          * IEEE1722TpConfig
          * IEEE1722TpConnection (abstract)
          * IEEE1722TpAvConnection (abstract)
          * IEEE1722TpAcfConnection
          * IEEE1722TpAv
            * IEEE1722TpCrfConnection
            * IEEE1722TpCrfTypeEnum
            * IEEE1722TpCrfPullEnum
            * IEEE1722TpAafConnection
            * IEEE1722TpAafNominalRateEnum
            * IEEE1722TpAafFormatEnum
            * IEEE1722TpAafAes3DataTypeEnum
            * IEEE1722TpIidcConnection
            * IEEE1722TpRvfConnection
            * IEEE1722TpRvfPixelDepthEnum
            * IEEE1722TpRvfPixelFormatEnum
            * IEEE1722TpRvfColorSpaceEnum
            * IEEE1722TpRvfFrameRateEnum
          * IEEE1722TpAcf
            * IEEE1722TpAcfBus (abstract)
            * IEEE1722TpAcfBusPart (abstract)
            * IEEE1722TpAcfCan
            * IEEE1722TpAcfCanPart
            * IEEE1722TpAcfCanMessageTypeEnum
            * IEEE1722TpAcfLin
            * IEEE1722TpAcfLinPart
      * BusMirror
        * BusMirrorChannelMapping (abstract)
        * MirroringProtocolEnum
        * BusMirrorChannel
        * BusMirrorChannelMappingCan
        * BusMirrorCanIdRangeMapping
        * BusMirrorCanIdToCanIdMapping
        * BusMirrorLinPidToCanIdMapping
        * BusMirrorChannelMappingFlexray
        * BusMirrorChannelMappingIp
        * BusMirrorChannelMappingUserDefined
      * Dlt
        * DltConfig
        * DltLogChannel
        * DltDefaultTraceStateEnum
        * LogTraceDefaultLogLevelEnum
      * GlobalTime
        * GlobalTimeDomain
        * AbstractGlobalTimeDomainProps (abstract)
        * NetworkSegmentIdentification
        * GlobalTimeMaster (abstract)
        * GlobalTimeSlave (abstract)
        * GlobalTimeGateway
        * GlobalTimeCorrectionProps
        * GlobalTimeCrcSupportEnum
        * GlobalTimeCrcValidationEnum
        * GlobalTimeIcvSupportEnum
        * GlobalTimeIcvVerificationEnum
        * CAN
          * GlobalTimeCanMaster
          * GlobalTimeCanSlave
          * CanGlobalTimeDomainProps
        * ETH
          * GlobalTimeEthMaster
          * EthTSynSubTlvConfig
          * GlobalTimeEthSlave
          * EthGlobalTimeDomainProps
          * EthTSynCrcFlags
          * EthGlobalTimeMessageFormatEnum
          * EthGlobalTimeManagedCouplingPort
          * GlobalTimePortRoleEnum
        * FR
          * GlobalTimeFrMaster
          * GlobalTimeFrSlave
          * FrGlobalTimeDomainProps
        * UserDefined
          * UserDefinedGlobalTimeMaster
          * UserDefinedGlobalTimeSlave
      * InstanceRefs
        * ComponentInSystemInstanceRef
        * OperationInSystemInstanceRef
        * VariableDataPrototypeInSystemInstanceRef
        * TriggerInSystemInstanceRef
        * PortGroupInSystemInstanceRef
    * DiagnosticExtract
      * CommonDiagnostics
        * DiagnosticCommonElement (abstract)
        * DiagnosticDataIdentifier
        * DiagnosticDynamicDataIdentifier
        * DiagnosticAbstractDataIdentifier (abstract)
        * DiagnosticParameter
        * DiagnosticParameterElement
        * DiagnosticParameterIdent
        * DiagnosticAbstractParameter (abstract)
        * DiagnosticDataElement
        * DiagnosticRoutineSubfunction (abstract)
        * DiagnosticRoutine
        * DiagnosticStartRoutine
        * DiagnosticStopRoutine
        * DiagnosticRequestRoutineResults
        * DiagnosticParameterIdentifier
        * DiagnosticParameterSupportInfo
        * DiagnosticSupportInfoByte
        * DiagnosticInfoType
      * DiagnosticContribution
        * DiagnosticContributionSet
        * DiagnosticProtocol
        * DiagnosticServiceTable
        * DiagnosticEcuInstanceProps
        * DiagnosticObdSupportEnum
      * DiagnosticCommonProps
        * DiagnosticCommonProps (interface)
        * DiagnosticOccurrenceCounterProcessingEnum
        * DiagnosticEventCombinationBehaviorEnum
        * DiagnosticEventCombinationReportingBehaviorEnum
      * Dem
        * DiagnosticTroubleCode
          * DiagnosticTypeOfDtcSupportedEnum
          * DiagnosticTroubleCodeUds
          * DiagnosticTroubleCodeObd
          * EventObdReadinessGroup
          * DiagnosticTroubleCode (abstract)
          * DiagnosticTroubleCodeGroup
          * DiagnosticStatusBitHandlingTestFailedSinceLastClearEnum
          * DiagnosticTroubleCodeProps
          * DiagnosticSignificanceEnum
          * DiagnosticUdsSeverityEnum
          * DiagnosticDataIdentifierSet
          * DiagnosticWwhObdDtcClassEnum
          * DiagnosticTroubleCodeJ1939DtcKindEnum
          * DiagnosticTroubleCodeJ1939
        * DiagnosticEvent
          * DiagnosticEvent
          * DiagnosticClearEventAllowedBehaviorEnum
          * DiagnosticConnectedIndicator
          * DiagnosticEventClearAllowedEnum
          * DiagnosticEventKindEnum
          * DiagnosticConnectedIndicatorBehaviorEnum
          * DiagnosticIumpr
          * DiagnosticIumprKindEnum
          * DiagnosticIumprGroup
          * DiagnosticIumprGroupIdentifier
          * DiagnosticIumprDenominatorGroup
          * DiagnosticAbstractAliasEvent (abstract)
          * DiagnosticFimAliasEventMapping
        * DiagnosticMemoryDestination
          * DiagnosticMemoryDestination (abstract)
          * DiagnosticMemoryEntryStorageTriggerEnum
          * DiagnosticClearDtcLimitationEnum
          * DiagnosticEventDisplacementStrategyEnum
          * DiagnosticTypeOfFreezeFrameRecordNumerationEnum
          * DiagnosticMemoryDestinationPrimary
          * DiagnosticMemoryDestinationUserDefined
        * DiagnosticExtendedDataRecord
          * DiagnosticExtendedDataRecord
        * DiagnosticFreezeFrame
          * DiagnosticRecordTriggerEnum
          * DiagnosticFreezeFrame
        * DiagnosticCondition
          * DiagnosticCondition (abstract)
          * DiagnosticEnableCondition
          * DiagnosticStorageCondition
        * DiagnosticDebouncingAlgorithm
          * DiagnosticDebounceAlgorithmProps
          * DiagnosticDebounceBehaviorEnum
        * DiagnosticConditionGroup
          * DiagnosticConditionGroup (abstract)
          * DiagnosticEnableConditionGroup
          * DiagnosticStorageConditionGroup
        * DiagnosticOperationCycle
          * DiagnosticOperationCycle
          * DiagnosticOperationCycleTypeEnum
        * DiagnosticAging
          * DiagnosticAging
        * DiagnosticIndicator
          * DiagnosticIndicator
          * DiagnosticIndicatorTypeEnum
        * DiagnosticTestResult
          * DiagnosticTestResult
          * DiagnosticTestResultUpdateEnum
          * DiagnosticTestIdentifier
          * DiagnosticMeasurementIdentifier
      * Dcm
        * DiagnosticAccessPermission
        * DiagnosticSession
        * DiagnosticJumpToBootLoaderEnum
        * DiagnosticSecurityLevel
        * DiagnosticAuthRoleProxy
        * DiagnosticAuthRole
        * DiagnosticService
          * CommonService
            * DiagnosticServiceClass (abstract)
            * DiagnosticServiceInstance (abstract)
            * DiagnosticCustomServiceClass
          * CustomServiceInstance
            * DiagnosticCustomServiceInstance
          * SessionControl
            * DiagnosticSessionControl
            * DiagnosticSessionControlClass
          * SecurityAccess
            * DiagnosticSecurityAccess
            * DiagnosticSecurityAccessClass
          * Authentication
            * DiagnosticAuthentication (abstract)
            * DiagnosticAuthenticationClass
            * DiagnosticAuthenticationConfiguration
            * DiagnosticVerifyCertificateBidirectional
            * DiagnosticVerifyCertificateUnidirectional
            * DiagnosticDeAuthentication
            * DiagnosticProofOfOwnership
            * DiagnosticAuthTransmitCertificate
            * DiagnosticAuthTransmitCertificateEvaluation
          * EcuReset
            * DiagnosticEcuReset
            * DiagnosticEcuResetClass
            * DiagnosticResponseToEcuResetEnum
          * CommunicationControl
            * DiagnosticComControl
            * DiagnosticComControlSpecificChannel
            * DiagnosticComControlClass
            * DiagnosticComControlSubNodeChannel
          * ControlDTCSetting
            * DiagnosticControlDTCSetting
            * DiagnosticControlDTCSettingClass
          * DataByIdentifier
            * DiagnosticReadDataByIdentifier
            * DiagnosticWriteDataByIdentifier
            * DiagnosticWriteDataByIdentifierClass
            * DiagnosticDataByIdentifier (abstract)
            * DiagnosticReadDataByIdentifierClass
            * DiagnosticReadScalingDataByIdentifier
            * DiagnosticReadScalingDataByIdentifierClass
          * IOControl
            * DiagnosticIOControl
            * DiagnosticIoControlClass
            * DiagnosticControlEnableMaskBit
          * RoutineControl
            * DiagnosticRoutineControl
            * DiagnosticRoutineControlClass
          * DynamicallyDefineDataIdentifier
            * DiagnosticDynamicallyDefineDataIdentifier
            * DiagnosticDynamicallyDefineDataIdentifierClass
          * DynamicallyDefineData
            * DiagnosticHandleDDDIConfigurationEnum
            * DiagnosticDynamicallyDefineDataIdentifierSubfunctionEnum
          * ReadDataByPeriodicID
            * DiagnosticReadDataByPeriodicID
            * DiagnosticReadDataByPeriodicIDClass
            * DiagnosticPeriodicRate
            * DiagnosticPeriodicRateCategoryEnum
          * ResponseOnEvent
            * DiagnosticResponseOnEvent
            * DiagnosticResponseOnEventClass
            * DiagnosticEventWindow
            * DiagnosticEventWindowTimeEnum
            * DiagnosticResponseOnEventActionEnum
          * ReadDTCInformation
            * DiagnosticReadDTCInformation
            * DiagnosticReadDTCInformationClass
          * ClearDiagnosticInfo
            * DiagnosticClearDiagnosticInformation
            * DiagnosticClearDiagnosticInformationClass
          * MemoryByAddress
            * DiagnosticMemoryByAddress (abstract)
            * DiagnosticMemoryAddressableRangeAccess (abstract)
            * DiagnosticMemoryIdentifier
            * DiagnosticWriteMemoryByAddress
            * DiagnosticWriteMemoryByAddressClass
            * DiagnosticReadMemoryByAddress
            * DiagnosticReadMemoryByAddressClass
            * DiagnosticTransferExit
            * DiagnosticTransferExitClass
            * DiagnosticDataTransfer
            * DiagnosticDataTransferClass
            * DiagnosticRequestDownload
            * DiagnosticRequestDownloadClass
            * DiagnosticRequestUpload
            * DiagnosticRequestUploadClass
          * RequestFileTransfer
            * DiagnosticRequestFileTransfer
            * DiagnosticRequestFileTransferClass
        * EnvironmentalCondition
          * DiagnosticEnvironmentalCondition
          * DiagnosticEnvConditionFormula
          * DiagnosticLogicalOperatorEnum
          * DiagnosticEnvConditionFormulaPart (abstract)
          * DiagnosticEnvCompareCondition (abstract)
          * DiagnosticCompareTypeEnum
          * DiagnosticEnvDataCondition
          * DiagnosticEnvDataElementCondition
          * DiagnosticEnvModeCondition
          * DiagnosticEnvModeElement (abstract)
          * DiagnosticEnvSwcModeElement
          * DiagnosticEnvBswModeElement
        * ObdService
          * Mode_0x01_RequestCurrentPowertrain
            * DiagnosticRequestCurrentPowertrainData
            * DiagnosticRequestCurrentPowertrainDataClass
          * Mode_0x02_RequestPowertrainFreeze
            * DiagnosticRequestPowertrainFreezeFrameData
            * DiagnosticRequestPowertrainFreezeFrameDataClass
            * DiagnosticPowertrainFreezeFrame
          * Mode_0x03_0x07_RequestEmission
            * DiagnosticRequestEmissionRelatedDTC
            * DiagnosticRequestEmissionRelatedDTCClass
          * Mode_0x04_ClearResetEmission
            * DiagnosticClearResetEmissionRelatedInfo
            * DiagnosticClearResetEmissionRelatedInfoClass
          * Mode_0x06_RequestOnBoard
            * DiagnosticRequestOnBoardMonitoringTestResults
            * DiagnosticRequestOnBoardMonitoringTestResultsClass
          * Mode_0x08_RequestControlOfOnBoard
            * DiagnosticRequestControlOfOnBoardDevice
            * DiagnosticRequestControlOfOnBoardDeviceClass
            * DiagnosticTestRoutineIdentifier
          * Mode_0x09_RequestVehicleInformation
            * DiagnosticRequestVehicleInfo
            * DiagnosticRequestVehicleInfoClass
          * Mode_0x0A_RequestEmissionRelated
            * DiagnosticRequestEmissionRelatedDTCPermanentStatus
            * DiagnosticRequestEmissionRelatedDTCPermanentStatusClass
      * DiagnosticMapping
        * DiagnosticTroubleCodeUdsToTroubleCodeObdMapping
        * DiagnosticMapping (abstract)
        * DiagnosticSwMapping (abstract)
        * DiagnosticAuthTransmitCertificateMapping
        * DiagnosticEventToTroubleCodeUdsMapping
        * DiagnosticEventToOperationCycleMapping
        * DiagnosticEventToDebounceAlgorithmMapping
        * DiagnosticEventToEnableConditionGroupMapping
        * DiagnosticEventToStorageConditionGroupMapping
        * DiagnosticEventPortMapping
        * DiagnosticOperationCyclePortMapping
        * DiagnosticEnableConditionPortMapping
        * DiagnosticStorageConditionPortMapping
        * DiagnosticMasterToSlaveEventMapping
        * DiagnosticEventToSecurityEventMapping
        * DiagnosticIumprToFunctionIdentifierMapping
        * DiagnosticSecureCodingMapping
        * ServiceMapping
          * DiagnosticServiceDataMapping
          * DiagnosticParameterElementAccess
          * DiagnosticServiceMappingDiagTarget (abstract)
          * DiagnosticServiceSwMapping
          * BswServiceDependencyIdent
          * DiagnosticSecurityEventReportingModeMapping
          * DiagnosticDemProvidedDataMapping
          * DiagnosticFimFunctionMapping
        * FimMapping
          * DiagnosticInhibitSourceEventMapping
          * DiagnosticFimAliasEventGroupMapping
        * DiagnosticJ1939Mapping
          * DiagnosticJ1939SpnMapping
          * DiagnosticJ1939SwMapping
          * DiagnosticEventToTroubleCodeJ1939Mapping
        * CpSoftwareCluster
          * CpSwClusterToDiagEventMapping
          * CpSwClusterResourceToDiagDataElemMapping
          * CpSwClusterToDiagRoutineSubfunctionMapping
          * CpSwClusterResourceToDiagFunctionIdMapping
      * Fim
        * DiagnosticFimAliasEvent
        * DiagnosticFunctionIdentifier
        * DiagnosticFunctionIdentifierInhibit
        * DiagnosticFunctionInhibitSource
        * DiagnosticInhibitionMaskEnum
        * DiagnosticFimEventGroup
        * DiagnosticFimAliasEventGroup
      * J1939
        * DiagnosticJ1939Spn
        * DiagnosticJ1939FreezeFrame
        * DiagnosticJ1939ExpandedFreezeFrame
        * DiagnosticJ1939Node
      * InstanceRefs
        * DataPrototypeInSystemInstanceRef
        * SwcServiceDependencyInSystemInstanceRef
        * PModeInSystemInstanceRef
    * SecurityExtractTemplate
      * SecurityEventContextProps
      * SecurityEventDefinition
      * IdsDesign
      * SecurityEventFilterChain
      * AbstractSecurityEventFilter (abstract)
      * SecurityEventStateFilter
      * SecurityEventOneEveryNFilter
      * SecurityEventAggregationFilter
      * SecurityEventContextDataSourceEnum
      * SecurityEventThresholdFilter
      * IdsmRateLimitation
      * IdsmTrafficLimitation
      * SecurityEventContextMapping (abstract)
      * SecurityEventReportingModeEnum
      * SecurityEventContextMappingBswModule
      * SecurityEventContextMappingFunctionalCluster
      * SecurityEventContextMappingCommConnector
      * SecurityEventContextMappingApplication
      * IdsmInstance
      * BlockState
      * IdsCommonElement (abstract)
      * IdsMapping (abstract)
      * IdsmProperties
      * IdsmSignatureSupportAp
      * IdsmSignatureSupportCp
      * SecurityEventContextData
    * EcuResourceTemplate
      * HwElement
      * HwDescriptionEntity (abstract)
      * HwPinGroup
      * HwPinGroupContent (interface)
      * HwPin
      * HwElementConnector
      * HwPinGroupConnector
      * HwPinConnector
      * HwElementCategory
        * HwAttributeValue
        * HwType
        * HwCategory
        * HwAttributeDef
        * HwAttributeLiteralDef
    * LogAndTraceExtract
      * DltArgument
      * DltApplication
      * DltContext
      * DltEcu
      * DltMessage
      * LogAndTraceMessageCollectionSet
      * PrivacyLevel
    * AdaptivePlatform
      * PlatformModuleDeployment
        * Firewall
          * StateDependentFirewall
          * FirewallRuleProps
          * FirewallRule
        * CryptoDeployment
          * CryptoKeySlot
        * IntrusionDetectionSystem
          * IdsPlatformInstantiation (abstract)
          * IdsmModuleInstantiation
        * AdaptiveModule
          * PlatformModuleEthernetEndpointConfiguration
      * ApplicationDesign
        * PortInterface
          * Field
    * AbstractPlatform
      * ApplicationInterface
      * ApplicationDeferredDataType
    * FeatureModelTemplate
      * FMFeatureModel
      * FMFeature
      * FMAttributeDef
      * FMFeatureDecomposition
      * FMFeatureRestriction
      * FMFeatureRelation
      * FMFeatureSelection
      * FMFeatureSelectionState
      * FMAttributeValue
      * FMFeatureSelectionSet
      * FMFeatureMap
      * FMFeatureMapElement
      * FMFeatureMapCondition
      * FMFeatureMapAssertion
      * FMFormulaByFeaturesAndAttributes (interface)
      * FMConditionByFeaturesAndAttributes (interface)
      * FMFormulaByFeaturesAndSwSystemconsts (interface)
      * FMConditionByFeaturesAndSwSystemconsts (interface)
  * MSR
    * DataDictionary
      * ServiceProcessTask
        * SwServiceImplPolicyEnum
        * SwServiceArg
      * DataDefProperties
        * SwPointerTargetProps
        * SwCalibrationAccessEnum
        * SwDataDefProps (interface)
        * SwImplPolicyEnum
        * SwTextProps
        * ValueList (interface)
        * SwBitRepresentation
        * SwDataDependency
        * SwDataDependencyArgs (interface)
        * DisplayPresentationEnum
      * AuxillaryObjects
        * SwAddrMethod
        * MemoryAllocationKeywordPolicyType
        * MemorySectionType
      * SystemConstant
        * SwSystemconst
      * CalibrationParameter
        * SwCalprmAxisSet
        * SwCalprmAxis
        * CalprmAxisCategoryEnum
        * SwCalprmAxisTypeProps (abstract)
      * Axis
        * SwAxisIndividual
        * SwAxisGeneric
        * SwAxisType
        * SwGenericAxisParam
        * SwGenericAxisParamType
        * SwAxisGrouped
      * DatadictionaryProxies
        * SwCalprmRefProxy
        * SwVariableRefProxy
      * RecordLayout
        * SwRecordLayout
        * SwRecordLayoutV
        * SwRecordLayoutGroup
        * SwRecordLayoutGroupContent (interface)
    * AsamHdo
      * ComputationMethod
        * CompuMethod
        * CompuGenericMath (interface)
        * Compu
        * CompuContent (abstract)
        * CompuScale
        * CompuScales
        * CompuScaleContents (abstract)
        * CompuConstTextContent
        * CompuConstNumericContent
        * CompuRationalCoeffs
        * CompuConst
        * CompuConstContent (abstract)
        * CompuScaleRationalFormula
        * CompuScaleConstantContents
        * CompuNominatorDenominator
        * CompuConstFormulaContent
      * BaseTypes
        * SwBaseType
        * BaseType (abstract)
        * BaseTypeDirectDefinition
        * BaseTypeDefinition (abstract)
      * Constraints
        * GlobalConstraints
          * DataConstr
          * DataConstrRule
          * PhysConstrs
          * InternalConstrs
          * ScaleConstr
      * SpecialData
        * Sdg
        * SdgContents (interface)
        * SdgCaption
        * Sd
        * Sdf
      * Units
        * Unit
        * UnitGroup
        * PhysicalDimension
        * PhysicalDimensionMapping
        * PhysicalDimensionMappingSet
      * AdminData
        * AdminData
        * DocRevision
        * Modification
    * Documentation
      * BlockElements
        * DocumentationBlock (interface)
        * Caption
        * RequirementsTracing
          * StructuredReq
          * TraceableText
          * Traceable (abstract)
        * Formula
          * MlFormula
        * ListElements
          * List
          * Item
          * ListEnum
          * LabeledList
          * LabeledItem
          * IndentSample
          * ItemLabelPosEnum
          * DefList
          * DefItem
        * Figure
          * Area
          * AreaEnumNohref
          * AreaEnumShape
          * Graphic
          * GraphicFitEnum
          * GraphicNotationEnum
          * Map
          * MlFigure
          * LGraphic
        * Note
          * Note
          * NoteTypeEnum
        * PaginationAndView
          * ChapterEnumBreak
          * Paginateable (abstract)
          * KeepWithPreviousEnum
          * DocumentViewSelectable (abstract)
        * OasisExchangeTable
          * Table
          * FloatEnum
          * FrameEnum
          * Tgroup
          * AlignEnum
          * Tbody
          * ValignEnum
          * Row
          * Entry
          * PgwideEnum
          * Colspec
        * GerneralParameters
          * Prms
      * TextModel
        * MultilanguageData
          * MultiLanguageOverviewParagraph
          * MultilanguageLongName
          * MultiLanguageParagraph
          * MultiLanguageVerbatim
          * MultiLanguagePlainText
        * LanguageDataModel
          * LLongName (interface)
          * WhitespaceControlled (abstract)
          * LVerbatim (interface)
          * LOverviewParagraph (interface)
          * LParagraph (interface)
          * LPlainText (interface)
          * LanguageSpecific (abstract)
          * LEnum
        * SingleLanguageData
          * SingleLanguageUnitNames (interface)
          * SingleLanguageLongName (interface)
          * SlOverviewParagraph (interface)
          * SlParagraph (interface)
        * InlineTextModel
          * MixedContentForLongName (interface)
          * MixedContentForParagraph (interface)
          * MixedContentForOverviewParagraph (interface)
          * MixedContentForVerbatim (interface)
          * MixedContentForPlainText (interface)
          * MixedContentForUnitNames (interface)
        * InlineTextElements
          * Br
          * EmphasisText (interface)
          * IndexEntry (interface)
          * Std
          * Tt
          * Xdoc
          * Xfile
          * Xref
          * XrefTarget
        * InlineAttributeEnums
          * EEnumFont
          * EEnum
          * ResolutionPolicyEnum
          * ShowContentEnum
          * ShowResourceAliasNameEnum
          * ShowResourceCategoryEnum
          * ShowResourceLongNameEnum
          * ShowResourceNumberEnum
          * ShowResourcePageEnum
          * ShowResourceShortNameEnum
          * ShowResourceTypeEnum
          * ShowSeeEnum
      * Annotation
        * Annotation
      * Chapters
        * Chapter
        * ChapterModel
        * ChapterContent (interface)
        * PredefinedChapter
        * Topic1
        * TopicContentOrMsrQuery (interface)
        * TopicOrMsrQuery (interface)
        * ChapterOrMsrQuery (interface)
        * TopicContent (interface)
      * MsrQuery
        * MsrQueryP1
        * MsrQueryTopic1
        * MsrQueryChapter
        * MsrQueryProps
        * MsrQueryArg
        * MsrQueryResultChapter
        * MsrQueryResultTopic1
        * MsrQueryP2
    * CalibrationData
      * CalibrationValue
        * SwValueCont
        * SwAxisCont
        * SwValues (interface)
        * ValueGroup
