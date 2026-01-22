## Class Hierarchy

* ARObject (abstract)
  * AUTOSAR
  * AbstractCanCommunicationControllerAttributes (abstract)
    * CanControllerConfiguration
    * CanControllerConfigurationRequirements
  * AbstractGlobalTimeDomainProps (abstract)
    * CanGlobalTimeDomainProps
    * EthGlobalTimeDomainProps
    * FrGlobalTimeDomainProps
  * AbstractMultiplicityRestriction (abstract)
  * AbstractValueRestriction (abstract)
  * AbstractVariationRestriction (abstract)
    * SdgPrimitiveAttributeWithVariation
  * AccessCount
  * AccessCountSet
  * AdminData
  * AliasNameAssignment
  * ArParameterInImplementationDataInstanceRef
  * ArVariableInImplementationDataInstanceRef
  * Area
  * AtpInstanceRef (abstract)
    * AnyInstanceRef
    * ApplicationCompositeElementInPortInterfaceInstanceRef
    * ComponentInCompositionInstanceRef
    * ComponentInSystemInstanceRef
    * DataPrototypeInPortInterfaceInstanceRef (abstract)
      * DataPrototypeInClientServerInterfaceInstanceRef
      * DataPrototypeInSenderReceiverInterfaceInstanceRef
    * DataPrototypeInSystemInstanceRef
    * InnerDataPrototypeGroupInCompositionInstanceRef
    * InnerPortGroupInCompositionInstanceRef
    * InnerRunnableEntityGroupInCompositionInstanceRef
    * InstanceEventInCompositionInstanceRef
    * ModeGroupInAtomicSwcInstanceRef (abstract)
      * PModeGroupInAtomicSwcInstanceRef
      * RModeGroupInAtomicSWCInstanceRef
    * ModeInBswModuleDescriptionInstanceRef
    * ModeInSwcInstanceRef
    * OperationInAtomicSwcInstanceRef (abstract)
      * POperationInAtomicSwcInstanceRef
      * ROperationInAtomicSwcInstanceRef
    * OperationInSystemInstanceRef
    * PModeInSystemInstanceRef
    * ParameterInAtomicSWCTypeInstanceRef
    * PortGroupInSystemInstanceRef
    * PortInCompositionTypeInstanceRef (abstract)
      * PPortInCompositionInstanceRef
      * RPortInCompositionInstanceRef
    * RModeInAtomicSwcInstanceRef
    * RunnableEntityInCompositionInstanceRef
    * SwcServiceDependencyInSystemInstanceRef
    * TriggerInAtomicSwcInstanceRef (abstract)
      * PTriggerInAtomicSwcTypeInstanceRef
      * RTriggerInAtomicSwcInstanceRef
    * TriggerInSystemInstanceRef
    * VariableDataPrototypeInCompositionInstanceRef
    * VariableDataPrototypeInSystemInstanceRef
    * VariableInAtomicSWCTypeInstanceRef
    * VariableInAtomicSwcInstanceRef (abstract)
      * RVariableInAtomicSwcInstanceRef
  * AutosarParameterRef
  * AutosarVariableRef
  * BaseTypeDefinition (abstract)
    * BaseTypeDirectDefinition
  * BinaryManifestItemValue (abstract)
    * BinaryManifestItemNumericalValue
    * BinaryManifestItemPointerValue
  * BlueprintGenerator
  * Br
  * BswEntryRelationship
  * BswModeReceiverPolicy
  * BswModeSenderPolicy
  * BswModeSwitchAckRequest
  * BswTriggerDirectImplementation
  * BufferProperties
  * BuildActionInvocator
  * BuildActionIoElement
  * BusMirrorCanIdRangeMapping
  * BusMirrorCanIdToCanIdMapping
  * BusMirrorChannel
  * BusMirrorLinPidToCanIdMapping
  * BusspecificNmEcu (abstract)
    * CanNmEcu
    * FlexrayNmEcu
    * J1939NmEcu
    * UdpNmEcu
  * CalibrationParameterValue
  * CanClusterBusOffRecovery
  * CanControllerFdConfiguration
  * CanControllerFdConfigurationRequirements
  * CanControllerXlConfiguration
  * CanControllerXlConfigurationRequirements
  * CanTpEcu
  * CanXlFrameTriggeringProps
  * ChapterContent
  * ChapterModel
  * ChapterOrMsrQuery
  * ClientIdRange
  * ClientServerApplicationErrorMapping
  * ClientServerOperationMapping
  * Colspec
  * CommunicationControllerMapping
  * CommunicationCycle (abstract)
    * CycleCounter
    * CycleRepetition
  * CompositeNetworkRepresentation
  * CompositeRuleBasedValueArgument (abstract)
    * ApplicationRuleBasedValueSpecification
  * Compu
  * CompuConst
  * CompuConstContent (abstract)
    * CompuConstFormulaContent
    * CompuConstNumericContent
    * CompuConstTextContent
  * CompuContent (abstract)
    * CompuScales
  * CompuNominatorDenominator
  * CompuRationalCoeffs
  * CompuScale
  * CompuScaleContents (abstract)
    * CompuScaleConstantContents
    * CompuScaleRationalFormula
  * ConfidenceInterval
  * ConstantSpecificationMapping
  * ContainedIPduProps
  * CouplingPortConnection
  * CouplingPortDetails
  * CouplingPortRatePolicy
  * CpSoftwareClusterCommunicationResourceProps (abstract)
    * ClientServerOperationComProps
    * DataComProps
  * DataConstrRule
  * DataFilter
  * DataMapping (abstract)
    * ClientServerToSignalMapping
    * SenderReceiverCompositeElementToSignalMapping
    * SenderReceiverToSignalGroupMapping
    * SenderReceiverToSignalMapping
    * TriggerToSignalMapping
  * DataPrototypeMapping
  * DataPrototypeReference (abstract)
    * DataPrototypeInPortInterfaceRef
    * ImplementationDataTypeElementInPortInterfaceRef
  * DataPrototypeTransformationProps
  * DataTypeMap
  * DdsCpISignalToDdsTopicMapping
  * DdsCpServiceInstanceEvent
  * DdsCpServiceInstanceOperation
  * DdsDeadline
  * DdsDestinationOrder
  * DdsDurability
  * DdsDurabilityService
  * DdsHistory
  * DdsLatencyBudget
  * DdsLifespan
  * DdsLiveliness
  * DdsOwnership
  * DdsOwnershipStrength
  * DdsReliability
  * DdsResourceLimits
  * DdsTopicData
  * DdsTransportPriority
  * DefaultValueElement
  * Describable (abstract)
    * CyclicTiming
    * EventControlledTiming
    * HwElementConnector
    * HwPinConnector
    * HwPinGroupConnector
    * IPduTiming
    * Ipv4DhcpServerConfiguration
    * Ipv6DhcpServerConfiguration
    * PncMapping
    * SocketConnection
    * TransformationComSpecProps (abstract)
      * EndToEndTransformationComSpecProps
      * UserDefinedTransformationComSpecProps
    * TransformationDescription (abstract)
      * EndToEndTransformationDescription
      * SOMEIPTransformationDescription
      * UserDefinedTransformationDescription
    * TransformationISignalProps (abstract)
      * EndToEndTransformationISignalProps
      * SOMEIPTransformationISignalProps
      * UserDefinedTransformationISignalProps
  * DhcpServerConfiguration
  * Dhcpv6Props
  * DiagnosticAbstractParameter (abstract)
    * DiagnosticParameter
  * DiagnosticAuthRoleProxy
  * DiagnosticComControlSpecificChannel
  * DiagnosticComControlSubNodeChannel
  * DiagnosticCommonProps
  * DiagnosticControlEnableMaskBit
  * DiagnosticEnvConditionFormulaPart (abstract)
    * DiagnosticEnvCompareCondition (abstract)
      * DiagnosticEnvDataCondition
      * DiagnosticEnvDataElementCondition
      * DiagnosticEnvModeCondition
    * DiagnosticEnvConditionFormula
  * DiagnosticEventWindow
  * DiagnosticIumprGroupIdentifier
  * DiagnosticParameterElementAccess
  * DiagnosticParameterSupportInfo
  * DiagnosticPeriodicRate
  * DiagnosticServiceMappingDiagTarget (abstract)
    * DiagnosticParameterIdent
  * DiagnosticSupportInfoByte
  * DiagnosticTestIdentifier
  * DltConfig
  * DoIpConfig
  * DoIpEntity
  * DocRevision
  * DocumentViewSelectable (abstract)
    * Paginateable (abstract)
      * Chapter
      * DefItem
      * DefList
      * Item
      * LabeledItem
      * LabeledList
      * List
      * MlFigure
      * MlFormula
      * MsrQueryChapter
      * MsrQueryP1
      * MsrQueryTopic1
      * MultiLanguageParagraph
      * MultiLanguageVerbatim
      * Note
      * Prms
      * Row
      * StructuredReq
      * Table
      * Topic1
      * TraceableText
  * DocumentationBlock
  * DynamicPartAlternative
  * EcuResourceEstimation
  * EcucAbstractConfigurationClass (abstract)
    * EcucMultiplicityConfigurationClass
    * EcucValueConfigurationClass
  * EcucConditionSpecification
  * EcucDerivationSpecification
  * EcucDestinationUriPolicy
  * EcucIndexableValue (abstract)
    * EcucAbstractReferenceValue (abstract)
      * EcucInstanceReferenceValue
      * EcucReferenceValue
    * EcucParameterValue (abstract)
      * EcucAddInfoParamValue
      * EcucNumericalParamValue
      * EcucTextualParamValue
  * EcucQueryExpression
  * EmphasisText
  * EndToEndDescription
  * EndToEndProtectionISignalIPdu
  * EndToEndProtectionVariablePrototype
  * EngineeringObject (abstract)
    * AutosarEngineeringObject
    * BuildEngineeringObject
    * Graphic
  * Entry
  * EnumerationMappingEntry
  * EthGlobalTimeManagedCouplingPort
  * EthTSynCrcFlags
  * EthTSynSubTlvConfig
  * EventObdReadinessGroup
  * ExternalTriggeringPoint
  * FileInfoComment
  * FirewallRuleProps
  * FlexrayAbsolutelyScheduledTiming
  * FlexrayArTpChannel
  * FlexrayFifoConfiguration
  * FlexrayFifoRange
  * FlexrayTpEcu
  * FormulaExpression (abstract)
    * CompuGenericMath
    * EcucConditionFormula
    * EcucParameterDerivationFormula
    * SwSystemconstDependentFormula (abstract)
      * AttributeValueVariationPoint (abstract)
        * AbstractEnumerationValueVariationPoint (abstract)
        * AbstractNumericalVariationPoint (abstract)
          * LimitValueVariationPoint
          * NumericalValueVariationPoint
        * BooleanValueVariationPoint
        * FloatValueVariationPoint
        * IntegerValueVariationPoint
        * PositiveIntegerValueVariationPoint
        * TimeValueValueVariationPoint
        * UnlimitedIntegerValueVariationPoint
      * ConditionByFormula
    * TDEventOccurrenceExpressionFormula
    * TimingConditionFormula
  * FrameMapping
  * FramePid
  * GeneralAnnotation (abstract)
    * Annotation
    * ClientServerAnnotation
    * DelegatedPortAnnotation
    * IoHwAbstractionServerAnnotation
    * ModePortAnnotation
    * NvDataPortAnnotation
    * ParameterPortAnnotation
    * SenderReceiverAnnotation (abstract)
      * ReceiverAnnotation
      * SenderAnnotation
    * TriggerPortAnnotation
  * GenericModelReference
  * GlobalTimeCorrectionProps
  * GlobalTimeCouplingPortProps
  * HardwareConfiguration
  * HwAttributeValue
  * HwPinGroupContent
  * HwPortMapping
  * IPSecConfig
  * IPduMapping
  * ISignalMapping
  * ISignalProps
  * ImplementationElementInParameterInstanceRef
  * IncludedDataTypeSet
  * IncludedModeDeclarationGroupSet
  * IndentSample
  * IndexEntry
  * IndexedArrayElement
  * InfrastructureServices
  * InitialSdDelayConfig
  * InstantiationDataDefProps
  * InstantiationRTEEventProps (abstract)
    * InstantiationTimingEventProps
  * InternalConstrs
  * InterpolationRoutine
  * InterpolationRoutineMapping
  * InvalidationPolicy
  * Ipv4ArpProps
  * Ipv4AutoIpProps
  * Ipv4FragmentationProps
  * Ipv4Props
  * Ipv6FragmentationProps
  * Ipv6NdpProps
  * Ipv6Props
  * J1939ControllerApplicationToJ1939NmNodeMapping
  * J1939NodeName
  * J1939TpPg
  * LanguageSpecific (abstract)
    * LGraphic
  * LifeCycleInfo
  * LifeCyclePeriod
  * LinConfigurableFrame
  * LinErrorResponse
  * LinOrderedConfigurableFrame
  * LinSlaveConfig
  * MacSecCipherSuiteConfig
  * MacSecCryptoAlgoConfig
  * MacSecLocalKayProps
  * MacSecProps
  * Map
  * MappingConstraint (abstract)
    * ComponentClustering
    * ComponentSeparation
  * McDataAccessDetails
  * McFunctionDataRefSet
  * McGroupDataRefSet
  * McParameterElementGroup
  * McSupportData
  * McSwEmulationMethodSupport
  * MemorySectionLocation
  * MetaDataItem
  * MetaDataItemSet
  * MixedContentForLongName (abstract)
    * LLongName
    * SingleLanguageLongName
  * MixedContentForOverviewParagraph (abstract)
    * LOverviewParagraph
    * SlOverviewParagraph
  * MixedContentForParagraph (abstract)
    * LParagraph
    * SlParagraph
  * MixedContentForUnitNames (abstract)
    * SingleLanguageUnitNames
  * ModeAccessPoint
  * ModeDeclarationGroupPrototypeMapping
  * ModeDrivenTransmissionModeCondition
  * ModeErrorBehavior
  * ModeRequestTypeMap
  * ModeSwitchEventTriggeredActivity
  * ModeSwitchedAckRequest
  * Modification
  * MsrQueryArg
  * MsrQueryP2
  * MsrQueryProps
  * MsrQueryResultChapter
  * MsrQueryResultTopic1
  * MultiLanguageOverviewParagraph
  * MultiLanguagePlainText
  * MultidimensionalTime
  * MultilanguageLongName
  * MultiplexedPart (abstract)
    * DynamicPart
    * StaticPart
  * NetworkEndpointAddress (abstract)
    * Ipv4Configuration
    * Ipv6Configuration
    * MacMulticastConfiguration
  * NetworkSegmentIdentification
  * NmClusterCoupling (abstract)
    * CanNmClusterCoupling
    * FlexrayNmClusterCoupling
    * UdpNmClusterCoupling
  * NmCoordinator
  * NumericalOrText
  * NvBlockDataMapping
  * OrderedMaster
  * PPortComSpec (abstract)
    * ModeSwitchSenderComSpec
    * NvProvideComSpec
    * ParameterProvideComSpec
    * SenderComSpec (abstract)
      * NonqueuedSenderComSpec
      * QueuedSenderComSpec
    * ServerComSpec
  * PduMappingDefaultValue
  * PerInstanceMemorySize
  * PhysConstrs
  * PhysicalDimensionMapping
  * PlcaProps
  * PortAPIOption
  * PortDefinedArgumentValue
  * PostBuildVariantCondition
  * PostBuildVariantCriterionValue
  * PredefinedChapter
  * RPortComSpec (abstract)
    * ClientComSpec
    * ModeSwitchReceiverComSpec
    * NvRequireComSpec
    * ParameterRequireComSpec
    * ReceiverComSpec (abstract)
      * NonqueuedReceiverComSpec
      * QueuedReceiverComSpec
  * ReceptionComSpecProps
  * ReferenceBase
  * Referrable (abstract)
    * AtpDefinition (abstract)
      * EcucModuleDef
      * HwCategory
      * PostBuildVariantCriterion
      * SwSystemconst
    * BswDistinguishedPartition
    * BswModuleCallPoint (abstract)
      * BswAsynchronousServerCallPoint
      * BswAsynchronousServerCallResultPoint
      * BswDirectCallPoint
      * BswSynchronousServerCallPoint
    * BswModuleClientServerEntry
    * BswVariableAccess
    * CouplingPortTrafficClassAssignment
    * DiagnosticEnvModeElement (abstract)
      * DiagnosticEnvBswModeElement
      * DiagnosticEnvSwcModeElement
    * EthernetPriorityRegeneration
    * ExclusiveAreaNestingOrder
    * HwDescriptionEntity (abstract)
      * HwElement
      * HwType
    * ImplementationProps (abstract)
      * BswSchedulerNamePrefix
      * ExecutableEntityActivationReason
      * SectionNamePrefix
      * SymbolProps
      * SymbolicNameProps
    * LinSlaveConfigIdent
    * MultilanguageReferrable (abstract)
      * Caption
      * DocumentationContext
      * Identifiable (abstract)
        * <<atpPrototype>> PduToFrameMapping
        * AbstractDoIpLogicAddressProps (abstract)
          * DoIpLogicTargetAddressProps
          * DoIpLogicTesterAddressProps
        * AbstractEvent (abstract)
          * BswEvent (abstract)
            * BswInterruptEvent
            * BswOperationInvokedEvent
            * BswScheduleEvent (abstract)
              * BswAsynchronousServerCallReturnsEvent
              * BswBackgroundEvent
              * BswDataReceivedEvent
              * BswExternalTriggerOccurredEvent
              * BswInternalTriggerOccurredEvent
              * BswModeManagerErrorEvent
              * BswModeSwitchEvent
              * BswModeSwitchedAckEvent
              * BswOsTaskExecutionEvent
              * BswTimingEvent
        * AbstractServiceInstance (abstract)
          * ConsumedServiceInstance
          * DdsCpServiceInstance (abstract)
            * DdsCpConsumedServiceInstance
            * DdsCpProvidedServiceInstance
          * ProvidedServiceInstance
        * AppOsTaskProxyToEcuTaskProxyMapping
        * ApplicationEndpoint
        * ApplicationError
        * ApplicationPartitionToEcuPartitionMapping
        * AtpBlueprint (abstract)
        * AtpBlueprintable (abstract)
          * AclObjectSet
          * AclOperation
          * AclPermission
          * AclRole
          * AliasNameSet
          * BswEntryRelationshipSet
          * BswModuleEntry
          * BuildActionEntity (abstract)
            * BuildAction
          * BuildActionEnvironment
          * BuildActionManifest
          * CompuMethod
          * ConsistencyNeeds
          * DataConstr
          * DataTypeMappingSet
          * EcucDefinitionCollection
          * EcucDestinationUriDefSet
          * FlatMap
          * LifeCycleState
          * LifeCycleStateDefinitionGroup
          * PortInterfaceMapping (abstract)
            * ClientServerInterfaceMapping
            * ModeInterfaceMapping
            * TriggerInterfaceMapping
            * VariableAndParameterInterfaceMapping
          * PortInterfaceMappingSet
          * SwAddrMethod
          * VfbTiming
        * AtpClassifier (abstract)
          * AtpType (abstract)
            * AtomicSwComponentType (abstract)
              * ApplicationSwComponentType
              * ComplexDeviceDriverSwComponentType
              * EcuAbstractionSwComponentType
              * NvBlockSwComponentType
              * SensorActuatorSwComponentType
              * ServiceProxySwComponentType
              * ServiceSwComponentType
            * AutosarDataType (abstract)
              * AbstractImplementationDataType (abstract)
                * ImplementationDataType
              * ApplicationDataType (abstract)
                * ApplicationCompositeDataType (abstract)
                  * ApplicationArrayDataType
                  * ApplicationRecordDataType
                * ApplicationPrimitiveDataType
            * ClientServerInterface
            * CompositionSwComponentType
            * DataInterface (abstract)
            * ModeDeclarationGroup
            * ModeDeclarationMappingSet
            * ModeSwitchInterface
            * NvDataInterface
            * ParameterInterface
            * ParameterSwComponentType
            * PortInterface (abstract)
            * SenderReceiverInterface
            * SwComponentType (abstract)
            * TriggerInterface
        * AtpFeature (abstract)
          * AtpPrototype (abstract)
            * AbstractProvidedPortPrototype (abstract)
              * PPortPrototype
            * AbstractRequiredPortPrototype (abstract)
              * PRPortPrototype
              * RPortPrototype
            * DataPrototype (abstract)
              * ApplicationCompositeElementDataPrototype (abstract)
                * ApplicationArrayElement
                * ApplicationRecordElement
              * AutosarDataPrototype (abstract)
                * ArgumentDataPrototype
                * ParameterDataPrototype
                * VariableDataPrototype
            * ModeDeclarationGroupPrototype
            * PortPrototype (abstract)
            * RootSwCompositionPrototype
            * SwComponentPrototype
          * AtpStructureElement (abstract)
            * AbstractAccessPoint (abstract)
              * AsynchronousServerCallPoint
              * AsynchronousServerCallResultPoint
              * InternalTriggeringPoint
              * ModeSwitchPoint
              * ParameterAccess
              * ServerCallPoint (abstract)
              * SynchronousServerCallPoint
              * VariableAccess
            * AbstractImplementationDataTypeElement (abstract)
              * ImplementationDataTypeElement
            * AssemblySwConnector
            * AsynchronousServerCallReturnsEvent
            * BackgroundEvent
            * BswModuleDescription
            * BulkNvDataDescriptor
            * ClientServerOperation
            * DataPrototypeGroup
            * DataReceiveErrorEvent
            * DataReceivedEvent
            * DataSendCompletedEvent
            * DataWriteCompletedEvent
            * DelegationSwConnector
            * ExternalTriggerOccurredEvent
            * IdentCaption (abstract)
              * BswServiceDependencyIdent
              * ExternalTriggeringPointIdent
              * ModeAccessPointIdent
            * InitEvent
            * InternalBehavior (abstract)
              * BswInternalBehavior
              * SwcInternalBehavior
            * InternalTriggerOccurredEvent
            * ModeDeclaration
            * ModeDeclarationMapping
            * ModeSwitchedAckEvent
            * ModeTransition
            * NvBlockDescriptor
            * OperationInvokedEvent
            * OsTaskExecutionEvent
            * PassThroughSwConnector
            * PerInstanceMemory
            * PortGroup
            * PortPrototypeBlueprint
            * RTEEvent (abstract)
            * RunnableEntityGroup
            * SwConnector (abstract)
            * SwcBswMapping
            * SwcModeManagerErrorEvent
            * SwcModeSwitchEvent
            * SwcServiceDependency
            * System
            * TimingEvent
            * TransformerHardErrorEvent
            * Trigger
        * AutosarOperationArgumentInstance
        * AutosarVariableInstance
        * BinaryManifestAddressableObject (abstract)
          * BinaryManifestItem
          * BinaryManifestMetaDataField
        * BinaryManifestItemDefinition
        * BinaryManifestResource (abstract)
          * BinaryManifestProvideResource
          * BinaryManifestRequireResource
        * BinaryManifestResourceDefinition
        * BswInternalTriggeringPoint
        * BswModuleDependency
        * CanTpAddress
        * CanTpChannel
        * CanTpNode
        * ClientIdDefinition
        * Code
        * CollectableElement (abstract)
          * ARPackage
          * PackageableElement (abstract)
            * ARElement (abstract)
              * ApplicationPartition
              * BaseType (abstract)
                * SwBaseType
              * BlueprintMappingSet
              * BswCompositionTiming
              * BswModuleTiming
              * CalibrationParameterValueSet
              * ClientIdDefinitionSet
              * Collection
              * ConstantSpecification
              * ConstantSpecificationMappingSet
              * CpSoftwareCluster
              * CpSoftwareClusterBinaryManifestDescriptor
              * CpSoftwareClusterMappingSet
              * CpSoftwareClusterResourcePool
              * CryptoEllipticCurveProps
              * CryptoServiceCertificate
              * CryptoServiceKey
              * CryptoServicePrimitive
              * CryptoServiceQueue
              * CryptoSignatureScheme
              * DataTransformationSet
              * DdsCpConfig
              * DiagnosticCommonElement (abstract)
                * DiagnosticAbstractAliasEvent (abstract)
                  * DiagnosticFimAliasEvent
                  * DiagnosticFimAliasEventGroup
                * DiagnosticAbstractDataIdentifier (abstract)
                  * DiagnosticDataIdentifier
                  * DiagnosticDynamicDataIdentifier
                * DiagnosticAccessPermission
                * DiagnosticAging
                * DiagnosticAuthRole
                * DiagnosticCondition (abstract)
                  * DiagnosticEnableCondition
                  * DiagnosticStorageCondition
                * DiagnosticConditionGroup (abstract)
                  * DiagnosticEnableConditionGroup
                  * DiagnosticStorageConditionGroup
                * DiagnosticDataIdentifierSet
                * DiagnosticEcuInstanceProps
                * DiagnosticEnvironmentalCondition
                * DiagnosticEvent
                * DiagnosticExtendedDataRecord
                * DiagnosticFimEventGroup
                * DiagnosticFreezeFrame
                * DiagnosticFunctionIdentifier
                * DiagnosticFunctionIdentifierInhibit
                * DiagnosticIndicator
                * DiagnosticInfoType
                * DiagnosticIumpr
                * DiagnosticIumprDenominatorGroup
                * DiagnosticIumprGroup
                * DiagnosticJ1939ExpandedFreezeFrame
                * DiagnosticJ1939FreezeFrame
                * DiagnosticJ1939Node
                * DiagnosticJ1939Spn
                * DiagnosticMapping (abstract)
                  * CpSwClusterResourceToDiagDataElemMapping
                  * CpSwClusterResourceToDiagFunctionIdMapping
                  * CpSwClusterToDiagEventMapping
                  * CpSwClusterToDiagRoutineSubfunctionMapping
                  * DiagnosticAuthTransmitCertificateMapping
                  * DiagnosticDemProvidedDataMapping
                  * DiagnosticEnableConditionPortMapping
                  * DiagnosticEventPortMapping
                  * DiagnosticEventToDebounceAlgorithmMapping
                  * DiagnosticEventToEnableConditionGroupMapping
                  * DiagnosticEventToOperationCycleMapping
                  * DiagnosticEventToSecurityEventMapping
                  * DiagnosticEventToStorageConditionGroupMapping
                  * DiagnosticEventToTroubleCodeJ1939Mapping
                  * DiagnosticEventToTroubleCodeUdsMapping
                  * DiagnosticFimAliasEventGroupMapping
                  * DiagnosticFimAliasEventMapping
                  * DiagnosticFimFunctionMapping
                  * DiagnosticInhibitSourceEventMapping
                  * DiagnosticIumprToFunctionIdentifierMapping
                  * DiagnosticJ1939SpnMapping
                  * DiagnosticJ1939SwMapping
                  * DiagnosticMasterToSlaveEventMapping
                  * DiagnosticOperationCyclePortMapping
                  * DiagnosticSecureCodingMapping
                  * DiagnosticSecurityEventReportingModeMapping
                  * DiagnosticServiceDataMapping
                  * DiagnosticServiceSwMapping
                  * DiagnosticStorageConditionPortMapping
                  * DiagnosticSwMapping (abstract)
                  * DiagnosticTroubleCodeUdsToTroubleCodeObdMapping
                * DiagnosticMeasurementIdentifier
                * DiagnosticMemoryDestination (abstract)
                * DiagnosticMemoryDestinationPrimary
                * DiagnosticMemoryDestinationUserDefined
                * DiagnosticMemoryIdentifier
                * DiagnosticOperationCycle
                * DiagnosticParameterIdentifier
                * DiagnosticPowertrainFreezeFrame
                * DiagnosticProtocol
                * DiagnosticReadMemoryByAddress
                * DiagnosticRequestDownload
                * DiagnosticRequestUpload
                * DiagnosticRoutine
                * DiagnosticSecurityLevel
                * DiagnosticServiceClass (abstract)
                  * DiagnosticAuthenticationClass
                  * DiagnosticClearDiagnosticInformationClass
                  * DiagnosticClearResetEmissionRelatedInfoClass
                  * DiagnosticComControlClass
                  * DiagnosticControlDTCSettingClass
                  * DiagnosticCustomServiceClass
                  * DiagnosticDataTransferClass
                  * DiagnosticDynamicallyDefineDataIdentifierClass
                  * DiagnosticEcuResetClass
                  * DiagnosticIoControlClass
                  * DiagnosticReadDTCInformationClass
                  * DiagnosticReadDataByIdentifierClass
                  * DiagnosticReadDataByPeriodicIDClass
                  * DiagnosticReadMemoryByAddressClass
                  * DiagnosticReadScalingDataByIdentifierClass
                  * DiagnosticRequestControlOfOnBoardDeviceClass
                  * DiagnosticRequestCurrentPowertrainDataClass
                  * DiagnosticRequestDownloadClass
                  * DiagnosticRequestEmissionRelatedDTCClass
                  * DiagnosticRequestEmissionRelatedDTCPermanentStatusClass
                  * DiagnosticRequestFileTransferClass
                  * DiagnosticRequestOnBoardMonitoringTestResultsClass
                  * DiagnosticRequestPowertrainFreezeFrameDataClass
                  * DiagnosticRequestUploadClass
                  * DiagnosticRequestVehicleInfoClass
                  * DiagnosticResponseOnEventClass
                  * DiagnosticRoutineControlClass
                  * DiagnosticSecurityAccessClass
                  * DiagnosticSessionControlClass
                  * DiagnosticTransferExitClass
                  * DiagnosticWriteDataByIdentifierClass
                  * DiagnosticWriteMemoryByAddressClass
                * DiagnosticServiceInstance (abstract)
                  * DiagnosticAuthentication (abstract)
                    * DiagnosticAuthTransmitCertificate
                    * DiagnosticAuthenticationConfiguration
                    * DiagnosticDeAuthentication
                    * DiagnosticProofOfOwnership
                    * DiagnosticVerifyCertificateBidirectional
                    * DiagnosticVerifyCertificateUnidirectional
                  * DiagnosticClearDiagnosticInformation
                  * DiagnosticClearResetEmissionRelatedInfo
                  * DiagnosticComControl
                  * DiagnosticControlDTCSetting
                  * DiagnosticCustomServiceInstance
                  * DiagnosticDataByIdentifier (abstract)
                    * DiagnosticReadDataByIdentifier
                    * DiagnosticReadScalingDataByIdentifier
                    * DiagnosticWriteDataByIdentifier
                  * DiagnosticDynamicallyDefineDataIdentifier
                  * DiagnosticEcuReset
                  * DiagnosticIOControl
                  * DiagnosticMemoryByAddress (abstract)
                    * DiagnosticDataTransfer
                    * DiagnosticMemoryAddressableRangeAccess (abstract)
                    * DiagnosticTransferExit
                  * DiagnosticReadDTCInformation
                  * DiagnosticReadDataByPeriodicID
                  * DiagnosticRequestControlOfOnBoardDevice
                  * DiagnosticRequestCurrentPowertrainData
                  * DiagnosticRequestEmissionRelatedDTC
                  * DiagnosticRequestEmissionRelatedDTCPermanentStatus
                  * DiagnosticRequestFileTransfer
                  * DiagnosticRequestOnBoardMonitoringTestResults
                  * DiagnosticRequestPowertrainFreezeFrameData
                  * DiagnosticRequestVehicleInfo
                  * DiagnosticResponseOnEvent
                  * DiagnosticRoutineControl
                  * DiagnosticSecurityAccess
                  * DiagnosticSessionControl
                * DiagnosticServiceTable
                * DiagnosticSession
                * DiagnosticTestResult
                * DiagnosticTestRoutineIdentifier
                * DiagnosticTroubleCode (abstract)
                  * DiagnosticTroubleCodeJ1939
                  * DiagnosticTroubleCodeObd
                  * DiagnosticTroubleCodeUds
                * DiagnosticTroubleCodeGroup
                * DiagnosticTroubleCodeProps
                * DiagnosticWriteMemoryByAddress
              * DiagnosticConnection
              * DiagnosticContributionSet
              * DltContext
              * DltEcu
              * Documentation
              * E2EProfileCompatibilityProps
              * EcuTiming
              * EcucModuleConfigurationValues
              * EcucValueCollection
              * EndToEndProtectionSet
              * EthIpProps
              * EthTcpIpIcmpProps
              * EthTcpIpProps
              * EvaluatedVariantSet
              * FMFeature
              * FMFeatureModel
              * FirewallRule
              * GeneralPurposeConnection
              * IEEE1722TpConnection (abstract)
                * IEEE1722TpAcfConnection
                * IEEE1722TpAvConnection (abstract)
                  * IEEE1722TpAafConnection
                  * IEEE1722TpCrfConnection
                  * IEEE1722TpIidcConnection
                  * IEEE1722TpRvfConnection
              * IPSecConfigProps
              * IPv6ExtHeaderFilterSet
              * Implementation (abstract)
                * BswImplementation
                * SwcImplementation
              * InterpolationRoutineMappingSet
              * J1939ControllerApplication
              * LifeCycleInfoSet
              * MacSecGlobalKayProps
              * MacSecParticipantSet
              * McFunction
              * McGroup
              * OsTaskProxy
              * PhysicalDimension
              * PhysicalDimensionMappingSet
              * PostBuildVariantCriterionValueSet
              * PredefinedVariant
              * RapidPrototypingScenario
              * SdgDef
              * SecurityEventDefinition
              * SignalServiceTranslationPropsSet
              * SomeipSdClientEventGroupTimingConfig
              * SomeipSdClientServiceInstanceConfig
              * SomeipSdServerEventGroupTimingConfig
              * SomeipSdServerServiceInstanceConfig
              * StateDependentFirewall
              * SwAxisType
              * SwRecordLayout
              * SwSystemconstantValueSet
              * SwcTiming
              * SystemSignal
              * SystemSignalGroup
              * SystemTiming
              * TDCpSoftwareClusterMappingSet
              * TcpOptionFilterSet
              * TimingExtension (abstract)
              * TlvDataIdDefinitionSet
              * TransformationPropsSet
              * Unit
              * UnitGroup
              * ViewMapSet
            * EnumerationMappingTable
            * FibexElement (abstract)
              * BusMirrorChannelMapping (abstract)
                * BusMirrorChannelMappingCan
                * BusMirrorChannelMappingFlexray
                * BusMirrorChannelMappingIp
                * BusMirrorChannelMappingUserDefined
              * CanTpConfig
              * CommunicationCluster (abstract)
                * AbstractCanCluster (abstract)
                  * CanCluster
                  * J1939Cluster
                  * TtcanCluster
                * EthernetCluster
                * FlexrayCluster
                * LinCluster
                * UserDefinedCluster
              * ConsumedProvidedServiceInstanceGroup
              * CouplingElement
              * DoIpTpConfig
              * EcuInstance
              * EthTpConfig
              * EthernetWakeupSleepOnDatalineConfigSet
              * FlexrayArTpConfig
              * FlexrayTpConfig
              * Frame (abstract)
                * AbstractEthernetFrame (abstract)
                  * GenericEthernetFrame
                  * Ieee1722TpEthernetFrame
                  * UserDefinedEthernetFrame
                * CanFrame
                * FlexrayFrame
                * LinFrame (abstract)
                  * LinEventTriggeredFrame
                  * LinSporadicFrame
                  * LinUnconditionalFrame
              * Gateway
              * GeneralPurposePdu
              * GlobalTimeDomain
              * IEEE1722TpConfig
              * IPdu (abstract)
                * ContainerIPdu
                * DcmIPdu
                * GeneralPurposeIPdu
                * ISignalIPdu
                * J1939DcmIPdu
                * MultiplexedIPdu
                * NPdu
                * SecuredIPdu
                * UserDefinedIPdu
              * ISignal
              * ISignalGroup
              * ISignalIPduGroup
              * J1939TpConfig
              * LinTpConfig
              * NmConfig
              * NmPdu
              * Pdu (abstract)
              * PdurIPduGroup
              * SecureCommunicationPropsSet
              * ServiceInstanceCollectionSet
              * SoAdRoutingGroup
              * SocketConnectionIpduIdentifierSet
              * SomeipTpConfig
              * TpConfig (abstract)
              * UserDefinedPdu
        * ComManagementMapping
        * CommConnectorPort (abstract)
          * FramePort
          * IPduPort
        * CommunicationConnector (abstract)
          * AbstractCanCommunicationConnector (abstract)
            * CanCommunicationConnector
            * TtcanCommunicationConnector
          * EthernetCommunicationConnector
          * FlexrayCommunicationConnector
          * LinCommunicationConnector
          * UserDefinedCommunicationConnector
        * CommunicationController (abstract)
          * AbstractCanCommunicationController (abstract)
            * CanCommunicationController
            * TtcanCommunicationController
          * EthernetCommunicationController
          * FlexrayCommunicationController
          * LinCommunicationController (abstract)
            * LinMaster
            * LinSlave
          * UserDefinedCommunicationController
        * Compiler
        * ConsumedEventGroup
        * CouplingElementAbstractDetails (abstract)
          * CouplingElementSwitchDetails
        * CouplingPort
        * CouplingPortAsynchronousTrafficShaper
        * CouplingPortCreditBasedShaper
        * CouplingPortStructuralElement (abstract)
          * CouplingPortFifo
          * CouplingPortScheduler
          * CouplingPortShaper
        * CpSoftwareClusterResource (abstract)
          * CpSoftwareClusterCommunicationResource
          * CpSoftwareClusterServiceResource
        * CpSoftwareClusterResourceToApplicationPartitionMapping
        * CpSoftwareClusterToApplicationPartitionMapping
        * CpSoftwareClusterToEcuInstanceMapping
        * CpSoftwareClusterToResourceMapping
        * CryptoServiceMapping (abstract)
          * SecOcCryptoServiceMapping
          * TlsCryptoServiceMapping
        * DataTransformation
        * DdsCpDomain
        * DdsCpPartition
        * DdsCpQosProfile
        * DdsCpTopic
        * DependencyOnArtifact
        * DiagEventDebounceAlgorithm (abstract)
          * DiagEventDebounceCounterBased
          * DiagEventDebounceMonitorInternal
          * DiagEventDebounceTimeBased
        * DiagnosticAuthTransmitCertificateEvaluation
        * DiagnosticConnectedIndicator
        * DiagnosticDataElement
        * DiagnosticDebounceAlgorithmProps
        * DiagnosticFunctionInhibitSource
        * DiagnosticParameterElement
        * DiagnosticRoutineSubfunction (abstract)
          * DiagnosticRequestRoutineResults
          * DiagnosticStartRoutine
          * DiagnosticStopRoutine
        * DltApplication
        * DltArgument
        * DltLogChannel
        * DltMessage
        * DoIpInterface
        * DoIpLogicAddress
        * DoIpRoutingActivation
        * ECUMapping
        * EOCExecutableEntityRefAbstract (abstract)
          * EOCEventRef
          * EOCExecutableEntityRef
          * EOCExecutableEntityRefGroup
        * EcuPartition
        * EcucContainerValue
        * EcucDefinitionElement (abstract)
          * EcucCommonAttributes (abstract)
            * EcucAbstractReferenceDef (abstract)
              * EcucAbstractExternalReferenceDef (abstract)
                * EcucForeignReferenceDef
                * EcucInstanceReferenceDef
              * EcucAbstractInternalReferenceDef (abstract)
                * EcucChoiceReferenceDef
                * EcucReferenceDef
                * EcucUriReferenceDef
            * EcucParameterDef (abstract)
              * EcucAbstractStringParamDef (abstract)
                * EcucFunctionNameDef
                * EcucLinkerSymbolDef
                * EcucMultilineStringParamDef
                * EcucStringParamDef
              * EcucAddInfoParamDef
              * EcucBooleanParamDef
              * EcucEnumerationParamDef
              * EcucFloatParamDef
              * EcucIntegerParamDef
          * EcucContainerDef (abstract)
            * EcucChoiceContainerDef
            * EcucParamConfContainerDef
        * EcucDestinationUriDef
        * EcucEnumerationLiteralDef
        * EcucQuery
        * EcucValidationCondition
        * EndToEndProtection
        * EthernetWakeupSleepOnDatalineConfig
        * EventHandler
        * ExclusiveArea
        * ExecutableEntity (abstract)
          * BswModuleEntity (abstract)
            * BswCalledEntity
            * BswInterruptEntity
            * BswSchedulableEntity
          * RunnableEntity
        * ExecutionTime (abstract)
          * AnalyzedExecutionTime
          * MeasuredExecutionTime
          * RoughEstimateOfExecutionTime
          * SimulatedExecutionTime
        * FlatInstanceDescriptor
        * FlexrayArTpNode
        * FlexrayTpConnectionControl
        * FlexrayTpNode
        * FlexrayTpPduPool
        * FrameTriggering (abstract)
          * CanFrameTriggering
          * EthernetFrameTriggering
          * FlexrayFrameTriggering
          * LinFrameTriggering
        * GlobalTimeCanSlave
        * GlobalTimeEthSlave
        * GlobalTimeFrSlave
        * GlobalTimeGateway
        * GlobalTimeMaster (abstract)
          * GlobalTimeCanMaster
          * GlobalTimeEthMaster
          * GlobalTimeFrMaster
          * UserDefinedGlobalTimeMaster
        * HeapUsage (abstract)
          * MeasuredHeapUsage
          * RoughEstimateHeapUsage
          * WorstCaseHeapUsage
        * HwAttributeDef
        * HwAttributeLiteralDef
        * HwPin
        * HwPinGroup
        * IEEE1722TpAcfBus (abstract)
          * IEEE1722TpAcfCan
          * IEEE1722TpAcfLin
        * IEEE1722TpAcfBusPart (abstract)
          * IEEE1722TpAcfCanPart
          * IEEE1722TpAcfLinPart
        * IPSecRule
        * IPv6ExtHeaderFilterList
        * ISignalToIPduMapping
        * ISignalTriggering
        * J1939SharedAddressCluster
        * J1939TpNode
        * Keyword
        * LinScheduleTable
        * LinTpNode
        * Linker
        * MacMulticastGroup
        * MacSecKayParticipant
        * McDataInstance
        * MemorySection
        * NetworkEndpoint
        * NmCluster (abstract)
          * CanNmCluster
          * FlexrayNmCluster
          * J1939NmCluster
          * UdpNmCluster
        * NmEcu
        * NmNode (abstract)
          * CanNmNode
          * FlexrayNmNode
          * J1939NmNode
          * UdpNmNode
        * PduActivationRoutingGroup
        * PduTriggering
        * PhysicalChannel (abstract)
          * AbstractCanPhysicalChannel (abstract)
            * CanPhysicalChannel
            * TtcanPhysicalChannel
          * EthernetPhysicalChannel
          * FlexrayPhysicalChannel
          * LinPhysicalChannel
          * UserDefinedPhysicalChannel
        * PortElementToCommunicationResourceMapping
        * ResourceConsumption
        * RptComponent
        * RptContainer
        * RptExecutableEntity
        * RptExecutableEntityEvent
        * RptExecutionContext
        * RptProfile
        * RptServicePoint
        * RteEventInCompositionSeparation
        * RteEventInCompositionToOsTaskProxyMapping
        * RteEventInSystemSeparation
        * RteEventInSystemToOsTaskProxyMapping
        * SdgAbstractPrimitiveAttribute (abstract)
        * SdgAggregationWithVariation
        * SdgAttribute (abstract)
          * SdgAbstractForeignReference (abstract)
          * SdgReference
        * SdgForeignReference
        * SdgForeignReferenceWithVariation
        * SdgPrimitiveAttribute
        * SecureCommunicationAuthenticationProps
        * SecureCommunicationFreshnessProps
        * SecurityEventContextProps
        * ServiceNeeds (abstract)
          * BswMgrNeeds
          * ComMgrUserNeeds
          * CryptoKeyManagementNeeds
          * CryptoServiceJobNeeds
          * CryptoServiceNeeds
          * DiagnosticCapabilityElement (abstract)
            * DiagnosticCommunicationManagerNeeds
            * DiagnosticComponentNeeds
            * DiagnosticControlNeeds
            * DiagnosticEnableConditionNeeds
            * DiagnosticEventInfoNeeds
            * DiagnosticEventManagerNeeds
            * DiagnosticEventNeeds
            * DiagnosticIoControlNeeds
            * DiagnosticOperationCycleNeeds
            * DiagnosticRequestFileTransferNeeds
            * DiagnosticRoutineNeeds
            * DiagnosticStorageConditionNeeds
            * DiagnosticUploadDownloadNeeds
            * DiagnosticValueNeeds
            * DiagnosticsCommunicationSecurityNeeds
            * DtcStatusChangeNotificationNeeds
            * ObdControlServiceNeeds
            * ObdInfoServiceNeeds
            * ObdMonitorServiceNeeds
            * ObdPidServiceNeeds
            * ObdRatioDenominatorNeeds
            * ObdRatioServiceNeeds
            * WarningIndicatorRequestedBitNeeds
          * DltUserNeeds
          * DoIpServiceNeeds (abstract)
            * DoIpActivationLineNeeds
            * DoIpGidNeeds
            * DoIpGidSynchronizationNeeds
            * DoIpPowerModeStatusNeeds
            * DoIpRoutingActivationAuthenticationNeeds
            * DoIpRoutingActivationConfirmationNeeds
            * FurtherActionByteNeeds
          * EcuStateMgrUserNeeds
          * ErrorTracerNeeds
          * FunctionInhibitionAvailabilityNeeds
          * FunctionInhibitionNeeds
          * GlobalSupervisionNeeds
          * HardwareTestNeeds
          * IdsMgrCustomTimestampNeeds
          * IdsMgrNeeds
          * IndicatorStatusNeeds
          * J1939DcmDm19Support
          * J1939RmIncomingRequestServiceNeeds
          * J1939RmOutgoingRequestServiceNeeds
          * NvBlockNeeds
          * SecureOnBoardCommunicationNeeds
          * SupervisedEntityCheckpointNeeds
          * SupervisedEntityNeeds
          * SyncTimeBaseMgrUserNeeds
          * V2xDataManagerNeeds
          * V2xFacUserNeeds
          * V2xMUserNeeds
          * VendorSpecificServiceNeeds
        * SignalServiceTranslationElementProps
        * SignalServiceTranslationEventProps
        * SignalServiceTranslationProps
        * SocketAddress
        * SomeipTpChannel
        * StackUsage (abstract)
          * MeasuredStackUsage
          * RoughEstimateStackUsage
          * WorstCaseStackUsage
        * StaticSocketConnection
        * SwGenericAxisParamType
        * SwServiceArg
        * SwcToApplicationPartitionMapping
        * SwcToEcuMapping
        * SwcToImplMapping
        * SwitchAsynchronousTrafficShaperGroupEntry
        * SwitchFlowMeteringEntry
        * SwitchStreamFilterActionDestPortModification
        * SwitchStreamFilterEntry
        * SwitchStreamFilterRule
        * SwitchStreamGateEntry
        * SwitchStreamIdentification
        * SystemMapping
        * SystemSignalGroupToCommunicationResourceMapping
        * SystemSignalToCommunicationResourceMapping
        * TDCpSoftwareClusterMapping
        * TDCpSoftwareClusterResourceMapping
        * TcpOptionFilterList
        * TimingClockSyncAccuracy
        * TimingCondition
        * TimingDescription (abstract)
          * TimingDescriptionEvent (abstract)
            * TDEventBsw (abstract)
              * TDEventBswModeDeclaration
              * TDEventBswModule
            * TDEventBswInternalBehavior
            * TDEventCom (abstract)
              * TDEventCycleStart (abstract)
                * TDEventFrClusterCycleStart
                * TDEventTTCanCycleStart
              * TDEventFrame
              * TDEventFrameEthernet
              * TDEventIPdu
              * TDEventISignal
            * TDEventComplex
            * TDEventSLLET (abstract)
              * TDEventSLLETPort
            * TDEventSwc (abstract)
              * TDEventSwcInternalBehavior
              * TDEventSwcInternalBehaviorReference
            * TDEventVfb (abstract)
              * TDEventVfbPort (abstract)
                * TDEventModeDeclaration
                * TDEventOperation
                * TDEventTrigger
                * TDEventVariableDataPrototype
              * TDEventVfbReference
          * TimingDescriptionEventChain
        * TimingExtensionResource
        * TimingModeInstance
        * TlsCryptoCipherSuite
        * TlsCryptoCipherSuiteProps
        * TpAddress
        * TracedFailure (abstract)
          * DevelopmentError
          * RuntimeError
          * TransientFault
        * TransformationProps (abstract)
          * SOMEIPTransformationProps
          * UserDefinedTransformationProps
        * TransformationTechnology
        * UserDefinedGlobalTimeSlave
        * VariationPointProxy
        * ViewMap
        * VlanConfig
        * WaitPoint
      * SdgCaption
      * Traceable (abstract)
        * TimingConstraint (abstract)
          * AgeConstraint
          * EventTriggeringConstraint (abstract)
            * ArbitraryEventTriggering
            * BurstPatternEventTriggering
            * ConcretePatternEventTriggering
            * PeriodicEventTriggering
            * SporadicEventTriggering
          * ExecutionOrderConstraint
          * ExecutionTimeConstraint
          * LatencyTimingConstraint
          * OffsetTimingConstraint
          * SynchronizationPointConstraint
          * SynchronizationTimingConstraint
    * PncMappingIdent
    * SingleLanguageReferrable (abstract)
      * Std
      * Xdoc
      * Xfile
      * XrefTarget
    * SoConIPduIdentifier
    * TimeSyncServerConfiguration
    * TpConnectionIdent
  * RequestResponseDelay
  * RoleBasedBswModuleEntryAssignment
  * RoleBasedDataAssignment
  * RoleBasedDataTypeAssignment
  * RoleBasedMcDataAssignment
  * RoleBasedPortAssignment
  * RoleBasedResourceDependency
  * RptExecutableEntityProperties
  * RptHook
  * RptImplPolicy
  * RptSupportData
  * RptSwPrototypingAccess
  * RtePluginProps
  * RuleArguments
  * RuleBasedAxisCont
  * RuleBasedValueCont
  * RuleBasedValueSpecification
  * RunnableEntityArgument
  * RxIdentifierRange
  * ScaleConstr
  * ScheduleTableEntry (abstract)
    * ApplicationEntry
    * FreeFormatEntry (abstract)
      * FreeFormat
    * LinConfigurationEntry (abstract)
      * AssignFrameId
      * AssignFrameIdRange
      * AssignNad
      * ConditionalChangeNad
      * DataDumpEntry
      * SaveConfigurationEntry
      * UnassignFrameId
  * Sd
  * Sdf
  * Sdg
  * SdgContents
  * SdgElementWithGid (abstract)
    * SdgClass
  * SecureCommunicationProps
  * SegmentPosition
  * SenderRecArrayElementMapping
  * SenderRecCompositeTypeMapping (abstract)
    * SenderRecArrayTypeMapping
    * SenderRecRecordTypeMapping
  * SenderRecRecordElementMapping
  * ServiceDependency (abstract)
    * BswServiceDependency
  * ShortNameFragment
  * SignalPathConstraint (abstract)
    * CommonSignalPath
    * ForbiddenSignalPath
    * PermissibleSignalPath
    * SeparateSignalPath
  * SoAdConfig
  * SoftwareContext
  * SomeipServiceVersion
  * SomeipTpConnection
  * StreamFilterIEEE1722Tp
  * StreamFilterIpv4Address
  * StreamFilterIpv6Address
  * StreamFilterMACAddress
  * StreamFilterPortRange
  * StreamFilterRuleDataLinkLayer
  * StreamFilterRuleIpTp
  * SubElementMapping
  * SubElementRef (abstract)
    * ApplicationCompositeDataTypeSubElementRef
    * ImplementationDataTypeSubElementRef
  * SwAxisCont
  * SwAxisGeneric
  * SwBitRepresentation
  * SwCalprmAxis
  * SwCalprmAxisSet
  * SwCalprmAxisTypeProps (abstract)
    * SwAxisGrouped
    * SwAxisIndividual
  * SwCalprmRefProxy
  * SwComponentDocumentation
  * SwComponentPrototypeAssignment
  * SwDataDefProps
  * SwDataDependency
  * SwDataDependencyArgs
  * SwGenericAxisParam
  * SwPointerTargetProps
  * SwRecordLayoutGroup
  * SwRecordLayoutGroupContent
  * SwRecordLayoutV
  * SwSystemconstValue
  * SwTextProps
  * SwValueCont
  * SwValues
  * SwVariableRefProxy
  * SwcBswRunnableMapping
  * SwcBswSynchronizedModeGroupPrototype
  * SwcBswSynchronizedTrigger
  * SwcExclusiveAreaPolicy
  * SwcSupportedFeature (abstract)
    * CommunicationBufferLocking
  * SwcToSwcOperationArguments
  * SwcToSwcSignal
  * TDEventOccurrenceExpression
  * TDHeaderIdRange
  * TagWithOptionalValue
  * TargetIPduRef
  * Tbody
  * TcpIpIcmpv4Props
  * TcpIpIcmpv6Props
  * TcpProps
  * TextTableMapping
  * TextTableValuePair
  * Tgroup
  * TimeRangeType
  * TimeSyncClientConfiguration
  * TimeSynchronization
  * TlsPskIdentity
  * TlvDataIdDefinition
  * TopicContent
  * TopicContentOrMsrQuery
  * TopicOrMsrQuery
  * TpConnection (abstract)
    * CanTpConnection
    * DoIpTpConnection
    * EthTpConnection
    * FlexrayArTpConnection
    * FlexrayTpConnection
    * J1939TpConnection
    * LinTpConnection
  * TpPort
  * TransmissionAcknowledgementRequest
  * TransmissionComSpecProps
  * TransmissionModeCondition
  * TransmissionModeDeclaration
  * TransmissionModeTiming
  * TransportProtocolConfiguration (abstract)
    * GenericTp
    * HttpTp
    * Ieee1722Tp
    * RtpTp
    * TcpUdpConfig (abstract)
      * TcpTp
      * UdpTp
  * TriggerIPduSendCondition
  * TriggerMapping
  * Tt
  * TtcanAbsolutelyScheduledTiming
  * UdpProps
  * ValueGroup
  * ValueList
  * ValueSpecification (abstract)
    * AbstractRuleBasedValueSpecification (abstract)
      * CompositeRuleBasedValueSpecification
      * NumericalRuleBasedValueSpecification
    * ApplicationValueSpecification
    * CompositeValueSpecification (abstract)
      * ArrayValueSpecification
      * RecordValueSpecification
    * ConstantReference
    * NotAvailableValueSpecification
    * NumericalValueSpecification
    * ReferenceValueSpecification
    * TextValueSpecification
  * VariationPoint
  * VlanMembership
  * WhitespaceControlled (abstract)
    * MixedContentForPlainText (abstract)
      * LPlainText
    * MixedContentForVerbatim (abstract)
      * LVerbatim
  * Xref
