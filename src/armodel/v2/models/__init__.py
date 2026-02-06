"""
AUTOSAR V2 Models - Clean import architecture.

V2 Implementation:
- Absolute imports only (CODING_RULE_V2_00001)
- No TYPE_CHECKING (CODING_RULE_V2_00002)
- Explicit __all__ exports (CODING_RULE_V2_00003)
- String annotations for forward refs (CODING_RULE_V2_00005)
- V2 module path convention (CODING_RULE_V2_00004)

Compatible with V1 API.
"""

# ruff: noqa: F401  # Dynamically exported via __all__ generation at end of file

# Version
__version__ = "2.0.0"

# MSR imports
from armodel.v2.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import (
    AUTOSAR,
    AbstractAUTOSAR,
    AUTOSARDoc,
    FileInfoComment,
)
from armodel.v2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior import (
    BswApiOptions,
    BswAsynchronousServerCallPoint,
    BswAsynchronousServerCallResultPoint,
    BswAsynchronousServerCallReturnsEvent,
    BswBackgroundEvent,
    BswCalledEntity,
    BswDataReceivedEvent,
    BswDataReceptionPolicy,
    BswDirectCallPoint,
    BswDistinguishedPartition,
    BswEvent,
    BswExclusiveAreaPolicy,
    BswExternalTriggerOccurredEvent,
    BswInternalBehavior,
    BswInternalTriggeringPoint,
    BswInternalTriggerOccurredEvent,
    BswInterruptCategory,
    BswInterruptEntity,
    BswInterruptEvent,
    BswModeManagerErrorEvent,
    BswModeReceiverPolicy,
    BswModeSenderPolicy,
    BswModeSwitchAckRequest,
    BswModeSwitchedAckEvent,
    BswModeSwitchEvent,
    BswModuleCallPoint,
    BswModuleEntity,
    BswOperationInvokedEvent,
    BswOsTaskExecutionEvent,
    BswQueuedDataReceptionPolicy,
    BswSchedulableEntity,
    BswScheduleEvent,
    BswSchedulerNamePrefix,
    BswServiceDependency,
    BswSynchronousServerCallPoint,
    BswTimingEvent,
    BswTriggerDirectImplementation,
    BswVariableAccess,
    RoleBasedBswModuleEntryAssignment,
)
from armodel.v2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswImplementation import (
    BswImplementation,
)
from armodel.v2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces import (
    BswCallType,
    BswEntryKindEnum,
    BswEntryRelationship,
    BswEntryRelationshipEnum,
    BswEntryRelationshipSet,
    BswExecutionContext,
    BswModuleClientServerEntry,
    BswModuleDependency,
    BswModuleEntry,
)
from armodel.v2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswOverview import (
    BswModuleDescription,
)
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.Filter import (
    DataFilter,
    DataFilterTypeEnum,
)
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.FlatMap import (
    AliasNameAssignment,
    AliasNameSet,
    FlatInstanceDescriptor,
    FlatMap,
    RtePluginProps,
)
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.Implementation import (
    Code,
    Compiler,
    DependencyOnArtifact,
    DependencyUsageEnum,
    Implementation,
    ImplementationProps,
    Linker,
    ProgramminglanguageEnum,
)
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.ImplementationDataTypes import (
    AbstractImplementationDataType,
    AbstractImplementationDataTypeElement,
    ArrayImplPolicyEnum,
    ArraySizeSemanticsEnum,
    ImplementationDataType,
    ImplementationDataTypeElement,
)
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior import (
    AbstractEvent,
    ApiPrincipleEnum,
    ExclusiveArea,
    ExclusiveAreaNestingOrder,
    ExecutableEntity,
    ExecutableEntityActivationReason,
    InternalBehavior,
    ReentrancyLevelEnum,
)
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration import (
    ModeActivationKind,
    ModeDeclaration,
    ModeDeclarationGroup,
    ModeDeclarationGroupPrototype,
    ModeDeclarationGroupPrototypeMapping,
    ModeErrorBehavior,
    ModeErrorReactionPolicyEnum,
    ModeRequestTypeMap,
    ModeTransition,
)
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption import (
    ResourceConsumption,
)

