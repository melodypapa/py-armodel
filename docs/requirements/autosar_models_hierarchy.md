## Class Hierarchy

* ARObject (abstract)
  * AUTOSAR
  * AbstractCanCommunicationControllerAttributes (abstract)
    * CanControllerConfiguration
    * CanControllerConfigurationRequirements
  * AbstractCondition (abstract)
    * InvertCondition
    * TextualCondition
  * AbstractGlobalTimeDomainProps (abstract)
    * CanGlobalTimeDomainProps
    * EthGlobalTimeDomainProps
    * FrGlobalTimeDomainProps
  * AbstractMultiplicityRestriction (abstract)
    * AttributeCondition (abstract)
      * AggregationCondition
      * PrimitiveAttributeCondition
      * ReferenceCondition
  * AbstractValueRestriction (abstract)
  * AbstractVariationRestriction (abstract)
  * AccessCount
  * AccessCountSet
  * AdminData
  * AliasNameAssignment
  * AnyInstanceRef
  * ApplicationCompositeElementInPortInterfaceInstanceRef
  * ArParameterInImplementationDataInstanceRef
  * ArVariableInImplementationDataInstanceRef
  * Area
  * AtpBlueprintMapping (abstract)
  * AtpInstanceRef (abstract)
  * AutosarParameterRef
  * AutosarVariableRef
  * BaseTypeDefinition (abstract)
    * BaseTypeDirectDefinition
  * Baseline
  * BinaryManifestItemValue (abstract)
    * BinaryManifestItemNumericalValue
    * BinaryManifestItemPointerValue
  * BlueprintGenerator
  * BlueprintMapping
  * BlueprintPolicy (abstract)
    * BlueprintPolicyList
    * BlueprintPolicyNotModifiable
    * BlueprintPolicySingle
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
  * ChapterModel
  * ClassTailoring (abstract)
  * ClientIdRange
  * ClientServerApplicationErrorMapping
  * ClientServerOperationBlueprintMapping
  * ClientServerOperationMapping
  * Colspec
  * CommunicationControllerMapping
  * CommunicationCycle (abstract)
    * CycleCounter
    * CycleRepetition
  * ComponentInCompositionInstanceRef
  * ComponentInSystemInstanceRef
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
  * DataFormatTailoring
  * DataMapping (abstract)
    * ClientServerToSignalMapping
    * SenderReceiverCompositeElementToSignalMapping
    * SenderReceiverToSignalGroupMapping
    * SenderReceiverToSignalMapping
    * TriggerToSignalMapping
  * DataPrototypeInPortInterfaceInstanceRef (abstract)
    * DataPrototypeInClientServerInterfaceInstanceRef
    * DataPrototypeInSenderReceiverInterfaceInstanceRef
  * DataPrototypeInSystemInstanceRef
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
  * DhcpServerConfiguration
  * Dhcpv6Props
  * DiagnosticAbstractParameter (abstract)
    * DiagnosticParameter
  * DiagnosticAuthRoleProxy
  * DiagnosticComControlSpecificChannel
  * DiagnosticComControlSubNodeChannel
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
  * FMAttributeValue
  * FMFeatureDecomposition
  * FileInfoComment
  * FirewallRuleProps
  * FlexrayAbsolutelyScheduledTiming
  * FlexrayArTpChannel
  * FlexrayFifoConfiguration
  * FlexrayFifoRange
  * FlexrayTpEcu
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
  * HwPortMapping
  * IPSecConfig
  * IPduMapping
  * ISignalMapping
  * ISignalProps
  * IdsmSignatureSupportAp
  * IdsmSignatureSupportCp
  * ImplementationElementInParameterInstanceRef
  * IncludedDataTypeSet
  * IncludedModeDeclarationGroupSet
  * IndentSample
  * IndexedArrayElement
  * InfrastructureServices
  * InitialSdDelayConfig
  * InnerDataPrototypeGroupInCompositionInstanceRef
  * InnerPortGroupInCompositionInstanceRef
  * InnerRunnableEntityGroupInCompositionInstanceRef
  * InstanceEventInCompositionInstanceRef
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
  * McParameterElementGroup
  * McSupportData
  * McSwEmulationMethodSupport
  * MemorySectionLocation
  * MetaDataItem
  * MetaDataItemSet
  * ModeAccessPoint
  * ModeDeclarationGroupPrototypeMapping
  * ModeDrivenTransmissionModeCondition
  * ModeErrorBehavior
  * ModeGroupInAtomicSwcInstanceRef (abstract)
    * PModeGroupInAtomicSwcInstanceRef
    * RModeGroupInAtomicSWCInstanceRef
  * ModeInBswModuleDescriptionInstanceRef
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
  * OperationInAtomicSwcInstanceRef (abstract)
    * POperationInAtomicSwcInstanceRef
    * ROperationInAtomicSwcInstanceRef
  * OperationInSystemInstanceRef
  * OrderedMaster
  * PModeInSystemInstanceRef
  * PPortComSpec (abstract)
    * ModeSwitchSenderComSpec
    * NvProvideComSpec
    * ParameterProvideComSpec
    * SenderComSpec (abstract)
      * NonqueuedSenderComSpec
      * QueuedSenderComSpec
    * ServerComSpec
  * ParameterInAtomicSWCTypeInstanceRef
  * PduMappingDefaultValue
  * PerInstanceMemorySize
  * PhysConstrs
  * PhysicalDimensionMapping
  * PlcaProps
  * PortAPIOption
  * PortDefinedArgumentValue
  * PortGroupInSystemInstanceRef
  * PortInCompositionTypeInstanceRef (abstract)
    * PPortInCompositionInstanceRef
    * RPortInCompositionInstanceRef
  * PortPrototypeBlueprintInitValue
  * PostBuildVariantCondition
  * PostBuildVariantCriterionValue
  * PredefinedChapter
  * PrivacyLevel
  * RModeInAtomicSwcInstanceRef
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
        * AbstractAccessPoint (abstract)
          * AsynchronousServerCallResultPoint
          * InternalTriggeringPoint
          * ModeSwitchPoint
          * ParameterAccess
          * ServerCallPoint (abstract)
            * AsynchronousServerCallPoint
            * SynchronousServerCallPoint
          * VariableAccess
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
          * RTEEvent (abstract)
            * AsynchronousServerCallReturnsEvent
            * BackgroundEvent
            * DataReceiveErrorEvent
            * DataReceivedEvent
            * DataSendCompletedEvent
            * DataWriteCompletedEvent
            * ExternalTriggerOccurredEvent
            * InitEvent
            * InternalTriggerOccurredEvent
            * ModeSwitchedAckEvent
            * OperationInvokedEvent
            * OsTaskExecutionEvent
            * SwcModeManagerErrorEvent
            * SwcModeSwitchEvent
            * TimingEvent
            * TransformerHardErrorEvent
        * AbstractImplementationDataTypeElement (abstract)
          * ImplementationDataTypeElement
        * AbstractSecurityEventFilter (abstract)
          * SecurityEventAggregationFilter
          * SecurityEventOneEveryNFilter
          * SecurityEventStateFilter
          * SecurityEventThresholdFilter
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
        * AtpClassifier (abstract)
        * AtpFeature (abstract)
        * AtpPrototype (abstract)
        * AtpStructureElement (abstract)
        * AtpType (abstract)
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
        * BlockState
        * BswInternalTriggeringPoint
        * BswModuleDependency
        * BuildActionEntity (abstract)
          * BuildAction
        * BuildActionEnvironment
        * BulkNvDataDescriptor
        * CanTpAddress
        * CanTpChannel
        * CanTpNode
        * ClassContentConditional
        * ClientIdDefinition
        * ClientServerOperation
        * Code
        * CollectableElement (abstract)
          * ARPackage
          * PackageableElement (abstract)
            * ARElement (abstract)
              * AclObjectSet
              * AclOperation
              * AclPermission
              * AclRole
              * AliasNameSet
              * ApplicationPartition
              * AutosarDataType (abstract)
                * AbstractImplementationDataType (abstract)
                  * ImplementationDataType
                * ApplicationDataType (abstract)
                  * ApplicationCompositeDataType (abstract)
                    * ApplicationArrayDataType
                    * ApplicationRecordDataType
                  * ApplicationDeferredDataType
                  * ApplicationPrimitiveDataType
              * BaseType (abstract)
                * SwBaseType
              * BlueprintMappingSet
              * BswEntryRelationshipSet
              * BswModuleDescription
              * BswModuleEntry
              * BuildActionManifest
              * CalibrationParameterValueSet
              * ClientIdDefinitionSet
              * ClientServerInterfaceToBswModuleEntryBlueprintMapping
              * Collection
              * CompuMethod
              * ConsistencyNeedsBlueprintSet
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
              * DataConstr
              * DataExchangePoint
              * DataTransformationSet
              * DataTypeMappingSet
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
                  * DiagnosticEventToDebounceAlgorithmMapping
                  * DiagnosticEventToEnableConditionGroupMapping
                  * DiagnosticEventToOperationCycleMapping
                  * DiagnosticEventToSecurityEventMapping
                  * DiagnosticEventToStorageConditionGroupMapping
                  * DiagnosticEventToTroubleCodeJ1939Mapping
                  * DiagnosticEventToTroubleCodeUdsMapping
                  * DiagnosticFimAliasEventGroupMapping
                  * DiagnosticFimAliasEventMapping
                  * DiagnosticInhibitSourceEventMapping
                  * DiagnosticIumprToFunctionIdentifierMapping
                  * DiagnosticJ1939SpnMapping
                  * DiagnosticMasterToSlaveEventMapping
                  * DiagnosticSecureCodingMapping
                  * DiagnosticSecurityEventReportingModeMapping
                  * DiagnosticSwMapping (abstract)
                    * DiagnosticEnableConditionPortMapping
                    * DiagnosticEventPortMapping
                    * DiagnosticFimFunctionMapping
                    * DiagnosticJ1939SwMapping
                    * DiagnosticOperationCyclePortMapping
                    * DiagnosticServiceDataMapping
                    * DiagnosticServiceSwMapping
                    * DiagnosticStorageConditionPortMapping
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
                      * DiagnosticReadMemoryByAddress
                      * DiagnosticRequestDownload
                      * DiagnosticRequestUpload
                      * DiagnosticWriteMemoryByAddress
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
              * DiagnosticConnection
              * DiagnosticContributionSet
              * DltContext
              * DltEcu
              * Documentation
              * E2EProfileCompatibilityProps
              * EcucDefinitionCollection
              * EcucDestinationUriDefSet
              * EcucModuleConfigurationValues
              * EcucValueCollection
              * EndToEndProtectionSet
              * EthIpProps
              * EthTcpIpIcmpProps
              * EthTcpIpProps
              * EvaluatedVariantSet
              * FMFeature
              * FMFeatureMap
              * FMFeatureModel
              * FMFeatureSelectionSet
              * FirewallRule
              * FlatMap
              * GeneralPurposeConnection
              * HwCategory
              * IEEE1722TpConnection (abstract)
                * IEEE1722TpAcfConnection
                * IEEE1722TpAvConnection (abstract)
                  * IEEE1722TpAafConnection
                  * IEEE1722TpCrfConnection
                  * IEEE1722TpIidcConnection
                  * IEEE1722TpRvfConnection
              * IPSecConfigProps
              * IPv6ExtHeaderFilterSet
              * IdsCommonElement (abstract)
                * IdsMapping (abstract)
                  * SecurityEventContextMapping (abstract)
                    * SecurityEventContextMappingApplication
                    * SecurityEventContextMappingBswModule
                    * SecurityEventContextMappingCommConnector
                    * SecurityEventContextMappingFunctionalCluster
                * IdsmInstance
                * IdsmProperties
                * SecurityEventDefinition
                * SecurityEventFilterChain
              * IdsDesign
              * Implementation (abstract)
                * BswImplementation
                * SwcImplementation
              * InterpolationRoutineMappingSet
              * J1939ControllerApplication
              * KeywordSet
              * LifeCycleInfoSet
              * LifeCycleStateDefinitionGroup
              * LogAndTraceMessageCollectionSet
              * MacSecGlobalKayProps
              * MacSecParticipantSet
              * McFunction
              * McGroup
              * ModeDeclarationGroup
              * ModeDeclarationMappingSet
              * OsTaskProxy
              * PhysicalDimension
              * PhysicalDimensionMappingSet
              * PlatformModuleEthernetEndpointConfiguration
              * PortInterface (abstract)
                * ApplicationInterface
                * ClientServerInterface
                * DataInterface (abstract)
                  * NvDataInterface
                  * ParameterInterface
                  * SenderReceiverInterface
                * ModeSwitchInterface
                * TriggerInterface
              * PortInterfaceMappingSet
              * PortPrototypeBlueprint
              * PostBuildVariantCriterion
              * PostBuildVariantCriterionValueSet
              * PredefinedVariant
              * RapidPrototypingScenario
              * SdgDef
              * SignalServiceTranslationPropsSet
              * SomeipSdClientEventGroupTimingConfig
              * SomeipSdClientServiceInstanceConfig
              * SomeipSdServerEventGroupTimingConfig
              * SomeipSdServerServiceInstanceConfig
              * StateDependentFirewall
              * SwAddrMethod
              * SwAxisType
              * SwComponentType (abstract)
                * AtomicSwComponentType (abstract)
                  * ApplicationSwComponentType
                  * ComplexDeviceDriverSwComponentType
                  * EcuAbstractionSwComponentType
                  * NvBlockSwComponentType
                  * SensorActuatorSwComponentType
                  * ServiceProxySwComponentType
                  * ServiceSwComponentType
                * CompositionSwComponentType
                * ParameterSwComponentType
              * SwRecordLayout
              * SwSystemconst
              * SwSystemconstantValueSet
              * SwcBswMapping
              * System
              * SystemSignal
              * SystemSignalGroup
              * TDCpSoftwareClusterMappingSet
              * TcpOptionFilterSet
              * TimingExtension (abstract)
                * BswCompositionTiming
                * BswModuleTiming
                * EcuTiming
                * SwcTiming
                * SystemTiming
                * VfbTiming
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
              * ConsumedProvidedServiceInstanceGroup
              * CouplingElement
              * EcuInstance
              * EthernetWakeupSleepOnDatalineConfigSet
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
              * GlobalTimeDomain
              * ISignal
              * ISignalGroup
              * ISignalIPduGroup
              * NmConfig
              * Pdu (abstract)
                * GeneralPurposePdu
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
                * NmPdu
                * UserDefinedPdu
              * PdurIPduGroup
              * SecureCommunicationPropsSet
              * ServiceInstanceCollectionSet
              * SoAdRoutingGroup
              * SocketConnectionIpduIdentifierSet
              * TpConfig (abstract)
                * CanTpConfig
                * DoIpTpConfig
                * EthTpConfig
                * FlexrayArTpConfig
                * FlexrayTpConfig
                * IEEE1722TpConfig
                * J1939TpConfig
                * LinTpConfig
                * SomeipTpConfig
        * ComManagementMapping
        * CommConnectorPort (abstract)
          * FramePort
          * IPduPort
          * ISignalPort
        * CommunicationConnector (abstract)
          * AbstractCanCommunicationConnector (abstract)
            * CanCommunicationConnector
            * TtcanCommunicationConnector
          * EthernetCommunicationConnector
          * FlexrayCommunicationConnector
          * LinCommunicationConnector
          * UserDefinedCommunicationConnector
        * Compiler
        * ConsistencyNeeds
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
        * CryptoKeySlot
        * CryptoServiceMapping (abstract)
          * SecOcCryptoServiceMapping
          * TlsCryptoServiceMapping
        * DataPrototype (abstract)
          * ApplicationCompositeElementDataPrototype (abstract)
            * ApplicationArrayElement
            * ApplicationRecordElement
          * AutosarDataPrototype (abstract)
            * ArgumentDataPrototype
            * Field
            * ParameterDataPrototype
            * VariableDataPrototype
        * DataPrototypeGroup
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
              * EcucAddInfoParamDef
              * EcucBooleanParamDef
              * EcucEnumerationParamDef
              * EcucFloatParamDef
              * EcucIntegerParamDef
          * EcucContainerDef (abstract)
            * EcucChoiceContainerDef
            * EcucParamConfContainerDef
          * EcucModuleDef
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
        * FMAttributeDef
        * FMFeatureMapAssertion
        * FMFeatureMapCondition
        * FMFeatureMapElement
        * FMFeatureRelation
        * FMFeatureRestriction
        * FMFeatureSelection
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
        * GlobalTimeGateway
        * GlobalTimeMaster (abstract)
          * GlobalTimeCanMaster
          * GlobalTimeEthMaster
          * GlobalTimeFrMaster
          * UserDefinedGlobalTimeMaster
        * GlobalTimeSlave (abstract)
          * GlobalTimeCanSlave
          * GlobalTimeEthSlave
          * GlobalTimeFrSlave
          * UserDefinedGlobalTimeSlave
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
        * IdentCaption (abstract)
          * BswServiceDependencyIdent
          * DiagnosticParameterIdent
          * ExternalTriggeringPointIdent
          * ModeAccessPointIdent
        * IdsPlatformInstantiation (abstract)
          * IdsmModuleInstantiation
        * IdsmRateLimitation
        * IdsmTrafficLimitation
        * ImpositionTime
        * InternalBehavior (abstract)
          * BswInternalBehavior
          * SwcInternalBehavior
        * J1939SharedAddressCluster
        * J1939TpNode
        * Keyword
        * LifeCycleState
        * LinScheduleTable
        * LinTpNode
        * Linker
        * MacMulticastGroup
        * MacSecKayParticipant
        * McDataInstance
        * MemorySection
        * ModeDeclaration
        * ModeDeclarationGroupPrototype
        * ModeDeclarationMapping
        * ModeTransition
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
        * NvBlockDescriptor
        * PduActivationRoutingGroup
        * PduTriggering
        * PerInstanceMemory
        * PhysicalChannel (abstract)
          * AbstractCanPhysicalChannel (abstract)
            * CanPhysicalChannel
            * TtcanPhysicalChannel
          * EthernetPhysicalChannel
          * FlexrayPhysicalChannel
          * LinPhysicalChannel
          * UserDefinedPhysicalChannel
        * PortElementToCommunicationResourceMapping
        * PortGroup
        * PortInterfaceMapping (abstract)
          * ClientServerInterfaceMapping
          * ModeInterfaceMapping
          * TriggerInterfaceMapping
          * VariableAndParameterInterfaceMapping
        * PortPrototype (abstract)
          * AbstractProvidedPortPrototype (abstract)
            * PPortPrototype
          * AbstractRequiredPortPrototype (abstract)
            * PRPortPrototype
            * RPortPrototype
        * ResourceConsumption
        * RootSwCompositionPrototype
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
        * RunnableEntityGroup
        * SdgAttribute (abstract)
          * SdgReference
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
        * SpecElementReference (abstract)
          * DataFormatElementReference (abstract)
            * AbstractClassTailoring (abstract)
          * DocumentElementScope
          * SpecElementScope (abstract)
            * DataFormatElementScope (abstract)
              * AttributeTailoring (abstract)
                * AggregationTailoring
                * PrimitiveAttributeTailoring
                * ReferenceTailoring
              * ConcreteClassTailoring
          * SpecificationDocumentScope
        * StackUsage (abstract)
          * MeasuredStackUsage
          * RoughEstimateStackUsage
          * WorstCaseStackUsage
        * StaticSocketConnection
        * SwComponentPrototype
        * SwConnector (abstract)
          * AssemblySwConnector
          * DelegationSwConnector
          * PassThroughSwConnector
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
        * TimingClock (abstract)
          * TDLETZoneClock
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
        * Trigger
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
  * RestrictionWithSeverity (abstract)
    * ConstraintTailoring
    * MultiplicityRestrictionWithSeverity
    * SdgTailoring
    * UnresolvedReferenceRestrictionWithSeverity
    * ValueRestrictionWithSeverity
    * VariationRestrictionWithSeverity
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
  * RuleBasedAxisCont
  * RuleBasedValueCont
  * RuleBasedValueSpecification
  * RunnableEntityArgument
  * RunnableEntityInCompositionInstanceRef
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
  * SdgElementWithGid (abstract)
    * SdgAbstractForeignReference (abstract)
      * SdgForeignReference
      * SdgForeignReferenceWithVariation
    * SdgAbstractPrimitiveAttribute (abstract)
      * SdgPrimitiveAttribute
      * SdgPrimitiveAttributeWithVariation
    * SdgAggregationWithVariation
    * SdgClass
  * SecureCommunicationProps
  * SecurityEventContextData
  * SegmentPosition
  * SenderRecArrayElementMapping
  * SenderRecCompositeTypeMapping (abstract)
    * SenderRecArrayTypeMapping
    * SenderRecRecordTypeMapping
  * SenderRecRecordElementMapping
  * ServiceDependency (abstract)
    * BswServiceDependency
    * SwcServiceDependency
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
  * SpecificationScope
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
  * SwDataDependency
  * SwGenericAxisParam
  * SwPointerTargetProps
  * SwRecordLayoutGroup
  * SwRecordLayoutV
  * SwSystemconstValue
  * SwTextProps
  * SwValueCont
  * SwVariableRefProxy
  * SwcBswRunnableMapping
  * SwcBswSynchronizedModeGroupPrototype
  * SwcBswSynchronizedTrigger
  * SwcExclusiveAreaPolicy
  * SwcServiceDependencyInSystemInstanceRef
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
  * TriggerInAtomicSwcInstanceRef (abstract)
    * PTriggerInAtomicSwcTypeInstanceRef
    * RTriggerInAtomicSwcInstanceRef
  * TriggerInSystemInstanceRef
  * TriggerMapping
  * Tt
  * TtcanAbsolutelyScheduledTiming
  * UdpProps
  * ValueGroup
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
  * VariableDataPrototypeInCompositionInstanceRef
  * VariableDataPrototypeInSystemInstanceRef
  * VariableInAtomicSWCTypeInstanceRef
  * VariableInAtomicSwcInstanceRef (abstract)
    * RVariableInAtomicSwcInstanceRef
  * VariationPoint
  * VlanMembership
  * WhitespaceControlled (abstract)
  * Xref
