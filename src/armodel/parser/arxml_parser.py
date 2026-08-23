import os
import xml.etree.ElementTree as ET
from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior import (
    BswApiOptions,
    BswAsynchronousServerCallPoint,
    BswAsynchronousServerCallReturnsEvent,
    BswBackgroundEvent,
    BswCalledEntity,
    BswDataReceivedEvent,
    BswDataReceptionPolicy,
    BswExternalTriggerOccurredEvent,
    BswInternalBehavior,
    BswInternalTriggeringPoint,
    BswInternalTriggerOccurredEvent,
    BswInterruptEntity,
    BswModeManagerErrorEvent,
    BswModeSenderPolicy,
    BswModeSwitchAckRequest,
    BswModeSwitchedAckEvent,
    BswModeSwitchEvent,
    BswModuleCallPoint,
    BswModuleEntity,
    BswOperationInvokedEvent,
    BswQueuedDataReceptionPolicy,
    BswSchedulableEntity,
    BswScheduleEvent,
    BswServiceDependency,
    BswServiceDependencyIdent,
    BswSynchronousServerCallPoint,
    BswTimingEvent,
    BswVariableAccess,
    RoleBasedBswModuleEntryAssignment,
)
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswImplementation import BswImplementation
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces import BswModuleClientServerEntry, BswModuleEntry
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswOverview import BswModuleDescription
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswOverview.InstanceRefs import ModeInBswModuleDescriptionInstanceRef
from armodel.models.M2.AUTOSARTemplates.CommonStructure import (
    ApplicationRuleBasedValueSpecification,
    ApplicationValueSpecification,
    ArrayValueSpecification,
    CompositeRuleBasedValueSpecification,
    ConstantReference,
    ConstantSpecification,
    NumericalValueSpecification,
    RecordValueSpecification,
    RuleArguments,
    RuleBasedAxisCont,
    RuleBasedValueCont,
    RuleBasedValueSpecification,
    TextValueSpecification,
    ValueSpecification,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants import NumericalOrText
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Filter import DataFilter
from armodel.models.M2.AUTOSARTemplates.CommonStructure.FlatMap import FlatInstanceDescriptor, FlatMap
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Implementation import Code, DependencyUsageEnum, Implementation, ImplementationProps
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ImplementationDataTypes import ImplementationDataType, ImplementationDataTypeElement
from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior import ExecutableEntity, ExecutableEntityActivationReason, InternalBehavior
from armodel.models.M2.AUTOSARTemplates.CommonStructure.McGroups import McGroup, McGroupDataRefSet
from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport import (
    ImplementationElementInParameterInstanceRef,
    McDataAccessDetails,
    McDataInstance,
    McFunction,
    McParameterElementGroup,
    McSupportData,
    McSwEmulationMethodSupport,
    RoleBasedMcDataAssignment,
    RteEventInEcuInstanceRef,
    VariableAccessInEcuInstanceRef,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.RptSupport import (
    McFunctionDataRefSet,
    RptComponent,
    RptExecutableEntity,
    RptExecutableEntityEvent,
    RptServicePoint,
    RptSupportData,
    RptSwPrototypingAccess,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration import (
    ModeActivationKind,
    ModeDeclarationGroup,
    ModeDeclarationGroupPrototype,
    ModeDeclarationGroupPrototypeMapping,
    ModeErrorBehavior,
    ModeErrorReactionPolicyEnum,
    ModeRequestTypeMap,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption import HardwareConfiguration, ResourceConsumption, SoftwareContext
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.ExecutionTime import (
    AnalyzedExecutionTime,
    MeasuredExecutionTime,
    MemorySectionLocation,
    RoughEstimateOfExecutionTime,
    SimulatedExecutionTime,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.HeapUsage import MeasuredHeapUsage, RoughEstimateHeapUsage, WorstCaseHeapUsage
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.MemorySectionUsage import MemorySection
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.StackUsage import MeasuredStackUsage, RoughEstimateStackUsage, StackUsage, WorstCaseStackUsage
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import (
    BswMgrNeeds,
    ComMgrUserNeeds,
    CryptoServiceNeeds,
    DevelopmentError,
    DiagEventDebounceCounterBased,
    DiagEventDebounceMonitorInternal,
    DiagEventDebounceTimeBased,
    DiagnosticCapabilityElement,
    DiagnosticCommunicationManagerNeeds,
    DiagnosticEnableConditionNeeds,
    DiagnosticEventInfoNeeds,
    DiagnosticEventNeeds,
    DiagnosticIoControlNeeds,
    DiagnosticOperationCycleNeeds,
    DiagnosticRoutineNeeds,
    DiagnosticStorageConditionNeeds,
    DiagnosticValueNeeds,
    DltUserNeeds,
    DoIpRoutingActivationAuthenticationNeeds,
    DoIpRoutingActivationConfirmationNeeds,
    DtcStatusChangeNotificationNeeds,
    EcuStateMgrUserNeeds,
    ErrorTracerNeeds,
    FunctionInhibitionAvailabilityNeeds,
    IdsMgrNeeds,
    IndicatorStatusNeeds,
    NvBlockNeeds,
    ObdControlServiceNeeds,
    ObdInfoServiceNeeds,
    ObdMonitorServiceNeeds,
    ObdPidServiceNeeds,
    ObdRatioDenominatorNeeds,
    ObdRatioServiceNeeds,
    PossibleErrorReaction,
    RoleBasedDataAssignment,
    RoleBasedDataTypeAssignment,
    RuntimeError,
    SecureOnBoardCommunicationNeeds,
    ServiceDependency,
    ServiceNeeds,
    SupervisedEntityNeeds,
    SymbolicNameProps,
    TracedFailure,
    TransientFault,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.SignalServiceTranslation import (
    SignalServiceTranslationElementProps,
    SignalServiceTranslationEventProps,
    SignalServiceTranslationProps,
    SignalServiceTranslationPropsSet,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.BlueprintDedicated.PortPrototypeBlueprint import PortPrototypeBlueprint
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.BlueprintGenerator.BlueprintGenerator import BlueprintGenerator
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.Keyword import Keyword, KeywordSet
from armodel.models.M2.AUTOSARTemplates.CommonStructure.SwcBswMapping import SwcBswMapping, SwcBswRunnableMapping, SwcBswSynchronizedModeGroupPrototype, SwcBswSynchronizedTrigger
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.ExecutionOrderConstraint import ExecutionOrderConstraint
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.TimingExtensions import SwcTiming, TimingExtension
from armodel.models.M2.AUTOSARTemplates.CommonStructure.TriggerDeclaration import Trigger
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticContribution import DiagnosticServiceTable
from armodel.models.M2.AUTOSARTemplates.ECUCDescriptionTemplate import (
    EcucAbstractReferenceValue,
    EcucAddInfoParamValue,
    EcucContainerValue,
    EcucInstanceReferenceValue,
    EcucModuleConfigurationValues,
    EcucNumericalParamValue,
    EcucParameterValue,
    EcucReferenceValue,
    EcucTextualParamValue,
    EcucValueCollection,
)
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import (
    EcucAbstractConfigurationClass,
    EcucAbstractExternalReferenceDef,
    EcucAbstractInternalReferenceDef,
    EcucAbstractReferenceDef,
    EcucAbstractStringParamDef,
    EcucBooleanParamDef,
    EcucChoiceContainerDef,
    EcucChoiceReferenceDef,
    EcucCommonAttributes,
    EcucConditionFormula,
    EcucConditionSpecification,
    EcucContainerDef,
    EcucDefinitionCollection,
    EcucDefinitionElement,
    EcucDerivationSpecification,
    EcucDestinationUriDef,
    EcucDestinationUriDefRefType,
    EcucDestinationUriDefSet,
    EcucDestinationUriNestingContractEnum,
    EcucDestinationUriPolicy,
    EcucEnumerationLiteralDef,
    EcucEnumerationParamDef,
    EcucFloatParamDef,
    EcucFunctionNameDef,
    EcucInstanceReferenceDef,
    EcucIntegerParamDef,
    EcucModuleDef,
    EcucMultilineStringParamDef,
    EcucMultiplicityConfigurationClass,
    EcucParamConfContainerDef,
    EcucParameterDef,
    EcucParameterDerivationFormula,
    EcucQuery,
    EcucQueryExpression,
    EcucReferenceDef,
    EcucStringParamDef,
    EcucSymbolicNameReferenceDef,
    EcucValidationCondition,
    EcucValueConfigurationClass,
)
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate import HwDescriptionEntity, HwElement, HwElementConnector, HwPin, HwPinConnector, HwPinGroup, HwPinGroupConnector
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.HwAttributeValue import HwAttributeValue
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.HwElementCategory import HwAttributeDef, HwCategory, HwType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.DocumentationOnM1 import Documentation, DocumentationContext
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.AnyInstanceRef import AnyInstanceRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARPackage, ReferenceBase
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ElementCollection import Collection
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.EngineeringObject import AutosarEngineeringObject, EngineeringObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Enumerations import BindingTimeEnum
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import ARElement, Describable, Identifiable, MultilanguageReferrable, Referrable, ShortNameFragment
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime import MultidimensionalTime
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ARLiteral,
    IntervalTypeEnum,
    NameToken,
    Numerical,
    PrimitiveIdentifier,
    RefType,
    SectionInitializationPolicyType,
    String,
    VerbatimString,
    VerbatimStringPlain,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.LifeCycles import LifeCycleInfo, LifeCycleInfoSet, LifeCyclePeriod
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import (
    ConditionByFormula,
    PostBuildVariantCondition,
    PostBuildVariantCriterion,
    PredefinedVariant,
    SwSystemconstantValueSet,
    SwSystemconstValue,
    VariationPoint,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling.AttributeValueVariationPoints import (
    AttributeValueVariationPoint,
    BooleanValueVariationPoint,
    FloatValueVariationPoint,
    IntegerValueVariationPoint,
    LimitValueVariationPoint,
    NumericalValueVariationPoint,
    PositiveIntegerValueVariationPoint,
    TimeValueValueVariationPoint,
    UnlimitedIntegerValueVariationPoint,
)

VALUE_ACCESS_TAG_TO_CLASS = {
    "LIMIT": LimitValueVariationPoint,
    "NUMERICAL-VALUE-VARIATION-POINT": NumericalValueVariationPoint,
    "BOOLEAN-VALUE-VARIATION-POINT": BooleanValueVariationPoint,
    "FLOAT-VALUE-VARIATION-POINT": FloatValueVariationPoint,
    "INTEGER-VALUE-VARIATION-POINT": IntegerValueVariationPoint,
    "POSITIVE-INTEGER-VALUE-VARIATION-POINT": PositiveIntegerValueVariationPoint,
    "TIME-VALUE-VARIATION-POINT": TimeValueValueVariationPoint,
    "UNLIMITED-INTEGER-VALUE-VARIATION-POINT": UnlimitedIntegerValueVariationPoint,
}
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ApplicationAttributes import (
    ClientServerAnnotation,
    DataLimitKindEnum,
    DelegatedPortAnnotation,
    FilterDebouncingEnum,
    IoHwAbstractionServerAnnotation,
    ModePortAnnotation,
    NvDataPortAnnotation,
    ParameterPortAnnotation,
    ProcessingKindEnum,
    PulseTestEnum,
    SenderReceiverAnnotation,
    SignalFanEnum,
    TriggerPortAnnotation,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import (
    ClientComSpec,
    CompositeNetworkRepresentation,
    ModeSwitchedAckRequest,
    ModeSwitchReceiverComSpec,
    ModeSwitchSenderComSpec,
    NonqueuedReceiverComSpec,
    NonqueuedSenderComSpec,
    NvProvideComSpec,
    NvRequireComSpec,
    ParameterProvideComSpec,
    ParameterRequireComSpec,
    PPortComSpec,
    QueuedReceiverComSpec,
    QueuedSenderComSpec,
    ReceiverComSpec,
    ReceptionComSpecProps,
    RPortComSpec,
    SenderComSpec,
    ServerComSpec,
    TransformationComSpecProps,
    TransmissionAcknowledgementRequest,
    TransmissionComSpecProps,
    UserDefinedTransformationComSpecProps,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components import (
    AbstractProvidedPortPrototype,
    AbstractRequiredPortPrototype,
    ApplicationSwComponentType,
    AtomicSwComponentType,
    ComplexDeviceDriverSwComponentType,
    EcuAbstractionSwComponentType,
    NvBlockSwComponentType,
    PortGroup,
    PortPrototype,
    PPortPrototype,
    PRPortPrototype,
    RPortPrototype,
    SensorActuatorSwComponentType,
    ServiceProxySwComponentType,
    ServiceSwComponentType,
    SwComponentType,
    SymbolProps,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs import (
    InnerPortGroupInCompositionInstanceRef,
    ModeGroupInAtomicSwcInstanceRef,
    PModeGroupInAtomicSwcInstanceRef,
    PTriggerInAtomicSwcTypeInstanceRef,
    RModeGroupInAtomicSWCInstanceRef,
    RModeInAtomicSwcInstanceRef,
    RVariableInAtomicSwcInstanceRef,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition import (
    AssemblySwConnector,
    CompositionSwComponentType,
    DelegationSwConnector,
    InstantiationTimingEventProps,
    PassThroughSwConnector,
    SwComponentPrototype,
    SwConnector,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.InstanceRefs import (
    InstanceEventInCompositionInstanceRef,
    POperationInAtomicSwcInstanceRef,
    PPortInCompositionInstanceRef,
    ROperationInAtomicSwcInstanceRef,
    RPortInCompositionInstanceRef,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes import (
    ApplicationCompositeElementDataPrototype,
    ApplicationRecordElement,
    AutosarDataPrototype,
    DataPrototype,
    ParameterDataPrototype,
    VariableDataPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes import (
    ApplicationArrayDataType,
    ApplicationCompositeDataType,
    ApplicationDataType,
    ApplicationPrimitiveDataType,
    ApplicationRecordDataType,
    AutosarDataType,
    DataTypeMap,
    DataTypeMappingSet,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.EndToEndProtection import (
    EndToEndDescription,
    EndToEndProtection,
    EndToEndProtectionISignalIPdu,
    EndToEndProtectionSet,
    EndToEndProtectionVariablePrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ImplicitCommunicationBehavior import (
    ConsistencyNeeds,
    DataPrototypeGroup,
    RunnableEntityGroup,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ImplicitCommunicationBehavior.InstanceRefs import (
    InnerDataPrototypeGroupInCompositionInstanceRef,
    InnerRunnableEntityGroupInCompositionInstanceRef,
    RunnableEntityInCompositionInstanceRef,
    VariableDataPrototypeInCompositionInstanceRef,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent import BulkNvDataDescriptor, ModeSwitchEventTriggeredActivity, NvBlockDataMapping, NvBlockDescriptor
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import (
    ArgumentDataPrototype,
    ClientServerInterface,
    ClientServerInterfaceMapping,
    ClientServerOperation,
    ClientServerOperationMapping,
    DataInterface,
    DataPrototypeMapping,
    InvalidationPolicy,
    ModeDeclarationMapping,
    ModeDeclarationMappingSet,
    ModeInterfaceMapping,
    ModeSwitchInterface,
    NvDataInterface,
    ParameterInterface,
    PortInterface,
    PortInterfaceMappingSet,
    SenderReceiverInterface,
    SubElementMapping,
    TextTableMapping,
    TriggerInterface,
    VariableAndParameterInterfaceMapping,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.InstanceRefs import ApplicationCompositeElementInPortInterfaceInstanceRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.RPTScenario import RptExecutableEntityProperties, RptImplPolicy
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SoftwareComponentDocumentation import (
    SwComponentDocumentation,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcImplementation import SwcImplementation
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior import ExternalTriggeringPoint, RunnableEntity, RunnableEntityArgument, SwcExclusiveAreaPolicy, SwcInternalBehavior
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.AccessCount import AccessCount, AccessCountSet
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.AutosarVariableRef import AutosarVariableRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements import ParameterAccess, VariableAccess
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.IncludedDataTypes import IncludedDataTypeSet
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.InstanceRefsUsage import AutosarParameterRef, ParameterInAtomicSWCTypeInstanceRef, VariableInAtomicSWCTypeInstanceRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.InstantiationDataDefProps import InstantiationDataDefProps
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ModeDeclarationGroup import IncludedModeDeclarationGroupSet, ModeAccessPoint, ModeSwitchPoint
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.PortAPIOptions import PortAPIOption, PortDefinedArgumentValue
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents import (
    AsynchronousServerCallReturnsEvent,
    BackgroundEvent,
    DataReceivedEvent,
    DataSendCompletedEvent,
    InitEvent,
    InternalTriggerOccurredEvent,
    ModeSwitchedAckEvent,
    OperationInvokedEvent,
    RTEEvent,
    SwcModeSwitchEvent,
    TimingEvent,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ServerCall import ServerCallPoint
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ServiceMapping import RoleBasedPortAssignment, SwcServiceDependency
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.VariantHandling import VariationPointProxy
from armodel.models.M2.AUTOSARTemplates.SystemTemplate import SwcToEcuMapping, System, SystemMapping
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping import (
    SenderRecCompositeTypeMapping,
    SenderReceiverToSignalGroupMapping,
    SenderReceiverToSignalMapping,
    SenderRecRecordElementMapping,
    SenderRecRecordTypeMapping,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DiagnosticConnection import DiagnosticConnection
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.ECUResourceMapping import ECUMapping
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanCommunication import CanFrame, CanFrameTriggering, RxIdentifierRange
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology import (
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
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetCommunication import SoAdRoutingGroup, SocketConnection, SocketConnectionBundle, SocketConnectionIpduIdentifier
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetFrame import GenericEthernetFrame
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
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
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.NetworkEndpoint import DoIpEntity, InfrastructureServices, Ipv6Configuration, NetworkEndpoint
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import (
    ApplicationEndpoint,
    ConsumedEventGroup,
    ConsumedServiceInstance,
    EventHandler,
    GenericTp,
    ProvidedServiceInstance,
    SdServerConfig,
    SoAdConfig,
    SocketAddress,
    TcpTp,
    TpPort,
    TransportProtocolConfiguration,
    UdpTp,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Flexray.FlexrayCommunication import FlexrayAbsolutelyScheduledTiming, FlexrayFrame, FlexrayFrameTriggering
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Flexray.FlexrayTopology import (
    FlexrayCluster,
    FlexrayCommunicationConnector,
    FlexrayCommunicationController,
    FlexrayFifoConfiguration,
    FlexrayFifoRange,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication import (
    ApplicationEntry,
    LinErrorResponse,
    LinFrameTriggering,
    LinScheduleTable,
    LinUnconditionalFrame,
    ScheduleTableEntry,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinTopology import (
    LinCluster,
    LinCommunicationConnector,
    LinCommunicationController,
    LinConfigurableFrame,
    LinMaster,
    LinOrderedConfigurableFrame,
    LinSlaveConfig,
    LinSlaveConfigIdent,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Multiplatform import Gateway, IPduMapping, ISignalMapping, TargetIPduRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (
    ContainedIPduProps,
    DcmIPdu,
    DynamicPart,
    DynamicPartAlternative,
    Frame,
    FrameTriggering,
    GeneralPurposeIPdu,
    GeneralPurposePdu,
    IPdu,
    IPduTiming,
    ISignal,
    ISignalGroup,
    ISignalIPdu,
    ISignalIPduGroup,
    ISignalProps,
    ISignalToIPduMapping,
    ISignalTriggering,
    MultiplexedIPdu,
    MultiplexedPart,
    NmPdu,
    NPdu,
    Pdu,
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
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import (
    AbstractCanCluster,
    CanCluster,
    CanClusterBusOffRecovery,
    CanPhysicalChannel,
    CommConnectorPort,
    CommunicationCluster,
    CommunicationConnector,
    CommunicationController,
    CommunicationCycle,
    CycleRepetition,
    EthernetPhysicalChannel,
    FlexrayPhysicalChannel,
    FramePort,
    IPduPort,
    ISignalPort,
    LinPhysicalChannel,
    PhysicalChannel,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.EcuInstance import EcuInstance
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.Timing import (
    CyclicTiming,
    EventControlledTiming,
    TimeRangeType,
    TransmissionModeCondition,
    TransmissionModeDeclaration,
    TransmissionModeTiming,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.InstanceRefs import ComponentInSystemInstanceRef, VariableDataPrototypeInSystemInstanceRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement import (
    CanNmCluster,
    CanNmClusterCoupling,
    CanNmNode,
    J1939NmNode,
    J1939NodeName,
    NmCluster,
    NmConfig,
    NmEcu,
    NmNode,
    UdpNmCluster,
    UdpNmClusterCoupling,
    UdpNmEcu,
    UdpNmNode,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SWmapping import SwcToImplMapping
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import (
    BufferProperties,
    DataPrototypeInPortInterfaceRef,
    DataPrototypeInClientServerInterfaceInstanceRef,
    DataPrototypeInSenderReceiverInterfaceInstanceRef,
    DataPrototypeTransformationProps,
    DataTransformation,
    DataTransformationSet,
    E2EProfileCompatibilityProps,
    EndToEndTransformationComSpecProps,
    EndToEndTransformationDescription,
    EndToEndTransformationISignalProps,
    TransformationDescription,
    TransformationISignalProps,
    TransformationTechnology,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols import (
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
)
from armodel.models.M2.MSR.AsamHdo.AdminData import AdminData, DocRevision, Modification
from armodel.models.M2.MSR.AsamHdo.BaseTypes import BaseTypeDirectDefinition, SwBaseType
from armodel.models.M2.MSR.AsamHdo.ComputationMethod import (
    Compu,
    CompuConst,
    CompuConstContent,
    CompuConstFormulaContent,
    CompuConstNumericContent,
    CompuConstTextContent,
    CompuMethod,
    CompuNominatorDenominator,
    CompuRationalCoeffs,
    CompuScale,
    CompuScaleConstantContents,
    CompuScaleRationalFormula,
    CompuScales,
)
from armodel.models.M2.MSR.AsamHdo.Constraints.GlobalConstraints import DataConstr, DataConstrRule, InternalConstrs, PhysConstrs, ScaleConstr, ScaleConstrValidityEnum
from armodel.models.M2.MSR.AsamHdo.SpecialData import Sd, Sdf, Sdg, SdgContents
from armodel.models.M2.MSR.AsamHdo.Units import PhysicalDimension, Unit
from armodel.models.M2.MSR.CalibrationData.CalibrationValue import SwValueCont, SwValues
from armodel.models.M2.MSR.DataDictionary.AuxillaryObjects import MemoryAllocationKeywordPolicyType, MemorySectionType, SwAddrMethod
from armodel.models.M2.MSR.DataDictionary.Axis import SwAxisGeneric, SwAxisGrouped, SwAxisIndividual, SwGenericAxisParam
from armodel.models.M2.MSR.DataDictionary.CalibrationParameter import SwCalprmAxis, SwCalprmAxisSet
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import (
    CompuGenericMath,
    SwBitRepresentation,
    SwCalibrationAccessEnum,
    SwCalprmRefProxy,
    SwDataDefProps,
    SwDataDependency,
    SwDataDependencyArgs,
    SwPointerTargetProps,
    SwTextProps,
    SwVariableRefProxy,
    ValueList,
)
from armodel.models.M2.MSR.DataDictionary.RecordLayout import SwRecordLayout, SwRecordLayoutGroup, SwRecordLayoutGroupContent, SwRecordLayoutV
from armodel.models.M2.MSR.DataDictionary.ServiceProcessTask import SwServiceArg
from armodel.models.M2.MSR.DataDictionary.SystemConstant import SwSystemconst
from armodel.models.M2.MSR.Documentation.Annotation import Annotation, GeneralAnnotation
from armodel.models.M2.MSR.Documentation.BlockElements import Caption
from armodel.models.M2.MSR.Documentation.BlockElements.Figure import Graphic, LGraphic, MlFigure
from armodel.models.M2.MSR.Documentation.BlockElements.Formula import MlFormula
from armodel.models.M2.MSR.Documentation.BlockElements.OasisExchangeTable import FloatEnum, PgwideEnum
from armodel.models.M2.MSR.Documentation.Chapters import (
    Chapter,
    ChapterContent,
    ChapterModel,
    ChapterOrMsrQuery,
    MsrQueryChapter,
    MsrQueryTopic1,
    PredefinedChapter,
    Topic1,
    TopicContent,
    TopicContentOrMsrQuery,
    TopicOrMsrQuery,
)
from armodel.models.M2.MSR.Documentation.TextModel.BlockElements import DocumentationBlock
from armodel.models.M2.MSR.Documentation.TextModel.BlockElements.ListElements import ARList, DefItem, DefList, IndentSample, ItemLabelPosEnum, LabeledItem, LabeledList
from armodel.models.M2.MSR.Documentation.TextModel.BlockElements.Note import Note, NoteTypeEnum
from armodel.models.M2.MSR.Documentation.TextModel.BlockElements.PaginationAndView import DocumentViewSelectable, Paginateable
from armodel.models.M2.MSR.Documentation.TextModel.BlockElements.RequirementsTracing import StructuredReq, TraceableText
from armodel.models.M2.MSR.Documentation.TextModel.InlineTextElements import EmphasisText, IndexEntry, Superscript, Tt
from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel import LanguageSpecific, LLongName, LOverviewParagraph, LParagraph, LVerbatim
from armodel.models.M2.MSR.Documentation.TextModel.MsrQuery import MsrQueryArg, MsrQueryP1, MsrQueryP2, MsrQueryProps
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import MultilanguageLongName, MultiLanguageOverviewParagraph, MultiLanguageParagraph, MultiLanguagePlainText, MultiLanguageVerbatim
from armodel.parser.abstract_arxml_parser import AbstractARXMLParser

#: Mapping between BindingTimeEnum camelCase values and their XML attribute tokens
#: (AR:BINDING-TIME-ENUM--SIMPLE).
BINDING_TIME_XML_MAP = {
    "codeGenerationTime": "CODE-GENERATION-TIME",
    "linkTime": "LINK-TIME",
    "preCompileTime": "PRE-COMPILE-TIME",
    "systemDesignTime": "SYSTEM-DESIGN-TIME",
}

#: Mapping between IntervalTypeEnum values and their XML attribute tokens
#: (AR:INTERVAL-TYPE-ENUM--SIMPLE).
INTERVAL_TYPE_XML_MAP = {
    "closed": "CLOSED",
    "open": "OPEN",
}


class ARXMLParser(AbstractARXMLParser):
    """
    Main ARXML parser that loads AUTOSAR XML files into the model.
    Parses elements by dispatching to type-specific read methods based on
    XML tag names.
    """

    def __init__(self, options=None) -> None:
        super().__init__(options)

    def getChildElementRxIdentifierRange(self, element: ET.Element, key: str) -> RxIdentifierRange:
        child_element = self.find(element, key)
        range = None
        if child_element is not None:
            range = RxIdentifierRange()
            range.setLowerCanId(self.getChildElementOptionalNumericalValue(child_element, "LOWER-CAN-ID"))
            range.setUpperCanId(self.getChildElementOptionalNumericalValue(child_element, "UPPER-CAN-ID"))
        return range

    def getChildElementJ1939NodeName(self, element: ET.Element, key: str) -> J1939NodeName:
        child_element = self.find(element, key)
        node_name = None
        if child_element is not None:
            node_name = J1939NodeName()
            node_name.setArbitraryAddressCapable(self.getChildElementOptionalBooleanValue(child_element, "ARBITRARY-ADDRESS-CAPABLE"))
            node_name.setEcuInstance(self.getChildElementOptionalIntegerValue(child_element, "ECU-INSTANCE"))
            node_name.setFunction(self.getChildElementOptionalIntegerValue(child_element, "FUNCTION"))
            node_name.setFunctionInstance(self.getChildElementOptionalIntegerValue(child_element, "FUNCTION-INSTANCE"))
            node_name.setIdentitiyNumber(self.getChildElementOptionalIntegerValue(child_element, "IDENTITIY-NUMBER"))
            node_name.setIndustryGroup(self.getChildElementOptionalIntegerValue(child_element, "INDUSTRY-GROUP"))
            node_name.setManufacturerCode(self.getChildElementOptionalIntegerValue(child_element, "MANUFACTURER-CODE"))
            node_name.setVehicleSystem(self.getChildElementOptionalIntegerValue(child_element, "VEHICLE-SYSTEM"))
            node_name.setVehicleSystemInstance(self.getChildElementOptionalIntegerValue(child_element, "VEHICLE-SYSTEM-INSTANCE"))
        return node_name

    def readSd(self, element: ET.Element, contents: SdgContents):
        for child_element in self.findall(element, "./SD"):
            sd = Sd()
            self.readARObjectAttributes(child_element, sd)
            if "GID" in child_element.attrib:
                sd.setGID(NameToken().setValue(child_element.attrib["GID"]))
            if child_element.text is not None and child_element.text.strip() != "":
                sd.setValue(VerbatimStringPlain().setValue(child_element.text))
            contents.addSd(sd)

    def readSdf(self, element: ET.Element, contents: SdgContents):
        for child_element in self.findall(element, "./SDF"):
            sdf = Sdf()
            self.readARObjectAttributes(child_element, sdf)
            if "GID" in child_element.attrib:
                sdf.setGID(NameToken().setValue(child_element.attrib["GID"]))
            if child_element.text is not None and child_element.text.strip() != "":
                sdf.setValue(Numerical().setValue(child_element.text))
            contents.addSdf(sdf)

    def readSdgCaption(self, element: ET.Element, sdg: Sdg):
        child_element = self.find(element, "SDG-CAPTION")
        if child_element is not None:
            sdg.createSdgCaption(self.getShortName(child_element))

    def readSdgSdxRefs(self, element: ET.SubElement, contents: SdgContents):
        for ref in self.getChildElementRefTypeList(element, "SDX-REF"):
            contents.addSdxRef(ref)

    def readSdgSdxfRefs(self, element: ET.SubElement, contents: SdgContents):
        for ref in self.getChildElementRefTypeList(element, "SDXF"):
            contents.addSdxfRef(ref)

    def getSdg(self, element: ET.Element) -> Sdg:
        sdg = Sdg()
        self.readARObjectAttributes(element, sdg)
        if "GID" in element.attrib:
            sdg.setGID(NameToken().setValue(element.attrib["GID"]))
        self.readSdgCaption(element, sdg)
        contents = SdgContents()
        self.readSd(element, contents)
        self.readSdf(element, contents)
        for child_element in self.findall(element, "SDG"):
            contents.addSdg(self.getSdg(child_element))
        self.readSdgSdxRefs(element, contents)
        self.readSdgSdxfRefs(element, contents)
        if len(contents.getSds()) > 0 or len(contents.getSdfs()) > 0 or len(contents.getSdgs()) > 0 or len(contents.getSdxRefs()) > 0 or len(contents.getSdxfRefs()) > 0:
            sdg.setSdgContentsType(contents)
        return sdg

    def readBlueprintGenerator(self, element: ET.Element, generator: BlueprintGenerator) -> BlueprintGenerator:
        self.readARObjectAttributes(element, generator)
        generator.setIntroduction(self.getDocumentationBlock(element, "INTRODUCTION"))
        expression_element = self.find(element, "EXPRESSION")
        if expression_element is not None:
            generator.setExpression(VerbatimString().setValue(expression_element.text))
        return generator

    def readConditionByFormula(self, element: ET.Element, condition: ConditionByFormula) -> ConditionByFormula:
        self.readARObjectAttributes(element, condition)
        if "BINDING-TIME" in element.attrib:
            binding_time = None
            for camel, token in BINDING_TIME_XML_MAP.items():
                if token == element.attrib["BINDING-TIME"]:
                    binding_time = camel
                    break
            if binding_time is not None:
                condition.setBindingTime(BindingTimeEnum().setValue(binding_time))
            else:
                self.notImplemented("Unsupported BINDING-TIME <%s>" % element.attrib["BINDING-TIME"])
        return condition

    def readPostBuildVariantCondition(self, element: ET.Element, condition: PostBuildVariantCondition) -> PostBuildVariantCondition:
        self.readARObjectAttributes(element, condition)
        condition.setMatchingCriterionRef(self.getChildElementRefType("", element, "MATCHING-CRITERION-REF"))
        condition.setValue(self.getChildElementOptionalIntegerValue(element, "VALUE"))
        return condition

    def readVariationPoint(self, element: ET.Element, variation_point: VariationPoint) -> VariationPoint:
        self.readARObjectAttributes(element, variation_point)
        variation_point.setShortLabel(self.getChildElementOptionalIdentifier(element, "SHORT-LABEL"))
        variation_point.setDesc(self.getMultiLanguageOverviewParagraph(element, "DESC"))
        variation_point.setBlueprintCondition(self.getDocumentationBlock(element, "BLUEPRINT-CONDITION"))
        # FORMAL-BLUEPRINT-CONDITION is obsolete (atp.Status="obsolete") and has no
        # model attribute — deliberately not read.
        formal_element = self.find(element, "FORMAL-BLUEPRINT-GENERATOR")
        if formal_element is not None:
            variation_point.setFormalBlueprintGenerator(self.readBlueprintGenerator(formal_element, BlueprintGenerator()))
        sw_syscond_element = self.find(element, "SW-SYSCOND")
        if sw_syscond_element is not None:
            variation_point.setSwSyscond(self.readConditionByFormula(sw_syscond_element, ConditionByFormula()))
        for child_element in self.findall(element, "POST-BUILD-VARIANT-CONDITIONS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "POST-BUILD-VARIANT-CONDITION":
                variation_point.addPostBuildVariantCondition(self.readPostBuildVariantCondition(child_element, PostBuildVariantCondition()))
            else:
                self.notImplemented("Unsupported POST-BUILD-VARIANT-CONDITIONS content <%s>" % tag_name)
        sdg_element = self.find(element, "SDG")
        if sdg_element is not None:
            variation_point.setSdg(self.getSdg(sdg_element))
        return variation_point

    def readAdminDataSdgs(self, element: ET.Element, admin_data: AdminData):
        for child_element in self.findall(element, "SDGS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "SDG":
                admin_data.addSdg(self.getSdg(child_element))
            else:
                self.notImplemented("Unsupported SDG <%s>" % tag_name)

    def readModification(self, element: ET.Element, modification: Modification):
        modification.setChange(self.getMultiLanguageOverviewParagraph(element, "CHANGE"))
        modification.setReason(self.getMultiLanguageOverviewParagraph(element, "REASON"))

    def readDocRevisionModifications(self, element: ET.Element, revision: DocRevision):
        for child_element in self.findall(element, "MODIFICATIONS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "MODIFICATION":
                modification = Modification()
                self.readModification(child_element, modification)
                revision.addModification(modification)
            else:
                self.notImplemented("Unsupported Modification <%s>" % tag_name)

    def readDocRevision(self, element: ET.Element, revision: DocRevision):
        revision.setDate(self.getChildElementOptionalDataTime(element, "DATE"))
        revision.setIssuedBy(self.getChildElementOptionalLiteral(element, "ISSUED-BY"))
        revision.setRevisionLabel(self.getChildElementOptionalRevisionLabelString(element, "REVISION-LABEL"))
        revision.setState(self.getChildElementOptionalLiteral(element, "STATE"))

        self.readDocRevisionModifications(element, revision)

    def readAdminDataDocRevisions(self, element: ET.Element, admin_data: AdminData):
        for child_element in self.findall(element, "DOC-REVISIONS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "DOC-REVISION":
                revision = DocRevision()
                self.readDocRevision(child_element, revision)
                admin_data.addDocRevision(revision)
            else:
                self.notImplemented("Unsupported DocRevision <%s>" % tag_name)

    def getAdminData(self, element: ET.Element, key: str) -> AdminData:
        admin_data = None
        child_element = self.find(element, key)
        if child_element is not None:
            # self.logger.debug("Read AdminData")
            admin_data = AdminData()
            self.readARObjectAttributes(child_element, admin_data)
            admin_data.setLanguage(self.getChildElementOptionalLiteral(child_element, "LANGUAGE"))
            admin_data.setUsedLanguages(self.getMultiLanguagePlainText(child_element, "USED-LANGUAGES"))

            self.readAdminDataSdgs(child_element, admin_data)
            self.readAdminDataDocRevisions(child_element, admin_data)
        return admin_data

    def readReferrable(self, element: ET.Element, referrable: Referrable):
        self.readARObjectAttributes(element, referrable)

        if isinstance(referrable, Referrable):
            for child_element in self.findall(element, "SHORT-NAME-FRAGMENTS/SHORT-NAME-FRAGMENT"):
                fragment = ShortNameFragment()
                self.readARObjectAttributes(child_element, fragment)
                role_element = self.find(child_element, "ROLE")
                if role_element is not None:
                    fragment.setRole(role_element.text)
                fragment.setFragment(self.getChildElementOptionalIdentifier(child_element, "FRAGMENT"))
                referrable.addShortNameFragment(fragment)

    def readMultilanguageReferrable(self, element: ET.Element, referrable: MultilanguageReferrable):
        self.readReferrable(element, referrable)
        referrable.setLongName(self.getMultilanguageLongName(element, "LONG-NAME"))

    def getCaption(self, element: ET.Element, key: str) -> Caption:
        caption = None
        child_element = self.find(element, key)
        if child_element is not None:
            caption = Caption(None, self.getShortName(child_element))
            self.readMultilanguageReferrable(child_element, caption)
            caption.setDesc(self.getMultiLanguageOverviewParagraph(child_element, "DESC"))
        return caption

    def readIdentifiable(self, element: ET.Element, identifiable: Identifiable):
        self.readMultilanguageReferrable(element, identifiable)

        for annotation in self.getAnnotations(element):
            identifiable.addAnnotation(annotation)

        identifiable.setCategory(self.getChildElementOptionalLiteral(element, "CATEGORY"))
        identifiable.setDesc(self.getMultiLanguageOverviewParagraph(element, "DESC"))
        identifiable.setIntroduction(self.getDocumentationBlock(element, "INTRODUCTION"))

        identifiable.setAdminData(self.getAdminData(element, "ADMIN-DATA"))

        if isinstance(identifiable, Identifiable):
            variation_point_element = self.find(element, "VARIATION-POINT")
            if variation_point_element is not None:
                identifiable.setVariationPoint(self.readVariationPoint(variation_point_element, VariationPoint()))

    def readARElement(self, element: ET.Element, ar_element: ARElement):
        self.readIdentifiable(element, ar_element)

    def readLLongName(self, element: ET.Element, long_name: MultilanguageLongName):
        for child_element in self.findall(element, "L-4"):
            l4 = LLongName()
            self.readARObjectAttributes(child_element, l4)
            l4.setValue(child_element.text)
            if "L" in child_element.attrib:
                l4.setL(child_element.attrib["L"])  # noqa: E741
            if "SUP" in child_element.attrib:
                l4.setSup(Superscript().setValue(child_element.attrib["SUP"]))
            if "SUB" in child_element.attrib:
                l4.setSub(Superscript().setValue(child_element.attrib["SUB"]))
            for inline in child_element:
                tag_name = self.getTagName(inline)
                if tag_name == "E":
                    l4.setE(self.readEmphasisText(inline))
                elif tag_name == "IE":
                    l4.setIe(self.readIndexEntry(inline))
                elif tag_name == "TT":
                    l4.setTt(self.readTt(inline))
            long_name.addL4(l4)

    def readEmphasisText(self, element: ET.Element) -> EmphasisText:
        emphasis = EmphasisText()
        if element.text is not None:
            emphasis.setValue(String().setValue(element.text))
        if "COLOR" in element.attrib:
            emphasis.setColor(String().setValue(element.attrib["COLOR"]))
        if "SUP" in element.attrib:
            emphasis.setSup(Superscript().setValue(element.attrib["SUP"]))
        if "SUB" in element.attrib:
            emphasis.setSub(Superscript().setValue(element.attrib["SUB"]))
        for inline in element:
            tag_name = self.getTagName(inline)
            if tag_name == "TT":
                emphasis.setTt(self.readTt(inline))
        return emphasis

    def readIndexEntry(self, element: ET.Element) -> IndexEntry:
        index_entry = IndexEntry()
        if element.text is not None:
            index_entry.setValue(String().setValue(element.text))
        if "SUP" in element.attrib:
            index_entry.setSup(Superscript().setValue(element.attrib["SUP"]))
        if "SUB" in element.attrib:
            index_entry.setSub(Superscript().setValue(element.attrib["SUB"]))
        return index_entry

    def readTt(self, element: ET.Element) -> Tt:
        tt = Tt()
        if element.text is not None:
            tt.setValue(String().setValue(element.text))
        if "TYPE" in element.attrib:
            tt.setType(NameToken().setValue(element.attrib["TYPE"]))
        if "TEX-RENDER" in element.attrib:
            tt.setTexRender(String().setValue(element.attrib["TEX-RENDER"]))
        return tt

    def getMultilanguageLongName(self, element: ET.Element, key: str) -> MultilanguageLongName:
        long_name = None
        child_element = self.find(element, "%s" % key)
        if child_element is not None:
            long_name = MultilanguageLongName()
            self.readARObjectAttributes(child_element, long_name)
            self.readLLongName(child_element, long_name)
        return long_name

    def readLOverviewParagraph(self, element: ET.Element, paragraph: MultiLanguageOverviewParagraph):
        for child_element in self.findall(element, "L-2"):
            l2 = LOverviewParagraph()
            self.readARObjectAttributes(child_element, l2)
            l2.setValue(child_element.text)
            if "L" in child_element.attrib:
                l2.setL(child_element.attrib["L"])  # noqa: E741
            paragraph.addL2(l2)

    def getMultiLanguageOverviewParagraph(self, element: ET.Element, key: str) -> MultiLanguageOverviewParagraph:
        paragraph = None
        child_element = self.find(element, key)
        if child_element is not None:
            paragraph = MultiLanguageOverviewParagraph()
            self.readARObjectAttributes(child_element, paragraph)
            self.readLOverviewParagraph(child_element, paragraph)
        return paragraph

    def getVariableInAtomicSWCTypeInstanceRef(self, element: ET.Element) -> VariableInAtomicSWCTypeInstanceRef:
        instance_ref = None
        if element is not None:
            instance_ref = VariableInAtomicSWCTypeInstanceRef()
            self.readARObjectAttributes(element, instance_ref)
            instance_ref.setPortPrototypeRef(self.getChildElementOptionalRefType(element, "PORT-PROTOTYPE-REF"))
            instance_ref.setTargetDataPrototypeRef(self.getChildElementOptionalRefType(element, "TARGET-DATA-PROTOTYPE-REF"))
        return instance_ref

    def getComponentInSystemInstanceRef(self, element: ET.Element) -> ComponentInSystemInstanceRef:
        instance_ref = None
        if element is not None:
            instance_ref = ComponentInSystemInstanceRef()
            self.readARObjectAttributes(element, instance_ref)
            instance_ref.setBaseRef(self.getChildElementOptionalRefType(element, "BASE-REF"))
            instance_ref.setContextCompositionRef(self.getChildElementOptionalRefType(element, "CONTEXT-COMPOSITION-REF"))
            instance_ref.setTargetComponentRef(self.getChildElementOptionalRefType(element, "TARGET-COMPONENT-REF"))
        return instance_ref

    def getAutosarVariableRef(self, element: ET.Element, key: str) -> AutosarVariableRef:
        child_element = self.find(element, key)
        instance_ref = None
        if child_element is not None:
            instance_ref = AutosarVariableRef()
            self.readARObjectAttributes(child_element, instance_ref)
            instance_ref.setAutosarVariableIRef(self.getVariableInAtomicSWCTypeInstanceRef(self.find(child_element, "AUTOSAR-VARIABLE-IREF")))
            instance_ref.setLocalVariableRef(self.getChildElementOptionalRefType(child_element, "LOCAL-VARIABLE-REF"))
        return instance_ref

    def getNvBlockDataMapping(self, element: ET.Element, key: str) -> NvBlockDataMapping:
        child_element = self.find(element, key)
        mapping = None
        if child_element is not None:
            mapping = NvBlockDataMapping()
            self.readNvBlockDataMapping(child_element, mapping)
        return mapping

    def readNvBlockDataMapping(self, element: ET.Element, mapping: NvBlockDataMapping):
        mapping.setBitfieldTextTableMaskNvBlockDescriptor(self.getChildElementOptionalPositiveInteger(element, "BITFIELD-TEXT-TABLE-MASK-NV-BLOCK-DESCRIPTOR"))
        mapping.setBitfieldTextTableMaskPortPrototype(self.getChildElementOptionalPositiveInteger(element, "BITFIELD-TEXT-TABLE-MASK-PORT-PROTOTYPE"))
        mapping.setNvRamBlockElement(self.getAutosarVariableRef(element, "NV-RAM-BLOCK-ELEMENT"))
        mapping.setReadNvData(self.getAutosarVariableRef(element, "READ-NV-DATA"))
        mapping.setWrittenNvData(self.getAutosarVariableRef(element, "WRITTEN-NV-DATA"))
        mapping.setWrittenReadNvData(self.getAutosarVariableRef(element, "WRITTEN-READ-NV-DATA"))

    def readBulkNvDataDescriptor(self, element: ET.Element, descriptor: BulkNvDataDescriptor):
        self.readIdentifiable(element, descriptor)
        child_element = self.find(element, "BULK-NV-BLOCK")
        if child_element is not None:
            prototype_element = self.find(child_element, "VARIABLE-DATA-PROTOTYPE")
            block = VariableDataPrototype(descriptor, self.getShortName(prototype_element))
            self.readVariableDataPrototype(prototype_element, block)
            descriptor.setBulkNvBlock(block)
        for child_element in self.findall(element, "NV-BLOCK-DATA-MAPPINGS/NV-BLOCK-DATA-MAPPING"):
            mapping = NvBlockDataMapping()
            self.readNvBlockDataMapping(child_element, mapping)
            descriptor.addNvBlockDataMapping(mapping)

    def readNvBlockDescriptor(self, element: ET.Element, descriptor: NvBlockDescriptor):
        self.readIdentifiable(element, descriptor)
        for child_element in self.findall(element, "CLIENT-SERVER-PORTS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "ROLE-BASED-PORT-ASSIGNMENT":
                descriptor.addClientServerPort(self.getRoleBasedPortAssignment(child_element))
            else:
                self.notImplemented("Unsupported client server port <%s>" % tag_name)
        for ref in self.getChildElementRefTypeList(element, "CONSTANT-VALUE-MAPPING-REFS/CONSTANT-VALUE-MAPPING-REF"):
            descriptor.addConstantValueMappingRef(ref)
        for ref in self.getChildElementRefTypeList(element, "DATA-TYPE-MAPPING-REFS/DATA-TYPE-MAPPING-REF"):
            descriptor.addDataTypeMappingRef(ref)
        for child_element in self.findall(element, "INSTANTIATION-DATA-DEF-PROPSS/INSTANTIATION-DATA-DEF-PROPS"):
            props = InstantiationDataDefProps()
            self.readARObjectAttributes(child_element, props)
            props.setParameterInstance(self.getAutosarParameterRef(child_element, "PARAMETER-INSTANCE"))
            props.setSwDataDefProps(self.getSwDataDefProps(child_element, "SW-DATA-DEF-PROPS"))
            props.setVariableInstance(self.getAutosarVariableRef(child_element, "VARIABLE-INSTANCE"))
            descriptor.addInstantiationDataDefProps(props)
        for child_element in self.findall(element, "MODE-SWITCH-EVENT-TRIGGERED-ACTIVITYS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "MODE-SWITCH-EVENT-TRIGGERED-ACTIVITY":
                descriptor.addModeSwitchEventTriggeredActivity(self.getModeSwitchEventTriggeredActivity(child_element))
            else:
                self.notImplemented("Unsupported mode switch event triggered activity <%s>" % tag_name)
        for child_element in self.findall(element, "NV-BLOCK-DATA-MAPPINGS/NV-BLOCK-DATA-MAPPING"):
            mapping = NvBlockDataMapping()
            self.readNvBlockDataMapping(child_element, mapping)
            descriptor.addNvBlockDataMapping(mapping)
        needs_element = self.find(element, "NV-BLOCK-NEEDS")
        if needs_element is not None:
            needs = NvBlockNeeds(descriptor, self.getShortName(needs_element))
            self.readNvBlockNeeds(needs_element, needs)
            descriptor.setNvBlockNeeds(needs)
        ram_block_element = self.find(element, "RAM-BLOCK")
        if ram_block_element is not None:
            ram_block = VariableDataPrototype(descriptor, self.getShortName(ram_block_element))
            self.readVariableDataPrototype(ram_block_element, ram_block)
            descriptor.setRamBlock(ram_block)
        rom_block_element = self.find(element, "ROM-BLOCK")
        if rom_block_element is not None:
            rom_block = ParameterDataPrototype(descriptor, self.getShortName(rom_block_element))
            self.readParameterDataPrototype(rom_block_element, rom_block)
            descriptor.setRomBlock(rom_block)
        descriptor.setSupportDirtyFlag(self.getChildElementOptionalBooleanValue(element, "SUPPORT-DIRTY-FLAG"))
        descriptor.setTimingEventRef(self.getChildElementOptionalRefType(element, "TIMING-EVENT-REF"))
        for child_element in self.findall(element, "WRITING-STRATEGYS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "ROLE-BASED-DATA-ASSIGNMENT":
                descriptor.addWritingStrategy(self.getRoleBasedDataAssignment(child_element))
            else:
                self.notImplemented("Unsupported writing strategy <%s>" % tag_name)

    def _readVariableAccesses(self, element: ET.Element, parent: RunnableEntity, key: str):
        for child_element in self.findall(element, "%s/VARIABLE-ACCESS" % key):
            short_name = self.getShortName(child_element)

            # self.logger.debug("Read VariableAccesses %s" % short_name)
            supported = True

            if key == "DATA-RECEIVE-POINT-BY-ARGUMENTS":
                variable_access = parent.createDataReceivePointByArgument(short_name)
                variable_access.setAccessedVariableRef(self.getAutosarVariableRef(child_element, "ACCESSED-VARIABLE"))
            elif key == "DATA-RECEIVE-POINT-BY-VALUES":
                variable_access = parent.createDataReceivePointByValue(short_name)
                variable_access.setAccessedVariableRef(self.getAutosarVariableRef(child_element, "ACCESSED-VARIABLE"))
            elif key == "DATA-READ-ACCESSS":
                variable_access = parent.createDataReadAccess(short_name)
                variable_access.setAccessedVariableRef(self.getAutosarVariableRef(child_element, "ACCESSED-VARIABLE"))
            elif key == "DATA-WRITE-ACCESSS":
                variable_access = parent.createDataWriteAccess(short_name)
                variable_access.setAccessedVariableRef(self.getAutosarVariableRef(child_element, "ACCESSED-VARIABLE"))
            elif key == "DATA-SEND-POINTS":
                variable_access = parent.createDataSendPoint(short_name)
                variable_access.setAccessedVariableRef(self.getAutosarVariableRef(child_element, "ACCESSED-VARIABLE"))
            elif key == "WRITTEN-LOCAL-VARIABLES":
                variable_access = parent.createWrittenLocalVariable(short_name)
                variable_access.setAccessedVariableRef(self.getAutosarVariableRef(child_element, "ACCESSED-VARIABLE"))
            elif key == "READ-LOCAL-VARIABLES":
                variable_access = parent.createReadLocalVariable(short_name)
                variable_access.setAccessedVariableRef(self.getAutosarVariableRef(child_element, "ACCESSED-VARIABLE"))
            else:
                self.notImplemented("Unsupported Variable Accesss <%s>" % key)
                supported = False

            if supported:
                self.readIdentifiable(child_element, variable_access)

    def readBswModuleDescriptionImplementedEntryRefs(self, element: ET.Element, parent: BswModuleDescription):
        for child_element in self.findall(element, "PROVIDED-ENTRYS/BSW-MODULE-ENTRY-REF-CONDITIONAL"):
            ref = self.getChildElementOptionalRefType(child_element, "BSW-MODULE-ENTRY-REF")
            if ref is not None:
                parent.addImplementedEntryRef(ref)
            # self.logger.debug("ImplementedEntry <%s> of BswModuleDescription <%s> has been added", ref.value, parent.getShortName())

    def readModeDeclarationGroupPrototype(self, element: ET.Element, prototype: ModeDeclarationGroupPrototype):
        self.readIdentifiable(element, prototype)
        prototype.setTypeTRef(self.getChildElementOptionalRefType(element, "TYPE-TREF"))
        sw_calibration_access = self.getChildElementOptionalLiteral(element, "SW-CALIBRATION-ACCESS")
        if sw_calibration_access is not None:
            prototype.setSwCalibrationAccess(SwCalibrationAccessEnum().setValue(sw_calibration_access.getValue()))

    def readBswModuleDescriptionProvidedModeGroups(self, element: ET.Element, parent: BswModuleDescription):
        for child_element in self.findall(element, "PROVIDED-MODE-GROUPS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "MODE-DECLARATION-GROUP-PROTOTYPE":
                mode_group = parent.createProvidedModeGroup(self.getShortName(child_element))
                self.readModeDeclarationGroupPrototype(child_element, mode_group)
            else:
                self.notImplemented("Unsupported ProvidedModeGroup <%s>" % tag_name)

    def readBswModuleDescriptionRequiredModeGroups(self, element: ET.Element, parent: BswModuleDescription):
        for child_element in self.findall(element, "REQUIRED-MODE-GROUPS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "MODE-DECLARATION-GROUP-PROTOTYPE":
                prototype = parent.createRequiredModeGroup(self.getShortName(child_element))
                self.readModeDeclarationGroupPrototype(child_element, prototype)
            else:
                self.notImplemented("Unsupported RequiredModeGroup <%s>" % tag_name)

    def readActivationReasons(self, element: ET.Element, entity: ExecutableEntity):
        for reason_element in self.findall(element, "ACTIVATION-REASONS/EXECUTABLE-ENTITY-ACTIVATION-REASON"):
            reason = entity.createActivationReason(self.getShortName(reason_element))
            self.readExecutableEntityActivationReason(reason_element, reason)

    def readExecutableEntityActivationReason(self, element: ET.Element, reason: ExecutableEntityActivationReason):
        self.readImplementationProps(element, reason)
        reason.setBitPosition(self.getChildElementOptionalPositiveInteger(element, "BIT-POSITION"))

    def readCanEnterRefs(self, element: ET.Element, entity: ExecutableEntity):
        for ref in self.getChildElementRefTypeList(element, "CAN-ENTER-EXCLUSIVE-AREA-REFS/CAN-ENTER-EXCLUSIVE-AREA-REF"):
            entity.addCanEnterRef(ref)

    def readExclusiveAreaNestingOrderRefs(self, element: ET.Element, entity: ExecutableEntity):
        for ref in self.getChildElementRefTypeList(element, "EXCLUSIVE-AREA-NESTING-ORDER-REFS/EXCLUSIVE-AREA-NESTING-ORDER-REF"):
            entity.addExclusiveAreaNestingOrderRef(ref)

    def readRunsInsideRefs(self, element: ET.Element, entity: ExecutableEntity):
        for ref in self.getChildElementRefTypeList(element, "RUNS-INSIDE-EXCLUSIVE-AREA-REFS/RUNS-INSIDE-EXCLUSIVE-AREA-REF"):
            entity.addRunsInsideRef(ref)

    def readExecutableEntity(self, element: ET.Element, entity: ExecutableEntity):
        # self.logger.debug("Read ExecutableEntity %s" % entity.getShortName())
        self.readIdentifiable(element, entity)
        self.readActivationReasons(element, entity)
        self.readCanEnterRefs(element, entity)
        self.readExclusiveAreaNestingOrderRefs(element, entity)
        entity.setMinimumStartInterval(self.getChildElementOptionalTimeValue(element, "MINIMUM-START-INTERVAL"))
        entity.setReentrancyLevel(self.getChildElementOptionalLiteral(element, "REENTRANCY-LEVEL"))
        self.readRunsInsideRefs(element, entity)
        entity.setSwAddrMethodRef(self.getChildElementOptionalRefType(element, "SW-ADDR-METHOD-REF"))

    def readBswModuleEntityManagedModeGroups(self, element: ET.Element, entity: BswModuleEntity):
        for child_element in self.findall(element, "MANAGED-MODE-GROUPS/MODE-DECLARATION-GROUP-PROTOTYPE-REF-CONDITIONAL"):
            ref_type = self.getChildElementOptionalRefType(child_element, "MODE-DECLARATION-GROUP-PROTOTYPE-REF")
            if ref_type is not None:
                entity.addManagedModeGroupRef(ref_type)

    def readBswModuleEntityAccessedModeGroups(self, element: ET.Element, entity: BswModuleEntity):
        for child_element in self.findall(element, "ACCESSED-MODE-GROUPS/MODE-DECLARATION-GROUP-PROTOTYPE-REF-CONDITIONAL"):
            ref_type = self.getChildElementOptionalRefType(child_element, "MODE-DECLARATION-GROUP-PROTOTYPE-REF")
            if ref_type is not None:
                entity.addAccessedModeGroupRef(ref_type)

    def readBswEvent(self, element: ET.Element, event: BswScheduleEvent):
        event.activationReasonRepresentationRef = self.getChildElementOptionalRefType(element, "ACTIVATION-REASON-REPRESENTATION-REF")
        for ref in self.getChildElementRefTypeList(element, "CONTEXT-LIMITATION-REFS/CONTEXT-LIMITATION-REF"):
            event.addContextLimitationRef(ref)
        for child_element in self.findall(element, "DISABLED-IN-MODE-IREFS/DISABLED-IN-MODE-IREF"):
            event.addDisabledInModeIRef(self.getModeInBswModuleDescriptionInstanceRef(child_element))
        event.setStartsOnEventRef(self.getChildElementOptionalRefType(element, "STARTS-ON-EVENT-REF"))

    def readBswScheduleEvent(self, element, event: BswScheduleEvent):
        self.readBswEvent(element, event)

    def readBswModeSwitchEvent(self, element: ET.Element, event: BswModeSwitchEvent):
        # self.logger.debug("Read BswModeSwitchEvent <%s>" % event.getShortName())
        # Read the Inherit BswScheduleEvent
        self.readBswScheduleEvent(element, event)
        event.setActivation(self.getChildElementOptionalLiteral(element, "ACTIVATION"))
        for child_element in self.findall(element, "MODE-IREFS/MODE-IREF"):
            event.addModeIRef(self.getModeInBswModuleDescriptionInstanceRef(child_element))

    def readBswModeManagerErrorEvent(self, element: ET.Element, event: BswModeManagerErrorEvent):
        # self.logger.debug("Read BswModeManagerErrorEvent <%s>" % event.getShortName())
        # Read the Inherit BswScheduleEvent
        self.readBswScheduleEvent(element, event)
        event.setModeGroupRef(self.getChildElementOptionalRefType(element, "MODE-GROUP-REF"))

    def readBswModeSwitchedAckEvent(self, element: ET.Element, event: BswModeSwitchedAckEvent):
        self.readBswScheduleEvent(element, event)
        event.setModeGroupRef(self.getChildElementOptionalRefType(element, "MODE-GROUP-REF"))

    def readBswAsynchronousServerCallReturnsEvent(self, element: ET.Element, event: BswAsynchronousServerCallReturnsEvent):
        self.readBswScheduleEvent(element, event)
        event.setEventSourceRef(self.getChildElementOptionalRefType(element, "EVENT-SOURCE-REF"))

    def readBswTimingEvent(self, element: ET.Element, event: BswTimingEvent):
        self.logger.debug("Read BswTimingEvent <%s>" % event.getShortName())
        # Read the Inherit BswScheduleEvent
        self.readBswScheduleEvent(element, event)
        event.setPeriod(self.getChildElementOptionalTimeValue(element, "PERIOD"))
        if event.getPeriod() is None:
            self.logger.warning("Period of BswTimingEvent <%s> is invalid." % event.getShortName())
        else:
            self.logger.debug(" Period: <%f, %s>" % (event.getPeriod().getValue(), event.getPeriod().getText()))

    def readBswDataReceivedEvent(self, element: ET.Element, event: BswDataReceivedEvent):
        # self.logger.debug("Read BswDataReceivedEvent <%s>" % event.getShortName())
        # Read the Inherit BswScheduleEvent
        self.readBswScheduleEvent(element, event)
        event.setDataRef(self.getChildElementOptionalRefType(element, "DATA-REF"))

    def readBswInternalTriggerOccurredEvent(self, element: ET.Element, event: BswInternalTriggerOccurredEvent):
        # self.logger.debug("Read BswInternalTriggerOccurredEvent <%s>" % event.getShortName())
        # Read the Inherit BswScheduleEvent
        self.readBswScheduleEvent(element, event)
        event.setEventSourceRef(self.getChildElementOptionalRefType(element, "EVENT-SOURCE-REF"))

    def getBswModeSenderPolicy(self, element: ET.Element) -> BswModeSenderPolicy:
        policy = BswModeSenderPolicy()
        policy.setAckRequest(self.getBswModeSwitchAckRequest(element, "ACK-REQUEST"))
        policy.setEnhancedModeApi(self.getChildElementOptionalBooleanValue(element, "ENHANCED-MODE-API"))
        policy.setProvidedModeGroupRef(self.getChildElementOptionalRefType(element, "PROVIDED-MODE-GROUP-REF"))
        policy.setQueueLength(self.getChildElementOptionalPositiveInteger(element, "QUEUE-LENGTH"))
        return policy

    def getBswModeSwitchAckRequest(self, element: ET.Element, key: str) -> BswModeSwitchAckRequest:
        request = None
        child_element = self.find(element, key)
        if child_element is not None:
            request = BswModeSwitchAckRequest()
            request.setTimeout(self.getChildElementOptionalTimeValue(child_element, "TIMEOUT"))
        return request

    def readBswInternalBehaviorModeSenderPolicy(self, element: ET.Element, parent: BswInternalBehavior):
        for child_element in self.findall(element, "MODE-SENDER-POLICYS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "BSW-MODE-SENDER-POLICY":
                parent.addModeSenderPolicy(self.getBswModeSenderPolicy(child_element))
            else:
                self.raiseError("Unsupported ModeSenderPolicy type <%s>." % tag_name)

    def readDataTypeMappingRefs(self, element: ET.Element, behavior: InternalBehavior):
        child_element = self.find(element, "DATA-TYPE-MAPPING-REFS")
        if child_element is not None:
            for ref in self.getChildElementRefTypeList(child_element, "DATA-TYPE-MAPPING-REF"):
                behavior.addDataTypeMappingRef(ref)

    def readInternalBehaviorConstantMemories(self, element: ET.Element, behavior: InternalBehavior):
        for child_element in self.findall(element, "CONSTANT-MEMORYS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "PARAMETER-DATA-PROTOTYPE":
                prototype = behavior.createConstantMemory(self.getShortName(child_element))
                self.readParameterDataPrototype(child_element, prototype)
            else:
                self.notImplemented("Unsupported constant memories <%s>" % tag_name)

    def readInternalBehaviorStaticMemories(self, element: ET.Element, behavior: InternalBehavior):
        for child_element in self.findall(element, "STATIC-MEMORYS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "VARIABLE-DATA-PROTOTYPE":
                prototype = behavior.createStaticMemory(self.getShortName(child_element))
                self.readVariableDataPrototype(child_element, prototype)
            else:
                self.notImplemented("Unsupported static memories <%s>" % tag_name)

    def readInternalBehavior(self, element: ET.Element, behavior: InternalBehavior):
        self.readIdentifiable(element, behavior)
        self.readInternalBehaviorConstantMemories(element, behavior)
        for child_element in self.findall(element, "EXCLUSIVE-AREAS/EXCLUSIVE-AREA"):
            short_name = self.getShortName(child_element)
            behavior.createExclusiveArea(short_name)
        self.readExclusiveAreaNestingOrders(element, behavior)
        self.readDataTypeMappingRefs(element, behavior)
        self.readInternalBehaviorStaticMemories(element, behavior)

    def readExclusiveAreaNestingOrders(self, element: ET.Element, behavior: InternalBehavior):
        for child_element in self.findall(element, "EXCLUSIVE-AREA-NESTING-ORDERS/EXCLUSIVE-AREA-NESTING-ORDER"):
            short_name = self.getShortName(child_element)
            nesting_order = behavior.createExclusiveAreaNestingOrder(short_name)
            for ref in self.getChildElementRefTypeList(child_element, "EXCLUSIVE-AREA-REFS/EXCLUSIVE-AREA-REF"):
                nesting_order.addExclusiveAreaRef(ref)

    def getRoleBasedDataAssignment(self, element: ET.Element) -> RoleBasedDataAssignment:
        assignment = RoleBasedDataAssignment()
        assignment.setRole(self.getChildElementOptionalLiteral(element, "ROLE"))
        assignment.setUsedDataElement(self.getAutosarVariableRef(element, "USED-DATA-ELEMENT"))
        assignment.setUsedParameterElement(self.getAutosarParameterRef(element, "USED-PARAMETER-ELEMENT"))
        assignment.setUsedPimRef(self.getChildElementOptionalRefType(element, "USED-PIM-REF"))
        return assignment

    def getModeSwitchEventTriggeredActivity(self, element: ET.Element) -> ModeSwitchEventTriggeredActivity:
        activity = ModeSwitchEventTriggeredActivity()
        activity.setRole(self.getChildElementOptionalLiteral(element, "ROLE"))
        activity.setSwcModeSwitchEventRef(self.getChildElementOptionalRefType(element, "SWC-MODE-SWITCH-EVENT-REF"))
        return activity

    def getRoleBasedPortAssignment(self, element: ET.Element) -> RoleBasedPortAssignment:
        assignment = RoleBasedPortAssignment()
        self.readARObjectAttributes(element, assignment)
        assignment.portPrototypeRef = self.getChildElementOptionalRefType(element, "PORT-PROTOTYPE-REF")
        assignment.role = self.getChildElementOptionalLiteral(element, "ROLE")
        return assignment

    def getRoleBasedDataTypeAssignment(self, element: ET.Element) -> RoleBasedDataTypeAssignment:
        assignment = RoleBasedDataTypeAssignment()
        assignment.setRole(self.getChildElementOptionalLiteral(element, "ROLE"))
        assignment.setUsedImplementationDataTypeRef(self.getChildElementOptionalRefType(element, "USED-IMPLEMENTATION-DATA-TYPE-REF"))
        return assignment

    def readServiceDependency(self, element: ET.Element, dependency: ServiceDependency):
        self.readIdentifiable(element, dependency)
        for child_element in self.findall(element, "ASSIGNED-DATA-TYPES/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "ROLE-BASED-DATA-TYPE-ASSIGNMENT":
                dependency.addAssignedDataType(self.getRoleBasedDataTypeAssignment(child_element))
            else:
                self.notImplemented("Unsupported assigned data type <%s>" % tag_name)
        self.readSymbolicNameProps(element, dependency)

    def getBswServiceDependencyIdent(self, element: ET.Element, dependency: BswServiceDependency) -> BswServiceDependencyIdent:
        ident_element = self.find(element, "IDENT")
        if ident_element is not None:
            return BswServiceDependencyIdent(dependency, self.getShortName(ident_element))
        return None

    def readSymbolicNameProps(self, element: ET.Element, dependency: ServiceDependency):
        props_element = self.find(element, "SYMBOLIC-NAME-PROPS")
        if props_element is None:
            return
        props = SymbolicNameProps(dependency, self.getShortName(props_element))
        self.readImplementationProps(props_element, props)
        dependency.setSymbolicNameProps(props)

    def getRoleBasedBswModuleEntryAssignment(self, element: ET.Element) -> RoleBasedBswModuleEntryAssignment:
        assignment = RoleBasedBswModuleEntryAssignment()
        assignment.setAssignedEntryRef(self.getChildElementOptionalRefType(element, "ASSIGNED-ENTRY-REF"))
        assignment.setRole(self.getChildElementOptionalLiteral(element, "ROLE"))
        return assignment

    def readBswServiceDependencyAssignedData(self, element: ET.Element, dependency: BswServiceDependency):
        for child_element in self.findall(element, "ASSIGNED-DATAS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "ROLE-BASED-DATA-ASSIGNMENT":
                dependency.addAssignedData(self.getRoleBasedDataAssignment(child_element))
            else:
                self.notImplemented("Unsupported assigned data <%s>" % tag_name)

    def readBswServiceDependencyAssignedEntryRoles(self, element: ET.Element, dependency: BswServiceDependency):
        for child_element in self.findall(element, "ASSIGNED-ENTRY-ROLES/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "ROLE-BASED-BSW-MODULE-ENTRY-ASSIGNMENT":
                dependency.addAssignedEntryRole(self.getRoleBasedBswModuleEntryAssignment(child_element))
            else:
                self.notImplemented("Unsupported assigned entry role <%s>" % tag_name)

    def readBswServiceDependencyServiceNeeds(self, element: ET.Element, dependency: BswServiceDependency):
        needs_element = self.find(element, "SERVICE-NEEDS")
        if needs_element is None:
            return
        for child_element in self.findall(needs_element, "*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "BSW-MGR-NEEDS":
                short_name = self.getShortName(child_element)
                needs = BswMgrNeeds(dependency, short_name)
                self.readBswMgrNeeds(child_element, needs)
            elif tag_name == "NV-BLOCK-NEEDS":
                short_name = self.getShortName(child_element)
                needs = NvBlockNeeds(dependency, short_name)
                self.readNvBlockNeeds(child_element, needs)
            elif tag_name == "DIAGNOSTIC-COMMUNICATION-MANAGER-NEEDS":
                short_name = self.getShortName(child_element)
                needs = DiagnosticCommunicationManagerNeeds(dependency, short_name)
                self.readDiagnosticCommunicationManagerNeeds(child_element, needs)
            elif tag_name == "DIAGNOSTIC-ROUTINE-NEEDS":
                short_name = self.getShortName(child_element)
                needs = DiagnosticRoutineNeeds(dependency, short_name)
                self.readDiagnosticRoutineNeeds(child_element, needs)
            elif tag_name == "DIAGNOSTIC-VALUE-NEEDS":
                short_name = self.getShortName(child_element)
                needs = DiagnosticValueNeeds(dependency, short_name)
                self.readDiagnosticValueNeeds(child_element, needs)
            elif tag_name == "DIAGNOSTIC-EVENT-NEEDS":
                short_name = self.getShortName(child_element)
                needs = DiagnosticEventNeeds(dependency, short_name)
                self.readDiagnosticEventNeeds(child_element, needs)
            elif tag_name == "DIAGNOSTIC-EVENT-INFO-NEEDS":
                short_name = self.getShortName(child_element)
                needs = DiagnosticEventInfoNeeds(dependency, short_name)
                self.readDiagnosticEventInfoNeeds(child_element, needs)
            elif tag_name == "DIAGNOSTIC-IO-CONTROL-NEEDS":
                short_name = self.getShortName(child_element)
                needs = DiagnosticIoControlNeeds(dependency, short_name)
                self.readDiagnosticIoControlNeeds(child_element, needs)
            elif tag_name == "DIAGNOSTIC-ENABLE-CONDITION-NEEDS":
                short_name = self.getShortName(child_element)
                needs = DiagnosticEnableConditionNeeds(dependency, short_name)
                self.readDiagnosticEnableConditionNeeds(child_element, needs)
            elif tag_name == "DIAGNOSTIC-OPERATION-CYCLE-NEEDS":
                short_name = self.getShortName(child_element)
                needs = DiagnosticOperationCycleNeeds(dependency, short_name)
                self.readDiagnosticOperationCycleNeeds(child_element, needs)
            elif tag_name == "DIAGNOSTIC-STORAGE-CONDITION-NEEDS":
                short_name = self.getShortName(child_element)
                needs = DiagnosticStorageConditionNeeds(dependency, short_name)
                self.readDiagnosticStorageConditionNeeds(child_element, needs)
            elif tag_name == "INDICATOR-STATUS-NEEDS":
                short_name = self.getShortName(child_element)
                needs = IndicatorStatusNeeds(dependency, short_name)
                self.readIndicatorStatusNeeds(child_element, needs)
            elif tag_name == "FUNCTION-INHIBITION-AVAILABILITY-NEEDS":
                short_name = self.getShortName(child_element)
                needs = FunctionInhibitionAvailabilityNeeds(dependency, short_name)
                self.readFunctionInhibitionAvailabilityNeeds(child_element, needs)
            elif tag_name == "CRYPTO-SERVICE-NEEDS":
                short_name = self.getShortName(child_element)
                needs = CryptoServiceNeeds(dependency, short_name)
                self.readCryptoServiceNeeds(child_element, needs)
            elif tag_name == "ECU-STATE-MGR-USER-NEEDS":
                short_name = self.getShortName(child_element)
                needs = EcuStateMgrUserNeeds(dependency, short_name)
                self.readEcuStateMgrUserNeeds(child_element, needs)
            elif tag_name == "DTC-STATUS-CHANGE-NOTIFICATION-NEEDS":
                short_name = self.getShortName(child_element)
                needs = DtcStatusChangeNotificationNeeds(dependency, short_name)
                self.readDtcStatusChangeNotificationNeeds(child_element, needs)
            elif tag_name == "DLT-USER-NEEDS":
                short_name = self.getShortName(child_element)
                needs = DltUserNeeds(dependency, short_name)
                self.readDltUserNeeds(child_element, needs)
            elif tag_name == "COM-MGR-USER-NEEDS":
                short_name = self.getShortName(child_element)
                needs = ComMgrUserNeeds(dependency, short_name)
                self.readComMgrUserNeeds(child_element, needs)
            elif tag_name == "SUPERVISED-ENTITY-NEEDS":
                short_name = self.getShortName(child_element)
                needs = SupervisedEntityNeeds(dependency, short_name)
                self.readSupervisedEntityNeeds(child_element, needs)
            elif tag_name == "ERROR-TRACER-NEEDS":
                short_name = self.getShortName(child_element)
                needs = ErrorTracerNeeds(dependency, short_name)
                self.readErrorTracerNeeds(child_element, needs)
            elif tag_name == "OBD-INFO-SERVICE-NEEDS":
                short_name = self.getShortName(child_element)
                needs = ObdInfoServiceNeeds(dependency, short_name)
                self.readObdInfoServiceNeeds(child_element, needs)
            elif tag_name == "OBD-MONITOR-SERVICE-NEEDS":
                short_name = self.getShortName(child_element)
                needs = ObdMonitorServiceNeeds(dependency, short_name)
                self.readObdMonitorServiceNeeds(child_element, needs)
            elif tag_name == "OBD-PID-SERVICE-NEEDS":
                short_name = self.getShortName(child_element)
                needs = ObdPidServiceNeeds(dependency, short_name)
                self.readObdPidServiceNeeds(child_element, needs)
            elif tag_name == "OBD-CONTROL-SERVICE-NEEDS":
                short_name = self.getShortName(child_element)
                needs = ObdControlServiceNeeds(dependency, short_name)
                self.readObdControlServiceNeeds(child_element, needs)
            elif tag_name == "OBD-RATIO-SERVICE-NEEDS":
                short_name = self.getShortName(child_element)
                needs = ObdRatioServiceNeeds(dependency, short_name)
                self.readObdRatioServiceNeeds(child_element, needs)
            elif tag_name == "OBD-RATIO-DENOMINATOR-NEEDS":
                short_name = self.getShortName(child_element)
                needs = ObdRatioDenominatorNeeds(dependency, short_name)
                self.readObdRatioDenominatorNeeds(child_element, needs)
            elif tag_name == "DO-IP-ROUTING-ACTIVATION-AUTHENTICATION-NEEDS":
                short_name = self.getShortName(child_element)
                needs = DoIpRoutingActivationAuthenticationNeeds(dependency, short_name)
                self.readDoIpRoutingActivationAuthenticationNeeds(child_element, needs)
            elif tag_name == "DO-IP-ROUTING-ACTIVATION-CONFIRMATION-NEEDS":
                short_name = self.getShortName(child_element)
                needs = DoIpRoutingActivationConfirmationNeeds(dependency, short_name)
                self.readDoIpRoutingActivationConfirmationNeeds(child_element, needs)
            elif tag_name == "SECURE-ON-BOARD-COMMUNICATION-NEEDS":
                short_name = self.getShortName(child_element)
                needs = SecureOnBoardCommunicationNeeds(dependency, short_name)
                self.readSecureOnBoardCommunicationNeeds(child_element, needs)
            elif tag_name == "IDS-MGR-NEEDS":
                short_name = self.getShortName(child_element)
                needs = IdsMgrNeeds(dependency, short_name)
                self.readIdsMgrNeeds(child_element, needs)
            else:
                self.notImplemented("Unsupported service needs <%s>" % tag_name)
                continue
            dependency.setServiceNeeds(needs)

    def readBswServiceDependency(self, element: ET.Element, dependency: BswServiceDependency):
        self.readARObjectAttributes(element, dependency)
        dependency.setIdent(self.getBswServiceDependencyIdent(element, dependency))
        for child_element in self.findall(element, "ASSIGNED-DATA-TYPES/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "ROLE-BASED-DATA-TYPE-ASSIGNMENT":
                dependency.addAssignedDataType(self.getRoleBasedDataTypeAssignment(child_element))
            else:
                self.notImplemented("Unsupported assigned data type <%s>" % tag_name)
        self.readBswServiceDependencyAssignedData(element, dependency)
        self.readBswServiceDependencyAssignedEntryRoles(element, dependency)
        self.readBswServiceDependencyServiceNeeds(element, dependency)
        self.readSymbolicNameProps(element, dependency)

    def readSwcServiceDependencyAssignedData(self, element: ET.Element, dependency: SwcServiceDependency):
        for child_element in self.findall(element, "ASSIGNED-DATAS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "ROLE-BASED-DATA-ASSIGNMENT":
                dependency.AddAssignedData(self.getRoleBasedDataAssignment(child_element))
            else:
                self.raiseError("Unsupported assigned data <%s>" % tag_name)

    def readSwcServiceDependencyAssignedPorts(self, element: ET.Element, dependency: SwcServiceDependency):
        for child_element in self.findall(element, "ASSIGNED-PORTS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "ROLE-BASED-PORT-ASSIGNMENT":
                dependency.AddAssignedPort(self.getRoleBasedPortAssignment(child_element))
            else:
                self.raiseError("Unsupported assigned ports <%s>" % tag_name)

    def readServiceNeeds(self, element: ET.Element, needs: ServiceNeeds):
        self.readIdentifiable(element, needs)

    def readBswMgrNeeds(self, element: ET.Element, needs: BswMgrNeeds):
        self.readServiceNeeds(element, needs)

    def readNvBlockNeeds(self, element: ET.Element, needs: NvBlockNeeds):
        # self.logger.debug("Read NvBlockNeeds <%s>" % needs.getShortName())
        self.readServiceNeeds(element, needs)
        needs.setCalcRamBlockCrc(self.getChildElementOptionalBooleanValue(element, "CALC-RAM-BLOCK-CRC"))
        needs.setCheckStaticBlockId(self.getChildElementOptionalBooleanValue(element, "CHECK-STATIC-BLOCK-ID"))
        needs.setNDataSets(self.getChildElementOptionalNumericalValue(element, "N-DATA-SETS"))
        needs.setNRomBlocks(self.getChildElementOptionalNumericalValue(element, "N-ROM-BLOCKS"))
        needs.setRamBlockStatusControl(self.getChildElementOptionalLiteral(element, "RAM-BLOCK-STATUS-CONTROL"))
        needs.setReadonly(self.getChildElementOptionalBooleanValue(element, "READONLY"))
        needs.setReliability(self.getChildElementOptionalLiteral(element, "RELIABILITY"))
        needs.setResistantToChangedSw(self.getChildElementOptionalBooleanValue(element, "RESISTANT-TO-CHANGED-SW"))
        needs.setRestoreAtStart(self.getChildElementOptionalBooleanValue(element, "RESTORE-AT-START"))
        needs.setStoreAtShutdown(self.getChildElementOptionalBooleanValue(element, "STORE-AT-SHUTDOWN"))
        needs.setStoreCyclic(self.getChildElementOptionalBooleanValue(element, "STORE-CYCLIC"))
        needs.setStoreEmergency(self.getChildElementOptionalBooleanValue(element, "STORE-EMERGENCY"))
        needs.setStoreImmediate(self.getChildElementOptionalBooleanValue(element, "STORE-IMMEDIATE"))
        needs.setUseAutoValidationAtShutDown(self.getChildElementOptionalBooleanValue(element, "USE-AUTO-VALIDATION-AT-SHUT-DOWN"))
        needs.setUseCRCCompMechanism(self.getChildElementOptionalBooleanValue(element, "USE-CRC-COMP-MECHANISM"))
        needs.setWriteOnlyOnce(self.getChildElementOptionalBooleanValue(element, "WRITE-ONLY-ONCE"))
        needs.setWriteVerification(self.getChildElementOptionalBooleanValue(element, "WRITE-VERIFICATION"))
        needs.setWritingFrequency(self.getChildElementOptionalPositiveInteger(element, "WRITING-FREQUENCY"))
        needs.setWritingPriority(self.getChildElementOptionalLiteral(element, "WRITING-PRIORITY"))

    def readDiagnosticCapabilityElement(self, element: ET.Element, needs: DiagnosticCapabilityElement):
        self.readServiceNeeds(element, needs)

    def readObdInfoServiceNeeds(self, element: ET.Element, needs: ObdInfoServiceNeeds):
        self.readDiagnosticCapabilityElement(element, needs)

    def readObdMonitorServiceNeeds(self, element: ET.Element, needs: ObdMonitorServiceNeeds):
        self.readDiagnosticCapabilityElement(element, needs)
        needs.setApplicationDataTypeRef(self.getChildElementOptionalRefType(element, "APPLICATION-DATA-TYPE-REF"))
        needs.setEventNeedsRef(self.getChildElementOptionalRefType(element, "EVENT-NEEDS-REF"))
        needs.setUnitAndScalingId(self.getChildElementOptionalPositiveInteger(element, "UNIT-AND-SCALING-ID"))
        needs.setUpdateKind(self.getChildElementOptionalLiteral(element, "UPDATE-KIND"))

    def readObdPidServiceNeeds(self, element: ET.Element, needs: ObdPidServiceNeeds):
        self.readDiagnosticCapabilityElement(element, needs)

    def readObdControlServiceNeeds(self, element: ET.Element, needs: ObdControlServiceNeeds):
        self.readDiagnosticCapabilityElement(element, needs)

    def readObdRatioServiceNeeds(self, element: ET.Element, needs: ObdRatioServiceNeeds):
        self.readDiagnosticCapabilityElement(element, needs)
        needs.setConnectionType(self.getChildElementOptionalLiteral(element, "CONNECTION-TYPE"))
        needs.setRateBasedMonitoredEventRef(self.getChildElementOptionalRefType(element, "RATE-BASED-MONITORED-EVENT-REF"))
        needs.setUsedFidRef(self.getChildElementOptionalRefType(element, "USED-FID-REF"))

    def readObdRatioDenominatorNeeds(self, element: ET.Element, needs: ObdRatioDenominatorNeeds):
        self.readServiceNeeds(element, needs)
        needs.setDenominatorCondition(self.getChildElementOptionalLiteral(element, "DENOMINATOR-CONDITION"))

    def readDoIpRoutingActivationAuthenticationNeeds(self, element: ET.Element, needs: DoIpRoutingActivationAuthenticationNeeds):
        self.readServiceNeeds(element, needs)
        needs.setDataLengthRequest(self.getChildElementOptionalPositiveInteger(element, "DATA-LENGTH-REQUEST"))
        needs.setDataLengthResponse(self.getChildElementOptionalPositiveInteger(element, "DATA-LENGTH-RESPONSE"))
        child_element = self.find(element, "ROUTING-ACTIVATION-TYPE")
        if child_element is not None:
            needs.setRoutingActivationType(NameToken().setValue(child_element.text or ""))

    def readDoIpRoutingActivationConfirmationNeeds(self, element: ET.Element, needs: DoIpRoutingActivationConfirmationNeeds):
        self.readServiceNeeds(element, needs)
        needs.setDataLengthRequest(self.getChildElementOptionalPositiveInteger(element, "DATA-LENGTH-REQUEST"))
        needs.setDataLengthResponse(self.getChildElementOptionalPositiveInteger(element, "DATA-LENGTH-RESPONSE"))
        child_element = self.find(element, "ROUTING-ACTIVATION-TYPE")
        if child_element is not None:
            needs.setRoutingActivationType(NameToken().setValue(child_element.text or ""))

    def readSecureOnBoardCommunicationNeeds(self, element: ET.Element, needs: SecureOnBoardCommunicationNeeds):
        self.readServiceNeeds(element, needs)
        needs.setVerificationStatusIndicationMode(self.getChildElementOptionalLiteral(element, "VERIFICATION-STATUS-INDICATION-MODE"))

    def readIdsMgrNeeds(self, element: ET.Element, needs: IdsMgrNeeds):
        self.readServiceNeeds(element, needs)
        needs.setUseSmartSensorApi(self.getChildElementOptionalBooleanValue(element, "USE-SMART-SENSOR-API"))

    def readDiagnosticCommunicationManagerNeeds(self, element: ET.Element, needs: DiagnosticCommunicationManagerNeeds):
        # self.logger.debug("Read DiagnosticCommunicationManagerNeeds <%s>" % needs.getShortName())
        self.readDiagnosticCapabilityElement(element, needs)
        needs.setServiceRequestCallbackType(self.getChildElementOptionalLiteral(element, "SERVICE-REQUEST-CALLBACK-TYPE"))

    def readDiagnosticRoutineNeeds(self, element: ET.Element, needs: DiagnosticRoutineNeeds):
        # self.logger.debug("Read DiagnosticRoutineNeeds %s" % needs.getShortName())
        self.readDiagnosticCapabilityElement(element, needs)
        needs.setDiagRoutineType(self.getChildElementOptionalLiteral(element, "DIAG-ROUTINE-TYPE"))
        needs.setRidNumber(self.getChildElementOptionalIntegerValue(element, "RID-NUMBER"))

    def readDiagnosticValueNeeds(self, element: ET.Element, needs: DiagnosticValueNeeds):
        # self.logger.debug("Read DiagnosticValueNeeds %s" % needs.getShortName())
        self.readDiagnosticCapabilityElement(element, needs)
        needs.setDataLength(self.getChildElementOptionalPositiveInteger(element, "DATA-LENGTH"))
        needs.setDiagnosticValueAccess(self.getChildElementOptionalLiteral(element, "DIAGNOSTIC-VALUE-ACCESS"))
        needs.setDidNumber(self.getChildElementOptionalIntegerValue(element, "DID-NUMBER"))
        needs.setFixedLength(self.getChildElementOptionalBooleanValue(element, "FIXED-LENGTH"))
        needs.setProcessingStyle(self.getChildElementOptionalLiteral(element, "PROCESSING-STYLE"))

    def readDiagEventDebounceCounterBased(self, element: ET.Element, algorithm: DiagEventDebounceCounterBased):
        self.readDiagnosticCapabilityElement(element, algorithm)

    def readDiagEventDebounceMonitorInternal(self, element: ET.Element, algorithm: DiagEventDebounceMonitorInternal):
        self.readDiagnosticCapabilityElement(element, algorithm)

    def readDiagEventDebounceTimeBased(self, element: ET.Element, algorithm: DiagEventDebounceTimeBased):
        self.readDiagnosticCapabilityElement(element, algorithm)

    def readDiagEventDebounceAlgorithm(self, element: ET.Element, needs: DiagnosticEventNeeds):
        for child_element in self.findall(element, "DIAG-EVENT-DEBOUNCE-ALGORITHM/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "DIAG-EVENT-DEBOUNCE-COUNTER-BASED":
                algorithm = needs.createDiagEventDebounceCounterBased(self.getShortName(child_element))
                self.readDiagEventDebounceCounterBased(child_element, algorithm)
            elif tag_name == "DIAG-EVENT-DEBOUNCE-MONITOR-INTERNAL":
                algorithm = needs.createDiagEventDebounceMonitorInternal(self.getShortName(child_element))
                self.readDiagEventDebounceMonitorInternal(child_element, algorithm)
            elif tag_name == "DIAG-EVENT-DEBOUNCE-TIME-BASED":
                algorithm = needs.createDiagEventDebounceTimeBased(self.getShortName(child_element))
                self.readDiagEventDebounceTimeBased(child_element, algorithm)
            else:
                self.notImplemented("Unsupported DiagEventDebounceAlgorithm <%s>" % tag_name)

    def readDiagnosticEventNeeds(self, element: ET.Element, needs: DiagnosticEventNeeds):
        # self.logger.debug("Read DiagnosticEventNeeds <%s>" % needs.getShortName())
        self.readDiagnosticCapabilityElement(element, needs)
        for ref in self.getChildElementRefTypeList(element, "DEFERRING-FID-REFS/DEFERRING-FID-REF"):
            needs.addDeferringFidRef(ref)
        self.readDiagEventDebounceAlgorithm(element, needs)
        needs.setInhibitingFidRef(self.getChildElementOptionalRefType(element, "INHIBITING-FID-REF"))
        for ref in self.getChildElementRefTypeList(element, "INHIBITING-SECONDARY-FID-REFS/INHIBITING-SECONDARY-FID-REF"):
            needs.addInhibitingSecondaryFidRef(ref)
        needs.setPrestoredFreezeframeStoredInNvm(self.getChildElementOptionalBooleanValue(element, "PRESTORED-FREEZEFRAME-STORED-IN-NVM"))
        needs.setUsesMonitorData(self.getChildElementOptionalBooleanValue(element, "USES-MONITOR-DATA"))

    def readDiagnosticEventInfoNeeds(self, element: ET.Element, needs: DiagnosticEventInfoNeeds):
        # self.logger.debug("Read DiagnosticEventInfoNeeds <%s>" % needs.getShortName())
        self.readDiagnosticCapabilityElement(element, needs)
        needs.setDtcKind(self.getChildElementOptionalLiteral(element, "DTC-KIND"))
        needs.setUdsDtcNumber(self.getChildElementOptionalPositiveInteger(element, "UDS-DTC-NUMBER"))

    def readDiagnosticIoControlNeeds(self, element: ET.Element, needs: DiagnosticIoControlNeeds):
        # self.logger.debug("Read DiagnosticIoControlNeeds %s" % needs.getShortName())
        self.readDiagnosticCapabilityElement(element, needs)
        needs.setCurrentValueRef(self.getChildElementOptionalRefType(element, "CURRENT-VALUE-REF"))
        needs.setFreezeCurrentStateSupported(self.getChildElementOptionalBooleanValue(element, "FREEZE-CURRENT-STATE-SUPPORTED"))
        needs.setResetToDefaultSupported(self.getChildElementOptionalBooleanValue(element, "RESET-TO-DEFAULT-SUPPORTED"))
        needs.setShortTermAdjustmentSupported(self.getChildElementOptionalBooleanValue(element, "SHORT-TERM-ADJUSTMENT-SUPPORTED"))

    def readDiagnosticEnableConditionNeeds(self, element: ET.Element, needs: DiagnosticEnableConditionNeeds):
        # self.logger.debug("Read DiagnosticEnableConditionNeeds %s" % needs.getShortName())
        self.readDiagnosticCapabilityElement(element, needs)
        needs.setInitialStatus(self.getChildElementOptionalLiteral(element, "INITIAL-STATUS"))

    def readDiagnosticOperationCycleNeeds(self, element: ET.Element, needs: DiagnosticOperationCycleNeeds):
        # self.logger.debug("Read DiagnosticOperationCycleNeeds %s" % needs.getShortName())
        self.readDiagnosticCapabilityElement(element, needs)
        needs.setOperationCycle(self.getChildElementOptionalLiteral(element, "OPERATION-CYCLE"))

    def readDiagnosticStorageConditionNeeds(self, element: ET.Element, needs: DiagnosticStorageConditionNeeds):
        # self.logger.debug("Read DiagnosticStorageConditionNeeds %s" % needs.getShortName())
        self.readDiagnosticCapabilityElement(element, needs)
        needs.setInitialStatus(self.getChildElementOptionalLiteral(element, "INITIAL-STATUS"))

    def readIndicatorStatusNeeds(self, element: ET.Element, needs: IndicatorStatusNeeds):
        # self.logger.debug("Read IndicatorStatusNeeds %s" % needs.getShortName())
        self.readServiceNeeds(element, needs)
        needs.setType(self.getChildElementOptionalLiteral(element, "TYPE"))

    def readFunctionInhibitionAvailabilityNeeds(self, element: ET.Element, needs: FunctionInhibitionAvailabilityNeeds):
        # self.logger.debug("Read FunctionInhibitionAvailabilityNeeds %s" % needs.getShortName())
        self.readServiceNeeds(element, needs)
        needs.setControlledFidRef(self.getChildElementOptionalRefType(element, "CONTROLLED-FID-REF"))

    def readCryptoServiceNeeds(self, element: ET.Element, needs: CryptoServiceNeeds):
        # self.logger.debug("Read CryptoServiceNeeds <%s>" % needs.getShortName())
        self.readServiceNeeds(element, needs)
        needs.setMaximumKeyLength(self.getChildElementOptionalPositiveInteger(element, "MAXIMUM-KEY-LENGTH"))

    def readEcuStateMgrUserNeeds(self, element: ET.Element, needs: EcuStateMgrUserNeeds):
        # self.logger.debug("Read EcuStateMgrUserNeeds %s" % needs.getShortName())
        self.readServiceNeeds(element, needs)

    def readDtcStatusChangeNotificationNeeds(self, element: ET.Element, needs: DtcStatusChangeNotificationNeeds):
        # self.logger.debug("Read DtcStatusChangeNotificationNeeds %s" % needs.getShortName())
        self.readDiagnosticCapabilityElement(element, needs)
        needs.setDtcFormatType(self.getChildElementOptionalLiteral(element, "DTC-FORMAT-TYPE"))

    def readDltUserNeeds(self, element: ET.Element, needs: DltUserNeeds):
        # self.logger.debug("Read DltUserNeeds %s" % needs.getShortName())
        self.readServiceNeeds(element, needs)

    def readComMgrUserNeeds(self, element: ET.Element, needs: ComMgrUserNeeds):
        # self.logger.debug("Read ComMgrUserNeeds %s" % needs.getShortName())
        self.readServiceNeeds(element, needs)
        needs.setMaxCommMode(self.getChildElementOptionalLiteral(element, "MAX-COMM-MODE"))

    def readSupervisedEntityNeeds(self, element: ET.Element, needs: SupervisedEntityNeeds):
        self.readServiceNeeds(element, needs)
        needs.setActivateAtStart(self.getChildElementOptionalBooleanValue(element, "ACTIVATE-AT-START"))
        for ref in self.getChildElementRefTypeList(element, "CHECKPOINTSS/SUPERVISED-ENTITY-CHECKPOINT-NEEDS-REF-CONDITIONAL/SUPERVISED-ENTITY-CHECKPOINT-NEEDS-REF"):
            needs.addCheckpointsRef(ref)
        needs.setEnableDeactivation(self.getChildElementOptionalBooleanValue(element, "ENABLE-DEACTIVATION"))
        needs.setExpectedAliveCycle(self.getChildElementOptionalTimeValue(element, "EXPECTED-ALIVE-CYCLE"))
        needs.setMaxAliveCycle(self.getChildElementOptionalTimeValue(element, "MAX-ALIVE-CYCLE"))
        needs.setMinAliveCycle(self.getChildElementOptionalTimeValue(element, "MIN-ALIVE-CYCLE"))
        needs.setToleratedFailedCycles(self.getChildElementOptionalPositiveInteger(element, "TOLERATED-FAILED-CYCLES"))

    def readTracedFailure(self, element: ET.Element, failure: TracedFailure):
        self.readIdentifiable(element, failure)
        failure.setId(self.getChildElementOptionalPositiveInteger(element, "ID"))

    def readDevelopmentError(self, element: ET.Element, failure: DevelopmentError):
        self.readTracedFailure(element, failure)

    def readRuntimeError(self, element: ET.Element, failure: RuntimeError):
        self.readTracedFailure(element, failure)

    def readPossibleErrorReaction(self, element: ET.Element, reaction: PossibleErrorReaction):
        self.readIdentifiable(element, reaction)
        reaction.setReactionCode(self.getChildElementOptionalPositiveInteger(element, "REACTION-CODE"))

    def readTransientFault(self, element: ET.Element, failure: TransientFault):
        self.readTracedFailure(element, failure)
        for child_element in self.findall(element, "POSSIBLE-ERROR-REACTIONS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "POSSIBLE-ERROR-REACTION":
                reaction = failure.createPossibleErrorReaction(self.getShortName(child_element))
                self.readPossibleErrorReaction(child_element, reaction)
            else:
                self.notImplemented("Unsupported PossibleErrorReaction <%s>" % tag_name)

    def readErrorTracerNeeds(self, element: ET.Element, needs: ErrorTracerNeeds):
        # self.logger.debug("Read ErrorTracerNeeds <%s>" % needs.getShortName())
        self.readServiceNeeds(element, needs)
        for child_element in self.findall(element, "TRACED-FAILURES/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "DEVELOPMENT-ERROR":
                failure = needs.createDevelopmentError(self.getShortName(child_element))
                self.readDevelopmentError(child_element, failure)
            elif tag_name == "RUNTIME-ERROR":
                failure = needs.createRuntimeError(self.getShortName(child_element))
                self.readRuntimeError(child_element, failure)
            elif tag_name == "TRANSIENT-FAULT":
                failure = needs.createTransientFault(self.getShortName(child_element))
                self.readTransientFault(child_element, failure)
            else:
                self.notImplemented("Unsupported traced failure <%s>" % tag_name)

    def readSwcServiceDependencyServiceNeeds(self, element: ET.Element, parent: SwcServiceDependency):
        for child_element in self.findall(element, "SERVICE-NEEDS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "NV-BLOCK-NEEDS":
                needs = parent.createNvBlockNeeds(self.getShortName(child_element))
                self.readNvBlockNeeds(child_element, needs)
            elif tag_name == "DIAGNOSTIC-COMMUNICATION-MANAGER-NEEDS":
                needs = parent.createDiagnosticCommunicationManagerNeeds(self.getShortName(child_element))
                self.readDiagnosticCommunicationManagerNeeds(child_element, needs)
            elif tag_name == "DIAGNOSTIC-ROUTINE-NEEDS":
                needs = parent.createDiagnosticRoutineNeeds(self.getShortName(child_element))
                self.readDiagnosticRoutineNeeds(child_element, needs)
            elif tag_name == "DIAGNOSTIC-VALUE-NEEDS":
                needs = parent.createDiagnosticValueNeeds(self.getShortName(child_element))
                self.readDiagnosticValueNeeds(child_element, needs)
            elif tag_name == "DIAGNOSTIC-EVENT-NEEDS":
                needs = parent.createDiagnosticEventNeeds(self.getShortName(child_element))
                self.readDiagnosticEventNeeds(child_element, needs)
            elif tag_name == "DIAGNOSTIC-EVENT-INFO-NEEDS":
                needs = parent.createDiagnosticEventInfoNeeds(self.getShortName(child_element))
                self.readDiagnosticEventInfoNeeds(child_element, needs)
            elif tag_name == "DIAGNOSTIC-IO-CONTROL-NEEDS":
                needs = parent.createDiagnosticIoControlNeeds(self.getShortName(child_element))
                self.readDiagnosticIoControlNeeds(child_element, needs)
            elif tag_name == "CRYPTO-SERVICE-NEEDS":
                needs = parent.createCryptoServiceNeeds(self.getShortName(child_element))
                self.readCryptoServiceNeeds(child_element, needs)
            elif tag_name == "ECU-STATE-MGR-USER-NEEDS":
                needs = parent.createEcuStateMgrUserNeeds(self.getShortName(child_element))
                self.readEcuStateMgrUserNeeds(child_element, needs)
            elif tag_name == "DTC-STATUS-CHANGE-NOTIFICATION-NEEDS":
                needs = parent.createDtcStatusChangeNotificationNeeds(self.getShortName(child_element))
                self.readDtcStatusChangeNotificationNeeds(child_element, needs)
            elif tag_name == "DLT-USER-NEEDS":
                needs = parent.createDltUserNeeds(self.getShortName(child_element))
                self.readDltUserNeeds(child_element, needs)
            elif tag_name == "COM-MGR-USER-NEEDS":
                needs = parent.createComMgrUserNeeds(self.getShortName(child_element))
                self.readComMgrUserNeeds(child_element, needs)
            elif tag_name == "ERROR-TRACER-NEEDS":
                needs = parent.createErrorTracerNeeds(self.getShortName(child_element))
                self.readErrorTracerNeeds(child_element, needs)
            elif tag_name == "DIAGNOSTIC-ENABLE-CONDITION-NEEDS":
                needs = parent.createDiagnosticEnableConditionNeeds(self.getShortName(child_element))
                self.readDiagnosticEnableConditionNeeds(child_element, needs)
            elif tag_name == "DIAGNOSTIC-OPERATION-CYCLE-NEEDS":
                needs = parent.createDiagnosticOperationCycleNeeds(self.getShortName(child_element))
                self.readDiagnosticOperationCycleNeeds(child_element, needs)
            elif tag_name == "DIAGNOSTIC-STORAGE-CONDITION-NEEDS":
                needs = parent.createDiagnosticStorageConditionNeeds(self.getShortName(child_element))
                self.readDiagnosticStorageConditionNeeds(child_element, needs)
            elif tag_name == "INDICATOR-STATUS-NEEDS":
                needs = parent.createIndicatorStatusNeeds(self.getShortName(child_element))
                self.readIndicatorStatusNeeds(child_element, needs)
            elif tag_name == "FUNCTION-INHIBITION-AVAILABILITY-NEEDS":
                needs = parent.createFunctionInhibitionAvailabilityNeeds(self.getShortName(child_element))
                self.readFunctionInhibitionAvailabilityNeeds(child_element, needs)
            elif tag_name == "OBD-INFO-SERVICE-NEEDS":
                needs = parent.createObdInfoServiceNeeds(self.getShortName(child_element))
                self.readObdInfoServiceNeeds(child_element, needs)
            elif tag_name == "OBD-MONITOR-SERVICE-NEEDS":
                needs = parent.createObdMonitorServiceNeeds(self.getShortName(child_element))
                self.readObdMonitorServiceNeeds(child_element, needs)
            elif tag_name == "OBD-PID-SERVICE-NEEDS":
                needs = parent.createObdPidServiceNeeds(self.getShortName(child_element))
                self.readObdPidServiceNeeds(child_element, needs)
            elif tag_name == "OBD-CONTROL-SERVICE-NEEDS":
                needs = parent.createObdControlServiceNeeds(self.getShortName(child_element))
                self.readObdControlServiceNeeds(child_element, needs)
            elif tag_name == "OBD-RATIO-SERVICE-NEEDS":
                needs = parent.createObdRatioServiceNeeds(self.getShortName(child_element))
                self.readObdRatioServiceNeeds(child_element, needs)
            elif tag_name == "OBD-RATIO-DENOMINATOR-NEEDS":
                needs = parent.createObdRatioDenominatorNeeds(self.getShortName(child_element))
                self.readObdRatioDenominatorNeeds(child_element, needs)
            elif tag_name == "DO-IP-ROUTING-ACTIVATION-AUTHENTICATION-NEEDS":
                needs = parent.createDoIpRoutingActivationAuthenticationNeeds(self.getShortName(child_element))
                self.readDoIpRoutingActivationAuthenticationNeeds(child_element, needs)
            elif tag_name == "DO-IP-ROUTING-ACTIVATION-CONFIRMATION-NEEDS":
                needs = parent.createDoIpRoutingActivationConfirmationNeeds(self.getShortName(child_element))
                self.readDoIpRoutingActivationConfirmationNeeds(child_element, needs)
            elif tag_name == "SECURE-ON-BOARD-COMMUNICATION-NEEDS":
                needs = parent.createSecureOnBoardCommunicationNeeds(self.getShortName(child_element))
                self.readSecureOnBoardCommunicationNeeds(child_element, needs)
            elif tag_name == "IDS-MGR-NEEDS":
                needs = parent.createIdsMgrNeeds(self.getShortName(child_element))
                self.readIdsMgrNeeds(child_element, needs)
            else:
                self.notImplemented("Unsupported service needs <%s>" % tag_name)

    def readSwcServiceDependencyRepresentedPortGroup(self, element: ET.Element, dependency: SwcServiceDependency):
        ref = self.getChildElementOptionalRefType(element, "REPRESENTED-PORT-GROUP-REF")
        if ref is not None:
            dependency.setRepresentedPortGroup(ref)

    def readSwcServiceDependency(self, element: ET.Element, parent: SwcInternalBehavior):
        short_name = self.getShortName(element)
        dependency = parent.createSwcServiceDependency(short_name)
        # self.logger.debug("Read SwcServiceDependency %s" % short_name)
        self.readServiceDependency(element, dependency)
        self.readSwcServiceDependencyAssignedData(element, dependency)
        self.readSwcServiceDependencyAssignedPorts(element, dependency)
        self.readSwcServiceDependencyServiceNeeds(element, dependency)
        self.readSwcServiceDependencyRepresentedPortGroup(element, dependency)

    def readSwcInternalBehaviorServiceDependencies(self, element: ET.Element, parent: SwcInternalBehavior):
        for child_element in self.findall(element, "SERVICE-DEPENDENCYS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "SWC-SERVICE-DEPENDENCY":
                self.readSwcServiceDependency(child_element, parent)
            else:
                self.notImplemented("Unsupported Service Dependencies <%s>" % tag_name)

    def getIncludedDataTypeSets(self, element: ET.Element) -> List[IncludedDataTypeSet]:
        include_data_type_sets = []
        for child_element in self.findall(element, "INCLUDED-DATA-TYPE-SETS/INCLUDED-DATA-TYPE-SET"):
            include_data_type_set = IncludedDataTypeSet()
            self.readARObjectAttributes(child_element, include_data_type_set)
            include_data_type_set.setLiteralPrefix(self.getChildElementOptionalLiteral(child_element, "LITERAL-PREFIX"))
            for ref_type in self.getChildElementRefTypeList(child_element, "DATA-TYPE-REFS/DATA-TYPE-REF"):
                include_data_type_set.addDataTypeRef(ref_type)
            include_data_type_sets.append(include_data_type_set)
        return include_data_type_sets

    def readSwcInternalBehaviorArTypedPerInstanceMemories(self, element: ET.Element, parent: SwcInternalBehavior):
        for child_element in self.findall(element, "AR-TYPED-PER-INSTANCE-MEMORYS/VARIABLE-DATA-PROTOTYPE"):
            short_name = self.getShortName(child_element)
            prototype = parent.createArTypedPerInstanceMemory(short_name)
            self.readVariableDataPrototype(child_element, prototype)

    def readSwcInternalBehaviorSharedParameters(self, element: ET.Element, behavior: SwcInternalBehavior):
        for child_element in self.findall(element, "SHARED-PARAMETERS/PARAMETER-DATA-PROTOTYPE"):
            short_name = self.getShortName(child_element)
            prototype = behavior.createSharedParameter(short_name)
            self.readParameterDataPrototype(child_element, prototype)

    def readVariationPointProxy(self, element: ET.Element, proxy: VariationPointProxy):
        self.readIdentifiable(element, proxy)
        condition_element = self.find(element, "CONDITION-ACCESS")
        if condition_element is not None:
            proxy.setConditionAccess(self.readConditionByFormula(condition_element, ConditionByFormula()))
        proxy.setImplementationDataTypeRef(self.getChildElementOptionalRefType(element, "IMPLEMENTATION-DATA-TYPE-REF"))
        proxy.setPostBuildValueAccessRef(self.getChildElementOptionalRefType(element, "POST-BUILD-VALUE-ACCESS-REF"))
        for child_element in self.findall(element, "POST-BUILD-VARIANT-CONDITIONS/POST-BUILD-VARIANT-CONDITION"):
            proxy.addPostBuildVariantCondition(self.readPostBuildVariantCondition(child_element, PostBuildVariantCondition()))
        value_access_element = self.find(element, "VALUE-ACCESS")
        if value_access_element is not None:
            for child_element in value_access_element:
                tag = self.getTagName(child_element)
                avp_class = VALUE_ACCESS_TAG_TO_CLASS.get(tag)
                if avp_class is not None:
                    proxy.setValueAccess(self.readAttributeValueVariationPoint(child_element, avp_class()))
                else:
                    self.notImplemented("Unsupported VALUE-ACCESS content <%s>" % tag)

    def readAttributeValueVariationPoint(self, element: ET.Element, avp: AttributeValueVariationPoint) -> AttributeValueVariationPoint:
        self.readARObjectAttributes(element, avp)
        if "BINDING-TIME" in element.attrib:
            binding_time = None
            for camel, token in BINDING_TIME_XML_MAP.items():
                if token == element.attrib["BINDING-TIME"]:
                    binding_time = camel
                    break
            if binding_time is not None:
                avp.setBindingTime(BindingTimeEnum().setValue(binding_time))
            else:
                self.notImplemented("Unsupported BINDING-TIME <%s>" % element.attrib["BINDING-TIME"])
        if "BLUEPRINT-VALUE" in element.attrib:
            avp.setBlueprintValue(String().setValue(element.attrib["BLUEPRINT-VALUE"]))
        if "SD" in element.attrib:
            avp.setSd(String().setValue(element.attrib["SD"]))
        if "SHORT-LABEL" in element.attrib:
            avp.setShortLabel(PrimitiveIdentifier().setValue(element.attrib["SHORT-LABEL"]))
        if isinstance(avp, LimitValueVariationPoint) and "INTERVAL-TYPE" in element.attrib:
            interval_type = None
            for value, token in INTERVAL_TYPE_XML_MAP.items():
                if token == element.attrib["INTERVAL-TYPE"]:
                    interval_type = value
                    break
            if interval_type is not None:
                avp.setIntervalType(IntervalTypeEnum().setValue(interval_type))
            else:
                self.notImplemented("Unsupported INTERVAL-TYPE <%s>" % element.attrib["INTERVAL-TYPE"])
        if element.text is not None and element.text.strip() != "":
            avp.setText(element.text)
        return avp

    def readSwcInternalBehaviorVariationPointProxies(self, element: ET.Element, behavior: SwcInternalBehavior):
        for child_element in self.findall(element, "VARIATION-POINT-PROXYS/VARIATION-POINT-PROXY"):
            short_name = self.getShortName(child_element)
            proxy = VariationPointProxy(behavior, short_name)
            self.readVariationPointProxy(child_element, proxy)
            behavior.addVariationPointProxy(proxy)

    def readIncludedModeDeclarationGroupSet(self, element: ET.Element, group_set: IncludedModeDeclarationGroupSet):
        for ref in self.getChildElementRefTypeList(element, "MODE-DECLARATION-GROUP-REFS/MODE-DECLARATION-GROUP-REF"):
            group_set.addModeDeclarationGroupRef(ref)
        group_set.setPrefix(self.getChildElementOptionalLiteral(element, "PREFIX"))

    def readSwcInternalBehaviorIncludedModeDeclarationGroupSets(self, element: ET.Element, behavior: SwcInternalBehavior):
        for child_element in self.findall(element, "INCLUDED-MODE-DECLARATION-GROUP-SETS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "INCLUDED-MODE-DECLARATION-GROUP-SET":
                group_set = IncludedModeDeclarationGroupSet()
                self.readIncludedModeDeclarationGroupSet(child_element, group_set)
                behavior.addIncludedModeDeclarationGroupSet(group_set)
            else:
                self.notImplemented("Unsupported IncludedModeDeclarationGroupSet <%s>" % tag_name)

    def readSwcInternalBehaviorExclusiveAreaPolicies(self, element: ET.Element, behavior: SwcInternalBehavior):
        for child_element in self.findall(element, "EXCLUSIVE-AREA-POLICYS/SWC-EXCLUSIVE-AREA-POLICY"):
            policy = SwcExclusiveAreaPolicy()
            policy.setApiPrinciple(self.getChildElementOptionalLiteral(child_element, "API-PRINCIPLE"))
            policy.setExclusiveAreaRef(self.getChildElementOptionalRefType(child_element, "EXCLUSIVE-AREA-REF"))
            behavior.addExclusiveAreaPolicy(policy)

    def readSwcInternalBehavior(self, element: ET.Element, behavior: SwcInternalBehavior):
        # read the internal behavior
        self.readInternalBehavior(element, behavior)

        # read the extra SwcInternalBehavior
        self.readSwcInternalBehaviorArTypedPerInstanceMemories(element, behavior)
        self.readSwcInternalBehaviorExclusiveAreaPolicies(element, behavior)
        self.readSwcInternalBehaviorEvents(element, behavior)
        self.readSwcInternalBehaviorExplicitInterRunnableVariables(element, behavior)
        behavior.setHandleTerminationAndRestart(self.getChildElementOptionalLiteral(element, "HANDLE-TERMINATION-AND-RESTART"))
        self.readSwcInternalBehaviorIncludedModeDeclarationGroupSets(element, behavior)
        self.readSwcInternalBehaviorInstantiationDataDefProps(element, behavior)
        self.readSwcInternalBehaviorPerInstanceMemories(element, behavior)
        self.readSwcInternalBehaviorPerInstanceParameters(element, behavior)
        self.readSwcInternalBehaviorPortAPIOptions(element, behavior)
        self.readSwcInternalBehaviorRunnables(element, behavior)
        self.readSwcInternalBehaviorServiceDependencies(element, behavior)
        self.readSwcInternalBehaviorSharedParameters(element, behavior)
        self.readSwcInternalBehaviorVariationPointProxies(element, behavior)
        behavior.setSupportsMultipleInstantiation(self.getChildElementOptionalBooleanValue(element, "SUPPORTS-MULTIPLE-INSTANTIATION"))

    def readSwcInternalBehaviorInstantiationDataDefProps(self, element: ET.Element, behavior: SwcInternalBehavior):
        for child_element in self.findall(element, "INSTANTIATION-DATA-DEF-PROPSS/INSTANTIATION-DATA-DEF-PROPS"):
            props = InstantiationDataDefProps()
            self.readARObjectAttributes(child_element, props)
            props.setParameterInstance(self.getAutosarParameterRef(child_element, "PARAMETER-INSTANCE"))
            props.setSwDataDefProps(self.getSwDataDefProps(child_element, "SW-DATA-DEF-PROPS"))
            props.setVariableInstance(self.getAutosarVariableRef(child_element, "VARIABLE-INSTANCE"))
            behavior.addInstantiationDataDefProps(props)

    def readAtomicSwComponentTypeSwcInternalBehavior(self, element: ET.Element, parent: AtomicSwComponentType):
        for child_element in self.findall(element, "INTERNAL-BEHAVIORS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "SWC-INTERNAL-BEHAVIOR":
                behavior = parent.createSwcInternalBehavior(self.getShortName(child_element))
                self.readSwcInternalBehavior(child_element, behavior)
            else:
                self.notImplemented("Unsupported Internal Behaviors <%s>" % tag_name)

    def getIncludedModeDeclarationGroupSets(self, element: ET.Element) -> List[IncludedModeDeclarationGroupSet]:
        group_sets = []
        for child_element in self.findall(element, "INCLUDED-MODE-DECLARATION-GROUP-SETS/INCLUDED-MODE-DECLARATION-GROUP-SET"):
            group_set = IncludedModeDeclarationGroupSet()
            for ref_type in self.getChildElementRefTypeList(child_element, "MODE-DECLARATION-GROUP-REFS/MODE-DECLARATION-GROUP-REF"):
                group_set.addModeDeclarationGroupRef(ref_type)
            group_sets.append(group_set)
        return group_sets

    def readBswVariableAccess(self, element: ET.Element, access: BswVariableAccess):
        self.readReferrable(element, access)
        access.setAccessedVariableRef(self.getChildElementOptionalRefType(element, "ACCESSED-VARIABLE-REF"))

    def readBswModuleEntityDataSendPoints(self, element: ET.Element, entity: BswModuleEntity):
        for child_element in self.findall(element, "DATA-SEND-POINTS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "BSW-VARIABLE-ACCESS":
                point = entity.createDataSendPoint(self.getShortName(child_element))
                self.readBswVariableAccess(child_element, point)
            else:
                self.notImplemented("Unsupported Data Send Point <%s>" % tag_name)

    def readBswModuleEntityDataReceiverPoints(self, element: ET.Element, entity: BswModuleEntity):
        for child_element in self.findall(element, "DATA-RECEIVE-POINTS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "BSW-VARIABLE-ACCESS":
                point = entity.createDataReceivePoint(self.getShortName(child_element))
                self.readBswVariableAccess(child_element, point)
            else:
                self.notImplemented("Unsupported Data Receive Point <%s>" % tag_name)

    def readBswModuleEntityIssuedTriggerRefs(self, element: ET.Element, entity: BswModuleEntity):
        for ref in self.getChildElementRefTypeList(element, "ISSUED-TRIGGERS/TRIGGER-REF-CONDITIONAL/TRIGGER-REF"):
            entity.addIssuedTriggerRef(ref)

    def readBswModuleEntityActivationPointRefs(self, element: ET.Element, entity: BswModuleEntity):
        for ref in self.getChildElementRefTypeList(element, "ACTIVATION-POINTS/BSW-INTERNAL-TRIGGERING-POINT-REF-CONDITIONAL/BSW-INTERNAL-TRIGGERING-POINT-REF"):  # noqa E501
            entity.addActivationPointRef(ref)

    def readBswModuleCallPoint(self, element: ET.Element, point: BswModuleCallPoint):
        self.readReferrable(element, point)

    def readBswAsynchronousServerCallPoint(self, element: ET.Element, point: BswAsynchronousServerCallPoint):
        self.readBswModuleCallPoint(element, point)
        point.setCalledEntryRef(self.getChildElementOptionalRefType(element, "CALLED-ENTRY-REF"))

    def readBswSynchronousServerCallPoint(self, element: ET.Element, point: BswSynchronousServerCallPoint):
        self.readBswModuleCallPoint(element, point)
        point.setCalledEntryRef(self.getChildElementOptionalRefType(element, "CALLED-ENTRY-REF"))

    def readBswModuleEntityCallPoints(self, element: ET.Element, entity: BswModuleEntity):
        for child_element in self.findall(element, "CALL-POINTS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "BSW-ASYNCHRONOUS-SERVER-CALL-POINT":
                point = entity.createBswAsynchronousServerCallPoint(self.getShortName(child_element))
                self.readBswAsynchronousServerCallPoint(child_element, point)
            elif tag_name == "BSW-SYNCHRONOUS-SERVER-CALL-POINT":
                point = entity.createBswSynchronousServerCallPoint(self.getShortName(child_element))
                self.readBswSynchronousServerCallPoint(child_element, point)
            else:
                self.notImplemented("Unsupported Call Point <%s>" % tag_name)

    def readBswModuleEntity(self, element: ET.Element, entity: BswModuleEntity):
        self.readExecutableEntity(element, entity)
        self.readBswModuleEntityActivationPointRefs(element, entity)
        self.readBswModuleEntityCallPoints(element, entity)
        self.readBswModuleEntityDataReceiverPoints(element, entity)
        self.readBswModuleEntityDataSendPoints(element, entity)
        entity.setImplementedEntryRef(self.getChildElementRefType(entity.getShortName(), element, "IMPLEMENTED-ENTRY-REF"))
        entity.setSchedulerNamePrefixRef(self.getChildElementOptionalRefType(element, "SCHEDULER-NAME-PREFIX-REF"))
        self.readBswModuleEntityAccessedModeGroups(element, entity)
        self.readBswModuleEntityManagedModeGroups(element, entity)
        self.readBswModuleEntityIssuedTriggerRefs(element, entity)

    def readBswCalledEntity(self, element: ET.Element, entity: BswCalledEntity):
        # self.logger.debug("Read BswCalledEntity %s" % entity.getShortName())
        self.readBswModuleEntity(element, entity)

    def readBswSchedulableEntity(self, element: ET.Element, entity: BswSchedulableEntity):
        # self.logger.debug("Read BswSchedulableEntity %s" % entity.getShortName())
        self.readBswModuleEntity(element, entity)

    def readBswInterruptEntity(self, element: ET.Element, entity: BswInterruptEntity):
        # self.logger.debug("Read BswSchedulableEntity %s" % entity.getShortName())
        self.readBswModuleEntity(element, entity)
        entity.setInterruptCategory(self.getChildElementOptionalLiteral(element, "INTERRUPT-CATEGORY"))
        entity.setInterruptSource(self.getChildElementOptionalLiteral(element, "INTERRUPT-SOURCE"))

    def readBswInternalBehaviorEntities(self, element: ET.Element, behavior: BswInternalBehavior):
        for child_element in self.findall(element, "ENTITYS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "BSW-CALLED-ENTITY":
                entity = behavior.createBswCalledEntity(self.getShortName(child_element))
                self.readBswCalledEntity(child_element, entity)
            elif tag_name == "BSW-SCHEDULABLE-ENTITY":
                entity = behavior.createBswSchedulableEntity(self.getShortName(child_element))
                self.readBswSchedulableEntity(child_element, entity)
            elif tag_name == "BSW-INTERRUPT-ENTITY":
                entity = behavior.createBswInterruptEntity(self.getShortName(child_element))
                self.readBswInterruptEntity(child_element, entity)
            else:
                self.notImplemented("Unsupported BswModuleEntity <%s>" % tag_name)

    def readBswBackgroundEvent(self, element: ET.Element, event: BswBackgroundEvent):
        self.readBswScheduleEvent(element, event)

    def readBswExternalTriggerOccurredEvent(self, element: ET.Element, event: BswExternalTriggerOccurredEvent):
        self.readBswScheduleEvent(element, event)
        event.setTriggerRef(self.getChildElementOptionalRefType(element, "TRIGGER-REF"))

    def readBswOperationInvokedEvent(self, element: ET.Element, event: BswOperationInvokedEvent):
        self.readBswEvent(element, event)
        event.setEntryRef(self.getChildElementOptionalRefType(element, "ENTRY-REF"))

    def readBswInternalBehaviorEvents(self, element: ET.Element, behavior: BswInternalBehavior):
        for child_element in self.findall(element, "EVENTS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "BSW-MODE-SWITCH-EVENT":
                event = behavior.createBswModeSwitchEvent(self.getShortName(child_element))
                self.readBswModeSwitchEvent(child_element, event)
            elif tag_name == "BSW-MODE-MANAGER-ERROR-EVENT":
                event = behavior.createBswModeManagerErrorEvent(self.getShortName(child_element))
                self.readBswModeManagerErrorEvent(child_element, event)
            elif tag_name == "BSW-MODE-SWITCHED-ACK-EVENT":
                event = behavior.createBswModeSwitchedAckEvent(self.getShortName(child_element))
                self.readBswModeSwitchedAckEvent(child_element, event)
            elif tag_name == "BSW-TIMING-EVENT":
                event = behavior.createBswTimingEvent(self.getShortName(child_element))
                self.readBswTimingEvent(child_element, event)
            elif tag_name == "BSW-DATA-RECEIVED-EVENT":
                event = behavior.createBswDataReceivedEvent(self.getShortName(child_element))
                self.readBswDataReceivedEvent(child_element, event)
            elif tag_name == "BSW-INTERNAL-TRIGGER-OCCURRED-EVENT":
                event = behavior.createBswInternalTriggerOccurredEvent(self.getShortName(child_element))
                self.readBswInternalTriggerOccurredEvent(child_element, event)
            elif tag_name == "BSW-BACKGROUND-EVENT":
                event = behavior.createBswBackgroundEvent(self.getShortName(child_element))
                self.readBswBackgroundEvent(child_element, event)
            elif tag_name == "BSW-EXTERNAL-TRIGGER-OCCURRED-EVENT":
                event = behavior.createBswExternalTriggerOccurredEvent(self.getShortName(child_element))
                self.readBswExternalTriggerOccurredEvent(child_element, event)
            elif tag_name == "BSW-OPERATION-INVOKED-EVENT":
                event = behavior.createBswOperationInvokedEvent(self.getShortName(child_element))
                self.readBswOperationInvokedEvent(child_element, event)
            elif tag_name == "BSW-ASYNCHRONOUS-SERVER-CALL-RETURNS-EVENT":
                event = behavior.createBswAsynchronousServerCallReturnsEvent(self.getShortName(child_element))
                self.readBswAsynchronousServerCallReturnsEvent(child_element, event)
            else:
                self.notImplemented("Unsupported BswModuleEntity <%s>" % tag_name)

    def readBswApiOptions(self, element: ET.Element, options: BswApiOptions):
        self.readARObjectAttributes(element, options)
        options.setEnableTakeAddress(self.getChildElementOptionalBooleanValue(element, "ENABLE-TAKE-ADDRESS"))

    def readBswDataReceptionPolicy(self, element: ET.Element, policy: BswDataReceptionPolicy):
        self.readBswApiOptions(element, policy)
        policy.setReceivedDataRef(self.getChildElementOptionalRefType(element, "RECEIVED-DATA-REF"))

    def readBswQueuedDataReceptionPolicy(self, element: ET.Element, policy: BswQueuedDataReceptionPolicy):
        self.readBswDataReceptionPolicy(element, policy)
        policy.setQueueLength(self.getChildElementOptionalPositiveInteger(element, "QUEUE-LENGTH"))

    def readBswInternalBehaviorReceptionPolicies(self, element: ET.Element, behavior: BswInternalBehavior):
        for child_element in self.findall(element, "RECEPTION-POLICYS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "BSW-QUEUED-DATA-RECEPTION-POLICY":
                policy = BswQueuedDataReceptionPolicy()
                self.readBswQueuedDataReceptionPolicy(child_element, policy)
                behavior.addReceptionPolicy(policy)
            else:
                self.notImplemented("Unsupported Reception Policies <%s>" % tag_name)

    def readBswInternalTriggeringPoint(self, element: ET.Element, point: BswInternalTriggeringPoint):
        self.readIdentifiable(element, point)

    def readBswInternalBehaviorInternalTriggeringPoints(self, element: ET.Element, behavior: BswInternalBehavior):
        for child_element in self.findall(element, "INTERNAL-TRIGGERING-POINTS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "BSW-INTERNAL-TRIGGERING-POINT":
                point = behavior.createBswInternalTriggeringPoint(self.getShortName(child_element))
                self.readBswInternalTriggeringPoint(child_element, point)
            else:
                self.notImplemented("Unsupported Internal Triggering Points <%s>" % tag_name)

    def readBswInternalBehaviorServiceDependencies(self, element: ET.Element, behavior: BswInternalBehavior):
        for child_element in self.findall(element, "SERVICE-DEPENDENCYS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "BSW-SERVICE-DEPENDENCY":
                dependency = BswServiceDependency()
                self.readBswServiceDependency(child_element, dependency)
                behavior.addServiceDependency(dependency)
            else:
                self.notImplemented("Unsupported Service Dependencies <%s>" % tag_name)

    def readBswInternalBehavior(self, element: ET.Element, behavior: BswInternalBehavior):
        self.logger.debug("Read BswInternalBehavior <%s>" % behavior.full_name)

        # read the internal behavior
        self.readInternalBehavior(element, behavior)
        self.readBswInternalBehaviorInternalTriggeringPoints(element, behavior)
        self.readBswInternalBehaviorEntities(element, behavior)
        self.readBswInternalBehaviorEvents(element, behavior)
        self.readBswInternalBehaviorModeSenderPolicy(element, behavior)
        for group_set in self.getIncludedModeDeclarationGroupSets(element):
            behavior.addIncludedModeDeclarationGroupSet(group_set)
        self.readBswInternalBehaviorReceptionPolicies(element, behavior)
        self.readBswInternalBehaviorServiceDependencies(element, behavior)

    def readBswModuleDescriptionBswInternalBehaviors(self, element: ET.Element, desc: BswModuleDescription):
        for child_element in self.findall(element, "INTERNAL-BEHAVIORS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "BSW-INTERNAL-BEHAVIOR":
                behavior = desc.createBswInternalBehavior(self.getShortName(child_element))
                self.readBswInternalBehavior(child_element, behavior)
            else:
                self.notImplemented("Unsupported Internal Behavior <%s>" % tag_name)

    def readTrigger(self, element: ET.Element, trigger: Trigger):
        self.readIdentifiable(element, trigger)

    def readBswModuleDescriptionReleasedTriggers(self, element: ET.Element, desc: BswModuleDescription):
        for child_element in self.findall(element, "RELEASED-TRIGGERS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "TRIGGER":
                trigger = desc.createReleasedTrigger(self.getShortName(child_element))
                self.readTrigger(child_element, trigger)
            else:
                self.notImplemented("Unsupported Released Trigger <%s>" % tag_name)

    def readBswModuleDescriptionRequiredTriggers(self, element: ET.Element, desc: BswModuleDescription):
        for child_element in self.findall(element, "REQUIRED-TRIGGERS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "TRIGGER":
                trigger = desc.createRequiredTrigger(self.getShortName(child_element))
                self.readTrigger(child_element, trigger)
            else:
                self.notImplemented("Unsupported Required Trigger <%s>" % tag_name)

    def readBswModuleDescriptionProvidedDatas(self, element: ET.Element, desc: BswModuleDescription):
        for child_element in self.findall(element, "PROVIDED-DATAS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "VARIABLE-DATA-PROTOTYPE":
                data = desc.createProvidedData(self.getShortName(child_element))
                self.readVariableDataPrototype(child_element, data)
            else:
                self.notImplemented("Unsupported Provided Data <%s>" % tag_name)

    def readBswModuleDescriptionRequiredDatas(self, element: ET.Element, desc: BswModuleDescription):
        for child_element in self.findall(element, "REQUIRED-DATAS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "VARIABLE-DATA-PROTOTYPE":
                data = desc.createRequiredData(self.getShortName(child_element))
                self.readVariableDataPrototype(child_element, data)
            else:
                self.notImplemented("Unsupported Required Data <%s>" % tag_name)

    def readBswModuleClientServerEntry(self, element: ET.Element, entry: BswModuleClientServerEntry):
        self.readReferrable(element, entry)
        entry.setEncapsulatedEntryRef(self.getChildElementOptionalRefType(element, "ENCAPSULATED-ENTRY-REF"))
        entry.setIsReentrant(self.getChildElementOptionalBooleanValue(element, "IS-REENTRANT"))
        entry.setIsSynchronous(self.getChildElementOptionalBooleanValue(element, "IS-SYNCHRONOUS"))

    def readBswModuleDescriptionProvidedClientServerEntries(self, element: ET.Element, desc: BswModuleDescription):
        for child_element in self.findall(element, "PROVIDED-CLIENT-SERVER-ENTRYS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "BSW-MODULE-CLIENT-SERVER-ENTRY":
                entry = desc.createProvidedClientServerEntry(self.getShortName(child_element))
                self.readBswModuleClientServerEntry(child_element, entry)
            else:
                self.notImplemented("Unsupported Provided Client Server Entry <%s>" % tag_name)

    def readBswModuleDescriptionRequiredClientServerEntries(self, element: ET.Element, desc: BswModuleDescription):
        for child_element in self.findall(element, "REQUIRED-CLIENT-SERVER-ENTRYS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "BSW-MODULE-CLIENT-SERVER-ENTRY":
                entry = desc.createRequiredClientServerEntry(self.getShortName(child_element))
                self.readBswModuleClientServerEntry(child_element, entry)
            else:
                self.notImplemented("Unsupported Required Client Server Entry <%s>" % tag_name)

    def readBswModuleDescription(self, element: ET.Element, desc: BswModuleDescription):
        self.logger.debug("Read BswModuleDescription <%s>" % desc.getShortName())

        self.readIdentifiable(element, desc)
        desc.setModuleId(self.getChildElementOptionalNumericalValue(element, "MODULE-ID"))
        self.readBswModuleDescriptionExpectedEntryRefs(element, desc)
        self.readBswModuleDescriptionImplementedEntryRefs(element, desc)
        self.readBswModuleDescriptionProvidedModeGroups(element, desc)
        self.readBswModuleDescriptionRequiredModeGroups(element, desc)
        self.readBswModuleDescriptionProvidedClientServerEntries(element, desc)
        self.readBswModuleDescriptionRequiredClientServerEntries(element, desc)
        self.readBswModuleDescriptionProvidedDatas(element, desc)
        self.readBswModuleDescriptionRequiredDatas(element, desc)
        self.readBswModuleDescriptionBswInternalBehaviors(element, desc)
        self.readBswModuleDescriptionRequiredTriggers(element, desc)
        self.readBswModuleDescriptionBswModuleDependencies(element, desc)
        self.readBswModuleDescriptionBswModuleDocumentation(element, desc)

    def readBswModuleDescriptionExpectedEntryRefs(self, element: ET.Element, parent: BswModuleDescription):
        for child_element in self.findall(element, "EXPECTED-ENTRYS/BSW-MODULE-ENTRY-REF-CONDITIONAL"):
            ref = self.getChildElementOptionalRefType(child_element, "BSW-MODULE-ENTRY-REF")
            if ref is not None:
                parent.addExpectedEntryRef(ref)

    def readBswModuleDescriptionBswModuleDependencies(self, element: ET.Element, parent: BswModuleDescription):
        for child_element in self.findall(element, "BSW-MODULE-DEPENDENCYS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "BSW-MODULE-DEPENDENCY":
                dependency = parent.createBswModuleDependency(self.getShortName(child_element))
                dependency.setTargetModuleId(self.getChildElementOptionalNumericalValue(child_element, "TARGET-MODULE-ID"))
                dependency.setTargetModuleRef(self.getChildElementOptionalRefType(child_element, "TARGET-MODULE-REF"))
            else:
                self.notImplemented("Unsupported BswModuleDependency <%s>" % tag_name)

    def readBswModuleDescriptionBswModuleDocumentation(self, element: ET.Element, parent: BswModuleDescription):
        container = self.find(element, "BSW-MODULE-DOCUMENTATIONS")
        if container is None:
            return
        child_element = self.find(container, "SW-COMPONENT-DOCUMENTATION")
        if child_element is None:
            return
        parent.setBswModuleDocumentation(self.readSwComponentDocumentationElement(child_element))

    def readSwServiceArg(self, element: ET.Element, arg: SwServiceArg):
        self.readIdentifiable(element, arg)
        arg.setDirection(self.getChildElementOptionalLiteral(element, "DIRECTION"))
        arg.setSwArraysize(self.getValueList(element, "SW-ARRAYSIZE"))
        arg.setSwDataDefProps(self.getSwDataDefProps(element, "SW-DATA-DEF-PROPS"))

    def readBswModuleEntryArguments(self, element: ET.Element, entry: BswModuleEntry):
        for child_element in self.findall(element, "ARGUMENTS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "SW-SERVICE-ARG":
                arg = entry.createArgument(self.getShortName(child_element))
                self.readSwServiceArg(child_element, arg)
            else:
                self.notImplemented("Unsupported Argument <%s>" % tag_name)

    def readBswModuleEntryReturnType(self, element: ET.Element, entry: BswModuleEntry):
        child_element = self.find(element, "RETURN-TYPE")
        if child_element is not None:
            self.logger.debug("Read ReturnType of BswModuleEntry <%s>" % entry.getShortName())
            return_type = entry.createReturnType(self.getShortName(child_element))
            self.readSwServiceArg(child_element, return_type)

    def readBswModuleEntry(self, element: ET.Element, entry: BswModuleEntry):
        self.logger.debug("Read BswModuleEntry <%s>" % entry.getShortName())
        self.readIdentifiable(element, entry)
        self.readBswModuleEntryArguments(element, entry)
        entry.setIsReentrant(self.getChildElementOptionalBooleanValue(element, "IS-REENTRANT"))
        entry.setIsSynchronous(self.getChildElementOptionalBooleanValue(element, "IS-SYNCHRONOUS"))
        entry.setServiceId(self.getChildElementOptionalNumericalValue(element, "SERVICE-ID"))
        entry.setCallType(self.getChildElementOptionalLiteral(element, "CALL-TYPE"))
        entry.setExecutionContext(self.getChildElementOptionalLiteral(element, "EXECUTION-CONTEXT"))
        entry.setSwServiceImplPolicy(self.getChildElementOptionalLiteral(element, "SW-SERVICE-IMPL-POLICY"))
        entry.setBswEntryKind(self.getChildElementOptionalLiteral(element, "BSW-ENTRY-KIND"))
        entry.setRole(self.getChildElementOptionalLiteral(element, "ROLE"))
        entry.setFunctionPrototypeEmitter(self.getChildElementOptionalLiteral(element, "FUNCTION-PROTOTYPE-EMITTER"))
        self.readBswModuleEntryReturnType(element, entry)

    def readEngineeringObject(self, element: ET.Element, engineering_obj: EngineeringObject):
        self.readARObjectAttributes(element, engineering_obj)
        engineering_obj.setShortLabel(self.getChildElementOptionalLiteral(element, "SHORT-LABEL"))
        engineering_obj.setCategory(self.getChildElementOptionalLiteral(element, "CATEGORY"))
        for child_element in self.findall(element, "REVISION-LABELS/REVISION-LABEL"):
            engineering_obj.addRevisionLabel(self.getChildElementOptionalRevisionLabelString(child_element, "."))
        engineering_obj.setDomain(self.getChildElementOptionalLiteral(element, "DOMAIN"))

    def getAutosarEngineeringObject(self, element: ET.Element) -> AutosarEngineeringObject:
        obj = AutosarEngineeringObject()
        self.readEngineeringObject(element, obj)
        # self.logger.debug("Get AutosarEngineeringObject %s", obj.shortLabel)
        return obj

    def readArtifactDescriptor(self, element: ET.Element, code_desc: Code):
        for child_element in self.findall(element, "ARTIFACT-DESCRIPTORS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "AUTOSAR-ENGINEERING-OBJECT":
                code_desc.addArtifactDescriptor(self.getAutosarEngineeringObject(child_element))
            else:
                self.notImplemented("Unsupported Artifact Descriptor <%s>" % tag_name)

    def readCodeDescriptor(self, element: ET.Element, impl: Implementation):
        for child_element in self.findall(element, "CODE-DESCRIPTORS/CODE"):
            short_name = self.getShortName(child_element)
            # self.logger.debug("Read CodeDescriptor %s" % short_name)
            code_desc = impl.createCodeDescriptor(short_name)
            self.readIdentifiable(child_element, code_desc)
            self.readArtifactDescriptor(child_element, code_desc)
            self.readCallbackHeaderRefs(child_element, code_desc)

    def readCallbackHeaderRefs(self, element: ET.Element, code_desc: Code):
        child_element = self.find(element, "CALLBACK-HEADER-REFS")
        if child_element is not None:
            for ref in self.getChildElementRefTypeList(child_element, "CALLBACK-HEADER-REF"):
                code_desc.addCallbackHeaderRef(ref)

    def readCompiler(self, element: ET.Element, impl: Implementation):
        child_element = self.find(element, "COMPILERS")
        if child_element is not None:
            for compiler_element in self.findall(child_element, "COMPILER"):
                compiler = impl.createCompiler(self.getShortName(compiler_element))
                self.readIdentifiable(compiler_element, compiler)
                compiler.setName(self.getChildElementOptionalLiteral(compiler_element, "NAME"))
                compiler.setOptions(self.getChildElementOptionalLiteral(compiler_element, "OPTIONS"))
                compiler.setVendor(self.getChildElementOptionalLiteral(compiler_element, "VENDOR"))
                compiler.setVersion(self.getChildElementOptionalLiteral(compiler_element, "VERSION"))

    def readLinker(self, element: ET.Element, impl: Implementation):
        child_element = self.find(element, "LINKERS")
        if child_element is not None:
            for linker in self.findall(child_element, "LINKER"):
                linker_obj = impl.createLinker(self.getShortName(linker))
                self.readIdentifiable(linker, linker_obj)
                linker_obj.setName(self.getChildElementOptionalLiteral(linker, "NAME"))
                linker_obj.setOptions(self.getChildElementOptionalLiteral(linker, "OPTIONS"))
                linker_obj.setVendor(self.getChildElementOptionalLiteral(linker, "VENDOR"))
                linker_obj.setVersion(self.getChildElementOptionalLiteral(linker, "VERSION"))

    def readDependencyOnArtifact(self, element: ET.Element, impl: Implementation, key: str, create):
        child_element = self.find(element, key)
        if child_element is not None:
            for dependency_element in self.findall(child_element, "DEPENDENCY-ON-ARTIFACT"):
                dependency = create(self.getShortName(dependency_element))
                self.readIdentifiable(dependency_element, dependency)
                descriptor_element = self.find(dependency_element, "ARTIFACT-DESCRIPTOR")
                if descriptor_element is not None:
                    dependency.setArtifactDescriptor(self.getAutosarEngineeringObject(descriptor_element))
                usages_element = self.find(dependency_element, "USAGES")
                if usages_element is not None:
                    for usage_element in self.findall(usages_element, "USAGE"):
                        usage = DependencyUsageEnum()
                        usage.setValue(usage_element.text)
                        dependency.addUsage(usage)

    def readMemorySectionOptions(self, element: ET.Element, section: MemorySection):
        child_element = self.find(element, "OPTIONS")
        if child_element is not None:
            for value in self.getChildElementLiteralValueList(child_element, "OPTION"):
                section.addOption(value)

    def readMemorySections(self, element: ET.Element, consumption: ResourceConsumption):
        for child_element in self.findall(element, "MEMORY-SECTIONS/MEMORY-SECTION"):
            memory_section = consumption.createMemorySection(self.getShortName(child_element))
            self.readIdentifiable(child_element, memory_section)
            memory_section.setAlignment(self.getChildElementOptionalLiteral(child_element, "ALIGNMENT"))
            memory_section.setMemClassSymbol(self.getChildElementOptionalLiteral(child_element, "MEM-CLASS-SYMBOL"))
            self.readMemorySectionOptions(child_element, memory_section)
            memory_section.setSize(self.getChildElementOptionalPositiveInteger(child_element, "SIZE"))
            memory_section.setSwAddrMethodRef(self.getChildElementOptionalRefType(child_element, "SW-ADDRMETHOD-REF"))
            memory_section.setSymbol(self.getChildElementOptionalLiteral(child_element, "SYMBOL"))
            memory_section.setPrefixRef(self.getChildElementOptionalRefType(child_element, "PREFIX-REF"))
            for ref in self.getChildElementRefTypeList(child_element, "EXECUTABLE-ENTITY-REFS/EXECUTABLE-ENTITY-REF"):
                memory_section.addExecutableEntityRef(ref)
            # self.logger.debug("read MemorySections %s" % memory_section.getShortName())

    def readMultidimensionalTime(self, element: ET.Element, time: MultidimensionalTime):
        time.setCseCode(self.getChildElementOptionalLiteral(element, "CSE-CODE"))
        time.setCseCodeFactor(self.getChildElementOptionalIntegerValue(element, "CSE-CODE-FACTOR"))

    def readHardwareConfiguration(self, element: ET.Element, config: HardwareConfiguration):
        config.setAdditionalInformation(self.getChildElementOptionalLiteral(element, "ADDITIONAL-INFORMATION"))
        config.setProcessorMode(self.getChildElementOptionalLiteral(element, "PROCESSOR-MODE"))
        config.setProcessorSpeed(self.getChildElementOptionalLiteral(element, "PROCESSOR-SPEED"))

    def readSoftwareContext(self, element: ET.Element, context: SoftwareContext):
        context.setInput(self.getChildElementOptionalLiteral(element, "INPUT"))
        context.setState(self.getChildElementOptionalLiteral(element, "STATE"))

    def readMemorySectionLocation(self, element: ET.Element, location):
        location.setProvidedMemoryRef(self.getChildElementOptionalRefType(element, "PROVIDED-MEMORY-REF"))
        location.setSoftwareMemorySectionRef(self.getChildElementOptionalRefType(element, "SOFTWARE-MEMORY-SECTION-REF"))

    def readExecutionTime(self, element: ET.Element, execution_time):
        self.readIdentifiable(element, execution_time)
        execution_time.setExclusiveAreaRef(self.getChildElementOptionalRefType(element, "EXCLUSIVE-AREA-REF"))
        execution_time.setExecutableEntityRef(self.getChildElementOptionalRefType(element, "EXECUTABLE-ENTITY-REF"))
        execution_time.setHwElementRef(self.getChildElementOptionalRefType(element, "HW-ELEMENT-REF"))
        hardware_configuration_element = self.find(element, "HARDWARE-CONFIGURATION")
        if hardware_configuration_element is not None:
            config = HardwareConfiguration()
            self.readHardwareConfiguration(hardware_configuration_element, config)
            execution_time.setHardwareConfiguration(config)
        for ref in self.getChildElementRefTypeList(element, "INCLUDED-LIBRARY-REFS/INCLUDED-LIBRARY-REF"):
            execution_time.addIncludedLibraryRef(ref)
        for location_element in self.findall(element, "MEMORY-SECTION-LOCATIONS/MEMORY-SECTION-LOCATION"):
            location = MemorySectionLocation()
            execution_time.addMemorySectionLocation(location)
            self.readMemorySectionLocation(location_element, location)
        software_context_element = self.find(element, "SOFTWARE-CONTEXT")
        if software_context_element is not None:
            context = SoftwareContext()
            self.readSoftwareContext(software_context_element, context)
            execution_time.setSoftwareContext(context)

    def readAnalyzedExecutionTime(self, element: ET.Element, execution_time: AnalyzedExecutionTime):
        self.readExecutionTime(element, execution_time)
        best_element = self.find(element, "BEST-CASE-EXECUTION-TIME")
        if best_element is not None:
            best = MultidimensionalTime()
            self.readMultidimensionalTime(best_element, best)
            execution_time.setBestCaseExecutionTime(best)
        worst_element = self.find(element, "WORST-CASE-EXECUTION-TIME")
        if worst_element is not None:
            worst = MultidimensionalTime()
            self.readMultidimensionalTime(worst_element, worst)
            execution_time.setWorstCaseExecutionTime(worst)

    def readMeasuredExecutionTime(self, element: ET.Element, execution_time: MeasuredExecutionTime):
        self.readExecutionTime(element, execution_time)
        for key, setter in (
            ("MAXIMUM-EXECUTION-TIME", execution_time.setMaximumExecutionTime),
            ("MINIMUM-EXECUTION-TIME", execution_time.setMinimumExecutionTime),
            ("NOMINAL-EXECUTION-TIME", execution_time.setNominalExecutionTime),
        ):
            child_element = self.find(element, key)
            if child_element is not None:
                value = MultidimensionalTime()
                self.readMultidimensionalTime(child_element, value)
                setter(value)

    def readSimulatedExecutionTime(self, element: ET.Element, execution_time: SimulatedExecutionTime):
        self.readExecutionTime(element, execution_time)
        for key, setter in (
            ("MAXIMUM-EXECUTION-TIME", execution_time.setMaximumExecutionTime),
            ("MINIMUM-EXECUTION-TIME", execution_time.setMinimumExecutionTime),
            ("NOMINAL-EXECUTION-TIME", execution_time.setNominalExecutionTime),
        ):
            child_element = self.find(element, key)
            if child_element is not None:
                value = MultidimensionalTime()
                self.readMultidimensionalTime(child_element, value)
                setter(value)

    def readRoughEstimateOfExecutionTime(self, element: ET.Element, execution_time: RoughEstimateOfExecutionTime):
        self.readExecutionTime(element, execution_time)
        execution_time.setAdditionalInformation(self.getChildElementOptionalLiteral(element, "ADDITIONAL-INFORMATION"))
        estimated_element = self.find(element, "ESTIMATED-EXECUTION-TIME")
        if estimated_element is not None:
            estimated = MultidimensionalTime()
            self.readMultidimensionalTime(estimated_element, estimated)
            execution_time.setEstimatedExecutionTime(estimated)

    def readExecutionTimes(self, element: ET.Element, consumption: ResourceConsumption):
        for child_element in self.findall(element, "EXECUTION-TIMES/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "ANALYZED-EXECUTION-TIME":
                execution_time = consumption.createAnalyzedExecutionTime(self.getShortName(child_element))
                self.readAnalyzedExecutionTime(child_element, execution_time)
            elif tag_name == "MEASURED-EXECUTION-TIME":
                execution_time = consumption.createMeasuredExecutionTime(self.getShortName(child_element))
                self.readMeasuredExecutionTime(child_element, execution_time)
            elif tag_name == "ROUGH-ESTIMATE-OF-EXECUTION-TIME":
                execution_time = consumption.createRoughEstimateOfExecutionTime(self.getShortName(child_element))
                self.readRoughEstimateOfExecutionTime(child_element, execution_time)
            elif tag_name == "SIMULATED-EXECUTION-TIME":
                execution_time = consumption.createSimulatedExecutionTime(self.getShortName(child_element))
                self.readSimulatedExecutionTime(child_element, execution_time)
            else:
                self.notImplemented("Unsupported Execution Time: <%s>" % tag_name)

    def readHeapUsage(self, element: ET.Element, usage):
        self.readIdentifiable(element, usage)
        usage.setHwElementRef(self.getChildElementOptionalRefType(element, "HW-ELEMENT-REF"))
        hardware_configuration_element = self.find(element, "HARDWARE-CONFIGURATION")
        if hardware_configuration_element is not None:
            config = HardwareConfiguration()
            self.readHardwareConfiguration(hardware_configuration_element, config)
            usage.setHardwareConfiguration(config)
        software_context_element = self.find(element, "SOFTWARE-CONTEXT")
        if software_context_element is not None:
            context = SoftwareContext()
            self.readSoftwareContext(software_context_element, context)
            usage.setSoftwareContext(context)

    def readMeasuredHeapUsage(self, element: ET.Element, usage: MeasuredHeapUsage):
        self.readHeapUsage(element, usage)
        usage.setAverageMemoryConsumption(self.getChildElementOptionalPositiveInteger(element, "AVERAGE-MEMORY-CONSUMPTION"))
        usage.setMaximumMemoryConsumption(self.getChildElementOptionalPositiveInteger(element, "MAXIMUM-MEMORY-CONSUMPTION"))
        usage.setMinimumMemoryConsumption(self.getChildElementOptionalPositiveInteger(element, "MINIMUM-MEMORY-CONSUMPTION"))
        usage.setTestPattern(self.getChildElementOptionalLiteral(element, "TEST-PATTERN"))

    def readRoughEstimateHeapUsage(self, element: ET.Element, usage: RoughEstimateHeapUsage):
        self.readHeapUsage(element, usage)
        usage.setMemoryConsumption(self.getChildElementOptionalPositiveInteger(element, "MEMORY-CONSUMPTION"))

    def readWorstCaseHeapUsage(self, element: ET.Element, usage: WorstCaseHeapUsage):
        self.readHeapUsage(element, usage)
        usage.setMemoryConsumption(self.getChildElementOptionalPositiveInteger(element, "MEMORY-CONSUMPTION"))

    def readHeapUsages(self, element: ET.Element, consumption: ResourceConsumption):
        for child_element in self.findall(element, "HEAP-USAGES/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "MEASURED-HEAP-USAGE":
                usage = consumption.createMeasuredHeapUsage(self.getShortName(child_element))
                self.readMeasuredHeapUsage(child_element, usage)
            elif tag_name == "ROUGH-ESTIMATE-HEAP-USAGE":
                usage = consumption.createRoughEstimateHeapUsage(self.getShortName(child_element))
                self.readRoughEstimateHeapUsage(child_element, usage)
            elif tag_name == "WORST-CASE-HEAP-USAGE":
                usage = consumption.createWorstCaseHeapUsage(self.getShortName(child_element))
                self.readWorstCaseHeapUsage(child_element, usage)
            else:
                self.notImplemented("Unsupported Heap Usage: <%s>" % tag_name)

    def readSectionNamePrefixes(self, element: ET.Element, consumption: ResourceConsumption):
        for child_element in self.findall(element, "SECTION-NAME-PREFIXS/SECTION-NAME-PREFIX"):
            prefix = consumption.createSectionNamePrefix(self.getShortName(child_element))
            self.readReferrable(child_element, prefix)
            prefix.setImplementedInRef(self.getChildElementOptionalRefType(child_element, "IMPLEMENTED-IN-REF"))

    def readAccessCountSets(self, element: ET.Element, consumption: ResourceConsumption):
        for child_element in self.findall(element, "ACCESS-COUNT-SETS/ACCESS-COUNT-SET"):
            access_count_set = AccessCountSet()
            consumption.addAccessCountSet(access_count_set)
            access_count_set.setCountProfile(self.getChildElementOptionalLiteral(child_element, "COUNT-PROFILE"))
            for count_element in self.findall(child_element, "ACCESS-COUNTS/ACCESS-COUNT"):
                count = AccessCount()
                count.setAccessPointRef(self.getChildElementOptionalRefType(count_element, "ACCESS-POINT-REF"))
                count.setValue(self.getChildElementOptionalPositiveInteger(count_element, "VALUE"))
                access_count_set.addAccessCount(count)

    def readStackUsage(self, element: ET.Element, usage: StackUsage):
        self.logger.debug("read StackUsage %s" % usage.getShortName())
        self.readIdentifiable(element, usage)
        usage.setExecutableEntityRef(self.getChildElementOptionalRefType(element, "EXECUTABLE-ENTITY-REF"))
        usage.setHwElementRef(self.getChildElementOptionalRefType(element, "HW-ELEMENT-REF"))
        hardware_configuration_element = self.find(element, "HARDWARE-CONFIGURATION")
        if hardware_configuration_element is not None:
            config = HardwareConfiguration()
            self.readHardwareConfiguration(hardware_configuration_element, config)
            usage.setHardwareConfiguration(config)
        software_context_element = self.find(element, "SOFTWARE-CONTEXT")
        if software_context_element is not None:
            context = SoftwareContext()
            self.readSoftwareContext(software_context_element, context)
            usage.setSoftwareContext(context)

    def readRoughEstimateStackUsage(self, element: ET.Element, usage: RoughEstimateStackUsage):
        self.readStackUsage(element, usage)
        usage.setMemoryConsumption(self.getChildElementOptionalPositiveInteger(element, "MEMORY-CONSUMPTION"))

    def readMeasuredStackUsage(self, element: ET.Element, usage: MeasuredStackUsage):
        self.readStackUsage(element, usage)
        usage.setAverageMemoryConsumption(self.getChildElementOptionalPositiveInteger(element, "AVERAGE-MEMORY-CONSUMPTION"))
        usage.setMaximumMemoryConsumption(self.getChildElementOptionalPositiveInteger(element, "MAXIMUM-MEMORY-CONSUMPTION"))
        usage.setMinimumMemoryConsumption(self.getChildElementOptionalPositiveInteger(element, "MINIMUM-MEMORY-CONSUMPTION"))
        usage.setTestPattern(self.getChildElementOptionalLiteral(element, "TEST-PATTERN"))

    def readWorstCaseStackUsage(self, element: ET.Element, usage: WorstCaseStackUsage):
        self.readStackUsage(element, usage)
        usage.setMemoryConsumption(self.getChildElementOptionalPositiveInteger(element, "MEMORY-CONSUMPTION"))

    def readStackUsages(self, element: ET.Element, consumption: ResourceConsumption):
        for child_element in self.findall(element, "STACK-USAGES/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "ROUGH-ESTIMATE-STACK-USAGE":
                usage = consumption.createRoughEstimateStackUsage(self.getShortName(child_element))
                self.readRoughEstimateStackUsage(child_element, usage)
            elif tag_name == "MEASURED-STACK-USAGE":
                usage = consumption.createMeasuredStackUsage(self.getShortName(child_element))
                self.readMeasuredStackUsage(child_element, usage)
            elif tag_name == "WORST-CASE-STACK-USAGE":
                usage = consumption.createWorstCaseStackUsage(self.getShortName(child_element))
                self.readWorstCaseStackUsage(child_element, usage)
            else:
                self.notImplemented("Unsupported Stack Usages: <%s>" % tag_name)

    def readResourceConsumption(self, element: ET.Element, impl: Implementation):
        child_element = self.find(element, "RESOURCE-CONSUMPTION")
        if child_element is not None:
            consumption = impl.createResourceConsumption(self.getShortName(child_element))
            self.readIdentifiable(child_element, consumption)
            self.readAccessCountSets(child_element, consumption)
            self.readExecutionTimes(child_element, consumption)
            self.readHeapUsages(child_element, consumption)
            self.readMemorySections(child_element, consumption)
            self.readSectionNamePrefixes(child_element, consumption)
            self.readStackUsages(child_element, consumption)

    def readImplementation(self, element: ET.Element, impl: Implementation):
        self.readIdentifiable(element, impl)
        self.readCodeDescriptor(element, impl)
        impl.setProgrammingLanguage(self.getChildElementOptionalLiteral(element, "PROGRAMMING-LANGUAGE"))
        self.readResourceConsumption(element, impl)
        self.readBuildActionManifests(element, impl)
        self.readCompiler(element, impl)
        self.readLinker(element, impl)
        self.readDependencyOnArtifact(element, impl, "GENERATED-ARTIFACTS", impl.createGeneratedArtifact)
        self.readDependencyOnArtifact(element, impl, "REQUIRED-ARTIFACTS", impl.createRequiredArtifact)
        self.readDependencyOnArtifact(element, impl, "REQUIRED-GENERATOR-TOOLS", impl.createRequiredGeneratorTool)
        for ref in self.getChildElementRefTypeList(element, "HW-ELEMENT-REFS/HW-ELEMENT-REF"):
            impl.addHwElementRef(ref)
        impl.setBuildActionManifestRef(self.getChildElementOptionalRefType(element, "BUILD-ACTION-MANIFESTS/BUILD-ACTION-MANIFEST-REF-CONDITIONAL/BUILD-ACTION-MANIFEST-REF"))
        impl.setSwVersion(self.getChildElementOptionalLiteral(element, "SW-VERSION"))
        impl.setSwcBswMappingRef(self.getChildElementOptionalRefType(element, "SWC-BSW-MAPPING-REF"))
        impl.setUsedCodeGenerator(self.getChildElementOptionalLiteral(element, "USED-CODE-GENERATOR"))
        impl.setVendorId(self.getChildElementOptionalPositiveInteger(element, "VENDOR-ID"))
        mc_support_element = self.find(element, "MC-SUPPORT")
        if mc_support_element is not None:
            support = McSupportData()
            self.readMcSupportData(mc_support_element, support)
            impl.setMcSupport(support)

    def readMcSupportData(self, element: ET.Element, support: McSupportData):
        for child_element in self.findall(element, "EMULATION-SUPPORTS/MC-SW-EMULATION-METHOD-SUPPORT"):
            emulation_support = McSwEmulationMethodSupport()
            self.readMcSwEmulationMethodSupport(child_element, emulation_support)
            support.addEmulationSupport(emulation_support)
        for child_element in self.findall(element, "MC-PARAMETER-INSTANCES/MC-DATA-INSTANCE"):
            instance = support.createMcParameterInstance(self.getShortName(child_element))
            self.readMcDataInstance(child_element, instance)
        for child_element in self.findall(element, "MC-VARIABLE-INSTANCES/MC-DATA-INSTANCE"):
            instance = support.createMcVariableInstance(self.getShortName(child_element))
            self.readMcDataInstance(child_element, instance)
        for ref in self.getChildElementRefTypeList(element, "MEASURABLE-SYSTEM-CONSTANT-VALUES-REFS/MEASURABLE-SYSTEM-CONSTANT-VALUES-REF"):
            support.addMeasurableSystemConstantValuesRef(ref)
        rpt_support_data_element = self.find(element, "RPT-SUPPORT-DATA")
        if rpt_support_data_element is not None:
            rpt_support_data = RptSupportData()
            self.readRptSupportData(rpt_support_data_element, rpt_support_data)
            support.setRptSupportData(rpt_support_data)

    def readMcSwEmulationMethodSupport(self, element: ET.Element, support: McSwEmulationMethodSupport):
        support.setShortLabel(self.getChildElementOptionalLiteral(element, "SHORT-LABEL"))
        support.setCategory(self.getChildElementOptionalLiteral(element, "CATEGORY"))
        support.setBaseReferenceRef(self.getChildElementOptionalRefType(element, "BASE-REFERENCE-REF"))
        for child_element in self.findall(element, "ELEMENT-GROUPS/MC-PARAMETER-ELEMENT-GROUP"):
            group = McParameterElementGroup()
            self.readMcParameterElementGroup(child_element, group)
            support.addElementGroup(group)
        support.setReferenceTableRef(self.getChildElementOptionalRefType(element, "REFERENCE-TABLE-REF"))

    def readMcParameterElementGroup(self, element: ET.Element, group: McParameterElementGroup):
        group.setShortLabel(self.getChildElementOptionalLiteral(element, "SHORT-LABEL"))
        group.setRamLocationRef(self.getChildElementOptionalRefType(element, "RAM-LOCATION-REF"))
        group.setRomLocationRef(self.getChildElementOptionalRefType(element, "ROM-LOCATION-REF"))

    def readImplementationElementInParameterInstanceRef(self, element: ET.Element, instance_in_memory: ImplementationElementInParameterInstanceRef):
        instance_in_memory.setContextRef(self.getChildElementOptionalRefType(element, "CONTEXT-REF"))
        instance_in_memory.setTargetRef(self.getChildElementOptionalRefType(element, "TARGET-REF"))

    def readRteEventInEcuInstanceRef(self, element: ET.Element, iref: RteEventInEcuInstanceRef):
        iref.setContextRootCompositionRef(self.getChildElementOptionalRefType(element, "CONTEXT-ROOT-COMPOSITION-REF"))
        iref.setContextAtomicComponentRef(self.getChildElementOptionalRefType(element, "CONTEXT-ATOMIC-COMPONENT-REF"))
        iref.setTargetRteEventRef(self.getChildElementOptionalRefType(element, "TARGET-RTE-EVENT-REF"))

    def readVariableAccessInEcuInstanceRef(self, element: ET.Element, iref: VariableAccessInEcuInstanceRef):
        iref.setContextRootCompositionRef(self.getChildElementOptionalRefType(element, "CONTEXT-ROOT-COMPOSITION-REF"))
        iref.setContextAtomicComponentRef(self.getChildElementOptionalRefType(element, "CONTEXT-ATOMIC-COMPONENT-REF"))
        iref.setTargetVariableAccessRef(self.getChildElementOptionalRefType(element, "TARGET-VARIABLE-ACCESS-REF"))

    def readMcDataAccessDetails(self, element: ET.Element, details: McDataAccessDetails):
        for child_element in self.findall(element, "RTE-EVENT-IREFS/RTE-EVENT-IREF"):
            iref = RteEventInEcuInstanceRef()
            self.readRteEventInEcuInstanceRef(child_element, iref)
            details.addRteEventIRef(iref)
        for child_element in self.findall(element, "VARIABLE-ACCESS-IREFS/VARIABLE-ACCESS-IREF"):
            iref = VariableAccessInEcuInstanceRef()
            self.readVariableAccessInEcuInstanceRef(child_element, iref)
            details.addVariableAccessIRef(iref)

    def readMcDataInstance(self, element: ET.Element, instance: McDataInstance):
        instance.setArraySize(self.getChildElementOptionalPositiveInteger(element, "ARRAY-SIZE"))
        instance.setDisplayIdentifier(self.getChildElementOptionalLiteral(element, "DISPLAY-IDENTIFIER"))
        instance.setFlatMapEntryRef(self.getChildElementOptionalRefType(element, "FLAT-MAP-ENTRY-REF"))
        instance_in_memory_element = self.find(element, "INSTANCE-IN-MEMORY")
        if instance_in_memory_element is not None:
            instance_in_memory = ImplementationElementInParameterInstanceRef()
            self.readImplementationElementInParameterInstanceRef(instance_in_memory_element, instance_in_memory)
            instance.setInstanceInMemory(instance_in_memory)
        instance.setRole(self.getChildElementOptionalLiteral(element, "ROLE"))
        instance.setSymbol(self.getChildElementOptionalLiteral(element, "SYMBOL"))
        mc_data_access_details_element = self.find(element, "MC-DATA-ACCESS-DETAILS")
        if mc_data_access_details_element is not None:
            details = McDataAccessDetails()
            self.readMcDataAccessDetails(mc_data_access_details_element, details)
            instance.setMcDataAccessDetails(details)
        if self.find(element, "RESULTING-PROPERTIES") is not None:
            instance.setResultingProperties(SwDataDefProps())
        rpt_sw_prototyping_access_element = self.find(element, "RESULTING-RPT-SW-PROTOTYPING-ACCESS")
        if rpt_sw_prototyping_access_element is not None:
            access = RptSwPrototypingAccess()
            self.readRptSwPrototypingAccess(rpt_sw_prototyping_access_element, access)
            instance.setResultingRptSwPrototypingAccess(access)
        rpt_impl_policy_element = self.find(element, "RPT-IMPL-POLICY")
        if rpt_impl_policy_element is not None:
            policy = RptImplPolicy()
            self.readRptImplPolicy(rpt_impl_policy_element, policy)
            instance.setRptImplPolicy(policy)
        for assignment_element in self.findall(element, "MC-DATA-ASSIGNMENTS/ROLE-BASED-MC-DATA-ASSIGNMENT"):
            assignment = RoleBasedMcDataAssignment()
            self.readRoleBasedMcDataAssignment(assignment_element, assignment)
            instance.addMcDataAssignment(assignment)
        for sub_element in self.findall(element, "SUB-ELEMENTS/MC-DATA-INSTANCE"):
            self.readMcDataInstance(sub_element, instance.createSubElement(self.getShortName(sub_element)))

    def readRoleBasedMcDataAssignment(self, element: ET.Element, assignment: RoleBasedMcDataAssignment):
        for ref in self.getChildElementRefTypeList(element, "EXECUTION-CONTEXT-REFS/EXECUTION-CONTEXT-REF"):
            assignment.addExecutionContextRef(ref)
        for ref in self.getChildElementRefTypeList(element, "MC-DATA-INSTANCE-REFS/MC-DATA-INSTANCE-REF"):
            assignment.addMcDataInstanceRef(ref)
        assignment.setRole(self.getChildElementOptionalIdentifier(element, "ROLE"))

    def readRptSwPrototypingAccess(self, element: ET.Element, access: RptSwPrototypingAccess):
        access.setRptHookAccess(self.getChildElementOptionalLiteral(element, "RPT-HOOK-ACCESS"))
        access.setRptReadAccess(self.getChildElementOptionalLiteral(element, "RPT-READ-ACCESS"))
        access.setRptWriteAccess(self.getChildElementOptionalLiteral(element, "RPT-WRITE-ACCESS"))

    def readRptImplPolicy(self, element: ET.Element, policy: RptImplPolicy):
        policy.setRptEnablerImplType(self.getChildElementOptionalLiteral(element, "RPT-ENABLER-IMPL-TYPE"))
        policy.setRptPreparationLevel(self.getChildElementOptionalLiteral(element, "RPT-PREPARATION-LEVEL"))

    def readRptExecutableEntityProperties(self, element: ET.Element, properties: RptExecutableEntityProperties):
        properties.setMaxRptEventId(self.getChildElementOptionalPositiveInteger(element, "MAX-RPT-EVENT-ID"))
        properties.setMinRptEventId(self.getChildElementOptionalPositiveInteger(element, "MIN-RPT-EVENT-ID"))
        properties.setRptExecutionControl(self.getChildElementOptionalLiteral(element, "RPT-EXECUTION-CONTROL"))
        properties.setRptServicePoint(self.getChildElementOptionalLiteral(element, "RPT-SERVICE-POINT"))

    def readRptServicePoint(self, element: ET.Element, service_point: RptServicePoint):
        service_point.setServiceId(self.getChildElementOptionalPositiveInteger(element, "SERVICE-ID"))
        service_point.setSymbol(self.getChildElementOptionalLiteral(element, "SYMBOL"))

    def readRptExecutableEntityEvent(self, element: ET.Element, event: RptExecutableEntityEvent):
        for ref in self.getChildElementRefTypeList(element, "EXECUTION-CONTEXT-REFS/EXECUTION-CONTEXT-REF"):
            event.addExecutionContextRef(ref)
        for assignment_element in self.findall(element, "MC-DATA-ASSIGNMENTS/ROLE-BASED-MC-DATA-ASSIGNMENT"):
            assignment = RoleBasedMcDataAssignment()
            self.readRoleBasedMcDataAssignment(assignment_element, assignment)
            event.addMcDataAssignment(assignment)
        event.setRptEventId(self.getChildElementOptionalPositiveInteger(element, "RPT-EVENT-ID"))
        rpt_executable_entity_properties_element = self.find(element, "RPT-EXECUTABLE-ENTITY-PROPERTIES")
        if rpt_executable_entity_properties_element is not None:
            properties = RptExecutableEntityProperties()
            self.readRptExecutableEntityProperties(rpt_executable_entity_properties_element, properties)
            event.setRptExecutableEntityProperties(properties)
        rpt_impl_policy_element = self.find(element, "RPT-IMPL-POLICY")
        if rpt_impl_policy_element is not None:
            policy = RptImplPolicy()
            self.readRptImplPolicy(rpt_impl_policy_element, policy)
            event.setRptImplPolicy(policy)
        for ref in self.getChildElementRefTypeList(element, "RPT-SERVICE-POINT-POST-REFS/RPT-SERVICE-POINT-POST-REF"):
            event.addRptServicePointPostRef(ref)
        for ref in self.getChildElementRefTypeList(element, "RPT-SERVICE-POINT-PRE-REFS/RPT-SERVICE-POINT-PRE-REF"):
            event.addRptServicePointPreRef(ref)

    def readRptExecutableEntity(self, element: ET.Element, entity: RptExecutableEntity):
        for event_element in self.findall(element, "RPT-EXECUTABLE-ENTITY-EVENTS/RPT-EXECUTABLE-ENTITY-EVENT"):
            event = entity.createRptExecutableEntityEvent(self.getShortName(event_element))
            self.readRptExecutableEntityEvent(event_element, event)
        for assignment_element in self.findall(element, "RPT-READS/ROLE-BASED-MC-DATA-ASSIGNMENT"):
            assignment = RoleBasedMcDataAssignment()
            self.readRoleBasedMcDataAssignment(assignment_element, assignment)
            entity.addRptRead(assignment)
        for assignment_element in self.findall(element, "RPT-WRITES/ROLE-BASED-MC-DATA-ASSIGNMENT"):
            assignment = RoleBasedMcDataAssignment()
            self.readRoleBasedMcDataAssignment(assignment_element, assignment)
            entity.addRptWrite(assignment)
        entity.setSymbol(self.getChildElementOptionalLiteral(element, "SYMBOL"))

    def readRptComponent(self, element: ET.Element, component: RptComponent):
        for assignment_element in self.findall(element, "MC-DATA-ASSIGNMENTS/ROLE-BASED-MC-DATA-ASSIGNMENT"):
            assignment = RoleBasedMcDataAssignment()
            self.readRoleBasedMcDataAssignment(assignment_element, assignment)
            component.addMcDataAssignment(assignment)
        rp_impl_policy_element = self.find(element, "RP-IMPL-POLICY")
        if rp_impl_policy_element is not None:
            policy = RptImplPolicy()
            self.readRptImplPolicy(rp_impl_policy_element, policy)
            component.setRpImplPolicy(policy)
        for entity_element in self.findall(element, "RPT-EXECUTABLE-ENTITYS/RPT-EXECUTABLE-ENTITY"):
            entity = component.createRptExecutableEntity(self.getShortName(entity_element))
            self.readRptExecutableEntity(entity_element, entity)

    def readRptSupportData(self, element: ET.Element, rpt_support_data: RptSupportData):
        for context_element in self.findall(element, "EXECUTION-CONTEXTS/RPT-EXECUTION-CONTEXT"):
            rpt_support_data.createExecutionContext(self.getShortName(context_element))
        for component_element in self.findall(element, "RPT-COMPONENTS/RPT-COMPONENT"):
            component = rpt_support_data.createRptComponent(self.getShortName(component_element))
            self.readRptComponent(component_element, component)
        for service_point_element in self.findall(element, "RPT-SERVICE-POINTS/RPT-SERVICE-POINT"):
            service_point = rpt_support_data.createRptServicePoint(self.getShortName(service_point_element))
            self.readRptServicePoint(service_point_element, service_point)

    def readBuildActionManifests(self, element: ET.Element, impl: Implementation):
        child_element = self.find(element, "BUILD-ACTION-MANIFESTS")
        if child_element is not None:
            ref = self.getChildElementOptionalRefType(child_element, "BUILD-ACTION-MANIFEST-REF-CONDITIONAL/BUILD-ACTION-MANIFEST-REF")
            if ref is not None:
                impl.setBuildActionManifestRef(ref)

    def readBswImplementationVendorSpecificModuleDefRefs(self, element: ET.Element, impl: BswImplementation):
        child_element = self.find(element, "VENDOR-SPECIFIC-MODULE-DEF-REFS")
        if child_element is not None:
            for ref in self.getChildElementRefTypeList(child_element, "VENDOR-SPECIFIC-MODULE-DEF-REF"):
                impl.addVendorSpecificModuleDefRef(ref)

    def readBswImplementationPreconfiguredConfigurationRefs(self, element: ET.Element, impl: BswImplementation):
        child_element = self.find(element, "PRECONFIGURED-CONFIGURATION-REFS")
        if child_element is not None:
            for ref in self.getChildElementRefTypeList(child_element, "PRECONFIGURED-CONFIGURATION-REF"):
                impl.addPreconfiguredConfigurationRef(ref)

    def readBswImplementationRecommendedConfigurationRefs(self, element: ET.Element, impl: BswImplementation):
        child_element = self.find(element, "RECOMMENDED-CONFIGURATION-REFS")
        if child_element is not None:
            for ref in self.getChildElementRefTypeList(child_element, "RECOMMENDED-CONFIGURATION-REF"):
                impl.addRecommendedConfigurationRef(ref)

    def readBswImplementation(self, element: ET.Element, impl: BswImplementation):
        self.logger.debug("Read BswImplementation <%s>" % impl.getShortName())
        self.readImplementation(element, impl)
        impl.setArReleaseVersion(self.getChildElementOptionalLiteral(element, "AR-RELEASE-VERSION"))
        impl.setBehaviorRef(self.getChildElementOptionalRefType(element, "BEHAVIOR-REF"))
        impl.setVendorApiInfix(self.getChildElementOptionalLiteral(element, "VENDOR-API-INFIX"))
        self.readBswImplementationPreconfiguredConfigurationRefs(element, impl)
        self.readBswImplementationRecommendedConfigurationRefs(element, impl)
        self.readBswImplementationVendorSpecificModuleDefRefs(element, impl)
        behavior_ref = impl.getBehaviorRef()
        if behavior_ref is not None:
            document = AUTOSAR.getInstance()
            document.addImplementationBehaviorMap(impl.getFullName(), behavior_ref.getValue())

    def readSwcImplementation(self, element: ET.Element, impl: SwcImplementation):
        self.logger.debug("Read SwcImplementation <%s>" % impl.getShortName())
        self.readImplementation(element, impl)
        impl.setBehaviorRef(self.getChildElementOptionalRefType(element, "BEHAVIOR-REF"))
        behavior_ref = impl.getBehaviorRef()
        if behavior_ref is not None:
            document = AUTOSAR.getInstance()
            document.addImplementationBehaviorMap(impl.getFullName(), behavior_ref.getValue())

    def readRunnableEntityDataReceivePointByArguments(self, element, parent: RunnableEntity):
        self._readVariableAccesses(element, parent, "DATA-RECEIVE-POINT-BY-ARGUMENTS")

    def readRunnableEntityDataReceivePointByValues(self, element: ET.Element, parent: RunnableEntity):
        self._readVariableAccesses(element, parent, "DATA-RECEIVE-POINT-BY-VALUES")

    def readRunnableEntityDataReadAccesses(self, element: ET.Element, parent: RunnableEntity):
        self._readVariableAccesses(element, parent, "DATA-READ-ACCESSS")

    def readRunnableEntityDataWriteAccesses(self, element: ET.Element, parent: RunnableEntity):
        self._readVariableAccesses(element, parent, "DATA-WRITE-ACCESSS")

    def readRunnableEntityDataSendPoints(self, element: ET.Element, parent: RunnableEntity):
        self._readVariableAccesses(element, parent, "DATA-SEND-POINTS")

    def getRunnableEntityArgument(self, element: ET.Element) -> RunnableEntityArgument:
        argument = RunnableEntityArgument()
        argument.setSymbol(self.getChildElementOptionalLiteral(element, "SYMBOL"))
        return argument

    def getParameterInAtomicSWCTypeInstanceRef(self, element: ET.Element, key: str) -> ParameterInAtomicSWCTypeInstanceRef:
        parameter_iref = None
        child_element = self.find(element, key)
        if child_element is not None:
            parameter_iref = ParameterInAtomicSWCTypeInstanceRef()
            for ref in self.getChildElementRefTypeList(child_element, "CONTEXT-DATA-PROTOTYPE-REF"):
                parameter_iref.addContextDataPrototypeRef(ref)
            parameter_iref.setPortPrototypeRef(self.getChildElementOptionalRefType(child_element, "PORT-PROTOTYPE-REF"))
            parameter_iref.setRootParameterDataPrototypeRef(self.getChildElementOptionalRefType(child_element, "ROOT-PARAMETER-DATA-PROTOTYPE-REF"))
            parameter_iref.setTargetDataPrototypeRef(self.getChildElementOptionalRefType(child_element, "TARGET-DATA-PROTOTYPE-REF"))
        return parameter_iref

    def getAutosarParameterRef(self, element: ET.Element, key: str) -> AutosarParameterRef:
        parameter = None
        child_element = self.find(element, key)
        if child_element is not None:
            parameter = AutosarParameterRef()
            parameter.setAutosarParameterIRef(self.getParameterInAtomicSWCTypeInstanceRef(child_element, "AUTOSAR-PARAMETER-IREF"))
            parameter.setLocalParameterRef(self.getChildElementOptionalRefType(child_element, "LOCAL-PARAMETER-REF"))
        return parameter

    def readParameterAccess(self, element: ET.Element, access: ParameterAccess):
        self.readIdentifiable(element, access)
        access.setAccessedParameter(self.getAutosarParameterRef(element, "ACCESSED-PARAMETER"))

    def readRunnableEntityParameterAccesses(self, element: ET.Element, parent: RunnableEntity):
        for child_element in self.findall(element, "PARAMETER-ACCESSS/PARAMETER-ACCESS"):
            short_name = self.getShortName(child_element)
            self.logger.debug("readParameterAccesses %s" % short_name)
            parameter_access = parent.createParameterAccess(short_name)
            self.readParameterAccess(child_element, parameter_access)

    def readRunnableEntityWrittenLocalVariables(self, element: ET.Element, parent: RunnableEntity):
        self._readVariableAccesses(element, parent, "WRITTEN-LOCAL-VARIABLES")

    def readRunnableEntityReadLocalVariables(self, element: ET.Element, parent: RunnableEntity):
        self._readVariableAccesses(element, parent, "READ-LOCAL-VARIABLES")

    def readROperationIRef(self, element: ET.Element, key: str, parent: ServerCallPoint):
        child_element = self.find(element, key)
        if child_element is not None:
            operation_iref = ROperationInAtomicSwcInstanceRef()
            self.readARObjectAttributes(child_element, operation_iref)
            operation_iref.setContextRPortRef(self.getChildElementOptionalRefType(child_element, "CONTEXT-R-PORT-REF"))
            operation_iref.setTargetRequiredOperationRef(self.getChildElementOptionalRefType(child_element, "TARGET-REQUIRED-OPERATION-REF"))
            parent.setOperationIRef(operation_iref)

    def readRVariableInAtomicSwcInstanceRef(self, element: ET.Element, parent: DataReceivedEvent):
        child_element = self.find(element, "DATA-IREF")
        if child_element is not None:
            data_iref = RVariableInAtomicSwcInstanceRef()
            data_iref.setContextRPortRef(self.getChildElementOptionalRefType(child_element, "CONTEXT-R-PORT-REF"))
            data_iref.setTargetDataElementRef(self.getChildElementOptionalRefType(child_element, "TARGET-DATA-ELEMENT-REF"))
            parent.setDataIRef(data_iref)

    def readRModeInAtomicSwcInstanceRef(self, element: ET.Element, parent: SwcModeSwitchEvent):
        for child_element in self.findall(element, "MODE-IREFS/MODE-IREF"):
            mode_iref = RModeInAtomicSwcInstanceRef()
            mode_iref.setContextPortRef(self.getChildElementOptionalRefType(child_element, "CONTEXT-PORT-REF"))
            mode_iref.setContextModeDeclarationGroupPrototypeRef(self.getChildElementOptionalRefType(child_element, "CONTEXT-MODE-DECLARATION-GROUP-PROTOTYPE-REF"))
            mode_iref.setTargetModeDeclarationRef(self.getChildElementOptionalRefType(child_element, "TARGET-MODE-DECLARATION-REF"))  # NOQA E501
            parent.addModeIRef(mode_iref)

    def readSynchronousServerCallPoint(self, element: ET.Element, parent: RunnableEntity):
        # self.logger.debug("readSynchronousServerCallPoint %s" % short_name)
        short_name = self.getShortName(element)
        server_call_point = parent.createSynchronousServerCallPoint(short_name)
        self.readIdentifiable(element, server_call_point)
        server_call_point.setTimeout(self.getChildElementOptionalFloatValue(element, "TIMEOUT"))
        self.readROperationIRef(element, "OPERATION-IREF", server_call_point)

    def readAsynchronousServerCallPoint(self, element: ET.Element, parent: RunnableEntity):
        # self.logger.debug("readAsynchronousServerCallPoint %s" % short_name)
        short_name = self.getShortName(element)
        server_call_point = parent.createAsynchronousServerCallPoint(short_name)
        self.readIdentifiable(element, server_call_point)
        server_call_point.setTimeout(self.getChildElementOptionalFloatValue(element, "TIMEOUT"))
        self.readROperationIRef(element, "OPERATION-IREF", server_call_point)

    def readRunnableEntityInternalBehaviorServerCallPoint(self, element: ET.Element, parent: RunnableEntity):
        for child_element in self.findall(element, "SERVER-CALL-POINTS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "SYNCHRONOUS-SERVER-CALL-POINT":
                self.readSynchronousServerCallPoint(child_element, parent)
            elif tag_name == "ASYNCHRONOUS-SERVER-CALL-POINT":
                self.readAsynchronousServerCallPoint(child_element, parent)
            else:
                self.raiseError("Unsupported server call point type <%s>" % tag_name)

    def readRunnableEntityInternalTriggeringPoints(self, element: ET.Element, parent: RunnableEntity):
        for child_element in self.findall(element, "INTERNAL-TRIGGERING-POINTS/INTERNAL-TRIGGERING-POINT"):
            short_name = self.getShortName(child_element)
            point = parent.createInternalTriggeringPoint(short_name)
            point.sw_impl_policy = self.getChildElementOptionalLiteral(child_element, "SW-IMPL-POLICY")

    def readRunnableEntityExternalTriggeringPoints(self, element: ET.Element, parent: RunnableEntity):
        for child_element in self.findall(element, "EXTERNAL-TRIGGERING-POINTS/EXTERNAL-TRIGGERING-POINT"):
            point = ExternalTriggeringPoint()
            ident_element = self.find(child_element, "IDENT")
            if ident_element is not None:
                point.createIdent(self.getShortName(ident_element))
            trigger_element = self.find(child_element, "TRIGGER-IREF")
            if trigger_element is not None:
                trigger = PTriggerInAtomicSwcTypeInstanceRef()
                self.readPTriggerInAtomicSwcTypeInstanceRef(trigger_element, trigger)
                point.setTrigger(trigger)
            parent.addExternalTriggeringPoint(point)

    def readModeGroupInAtomicSwcInstanceRef(self, element: ET.Element, instance_ref: ModeGroupInAtomicSwcInstanceRef):
        instance_ref.setBaseRef(self.getChildElementOptionalRefType(element, "BASE-REF"))
        instance_ref.setContextPortRef(self.getChildElementOptionalRefType(element, "CONTEXT-PORT-REF"))

    def readRModeGroupInAtomicSWCInstanceRef(self, element: ET.Element, instance_ref: RModeGroupInAtomicSWCInstanceRef):
        self.readModeGroupInAtomicSwcInstanceRef(element, instance_ref)
        instance_ref.setContextRPortRef(self.getChildElementOptionalRefType(element, "CONTEXT-R-PORT-REF"))
        instance_ref.setTargetModeGroupRef(self.getChildElementOptionalRefType(element, "TARGET-MODE-GROUP-REF"))

    def readPModeGroupInAtomicSWCInstanceRef(self, element: ET.Element, instance_ref: PModeGroupInAtomicSwcInstanceRef):
        self.readModeGroupInAtomicSwcInstanceRef(element, instance_ref)
        instance_ref.setContextPPortRef(self.getChildElementOptionalRefType(element, "CONTEXT-P-PORT-REF"))
        instance_ref.setTargetModeGroupRef(self.getChildElementOptionalRefType(element, "TARGET-MODE-GROUP-REF"))

    def readPTriggerInAtomicSwcTypeInstanceRef(self, element: ET.Element, instance_ref: PTriggerInAtomicSwcTypeInstanceRef):
        instance_ref.setContextPPortRef(self.getChildElementOptionalRefType(element, "CONTEXT-P-PORT-REF"))
        instance_ref.setTargetTriggerRef(self.getChildElementOptionalRefType(element, "TARGET-TRIGGER-REF"))

    def readInnerDataPrototypeGroupInCompositionInstanceRef(self, element: ET.Element, instance_ref: InnerDataPrototypeGroupInCompositionInstanceRef):
        for ref in self.getChildElementRefTypeList(element, "CONTEXT-SW-COMPONENT-PROTOTYPE-REF"):
            instance_ref.addContextSwComponentPrototypeRef(ref)
        instance_ref.setTargetDataPrototypeGroupRef(self.getChildElementOptionalRefType(element, "TARGET-DATA-PROTOTYPE-GROUP-REF"))

    def readInnerRunnableEntityGroupInCompositionInstanceRef(self, element: ET.Element, instance_ref: InnerRunnableEntityGroupInCompositionInstanceRef):
        for ref in self.getChildElementRefTypeList(element, "CONTEXT-SW-COMPONENT-PROTOTYPE-REF"):
            instance_ref.addContextSwComponentPrototypeRef(ref)
        instance_ref.setTargetRunnableEntityGroupRef(self.getChildElementOptionalRefType(element, "TARGET-RUNNABLE-ENTITY-GROUP-REF"))

    def readRunnableEntityInCompositionInstanceRef(self, element: ET.Element, instance_ref: RunnableEntityInCompositionInstanceRef):
        for ref in self.getChildElementRefTypeList(element, "CONTEXT-SW-COMPONENT-PROTOTYPE-REF"):
            instance_ref.addContextSwComponentPrototypeRef(ref)
        instance_ref.setTargetRunnableEntityRef(self.getChildElementOptionalRefType(element, "TARGET-RUNNABLE-ENTITY-REF"))

    def readVariableDataPrototypeInCompositionInstanceRef(self, element: ET.Element, instance_ref: VariableDataPrototypeInCompositionInstanceRef):
        for ref in self.getChildElementRefTypeList(element, "CONTEXT-SW-COMPONENT-PROTOTYPE-REF"):
            instance_ref.addContextSwComponentPrototypeRef(ref)
        instance_ref.setContextPortPrototypeRef(self.getChildElementOptionalRefType(element, "CONTEXT-PORT-PROTOTYPE-REF"))
        instance_ref.setTargetVariableDataPrototypeRef(self.getChildElementOptionalRefType(element, "TARGET-VARIABLE-DATA-PROTOTYPE-REF"))

    def readDataPrototypeGroupDataPrototypeGroupIRefs(self, element: ET.Element, parent: DataPrototypeGroup):
        for child_element in self.findall(element, "DATA-PROTOTYPE-GROUP-IREFS/DATA-PROTOTYPE-GROUP-IREF"):
            instance_ref = InnerDataPrototypeGroupInCompositionInstanceRef()
            self.readInnerDataPrototypeGroupInCompositionInstanceRef(child_element, instance_ref)
            parent.addDataPrototypeGroupIRef(instance_ref)

    def readDataPrototypeGroupImplicitDataAccessIRefs(self, element: ET.Element, parent: DataPrototypeGroup):
        for child_element in self.findall(element, "IMPLICIT-DATA-ACCESS-IREFS/IMPLICIT-DATA-ACCESS-IREF"):
            instance_ref = VariableDataPrototypeInCompositionInstanceRef()
            self.readVariableDataPrototypeInCompositionInstanceRef(child_element, instance_ref)
            parent.addImplicitDataAccessIRef(instance_ref)

    def readDataPrototypeGroup(self, element: ET.Element, data_group: DataPrototypeGroup):
        self.logger.debug("readDataPrototypeGroup %s" % data_group.getShortName())
        self.readIdentifiable(element, data_group)
        self.readDataPrototypeGroupDataPrototypeGroupIRefs(element, data_group)
        self.readDataPrototypeGroupImplicitDataAccessIRefs(element, data_group)

    def readRunnableEntityGroupRunnableEntityGroupIRefs(self, element: ET.Element, parent: RunnableEntityGroup):
        for child_element in self.findall(element, "RUNNABLE-ENTITY-GROUP-IREFS/RUNNABLE-ENTITY-GROUP-IREF"):
            instance_ref = InnerRunnableEntityGroupInCompositionInstanceRef()
            self.readInnerRunnableEntityGroupInCompositionInstanceRef(child_element, instance_ref)
            parent.addRunnableEntityGroupIRef(instance_ref)

    def readRunnableEntityGroupRunnableEntityIRefs(self, element: ET.Element, parent: RunnableEntityGroup):
        for child_element in self.findall(element, "RUNNABLE-ENTITY-IREFS/RUNNABLE-ENTITY-IREF"):
            instance_ref = RunnableEntityInCompositionInstanceRef()
            self.readRunnableEntityInCompositionInstanceRef(child_element, instance_ref)
            parent.addRunnableEntityIRef(instance_ref)

    def readRunnableEntityGroup(self, element: ET.Element, runnable_group: RunnableEntityGroup):
        self.logger.debug("readRunnableEntityGroup %s" % runnable_group.getShortName())
        self.readIdentifiable(element, runnable_group)
        self.readRunnableEntityGroupRunnableEntityGroupIRefs(element, runnable_group)
        self.readRunnableEntityGroupRunnableEntityIRefs(element, runnable_group)

    def readConsistencyNeedsDpgDoesNotRequireCoherencys(self, element: ET.Element, parent: ConsistencyNeeds):
        for child_element in self.findall(element, "DPG-DOES-NOT-REQUIRE-COHERENCYS/DATA-PROTOTYPE-GROUP"):
            data_group = parent.createDpgDoesNotRequireCoherency(self.getShortName(child_element))
            self.readDataPrototypeGroup(child_element, data_group)

    def readConsistencyNeedsDpgRequiresCoherencys(self, element: ET.Element, parent: ConsistencyNeeds):
        for child_element in self.findall(element, "DPG-REQUIRES-COHERENCYS/DATA-PROTOTYPE-GROUP"):
            data_group = parent.createDpgRequiresCoherency(self.getShortName(child_element))
            self.readDataPrototypeGroup(child_element, data_group)

    def readConsistencyNeedsRegDoesNotRequireStabilitys(self, element: ET.Element, parent: ConsistencyNeeds):
        for child_element in self.findall(element, "REG-DOES-NOT-REQUIRE-STABILITYS/RUNNABLE-ENTITY-GROUP"):
            runnable_group = parent.createRegDoesNotRequireStability(self.getShortName(child_element))
            self.readRunnableEntityGroup(child_element, runnable_group)

    def readConsistencyNeedsRegRequiresStabilitys(self, element: ET.Element, parent: ConsistencyNeeds):
        for child_element in self.findall(element, "REG-REQUIRES-STABILITYS/RUNNABLE-ENTITY-GROUP"):
            runnable_group = parent.createRegRequiresStability(self.getShortName(child_element))
            self.readRunnableEntityGroup(child_element, runnable_group)

    def readConsistencyNeeds(self, element: ET.Element, consistency_needs: ConsistencyNeeds):
        self.logger.debug("readConsistencyNeeds %s" % consistency_needs.getShortName())
        self.readIdentifiable(element, consistency_needs)
        self.readConsistencyNeedsDpgDoesNotRequireCoherencys(element, consistency_needs)
        self.readConsistencyNeedsDpgRequiresCoherencys(element, consistency_needs)
        self.readConsistencyNeedsRegDoesNotRequireStabilitys(element, consistency_needs)
        self.readConsistencyNeedsRegRequiresStabilitys(element, consistency_needs)

    def getModeGroupIRef(self, element: ET.Element, key: str) -> ModeGroupInAtomicSwcInstanceRef:
        instance_ref = None
        for child_element in self.findall(element, "%s/*" % key):
            tag_name = self.getTagName(child_element)
            if tag_name == "P-MODE-GROUP-IN-ATOMIC-SWC-INSTANCE-REF":
                instance_ref = PModeGroupInAtomicSwcInstanceRef()
                self.readPModeGroupInAtomicSWCInstanceRef(child_element, instance_ref)
            elif tag_name == "R-MODE-GROUP-IN-ATOMIC-SWC-INSTANCE-REF":
                instance_ref = RModeGroupInAtomicSWCInstanceRef()
                self.readRModeGroupInAtomicSWCInstanceRef(child_element, instance_ref)
            else:
                self.notImplemented("Unsupported Mode Group IRef <%s>" % tag_name)
        return instance_ref

    def readModeAccessPoint(self, element: ET.Element, point: ModeAccessPoint):
        self.readARObjectAttributes(element, point)
        point.setModeGroupIRef(self.getModeGroupIRef(element, "MODE-GROUP-IREF"))

    def readRunnableEntityModeAccessPoints(self, element: ET.Element, entity: RunnableEntity):
        for child_element in self.findall(element, "MODE-ACCESS-POINTS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "MODE-ACCESS-POINT":
                point = ModeAccessPoint()
                self.readModeAccessPoint(child_element, point)
                entity.addModeAccessPoint(point)
            else:
                self.notImplemented("Unsupported Mode Access Point <%s>" % tag_name)

    def readModeSwitchPointModeGroupIRef(self, element: ET.Element, point: ModeSwitchPoint):
        child_element = self.find(element, "MODE-GROUP-IREF")
        if child_element is not None:
            instance_ref = PModeGroupInAtomicSwcInstanceRef()
            self.readPModeGroupInAtomicSWCInstanceRef(child_element, instance_ref)
            point.setModeGroupIRef(instance_ref)

    def readModeSwitchPoint(self, element: ET.Element, point: ModeSwitchPoint):
        self.readARObjectAttributes(element, point)
        self.readModeSwitchPointModeGroupIRef(element, point)

    def readRunnableEntityModeSwitchPoints(self, element: ET.Element, parent: RunnableEntity):
        for child_element in self.findall(element, "MODE-SWITCH-POINTS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "MODE-SWITCH-POINT":
                point = parent.createModeSwitchPoint(self.getShortName(child_element))
                self.readModeSwitchPoint(child_element, point)
            else:
                self.notImplemented("Unsupported Mode Switch Point <%s>" % tag_name)

    def readRunnableEntityArguments(self, element: ET.Element, entity: RunnableEntity):
        for child_element in self.findall(element, "ARGUMENTS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "RUNNABLE-ENTITY-ARGUMENT":
                entity.addArgument(self.getRunnableEntityArgument(child_element))
            else:
                self.notImplemented("Unsupported Arguments of runnable entity <%s>" % tag_name)

    def readRunnableEntityAsynchronousServerCallResultPoint(self, element: ET.Element, entity: RunnableEntity):
        for child_element in self.findall(element, "ASYNCHRONOUS-SERVER-CALL-RESULT-POINTS/ASYNCHRONOUS-SERVER-CALL-RESULT-POINT"):
            point = entity.createAsynchronousServerCallResultPoint(self.getShortName(child_element))
            self.readIdentifiable(child_element, point)
            point.setAsynchronousServerCallPointRef(self.getChildElementOptionalRefType(child_element, "ASYNCHRONOUS-SERVER-CALL-POINT-REF"))

    def readRunnableEntityWaitPoints(self, element: ET.Element, entity: RunnableEntity):
        for child_element in self.findall(element, "WAIT-POINTS/WAIT-POINT"):
            point = entity.createWaitPoint(self.getShortName(child_element))
            self.readIdentifiable(child_element, point)
            point.setTimeout(self.getChildElementOptionalTimeValue(child_element, "TIMEOUT"))
            point.setTriggerRef(self.getChildElementOptionalRefType(child_element, "TRIGGER"))

    def readRunnableEntity(self, element: ET.Element, entity: RunnableEntity):
        self.readExecutableEntity(element, entity)
        self.readRunnableEntityArguments(element, entity)

        self.readRunnableEntityAsynchronousServerCallResultPoint(element, entity)
        entity.setCanBeInvokedConcurrently(self.getChildElementOptionalBooleanValue(element, "CAN-BE-INVOKED-CONCURRENTLY"))
        self.readRunnableEntityDataReadAccesses(element, entity)
        self.readRunnableEntityDataReceivePointByArguments(element, entity)
        self.readRunnableEntityDataReceivePointByValues(element, entity)
        self.readRunnableEntityDataWriteAccesses(element, entity)
        self.readRunnableEntityDataSendPoints(element, entity)
        self.readRunnableEntityInternalBehaviorServerCallPoint(element, entity)
        self.readRunnableEntityInternalTriggeringPoints(element, entity)
        self.readRunnableEntityExternalTriggeringPoints(element, entity)
        self.readRunnableEntityModeAccessPoints(element, entity)
        self.readRunnableEntityModeSwitchPoints(element, entity)
        self.readRunnableEntityParameterAccesses(element, entity)
        self.readRunnableEntityReadLocalVariables(element, entity)
        self.readRunnableEntityWaitPoints(element, entity)
        self.readRunnableEntityWrittenLocalVariables(element, entity)

        entity.setSymbol(self.getChildElementOptionalLiteral(element, "SYMBOL"))

    def readSwcInternalBehaviorRunnables(self, element: ET.Element, parent: SwcInternalBehavior):
        for child_element in self.findall(element, "RUNNABLES/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "RUNNABLE-ENTITY":
                entity = parent.createRunnableEntity(self.getShortName(child_element))
                self.readRunnableEntity(child_element, entity)
            else:
                self.notImplemented("Unsupported Runnables <%s>" % tag_name)

    def getRModeInAtomicSwcInstanceRef(self, element: ET.Element) -> RModeInAtomicSwcInstanceRef:
        instance_ref = RModeInAtomicSwcInstanceRef()
        instance_ref.setBaseRef(self.getChildElementOptionalRefType(element, "BASE-REF"))
        instance_ref.setContextPortRef(self.getChildElementOptionalRefType(element, "CONTEXT-PORT-REF"))
        instance_ref.setContextModeDeclarationGroupPrototypeRef(self.getChildElementOptionalRefType(element, "CONTEXT-MODE-DECLARATION-GROUP-PROTOTYPE-REF"))
        instance_ref.setTargetModeDeclarationRef(self.getChildElementOptionalRefType(element, "TARGET-MODE-DECLARATION-REF"))  # NOQA E501
        return instance_ref

    def getModeInBswModuleDescriptionInstanceRef(self, element: ET.Element) -> ModeInBswModuleDescriptionInstanceRef:
        instance_ref = ModeInBswModuleDescriptionInstanceRef()
        self.readARObjectAttributes(element, instance_ref)
        instance_ref.setContextModeDeclarationGroupRef(self.getChildElementOptionalRefType(element, "CONTEXT-MODE-DECLARATION-GROUP-REF"))
        instance_ref.setTargetModeRef(self.getChildElementOptionalRefType(element, "TARGET-MODE-REF"))  # NOQA E501
        return instance_ref

    def readRTEEvent(self, element: ET.Element, event: RTEEvent):
        self.readIdentifiable(element, event)
        event.activationReasonRepresentationRef = self.getChildElementOptionalRefType(element, "ACTIVATION-REASON-REPRESENTATION-REF")
        event.startOnEventRef = self.getChildElementOptionalRefType(element, "START-ON-EVENT-REF")
        for child_element in self.findall(element, "DISABLED-MODE-IREFS/DISABLED-MODE-IREF"):
            iref = self.getRModeInAtomicSwcInstanceRef(child_element)
            event.addDisabledModeIRef(iref)

    def readPOperationIRef(self, element: ET.Element, key: str, parent: OperationInvokedEvent):
        child_element = self.find(element, key)
        if child_element is not None:
            operation_iref = POperationInAtomicSwcInstanceRef()
            self.readARObjectAttributes(child_element, operation_iref)
            operation_iref.setContextPPortRef(self.getChildElementRefType(parent.getShortName(), child_element, "CONTEXT-P-PORT-REF"))
            operation_iref.setTargetProvidedOperationRef(self.getChildElementRefType(parent.getShortName(), child_element, "TARGET-PROVIDED-OPERATION-REF"))  # NOQA E501
            parent.setOperationIRef(operation_iref)

    def readOperationInvokedEvent(self, element: ET.Element, event: OperationInvokedEvent):
        # self.logger.debug("Read OperationInvokedEvent <%s>" % event.getShortName())
        self.readPOperationIRef(element, "OPERATION-IREF", event)
        self.readRTEEvent(element, event)

    def readVariableDataPrototype(self, element: ET.Element, prototype: VariableDataPrototype):
        self.readAutosarDataPrototype(element, prototype)
        prototype.setInitValue(self.getInitValue(element))

    def readSwcInternalBehaviorExplicitInterRunnableVariables(self, element: ET.Element, parent: SwcInternalBehavior):
        for child_element in self.findall(element, "EXPLICIT-INTER-RUNNABLE-VARIABLES/VARIABLE-DATA-PROTOTYPE"):
            short_name = self.getShortName(child_element)
            prototype = parent.createExplicitInterRunnableVariable(short_name)
            self.readVariableDataPrototype(child_element, prototype)

    def readSwcInternalBehaviorPerInstanceMemories(self, element: ET.Element, behavior: SwcInternalBehavior):
        for child_element in self.findall(element, "PER-INSTANCE-MEMORYS/PER-INSTANCE-MEMORY"):
            short_name = self.getShortName(child_element)
            memory = behavior.createPerInstanceMemory(short_name)
            self.readIdentifiable(child_element, memory)
            memory.setInitValue(self.getChildElementOptionalLiteral(child_element, "INIT-VALUE"))
            memory.setSwDataDefProps(self.getSwDataDefProps(child_element, "SW-DATA-DEF-PROPS"))
            memory.setType(self.getChildElementOptionalLiteral(child_element, "TYPE"))
            memory.setTypeDefinition(self.getChildElementOptionalLiteral(child_element, "TYPE-DEFINITION"))

    def readAutosarDataPrototype(self, element: ET.Element, prototype: AutosarDataPrototype):
        self.readDataPrototype(element, prototype)
        prototype.setTypeTRef(self.getChildElementOptionalRefType(element, "TYPE-TREF"))

    def readParameterDataPrototype(self, element: ET.Element, prototype: ParameterDataPrototype):
        self.readAutosarDataPrototype(element, prototype)
        prototype.setInitValue(self.getInitValue(element))

    def readSwcInternalBehaviorPerInstanceParameters(self, element: ET.Element, behavior: SwcInternalBehavior):
        for child_element in self.findall(element, "PER-INSTANCE-PARAMETERS/PARAMETER-DATA-PROTOTYPE"):
            short_name = self.getShortName(child_element)
            prototype = behavior.createPerInstanceParameter(short_name)
            self.readParameterDataPrototype(child_element, prototype)

    def readPortDefinedArgumentValue(self, element: ET.Element) -> PortDefinedArgumentValue:
        argument_value = PortDefinedArgumentValue()
        child_element = self.find(element, "VALUE/*")
        if child_element is not None:
            argument_value.setValue(self.getValueSpecification(child_element, self.getTagName(child_element)))
        argument_value.setValueTypeTRef(self.getChildElementOptionalRefType(element, "VALUE-TYPE-TREF"))
        return argument_value

    def readSwcInternalBehaviorPortAPIOptions(self, element: ET.Element, behavior: SwcInternalBehavior):
        for child_element in self.findall(element, "PORT-API-OPTIONS/PORT-API-OPTION"):
            option = PortAPIOption()
            option.setEnableTakeAddress(self.getChildElementOptionalBooleanValue(child_element, "ENABLE-TAKE-ADDRESS"))
            option.setErrorHandling(self.getChildElementOptionalLiteral(child_element, "ERROR-HANDLING"))
            option.setIndirectAPI(self.getChildElementOptionalBooleanValue(child_element, "INDIRECT-API"))
            option.setPortRef(self.getChildElementOptionalRefType(child_element, "PORT-REF"))
            for argument_value_tag in self.findall(child_element, "PORT-ARG-VALUES/PORT-DEFINED-ARGUMENT-VALUE"):
                option.addPortArgValue(self.readPortDefinedArgumentValue(argument_value_tag))
            behavior.addPortAPIOption(option)

    def readTimingEvent(self, element: ET.Element, event: TimingEvent):
        # self.logger.debug("Read TimingEvent <%s>" % event.getShortName())
        self.readRTEEvent(element, event)
        event.setOffset(self.getChildElementOptionalTimeValue(element, "OFFSET"))
        event.setPeriod(self.getChildElementOptionalTimeValue(element, "PERIOD"))

    def readDataReceivedEvent(self, element: ET.Element, event: DataReceivedEvent):
        # self.logger.debug("Read DataReceivedEvent <%s>" % event.getShortName())
        self.readRTEEvent(element, event)
        self.readRVariableInAtomicSwcInstanceRef(element, event)

    def readSwcModeSwitchEvent(self, element: ET.Element, event: SwcModeSwitchEvent):
        # self.logger.debug("Read SwcModeSwitchEvent <%s>" % event.getShortName())
        self.readRTEEvent(element, event)
        activation = self.getChildElementOptionalLiteral(element, "ACTIVATION")
        if activation is not None:
            event.setActivation(ModeActivationKind().setValue(activation.getValue()))
        self.readRModeInAtomicSwcInstanceRef(element, event)

    def readInternalTriggerOccurredEvent(self, element: ET.Element, event: InternalTriggerOccurredEvent):
        # self.logger.debug("Read InternalTriggerOccurredEvent <%s>" % event.getShortName())
        self.readRTEEvent(element, event)
        event.setEventSourceRef(self.getChildElementOptionalRefType(element, "EVENT-SOURCE-REF"))

    def readInitEvent(self, element, event: InitEvent):
        # self.logger.debug("Read InitEvent <%s>" % event.getShortName())
        self.readRTEEvent(element, event)

    def readAsynchronousServerCallReturnsEvent(self, element, event: AsynchronousServerCallReturnsEvent):
        # self.logger.debug("Read AsynchronousServerCallReturnsEvent <%s>" % event.getShortName())
        self.readRTEEvent(element, event)
        event.setEventSourceRef(self.getChildElementOptionalRefType(element, "EVENT-SOURCE-REF"))

    def readModeSwitchedAckEvent(self, element, event: ModeSwitchedAckEvent):
        # self.logger.debug("Read ModeSwitchedAckEvent <%s>" % event.getShortName())
        self.readRTEEvent(element, event)
        event.setEventSourceRef(self.getChildElementOptionalRefType(element, "EVENT-SOURCE-REF"))

    def readBackgroundEvent(self, element, event: BackgroundEvent):
        # self.logger.debug("Read BackgroundEvent <%s>" % event.getShortName())
        self.readRTEEvent(element, event)

    def readDataSendCompletedEvent(self, element, event: DataSendCompletedEvent):
        # self.logger.debug("Read DataSendCompletedEvent <%s>" % event.getShortName())
        self.readRTEEvent(element, event)
        event.setEventSourceRef(self.getChildElementOptionalRefType(element, "EVENT-SOURCE-REF"))

    def readSwcInternalBehaviorEvents(self, element: ET.Element, parent: SwcInternalBehavior):
        for child_element in self.findall(element, "EVENTS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "TIMING-EVENT":
                event = parent.createTimingEvent(self.getShortName(child_element))
                self.readTimingEvent(child_element, event)
            elif tag_name == "SWC-MODE-SWITCH-EVENT":
                event = parent.createSwcModeSwitchEvent(self.getShortName(child_element))
                self.readSwcModeSwitchEvent(child_element, event)
            elif tag_name == "OPERATION-INVOKED-EVENT":
                event = parent.createOperationInvokedEvent(self.getShortName(child_element))
                self.readOperationInvokedEvent(child_element, event)
            elif tag_name == "DATA-RECEIVED-EVENT":
                event = parent.createDataReceivedEvent(self.getShortName(child_element))
                self.readDataReceivedEvent(child_element, event)
            elif tag_name == "INTERNAL-TRIGGER-OCCURRED-EVENT":
                event = parent.createInternalTriggerOccurredEvent(self.getShortName(child_element))
                self.readInternalTriggerOccurredEvent(child_element, event)
            elif tag_name == "INIT-EVENT":
                event = parent.createInitEvent(self.getShortName(child_element))
                self.readInitEvent(child_element, event)
            elif tag_name == "ASYNCHRONOUS-SERVER-CALL-RETURNS-EVENT":
                event = parent.createAsynchronousServerCallReturnsEvent(self.getShortName(child_element))
                self.readAsynchronousServerCallReturnsEvent(child_element, event)
            elif tag_name == "MODE-SWITCHED-ACK-EVENT":
                event = parent.createModeSwitchedAckEvent(self.getShortName(child_element))
                self.readModeSwitchedAckEvent(child_element, event)
            elif tag_name == "BACKGROUND-EVENT":
                event = parent.createBackgroundEvent(self.getShortName(child_element))
                self.readBackgroundEvent(child_element, event)
            elif tag_name == "DATA-SEND-COMPLETED-EVENT":
                event = parent.createDataSendCompletedEvent(self.getShortName(child_element))
                self.readDataSendCompletedEvent(child_element, event)
            else:
                self.notImplemented("Unsupported SwcInternalBehavior Event <%s>" % tag_name)

    def getSwPointerTargetProps(self, element: ET.Element, key: str) -> SwPointerTargetProps:
        child_element = self.find(element, key)
        props = None
        if child_element is not None:
            props = SwPointerTargetProps()
            props.setTargetCategory(self.getChildElementOptionalLiteral(child_element, "TARGET-CATEGORY"))
            props.setSwDataDefProps(self.getSwDataDefProps(child_element, "SW-DATA-DEF-PROPS"))
            props.setFunctionPointerSignatureRef(self.getChildElementOptionalRefType(child_element, "FUNCTION-POINTER-SIGNATURE-REF"))
        return props

    def readSwPointerTargetProps(self, element: ET.Element, parent: SwDataDefProps):
        child_element = self.find(element, "SW-POINTER-TARGET-PROPS")
        if child_element is not None:
            sw_pointer_target_props = SwPointerTargetProps()
            sw_pointer_target_props.setTargetCategory(self.getChildElementOptionalLiteral(child_element, "TARGET-CATEGORY"))
            sw_pointer_target_props.setSwDataDefProps(self.getSwDataDefProps(child_element, "SW-DATA-DEF-PROPS"))
            sw_pointer_target_props.setFunctionPointerSignatureRef(self.getChildElementOptionalRefType(child_element, "FUNCTION-POINTER-SIGNATURE-REF"))
            parent.swPointerTargetProps = sw_pointer_target_props

    def getSwTextProps(self, element: ET.Element, key: str) -> SwTextProps:
        child_element = self.find(element, key)
        props = None
        if child_element is not None:
            props = SwTextProps()
            props.setArraySizeSemantics(self.getChildElementOptionalLiteral(child_element, "ARRAY-SIZE-SEMANTICS"))
            props.setBaseTypeRef(self.getChildElementOptionalRefType(child_element, "BASE-TYPE-REF"))
            props.setSwFillCharacter(self.getChildElementOptionalIntegerValue(child_element, "SW-FILL-CHARACTER"))
            props.setSwMaxTextSize(self.getChildElementOptionalIntegerValue(child_element, "SW-MAX-TEXT-SIZE"))
        return props

    def readLanguageSpecific(self, element: ET.Element, specific: LanguageSpecific):
        self.readARObjectAttributes(element, specific)
        specific.setValue(element.text)
        if "L" in element.attrib:
            specific.setL(element.attrib["L"])  # noqa E741

    def getLParagraphs(self, element: ET.Element, key: str) -> List[LParagraph]:
        results = []
        for child_element in self.findall(element, key):
            l1 = LParagraph()
            self.readLanguageSpecific(child_element, l1)
            results.append(l1)
        return results

    def getMultiLanguageParagraphs(self, element: ET.Element, key: str) -> List[MultiLanguageParagraph]:
        paragraphs = []
        for child_element in self.findall(element, key):
            paragraph = MultiLanguageParagraph()
            self.readARObjectAttributes(child_element, paragraph)
            for l1 in self.getLParagraphs(child_element, "L-1"):
                paragraph.addL1(l1)
            paragraphs.append(paragraph)
        return paragraphs

    def getLPlainTexts(self, element: ET.Element, key: str) -> List[LParagraph]:
        results = []
        for child_element in self.findall(element, key):
            l1 = LParagraph()
            self.readLanguageSpecific(child_element, l1)
            results.append(l1)
        return results

    def getListElements(self, element: ET.Element, key: str) -> List[ARList]:
        """
        Read the DocumentationBlock List
        """
        result = []
        for child_element in self.findall(element, key):
            list = ARList()
            if "TYPE" in child_element.attrib:
                list.setType(child_element.attrib["TYPE"])
            for block in self.getDocumentationBlockList(child_element, "ITEM"):
                list.addItem(block)
            result.append(list)
        return result

    def getGraphic(self, element: ET.Element, key: str) -> Graphic:
        graphic = None
        child_element = self.find(element, key)
        if child_element is not None:
            graphic = Graphic()
            if "FILENAME" in child_element.attrib:
                graphic.setFilename(child_element.attrib["FILENAME"])
        return graphic

    def readMlFigureLGraphics(self, element: ET.Element, figure: MlFigure):
        for child_element in self.findall(element, "L-GRAPHIC"):
            graphic = LGraphic()
            if "L" in child_element.attrib:
                graphic.setL(child_element.attrib["L"])
            graphic.setGraphic(self.getGraphic(child_element, "GRAPHIC"))
            figure.addLGraphics(graphic)

    def readDocumentViewSelectable(self, element: ET.Element, selectable: DocumentViewSelectable):
        self.readARObjectAttributes(element, selectable)

    def readPaginateable(self, element: ET.Element, paginateable: Paginateable):
        self.readDocumentViewSelectable(element, paginateable)

    def readMlFigure(self, element: ET.Element, figure: MlFigure):
        self.readPaginateable(element, figure)
        self.readMlFigureLGraphics(element, figure)

    def getMlFigures(self, element: ET.Element, key: str) -> List[MlFigure]:
        result = []
        for child_element in self.findall(element, key):
            figure = MlFigure()
            self.readMlFigure(child_element, figure)
            result.append(figure)
        return result

    def getMultiLanguagePlainText(self, element: ET.Element, key: str) -> MultiLanguagePlainText:
        paragraph = None
        child_element = self.find(element, key)
        if child_element is not None:
            paragraph = MultiLanguagePlainText()
            self.readARObjectAttributes(child_element, paragraph)
            for l10 in self.getLPlainTexts(child_element, "L-10"):
                paragraph.addL10(l10)
        return paragraph

    def getNote(self, element: ET.Element, key: str) -> Note:
        note = None
        child_element = self.find(element, key)
        if child_element is not None:
            note = Note()
            self.readARObjectAttributes(child_element, note)
            note.setLabel(self.getMultilanguageLongName(child_element, "LABEL"))
            note.setNoteText(self.getDocumentationBlock(child_element, "NOTE-TEXT"))
            if "NOTETYPE" in child_element.attrib:
                note.setNoteType(NoteTypeEnum().setValue(child_element.attrib["NOTETYPE"]))
        return note

    def getTraceableText(self, element: ET.Element, key: str) -> TraceableText:
        traceable_text = None
        child_element = self.find(element, key)
        if child_element is not None:
            traceable_text = TraceableText()
            self.readARObjectAttributes(child_element, traceable_text)
            traceable_text.setText(self.getDocumentationBlock(child_element, "TEXT"))
            for trace_ref in self.findall(child_element, "TRACE-REFS/TRACE-REF"):
                traceable_text.addTraceRef(RefType().setDest(trace_ref.text))
        return traceable_text

    def getStructuredReq(self, element: ET.Element, key: str) -> StructuredReq:
        structured_req = None
        child_element = self.find(element, key)
        if child_element is not None:
            structured_req = StructuredReq()
            self.readARObjectAttributes(child_element, structured_req)
            structured_req.setDate(self.getChildElementOptionalLiteral(child_element, "DATE"))
            structured_req.setImportance(self.getChildElementOptionalLiteral(child_element, "IMPORTANCE"))
            structured_req.setIssuedBy(self.getChildElementOptionalLiteral(child_element, "ISSUED-BY"))
            structured_req.setType(self.getChildElementOptionalLiteral(child_element, "TYPE"))
            structured_req.setDescription(self.getDocumentationBlock(child_element, "DESCRIPTION"))
            structured_req.setRationale(self.getDocumentationBlock(child_element, "RATIONALE"))
            structured_req.setDependencies(self.getDocumentationBlock(child_element, "DEPENDENCIES"))
            structured_req.setUseCase(self.getDocumentationBlock(child_element, "USE-CASE"))
            structured_req.setConflicts(self.getDocumentationBlock(child_element, "CONFLICTS"))
            structured_req.setSupportingMaterial(self.getDocumentationBlock(child_element, "SUPPORTING-MATERIAL"))
            structured_req.setRemark(self.getDocumentationBlock(child_element, "REMARK"))
            for tested_item_ref in self.findall(child_element, "TESTED-ITEM-REFS/TESTED-ITEM-REF"):
                structured_req.addTestedItemRef(RefType().setDest(tested_item_ref.text))
        return structured_req

    def getDefItem(self, element: ET.Element) -> DefItem:
        def_item = DefItem()
        self.readARObjectAttributes(element, def_item)
        def_item.setDef(self.getDocumentationBlock(element, "DEF"))
        if "HELPENTRY" in element.attrib:
            def_item.setHelpEntry(String().setValue(element.attrib["HELPENTRY"]))
        return def_item

    def getDefList(self, element: ET.Element, key: str) -> DefList:
        def_list = None
        child_element = self.find(element, key)
        if child_element is not None:
            def_list = DefList()
            self.readARObjectAttributes(child_element, def_list)
            for def_item in self.findall(child_element, "DEF-ITEM"):
                def_list.addDefItem(self.getDefItem(def_item))
        return def_list

    def getIndentSample(self, element: ET.Element) -> IndentSample:
        indent_sample = IndentSample()
        self.readARObjectAttributes(element, indent_sample)
        if "ITEMLABELPOS" in element.attrib:
            indent_sample.setItemLabelPos(ItemLabelPosEnum().setValue(element.attrib["ITEMLABELPOS"]))
        for l2 in self.getLOverviewParagraphs(element, "L-2"):
            indent_sample.addL2(l2)
        return indent_sample

    def getLabeledItem(self, element: ET.Element) -> LabeledItem:
        labeled_item = LabeledItem()
        self.readARObjectAttributes(element, labeled_item)
        if "HELPENTRY" in element.attrib:
            labeled_item.setHelpEntry(String().setValue(element.attrib["HELPENTRY"]))
        labeled_item.setItemContents(self.getDocumentationBlock(element, "ITEM-CONTENTS"))
        labeled_item.setItemLabel(self.getMultiLanguageOverviewParagraph(element, "ITEM-LABEL"))
        return labeled_item

    def getLabeledList(self, element: ET.Element, key: str) -> LabeledList:
        labeled_list = None
        child_element = self.find(element, key)
        if child_element is not None:
            labeled_list = LabeledList()
            self.readARObjectAttributes(child_element, labeled_list)
            indent_sample = self.find(child_element, "INDENT-SAMPLE")
            if indent_sample is not None:
                labeled_list.setIndentSample(self.getIndentSample(indent_sample))
            for labeled_item in self.findall(child_element, "LABELED-ITEM"):
                labeled_list.addLabeledItem(self.getLabeledItem(labeled_item))
        return labeled_list

    def getLOverviewParagraphs(self, element: ET.Element, key: str) -> List[LOverviewParagraph]:
        results = []
        for child_element in self.findall(element, key):
            l2 = LOverviewParagraph()
            self.readLanguageSpecific(child_element, l2)
            results.append(l2)
        return results

    def getMultiLanguageVerbatim(self, element: ET.Element, key: str) -> MultiLanguageVerbatim:
        verbatim = None
        child_element = self.find(element, key)
        if child_element is not None:
            verbatim = MultiLanguageVerbatim()
            self.readARObjectAttributes(child_element, verbatim)
            if "ALLOWBREAK" in child_element.attrib:
                verbatim.setAllowBreak(NameToken().setValue(child_element.attrib["ALLOWBREAK"]))
            if "FLOAT" in child_element.attrib:
                verbatim.setFloat(FloatEnum().setValue(child_element.attrib["FLOAT"]))
            if "HELPENTRY" in child_element.attrib:
                verbatim.setHelpEntry(String().setValue(child_element.attrib["HELPENTRY"]))
            if "PGWIDE" in child_element.attrib:
                verbatim.setPgwide(PgwideEnum().setValue(child_element.attrib["PGWIDE"]))
            for l5 in self.findall(child_element, "L-5"):
                verbatim_l5 = LVerbatim()
                self.readLanguageSpecific(l5, verbatim_l5)
                verbatim.addL5(verbatim_l5)
        return verbatim

    def getMsrQueryArg(self, element: ET.Element) -> MsrQueryArg:
        msr_query_arg = MsrQueryArg()
        self.readARObjectAttributes(element, msr_query_arg)
        msr_query_arg.setArg(self.getChildElementOptionalLiteral(element, "ARG"))
        if "SI" in element.attrib:
            msr_query_arg.setSi(NameToken().setValue(element.attrib["SI"]))
        return msr_query_arg

    def getMsrQueryProps(self, element: ET.Element) -> MsrQueryProps:
        msr_query_props = MsrQueryProps()
        self.readARObjectAttributes(element, msr_query_props)
        msr_query_props.setComment(self.getChildElementOptionalLiteral(element, "COMMENT"))
        msr_query_props.setMsrQueryName(self.getChildElementOptionalLiteral(element, "MSR-QUERY-NAME"))
        for msr_query_arg in self.findall(element, "MSR-QUERY-ARG"):
            msr_query_props.addMsrQueryArg(self.getMsrQueryArg(msr_query_arg))
        return msr_query_props

    def getMsrQueryP2(self, element: ET.Element, key: str) -> MsrQueryP2:
        msr_query_p2 = None
        child_element = self.find(element, key)
        if child_element is not None:
            msr_query_p2 = MsrQueryP2()
            self.readARObjectAttributes(child_element, msr_query_p2)
            msr_query_props = self.find(child_element, "MSR-QUERY-PROPS")
            if msr_query_props is not None:
                msr_query_p2.setMsrQueryProps(self.getMsrQueryProps(msr_query_props))
            msr_query_p2.setMsrQueryResultP2(self.getDocumentationBlock(child_element, "MSR-QUERY-RESULT-P2"))
        return msr_query_p2

    def getMlFormula(self, element: ET.Element, key: str) -> MlFormula:
        formula = None
        child_element = self.find(element, key)
        if child_element is not None:
            formula = MlFormula()
            self.readPaginateable(child_element, formula)
            formula.setFormulaCaption(self.getCaption(child_element, "FORMULA-CAPTION"))
            for l_graphic in self.findall(child_element, "L-GRAPHIC"):
                graphic = LGraphic()
                if "L" in l_graphic.attrib:
                    graphic.setL(l_graphic.attrib["L"])
                graphic.setGraphic(self.getGraphic(l_graphic, "GRAPHIC"))
                formula.addLGraphic(graphic)
            formula.setVerbatim(self.getMultiLanguageVerbatim(child_element, "VERBATIM"))
            formula.setTexMath(self.getMultiLanguagePlainText(child_element, "TEX-MATH"))
            formula.setGenericMath(self.getMultiLanguagePlainText(child_element, "GENERIC-MATH"))
        return formula

    def readDocumentationBlock(self, element: ET.Element, block: DocumentationBlock):
        self.readARObjectAttributes(element, block)
        for paragraph in self.getMultiLanguageParagraphs(element, "P"):
            block.addP(paragraph)
        for list in self.getListElements(element, "LIST"):
            block.addList(list)
        for figure in self.getMlFigures(element, "FIGURE"):
            block.addFigure(figure)
        block.setDefList(self.getDefList(element, "DEF-LIST"))
        block.setFormula(self.getMlFormula(element, "FORMULA"))
        block.setLabeledList(self.getLabeledList(element, "LABELED-LIST"))
        block.setMsrQueryP2(self.getMsrQueryP2(element, "MSR-QUERY-P2"))
        block.setNote(self.getNote(element, "NOTE"))
        block.setStructuredReq(self.getStructuredReq(element, "STRUCTURED-REQ"))
        block.setTrace(self.getTraceableText(element, "TRACE"))
        block.setVerbatim(self.getMultiLanguageVerbatim(element, "VERBATIM"))

    def getDocumentationBlock(self, element: ET.Element, key: str) -> DocumentationBlock:
        block = None
        child_element = self.find(element, key)
        if child_element is not None:
            block = DocumentationBlock()
            self.readDocumentationBlock(child_element, block)
        return block

    def getDocumentationBlockList(self, element: ET.Element, key: str) -> List[DocumentationBlock]:
        blocks = []
        for child_element in self.findall(element, key):
            block = DocumentationBlock()
            self.readDocumentationBlock(child_element, block)
            blocks.append(block)
        return blocks

    def readGeneralAnnotation(self, element: ET.Element, annotation: GeneralAnnotation):
        annotation.setAnnotationOrigin(self.getChildElementOptionalLiteral(element, "ANNOTATION-ORIGIN"))
        annotation.setAnnotationText(self.getDocumentationBlock(element, "ANNOTATION-TEXT"))
        annotation.setLabel(self.getMultilanguageLongName(element, "LABEL"))

    def getAnnotations(self, element: ET.Element) -> List[Annotation]:
        annotations = []
        for child_element in self.findall(element, "ANNOTATIONS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "ANNOTATION":
                annotation = Annotation()
                self.readGeneralAnnotation(child_element, annotation)
                annotations.append(annotation)
            else:
                self.notImplemented("Unsupported Annotation <%s>" % tag_name)
        return annotations

    def getSwAxisIndividual(self, element: ET.Element) -> SwAxisIndividual:
        props = SwAxisIndividual()
        self.readARObjectAttributes(element, props)
        props.setMaxGradient(self.getChildElementOptionalFloatValue(element, "MAX-GRADIENT"))
        props.setMonotony(self.getChildElementOptionalLiteral(element, "MONOTONY"))
        props.setInputVariableTypeRef(self.getChildElementOptionalRefType(element, "INPUT-VARIABLE-TYPE-REF"))
        props.setCompuMethodRef(self.getChildElementOptionalRefType(element, "COMPU-METHOD-REF"))
        props.setSwMaxAxisPoints(self.getChildElementOptionalNumericalValue(element, "SW-MAX-AXIS-POINTS"))
        props.setSwMinAxisPoints(self.getChildElementOptionalNumericalValue(element, "SW-MIN-AXIS-POINTS"))
        props.setDataConstrRef(self.getChildElementOptionalRefType(element, "DATA-CONSTR-REF"))
        child_element = self.find(element, "SW-AXIS-GENERIC")
        if child_element is not None:
            props.setSwAxisGeneric(self.getSwAxisGeneric(child_element))
        return props

    def getSwAxisGeneric(self, element: ET.Element) -> SwAxisGeneric:
        axis = SwAxisGeneric()
        self.readARObjectAttributes(element, axis)
        axis.setSwAxisTypeRef(self.getChildElementOptionalRefType(element, "SW-AXIS-TYPE-REF"))
        params_wrapper = self.find(element, "SW-GENERIC-AXIS-PARAMS")
        if params_wrapper is not None:
            for param_element in self.findall(params_wrapper, "SW-GENERIC-AXIS-PARAM"):
                axis.addSwGenericAxisParam(self.getSwGenericAxisParam(param_element))
        return axis

    def getSwGenericAxisParam(self, element: ET.Element) -> SwGenericAxisParam:
        param = SwGenericAxisParam()
        self.readARObjectAttributes(element, param)
        param.setSwGenericAxisParamTypeRef(self.getChildElementOptionalRefType(element, "SW-GENERIC-AXIS-PARAM-TYPE-REF"))
        for vf in self.getChildElementNumericalValueList(element, "VF"):
            param.addVf(vf)
        return param

    def getSwAxisGrouped(self, element: ET.Element) -> SwAxisGrouped:
        props = SwAxisGrouped()
        props.setMaxGradient(self.getChildElementOptionalFloatValue(element, "MAX-GRADIENT"))
        props.setMonotony(self.getChildElementOptionalLiteral(element, "MONOTONY"))
        props.setSharedAxisTypeRef(self.getChildElementOptionalRefType(element, "SHARED-AXIS-TYPE-REF"))
        return props

    def getSwCalprmAxis(self, element: ET.Element) -> SwCalprmAxis:
        axis = SwCalprmAxis()
        axis.setSwAxisIndex(self.getChildElementOptionalLiteral(element, "SW-AXIS-INDEX"))
        axis.setCategory(self.getChildElementOptionalLiteral(element, "CATEGORY"))
        child_element = self.find(element, "SW-AXIS-INDIVIDUAL")
        if child_element is not None:
            axis.setSwCalprmAxisTypeProps(self.getSwAxisIndividual(child_element))
        child_element = self.find(element, "SW-AXIS-GROUPED")
        if child_element is not None:
            axis.setSwCalprmAxisTypeProps(self.getSwAxisGrouped(child_element))
        axis.setSwCalibrationAccess(self.getChildElementOptionalLiteral(element, "SW-CALIBRATION-ACCESS"))
        axis.setDisplayFormat(self.getChildElementOptionalLiteral(element, "DISPLAY-FORMAT"))

        return axis

    def getSwCalprmAxisSet(self, element: ET.Element, key: str) -> SwCalprmAxisSet:
        set = SwCalprmAxisSet()
        for child_element in self.findall(element, "%s/*" % key):
            tag_name = self.getTagName(child_element)
            if tag_name == "SW-CALPRM-AXIS":
                set.addSwCalprmAxis(self.getSwCalprmAxis(child_element))
        return set

    def readSwDataDefProsInvalidValue(self, element: ET.Element, props: SwDataDefProps):
        child_element = self.find(element, "INVALID-VALUE/*")
        if child_element is not None:
            props.setInvalidValue(self.getValueSpecification(child_element, self.getTagName(child_element)))

    def getSwDataDefProps(self, element: ET.Element, key: str) -> SwDataDefProps:
        child_element = self.find(element, key)
        sw_data_def_props = None
        if child_element is not None:
            conditional_tag = self.find(child_element, "SW-DATA-DEF-PROPS-VARIANTS/SW-DATA-DEF-PROPS-CONDITIONAL")
            if conditional_tag is not None:
                sw_data_def_props = SwDataDefProps()
                self.readARObjectAttributes(child_element, sw_data_def_props)

                for annotation in self.getAnnotations(conditional_tag):
                    sw_data_def_props.addAnnotation(annotation)

                sw_data_def_props.setDisplayPresentation(self.getChildElementOptionalLiteral(conditional_tag, "DISPLAY-PRESENTATION"))
                sw_data_def_props.setBaseTypeRef(self.getChildElementOptionalRefType(conditional_tag, "BASE-TYPE-REF"))
                sw_data_def_props.setDataConstrRef(self.getChildElementOptionalRefType(conditional_tag, "DATA-CONSTR-REF"))
                sw_data_def_props.setCompuMethodRef(self.getChildElementOptionalRefType(conditional_tag, "COMPU-METHOD-REF"))
                sw_data_def_props.setSwAddrMethodRef(self.getChildElementOptionalRefType(conditional_tag, "SW-ADDR-METHOD-REF"))
                sw_data_def_props.setSwAlignment(self.getChildElementOptionalLiteral(conditional_tag, "SW-ALIGNMENT"))
                sw_data_def_props.setSwImplPolicy(self.getChildElementOptionalLiteral(conditional_tag, "SW-IMPL-POLICY"))
                sw_data_def_props.setSwIntendedResolution(self.getChildElementOptionalNumericalValue(conditional_tag, "SW-INTENDED-RESOLUTION"))
                sw_data_def_props.setImplementationDataTypeRef(self.getChildElementOptionalRefType(conditional_tag, "IMPLEMENTATION-DATA-TYPE-REF"))
                sw_data_def_props.setStepSize(self.getChildElementOptionalFloatValue(conditional_tag, "STEP-SIZE"))
                sw_data_def_props.setSwCalibrationAccess(self.getChildElementOptionalLiteral(conditional_tag, "SW-CALIBRATION-ACCESS"))
                sw_data_def_props.setSwCalprmAxisSet(self.getSwCalprmAxisSet(conditional_tag, "SW-CALPRM-AXIS-SET"))
                sw_data_def_props.setSwPointerTargetProps(self.getSwPointerTargetProps(conditional_tag, "SW-POINTER-TARGET-PROPS"))
                sw_data_def_props.setSwTextProps(self.getSwTextProps(conditional_tag, "SW-TEXT-PROPS"))
                sw_data_def_props.setSwRecordLayoutRef(self.getChildElementOptionalRefType(conditional_tag, "SW-RECORD-LAYOUT-REF"))
                sw_data_def_props.setValueAxisDataTypeRef(self.getChildElementOptionalRefType(conditional_tag, "VALUE-AXIS-DATA-TYPE-REF"))
                sw_data_def_props.setUnitRef(self.getChildElementOptionalRefType(conditional_tag, "UNIT-REF"))
                sw_data_def_props.setDisplayFormat(self.getChildElementOptionalLiteral(conditional_tag, "DISPLAY-FORMAT"))
                sw_data_def_props.setAdditionalNativeTypeQualifier(self.getChildElementOptionalLiteral(conditional_tag, "ADDITIONAL-NATIVE-TYPE-QUALIFIER"))
                sw_data_def_props.setSwInterpolationMethod(self.getChildElementOptionalLiteral(conditional_tag, "SW-INTERPOLATION-METHOD"))
                sw_data_def_props.setSwIsVirtual(self.getChildElementOptionalBooleanValue(conditional_tag, "SW-IS-VIRTUAL"))
                self.readSwDataDefProsInvalidValue(conditional_tag, sw_data_def_props)
                self.readSwDataDefPropsBits(conditional_tag, sw_data_def_props)
                self.readSwComparisonVariables(conditional_tag, sw_data_def_props)
                self.readSwDataDependency(conditional_tag, sw_data_def_props)
                self.readSwHostVariable(conditional_tag, sw_data_def_props)
                self.readSwRefTiming(conditional_tag, sw_data_def_props)
                # self.readSwPointerTargetProps(conditional_tag, sw_data_def_props)
        return sw_data_def_props

    def readSwDataDefPropsBits(self, element: ET.Element, props: SwDataDefProps):
        bit_representation_element = self.find(element, "SW-BIT-REPRESENTATION")
        if bit_representation_element is not None:
            bit_representation = SwBitRepresentation()
            bit_representation.setBitPosition(self.getChildElementOptionalIntegerValue(bit_representation_element, "BIT-POSITION"))
            bit_representation.setNumberOfBits(self.getChildElementOptionalIntegerValue(bit_representation_element, "NUMBER-OF-BITS"))
            props.setSwBitRepresentation(bit_representation)
        value_block_size = self.getChildElementOptionalNumericalValue(element, "SW-VALUE-BLOCK-SIZE")
        props.setSwValueBlockSize(value_block_size)
        for mult_element in self.findall(element, "SW-VALUE-BLOCK-SIZE-MULTS/NUMERICAL-VALUE-VARIATION-POINT"):
            value = self.getChildElementOptionalNumericalValue(mult_element, "VALUE")
            if value is None:
                value = self.getChildElementOptionalNumericalValue(mult_element, "V")
            props.addSwValueBlockSizeMult(value)

    def readSwComparisonVariables(self, element: ET.Element, props: SwDataDefProps):
        for proxy_element in self.findall(element, "SW-COMPARISON-VARIABLES/SW-VARIABLE-REF-PROXY"):
            props.addSwComparisonVariable(self.readSwVariableRefProxy(proxy_element))

    def readSwHostVariable(self, element: ET.Element, props: SwDataDefProps):
        host_variable_element = self.find(element, "SW-HOST-VARIABLE")
        if host_variable_element is not None:
            props.setSwHostVariable(self.readSwVariableRefProxy(host_variable_element))

    def readSwVariableRefProxy(self, element: ET.Element) -> SwVariableRefProxy:
        proxy = SwVariableRefProxy()
        proxy.setAutosarVariable(self.getAutosarVariableRef(element, "AUTOSAR-VARIABLE"))
        proxy.setMcDataInstanceVarRef(self.getChildElementOptionalRefType(element, "MC-DATA-INSTANCE-VAR-REF"))
        return proxy

    def readSwDataDependency(self, element: ET.Element, props: SwDataDefProps):
        dependency_element = self.find(element, "SW-DATA-DEPENDENCY")
        if dependency_element is not None:
            dependency = SwDataDependency()
            formula_element = self.find(dependency_element, "SW-DATA-DEPENDENCY-FORMULA")
            if formula_element is not None:
                formula = CompuGenericMath()
                level = formula_element.attrib.get("LEVEL")
                if level is not None:
                    formula.setLevel(ARLiteral().setValue(level))
                dependency.setSwDataDependencyFormula(formula)
            args_element = self.find(dependency_element, "SW-DATA-DEPENDENCY-ARGS")
            if args_element is not None:
                args = SwDataDependencyArgs()
                calprm_element = self.find(args_element, "SW-CALPRM-REF-PROXY")
                if calprm_element is not None:
                    args.setSwCalprmRef(self.readSwCalprmRefProxy(calprm_element))
                variable_element = self.find(args_element, "SW-VARIABLE-REF-PROXY")
                if variable_element is not None:
                    args.setSwVariable(self.readSwVariableRefProxy(variable_element))
                dependency.setSwDataDependencyArgs(args)
            props.setSwDataDependency(dependency)

    def readSwCalprmRefProxy(self, element: ET.Element) -> SwCalprmRefProxy:
        proxy = SwCalprmRefProxy()
        proxy.setArParameter(self.getAutosarParameterRef(element, "AR-PARAMETER"))
        proxy.setMcDataInstanceRef(self.getChildElementOptionalRefType(element, "MC-DATA-INSTANCE-REF"))
        return proxy

    def readSwRefTiming(self, element: ET.Element, props: SwDataDefProps):
        refresh_timing_element = self.find(element, "SW-REFRESH-TIMING")
        if refresh_timing_element is not None:
            refresh_timing = MultidimensionalTime()
            self.readMultidimensionalTime(refresh_timing_element, refresh_timing)
            props.setSwRefreshTiming(refresh_timing)

    def readAutosarDataType(self, element: ET.Element, data_type: AutosarDataType):
        self.readIdentifiable(element, data_type)
        data_type.setSwDataDefProps(self.getSwDataDefProps(element, "SW-DATA-DEF-PROPS"))

    def readApplicationPrimitiveDataType(self, element: ET.Element, data_type: ApplicationPrimitiveDataType):
        self.logger.debug("Read ApplicationPrimitiveDataType <%s>" % data_type.getShortName())
        self.readAutosarDataType(element, data_type)

    def readApplicationRecordElement(self, element: ET.Element, record_element: ApplicationRecordElement):
        # self.logger.debug("Read ApplicationRecordElement %s" % record_element.getShortName())
        self.readApplicationCompositeElementDataPrototype(element, record_element)

    def readApplicationRecordDataTypeElements(self, element: ET.Element, parent: ApplicationRecordDataType):
        for child_element in self.findall(element, "ELEMENTS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "APPLICATION-RECORD-ELEMENT":
                record_element = parent.createApplicationRecordElement(self.getShortName(child_element))
                self.readApplicationRecordElement(child_element, record_element)
            else:
                self.notImplemented("Unsupported ApplicationRecordDataType Element <%s>" % tag_name)

    def readApplicationRecordDataType(self, element: ET.Element, data_type: ApplicationRecordDataType):
        self.logger.debug("Read ApplicationRecordDataType <%s>" % data_type.getShortName())
        self.readIdentifiable(element, data_type)
        data_type.setSwDataDefProps(self.getSwDataDefProps(element, "SW-DATA-DEF-PROPS"))
        self.readApplicationRecordDataTypeElements(element, data_type)

    def readImplementationDataTypeElement(self, element: ET.Element, impl_data_type_element: ImplementationDataTypeElement):
        self.readAutosarDataType(element, impl_data_type_element)
        impl_data_type_element.setArraySize(self.getChildElementOptionalPositiveInteger(element, "ARRAY-SIZE"))
        impl_data_type_element.setArraySizeHandling(self.getChildElementOptionalLiteral(element, "ARRAY-SIZE-HANDLING"))
        impl_data_type_element.setArraySizeSemantics(self.getChildElementOptionalLiteral(element, "ARRAY-SIZE-SEMANTICS"))
        self.readImplementationDataTypeSubElements(element, impl_data_type_element)

    def readImplementationDataTypeSubElements(self, element: ET.Element, parent: ImplementationDataType):
        for child_element in self.findall(element, "SUB-ELEMENTS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "IMPLEMENTATION-DATA-TYPE-ELEMENT":
                impl_data_type_element = parent.createImplementationDataTypeElement(self.getShortName(child_element))
                self.readImplementationDataTypeElement(child_element, impl_data_type_element)
            else:
                self.notImplemented("Unsupported ImplementationDataType SubElement <%s>" % tag_name)

    def readImplementationDataType(self, element: ET.Element, data_type: ImplementationDataType):
        self.logger.debug("Read ImplementationDataType <%s>" % data_type.getShortName())
        self.readAutosarDataType(element, data_type)
        data_type.setDynamicArraySizeProfile(self.getChildElementOptionalLiteral(element, "DYNAMIC-ARRAY-SIZE-PROFILE"))
        data_type.setIsStructWithOptionalElement(self.getChildElementOptionalBooleanValue(element, "IS-STRUCT-WITH-OPTIONAL-ELEMENT"))
        self.readImplementationDataTypeSubElements(element, data_type)
        self.readImplementationDataTypeSymbolProps(element, data_type)
        data_type.setTypeEmitter(self.getChildElementOptionalLiteral(element, "TYPE-EMITTER"))

    def readBaseTypeDirectDefinition(self, element: ET.Element, definition: BaseTypeDirectDefinition):
        definition.setBaseTypeSize(self.getChildElementOptionalPositiveInteger(element, "BASE-TYPE-SIZE"))
        definition.setBaseTypeEncoding(self.getChildElementOptionalLiteral(element, "BASE-TYPE-ENCODING"))
        definition.setMemAlignment(self.getChildElementOptionalPositiveInteger(element, "MEM-ALIGNMENT"))
        definition.setByteOrder(self.getChildElementOptionalLiteral(element, "BYTE-ORDER"))
        definition.setNativeDeclaration(self.getChildElementOptionalLiteral(element, "NATIVE-DECLARATION"))

    def readSwBaseType(self, element: ET.Element, data_type: SwBaseType):
        self.logger.debug("Read SwBaseType <%s>" % data_type.getShortName())
        self.readIdentifiable(element, data_type)
        self.readBaseTypeDirectDefinition(element, data_type.getBaseTypeDefinition())

    def getApplicationCompositeElementInPortInterfaceInstanceRef(self, element: ET.Element, key: str) -> ApplicationCompositeElementInPortInterfaceInstanceRef:
        child_element = self.find(element, key)
        iref = None
        if child_element is not None:
            iref = ApplicationCompositeElementInPortInterfaceInstanceRef()
            iref.setRootDataPrototypeRef(self.getChildElementOptionalRefType(child_element, "ROOT-DATA-PROTOTYPE-REF"))
            iref.setTargetDataPrototypeRef(self.getChildElementOptionalRefType(child_element, "TARGET-DATA-PROTOTYPE-REF"))
        return iref

    def getCompositeNetworkRepresentation(self, element: ET.Element) -> CompositeNetworkRepresentation:
        # self.logger.debug("getCompositeNetworkRepresentation")
        representation = CompositeNetworkRepresentation()
        representation.setLeafElementIRef(self.getApplicationCompositeElementInPortInterfaceInstanceRef(element, "LEAF-ELEMENT-IREF"))
        representation.setNetworkRepresentation(self.getSwDataDefProps(element, "NETWORK-REPRESENTATION"))
        return representation

    def readReceiverComSpec(self, element: ET.Element, com_spec: ReceiverComSpec):
        self.readRPortComSpec(element, com_spec)
        for child_element in self.findall(element, "COMPOSITE-NETWORK-REPRESENTATIONS/COMPOSITE-NETWORK-REPRESENTATION"):
            com_spec.addCompositeNetworkRepresentation(self.getCompositeNetworkRepresentation(child_element))
        com_spec.setDataElementRef(self.getChildElementOptionalRefType(element, "DATA-ELEMENT-REF"))
        com_spec.setNetworkRepresentation(self.getSwDataDefProps(element, "NETWORK-REPRESENTATION"))
        com_spec.setHandleOutOfRange(self.getChildElementOptionalLiteral(element, "HANDLE-OUT-OF-RANGE"))
        com_spec.setHandleOutOfRangeStatus(self.getChildElementOptionalLiteral(element, "HANDLE-OUT-OF-RANGE-STATUS"))
        com_spec.setMaxDeltaCounterInit(self.getChildElementOptionalPositiveInteger(element, "MAX-DELTA-COUNTER-INIT"))
        com_spec.setMaxNoNewOrRepeatedData(self.getChildElementOptionalPositiveInteger(element, "MAX-NO-NEW-OR-REPEATED-DATA"))
        com_spec.setUsesEndToEndProtection(self.getChildElementOptionalBooleanValue(element, "USES-END-TO-END-PROTECTION"))
        reception_props = self.getReceptionComSpecProps(element, "RECEPTION-PROPS")
        if reception_props is not None:
            com_spec.setReceptionProps(reception_props)
        replace_with = self.find(element, "REPLACE-WITH")
        if replace_with is not None:
            variable_access = VariableAccess(None, self.getShortName(replace_with))
            self.readVariableAccess(replace_with, variable_access)
            com_spec.setReplaceWith(variable_access)
        com_spec.setSyncCounterInit(self.getChildElementOptionalPositiveInteger(element, "SYNC-COUNTER-INIT"))
        for child_element in self.findall(element, "TRANSFORMATION-COM-SPEC-PROPSS/TRANSFORMATION-COM-SPEC-PROPS"):
            com_spec.addTransformationComSpecProps(self.getTransformationComSpecProps(child_element))

    def getReceptionComSpecProps(self, element: ET.Element, key: str) -> ReceptionComSpecProps:
        child_element = self.find(element, key)
        if child_element is None:
            return None
        props = ReceptionComSpecProps()
        self.readARObjectAttributes(child_element, props)
        props.setDataUpdatePeriod(self.getChildElementOptionalTimeValue(child_element, "DATA-UPDATE-PERIOD"))
        props.setTimeout(self.getChildElementOptionalTimeValue(child_element, "TIMEOUT"))
        return props

    def readVariableAccess(self, element: ET.Element, access: VariableAccess):
        self.readIdentifiable(element, access)
        access.setAccessedVariableRef(self.getAutosarVariableRef(element, "ACCESSED-VARIABLE"))
        access.setScope(self.getChildElementOptionalLiteral(element, "SCOPE"))

    def getTransformationComSpecProps(self, element: ET.Element) -> TransformationComSpecProps:
        child = self.find(element, "*")
        if child is None:
            return None
        tag_name = self.getTagName(child)
        if tag_name == "END-TO-END-TRANSFORMATION-COM-SPEC-PROPS":
            props = EndToEndTransformationComSpecProps()
            self.readTransformationComSpecProps(child, props)
            return props
        elif tag_name == "USER-DEFINED-TRANSFORMATION-COM-SPEC-PROPS":
            props = UserDefinedTransformationComSpecProps()
            self.readUserDefinedTransformationComSpecProps(child, props)
            return props
        self.notImplemented("Unsupported TransformationComSpecProps <%s>" % tag_name)
        return None

    def getSwValues(self, element: ET.Element, key: str) -> SwValues:
        child_element = self.find(element, key)
        if child_element is None:
            return None
        sw_values = SwValues()
        self.readARObjectAttributes(child_element, sw_values)
        for v in self.getChildElementFloatValueList(child_element, "V"):
            sw_values.addV(v)
        sw_values.vt = self.getChildElementOptionalLiteral(child_element, "VT")
        return sw_values

    def getValueList(self, element: ET.Element, key: str) -> ValueList:
        value_list = None
        child_element = self.find(element, key)
        if child_element is not None:
            # self.logger.debug("Get ValueList %s" % key)
            value_list = ValueList()
            self.readARObjectAttributes(child_element, value_list)
            value_list.setV(self.getChildElementOptionalFloatValue(child_element, "V"))
        return value_list

    def getSwValueCont(self, element: ET.Element) -> SwValueCont:
        cont = None
        child_element = self.find(element, "SW-VALUE-CONT")
        if child_element is not None:
            # self.logger.debug("Get SwValueCont")
            cont = SwValueCont()
            self.readARObjectAttributes(child_element, cont)
            cont.setUnitRef(self.getChildElementOptionalRefType(child_element, "UNIT-REF"))
            cont.setSwArraysize(self.getValueList(child_element, "SW-ARRAYSIZE"))
            cont.setSwValuesPhys(self.getSwValues(child_element, "SW-VALUES-PHYS"))
        return cont

    def readApplicationValueSpecification(self, element: ET.Element, value_spec: ApplicationValueSpecification):
        self.readValueSpecification(element, value_spec)
        value_spec.setCategory(self.getChildElementOptionalLiteral(element, "CATEGORY"))
        value_spec.setSwValueCont(self.getSwValueCont(element))

        self.logger.debug("readApplicationValueSpecification Category %s" % value_spec.category)

    def getChildValueSpecification(self, element: ET.Element, key: str) -> ValueSpecification:
        value_spec = None
        child_element = self.find(element, key + "/*")
        if child_element is not None:
            value_spec = self.getValueSpecification(child_element, self.getTagName(child_element))
        return value_spec

    def getInitValue(self, element: ET.Element) -> ValueSpecification:
        return self.getChildValueSpecification(element, "INIT-VALUE")

    def readRPortComSpec(self, element: ET.Element, com_spec: RPortComSpec):
        self.readARObjectAttributes(element, com_spec)

    def getClientComSpec(self, element: ET.Element) -> ClientComSpec:
        com_spec = ClientComSpec()
        self.readRPortComSpec(element, com_spec)
        com_spec.setEndToEndCallResponseTimeout(self.getChildElementOptionalTimeValue(element, "END-TO-END-CALL-RESPONSE-TIMEOUT"))
        com_spec.setOperationRef(self.getChildElementOptionalRefType(element, "OPERATION-REF"))
        self.readTransformationComSpecPropss(element, com_spec)
        return com_spec

    def getParameterRequireComSpec(self, element: ET.Element) -> ParameterRequireComSpec:
        com_spec = ParameterRequireComSpec()
        self.readRPortComSpec(element, com_spec)
        com_spec.setInitValue(self.getChildValueSpecification(element, "INIT-VALUE"))
        com_spec.setParameterRef(self.getChildElementOptionalRefType(element, "PARAMETER-REF"))
        return com_spec

    def getNvRequireComSpec(self, element: ET.Element) -> NvRequireComSpec:
        com_spec = NvRequireComSpec()
        self.readRPortComSpec(element, com_spec)
        com_spec.setInitValue(self.getChildValueSpecification(element, "INIT-VALUE"))
        com_spec.setVariableRef(self.getChildElementOptionalRefType(element, "VARIABLE-REF"))
        return com_spec

    def getQueuedReceiverComSpec(self, element: ET.Element) -> QueuedReceiverComSpec:
        com_spec = QueuedReceiverComSpec()
        self.readARObjectAttributes(element, com_spec)
        self.readReceiverComSpec(element, com_spec)
        com_spec.queueLength = self.getChildElementOptionalNumericalValue(element, "QUEUE-LENGTH")
        return com_spec

    def getModeSwitchReceiverComSpec(self, element: ET.Element) -> ModeSwitchReceiverComSpec:
        com_spec = ModeSwitchReceiverComSpec()
        self.readRPortComSpec(element, com_spec)
        com_spec.setEnhancedModeApi(self.getChildElementOptionalBooleanValue(element, "ENHANCED-MODE-API"))
        com_spec.setModeGroupRef(self.getChildElementOptionalRefType(element, "MODE-GROUP-REF"))
        com_spec.setSupportsAsynchronousModeSwitch(self.getChildElementOptionalBooleanValue(element, "SUPPORTS-ASYNCHRONOUS-MODE-SWITCH"))
        return com_spec

    def getNonqueuedReceiverComSpec(self, element: ET.Element) -> NonqueuedReceiverComSpec:
        com_spec = NonqueuedReceiverComSpec()
        self.readARObjectAttributes(element, com_spec)
        self.readReceiverComSpec(element, com_spec)
        com_spec.setAliveTimeout(self.getChildElementOptionalFloatValue(element, "ALIVE-TIMEOUT"))
        com_spec.setEnableUpdate(self.getChildElementOptionalBooleanValue(element, "ENABLE-UPDATE"))
        com_spec.setHandleDataStatus(self.getChildElementOptionalBooleanValue(element, "HANDLE-DATA-STATUS"))
        com_spec.setHandleNeverReceived(self.getChildElementOptionalBooleanValue(element, "HANDLE-NEVER-RECEIVED"))
        com_spec.setFilter(self.getDataFilter(element, "FILTER"))
        com_spec.setHandleTimeoutType(self.getChildElementOptionalLiteral(element, "HANDLE-TIMEOUT-TYPE"))
        com_spec.setInitValue(self.getInitValue(element))
        com_spec.setTimeoutSubstitutionValue(self.getChildValueSpecification(element, "TIMEOUT-SUBSTITUTION-VALUE"))
        return com_spec

    def readRequiredComSpec(self, element: ET.Element, parent: RPortPrototype):
        for child_element in self.findall(element, "REQUIRED-COM-SPECS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "NONQUEUED-RECEIVER-COM-SPEC":
                parent.addRequiredComSpec(self.getNonqueuedReceiverComSpec(child_element))
            elif tag_name == "CLIENT-COM-SPEC":
                parent.addRequiredComSpec(self.getClientComSpec(child_element))
            elif tag_name == "QUEUED-RECEIVER-COM-SPEC":
                parent.addRequiredComSpec(self.getQueuedReceiverComSpec(child_element))
            elif tag_name == "MODE-SWITCH-RECEIVER-COM-SPEC":
                parent.addRequiredComSpec(self.getModeSwitchReceiverComSpec(child_element))
            elif tag_name == "PARAMETER-REQUIRE-COM-SPEC":
                parent.addRequiredComSpec(self.getParameterRequireComSpec(child_element))
            elif tag_name == "NV-REQUIRE-COM-SPEC":
                parent.addRequiredComSpec(self.getNvRequireComSpec(child_element))
            else:
                self.raiseError("Unsupported RequiredComSpec <%s>" % tag_name)

    def readAbstractRequiredPortPrototype(self, element: ET.Element, prototype: AbstractRequiredPortPrototype):
        self.readProvidedComSpec(element, prototype)

    def readPPortPrototype(self, element: ET.Element, prototype: PPortPrototype):
        # self.logger.debug("Read PPortPrototype %s" % prototype.getShortName())
        self.readIdentifiable(element, prototype)
        self.readAbstractRequiredPortPrototype(element, prototype)
        prototype.setProvidedInterfaceTRef(self.getChildElementOptionalRefType(element, "PROVIDED-INTERFACE-TREF"))
        self.readPortPrototype(element, prototype)

    def readAbstractProvidedPortPrototype(self, element: ET.Element, prototype: AbstractProvidedPortPrototype):
        self.readRequiredComSpec(element, prototype)

    def readRPortPrototype(self, element: ET.Element, prototype: RPortPrototype):
        # self.logger.debug("Read RPortPrototype %s" % prototype.getShortName())
        self.readIdentifiable(element, prototype)
        self.readAbstractProvidedPortPrototype(element, prototype)
        prototype.setRequiredInterfaceTRef(self.getChildElementOptionalRefType(element, "REQUIRED-INTERFACE-TREF"))
        self.readPortPrototype(element, prototype)

    def readPRPortPrototype(self, element: ET.Element, prototype: PRPortPrototype):
        # self.logger.debug("Read PRPortPrototype %s" % prototype.getShortName())
        self.readIdentifiable(element, prototype)
        self.readAbstractRequiredPortPrototype(element, prototype)
        self.readAbstractProvidedPortPrototype(element, prototype)
        prototype.setProvidedRequiredInterface(self.getChildElementOptionalRefType(element, "PROVIDED-REQUIRED-INTERFACE-TREF"))
        self.readPortPrototype(element, prototype)

    def readPortPrototype(self, element: ET.Element, prototype: PortPrototype):
        for child in self.findall(element, "CLIENT-SERVER-ANNOTATIONS/CLIENT-SERVER-ANNOTATION"):
            annotation = ClientServerAnnotation()
            annotation.setOperationRef(self.getChildElementOptionalRefType(child, "OPERATION-REF"))
            prototype.addClientServerAnnotation(annotation)
        child = self.find(element, "DELEGATED-PORT-ANNOTATION")
        if child is not None:
            annotation = DelegatedPortAnnotation()
            signal_fan = self.getChildElementOptionalLiteral(child, "SIGNAL-FAN")
            if signal_fan is not None:
                annotation.setSignalFan(SignalFanEnum().setValue(signal_fan.getValue()))
            prototype.setDelegatedPortAnnotation(annotation)
        for child in self.findall(element, "IO-HW-ABSTRACTION-SERVER-ANNOTATIONS/IO-HW-ABSTRACTION-SERVER-ANNOTATION"):
            annotation = IoHwAbstractionServerAnnotation()
            filtering_debouncing = self.getChildElementOptionalLiteral(child, "FILTERING-DEBOUNCING")
            if filtering_debouncing is not None:
                annotation.setFilteringDebouncing(FilterDebouncingEnum().setValue(filtering_debouncing.getValue()))
            pulse_test = self.getChildElementOptionalLiteral(child, "PULSE-TEST")
            if pulse_test is not None:
                annotation.setPulseTest(PulseTestEnum().setValue(pulse_test.getValue()))
            annotation.setTriggerRef(self.getChildElementOptionalRefType(child, "TRIGGER-REF"))
            prototype.addIoHwAbstractionServerAnnotation(annotation)
        for child in self.findall(element, "MODE-PORT-ANNOTATIONS/MODE-PORT-ANNOTATION"):
            annotation = ModePortAnnotation()
            annotation.setModeGroupRef(self.getChildElementOptionalRefType(child, "MODE-GROUP-REF"))
            prototype.addModePortAnnotation(annotation)
        for child in self.findall(element, "NV-DATA-PORT-ANNOTATIONS/NV-DATA-PORT-ANNOTATION"):
            annotation = NvDataPortAnnotation()
            annotation.setVariableRef(self.getChildElementOptionalRefType(child, "VARIABLE-REF"))
            prototype.addNvDataPortAnnotation(annotation)
        for child in self.findall(element, "PARAMETER-PORT-ANNOTATIONS/PARAMETER-PORT-ANNOTATION"):
            annotation = ParameterPortAnnotation()
            annotation.setParameterRef(self.getChildElementOptionalRefType(child, "PARAMETER-REF"))
            prototype.addParameterPortAnnotation(annotation)
        for child in self.findall(element, "SENDER-RECEIVER-ANNOTATIONS/SENDER-RECEIVER-ANNOTATION"):
            annotation = SenderReceiverAnnotation()
            annotation.setComputed(self.getChildElementOptionalBooleanValue(child, "COMPUTED"))
            annotation.setDataElementRef(self.getChildElementOptionalRefType(child, "DATA-ELEMENT-REF"))
            limit_kind = self.getChildElementOptionalLiteral(child, "LIMIT-KIND")
            if limit_kind is not None:
                annotation.setLimitKind(DataLimitKindEnum().setValue(limit_kind.getValue()))
            processing_kind = self.getChildElementOptionalLiteral(child, "PROCESSING-KIND")
            if processing_kind is not None:
                annotation.setProcessingKind(ProcessingKindEnum().setValue(processing_kind.getValue()))
            prototype.addSenderReceiverAnnotation(annotation)
        for child in self.findall(element, "TRIGGER-PORT-ANNOTATIONS/TRIGGER-PORT-ANNOTATION"):
            annotation = TriggerPortAnnotation()
            annotation.setTriggerRef(self.getChildElementOptionalRefType(child, "TRIGGER-REF"))
            prototype.addTriggerPortAnnotation(annotation)

    def readSwComponentTypePorts(self, element: ET.Element, sw_component: SwComponentType):
        for child_element in self.findall(element, "PORTS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "P-PORT-PROTOTYPE":
                prototype = sw_component.createPPortPrototype(self.getShortName(child_element))
                self.readPPortPrototype(child_element, prototype)
            elif tag_name == "R-PORT-PROTOTYPE":
                prototype = sw_component.createRPortPrototype(self.getShortName(child_element))
                self.readRPortPrototype(child_element, prototype)
            elif tag_name == "PR-PORT-PROTOTYPE":
                prototype = sw_component.createPRPortPrototype(self.getShortName(child_element))
                self.readPRPortPrototype(child_element, prototype)
            else:
                self.notImplemented("Unsupported Port Prototype <%s>" % tag_name)

    def readTransmissionAcknowledgementRequest(self, element: ET.Element) -> TransmissionAcknowledgementRequest:
        child_element = self.find(element, "TRANSMISSION-ACKNOWLEDGE")
        if child_element is not None:
            acknowledge = TransmissionAcknowledgementRequest()
            self.readARObjectAttributes(child_element, acknowledge)
            acknowledge.setTimeout(self.getChildElementOptionalTimeValue(child_element, "TIMEOUT"))
            return acknowledge
        return None

    def getTransmissionComSpecProps(self, element: ET.Element, key: str) -> TransmissionComSpecProps:
        child_element = self.find(element, key)
        if child_element is not None:
            props = TransmissionComSpecProps()
            self.readARObjectAttributes(child_element, props)
            props.setDataUpdatePeriod(self.getChildElementOptionalTimeValue(child_element, "DATA-UPDATE-PERIOD"))
            props.setMinimumSendInterval(self.getChildElementOptionalTimeValue(child_element, "MINIMUM-SEND-INTERVAL"))
            props.setTransmissionMode(self.getChildElementOptionalLiteral(child_element, "TRANSMISSION-MODE"))
            return props
        return None

    def readSenderComSpec(self, element: ET.Element, com_spec: SenderComSpec):
        self.readARObjectAttributes(element, com_spec)
        for child_element in self.findall(element, "COMPOSITE-NETWORK-REPRESENTATIONS/COMPOSITE-NETWORK-REPRESENTATION"):
            com_spec.addCompositeNetworkRepresentation(self.getCompositeNetworkRepresentation(child_element))
        com_spec.setDataElementRef(self.getChildElementOptionalRefType(element, "DATA-ELEMENT-REF"))
        com_spec.setHandleOutOfRange(self.getChildElementOptionalLiteral(element, "HANDLE-OUT-OF-RANGE"))
        com_spec.setNetworkRepresentation(self.getSwDataDefProps(element, "NETWORK-REPRESENTATION"))
        com_spec.setTransmissionAcknowledge(self.readTransmissionAcknowledgementRequest(element))
        com_spec.setTransmissionProps(self.getTransmissionComSpecProps(element, "TRANSMISSION-PROPS"))
        com_spec.setUsesEndToEndProtection(self.getChildElementOptionalBooleanValue(element, "USES-END-TO-END-PROTECTION"))

    def getNonqueuedSenderComSpec(self, element: ET.Element) -> NonqueuedSenderComSpec:
        com_spec = NonqueuedSenderComSpec()
        self.readSenderComSpec(element, com_spec)
        com_spec.setDataFilter(self.getDataFilter(element, "DATA-FILTER"))
        com_spec.setInitValue(self.getInitValue(element))
        return com_spec

    def readTransformationComSpecProps(self, element: ET.Element, props: TransformationComSpecProps):
        self.readARObjectAttributes(element, props)

    def readUserDefinedTransformationComSpecProps(self, element: ET.Element, props: UserDefinedTransformationComSpecProps):
        self.readTransformationComSpecProps(element, props)

    def readEndToEndTransformationComSpecProps(self, element: ET.Element, props: EndToEndTransformationComSpecProps):
        self.readTransformationComSpecProps(element, props)
        props.setClearFromValidToInvalid(self.getChildElementOptionalBooleanValue(element, "CLEAR-FROM-VALID-TO-INVALID"))
        props.setDisableEndToEndCheck(self.getChildElementOptionalBooleanValue(element, "DISABLE-END-TO-END-CHECK"))
        props.setDisableEndToEndStateMachine(self.getChildElementOptionalBooleanValue(element, "DISABLE-END-TO-END-STATE-MACHINE"))
        props.setE2eProfileCompatibilityPropsRef(self.getChildElementOptionalRefType(element, "E2E-PROFILE-COMPATIBILITY-PROPS-REF"))
        props.setMaxDeltaCounter(self.getChildElementOptionalPositiveInteger(element, "MAX-DELTA-COUNTER"))
        props.setMaxErrorStateInit(self.getChildElementOptionalPositiveInteger(element, "MAX-ERROR-STATE-INIT"))
        props.setMaxErrorStateInvalid(self.getChildElementOptionalPositiveInteger(element, "MAX-ERROR-STATE-INVALID"))
        props.setMaxErrorStateValid(self.getChildElementOptionalPositiveInteger(element, "MAX-ERROR-STATE-VALID"))
        props.setMaxNoNewOrRepeatedData(self.getChildElementOptionalPositiveInteger(element, "MAX-NO-NEW-OR-REPEATED-DATA"))
        props.setMinOkStateInit(self.getChildElementOptionalPositiveInteger(element, "MIN-OK-STATE-INIT"))
        props.setMinOkStateInvalid(self.getChildElementOptionalPositiveInteger(element, "MIN-OK-STATE-INVALID"))
        props.setMinOkStateValid(self.getChildElementOptionalPositiveInteger(element, "MIN-OK-STATE-VALID"))
        props.setSyncCounterInit(self.getChildElementOptionalPositiveInteger(element, "SYNC-COUNTER-INIT"))
        props.setWindowSizeInit(self.getChildElementOptionalPositiveInteger(element, "WINDOW-SIZE-INIT"))
        props.setWindowSizeInvalid(self.getChildElementOptionalPositiveInteger(element, "WINDOW-SIZE-INVALID"))
        props.setWindowSizeValid(self.getChildElementOptionalPositiveInteger(element, "WINDOW-SIZE-VALID"))

    def readTransformationComSpecPropss(self, element: ET.Element, com_spec):
        for child_element in self.findall(element, "TRANSFORMATION-COM-SPEC-PROPSS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "END-TO-END-TRANSFORMATION-COM-SPEC-PROPS":
                props = EndToEndTransformationComSpecProps()
                self.readEndToEndTransformationComSpecProps(child_element, props)
                com_spec.addTransformationComSpecProps(props)
            elif tag_name == "USER-DEFINED-TRANSFORMATION-COM-SPEC-PROPS":
                props = UserDefinedTransformationComSpecProps()
                self.readUserDefinedTransformationComSpecProps(child_element, props)
                com_spec.addTransformationComSpecProps(props)
            else:
                self.notImplemented("Unsupported TransformationComSpecProps <%s>" % tag_name)

    def readPPortComSpec(self, element: ET.Element, com_spec: PPortComSpec):
        self.readARObjectAttributes(element, com_spec)

    def getServerComSpec(self, element: ET.Element) -> ServerComSpec:
        com_spec = ServerComSpec()
        self.readPPortComSpec(element, com_spec)
        com_spec.setOperationRef(self.getChildElementOptionalRefType(element, "OPERATION-REF"))
        com_spec.setQueueLength(self.getChildElementOptionalPositiveInteger(element, "QUEUE-LENGTH"))
        self.readTransformationComSpecPropss(element, com_spec)
        return com_spec

    def getParameterProvideComSpec(self, element: ET.Element) -> ParameterProvideComSpec:
        com_spec = ParameterProvideComSpec()
        self.readPPortComSpec(element, com_spec)
        com_spec.setInitValue(self.getInitValue(element))
        com_spec.setParameterRef(self.getChildElementOptionalRefType(element, "PARAMETER-REF"))
        return com_spec

    def getQueuedSenderComSpec(self, element: ET.Element) -> QueuedSenderComSpec:
        com_spec = QueuedSenderComSpec()
        self.readSenderComSpec(element, com_spec)
        return com_spec

    def getModeSwitchedAckRequest(self, element: ET.Element, key: str) -> ModeSwitchedAckRequest:
        request = None
        child_element = self.find(element, key)
        if child_element is not None:
            request = ModeSwitchedAckRequest()
            request.setTimeout(self.getChildElementOptionalTimeValue(child_element, "TIMEOUT"))
        return request

    def getModeSwitchSenderComSpec(self, element) -> ModeSwitchSenderComSpec:
        com_spec = ModeSwitchSenderComSpec()
        com_spec.setModeGroupRef(self.getChildElementOptionalRefType(element, "MODE-GROUP-REF"))
        com_spec.setModeSwitchedAck(self.getModeSwitchedAckRequest(element, "MODE-SWITCHED-ACK"))
        com_spec.setQueueLength(self.getChildElementOptionalNumericalValue(element, "QUEUE-LENGTH"))
        return com_spec

    def getNvProvideComSpec(self, element: ET.Element) -> NvProvideComSpec:
        com_spec = NvProvideComSpec()
        self.readPPortComSpec(element, com_spec)
        com_spec.setRamBlockInitValue(self.getChildValueSpecification(element, "RAM-BLOCK-INIT-VALUE"))
        com_spec.setRomBlockInitValue(self.getChildValueSpecification(element, "ROM-BLOCK-INIT-VALUE"))
        com_spec.setVariableRef(self.getChildElementOptionalRefType(element, "VARIABLE-REF"))
        return com_spec

    def readProvidedComSpec(self, element: ET.Element, parent: PPortPrototype):
        for child_element in self.findall(element, "PROVIDED-COM-SPECS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "NONQUEUED-SENDER-COM-SPEC":
                parent.addProvidedComSpec(self.getNonqueuedSenderComSpec(child_element))
            elif tag_name == "SERVER-COM-SPEC":
                parent.addProvidedComSpec(self.getServerComSpec(child_element))
            elif tag_name == "QUEUED-SENDER-COM-SPEC":
                parent.addProvidedComSpec(self.getQueuedSenderComSpec(child_element))
            elif tag_name == "MODE-SWITCH-SENDER-COM-SPEC":
                parent.addProvidedComSpec(self.getModeSwitchSenderComSpec(child_element))
            elif tag_name == "NV-PROVIDE-COM-SPEC":
                parent.addProvidedComSpec(self.getNvProvideComSpec(child_element))
            elif tag_name == "PARAMETER-PROVIDE-COM-SPEC":
                parent.addProvidedComSpec(self.getParameterProvideComSpec(child_element))
            else:
                self.raiseError("Unsupported RequiredComSpec <%s>" % tag_name)

    def readPortGroupInnerGroupIRefs(self, element: ET.Element, parent: PortGroup):
        for child_element in self.findall(element, "INNER-GROUP-IREFS/INNER-GROUP-IREF"):
            inner_group_iref = InnerPortGroupInCompositionInstanceRef()
            # inner_group_iref.contextRef = self.getChildElementOptionalRefType(child_element, "CONTEXT-REF")
            inner_group_iref.setTargetRef(self.getChildElementOptionalRefType(child_element, "TARGET-REF"))
            parent.addInnerGroupIRef(inner_group_iref)

    def readPortGroupOuterPortRefs(self, element: ET.Element, parent: PortGroup):
        for child_element in self.findall(element, "OUTER-PORTS/PORT-PROTOTYPE-REF-CONDITIONAL"):
            parent.addOuterPortRef(self.getChildElementOptionalRefType(child_element, "PORT-PROTOTYPE-REF"))

    def readPortGroup(self, element: ET.Element, parent: SwComponentType):
        short_name = self.getShortName(element)
        self.logger.debug("readPortGroup %s" % short_name)
        port_group = parent.createPortGroup(short_name)
        self.readIdentifiable(element, port_group)
        self.readPortGroupInnerGroupIRefs(element, port_group)
        self.readPortGroupOuterPortRefs(element, port_group)

    def readSwComponentTypePortGroups(self, element: ET.Element, parent: SwComponentType):
        for child_element in self.findall(element, "PORT-GROUPS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "PORT-GROUP":
                self.readPortGroup(child_element, parent)
            else:
                self.raiseError("Unsupported Port Group type: %s" % tag_name)

    def readSwComponentTypeSwcMappingConstraints(self, element: ET.Element, parent: SwComponentType):
        for ref in self.getChildElementRefTypeList(element, "SWC-MAPPING-CONSTRAINT-REFS/SWC-MAPPING-CONSTRAINT-REF"):
            parent.addSwcMappingConstraintRef(ref)

    def readSwComponentTypeUnitGroups(self, element: ET.Element, parent: SwComponentType):
        for ref in self.getChildElementRefTypeList(element, "UNIT-GROUP-REFS/UNIT-GROUP-REF"):
            parent.addUnitGroupRef(ref)

    def readSwComponentTypeConsistencyNeeds(self, element: ET.Element, parent: SwComponentType):
        for child_element in self.findall(element, "CONSISTENCY-NEEDSS/CONSISTENCY-NEEDS"):
            self.readConsistencyNeeds(child_element, parent.createConsistencyNeeds(self.getShortName(child_element)))

    def readSwComponentDocumentationElement(self, child_element: ET.Element) -> SwComponentDocumentation:
        documentation = SwComponentDocumentation()
        predefined_chapter_map = [
            ("SW-FEATURE-DEF", documentation.createSwFeatureDef),
            ("SW-FEATURE-DESC", documentation.createSwFeatureDesc),
            ("SW-TEST-DESC", documentation.createSwTestDesc),
            ("SW-CALIBRATION-NOTES", documentation.createSwCalibrationNotes),
            ("SW-MAINTENANCE-NOTES", documentation.createSwMaintenanceNotes),
            ("SW-DIAGNOSTICS-NOTES", documentation.createSwDiagnosticsNotes),
            ("SW-CARB-DOC", documentation.createSwCarbDoc),
        ]
        for tag_name, creator in predefined_chapter_map:
            chapter_element = self.find(child_element, tag_name)
            if chapter_element is not None:
                chapter = creator(self.getShortName(chapter_element))
                self.readChapterBody(chapter_element, chapter)
        for chapter_element in self.findall(child_element, "CHAPTER"):
            chapter = documentation.createChapter(self.getShortName(chapter_element))
            self.readChapterBody(chapter_element, chapter)
        return documentation

    def readSwComponentTypeSwComponentDocumentation(self, element: ET.Element, parent: SwComponentType):
        child_element = self.find(element, "SW-COMPONENT-DOCUMENTATION")
        if child_element is None:
            return
        parent.setSwComponentDocumentation(self.readSwComponentDocumentationElement(child_element))

    def readChapter(self, element: ET.Element, parent: ARObject) -> Chapter:
        chapter = Chapter(parent, self.getShortName(element))
        self.readChapterBody(element, chapter)
        return chapter

    def readChapterBody(self, element: ET.Element, chapter: Chapter):
        self.readIdentifiable(element, chapter)
        help_entry = element.get("HELP-ENTRY")
        if help_entry is not None:
            chapter.setHelpEntry(String().setValue(help_entry))
        chapter_model_element = self.find(element, "CHAPTER-MODEL")
        if chapter_model_element is not None:
            chapter.setChapterModel(self.readChapterModel(chapter_model_element, chapter))

    def readChapterModel(self, element: ET.Element, parent: Chapter) -> ChapterModel:
        chapter_model = ChapterModel()
        chapter_content_element = self.find(element, "CHAPTER-CONTENT")
        if chapter_content_element is not None:
            chapter_model.setChapterContent(self.readChapterContent(chapter_content_element, parent))
        topic_elements = self.findall(element, "TOPIC-1")
        msr_query_topic1_element = self.find(element, "MSR-QUERY-TOPIC-1")
        if len(topic_elements) > 0 or msr_query_topic1_element is not None:
            topic_or_msr_query = TopicOrMsrQuery()
            for topic_element in topic_elements:
                topic_or_msr_query.addTopic1(self.readTopic1(topic_element, parent))
            if msr_query_topic1_element is not None:
                topic_or_msr_query.setMsrQueryTopic1(self.readMsrQueryTopic1(msr_query_topic1_element, parent))
            chapter_model.setTopic1(topic_or_msr_query)
        chapter_elements = self.findall(element, "CHAPTER")
        msr_query_chapter_element = self.find(element, "MSR-QUERY-CHAPTER")
        if len(chapter_elements) > 0 or msr_query_chapter_element is not None:
            chapter_or_msr_query = ChapterOrMsrQuery()
            for chapter_element in chapter_elements:
                chapter_or_msr_query.addChapter(self.readChapter(chapter_element, parent))
            if msr_query_chapter_element is not None:
                chapter_or_msr_query.setMsrQueryChapter(self.readMsrQueryChapter(msr_query_chapter_element, parent))
            chapter_model.setChapter(chapter_or_msr_query)
        return chapter_model

    def readPredefinedChapter(self, element: ET.Element) -> PredefinedChapter:
        predefined = PredefinedChapter()
        chapter_model_element = self.find(element, "CHAPTER-MODEL")
        if chapter_model_element is not None:
            predefined.setChapterModel(self.readChapterModel(chapter_model_element, None))
        return predefined

    def readDocumentationContext(self, element: ET.Element, parent: ARObject) -> DocumentationContext:
        context = DocumentationContext(parent, self.getShortName(element))
        self.readMultilanguageReferrable(element, context)
        context.setFeatureIRef(self.getAnyInstanceRef(element, "FEATURE-IREF"))
        context.setIdentifiableRef(self.getChildElementOptionalRefType(element, "IDENTIFIABLE-REF"))
        return context

    def readDocumentation(self, element: ET.Element, documentation: Documentation):
        self.readARElement(element, documentation)
        for context_element in self.findall(element, "CONTEXTS/DOCUMENTATION-CONTEXT"):
            documentation.addContext(self.readDocumentationContext(context_element, documentation))
        documentation_content_element = self.find(element, "DOCUMENTATION-CONTENT")
        if documentation_content_element is not None:
            documentation.setDocumentationContent(self.readPredefinedChapter(documentation_content_element))
        return documentation

    def readChapterContent(self, element: ET.Element, parent: Chapter) -> ChapterContent:
        chapter_content = ChapterContent()
        topic_content_or_msr_query = self.readTopicContentOrMsrQuery(element, chapter_content)
        if topic_content_or_msr_query is not None:
            chapter_content.setTopicContent(topic_content_or_msr_query)
        return chapter_content

    def readTopicContentOrMsrQuery(self, element: ET.Element, parent: ARObject) -> "TopicContentOrMsrQuery":
        result = None
        msr_query_p1_element = self.find(element, "MSR-QUERY-P1")
        topic_content_element = self.find(element, "TOPIC-CONTENT")
        if msr_query_p1_element is not None or topic_content_element is not None:
            result = TopicContentOrMsrQuery()
            if msr_query_p1_element is not None:
                result.setMsrQueryP1(self.readMsrQueryP1(msr_query_p1_element, parent))
            if topic_content_element is not None:
                result.setTopicContent(self.readTopicContent(topic_content_element, parent))
        return result

    def readMsrQueryP1(self, element: ET.Element, parent: ARObject) -> MsrQueryP1:
        return MsrQueryP1()

    def readTopicContent(self, element: ET.Element, parent: ARObject) -> TopicContent:
        topic_content = TopicContent()
        self.readARObjectAttributes(element, topic_content)
        block_level_content = self.getDocumentationBlock(element, "DOCUMENTATION-BLOCK")
        if block_level_content is not None:
            topic_content.setBlockLevelContent(block_level_content)
        return topic_content

    def readTopic1(self, element: ET.Element, parent: Chapter) -> Topic1:
        topic1 = Topic1(parent, self.getShortName(element))
        self.readIdentifiable(element, topic1)
        help_entry = element.get("HELP-ENTRY")
        if help_entry is not None:
            topic1.setHelpEntry(String().setValue(help_entry))
        topic_content_or_msr_query = self.readTopicContentOrMsrQuery(element, topic1)
        if topic_content_or_msr_query is not None:
            topic1.setTopicContent(topic_content_or_msr_query)
        return topic1

    def readMsrQueryTopic1(self, element: ET.Element, parent: Chapter) -> MsrQueryTopic1:
        msr_query_topic1 = MsrQueryTopic1()
        self.readARObjectAttributes(element, msr_query_topic1)
        msr_query_props = self.find(element, "MSR-QUERY-PROPS")
        if msr_query_props is not None:
            msr_query_topic1.setMsrQueryProps(self.getMsrQueryProps(msr_query_props))
        return msr_query_topic1

    def readMsrQueryChapter(self, element: ET.Element, parent: Chapter) -> MsrQueryChapter:
        msr_query_chapter = MsrQueryChapter()
        self.readARObjectAttributes(element, msr_query_chapter)
        msr_query_props = self.find(element, "MSR-QUERY-PROPS")
        if msr_query_props is not None:
            msr_query_chapter.setMsrQueryProps(self.getMsrQueryProps(msr_query_props))
        return msr_query_chapter

    def readSwComponentType(self, element: ET.Element, parent: SwComponentType):
        self.readIdentifiable(element, parent)
        self.readSwComponentTypeSwComponentDocumentation(element, parent)
        self.readSwComponentTypeConsistencyNeeds(element, parent)
        self.readSwComponentTypePorts(element, parent)
        self.readSwComponentTypePortGroups(element, parent)
        self.readSwComponentTypeSwcMappingConstraints(element, parent)
        self.readSwComponentTypeUnitGroups(element, parent)

    def readAtomicSwComponentTypeSymbolProps(self, element: ET.Element, sw_component: AtomicSwComponentType):
        child_element = self.find(element, "SYMBOL-PROPS")
        if child_element is not None:
            props = sw_component.createSymbolProps(self.getShortName(child_element))
            self.readSymbolProps(child_element, props)

    def readAtomicSwComponentType(self, element, parent: AtomicSwComponentType):
        self.readSwComponentType(element, parent)
        self.readAtomicSwComponentTypeSwcInternalBehavior(element, parent)
        self.readAtomicSwComponentTypeSymbolProps(element, parent)

    def readEcuAbstractionSwComponentType(self, element, sw_component: EcuAbstractionSwComponentType):
        self.logger.debug("Read EcuAbstractionSwComponentType <%s>" % sw_component.getShortName())
        self.readAtomicSwComponentType(element, sw_component)
        self.readEcuAbstractionSwComponentTypeHardwareElementRefs(element, sw_component)

    def readEcuAbstractionSwComponentTypeHardwareElementRefs(self, element, sw_component: EcuAbstractionSwComponentType):
        for ref in self.getChildElementRefTypeList(element, "HARDWARE-ELEMENT-REFS/HARDWARE-ELEMENT-REF"):
            sw_component.addHardwareElementRef(ref)

    def readApplicationSwComponentType(self, element: ET.Element, sw_component: ApplicationSwComponentType):
        self.logger.debug("Read ApplicationSwComponentType <%s>" % sw_component.getShortName())
        self.readAtomicSwComponentType(element, sw_component)

    def readComplexDeviceDriverSwComponentType(self, element: ET.Element, type: ComplexDeviceDriverSwComponentType):
        self.logger.debug("Read ComplexDeviceDriverSwComponentType <%s>" % type.getShortName())
        self.readAtomicSwComponentType(element, type)
        for ref in self.getChildElementRefTypeList(element, "HARDWARE-ELEMENT-REFS/HARDWARE-ELEMENT-REF"):
            type.addHardwareElementRef(ref)

    def readSensorActuatorSwComponentType(self, element: ET.Element, sw_component: SensorActuatorSwComponentType):
        self.logger.debug("Read SensorActuatorSwComponentType <%s>" % sw_component.getShortName())
        self.readAtomicSwComponentType(element, sw_component)
        sw_component.setSensorActuatorRef(self.getChildElementOptionalRefType(element, "SENSOR-ACTUATOR-REF"))

    def readServiceSwComponentType(self, element: ET.Element, sw_component: ServiceSwComponentType):
        self.logger.debug("Read ServiceSwComponentType <%s>" % sw_component.getShortName())
        self.readAtomicSwComponentType(element, sw_component)

    def readServiceProxySwComponentType(self, element: ET.Element, sw_component: ServiceProxySwComponentType):
        self.logger.debug("Read ServiceProxySwComponentType <%s>" % sw_component.getShortName())
        self.readAtomicSwComponentType(element, sw_component)

    def readNvBlockSwComponentType(self, element: ET.Element, sw_component: NvBlockSwComponentType):
        self.logger.debug("Read NvBlockSwComponentType <%s>" % sw_component.getShortName())
        self.readAtomicSwComponentType(element, sw_component)
        for child_element in self.findall(element, "BULK-NV-DATA-DESCRIPTORS/BULK-NV-DATA-DESCRIPTOR"):
            descriptor = sw_component.createBulkNvDataDescriptor(self.getShortName(child_element))
            self.readBulkNvDataDescriptor(child_element, descriptor)
        for child_element in self.findall(element, "NV-BLOCK-DESCRIPTORS/NV-BLOCK-DESCRIPTOR"):
            descriptor = sw_component.createNvBlockDescriptor(self.getShortName(child_element))
            self.readNvBlockDescriptor(child_element, descriptor)

    def readPPortInCompositionInstanceRef(self, element: ET.Element, p_port_in_composition_instance_ref: PPortInCompositionInstanceRef):
        p_port_in_composition_instance_ref.setContextComponentRef(self.getChildElementOptionalRefType(element, "CONTEXT-COMPONENT-REF"))
        p_port_in_composition_instance_ref.setTargetPPortRef(self.getChildElementOptionalRefType(element, "TARGET-P-PORT-REF"))

        """
        self.logger.debug("PPortInCompositionInstanceRef")
        self.logger.debug("  CONTEXT-COMPONENT-REF DEST: %s, %s"
                          % (p_port_in_composition_instance_ref.getContextComponentRef().getDest(),
                             p_port_in_composition_instance_ref.getContextComponentRef().getValue()))
        self.logger.debug("  TARGET-P-PORT-REF DEST: %s, %s"
                          % (p_port_in_composition_instance_ref.getTargetPPortRef().getDest(),
                             p_port_in_composition_instance_ref.getTargetPPortRef().getValue()))
        """

    def readRPortInCompositionInstanceRef(self, element, r_port_in_composition_instance_ref: RPortInCompositionInstanceRef):
        r_port_in_composition_instance_ref.setContextComponentRef(self.getChildElementOptionalRefType(element, "CONTEXT-COMPONENT-REF"))
        r_port_in_composition_instance_ref.setTargetRPortRef(self.getChildElementOptionalRefType(element, "TARGET-R-PORT-REF"))

        """
        self.logger.debug("RPortInCompositionInstanceRef")
        self.logger.debug("  CONTEXT-COMPONENT-REF DEST: %s, %s"
                          % (r_port_in_composition_instance_ref.getContextComponentRef().getDest(),
                             r_port_in_composition_instance_ref.getContextComponentRef().getValue()))
        self.logger.debug("  TARGET-P-PORT-REF DEST: %s, %s"
                          % (r_port_in_composition_instance_ref.getTargetRPortRef().getDest(),
                             r_port_in_composition_instance_ref.getTargetRPortRef().getValue()))
        """

    def readAssemblySwConnectorProviderIRef(self, element: ET.Element, parent: AssemblySwConnector):
        child_element = self.find(element, "PROVIDER-IREF")
        if child_element is not None:
            provide_iref = PPortInCompositionInstanceRef()
            self.readARObjectAttributes(child_element, provide_iref)
            self.readPPortInCompositionInstanceRef(child_element, provide_iref)
            parent.setProviderIRef(provide_iref)

    def readAssemblySwConnectorRequesterIRef(self, element: ET.Element, parent: AssemblySwConnector):
        child_element = self.find(element, "REQUESTER-IREF")
        if child_element is not None:
            requester_iref = RPortInCompositionInstanceRef()
            self.readARObjectAttributes(child_element, requester_iref)
            self.readRPortInCompositionInstanceRef(child_element, requester_iref)
            parent.setRequesterIRef(requester_iref)

    def readSwConnector(self, element: ET.Element, connector: SwConnector):
        self.readIdentifiable(element, connector)
        connector.setMappingRef(self.getChildElementOptionalRefType(element, "MAPPING-REF"))

    def readAssemblySwConnector(self, element: ET.Element, connector: AssemblySwConnector):
        # self.logger.debug("Read AssemblySwConnectors %s" % connector.getShortName())
        self.readSwConnector(element, connector)
        self.readAssemblySwConnectorProviderIRef(element, connector)
        self.readAssemblySwConnectorRequesterIRef(element, connector)

    def readCompositionSwComponentTypeSwConnectors(self, element: ET.Element, parent: CompositionSwComponentType):
        for child_element in self.findall(element, "CONNECTORS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "ASSEMBLY-SW-CONNECTOR":
                connector = parent.createAssemblySwConnector(self.getShortName(child_element))
                self.readAssemblySwConnector(child_element, connector)
            elif tag_name == "DELEGATION-SW-CONNECTOR":
                connector = parent.createDelegationSwConnector(self.getShortName(child_element))
                self.readDelegationSwConnector(child_element, connector)
            elif tag_name == "PASS-THROUGH-SW-CONNECTOR":
                connector = parent.createPassThroughSwConnector(self.getShortName(child_element))
                self.readPassThroughSwConnector(child_element, connector)
            else:
                self.notImplemented("Unsupported SwConnector <%s>" % tag_name)

    def readPassThroughSwConnector(self, element: ET.Element, connector: PassThroughSwConnector):
        self.readSwConnector(element, connector)
        connector.setProvidedOuterPortRef(self.getChildElementOptionalRefType(element, "PROVIDED-OUTER-PORT-REF"))
        connector.setRequiredOuterPortRef(self.getChildElementOptionalRefType(element, "REQUIRED-OUTER-PORT-REF"))

    def readDelegationSwConnectorInnerPortIRef(self, element, parent: DelegationSwConnector):
        inner_port_iref_element = self.find(element, "INNER-PORT-IREF")
        if inner_port_iref_element is not None:
            child_element = self.find(inner_port_iref_element, "R-PORT-IN-COMPOSITION-INSTANCE-REF")
            if child_element is not None:
                r_port_in_composition_instance_ref = RPortInCompositionInstanceRef()
                self.readRPortInCompositionInstanceRef(child_element, r_port_in_composition_instance_ref)
                parent.setInnerPortIRref(r_port_in_composition_instance_ref)
                return

            child_element = self.find(inner_port_iref_element, "P-PORT-IN-COMPOSITION-INSTANCE-REF")
            if child_element is not None:
                p_port_in_composition_instance_ref = PPortInCompositionInstanceRef()
                self.readPPortInCompositionInstanceRef(child_element, p_port_in_composition_instance_ref)
                parent.setInnerPortIRref(p_port_in_composition_instance_ref)
                return

            self.raiseError("Unsupported child element of INNER-PORT-IREF")

    def readDelegationSwConnector(self, element, connector: DelegationSwConnector):
        # self.logger.debug("Read DelegationSwConnectors %s" % connector.getShortName())
        self.readSwConnector(element, connector)
        self.readDelegationSwConnectorInnerPortIRef(element, connector)

        if connector.getInnerPortIRref() is None and connector.getOuterPortRef() is None:
            self.raiseError("Invalid PortPrototype of DELEGATION-SW-CONNECTOR")

        connector.setOuterPortRef(self.getChildElementOptionalRefType(element, "OUTER-PORT-REF"))
        # self.logger.debug("OUTER-PORT-REF DEST: %s, %s" % (connector.getOuterPortRef().getDest(), connector.getOuterPortRef().getValue()))

    def readSwComponentPrototype(self, element: ET.Element, prototype: SwComponentPrototype):
        self.logger.debug("Read SwComponentPrototypes <%s>" % prototype.getShortName())
        self.readIdentifiable(element, prototype)
        prototype.setTypeTRef(self.getChildElementOptionalRefType(element, "TYPE-TREF"))

    def readCompositionSwComponentTypeComponents(self, element: ET.Element, parent: CompositionSwComponentType):
        for child_element in self.findall(element, "COMPONENTS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "SW-COMPONENT-PROTOTYPE":
                prototype = parent.createSwComponentPrototype(self.getShortName(child_element))
                self.readSwComponentPrototype(child_element, prototype)
            else:
                self.notImplemented("Unsupported Component <%s>" % tag_name)

    def readCompositionSwComponentTypeDataTypeMappingSet(self, element: ET.Element, parent: CompositionSwComponentType):
        child_element = self.find(element, "DATA-TYPE-MAPPING-REFS")
        if child_element is not None:
            for ref in self.getChildElementRefTypeList(child_element, "DATA-TYPE-MAPPING-REF"):
                parent.addDataTypeMappingRef(ref)

    def readCompositionSwComponentTypeConstantValueMappingSet(self, element: ET.Element, parent: CompositionSwComponentType):
        child_element = self.find(element, "CONSTANT-VALUE-MAPPING-REFS")
        if child_element is not None:
            for ref in self.getChildElementRefTypeList(child_element, "CONSTANT-VALUE-MAPPING-REF"):
                parent.addConstantValueMappingRef(ref)

    def readInstanceEventInCompositionInstanceRef(self, element: ET.Element, instance_ref: InstanceEventInCompositionInstanceRef):
        for ref in self.getChildElementRefTypeList(element, "CONTEXT-COMPONENT-PROTOTYPE-REF"):
            instance_ref.addContextComponentPrototypeRef(ref)
        instance_ref.setTargetEventRef(self.getChildElementOptionalRefType(element, "TARGET-EVENT-REF"))

    def readInstantiationRTEEventProps(self, element: ET.Element, props: InstantiationTimingEventProps):
        refined_event_element = self.find(element, "REFINED-EVENT-IREF")
        if refined_event_element is not None:
            refined_event = InstanceEventInCompositionInstanceRef()
            self.readARObjectAttributes(refined_event_element, refined_event)
            self.readInstanceEventInCompositionInstanceRef(refined_event_element, refined_event)
            props.setRefinedEventIRef(refined_event)
        props.setShortLabel(self.getChildElementOptionalLiteral(element, "SHORT-LABEL"))

    def readInstantiationTimingEventProps(self, element: ET.Element, props: InstantiationTimingEventProps):
        self.readInstantiationRTEEventProps(element, props)
        props.setPeriod(self.getChildElementOptionalTimeValue(element, "PERIOD"))

    def readCompositionSwComponentTypeInstantiationRTEEventProps(self, element: ET.Element, parent: CompositionSwComponentType):
        child_element = self.find(element, "INSTANTIATION-RTE-EVENT-PROPSS")
        if child_element is not None:
            for props_element in self.findall(child_element, "INSTANTIATION-TIMING-EVENT-PROPS"):
                props = InstantiationTimingEventProps()
                self.readARObjectAttributes(props_element, props)
                self.readInstantiationTimingEventProps(props_element, props)
                parent.addInstantiationRTEEventProps(props)

    def readCompositionSwComponentType(self, element: ET.Element, type: CompositionSwComponentType):
        self.logger.debug("Read CompositionSwComponentType: <%s>" % type.getShortName())
        self.readSwComponentType(element, type)
        self.readCompositionSwComponentTypeComponents(element, type)
        self.readCompositionSwComponentTypeSwConnectors(element, type)
        self.readCompositionSwComponentTypeDataTypeMappingSet(element, type)
        self.readCompositionSwComponentTypeConstantValueMappingSet(element, type)
        self.readCompositionSwComponentTypeInstantiationRTEEventProps(element, type)
        document = AUTOSAR.getInstance()
        document.addCompositionSwComponentType(type)

    def readDataTypeMaps(self, element: ET.Element, parent: DataTypeMappingSet):
        for child_element in element.findall("./xmlns:DATA-TYPE-MAPS/xmlns:DATA-TYPE-MAP", self.nsmap):
            data_type_map = DataTypeMap()
            self.readARObjectAttributes(child_element, data_type_map)
            data_type_map.applicationDataTypeRef = self.getChildElementOptionalRefType(child_element, "APPLICATION-DATA-TYPE-REF")
            data_type_map.implementationDataTypeRef = self.getChildElementOptionalRefType(child_element, "IMPLEMENTATION-DATA-TYPE-REF")
            parent.addDataTypeMap(data_type_map)
            # add the data type map to global namespace
            document = AUTOSAR.getInstance()
            document.addDataTypeMap(data_type_map)

    def readModeRequestTypeMaps(self, element: ET.Element, parent: DataTypeMappingSet):
        for child_element in element.findall("./xmlns:MODE-REQUEST-TYPE-MAPS/xmlns:MODE-REQUEST-TYPE-MAP", self.nsmap):
            map = ModeRequestTypeMap()
            self.readARObjectAttributes(child_element, map)
            map.implementationDataTypeRef = self.getChildElementOptionalRefType(child_element, "IMPLEMENTATION-DATA-TYPE-REF")
            map.modeGroupRef = self.getChildElementOptionalRefType(child_element, "MODE-GROUP-REF")
            parent.addModeRequestTypeMap(map)

    def readDataTypeMappingSet(self, element: ET.Element, mapping_set: DataTypeMappingSet):
        self.logger.debug("Read DataTypeMappingSet: <%s>" % mapping_set.getShortName())
        self.readIdentifiable(element, mapping_set)
        self.readDataTypeMaps(element, mapping_set)
        self.readModeRequestTypeMaps(element, mapping_set)

    def readSenderReceiverInterfaceDataElements(self, element: ET.Element, sr_interface: SenderReceiverInterface):
        for child_element in self.findall(element, "DATA-ELEMENTS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "VARIABLE-DATA-PROTOTYPE":
                prototype = sr_interface.createDataElement(self.getShortName(child_element))
                self.readVariableDataPrototype(child_element, prototype)
                # prototype.swDataDefProps = self.getSwDataDefProps(child_element, "SW-DATA-DEF-PROPS")
                # self.readAutosarDataPrototype(child_element, prototype)
            else:
                self.notImplemented("Unsupported Data Element <%s>" % tag_name)

    def readSenderReceiverInterfaceInvalidationPolicies(self, element: ET.Element, sr_interface: SenderReceiverInterface):
        for child_element in self.findall(element, "INVALIDATION-POLICYS/INVALIDATION-POLICY"):
            policy = InvalidationPolicy()
            policy.setDataElementRef(self.getChildElementOptionalRefType(child_element, "DATA-ELEMENT-REF"))
            policy.setHandleInvalid(self.getChildElementOptionalLiteral(child_element, "HANDLE-INVALID"))
            sr_interface.addInvalidationPolicy(policy)

    def readInvalidationPolicys(self, element: ET.Element, parent: SenderReceiverInterface):
        for child_element in self.findall(element, "INVALIDATION-POLICYS/INVALIDATION-POLICY"):
            # short_name = self.getShortName(child_element)
            policy = parent.createInvalidationPolicy()
            self.readIdentifiable(child_element, policy)
            policy.data_element_ref = self.getChildElementOptionalRefType(child_element, "DATA-ELEMENT-REF")
            policy.handle_invalid = self.getChildElementOptionalLiteral(child_element, "HANDLE-INVALID")

    def readSenderReceiverInterface(self, element, sr_interface: SenderReceiverInterface):
        self.logger.debug("Read SenderReceiverInterface <%s>" % sr_interface.getShortName())
        self.readIdentifiable(element, sr_interface)
        sr_interface.setIsService(self.getChildElementOptionalBooleanValue(element, "IS-SERVICE"))
        self.readSenderReceiverInterfaceDataElements(element, sr_interface)
        self.readSenderReceiverInterfaceInvalidationPolicies(element, sr_interface)

    def readArgumentDataPrototype(self, element: ET.Element, prototype: ArgumentDataPrototype):
        self.readAutosarDataPrototype(element, prototype)
        prototype.setDirection(self.getChildElementOptionalLiteral(element, "DIRECTION"))
        prototype.setServerArgumentImplPolicy(self.getChildElementOptionalLiteral(element, "SERVER-ARGUMENT-IMPL-POLICY"))

    def readClientServerOperationArguments(self, element: ET.Element, operation: ClientServerOperation):
        for child_element in self.findall(element, "ARGUMENTS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "ARGUMENT-DATA-PROTOTYPE":
                prototype = operation.createArgumentDataPrototype(self.getShortName(child_element))
                self.readArgumentDataPrototype(child_element, prototype)
            else:
                self.notImplemented("Unsupported Argument <%s>" % tag_name)

    def readPossibleErrorRefs(self, element: ET.Element, parent: ClientServerOperation):
        child_element = self.find(element, "POSSIBLE-ERROR-REFS")
        if child_element is not None:
            for ref in self.getChildElementRefTypeList(child_element, "POSSIBLE-ERROR-REF"):
                parent.addPossibleErrorRef(ref)

    def readClientServerOperation(self, element: ET.Element, operation: ClientServerOperation):
        self.readIdentifiable(element, operation)
        self.readClientServerOperationArguments(element, operation)
        operation.setDiagArgIntegrity(self.getChildElementOptionalBooleanValue(element, "DIAG-ARG-INTEGRITY"))
        self.readPossibleErrorRefs(element, operation)

    def readClientServerInterfaceOperations(self, element: ET.Element, parent: ClientServerInterface):
        for child_element in self.findall(element, "OPERATIONS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "CLIENT-SERVER-OPERATION":
                operation = parent.createOperation(self.getShortName(child_element))
                self.readClientServerOperation(child_element, operation)
            else:
                self.notImplemented("Unsupported Operation <%s>" % tag_name)

    def readPossibleErrors(self, element: ET.Element, parent: ClientServerInterface):
        for child_element in self.findall(element, "POSSIBLE-ERRORS/APPLICATION-ERROR"):
            short_name = self.getShortName(child_element)
            error = parent.createApplicationError(short_name)
            self.readIdentifiable(child_element, error)  # some errors has its uuid
            error.setErrorCode(self.getChildElementOptionalIntegerValue(child_element, "ERROR-CODE"))

    def readPortInterface(self, element: ET.Element, port_interface: PortInterface):
        self.readIdentifiable(element, port_interface)
        port_interface.setIsService(self.getChildElementOptionalBooleanValue(element, "IS-SERVICE"))
        port_interface.setServiceKind(self.getChildElementOptionalLiteral(element, "SERVICE-KIND"))

    def readParameterInterfaceParameters(self, element: ET.Element, param_interface: ParameterInterface):
        for child_element in self.findall(element, "PARAMETERS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "PARAMETER-DATA-PROTOTYPE":
                prototype = param_interface.createParameterDataPrototype(self.getShortName(child_element))
                self.readParameterDataPrototype(child_element, prototype)
            else:
                self.notImplemented("Unsupported Parameter <%s>" % tag_name)

    def readDataInterface(self, element: ET.Element, interface: DataInterface):
        self.readPortInterface(element, interface)

    def readParameterInterface(self, element: ET.Element, interface: ParameterInterface):
        self.logger.debug("Read ParameterInterface <%s>" % interface.getShortName())
        self.readDataInterface(element, interface)
        self.readParameterInterfaceParameters(element, interface)

    def readNvDataInterfaceNvDatas(self, element: ET.Element, nv_interface: NvDataInterface):
        for child_element in self.findall(element, "NV-DATAS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "VARIABLE-DATA-PROTOTYPE":
                prototype = nv_interface.createNvData(self.getShortName(child_element))
                self.readVariableDataPrototype(child_element, prototype)
            else:
                self.notImplemented("Unsupported NvData <%s>" % tag_name)

    def readNvDataInterface(self, element: ET.Element, nv_interface: NvDataInterface):
        self.logger.debug("Read NvDataInterface <%s>" % nv_interface.getShortName())
        self.readDataInterface(element, nv_interface)
        self.readNvDataInterfaceNvDatas(element, nv_interface)

    def readClientServerInterface(self, element: ET.Element, cs_interface: ClientServerInterface):
        self.logger.debug("Read ClientServerInterface <%s>" % cs_interface.getShortName())
        self.readPortInterface(element, cs_interface)
        self.readClientServerInterfaceOperations(element, cs_interface)
        self.readPossibleErrors(element, cs_interface)

    def getCompuConstContent(self, element: ET.Element) -> CompuConstContent:
        child_element = self.find(element, "*")
        content = None
        if child_element is not None:
            tag_name = self.getTagName(child_element)
            if tag_name == "VF":
                content = CompuConstFormulaContent()
                content.setVf(self.getChildElementOptionalLiteral(element, "VF"))
            elif tag_name == "V":
                content = CompuConstNumericContent()
                content.setV(self.getChildElementOptionalNumericalValue(element, "V"))
            elif tag_name == "VT":
                content = CompuConstTextContent()
                content.setVt(self.getChildElementOptionalLiteral(element, "VT"))
            else:
                self.notImplemented("Unsupported CompuConstContent <%s>" % tag_name)
        return content

    def getCompuConst(self, element: ET.Element, key: str) -> CompuConst:
        compu_const = None
        child_element = self.find(element, key)
        if child_element is not None:
            compu_const = CompuConst()
            self.readARObjectAttributes(child_element, compu_const)
            compu_const.setCompuConstContentType(self.getCompuConstContent(child_element))
        return compu_const

    def readCompuConst(self, element: ET.Element, parent: CompuScale):
        child_element = self.find(element, "COMPU-CONST/VT")
        if child_element is not None:
            # self.logger.debug("Read CompuConst VT: %s" % child_element.text)
            contents = CompuScaleConstantContents()
            contents.compuConst = CompuConst()
            contents.compuConst.compuConstContentType = CompuConstTextContent()
            contents.compuConst.compuConstContentType.vt = ARLiteral()
            contents.compuConst.compuConstContentType.vt.setValue(child_element.text)
            parent.compuScaleContents = contents

    def readCompuNominatorDenominator(self, element: ET.Element, key: str, parent: CompuNominatorDenominator):
        for child_element in self.findall(element, "%s/V" % key):
            # self.logger.debug("Read CompuNominatorDenominator - %s: %s" % (key, child_element.text))
            parent.add_v(child_element.text)

    def readCompuRationCoeffs(self, element: ET.Element, parent: CompuScale):
        child_element = self.find(element, "COMPU-RATIONAL-COEFFS")
        if child_element is not None:
            # self.logger.debug("Read CompuRationCoeffs")
            contents = CompuScaleRationalFormula()
            contents.compuRationalCoeffs = CompuRationalCoeffs()
            contents.compuRationalCoeffs.compuDenominator = CompuNominatorDenominator()
            contents.compuRationalCoeffs.compuNumerator = CompuNominatorDenominator()
            self.readCompuNominatorDenominator(child_element, "COMPU-DENOMINATOR", contents.compuRationalCoeffs.compuDenominator)
            self.readCompuNominatorDenominator(child_element, "COMPU-NUMERATOR", contents.compuRationalCoeffs.compuNumerator)
            parent.compuScaleContents = contents

    def readCompuScaleContents(self, element: ET.Element, parent: CompuScale):
        self.readCompuConst(element, parent)
        self.readCompuRationCoeffs(element, parent)

    def readCompuScale(self, element: ET.Element, compu_scale: CompuScale):
        self.readARObjectAttributes(element, compu_scale)
        compu_scale.setShortLabel(self.getChildElementOptionalLiteral(element, "SHORT-LABEL"))
        compu_scale.setSymbol(self.getChildElementOptionalLiteral(element, "SYMBOL"))
        compu_scale.setDesc(self.getMultiLanguageOverviewParagraph(element, "DESC"))
        compu_scale.setMask(self.getChildElementOptionalPositiveInteger(element, "MASK"))
        compu_scale.setLowerLimit(self.getChildLimitElement(element, "LOWER-LIMIT"))
        compu_scale.setUpperLimit(self.getChildLimitElement(element, "UPPER-LIMIT"))
        self.readCompuScaleContents(element, compu_scale)

    def getCompuScales(self, element: ET.Element) -> CompuScales:
        compu_scales = None
        compu_scales_tag = self.find(element, "COMPU-SCALES")
        if compu_scales_tag is not None:
            compu_scales = CompuScales()
            for child_element in self.findall(compu_scales_tag, "COMPU-SCALE"):
                compu_scale = CompuScale()
                self.readCompuScale(child_element, compu_scale)
                compu_scales.addCompuScale(compu_scale)
        return compu_scales

    def getCompu(self, element: ET.Element, key: str) -> Compu:
        child_element = self.find(element, key)
        compu = None
        if child_element is not None:
            compu = Compu()
            self.readARObjectAttributes(child_element, compu)
            compu.setCompuContent(self.getCompuScales(child_element))
            compu.setCompuDefaultValue(self.getCompuConst(child_element, "COMPU-DEFAULT-VALUE"))
        return compu

    def readCompuMethod(self, element: ET.Element, compu_method: CompuMethod):
        self.logger.debug("Read CompuMethod <%s>" % compu_method.getShortName())
        self.readIdentifiable(element, compu_method)
        compu_method.setUnitRef(self.getChildElementOptionalRefType(element, "UNIT-REF"))
        compu_method.setCompuInternalToPhys(self.getCompu(element, "COMPU-INTERNAL-TO-PHYS"))
        compu_method.setCompuPhysToInternal(self.getCompu(element, "COMPU-PHYS-TO-INTERNAL"))

    def readSwcBswMappingSwcBswRunnableMappings(self, element: ET.Element, parent: SwcBswMapping):
        for child_element in self.findall(element, "RUNNABLE-MAPPINGS/SWC-BSW-RUNNABLE-MAPPING"):
            mapping = SwcBswRunnableMapping()
            mapping.setBswEntityRef(self.getChildElementOptionalRefType(child_element, "BSW-ENTITY-REF"))
            mapping.setSwcRunnableRef(self.getChildElementOptionalRefType(child_element, "SWC-RUNNABLE-REF"))
            parent.addRunnableMapping(mapping)

    def readSwcBswSynchronizedModeGroupPrototype(self, element: ET.Element) -> SwcBswSynchronizedModeGroupPrototype:
        mode_group = SwcBswSynchronizedModeGroupPrototype()
        mode_group.setBswModeGroupRef(self.getChildElementOptionalRefType(element, "BSW-MODE-GROUP-REF"))
        child_element = self.find(element, "SWC-MODE-GROUP-IREF")
        if child_element is not None:
            instance_ref = PModeGroupInAtomicSwcInstanceRef()
            self.readPModeGroupInAtomicSWCInstanceRef(child_element, instance_ref)
            mode_group.setSwcModeGroupIRef(instance_ref)
        return mode_group

    def readSwcBswSynchronizedTrigger(self, element: ET.Element) -> SwcBswSynchronizedTrigger:
        trigger = SwcBswSynchronizedTrigger()
        trigger.setBswTriggerRef(self.getChildElementOptionalRefType(element, "BSW-TRIGGER-REF"))
        child_element = self.find(element, "SWC-TRIGGER-IREF")
        if child_element is not None:
            instance_ref = PTriggerInAtomicSwcTypeInstanceRef()
            self.readPTriggerInAtomicSwcTypeInstanceRef(child_element, instance_ref)
            trigger.setSwcTriggerIRef(instance_ref)
        return trigger

    def readSwcBswMappingSwcBswSynchronizedModeGroups(self, element: ET.Element, parent: SwcBswMapping):
        for child_element in self.findall(element, "SYNCHRONIZED-MODE-GROUPS/SWC-BSW-SYNCHRONIZED-MODE-GROUP-PROTOTYPE"):
            parent.addSynchronizedModeGroup(self.readSwcBswSynchronizedModeGroupPrototype(child_element))

    def readSwcBswMappingSwcBswSynchronizedTriggers(self, element: ET.Element, parent: SwcBswMapping):
        for child_element in self.findall(element, "SYNCHRONIZED-TRIGGERS/SWC-BSW-SYNCHRONIZED-TRIGGER"):
            parent.addSynchronizedTrigger(self.readSwcBswSynchronizedTrigger(child_element))

    def readSwcBswMapping(self, element: ET.Element, mapping: SwcBswMapping):
        self.logger.debug("Read SwcBswMapping <%s>" % mapping.getShortName())
        self.readIdentifiable(element, mapping)
        mapping.setBswBehaviorRef(self.getChildElementOptionalRefType(element, "BSW-BEHAVIOR-REF"))
        self.readSwcBswMappingSwcBswRunnableMappings(element, mapping)
        self.readSwcBswMappingSwcBswSynchronizedModeGroups(element, mapping)
        self.readSwcBswMappingSwcBswSynchronizedTriggers(element, mapping)
        mapping.setSwcBehaviorRef(self.getChildElementOptionalRefType(element, "SWC-BEHAVIOR-REF"))

    def readValueSpecification(self, element: ET.Element, value_spec: ValueSpecification):
        self.readARObjectAttributes(element, value_spec)
        value_spec.setShortLabel(self.getChildElementOptionalLiteral(element, "SHORT-LABEL"))
        # self.logger.debug("read ValueSpecification")

    def getApplicationValueSpecification(self, element: ET.Element) -> ApplicationValueSpecification:
        value_spec = ApplicationValueSpecification()
        self.readValueSpecification(element, value_spec)
        value_spec.setCategory(self.getChildElementOptionalLiteral(element, "CATEGORY"))
        value_spec.setShortLabel(self.getChildElementOptionalLiteral(element, "SHORT-LABEL"))
        value_spec.setSwValueCont(self.getSwValueCont(element))
        return value_spec

    def getNumericalOrText(self, element: ET.Element) -> NumericalOrText:
        not_text = NumericalOrText()
        self.readARObjectAttributes(element, not_text)
        not_text.setVf(self.getChildElementOptionalNumericalValue(element, "VF"))
        not_text.setVt(self.getChildElementOptionalLiteral(element, "VT"))
        return not_text

    def getRuleArguments(self, element: ET.Element) -> RuleArguments:
        arguments = RuleArguments()
        self.readARObjectAttributes(element, arguments)
        arguments.setV(self.getChildElementOptionalNumericalValue(element, "V"))
        arguments.setVf(self.getChildElementOptionalNumericalValue(element, "VF"))
        arguments.setVt(self.getChildElementOptionalVerbatimString(element, "VT"))
        vtf = self.find(element, "VTF")
        if vtf is not None:
            arguments.setVtf(self.getNumericalOrText(vtf))
        return arguments

    def getRuleBasedValueSpecification(self, element: ET.Element) -> RuleBasedValueSpecification:
        if element is None:
            return None
        value_spec = RuleBasedValueSpecification()
        self.readARObjectAttributes(element, value_spec)
        value_spec.setRule(self.getChildElementOptionalIdentifier(element, "RULE"))
        for child_element in self.findall(element, "ARGUMENTSS/RULE-ARGUMENTS"):
            value_spec.addArgument(self.getRuleArguments(child_element))
        value_spec.setMaxSizeToFill(self.getChildElementOptionalIntegerValue(element, "MAX-SIZE-TO-FILL"))
        return value_spec

    def getRuleBasedAxisCont(self, element: ET.Element) -> RuleBasedAxisCont:
        cont = RuleBasedAxisCont()
        self.readARObjectAttributes(element, cont)
        cont.setCategory(self.getChildElementOptionalLiteral(element, "CATEGORY"))
        cont.setUnitRef(self.getChildElementOptionalRefType(element, "UNIT-REF"))
        cont.setSwArraysize(self.getValueList(element, "SW-ARRAYSIZE"))
        cont.setSwAxisIndex(self.getChildElementOptionalLiteral(element, "SW-AXIS-INDEX"))
        cont.setRuleBasedValues(self.getRuleBasedValueSpecification(self.find(element, "RULE-BASED-VALUES")))
        return cont

    def getRuleBasedValueCont(self, element: ET.Element) -> RuleBasedValueCont:
        cont = None
        child_element = self.find(element, "SW-VALUE-CONT")
        if child_element is not None:
            cont = RuleBasedValueCont()
            self.readARObjectAttributes(child_element, cont)
            cont.setUnitRef(self.getChildElementOptionalRefType(child_element, "UNIT-REF"))
            cont.setSwArraysize(self.getValueList(child_element, "SW-ARRAYSIZE"))
            cont.setRuleBasedValues(self.getRuleBasedValueSpecification(self.find(child_element, "RULE-BASED-VALUES")))
        return cont

    def getApplicationRuleBasedValueSpecification(self, element: ET.Element) -> ApplicationRuleBasedValueSpecification:
        value_spec = ApplicationRuleBasedValueSpecification()
        self.readValueSpecification(element, value_spec)
        value_spec.setCategory(self.getChildElementOptionalLiteral(element, "CATEGORY"))
        for child_element in self.findall(element, "SW-AXIS-CONTS/RULE-BASED-AXIS-CONT"):
            value_spec.addSwAxisCont(self.getRuleBasedAxisCont(child_element))
        value_spec.setSwValueCont(self.getRuleBasedValueCont(element))
        return value_spec

    def getCompositeRuleBasedValueSpecification(self, element: ET.Element) -> CompositeRuleBasedValueSpecification:
        value_spec = CompositeRuleBasedValueSpecification()
        self.readValueSpecification(element, value_spec)
        value_spec.setRule(self.getChildElementOptionalIdentifier(element, "RULE"))
        for child_element in self.findall(element, "ARGUMENTS/*"):
            value_spec.addArgument(self.getValueSpecification(child_element, self.getTagName(child_element)))
        for child_element in self.findall(element, "COMPOUND-PRIMITIVE-ARGUMENTS/*"):
            value_spec.addCompoundPrimitiveArgument(self.getValueSpecification(child_element, self.getTagName(child_element)))
        value_spec.setMaxSizeToFill(self.getChildElementOptionalIntegerValue(element, "MAX-SIZE-TO-FILL"))
        return value_spec

    def getNumericalValueSpecification(self, element: ET.Element) -> NumericalValueSpecification:
        value_spec = NumericalValueSpecification()
        self.readValueSpecification(element, value_spec)
        value_spec.setShortLabel(self.getChildElementOptionalLiteral(element, "SHORT-LABEL"))
        value_spec.setValue(self.getChildElementOptionalNumericalValue(element, "VALUE"))
        return value_spec

    def getTextValueSpecification(self, element: ET.Element) -> TextValueSpecification:
        # self.logger.debug("Get TextValueSpecification")
        value_spec = TextValueSpecification()
        self.readValueSpecification(element, value_spec)
        value_spec.setShortLabel(self.getChildElementOptionalLiteral(element, "SHORT-LABEL"))
        value_spec.setValue(self.getChildElementOptionalLiteral(element, "VALUE"))
        return value_spec

    def getArrayValueSpecification(self, element: ET.Element) -> ArrayValueSpecification:
        # self.logger.debug("Get ArrayValueSpecification")
        value_spec = ArrayValueSpecification()
        self.readValueSpecification(element, value_spec)
        child_elements = element.findall("./xmlns:ELEMENTS/*", self.nsmap)
        for child_element in child_elements:
            value_spec.addElement(self.getValueSpecification(child_element, self.getTagName(child_element)))
        return value_spec

    def getConstantReference(self, element: ET.Element) -> ConstantReference:
        # self.logger.debug("getConstantReference")
        value_spec = ConstantReference()
        self.readValueSpecification(element, value_spec)
        value_spec.setConstantRef(self.getChildElementOptionalRefType(element, "CONSTANT-REF"))
        return value_spec

    def getValueSpecification(self, element: ET.Element, tag_name: str) -> ValueSpecification:
        if tag_name == "APPLICATION-VALUE-SPECIFICATION":
            value_spec = self.getApplicationValueSpecification(element)
        elif tag_name == "APPLICATION-RULE-BASED-VALUE-SPECIFICATION":
            value_spec = self.getApplicationRuleBasedValueSpecification(element)
        elif tag_name == "COMPOSITE-RULE-BASED-VALUE-SPECIFICATION":
            value_spec = self.getCompositeRuleBasedValueSpecification(element)
        elif tag_name == "RECORD-VALUE-SPECIFICATION":
            value_spec = self.getRecordValueSpecification(element)
        elif tag_name == "NUMERICAL-VALUE-SPECIFICATION":
            value_spec = self.getNumericalValueSpecification(element)
        elif tag_name == "ARRAY-VALUE-SPECIFICATION":
            value_spec = self.getArrayValueSpecification(element)
        elif tag_name == "TEXT-VALUE-SPECIFICATION":
            value_spec = self.getTextValueSpecification(element)
        elif tag_name == "CONSTANT-REFERENCE":
            value_spec = self.getConstantReference(element)
        else:
            self.notImplemented("Unsupported RecordValueSpecificationField %s" % tag_name)
        return value_spec

    def readRecordValueSpecificationFields(self, element: ET.Element, spec: RecordValueSpecification):
        for child_element in element.findall("./xmlns:FIELDS/*", self.nsmap):
            spec.addField(self.getValueSpecification(child_element, self.getTagName(child_element)))

    def getRecordValueSpecification(self, element: ET.Element) -> RecordValueSpecification:
        value_spec = RecordValueSpecification()
        self.readValueSpecification(element, value_spec)
        self.readRecordValueSpecificationFields(element, value_spec)
        return value_spec

    def readConstantSpecification(self, element: ET.Element, spec: ConstantSpecification):
        self.logger.debug("Read ConstantSpecification <%s>" % spec.getShortName())
        self.readIdentifiable(element, spec)
        for child_element in self.findall(element, "VALUE-SPEC/*"):
            spec.setValueSpec(self.getValueSpecification(child_element, self.getTagName(child_element)))

    def readInternalConstrs(self, element: ET.Element, parent: DataConstrRule):
        child_element = self.find(element, "INTERNAL-CONSTRS")
        if child_element is not None:
            constrs = InternalConstrs()
            self.readARObjectAttributes(child_element, constrs)
            constrs.setLowerLimit(self.getChildLimitElement(child_element, "LOWER-LIMIT"))
            constrs.setUpperLimit(self.getChildLimitElement(child_element, "UPPER-LIMIT"))
            for sc_element in self.findall(child_element, "SCALE-CONSTRS/SCALE-CONSTR"):
                constrs.addScaleConstr(self.readScaleConstr(sc_element))
            constrs.setMaxGradient(self.getChildElementOptionalNumericalValue(child_element, "MAX-GRADIENT"))
            constrs.setMaxDiff(self.getChildElementOptionalNumericalValue(child_element, "MAX-DIFF"))
            constrs.setMonotony(self.getChildElementOptionalLiteral(child_element, "MONOTONY"))
            parent.internalConstrs = constrs

    def readScaleConstr(self, element: ET.Element) -> ScaleConstr:
        scale_constr = ScaleConstr()
        self.readARObjectAttributes(element, scale_constr)
        scale_constr.setDesc(self.getMultiLanguageOverviewParagraph(element, "DESC"))
        scale_constr.setLowerLimit(self.getChildLimitElement(element, "LOWER-LIMIT"))
        scale_constr.setShortLabel(self.getChildElementOptionalIdentifier(element, "SHORT-LABEL"))
        scale_constr.setUpperLimit(self.getChildLimitElement(element, "UPPER-LIMIT"))
        validity_value = element.get("VALIDITY")
        if validity_value is not None:
            scale_constr.setValidity(ScaleConstrValidityEnum().setValue(validity_value))
        return scale_constr

    def readPhysConstrs(self, element: ET.Element, parent: DataConstrRule):
        child_element = self.find(element, "PHYS-CONSTRS")
        if child_element is not None:
            constrs = PhysConstrs()
            self.readARObjectAttributes(child_element, constrs)
            constrs.setLowerLimit(self.getChildLimitElement(child_element, "LOWER-LIMIT"))
            constrs.setUpperLimit(self.getChildLimitElement(child_element, "UPPER-LIMIT"))
            constrs.setMaxDiff(self.getChildElementOptionalNumericalValue(child_element, "MAX-DIFF"))
            constrs.setMaxGradient(self.getChildElementOptionalNumericalValue(child_element, "MAX-GRADIENT"))
            constrs.setMonotony(self.getChildElementOptionalLiteral(child_element, "MONOTONY"))
            for sc_element in self.findall(child_element, "SCALE-CONSTRS/SCALE-CONSTR"):
                constrs.addScaleConstr(self.readScaleConstr(sc_element))
            constrs.setUnitRef(self.getChildElementOptionalRefType(child_element, "UNIT-REF"))
            parent.physConstrs = constrs

    def readDataConstrRule(self, element: ET.Element, parent: DataConstr):
        for child_element in self.findall(element, "DATA-CONSTR-RULES/DATA-CONSTR-RULE"):
            # self.logger.debug("Read DataConstrRule")
            rule = DataConstrRule()
            self.readARObjectAttributes(child_element, rule)
            rule.constrLevel = self.getChildElementOptionalNumericalValue(child_element, "CONSTR-LEVEL")
            self.readInternalConstrs(child_element, rule)
            self.readPhysConstrs(child_element, rule)
            parent.addDataConstrRule(rule)

    def readDataConstr(self, element: ET.Element, constr: DataConstr):
        # self.logger.debug("Read DataConstr <%s>" % constr.getShortName())
        self.readIdentifiable(element, constr)
        self.readDataConstrRule(element, constr)

    def readUnit(self, element: ET.Element, unit: Unit):
        self.logger.debug("Read Unit <%s>" % unit.getShortName())
        self.readIdentifiable(element, unit)
        unit.setDisplayName(self.getChildElementOptionalLiteral(element, "DISPLAY-NAME"))
        unit.setFactorSiToUnit(self.getChildElementOptionalFloatValue(element, "FACTOR-SI-TO-UNIT"))
        unit.setOffsetSiToUnit(self.getChildElementOptionalFloatValue(element, "OFFSET-SI-TO-UNIT"))
        unit.setPhysicalDimensionRef(self.getChildElementOptionalRefType(element, "PHYSICAL-DIMENSION-REF"))

    def readEndToEndDescriptionDataIds(self, element: ET.Element, parent: EndToEndDescription):
        child_element = self.find(element, "DATA-IDS")
        if child_element is not None:
            for value in self.getChildElementNumericalValueList(child_element, "DATA-ID"):
                parent.addDataId(value)

    def getEndToEndDescription(self, element: ET.Element, key: str) -> EndToEndDescription:
        child_element = self.find(element, key)
        desc = None
        if child_element is not None:
            desc = EndToEndDescription()
            self.readARObjectAttributes(child_element, desc)
            desc.setCategory(self.getChildElementOptionalLiteral(child_element, "CATEGORY"))
            self.readEndToEndDescriptionDataIds(child_element, desc)
            desc.setDataIdMode(self.getChildElementOptionalPositiveInteger(child_element, "DATA-ID-MODE"))
            desc.setDataLength(self.getChildElementOptionalPositiveInteger(child_element, "DATA-LENGTH"))
            desc.setMaxDeltaCounterInit(self.getChildElementOptionalPositiveInteger(child_element, "MAX-DELTA-COUNTER-INIT"))
            desc.setCrcOffset(self.getChildElementOptionalPositiveInteger(child_element, "CRC-OFFSET"))
            desc.setCounterOffset(self.getChildElementOptionalPositiveInteger(child_element, "COUNTER-OFFSET"))
        return desc

    def getVariableDataPrototypeInSystemInstanceRef(self, element: ET.Element) -> VariableDataPrototypeInSystemInstanceRef:
        instance_ref = None
        if element is not None:
            instance_ref = VariableDataPrototypeInSystemInstanceRef()
            for ref in self.getChildElementRefTypeList(element, "CONTEXT-COMPONENT-REF"):
                instance_ref.addContextComponentRef(ref)
            instance_ref.setContextCompositionRef(self.getChildElementOptionalRefType(element, "CONTEXT-COMPOSITION-REF"))
            instance_ref.setContextPortRef(self.getChildElementOptionalRefType(element, "CONTEXT-PORT-REF"))
            instance_ref.setTargetDataPrototypeRef(self.getChildElementOptionalRefType(element, "TARGET-DATA-PROTOTYPE-REF"))
        return instance_ref

    def readEndToEndProtectionVariablePrototype(self, element: ET.Element, prototype: EndToEndProtectionVariablePrototype):
        self.readARObjectAttributes(element, prototype)
        for child_element in self.findall(element, "RECEIVER-IREFS/RECEIVER-IREF"):
            prototype.addReceiverIref(self.getVariableDataPrototypeInSystemInstanceRef(child_element))
        child_element = self.find(element, "SENDER-IREF")
        if child_element is not None:
            prototype.senderIRef = self.getVariableDataPrototypeInSystemInstanceRef(child_element)
        return prototype

    def readEndToEndProtectionEndToEndProtectionVariablePrototypes(self, element: ET.Element, protection: EndToEndProtection):
        for child_element in self.findall(element, "END-TO-END-PROTECTION-VARIABLE-PROTOTYPES/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "END-TO-END-PROTECTION-VARIABLE-PROTOTYPE":
                prototype = EndToEndProtectionVariablePrototype()
                self.readEndToEndProtectionVariablePrototype(child_element, prototype)
                protection.addEndToEndProtectionVariablePrototype(prototype)
            else:
                self.raiseError("Unsupported End To End Protection Variable Prototype <%s>" % tag_name)

    def readEndToEndProtectionISignalIPdu(self, element: ET.Element, ipdu: EndToEndProtectionISignalIPdu):
        ipdu.setDataOffset(self.getChildElementOptionalIntegerValue(element, "DATA-OFFSET"))
        ipdu.setISignalGroupRef(self.getChildElementOptionalRefType(element, "I-SIGNAL-GROUP-REF"))
        ipdu.setISignalIPduRef(self.getChildElementOptionalRefType(element, "I-SIGNAL-I-PDU-REF"))

    def readEndToEndProtectionEndToEndProtectionISignalIPdus(self, element: ET.Element, protection: EndToEndProtection):
        for child_element in self.findall(element, "END-TO-END-PROTECTION-I-SIGNAL-I-PDUS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "END-TO-END-PROTECTION-I-SIGNAL-I-PDU":
                ipdu = EndToEndProtectionISignalIPdu()
                self.readEndToEndProtectionISignalIPdu(child_element, ipdu)
                protection.addEndToEndProtectionISignalIPdu(ipdu)
            else:
                self.notImplemented("Unsupported EndToEndProtectionISignalIPdu <%s>" % tag_name)

    def readEndToEndProtection(self, element: ET.Element, parent: EndToEndProtectionSet):
        short_name = self.getShortName(element)
        self.logger.debug("readEndToEndProtection %s" % short_name)
        protection = parent.createEndToEndProtection(short_name)
        self.readIdentifiable(element, protection)
        protection.setEndToEndProfile(self.getEndToEndDescription(element, "END-TO-END-PROFILE"))
        self.readEndToEndProtectionEndToEndProtectionISignalIPdus(element, protection)
        self.readEndToEndProtectionEndToEndProtectionVariablePrototypes(element, protection)

    def readEndToEndProtections(self, element: ET.Element, parent: EndToEndProtectionSet):
        for child_element in self.findall(element, "END-TO-END-PROTECTIONS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "END-TO-END-PROTECTION":
                self.readEndToEndProtection(child_element, parent)
            else:
                self.notImplemented("Unsupported EndToEndProtectionSet <%s>" % tag_name)

    def readEndToEndProtectionSet(self, element: ET.Element, protection_set: EndToEndProtectionSet):
        self.logger.debug("Read EndToEndProtectionSet <%s>" % protection_set.getShortName())
        self.readIdentifiable(element, protection_set)
        self.readEndToEndProtections(element, protection_set)

    def readImplementationProps(self, element: ET.Element, props: ImplementationProps):
        self.readReferrable(element, props)
        props.setSymbol(self.getChildElementOptionalLiteral(element, "SYMBOL"))

    def readSymbolProps(self, element: ET.Element, props: SymbolProps):
        self.readImplementationProps(element, props)

    def readImplementationDataTypeSymbolProps(self, element: ET.Element, data_type: ImplementationDataType):
        child_element = self.find(element, "SYMBOL-PROPS")
        if child_element is not None:
            props = data_type.createSymbolProps(self.getShortName(child_element))
            self.readSymbolProps(child_element, props)

    def readApplicationDataType(self, element: ET.Element, data_type: ApplicationDataType):
        self.readAutosarDataType(element, data_type)

    def readApplicationCompositeDataType(self, element: ET.Element, data_type: ApplicationCompositeDataType):
        self.readApplicationDataType(element, data_type)

    def readDataPrototype(self, element: ET.Element, prototype: DataPrototype):
        self.readIdentifiable(element, prototype)
        prototype.setSwDataDefProps(self.getSwDataDefProps(element, "SW-DATA-DEF-PROPS"))

    def readApplicationCompositeElementDataPrototype(self, element: ET.Element, prototype: ApplicationCompositeElementDataPrototype):
        self.readDataPrototype(element, prototype)
        prototype.typeTRef = self.getChildElementOptionalRefType(element, "TYPE-TREF")

    def readApplicationArrayElement(self, element: ET.Element, parent: ApplicationArrayDataType):
        child_element = self.find(element, "ELEMENT")
        if child_element is not None:
            short_name = self.getShortName(child_element)
            self.logger.debug("Read ApplicationArrayElement %s" % short_name)
            array_element = parent.createApplicationArrayElement(short_name)
            self.readApplicationCompositeElementDataPrototype(child_element, array_element)
            array_element.setArraySizeHandling(self.getChildElementOptionalLiteral(child_element, "ARRAY-SIZE-HANDLING"))
            array_element.setArraySizeSemantics(self.getChildElementOptionalLiteral(child_element, "ARRAY-SIZE-SEMANTICS"))
            array_element.setIndexDataTypeRef(self.getChildElementOptionalRefType(child_element, "INDEX-DATA-TYPE-REF"))
            array_element.setMaxNumberOfElements(self.getChildElementOptionalNumericalValue(child_element, "MAX-NUMBER-OF-ELEMENTS"))

    def readApplicationArrayDataType(self, element: ET.Element, data_type: ApplicationArrayDataType):
        self.logger.debug("Read ApplicationArrayDataType <%s>" % data_type.getShortName())
        self.readApplicationCompositeDataType(element, data_type)
        data_type.setDynamicArraySizeProfile(self.getChildElementOptionalLiteral(element, "DYNAMIC-ARRAY-SIZE-PROFILE"))
        self.readApplicationArrayElement(element, data_type)

    def getSwRecordLayoutV(self, element: ET.Element, key: str) -> SwRecordLayoutV:
        child_element = self.find(element, key)
        layout_v = None
        if child_element is not None:
            layout_v = SwRecordLayoutV()
            layout_v.setShortLabel(self.getChildElementOptionalLiteral(child_element, "SHORT-LABEL"))
            layout_v.setBaseTypeRef(self.getChildElementOptionalRefType(child_element, "BASE-TYPE-REF"))
            layout_v.setSwRecordLayoutVAxis(self.getChildElementOptionalLiteral(child_element, "SW-RECORD-LAYOUT-V-AXIS"))
            layout_v.setSwRecordLayoutVProp(self.getChildElementOptionalLiteral(child_element, "SW-RECORD-LAYOUT-V-PROP"))
            layout_v.setSwRecordLayoutVIndex(self.getChildElementOptionalLiteral(child_element, "SW-RECORD-LAYOUT-V-INDEX"))
        return layout_v

    def readSwRecordLayoutGroupSwRecordLayoutGroupContentType(self, element: ET.Element, group: SwRecordLayoutGroup):
        content = SwRecordLayoutGroupContent()
        content.setSwRecordLayoutGroup(self.getSwRecordLayoutGroup(element, "SW-RECORD-LAYOUT-GROUP"))
        content.setSwRecordLayoutV(self.getSwRecordLayoutV(element, "SW-RECORD-LAYOUT-V"))
        group.setSwRecordLayoutGroupContentType(content)

    def getSwRecordLayoutGroup(self, element: ET.Element, key: str) -> SwRecordLayoutGroup:
        child_element = self.find(element, key)
        group = None
        if child_element is not None:
            group = SwRecordLayoutGroup()
            group.setShortLabel(self.getChildElementOptionalLiteral(child_element, "SHORT-LABEL"))
            group.setCategory(self.getChildElementOptionalLiteral(child_element, "CATEGORY"))
            group.setSwRecordLayoutGroupAxis(self.getChildElementOptionalLiteral(child_element, "SW-RECORD-LAYOUT-GROUP-AXIS"))
            group.setSwRecordLayoutGroupIndex(self.getChildElementOptionalLiteral(child_element, "SW-RECORD-LAYOUT-GROUP-INDEX"))
            group.setSwRecordLayoutGroupFrom(self.getChildElementOptionalLiteral(child_element, "SW-RECORD-LAYOUT-GROUP-FROM"))
            group.setSwRecordLayoutGroupStep(self.getChildElementOptionalIntegerValue(child_element, "SW-RECORD-LAYOUT-GROUP-STEP"))
            group.setSwRecordLayoutGroupTo(self.getChildElementOptionalLiteral(child_element, "SW-RECORD-LAYOUT-GROUP-TO"))
            self.readSwRecordLayoutGroupSwRecordLayoutGroupContentType(child_element, group)

        return group

    def readSwRecordLayout(self, element: ET.Element, layout: SwRecordLayout):
        self.logger.debug("Read SwRecordLayout <%s>" % layout.getShortName())
        self.readIdentifiable(element, layout)
        layout.setSwRecordLayoutGroup(self.getSwRecordLayoutGroup(element, "SW-RECORD-LAYOUT-GROUP"))

    def readSwAddrMethod(self, element: ET.Element, method: SwAddrMethod):
        self.logger.debug("Read SwAddrMethod <%s>" % method.getShortName())
        self.readIdentifiable(element, method)
        memory_allocation_keyword_policy = self.getChildElementOptionalLiteral(element, "MEMORY-ALLOCATION-KEYWORD-POLICY")
        if memory_allocation_keyword_policy is not None:
            method.setMemoryAllocationKeywordPolicy(MemoryAllocationKeywordPolicyType().setValue(memory_allocation_keyword_policy.getValue()))
        for option in self.getChildElementLiteralValueList(element, "OPTIONS/OPTION"):
            method.addOption(option)
        section_initialization_policy = self.getChildElementOptionalLiteral(element, "SECTION-INITIALIZATION-POLICY")
        if section_initialization_policy is not None:
            method.setSectionInitializationPolicy(SectionInitializationPolicyType().setValue(section_initialization_policy.getValue()))
        section_type = self.getChildElementOptionalLiteral(element, "SECTION-TYPE")
        if section_type is not None:
            method.setSectionType(MemorySectionType().setValue(section_type.getValue()))

    def readTriggerInterface(self, element: ET.Element, trigger_if: TriggerInterface):
        self.logger.debug("Read TriggerInterface <%s>" % trigger_if.getShortName())
        self.readIdentifiable(element, trigger_if)

    def readModeDeclarationGroupModeDeclaration(self, element: ET.Element, parent: ModeDeclarationGroup):
        for child_element in self.findall(element, "MODE-DECLARATIONS/MODE-DECLARATION"):
            short_name = self.getShortName(child_element)
            declaration = parent.createModeDeclaration(short_name)
            self.readARObjectAttributes(child_element, declaration)
            declaration.setValue(self.getChildElementOptionalPositiveInteger(child_element, "VALUE"))

    def readModeErrorBehavior(self, element: ET.Element) -> ModeErrorBehavior:
        behavior = ModeErrorBehavior()
        self.readARObjectAttributes(element, behavior)
        behavior.setDefaultModeRef(self.getChildElementOptionalRefType(element, "DEFAULT-MODE-REF"))
        error_reaction_policy = self.getChildElementOptionalLiteral(element, "ERROR-REACTION-POLICY")
        if error_reaction_policy is not None:
            behavior.setErrorReactionPolicy(ModeErrorReactionPolicyEnum().setValue(error_reaction_policy.getValue()))
        return behavior

    def readModeDeclarationGroupModeTransition(self, element: ET.Element, parent: ModeDeclarationGroup):
        for child_element in self.findall(element, "MODE-TRANSITIONS/MODE-TRANSITION"):
            short_name = self.getShortName(child_element)
            transition = parent.createModeTransition(short_name)
            self.readARObjectAttributes(child_element, transition)
            transition.setEnteredModeRef(self.getChildElementOptionalRefType(child_element, "ENTERED-MODE-REF"))
            transition.setExitedModeRef(self.getChildElementOptionalRefType(child_element, "EXITED-MODE-REF"))

    def readModeDeclarationGroup(self, element: ET.Element, group: ModeDeclarationGroup):
        self.logger.debug("Read ModeDeclarationGroup <%s>" % group.getShortName())
        self.readIdentifiable(element, group)
        self.readModeDeclarationGroupModeDeclaration(element, group)
        group.setInitialModeRef(self.getChildElementOptionalRefType(element, "INITIAL-MODE-REF"))
        mode_manager_error_behavior = self.find(element, "MODE-MANAGER-ERROR-BEHAVIOR")
        if mode_manager_error_behavior is not None:
            group.setModeManagerErrorBehavior(self.readModeErrorBehavior(mode_manager_error_behavior))
        self.readModeDeclarationGroupModeTransition(element, group)
        mode_user_error_behavior = self.find(element, "MODE-USER-ERROR-BEHAVIOR")
        if mode_user_error_behavior is not None:
            group.setModeUserErrorBehavior(self.readModeErrorBehavior(mode_user_error_behavior))
        group.setOnTransitionValue(self.getChildElementOptionalPositiveInteger(element, "ON-TRANSITION-VALUE"))

    def readModeSwitchInterfaceModeGroup(self, element: ET.Element, parent: ModeSwitchInterface):
        child_element = self.find(element, "MODE-GROUP")
        if child_element is not None:
            short_name = self.getShortName(child_element)
            mode_group = parent.createModeGroup(short_name)
            self.readModeDeclarationGroupPrototype(child_element, mode_group)

    def readModeSwitchInterface(self, element: ET.Element, mode_interface: ModeSwitchInterface):
        self.logger.debug("Read ModeSwitchInterface <%s>" % mode_interface.getShortName())
        self.readPortInterface(element, mode_interface)
        self.readModeSwitchInterfaceModeGroup(element, mode_interface)

    def readEOCExecutableEntityRef(self, element: ET.Element, constraint: ExecutionOrderConstraint):
        short_name = self.getShortName(element)
        self.logger.debug("readEocExecutableEntityRef %s" % short_name)
        entity_ref = constraint.createEOCExecutableEntityRef(short_name)
        self.readIdentifiable(element, entity_ref)
        for ref in self.getChildElementRefTypeList(element, "SUCCESSOR-REFS/SUCCESSOR-REF"):
            entity_ref.addSuccessorRef(ref)

    def readExecutionOrderConstraintOrderedElement(self, element: ET.Element, constrain: ExecutionOrderConstraint):
        for child_element in self.findall(element, "ORDERED-ELEMENTS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "EOC-EXECUTABLE-ENTITY-REF":
                self.readEOCExecutableEntityRef(child_element, constrain)
            else:
                self.raiseError("Unsupported order element <%s>." % tag_name)

    def readExecutionOrderConstraint(self, element: ET.Element, extension: TimingExtension):
        short_name = self.getShortName(element)
        self.logger.debug("readExecutionOrderConstraint %s" % short_name)
        constraint = extension.createExecutionOrderConstraint(short_name)
        self.readIdentifiable(element, constraint)
        self.readExecutionOrderConstraintOrderedElement(element, constraint)

    def readTimingExtension(self, element: ET.Element, extension: TimingExtension):
        for child_element in self.findall(element, "TIMING-REQUIREMENTS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "EXECUTION-ORDER-CONSTRAINT":
                self.readExecutionOrderConstraint(child_element, extension)
            else:
                self.raiseError("Unsupported timing requirement <%s>" % tag_name)

    def readSwcTiming(self, element: ET.Element, timing: SwcTiming):
        self.logger.debug("Read SwcTiming <%s>" % timing.getShortName())
        self.readIdentifiable(element, timing)
        self.readTimingExtension(element, timing)

    def readFrameTriggering(self, element: ET.Element, triggering: FrameTriggering):
        self.readIdentifiable(element, triggering)
        for ref in self.getChildElementRefTypeList(element, "FRAME-PORT-REFS/FRAME-PORT-REF"):
            triggering.addFramePortRef(ref)
        triggering.setFrameRef(self.getChildElementOptionalRefType(element, "FRAME-REF"))
        for child_element in self.findall(element, "PDU-TRIGGERINGS/PDU-TRIGGERING-REF-CONDITIONAL"):
            triggering.addPduTriggeringRef(self.getChildElementOptionalRefType(child_element, "PDU-TRIGGERING-REF"))

    def readCanFrameTriggering(self, element: ET.Element, triggering: CanFrameTriggering):
        self.logger.debug("Read CanFrameTriggering %s" % triggering.getShortName())
        self.readFrameTriggering(element, triggering)
        triggering.setCanAddressingMode(self.getChildElementOptionalLiteral(element, "CAN-ADDRESSING-MODE"))
        triggering.setCanFdFrameSupport(self.getChildElementOptionalBooleanValue(element, "CAN-FD-FRAME-SUPPORT"))
        triggering.setCanFrameRxBehavior(self.getChildElementOptionalLiteral(element, "CAN-FRAME-RX-BEHAVIOR"))
        triggering.setCanFrameTxBehavior(self.getChildElementOptionalLiteral(element, "CAN-FRAME-TX-BEHAVIOR"))
        triggering.setIdentifier(self.getChildElementOptionalNumericalValue(element, "IDENTIFIER"))
        triggering.setRxIdentifierRange(self.getChildElementRxIdentifierRange(element, "RX-IDENTIFIER-RANGE"))

    def readLinFrameTriggering(self, element: ET.Element, triggering: LinFrameTriggering):
        self.logger.debug("Read LinFrameTriggering %s" % triggering.getShortName())
        self.readFrameTriggering(element, triggering)
        triggering.setIdentifier(self.getChildElementOptionalNumericalValue(element, "IDENTIFIER"))
        triggering.setLinChecksum(self.getChildElementOptionalLiteral(element, "LIN-CHECKSUM"))

    def readCommunicationCycle(self, element: ET.Element, cycle: CommunicationCycle):
        self.readARObjectAttributes(element, cycle)

    def readCycleRepetition(self, element: ET.Element, cycle: CycleRepetition):
        self.readCommunicationCycle(element, cycle)
        cycle.setBaseCycle(self.getChildElementOptionalIntegerValue(element, "BASE-CYCLE"))
        cycle.setCycleRepetition(self.getChildElementOptionalLiteral(element, "CYCLE-REPETITION"))

    def readFlexrayAbsolutelyScheduledTimingCommunicationCycle(self, element: ET.Element, timing: FlexrayAbsolutelyScheduledTiming):
        for child_element in self.findall(element, "COMMUNICATION-CYCLE/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "CYCLE-REPETITION":
                repetition = CycleRepetition()
                self.readCycleRepetition(child_element, repetition)
                timing.setCommunicationCycle(repetition)
            else:
                self.notImplemented("Unsupported CommunicationCycle <%s>" % tag_name)

    def readFlexrayAbsolutelyScheduledTiming(self, element: ET.Element, timing: FlexrayAbsolutelyScheduledTiming):
        self.readARObjectAttributes(element, timing)
        self.readFlexrayAbsolutelyScheduledTimingCommunicationCycle(element, timing)
        timing.setSlotID(self.getChildElementOptionalPositiveInteger(element, "SLOT-ID"))

    def readFlexrayFrameTriggeringAbsolutelyScheduledTimings(self, element: ET.Element, triggering: FlexrayFrameTriggering):
        for child_element in self.findall(element, "ABSOLUTELY-SCHEDULED-TIMINGS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "FLEXRAY-ABSOLUTELY-SCHEDULED-TIMING":
                timing = FlexrayAbsolutelyScheduledTiming()
                self.readFlexrayAbsolutelyScheduledTiming(child_element, timing)
                triggering.addAbsolutelyScheduledTiming(timing)
            else:
                self.notImplemented("Unsupported AbsolutelyScheduledTiming <%s>" % tag_name)

    def readFlexrayFrameTriggering(self, element: ET.Element, triggering: FlexrayFrameTriggering):
        self.logger.debug("Read FlexrayFrameTriggering %s" % triggering.getShortName())
        self.readFrameTriggering(element, triggering)
        self.readFlexrayFrameTriggeringAbsolutelyScheduledTimings(element, triggering)
        triggering.setAllowDynamicLSduLength(self.getChildElementOptionalBooleanValue(element, "ALLOW-DYNAMIC-L-SDU-LENGTH"))
        triggering.setMessageId(self.getChildElementOptionalPositiveInteger(element, "MESSAGE-ID"))
        triggering.setPayloadPreambleIndicator(self.getChildElementOptionalBooleanValue(element, "PAYLOAD-PREAMBLE-INDICATOR"))

    def readISignalTriggering(self, element: ET.Element, triggering: ISignalTriggering):
        self.logger.debug("Read ISignalTriggering %s" % triggering.getShortName())
        self.readIdentifiable(element, triggering)
        triggering.setISignalGroupRef(self.getChildElementOptionalRefType(element, "I-SIGNAL-GROUP-REF"))
        for ref in self.getChildElementRefTypeList(element, "I-SIGNAL-PORT-REFS/I-SIGNAL-PORT-REF"):
            triggering.addISignalPortRef(ref)
        triggering.setISignalRef(self.getChildElementOptionalRefType(element, "I-SIGNAL-REF"))

    def readPduTriggering(self, element: ET.Element, triggering: PduTriggering):
        self.logger.debug("Read PduTriggering %s" % triggering.getShortName())
        self.readIdentifiable(element, triggering)
        for ref in self.getChildElementRefTypeList(element, "I-PDU-PORT-REFS/I-PDU-PORT-REF"):
            triggering.addIPduPortRef(ref)
        triggering.setIPduRef(self.getChildElementOptionalRefType(element, "I-PDU-REF"))
        for child_element in self.findall(element, "I-SIGNAL-TRIGGERINGS/I-SIGNAL-TRIGGERING-REF-CONDITIONAL"):
            triggering.addISignalTriggeringRef(self.getChildElementOptionalRefType(child_element, "I-SIGNAL-TRIGGERING-REF"))

    def readPhysicalChannelCommConnectorRefs(self, element: ET.Element, channel: PhysicalChannel):
        for child_element in self.findall(element, "COMM-CONNECTORS/COMMUNICATION-CONNECTOR-REF-CONDITIONAL"):
            channel.addCommConnectorRef(self.getChildElementOptionalRefType(child_element, "COMMUNICATION-CONNECTOR-REF"))

    def readPhysicalChannelFrameTriggerings(self, element: ET.Element, channel: PhysicalChannel):
        for child_element in self.findall(element, "FRAME-TRIGGERINGS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "CAN-FRAME-TRIGGERING":
                triggering = channel.createCanFrameTriggering(self.getShortName(child_element))
                self.readCanFrameTriggering(child_element, triggering)
            elif tag_name == "LIN-FRAME-TRIGGERING":
                triggering = channel.createLinFrameTriggering(self.getShortName(child_element))
                self.readLinFrameTriggering(child_element, triggering)
            elif tag_name == "FLEXRAY-FRAME-TRIGGERING":
                triggering = channel.createFlexrayFrameTriggering(self.getShortName(child_element))
                self.readFlexrayFrameTriggering(child_element, triggering)
            else:
                self.notImplemented("Unsupported Frame Triggering <%s>" % tag_name)

    def readPhysicalChannelISignalTriggerings(self, element: ET.Element, channel: PhysicalChannel):
        for child_element in self.findall(element, "I-SIGNAL-TRIGGERINGS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "I-SIGNAL-TRIGGERING":
                triggering = channel.createISignalTriggering(self.getShortName(child_element))
                self.readISignalTriggering(child_element, triggering)
            else:
                self.notImplemented("Unsupported Frame Triggering <%s>" % tag_name)

    def readPhysicalChannelPduTriggerings(self, element, channel):
        for child_element in self.findall(element, "PDU-TRIGGERINGS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "PDU-TRIGGERING":
                triggering = channel.createPduTriggering(self.getShortName(child_element))
                self.readPduTriggering(child_element, triggering)
            else:
                self.notImplemented("Unsupported Frame Triggering <%s>" % tag_name)

    def readPhysicalChannel(self, element: ET.Element, channel: PhysicalChannel):
        self.readIdentifiable(element, channel)

        self.readPhysicalChannelCommConnectorRefs(element, channel)
        self.readPhysicalChannelFrameTriggerings(element, channel)
        self.readPhysicalChannelISignalTriggerings(element, channel)
        self.readPhysicalChannelPduTriggerings(element, channel)

    def readCanPhysicalChannel(self, element: ET.Element, channel: CanPhysicalChannel):
        self.readPhysicalChannel(element, channel)

    def readScheduleTableEntry(self, element: ET.Element, entry: ScheduleTableEntry):
        entry.setDelay(self.getChildElementOptionalTimeValue(element, "DELAY"))
        entry.setPositionInTable(self.getChildElementOptionalIntegerValue(element, "POSITION-IN-TABLE"))

    def getApplicationEntry(self, element: ET.Element, key: str) -> ApplicationEntry:
        entry = None
        if element is not None:
            entry = ApplicationEntry()
            self.readScheduleTableEntry(element, entry)
            entry.setFrameTriggeringRef(self.getChildElementOptionalRefType(element, "FRAME-TRIGGERING-REF"))
        return entry

    def readLinScheduleTableTableEntries(self, element: ET.Element, table: LinScheduleTable):
        for child_element in self.findall(element, "TABLE-ENTRYS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "APPLICATION-ENTRY":
                table = table.addTableEntry(self.getApplicationEntry(child_element, "APPLICATION-ENTRY"))
            else:
                self.notImplemented("Unsupported Schedule Table <%s>" % tag_name)

    def readLinScheduleTable(self, element: ET.Element, table: LinScheduleTable):
        self.readIdentifiable(element, table)
        table.setResumePosition(self.getChildElementOptionalLiteral(element, "RESUME-POSITION"))
        table.setRunMode(self.getChildElementOptionalLiteral(element, "RUN-MODE"))
        self.readLinScheduleTableTableEntries(element, table)

    def readLinPhysicalChannelScheduleTables(self, element: ET.Element, channel: LinPhysicalChannel):
        for child_element in self.findall(element, "SCHEDULE-TABLES/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "LIN-SCHEDULE-TABLE":
                table = channel.createLinScheduleTable(self.getShortName(child_element))
                self.readLinScheduleTable(child_element, table)
            else:
                self.notImplemented("Unsupported Schedule Table <%s>" % tag_name)

    def readLinPhysicalChannel(self, element: ET.Element, channel: LinPhysicalChannel):
        self.readPhysicalChannel(element, channel)
        self.readLinPhysicalChannelScheduleTables(element, channel)

    def getIpv6Configuration(self, element: ET.Element) -> Ipv6Configuration:
        configuration = None
        if element is not None:
            configuration = Ipv6Configuration()
            configuration.setAssignmentPriority(self.getChildElementOptionalPositiveInteger(element, "ASSIGNMENT-PRIORITY"))
            configuration.setDefaultRouter(self.getChildElementOptionalLiteral(element, "DEFAULT-ROUTER"))
            configuration.setEnableAnycast(self.getChildElementOptionalBooleanValue(element, "ENABLE-ANYCAST"))
            configuration.setHopCount(self.getChildElementOptionalPositiveInteger(element, "HOP-COUNT"))
            configuration.setIpAddressPrefixLength(self.getChildElementOptionalPositiveInteger(element, "IP-ADDRESS-PREFIX-LENGTH"))
            configuration.setIpv6Address(self.getChildElementOptionalLiteral(element, "IPV-6-ADDRESS"))
            configuration.setIpv6AddressSource(self.getChildElementOptionalLiteral(element, "IPV-6-ADDRESS-SOURCE"))
        return configuration

    def readNetworkEndPointNetworkEndPointAddress(self, element: ET.Element, end_point: NetworkEndpoint):
        for child_element in self.findall(element, "NETWORK-ENDPOINT-ADDRESSES/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "IPV-6-CONFIGURATION":
                end_point.addNetworkEndpointAddress(self.getIpv6Configuration(child_element))
            else:
                self.notImplemented("Unsupported Network EndPoint Address <%s>" % tag_name)

    def getDoIpEntity(self, element: ET.Element, key: str) -> DoIpEntity:
        entity = None
        child_element = self.find(element, key)
        if child_element is not None:
            entity = DoIpEntity()
            entity.setDoIpEntityRole(self.getChildElementOptionalLiteral(child_element, "DO-IP-ENTITY-ROLE"))
        return entity

    def getInfrastructureServices(self, element: ET.Element, key: str) -> InfrastructureServices:
        services = None
        child_element = self.find(element, key)
        if child_element is not None:
            services = InfrastructureServices()
            services.setDoIpEntity(self.getDoIpEntity(child_element, "DO-IP-ENTITY"))
        return services

    def readNetworkEndPoint(self, element: ET.Element, end_point: NetworkEndpoint):
        self.readIdentifiable(element, end_point)
        end_point.setInfrastructureServices(self.getInfrastructureServices(element, "INFRASTRUCTURE-SERVICES"))
        self.readNetworkEndPointNetworkEndPointAddress(element, end_point)
        end_point.setPriority(self.getChildElementOptionalPositiveInteger(element, "PRIORITY"))

    def readEthernetPhysicalChannelNetworkEndPoints(self, element: ET.Element, channel: EthernetPhysicalChannel):
        for child_element in self.findall(element, "NETWORK-ENDPOINTS/NETWORK-ENDPOINT"):
            end_point = channel.createNetworkEndPoint(self.getShortName(child_element))
            self.readNetworkEndPoint(child_element, end_point)

    def getSocketConnectionIpduIdentifier(self, element: ET.Element) -> SocketConnectionIpduIdentifier:
        identifier = None
        if element is not None:
            identifier = SocketConnectionIpduIdentifier()
            identifier.setHeaderId(self.getChildElementOptionalPositiveInteger(element, "HEADER-ID"))
            identifier.setPduCollectionSemantics(self.getChildElementOptionalLiteral(element, "PDU-COLLECTION-SEMANTICS"))
            identifier.setPduCollectionTrigger(self.getChildElementOptionalLiteral(element, "PDU-COLLECTION-TRIGGER"))
            identifier.setPduRef(self.getChildElementOptionalRefType(element, "PDU-REF"))
            identifier.setPduTriggeringRef(self.getChildElementOptionalRefType(element, "PDU-TRIGGERING-REF"))
        return identifier

    def getSocketConnectionPdus(self, element: ET.Element) -> List[SocketConnectionIpduIdentifier]:
        pdus = []
        for child_element in self.findall(element, "PDUS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "SOCKET-CONNECTION-IPDU-IDENTIFIER":
                pdus.append(self.getSocketConnectionIpduIdentifier(child_element))
            else:
                self.notImplemented("Unsupported Pdu <%s>" % tag_name)
        return pdus

    def getSocketConnection(self, element: ET.Element) -> SocketConnection:
        connection = None
        if element is not None:
            connection = SocketConnection()
            connection.setClientIpAddrFromConnectionRequest(self.getChildElementOptionalBooleanValue(element, "CLIENT-IP-ADDR-FROM-CONNECTION-REQUEST"))
            connection.setClientPortFromConnectionRequest(self.getChildElementOptionalBooleanValue(element, "CLIENT-PORT-FROM-CONNECTION-REQUEST"))
            connection.setClientPortRef(self.getChildElementOptionalRefType(element, "CLIENT-PORT-REF"))  # NOQA E501
            for pdu in self.getSocketConnectionPdus(element):
                connection.addPdu(pdu)
            connection.setPduCollectionMaxBufferSize(self.getChildElementOptionalPositiveInteger(element, "PDU-COLLECTION-MAX-BUFFER-SIZE"))
            connection.setPduCollectionTimeout(self.getChildElementOptionalTimeValue(element, "PDU-COLLECTION-TIMEOUT"))
            connection.setRuntimeIpAddressConfiguration(self.getChildElementOptionalLiteral(element, "RUNTIME-IP-ADDRESS-CONFIGURATION"))
            connection.setRuntimePortConfiguration(self.getChildElementOptionalLiteral(element, "RUNTIME-PORT-CONFIGURATION"))
            connection.setShortLabel(self.getChildElementOptionalLiteral(element, "SHORT-LABEL"))
        return connection

    def readSocketConnectionBundleConnections(self, element: ET.Element, bundle: SocketConnectionBundle):
        for child_element in self.findall(element, "BUNDLED-CONNECTIONS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "SOCKET-CONNECTION":
                bundle.addBundledConnection(self.getSocketConnection(child_element))
            else:
                self.notImplemented("Unsupported Bundled Connection <%s>" % tag_name)

    def readSocketConnectionBundle(self, element: ET.Element, bundle: SocketConnectionBundle):
        self.readSocketConnectionBundleConnections(element, bundle)
        bundle.setServerPortRef(self.getChildElementOptionalRefType(element, "SERVER-PORT-REF"))

    def readSoAdConfigConnectionBundles(self, element: ET.Element, config: SoAdConfig):
        for child_element in self.findall(element, "CONNECTION-BUNDLES/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "SOCKET-CONNECTION-BUNDLE":
                bundle = config.createSocketConnectionBundle(self.getShortName(child_element))
                self.readSocketConnectionBundle(child_element, bundle)
            else:
                self.notImplemented("Unsupported Connection Bundle <%s>" % tag_name)

    def getTpPort(self, element: ET.SubElement, key: str) -> TpPort:
        port = None
        child_element = self.find(element, key)
        if child_element is not None:
            port = TpPort()
            port.setDynamicallyAssigned(self.getChildElementOptionalBooleanValue(child_element, "DYNAMICALLY-ASSIGNED"))
            port.setPortNumber(self.getChildElementOptionalPositiveInteger(child_element, "PORT-NUMBER"))
        return port

    def readUdpTp(self, element: ET.Element, tp: UdpTp):
        tp.setUdpTpPort(self.getTpPort(element, "UDP-TP-PORT"))

    def readTcpTp(self, element: ET.Element, tp: TcpTp):
        tp.setKeepAliveInterval(self.getChildElementOptionalTimeValue(element, "KEEP-ALIVE-INTERVAL"))
        tp.setKeepAliveProbesMax(self.getChildElementOptionalPositiveInteger(element, "KEEP-ALIVE-PROBES-MAX"))
        tp.setKeepAliveTime(self.getChildElementOptionalTimeValue(element, "KEEP-ALIVE-TIME"))
        tp.setKeepAlives(self.getChildElementOptionalBooleanValue(element, "KEEP-ALIVES"))
        tp.setNaglesAlgorithm(self.getChildElementOptionalLiteral(element, "NAGLES-ALGORITHM"))
        tp.setTcpTpPort(self.getTpPort(element, "TCP-TP-PORT"))

    def readGenericTp(self, element: ET.Element, tp: GenericTp):
        tp.setTpAddress(self.getChildElementOptionalLiteral(element, "TP-ADDRESS"))
        tp.setTpTechnology(self.getChildElementOptionalLiteral(element, "TP-TECHNOLOGY"))

    def getTransportProtocolConfiguration(self, element: ET.Element, key: str) -> TransportProtocolConfiguration:
        configuration = None
        child_element = self.find(element, "%s/*" % key)
        if child_element is not None:
            tag_name = self.getTagName(child_element)
            if tag_name == "UDP-TP":
                configuration = UdpTp()
                self.readUdpTp(child_element, configuration)
            elif tag_name == "TCP-TP":
                configuration = TcpTp()
                self.readTcpTp(child_element, configuration)
            elif tag_name == "GENERIC-TP":
                configuration = GenericTp()
                self.readGenericTp(child_element, configuration)
            else:
                self.notImplemented("Unsupported TransportProtocolConfiguration <%s>" % tag_name)
        return configuration

    def readConsumedEventGroupRoutingGroupRefs(self, element: ET.Element, group: ConsumedEventGroup):
        for ref in self.getChildElementRefTypeList(element, "ROUTING-GROUP-REFS/ROUTING-GROUP-REF"):
            group.addRoutingGroupRef(ref)

    def getRequestResponseDelay(self, element: ET.Element, key: str) -> RequestResponseDelay:
        delay = None
        child_element = self.find(element, key)
        if child_element is not None:
            delay = RequestResponseDelay()
            delay.setMaxValue(self.getChildElementOptionalTimeValue(child_element, "MAX-VALUE"))
            delay.setMinValue(self.getChildElementOptionalTimeValue(child_element, "MIN-VALUE"))
        return delay

    def getSdClientConfig(self, element: ET.Element, key: str) -> SdClientConfig:
        config = None
        child_element = self.find(element, key)
        if child_element is not None:
            config = SdClientConfig()
            config.setClientServiceMajorVersion(self.getChildElementOptionalPositiveInteger(child_element, "CLIENT-SERVICE-MAJOR-VERSION"))
            config.setClientServiceMinorVersion(self.getChildElementOptionalPositiveInteger(child_element, "CLIENT-SERVICE-MINOR-VERSION"))
            config.setInitialFindBehavior(self.getInitialSdDelayConfig(child_element, "INITIAL-FIND-BEHAVIOR"))
            config.setRequestResponseDelay(self.getRequestResponseDelay(child_element, "REQUEST-RESPONSE-DELAY"))
            config.setTtl(self.getChildElementOptionalPositiveInteger(child_element, "TTL"))
        return config

    def readConsumedEventGroup(self, element: ET.Element, group: ConsumedEventGroup):
        self.readIdentifiable(element, group)
        group.setApplicationEndpointRef(self.getChildElementOptionalRefType(element, "APPLICATION-ENDPOINT-REF"))
        group.setEventGroupIdentifier(self.getChildElementOptionalPositiveInteger(element, "EVENT-GROUP-IDENTIFIER"))
        self.readConsumedEventGroupRoutingGroupRefs(element, group)
        group.setSdClientConfig(self.getSdClientConfig(element, "SD-CLIENT-CONFIG"))

    def readConsumedServiceInstanceConsumedEventGroups(self, element: ET.Element, instance: ConsumedServiceInstance):
        for child_element in self.findall(element, "CONSUMED-EVENT-GROUPS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "CONSUMED-EVENT-GROUP":
                group = instance.createConsumedEventGroup(self.getShortName(child_element))
                self.readConsumedEventGroup(child_element, group)
            else:
                self.notImplemented("Unsupported ConsumedEventGroups <%s>" % tag_name)

    def readConsumedServiceInstance(self, element: ET.Element, instance: ConsumedServiceInstance):
        self.readIdentifiable(element, instance)
        self.readConsumedServiceInstanceConsumedEventGroups(element, instance)
        instance.setProvidedServiceInstanceRef(self.getChildElementOptionalRefType(element, "PROVIDED-SERVICE-INSTANCE-REF"))
        instance.setSdClientConfig(self.getSdClientConfig(element, "SD-CLIENT-CONFIG"))

    def readSocketAddressApplicationEndpointConsumedServiceInstances(self, element: ET.Element, end_point: ApplicationEndpoint):
        for child_element in self.findall(element, "CONSUMED-SERVICE-INSTANCES/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "CONSUMED-SERVICE-INSTANCE":
                instance = end_point.createConsumedServiceInstance(self.getShortName(child_element))
                self.readConsumedServiceInstance(child_element, instance)
            else:
                self.notImplemented("Unsupported ConsumedServiceInstances <%s>" % tag_name)

    def getInitialSdDelayConfig(self, element: ET.Element, key: str) -> InitialSdDelayConfig:
        config = None
        child_element = self.find(element, key)
        if child_element is not None:
            config = InitialSdDelayConfig()
            config.setInitialDelayMaxValue(self.getChildElementOptionalTimeValue(child_element, "INITIAL-DELAY-MAX-VALUE"))
            config.setInitialDelayMinValue(self.getChildElementOptionalTimeValue(child_element, "INITIAL-DELAY-MIN-VALUE"))
            config.setInitialRepetitionsBaseDelay(self.getChildElementOptionalTimeValue(child_element, "INITIAL-REPETITIONS-BASE-DELAY"))
            config.setInitialRepetitionsMax(self.getChildElementOptionalPositiveInteger(child_element, "INITIAL-REPETITIONS-MAX"))
        return config

    def getSdServerConfig(self, element: ET.Element, key: str) -> SdServerConfig:
        config = None
        child_element = self.find(element, key)
        if child_element is not None:
            config = SdServerConfig()
            config.setInitialOfferBehavior(self.getInitialSdDelayConfig(child_element, "INITIAL-OFFER-BEHAVIOR"))
            config.setOfferCyclicDelay(self.getChildElementOptionalTimeValue(child_element, "OFFER-CYCLIC-DELAY"))
            config.setRequestResponseDelay(self.getRequestResponseDelay(child_element, "REQUEST-RESPONSE-DELAY"))
            config.setServerServiceMajorVersion(self.getChildElementOptionalPositiveInteger(child_element, "SERVER-SERVICE-MAJOR-VERSION"))
            config.setServerServiceMinorVersion(self.getChildElementOptionalPositiveInteger(child_element, "SERVER-SERVICE-MINOR-VERSION"))
            config.setTtl(self.getChildElementOptionalPositiveInteger(child_element, "TTL"))
        return config

    def readEventHandler(self, element: ET.Element, handler: EventHandler):
        self.readIdentifiable(element, handler)
        handler.setApplicationEndpointRef(self.getChildElementOptionalRefType(element, "APPLICATION-ENDPOINT-REF"))
        for ref in self.getChildElementRefTypeList(element, "CONSUMED-EVENT-GROUP-REFS/CONSUMED-EVENT-GROUP-REF"):
            handler.addConsumedEventGroupRef(ref)
        handler.setMulticastThreshold(self.getChildElementOptionalPositiveInteger(element, "MULTICAST-THRESHOLD"))
        for ref in self.getChildElementRefTypeList(element, "ROUTING-GROUP-REFS/ROUTING-GROUP-REF"):
            handler.addRoutingGroupRef(ref)
        handler.setSdServerConfig(self.getSdServerConfig(element, "SD-SERVER-CONFIG"))

    def readProvidedServiceInstanceEventHandlers(self, element: ET.Element, instance: ProvidedServiceInstance):
        for child_element in self.findall(element, "EVENT-HANDLERS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "EVENT-HANDLER":
                handler = instance.createEventHandler(self.getShortName(child_element))
                self.readEventHandler(child_element, handler)
            else:
                self.notImplemented("Unsupported Event Handler <%s>" % tag_name)

    def readProvidedServiceInstance(self, element: ET.Element, instance: ProvidedServiceInstance):
        self.readIdentifiable(element, instance)
        self.readProvidedServiceInstanceEventHandlers(element, instance)
        instance.setInstanceIdentifier(self.getChildElementOptionalPositiveInteger(element, "INSTANCE-IDENTIFIER"))
        instance.setLoadBalancingPriority(self.getChildElementOptionalPositiveInteger(element, "LOAD-BALANCING-PRIORITY"))
        instance.setLoadBalancingWeight(self.getChildElementOptionalPositiveInteger(element, "LOAD-BALANCING-WEIGHT"))
        for ref in self.getChildElementRefTypeList(element, "LOCAL-UNICAST-ADDRESSS/APPLICATION-ENDPOINT-REF-CONDITIONAL/APPLICATION-ENDPOINT-REF"):
            instance.addLocalUnicastAddressRef(ref)
        instance.setMinorVersion(self.getChildElementOptionalPositiveInteger(element, "MINOR-VERSION"))
        instance.setPriority(self.getChildElementOptionalPositiveInteger(element, "PRIORITY"))
        for ref in self.getChildElementRefTypeList(element, "REMOTE-MULTICAST-SUBSCRIPTION-ADDRESSS/APPLICATION-ENDPOINT-REF-CONDITIONAL/APPLICATION-ENDPOINT-REF"):
            instance.addRemoteMulticastSubscriptionAddressRef(ref)
        for ref in self.getChildElementRefTypeList(element, "REMOTE-UNICAST-ADDRESSS/APPLICATION-ENDPOINT-REF-CONDITIONAL/APPLICATION-ENDPOINT-REF"):
            instance.addRemoteUnicastAddressRef(ref)
        instance.setSdServerConfig(self.getSdServerConfig(element, "SD-SERVER-CONFIG"))
        instance.setSdServerTimerConfigRef(
            self.getChildElementOptionalRefType(element, "SD-SERVER-TIMER-CONFIGS/SOMEIP-SD-SERVER-SERVICE-INSTANCE-CONFIG-REF-CONDITIONAL/SOMEIP-SD-SERVER-SERVICE-INSTANCE-CONFIG-REF")
        )
        for ref in self.getChildElementRefTypeList(element, "ALLOWED-SERVICE-CONSUMERS/NETWORK-ENDPOINT-REF-CONDITIONAL/NETWORK-ENDPOINT-REF"):
            instance.addAllowedServiceConsumerRef(ref)
        instance.setAutoAvailable(self.getChildElementOptionalBooleanValue(element, "AUTO-AVAILABLE"))
        instance.setServiceIdentifier(self.getChildElementOptionalPositiveInteger(element, "SERVICE-IDENTIFIER"))

    def readSocketAddressApplicationEndpointProvidedServiceInstance(self, element: ET.Element, end_point: ApplicationEndpoint):
        for child_element in self.findall(element, "PROVIDED-SERVICE-INSTANCES/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "PROVIDED-SERVICE-INSTANCE":
                instance = end_point.createProvidedServiceInstance(self.getShortName(child_element))
                self.readProvidedServiceInstance(child_element, instance)
            else:
                self.notImplemented("Unsupported ConsumedServiceInstances <%s>" % tag_name)

    def readSocketAddressApplicationEndpoint(self, element: ET.Element, address: SocketAddress):
        child_element = self.find(element, "APPLICATION-ENDPOINT")
        if child_element is not None:
            end_point = address.createApplicationEndpoint(self.getShortName(child_element))
            self.readSocketAddressApplicationEndpointConsumedServiceInstances(child_element, end_point)
            end_point.setNetworkEndpointRef(self.getChildElementOptionalRefType(child_element, "NETWORK-ENDPOINT-REF"))
            end_point.setPriority(self.getChildElementOptionalPositiveInteger(child_element, "PRIORITY"))
            self.readSocketAddressApplicationEndpointProvidedServiceInstance(child_element, end_point)
            end_point.setTpConfiguration(self.getTransportProtocolConfiguration(child_element, "TP-CONFIGURATION"))

    def readSocketAddressMulticastConnectorRefs(self, element: ET.Element, address: SocketAddress):
        for ref in self.getChildElementRefTypeList(element, "MULTICAST-CONNECTOR-REFS/MULTICAST-CONNECTOR-REF"):
            address.addMulticastConnectorRef(ref)

    def readSocketAddress(self, element: ET.Element, address: SocketAddress):
        self.readIdentifiable(element, address)
        self.readSocketAddressApplicationEndpoint(element, address)
        self.readSocketAddressMulticastConnectorRefs(element, address)
        address.setConnectorRef(self.getChildElementOptionalRefType(element, "CONNECTOR-REF"))
        address.setPortAddress(self.getChildElementOptionalPositiveInteger(element, "PORT-ADDRESS"))

    def readSoAdConfigSocketAddresses(self, element: ET.Element, config: SoAdConfig):
        for child_element in self.findall(element, "SOCKET-ADDRESSS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "SOCKET-ADDRESS":
                address = config.createSocketAddress(self.getShortName(child_element))
                self.readSocketAddress(child_element, address)
            else:
                self.notImplemented("Unsupported Socket Address <%s>" % tag_name)

    def getSoAdConfig(self, element: ET.Element, key: str) -> SoAdConfig:
        child_element = self.find(element, key)
        config = None
        if child_element is not None:
            config = SoAdConfig()
            self.readSoAdConfigConnectionBundles(child_element, config)
            self.readSoAdConfigSocketAddresses(child_element, config)
        return config

    def readEthernetPhysicalChannelVlan(self, element: ET.Element, channel: EthernetPhysicalChannel):
        child_element = self.find(element, "VLAN")
        if child_element is not None:
            vlan = channel.createVlanConfig(self.getShortName(child_element))
            vlan.setVlanIdentifier(self.getChildElementOptionalPositiveInteger(child_element, "VLAN-IDENTIFIER"))

    def readEthernetPhysicalChannel(self, element: ET.Element, channel: EthernetPhysicalChannel):
        self.readPhysicalChannel(element, channel)
        self.readEthernetPhysicalChannelNetworkEndPoints(element, channel)
        channel.setSoAdConfig(self.getSoAdConfig(element, "SO-AD-CONFIG"))
        self.readEthernetPhysicalChannelVlan(element, channel)

    def readFlexrayPhysicalChannel(self, element: ET.Element, channel: FlexrayPhysicalChannel):
        self.readPhysicalChannel(element, channel)
        channel.setChannelName(self.getChildElementOptionalLiteral(element, "CHANNEL-NAME"))

    def readCommunicationClusterPhysicalChannels(self, element: ET.Element, cluster: CommunicationCluster):
        for child_element in self.findall(element, "PHYSICAL-CHANNELS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "CAN-PHYSICAL-CHANNEL":
                channel = cluster.createCanPhysicalChannel(self.getShortName(child_element))
                self.readCanPhysicalChannel(child_element, channel)
            elif tag_name == "LIN-PHYSICAL-CHANNEL":
                channel = cluster.createLinPhysicalChannel(self.getShortName(child_element))
                self.readLinPhysicalChannel(child_element, channel)
            elif tag_name == "ETHERNET-PHYSICAL-CHANNEL":
                channel = cluster.createEthernetPhysicalChannel(self.getShortName(child_element))
                self.readEthernetPhysicalChannel(child_element, channel)
            elif tag_name == "FLEXRAY-PHYSICAL-CHANNEL":
                channel = cluster.createFlexrayPhysicalChannel(self.getShortName(child_element))
                self.readFlexrayPhysicalChannel(child_element, channel)
            else:
                self.notImplemented("Unsupported Physical Channel <%s>" % tag_name)

    def readCommunicationCluster(self, element: ET.Element, cluster: CommunicationCluster):
        cluster.setBaudrate(self.getChildElementOptionalNumericalValue(element, "BAUDRATE"))
        self.readCommunicationClusterPhysicalChannels(element, cluster)
        cluster.setProtocolName(self.getChildElementOptionalLiteral(element, "PROTOCOL-NAME"))
        cluster.setProtocolVersion(self.getChildElementOptionalLiteral(element, "PROTOCOL-VERSION"))

    def getCanClusterBusOffRecovery(self, element: ET.Element, key: str) -> CanClusterBusOffRecovery:
        recovery = None
        child_element = self.find(element, key)
        if child_element is not None:
            recovery = CanClusterBusOffRecovery()
            recovery.setBorCounterL1ToL2(self.getChildElementOptionalPositiveInteger(child_element, "BOR-COUNTER-L-1-TO-L-2"))
            recovery.setBorTimeL1(self.getChildElementOptionalTimeValue(child_element, "BOR-TIME-L-1"))
            recovery.setBorTimeL2(self.getChildElementOptionalTimeValue(child_element, "BOR-TIME-L-2"))
        return recovery

    def readAbstractCanCluster(self, element: ET.Element, cluster: AbstractCanCluster):
        self.readCommunicationCluster(element, cluster)
        cluster.setBusOffRecovery(self.getCanClusterBusOffRecovery(element, "BUS-OFF-RECOVERY"))
        cluster.setCanFdBaudrate(self.getChildElementOptionalNumericalValue(element, "CAN-FD-BAUDRATE"))
        cluster.setCanXlBaudrate(self.getChildElementOptionalNumericalValue(element, "CAN-XL-BAUDRATE"))

    def readLinCluster(self, element: ET.Element, cluster: LinCluster):
        self.logger.debug("Read LinCluster <%s>" % cluster.getShortName())
        self.readIdentifiable(element, cluster)
        child_element = self.find(element, "LIN-CLUSTER-VARIANTS/LIN-CLUSTER-CONDITIONAL")
        if child_element is not None:
            self.readCommunicationCluster(child_element, cluster)

    def readCanCluster(self, element: ET.Element, cluster: CanCluster):
        self.logger.debug("Read CanCluster <%s>" % cluster.getShortName())
        self.readIdentifiable(element, cluster)
        child_element = self.find(element, "CAN-CLUSTER-VARIANTS/CAN-CLUSTER-CONDITIONAL")
        if child_element is not None:
            self.readAbstractCanCluster(child_element, cluster)

    def readFlexrayCluster(self, element: ET.Element, cluster: FlexrayCluster):
        self.logger.debug("Read FlexrayCluster <%s>" % cluster.getShortName())
        self.readIdentifiable(element, cluster)
        child_element = self.find(element, "FLEXRAY-CLUSTER-VARIANTS/FLEXRAY-CLUSTER-CONDITIONAL")
        if child_element is not None:
            self.readCommunicationCluster(child_element, cluster)
            cluster.setActionPointOffset(self.getChildElementOptionalIntegerValue(child_element, "ACTION-POINT-OFFSET"))
            cluster.setBit(self.getChildElementOptionalTimeValue(child_element, "BIT"))
            cluster.setCasRxLowMax(self.getChildElementOptionalIntegerValue(child_element, "CAS-RX-LOW-MAX"))
            cluster.setColdStartAttempts(self.getChildElementOptionalIntegerValue(child_element, "COLD-START-ATTEMPTS"))
            cluster.setCycle(self.getChildElementOptionalTimeValue(child_element, "CYCLE"))
            cluster.setCycleCountMax(self.getChildElementOptionalIntegerValue(child_element, "CYCLE-COUNT-MAX"))
            cluster.setDetectNitError(self.getChildElementOptionalBooleanValue(child_element, "DETECT-NIT-ERROR"))
            cluster.setDynamicSlotIdlePhase(self.getChildElementOptionalIntegerValue(child_element, "DYNAMIC-SLOT-IDLE-PHASE"))
            cluster.setIgnoreAfterTx(self.getChildElementOptionalIntegerValue(child_element, "IGNORE-AFTER-TX"))
            cluster.setListenNoise(self.getChildElementOptionalIntegerValue(child_element, "LISTEN-NOISE"))
            cluster.setMacroPerCycle(self.getChildElementOptionalIntegerValue(child_element, "MACRO-PER-CYCLE"))
            cluster.setMacrotickDuration(self.getChildElementOptionalTimeValue(child_element, "MACROTICK-DURATION"))
            cluster.setMaxWithoutClockCorrectionFatal(self.getChildElementOptionalIntegerValue(child_element, "MAX-WITHOUT-CLOCK-CORRECTION-FATAL"))
            cluster.setMaxWithoutClockCorrectionPassive(self.getChildElementOptionalIntegerValue(child_element, "MAX-WITHOUT-CLOCK-CORRECTION-PASSIVE"))
            cluster.setMinislotActionPointOffset(self.getChildElementOptionalIntegerValue(child_element, "MINISLOT-ACTION-POINT-OFFSET"))
            cluster.setMinislotDuration(self.getChildElementOptionalIntegerValue(child_element, "MINISLOT-DURATION"))
            cluster.setNetworkIdleTime(self.getChildElementOptionalIntegerValue(child_element, "NETWORK-IDLE-TIME"))
            cluster.setNetworkManagementVectorLength(self.getChildElementOptionalIntegerValue(child_element, "NETWORK-MANAGEMENT-VECTOR-LENGTH"))
            cluster.setNumberOfMinislots(self.getChildElementOptionalIntegerValue(child_element, "NUMBER-OF-MINISLOTS"))
            cluster.setNumberOfStaticSlots(self.getChildElementOptionalIntegerValue(child_element, "NUMBER-OF-STATIC-SLOTS"))
            cluster.setOffsetCorrectionStart(self.getChildElementOptionalIntegerValue(child_element, "OFFSET-CORRECTION-START"))
            cluster.setPayloadLengthStatic(self.getChildElementOptionalIntegerValue(child_element, "PAYLOAD-LENGTH-STATIC"))
            cluster.setSafetyMargin(self.getChildElementOptionalIntegerValue(child_element, "SAFETY-MARGIN"))
            cluster.setSampleClockPeriod(self.getChildElementOptionalTimeValue(child_element, "SAMPLE-CLOCK-PERIOD"))
            cluster.setStaticSlotDuration(self.getChildElementOptionalIntegerValue(child_element, "STATIC-SLOT-DURATION"))
            cluster.setSymbolWindow(self.getChildElementOptionalIntegerValue(child_element, "SYMBOL-WINDOW"))
            cluster.setSymbolWindowActionPointOffset(self.getChildElementOptionalIntegerValue(child_element, "SYMBOL-WINDOW-ACTION-POINT-OFFSET"))
            cluster.setSyncFrameIdCountMax(self.getChildElementOptionalIntegerValue(child_element, "SYNC-FRAME-ID-COUNT-MAX"))
            cluster.setTranceiverStandbyDelay(self.getChildElementOptionalFloatValue(child_element, "TRANCEIVER-STANDBY-DELAY"))
            cluster.setTransmissionStartSequenceDuration(self.getChildElementOptionalIntegerValue(child_element, "TRANSMISSION-START-SEQUENCE-DURATION"))
            cluster.setWakeupRxIdle(self.getChildElementOptionalIntegerValue(child_element, "WAKEUP-RX-IDLE"))
            cluster.setWakeupRxLow(self.getChildElementOptionalIntegerValue(child_element, "WAKEUP-RX-LOW"))
            cluster.setWakeupRxWindow(self.getChildElementOptionalIntegerValue(child_element, "WAKEUP-RX-WINDOW"))
            cluster.setWakeupTxActive(self.getChildElementOptionalIntegerValue(child_element, "WAKEUP-TX-ACTIVE"))
            cluster.setWakeupTxIdle(self.getChildElementOptionalIntegerValue(child_element, "WAKEUP-TX-IDLE"))  # noqa E501

    def readMacMulticastGroup(self, element: ET.Element, group: MacMulticastGroup):
        self.readIdentifiable(element, group)
        group.setMacMulticastAddress(
            self.getChildElementOptionalLiteral(
                element,
                "MAC-MULTICAST-ADDRESS",
            )
        )

    def readEthernetClusterMacMulticastGroups(self, element: ET.Element, cluster: EthernetCluster):
        for child_element in self.findall(element, "MAC-MULTICAST-GROUPS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "MAC-MULTICAST-GROUP":
                group = cluster.createMacMulticastGroup(self.getShortName(child_element))
                self.readMacMulticastGroup(child_element, group)
            else:
                self.notImplemented("Unsupported assigned data type <%s>" % tag_name)

    def readEthernetCluster(self, element: ET.Element, cluster: EthernetCluster):
        self.logger.debug("Read EthernetCluster <%s>" % cluster.getShortName())
        self.readIdentifiable(element, cluster)
        child_element = self.find(element, "ETHERNET-CLUSTER-VARIANTS/ETHERNET-CLUSTER-CONDITIONAL")
        if child_element is not None:
            self.readCommunicationCluster(child_element, cluster)
            self.readEthernetClusterMacMulticastGroups(child_element, cluster)

    def readDiagnosticConnectionFunctionalRequestRefs(self, element: ET.Element, connection: DiagnosticConnection):
        for ref in self.getChildElementRefTypeList(element, "FUNCTIONAL-REQUEST-REFS/FUNCTIONAL-REQUEST-REF"):
            connection.addFunctionalRequestRef(ref)

    def readDiagnosticConnection(self, element: ET.Element, connection: DiagnosticConnection):
        self.logger.debug("Read DiagnosticConnection <%s>" % connection.getShortName())
        self.readIdentifiable(element, connection)
        self.readDiagnosticConnectionFunctionalRequestRefs(element, connection)
        connection.setPhysicalRequestRef(self.getChildElementOptionalRefType(element, "PHYSICAL-REQUEST-REF"))
        connection.setResponseOnEventRef(self.getChildElementOptionalRefType(element, "RESPONSE-REF"))

    def readDiagnosticServiceTableDiagnosticConnectionRefs(self, element: ET.Element, table: DiagnosticServiceTable):
        for ref in self.getChildElementRefTypeList(element, "DIAGNOSTIC-CONNECTIONS/DIAGNOSTIC-CONNECTION-REF-CONDITIONAL/DIAGNOSTIC-CONNECTION-REF"):
            table.addDiagnosticConnectionRef(ref)

    def readDiagnosticServiceTable(self, element: ET.Element, table: DiagnosticServiceTable):
        self.logger.debug("Read DiagnosticServiceTable <%s>" % table.getShortName())
        self.readIdentifiable(element, table)
        self.readDiagnosticServiceTableDiagnosticConnectionRefs(element, table)
        table.setEcuInstanceRef(self.getChildElementOptionalRefType(element, "ECU-INSTANCE-REF"))

    def readSegmentPosition(self, element: ET.Element, position: SegmentPosition):
        position.setSegmentByteOrder(self.getChildElementOptionalLiteral(element, "SEGMENT-BYTE-ORDER"))
        position.setSegmentLength(self.getChildElementOptionalIntegerValue(element, "SEGMENT-LENGTH"))
        position.setSegmentPosition(self.getChildElementOptionalIntegerValue(element, "SEGMENT-POSITION"))

    def readMultiplexedPartSegmentPositions(self, element: ET.Element, part: MultiplexedPart):
        for child_element in self.findall(element, "SEGMENT-POSITIONS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "SEGMENT-POSITION":
                position = SegmentPosition()
                self.readSegmentPosition(child_element, position)
                part.addSegmentPosition(position)
            else:
                self.notImplemented("Unsupported DynamicPart <%s>" % tag_name)

    def readMultiplexedPart(self, element: ET.Element, part: MultiplexedPart):
        self.readMultiplexedPartSegmentPositions(element, part)

    def readDynamicPartAlternative(self, element: ET.Element, alternative: DynamicPartAlternative):
        alternative.setIPduRef(self.getChildElementOptionalRefType(element, "I-PDU-REF"))
        alternative.setInitialDynamicPart(self.getChildElementOptionalBooleanValue(element, "INITIAL-DYNAMIC-PART"))
        alternative.setSelectorFieldCode(self.getChildElementOptionalIntegerValue(element, "SELECTOR-FIELD-CODE"))

    def readDynamicPartDynamicPartAlternatives(self, element: ET.Element, part: DynamicPart):
        for child_element in self.findall(element, "DYNAMIC-PART-ALTERNATIVES/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "DYNAMIC-PART-ALTERNATIVE":
                alternative = DynamicPartAlternative()
                self.readDynamicPartAlternative(child_element, alternative)
                part.addDynamicPartAlternative(alternative)
            else:
                self.notImplemented("Unsupported DynamicPartAlternative <%s>" % tag_name)

    def readDynamicPart(self, element: ET.Element, part: DynamicPart):
        self.readMultiplexedPart(element, part)
        self.readDynamicPartDynamicPartAlternatives(element, part)

    def readMultiplexedIPduDynamicParts(self, element: ET.Element, ipdu: MultiplexedIPdu):
        for child_element in self.findall(element, "DYNAMIC-PARTS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "DYNAMIC-PART":
                part = DynamicPart()
                self.readDynamicPart(child_element, part)
                ipdu.setDynamicPart(part)
            else:
                self.notImplemented("Unsupported DynamicPart <%s>" % tag_name)

    def readStaticPart(self, element: ET.Element, part: StaticPart):
        self.readMultiplexedPart(element, part)
        part.setIPduRef(self.getChildElementOptionalRefType(element, "I-PDU-REF"))

    def readMultiplexedIPduStaticParts(self, element: ET.Element, ipdu: MultiplexedIPdu):
        for child_element in self.findall(element, "STATIC-PARTS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "STATIC-PART":
                part = StaticPart()
                self.readStaticPart(child_element, part)
                ipdu.setStaticPart(part)
            else:
                self.notImplemented("Unsupported StaticPart <%s>" % tag_name)

    def readMultiplexedIPdu(self, element: ET.Element, ipdu: MultiplexedIPdu):
        self.logger.debug("Read MultiplexedIPdu <%s>" % ipdu.getShortName())
        self.readIPdu(element, ipdu)
        self.readMultiplexedIPduDynamicParts(element, ipdu)
        ipdu.setSelectorFieldByteOrder(self.getChildElementOptionalLiteral(element, "SELECTOR-FIELD-BYTE-ORDER"))
        ipdu.setSelectorFieldLength(self.getChildElementOptionalIntegerValue(element, "SELECTOR-FIELD-LENGTH"))
        ipdu.setSelectorFieldStartPosition(self.getChildElementOptionalIntegerValue(element, "SELECTOR-FIELD-START-POSITION"))
        self.readMultiplexedIPduStaticParts(element, ipdu)
        ipdu.setTriggerMode(self.getChildElementOptionalLiteral(element, "TRIGGER-MODE"))
        ipdu.setUnusedBitPattern(self.getChildElementOptionalIntegerValue(element, "UNUSED-BIT-PATTERN"))

    def readUserDefinedIPdu(self, element: ET.Element, ipdu: UserDefinedIPdu):
        self.logger.debug("Read UserDefinedIPdu <%s>" % ipdu.getShortName())
        self.readIPdu(element, ipdu)
        ipdu.setCddType(self.getChildElementOptionalLiteral(element, "CDD-TYPE"))

    def readUserDefinedPdu(self, element: ET.Element, pdu: UserDefinedPdu):
        self.logger.debug("Read UserDefinedPdu <%s>" % pdu.getShortName())
        self.readPdu(element, pdu)
        pdu.setCddType(self.getChildElementOptionalLiteral(element, "CDD-TYPE"))

    def readGeneralPurposePdu(self, element: ET.Element, pdu: GeneralPurposePdu):
        self.logger.debug("Read GeneralPurposePdu <%s>" % pdu.getShortName())
        self.readPdu(element, pdu)

    def readGeneralPurposeIPdu(self, element: ET.Element, i_pdu: GeneralPurposeIPdu):
        self.logger.debug("Read GeneralPurposeIPdu <%s>" % i_pdu.getShortName())
        self.readIPdu(element, i_pdu)

    def readSecureCommunicationAuthenticationProps(self, element: ET.Element, props: SecureCommunicationAuthenticationProps):
        self.readIdentifiable(element, props)
        props.setAuthInfoTxLength(self.getChildElementOptionalPositiveInteger(element, "AUTH-INFO-TX-LENGTH"))

    def readSecureCommunicationPropsSetAuthenticationProps(self, element: ET.Element, props_set: SecureCommunicationPropsSet):
        for child_element in self.findall(element, "AUTHENTICATION-PROPSS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "SECURE-COMMUNICATION-AUTHENTICATION-PROPS":
                props = props_set.createSecureCommunicationAuthenticationProps(self.getShortName(child_element))
                self.readSecureCommunicationAuthenticationProps(child_element, props)
            else:
                self.notImplemented("Unsupported AuthenticationProps <%s>" % tag_name)

    def readSecureCommunicationFreshnessProps(self, element: ET.Element, props: SecureCommunicationFreshnessProps):
        self.readIdentifiable(element, props)
        props.setFreshnessCounterSyncAttempts(self.getChildElementOptionalPositiveInteger(element, "FRESHNESS-COUNTER-SYNC-ATTEMPTS"))
        props.setFreshnessTimestampTimePeriodFactor(self.getChildElementOptionalPositiveInteger(element, "FRESHNESS-TIMESTAMP-TIME-PERIOD-FACTOR"))
        props.setFreshnessValueLength(self.getChildElementOptionalPositiveInteger(element, "FRESHNESS-VALUE-LENGTH"))
        props.setFreshnessValueTxLength(self.getChildElementOptionalPositiveInteger(element, "FRESHNESS-VALUE-TX-LENGTH"))
        props.setUseFreshnessTimestamp(self.getChildElementOptionalBooleanValue(element, "USE-FRESHNESS-TIMESTAMP"))

    def readSecureCommunicationPropsSetFreshnessProps(self, element: ET.Element, props_set: SecureCommunicationPropsSet):
        for child_element in self.findall(element, "FRESHNESS-PROPSS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "SECURE-COMMUNICATION-FRESHNESS-PROPS":
                props = props_set.createSecureCommunicationFreshnessProps(self.getShortName(child_element))
                self.readSecureCommunicationFreshnessProps(child_element, props)
            else:
                self.notImplemented("Unsupported FreshnessProps <%s>" % tag_name)

    def readSecureCommunicationPropsSet(self, element: ET.Element, props_set: SecureCommunicationPropsSet):
        self.logger.debug("Read SecureCommunicationPropsSet <%s>" % props_set.getShortName())
        self.readIdentifiable(element, props_set)
        self.readSecureCommunicationPropsSetAuthenticationProps(element, props_set)
        self.readSecureCommunicationPropsSetFreshnessProps(element, props_set)

    def readSoAdRoutingGroup(self, element: ET.Element, group: SoAdRoutingGroup):
        self.logger.debug("Read SoAdRoutingGroup <%s>" % group.getShortName())
        self.readIdentifiable(element, group)
        group.setEventGroupControlType(self.getChildElementOptionalLiteral(element, "EVENT-GROUP-CONTROL-TYPE"))

    def readDoIpLogicAddress(self, element: ET.Element, address: DoIpLogicAddress):
        self.readIdentifiable(element, address)
        address.setAddress(self.getChildElementOptionalIntegerValue(element, "ADDRESS"))

    def readDoIpTpConfigDoIpLogicAddresses(self, element: ET.Element, config: DoIpTpConfig):
        for child_element in self.findall(element, "DO-IP-LOGIC-ADDRESSS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "DO-IP-LOGIC-ADDRESS":
                address = config.createDoIpLogicAddress(self.getShortName(child_element))
                self.readDoIpLogicAddress(child_element, address)
            else:
                self.notImplemented("Unsupported DoIpLogicAddress <%s>" % tag_name)

    def readDoIpTpConnection(self, element: ET.Element, connection: DoIpTpConnection):
        self.readTpConnection(element, connection)
        connection.setDoIpSourceAddressRef(self.getChildElementOptionalRefType(element, "DO-IP-SOURCE-ADDRESS-REF"))
        connection.setDoIpTargetAddressRef(self.getChildElementOptionalRefType(element, "DO-IP-TARGET-ADDRESS-REF"))
        connection.setTpSduRef(self.getChildElementOptionalRefType(element, "TP-SDU-REF"))

    def readDoIpTpConfigTpConnections(self, element: ET.Element, config: DoIpTpConfig):
        for child_element in self.findall(element, "TP-CONNECTIONS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "DO-IP-TP-CONNECTION":
                connection = DoIpTpConnection()
                self.readDoIpTpConnection(child_element, connection)
                config.addTpConnection(connection)
            else:
                self.notImplemented("Unsupported TpConnection <%s>" % tag_name)

    def readDoIpTpConfig(self, element: ET.Element, config: DoIpTpConfig):
        self.logger.debug("Read DoIpTpConfig <%s>" % config.getShortName())
        self.readTpConfig(element, config)
        self.readDoIpTpConfigDoIpLogicAddresses(element, config)
        self.readDoIpTpConfigTpConnections(element, config)

    def readHwDescriptionEntityHwCategoryRefs(self, element: ET.Element, entity: HwDescriptionEntity):
        for ref in self.getChildElementRefTypeList(element, "HW-CATEGORY-REFS/HW-CATEGORY-REF"):
            entity.addHwCategoryRef(ref)

    def readHwAttributeValue(self, element: ET.Element, attribute_value: HwAttributeValue):
        self.readARObjectAttributes(element, attribute_value)
        attribute_value.setHwAttributeDefRef(self.getChildElementOptionalRefType(element, "HW-ATTRIBUTE-DEF-REF"))

    def readHwDescriptionEntityHwAttributeValues(self, element: ET.Element, entity: HwDescriptionEntity):
        for child_element in self.findall(element, "HW-ATTRIBUTE-VALUES/HW-ATTRIBUTE-VALUE"):
            attribute_value = HwAttributeValue()
            self.readHwAttributeValue(child_element, attribute_value)
            entity.addHwAttributeValue(attribute_value)

    def readHwDescriptionEntity(self, element: ET.Element, entity: HwDescriptionEntity):
        self.readReferrable(element, entity)
        entity.setHwTypeRef(self.getChildElementOptionalRefType(element, "HW-TYPE-REF"))
        self.readHwDescriptionEntityHwCategoryRefs(element, entity)
        self.readHwDescriptionEntityHwAttributeValues(element, entity)

    def readHwPinGroup(self, element: ET.SubElement, pin_group: HwPinGroup):
        self.readHwDescriptionEntity(element, pin_group)

    def readHwPin(self, element: ET.Element, hw_pin: HwPin):
        self.readHwDescriptionEntity(element, hw_pin)
        for function_name_element in self.findall(element, "FUNCTION-NAMES/FUNCTION-NAME"):
            if function_name_element.text is not None:
                hw_pin.addFunctionName(function_name_element.text)
        packaging_pin_name_element = self.find(element, "PACKAGING-PIN-NAME")
        if packaging_pin_name_element is not None and packaging_pin_name_element.text is not None:
            hw_pin.setPackagingPinName(packaging_pin_name_element.text)
        hw_pin.setPinNumber(self.getChildElementOptionalIntegerValue(element, "PIN-NUMBER"))

    def readHwElementHwPinGroups(self, element: ET.Element, hw_element: HwElement):
        for child_element in self.findall(element, "HW-PIN-GROUPS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "HW-PIN-GROUP":
                pin_group = hw_element.createHwPinGroup(self.getShortName(child_element))
                self.readHwPinGroup(child_element, pin_group)
            else:
                self.notImplemented("Unsupported Hw Pin Group <%s>" % tag_name)

    def readHwPinConnector(self, element: ET.Element) -> HwPinConnector:
        pin = HwPinConnector()
        self.readDescribable(element, pin)
        for ref in self.getChildElementRefTypeList(element, "HW-PIN-REF"):
            pin.addHwPinRef(ref)
        return pin

    def readHwPinGroupConnector(self, element: ET.Element) -> HwPinGroupConnector:
        group = HwPinGroupConnector()
        self.readDescribable(element, group)
        for child_element in self.findall(element, "HW-PIN-CONNECTION"):
            group.addHwPinConnection(self.readHwPinConnector(child_element))
        for ref in self.getChildElementRefTypeList(element, "HW-PIN-GROUP-REF"):
            group.addHwPinGroupRef(ref)
        return group

    def readHwElementConnector(self, element: ET.Element, connector: HwElementConnector):
        self.readDescribable(element, connector)
        for ref in self.getChildElementRefTypeList(element, "HW-ELEMENT-REF"):
            connector.addHwElementRef(ref)
        for child_element in self.findall(element, "HW-PIN-CONNECTION"):
            connector.addHwPinConnection(self.readHwPinConnector(child_element))
        for child_element in self.findall(element, "HW-PIN-GROUP-CONNECTION"):
            connector.addHwPinGroupConnection(self.readHwPinGroupConnector(child_element))

    def readHwElementHwElementConnections(self, element: ET.Element, hw_element: HwElement):
        for child_element in self.findall(element, "HW-ELEMENT-CONNECTIONS/HW-ELEMENT-CONNECTOR"):
            connector = HwElementConnector()
            self.readHwElementConnector(child_element, connector)
            hw_element.addHwElementConnection(connector)

    def readHwElementHwNestedElementRefs(self, element: ET.Element, hw_element: HwElement):
        refs = self.getChildElementRefTypeList(element, "NESTED-ELEMENTS/HW-ELEMENT-REF-CONDITIONAL/HW-ELEMENT-REF")
        if len(refs) == 0:
            refs = self.getChildElementRefTypeList(element, "NESTED-ELEMENTS/HW-ELEMENT-REF")
        for ref in refs:
            hw_element.addNestedElementRef(ref)

    def readHwElement(self, element: ET.Element, hw_element: HwElement):
        self.logger.debug("Read HwElement <%s>" % hw_element.getShortName())
        self.readHwDescriptionEntity(element, hw_element)
        self.readHwElementHwPinGroups(element, hw_element)
        self.readHwElementHwElementConnections(element, hw_element)
        self.readHwElementHwNestedElementRefs(element, hw_element)

    def readHwAttributeDef(self, element: ET.Element, attribute_def: HwAttributeDef):
        self.readIdentifiable(element, attribute_def)
        attribute_def.setIsRequired(self.getChildElementOptionalBooleanValue(element, "IS-REQUIRED"))
        attribute_def.setUnitRef(self.getChildElementOptionalRefType(element, "UNIT-REF"))
        for child_element in self.findall(element, "HW-ATTRIBUTE-LITERALS/HW-ATTRIBUTE-LITERAL-DEF"):
            literal_def = attribute_def.createHwAttributeLiteral(self.getShortName(child_element))
            self.readHwAttributeLiteralDef(child_element, literal_def)

    def readHwAttributeLiteralDef(self, element: ET.Element, literal_def):
        self.readIdentifiable(element, literal_def)
        literal_def.setValue(self.getChildElementOptionalString(element, "VALUE"))

    def readHwCategoryHwAttributeDef(self, element: ET.Element, hw_category: HwCategory):
        for child_element in self.findall(element, "HW-ATTRIBUTE-DEFS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "HW-ATTRIBUTE-DEF":
                pin_group = hw_category.createHwAttributeDef(self.getShortName(child_element))
                self.readHwAttributeDef(child_element, pin_group)
            else:
                self.notImplemented("Unsupported Hw Attribute Defs <%s>" % tag_name)

    def readHwCategory(self, element: ET.Element, hw_category: HwCategory):
        self.logger.debug("Read HwCategory <%s>" % hw_category.getShortName())
        self.readARElement(element, hw_category)
        self.readHwCategoryHwAttributeDef(element, hw_category)

    def readHwType(self, element: ET.Element, type: HwType):
        self.logger.debug("Read HwType <%s>" % type.getShortName())
        self.readReferrable(element, type)

    def readPduToFrameMappings(self, element: ET.Element, parent: Frame):
        for child_element in self.findall(element, "PDU-TO-FRAME-MAPPINGS/PDU-TO-FRAME-MAPPING"):
            short_name = self.getShortName(child_element)
            self.logger.debug("readPduToFrameMapping %s" % short_name)
            mapping = parent.createPduToFrameMapping(short_name)
            self.readIdentifiable(child_element, mapping)
            mapping.packingByteOrder = self.getChildElementOptionalLiteral(child_element, "PACKING-BYTE-ORDER")
            mapping.pduRef = self.getChildElementOptionalRefType(child_element, "PDU-REF")
            mapping.startPosition = self.getChildElementOptionalNumericalValue(child_element, "START-POSITION")

    def readFrame(self, element: ET.Element, frame: Frame):
        self.readIdentifiable(element, frame)
        frame.frameLength = self.getChildElementOptionalNumericalValue(element, "FRAME-LENGTH")
        self.readPduToFrameMappings(element, frame)

    def readLinUnconditionalFrame(self, element: ET.Element, frame: LinUnconditionalFrame):
        self.logger.debug("Read LinUnconditionalFrame <%s>" % frame.getShortName())
        self.readFrame(element, frame)

    def readPdu(self, element: ET.Element, pdu: Pdu):
        self.readIdentifiable(element, pdu)
        pdu.setHasDynamicLength(self.getChildElementOptionalBooleanValue(element, "HAS-DYNAMIC-LENGTH"))
        pdu.setLength(self.getChildElementOptionalNumericalValue(element, "LENGTH"))

    def readISignalToIPduMapping(self, element: ET.Element, mapping: ISignalToIPduMapping):
        self.readIdentifiable(element, mapping)
        mapping.setISignalRef(self.getChildElementOptionalRefType(element, "I-SIGNAL-REF"))
        mapping.setISignalGroupRef(self.getChildElementOptionalRefType(element, "I-SIGNAL-GROUP-REF"))
        mapping.setPackingByteOrder(self.getChildElementOptionalLiteral(element, "PACKING-BYTE-ORDER"))
        mapping.setStartPosition(self.getChildElementOptionalIntegerValue(element, "START-POSITION"))
        mapping.setTransferProperty(self.getChildElementOptionalLiteral(element, "TRANSFER-PROPERTY"))
        mapping.setUpdateIndicationBitPosition(self.getChildElementOptionalNumericalValue(element, "UPDATE-INDICATION-BIT-POSITION"))

    def readNmPduISignalToIPduMappings(self, element: ET.Element, pdu: NmPdu):
        for child_element in self.findall(element, "I-SIGNAL-TO-I-PDU-MAPPINGS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "I-SIGNAL-TO-I-PDU-MAPPING":
                mapping = pdu.createISignalToIPduMapping(self.getShortName(child_element))
                self.readISignalToIPduMapping(child_element, mapping)
            else:
                self.notImplemented("Unsupported ISignalToIPduMapping <%s>" % tag_name)

    def readNmPdu(self, element: ET.Element, pdu: NmPdu):
        self.logger.debug("Read NmPdu <%s>" % pdu.getShortName())
        self.readPdu(element, pdu)
        self.readNmPduISignalToIPduMappings(element, pdu)
        pdu.setUnusedBitPattern(self.getChildElementOptionalIntegerValue(element, "UNUSED-BIT-PATTERN"))

    def readContainedIPduProps(self, element: ET.Element) -> ContainedIPduProps:
        props = None
        child_element = self.find(element, "CONTAINED-I-PDU-PROPS")
        if child_element is not None:
            props = ContainedIPduProps()
            props.setCollectionSemantics(self.getChildElementOptionalLiteral(child_element, "COLLECTION-SEMANTICS"))
            props.setHeaderIdLongHeader(self.getChildElementOptionalPositiveInteger(child_element, "HEADER-ID-LONG-HEADER"))
            props.setHeaderIdShortHeader(self.getChildElementOptionalPositiveInteger(child_element, "HEADER-ID-SHORT-HEADER"))
            props.setOffset(self.getChildElementOptionalNumericalValue(child_element, "OFFSET"))
            props.setTimeout(self.getChildElementOptionalNumericalValue(child_element, "TIMEOUT"))
            props.setTrigger(self.getChildElementOptionalLiteral(child_element, "TRIGGER"))
            props.setUpdateIndicationBitPosition(self.getChildElementOptionalNumericalValue(child_element, "UPDATE-INDICATION-BIT-POSITION"))
        return props

    def readIPdu(self, element: ET.Element, pdu: IPdu):
        self.readPdu(element, pdu)
        pdu.setContainedIPduProps(self.readContainedIPduProps(element))

    def readNPdu(self, element: ET.Element, pdu: NPdu):
        self.logger.debug("Read NPdu <%s>" % pdu.getShortName())
        self.readIPdu(element, pdu)

    def readDcmIPdu(self, element: ET.Element, i_pdu: DcmIPdu):
        self.logger.debug("Read DcmIPdu <%s>" % i_pdu.getShortName())
        self.readIPdu(element, i_pdu)
        i_pdu.setDiagPduType(self.getChildElementOptionalLiteral(element, "DIAG-PDU-TYPE"))

    def getSecureCommunicationProps(self, element: ET.Element, key: str) -> SecureCommunicationProps:
        props = None
        child_element = self.find(element, key)
        if child_element is not None:
            props = SecureCommunicationProps()
            props.setAuthDataFreshnessLength(self.getChildElementOptionalPositiveInteger(child_element, "AUTH-DATA-FRESHNESS-LENGTH"))
            props.setAuthDataFreshnessStartPosition(self.getChildElementOptionalPositiveInteger(child_element, "AUTH-DATA-FRESHNESS-START-POSITION"))
            props.setAuthenticationBuildAttempts(self.getChildElementOptionalPositiveInteger(child_element, "AUTHENTICATION-BUILD-ATTEMPTS"))
            props.setAuthenticationRetries(self.getChildElementOptionalPositiveInteger(child_element, "AUTHENTICATION-RETRIES"))
            props.setDataId(self.getChildElementOptionalPositiveInteger(child_element, "DATA-ID"))
            props.setFreshnessValueId(self.getChildElementOptionalPositiveInteger(child_element, "FRESHNESS-VALUE-ID"))
            props.setMessageLinkLength(self.getChildElementOptionalPositiveInteger(child_element, "MESSAGE-LINK-LENGTH"))
            props.setMessageLinkPosition(self.getChildElementOptionalPositiveInteger(child_element, "MESSAGE-LINK-POSITION"))
            props.setSecondaryFreshnessValueId(self.getChildElementOptionalPositiveInteger(child_element, "SECONDARY-FRESHNESS-VALUE-ID"))
            props.setSecuredAreaLength(self.getChildElementOptionalPositiveInteger(child_element, "SECURED-AREA-LENGTH"))
            props.setSecuredAreaOffset(self.getChildElementOptionalPositiveInteger(child_element, "SECURED-AREA-OFFSET"))
        return props

    def readSecuredIPdu(self, element: ET.Element, i_pdu: SecuredIPdu):
        self.logger.debug("Read SecuredIPdu <%s>" % i_pdu.getShortName())
        self.readIPdu(element, i_pdu)
        i_pdu.setAuthenticationPropsRef(self.getChildElementOptionalRefType(element, "AUTHENTICATION-PROPS-REF"))
        i_pdu.setFreshnessPropsRef(self.getChildElementOptionalRefType(element, "FRESHNESS-PROPS-REF"))
        i_pdu.setPayloadRef(self.getChildElementOptionalRefType(element, "PAYLOAD-REF"))
        i_pdu.setSecureCommunicationProps(self.getSecureCommunicationProps(element, "SECURE-COMMUNICATION-PROPS"))
        i_pdu.setUseAsCryptographicIPdu(self.getChildElementOptionalBooleanValue(element, "USE-AS-CRYPTOGRAPHIC-I-PDU"))

    def readNmNode(self, element: ET.Element, nm_node: NmNode):
        self.readIdentifiable(element, nm_node)

        nm_node.setControllerRef(self.getChildElementOptionalRefType(element, "CONTROLLER-REF"))
        nm_node.setNmCoordCluster(self.getChildElementOptionalPositiveInteger(element, "NM-COORD-CLUSTER"))
        nm_node.setNmCoordinatorRole(self.getChildElementOptionalLiteral(element, "NM-COORDINATOR-ROLE"))
        nm_node.setNmIfEcuRef(self.getChildElementOptionalRefType(element, "NM-IF-ECU-REF"))
        nm_node.setNmNodeId(self.getChildElementOptionalIntegerValue(element, "NM-NODE-ID"))
        nm_node.setNmPassiveModeEnabled(self.getChildElementOptionalBooleanValue(element, "NM-PASSIVE-MODE-ENABLED"))
        for ref in self.getChildElementRefTypeList(element, "RX-NM-PDU-REFS/RX-NM-PDU-REF"):
            nm_node.addRxNmPduRef(ref)
        for ref in self.getChildElementRefTypeList(element, "TX-NM-PDU-REFS/TX-NM-PDU-REF"):
            nm_node.addTxNmPduRef(ref)

    def readCanNmNode(self, element: ET.Element, nm_node: CanNmNode):
        self.logger.debug("Read CanNmNode <%s>" % nm_node.getShortName())
        self.readNmNode(element, nm_node)
        nm_node.setNmCarWakeUpRxEnabled(self.getChildElementOptionalBooleanValue(element, "NM-CAR-WAKE-UP-RX-ENABLED"))
        nm_node.setNmMsgCycleOffset(self.getChildElementOptionalFloatValue(element, "NM-MSG-CYCLE-OFFSET"))
        nm_node.setNmMsgReducedTime(self.getChildElementOptionalFloatValue(element, "NM-MSG-REDUCED-TIME"))
        nm_node.setNmRangeConfig(self.getChildElementRxIdentifierRange(element, "NM-RANGE-CONFIG"))

    def readUdpNmNode(self, element: ET.Element, nm_node: UdpNmNode):
        self.logger.debug("Read UdpNmNode <%s>" % nm_node.getShortName())
        self.readNmNode(element, nm_node)
        nm_node.setNmMsgCycleOffset(self.getChildElementOptionalTimeValue(element, "NM-MSG-CYCLE-OFFSET"))

    def readJ1939NmNode(self, element: ET.Element, nm_node: J1939NmNode):
        self.logger.debug("Read J1939NmNode <%s>" % nm_node.getShortName())
        self.readNmNode(element, nm_node)
        nm_node.setAddressConfigurationCapability(self.getChildElementOptionalLiteral(element, "ADDRESS-CONFIGURATION-CAPABILITY"))
        nm_node.setNodeName(self.getChildElementJ1939NodeName(element, "NODE-NAME"))

    def readNmClusterNmNodes(self, element: ET.Element, cluster: NmCluster):
        self.logger.debug("readNmConfigNmNodes %s" % cluster.getShortName())
        for child_element in self.findall(element, "NM-NODES/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "CAN-NM-NODE":
                nm_node = cluster.createCanNmNode(self.getShortName(child_element))
                self.readCanNmNode(child_element, nm_node)
            elif tag_name == "UDP-NM-NODE":
                nm_node = cluster.readUdpNmNode(self.getShortName(child_element))
                self.readUdpNmNode(child_element, nm_node)
            elif tag_name == "J-1939-NM-NODE":
                nm_node = cluster.createJ1939NmNode(self.getShortName(child_element))
                self.readJ1939NmNode(child_element, nm_node)
            else:
                self.notImplemented("Unsupported Nm Node <%s>" % tag_name)

    def getCanNmClusterCoupling(self, element: ET.Element) -> CanNmClusterCoupling:
        coupling = CanNmClusterCoupling()
        for ref in self.getChildElementRefTypeList(element, "COUPLED-CLUSTER-REFS/COUPLED-CLUSTER-REF"):
            coupling.addCoupledClusterRef(ref)
        coupling.setNmBusloadReductionEnabled(self.getChildElementOptionalBooleanValue(element, "NM-BUSLOAD-REDUCTION-ENABLED"))
        coupling.setNmImmediateRestartEnabled(self.getChildElementOptionalBooleanValue(element, "NM-IMMEDIATE-RESTART-ENABLED"))
        return coupling

    def getUdpNmClusterCoupling(self, element: ET.Element) -> UdpNmClusterCoupling:
        coupling = UdpNmClusterCoupling()
        for ref in self.getChildElementRefTypeList(element, "COUPLED-CLUSTER-REFS/COUPLED-CLUSTER-REF"):
            coupling.addCoupledClusterRef(ref)
        coupling.setNmImmediateRestartEnabled(self.getChildElementOptionalBooleanValue(element, "NM-IMMEDIATE-RESTART-ENABLED"))
        return coupling

    def readNmConfigNmClusterCouplings(self, element: ET.Element, nm_config: NmConfig):
        for child_element in self.findall(element, "NM-CLUSTER-COUPLINGS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "CAN-NM-CLUSTER-COUPLING":
                nm_config.addNmClusterCouplings(self.getCanNmClusterCoupling(child_element))
            elif tag_name == "UDP-NM-CLUSTER-COUPLING":
                nm_config.addNmClusterCouplings(self.getUdpNmClusterCoupling(child_element))
            else:
                self.notImplemented("Unsupported Nm Node <%s>" % tag_name)

    def readNmCluster(self, element: ET.Element, cluster: NmCluster):
        self.logger.debug("read NmCluster %s" % cluster.getShortName())
        self.readIdentifiable(element, cluster)
        cluster.setCommunicationClusterRef(self.getChildElementOptionalRefType(element, "COMMUNICATION-CLUSTER-REF"))
        cluster.setNmChannelId(self.getChildElementOptionalNumericalValue(element, "NM-CHANNEL-ID"))
        cluster.setNmChannelSleepMaster(self.getChildElementOptionalBooleanValue(element, "NM-CHANNEL-SLEEP-MASTER"))
        self.readNmClusterNmNodes(element, cluster)
        cluster.setNmSynchronizingNetwork(self.getChildElementOptionalBooleanValue(element, "NM-SYNCHRONIZING-NETWORK"))

    def readCanNmCluster(self, element: ET.Element, cluster: CanNmCluster):
        self.logger.debug("Read CanNmCluster <%s>" % cluster.getShortName())
        self.readNmCluster(element, cluster)
        cluster.setNmBusloadReductionActive(self.getChildElementOptionalBooleanValue(element, "NM-BUSLOAD-REDUCTION-ACTIVE"))
        cluster.setNmCarWakeUpRxEnabled(self.getChildElementOptionalBooleanValue(element, "NM-CAR-WAKE-UP-RX-ENABLED"))
        cluster.setNmCbvPosition(self.getChildElementOptionalNumericalValue(element, "NM-CBV-POSITION"))
        cluster.setNmChannelActive(self.getChildElementOptionalBooleanValue(element, "NM-CHANNEL-ACTIVE"))
        cluster.setNmImmediateNmCycleTime(self.getChildElementOptionalFloatValue(element, "NM-IMMEDIATE-NM-CYCLE-TIME"))
        cluster.setNmImmediateNmTransmissions(self.getChildElementOptionalNumericalValue(element, "NM-IMMEDIATE-NM-TRANSMISSIONS"))
        cluster.setNmMessageTimeoutTime(self.getChildElementOptionalFloatValue(element, "NM-MESSAGE-TIMEOUT-TIME"))
        cluster.setNmMsgCycleTime(self.getChildElementOptionalFloatValue(element, "NM-MSG-CYCLE-TIME"))
        cluster.setNmNetworkTimeout(self.getChildElementOptionalFloatValue(element, "NM-NETWORK-TIMEOUT"))
        cluster.setNmNidPosition(self.getChildElementOptionalNumericalValue(element, "NM-NID-POSITION"))
        cluster.setNmRemoteSleepIndicationTime(self.getChildElementOptionalFloatValue(element, "NM-REMOTE-SLEEP-INDICATION-TIME"))
        cluster.setNmRepeatMessageTime(self.getChildElementOptionalFloatValue(element, "NM-REPEAT-MESSAGE-TIME"))
        cluster.setNmUserDataLength(self.getChildElementOptionalNumericalValue(element, "NM-USER-DATA-LENGTH"))
        cluster.setNmWaitBusSleepTime(self.getChildElementOptionalFloatValue(element, "NM-WAIT-BUS-SLEEP-TIME"))

    def readUdpNmCluster(self, element: ET.Element, cluster: UdpNmCluster):
        self.logger.debug("Read UdpNmCluster %s" % cluster.getShortName())
        self.readNmCluster(element, cluster)
        cluster.setNmCbvPosition(self.getChildElementOptionalIntegerValue(element, "NM-CBV-POSITION"))
        cluster.setNmChannelActive(self.getChildElementOptionalBooleanValue(element, "NM-CHANNEL-ACTIVE"))
        cluster.setNmImmediateNmCycleTime(self.getChildElementOptionalTimeValue(element, "NM-IMMEDIATE-NM-CYCLE-TIME"))
        cluster.setNmImmediateNmTransmissions(self.getChildElementOptionalPositiveInteger(element, "NM-IMMEDIATE-NM-TRANSMISSIONS"))
        cluster.setNmMessageTimeoutTime(self.getChildElementOptionalTimeValue(element, "NM-MESSAGE-TIMEOUT-TIME"))
        cluster.setNmMsgCycleTime(self.getChildElementOptionalTimeValue(element, "NM-MSG-CYCLE-TIME"))
        cluster.setNmNetworkTimeout(self.getChildElementOptionalTimeValue(element, "NM-NETWORK-TIMEOUT"))
        cluster.setNmNidPosition(self.getChildElementOptionalIntegerValue(element, "NM-NID-POSITION"))
        cluster.setNmRemoteSleepIndicationTime(self.getChildElementOptionalTimeValue(element, "NM-REMOTE-SLEEP-INDICATION-TIME"))
        cluster.setNmRepeatMessageTime(self.getChildElementOptionalTimeValue(element, "NM-REPEAT-MESSAGE-TIME"))
        cluster.setNmWaitBusSleepTime(self.getChildElementOptionalTimeValue(element, "NM-WAIT-BUS-SLEEP-TIME"))
        cluster.setVlanRef(self.getChildElementOptionalRefType(element, "VLAN-REF"))

    def readNmConfigNmClusters(self, element: ET.Element, nm_config: NmConfig):
        for child_element in self.findall(element, "NM-CLUSTERS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "CAN-NM-CLUSTER":
                cluster = nm_config.createCanNmCluster(self.getShortName(child_element))
                self.readCanNmCluster(child_element, cluster)
            elif tag_name == "UDP-NM-CLUSTER":
                cluster = nm_config.createUdpNmCluster(self.getShortName(child_element))
                self.readUdpNmCluster(child_element, cluster)
            else:
                self.raiseError("Unsupported Nm Cluster <%s>" % tag_name)

    def readUdpNmEcu(self, element: ET.Element, ecu: UdpNmEcu):
        ecu.setNmSynchronizationPointEnabled(self.getChildElementOptionalBooleanValue(element, "NM-SYNCHRONIZATION-POINT-ENABLED"))

    def readBusDependentNmEcus(self, element: ET.Element, nm_ecu: NmEcu):
        for child_element in self.findall(element, "BUS-DEPENDENT-NM-ECUS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "UDP-NM-ECU":
                udp_nm_ecu = UdpNmEcu()
                self.readUdpNmEcu(child_element, udp_nm_ecu)
                nm_ecu.addBusDependentNmEcu(udp_nm_ecu)
            else:
                self.notImplemented("Unsupported BusDependentNmEcu <%s>" % tag_name)

    def readNmEcu(self, element: ET.Element, nm_ecu: NmEcu):
        self.readIdentifiable(element, nm_ecu)
        self.readBusDependentNmEcus(element, nm_ecu)
        nm_ecu.setEcuInstanceRef(self.getChildElementOptionalRefType(element, "ECU-INSTANCE-REF"))
        nm_ecu.setNmBusSynchronizationEnabled(self.getChildElementOptionalBooleanValue(element, "NM-BUS-SYNCHRONIZATION-ENABLED"))
        nm_ecu.setNmComControlEnabled(self.getChildElementOptionalBooleanValue(element, "NM-COM-CONTROL-ENABLED"))
        nm_ecu.setNmNodeDetectionEnabled(self.getChildElementOptionalBooleanValue(element, "NM-NODE-DETECTION-ENABLED"))
        nm_ecu.setNmNodeIdEnabled(self.getChildElementOptionalBooleanValue(element, "NM-NODE-ID-ENABLED"))
        nm_ecu.setNmPduRxIndicationEnabled(self.getChildElementOptionalBooleanValue(element, "NM-PDU-RX-INDICATION-ENABLED"))
        nm_ecu.setNmRemoteSleepIndEnabled(self.getChildElementOptionalBooleanValue(element, "NM-REMOTE-SLEEP-IND-ENABLED"))
        nm_ecu.setNmRepeatMsgIndEnabled(self.getChildElementOptionalBooleanValue(element, "NM-REPEAT-MSG-IND-ENABLED"))
        nm_ecu.setNmStateChangeIndEnabled(self.getChildElementOptionalBooleanValue(element, "NM-STATE-CHANGE-IND-ENABLED"))
        nm_ecu.setNmUserDataEnabled(self.getChildElementOptionalBooleanValue(element, "NM-USER-DATA-ENABLED"))

    def readNmConfigNmIfEcus(self, element: ET.Element, nm_config: NmConfig):
        for child_element in self.findall(element, "NM-IF-ECUS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "NM-ECU":
                ecu = nm_config.createNmEcu(self.getShortName(child_element))
                self.readNmEcu(child_element, ecu)
            else:
                self.notImplemented("Unsupported NmIfEcus <%s>" % tag_name)

    def readNmConfig(self, element: ET.Element, config: NmConfig):
        self.logger.debug("Read NmConfig <%s>" % config.getShortName())
        self.readIdentifiable(element, config)
        self.readNmConfigNmClusters(element, config)
        self.readNmConfigNmClusterCouplings(element, config)
        self.readNmConfigNmIfEcus(element, config)

    def readTpConfig(self, element: ET.Element, config: TpConfig):
        self.readIdentifiable(element, config)
        config.setCommunicationClusterRef(self.getChildElementOptionalRefType(element, "COMMUNICATION-CLUSTER-REF"))

    def readCanTpAddress(self, element: ET.Element, address: CanTpAddress):
        self.readIdentifiable(element, address)
        address.setTpAddress(self.getChildElementOptionalIntegerValue(element, "TP-ADDRESS"))
        address.setTpAddressExtensionValue(self.getChildElementOptionalIntegerValue(element, "TP-ADDRESS-EXTENSION-VALUE"))

    def readCanTpConfigTpAddresses(self, element: ET.Element, config: CanTpConfig):
        for child_element in self.findall(element, "TP-ADDRESSS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "CAN-TP-ADDRESS":
                address = config.createCanTpAddress(self.getShortName(child_element))
                self.readCanTpAddress(child_element, address)
            else:
                self.notImplemented("Unsupported TpAddress <%s>" % tag_name)

    def readCanTpChannel(self, element: ET.Element, channel: CanTpChannel):
        self.readIdentifiable(element, channel)
        channel.setChannelId(self.getChildElementOptionalPositiveInteger(element, "CHANNEL-ID"))
        channel.setChannelMode(self.getChildElementOptionalLiteral(element, "CHANNEL-MODE"))

    def readCanTpConfigTpChannels(self, element: ET.Element, config: CanTpConfig):
        for child_element in self.findall(element, "TP-CHANNELS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "CAN-TP-CHANNEL":
                channel = config.createCanTpChannel(self.getShortName(child_element))
                self.readCanTpChannel(child_element, channel)
            else:
                self.notImplemented("Unsupported TpChannel <%s>" % tag_name)

    def readTpConnection(self, element: ET.Element, connection: TpConnection):
        self.readARObjectAttributes(element, connection)
        child_element = self.find(element, "IDENT")
        if child_element is not None:
            ident = connection.createTpConnectionIdent(self.getShortName(child_element))
            self.readReferrable(child_element, ident)

    def readTpConnectionReceiverRefs(self, element: ET.Element, connection: CanTpConnection):
        for ref in self.getChildElementRefTypeList(element, "RECEIVER-REFS/RECEIVER-REF"):
            connection.addReceiverRef(ref)

    def readCanTpConnection(self, element: ET.Element, connection: CanTpConnection):
        self.readTpConnection(element, connection)
        connection.setAddressingFormat(self.getChildElementOptionalLiteral(element, "ADDRESSING-FORMAT"))
        connection.setCanTpChannelRef(self.getChildElementOptionalRefType(element, "CAN-TP-CHANNEL-REF"))
        connection.setCancellation(self.getChildElementOptionalBooleanValue(element, "CANCELLATION"))
        connection.setDataPduRef(self.getChildElementOptionalRefType(element, "DATA-PDU-REF"))
        connection.setFlowControlPduRef(self.getChildElementOptionalRefType(element, "FLOW-CONTROL-PDU-REF"))
        connection.setMaxBlockSize(self.getChildElementOptionalIntegerValue(element, "MAX-BLOCK-SIZE"))
        connection.setMulticastRef(self.getChildElementOptionalRefType(element, "MULTICAST-REF"))
        connection.setPaddingActivation(self.getChildElementOptionalBooleanValue(element, "PADDING-ACTIVATION"))
        self.readTpConnectionReceiverRefs(element, connection)
        connection.setTaType(self.getChildElementOptionalLiteral(element, "TA-TYPE"))
        connection.setTimeoutBr(self.getChildElementOptionalTimeValue(element, "TIMEOUT-BR"))
        connection.setTimeoutBs(self.getChildElementOptionalTimeValue(element, "TIMEOUT-BS"))
        connection.setTimeoutCr(self.getChildElementOptionalTimeValue(element, "TIMEOUT-CR"))
        connection.setTimeoutCs(self.getChildElementOptionalTimeValue(element, "TIMEOUT-CS"))
        connection.setTpSduRef(self.getChildElementOptionalRefType(element, "TP-SDU-REF"))
        connection.setTransmitterRef(self.getChildElementOptionalRefType(element, "TRANSMITTER-REF"))

    def readCanTpConfigTpConnections(self, element: ET.Element, config: CanTpConfig):
        for child_element in self.findall(element, "TP-CONNECTIONS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "CAN-TP-CONNECTION":
                connection = CanTpConnection()
                self.readCanTpConnection(child_element, connection)
                config.addTpConnection(connection)
            else:
                self.notImplemented("Unsupported TpConnection <%s>" % tag_name)

    def readCanTpEcu(self, element: ET.Element, tp_ecu: CanTpEcu):
        tp_ecu.setCycleTimeMainFunction(self.getChildElementOptionalTimeValue(element, "CYCLE-TIME-MAIN-FUNCTION"))
        tp_ecu.setEcuInstanceRef(self.getChildElementOptionalRefType(element, "ECU-INSTANCE-REF"))

    def readCanTpConfigTpEcus(self, element: ET.Element, config: CanTpConfig):
        for child_element in self.findall(element, "TP-ECUS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "CAN-TP-ECU":
                tp_ecu = CanTpEcu()
                self.readCanTpEcu(child_element, tp_ecu)
                config.addTpEcu(tp_ecu)
            else:
                self.notImplemented("Unsupported TpEcu <%s>" % tag_name)

    def readCanTpNode(self, element: ET.Element, tp_node: CanTpNode):
        self.readIdentifiable(element, tp_node)
        tp_node.setConnectorRef(self.getChildElementOptionalRefType(element, "CONNECTOR-REF"))
        tp_node.setMaxFcWait(self.getChildElementOptionalIntegerValue(element, "MAX-FC-WAIT"))
        tp_node.setStMin(self.getChildElementOptionalTimeValue(element, "ST-MIN"))
        tp_node.setTimeoutAr(self.getChildElementOptionalTimeValue(element, "TIMEOUT-AR"))
        tp_node.setTimeoutAs(self.getChildElementOptionalTimeValue(element, "TIMEOUT-AS"))
        tp_node.setTpAddressRef(self.getChildElementOptionalRefType(element, "TP-ADDRESS-REF"))

    def readCanTpConfigTpNodes(self, element: ET.Element, config: CanTpConfig):
        for child_element in self.findall(element, "TP-NODES/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "CAN-TP-NODE":
                tp_node = config.createCanTpNode(self.getShortName(child_element))
                self.readCanTpNode(child_element, tp_node)
            else:
                self.notImplemented("Unsupported TpNode <%s>" % tag_name)

    def readCanTpConfig(self, element: ET.Element, config: CanTpConfig):
        self.logger.debug("Read CanTpConfig <%s>" % config.getShortName())
        self.readTpConfig(element, config)
        self.readCanTpConfigTpAddresses(element, config)
        self.readCanTpConfigTpChannels(element, config)
        self.readCanTpConfigTpConnections(element, config)
        self.readCanTpConfigTpEcus(element, config)
        self.readCanTpConfigTpNodes(element, config)

    def readTpAddress(self, element: ET.Element, address: TpAddress):
        self.readIdentifiable(element, address)
        address.setTpAddress(self.getChildElementOptionalIntegerValue(element, "TP-ADDRESS"))

    def readLinTpConfigTpAddresses(self, element: ET.Element, config: LinTpConfig):
        for child_element in self.findall(element, "TP-ADDRESSS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "TP-ADDRESS":
                address = config.createTpAddress(self.getShortName(child_element))
                self.readTpAddress(child_element, address)
            else:
                self.notImplemented("Unsupported TpAddress <%s>" % tag_name)

    def readLinTpConnection(self, element: ET.Element, connection: LinTpConnection):
        self.readTpConnection(element, connection)
        connection.setDataPduRef(self.getChildElementOptionalRefType(element, "DATA-PDU-REF"))
        connection.setFlowControlRef(self.getChildElementOptionalRefType(element, "FLOW-CONTROL-REF"))
        connection.setLinTpNSduRef(self.getChildElementOptionalRefType(element, "LIN-TP-N-SDU-REF"))
        self.readTpConnectionReceiverRefs(element, connection)
        connection.setTimeoutAs(self.getChildElementOptionalTimeValue(element, "TIMEOUT-AS"))
        connection.setTimeoutCr(self.getChildElementOptionalTimeValue(element, "TIMEOUT-CR"))
        connection.setTimeoutCs(self.getChildElementOptionalTimeValue(element, "TIMEOUT-CS"))
        connection.setTransmitterRef(self.getChildElementOptionalRefType(element, "TRANSMITTER-REF"))

    def readLinTpConfigTpConnections(self, element: ET.Element, config: LinTpConfig):
        for child_element in self.findall(element, "TP-CONNECTIONS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "LIN-TP-CONNECTION":
                connection = LinTpConnection()
                self.readLinTpConnection(child_element, connection)
                config.addTpConnection(connection)
            else:
                self.notImplemented("Unsupported TpConnection <%s>" % tag_name)

    def readLinTpNode(self, element: ET.Element, tp_node: LinTpNode):
        self.readIdentifiable(element, tp_node)
        tp_node.setConnectorRef(self.getChildElementOptionalRefType(element, "CONNECTOR-REF"))
        tp_node.setDropNotRequestedNad(self.getChildElementOptionalBooleanValue(element, "DROP-NOT-REQUESTED-NAD"))
        tp_node.setP2Max(self.getChildElementOptionalTimeValue(element, "P-2-MAX"))
        tp_node.setP2Timing(self.getChildElementOptionalTimeValue(element, "P-2-TIMING"))
        tp_node.setTpAddressRef(self.getChildElementOptionalRefType(element, "TP-ADDRESS-REF"))

    def readLinTpConfigTpNodes(self, element: ET.Element, config: LinTpConfig):
        for child_element in self.findall(element, "TP-NODES/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "LIN-TP-NODE":
                tp_node = config.createLinTpNode(self.getShortName(child_element))
                self.readLinTpNode(child_element, tp_node)
            else:
                self.notImplemented("Unsupported TpNode <%s>" % tag_name)

    def readLinTpConfig(self, element: ET.Element, config: LinTpConfig):
        self.logger.debug("Read LinTpConfig <%s>" % config.getShortName())
        self.readTpConfig(element, config)
        self.readLinTpConfigTpAddresses(element, config)
        self.readLinTpConfigTpConnections(element, config)
        self.readLinTpConfigTpNodes(element, config)

    def readCanFrame(self, element: ET.Element, frame: CanFrame):
        self.logger.debug("Read CanFrame <%s>" % frame.getShortName())
        self.readFrame(element, frame)

    def readFlexrayFrame(self, element: ET.Element, frame: FlexrayFrame):
        self.logger.debug("Read FlexrayFrame <%s>" % frame.getShortName())
        self.readFrame(element, frame)

    def readFlexrayCommunicationController(self, element: ET.Element, controller: FlexrayCommunicationController):
        self.logger.debug("Read CommunicationController <%s>" % controller.getShortName())
        self.readIdentifiable(element, controller)
        child_element = self.find(element, "FLEXRAY-COMMUNICATION-CONTROLLER-VARIANTS/FLEXRAY-COMMUNICATION-CONTROLLER-CONDITIONAL")
        if child_element is not None:
            self.readCommunicationController(element, controller)
            controller.setAcceptedStartupRange(self.getChildElementOptionalIntegerValue(child_element, "ACCEPTED-STARTUP-RANGE"))
            controller.setAllowHaltDueToClock(self.getChildElementOptionalBooleanValue(child_element, "ALLOW-HALT-DUE-TO-CLOCK"))
            controller.setAllowPassiveToActive(self.getChildElementOptionalIntegerValue(child_element, "ALLOW-PASSIVE-TO-ACTIVE"))
            controller.setClusterDriftDamping(self.getChildElementOptionalIntegerValue(child_element, "CLUSTER-DRIFT-DAMPING"))
            controller.setDecodingCorrection(self.getChildElementOptionalIntegerValue(child_element, "DECODING-CORRECTION"))
            controller.setDelayCompensationA(self.getChildElementOptionalIntegerValue(child_element, "DELAY-COMPENSATION-A"))
            controller.setDelayCompensationB(self.getChildElementOptionalIntegerValue(child_element, "DELAY-COMPENSATION-B"))
            controller.setKeySlotOnlyEnabled(self.getChildElementOptionalBooleanValue(child_element, "KEY-SLOT-ONLY-ENABLED"))
            controller.setKeySlotUsedForStartUp(self.getChildElementOptionalBooleanValue(child_element, "KEY-SLOT-USED-FOR-START-UP"))
            controller.setKeySlotUsedForSync(self.getChildElementOptionalBooleanValue(child_element, "KEY-SLOT-USED-FOR-SYNC"))
            controller.setLatestTX(self.getChildElementOptionalIntegerValue(child_element, "LATEST-TX"))
            controller.setListenTimeout(self.getChildElementOptionalIntegerValue(child_element, "LISTEN-TIMEOUT"))
            controller.setMacroInitialOffsetA(self.getChildElementOptionalIntegerValue(child_element, "MACRO-INITIAL-OFFSET-A"))
            controller.setMacroInitialOffsetB(self.getChildElementOptionalIntegerValue(child_element, "MACRO-INITIAL-OFFSET-B"))
            controller.setMaximumDynamicPayloadLength(self.getChildElementOptionalIntegerValue(child_element, "MAXIMUM-DYNAMIC-PAYLOAD-LENGTH"))
            controller.setMicroInitialOffsetA(self.getChildElementOptionalIntegerValue(child_element, "MICRO-INITIAL-OFFSET-A"))
            controller.setMicroInitialOffsetB(self.getChildElementOptionalIntegerValue(child_element, "MICRO-INITIAL-OFFSET-B"))
            controller.setMicroPerCycle(self.getChildElementOptionalIntegerValue(child_element, "MICRO-PER-CYCLE"))
            controller.setMicrotickDuration(self.getChildElementOptionalTimeValue(child_element, "MICROTICK-DURATION"))
            controller.setOffsetCorrectionOut(self.getChildElementOptionalIntegerValue(child_element, "OFFSET-CORRECTION-OUT"))
            controller.setRateCorrectionOut(self.getChildElementOptionalIntegerValue(child_element, "RATE-CORRECTION-OUT"))
            controller.setSamplesPerMicrotick(self.getChildElementOptionalIntegerValue(child_element, "SAMPLES-PER-MICROTICK"))
            controller.setExternOffsetCorrection(self.getChildElementOptionalIntegerValue(child_element, "EXTERN-OFFSET-CORRECTION"))
            controller.setExternRateCorrection(self.getChildElementOptionalIntegerValue(child_element, "EXTERN-RATE-CORRECTION"))
            controller.setExternalSync(self.getChildElementOptionalBooleanValue(child_element, "EXTERNAL-SYNC"))
            controller.setFallBackInternal(self.getChildElementOptionalBooleanValue(child_element, "FALL-BACK-INTERNAL"))
            for fifo_child in self.findall(child_element, "FLEXRAY-FIFOS/FLEXRAY-FIFO-CONFIGURATION"):
                fifo = controller.createFlexrayFifo()
                fifo.setAdmitWithoutMessageId(self.getChildElementOptionalBooleanValue(fifo_child, "ADMIT-WITHOUT-MESSAGE-ID"))
                fifo.setBaseCycle(self.getChildElementOptionalIntegerValue(fifo_child, "BASE-CYCLE"))
                fifo.setChannelRef(self.getChildElementOptionalRefType(fifo_child, "CHANNEL-REF"))
                fifo.setCycleRepetition(self.getChildElementOptionalIntegerValue(fifo_child, "CYCLE-REPETITION"))
                fifo.setFifoDepth(self.getChildElementOptionalIntegerValue(fifo_child, "FIFO-DEPTH"))
                for range_child in self.findall(fifo_child, "FLEXRAY-FIFO-RANGE"):
                    fifo_range = fifo.createFlexrayFifoRange()
                    fifo_range.setRangeMax(self.getChildElementOptionalIntegerValue(range_child, "RANGE-MAX"))
                    fifo_range.setRangeMin(self.getChildElementOptionalIntegerValue(range_child, "RANGE-MIN"))
                fifo.setMsgIdMask(self.getChildElementOptionalIntegerValue(fifo_child, "MSG-ID-MASK"))
                fifo.setMsgIdMatch(self.getChildElementOptionalIntegerValue(fifo_child, "MSG-ID-MATCH"))
            controller.setKeySlotID(self.getChildElementOptionalIntegerValue(child_element, "KEY-SLOT-ID"))
            controller.setNmVectorEarlyUpdate(self.getChildElementOptionalBooleanValue(child_element, "NM-VECTOR-EARLY-UPDATE"))
            controller.setSecondKeySlotId(self.getChildElementOptionalIntegerValue(child_element, "SECOND-KEY-SLOT-ID"))
            controller.setTwoKeySlotMode(self.getChildElementOptionalBooleanValue(child_element, "TWO-KEY-SLOT-MODE"))
            controller.setWakeUpPattern(self.getChildElementOptionalIntegerValue(child_element, "WAKE-UP-PATTERN"))

    def readDataTransformationTransformerChainRefs(self, element: ET.Element, dtf: DataTransformation):
        for ref in self.getChildElementRefTypeList(element, "TRANSFORMER-CHAIN-REFS/TRANSFORMER-CHAIN-REF"):
            dtf.addTransformerChainRef(ref)

    def readDataTransformation(self, element: ET.Element, dtf: DataTransformation):
        self.readIdentifiable(element, dtf)
        dtf.setDataTransformationKind(self.getChildElementOptionalLiteral(element, "DATA-TRANSFORMATION-KIND"))
        dtf.setExecuteDespiteDataUnavailability(self.getChildElementOptionalBooleanValue(element, "EXECUTE-DESPITE-DATA-UNAVAILABILITY"))
        self.readDataTransformationTransformerChainRefs(element, dtf)

    def readDataTransformationSetDataTransformations(self, element: ET.Element, dtf_set: DataTransformationSet):
        for child_element in self.findall(element, "DATA-TRANSFORMATIONS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "DATA-TRANSFORMATION":
                dtf = dtf_set.createDataTransformation(self.getShortName(child_element))
                self.readDataTransformation(child_element, dtf)
            else:
                self.notImplemented("Unsupported DataTransformation <%s>" % tag_name)

    def getBufferProperties(self, element: ET.Element, key: str) -> BufferProperties:
        properties = None
        child_element = self.find(element, key)
        if child_element is not None:
            properties = BufferProperties()
            properties.setHeaderLength(self.getChildElementOptionalIntegerValue(child_element, "HEADER-LENGTH"))
            properties.setInPlace(self.getChildElementOptionalBooleanValue(child_element, "IN-PLACE"))
        return properties

    def readDescribable(self, element: ET.Element, desc: Describable):
        self.readARObjectAttributes(element, desc)

        desc.setDesc(self.getMultiLanguageOverviewParagraph(element, "DESC"))
        desc.setCategory(self.getChildElementOptionalLiteral(element, "CATEGORY"))
        desc.setIntroduction(self.getDocumentationBlock(element, "INTRODUCTION"))
        desc.setAdminData(self.getAdminData(element, "ADMIN-DATA"))

    def readTransformationDescription(self, element: ET.Element, desc: TransformationDescription):
        self.readDescribable(element, desc)

    def readEndToEndTransformationDescription(self, element: ET.Element, desc: EndToEndTransformationDescription):
        self.readTransformationDescription(element, desc)
        desc.setClearFromValidToInvalid(self.getChildElementOptionalBooleanValue(element, "CLEAR-FROM-VALID-TO-INVALID"))
        desc.setCounterOffset(self.getChildElementOptionalPositiveInteger(element, "COUNTER-OFFSET"))
        desc.setCrcOffset(self.getChildElementOptionalPositiveInteger(element, "CRC-OFFSET"))
        desc.setDataIdMode(self.getChildElementOptionalLiteral(element, "DATA-ID-MODE"))
        desc.setDataIdNibbleOffset(self.getChildElementOptionalPositiveInteger(element, "DATA-ID-NIBBLE-OFFSET"))
        desc.setE2eProfileCompatibilityPropsRef(self.getChildElementOptionalRefType(element, "E-2-E-PROFILE-COMPATIBILITY-PROPS-REF"))
        desc.setMaxDeltaCounter(self.getChildElementOptionalPositiveInteger(element, "MAX-DELTA-COUNTER"))
        desc.setMaxErrorStateInit(self.getChildElementOptionalPositiveInteger(element, "MAX-ERROR-STATE-INIT"))
        desc.setMaxErrorStateInvalid(self.getChildElementOptionalPositiveInteger(element, "MAX-ERROR-STATE-INVALID"))
        desc.setMaxErrorStateValid(self.getChildElementOptionalPositiveInteger(element, "MAX-ERROR-STATE-VALID"))
        desc.setMaxNoNewOrRepeatedData(self.getChildElementOptionalPositiveInteger(element, "MAX-NO-NEW-OR-REPEATED-DATA"))
        desc.setMinOkStateInit(self.getChildElementOptionalPositiveInteger(element, "MIN-OK-STATE-INIT"))
        desc.setMinOkStateInvalid(self.getChildElementOptionalPositiveInteger(element, "MIN-OK-STATE-INVALID"))
        desc.setMinOkStateValid(self.getChildElementOptionalPositiveInteger(element, "MIN-OK-STATE-VALID"))
        desc.setOffset(self.getChildElementOptionalPositiveInteger(element, "OFFSET"))
        desc.setProfileBehavior(self.getChildElementOptionalLiteral(element, "PROFILE-BEHAVIOR"))
        desc.setProfileName(self.getChildElementOptionalLiteral(element, "PROFILE-NAME"))
        desc.setSyncCounterInit(self.getChildElementOptionalPositiveInteger(element, "SYNC-COUNTER-INIT"))
        desc.setUpperHeaderBitsToShift(self.getChildElementOptionalPositiveInteger(element, "UPPER-HEADER-BITS-TO-SHIFT"))
        desc.setWindowSizeInit(self.getChildElementOptionalPositiveInteger(element, "WINDOW-SIZE-INIT"))
        desc.setWindowSizeInvalid(self.getChildElementOptionalPositiveInteger(element, "WINDOW-SIZE-INVALID"))
        desc.setWindowSizeValid(self.getChildElementOptionalPositiveInteger(element, "WINDOW-SIZE-VALID"))

    def readTransformationTechnologyTransformationDescriptions(self, element: ET.Element, tech: TransformationTechnology):
        for child_element in self.findall(element, "TRANSFORMATION-DESCRIPTIONS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "END-TO-END-TRANSFORMATION-DESCRIPTION":
                desc = EndToEndTransformationDescription()
                self.readEndToEndTransformationDescription(child_element, desc)
                tech.setTransformationDescription(desc)
            else:
                self.notImplemented("Unsupported TransformationDescription <%s>" % tag_name)

    def readTransformationTechnology(self, element: ET.Element, tech: TransformationTechnology):
        self.readIdentifiable(element, tech)
        tech.setBufferProperties(self.getBufferProperties(element, "BUFFER-PROPERTIES"))
        tech.setHasInternalState(self.getChildElementOptionalBooleanValue(element, "HAS-INTERNAL-STATE"))
        tech.setNeedsOriginalData(self.getChildElementOptionalBooleanValue(element, "NEEDS-ORIGINAL-DATA"))
        tech.setProtocol(self.getChildElementOptionalLiteral(element, "PROTOCOL"))
        self.readTransformationTechnologyTransformationDescriptions(element, tech)
        tech.setTransformerClass(self.getChildElementOptionalLiteral(element, "TRANSFORMER-CLASS"))
        tech.setVersion(self.getChildElementOptionalLiteral(element, "VERSION"))

    def readDataTransformationSetTransformationTechnologies(self, element: ET.Element, dtf_set: DataTransformationSet):
        for child_element in self.findall(element, "TRANSFORMATION-TECHNOLOGYS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "TRANSFORMATION-TECHNOLOGY":
                tech = dtf_set.createTransformationTechnology(self.getShortName(child_element))
                self.readTransformationTechnology(child_element, tech)
            else:
                self.notImplemented("Unsupported TransformationTechnology <%s>" % tag_name)

    def readDataTransformationSet(self, element: ET.Element, dtf_set: DataTransformationSet):
        self.logger.debug("Read DataTransformationSet <%s>" % dtf_set.getShortName())
        self.readARElement(element, dtf_set)
        self.readDataTransformationSetDataTransformations(element, dtf_set)
        self.readDataTransformationSetTransformationTechnologies(element, dtf_set)

    def readE2EProfileCompatibilityProps(self, element: ET.Element, props: E2EProfileCompatibilityProps):
        self.logger.debug("Read E2EProfileCompatibilityProps <%s>" % props.getShortName())
        self.readARElement(element, props)
        props.setTransitToInvalidExtended(self.getChildElementOptionalBooleanValue(element, "TRANSIT-TO-INVALID-EXTENDED"))

    def readCollectionElementRefs(self, element: ET.Element, collection: Collection):
        for ref in self.getChildElementRefTypeList(element, "ELEMENT-REFS/ELEMENT-REF"):
            collection.addElementRef(ref)

    def readCollectionSourceElementRefs(self, element: ET.Element, collection: Collection):
        for ref in self.getChildElementRefTypeList(element, "SOURCE-ELEMENT-REFS/SOURCE-ELEMENT-REF"):
            collection.addSourceElementRef(ref)

    def readCollection(self, element: ET.Element, collection: Collection):
        self.logger.debug("Read Collection <%s>" % collection.getShortName())
        self.readARElement(element, collection)
        collection.setAutoCollect(self.getChildElementOptionalLiteral(element, "AUTO-COLLECT"))
        collection.setElementRole(self.getChildElementOptionalLiteral(element, "ELEMENT-ROLE"))
        self.readCollectionElementRefs(element, collection)
        self.readCollectionSourceElementRefs(element, collection)

    def readKeywordClassifications(self, element: ET.Element, keyword: Keyword):
        for literal in self.getChildElementLiteralValueList(element, "CLASSIFICATIONS/CLASSIFICATION"):
            keyword.addClassification(literal)

    def readKeyword(self, element: ET.Element, keyword: Keyword):
        # self.logger.debug("Read Keyword <%s>" % keyword.getShortName())
        self.readIdentifiable(element, keyword)
        keyword.setAbbrName(self.getChildElementOptionalLiteral(element, "ABBR-NAME"))
        self.readKeywordClassifications(element, keyword)

    def readKeywordSetKeywords(self, element: ET.Element, keyword_set: KeywordSet):
        for child_element in self.findall(element, "KEYWORDS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "KEYWORD":
                tech = keyword_set.createKeyword(self.getShortName(child_element))
                self.readKeyword(child_element, tech)
            else:
                self.notImplemented("Unsupported Keyword <%s>" % tag_name)

    def readKeywordSet(self, element: ET.Element, keyword_set: KeywordSet):
        self.logger.debug("Read KeywordSet <%s>" % keyword_set.getShortName())
        self.readARElement(element, keyword_set)
        self.readKeywordSetKeywords(element, keyword_set)

    def readPortPrototypeBlueprint(self, element: ET.Element, blueprint: PortPrototypeBlueprint):
        self.logger.debug("Read PortPrototypeBlueprint <%s>" % blueprint.getShortName())
        self.readARElement(element, blueprint)
        blueprint.setInterfaceRef(self.getChildElementOptionalRefType(element, "INTERFACE-REF"))

    def readModeDeclarationMappingFirstModeRefs(self, element: ET.Element, mapping: ModeDeclarationMapping):
        for ref_link in self.getChildElementRefTypeList(element, "FIRST-MODE-REFS/FIRST-MODE-REF"):
            mapping.addFirstModeRef(ref_link)

    def readModeDeclarationMapping(self, element: ET.Element, mapping: ModeDeclarationMapping):
        # self.logger.debug("Read ModeDeclarationMapping <%s>" % mapping.getShortName())
        self.readIdentifiable(element, mapping)
        self.readModeDeclarationMappingFirstModeRefs(element, mapping)
        mapping.setSecondModeRef(self.getChildElementOptionalRefType(element, "SECOND-MODE-REF"))

    def readModeDeclarationMappingSetModeDeclarationMappings(self, element: ET.Element, mapping_set: ModeDeclarationMappingSet):
        for child_element in self.findall(element, "MODE-DECLARATION-MAPPINGS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "MODE-DECLARATION-MAPPING":
                mapping = mapping_set.createModeDeclarationMapping(self.getShortName(child_element))
                self.readModeDeclarationMapping(child_element, mapping)
            else:
                self.notImplemented("Unsupported ModeDeclarationMapping <%s>" % tag_name)

    def readModeDeclarationMappingSet(self, element: ET.Element, mapping_set: ModeDeclarationMappingSet):
        self.logger.debug("Read ModeDeclarationMappingSet <%s>" % mapping_set.getShortName())
        self.readARElement(element, mapping_set)
        self.readModeDeclarationMappingSetModeDeclarationMappings(element, mapping_set)

    def readEcucDefinitionElement(self, element: ET.Element, def_element: EcucDefinitionElement):
        self.readIdentifiable(element, def_element)
        def_element.setEcucCond(self.readEcucConditionSpecification(element))
        self.readEcucValidationConditions(element, def_element)
        def_element.setLowerMultiplicity(self.getChildElementOptionalPositiveInteger(element, "LOWER-MULTIPLICITY"))
        def_element.setUpperMultiplicity(self.getChildElementOptionalPositiveInteger(element, "UPPER-MULTIPLICITY"))
        def_element.setScope(self.getChildElementOptionalLiteral(element, "SCOPE"))

    def readEcucModuleDefSupportedConfigVariants(self, element: ET.Element, module_def: EcucModuleDef):
        for variant in self.getChildElementLiteralValueList(element, "SUPPORTED-CONFIG-VARIANTS/SUPPORTED-CONFIG-VARIANT"):
            module_def.addSupportedConfigVariant(variant)

    def readEcucAbstractConfigurationClass(self, element: ET.Element, cfg_class: EcucAbstractConfigurationClass):
        self.readARObjectAttributes(element, cfg_class)
        cfg_class.setConfigClass(self.getChildElementOptionalLiteral(element, "CONFIG-CLASS"))
        cfg_class.setConfigVariant(self.getChildElementOptionalLiteral(element, "CONFIG-VARIANT"))

    def readEcucMultiplicityConfigurationClass(self, element: ET.Element, cfg_class: EcucMultiplicityConfigurationClass):
        self.readEcucAbstractConfigurationClass(element, cfg_class)

    def getEcucMultiplicityConfigurationClasses(self, element: ET.Element) -> List[EcucMultiplicityConfigurationClass]:
        cfg_classes = []
        for child_element in self.findall(element, "MULTIPLICITY-CONFIG-CLASSES/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "ECUC-MULTIPLICITY-CONFIGURATION-CLASS":
                cfg_class = EcucMultiplicityConfigurationClass()
                self.readEcucMultiplicityConfigurationClass(child_element, cfg_class)
                cfg_classes.append(cfg_class)
            else:
                self.notImplemented("Unsupported MultiplicityConfigClass <%s>" % tag_name)
        return cfg_classes

    def readEcucContainerDef(self, element: ET.Element, container_def: EcucContainerDef):
        self.readEcucDefinitionElement(element, container_def)
        for uri_ref in self.getEcucDestinationUriRefs(element):
            container_def.addDestinationUriRef(uri_ref)
        for cfg_class in self.getEcucMultiplicityConfigurationClasses(element):
            container_def.addMultiplicityConfigClass(cfg_class)
        container_def.setPostBuildVariantMultiplicity(self.getChildElementOptionalBooleanValue(element, "POST-BUILD-VARIANT-MULTIPLICITY"))
        container_def.setRequiresIndex(self.getChildElementOptionalBooleanValue(element, "REQUIRES-INDEX"))
        origin_lit = self.getChildElementOptionalLiteral(element, "ORIGIN")
        if origin_lit is not None:
            origin = String()
            origin.setValue(origin_lit.getValue())
            container_def.setOrigin(origin)

    def getEcucDestinationUriRefs(self, element: ET.Element) -> List[EcucDestinationUriDefRefType]:
        uri_refs = []
        for child_element in self.findall(element, "DESTINATION-URI-REFS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "DESTINATION-URI-REF":
                uri_ref = EcucDestinationUriDefRefType()
                if "BASE" in child_element.attrib:
                    uri_ref.setBase(child_element.attrib["BASE"])
                if "DEST" in child_element.attrib:
                    uri_ref.setDest(child_element.attrib["DEST"])
                uri_ref.setValue(child_element.text)
                uri_refs.append(uri_ref)
            else:
                self.notImplemented("Unsupported DestinationUriRef <%s>" % tag_name)
        return uri_refs

    def readEcucDestinationUriDefSet(self, element: ET.Element, uri_def_set: EcucDestinationUriDefSet):
        self.logger.debug("Read EcucDestinationUriDefSet <%s>" % uri_def_set.getShortName())
        for child_element in self.findall(element, "DESTINATION-URI-DEFS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "ECUC-DESTINATION-URI-DEF":
                uri_def = uri_def_set.createEcucDestinationUriDef(self.getShortName(child_element))
                self.readEcucDestinationUriDef(child_element, uri_def)
            else:
                self.notImplemented("Unsupported DestinationUriDef <%s>" % tag_name)

    def readEcucDestinationUriDef(self, element: ET.Element, uri_def: EcucDestinationUriDef):
        self.logger.debug("Read EcucDestinationUriDef <%s>" % uri_def.getShortName())
        self.readIdentifiable(element, uri_def)
        policy_element = self.find(element, "DESTINATION-URI-POLICY")
        if policy_element is not None:
            policy = EcucDestinationUriPolicy()
            self.readEcucDestinationUriPolicy(policy_element, policy)
            uri_def.setDestinationUriPolicy(policy)

    def readEcucDestinationUriPolicy(self, element: ET.Element, policy: EcucDestinationUriPolicy):
        self.readARObjectAttributes(element, policy)
        self.readEcucDestinationUriPolicyContainers(element, policy)
        nesting_contract = self.getChildElementOptionalLiteral(element, "DESTINATION-URI-NESTING-CONTRACT")
        if nesting_contract is not None:
            contract_enum = EcucDestinationUriNestingContractEnum()
            contract_enum.setValue(nesting_contract)
            policy.setDestinationUriNestingContract(contract_enum)
        self.readEcucDestinationUriPolicyParameters(element, policy)
        self.readEcucDestinationUriPolicyReferences(element, policy)

    def readEcucDestinationUriPolicyContainers(self, element: ET.Element, policy: EcucDestinationUriPolicy):
        for child_element in self.findall(element, "CONTAINERS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "ECUC-PARAM-CONF-CONTAINER-DEF":
                container_def = EcucParamConfContainerDef(policy, self.getShortName(child_element))
                self.readEcucParamConfContainerDef(child_element, container_def)
                policy.addContainer(container_def)
            elif tag_name == "ECUC-CHOICE-CONTAINER-DEF":
                container_def = EcucChoiceContainerDef(policy, self.getShortName(child_element))
                self.readEcucChoiceContainerDef(child_element, container_def)
                policy.addContainer(container_def)
            else:
                self.notImplemented("Unsupported DestinationUriPolicy Container <%s>" % tag_name)

    def readEcucDestinationUriPolicyParameters(self, element: ET.Element, policy: EcucDestinationUriPolicy):
        for child_element in self.findall(element, "PARAMETERS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "ECUC-BOOLEAN-PARAM-DEF":
                param_def = EcucBooleanParamDef(policy, self.getShortName(child_element))
                self.readEcucBooleanParamDef(child_element, param_def)
                policy.addParameter(param_def)
            elif tag_name == "ECUC-STRING-PARAM-DEF":
                param_def = EcucStringParamDef(policy, self.getShortName(child_element))
                self.readEcucStringParamDef(child_element, param_def)
                policy.addParameter(param_def)
            elif tag_name == "ECUC-INTEGER-PARAM-DEF":
                param_def = EcucIntegerParamDef(policy, self.getShortName(child_element))
                self.readEcucIntegerParamDef(child_element, param_def)
                policy.addParameter(param_def)
            elif tag_name == "ECUC-FLOAT-PARAM-DEF":
                param_def = EcucFloatParamDef(policy, self.getShortName(child_element))
                self.readEcucFloatParamDef(child_element, param_def)
                policy.addParameter(param_def)
            elif tag_name == "ECUC-ENUMERATION-PARAM-DEF":
                param_def = EcucEnumerationParamDef(policy, self.getShortName(child_element))
                self.readEcucEnumerationParamDef(child_element, param_def)
                policy.addParameter(param_def)
            elif tag_name == "ECUC-FUNCTION-NAME-DEF":
                param_def = EcucFunctionNameDef(policy, self.getShortName(child_element))
                self.readEcucFunctionNameDef(child_element, param_def)
                policy.addParameter(param_def)
            elif tag_name == "ECUC-MULTILINE-STRING-PARAM-DEF":
                param_def = EcucMultilineStringParamDef(policy, self.getShortName(child_element))
                self.readEcucMultilineStringParamDef(child_element, param_def)
                policy.addParameter(param_def)
            else:
                self.notImplemented("Unsupported DestinationUriPolicy Parameter <%s>" % tag_name)

    def readEcucDestinationUriPolicyReferences(self, element: ET.Element, policy: EcucDestinationUriPolicy):
        for child_element in self.findall(element, "REFERENCES/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "ECUC-SYMBOLIC-NAME-REFERENCE-DEF":
                ref_def = EcucSymbolicNameReferenceDef(policy, self.getShortName(child_element))
                self.readEcucSymbolicNameReferenceDef(child_element, ref_def)
                policy.addReference(ref_def)
            elif tag_name == "ECUC-REFERENCE-DEF":
                ref_def = EcucReferenceDef(policy, self.getShortName(child_element))
                self.readEcucReferenceDef(child_element, ref_def)
                policy.addReference(ref_def)
            elif tag_name == "ECUC-CHOICE-REFERENCE-DEF":
                ref_def = EcucChoiceReferenceDef(policy, self.getShortName(child_element))
                self.readEcucChoiceReferenceDef(child_element, ref_def)
                policy.addReference(ref_def)
            elif tag_name == "ECUC-INSTANCE-REFERENCE-DEF":
                ref_def = EcucInstanceReferenceDef(policy, self.getShortName(child_element))
                self.readEcucInstanceReferenceDef(child_element, ref_def)
                policy.addReference(ref_def)
            else:
                self.notImplemented("Unsupported DestinationUriPolicy Reference <%s>" % tag_name)

    def readEcucValueConfigurationClass(self, element: ET.Element, cfg_class: EcucValueConfigurationClass):
        self.readEcucAbstractConfigurationClass(element, cfg_class)

    def getEcucValueConfigurationClasses(self, element: ET.Element) -> List[EcucValueConfigurationClass]:
        cfg_classes = []
        for child_element in self.findall(element, "VALUE-CONFIG-CLASSES/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "ECUC-VALUE-CONFIGURATION-CLASS":
                cfg_class = EcucValueConfigurationClass()
                self.readEcucValueConfigurationClass(child_element, cfg_class)
                cfg_classes.append(cfg_class)
            else:
                self.notImplemented("Unsupported ValueConfigClass <%s>" % tag_name)
        return cfg_classes

    def readEcucCommonAttributes(self, element: ET.Element, common_attrs: EcucCommonAttributes):
        self.readEcucDefinitionElement(element, common_attrs)
        for cfg_class in self.getEcucMultiplicityConfigurationClasses(element):
            common_attrs.addMultiplicityConfigClass(cfg_class)
        common_attrs.setOrigin(self.getChildElementOptionalLiteral(element, "ORIGIN"))
        common_attrs.setPostBuildVariantMultiplicity(self.getChildElementOptionalBooleanValue(element, "POST-BUILD-VARIANT-MULTIPLICITY"))
        common_attrs.setPostBuildVariantValue(self.getChildElementOptionalBooleanValue(element, "POST-BUILD-VARIANT-VALUE"))
        common_attrs.setRequiresIndex(self.getChildElementOptionalBooleanValue(element, "REQUIRES-INDEX"))
        for cfg_class in self.getEcucValueConfigurationClasses(element):
            common_attrs.addValueConfigClass(cfg_class)

    def readEcucParameterDef(self, element: ET.Element, param_def: EcucParameterDef):
        self.readEcucCommonAttributes(element, param_def)
        param_def.setDerivation(self.readEcucDerivationSpecification(element))
        param_def.setSymbolicNameValue(self.getChildElementOptionalBooleanValue(element, "SYMBOLIC-NAME-VALUE"))
        param_def.setWithAuto(self.getChildElementOptionalBooleanValue(element, "WITH-AUTO"))

    def readEcucDerivationSpecification(self, element: ET.Element) -> Optional[EcucDerivationSpecification]:
        child_element = self.find(element, "DERIVATION")
        if child_element is None:
            return None
        derivation = EcucDerivationSpecification()
        calc_formula = self.find(child_element, "CALCULATION-FORMULA")
        if calc_formula is not None:
            derivation.setCalculationFormula(self.readEcucParameterDerivationFormula(calc_formula))
        for query_element in self.findall(child_element, "ECUC-QUERYS/ECUC-QUERY"):
            query = derivation.createEcucQuery(self.getShortName(query_element))
            self.readEcucQuery(query_element, query)
        derivation.setInformalFormula(self.getMlFormula(child_element, "INFORMAL-FORMULA"))
        return derivation

    def readEcucParameterDerivationFormula(self, element: ET.Element) -> EcucParameterDerivationFormula:
        formula = EcucParameterDerivationFormula()
        formula.setEcucQueryRef(self.getChildElementOptionalRefType(element, "ECUC-QUERY-REF"))
        formula.setEcucQueryStringRef(self.getChildElementOptionalRefType(element, "ECUC-QUERY-STRING-REF"))
        return formula

    def readEcucConditionFormula(self, element: ET.Element) -> EcucConditionFormula:
        formula = EcucConditionFormula()
        formula.setEcucQueryRef(self.getChildElementOptionalRefType(element, "ECUC-QUERY-REF"))
        formula.setEcucQueryStringRef(self.getChildElementOptionalRefType(element, "ECUC-QUERY-STRING-REF"))
        return formula

    def readEcucConditionSpecification(self, element: ET.Element) -> Optional[EcucConditionSpecification]:
        child_element = self.find(element, "ECUC-COND")
        if child_element is None:
            return None
        cond = EcucConditionSpecification()
        formula_element = self.find(child_element, "CONDITION-FORMULA")
        if formula_element is not None:
            cond.setConditionFormula(self.readEcucConditionFormula(formula_element))
        for query_element in self.findall(child_element, "ECUC-QUERYS/ECUC-QUERY"):
            query = cond.createEcucQuery(self.getShortName(query_element))
            self.readEcucQuery(query_element, query)
        cond.setInformalFormula(self.getMlFormula(child_element, "INFORMAL-FORMULA"))
        return cond

    def readEcucValidationCondition(self, element: ET.Element) -> EcucValidationCondition:
        vc = EcucValidationCondition(None, self.getShortName(element))
        self.readIdentifiable(element, vc)
        for query_element in self.findall(element, "ECUC-QUERYS/ECUC-QUERY"):
            query = vc.createEcucQuery(self.getShortName(query_element))
            self.readEcucQuery(query_element, query)
        formula_element = self.find(element, "VALIDATION-FORMULA")
        if formula_element is not None:
            vc.setValidationFormula(self.readEcucConditionFormula(formula_element))
        return vc

    def readEcucValidationConditions(self, element: ET.Element, def_element: EcucDefinitionElement):
        for vc_element in self.findall(element, "ECUC-VALIDATION-CONDS/ECUC-VALIDATION-CONDITION"):
            vc = self.readEcucValidationCondition(vc_element)
            def_element.addEcucValidationCond(vc)

    def readEcucQuery(self, element: ET.Element, query: EcucQuery):
        self.readIdentifiable(element, query)
        expr_element = self.find(element, "ECUC-QUERY-EXPRESSION")
        if expr_element is not None:
            expr = EcucQueryExpression()
            expr.setConfigElementDefGlobalRef(self.getChildElementOptionalRefType(expr_element, "CONFIG-ELEMENT-DEF-GLOBAL-REF"))
            expr.setConfigElementDefLocalRef(self.getChildElementOptionalRefType(expr_element, "CONFIG-ELEMENT-DEF-LOCAL-REF"))
            query.setEcucQueryExpression(expr)

    def readEcucBooleanParamDef(self, element: ET.Element, param_def: EcucBooleanParamDef):
        self.readEcucParameterDef(element, param_def)
        param_def.setDefaultValue(self.getChildElementOptionalBooleanValue(element, "DEFAULT-VALUE"))

    def readEcucAbstractStringParamDef(self, element: ET.Element, param_def: EcucAbstractStringParamDef):
        self.readEcucParameterDef(element, param_def)
        param_def.setDefaultValue(self.getChildElementOptionalLiteral(element, "DEFAULT-VALUE"))
        param_def.setMaxLength(self.getChildElementOptionalIntegerValue(element, "MAX-LENGTH"))
        param_def.setMinLength(self.getChildElementOptionalIntegerValue(element, "MIN-LENGTH"))
        param_def.setRegularExpression(self.getChildElementOptionalLiteral(element, "REGULAR-EXPRESSION"))

    def readEcucStringParamDef(self, element: ET.Element, param_def: EcucStringParamDef):
        self.readEcucParameterDef(element, param_def)
        child_element = self.find(element, "ECUC-STRING-PARAM-DEF-VARIANTS/ECUC-STRING-PARAM-DEF-CONDITIONAL")
        if child_element is not None:
            param_def.setDefaultValue(self.getChildElementOptionalLiteral(child_element, "DEFAULT-VALUE"))
            param_def.setMinLength(self.getChildElementOptionalIntegerValue(child_element, "MIN-LENGTH"))
            param_def.setMaxLength(self.getChildElementOptionalIntegerValue(child_element, "MAX-LENGTH"))
            param_def.setRegularExpression(self.getChildElementOptionalLiteral(child_element, "REGULAR-EXPRESSION"))

    def readEcucMultilineStringParamDef(self, element: ET.Element, param_def: EcucMultilineStringParamDef):
        self.readEcucParameterDef(element, param_def)
        child_element = self.find(element, "ECUC-MULTILINE-STRING-PARAM-DEF-VARIANTS/ECUC-MULTILINE-STRING-PARAM-DEF-CONDITIONAL")
        if child_element is not None:
            param_def.setDefaultValue(self.getChildElementOptionalLiteral(child_element, "DEFAULT-VALUE"))
            param_def.setMinLength(self.getChildElementOptionalIntegerValue(child_element, "MIN-LENGTH"))
            param_def.setMaxLength(self.getChildElementOptionalIntegerValue(child_element, "MAX-LENGTH"))
            param_def.setRegularExpression(self.getChildElementOptionalLiteral(child_element, "REGULAR-EXPRESSION"))

    def readEcucIntegerParamDef(self, element: ET.Element, param_def: EcucIntegerParamDef):
        self.readEcucParameterDef(element, param_def)
        param_def.setDefaultValue(self.getChildElementOptionalIntegerValue(element, "DEFAULT-VALUE"))
        param_def.setMax(self.getChildElementOptionalIntegerValue(element, "MAX"))
        param_def.setMin(self.getChildElementOptionalIntegerValue(element, "MIN"))

    def readEcucFloatParamDef(self, element: ET.Element, param_def: EcucFloatParamDef):
        self.readEcucParameterDef(element, param_def)
        param_def.setDefaultValue(self.getChildElementOptionalFloatValue(element, "DEFAULT-VALUE"))
        param_def.setMax(self.getChildLimitElement(element, "MAX"))
        param_def.setMin(self.getChildLimitElement(element, "MIN"))

    def readEcucEnumerationLiteral(self, element: ET.Element, literal: EcucEnumerationLiteralDef):
        self.readIdentifiable(element, literal)
        literal.setOrigin(self.getChildElementOptionalLiteral(element, "ORIGIN"))

    def readEcucEnumerationParamDefLiterals(self, element: ET.Element, literal_def: EcucEnumerationParamDef):
        for child_element in self.findall(element, "LITERALS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "ECUC-ENUMERATION-LITERAL-DEF":
                literal = literal_def.createLiteral(self.getShortName(child_element))
                self.readEcucEnumerationLiteral(child_element, literal)
            else:
                self.notImplemented("Unsupported EnumerationLiteral <%s>" % tag_name)

    def readEcucEnumerationParamDef(self, element: ET.Element, param_def: EcucEnumerationParamDef):
        self.readEcucParameterDef(element, param_def)
        param_def.setDefaultValue(self.getChildElementOptionalLiteral(element, "DEFAULT-VALUE"))
        self.readEcucEnumerationParamDefLiterals(element, param_def)

    def readEcucFunctionNameDef(self, element: ET.Element, ref_def: EcucFunctionNameDef):
        self.readEcucParameterDef(element, ref_def)
        child_element = self.find(element, "ECUC-FUNCTION-NAME-DEF-VARIANTS/ECUC-FUNCTION-NAME-DEF-CONDITIONAL")
        if child_element is not None:
            ref_def.setDefaultValue(self.getChildElementOptionalLiteral(child_element, "DEFAULT-VALUE"))
            ref_def.setMinLength(self.getChildElementOptionalIntegerValue(child_element, "MIN-LENGTH"))
            ref_def.setMaxLength(self.getChildElementOptionalIntegerValue(child_element, "MAX-LENGTH"))
            ref_def.setRegularExpression(self.getChildElementOptionalLiteral(child_element, "REGULAR-EXPRESSION"))

    def readEcucContainerDefParameters(self, element: ET.Element, container_def: EcucParamConfContainerDef):
        for child_element in self.findall(element, "PARAMETERS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "ECUC-BOOLEAN-PARAM-DEF":
                param_def = container_def.createEcucBooleanParamDef(self.getShortName(child_element))
                self.readEcucBooleanParamDef(child_element, param_def)
            elif tag_name == "ECUC-STRING-PARAM-DEF":
                param_def = container_def.createEcucStringParamDef(self.getShortName(child_element))
                self.readEcucStringParamDef(child_element, param_def)
            elif tag_name == "ECUC-INTEGER-PARAM-DEF":
                param_def = container_def.createEcucIntegerParamDef(self.getShortName(child_element))
                self.readEcucIntegerParamDef(child_element, param_def)
            elif tag_name == "ECUC-FLOAT-PARAM-DEF":
                param_def = container_def.createEcucFloatParamDef(self.getShortName(child_element))
                self.readEcucFloatParamDef(child_element, param_def)
            elif tag_name == "ECUC-ENUMERATION-PARAM-DEF":
                param_def = container_def.createEcucEnumerationParamDef(self.getShortName(child_element))
                self.readEcucEnumerationParamDef(child_element, param_def)
            elif tag_name == "ECUC-FUNCTION-NAME-DEF":
                param_def = container_def.createEcucFunctionNameDef(self.getShortName(child_element))
                self.readEcucFunctionNameDef(child_element, param_def)
            elif tag_name == "ECUC-MULTILINE-STRING-PARAM-DEF":
                param_def = container_def.createEcucMultilineStringParamDef(self.getShortName(child_element))
                self.readEcucMultilineStringParamDef(child_element, param_def)
            else:
                self.notImplemented("Unsupported Parameter <%s>" % tag_name)

    def readEcucAbstractReferenceDef(self, element: ET.Element, ref_def: EcucAbstractReferenceDef):
        self.readEcucCommonAttributes(element, ref_def)
        ref_def.setWithAuto(self.getChildElementOptionalBooleanValue(element, "WITH-AUTO"))

    def readEcucAbstractInternalReferenceDef(self, element: ET.Element, ref_def: EcucAbstractInternalReferenceDef):
        self.readEcucAbstractReferenceDef(element, ref_def)
        ref_def.setRequiresSymbolicNameValue(self.getChildElementOptionalBooleanValue(element, "REQUIRES-SYMBOLIC-NAME-VALUE"))

    def readEcucAbstractExternalReferenceDef(self, element: ET.Element, ref_def: EcucAbstractExternalReferenceDef):
        self.readEcucAbstractReferenceDef(element, ref_def)

    def readEcucSymbolicNameReferenceDef(self, element: ET.Element, ref_def: EcucSymbolicNameReferenceDef):
        self.readEcucAbstractInternalReferenceDef(element, ref_def)
        ref_def.setDestinationRef(self.getChildElementOptionalRefType(element, "DESTINATION-REF"))

    def readEcucReferenceDef(self, element: ET.Element, ref_def: EcucReferenceDef):
        self.readEcucAbstractInternalReferenceDef(element, ref_def)
        ref_def.setDestinationRef(self.getChildElementOptionalRefType(element, "DESTINATION-REF"))

    def readEcucChoiceReferenceDef(self, element: ET.Element, ref_def: EcucChoiceReferenceDef):
        self.readEcucAbstractInternalReferenceDef(element, ref_def)
        for ref in self.getChildElementRefTypeList(element, "DESTINATION-REFS/DESTINATION-REF"):
            ref_def.addDestinationRef(ref)

    def readEcucInstanceReferenceDef(self, element: ET.Element, ref_def: EcucInstanceReferenceDef):
        self.readEcucAbstractExternalReferenceDef(element, ref_def)
        ref_def.setDestinationContext(self.getChildElementOptionalLiteral(element, "DESTINATION-CONTEXT"))
        ref_def.setDestinationType(self.getChildElementOptionalLiteral(element, "DESTINATION-TYPE"))

    def readEcucContainerDefReferences(self, element: ET.Element, container_def: EcucParamConfContainerDef):
        for child_element in self.findall(element, "REFERENCES/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "ECUC-SYMBOLIC-NAME-REFERENCE-DEF":
                ref_def = container_def.createEcucSymbolicNameReferenceDef(self.getShortName(child_element))
                self.readEcucSymbolicNameReferenceDef(child_element, ref_def)
            elif tag_name == "ECUC-REFERENCE-DEF":
                ref_def = container_def.createEcucReferenceDef(self.getShortName(child_element))
                self.readEcucReferenceDef(child_element, ref_def)
            elif tag_name == "ECUC-CHOICE-REFERENCE-DEF":
                ref_def = container_def.createEcucChoiceReferenceDef(self.getShortName(child_element))
                self.readEcucChoiceReferenceDef(child_element, ref_def)
            elif tag_name == "ECUC-INSTANCE-REFERENCE-DEF":
                ref_def = container_def.createEcucInstanceReferenceDef(self.getShortName(child_element))
                self.readEcucInstanceReferenceDef(child_element, ref_def)
            else:
                self.notImplemented("Unsupported EcucReferenceDef <%s>" % tag_name)

    def readEcucContainerDefSubContainers(self, element: ET.Element, container_def: EcucParamConfContainerDef):
        for child_element in self.findall(element, "SUB-CONTAINERS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "ECUC-PARAM-CONF-CONTAINER-DEF":
                sub_container_def = container_def.createEcucParamConfContainerDef(self.getShortName(child_element))
                self.readEcucParamConfContainerDef(child_element, sub_container_def)
            elif tag_name == "ECUC-CHOICE-CONTAINER-DEF":
                sub_container_def = container_def.createEcucChoiceContainerDef(self.getShortName(child_element))
                self.readEcucChoiceContainerDef(child_element, sub_container_def)
            else:
                self.notImplemented("Unsupported SubContainer <%s>" % tag_name)

    def readEcucParamConfContainerDef(self, element: ET.Element, container_def: EcucParamConfContainerDef):
        self.readEcucContainerDef(element, container_def)
        self.readEcucContainerDefParameters(element, container_def)
        self.readEcucContainerDefReferences(element, container_def)
        self.readEcucContainerDefSubContainers(element, container_def)

    def readEcucChoiceContainerDefChoices(self, element: ET.Element, container_def: EcucChoiceContainerDef):
        for child_element in self.findall(element, "CHOICES/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "ECUC-PARAM-CONF-CONTAINER-DEF":
                ref_def = container_def.createEcucParamConfContainerDef(self.getShortName(child_element))
                self.readEcucParamConfContainerDef(child_element, ref_def)
            else:
                self.notImplemented("Unsupported Choice <%s>" % tag_name)

    def readEcucChoiceContainerDef(self, element: ET.Element, container_def: EcucChoiceContainerDef):
        self.readEcucContainerDef(element, container_def)
        self.readEcucChoiceContainerDefChoices(element, container_def)

    def readEcucModuleDefContainers(self, element: ET.Element, module_def: EcucModuleDef):
        for child_element in self.findall(element, "CONTAINERS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "ECUC-PARAM-CONF-CONTAINER-DEF":
                container_def = module_def.createEcucParamConfContainerDef(self.getShortName(child_element))
                self.readEcucParamConfContainerDef(child_element, container_def)
            elif tag_name == "ECUC-CHOICE-CONTAINER-DEF":
                container_def = module_def.createEcucChoiceContainerDef(self.getShortName(child_element))
                self.readEcucChoiceContainerDef(child_element, container_def)
            else:
                self.notImplemented("Unsupported Container <%s>" % tag_name)

    def readEcucModuleDef(self, element: ET.Element, module_def: EcucModuleDef):
        self.logger.debug("Read EcucModuleDef <%s>" % module_def.getShortName())
        self.readEcucDefinitionElement(element, module_def)
        module_def.setApiServicePrefix(self.getChildElementOptionalLiteral(element, "API-SERVICE-PREFIX"))
        module_def.setPostBuildVariantSupport(self.getChildElementOptionalBooleanValue(element, "POST-BUILD-VARIANT-SUPPORT"))
        module_def.setRefinedModuleDefRef(self.getChildElementOptionalRefType(element, "REFINED-MODULE-DEF-REF"))
        self.readEcucModuleDefSupportedConfigVariants(element, module_def)
        self.readEcucModuleDefContainers(element, module_def)

    def readEcucDefinitionCollection(self, element: ET.Element, collection: EcucDefinitionCollection):
        self.logger.debug("Read EcucDefinitionCollection <%s>" % collection.getShortName())
        self.readARElement(element, collection)
        module_refs = self.getChildElementRefTypeList(element, "MODULE-REFS/MODULE-REF")
        for module_ref in module_refs:
            collection.addModuleRef(module_ref)

    def readSwSystemconst(self, element: ET.Element, system_const: SwSystemconst):
        self.logger.debug("Read SwSystemconst <%s>" % system_const.getShortName())
        self.readIdentifiable(element, system_const)
        system_const.setSwDataDefProps(self.getSwDataDefProps(element, "SW-DATA-DEF-PROPS"))

    def readSwSystemconstValue(self, element: ET.Element, value: SwSystemconstValue):
        for annotation in self.getAnnotations(element):
            value.addAnnotation(annotation)
        value.setSwSystemconstRef(self.getChildElementOptionalRefType(element, "SW-SYSTEMCONST-REF"))
        value.setValue(self.getChildElementOptionalNumericalValue(element, "VALUE"))

    def readSwSystemconstantValueSetSwSystemconstantValues(self, element: ET.Element, value_set: SwSystemconstantValueSet):
        for child_element in self.findall(element, "SW-SYSTEMCONSTANT-VALUES/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "SW-SYSTEMCONST-VALUE":
                value = SwSystemconstValue()
                self.readSwSystemconstValue(child_element, value)
                value_set.addSwSystemconstantValue(value)
            else:
                self.notImplemented("Unsupported SwSystemconstValue <%s>" % tag_name)

    def readSwSystemconstantValueSet(self, element: ET.Element, value_set: SwSystemconstantValueSet):
        self.logger.debug("Read SwSystemconstantValueSet <%s>" % value_set.getShortName())
        self.readIdentifiable(element, value_set)
        self.readSwSystemconstantValueSetSwSystemconstantValues(element, value_set)

    def readPredefinedVariantIncludedVariantRefs(self, element: ET.Element, variant: PredefinedVariant):
        for ref in self.getChildElementRefTypeList(
            element,
            "INCLUDED-VARIANT-REFS/INCLUDED-VARIANT-REF",
        ):
            variant.addIncludedVariantRef(ref)

    def readPredefinedVariantPostBuildVariantCriterionValueSetRefs(self, element: ET.Element, variant: PredefinedVariant):
        for ref in self.getChildElementRefTypeList(
            element,
            "POST-BUILD-VARIANT-CRITERION-VALUE-SET-REFS/" "POST-BUILD-VARIANT-CRITERION-VALUE-SET-REF",
        ):
            variant.addPostBuildVariantCriterionValueSetRef(ref)

    def readPredefinedVariantSwSystemconstantValueSetRefs(self, element: ET.Element, variant: PredefinedVariant):
        for ref in self.getChildElementRefTypeList(
            element,
            "SW-SYSTEMCONSTANT-VALUE-SET-REFS/" "SW-SYSTEMCONSTANT-VALUE-SET-REF",
        ):
            variant.addSwSystemconstantValueSetRef(ref)

    def readPredefinedVariant(self, element: ET.Element, variant: PredefinedVariant):
        self.logger.debug("Read PredefinedVariant <%s>" % variant.getShortName())
        self.readIdentifiable(element, variant)
        self.readPredefinedVariantIncludedVariantRefs(element, variant)
        self.readPredefinedVariantPostBuildVariantCriterionValueSetRefs(element, variant)
        self.readPredefinedVariantSwSystemconstantValueSetRefs(element, variant)

    def readPostBuildVariantCriterion(self, element: ET.Element, criterion: PostBuildVariantCriterion):
        self.logger.debug("Read PostBuildVariantCriterion <%s>" % criterion.getShortName())
        self.readIdentifiable(element, criterion)
        criterion.setCompuMethodRef(self.getChildElementOptionalRefType(element, "COMPU-METHOD-REF"))

    def readCommunicationController(self, element: ET.Element, controller: CommunicationController):
        controller.setWakeUpByControllerSupported(self.getChildElementOptionalBooleanValue(element, "WAKE-UP-BY-CONTROLLER-SUPPORTED"))

    def getCanControllerFdConfiguration(self, element: ET.Element, key: str) -> CanControllerFdConfiguration:
        configuration = None
        child_element = self.find(element, key)
        if child_element is not None:
            configuration = CanControllerFdConfiguration()
            configuration.setPaddingValue(self.getChildElementOptionalIntegerValue(child_element, "PADDING-VALUE"))
            configuration.setPropSeg(self.getChildElementOptionalIntegerValue(child_element, "PROP-SEG"))
            configuration.setSspOffset(self.getChildElementOptionalIntegerValue(child_element, "SSP-OFFSET"))
            configuration.setSyncJumpWidth(self.getChildElementOptionalIntegerValue(child_element, "SYNC-JUMP-WIDTH"))
            configuration.setTimeSeg1(self.getChildElementOptionalIntegerValue(child_element, "TIME-SEG1"))
            configuration.setTimeSeg2(self.getChildElementOptionalIntegerValue(child_element, "TIME-SEG2"))
            configuration.setTxBitRateSwitch(self.getChildElementOptionalBooleanValue(child_element, "TX-BIT-RATE-SWITCH"))
        return configuration

    def getFlexrayFifoRange(self, element: ET.Element, key: str) -> FlexrayFifoRange:
        fifo_range = None
        child_element = self.find(element, key)
        if child_element is not None:
            fifo_range = FlexrayFifoRange()
            fifo_range.setRangeMax(self.getChildElementOptionalIntegerValue(child_element, "RANGE-MAX"))
            fifo_range.setRangeMin(self.getChildElementOptionalIntegerValue(child_element, "RANGE-MIN"))
        return fifo_range

    def getFlexrayFifoConfiguration(self, element: ET.Element, key: str) -> FlexrayFifoConfiguration:
        configuration = None
        child_element = self.find(element, key)
        if child_element is not None:
            configuration = FlexrayFifoConfiguration()
            configuration.setAdmitWithoutMessageId(self.getChildElementOptionalBooleanValue(child_element, "ADMIT-WITHOUT-MESSAGE-ID"))
            configuration.setBaseCycle(self.getChildElementOptionalIntegerValue(child_element, "BASE-CYCLE"))
            configuration.setChannelRef(self.getChildElementOptionalRefType(child_element, "CHANNEL-REF"))
            configuration.setCycleRepetition(self.getChildElementOptionalIntegerValue(child_element, "CYCLE-REPETITION"))
            configuration.setFifoDepth(self.getChildElementOptionalIntegerValue(child_element, "FIFO-DEPTH"))
            for range_child in self.findall(child_element, "FLEXRAY-FIFO-RANGE"):
                fifo_range = configuration.createFlexrayFifoRange()
                fifo_range.setRangeMax(self.getChildElementOptionalIntegerValue(range_child, "RANGE-MAX"))
                fifo_range.setRangeMin(self.getChildElementOptionalIntegerValue(range_child, "RANGE-MIN"))
            configuration.setMsgIdMask(self.getChildElementOptionalIntegerValue(child_element, "MSG-ID-MASK"))
            configuration.setMsgIdMatch(self.getChildElementOptionalIntegerValue(child_element, "MSG-ID-MATCH"))
        return configuration

    def getCanControllerFdConfigurationRequirements(self, element: ET.Element, key: str) -> CanControllerFdConfigurationRequirements:
        requirements = None
        child_element = self.find(element, key)
        if child_element is not None:
            requirements = CanControllerFdConfigurationRequirements()
            requirements.setMaxNumberOfTimeQuantaPerBit(self.getChildElementOptionalIntegerValue(child_element, "MAX-NUMBER-OF-TIME-QUANTA-PER-BIT"))
            requirements.setMaxSamplePoint(self.getChildElementOptionalFloatValue(child_element, "MAX-SAMPLE-POINT"))
            requirements.setMaxSyncJumpWidth(self.getChildElementOptionalFloatValue(child_element, "MAX-SYNC-JUMP-WIDTH"))
            requirements.setMaxTrcvDelayCompensationOffset(self.getChildElementOptionalTimeValue(child_element, "MAX-TRCV-DELAY-COMPENSATION-OFFSET"))
            requirements.setMinNumberOfTimeQuantaPerBit(self.getChildElementOptionalIntegerValue(child_element, "MIN-NUMBER-OF-TIME-QUANTA-PER-BIT"))
            requirements.setMinSamplePoint(self.getChildElementOptionalFloatValue(child_element, "MIN-SAMPLE-POINT"))
            requirements.setMinSyncJumpWidth(self.getChildElementOptionalFloatValue(child_element, "MIN-SYNC-JUMP-WIDTH"))
            requirements.setMinTrcvDelayCompensationOffset(self.getChildElementOptionalTimeValue(child_element, "MIN-TRCV-DELAY-COMPENSATION-OFFSET"))
            requirements.setTxBitRateSwitch(self.getChildElementOptionalBooleanValue(child_element, "TX-BIT-RATE-SWITCH"))  # NOQA E501
        return requirements

    def getCanControllerXlConfiguration(self, element: ET.Element, key: str) -> CanControllerXlConfiguration:
        configuration = None
        child_element = self.find(element, key)
        if child_element is not None:
            configuration = CanControllerXlConfiguration()
            configuration.setErrorSignalingEnabled(self.getChildElementOptionalBooleanValue(child_element, "ERROR-SIGNALING-ENABLED"))
            configuration.setPropSeg(self.getChildElementOptionalIntegerValue(child_element, "PROP-SEG"))
            configuration.setPwmL(self.getChildElementOptionalIntegerValue(child_element, "PWM-L"))
            configuration.setPwmO(self.getChildElementOptionalIntegerValue(child_element, "PWM-O"))
            configuration.setPwmS(self.getChildElementOptionalIntegerValue(child_element, "PWM-S"))
            configuration.setSspOffset(self.getChildElementOptionalIntegerValue(child_element, "SSP-OFFSET"))
            configuration.setSyncJumpWidth(self.getChildElementOptionalIntegerValue(child_element, "SYNC-JUMP-WIDTH"))
            configuration.setTimeSeg1(self.getChildElementOptionalIntegerValue(child_element, "TIME-SEG1"))
            configuration.setTimeSeg2(self.getChildElementOptionalIntegerValue(child_element, "TIME-SEG2"))
            configuration.setTrcvPwmModeEnabled(self.getChildElementOptionalBooleanValue(child_element, "TRCV-PWM-MODE-ENABLED"))
        return configuration

    def getCanControllerXlConfigurationRequirements(self, element: ET.Element, key: str) -> CanControllerXlConfigurationRequirements:
        requirements = None
        child_element = self.find(element, key)
        if child_element is not None:
            requirements = CanControllerXlConfigurationRequirements()
            requirements.setErrorSignalingEnabled(self.getChildElementOptionalBooleanValue(child_element, "ERROR-SIGNALING-ENABLED"))
            requirements.setMaxNumberOfTimeQuantaPerBit(self.getChildElementOptionalIntegerValue(child_element, "MAX-NUMBER-OF-TIME-QUANTA-PER-BIT"))
            requirements.setMaxPwmL(self.getChildElementOptionalIntegerValue(child_element, "MAX-PWM-L"))
            requirements.setMaxPwmO(self.getChildElementOptionalIntegerValue(child_element, "MAX-PWM-O"))
            requirements.setMaxPwmS(self.getChildElementOptionalIntegerValue(child_element, "MAX-PWM-S"))
            requirements.setMaxSamplePoint(self.getChildElementOptionalFloatValue(child_element, "MAX-SAMPLE-POINT"))
            requirements.setMaxSyncJumpWidth(self.getChildElementOptionalFloatValue(child_element, "MAX-SYNC-JUMP-WIDTH"))
            requirements.setMaxTrcvDelayCompensationOffset(self.getChildElementOptionalTimeValue(child_element, "MAX-TRCV-DELAY-COMPENSATION-OFFSET"))
            requirements.setMinNumberOfTimeQuantaPerBit(self.getChildElementOptionalIntegerValue(child_element, "MIN-NUMBER-OF-TIME-QUANTA-PER-BIT"))
            requirements.setMinPwmL(self.getChildElementOptionalIntegerValue(child_element, "MIN-PWM-L"))
            requirements.setMinPwmO(self.getChildElementOptionalIntegerValue(child_element, "MIN-PWM-O"))
            requirements.setMinPwmS(self.getChildElementOptionalIntegerValue(child_element, "MIN-PWM-S"))
            requirements.setMinSamplePoint(self.getChildElementOptionalFloatValue(child_element, "MIN-SAMPLE-POINT"))
            requirements.setMinSyncJumpWidth(self.getChildElementOptionalFloatValue(child_element, "MIN-SYNC-JUMP-WIDTH"))
            requirements.setMinTrcvDelayCompensationOffset(self.getChildElementOptionalTimeValue(child_element, "MIN-TRCV-DELAY-COMPENSATION-OFFSET"))
            requirements.setTrcvPwmModeEnabled(self.getChildElementOptionalBooleanValue(child_element, "TRCV-PWM-MODE-ENABLED"))
        return requirements

    def readAbstractCanCommunicationControllerAttributes(self, element: ET.Element, attributes: AbstractCanCommunicationControllerAttributes):
        attributes.setCanControllerFdAttributes(self.getCanControllerFdConfiguration(element, "CAN-CONTROLLER-FD-CONFIGURATION"))
        attributes.setCanControllerFdRequirements(self.getCanControllerFdConfigurationRequirements(element, "CAN-CONTROLLER-FD-REQUIREMENTS"))
        attributes.setCanControllerXlAttributes(self.getCanControllerXlConfiguration(element, "CAN-CONTROLLER-XL-CONFIGURATION"))
        attributes.setCanControllerXlRequirements(self.getCanControllerXlConfigurationRequirements(element, "CAN-CONTROLLER-XL-REQUIREMENTS"))

    def readCanControllerConfigurationRequirements(self, element: ET.Element, requirements: CanControllerConfigurationRequirements):
        self.readAbstractCanCommunicationControllerAttributes(element, requirements)
        requirements.setMaxNumberOfTimeQuantaPerBit(self.getChildElementOptionalIntegerValue(element, "MAX-NUMBER-OF-TIME-QUANTA-PER-BIT"))
        requirements.setMaxSamplePoint(self.getChildElementOptionalFloatValue(element, "MAX-SAMPLE-POINT"))
        requirements.setMaxSyncJumpWidth(self.getChildElementOptionalFloatValue(element, "MAX-SYNC-JUMP-WIDTH"))
        requirements.setMinNumberOfTimeQuantaPerBit(self.getChildElementOptionalIntegerValue(element, "MIN-NUMBER-OF-TIME-QUANTA-PER-BIT"))
        requirements.setMinSamplePoint(self.getChildElementOptionalFloatValue(element, "MIN-SAMPLE-POINT"))
        requirements.setMinSyncJumpWidth(self.getChildElementOptionalFloatValue(element, "MIN-SYNC-JUMP-WIDTH"))

    def readAbstractCanCommunicationControllerCanControllerAttributes(self, element: ET.SubElement, controller: AbstractCanCommunicationController):
        for child_element in self.findall(element, "CAN-CONTROLLER-ATTRIBUTES/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "CAN-CONTROLLER-CONFIGURATION-REQUIREMENTS":
                requirements = CanControllerConfigurationRequirements()
                self.readCanControllerConfigurationRequirements(child_element, requirements)
                controller.setCanControllerAttributes(requirements)
            else:
                self.notImplemented("Unsupported CanControllerAttributes <%s>" % tag_name)

    def readAbstractCanCommunicationController(self, element: ET.Element, controller: AbstractCanCommunicationController):
        self.readCommunicationController(element, controller)
        self.readAbstractCanCommunicationControllerCanControllerAttributes(element, controller)

    def readCanCommunicationController(self, element: ET.Element, controller: CanCommunicationController):
        self.logger.debug("Read CanCommunicationController %s" % controller.getShortName())
        self.readIdentifiable(element, controller)
        child_element = self.find(element, "CAN-COMMUNICATION-CONTROLLER-VARIANTS/CAN-COMMUNICATION-CONTROLLER-CONDITIONAL")
        if child_element is not None:
            self.readAbstractCanCommunicationController(child_element, controller)

    def readCouplingPortSchedulerCouplingPortStructuralElement(self, element: ET.Element, item: CouplingPortStructuralElement):
        self.readIdentifiable(element, item)

    def readCouplingPortFifo(self, element: ET.Element, fifo: CouplingPortFifo):
        self.readCouplingPortSchedulerCouplingPortStructuralElement(element, fifo)

    def readCouplingPortScheduler(self, element: ET.Element, scheduler: CouplingPortScheduler):
        self.readCouplingPortSchedulerCouplingPortStructuralElement(element, scheduler)
        scheduler.setPortScheduler(self.getChildElementOptionalLiteral(element, "PORT-SCHEDULER"))

    def readCouplingPortDetailsCouplingPortStructuralElements(self, item: ET.Element, details: CouplingPortDetails):
        for child_element in self.findall(item, "COUPLING-PORT-STRUCTURAL-ELEMENTS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "COUPLING-PORT-FIFO":
                item = details.createCouplingPortFifo(self.getShortName(child_element))
                self.readCouplingPortFifo(child_element, item)
            elif tag_name == "COUPLING-PORT-SCHEDULER":
                item = details.createCouplingPortScheduler(self.getShortName(child_element))
                self.readCouplingPortScheduler(child_element, item)
            else:
                self.notImplemented("Unsupported CouplingPortStructuralElement <%s>" % tag_name)

    def readEthernetPriorityRegeneration(self, element: ET.Element, regeneration: EthernetPriorityRegeneration):
        regeneration.setIngressPriority(self.getChildElementOptionalPositiveInteger(element, "INGRESS-PRIORITY"))
        regeneration.setRegeneratedPriority(self.getChildElementOptionalPositiveInteger(element, "REGENERATED-PRIORITY"))

    def readCouplingPortDetailsEthernetPriorityRegenerations(self, element: ET.Element, details: CouplingPortDetails):
        for child_element in self.findall(element, "ETHERNET-PRIORITY-REGENERATIONS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "ETHERNET-PRIORITY-REGENERATION":
                item = details.createEthernetPriorityRegeneration(self.getShortName(child_element))
                self.readEthernetPriorityRegeneration(child_element, item)
            else:
                self.notImplemented("Unsupported EthernetPriorityRegeneration <%s>" % tag_name)

    def getCouplingPortDetails(self, element: ET.Element, key: str) -> CouplingPortDetails:
        details = None
        child_element = self.find(element, key)
        if child_element is not None:
            details = CouplingPortDetails()
            self.readCouplingPortDetailsCouplingPortStructuralElements(child_element, details)
            self.readCouplingPortDetailsEthernetPriorityRegenerations(child_element, details)
            details.setLastEgressSchedulerRef(self.getChildElementOptionalRefType(child_element, "LAST-EGRESS-SCHEDULER-REF"))
        return details

    def readVlanMembership(self, element: ET.Element, membership: VlanMembership):
        membership.setSendActivity(self.getChildElementOptionalLiteral(element, "SEND-ACTIVITY"))
        membership.setVlanRef(self.getChildElementOptionalRefType(element, "VLAN-REF"))

    def readCouplingPortVlanMemberships(self, element: ET.Element, port: CouplingPort):
        for child_element in self.findall(element, "VLAN-MEMBERSHIPS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "VLAN-MEMBERSHIP":
                membership = VlanMembership()
                self.readVlanMembership(child_element, membership)
                port.addVlanMembership(membership)
            else:
                self.notImplemented("Unsupported VlanMembership <%s>" % tag_name)

    def readCouplingPort(self, element: ET.Element, port: CouplingPort):
        self.readIdentifiable(element, port)
        port.setCouplingPortDetails(self.getCouplingPortDetails(element, "COUPLING-PORT-DETAILS"))
        port.setMacLayerType(self.getChildElementOptionalLiteral(element, "MAC-LAYER-TYPE"))
        self.readCouplingPortVlanMemberships(element, port)

    def readEthernetCommunicationControllerCouplingPorts(self, element: ET.Element, controller: EthernetCommunicationController):
        for child_element in self.findall(element, "COUPLING-PORTS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "COUPLING-PORT":
                port = controller.createCouplingPort(self.getShortName(child_element))
                self.readCouplingPort(child_element, port)
            else:
                self.notImplemented("Unsupported Coupling Port <%s>" % tag_name)

    def readEthernetCommunicationController(self, element: ET.Element, controller: EthernetCommunicationController):
        self.logger.debug("Read EthernetCommunicationController %s" % controller.getShortName())
        self.readIdentifiable(element, controller)
        child_element = self.find(element, "ETHERNET-COMMUNICATION-CONTROLLER-VARIANTS/ETHERNET-COMMUNICATION-CONTROLLER-CONDITIONAL")
        if child_element is not None:
            self.readCommunicationController(child_element, controller)
            self.readEthernetCommunicationControllerCouplingPorts(child_element, controller)

    def readLinCommunicationController(self, element: ET.Element, controller: LinCommunicationController):
        self.readCommunicationController(element, controller)
        controller.setProtocolVersion(self.getChildElementOptionalLiteral(element, "PROTOCOL-VERSION"))

    def readLinMaster(self, element: ET.Element, controller: LinMaster):
        self.logger.debug("Read LinMaster %s" % controller.getShortName())
        self.readIdentifiable(element, controller)
        child_element = self.find(element, "LIN-MASTER-VARIANTS/LIN-MASTER-CONDITIONAL")
        if child_element is not None:
            self.readLinCommunicationController(child_element, controller)
            slaves_wrapper = self.find(child_element, "LIN-SLAVES")
            if slaves_wrapper is not None:
                for slave_element in self.findall(slaves_wrapper, "LIN-SLAVE-CONFIG"):
                    controller.addLinSlave(self.readLinSlaveConfig(slave_element))
            controller.setTimeBase(self.getChildElementOptionalTimeValue(child_element, "TIME-BASE"))
            controller.setTimeBaseJitter(self.getChildElementOptionalTimeValue(child_element, "TIME-BASE-JITTER"))

    def getLinErrorResponse(self, element: ET.Element, key: str) -> LinErrorResponse:
        response = None
        child_element = self.find(element, key)
        if child_element is not None:
            response = LinErrorResponse()
            response.setResponseErrorRef(self.getChildElementOptionalRefType(child_element, "RESPONSE-ERROR-REF"))
        return response

    def getLinConfigurableFrame(self, element: ET.Element, key: str) -> LinConfigurableFrame:
        frame = None
        child_element = self.find(element, key)
        if child_element is not None:
            frame = LinConfigurableFrame()
            frame.setFrameRef(self.getChildElementOptionalRefType(child_element, "FRAME-REF"))
            frame.setMessageId(self.getChildElementOptionalPositiveInteger(child_element, "MESSAGE-ID"))
        return frame

    def getLinOrderedConfigurableFrame(self, element: ET.Element, key: str) -> LinOrderedConfigurableFrame:
        frame = None
        child_element = self.find(element, key)
        if child_element is not None:
            frame = LinOrderedConfigurableFrame()
            frame.setFrameRef(self.getChildElementOptionalRefType(child_element, "FRAME-REF"))
            frame.setIndex(self.getChildElementOptionalIntegerValue(child_element, "INDEX"))
        return frame

    def getLinSlaveConfig(self, element: ET.Element, key: str) -> LinSlaveConfig:
        config = None
        child_element = self.find(element, key)
        if child_element is not None:
            config = self.readLinSlaveConfig(child_element)
        return config

    def readLinSlaveConfig(self, child_element: ET.Element) -> LinSlaveConfig:
        config = LinSlaveConfig()
        config.setConfiguredNad(self.getChildElementOptionalIntegerValue(child_element, "CONFIGURED-NAD"))
        config.setFunctionId(self.getChildElementOptionalPositiveInteger(child_element, "FUNCTION-ID"))
        ident_element = self.find(child_element, "IDENT")
        if ident_element is not None:
            ident = LinSlaveConfigIdent(config, self.getShortName(ident_element))
            self.readReferrable(ident_element, ident)
            config.setIdent(ident)
        config.setInitialNad(self.getChildElementOptionalIntegerValue(child_element, "INITIAL-NAD"))
        frames_wrapper = self.find(child_element, "LIN-CONFIGURABLE-FRAMES")
        if frames_wrapper is not None:
            for frame_element in self.findall(frames_wrapper, "LIN-CONFIGURABLE-FRAME"):
                frame = LinConfigurableFrame()
                frame.setFrameRef(self.getChildElementOptionalRefType(frame_element, "FRAME-REF"))
                frame.setMessageId(self.getChildElementOptionalPositiveInteger(frame_element, "MESSAGE-ID"))
                config.addLinConfigurableFrame(frame)
        config.setLinErrorResponse(self.getLinErrorResponse(child_element, "LIN-ERROR-RESPONSE"))
        ordered_wrapper = self.find(child_element, "LIN-ORDERED-CONFIGURABLE-FRAMES")
        if ordered_wrapper is not None:
            for frame_element in self.findall(ordered_wrapper, "LIN-ORDERED-CONFIGURABLE-FRAME"):
                frame = LinOrderedConfigurableFrame()
                frame.setFrameRef(self.getChildElementOptionalRefType(frame_element, "FRAME-REF"))
                frame.setIndex(self.getChildElementOptionalIntegerValue(frame_element, "INDEX"))
                config.addLinOrderedConfigurableFrame(frame)
        config.setProtocolVersion(self.getChildElementOptionalLiteral(child_element, "PROTOCOL-VERSION"))
        config.setSupplierId(self.getChildElementOptionalPositiveInteger(child_element, "SUPPLIER-ID"))
        config.setVariantId(self.getChildElementOptionalPositiveInteger(child_element, "VARIANT-ID"))
        return config

    def readEcuInstanceCommControllers(self, element: ET.Element, instance: EcuInstance):
        self.logger.debug("readEcuInstanceCommControllers %s" % instance.getShortName())
        for child_element in self.findall(element, "COMM-CONTROLLERS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "CAN-COMMUNICATION-CONTROLLER":
                controller = instance.createCanCommunicationController(self.getShortName(child_element))
                self.readCanCommunicationController(child_element, controller)
            elif tag_name == "ETHERNET-COMMUNICATION-CONTROLLER":
                controller = instance.createEthernetCommunicationController(self.getShortName(child_element))
                self.readEthernetCommunicationController(child_element, controller)
            elif tag_name == "LIN-MASTER":
                controller = instance.createLinMaster(self.getShortName(child_element))
                self.readLinMaster(child_element, controller)
            elif tag_name == "FLEXRAY-COMMUNICATION-CONTROLLER":
                controller = instance.createFlexrayCommunicationController(self.getShortName(child_element))
                self.readFlexrayCommunicationController(child_element, controller)
            else:
                self.raiseError("Unsupported Communication Controller <%s>" % tag_name)

    def readCommConnectorPort(self, element: ET.Element, port: CommConnectorPort):
        self.readIdentifiable(element, port)
        port.setCommunicationDirection(self.getChildElementOptionalLiteral(element, "COMMUNICATION-DIRECTION"))

    def readFramePort(self, element: ET.Element, port: FramePort):
        self.readCommConnectorPort(element, port)

    def readIPduPort(self, element: ET.Element, port: IPduPort):
        self.readCommConnectorPort(element, port)
        port.setKeyId(self.getChildElementOptionalPositiveInteger(element, "KEY-ID"))
        port.setRxSecurityVerification(self.getChildElementOptionalBooleanValue(element, "RX-SECURITY-VERIFICATION"))
        port.setUseAuthDataFreshness(self.getChildElementOptionalBooleanValue(element, "USE-AUTH-DATA-FRESHNESS"))

    def readISignalPort(self, element: ET.Element, port: ISignalPort):
        self.readCommConnectorPort(element, port)
        port.setTimeout(self.getChildElementOptionalTimeValue(element, "TIMEOUT"))

    def readCommunicationConnectorEcuCommPortInstances(self, element: ET.Element, connector: CommunicationConnector):
        self.logger.debug("read EcuCommPortInstances of CommunicationConnector %s" % connector.getShortName())
        for child_element in self.findall(element, "ECU-COMM-PORT-INSTANCES/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "FRAME-PORT":
                port = connector.createFramePort(self.getShortName(child_element))
                self.readFramePort(child_element, port)
            elif tag_name == "I-PDU-PORT":
                port = connector.createIPduPort(self.getShortName(child_element))
                self.readIPduPort(child_element, port)
            elif tag_name == "I-SIGNAL-PORT":
                port = connector.createISignalPort(self.getShortName(child_element))
                self.readISignalPort(child_element, port)
            else:
                self.raiseError("Unsupported EcuCommPortInstances <%s>" % tag_name)

    def readCommunicationConnector(self, element: ET.Element, connector: CommunicationConnector):
        self.readIdentifiable(element, connector)
        connector.setCommControllerRef(self.getChildElementOptionalRefType(element, "COMM-CONTROLLER-REF"))
        self.readCommunicationConnectorEcuCommPortInstances(element, connector)
        connector.setPncGatewayType(self.getChildElementOptionalLiteral(element, "PNC-GATEWAY-TYPE"))

    def readCanCommunicationConnector(self, element: ET.Element, connector: CanCommunicationConnector):
        self.readCommunicationConnector(element, connector)

    def readEthernetCommunicationConnectorNetworkEndpointRefs(self, element: ET.Element, connector: EthernetCommunicationConnector):
        for ref in self.getChildElementRefTypeList(element, "NETWORK-ENDPOINT-REFS/NETWORK-ENDPOINT-REF"):
            connector.addNetworkEndpointRef(ref)

    def readEthernetCommunicationConnector(self, element: ET.Element, connector: EthernetCommunicationConnector):
        self.readCommunicationConnector(element, connector)
        connector.setMaximumTransmissionUnit(self.getChildElementOptionalPositiveInteger(element, "MAXIMUM-TRANSMISSION-UNIT"))
        self.readEthernetCommunicationConnectorNetworkEndpointRefs(element, connector)

    def readLinCommunicationConnector(self, element: ET.Element, connector: LinCommunicationConnector):
        self.readCommunicationConnector(element, connector)

    def readFlexrayCommunicationConnector(self, element: ET.Element, connector: FlexrayCommunicationConnector):
        self.readCommunicationConnector(element, connector)

    def readEcuInstanceConnectors(self, element: ET.Element, instance: EcuInstance):
        self.logger.debug("readEcuInstanceCommControllers %s" % instance.getShortName())
        for child_element in self.findall(element, "CONNECTORS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "CAN-COMMUNICATION-CONNECTOR":
                connector = instance.createCanCommunicationConnector(self.getShortName(child_element))
                self.readCanCommunicationConnector(child_element, connector)
            elif tag_name == "ETHERNET-COMMUNICATION-CONNECTOR":
                connector = instance.createEthernetCommunicationConnector(self.getShortName(child_element))
                self.readEthernetCommunicationConnector(child_element, connector)
            elif tag_name == "LIN-COMMUNICATION-CONNECTOR":
                connector = instance.createLinCommunicationConnector(self.getShortName(child_element))
                self.readLinCommunicationConnector(child_element, connector)
            elif tag_name == "FLEXRAY-COMMUNICATION-CONNECTOR":
                connector = instance.createFlexrayCommunicationConnector(self.getShortName(child_element))
                self.readFlexrayCommunicationConnector(child_element, connector)
            else:
                self.notImplemented("Unsupported Communication Connector <%s>" % tag_name)

    def readEcuInstanceAssociatedComIPduGroupRefs(self, element: ET.Element, instance: EcuInstance):
        for ref in self.getChildElementRefTypeList(element, "ASSOCIATED-COM-I-PDU-GROUP-REFS/ASSOCIATED-COM-I-PDU-GROUP-REF"):
            instance.addAssociatedComIPduGroupRef(ref)

    def readEcuInstanceAssociatedConsumedProvidedServiceInstanceGroupRefs(self, element: ET.Element, instance: EcuInstance):
        for ref in self.getChildElementRefTypeList(element, "ASSOCIATED-CONSUMED-PROVIDED-SERVICE-INSTANCE-GROUP-REFS/ASSOCIATED-CONSUMED-PROVIDED-SERVICE-INSTANCE-GROUP-REF"):
            instance.addAssociatedConsumedProvidedServiceInstanceGroupRef(ref)

    def readEcuInstanceAssociatedPdurIPduGroupRefs(self, element: ET.Element, instance: EcuInstance):
        for ref in self.getChildElementRefTypeList(element, "ASSOCIATED-PDUR-I-PDU-GROUP-REFS/ASSOCIATED-PDUR-I-PDU-GROUP-REF"):
            instance.addAssociatedPdurIPduGroupRef(ref)

    def readEcuInstanceEcuTaskProxyRefs(self, element: ET.Element, instance: EcuInstance):
        for ref in self.getChildElementRefTypeList(element, "ECU-TASK-PROXY-REFS/ECU-TASK-PROXY-REF"):
            instance.addEcuTaskProxyRef(ref)

    def readEcuInstanceFirewallRuleRefs(self, element: ET.Element, instance: EcuInstance):
        for ref in self.getChildElementRefTypeList(element, "FIREWALL-RULE-REFS/FIREWALL-RULE-REF"):
            instance.addFirewallRuleRef(ref)

    def readEcuInstance(self, element: ET.Element, instance: EcuInstance):
        self.logger.debug("Read EcuInstance <%s>" % instance.getShortName())
        self.readIdentifiable(element, instance)
        self.readEcuInstanceAssociatedComIPduGroupRefs(element, instance)
        self.readEcuInstanceAssociatedConsumedProvidedServiceInstanceGroupRefs(element, instance)
        self.readEcuInstanceAssociatedPdurIPduGroupRefs(element, instance)
        instance.setChannelSynchronousWakeup(self.getChildElementOptionalBooleanValue(element, "CHANNEL-SYNCHRONOUS-WAKEUP"))
        instance.setComConfigurationGwTimeBase(self.getChildElementOptionalTimeValue(element, "COM-CONFIGURATION-GW-TIME-BASE"))
        instance.setComConfigurationRxTimeBase(self.getChildElementOptionalTimeValue(element, "COM-CONFIGURATION-RX-TIME-BASE"))
        instance.setComConfigurationTxTimeBase(self.getChildElementOptionalTimeValue(element, "COM-CONFIGURATION-TX-TIME-BASE"))
        instance.setComEnableMDTForCyclicTransmission(self.getChildElementOptionalBooleanValue(element, "COM-ENABLE-MDT-FOR-CYCLIC-TRANSMISSION"))
        self.readEcuInstanceCommControllers(element, instance)
        self.readEcuInstanceConnectors(element, instance)
        self.readEcuInstanceEcuTaskProxyRefs(element, instance)
        instance.setEthSwitchPortGroupDerivation(self.getChildElementOptionalBooleanValue(element, "ETH-SWITCH-PORT-GROUP-DERIVATION"))
        self.readEcuInstanceFirewallRuleRefs(element, instance)
        instance.setPncNmRequest(self.getChildElementOptionalBooleanValue(element, "PNC-NM-REQUEST"))
        instance.setPncPrepareSleepTimer(self.getChildElementOptionalTimeValue(element, "PNC-PREPARE-SLEEP-TIMER"))
        instance.setPncSynchronousWakeup(self.getChildElementOptionalBooleanValue(element, "PNC-SYNCHRONOUS-WAKEUP"))
        instance.setPnResetTime(self.getChildElementOptionalTimeValue(element, "PN-RESET-TIME"))
        instance.setSleepModeSupported(self.getChildElementOptionalBooleanValue(element, "SLEEP-MODE-SUPPORTED"))
        instance.setTcpIpIcmpPropsRef(self.getChildElementOptionalRefType(element, "TCP-IP-ICMP-PROPS"))
        instance.setTcpIpPropsRef(self.getChildElementOptionalRefType(element, "TCP-IP-PROPS"))
        instance.setV2xSupported(self.getChildElementOptionalLiteral(element, "V-2-X-SUPPORTED"))
        instance.setWakeUpOverBusSupported(self.getChildElementOptionalBooleanValue(element, "WAKE-UP-OVER-BUS-SUPPORTED"))

    """
    def getFrameMappings(self, element: ET.Element) -> List[FrameMapping]:
        mappings = []
        for child_element in self.findall(element, 'FRAME-MAPPINGS/'):
            mapping = FrameMapping()
            mapping.sourceFrameRef = self.getChildElementOptionalRefType(child_element, "SOURCE-FRAME-REF")
            mapping.targetFrameRef = self.getChildElementOptionalRefType(child_element, "TARGET-FRAME-REF")
            mappings.append(mapping)
        return mappings
    """

    def getISignalMappings(self, element: ET.Element) -> List[ISignalMapping]:
        mappings = []
        for child_element in self.findall(element, "SIGNAL-MAPPINGS/I-SIGNAL-MAPPING"):
            mapping = ISignalMapping()
            mapping.sourceSignalRef = self.getChildElementOptionalRefType(child_element, "SOURCE-SIGNAL-REF")
            mapping.targetSignalRef = self.getChildElementOptionalRefType(child_element, "TARGET-SIGNAL-REF")
            mappings.append(mapping)
        return mappings

    def getTargetIPduRef(self, element, key: str) -> TargetIPduRef:
        i_pdu_ref = None
        child_element = self.find(element, key)
        if child_element is not None:
            i_pdu_ref = TargetIPduRef()
            i_pdu_ref.setTargetIPdu(self.getChildElementOptionalRefType(child_element, "TARGET-I-PDU-REF"))
        return i_pdu_ref

    def getIPduMappings(self, element: ET.Element) -> List[IPduMapping]:
        mappings = []
        for child_element in self.findall(element, "I-PDU-MAPPINGS/I-PDU-MAPPING"):
            mapping = IPduMapping()
            mapping.setSourceIpduRef(self.getChildElementOptionalRefType(child_element, "SOURCE-I-PDU-REF"))
            mapping.setTargetIPdu(self.getTargetIPduRef(child_element, "TARGET-I-PDU"))
            mappings.append(mapping)
        return mappings

    def readGateway(self, element: ET.Element, gateway: Gateway):
        self.logger.debug("Read Gateway <%s>" % gateway.getShortName())
        self.readIdentifiable(element, gateway)
        gateway.setEcuRef(self.getChildElementOptionalRefType(element, "ECU-REF"))
        for mapping in self.getIPduMappings(element):
            gateway.addIPduMapping(mapping)
        for mapping in self.getISignalMappings(element):
            gateway.addSignalMapping(mapping)

    def readISignal(self, element: ET.Element, signal: ISignal):
        self.logger.debug("Read ISignal <%s>" % signal.getShortName())
        self.readIdentifiable(element, signal)
        signal.setDataTransformationRef(self.getChildElementOptionalRefType(element, "DATA-TRANSFORMATIONS/DATA-TRANSFORMATION-REF-CONDITIONAL/DATA-TRANSFORMATION-REF"))
        signal.setDataTypePolicy(self.getChildElementOptionalLiteral(element, "DATA-TYPE-POLICY"))
        signal.setISignalType(self.getChildElementOptionalLiteral(element, "I-SIGNAL-TYPE"))
        signal.setInitValue(self.getInitValue(element))
        signal.setLength(self.getChildElementOptionalNumericalValue(element, "LENGTH"))
        signal.setNetworkRepresentationProps(self.getSwDataDefProps(element, "NETWORK-REPRESENTATION-PROPS"))
        signal.setSystemSignalRef(self.getChildElementOptionalRefType(element, "SYSTEM-SIGNAL-REF"))
        signal.setTimeoutSubstitutionValue(self.getChildValueSpecification(element, "TIMEOUT-SUBSTITUTION-VALUE"))
        self.readISignalProps(element, signal)
        self.readISignalTransformationISignalProps(element, signal)

    def readISignalProps(self, element: ET.Element, signal: ISignal):
        props_element = self.find(element, "I-SIGNAL-PROPS")
        if props_element is not None:
            props = ISignalProps()
            props.setHandleOutOfRange(self.getChildElementOptionalLiteral(props_element, "HANDLE-OUT-OF-RANGE"))
            signal.setISignalProps(props)

    def readISignalTransformationISignalProps(self, element: ET.Element, signal: ISignal):
        for child_element in self.findall(element, "TRANSFORMATION-I-SIGNAL-PROPSS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS":
                props = EndToEndTransformationISignalProps()
                self.readEndToEndTransformationISignalProps(child_element, props)
                signal.addTransformationISignalProps(props)
            else:
                self.notImplemented("Unsupported TransformationISignalProps %s" % tag_name)

    def readEcucValueCollectionEcucValues(self, element: ET.Element, parent: EcucValueCollection):
        for child_element in self.findall(element, "ECUC-VALUES/ECUC-MODULE-CONFIGURATION-VALUES-REF-CONDITIONAL"):
            ref = self.getChildElementOptionalRefType(child_element, "ECUC-MODULE-CONFIGURATION-VALUES-REF")
            if ref is not None:
                parent.addEcucValueRef(ref)
            self.logger.debug("EcucValue <%s> of EcucValueCollection <%s> has been added", ref.value, parent.getShortName())

    def readEcucValueCollection(self, element: ET.Element, collection: EcucValueCollection):
        self.logger.debug("Read EcucValueCollection <%s>" % collection.getShortName())
        self.readIdentifiable(element, collection)
        collection.setEcuExtractRef(self.getChildElementOptionalRefType(element, "ECU-EXTRACT-REF"))
        self.readEcucValueCollectionEcucValues(element, collection)

    def readEcucParameterValue(self, element: ET.Element, param_value: EcucParameterValue):
        param_value.setDefinition(self.getChildElementOptionalRefType(element, "DEFINITION-REF"))
        param_value.setIndex(self.getChildElementOptionalPositiveInteger(element, "INDEX"))
        for annotation in self.getAnnotations(element):
            param_value.addAnnotation(annotation)
        param_value.setIsAutoValue(self.getChildElementOptionalBooleanValue(element, "IS-AUTO-VALUE"))

    def getEcucTextualParamValue(self, element: ET.Element) -> EcucTextualParamValue:
        param_value = EcucTextualParamValue()
        self.readEcucParameterValue(element, param_value)
        param_value.setValue(self.getChildElementOptionalVerbatimString(element, "VALUE"))
        return param_value

    def getEcucNumericalParamValue(self, element: ET.Element) -> EcucNumericalParamValue:
        param_value = EcucNumericalParamValue()
        self.readEcucParameterValue(element, param_value)
        param_value.setValue(self.getChildElementOptionalNumerical(element, "VALUE"))
        return param_value

    def getEcucAddInfoParamValue(self, element: ET.Element) -> EcucAddInfoParamValue:
        param_value = EcucAddInfoParamValue()
        self.readEcucParameterValue(element, param_value)
        param_value.setValue(self.getDocumentationBlock(element, "VALUE"))
        return param_value

    def readEcucContainerValueParameterValues(self, element: ET.Element, container_value: EcucContainerValue):
        for child_element in self.findall(element, "PARAMETER-VALUES/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "ECUC-TEXTUAL-PARAM-VALUE":
                container_value.addParameterValue(self.getEcucTextualParamValue(child_element))
            elif tag_name == "ECUC-NUMERICAL-PARAM-VALUE":
                container_value.addParameterValue(self.getEcucNumericalParamValue(child_element))
            elif tag_name == "ECUC-ADD-INFO-PARAM-VALUE":
                container_value.addParameterValue(self.getEcucAddInfoParamValue(child_element))
            else:
                self.notImplemented("Unsupported EcucParameterValue <%s>" % tag_name)

    def readEcucAbstractReferenceValue(self, element: ET.Element, value: EcucAbstractReferenceValue):
        value.setDefinitionRef(self.getChildElementOptionalRefType(element, "DEFINITION-REF"))
        value.setIndex(self.getChildElementOptionalPositiveInteger(element, "INDEX"))
        for annotation in self.getAnnotations(element):
            value.addAnnotation(annotation)
        value.setIsAutoValue(self.getChildElementOptionalBooleanValue(element, "IS-AUTO-VALUE"))

    def getEcucReferenceValue(self, element: ET.Element) -> EcucReferenceValue:
        value = EcucReferenceValue()
        self.readEcucAbstractReferenceValue(element, value)
        value.setValueRef(self.getChildElementOptionalRefType(element, "VALUE-REF"))
        return value

    def getAnyInstanceRef(self, element: ET.Element, key) -> AnyInstanceRef:
        instance_ref = None
        child_element = self.find(element, key)
        if child_element is not None:
            instance_ref = AnyInstanceRef()
            instance_ref.setBaseRef(self.getChildElementOptionalRefType(child_element, "BASE-REF"))
            for ref in self.getChildElementRefTypeList(child_element, "CONTEXT-ELEMENT-REF"):
                instance_ref.addContextElementRef(ref)
            instance_ref.setTargetRef(self.getChildElementOptionalRefType(child_element, "TARGET-REF"))
        return instance_ref

    def getEcucInstanceReferenceValue(self, element: ET.Element) -> EcucInstanceReferenceValue:
        value = EcucInstanceReferenceValue()
        self.readEcucAbstractReferenceValue(element, value)
        value.setValueIRef(self.getAnyInstanceRef(element, "VALUE-IREF"))
        return value

    def readEcucContainerValueReferenceValues(self, element: ET.Element, container_value: EcucContainerValue):
        for child_element in self.findall(element, "REFERENCE-VALUES/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "ECUC-REFERENCE-VALUE":
                container_value.addReferenceValue(self.getEcucReferenceValue(child_element))
            elif tag_name == "ECUC-INSTANCE-REFERENCE-VALUE":
                container_value.addReferenceValue(self.getEcucInstanceReferenceValue(child_element))
            else:
                self.notImplemented("Unsupported EcucParameterValue <%s>" % tag_name)

    def readEcucContainerValue(self, element: ET.Element, container_value: EcucContainerValue):
        self.readIdentifiable(element, container_value)
        container_value.setDefinitionRef(self.getChildElementOptionalRefType(element, "DEFINITION-REF"))
        container_value.setIndex(self.getChildElementOptionalPositiveInteger(element, "INDEX"))
        self.readEcucContainerValueParameterValues(element, container_value)
        self.readEcucContainerValueReferenceValues(element, container_value)
        self.readEcucContainerValueSubContainers(element, container_value)

    def readEcucContainerValueEcucContainerValue(self, element: ET.Element, parent: EcucContainerValue):
        short_name = self.getShortName(element)
        self.logger.debug("EcucContainerValue %s" % short_name)
        container_value = parent.createSubContainer(short_name)
        self.readEcucContainerValue(element, container_value)

    def readEcucContainerValueSubContainers(self, element: ET.Element, parent: EcucContainerValue):
        for child_element in self.findall(element, "SUB-CONTAINERS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "ECUC-CONTAINER-VALUE":
                self.readEcucContainerValueEcucContainerValue(child_element, parent)
            else:
                self.notImplemented("Unsupported Sub Container %s" % tag_name)

    def readEcucModuleConfigurationValuesEcucContainerValue(self, element: ET.Element, parent: EcucModuleConfigurationValues):
        short_name = self.getShortName(element)
        self.logger.debug("EcucContainerValue %s" % short_name)
        container_value = parent.createContainer(short_name)
        self.readEcucContainerValue(element, container_value)

    def readEcucModuleConfigurationValuesContainers(self, element: ET.Element, values: EcucModuleConfigurationValues):
        for child_element in self.findall(element, "CONTAINERS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "ECUC-CONTAINER-VALUE":
                self.readEcucModuleConfigurationValuesEcucContainerValue(child_element, values)
            else:
                self.notImplemented("Unsupported Container %s" % tag_name)

    def readEcucModuleConfigurationValues(self, element: ET.Element, values: EcucModuleConfigurationValues):
        self.logger.debug("Read EcucModuleConfigurationValues %s" % values.getShortName())
        self.readIdentifiable(element, values)
        values.setDefinition(self.getChildElementOptionalRefType(element, "DEFINITION-REF"))
        values.setEcucDefEdition(self.getChildElementOptionalRevisionLabelString(element, "ECUC-DEF-EDITION"))
        values.setImplementationConfigVariant(self.getChildElementOptionalLiteral(element, "IMPLEMENTATION-CONFIG-VARIANT"))
        values.setModuleDescription(self.getChildElementOptionalRefType(element, "MODULE-DESCRIPTION-REF"))
        values.setPostBuildVariantUsed(self.getChildElementOptionalBooleanValue(element, "POST-BUILD-VARIANT-USED"))
        self.readEcucModuleConfigurationValuesContainers(element, values)

    def readPhysicalDimension(self, element: ET.Element, dimension: PhysicalDimension):
        self.logger.debug("Read PhysicalDimension <%s>" % dimension.getShortName())
        self.readIdentifiable(element, dimension)
        dimension.setLengthExp(self.getChildElementOptionalNumericalValue(element, "LENGTH-EXP"))
        dimension.setLuminousIntensityExp(self.getChildElementOptionalNumericalValue(element, "LUMINOUS-INTENSITY-EXP"))
        dimension.setMassExp(self.getChildElementOptionalNumericalValue(element, "MASS-EXP"))
        dimension.setMolarAmountExp(self.getChildElementOptionalNumericalValue(element, "MOLAR-AMOUNT-EXP"))
        dimension.setTemperatureExp(self.getChildElementOptionalNumericalValue(element, "TEMPERATURE-EXP"))
        dimension.setTimeExp(self.getChildElementOptionalNumericalValue(element, "TIME-EXP"))
        dimension.setCurrentExp(self.getChildElementOptionalNumericalValue(element, "CURRENT-EXP"))

    def readISignalGroupISignalRef(self, element: ET.Element, group: ISignalGroup):
        for ref_type in self.getChildElementRefTypeList(element, "I-SIGNAL-REFS/I-SIGNAL-REF"):
            group.addISignalRef(ref_type)

    def readISignalGroupComBasedSignalGroupTransformation(self, element: ET.Element, group: ISignalGroup):
        ref = self.getChildElementOptionalRefType(element, "COM-BASED-SIGNAL-GROUP-TRANSFORMATIONS/DATA-TRANSFORMATION-REF-CONDITIONAL/DATA-TRANSFORMATION-REF")
        group.setComBasedSignalGroupTransformationRef(ref)

    def readTransformationISignalProps(self, element: ET.Element, props: TransformationISignalProps):
        self.readDescribable(element, props)
        props.setCsErrorReaction(self.getChildElementOptionalLiteral(element, "CS-ERROR-REACTION"))
        for child_element in self.findall(element, "DATA-PROTOTYPE-TRANSFORMATION-PROPSS/*"):
            if self.getTagName(child_element) == "DATA-PROTOTYPE-TRANSFORMATION-PROPS":
                dp_props = DataPrototypeTransformationProps()
                self.readDataPrototypeTransformationProps(child_element, dp_props)
                props.addDataPrototypeTransformationProps(dp_props)
            else:
                self.notImplemented("Unsupported DataPrototypeTransformationProps %s" % self.getTagName(child_element))

    def readDataPrototypeInPortInterfaceRef(self, element: ET.Element, ref: DataPrototypeInPortInterfaceRef):
        self.readARObjectAttributes(element, ref)
        ref.setTagId(self.getChildElementOptionalPositiveInteger(element, "TAG-ID"))
        child_element = self.find(element, "DATA-PROTOTYPE-IN-CLIENT-SERVER-INTERFACE-REF")
        if child_element is not None:
            cs_ref = DataPrototypeInClientServerInterfaceInstanceRef()
            self.readDataPrototypeInClientServerInterfaceInstanceRef(child_element, cs_ref)
            ref.setDataPrototypeInClientServerInterface(cs_ref)

    def readDataPrototypeInSenderReceiverInterfaceInstanceRef(self, element: ET.Element, iref: DataPrototypeInSenderReceiverInterfaceInstanceRef):
        self.readARObjectAttributes(element, iref)
        iref.setBaseRef(self.getChildElementOptionalRefType(element, "BASE"))
        for ctx in self.findall(element, "CONTEXT-DATA-PROTOTYPE-IN-SR"):
            iref.addContextDataPrototypeInSrRefs(self.getChildElementOptionalRefType(ctx, "CONTEXT-DATA-PROTOTYPE-IN-SR") or self.getChildElementOptionalRefType(ctx, "CONTEXT-DATA-PROTOTYPE"))
        iref.setRootDataPrototypeInSrRef(self.getChildElementOptionalRefType(element, "ROOT-DATA-PROTOTYPE-IN-SR"))
        iref.setTargetDataPrototypeInSrRef(self.getChildElementOptionalRefType(element, "TARGET-DATA-PROTOTYPE-IN-SR"))

    def readDataPrototypeInClientServerInterfaceInstanceRef(self, element: ET.Element, iref: DataPrototypeInClientServerInterfaceInstanceRef):
        self.readARObjectAttributes(element, iref)
        iref.setBaseRef(self.getChildElementOptionalRefType(element, "BASE"))
        for ctx in self.findall(element, "CONTEXT-DATA-PROTOTYPE-IN-CS"):
            iref.addContextDataPrototypeInCsRefs(self.getChildElementOptionalRefType(ctx, "CONTEXT-DATA-PROTOTYPE-IN-CS") or self.getChildElementOptionalRefType(ctx, "CONTEXT-DATA-PROTOTYPE"))
        iref.setRootDataPrototypeInCsRef(self.getChildElementOptionalRefType(element, "ROOT-DATA-PROTOTYPE-IN-CS"))
        iref.setTargetDataPrototypeInCsRef(self.getChildElementOptionalRefType(element, "TARGET-DATA-PROTOTYPE-IN-CS"))

    def readDataPrototypeTransformationProps(self, element: ET.Element, props: DataPrototypeTransformationProps):
        self.readARObjectAttributes(element, props)
        child_element = self.find(element, "DATA-PROTOTYPE-IN-PORT-INTERFACE-REF")
        if child_element is not None:
            ref = DataPrototypeInPortInterfaceRef()
            self.readDataPrototypeInPortInterfaceRef(child_element, ref)
            props.setDataPrototypeInPortInterfaceRef(ref)
        props.setNetworkRepresentationProps(self.getSwDataDefProps(element, "NETWORK-REPRESENTATION-PROPS"))
        props.setTransformationProps(self.getChildElementOptionalRefType(element, "TRANSFORMATION-PROPS"))

    def readEndToEndTransformationISignalPropsDataIds(self, element: ET.Element, props: EndToEndTransformationISignalProps):
        child_element = self.find(element, "DATA-IDS")
        if child_element is not None:
            props.addDataId(self.getChildElementOptionalPositiveInteger(child_element, "DATA-ID"))

    def readEndToEndTransformationISignalProps(self, element: ET.Element, props: EndToEndTransformationISignalProps):
        child_element = self.find(element, "END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS-VARIANTS/END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS-CONDITIONAL")
        if child_element is not None:
            self.readTransformationISignalProps(child_element, props)
            props.setTransformerRef(self.getChildElementOptionalRefType(child_element, "TRANSFORMER-REF"))
            self.readEndToEndTransformationISignalPropsDataIds(child_element, props)
            props.setDataLength(self.getChildElementOptionalPositiveInteger(child_element, "DATA-LENGTH"))

    def readISignalGroupTransformationISignalProps(self, element: ET.Element, group: ISignalGroup):
        for child_element in self.findall(element, "TRANSFORMATION-I-SIGNAL-PROPSS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS":
                props = EndToEndTransformationISignalProps()
                self.readEndToEndTransformationISignalProps(child_element, props)
                group.addTransformationISignalProps(props)
            else:
                self.notImplemented("Unsupported TransformationISignalProps %s" % tag_name)

    def readISignalGroup(self, element: ET.Element, group: ISignalGroup):
        self.logger.debug("Read ISignalGroup <%s>" % group.getShortName())
        self.readIdentifiable(element, group)
        self.readISignalGroupComBasedSignalGroupTransformation(element, group)
        self.readISignalGroupISignalRef(element, group)
        group.setSystemSignalGroupRef(self.getChildElementOptionalRefType(element, "SYSTEM-SIGNAL-GROUP-REF"))
        self.readISignalGroupTransformationISignalProps(element, group)

    def readSystemSignal(self, element: ET.Element, signal: SystemSignal):
        self.logger.debug("Read SystemSignal <%s>" % signal.getShortName())
        self.readIdentifiable(element, signal)
        signal.setDynamicLength(self.getChildElementOptionalBooleanValue(element, "DYNAMIC-LENGTH"))
        signal.setPhysicalProps(self.getSwDataDefProps(element, "PHYSICAL-PROPS"))

    def readSystemSignalGroup(self, element: ET.Element, group: SystemSignalGroup):
        self.logger.debug("Read SystemSignalGroup <%s>" % group.getShortName())
        self.readIdentifiable(element, group)
        for ref_type in self.getChildElementRefTypeList(element, "SYSTEM-SIGNAL-REFS/SYSTEM-SIGNAL-REF"):
            group.addSystemSignalRef(ref_type)
        group.setTransformingSystemSignalRef(self.getChildElementOptionalRefType(element, "TRANSFORMING-SYSTEM-SIGNAL-REF"))

    def readSignalServiceTranslationPropsSet(self, element: ET.Element, props_set: SignalServiceTranslationPropsSet):
        self.logger.debug("Read SignalServiceTranslationPropsSet <%s>" % props_set.getShortName())
        self.readIdentifiable(element, props_set)
        for child_element in self.findall(element, "SIGNAL-SERVICE-TRANSLATION-PROPS"):
            props = props_set.createSignalServiceTranslationProps(self.getShortName(child_element))
            self.readSignalServiceTranslationProps(child_element, props)

    def readSignalServiceTranslationProps(self, element: ET.Element, props: SignalServiceTranslationProps):
        self.logger.debug("Read SignalServiceTranslationProps <%s>" % props.getShortName())
        self.readIdentifiable(element, props)
        for ref_type in self.getChildElementRefTypeList(element, "CONTROL-CONSUMED-EVENT-GROUP-REFS/CONTROL-CONSUMED-EVENT-GROUP-REF"):
            props.addControlConsumedEventGroupRef(ref_type)
        for ref_type in self.getChildElementRefTypeList(element, "CONTROL-PNC-REFS/CONTROL-PNC-REF"):
            props.addControlPncRef(ref_type)
        for ref_type in self.getChildElementRefTypeList(element, "CONTROL-PROVIDED-EVENT-GROUP-REFS/CONTROL-PROVIDED-EVENT-GROUP-REF"):
            props.addControlProvidedEventGroupRef(ref_type)
        props.setServiceControl(self.getChildElementOptionalLiteral(element, "SERVICE-CONTROL"))
        for child_element in self.findall(element, "SIGNAL-SERVICE-TRANSLATION-EVENT-PROPS"):
            event_props = props.createSignalServiceTranslationEventProps(self.getShortName(child_element))
            self.readSignalServiceTranslationEventProps(child_element, event_props)

    def readSignalServiceTranslationEventProps(self, element: ET.Element, event_props: SignalServiceTranslationEventProps):
        self.logger.debug("Read SignalServiceTranslationEventProps <%s>" % event_props.getShortName())
        self.readIdentifiable(element, event_props)
        for child_element in self.findall(element, "SIGNAL-SERVICE-TRANSLATION-ELEMENT-PROPS"):
            element_props = event_props.createSignalServiceTranslationElementProps(self.getShortName(child_element))
            self.readSignalServiceTranslationElementProps(child_element, element_props)
        event_props.setSafeTranslation(self.getChildElementOptionalBooleanValue(element, "SAFE-TRANSLATION"))
        event_props.setSecureTranslation(self.getChildElementOptionalBooleanValue(element, "SECURE-TRANSLATION"))
        event_props.setTranslationTarget(self.getVariableDataPrototypeInSystemInstanceRef(self.find(element, "TRANSLATION-TARGET")))

    def readSignalServiceTranslationElementProps(self, element: ET.Element, element_props: SignalServiceTranslationElementProps):
        self.logger.debug("Read SignalServiceTranslationElementProps <%s>" % element_props.getShortName())
        self.readIdentifiable(element, element_props)
        element_props.setFilter(self.getDataFilter(element, "FILTER"))
        element_props.setTransmissionTrigger(self.getChildElementOptionalBooleanValue(element, "TRANSMISSION-TRIGGER"))

    def readISignalToPduMappings(self, element: ET.Element, parent: ISignalIPdu):
        for child_element in self.findall(element, "I-SIGNAL-TO-PDU-MAPPINGS/I-SIGNAL-TO-I-PDU-MAPPING"):
            short_name = self.getShortName(child_element)
            mapping = parent.createISignalToPduMappings(short_name)
            self.readIdentifiable(child_element, mapping)
            mapping.setISignalRef(self.getChildElementOptionalRefType(child_element, "I-SIGNAL-REF"))
            mapping.setISignalGroupRef(self.getChildElementOptionalRefType(child_element, "I-SIGNAL-GROUP-REF"))
            mapping.setPackingByteOrder(self.getChildElementOptionalLiteral(child_element, "PACKING-BYTE-ORDER"))
            mapping.setStartPosition(self.getChildElementOptionalNumericalValue(child_element, "START-POSITION"))
            mapping.setTransferProperty(self.getChildElementOptionalLiteral(child_element, "TRANSFER-PROPERTY"))
            mapping.setUpdateIndicationBitPosition(self.getChildElementOptionalNumericalValue(child_element, "UPDATE-INDICATION-BIT-POSITION"))

    def getDataFilter(self, element: ET.Element, key: str) -> DataFilter:
        filter = None
        child_element = self.find(element, key)
        if child_element is not None:
            filter = DataFilter()
            filter.setDataFilterType(self.getChildElementOptionalLiteral(child_element, "DATA-FILTER-TYPE"))
            filter.setMask(self.getChildElementOptionalIntegerValue(child_element, "MASK"))
            filter.setX(self.getChildElementOptionalIntegerValue(child_element, "X"))

        return filter

    def getTransmissionModeConditions(self, element: ET.Element, key: str) -> List[TransmissionModeCondition]:
        result = []
        child_elements = self.findall(element, key)
        for child_element in child_elements:
            condition = TransmissionModeCondition()
            condition.setDataFilter(self.getDataFilter(child_element, "DATA-FILTER"))
            condition.setISignalInIPduRef(self.getChildElementOptionalRefType(child_element, "I-SIGNAL-IN-I-PDU-REF"))
            result.append(condition)
        return result

    def getTimeRangeType(self, element: ET.Element, key: str) -> TimeRangeType:
        time_range = None
        child_element = self.find(element, key)
        if child_element is not None:
            time_range = TimeRangeType()
            time_range.setValue(self.getChildElementOptionalTimeValue(child_element, "VALUE"))
        return time_range

    def getCyclicTiming(self, element: ET.Element, key: str) -> CyclicTiming:
        timing = None
        child_element = self.find(element, key)
        if child_element is not None:
            timing = CyclicTiming()
            timing.setTimeOffset(self.getTimeRangeType(child_element, "TIME-OFFSET"))
            timing.setTimePeriod(self.getTimeRangeType(child_element, "TIME-PERIOD"))
        return timing

    def getEventControlledTiming(self, element: ET.Element, key: str) -> EventControlledTiming:
        timing = None
        child_element = self.find(element, key)
        if child_element is not None:
            timing = EventControlledTiming()
            timing.setNumberOfRepetitions(self.getChildElementOptionalIntegerValue(child_element, "NUMBER-OF-REPETITIONS"))
            timing.setRepetitionPeriod(self.getTimeRangeType(child_element, "REPETITION-PERIOD"))
        return timing

    def getTransmissionModeTiming(self, element: ET.Element, key: str) -> TransmissionModeTiming:
        timing = None
        child_element = self.find(element, key)
        if child_element is not None:
            # self.logger.debug("Get TransmissionModeTiming of <%s>" % key)
            timing = TransmissionModeTiming()
            timing.setCyclicTiming(self.getCyclicTiming(child_element, "CYCLIC-TIMING"))
            timing.setEventControlledTiming(self.getEventControlledTiming(child_element, "EVENT-CONTROLLED-TIMING"))
        return timing

    def getTransmissionModeDeclaration(self, element: ET.Element, key: str) -> TransmissionModeDeclaration:
        decl = None
        child_element = self.find(element, key)
        if child_element is not None:
            decl = TransmissionModeDeclaration()
            for condition in self.getTransmissionModeConditions(child_element, "TRANSMISSION-MODE-CONDITIONS/TRANSMISSION-MODE-CONDITION"):
                decl.addTransmissionModeCondition(condition)
            decl.setTransmissionModeFalseTiming(self.getTransmissionModeTiming(child_element, "TRANSMISSION-MODE-FALSE-TIMING"))
            decl.setTransmissionModeTrueTiming(self.getTransmissionModeTiming(child_element, "TRANSMISSION-MODE-TRUE-TIMING"))
        return decl

    def getISignalIPduIPduTimingSpecification(self, element: ET.Element) -> IPduTiming:
        timing = None
        child_element = self.find(element, "I-PDU-TIMING-SPECIFICATIONS/I-PDU-TIMING")
        if child_element is not None:
            timing = IPduTiming()
            timing.setMinimumDelay(self.getChildElementOptionalTimeValue(child_element, "MINIMUM-DELAY"))
            timing.setTransmissionModeDeclaration(self.getTransmissionModeDeclaration(child_element, "TRANSMISSION-MODE-DECLARATION"))
        return timing

    def readISignalIPdu(self, element: ET.Element, ipdu: ISignalIPdu):
        self.logger.debug("Read ISignalIPdu <%s>" % ipdu.getShortName())
        self.readIdentifiable(element, ipdu)
        ipdu.setLength(self.getChildElementOptionalNumericalValue(element, "LENGTH"))
        ipdu.setIPduTimingSpecification(self.getISignalIPduIPduTimingSpecification(element))
        self.readISignalToPduMappings(element, ipdu)
        ipdu.setUnusedBitPattern(self.getChildElementOptionalIntegerValue(element, "UNUSED-BIT-PATTERN"))

    def getISignalIPduRefs(self, element: ET.Element) -> List[RefType]:
        ref_types = []
        for child_element in self.findall(element, "I-SIGNAL-I-PDUS/I-SIGNAL-I-PDU-REF-CONDITIONAL"):
            ref_types.append(self.getChildElementOptionalRefType(child_element, "I-SIGNAL-I-PDU-REF"))
        return ref_types

    def readISignalIPduGroup(self, element: ET.Element, group: ISignalIPduGroup):
        self.logger.debug("Read ISignalIPduGroup <%s>" % group.getShortName())
        self.readIdentifiable(element, group)
        group.setCommunicationDirection(self.getChildElementOptionalLiteral(element, "COMMUNICATION-DIRECTION"))
        group.setCommunicationMode(self.getChildElementOptionalLiteral(element, "COMMUNICATION-MODE"))
        for ref_type in self.getChildElementRefTypeList(element, "CONTAINED-I-SIGNAL-I-PDU-GROUP-REFS/CONTAINED-I-SIGNAL-I-PDU-GROUP-REF"):
            group.addContainedISignalIPduGroupRef(ref_type)
        for ref_type in self.getISignalIPduRefs(element):
            group.addISignalIPduRef(ref_type)

    def readSenderReceiverToSignalMapping(self, element: ET.Element, mapping: SenderReceiverToSignalMapping):
        mapping.setCommunicationDirection(self.getChildElementOptionalLiteral(element, "COMMUNICATION-DIRECTION"))
        mapping.setDataElementIRef(self.getVariableDataPrototypeInSystemInstanceRef(self.find(element, "DATA-ELEMENT-IREF")))
        mapping.setSystemSignalRef(self.getChildElementOptionalRefType(element, "SYSTEM-SIGNAL-REF"))
        self.logger.debug("Read SenderReceiverToSignalMapping <%s>" % mapping.getSystemSignalRef().getValue())

    def readSenderRecCompositeTypeMapping(self, element: ET.Element, mapping: SenderRecCompositeTypeMapping):
        self.readARObjectAttributes(element, mapping)

    def readSenderRecRecordElementMapping(self, element: ET.Element, mapping: SenderRecRecordElementMapping):
        self.readARObjectAttributes(element, mapping)
        mapping.setApplicationRecordElementRef(self.getChildElementOptionalRefType(element, "APPLICATION-RECORD-ELEMENT-REF"))
        mapping.setImplementationRecordElementRef(self.getChildElementOptionalRefType(element, "IMPLEMENTATION-RECORD-ELEMENT-REF"))
        mapping.setSystemSignalRef(self.getChildElementOptionalRefType(element, "SYSTEM-SIGNAL-REF"))

    def readSenderRecArrayTypeMappingRecordElementMapping(self, element: ET.Element, mapping: SenderRecRecordTypeMapping):
        for child_element in self.findall(element, "RECORD-ELEMENT-MAPPINGS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "SENDER-REC-RECORD-ELEMENT-MAPPING":
                record_element_mapping = SenderRecRecordElementMapping()
                self.readSenderRecRecordElementMapping(child_element, record_element_mapping)
                mapping.addRecordElementMapping(record_element_mapping)
            else:
                self.notImplemented("Unsupported RecordElementMapping %s" % tag_name)

    def readSenderRecRecordTypeMapping(self, element: ET.Element, mapping: SenderRecRecordTypeMapping):
        self.readSenderRecCompositeTypeMapping(element, mapping)
        self.readSenderRecArrayTypeMappingRecordElementMapping(element, mapping)

    def readSenderReceiverToSignalGroupMappingTypeMapping(self, element: ET.Element, mapping: SenderReceiverToSignalGroupMapping):
        child_element = self.find(element, "TYPE-MAPPING/*")
        if child_element is not None:
            tag_name = self.getTagName(child_element)
            if tag_name == "SENDER-REC-RECORD-TYPE-MAPPING":
                type_mapping = SenderRecRecordTypeMapping()
                self.readSenderRecRecordTypeMapping(child_element, type_mapping)
                mapping.setTypeMapping(type_mapping)
            else:
                self.notImplemented("Unsupported Type Mapping %s" % tag_name)

    def readSenderReceiverToSignalGroupMapping(self, element: ET.Element, mapping: SenderReceiverToSignalGroupMapping):
        mapping.setDataElementIRef(self.getVariableDataPrototypeInSystemInstanceRef(self.find(element, "DATA-ELEMENT-IREF")))
        mapping.setSignalGroupRef(self.getChildElementOptionalRefType(element, "SIGNAL-GROUP-REF"))
        self.readSenderReceiverToSignalGroupMappingTypeMapping(element, mapping)

    def readSystemMappingDataMappings(self, element: ET.Element, mapping: SystemMapping):
        for child_element in self.findall(element, "DATA-MAPPINGS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "SENDER-RECEIVER-TO-SIGNAL-MAPPING":
                signal_mapping = SenderReceiverToSignalMapping()
                self.readSenderReceiverToSignalMapping(child_element, signal_mapping)
                mapping.addDataMapping(signal_mapping)
            elif tag_name == "SENDER-RECEIVER-TO-SIGNAL-GROUP-MAPPING":
                signal_group_mapping = SenderReceiverToSignalGroupMapping()
                self.readSenderReceiverToSignalGroupMapping(child_element, signal_group_mapping)
                mapping.addDataMapping(signal_group_mapping)
            else:
                self.notImplemented("Unsupported Data Mapping %s" % tag_name)

    def readSwcToEcuMapping(self, element: ET.Element, mapping: SwcToEcuMapping):
        # self.logger.debug("SwcToEcuMapping %s" % mapping.getShortName())
        self.readIdentifiable(element, mapping)
        for child_element in self.findall(element, "COMPONENT-IREFS/COMPONENT-IREF"):
            mapping.addComponentIRef(self.getComponentInSystemInstanceRef(child_element))
        mapping.setEcuInstanceRef(self.getChildElementOptionalRefType(element, "ECU-INSTANCE-REF"))

    def readSystemMappingSwMappings(self, element: ET.Element, mapping: SystemMapping):
        for child_element in self.findall(element, "SW-MAPPINGS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "SWC-TO-ECU-MAPPING":
                swc_to_ecu_mapping = mapping.createSwcToEcuMapping(self.getShortName(child_element))
                self.readSwcToEcuMapping(child_element, swc_to_ecu_mapping)
            else:
                self.notImplemented("Unsupported Sw Mapping %s" % tag_name)

    def readEcuMapping(self, element: ET.Element, mapping: ECUMapping):
        self.readIdentifiable(element, mapping)
        mapping.setEcuInstanceRef(self.getChildElementOptionalRefType(element, "ECU-INSTANCE-REF"))
        mapping.setEcuRef(self.getChildElementOptionalRefType(element, "ECU-REF"))

    def readSystemMappingEcuResourceMappings(self, element: ET.Element, mapping: SystemMapping):
        for child_element in self.findall(element, "ECU-RESOURCE-MAPPINGS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "ECU-MAPPING":
                ecu_mapping = mapping.createECUMapping(self.getShortName(child_element))
                self.readEcuMapping(child_element, ecu_mapping)
            else:
                self.notImplemented("Unsupported EcuResourceMapping <%s>" % tag_name)

    def readSwcToImplMapping(self, element: ET.Element, mapping: SwcToImplMapping):
        self.readIdentifiable(element, mapping)
        mapping.setComponentImplementationRef(self.getChildElementOptionalRefType(element, "COMPONENT-IMPLEMENTATION-REF"))
        for child_element in self.findall(element, "COMPONENT-IREFS/COMPONENT-IREF"):
            mapping.addComponentIRef(self.getComponentInSystemInstanceRef(child_element))

    def readSystemMappingSwImplMappings(self, element: ET.Element, mapping: SystemMapping):
        for child_element in self.findall(element, "SW-IMPL-MAPPINGS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "SWC-TO-IMPL-MAPPING":
                sw_impl_mapping = mapping.createSwcToImplMapping(self.getShortName(child_element))
                self.readSwcToImplMapping(child_element, sw_impl_mapping)
            else:
                self.notImplemented("Unsupported SwImplMapping <%s>" % tag_name)

    def readSystemMapping(self, element: ET.Element, mapping: SystemMapping):
        # self.logger.debug("Read SystemMapping <%s>" % mapping.getShortName())
        self.readIdentifiable(element, mapping)
        self.readSystemMappingDataMappings(element, mapping)
        self.readSystemMappingEcuResourceMappings(element, mapping)
        self.readSystemMappingSwImplMappings(element, mapping)
        self.readSystemMappingSwMappings(element, mapping)

    def readSystemMappings(self, element: ET.Element, system: System):
        for child_element in self.findall(element, "MAPPINGS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "SYSTEM-MAPPING":
                mapping = system.createSystemMapping(self.getShortName(child_element))
                self.readSystemMapping(child_element, mapping)
            else:
                self.notImplemented("Unsupported Mapping %s" % tag_name)

    def readRootSwCompositionPrototype(self, element: ET.Element, system: System):
        child_element = self.find(element, "ROOT-SOFTWARE-COMPOSITIONS/ROOT-SW-COMPOSITION-PROTOTYPE")
        if child_element is not None:
            short_name = self.getShortName(child_element)
            self.logger.debug("Read RootSwCompositionPrototype %s" % short_name)
            prototype = system.createRootSoftwareComposition(short_name)
            self.readIdentifiable(child_element, prototype)
            for ref in self.getChildElementRefTypeList(child_element, "CALIBRATION-PARAMETER-VALUE-SET-REFS/CALIBRATION-PARAMETER-VALUE-SET-REF"):
                prototype.addCalibrationParameterValueSetRef(ref)
            prototype.setFlatMapRef(self.getChildElementOptionalRefType(child_element, "FLAT-MAP-REF"))
            prototype.setSoftwareCompositionTRef(self.getChildElementOptionalRefType(child_element, "SOFTWARE-COMPOSITION-TREF"))
            try:
                document = AUTOSAR.getInstance()
                document.setRootSwCompositionPrototype(prototype)
            except ValueError as e:
                self.raiseWarning("%s" % e)

    def readSystemFibexElementRefs(self, element: ET.Element, system: System):
        for ref in self.getChildElementRefTypeList(element, "FIBEX-ELEMENTS/FIBEX-ELEMENT-REF-CONDITIONAL/FIBEX-ELEMENT-REF"):
            system.addFibexElementRef(ref)

    def readSystem(self, element: ET.Element, system: System):
        self.logger.debug("Read System <%s>" % system.getShortName())
        self.readIdentifiable(element, system)
        system.setEcuExtractVersion(self.getChildElementOptionalLiteral(element, "ECU-EXTRACT-VERSION"))
        self.readSystemFibexElementRefs(element, system)
        self.readSystemMappings(element, system)
        self.readRootSwCompositionPrototype(element, system)
        system.setSystemVersion(self.getChildElementOptionalRevisionLabelString(element, "SYSTEM-VERSION"))
        document = AUTOSAR.getInstance()
        document.addSystem(system)

    def readGenericEthernetFrame(self, element: ET.Element, frame: GenericEthernetFrame):
        self.logger.debug("Read GenericEthernetFrame <%s>" % frame.getShortName())
        self.readFrame(element, frame)

    def getLifeCyclePeriod(self, element: ET.Element, key: str) -> LifeCyclePeriod:
        child_element = self.find(element, key)
        period = None
        if child_element is not None:
            period = LifeCyclePeriod()
            period.setArReleaseVersion(self.getChildElementOptionalRevisionLabelString(child_element, "AR-RELEASE-VERSION"))
        return period

    def readLifeCycleInfoUseInsteadRefs(self, element: ET.Element, info: LifeCycleInfo):
        for ref in self.getChildElementRefTypeList(element, "USE-INSTEAD-REFS/USE-INSTEAD-REF"):
            info.addUseInsteadRef(ref)

    def readLifeCycleInfo(self, element: ET.Element, info: LifeCycleInfo):
        self.readARObjectAttributes(element, info)
        info.setLcObjectRef(self.getChildElementOptionalRefType(element, "LC-OBJECT-REF"))
        info.setLcStateRef(self.getChildElementOptionalRefType(element, "LC-STATE-REF"))
        info.setPeriodBegin(self.getLifeCyclePeriod(element, "PERIOD-BEGIN"))
        info.setRemark(self.getDocumentationBlock(element, "REMARK"))
        self.readLifeCycleInfoUseInsteadRefs(element, info)

    def readLifeCycleInfoSetLifeCycleInfos(self, element: ET.Element, info_set: LifeCycleInfoSet):
        for child_element in self.findall(element, "LIFE-CYCLE-INFOS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "LIFE-CYCLE-INFO":
                info = LifeCycleInfo()
                self.readLifeCycleInfo(child_element, info)
                info_set.addLifeCycleInfo(info)
            else:
                self.notImplemented("Unsupported Life Cycle Info <%s>" % tag_name)

    def readLifeCycleInfoSet(self, element: ET.Element, info_set: LifeCycleInfoSet):
        self.logger.debug("Read LifeCycleInfoSet <%s>" % info_set.getShortName())
        self.readIdentifiable(element, info_set)
        info_set.setDefaultLcStateRef(self.getChildElementOptionalRefType(element, "DEFAULT-LC-STATE-REF"))
        self.readLifeCycleInfoSetLifeCycleInfos(element, info_set)
        info_set.setUsedLifeCycleStateDefinitionGroupRef(self.getChildElementOptionalRefType(element, "USED-LIFE-CYCLE-STATE-DEFINITION-GROUP-REF"))

    def readFlatInstanceDescriptor(self, element: ET.Element, desc: FlatInstanceDescriptor):
        self.logger.debug("Read LifeCycleInfoSet %s" % desc.getShortName())
        self.readIdentifiable(element, desc)
        desc.setUpstreamReferenceIRef(self.getAnyInstanceRef(element, "UPSTREAM-REFERENCE-IREF"))
        desc.setEcuExtractReferenceIRef(self.getAnyInstanceRef(element, "ECU-EXTRACT-REFERENCE-IREF"))

    def readFlatMapInstances(self, element: ET.Element, map: FlatMap):
        for child_element in self.findall(element, "INSTANCES/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "FLAT-INSTANCE-DESCRIPTOR":
                desc = map.createFlatInstanceDescriptor(self.getShortName(child_element))
                self.readFlatInstanceDescriptor(child_element, desc)
            else:
                self.notImplemented("Unsupported Flat Map Instances <%s>" % tag_name)

    def readFlatMap(self, element: ET.Element, map: FlatMap):
        self.logger.debug("Read FlatMap <%s>" % map.getShortName())
        self.readIdentifiable(element, map)
        self.readFlatMapInstances(element, map)

    def getDataPrototypeMappings(self, element: ET.Element, key: str) -> List[DataPrototypeMapping]:
        mappings = []
        for child_element in self.findall(element, "%s/DATA-PROTOTYPE-MAPPING" % key):
            mapping = DataPrototypeMapping()
            mapping.setFirstDataPrototypeRef(self.getChildElementOptionalRefType(child_element, "FIRST-DATA-PROTOTYPE-REF"))
            mapping.setFirstToSecondDataTransformationRef(self.getChildElementOptionalRefType(child_element, "FIRST-TO-SECOND-DATA-TRANSFORMATION-REF"))
            mapping.setSecondDataPrototypeRef(self.getChildElementOptionalRefType(child_element, "SECOND-DATA-PROTOTYPE-REF"))
            mapping.setSecondToFirstDataTransformationRef(self.getChildElementOptionalRefType(child_element, "SECOND-TO-FIRST-DATA-TRANSFORMATION-REF"))
            for sub_element in self.findall(child_element, "SUB-ELEMENT-MAPPINGS/SUB-ELEMENT-MAPPING"):
                mapping.addSubElementMapping(self.getSubElementMapping(sub_element))
            for text_table in self.findall(child_element, "TEXT-TABLE-MAPPINGS/TEXT-TABLE-MAPPING"):
                mapping.addTextTableMapping(self.getTextTableMapping(text_table))
            mappings.append(mapping)
        return mappings

    def getSubElementMapping(self, element: ET.Element) -> SubElementMapping:
        mapping = SubElementMapping()
        for ref_element in self.findall(element, "FIRST-ELEMENTS/*"):
            if self.getTagName(ref_element) == "APPLICATION-COMPOSITE-DATA-TYPE-SUB-ELEMENT-REF":
                mapping.setFirstElement(self.getApplicationCompositeElementInPortInterfaceInstanceRef(ref_element, "APPLICATION-COMPOSITE-ELEMENT-IREF"))
            else:
                self.notImplemented("Unsupported firstElement SubElementRef <%s>" % self.getTagName(ref_element))
        for ref_element in self.findall(element, "SECOND-ELEMENTS/*"):
            if self.getTagName(ref_element) == "APPLICATION-COMPOSITE-DATA-TYPE-SUB-ELEMENT-REF":
                mapping.setSecondElement(self.getApplicationCompositeElementInPortInterfaceInstanceRef(ref_element, "APPLICATION-COMPOSITE-ELEMENT-IREF"))
            else:
                self.notImplemented("Unsupported secondElement SubElementRef <%s>" % self.getTagName(ref_element))
        for text_table in self.findall(element, "TEXT-TABLE-MAPPINGS/TEXT-TABLE-MAPPING"):
            mapping.addTextTableMapping(self.getTextTableMapping(text_table))
        return mapping

    def getTextTableMapping(self, element: ET.Element) -> TextTableMapping:
        mapping = TextTableMapping()
        mapping.setBitfieldTextTableMaskFirst(self.getChildElementOptionalPositiveInteger(element, "BITFIELD-TEXT-TABLE-MASK-FIRST"))
        mapping.setBitfieldTextTableMaskSecond(self.getChildElementOptionalPositiveInteger(element, "BITFIELD-TEXT-TABLE-MASK-SECOND"))
        mapping.setIdenticalMapping(self.getChildElementOptionalBooleanValue(element, "IDENTICAL-MAPPING"))
        mapping.setMappingDirection(self.getChildElementOptionalLiteral(element, "MAPPING-DIRECTION"))
        return mapping

    def readVariableAndParameterInterfaceMapping(self, element: ET.Element, mapping: VariableAndParameterInterfaceMapping):
        # self.logger.debug("Read VariableAndParameterInterfaceMapping %s" % mapping.getShortName())
        self.readIdentifiable(element, mapping)
        for item in self.getDataPrototypeMappings(element, "DATA-MAPPINGS"):
            mapping.addDataMapping(item)

    def readClientServerOperationMapping(self, element: ET.Element, mapping: ClientServerOperationMapping):
        mapping.setFirstOperationRef(self.getChildElementOptionalRefType(element, "FIRST-OPERATION-REF"))
        mapping.setSecondOperationRef(self.getChildElementOptionalRefType(element, "SECOND-OPERATION-REF"))

    def readClientServerInterfaceMappingOperationMappings(self, element: ET.Element, mapping: ClientServerInterfaceMapping):
        for child_element in self.findall(element, "OPERATION-MAPPINGS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "CLIENT-SERVER-OPERATION-MAPPING":
                operation_mapping = ClientServerOperationMapping()
                self.readClientServerOperationMapping(child_element, operation_mapping)
                mapping.addOperationMapping(operation_mapping)
            else:
                self.notImplemented("Unsupported Operation Mapping <%s>" % tag_name)

    def readClientServerInterfaceMapping(self, element: ET.Element, mapping: ClientServerInterfaceMapping):
        # self.logger.debug("Read ClientServerInterfaceMapping %s" % mapping.getShortName())
        self.readIdentifiable(element, mapping)
        self.readClientServerInterfaceMappingOperationMappings(element, mapping)

    def readModeInterfaceMappingModeMapping(self, element: ET.Element, mapping: ModeInterfaceMapping):
        child_element = self.find(element, "MODE-MAPPING")
        if child_element is not None:
            mode_mapping = ModeDeclarationGroupPrototypeMapping()
            mode_mapping.setFirstModeGroupRef(self.getChildElementOptionalRefType(child_element, "FIRST-MODE-GROUP-REF"))
            mode_mapping.setModeDeclarationMappingSetRef(self.getChildElementOptionalRefType(child_element, "MODE-DECLARATION-MAPPING-SET-REF"))
            mode_mapping.setSecondModeGroupRef(self.getChildElementOptionalRefType(child_element, "SECOND-MODE-GROUP-REF"))
            mapping.setModeMapping(mode_mapping)

    def readModeInterfaceMapping(self, element: ET.Element, mapping: ModeInterfaceMapping):
        # self.logger.debug("Read ModeInterfaceMapping %s" % mapping.getShortName())
        self.readIdentifiable(element, mapping)
        self.readModeInterfaceMappingModeMapping(element, mapping)

    def readPortInterfaceMappings(self, element: ET.Element, mapping_set: PortInterfaceMappingSet):
        for child_element in self.findall(element, "PORT-INTERFACE-MAPPINGS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "VARIABLE-AND-PARAMETER-INTERFACE-MAPPING":
                mapping = mapping_set.createVariableAndParameterInterfaceMapping(self.getShortName(child_element))
                self.readVariableAndParameterInterfaceMapping(child_element, mapping)
            elif tag_name == "CLIENT-SERVER-INTERFACE-MAPPING":
                mapping = mapping_set.createClientServerInterfaceMapping(self.getShortName(child_element))
                self.readClientServerInterfaceMapping(child_element, mapping)
            elif tag_name == "MODE-INTERFACE-MAPPING":
                mapping = mapping_set.createModeInterfaceMapping(self.getShortName(child_element))
                self.readModeInterfaceMapping(child_element, mapping)
            else:
                self.notImplemented("Unsupported PortInterfaceMapping <%s>" % tag_name)

    def readPortInterfaceMappingSet(self, element: ET.Element, mapping_set: PortInterfaceMappingSet):
        self.logger.debug("Read PortInterfaceMappingSet %s" % mapping_set.getShortName())
        self.readIdentifiable(element, mapping_set)
        self.readPortInterfaceMappings(element, mapping_set)

    def readARPackageElements(self, element: ET.Element, parent: ARPackage):
        for child_element in self.findall(element, "ELEMENTS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "COMPOSITION-SW-COMPONENT-TYPE":
                type = parent.createCompositionSwComponentType(self.getShortName(child_element))
                self.readCompositionSwComponentType(child_element, type)
            elif tag_name == "DATA-PROTOTYPE-GROUP":
                data_group = parent.createDataPrototypeGroup(self.getShortName(child_element))
                self.readDataPrototypeGroup(child_element, data_group)
            elif tag_name == "RUNNABLE-ENTITY-GROUP":
                runnable_group = parent.createRunnableEntityGroup(self.getShortName(child_element))
                self.readRunnableEntityGroup(child_element, runnable_group)
            elif tag_name == "CONSISTENCY-NEEDS":
                consistency_needs = parent.createConsistencyNeeds(self.getShortName(child_element))
                self.readConsistencyNeeds(child_element, consistency_needs)
            elif tag_name == "COMPLEX-DEVICE-DRIVER-SW-COMPONENT-TYPE":
                type = parent.createComplexDeviceDriverSwComponentType(self.getShortName(child_element))
                self.readComplexDeviceDriverSwComponentType(child_element, type)
            elif tag_name == "SWC-IMPLEMENTATION":
                impl = parent.createSwcImplementation(self.getShortName(child_element))
                self.readSwcImplementation(child_element, impl)
            elif tag_name == "APPLICATION-PRIMITIVE-DATA-TYPE":
                data_type = parent.createApplicationPrimitiveDataType(self.getShortName(child_element))
                self.readApplicationPrimitiveDataType(child_element, data_type)
            elif tag_name == "APPLICATION-RECORD-DATA-TYPE":
                data_type = parent.createApplicationRecordDataType(self.getShortName(child_element))
                self.readApplicationRecordDataType(child_element, data_type)
            elif tag_name == "SW-BASE-TYPE":
                data_type = parent.createSwBaseType(self.getShortName(child_element))
                self.readSwBaseType(child_element, data_type)
            elif tag_name == "COMPU-METHOD":
                compu_method = parent.createCompuMethod(self.getShortName(child_element))
                self.readCompuMethod(child_element, compu_method)
            elif tag_name == "CONSTANT-SPECIFICATION":
                spec = parent.createConstantSpecification(self.getShortName(child_element))
                self.readConstantSpecification(child_element, spec)
            elif tag_name == "DATA-CONSTR":
                constr = parent.createDataConstr(self.getShortName(child_element))
                self.readDataConstr(child_element, constr)
            elif tag_name == "END-TO-END-PROTECTION-SET":
                protection_set = parent.createEndToEndProtectionSet(self.getShortName(child_element))
                self.readEndToEndProtectionSet(child_element, protection_set)
            elif tag_name == "SENDER-RECEIVER-INTERFACE":
                sr_interface = parent.createSenderReceiverInterface(self.getShortName(child_element))
                self.readSenderReceiverInterface(child_element, sr_interface)
            elif tag_name == "UNIT":
                unit = parent.createUnit(self.getShortName(child_element))
                self.readUnit(child_element, unit)
            elif tag_name == "BSW-MODULE-DESCRIPTION":
                desc = parent.createBswModuleDescription(self.getShortName(child_element))
                self.readBswModuleDescription(child_element, desc)
            elif tag_name == "BSW-MODULE-ENTRY":
                entry = parent.createBswModuleEntry(self.getShortName(child_element))
                self.readBswModuleEntry(child_element, entry)
            elif tag_name == "SWC-BSW-MAPPING":
                mapping = parent.createSwcBswMapping(self.getShortName(child_element))
                self.readSwcBswMapping(child_element, mapping)
            elif tag_name == "BSW-IMPLEMENTATION":
                impl = parent.createBswImplementation(self.getShortName(child_element))
                self.readBswImplementation(child_element, impl)
            elif tag_name == "IMPLEMENTATION-DATA-TYPE":
                data_type = parent.createImplementationDataType(self.getShortName(child_element))
                self.readImplementationDataType(child_element, data_type)
            elif tag_name == "CLIENT-SERVER-INTERFACE":
                cs_interface = parent.createClientServerInterface(self.getShortName(child_element))
                self.readClientServerInterface(child_element, cs_interface)
            elif tag_name == "APPLICATION-SW-COMPONENT-TYPE":
                sw_component = parent.createApplicationSwComponentType(self.getShortName(child_element))
                self.readApplicationSwComponentType(child_element, sw_component)
            elif tag_name == "ECU-ABSTRACTION-SW-COMPONENT-TYPE":
                sw_component = parent.createEcuAbstractionSwComponentType(self.getShortName(child_element))
                self.readEcuAbstractionSwComponentType(child_element, sw_component)
            elif tag_name == "APPLICATION-ARRAY-DATA-TYPE":
                data_type = parent.createApplicationArrayDataType(self.getShortName(child_element))
                self.readApplicationArrayDataType(child_element, data_type)
            elif tag_name == "SW-RECORD-LAYOUT":
                layout = parent.createSwRecordLayout(self.getShortName(child_element))
                self.readSwRecordLayout(child_element, layout)
            elif tag_name == "SW-ADDR-METHOD":
                method = parent.createSwAddrMethod(self.getShortName(child_element))
                self.readSwAddrMethod(child_element, method)
            elif tag_name == "TRIGGER-INTERFACE":
                trigger_if = parent.createTriggerInterface(self.getShortName(child_element))
                self.readTriggerInterface(child_element, trigger_if)
            elif tag_name == "SERVICE-SW-COMPONENT-TYPE":
                sw_component = parent.createServiceSwComponentType(self.getShortName(child_element))
                self.readServiceSwComponentType(child_element, sw_component)
            elif tag_name == "SENSOR-ACTUATOR-SW-COMPONENT-TYPE":
                sw_component = parent.createSensorActuatorSwComponentType(self.getShortName(child_element))
                self.readSensorActuatorSwComponentType(child_element, sw_component)
            elif tag_name == "NV-BLOCK-SW-COMPONENT-TYPE":
                sw_component = parent.createNvBlockSwComponentType(self.getShortName(child_element))
                self.readNvBlockSwComponentType(child_element, sw_component)
            elif tag_name == "SERVICE-PROXY-SW-COMPONENT-TYPE":
                sw_component = parent.createServiceProxySwComponentType(self.getShortName(child_element))
                self.readServiceProxySwComponentType(child_element, sw_component)
            elif tag_name == "DATA-TYPE-MAPPING-SET":
                mapping_set = parent.createDataTypeMappingSet(self.getShortName(child_element))
                self.readDataTypeMappingSet(child_element, mapping_set)
            elif tag_name == "MODE-DECLARATION-GROUP":
                group = parent.createModeDeclarationGroup(self.getShortName(child_element))
                self.readModeDeclarationGroup(child_element, group)
            elif tag_name == "MODE-SWITCH-INTERFACE":
                mode_interface = parent.createModeSwitchInterface(self.getShortName(child_element))
                self.readModeSwitchInterface(child_element, mode_interface)
            elif tag_name == "SWC-TIMING":
                timing = parent.createSwcTiming(self.getShortName(child_element))
                self.readSwcTiming(child_element, timing)
            elif tag_name == "LIN-CLUSTER":
                cluster = parent.createLinCluster(self.getShortName(child_element))
                self.readLinCluster(child_element, cluster)
            elif tag_name == "LIN-UNCONDITIONAL-FRAME":
                frame = parent.createLinUnconditionalFrame(self.getShortName(child_element))
                self.readLinUnconditionalFrame(child_element, frame)
            elif tag_name == "NM-PDU":
                pdu = parent.createNmPdu(self.getShortName(child_element))
                self.readNmPdu(child_element, pdu)
            elif tag_name == "N-PDU":
                pdu = parent.createNPdu(self.getShortName(child_element))
                self.readNPdu(child_element, pdu)
            elif tag_name == "DCM-I-PDU":
                i_pdu = parent.createDcmIPdu(self.getShortName(child_element))
                self.readDcmIPdu(child_element, i_pdu)
            elif tag_name == "SECURED-I-PDU":
                i_pdu = parent.createSecuredIPdu(self.getShortName(child_element))
                self.readSecuredIPdu(child_element, i_pdu)
            elif tag_name == "NM-CONFIG":
                config = parent.createNmConfig(self.getShortName(child_element))
                self.readNmConfig(child_element, config)
            elif tag_name == "CAN-TP-CONFIG":
                config = parent.createCanTpConfig(self.getShortName(child_element))
                self.readCanTpConfig(child_element, config)
            elif tag_name == "LIN-TP-CONFIG":
                config = parent.createLinTpConfig(self.getShortName(child_element))
                self.readLinTpConfig(child_element, config)
            elif tag_name == "SYSTEM":
                system = parent.createSystem(self.getShortName(child_element))
                self.readSystem(child_element, system)
            elif tag_name == "ECU-INSTANCE":
                instance = parent.createEcuInstance(self.getShortName(child_element))
                self.readEcuInstance(child_element, instance)
            elif tag_name == "GATEWAY":
                gateway = parent.createGateway(self.getShortName(child_element))
                self.readGateway(child_element, gateway)
            elif tag_name == "I-SIGNAL-I-PDU-GROUP":
                group = parent.createISignalIPduGroup(self.getShortName(child_element))
                self.readISignalIPduGroup(child_element, group)
            elif tag_name == "CAN-CLUSTER":
                cluster = parent.createCanCluster(self.getShortName(child_element))
                self.readCanCluster(child_element, cluster)
            elif tag_name == "CAN-FRAME":
                frame = parent.createCanFrame(self.getShortName(child_element))
                self.readCanFrame(child_element, frame)
            elif tag_name == "I-SIGNAL":
                signal = parent.createISignal(self.getShortName(child_element))
                self.readISignal(child_element, signal)
            elif tag_name == "I-SIGNAL-GROUP":
                group = parent.createISignalGroup(self.getShortName(child_element))
                self.readISignalGroup(child_element, group)
            elif tag_name == "I-SIGNAL-I-PDU":
                i_pdu = parent.createISignalIPdu(self.getShortName(child_element))
                self.readISignalIPdu(child_element, i_pdu)
            elif tag_name == "SYSTEM-SIGNAL":
                signal = parent.createSystemSignal(self.getShortName(child_element))
                self.readSystemSignal(child_element, signal)
            elif tag_name == "SYSTEM-SIGNAL-GROUP":
                group = parent.createSystemSignalGroup(self.getShortName(child_element))
                self.readSystemSignalGroup(child_element, group)
            elif tag_name == "SIGNAL-SERVICE-TRANSLATION-PROPS-SET":
                props_set = parent.createSignalServiceTranslationPropsSet(self.getShortName(child_element))
                self.readSignalServiceTranslationPropsSet(child_element, props_set)
            elif tag_name == "ECUC-VALUE-COLLECTION":
                collection = parent.createEcucValueCollection(self.getShortName(child_element))
                self.readEcucValueCollection(child_element, collection)
            elif tag_name == "ECUC-MODULE-CONFIGURATION-VALUES":
                values = parent.createEcucModuleConfigurationValues(self.getShortName(child_element))
                self.readEcucModuleConfigurationValues(child_element, values)
            elif tag_name == "PHYSICAL-DIMENSION":
                dimension = parent.createPhysicalDimension(self.getShortName(child_element))
                self.readPhysicalDimension(child_element, dimension)
            elif tag_name == "PARAMETER-INTERFACE":
                param_interface = parent.createParameterInterface(self.getShortName(child_element))
                self.readParameterInterface(child_element, param_interface)
            elif tag_name == "ETHERNET-FRAME":
                frame = parent.createGenericEthernetFrame(self.getShortName(child_element))
                self.readGenericEthernetFrame(child_element, frame)
            elif tag_name == "LIFE-CYCLE-INFO-SET":
                info_set = parent.createLifeCycleInfoSet(self.getShortName(child_element))
                self.readLifeCycleInfoSet(child_element, info_set)
            elif tag_name == "FLAT-MAP":
                map = parent.createFlatMap(self.getShortName(child_element))
                self.readFlatMap(child_element, map)
            elif tag_name == "PORT-INTERFACE-MAPPING-SET":
                mapping_set = parent.createPortInterfaceMappingSet(self.getShortName(child_element))
                self.readPortInterfaceMappingSet(child_element, mapping_set)
            elif tag_name == "ETHERNET-CLUSTER":
                cluster = parent.createEthernetCluster(self.getShortName(child_element))
                self.readEthernetCluster(child_element, cluster)
            elif tag_name == "DIAGNOSTIC-CONNECTION":
                connection = parent.createDiagnosticConnection(self.getShortName(child_element))
                self.readDiagnosticConnection(child_element, connection)
            elif tag_name == "DIAGNOSTIC-SERVICE-TABLE":
                table = parent.createDiagnosticServiceTable(self.getShortName(child_element))
                self.readDiagnosticServiceTable(child_element, table)
            elif tag_name == "DOCUMENTATION":
                documentation = parent.createDocumentation(self.getShortName(child_element))
                self.readDocumentation(child_element, documentation)
            elif tag_name == "MULTIPLEXED-I-PDU":
                i_pdu = parent.createMultiplexedIPdu(self.getShortName(child_element))
                self.readMultiplexedIPdu(child_element, i_pdu)
            elif tag_name == "USER-DEFINED-I-PDU":
                i_pdu = parent.createUserDefinedIPdu(self.getShortName(child_element))
                self.readUserDefinedIPdu(child_element, i_pdu)
            elif tag_name == "USER-DEFINED-PDU":
                pdu = parent.createUserDefinedPdu(self.getShortName(child_element))
                self.readUserDefinedPdu(child_element, pdu)
            elif tag_name == "GENERAL-PURPOSE-PDU":
                pdu = parent.createGeneralPurposePdu(self.getShortName(child_element))
                self.readGeneralPurposePdu(child_element, pdu)
            elif tag_name == "GENERAL-PURPOSE-I-PDU":
                i_pdu = parent.createGeneralPurposeIPdu(self.getShortName(child_element))
                self.readGeneralPurposeIPdu(child_element, i_pdu)
            elif tag_name == "SECURE-COMMUNICATION-PROPS-SET":
                prop_set = parent.createSecureCommunicationPropsSet(self.getShortName(child_element))
                self.readSecureCommunicationPropsSet(child_element, prop_set)
            elif tag_name == "SO-AD-ROUTING-GROUP":
                group = parent.createSoAdRoutingGroup(self.getShortName(child_element))
                self.readSoAdRoutingGroup(child_element, group)
            elif tag_name == "DO-IP-TP-CONFIG":
                config = parent.createDoIpTpConfig(self.getShortName(child_element))
                self.readDoIpTpConfig(child_element, config)
            elif tag_name == "HW-ELEMENT":
                hw_element = parent.createHwElement(self.getShortName(child_element))
                self.readHwElement(child_element, hw_element)
            elif tag_name == "HW-CATEGORY":
                hw_category = parent.createHwCategory(self.getShortName(child_element))
                self.readHwCategory(child_element, hw_category)
            elif tag_name == "HW-TYPE":
                type = parent.createHwType(self.getShortName(child_element))
                self.readHwType(child_element, type)
            elif tag_name == "FLEXRAY-FRAME":
                frame = parent.createFlexrayFrame(self.getShortName(child_element))
                self.readFlexrayFrame(child_element, frame)
            elif tag_name == "FLEXRAY-CLUSTER":
                cluster = parent.createFlexrayCluster(self.getShortName(child_element))
                self.readFlexrayCluster(child_element, cluster)
            elif tag_name == "DATA-TRANSFORMATION-SET":
                transformation_set = parent.createDataTransformationSet(self.getShortName(child_element))
                self.readDataTransformationSet(child_element, transformation_set)
            elif tag_name == "E-2-E-PROFILE-COMPATIBILITY-PROPS":
                props = parent.createE2EProfileCompatibilityProps(self.getShortName(child_element))
                self.readE2EProfileCompatibilityProps(child_element, props)
            elif tag_name == "COLLECTION":
                collection = parent.createCollection(self.getShortName(child_element))
                self.readCollection(child_element, collection)
            elif tag_name == "KEYWORD-SET":
                keyword_set = parent.createKeywordSet(self.getShortName(child_element))
                self.readKeywordSet(child_element, keyword_set)
            elif tag_name == "PORT-PROTOTYPE-BLUEPRINT":
                blueprint = parent.createPortPrototypeBlueprint(self.getShortName(child_element))
                self.readPortPrototypeBlueprint(child_element, blueprint)
            elif tag_name == "MODE-DECLARATION-MAPPING-SET":
                mapping_set = parent.createModeDeclarationMappingSet(self.getShortName(child_element))
                self.readModeDeclarationMappingSet(child_element, mapping_set)
            elif tag_name == "ECUC-MODULE-DEF":
                module_def = parent.createEcucModuleDef(self.getShortName(child_element))
                self.readEcucModuleDef(child_element, module_def)
            elif tag_name == "ECUC-DEFINITION-COLLECTION":
                collection = parent.createEcucDefinitionCollection(self.getShortName(child_element))
                self.readEcucDefinitionCollection(child_element, collection)
            elif tag_name == "ECUC-DESTINATION-URI-DEF-SET":
                uri_def_set = parent.createEcucDestinationUriDefSet(self.getShortName(child_element))
                self.readEcucDestinationUriDefSet(child_element, uri_def_set)
            elif tag_name == "SW-SYSTEMCONST":
                system_const = parent.createSwSystemConst(self.getShortName(child_element))
                self.readSwSystemconst(child_element, system_const)
            elif tag_name == "SW-SYSTEMCONSTANT-VALUE-SET":
                value_set = parent.createSwSystemconstantValueSet(self.getShortName(child_element))
                self.readSwSystemconstantValueSet(child_element, value_set)
            elif tag_name == "PREDEFINED-VARIANT":
                variant = parent.createPredefinedVariant(self.getShortName(child_element))
                self.readPredefinedVariant(child_element, variant)
            elif tag_name == "POST-BUILD-VARIANT-CRITERION":
                criterion = parent.createPostBuildVariantCriterion(self.getShortName(child_element))
                self.readPostBuildVariantCriterion(child_element, criterion)
            elif tag_name == "NV-DATA-INTERFACE":
                interface = parent.createNvDataInterface(self.getShortName(child_element))
                self.readNvDataInterface(child_element, interface)
            elif tag_name == "MC-FUNCTION":
                func = parent.createMcFunction(self.getShortName(child_element))
                self.readMcFunction(child_element, func)
            elif tag_name == "MC-GROUP":
                group = parent.createMcGroup(self.getShortName(child_element))
                self.readMcGroup(child_element, group)
            else:
                self.notImplemented("Unsupported Element type of ARPackage <%s>" % tag_name)

    def readMcFunction(self, element: ET.Element, func: McFunction):
        self.readIdentifiable(element, func)
        def_calprm_set_element = self.find(element, "DEF-CALPRM-SET")
        if def_calprm_set_element is not None:
            def_calprm_set = McFunctionDataRefSet()
            self.readMcFunctionDataRefSet(def_calprm_set_element, def_calprm_set)
            func.setDefCalprmSet(def_calprm_set)
        ref_calprm_set_element = self.find(element, "REF-CALPRM-SET")
        if ref_calprm_set_element is not None:
            ref_calprm_set = McFunctionDataRefSet()
            self.readMcFunctionDataRefSet(ref_calprm_set_element, ref_calprm_set)
            func.setRefCalprmSet(ref_calprm_set)
        in_measurement_set_element = self.find(element, "IN-MEASUREMENT-SET")
        if in_measurement_set_element is not None:
            in_measurement_set = McFunctionDataRefSet()
            self.readMcFunctionDataRefSet(in_measurement_set_element, in_measurement_set)
            func.setInMeasurementSet(in_measurement_set)
        loc_measurement_set_element = self.find(element, "LOC-MEASUREMENT-SET")
        if loc_measurement_set_element is not None:
            loc_measurement_set = McFunctionDataRefSet()
            self.readMcFunctionDataRefSet(loc_measurement_set_element, loc_measurement_set)
            func.setLocMeasurementSet(loc_measurement_set)
        out_measurement_set_element = self.find(element, "OUT-MEASUREMENT-SET")
        if out_measurement_set_element is not None:
            out_measurement_set = McFunctionDataRefSet()
            self.readMcFunctionDataRefSet(out_measurement_set_element, out_measurement_set)
            func.setOutMeasurementSet(out_measurement_set)
        for ref in self.getChildElementRefTypeList(element, "SUB-FUNCTION-REFS/SUB-FUNCTION-REF"):
            func.addSubFunctionRef(ref)

    def readMcFunctionDataRefSet(self, element: ET.Element, data_ref_set: McFunctionDataRefSet):
        conditional_element = self.find(element, "MC-FUNCTION-DATA-REF-SET-VARIANTS/MC-FUNCTION-DATA-REF-SET-CONDITIONAL")
        if conditional_element is None:
            return
        for ref in self.getChildElementRefTypeList(conditional_element, "FLAT-MAP-ENTRY-REFS/FLAT-MAP-ENTRY-REF"):
            data_ref_set.addFlatMapEntryRef(ref)
        for ref in self.getChildElementRefTypeList(conditional_element, "MC-DATA-INSTANCE-REFS/MC-DATA-INSTANCE-REF"):
            data_ref_set.addMcDataInstanceRef(ref)

    def readMcGroup(self, element: ET.Element, group: McGroup):
        self.readIdentifiable(element, group)
        for ref in self.getChildElementRefTypeList(element, "SUB-GROUP-REFS/SUB-GROUP-REF"):
            group.addSubGroupRef(ref)
        ref_calprm_set_element = self.find(element, "REF-CALPRM-SET")
        if ref_calprm_set_element is not None:
            ref_calprm_set = McGroupDataRefSet()
            self.readMcGroupDataRefSet(ref_calprm_set_element, ref_calprm_set)
            group.setRefCalprmSet(ref_calprm_set)
        ref_measurement_set_element = self.find(element, "REF-MEASUREMENT-SET")
        if ref_measurement_set_element is not None:
            ref_measurement_set = McGroupDataRefSet()
            self.readMcGroupDataRefSet(ref_measurement_set_element, ref_measurement_set)
            group.setRefMeasurementSet(ref_measurement_set)
        for ref in self.getChildElementRefTypeList(element, "MC-FUNCTION-REFS/MC-FUNCTION-REF"):
            group.addMcFunctionRef(ref)

    def readMcGroupDataRefSet(self, element: ET.Element, data_ref_set: McGroupDataRefSet):
        conditional_element = self.find(element, "MC-GROUP-DATA-REF-SET-VARIANTS/MC-GROUP-DATA-REF-SET-CONDITIONAL")
        if conditional_element is None:
            return
        for ref in self.getChildElementRefTypeList(conditional_element, "FLAT-MAP-ENTRY-REFS/FLAT-MAP-ENTRY-REF"):
            data_ref_set.addFlatMapEntryRef(ref)
        for ref in self.getChildElementRefTypeList(conditional_element, "MC-DATA-INSTANCE-REFS/MC-DATA-INSTANCE-REF"):
            data_ref_set.addMcDataInstanceRef(ref)

    def readReferenceBases(self, element: ET.Element, parent: ARPackage):
        for child_element in self.findall(element, "REFERENCE-BASES/REFERENCE-BASE"):
            base = ReferenceBase()
            base.setShortLabel(self.getChildElementOptionalLiteral(child_element, "SHORT-LABEL"))
            base.setIsDefault(self.getChildElementOptionalBooleanValue(child_element, "IS-DEFAULT"))
            base.setIsGlobal(self.getChildElementOptionalBooleanValue(child_element, "IS-GLOBAL"))
            base.setBaseIsThisPackage(self.getChildElementOptionalBooleanValue(child_element, "BASE-IS-THIS-PACKAGE"))
            base.setPackageRef(self.getChildElementOptionalRefType(child_element, "PACKAGE-REF"))
            parent.addReferenceBase(base)

    def readARPackage(self, element: ET.Element, ar_package: ARPackage):
        self.logger.debug("Read ARPackages <%s>" % ar_package.getFullName())

        self.readIdentifiable(element, ar_package)
        self.readARPackages(element, ar_package)
        self.readARPackageElements(element, ar_package)
        self.readReferenceBases(element, ar_package)

    def readARPackages(self, element: ET.Element, parent: ARPackage):
        for child_element in self.findall(element, "AR-PACKAGES/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "AR-PACKAGE":
                ar_package = parent.createARPackage(self.getShortName(child_element))
                self.readARPackage(child_element, ar_package)
            else:
                self.notImplemented("Unsupported ARPackage <%s>" % tag_name)

    def load(self, filename, document: AUTOSAR):
        self.logger.info("Loading %s ..." % os.path.realpath(filename))

        tree = ET.parse(filename)
        root = tree.getroot()
        if self.getPureTagName(root.tag) != "AUTOSAR":
            self.raiseError("Invalid ARXML file <%s>" % filename)

        self.getAUTOSARInfo(root, document)
        document.setAdminData(self.getAdminData(root, "ADMIN-DATA"))
        self.readARPackages(root, document)

        document.reload()