# Additional CommonStructure imports
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.HardwareConfiguration import (
    HardwareConfiguration,
)
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.HeapUsage import (
    HeapUsage,
    MeasuredHeapUsage,
    RoughEstimateHeapUsage,
    WorstCaseHeapUsage,
)
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.MemorySectionUsage import (
    MemorySection,
    SectionNamePrefix,
)
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.SoftwareContext import (
    SoftwareContext,
)
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.StackUsage import (
    MeasuredStackUsage,
    RoughEstimateStackUsage,
    StackUsage,
    WorstCaseStackUsage,
)
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import (
    BswMgrNeeds,
    ComMgrUserNeeds,
    CryptoKeyManagementNeeds,
    CryptoServiceJobNeeds,
    CryptoServiceNeeds,
    DevelopmentError,
    DiagEventDebounceAlgorithm,
    DiagEventDebounceCounterBased,
    DiagEventDebounceMonitorInternal,
    DiagEventDebounceTimeBased,
    DiagnosticAudienceEnum,
    DiagnosticCapabilityElement,
    DiagnosticClearDtcNotificationEnum,
    DiagnosticCommunicationManagerNeeds,
    DiagnosticComponentNeeds,
    DiagnosticControlNeeds,
    DiagnosticDenominatorConditionEnum,
    DiagnosticEnableConditionNeeds,
    DiagnosticEventInfoNeeds,
    DiagnosticEventManagerNeeds,
    DiagnosticEventNeeds,
    DiagnosticIoControlNeeds,
    DiagnosticMonitorUpdateKindEnum,
    DiagnosticOperationCycleNeeds,
    DiagnosticProcessingStyleEnum,
    DiagnosticRequestFileTransferNeeds,
    DiagnosticRoutineNeeds,
    DiagnosticRoutineTypeEnum,
    DiagnosticsCommunicationSecurityNeeds,
    DiagnosticServiceRequestCallbackTypeEnum,
    DiagnosticStorageConditionNeeds,
    DiagnosticUploadDownloadNeeds,
    DiagnosticValueAccessEnum,
    DiagnosticValueNeeds,
    DltUserNeeds,
    DoIpActivationLineNeeds,
    DoIpGidNeeds,
    DoIpGidSynchronizationNeeds,
    DoIpPowerModeStatusNeeds,
    DoIpRoutingActivationAuthenticationNeeds,
    DoIpRoutingActivationConfirmationNeeds,
    DoIpServiceNeeds,
    DtcFormatTypeEnum,
    DtcKindEnum,
    DtcStatusChangeNotificationNeeds,
    EcuStateMgrUserNeeds,
    ErrorTracerNeeds,
    EventAcceptanceStatusEnum,
    FunctionInhibitionAvailabilityNeeds,
    FunctionInhibitionNeeds,
    FurtherActionByteNeeds,
    GlobalSupervisionNeeds,
    HardwareTestNeeds,
    IdsMgrCustomTimestampNeeds,
    IdsMgrNeeds,
    IndicatorStatusNeeds,
    J1939DcmDm19Support,
    J1939RmIncomingRequestServiceNeeds,
    J1939RmOutgoingRequestServiceNeeds,
    MaxCommModeEnum,
    NvBlockNeeds,
    NvBlockNeedsReliabilityEnum,
    NvBlockNeedsWritingPriorityEnum,
    ObdControlServiceNeeds,
    ObdInfoServiceNeeds,
    ObdMonitorServiceNeeds,
    ObdPidServiceNeeds,
    ObdRatioConnectionKindEnum,
    ObdRatioDenominatorNeeds,
    ObdRatioServiceNeeds,
    OperationCycleTypeEnum,
    RamBlockStatusControlEnum,
    RoleBasedDataAssignment,
    RoleBasedDataTypeAssignment,
    RuntimeError,
    SecureOnBoardCommunicationNeeds,
    ServiceDependency,
    ServiceDiagnosticRelevanceEnum,
    ServiceNeeds,
    ServiceProviderEnum,
    StorageConditionStatusEnum,
    SupervisedEntityCheckpointNeeds,
    SupervisedEntityNeeds,
    SymbolicNameProps,
    SyncTimeBaseMgrUserNeeds,
    TracedFailure,
    TransientFault,
    V2xDataManagerNeeds,
    V2xFacUserNeeds,
    V2xMUserNeeds,
    VendorSpecificServiceNeeds,
    VerificationStatusIndicationModeEnum,
    WarningIndicatorRequestedBitNeeds,
)
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.AbstractBlueprintStructure.AtpBlueprint import (
    AtpBlueprint,
    AtpBlueprintable,
    AtpBlueprintMapping,
)
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.BlueprintDedicated.PortPrototypeBlueprint import (
    PortPrototypeBlueprint,
    PortPrototypeBlueprintInitValue,
)
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.Keyword import (
    Keyword,
    KeywordSet,
)
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.SwcBswMapping import (
    SwcBswMapping,
    SwcBswRunnableMapping,
    SwcBswSynchronizedModeGroupPrototype,
    SwcBswSynchronizedTrigger,
)
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.ExecutionOrderConstraint import (
    EOCEventRef,
    EOCExecutableEntityRef,
    EOCExecutableEntityRefAbstract,
    EOCExecutableEntityRefGroup,
    ExecutionOrderConstraint,
    ExecutionOrderConstraintTypeEnum,
    LetDataExchangeParadigmEnum,
)
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.TimingConstraint import (
    TimingConstraint,
)
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingExtensions import (
    SwcTiming,
    TimingExtension,
)
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.Timing.Traceable import (
    Traceable,
)
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.TriggerDeclaration import (
    Trigger,
    TriggerMapping,
)

