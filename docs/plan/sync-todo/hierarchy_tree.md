# Sync-todo class hierarchy tree (names only)

Generated 2026-09-26 from the spec-table Base rows of every queue row in Group1-20 (parent-dependency
audit; extraction script: /tmp/audit_base_parents.py, same-table identity rule — see the audit notes in
Group8/14/15/16/17). Every queue class (pending and done) appears as a node, rooted at ARObject; classes
with several spec parents appear under EACH parent — the first occurrence expands the full subtree, later
occurrences carry the ↩ marker instead of re-expanding. Excluded from the tree: AtpMixedString /
VariationPointCapable (interface mixins) and the PrimitiveTypes leaf types. Omitted via the
most-derived-base-collapse precedent: UploadableDesignElement / UploadablePackageElement. Subclasses
mentioned only in table Subclasses rows (never queued) are not nodes. Source of every link: the R23-11
markdown Base row (R4.3.1 fallback; XSD group refs for XSD-only classes).

```
ARObject
├─ AbstractEnumerationValueVariationPoint
├─ AbstractNumericalVariationPoint
│  ├─ LimitValueVariationPoint
│  └─ NumericalValueVariationPoint
├─ AbstractProvidedPortPrototype
├─ AbstractRequiredPortPrototype
├─ ApplicationEntry
├─ ApplicationPartitionToEcuPartitionMapping
├─ AppOsTaskProxyToEcuTaskProxyMapping
├─ AsynchronousServerCallReturnsEvent
├─ AtpBlueprint
│  ├─ BswEntryRelationship
│  ├─ BswEntryRelationshipSet
│  ├─ ClientServerInterfaceMapping
│  ├─ ModeInterfaceMapping
│  ├─ ServiceProxySwComponentType
│  └─ VariableAndParameterInterfaceMapping
├─ AttributeValueVariationPoint
│  ├─ AbstractEnumerationValueVariationPoint
│  ├─ AbstractNumericalVariationPoint
│  │  ├─ LimitValueVariationPoint
│  │  └─ NumericalValueVariationPoint
│  ├─ BooleanValueVariationPoint
│  ├─ FloatValueVariationPoint
│  ├─ IntegerValueVariationPoint
│  ├─ LimitValueVariationPoint
│  ├─ NumericalValueVariationPoint
│  ├─ PositiveIntegerValueVariationPoint
│  ├─ TimeValueValueVariationPoint
│  └─ UnlimitedIntegerValueVariationPoint
├─ AutosarOperationArgumentInstance
├─ AutosarParameterRef
├─ AutosarVariableRef
├─ BlueprintFormula
├─ BlueprintGenerator
├─ BlueprintMapping
├─ BooleanValueVariationPoint
├─ BswAsynchronousServerCallReturnsEvent
├─ BswDataReceivedEvent
├─ BswDirectCallPoint
├─ BswEntryRelationship
├─ BswEntryRelationshipSet
├─ BswInternalTriggeringPoint
├─ BswInternalTriggerOccurredEvent
├─ BswInterruptEntity
├─ BswModeManagerErrorEvent
├─ BswModeSwitchAckRequest
├─ BswModeSwitchedAckEvent
├─ BswModuleCallPoint
│  ├─ BswDirectCallPoint
│  └─ BswSynchronousServerCallPoint
├─ BswModuleClientServerEntry
├─ BswModuleDependency
├─ BswQueuedDataReceptionPolicy
├─ BswSynchronousServerCallPoint
├─ BswTimingEvent
├─ BuildActionIoElement
├─ BulkNvDataDescriptor
├─ CanClusterBusOffRecovery
├─ CanCommunicationConnector
├─ CanControllerConfiguration
├─ CanControllerConfigurationRequirements
├─ CanControllerFdConfigurationRequirements
├─ CanNmCluster
├─ CanNmClusterCoupling
├─ CanNmNode
├─ ChapterContent
├─ ChapterModel
├─ ClientIdRange
├─ ClientServerApplicationErrorMapping
├─ ClientServerInterfaceMapping
├─ ClientServerOperationMapping
├─ CompositeNetworkRepresentation
├─ CompuGenericMath
├─ ConditionByFormula
├─ ConstantReference
├─ ConstantSpecification
├─ CryptoServiceNeeds
├─ CyclicTiming
├─ DataFilter
├─ DataMapping
│  ├─ SenderReceiverToSignalGroupMapping
│  └─ SenderReceiverToSignalMapping
├─ DataPrototypeTransformationProps
├─ DataReceivedEvent
├─ DataReceiveErrorEvent
├─ DataSendCompletedEvent
├─ DataTypeMap
├─ DataWriteCompletedEvent
├─ DefaultValueElement
├─ DiagEventDebounceCounterBased
├─ DiagnosticAccessPermission
├─ DiagnosticCapabilityElement
│  ├─ DiagnosticCommunicationManagerNeeds
│  ├─ DiagnosticControlNeeds
│  ├─ DiagnosticEventInfoNeeds
│  ├─ DiagnosticEventManagerNeeds
│  ├─ DiagnosticRequestFileTransferNeeds
│  ├─ DiagnosticRoutineNeeds
│  ├─ DiagnosticValueNeeds
│  └─ DtcStatusChangeNotificationNeeds
├─ DiagnosticCommunicationManagerNeeds
├─ DiagnosticControlNeeds
├─ DiagnosticEnvConditionFormula
├─ DiagnosticEnvConditionFormulaPart
│  ├─ DiagnosticEnvCompareCondition
│  └─ DiagnosticEnvConditionFormula
├─ DiagnosticEnvModeElement
├─ DiagnosticEventInfoNeeds
├─ DiagnosticEventManagerNeeds
├─ DiagnosticRequestFileTransferNeeds
├─ DiagnosticRoutineNeeds
├─ DiagnosticServiceClass
├─ DiagnosticValueNeeds
├─ DltApplication
├─ DltArgument
├─ DltContext
├─ DltLogChannel
├─ DoIpActivationLineNeeds
├─ DoIpEntity
├─ DoIpGidNeeds
├─ DoIpGidSynchronizationNeeds
├─ DoIpLogicAddress
├─ DoIpTpConnection
├─ DtcStatusChangeNotificationNeeds
├─ DynamicPart
├─ EcucBooleanParamDef
├─ EcucConditionFormula
├─ EcucFloatParamDef
├─ EcucForeignReferenceDef
├─ EcucLinkerSymbolDef
├─ EcucParameterDerivationFormula
├─ EcucQueryExpression
├─ EcucReferenceDef
├─ EcucSymbolicNameReferenceDef
├─ EcucUriReferenceDef
├─ EcucValueCollection
├─ EndToEndDescription
├─ EndToEndProtectionISignalIPdu
├─ EndToEndTransformationISignalProps
├─ EthernetPriorityRegeneration
├─ EventControlledTiming
├─ Field
├─ FlexrayCommunicationConnector
├─ FlexrayCommunicationController
├─ FlexrayFrameTriggering
├─ FlexrayNmClusterCoupling
├─ FlexrayPhysicalChannel
├─ FloatValueVariationPoint
├─ FMConditionByFeaturesAndAttributes
├─ FMConditionByFeaturesAndSwSystemconsts
├─ FMFormulaByFeaturesAndAttributes
│  └─ FMConditionByFeaturesAndAttributes
├─ FMFormulaByFeaturesAndSwSystemconsts
│  └─ FMConditionByFeaturesAndSwSystemconsts
├─ FormulaExpression
│  ├─ AbstractEnumerationValueVariationPoint
│  ├─ AbstractNumericalVariationPoint
│  │  ├─ LimitValueVariationPoint
│  │  └─ NumericalValueVariationPoint
│  ├─ AttributeValueVariationPoint
│  │  ├─ AbstractEnumerationValueVariationPoint
│  │  ├─ AbstractNumericalVariationPoint
│  │  │  ├─ LimitValueVariationPoint
│  │  │  └─ NumericalValueVariationPoint
│  │  ├─ BooleanValueVariationPoint
│  │  ├─ FloatValueVariationPoint
│  │  ├─ IntegerValueVariationPoint
│  │  ├─ LimitValueVariationPoint
│  │  ├─ NumericalValueVariationPoint
│  │  ├─ PositiveIntegerValueVariationPoint
│  │  ├─ TimeValueValueVariationPoint
│  │  └─ UnlimitedIntegerValueVariationPoint
│  ├─ BlueprintFormula
│  ├─ BooleanValueVariationPoint
│  ├─ CompuGenericMath
│  ├─ ConditionByFormula
│  ├─ EcucConditionFormula
│  ├─ EcucParameterDerivationFormula
│  ├─ FloatValueVariationPoint
│  ├─ FMConditionByFeaturesAndAttributes
│  ├─ FMConditionByFeaturesAndSwSystemconsts
│  ├─ FMFormulaByFeaturesAndAttributes
│  │  └─ FMConditionByFeaturesAndAttributes
│  ├─ FMFormulaByFeaturesAndSwSystemconsts
│  │  └─ FMConditionByFeaturesAndSwSystemconsts
│  ├─ IntegerValueVariationPoint
│  ├─ LimitValueVariationPoint
│  ├─ NumericalValueVariationPoint
│  ├─ PositiveIntegerValueVariationPoint
│  ├─ SwSystemconstDependentFormula
│  │  ├─ AbstractEnumerationValueVariationPoint
│  │  ├─ AbstractNumericalVariationPoint
│  │  │  ├─ LimitValueVariationPoint
│  │  │  └─ NumericalValueVariationPoint
│  │  ├─ AttributeValueVariationPoint
│  │  │  ├─ AbstractEnumerationValueVariationPoint
│  │  │  ├─ AbstractNumericalVariationPoint
│  │  │  │  ├─ LimitValueVariationPoint
│  │  │  │  └─ NumericalValueVariationPoint
│  │  │  ├─ BooleanValueVariationPoint
│  │  │  ├─ FloatValueVariationPoint
│  │  │  ├─ IntegerValueVariationPoint
│  │  │  ├─ LimitValueVariationPoint
│  │  │  ├─ NumericalValueVariationPoint
│  │  │  ├─ PositiveIntegerValueVariationPoint
│  │  │  ├─ TimeValueValueVariationPoint
│  │  │  └─ UnlimitedIntegerValueVariationPoint
│  │  ├─ BlueprintFormula
│  │  ├─ BooleanValueVariationPoint
│  │  ├─ ConditionByFormula
│  │  ├─ FloatValueVariationPoint
│  │  ├─ FMConditionByFeaturesAndSwSystemconsts
│  │  ├─ FMFormulaByFeaturesAndSwSystemconsts
│  │  │  └─ FMConditionByFeaturesAndSwSystemconsts
│  │  ├─ IntegerValueVariationPoint
│  │  ├─ LimitValueVariationPoint
│  │  ├─ NumericalValueVariationPoint
│  │  ├─ PositiveIntegerValueVariationPoint
│  │  ├─ TimeValueValueVariationPoint
│  │  └─ UnlimitedIntegerValueVariationPoint
│  ├─ TimeValueValueVariationPoint
│  └─ UnlimitedIntegerValueVariationPoint
├─ FrameMapping
├─ Gateway
├─ GenericTp
├─ HardwareConfiguration
├─ ImplementationDataTypeElement
├─ ImplementationProps
│  └─ SectionNamePrefix
├─ IndexedArrayElement
├─ InitialSdDelayConfig
├─ InstantiationDataDefProps
├─ IntegerValueVariationPoint
├─ InternalTriggeringPoint
├─ InternalTriggerOccurredEvent
├─ Ipv4Configuration
├─ IPv6ExtHeaderFilterList
├─ ISignalIPduGroup
├─ ISignalMapping
├─ ISignalPort
├─ Item
├─ LifeCycleInfo
├─ LifeCycleInfoSet
├─ LifeCyclePeriod
├─ LimitValueVariationPoint
├─ LinCommunicationConnector
├─ LinScheduleTable
├─ LinTpConnection
├─ LOverviewParagraph
├─ LPlainText
├─ LVerbatim
├─ MacMulticastGroup
├─ MeasuredStackUsage
├─ MemorySection
├─ MixedContentForOverviewParagraph
│  ├─ LOverviewParagraph
│  └─ SlOverviewParagraph
├─ MixedContentForPlainText
│  └─ LPlainText
├─ MixedContentForVerbatim
│  └─ LVerbatim
├─ ModeAccessPoint
├─ ModeDeclarationGroupPrototypeMapping
├─ ModeGroupInAtomicSwcInstanceRef
│  ├─ PModeGroupInAtomicSwcInstanceRef
│  └─ RModeGroupInAtomicSWCInstanceRef
├─ ModeInSwcInstanceRef
├─ ModeInterfaceMapping
├─ ModeRequestTypeMap
├─ ModeSwitchedAckRequest
├─ ModeSwitchEventTriggeredActivity
├─ ModeSwitchPoint
├─ ModeSwitchReceiverComSpec
├─ ModeSwitchSenderComSpec
├─ Modification
├─ MultidimensionalTime
├─ MultiplexedIPdu
├─ MultiplexedPart
│  └─ DynamicPart
├─ NetworkEndpoint
├─ NmEcu
├─ NumericalValueSpecification
├─ NumericalValueVariationPoint
├─ NvBlockDataMapping
├─ NvBlockDescriptor
├─ NvBlockNeeds
├─ NvProvideComSpec
├─ NvRequireComSpec
├─ OffsetTimingConstraint
├─ OperationInAtomicSwcInstanceRef
│  ├─ POperationInAtomicSwcInstanceRef
│  └─ ROperationInAtomicSwcInstanceRef
├─ OperationInvokedEvent
├─ OrderedMaster
├─ ParameterAccess
├─ ParameterRequireComSpec
├─ PModeGroupInAtomicSwcInstanceRef
├─ POperationInAtomicSwcInstanceRef
├─ PositiveIntegerValueVariationPoint
├─ PostBuildVariantCondition
├─ PostBuildVariantCriterion
├─ PostBuildVariantCriterionValue
├─ PPortInCompositionInstanceRef
├─ PTriggerInAtomicSwcTypeInstanceRef
├─ QueuedReceiverComSpec
├─ ReceptionComSpecProps
├─ RequestResponseDelay
├─ RModeGroupInAtomicSWCInstanceRef
├─ RModeInAtomicSwcInstanceRef
├─ RoleBasedDataAssignment
├─ RoleBasedPortAssignment
├─ ROperationInAtomicSwcInstanceRef
├─ RoughEstimateStackUsage
├─ RPortInCompositionInstanceRef
├─ RVariableInAtomicSwcInstanceRef
├─ SdServerConfig
├─ SecOcCryptoServiceMapping
├─ SectionNamePrefix
├─ SecuredIPdu
├─ SegmentPosition
├─ SenderReceiverToSignalGroupMapping
├─ SenderReceiverToSignalMapping
├─ SenderRecRecordElementMapping
├─ SenderRecRecordTypeMapping
├─ ServiceProxySwComponentType
├─ ShortNameFragment
├─ SignalServiceTranslationElementProps
├─ SingleLanguageUnitNames
├─ SlOverviewParagraph
├─ SoAdRoutingGroup
├─ SocketConnectionBundle
├─ SocketConnectionIpduIdentifier
├─ SoftwareContext
├─ StackUsage
│  ├─ MeasuredStackUsage
│  ├─ RoughEstimateStackUsage
│  └─ WorstCaseStackUsage
├─ SwcBswRunnableMapping
├─ SwcBswSynchronizedModeGroupPrototype
├─ SwcBswSynchronizedTrigger
├─ SwcImplementation
├─ SwcToEcuMapping
├─ SwcToImplMapping
├─ SwRecordLayoutGroup
├─ SwSystemconst
├─ SwSystemconstDependentFormula
│  ├─ AbstractEnumerationValueVariationPoint
│  ├─ AbstractNumericalVariationPoint
│  │  ├─ LimitValueVariationPoint
│  │  └─ NumericalValueVariationPoint
│  ├─ AttributeValueVariationPoint
│  │  ├─ AbstractEnumerationValueVariationPoint
│  │  ├─ AbstractNumericalVariationPoint
│  │  │  ├─ LimitValueVariationPoint
│  │  │  └─ NumericalValueVariationPoint
│  │  ├─ BooleanValueVariationPoint
│  │  ├─ FloatValueVariationPoint
│  │  ├─ IntegerValueVariationPoint
│  │  ├─ LimitValueVariationPoint
│  │  ├─ NumericalValueVariationPoint
│  │  ├─ PositiveIntegerValueVariationPoint
│  │  ├─ TimeValueValueVariationPoint
│  │  └─ UnlimitedIntegerValueVariationPoint
│  ├─ BlueprintFormula
│  ├─ BooleanValueVariationPoint
│  ├─ ConditionByFormula
│  ├─ FloatValueVariationPoint
│  ├─ FMConditionByFeaturesAndSwSystemconsts
│  ├─ FMFormulaByFeaturesAndSwSystemconsts
│  │  └─ FMConditionByFeaturesAndSwSystemconsts
│  ├─ IntegerValueVariationPoint
│  ├─ LimitValueVariationPoint
│  ├─ NumericalValueVariationPoint
│  ├─ PositiveIntegerValueVariationPoint
│  ├─ TimeValueValueVariationPoint
│  └─ UnlimitedIntegerValueVariationPoint
├─ SwSystemconstValue
├─ SynchronizationTimingConstraint
├─ SystemSignal
├─ TargetIPduRef
├─ TcpOptionFilterList
├─ TcpOptionFilterSet
├─ TcpProps
├─ TcpTp
├─ TextValueSpecification
├─ TimeRangeType
├─ TimeSynchronization
├─ TimeSyncServerConfiguration
├─ TimeValueValueVariationPoint
├─ TimingDescriptionEventChain
├─ TopicContentOrMsrQuery
├─ TpAddress
├─ TpPort
├─ TransmissionModeCondition
├─ TransmissionModeDeclaration
├─ TransmissionModeTiming
├─ TriggerInAtomicSwcInstanceRef
│  └─ PTriggerInAtomicSwcTypeInstanceRef
├─ TriggerIPduSendCondition
├─ UdpNmCluster
├─ UdpNmClusterCoupling
├─ UdpNmNode
├─ UdpTp
├─ UnitGroup
├─ UnlimitedIntegerValueVariationPoint
├─ UserDefinedIPdu
├─ UserDefinedPdu
├─ VariableAccess
├─ VariableAndParameterInterfaceMapping
├─ VariationPoint
├─ VlanConfig
├─ WhitespaceControlled
│  ├─ LPlainText
│  ├─ LVerbatim
│  ├─ MixedContentForPlainText
│  │  └─ LPlainText
│  └─ MixedContentForVerbatim
│     └─ LVerbatim
└─ WorstCaseStackUsage
```