# Additional DiagnosticExtract imports
from armodel.v2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics import (
    DiagnosticCommonElement,
)
from armodel.v2.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticContribution import (
    DiagnosticServiceTable,
)
from armodel.v2.models.M2.AUTOSARTemplates.ECUCDescriptionTemplate import (
    EcucAbstractReferenceValue,
    EcucAddInfoParamValue,
    EcucConditionSpecification,
    EcucConfigurationVariantEnum,
    EcucContainerValue,
    EcucIndexableValue,
    EcucInstanceReferenceValue,
    EcucModuleConfigurationValues,
    EcucNumericalParamValue,
    EcucParameterValue,
    EcucReferenceValue,
    EcucTextualParamValue,
    EcucValueCollection,
)

# ECUCParameterDefTemplate
from armodel.v2.models.M2.AUTOSARTemplates.EcuResourceTemplate.HwElementCategory import (
    HwAttributeDef,
    HwAttributeLiteralDef,
    HwAttributeValue,
    HwCategory,
    HwType,
)

# Additional EcuResourceTemplate imports
from armodel.v2.models.M2.AUTOSARTemplates.EcuResourceTemplate.HwElementConnector import (
    HwElementConnector,
)

# GenericStructure imports
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import (
    AtpClassifier,
    AtpFeature,
    AtpInstanceRef,
    AtpPrototype,
    AtpStructureElement,
    AtpType,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.AnyInstanceRef import (
    AnyInstanceRef,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    ARPackage,
    ReferenceBase,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ElementCollection import (
    CollectableElement,
    Collection,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.EngineeringObject import (
    AutosarEngineeringObject,
    EngineeringObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Enumerations import (
    AutoCollectEnum,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    ARElement,
    Describable,
    Identifiable,
    MultilanguageReferrable,
    PackageableElement,
    Referrable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ARBoolean,
    AREnum,
    ARFloat,
    ArgumentDirectionEnum,
    ARLiteral,
    ARNumerical,
    ARPositiveInteger,
    ARType,
    Boolean,
    ByteOrderEnum,
    CategoryString,
    CIdentifier,
    DateTime,
    DiagRequirementIdString,
    Float,
    Identifier,
    Integer,
    Ip4AddressString,
    Ip6AddressString,
    Limit,
    MacAddressString,
    NameToken,
    PositiveInteger,
    PositiveUnlimitedInteger,
    ReferrableSubtypesEnum,
    RefType,
    RegularExpression,
    RevisionLabelString,
    String,
    TimeValue,
    TRefType,
    UnlimitedInteger,
    VerbatimString,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.LifeCycles import (
    LifeCycleInfo,
    LifeCycleInfoSet,
    LifeCyclePeriod,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.RolesAndRights.AtpDefinition import (
    AtpDefinition,
)

# Explicit import from SWComponentTemplate for all exported classes
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate import (
    # Datatype
    ApplicationArrayDataType,
    ApplicationArrayElement,
    ApplicationCompositeDataType,
    ApplicationCompositeElementDataPrototype,
    ApplicationDataType,
    # PortInterface
    ApplicationError,
    ApplicationPrimitiveDataType,
    ApplicationRecordDataType,
    ApplicationRecordElement,
    ArgumentDataPrototype,
    # Composition
    AssemblySwConnector,
    AutosarDataPrototype,
    AutosarDataType,
    # Communication
    ClientComSpec,
    ClientServerApplicationErrorMapping,
    ClientServerInterface,
    ClientServerInterfaceMapping,
    ClientServerOperation,
    ClientServerOperationMapping,
    CompositeNetworkRepresentation,
    CompositionSwComponentType,
    DataInterface,
    # ApplicationAttributes
    DataLimitKindEnum,
    DataPrototype,
    DataPrototypeMapping,
    DataTypeMap,
    DataTypeMappingSet,
    DelegationSwConnector,
    # EndToEndProtection
    EndToEndDescription,
    EndToEndProtection,
    EndToEndProtectionISignalIPdu,
    EndToEndProtectionSet,
    EndToEndProtectionVariablePrototype,
    # RPTScenario
    ExternalTriggeringPointIdent,
    FilterDebouncingEnum,
    HandleInvalidEnum,
    HandleOutOfRangeEnum,
    HandleOutOfRangeStatusEnum,
    HandleTimeoutEnum,
    IdentCaption,
    InvalidationPolicy,
    MetaDataItem,
    MetaDataItemSet,
    ModeAccessPointIdent,
    ModeDeclarationMapping,
    ModeDeclarationMappingSet,
    ModeInterfaceMapping,
    ModeSwitchedAckRequest,
    ModeSwitchInterface,
    ModeSwitchReceiverComSpec,
    ModeSwitchSenderComSpec,
    NonqueuedReceiverComSpec,
    NonqueuedSenderComSpec,
    NvDataInterface,
    NvProvideComSpec,
    NvRequireComSpec,
    ParameterDataPrototype,
    ParameterInterface,
    ParameterProvideComSpec,
    ParameterRequireComSpec,
    PassThroughSwConnector,
    PortInterface,
    PortInterfaceMapping,
    PortInterfaceMappingSet,
    PPortComSpec,
    # Components
    PPortPrototype,
    ProcessingKindEnum,
    PulseTestEnum,
    QueuedReceiverComSpec,
    QueuedSenderComSpec,
    ReceiverComSpec,
    RPortComSpec,
    SenderComSpec,
    SenderReceiverInterface,
    ServerComSpec,
    SignalFanEnum,
    # SwcImplementation
    SwcImplementation,
    # SoftwareComponentDocumentation
    SwComponentDocumentation,
    SwComponentPrototype,
    # SwComponentType
    SwComponentType,
    SwConnector,
    TextTableMapping,
    TransformationComSpecProps,
    TransmissionAcknowledgementRequest,
    TransmissionModeDefinitionEnum,
    TriggerInterface,
    TriggerInterfaceMapping,
    UserDefinedTransformationComSpecProps,
    VariableAndParameterInterfaceMapping,
    VariableDataPrototype,
)
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping import (
    DataMapping,
    IndexedArrayElement,
    SenderRecArrayElementMapping,
    SenderRecArrayTypeMapping,
    SenderRecCompositeTypeMapping,
    SenderReceiverToSignalGroupMapping,
    SenderReceiverToSignalMapping,
    SenderRecRecordElementMapping,
    SenderRecRecordTypeMapping,
)
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.DiagnosticConnection import (
    DiagnosticConnection,
)
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.DoIP import (
    AbstractDoIpLogicAddressProps,
    DoIpLogicTargetAddressProps,
    DoIpLogicTesterAddressProps,
)
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.ECUResourceMapping import (
    ECUMapping,
)
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanCommunication import (
    CanFrame,
    CanFrameTriggering,
    RxIdentifierRange,
)
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology import (
    AbstractCanCommunicationConnector,
    AbstractCanCommunicationController,
    AbstractCanCommunicationControllerAttributes,
    CanCommunicationConnector,
    CanCommunicationController,
    CanControllerConfigurationRequirements,
    CanControllerFdConfiguration,
    CanControllerFdConfigurationRequirements,
    CanControllerXlConfiguration,
    CanControllerXlConfigurationRequirements,
)
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetCommunication import (
    SoAdRoutingGroup,
    SocketConnection,
    SocketConnectionBundle,
    SocketConnectionIpduIdentifier,
)
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetFrame import (
    AbstractEthernetFrame,
    GenericEthernetFrame,
)
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    CouplingPort,
    CouplingPortDetails,
    CouplingPortFifo,
    CouplingPortScheduler,
    CouplingPortStructuralElement,
    EthernetCluster,
    EthernetCommunicationConnector,
    EthernetCommunicationController,
    EthernetPriorityRegeneration,
    InitialSdDelayConfig,
    MacMulticastGroup,
    RequestResponseDelay,
    SdClientConfig,
    VlanMembership,
)
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.NetworkEndpoint import (
    DoIpEntity,
    InfrastructureServices,
    Ipv4Configuration,
    Ipv6Configuration,
    NetworkEndpoint,
    NetworkEndpointAddress,
    TimeSyncClientConfiguration,
    TimeSynchronization,
    TimeSyncServerConfiguration,
)
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Flexray.FlexrayCommunication import (
    FlexrayAbsolutelyScheduledTiming,
    FlexrayFrame,
    FlexrayFrameTriggering,
)

# Additional SystemTemplate imports
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Flexray.FlexrayTopology import (
    FlexrayChannelName,
    FlexrayCluster,
    FlexrayCommunicationConnector,
    FlexrayCommunicationController,
)
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication import (
    ApplicationEntry,
    FreeFormatEntry,
    LinConfigurationEntry,
    LinFrame,
    LinFrameTriggering,
    LinScheduleTable,
    LinUnconditionalFrame,
    ResumePosition,
    ScheduleTableEntry,
)
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinTopology import (
    LinCommunicationConnector,
    LinCommunicationController,
    LinMaster,
)
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Multiplatform import (
    DefaultValueElement,
    FrameMapping,
    Gateway,
    IPduMapping,
    ISignalMapping,
    PduMappingDefaultValue,
    TargetIPduRef,
)
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (
    CommunicationDirectionType,
    ContainedIPduProps,
    DcmIPdu,
    DynamicPart,
    DynamicPartAlternative,
    FibexElement,
    Frame,
    FrameTriggering,
    GeneralPurposeIPdu,
    GeneralPurposePdu,
    IPdu,
    IPduSignalProcessingEnum,
    IPduTiming,
    ISignal,
    ISignalGroup,
    ISignalIPdu,
    ISignalIPduGroup,
    ISignalToIPduMapping,
    ISignalTriggering,
    MultiplexedIPdu,
    MultiplexedPart,
    NmPdu,
    NPdu,
    Pdu,
    PduToFrameMapping,
    PduTriggering,
    SecureCommunicationAuthenticationProps,
    SecureCommunicationFreshnessProps,
    SecureCommunicationProps,
    SecureCommunicationPropsSet,
    SecuredIPdu,
    SegmentPosition,
    StaticPart,
    SystemSignal,
    SystemSignalGroup,
    UserDefinedIPdu,
    UserDefinedPdu,
)
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.Timing import (
    CyclicTiming,
    EventControlledTiming,
    ModeDrivenTransmissionModeCondition,
    TimeRangeType,
    TransmissionModeCondition,
    TransmissionModeDeclaration,
    TransmissionModeTiming,
)
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import (
    AbstractCanCluster,
    AbstractCanPhysicalChannel,
    CanCluster,
    CanClusterBusOffRecovery,
    CanPhysicalChannel,
    CommConnectorPort,
    CommunicationCluster,
    CommunicationConnector,
    CommunicationController,
    CommunicationCycle,
    CycleCounter,
    CycleRepetition,
    CycleRepetitionType,
    EcuInstance,
    EthernetPhysicalChannel,
    FlexrayPhysicalChannel,
    FramePort,
    IPduPort,
    ISignalPort,
    LinCluster,
    LinPhysicalChannel,
    PhysicalChannel,
    PncGatewayTypeEnum,
    VlanConfig,
)
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.InstanceRefs import (
    ComponentInSystemInstanceRef,
    VariableDataPrototypeInSystemInstanceRef,
)
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement import (
    BusspecificNmEcu,
    CanNmCluster,
    CanNmClusterCoupling,
    CanNmEcu,
    CanNmNode,
    FlexrayNmCluster,
    FlexrayNmClusterCoupling,
    FlexrayNmEcu,
    FlexrayNmNode,
    J1939NmCluster,
    J1939NmEcu,
    J1939NmNode,
    NmCluster,
    NmClusterCoupling,
    NmConfig,
    NmEcu,
    NmNode,
    UdpNmCluster,
    UdpNmClusterCoupling,
    UdpNmEcu,
    UdpNmNode,
)
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.RteEventToOsTaskMapping import (
    AppOsTaskProxyToEcuTaskProxyMapping,
)
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication import (
    CryptoServiceMapping,
    SecOcCryptoServiceMapping,
    TlsCryptoServiceMapping,
)
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.SWmapping import (
    ApplicationPartitionToEcuPartitionMapping,
    SwcToEcuMapping,
    SwcToImplMapping,
)
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols import (
    CanTpAddress,
    CanTpChannel,
    CanTpConfig,
    CanTpConnection,
    CanTpEcu,
    CanTpNode,
    DoIpLogicAddress,
    DoIpTpConfig,
    DoIpTpConnection,
    LinTpConfig,
    LinTpConnection,
    LinTpNode,
    TpAddress,
    TpConfig,
    TpConnection,
    TpConnectionIdent,
)
from armodel.v2.models.M2.MSR.AsamHdo.AdminData import (
    AdminData,
    DocRevision,
    Modification,
)
from armodel.v2.models.M2.MSR.AsamHdo.BaseTypes import (
    BaseType,
    BaseTypeDefinition,
    BaseTypeDirectDefinition,
    SwBaseType,
)
from armodel.v2.models.M2.MSR.AsamHdo.ComputationMethod import (
    Compu,
    CompuConst,
    CompuConstContent,
    CompuConstFormulaContent,
    CompuConstNumericContent,
    CompuConstTextContent,
    CompuContent,
    CompuMethod,
    CompuNominatorDenominator,
    CompuRationalCoeffs,
    CompuScale,
    CompuScaleConstantContents,
    CompuScaleContents,
    CompuScaleRationalFormula,
    CompuScales,
)
from armodel.v2.models.M2.MSR.AsamHdo.Constraints.GlobalConstraints import (
    DataConstr,
    DataConstrRule,
    InternalConstrs,
    PhysConstrs,
)
from armodel.v2.models.M2.MSR.AsamHdo.SpecialData import (
    Sd,
    Sdg,
    SdgCaption,
)
from armodel.v2.models.M2.MSR.AsamHdo.Units import (
    PhysicalDimension,
    SingleLanguageUnitNames,
    Unit,
    UnitGroup,
)

# Additional MSR imports
from armodel.v2.models.M2.MSR.CalibrationData import (
    SwValueCont,
    SwValues,
)
from armodel.v2.models.M2.MSR.DataDictionary import (
    SwAddrMethod,
    SwAxisGeneric,
    SwAxisGrouped,
    SwAxisIndividual,
    SwCalprmAxis,
    SwCalprmAxisSet,
    SwCalprmAxisTypeProps,
    SwDataDefProps,
    SwDataDefPropsConditional,
    SwGenericAxisParam,
    SwImplPolicyEnum,
    SwPointerTargetProps,
    SwRecordLayout,
    SwRecordLayoutGroup,
    SwRecordLayoutGroupContent,
    SwRecordLayoutV,
    SwServiceArg,
    SwServiceImplPolicyEnum,
    SwSystemconst,
    SwTextProps,
    ValueList,
)
from armodel.v2.models.M2.MSR.Documentation import (
    Annotation,
    ARList,
    DocumentationBlock,
    DocumentViewSelectable,
    GeneralAnnotation,
    Graphic,
    GraphicFitEnum,
    Item,
    LanguageSpecific,
    LEnum,
    LGraphic,
    ListEnum,
    LLongName,
    LOverviewParagraph,
    LParagraph,
    LPlainText,
    Map,
    MlFigure,
    MlFormula,
    MultilanguageLongName,
    MultiLanguageOverviewParagraph,
    MultiLanguageParagraph,
    MultiLanguagePlainText,
    Paginateable,
)

# utils
from armodel.v2.models.utils.uuid_mgr import (
    UUIDMgr,
)

# NOTE: Some classes in subdirectories with name collisions cannot be directly imported:
# - BswBehavior/*.py files (9 classes)
# - BswInterfaces/*.py files (3 classes)
# - BswOverview/InstanceRefs/*.py files (1 class)
# These are accessible via their full import paths, e.g.:
# from armodel.v2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.BswAsynchronousServerCallReturnsEvent

# Define __all__ to enable re-export of wildcard imports
# Start with version
__all__ = ['__version__']

# This collects all public names (not starting with _) for re-export
_all_exports = [name for name in globals() if not name.startswith('_')]
__all__.extend(_all_exports)
