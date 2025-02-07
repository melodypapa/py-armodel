import xml.etree.cElementTree as ET
from typing import List

from ..models.M2.MSR.AsamHdo.AdminData import AdminData
from ..models.M2.MSR.AsamHdo.BaseTypes import BaseTypeDirectDefinition, SwBaseType
from ..models.M2.MSR.AsamHdo.ComputationMethod import Compu, CompuConst, CompuConstContent, CompuConstFormulaContent, CompuConstNumericContent
from ..models.M2.MSR.AsamHdo.ComputationMethod import CompuConstTextContent, CompuMethod, CompuNominatorDenominator, CompuScale
from ..models.M2.MSR.AsamHdo.ComputationMethod import CompuScaleConstantContents, CompuScaleRationalFormula, CompuScales
from ..models.M2.MSR.AsamHdo.Constraints.GlobalConstraints import DataConstr, InternalConstrs, PhysConstrs
from ..models.M2.MSR.AsamHdo.SpecialData import Sdg
from ..models.M2.MSR.AsamHdo.Units import PhysicalDimension, Unit
from ..models.M2.MSR.CalibrationData.CalibrationValue import SwValueCont, SwValues
from ..models.M2.MSR.DataDictionary.Axis import SwAxisGrouped, SwAxisIndividual
from ..models.M2.MSR.DataDictionary.AuxillaryObjects import SwAddrMethod
from ..models.M2.MSR.DataDictionary.CalibrationParameter import SwCalprmAxis, SwCalprmAxisSet
from ..models.M2.MSR.DataDictionary.DataDefProperties import SwDataDefProps, SwPointerTargetProps, ValueList
from ..models.M2.MSR.DataDictionary.RecordLayout import SwRecordLayout, SwRecordLayoutGroup, SwRecordLayoutV
from ..models.M2.MSR.DataDictionary.ServiceProcessTask import SwServiceArg
from ..models.M2.MSR.Documentation.Annotation import Annotation
from ..models.M2.MSR.Documentation.BlockElements.Figure import Graphic, MlFigure
from ..models.M2.MSR.Documentation.TextModel.BlockElements.PaginationAndView import DocumentViewSelectable, Paginateable
from ..models.M2.MSR.Documentation.TextModel.BlockElements import DocumentationBlock
from ..models.M2.MSR.Documentation.TextModel.BlockElements.ListElements import ARList
from ..models.M2.MSR.Documentation.TextModel.LanguageDataModel import LLongName, LPlainText, LanguageSpecific
from ..models.M2.MSR.Documentation.TextModel.MultilanguageData import MultiLanguageOverviewParagraph, MultiLanguageParagraph, MultiLanguagePlainText
from ..models.M2.MSR.Documentation.TextModel.MultilanguageData import MultilanguageLongName

from ..models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from ..models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior import BswApiOptions, BswAsynchronousServerCallPoint, BswBackgroundEvent
from ..models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior import BswCalledEntity, BswDataReceivedEvent, BswModuleCallPoint
from ..models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior import BswInternalTriggerOccurredEvent, BswOperationInvokedEvent
from ..models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior import BswDataReceptionPolicy, BswEvent, BswExternalTriggerOccurredEvent
from ..models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior import BswInternalBehavior, BswInterruptEntity, BswModeSenderPolicy, BswModuleEntity
from ..models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior import BswQueuedDataReceptionPolicy, BswSchedulableEntity, BswScheduleEvent
from ..models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior import BswTimingEvent, BswVariableAccess, BswInternalTriggeringPoint
from ..models.M2.AUTOSARTemplates.BswModuleTemplate.BswOverview import BswModuleDescription
from ..models.M2.AUTOSARTemplates.BswModuleTemplate.BswImplementation import BswImplementation
from ..models.M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces import BswModuleClientServerEntry, BswModuleEntry
from ..models.M2.AUTOSARTemplates.CommonStructure import ApplicationValueSpecification, ArrayValueSpecification, ConstantReference
from ..models.M2.AUTOSARTemplates.CommonStructure import ConstantSpecification, NumericalValueSpecification, RecordValueSpecification
from ..models.M2.AUTOSARTemplates.CommonStructure import TextValueSpecification, ValueSpecification
from ..models.M2.AUTOSARTemplates.CommonStructure.FlatMap import FlatInstanceDescriptor, FlatMap
from ..models.M2.AUTOSARTemplates.CommonStructure.Filter import DataFilter
from ..models.M2.AUTOSARTemplates.CommonStructure.Implementation import Code, Implementation, ImplementationProps
from ..models.M2.AUTOSARTemplates.CommonStructure.ImplementationDataTypes import ImplementationDataType
from ..models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior import ExecutableEntity
from ..models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior import InternalBehavior
from ..models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration import ModeDeclaration, ModeDeclarationGroup, ModeDeclarationGroupPrototype
from ..models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption import ResourceConsumption
from ..models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.StackUsage import RoughEstimateStackUsage, StackUsage
from ..models.M2.AUTOSARTemplates.CommonStructure.SwcBswMapping import SwcBswMapping, SwcBswRunnableMapping
from ..models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import CryptoServiceNeeds, DiagEventDebounceMonitorInternal
from ..models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import DiagnosticCommunicationManagerNeeds, DiagnosticEventInfoNeeds
from ..models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import DiagnosticEventNeeds, DiagnosticRoutineNeeds, DiagnosticValueNeeds
from ..models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import EcuStateMgrUserNeeds, NvBlockNeeds, RoleBasedDataAssignment
from ..models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import RoleBasedDataTypeAssignment, ServiceDependency
from ..models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.Keyword import KeywordSet, Keyword
from ..models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.BlueprintDedicated.PortPrototypeBlueprint import PortPrototypeBlueprint
from ..models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.TimingExtensions import SwcTiming, TimingExtension
from ..models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.ExecutionOrderConstraint import EOCExecutableEntityRef
from ..models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.ExecutionOrderConstraint import ExecutionOrderConstraint
from ..models.M2.AUTOSARTemplates.CommonStructure.TriggerDeclaration import Trigger
from ..models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticContribution import DiagnosticServiceTable
from ..models.M2.AUTOSARTemplates.ECUCDescriptionTemplate import EcucAbstractReferenceValue, EcucContainerValue, EcucInstanceReferenceValue
from ..models.M2.AUTOSARTemplates.ECUCDescriptionTemplate import EcucModuleConfigurationValues, EcucNumericalParamValue, EcucParameterValue
from ..models.M2.AUTOSARTemplates.ECUCDescriptionTemplate import EcucReferenceValue, EcucTextualParamValue, EcucValueCollection
from ..models.M2.AUTOSARTemplates.EcuResourceTemplate import HwDescriptionEntity, HwElement, HwPinGroup
from ..models.M2.AUTOSARTemplates.EcuResourceTemplate.HwElementCategory import HwAttributeDef, HwCategory, HwType
from ..models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AnyInstanceRef
from ..models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ElementCollection import Collection
from ..models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARPackage, ReferenceBase
from ..models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.EngineeringObject import AutosarEngineeringObject, EngineeringObject
from ..models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import ARElement, Describable, Identifiable
from ..models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Referrable, MultilanguageReferrable
from ..models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType, ARLiteral, Limit
from ..models.M2.AUTOSARTemplates.GenericStructure.LifeCycles import LifeCycleInfo, LifeCycleInfoSet, LifeCyclePeriod
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import CompositeNetworkRepresentation, ModeSwitchedAckRequest
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import TransmissionAcknowledgementRequest
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import ClientComSpec, ModeSwitchReceiverComSpec, ModeSwitchSenderComSpec
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import NonqueuedReceiverComSpec, NonqueuedSenderComSpec, PPortComSpec
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import ParameterRequireComSpec, QueuedReceiverComSpec, QueuedSenderComSpec
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import RPortComSpec, ReceiverComSpec, SenderComSpec, ServerComSpec
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.Components import AbstractProvidedPortPrototype, AbstractRequiredPortPrototype
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.Components import ApplicationSwComponentType, AtomicSwComponentType
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.Components import ComplexDeviceDriverSwComponentType, CompositionSwComponentType
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.Components import EcuAbstractionSwComponentType, PRPortPrototype, PortGroup, SwComponentType
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.Components import PPortPrototype, PortPrototype, RPortPrototype, SymbolProps
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.Components import ServiceSwComponentType
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs import InnerPortGroupInCompositionInstanceRef
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs import ModeGroupInAtomicSwcInstanceRef
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs import PModeGroupInAtomicSwcInstanceRef
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs import RModeGroupInAtomicSWCInstanceRef
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs import RModeInAtomicSwcInstanceRef, RVariableInAtomicSwcInstanceRef
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.Composition import AssemblySwConnector, DelegationSwConnector, SwComponentPrototype, SwConnector
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.InstanceRefs import POperationInAtomicSwcInstanceRef, PPortInCompositionInstanceRef
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.InstanceRefs import ROperationInAtomicSwcInstanceRef, RPortInCompositionInstanceRef
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes import ApplicationArrayElement
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes import ApplicationCompositeElementDataPrototype
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes import ApplicationRecordElement, AutosarDataPrototype, DataPrototype
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes import ParameterDataPrototype, VariableDataPrototype
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes import ApplicationArrayDataType, ApplicationCompositeDataType
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes import ApplicationDataType, ApplicationPrimitiveDataType
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes import ApplicationRecordDataType, AutosarDataType
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes import DataTypeMappingSet
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.EndToEndProtection import EndToEndDescription, EndToEndProtection, EndToEndProtectionISignalIPdu
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.EndToEndProtection import EndToEndProtectionVariablePrototype
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.EndToEndProtection import EndToEndProtectionSet
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import ApplicationError, ArgumentDataPrototype, ClientServerInterface, ClientServerInterfaceMapping, ClientServerOperationMapping
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import ClientServerOperation, DataInterface
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import DataPrototypeMapping, ModeSwitchInterface, ParameterInterface
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import PortInterface, PortInterfaceMappingSet, SenderReceiverInterface
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import TriggerInterface, VariableAndParameterInterfaceMapping
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.InstanceRefs import ApplicationCompositeElementInPortInterfaceInstanceRef
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior import AsynchronousServerCallPoint, RunnableEntity, RunnableEntityArgument
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior import SwcInternalBehavior, SynchronousServerCallPoint
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.AutosarVariableRef import AutosarVariableRef
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements import ParameterAccess, VariableAccess
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.InstanceRefsUsage import AutosarParameterRef
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.PortAPIOptions import PortDefinedArgumentValue
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents import AsynchronousServerCallReturnsEvent, BackgroundEvent
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents import DataReceivedEvent, InitEvent, InternalTriggerOccurredEvent
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents import ModeSwitchedAckEvent, OperationInvokedEvent, RTEEvent
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents import SwcModeSwitchEvent, TimingEvent
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.IncludedDataTypes import IncludedDataTypeSet
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ModeDeclarationGroup import IncludedModeDeclarationGroupSet
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ModeDeclarationGroup import ModeAccessPoint, ModeSwitchPoint
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ServerCall import ServerCallPoint
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ServiceMapping import RoleBasedPortAssignment, SwcServiceDependency
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.SwcImplementation import SwcImplementation

from ..models.M2.AUTOSARTemplates.SystemTemplate import SwcToEcuMapping, System, SystemMapping
from ..models.M2.AUTOSARTemplates.SystemTemplate.DataMapping import SenderRecCompositeTypeMapping, SenderRecRecordElementMapping
from ..models.M2.AUTOSARTemplates.SystemTemplate.DataMapping import SenderRecRecordTypeMapping, SenderReceiverToSignalGroupMapping
from ..models.M2.AUTOSARTemplates.SystemTemplate.DataMapping import SenderReceiverToSignalMapping
from ..models.M2.AUTOSARTemplates.SystemTemplate.DiagnosticConnection import DiagnosticConnection
from ..models.M2.AUTOSARTemplates.SystemTemplate.EcuResourceMapping import ECUMapping
from ..models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanCommunication import CanFrame, CanFrameTriggering, RxIdentifierRange
from ..models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology import AbstractCanCommunicationController
from ..models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology import AbstractCanCommunicationControllerAttributes
from ..models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology import CanCommunicationConnector, CanCommunicationController
from ..models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology import CanControllerConfigurationRequirements
from ..models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology import CanControllerFdConfiguration
from ..models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology import CanControllerFdConfigurationRequirements
from ..models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetCommunication import SoAdRoutingGroup, SocketConnection
from ..models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetCommunication import SocketConnectionBundle
from ..models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetCommunication import SocketConnectionIpduIdentifier
from ..models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetFrame import GenericEthernetFrame
from ..models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import CouplingPort, CouplingPortDetails, CouplingPortFifo
from ..models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import CouplingPortScheduler, CouplingPortStructuralElement
from ..models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import EthernetCluster, EthernetCommunicationConnector
from ..models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import EthernetCommunicationController
from ..models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import EthernetPriorityRegeneration, InitialSdDelayConfig
from ..models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import MacMulticastGroup, RequestResponseDelay, SdClientConfig
from ..models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import VlanMembership
from ..models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.NetworkEndpoint import DoIpEntity, InfrastructureServices, Ipv6Configuration
from ..models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.NetworkEndpoint import NetworkEndpoint, NetworkEndpointAddress
from ..models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import ApplicationEndpoint, ConsumedEventGroup
from ..models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import ConsumedServiceInstance, EventHandler, GenericTp
from ..models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import ProvidedServiceInstance, SdServerConfig, SoAdConfig
from ..models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import SocketAddress, TcpTp, TpPort
from ..models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import TransportProtocolConfiguration, UdpTp
from ..models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Flexray.FlexrayCommunication import FlexrayAbsolutelyScheduledTiming, FlexrayFrame
from ..models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Flexray.FlexrayCommunication import FlexrayFrameTriggering
from ..models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Flexray.FlexrayTopology import FlexrayCluster, FlexrayCommunicationConnector
from ..models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Flexray.FlexrayTopology import FlexrayCommunicationController
from ..models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication import ApplicationEntry, LinFrameTriggering, LinScheduleTable
from ..models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication import LinUnconditionalFrame, ScheduleTableEntry
from ..models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinTopology import LinCommunicationConnector, LinCommunicationController, LinMaster
from ..models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Multiplatform import Gateway, IPduMapping, ISignalMapping, TargetIPduRef
from ..models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import DynamicPart, DynamicPartAlternative, FrameTriggering
from ..models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import GeneralPurposeIPdu, GeneralPurposePdu, IPdu, IPduTiming
from ..models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import ISignalGroup, ISignalIPdu, ISignalIPduGroup
from ..models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import ISignalToIPduMapping, ISignalTriggering, MultiplexedIPdu
from ..models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import MultiplexedPart, Pdu, PduTriggering
from ..models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import SecureCommunicationAuthenticationProps
from ..models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import SecureCommunicationFreshnessProps, SecureCommunicationProps
from ..models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import SecureCommunicationPropsSet, SecuredIPdu, SegmentPosition
from ..models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import StaticPart, SystemSignal, DcmIPdu, Frame, ISignal, NPdu
from ..models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import NmPdu, SystemSignalGroup, UserDefinedIPdu, UserDefinedPdu
from ..models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import AbstractCanCluster, CanCluster, CanClusterBusOffRecovery
from ..models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import FlexrayPhysicalChannel, CommunicationCycle, CycleRepetition
from ..models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import CanPhysicalChannel, CommConnectorPort, CommunicationCluster
from ..models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import CommunicationConnector, CommunicationController
from ..models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import EthernetPhysicalChannel, FramePort, IPduPort, ISignalPort
from ..models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import LinCluster, LinPhysicalChannel, PhysicalChannel
from ..models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.EcuInstance import EcuInstance
from ..models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.Timing import CyclicTiming, EventControlledTiming, TimeRangeType
from ..models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.Timing import TransmissionModeCondition, TransmissionModeDeclaration
from ..models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.Timing import TransmissionModeTiming
from ..models.M2.AUTOSARTemplates.SystemTemplate.InstanceRefs import ComponentInSystemInstanceRef, VariableDataPrototypeInSystemInstanceRef
from ..models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement import CanNmCluster, CanNmClusterCoupling, CanNmNode, NmCluster, NmConfig, NmEcu
from ..models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement import NmNode, UdpNmCluster, UdpNmClusterCoupling, UdpNmEcu, UdpNmNode
from ..models.M2.AUTOSARTemplates.SystemTemplate.SWmapping import SwcToImplMapping
from ..models.M2.AUTOSARTemplates.SystemTemplate.Transformer import BufferProperties, DataTransformation, DataTransformationSet
from ..models.M2.AUTOSARTemplates.SystemTemplate.Transformer import EndToEndTransformationISignalProps, TransformationISignalProps
from ..models.M2.AUTOSARTemplates.SystemTemplate.Transformer import EndToEndTransformationDescription, TransformationDescription
from ..models.M2.AUTOSARTemplates.SystemTemplate.Transformer import TransformationTechnology
from ..models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols import CanTpAddress, CanTpChannel, CanTpConfig, CanTpConnection, CanTpEcu
from ..models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols import CanTpNode, DoIpLogicAddress, DoIpTpConfig, DoIpTpConnection, LinTpConfig
from ..models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols import LinTpConnection, LinTpNode, TpAddress, TpConfig, TpConnection

from .abstract_arxml_writer import AbstractARXMLWriter


class ARXMLWriter(AbstractARXMLWriter):
    def __init__(self, options=None) -> None:
        super().__init__(options)

    def setShortName(self, parent: ET.Element, name: str) -> ET.Element:
        sub_element = ET.SubElement(parent, "SHORT-NAME")
        sub_element.text = name

        return sub_element
    
    def setChildElementRxIdentifierRange(self, element: ET.Element, key: str, range: RxIdentifierRange):
        if range is not None:
            child_element = ET.SubElement(element, key)
            self.setChildElementOptionalNumericalValue(child_element, "LOWER-CAN-ID", range.getLowerCanId())
            self.setChildElementOptionalNumericalValue(child_element, "UPPER-CAN-ID", range.getUpperCanId())
    
    def writeSds(self, parent: ET.Element, sdg: Sdg):
        for sd in sdg.getSds():
            sd_tag = ET.SubElement(parent, "SD")
            if sd.gid is not None:
                sd_tag.attrib['GID'] = sd.gid
            sd_tag.text = sd.value

    def writeSdgCaption(self, element: ET.Element, sdg: Sdg):
        caption = sdg.getSdgCaption()
        if caption is not None:
            child_element = ET.SubElement(element, "SDG-CAPTION")
            self.writeMultilanguageReferrable(child_element, caption)

    def writeSdgSdxRefs(self, element: ET.Element, sdg: Sdg):
        for ref in sdg.getSdxRefs():
            self.setChildElementOptionalRefType(element, "SDX-REF", ref)

    def setSdg(self, element: ET.Element, sdg: Sdg):
        if sdg is not None:
            child_element = ET.SubElement(element, "SDG")
            if sdg.gid is not None and sdg.gid != "":
                child_element.attrib['GID'] = sdg.gid
            self.writeSdgCaption(child_element, sdg)
            self.writeSds(child_element, sdg)
            for sdg_item in sdg.getSdgContentsTypes():
                self.setSdg(child_element, sdg_item)
            self.writeSdgSdxRefs(child_element, sdg)
            
    def writeSdgs(self, parent: ET.Element, admin_data: AdminData):
        sdgs = admin_data.getSdgs()
        if len(sdgs) > 0:
            sdgs_tag = ET.SubElement(parent, "SDGS")
            for sdg in sdgs:
                self.setSdg(sdgs_tag, sdg)
    
    def setChildLimitElement(self, element: ET.Element, key: str, limit: Limit):
        if limit is not None:
            limit_tag = ET.SubElement(element, key)
            self.writeARObjectAttributes(limit_tag, limit)
            if limit.intervalType is not None:
                limit_tag.attrib['INTERVAL-TYPE'] = limit.intervalType
            limit_tag.text = limit.value
    
    def writeReferrable(self, element: ET.Element, referrable: Referrable):
        self.writeARObjectAttributes(element, referrable)
        self.setShortName(element, referrable.getShortName())

    def setLanguageSpecific(self, element: ET.Element, key: str, specific: LanguageSpecific):
        child_element = ET.SubElement(element, key)
        self.writeARObjectAttributes(child_element, specific)
        if specific.l is not None:
            child_element.attrib['L'] = specific.l
        child_element.text = specific.value

    def setLLongName(self, element: ET.Element, name: LLongName):
        self.setLanguageSpecific(element, "L-4", name)

    def setMultiLongName(self, element: ET.Element, key: str, long_name: MultilanguageLongName):
        if long_name is not None:
            child_element = ET.SubElement(element, key)
            self.writeARObjectAttributes(child_element, long_name)
            for l4 in long_name.getL4s():
                self.setLLongName(child_element, l4)

    def setLOverviewParagraph(self, element: ET.Element, name: LLongName):
        self.setLanguageSpecific(element, "L-2", name)

    def setMultiLanguageOverviewParagraph(self, element: ET.Element, key: str, paragraph: MultiLanguageOverviewParagraph):
        if paragraph is not None:
            child_element = ET.SubElement(element, key)
            self.writeARObjectAttributes(child_element, paragraph)
            for l2 in paragraph.getL2s():
                self.setLOverviewParagraph(child_element, l2)

    def writeMultilanguageReferrable(self, element: ET.Element, referrable: MultilanguageReferrable):
        self.writeReferrable(element, referrable)
        if referrable.longName is not None:
            self.setMultiLongName(element, "LONG-NAME", referrable.longName)

    def setLPlainText(self, element: ET.Element, text: LPlainText):
        self.setLanguageSpecific(element, "L-10", text)

    def setMultiLanguagePlainText(self, element: ET.Element, key: str, paragraph: MultiLanguagePlainText):
        if paragraph is not None:
            child_element = ET.SubElement(element, key)
            self.writeARObjectAttributes(child_element, paragraph)
            for l10 in paragraph.getL10s():
                self.setLPlainText(child_element, l10)

    def setAdminData(self, element: ET.Element, admin_data: AdminData):
        if admin_data is not None:
            child_element = ET.SubElement(element, "ADMIN-DATA")
            self.setChildElementOptionalLiteral(child_element, "LANGUAGE", admin_data.getLanguage())
            self.setMultiLanguagePlainText(child_element, "USED-LANGUAGES", admin_data.getUsedLanguages())
            self.writeSdgs(child_element, admin_data)

    def writeIdentifiable(self, element: ET.Element, identifiable: Identifiable):
        self.writeMultilanguageReferrable(element, identifiable)
        self.setAnnotations(element, identifiable.getAnnotations())
        self.setMultiLanguageOverviewParagraph(element, "DESC", identifiable.getDesc())
        self.setChildElementOptionalLiteral(element, "CATEGORY", identifiable.getCategory())
        self.writeDocumentationBlock(element, "INTRODUCTION", identifiable.getIntroduction())
        self.setAdminData(element, identifiable.getAdminData())

    def writeARElement(self, parent: ET.Element, ar_element: ARElement):
        self.writeIdentifiable(parent, ar_element)

    def setTransmissionAcknowledgementRequest(self, element: ET.Element, acknowledge: TransmissionAcknowledgementRequest):
        if (acknowledge is not None):
            child_element = ET.SubElement(element, "TRANSMISSION-ACKNOWLEDGE")
            self.writeARObjectAttributes(child_element, acknowledge)
            if acknowledge.timeout is not None:
                self.setChildElementOptionalFloatValue(child_element, "TIMEOUT", acknowledge.timeout)

    def setSenderComSpec(self, element: ET.Element, com_spec: SenderComSpec):
        representations = com_spec.getCompositeNetworkRepresentations()
        if len(representations) > 0:
            child_element = ET.SubElement(element, "COMPOSITE-NETWORK-REPRESENTATIONS")
            for representation in representations:
                self.setCompositeNetworkRepresentation(child_element, representation)
        self.setChildElementOptionalRefType(element, "DATA-ELEMENT-REF", com_spec.getDataElementRef())
        self.setSwDataDefProps(element, "NETWORK-REPRESENTATION", com_spec.getNetworkRepresentation())
        self.setChildElementOptionalLiteral(element, "HANDLE-OUT-OF-RANGE", com_spec.getHandleOutOfRange())
        self.setTransmissionAcknowledgementRequest(element, com_spec.getTransmissionAcknowledge())
        self.setChildElementOptionalBooleanValue(element, "USES-END-TO-END-PROTECTION", com_spec.getUsesEndToEndProtection())

    def setNonqueuedSenderComSpec(self, element: ET.Element, com_spec: NonqueuedSenderComSpec):
        child_element = ET.SubElement(element, "NONQUEUED-SENDER-COM-SPEC")
        self.writeARObjectAttributes(child_element, com_spec)
        self.setSenderComSpec(child_element, com_spec)
        self.setValueSpecification(child_element, "INIT-VALUE", com_spec.getInitValue())

    def setServerComSpec(self, element: ET.Element, com_spec: ServerComSpec):
        child_element = ET.SubElement(element, "SERVER-COM-SPEC")
        self.writeARObjectAttributes(child_element, com_spec)
        self.setChildElementOptionalRefType(child_element, "OPERATION-REF", com_spec.getOperationRef())
        self.setChildElementOptionalNumericalValue(child_element, "QUEUE-LENGTH", com_spec.getQueueLength())

    def setQueuedSenderComSpec(self, element: ET.Element, com_spec: QueuedSenderComSpec):
        child_element = ET.SubElement(element, "QUEUED-SENDER-COM-SPEC")
        self.writeARObjectAttributes(child_element, com_spec)
        self.setSenderComSpec(child_element, com_spec)

    def setModeSwitchedAckRequest(self, element: ET.Element, key: str, request: ModeSwitchedAckRequest):
        if request is not None:
            child_element = ET.SubElement(element, key)
            self.writeARObjectAttributes(child_element, request)
            self.setChildElementOptionalTimeValue(child_element, "TIMEOUT", request.getTimeout())

    def setModeSwitchSenderComSpec(self, element: ET.Element, com_spec: ModeSwitchSenderComSpec):
        child_element = ET.SubElement(element, "MODE-SWITCH-SENDER-COM-SPEC")
        self.writeARObjectAttributes(child_element, com_spec)
        self.setChildElementOptionalRefType(child_element, "MODE-GROUP-REF", com_spec.getModeGroupRef())
        self.setModeSwitchedAckRequest(child_element, "MODE-SWITCHED-ACK", com_spec.getModeSwitchedAck())
        self.setChildElementOptionalNumericalValue(child_element, "QUEUE-LENGTH", com_spec.getQueueLength())
    
    def writePPortComSpec(self, com_specs_tag: ET.Element, com_spec: PPortComSpec):
        if isinstance(com_spec, NonqueuedSenderComSpec):
            self.setNonqueuedSenderComSpec(com_specs_tag, com_spec)
        elif isinstance(com_spec, ServerComSpec):
            self.setServerComSpec(com_specs_tag, com_spec)
        elif isinstance(com_spec, QueuedSenderComSpec):
            self.setQueuedSenderComSpec(com_specs_tag, com_spec)
        elif isinstance(com_spec, ModeSwitchSenderComSpec):
            self.setModeSwitchSenderComSpec(com_specs_tag, com_spec)
        else:
            self.notImplemented("Unsupported PPortComSpec %s" % type(com_spec))

    def setApplicationCompositeElementInPortInterfaceInstanceRef(self, element: ET.Element, key: str, iref: ApplicationCompositeElementInPortInterfaceInstanceRef):     # noqa E501
        if iref is not None:
            child_element = ET.SubElement(element, key)
            self.setChildElementOptionalRefType(child_element, "ROOT-DATA-PROTOTYPE-REF", iref.root_data_prototype_ref)
            self.setChildElementOptionalRefType(child_element, "TARGET-DATA-PROTOTYPE-REF", iref.target_data_prototype_ref)
        return iref

    def setCompositeNetworkRepresentation(self, element: ET.Element, representation: CompositeNetworkRepresentation):
        if representation is not None:
            self.logger.debug("setCompositeNetworkRepresentation")
            child_element = ET.SubElement(element, "COMPOSITE-NETWORK-REPRESENTATION")
            self.setApplicationCompositeElementInPortInterfaceInstanceRef(child_element, "LEAF-ELEMENT-IREF", representation.getLeafElementIRef())
            self.setSwDataDefProps(child_element, "NETWORK-REPRESENTATION", representation.getNetworkRepresentation())
        
    def writeReceiverComSpec(self, element: ET.Element, com_spec: ReceiverComSpec):
        representations = com_spec.getCompositeNetworkRepresentations()
        if len(representations) > 0:
            child_element = ET.SubElement(element, "COMPOSITE-NETWORK-REPRESENTATIONS")
            for representation in representations:
                self.setCompositeNetworkRepresentation(child_element, representation)
        self.setChildElementOptionalRefType(element, "DATA-ELEMENT-REF", com_spec.getDataElementRef())
        self.setSwDataDefProps(element, "NETWORK-REPRESENTATION", com_spec.getNetworkRepresentation())
        self.setChildElementOptionalLiteral(element, "HANDLE-OUT-OF-RANGE", com_spec.getHandleOutOfRange())
        self.setChildElementOptionalLiteral(element, "HANDLE-OUT-OF-RANGE-STATUS", com_spec.getHandleOutOfRangeStatus())
        self.setChildElementOptionalBooleanValue(element, "USES-END-TO-END-PROTECTION", com_spec.getUsesEndToEndProtection())

    def setSwValues(self, element: ET.Element, key: str, sw_values: SwValues):
        if sw_values is not None:
            child_element = ET.SubElement(element, key)
            self.writeARObjectAttributes(child_element, sw_values)
            for v in sw_values.getVs():
                self.setChildElementOptionalFloatValue(child_element, "V", v)
            self.setChildElementOptionalLiteral(child_element, "VT", sw_values.vt)

    def setValueList(self, element: ET.Element, key: str, value_list: ValueList):
        if value_list is not None:
            child_element = ET.SubElement(element, key)
            self.writeARObjectAttributes(child_element, value_list)
            self.setChildElementOptionalFloatValue(child_element, "V", value_list.v)

    def writeSwValueCont(self, element: ET.Element, cont: SwValueCont):
        if cont is not None:
            child_element = ET.SubElement(element, "SW-VALUE-CONT")
            self.writeARObjectAttributes(child_element, cont)
            self.setChildElementOptionalRefType(child_element, "UNIT-REF", cont.unitRef)
            self.setValueList(child_element, "SW-ARRAYSIZE", cont.swArraysize)
            self.setSwValues(child_element, "SW-VALUES-PHYS", cont.swValuesPhys)

    def writeValueSpecification(self, element: ET.Element, value_spec: ValueSpecification):
        if value_spec is not None:
            self.writeARObjectAttributes(element, value_spec)
            self.setChildElementOptionalLiteral(element, "SHORT-LABEL", value_spec.getShortLabel())

    def writeTextValueSpecification(self, element: ET.Element, value_spec: TextValueSpecification):
        if value_spec is not None:
            value_spec_tag = ET.SubElement(element, "TEXT-VALUE-SPECIFICATION")
            self.writeValueSpecification(value_spec_tag, value_spec)
            self.setChildElementOptionalLiteral(value_spec_tag, "VALUE", value_spec.getValue())

    def writeNumericalValueSpecification(self, element: ET.Element, value_spec: NumericalValueSpecification):
        if value_spec is not None:
            value_spec_tag = ET.SubElement(element, "NUMERICAL-VALUE-SPECIFICATION")
            self.writeValueSpecification(value_spec_tag, value_spec)
            self.setChildElementOptionalFloatValue(value_spec_tag, "VALUE", value_spec.getValue())

    def writeArrayValueSpecification(self, element: ET.Element, value_spec: ArrayValueSpecification):
        value_spec_tag = ET.SubElement(element, "ARRAY-VALUE-SPECIFICATION")
        self.writeValueSpecification(value_spec_tag, value_spec)
        sub_elements = value_spec.getElements()
        if len(sub_elements) > 0:
            elements_tag = ET.SubElement(value_spec_tag, "ELEMENTS")
            for sub_element in sub_elements:
                if isinstance(sub_element, NumericalValueSpecification):
                    self.writeNumericalValueSpecification(elements_tag, sub_element)
                elif isinstance(sub_element, ApplicationValueSpecification):
                    self.writeApplicationValueSpecification(elements_tag, sub_element)
                elif isinstance(sub_element, TextValueSpecification):
                    self.writeTextValueSpecification(elements_tag, sub_element)
                elif isinstance(sub_element, ArrayValueSpecification):
                    self.writeArrayValueSpecification(elements_tag, sub_element)
                elif isinstance(sub_element, RecordValueSpecification):
                    self.writeRecordValueSpecification(elements_tag, sub_element)
                else:
                    self.notImplemented("Unsupported element type of <%s> of ArrayValueSpecification" % type(sub_element))

    def setConstantReference(self, element: ET.Element, value_spec: ConstantReference):
        value_spec_tag = ET.SubElement(element, "CONSTANT-REFERENCE")
        self.writeValueSpecification(value_spec_tag, value_spec)
        self.setChildElementOptionalRefType(value_spec_tag, "CONSTANT-REF", value_spec.getConstantRef())

    def setValueSpecification(self, element: ET.Element, key: str, value_spec: ValueSpecification):
        if value_spec is not None:
            child_element = ET.SubElement(element, key)
            if isinstance(value_spec, ApplicationValueSpecification):
                self.writeApplicationValueSpecification(child_element, value_spec)
            elif isinstance(value_spec, TextValueSpecification):
                self.writeTextValueSpecification(child_element, value_spec)
            elif isinstance(value_spec, ConstantReference):
                self.setConstantReference(child_element, value_spec)
            elif isinstance(value_spec, NumericalValueSpecification):
                self.writeNumericalValueSpecification(child_element, value_spec)
            elif isinstance(value_spec, ArrayValueSpecification):
                self.writeArrayValueSpecification(child_element, value_spec)
            elif isinstance(value_spec, RecordValueSpecification):
                self.writeRecordValueSpecification(child_element, value_spec)
            else:
                self.notImplemented("Unsupported ValueSpecification %s" % type(value_spec))

    def writeNonqueuedReceiverComSpec(self, element: ET.Element, com_spec: NonqueuedReceiverComSpec):
        child_element = ET.SubElement(element, "NONQUEUED-RECEIVER-COM-SPEC")
        self.writeARObjectAttributes(child_element, com_spec)
        self.writeReceiverComSpec(child_element, com_spec)
        self.setChildElementOptionalFloatValue(child_element, "ALIVE-TIMEOUT", com_spec.getAliveTimeout())
        self.setChildElementOptionalBooleanValue(child_element, "ENABLE-UPDATE", com_spec.getEnableUpdated())
        self.setDataFilter(child_element, "FILTER", com_spec.getFilter())
        self.setChildElementOptionalBooleanValue(child_element, "HANDLE-NEVER-RECEIVED", com_spec.getHandleNeverReceived())
        self.setChildElementOptionalLiteral(child_element, "HANDLE-TIMEOUT-TYPE", com_spec.getHandleTimeoutType())
        self.setValueSpecification(child_element, "INIT-VALUE", com_spec.getInitValue())

    def writeQueuedReceiverComSpec(self, element: ET.Element, com_spec: QueuedReceiverComSpec):
        child_element = ET.SubElement(element, "QUEUED-RECEIVER-COM-SPEC")
        self.writeARObjectAttributes(child_element, com_spec)
        self.writeReceiverComSpec(child_element, com_spec)
        self.setChildElementOptionalNumericalValue(child_element, "QUEUE-LENGTH", com_spec.queueLength)
    
    def writeClientComSpec(self, element: ET.Element, com_spec: ClientComSpec):
        self.logger.debug("writeClientComSpec")
        child_element = ET.SubElement(element, "CLIENT-COM-SPEC")
        self.writeARObjectAttributes(child_element, com_spec)
        self.setChildElementOptionalRefType(child_element, "OPERATION-REF", com_spec.getOperationRef())

    def writeParameterRequireComSpec(self, element: ET.Element, com_spec: ParameterRequireComSpec):
        self.logger.debug("writeParameterRequireComSpec")
        child_element = ET.SubElement(element, "PARAMETER-REQUIRE-COM-SPEC")
        self.writeARObjectAttributes(child_element, com_spec)
        self.setChildElementOptionalRefType(child_element, "PARAMETER-REF", com_spec.getParameterRef())
        self.setValueSpecification(child_element, "INIT-VALUE", com_spec.getInitValue())

    def setModeSwitchReceiverComSpec(self, element: ET.Element, com_spec: ModeSwitchReceiverComSpec):
        self.logger.debug("writeModeSwitchReceiverComSpec")
        child_element = ET.SubElement(element, "MODE-SWITCH-RECEIVER-COM-SPEC")
        self.writeARObjectAttributes(child_element, com_spec)
        self.setChildElementOptionalBooleanValue(child_element, "ENHANCED-MODE-API", com_spec.getEnhancedModeApi())
        self.setChildElementOptionalRefType(child_element, "MODE-GROUP-REF", com_spec.getModeGroupRef())
        self.setChildElementOptionalBooleanValue(child_element, "SUPPORTS-ASYNCHRONOUS-MODE-SWITCH", com_spec.getSupportsAsynchronousModeSwitch())

    def writeRPortComSpec(self, element: ET.Element, com_spec: RPortComSpec):
        if isinstance(com_spec, NonqueuedReceiverComSpec):
            self.writeNonqueuedReceiverComSpec(element, com_spec)
        elif isinstance(com_spec, QueuedReceiverComSpec):
            self.writeQueuedReceiverComSpec(element, com_spec)
        elif isinstance(com_spec, ClientComSpec):
            self.writeClientComSpec(element, com_spec)
        elif isinstance(com_spec, ModeSwitchReceiverComSpec):
            self.setModeSwitchReceiverComSpec(element, com_spec)
        elif isinstance(com_spec, ParameterRequireComSpec):
            self.writeParameterRequireComSpec(element, com_spec)
        else:
            raise ValueError("Unsupported RPortComSpec %s" % type(com_spec))
        
    def setAbstractProvidedPortPrototype(self, element: ET.Element, prototype: AbstractProvidedPortPrototype):
        com_specs = prototype.getProvidedComSpecs()
        if len(com_specs):
            com_specs_tag = ET.SubElement(element, "PROVIDED-COM-SPECS")
            for com_spec in com_specs:
                self.writePPortComSpec(com_specs_tag, com_spec)
    
    def writePPortPrototype(self, ports_tag: ET.Element, prototype: PPortPrototype):
        prototype_tag = ET.SubElement(ports_tag, "P-PORT-PROTOTYPE")

        self.writeIdentifiable(prototype_tag, prototype)
        self.logger.debug("write PPortPrototype %s" % prototype.getShortName())
        self.setAbstractProvidedPortPrototype(prototype_tag, prototype)
        self.setChildElementOptionalRefType(prototype_tag, "PROVIDED-INTERFACE-TREF", prototype.getProvidedInterfaceTRef())

    def setAbstractRequiredPortPrototype(self, element: ET.Element, prototype: AbstractRequiredPortPrototype):
        com_specs = prototype.getRequiredComSpecs()
        if len(com_specs) > 0:
            com_specs_tag = ET.SubElement(element, "REQUIRED-COM-SPECS")
            for com_spec in com_specs:
                self.writeRPortComSpec(com_specs_tag, com_spec)

    def writeRPortPrototype(self, ports_tag: ET.Element, prototype: RPortPrototype):
        self.logger.debug("write RPortPrototype %s" % prototype.getShortName())
        prototype_tag = ET.SubElement(ports_tag, "R-PORT-PROTOTYPE")
        self.writeIdentifiable(prototype_tag, prototype)
        self.setAbstractRequiredPortPrototype(prototype_tag, prototype)
        self.setChildElementOptionalRefType(prototype_tag, "REQUIRED-INTERFACE-TREF", prototype.getRequiredInterfaceTRef())

    def writePRPortPrototype(self, ports_tag: ET.Element, prototype: PRPortPrototype):
        self.logger.debug("write PRPortPrototype %s" % prototype.getShortName())
        prototype_tag = ET.SubElement(ports_tag, "PR-PORT-PROTOTYPE")
        self.writeIdentifiable(prototype_tag, prototype)
        self.setAbstractProvidedPortPrototype(prototype_tag, prototype)
        self.setAbstractRequiredPortPrototype(prototype_tag, prototype)
        self.setChildElementOptionalRefType(prototype_tag, "PROVIDED-REQUIRED-INTERFACE-TREF", prototype.getProvidedRequiredInterface())

    def writeSwComponentTypePorts(self, element: ET.Element, sw_component: SwComponentType):
        ports = sw_component.getPorts()
        if len(ports) > 0:
            child_element = ET.SubElement(element, "PORTS")
            for port in ports:
                if isinstance(port, PPortPrototype):
                    self.writePPortPrototype(child_element, port)
                elif isinstance(port, RPortPrototype):
                    self.writeRPortPrototype(child_element, port)
                elif isinstance(port, PRPortPrototype):
                    self.writePRPortPrototype(child_element, port)
                else:
                    self.notImplemented("Unsupported Port Prototype <%s>" % type(port))

    def writeInnerGroupIRef(self, element: ET.Element, inner_group_iref: InnerPortGroupInCompositionInstanceRef):
        child_element = ET.SubElement(element, "INNER-GROUP-IREF")
        # self.setChildElementOptionalRefType(child_element, "CONTEXT-REF", inner_group_iref.contextRef)
        self.setChildElementOptionalRefType(child_element, "TARGET-REF", inner_group_iref.getTargetRef())

    def writePortGroupInnerGroupIRefs(self, element: ET.Element, parent: PortGroup):
        irefs = parent.getInnerGroupIRefs()
        if len(irefs) > 0:
            child_element = ET.SubElement(element, "INNER-GROUP-IREFS")
            for iref in irefs:
                self.writeInnerGroupIRef(child_element, iref)

    def writePortGroupOuterPortRefs(self, element: ET.Element, parent: PortGroup):
        refs = parent.getOuterPortRefs()
        if len(refs) > 0:
            outer_ports_element = ET.SubElement(element, "OUTER-PORTS")
            for ref in refs:
                child_element = ET.SubElement(outer_ports_element, "PORT-PROTOTYPE-REF-CONDITIONAL")
                self.setChildElementOptionalRefType(child_element, "PORT-PROTOTYPE-REF", ref)

    def writePortGroup(self, element: ET.Element, port_group: PortGroup):
        self.logger.debug("writePortGroup %s" % port_group.getShortName())
        child_element = ET.SubElement(element, "PORT-GROUP")
        self.writeIdentifiable(child_element, port_group)
        self.writePortGroupInnerGroupIRefs(child_element, port_group)
        self.writePortGroupOuterPortRefs(child_element, port_group)

    def writeSwComponentTypePortGroups(self, element: ET.Element, parent: SwComponentType):
        port_groups = parent.getPortGroups()
        if len(port_groups) > 0:
            child_element = ET.SubElement(element, "PORT-GROUPS")
            for port_group in port_groups:
                self.writePortGroup(child_element, port_group)
    
    def writeSwComponentType(self, element: ET.Element, sw_component: SwComponentType):
        self.writeIdentifiable(element, sw_component)
        self.writeSwComponentTypePorts(element, sw_component)
        self.writeSwComponentTypePortGroups(element, sw_component)

    def writeSwComponentPrototype(self, element: ET.Element, prototype: SwComponentPrototype):
        prototype_tag = ET.SubElement(element, "SW-COMPONENT-PROTOTYPE")
        self.writeIdentifiable(prototype_tag, prototype)
        self.setChildElementOptionalRefType(prototype_tag, "TYPE-TREF", prototype.getTypeTRef())

    def writeCompositionSwComponentTypeComponents(self, element: ET.Element, sw_component: CompositionSwComponentType):
        components = sw_component.getComponents()
        if len(components) > 0:
            components_tag = ET.SubElement(element, "COMPONENTS")
            for component in components:
                if isinstance(component, SwComponentPrototype):
                    self.writeSwComponentPrototype(components_tag, component)
                else:
                    self.notImplemented("Unsupported Component <%s>" % type(component))

    def writeAssemblySwConnector(self, element: ET.Element, sw_connector: AssemblySwConnector):
        child_element = ET.SubElement(element, "ASSEMBLY-SW-CONNECTOR")
        self.writeSwConnector(child_element, sw_connector)

        if sw_connector.getProviderIRef() is not None:
            provider_iref_tag = ET.SubElement(child_element, "PROVIDER-IREF")
            provider_iref = sw_connector.getProviderIRef()
            self.writeARObjectAttributes(provider_iref_tag, provider_iref)
            self.setChildElementOptionalRefType(provider_iref_tag, "CONTEXT-COMPONENT-REF", provider_iref.getContextComponentRef())
            self.setChildElementOptionalRefType(provider_iref_tag, "TARGET-P-PORT-REF", provider_iref.getTargetPPortRef())

        if sw_connector.getRequesterIRef() is not None:
            requester_iref_tag = ET.SubElement(child_element, "REQUESTER-IREF")
            requester_iref = sw_connector.getRequesterIRef()
            self.writeARObjectAttributes(requester_iref_tag, requester_iref)
            self.setChildElementOptionalRefType(requester_iref_tag, "CONTEXT-COMPONENT-REF", requester_iref.getContextComponentRef())
            self.setChildElementOptionalRefType(requester_iref_tag, "TARGET-R-PORT-REF", requester_iref.getTargetRPortRef())

    def writeDelegationSwConnector(self, element: ET.Element, sw_connector: DelegationSwConnector):
        connector_tag = ET.SubElement(element, "DELEGATION-SW-CONNECTOR")
        self.writeIdentifiable(connector_tag, sw_connector)

        if sw_connector.getInnerPortIRref() is not None:
            inner_port_iref_tag = ET.SubElement(connector_tag, "INNER-PORT-IREF")
            inner_port_iref = sw_connector.getInnerPortIRref()
            if isinstance(inner_port_iref, PPortInCompositionInstanceRef):
                instance_ref_tag = ET.SubElement(inner_port_iref_tag, "P-PORT-IN-COMPOSITION-INSTANCE-REF")
                self.setChildElementOptionalRefType(instance_ref_tag, "CONTEXT-COMPONENT-REF", inner_port_iref.getContextComponentRef())
                self.setChildElementOptionalRefType(instance_ref_tag, "TARGET-P-PORT-REF", inner_port_iref.getTargetPPortRef())
            elif isinstance(inner_port_iref, RPortInCompositionInstanceRef):
                instance_ref_tag = ET.SubElement(inner_port_iref_tag, "R-PORT-IN-COMPOSITION-INSTANCE-REF")
                self.setChildElementOptionalRefType(instance_ref_tag, "CONTEXT-COMPONENT-REF", inner_port_iref.getContextComponentRef())
                self.setChildElementOptionalRefType(instance_ref_tag, "TARGET-R-PORT-REF", inner_port_iref.getTargetRPortRef())
            else:
                self._raiseError("Invalid inner port of DelegationSwConnector <%s>" % sw_connector.getShortName())

        if sw_connector.getOuterPortRef() is not None:
            self.setChildElementOptionalRefType(connector_tag, "OUTER-PORT-REF", sw_connector.getOuterPortRef())
            # self.writeChildOptionalRefElement(requester_iref_tag, "TARGET-R-PORT-REF", sw_connector.requester_iref.target_r_port_ref)
        
    def writeSwConnector(self, element: ET.Element, sw_connector: SwConnector):
        self.writeIdentifiable(element, sw_connector)
        self.setChildElementOptionalRefType(element, "MAPPING-REF", sw_connector.getMappingRef())

    def writeCompositionSwComponentTypeSwConnectors(self, element: ET.Element, sw_component: CompositionSwComponentType):
        sw_connectors = sw_component.getSwConnectors()
        if len(sw_connectors) > 0:
            child_element = ET.SubElement(element, "CONNECTORS")
            for sw_connector in sw_connectors:
                if isinstance(sw_connector, AssemblySwConnector):
                    self.writeAssemblySwConnector(child_element, sw_connector)
                elif isinstance(sw_connector, DelegationSwConnector):
                    self.writeDelegationSwConnector(child_element, sw_connector)
                else:
                    self.notImplemented("Unsupported Sw Connector %s" % type(sw_connector))

    def writeCompositionSwComponentTypeDataTypeMappingSet(self, element: ET.Element, parent: CompositionSwComponentType):
        data_type_mappings = parent.getDataTypeMappings()
        if len(data_type_mappings) > 0:
            child_element = ET.SubElement(element, "DATA-TYPE-MAPPING-REFS")
            self.logger.debug("writeDataTypeMappingSet")
            for data_type_mapping in data_type_mappings:
                self.setChildElementOptionalRefType(child_element, "DATA-TYPE-MAPPING-REF", data_type_mapping)
    
    def writeCompositionSwComponentType(self, parent: ET.Element, sw_component: CompositionSwComponentType):
        child_element = ET.SubElement(parent, "COMPOSITION-SW-COMPONENT-TYPE")

        self.writeSwComponentType(child_element, sw_component)
        self.writeCompositionSwComponentTypeComponents(child_element, sw_component)
        self.writeCompositionSwComponentTypeSwConnectors(child_element, sw_component)
        self.writeCompositionSwComponentTypeDataTypeMappingSet(child_element, sw_component)

    def writeCompositionSwComponentTypes(self, element: ET.Element, ar_package: ARPackage):
        for sw_component in ar_package.getCompositionSwComponentTypes():
            self.writeCompositionSwComponentType(element, sw_component)

    def writeLParagraphs(self, element: ET.Element, paragraph: MultiLanguageParagraph):
        for l1 in paragraph.getL1s():
            l1_tag = ET.SubElement(element, "L-1")
            self.writeARObjectAttributes(l1_tag, l1)
            if l1.l is not None:
                l1_tag.attrib['L'] = l1.l
                l1_tag.text = l1.value
    
    def setMultiLanguageParagraphs(self, element: ET.Element, key: str, paragraphs: List[MultiLanguageParagraph]):
        for paragraph in paragraphs:
            child_element = ET.SubElement(element, key)
            self.writeARObjectAttributes(child_element, paragraph)
            self.writeLParagraphs(child_element, paragraph)
        return paragraphs
    
    def setListElement(self, element: ET.Element, key: str, list: ARList):
        if list is not None:
            child_element = ET.SubElement(element, key)
            type = list.getType()
            if type is not None:
                child_element.attrib['TYPE'] = type
            for item in list.getItems():
                self.writeDocumentationBlock(child_element, "ITEM", item)

    def setGraphic(self, element: ET.Element, key: str, graphic: Graphic):
        if graphic is not None:
            child_element = ET.SubElement(element, key)
            if graphic.getFilename() is not None:
                child_element.attrib["FILENAME"] = graphic.getFilename()
    
    def writeMlFigureLGraphics(self, element: ET.Element, figure: MlFigure):
        graphics = figure.getLGraphics()
        for graphic in graphics:
            child_element = ET.SubElement(element, "L-GRAPHIC")
            if graphic.getL() is not None:
                child_element.attrib["L"] = graphic.getL()
            self.setGraphic(child_element, "GRAPHIC", graphic.getGraphic())

    def writeDocumentViewSelectable(self, element: ET.Element, selectable: DocumentViewSelectable):
        self.writeARObjectAttributes(element, selectable)

    def writePaginateable(self, element: ET.Element, paginateable: Paginateable):
        self.writeDocumentViewSelectable(element, paginateable)
    
    def writeMlFigure(self, element: ET.Element, figure: MlFigure):
        self.writePaginateable(element, figure)
        self.writeMlFigureLGraphics(element, figure)

    def setMlFigures(self, element: ET.Element, key: str, figures: List[MlFigure]):
        for figure in figures:
            child_element = ET.SubElement(element, key)
            self.writeMlFigure(child_element, figure)

    def writeDocumentationBlock(self, element: ET.Element, key: str, block: DocumentationBlock):
        if block is not None:
            child_element = ET.SubElement(element, key)
            self.writeARObjectAttributes(child_element, block)
            self.setMultiLanguageParagraphs(child_element, "P", block.getPs())
            for list in block.getLists():
                self.setListElement(child_element, "LIST", list)
            self.setMlFigures(child_element, "FIGURE", block.getFigures())

    def writeGeneralAnnotation(self, element: ET.Element, annotation: Annotation):
        self.setMultiLongName(element, "LABEL", annotation.getLabel())
        self.setChildElementOptionalLiteral(element, "ANNOTATION-ORIGIN", annotation.getAnnotationOrigin())
        self.writeDocumentationBlock(element, "ANNOTATION-TEXT", annotation.getAnnotationText())

    def setAnnotations(self, element: ET.Element, annotations: List[Annotation]):
        if len(annotations) > 0:
            annotations_tag = ET.SubElement(element, "ANNOTATIONS")
            for annotation in annotations:
                annotation_tag = ET.SubElement(annotations_tag, "ANNOTATION")
                self.writeGeneralAnnotation(annotation_tag, annotation)

    def setSwAxisIndividual(self, element: ET.Element, props: SwAxisIndividual):
        child_element = ET.SubElement(element, "SW-AXIS-INDIVIDUAL")
        self.writeARObjectAttributes(child_element, props)
        self.setChildElementOptionalRefType(child_element, "INPUT-VARIABLE-TYPE-REF", props.getInputVariableTypeRef())
        self.setChildElementOptionalRefType(child_element, "COMPU-METHOD-REF", props.getCompuMethodRef())
        self.setChildElementOptionalNumericalValue(child_element, "SW-MAX-AXIS-POINTS", props.getSwMaxAxisPoints())
        self.setChildElementOptionalNumericalValue(child_element, "SW-MIN-AXIS-POINTS", props.getSwMinAxisPoints())
        self.setChildElementOptionalRefType(child_element, "DATA-CONSTR-REF", props.getDataConstrRef())

    def setSwAxisGrouped(self, element: ET.Element, props: SwAxisGrouped):
        child_element = ET.SubElement(element, "SW-AXIS-GROUPED")
        self.writeARObjectAttributes(child_element, props)
        self.setChildElementOptionalRefType(child_element, "SHARED-AXIS-TYPE-REF", props.sharedAxisTypeRef)

    def setSwCalprmAxis(self, element: ET.Element, axis: SwCalprmAxis):
        if axis is not None:
            child_element = ET.SubElement(element, "SW-CALPRM-AXIS")
            self.setChildElementOptionalNumericalValue(child_element, "SW-AXIS-INDEX", axis.sw_axis_index)
            self.setChildElementOptionalLiteral(child_element, "CATEGORY", axis.category)
            if axis.sw_calprm_axis_type_props is not None:
                if isinstance(axis.sw_calprm_axis_type_props, SwAxisIndividual):
                    self.setSwAxisIndividual(child_element, axis.sw_calprm_axis_type_props)
                elif isinstance(axis.sw_calprm_axis_type_props, SwAxisGrouped):
                    self.setSwAxisGrouped(child_element, axis.sw_calprm_axis_type_props)
                else:
                    self.notImplemented("Unsupported SwCalprmAxisTypeProps %s" % type(axis.sw_calprm_axis_type_props))

    def setSwCalprmAxisSet(self, element: ET.Element, key: str, set: SwCalprmAxisSet):
        axises = set.getSwCalprmAxises()
        if len(axises) > 0:
            child_element = ET.SubElement(element, key)
            for axis in axises:
                self.setSwCalprmAxis(child_element, axis)

    def setSwPointerTargetProps(self, element: ET.Element, key: str, props: SwPointerTargetProps):
        if props is not None:
            child_element = ET.SubElement(element, key)
            self.setChildElementOptionalLiteral(child_element, "TARGET-CATEGORY", props.getTargetCategory())
            self.setSwDataDefProps(child_element, "SW-DATA-DEF-PROPS", props.getSwDataDefProps())

    def setSwDataDefProps(self, element: ET.Element, key: str, props: SwDataDefProps):
        if props is not None:
            child_element = ET.SubElement(element, key)
            self.writeARObjectAttributes(child_element, props)
            sw_data_def_props_variants_tag = ET.SubElement(child_element, "SW-DATA-DEF-PROPS-VARIANTS")
            conditional_tag = ET.SubElement(sw_data_def_props_variants_tag, "SW-DATA-DEF-PROPS-CONDITIONAL")
            self.writeARObjectAttributes(conditional_tag, props.conditional)
            self.setAnnotations(conditional_tag, props.getAnnotations())
            self.setChildElementOptionalRefType(conditional_tag, "BASE-TYPE-REF", props.getBaseTypeRef())
            self.setChildElementOptionalLiteral(conditional_tag, "SW-CALIBRATION-ACCESS", props.getSwCalibrationAccess())
            self.setChildElementOptionalRefType(conditional_tag, "COMPU-METHOD-REF", props.getCompuMethodRef())
            self.setValueSpecification(conditional_tag, "INVALID-VALUE", props.getInvalidValue())
            self.setChildElementOptionalFloatValue(conditional_tag, "STEP-SIZE", props.getStepSize())
            self.setChildElementOptionalRefType(conditional_tag, "SW-ADDR-METHOD-REF", props.getSwAddrMethodRef())
            self.setChildElementOptionalRefType(conditional_tag, "DATA-CONSTR-REF", props.getDataConstrRef())
            self.setChildElementOptionalRefType(conditional_tag, "IMPLEMENTATION-DATA-TYPE-REF", props.getImplementationDataTypeRef())
            self.setSwCalprmAxisSet(conditional_tag, "SW-CALPRM-AXIS-SET", props.getSwCalprmAxisSet())
            self.setChildElementOptionalLiteral(conditional_tag, "SW-IMPL-POLICY", props.getSwImplPolicy())
            self.setChildElementOptionalNumericalValue(conditional_tag, "SW-INTENDED-RESOLUTION", props.getSwIntendedResolution())
            self.setSwPointerTargetProps(conditional_tag, "SW-POINTER-TARGET-PROPS", props.getSwPointerTargetProps())
            self.setChildElementOptionalRefType(conditional_tag, "SW-RECORD-LAYOUT-REF", props.getSwRecordLayoutRef())
            self.setChildElementOptionalRefType(conditional_tag, "VALUE-AXIS-DATA-TYPE-REF", props.getValueAxisDataTypeRef())
            self.setChildElementOptionalRefType(conditional_tag, "UNIT-REF", props.getUnitRef())

    def setApplicationDataType(self, element: ET.Element, data_type: ApplicationDataType):
        self.setAutosarDataType(element, data_type)

    def setApplicationCompositeDataType(self, element: ET.Element, data_type: ApplicationCompositeDataType):
        self.setApplicationDataType(element, data_type)

    def setAutosarDataType(self, element: ET.Element, data_type: AutosarDataType):
        self.writeARElement(element, data_type)
        self.setSwDataDefProps(element, "SW-DATA-DEF-PROPS", data_type.getSwDataDefProps())

    def writeApplicationPrimitiveDataType(self, element: ET.Element, data_type: ApplicationPrimitiveDataType):
        self.logger.debug("writeApplicationPrimitiveDataType %s" % data_type.getShortName())
        data_type_tag = ET.SubElement(element, "APPLICATION-PRIMITIVE-DATA-TYPE")
        self.setApplicationDataType(data_type_tag, data_type)

    def writeDataPrototype(self, element: ET.Element, prototype: DataPrototype):
        self.writeIdentifiable(element, prototype)
        self.setSwDataDefProps(element, "SW-DATA-DEF-PROPS", prototype.getSwDataDefProps())

    def writeApplicationCompositeElementDataPrototype(self, element: ET.Element, prototype: ApplicationCompositeElementDataPrototype):
        self.writeDataPrototype(element, prototype)
        self.setChildElementOptionalRefType(element, "TYPE-TREF", prototype.typeTRef)

    def writeApplicationRecordElement(self, element: ET.Element, prototype: ApplicationRecordElement):
        child_element = ET.SubElement(element, "APPLICATION-RECORD-ELEMENT")
        self.writeApplicationCompositeElementDataPrototype(child_element, prototype)

    def writeApplicationRecordDataTypeElements(self, element: ET.Element, data_type: ApplicationRecordDataType):
        record_elements = data_type.getApplicationRecordElements()
        if len(record_elements) > 0:
            child_element = ET.SubElement(element, "ELEMENTS")
            for record_element in record_elements:
                if isinstance(record_element, ApplicationRecordElement):
                    self.writeApplicationRecordElement(child_element, record_element)
                else:
                    self.notImplemented("Unsupported ApplicationRecordDataType Element <%s>" % type(record_element))

    def writeApplicationRecordDataType(self, element: ET.Element, data_type: ApplicationRecordDataType):
        data_type_tag = ET.SubElement(element, "APPLICATION-RECORD-DATA-TYPE")
        self.setApplicationDataType(data_type_tag, data_type)
        self.writeApplicationRecordDataTypeElements(data_type_tag, data_type)

    def writeApplicationDataTypes(self, parent: ET.Element, ar_package: ARPackage):
        for data_type in ar_package.getApplicationDataType():
            if isinstance(data_type, ApplicationPrimitiveDataType):
                self.writeApplicationPrimitiveDataType(parent, data_type)
            elif isinstance(data_type, ApplicationRecordDataType):
                self.writeApplicationRecordDataType(parent, data_type)
            else:
                self.notImplemented("Unsupported ApplicationDataType <%s>" % type(data_type))

    def setBaseTypeDirectDefinition(self, element: ET.Element, base_type_definition: BaseTypeDirectDefinition):
        self.setChildElementOptionalNumericalValue(element, "BASE-TYPE-SIZE", base_type_definition.getBaseTypeSize())
        self.setChildElementOptionalLiteral(element, "BASE-TYPE-ENCODING", base_type_definition.getBaseTypeEncoding())
        self.setChildElementOptionalLiteral(element, "BYTE-ORDER", base_type_definition.getByteOrder())
        self.setChildElementOptionalNumericalValue(element, "MEM-ALIGNMENT", base_type_definition.getMemAlignment())
        self.setChildElementOptionalLiteral(element, "NATIVE-DECLARATION", base_type_definition.getNativeDeclaration())

    def writeSwBaseType(self, element: ET.Element, base_type: SwBaseType):
        data_type_tag = ET.SubElement(element, "SW-BASE-TYPE")
        self.writeIdentifiable(data_type_tag, base_type)
        self.setBaseTypeDirectDefinition(data_type_tag, base_type.getBaseTypeDefinition())

    def writeCompuScaleConstantContents(self, element: ET.Element, contents: CompuScaleConstantContents):
        compu_const_tag = ET.SubElement(element, "COMPU-CONST")
        if isinstance(contents.compuConst.compuConstContentType, CompuConstTextContent):
            self.setChildElementOptionalLiteral(compu_const_tag, "VT", contents.compuConst.compuConstContentType.vt)

    def writeCompuNominatorDenominator(self, element: ET.Element, key: str, parent: CompuNominatorDenominator):
        child_element = ET.SubElement(element, key)
        for v in parent.get_vs():
            v_tag = ET.SubElement(child_element, "V")
            v_tag.text = v

    def writeCompuScaleRationalFormula(self, element: ET.Element, contents: CompuScaleRationalFormula):
        if contents.compuRationalCoeffs is not None:
            coeffs_tag = ET.SubElement(element, "COMPU-RATIONAL-COEFFS")
            if contents.compuRationalCoeffs.compuNumerator:
                self.writeCompuNominatorDenominator(coeffs_tag, "COMPU-NUMERATOR", contents.compuRationalCoeffs.compuNumerator)
            if contents.compuRationalCoeffs.compuDenominator:
                self.writeCompuNominatorDenominator(coeffs_tag, "COMPU-DENOMINATOR", contents.compuRationalCoeffs.compuDenominator)

    def writeCompuScaleContents(self, element: ET.Element, compu_scale: CompuScale):
        if isinstance(compu_scale.compuScaleContents, CompuScaleConstantContents):
            self.writeCompuScaleConstantContents(element, compu_scale.compuScaleContents)
        elif isinstance(compu_scale.compuScaleContents, CompuScaleRationalFormula):
            self.writeCompuScaleRationalFormula(element, compu_scale.compuScaleContents)
        else:
            self.notImplemented("Unsupported CompuScaleContents %s" % type(compu_scale.compuScaleContents))

    def setCompuConstContent(self, element: ET.Element, content: CompuConstContent):
        if content is not None:
            if isinstance(content, CompuConstFormulaContent):
                self.setChildElementOptionalLiteral(element, "VF", content.getVf())
            elif isinstance(content, CompuConstNumericContent):
                self.setChildElementOptionalNumericalValue(element, "V", content.getV())
            elif isinstance(content, CompuConstTextContent):
                self.setChildElementOptionalLiteral(element, "VT", content.getVt())
            else:
                self.notImplemented("Unsupported CompuConstContent <%s>" % type(content))

    def setCompuScale(self, element: ET.Element, key: str, compu_scale: CompuScale):
        if compu_scale is not None:
            child_element = ET.SubElement(element, key)
            self.writeARObjectAttributes(child_element, compu_scale)
            self.setChildElementOptionalLiteral(child_element, "SHORT-LABEL", compu_scale.getShortLabel())
            self.setChildElementOptionalLiteral(child_element, "SYMBOL", compu_scale.getSymbol())
            self.setMultiLanguageOverviewParagraph(child_element, "DESC", compu_scale.getDesc())
            self.setChildLimitElement(child_element, "LOWER-LIMIT", compu_scale.getLowerLimit())
            self.setChildLimitElement(child_element, "UPPER-LIMIT", compu_scale.getUpperLimit())
            self.writeCompuScaleContents(child_element, compu_scale)

    def setCompuScales(self, element: ET.Element, compu_scales: CompuScales):
        if compu_scales is not None:
            child_element = ET.SubElement(element, "COMPU-SCALES")
            for compu_scale in compu_scales.getCompuScales():
                self.setCompuScale(child_element, "COMPU-SCALE", compu_scale)

    def setCompuConst(self, element: ET.Element, key: str, compu_const: CompuConst):
        if compu_const is not None:
            child_element = ET.SubElement(element, key)
            self.writeARObjectAttributes(child_element, compu_const)
            self.setCompuConstContent(child_element, compu_const.getCompuConstContentType())

    def setCompu(self, element: ET.Element, key: str, compu: Compu):
        if compu is not None:
            child_element = ET.SubElement(element, key)
            self.writeARObjectAttributes(child_element, compu)
            self.setCompuScales(child_element, compu.getCompuContent())
            self.setCompuConst(child_element, "COMPU-DEFAULT-VALUE", compu.getCompuDefaultValue())

    def writeCompuMethod(self, element: ET.Element, compu_method: CompuMethod):
        child_element = ET.SubElement(element, "COMPU-METHOD")
        self.logger.debug("write CompuMethods %s" % compu_method.getShortName())
        self.writeIdentifiable(child_element, compu_method)
        self.setChildElementOptionalRefType(child_element, "UNIT-REF", compu_method.getUnitRef())
        self.setCompu(child_element, "COMPU-INTERNAL-TO-PHYS", compu_method.getCompuInternalToPhys())
        self.setCompu(child_element, "COMPU-PHYS-TO-INTERNAL", compu_method.getCompuPhysToInternal())

    def writeApplicationValueSpecification(self, element: ET.Element, value_spec: ApplicationValueSpecification):
        if value_spec is not None:
            child_element = ET.SubElement(element, "APPLICATION-VALUE-SPECIFICATION")
            self.writeValueSpecification(child_element, value_spec)
            self.setChildElementOptionalLiteral(child_element, "CATEGORY", value_spec.getCategory())
            self.writeSwValueCont(child_element, value_spec.getSwValueCont())

    def writeRecordValueSpecification(self, element: ET.Element, spec: RecordValueSpecification):
        child_element = ET.SubElement(element, "RECORD-VALUE-SPECIFICATION")
        self.writeARObjectAttributes(child_element, spec)
        self.setChildElementOptionalLiteral(child_element, "SHORT-LABEL", spec.getShortLabel())
        fields = spec.getFields()
        if len(fields) > 0:
            fields_tag = ET.SubElement(child_element, "FIELDS")
            for field in fields:
                if isinstance(field, ApplicationValueSpecification):
                    self.writeApplicationValueSpecification(fields_tag, field)
                elif isinstance(field, NumericalValueSpecification):
                    self.writeNumericalValueSpecification(fields_tag, field)
                elif isinstance(field, TextValueSpecification):
                    self.writeTextValueSpecification(fields_tag, field)
                elif isinstance(field, ArrayValueSpecification):
                    self.writeArrayValueSpecification(fields_tag, field)
                elif isinstance(field, RecordValueSpecification):
                    self.writeRecordValueSpecification(fields_tag, field)
                else:
                    self.notImplemented("Unsupported Field <%s>" % type(field))

    def writeConstantSpecification(self, element: ET.Element, spec: ConstantSpecification):
        spec_tag = ET.SubElement(element, "CONSTANT-SPECIFICATION")
        self.writeIdentifiable(spec_tag, spec)

        if spec.getValueSpec() is not None:
            self.setValueSpecification(spec_tag, "VALUE-SPEC", spec.getValueSpec())
                
    def setInternalConstrs(self, element: ET.Element, constrs: InternalConstrs):
        if constrs is not None:
            constrs_tag = ET.SubElement(element, "INTERNAL-CONSTRS")
            self.writeARObjectAttributes(constrs_tag, constrs)
            if constrs.lower_limit is not None:
                self.setChildLimitElement(constrs_tag, "LOWER-LIMIT", constrs.lower_limit)
            if constrs.upper_limit is not None:
                self.setChildLimitElement(constrs_tag, "UPPER-LIMIT", constrs.upper_limit)

    def setPhysConstrs(self, element: ET.Element, constrs: PhysConstrs):
        if constrs is not None:
            child_element = ET.SubElement(element, "PHYS-CONSTRS")
            self.writeARObjectAttributes(child_element, constrs)
            if constrs.lower_limit is not None:
                self.setChildLimitElement(child_element, "LOWER-LIMIT", constrs.lower_limit)
            if constrs.upper_limit is not None:
                self.setChildLimitElement(child_element, "UPPER-LIMIT", constrs.upper_limit)
            self.setChildElementOptionalRefType(child_element, "UNIT-REF", constrs.unit_ref)
                
    def writeDataConstrRules(self, element: ET.Element, parent: DataConstr):
        rules = parent.getDataConstrRules()
        if len(rules) > 0:
            rules_tag = ET.SubElement(element, "DATA-CONSTR-RULES")
            for rule in rules:
                child_element = ET.SubElement(rules_tag, "DATA-CONSTR-RULE")
                self.writeARObjectAttributes(child_element, rule)
                self.setChildElementOptionalNumericalValue(child_element, "CONSTR-LEVEL", rule.constrLevel)
                self.setPhysConstrs(child_element, rule.physConstrs)
                self.setInternalConstrs(child_element, rule.internalConstrs)

    def writeDataConstr(self, element: ET.Element, constr: DataConstr):
        child_element = ET.SubElement(element, "DATA-CONSTR")
        self.writeIdentifiable(child_element, constr)
        self.writeDataConstrRules(child_element, constr)

    def writeUnit(self, element: ET.Element, unit: Unit):
        self.logger.debug("writeUnit %s" % unit.getShortName())
        child_element = ET.SubElement(element, "UNIT")
        self.writeIdentifiable(child_element, unit)
        self.setChildElementOptionalLiteral(child_element, "DISPLAY-NAME", unit.getDisplayName())
        self.setChildElementOptionalFloatValue(child_element, "FACTOR-SI-TO-UNIT", unit.getFactorSiToUnit())
        self.setChildElementOptionalFloatValue(child_element, "OFFSET-SI-TO-UNIT", unit.getOffsetSiToUnit())
        self.setChildElementOptionalRefType(child_element, "PHYSICAL-DIMENSION-REF", unit.getPhysicalDimensionRef())

    def setRModeInAtomicSwcInstanceRef(self, element: ET.Element, key: str, iref: RModeInAtomicSwcInstanceRef):
        child_element = ET.SubElement(element, key)
        self.writeARObjectAttributes(child_element, iref)
        self.setChildElementOptionalRefType(child_element, "BASE", iref.getBaseRef())
        self.setChildElementOptionalRefType(child_element, "CONTEXT-PORT-REF", iref.getContextPortRef())
        self.setChildElementOptionalRefType(child_element, "CONTEXT-MODE-DECLARATION-GROUP-PROTOTYPE-REF", iref.getContextModeDeclarationGroupPrototypeRef())   # noqa E501
        self.setChildElementOptionalRefType(child_element, "TARGET-MODE-DECLARATION-REF", iref.getTargetModeDeclarationRef())

    def setPOperationInAtomicSwcInstanceRef(self, element: ET.Element, key: str, iref: POperationInAtomicSwcInstanceRef):
        if iref is not None:
            child_element = ET.SubElement(element, key)
            self.writeARObjectAttributes(child_element, iref)
            self.setChildElementOptionalRefType(child_element, "CONTEXT-P-PORT-REF", iref.getContextPPortRef())
            self.setChildElementOptionalRefType(child_element, "TARGET-PROVIDED-OPERATION-REF", iref.getTargetProvidedOperationRef())

    def setRTEEvent(self, element: ET.Element, event: RTEEvent):
        self.writeIdentifiable(element, event)
        irefs = event.getDisabledModeIRefs()
        if len(irefs) > 0:
            child_element = ET.SubElement(element, "DISABLED-MODE-IREFS")
            for iref in irefs:
                self.setRModeInAtomicSwcInstanceRef(child_element, "DISABLED-MODE-IREF", iref)
        self.setChildElementOptionalRefType(element, "START-ON-EVENT-REF", event.startOnEventRef)

    def writeTimingEvent(self, element: ET.Element, event: TimingEvent):
        if event is not None:
            child_element = ET.SubElement(element, "TIMING-EVENT")
            self.setRTEEvent(child_element, event)
            self.setChildElementOptionalTimeValue(child_element, "OFFSET", event.getOffset())
            self.setChildElementOptionalTimeValue(child_element, "PERIOD", event.getPeriod())

    def writeOperationInvokedEvent(self, element: ET.Element, event: OperationInvokedEvent):
        if event is not None:
            child_element = ET.SubElement(element, "OPERATION-INVOKED-EVENT")
            self.setRTEEvent(child_element, event)
            self.setPOperationInAtomicSwcInstanceRef(child_element, "OPERATION-IREF", event.operationIRef)

    def writeSwcModeSwitchEvent(self, element: ET.Element, event: SwcModeSwitchEvent):
        if event is not None:
            child_element = ET.SubElement(element, "SWC-MODE-SWITCH-EVENT")
            self.setRTEEvent(child_element, event)
            self.setChildElementOptionalLiteral(child_element, "ACTIVATION", event.activation)
            irefs = event.getModeIRefs()
            if len(irefs) > 0:
                mode_irefs_tag = ET.SubElement(child_element, "MODE-IREFS")
                for iref in irefs:
                    self.setRModeInAtomicSwcInstanceRef(mode_irefs_tag, "MODE-IREF", iref)

    def setRVariableInAtomicSwcInstanceRef(self, element: ET.Element, iref: RVariableInAtomicSwcInstanceRef):
        if iref is not None:
            child_element = ET.SubElement(element, "DATA-IREF")
            self.setChildElementOptionalRefType(child_element, "CONTEXT-R-PORT-REF", iref.getContextRPortRef())
            self.setChildElementOptionalRefType(child_element, "TARGET-DATA-ELEMENT-REF", iref.getTargetDataElementRef())

    def writeDataReceivedEvent(self, element: ET.Element, event: DataReceivedEvent):
        if event is not None:
            child_element = ET.SubElement(element, "DATA-RECEIVED-EVENT")
            self.setRTEEvent(child_element, event)
            self.setRVariableInAtomicSwcInstanceRef(child_element, event.dataIRef)

    def writeInternalTriggerOccurredEvent(self, element: ET.Element, event: DataReceivedEvent):
        pass

    def writeInitEvent(self, element: ET.Element, event: InitEvent):
        if event is not None:
            child_element = ET.SubElement(element, "INIT-EVENT")
            self.setRTEEvent(child_element, event)

    def writeAsynchronousServerCallReturnsEvent(self, element: ET.Element, event: InitEvent):
        if event is not None:
            child_element = ET.SubElement(element, "ASYNCHRONOUS-SERVER-CALL-RETURNS-EVENT")
            self.setRTEEvent(child_element, event)
            self.setChildElementOptionalRefType(child_element, "EVENT-SOURCE-REF", event.getActivationReasonRepresentationRef())

    def writeModeSwitchedAckEvent(self, element: ET.Element, event: ModeSwitchedAckEvent):
        if event is not None:
            child_element = ET.SubElement(element, "MODE-SWITCHED-ACK-EVENT")
            self.setRTEEvent(child_element, event)
            self.setChildElementOptionalRefType(child_element, "EVENT-SOURCE-REF", event.getEventSourceRef())

    def writeBackgroundEvent(self, element: ET.Element, event: BackgroundEvent):
        if event is not None:
            child_element = ET.SubElement(element, "BACKGROUND-EVENT")
            self.setRTEEvent(child_element, event)

    def writeSwcInternalBehaviorEvents(self, element: ET.Element, parent: SwcInternalBehavior):
        events = parent.getRteEvents()
        if len(events) > 0:
            child_element = ET.SubElement(element, "EVENTS")
            
            for event in events:
                if isinstance(event, TimingEvent):
                    self.writeTimingEvent(child_element, event)
                elif isinstance(event, OperationInvokedEvent):
                    self.writeOperationInvokedEvent(child_element, event)
                elif isinstance(event, SwcModeSwitchEvent):
                    self.writeSwcModeSwitchEvent(child_element, event)
                elif isinstance(event, DataReceivedEvent):
                    self.writeDataReceivedEvent(child_element, event)
                elif isinstance(event, InternalTriggerOccurredEvent):
                    self.writeInternalTriggerOccurredEvent(child_element, event)
                elif isinstance(event, InitEvent):
                    self.writeInitEvent(child_element, event)
                elif isinstance(event, AsynchronousServerCallReturnsEvent):
                    self.writeAsynchronousServerCallReturnsEvent(child_element, event)
                elif isinstance(event, ModeSwitchedAckEvent):
                    self.writeModeSwitchedAckEvent(child_element, event)
                elif isinstance(event, BackgroundEvent):
                    self.writeBackgroundEvent(child_element, event)
                else:
                    self.notImplemented("Unsupported Event <%s>" % type(event))
                
    def writeExclusiveAreas(self, element: ET.Element, behavior: InternalBehavior):
        areas = behavior.getExclusiveAreas()
        if len(areas) > 0:
            areas_tag = ET.SubElement(element, "EXCLUSIVE-AREAS")
            for area in areas:
                child_element = ET.SubElement(areas_tag, "EXCLUSIVE-AREA")
                self.writeIdentifiable(child_element, area)

    def writeDataTypeMappingRefs(self, element: ET.Element, behavior: InternalBehavior):
        refs = behavior.getDataTypeMappingRefs()
        if len(refs) > 0:
            refs_tag = ET.SubElement(element, "DATA-TYPE-MAPPING-REFS")
            for ref in refs:
                self.setChildElementOptionalRefType(refs_tag, "DATA-TYPE-MAPPING-REF", ref)

    def writeInternalBehaviorStaticMemories(self, element: ET.Element, behavior: InternalBehavior):
        memories = behavior.getStaticMemories()
        if len(memories) > 0:
            child_element = ET.SubElement(element, "STATIC-MEMORYS")
            for memory in memories:
                if isinstance(memory, VariableDataPrototype):
                    self.writeVariableDataPrototype(child_element, memory)

    def writeInternalBehavior(self, element: ET.Element, behavior: InternalBehavior):
        self.writeIdentifiable(element, behavior)
        self.writeSwcInternalBehaviorParameterDataPrototypes(element, "CONSTANT-MEMORYS", behavior.getConstantMemories())
        self.writeDataTypeMappingRefs(element, behavior)
        self.writeExclusiveAreas(element, behavior)
        self.writeInternalBehaviorStaticMemories(element, behavior)

    def setAutosarVariableRef(self, element: ET.Element, key: str, ref: AutosarVariableRef):
        if ref is not None:
            child_element = ET.SubElement(element, key)
            self.writeARObjectAttributes(child_element, ref)
            if ref.getAutosarVariableIRef() is not None:
                child_element = ET.SubElement(child_element, "AUTOSAR-VARIABLE-IREF")
                # self.setARObjectAttributes(child_element, ref)
                self.setChildElementOptionalRefType(child_element, "PORT-PROTOTYPE-REF", ref.getAutosarVariableIRef().getPortPrototypeRef())
                self.setChildElementOptionalRefType(child_element, "TARGET-DATA-PROTOTYPE-REF", ref.getAutosarVariableIRef().getTargetDataPrototypeRef())   # noqa E501
            self.setChildElementOptionalRefType(child_element, "LOCAL-VARIABLE-REF", ref.getLocalVariableRef())

    def setComponentInSystemInstanceRef(self, element: ET.Element, tag_name: str, ref: ComponentInSystemInstanceRef):
        if ref is not None:
            child_element = ET.SubElement(element, tag_name)
            self.writeARObjectAttributes(child_element, ref)
            self.setChildElementOptionalRefType(child_element, "BASE-REF", ref.getBaseRef())
            self.setChildElementOptionalRefType(child_element, "CONTEXT-COMPOSITION-REF", ref.getContextCompositionRef())
            self.setChildElementOptionalRefType(child_element, "TARGET-COMPONENT-REF", ref.getTargetComponentRef())

    def setVariableAccess(self, element: ET.Element, access: VariableAccess):
        child_element = ET.SubElement(element, "VARIABLE-ACCESS")
        self.writeIdentifiable(child_element, access)
        self.setAutosarVariableRef(child_element, "ACCESSED-VARIABLE", access.getAccessedVariableRef())

    def setAutosarParameterRef(self, element: ET.Element, key: str, parameter_ref: AutosarParameterRef):
        if parameter_ref is not None:
            child_element = ET.SubElement(element, key)
            self.setChildElementOptionalRefType(child_element, "LOCAL-PARAMETER-REF", parameter_ref.getLocalParameterRef())

    def writeParameterAccess(self, element: ET.Element, parameter_access: ParameterAccess):
        child_element = ET.SubElement(element, "PARAMETER-ACCESS")
        self.writeIdentifiable(child_element, parameter_access)
        self.setAutosarParameterRef(child_element, "ACCESSED-PARAMETER", parameter_access.getAccessedParameter())

    def writeRunnableEntityParameterAccesses(self, element: ET.Element, entity: RunnableEntity):
        parameter_accesses = entity.getParameterAccesses()
        if len(parameter_accesses) > 0:
            child_element = ET.SubElement(element, "PARAMETER-ACCESSS")
            for parameter_access in parameter_accesses:
                self.writeParameterAccess(child_element, parameter_access)
        
    def writeRunnableEntityDataReceivePointByArguments(self, element: ET.Element, entity: RunnableEntity):
        accesses = entity.getDataReceivePointByArguments()
        if len(accesses) > 0:
            child_element = ET.SubElement(element, "DATA-RECEIVE-POINT-BY-ARGUMENTS")
            for access in accesses:
                self.setVariableAccess(child_element, access)

    def writeRunnableEntityDataSendPoints(self, element: ET.Element, entity: RunnableEntity):
        points = entity.getDataSendPoints()
        if len(points) > 0:
            child_element = ET.SubElement(element, "DATA-SEND-POINTS")
            for point in points:
                self.setVariableAccess(child_element, point)

    def writeRunnableEntityDataReadAccesses(self, element: ET.Element, entity: RunnableEntity):
        accesses = entity.getDataReadAccesses()
        if len(accesses) > 0:
            child_element = ET.SubElement(element, "DATA-READ-ACCESSS")
            for access in accesses:
                self.setVariableAccess(child_element, access)

    def writeRunnableEntityDataWriteAccesses(self, element: ET.Element, entity: RunnableEntity):
        accesses = entity.getDataWriteAccesses()
        if len(accesses) > 0:
            child_element = ET.SubElement(element, "DATA-WRITE-ACCESSS")
            for access in accesses:
                self.setVariableAccess(child_element, access)

    def writeRunnableEntityReadLocalVariables(self, element: ET.Element, entity: RunnableEntity):
        variables = entity.getReadLocalVariables()
        if len(variables) > 0:
            child_element = ET.SubElement(element, "READ-LOCAL-VARIABLES")
            for access in variables:
                self.setVariableAccess(child_element, access)

    def setROperationInAtomicSwcInstanceRef(self, element: ET.Element, key: str, iref: ROperationInAtomicSwcInstanceRef):
        if iref is not None:
            child_element = ET.SubElement(element, key)
            self.writeARObjectAttributes(child_element, iref)
            self.setChildElementOptionalRefType(child_element, "CONTEXT-R-PORT-REF", iref.getContextRPortRef())
            self.setChildElementOptionalRefType(child_element, "TARGET-REQUIRED-OPERATION-REF", iref.getTargetRequiredOperationRef())
        
    def setServerCallPoint(self, element: ET.Element, call_point: ServerCallPoint):
        self.setROperationInAtomicSwcInstanceRef(element, "OPERATION-IREF", call_point.getOperationIRef())
        self.setChildElementOptionalFloatValue(element, "TIMEOUT", call_point.timeout)

    def setSynchronousServerCallPoint(self, element: ET.Element, call_point: SynchronousServerCallPoint):
        child_element = ET.SubElement(element, "SYNCHRONOUS-SERVER-CALL-POINT")
        self.writeIdentifiable(child_element, call_point)
        self.setServerCallPoint(child_element, call_point)

    def setAsynchronousServerCallPoint(self, element: ET.Element, call_point: SynchronousServerCallPoint):
        child_element = ET.SubElement(element, "ASYNCHRONOUS-SERVER-CALL-POINT")
        self.writeIdentifiable(child_element, call_point)
        self.setServerCallPoint(child_element, call_point)

    def writeRunnableEntityServerCallPoints(self, element: ET.Element, entity: RunnableEntity):
        call_points = entity.getServerCallPoints()
        if len(call_points) > 0:
            child_element = ET.SubElement(element, "SERVER-CALL-POINTS")
            for call_point in call_points:
                if isinstance(call_point, SynchronousServerCallPoint):
                    self.setSynchronousServerCallPoint(child_element, call_point)
                elif isinstance(call_point, AsynchronousServerCallPoint):
                    self.setAsynchronousServerCallPoint(child_element, call_point)
                else:
                    self.notImplemented("Unsupported ServerCallPoint type <%s>" % type(call_point))

    def writeRunnableEntityWrittenLocalVariable(self, element: ET.Element, entity: RunnableEntity):
        variables = entity.getWrittenLocalVariables()
        if len(variables) > 0:
            child_element = ET.SubElement(element, "WRITTEN-LOCAL-VARIABLES")
            for access in variables:
                self.setVariableAccess(child_element, access)

    def writeModeGroupInAtomicSwcInstanceRef(self, element: ET.Element, instance_ref: ModeGroupInAtomicSwcInstanceRef):
        self.setChildElementOptionalRefType(element, "BASE-REF", instance_ref.getBaseRef())
        self.setChildElementOptionalRefType(element, "CONTEXT-PORT-REF", instance_ref.getContextPortRef())

    def writeRModeGroupInAtomicSWCInstanceRef(self, element: ET.Element, instance_ref: RModeGroupInAtomicSWCInstanceRef):
        if instance_ref is not None:
            child_element = ET.SubElement(element, "R-MODE-GROUP-IN-ATOMIC-SWC-INSTANCE-REF")
            self.writeModeGroupInAtomicSwcInstanceRef(child_element, instance_ref)
            self.setChildElementOptionalRefType(child_element, "CONTEXT-R-PORT-REF", instance_ref.getContextRPortRef())
            self.setChildElementOptionalRefType(child_element, "TARGET-MODE-GROUP-REF", instance_ref.getTargetModeGroupRef())

    def writePModeGroupInAtomicSWCInstanceRef(self, element: ET.Element, instance_ref: PModeGroupInAtomicSwcInstanceRef):
        if instance_ref is not None:
            child_element = ET.SubElement(element, "P-MODE-GROUP-IN-ATOMIC-SWC-INSTANCE-REF")
            self.writeModeGroupInAtomicSwcInstanceRef(child_element, instance_ref)
            self.setChildElementOptionalRefType(child_element, "CONTEXT-P-PORT-REF", instance_ref.getContextPPortRef())
            self.setChildElementOptionalRefType(child_element, "TARGET-MODE-GROUP-REF", instance_ref.getTargetModeGroupRef())

    def setModeGroupIRef(self, element: ET.Element, key: str, instance_ref: ModeGroupInAtomicSwcInstanceRef):
        if instance_ref is not None:
            child_element = ET.SubElement(element, key)
            if isinstance(instance_ref, PModeGroupInAtomicSwcInstanceRef):
                self.writePModeGroupInAtomicSWCInstanceRef(child_element, instance_ref)
            elif isinstance(instance_ref, RModeGroupInAtomicSWCInstanceRef):
                self.writeRModeGroupInAtomicSWCInstanceRef(child_element, instance_ref)
            else:
                self.notImplemented("Unsupported Mode Group IRef <%s>" % type(instance_ref))
        return instance_ref

    def writeModeAccessPoint(self, element: ET.Element, point: ModeAccessPoint):
        if point is not None:
            child_element = ET.SubElement(element, "MODE-ACCESS-POINT")
            self.setModeGroupIRef(child_element, "MODE-GROUP-IREF", point.getModeGroupIRef())

    def writeRunnableEntityModeAccessPoints(self, element: ET.Element, entity: RunnableEntity):
        points = entity.getModeAccessPoints()
        if len(points) > 0:
            child_element = ET.SubElement(element, "MODE-ACCESS-POINTS")
            for point in points:
                if isinstance(point, ModeAccessPoint):
                    self.writeModeAccessPoint(child_element, point)
                else:
                    self.notImplemented("Unsupported Mode Access Points <%s>" % type(point))

    def writeModeSwitchPointModeGroupIRef(self, element: ET.Element, point: ModeSwitchPoint):
        if point is not None:
            child_element = ET.SubElement(element, "MODE-GROUP-IREF")
            instance_ref = point.getModeGroupIRef()
            self.setChildElementOptionalRefType(child_element, "CONTEXT-P-PORT-REF", instance_ref.getContextPPortRef())
            self.setChildElementOptionalRefType(child_element, "TARGET-MODE-GROUP-REF", instance_ref.getTargetModeGroupRef())

    def writeModeSwitchPoint(self, element: ET.Element, point: ModeSwitchPoint):
        if point is not None:
            child_element = ET.SubElement(element, "MODE-SWITCH-POINT")
            self.writeIdentifiable(child_element, point)
            self.writeModeSwitchPointModeGroupIRef(child_element, point)

    def writeRunnableEntityModeSwitchPoints(self, element: ET.Element, entity: RunnableEntity):
        points = entity.getModeSwitchPoints()
        if len(points) > 0:
            child_element = ET.SubElement(element, "MODE-SWITCH-POINTS")
            for point in points:
                if isinstance(point, ModeSwitchPoint):
                    self.writeModeSwitchPoint(child_element, point)
                else:
                    self.notImplemented("unsupported Mode Switch Point <%s>" % type(point))

    def setRunnableEntityArgument(self, element: ET.Element, argument: RunnableEntityArgument):
        child_element = ET.SubElement(element, "RUNNABLE-ENTITY-ARGUMENT")
        self.setChildElementOptionalLiteral(child_element, "SYMBOL", argument.getSymbol())

    def writeRunnableEntityArguments(self, element: ET.Element, entity: RunnableEntity):
        arguments = entity.getArguments()
        if len(arguments) > 0:
            child_element = ET.SubElement(element, "ARGUMENTS")
            for argument in arguments:
                if isinstance(argument, RunnableEntityArgument):
                    self.setRunnableEntityArgument(child_element, argument)
                else:
                    self.notImplemented("Unsupported argument of Runnable Entity <%s>" % type(argument))

    def writeRunnableEntityAsynchronousServerCallResultPoint(self, element: ET.Element, entity: RunnableEntity):
        points = entity.getAsynchronousServerCallResultPoints()
        if len(points) > 0:
            points_tag = ET.SubElement(element, "ASYNCHRONOUS-SERVER-CALL-RESULT-POINTS")
            for point in points:
                child_element = ET.SubElement(points_tag, "ASYNCHRONOUS-SERVER-CALL-RESULT-POINT")
                self.writeIdentifiable(child_element, point)
                self.setChildElementOptionalRefType(child_element, "ASYNCHRONOUS-SERVER-CALL-POINT-REF", point.getAsynchronousServerCallPointRef())

    def writeRunnableEntity(self, element: ET.Element, entity: RunnableEntity):
        if entity is not None:
            child_element = ET.SubElement(element, "RUNNABLE-ENTITY")
            self.writeExecutableEntity(child_element, entity)
            self.writeRunnableEntityArguments(child_element, entity)
            self.writeRunnableEntityAsynchronousServerCallResultPoint(child_element, entity)
            self.setChildElementOptionalBooleanValue(child_element, "CAN-BE-INVOKED-CONCURRENTLY", entity.getCanBeInvokedConcurrently())
            self.writeRunnableEntityDataReadAccesses(child_element, entity)
            self.writeRunnableEntityDataReceivePointByArguments(child_element, entity)
            self.writeRunnableEntityDataSendPoints(child_element, entity)
            self.writeRunnableEntityDataWriteAccesses(child_element, entity)
            self.writeRunnableEntityModeAccessPoints(child_element, entity)
            self.writeRunnableEntityModeSwitchPoints(child_element, entity)
            self.writeRunnableEntityParameterAccesses(child_element, entity)
            self.writeRunnableEntityReadLocalVariables(child_element, entity)
            self.writeRunnableEntityServerCallPoints(child_element, entity)
            self.setChildElementOptionalLiteral(child_element, "SYMBOL", entity.symbol)
            self.writeRunnableEntityWrittenLocalVariable(child_element, entity)

    def writeSwcInternalBehaviorRunnables(self, element: ET.Element, behavior: SwcInternalBehavior):
        entities = behavior.getRunnableEntities()
        if len(entities) > 0:
            runnables_tag = ET.SubElement(element, "RUNNABLES")
            for entity in entities:
                if isinstance(entity, RunnableEntity):
                    self.writeRunnableEntity(runnables_tag, entity)
                else:
                    self.notImplemented("Unsupported RunnableEntity <%s>" % type(entity))

    def writeSwcInternalBehaviorArTypedPerInstanceMemories(self, element: ET.Element, behavior: SwcInternalBehavior):
        prototypes = behavior.getArTypedPerInstanceMemories()
        if len(prototypes) > 0:
            child_element = ET.SubElement(element, "AR-TYPED-PER-INSTANCE-MEMORYS")
            for prototype in prototypes:
                if isinstance(prototype, VariableDataPrototype):
                    self.writeVariableDataPrototype(child_element, prototype)
                else:
                    self.notImplemented("Unsupported ArTypedPerInstanceMemories <%s>" % type(prototype))

    def writeSwcInternalBehaviorExplicitInterRunnableVariables(self, element: ET.Element, behavior: SwcInternalBehavior):
        prototypes = behavior.getExplicitInterRunnableVariables()
        if len(prototypes) > 0:
            child_element = ET.SubElement(element, "EXPLICIT-INTER-RUNNABLE-VARIABLES")
            for prototype in prototypes:
                if isinstance(prototype, VariableDataPrototype):
                    self.writeVariableDataPrototype(child_element, prototype)
                else:
                    self.notImplemented("Unsupported ExplicitInterRunnableVariables <%s>" % type(prototype))

    def writeSwcInternalBehaviorPerInstanceMemories(self, element: ET.Element, behavior: SwcInternalBehavior):
        memories = behavior.getPerInstanceMemories()
        if len(memories) > 0:
            memories_tag = ET.SubElement(element, "PER-INSTANCE-MEMORYS")
            for memory in memories:
                child_element = ET.SubElement(memories_tag, "PER-INSTANCE-MEMORY")
                self.writeIdentifiable(child_element, memory)
                self.setChildElementOptionalLiteral(child_element, "INIT-VALUE", memory.getInitValue())
                self.setSwDataDefProps(child_element, "SW-DATA-DEF-PROPS", memory.getSwDataDefProps())
                self.setChildElementOptionalLiteral(child_element, "TYPE", memory.getType())
                self.setChildElementOptionalLiteral(child_element, "TYPE-DEFINITION", memory.getTypeDefinition())

    def writeParameterDataPrototype(self, element: ET.Element, prototype: ParameterDataPrototype):
        child_element = ET.SubElement(element, "PARAMETER-DATA-PROTOTYPE")
        self.writeAutosarDataPrototype(child_element, prototype)
        self.setValueSpecification(child_element, "INIT-VALUE", prototype.getInitValue())

    def writeSwcInternalBehaviorParameterDataPrototypes(self, element: ET.Element, key: str, parameters: List[ParameterDataPrototype]):
        if len(parameters) > 0:
            child_element = ET.SubElement(element, key)
            for parameter in parameters:
                self.writeParameterDataPrototype(child_element, parameter)

    def writePortDefinedArgumentValues(self, element: ET.Element, argument_values: List[PortDefinedArgumentValue]):
        if len(argument_values) > 0:
            child_element = ET.SubElement(element, "PORT-ARG-VALUES")
            for argument_value in argument_values:
                child_element = ET.SubElement(child_element, "PORT-DEFINED-ARGUMENT-VALUE")
                if argument_value.getValue() is not None:
                    self.setValueSpecification(child_element, "VALUE", argument_value.getValue())
                self.setChildElementOptionalRefType(child_element, "VALUE-TYPE-TREF", argument_value.getValueTypeTRef())

    def writeSwcInternalBehaviorPortAPIOptions(self, element: ET.Element, behavior: SwcInternalBehavior):
        options = behavior.getPortAPIOptions()
        if len(options) > 0:
            port_api_options_tag = ET.SubElement(element, "PORT-API-OPTIONS")
            for option in options:
                child_element = ET.SubElement(port_api_options_tag, "PORT-API-OPTION")
                self.setChildElementOptionalBooleanValue(child_element, "ENABLE-TAKE-ADDRESS", option.getEnableTakeAddress())
                self.setChildElementOptionalLiteral(child_element, "ERROR-HANDLING", option.getErrorHandling())
                self.setChildElementOptionalBooleanValue(child_element, "INDIRECT-API", option.getIndirectAPI())
                self.writePortDefinedArgumentValues(child_element, option.getPortArgValues())
                self.setChildElementOptionalRefType(child_element, "PORT-REF", option.getPortRef())

    def writeRoleBasedDataTypeAssignment(self, element: ET.Element, assignment: RoleBasedDataTypeAssignment):
        child_element = ET.SubElement(element, "ROLE-BASED-DATA-TYPE-ASSIGNMENT")
        self.setChildElementOptionalLiteral(child_element, "ROLE", assignment.role)
        self.setChildElementOptionalRefType(child_element, "USED-IMPLEMENTATION-DATA-TYPE-REF", assignment.usedImplementationDataTypeRef)

    def writeServiceDependencyAssignedDataType(self, element: ET.Element, dependency: ServiceDependency):
        assigned_data = dependency.getAssignedDataTypes()
        if len(assigned_data) > 0:
            child_element = ET.SubElement(element, "ASSIGNED-DATA-TYPES")
            for data in assigned_data:
                if isinstance(data, RoleBasedDataTypeAssignment):
                    self.writeRoleBasedDataTypeAssignment(child_element, data)
                else:
                    self.notImplemented("Unsupported Assigned Data <%s>" % type(data))

    def writeServiceDependency(self, element: ET.Element, dependency: ServiceDependency):
        self.writeIdentifiable(element, dependency)
        self.writeServiceDependencyAssignedDataType(element, dependency)

    def writeRoleBasedDataAssignment(self, element: ET.Element, assignment: RoleBasedDataAssignment):
        child_element = ET.SubElement(element, "ROLE-BASED-DATA-ASSIGNMENT")
        self.setChildElementOptionalLiteral(child_element, "ROLE", assignment.role)
        self.setAutosarVariableRef(child_element, "USED-DATA-ELEMENT", assignment.getUsedDataElement())
        self.setAutosarParameterRef(child_element, "USED-PARAMETER-ELEMENT", assignment.getUsedParameterElement())
        self.setChildElementOptionalRefType(child_element, "USED-PIM-REF", assignment.getUsedPimRef())

    def writeRoleBasedPortAssignment(self, element: ET.Element, assignment: RoleBasedPortAssignment):
        child_element = ET.SubElement(element, "ROLE-BASED-PORT-ASSIGNMENT")
        self.setChildElementOptionalRefType(child_element, "PORT-PROTOTYPE-REF", assignment.portPrototypeRef)
        self.setChildElementOptionalLiteral(child_element, "ROLE", assignment.role)

    def writeSwcServiceDependencyAssignedData(self, element: ET.Element, dependency: SwcServiceDependency):
        assigned_data = dependency.getAssignedData()
        if len(assigned_data) > 0:
            child_element = ET.SubElement(element, "ASSIGNED-DATAS")
            for data in assigned_data:
                if isinstance(data, RoleBasedDataAssignment):
                    self.writeRoleBasedDataAssignment(child_element, data)
                else:
                    self.notImplemented("Unsupported Assigned Data <%s>" % type(data))

    def writeSwcServiceDependencyAssignedPorts(self, element: ET.Element, dependency: SwcServiceDependency):
        assigned_data = dependency.getAssignedPorts()
        if len(assigned_data) > 0:
            child_element = ET.SubElement(element, "ASSIGNED-PORTS")
            for data in assigned_data:
                if isinstance(data, RoleBasedPortAssignment):
                    self.writeRoleBasedPortAssignment(child_element, data)
                else:
                    self.notImplemented("Unsupported Assigned Data <%s>" % type(data))

    def setNvBlockNeeds(self, element: ET.Element, needs: NvBlockNeeds):
        child_element = ET.SubElement(element, "NV-BLOCK-NEEDS")
        self.logger.debug("write NvBlockNeeds %s" % needs.getShortName())
        self.writeIdentifiable(child_element, needs)
        self.setChildElementOptionalBooleanValue(child_element, "CALC-RAM-BLOCK-CRC", needs.getCalcRamBlockCrc())
        self.setChildElementOptionalBooleanValue(child_element, "CHECK-STATIC-BLOCK-ID", needs.getCheckStaticBlockId())
        self.setChildElementOptionalNumericalValue(child_element, "N-DATA-SETS", needs.getNDataSets())
        self.setChildElementOptionalNumericalValue(child_element, "N-ROM-BLOCKS", needs.getNRomBlocks())
        self.setChildElementOptionalLiteral(child_element, "RAM-BLOCK-STATUS-CONTROL", needs.getRamBlockStatusControl())
        self.setChildElementOptionalBooleanValue(child_element, "READONLY", needs.getReadonly())
        self.setChildElementOptionalLiteral(child_element, "RELIABILITY", needs.getReliability())
        self.setChildElementOptionalBooleanValue(child_element, "RESISTANT-TO-CHANGED-SW", needs.getResistantToChangedSw())
        self.setChildElementOptionalBooleanValue(child_element, "RESTORE-AT-START", needs.getRestoreAtStart())
        self.setChildElementOptionalBooleanValue(child_element, "STORE-AT-SHUTDOWN", needs.getStoreAtShutdown())
        self.setChildElementOptionalBooleanValue(child_element, "STORE-CYCLIC", needs.getStoreCyclic())
        self.setChildElementOptionalBooleanValue(child_element, "STORE-EMERGENCY", needs.getStoreEmergency())
        self.setChildElementOptionalBooleanValue(child_element, "STORE-IMMEDIATE", needs.getStoreImmediate())
        self.setChildElementOptionalBooleanValue(child_element, "USE-AUTO-VALIDATION-AT-SHUT-DOWN", needs.getUseAutoValidationAtShutDown())
        self.setChildElementOptionalBooleanValue(child_element, "USE-CRC-COMP-MECHANISM", needs.getUseCRCCompMechanism())
        self.setChildElementOptionalBooleanValue(child_element, "WRITE-ONLY-ONCE", needs.getWriteOnlyOnce())
        self.setChildElementOptionalBooleanValue(child_element, "WRITE-VERIFICATION", needs.getWriteVerification())
        self.setChildElementOptionalPositiveInteger(child_element, "WRITING-FREQUENCY", needs.getWritingFrequency())
        self.setChildElementOptionalLiteral(child_element, "WRITING-PRIORITY", needs.getWritingPriority())

    def setDiagnosticCommunicationManagerNeeds(self, element: ET.Element, needs: DiagnosticCommunicationManagerNeeds):
        child_element = ET.SubElement(element, "DIAGNOSTIC-COMMUNICATION-MANAGER-NEEDS")
        self.logger.debug("write DiagnosticCommunicationManagerNeeds %s" % needs.getShortName())
        self.writeIdentifiable(child_element, needs)
        self.setChildElementOptionalLiteral(child_element, "SERVICE-REQUEST-CALLBACK-TYPE", needs.getServiceRequestCallbackType())

    def setDiagnosticRoutineNeeds(self, element: ET.Element, needs: DiagnosticRoutineNeeds):
        child_element = ET.SubElement(element, "DIAGNOSTIC-ROUTINE-NEEDS")
        self.logger.debug("write DiagnosticRoutineNeeds %s" % needs.getShortName())
        self.writeIdentifiable(child_element, needs)
        self.setChildElementOptionalLiteral(child_element, "DIAG-ROUTINE-TYPE", needs.getDiagRoutineType())
        self.setChildElementOptionalIntegerValue(child_element, "RID-NUMBER", needs.getRidNumber())

    def setDiagnosticValueNeeds(self, element: ET.Element, needs: DiagnosticValueNeeds):
        child_element = ET.SubElement(element, "DIAGNOSTIC-VALUE-NEEDS")
        self.logger.debug("write DiagnosticValueNeeds %s" % needs.getShortName())
        self.writeIdentifiable(child_element, needs)
        self.setChildElementOptionalPositiveInteger(child_element, "DATA-LENGTH", needs.getDataLength())
        self.setChildElementOptionalLiteral(child_element, "DIAGNOSTIC-VALUE-ACCESS", needs.getDiagnosticValueAccess())
        self.setChildElementOptionalIntegerValue(child_element, "DID-NUMBER", needs.getDidNumber())
        self.setChildElementOptionalBooleanValue(child_element, "FIXED-LENGTH", needs.getFixedLength())
        self.setChildElementOptionalLiteral(child_element, "PROCESSING-STYLE", needs.getProcessingStyle())

    def setDiagEventDebounceMonitorInternal(self, element: ET.Element, algorithm: DiagEventDebounceMonitorInternal):
        child_element = ET.SubElement(element, "DIAG-EVENT-DEBOUNCE-MONITOR-INTERNAL")
        self.writeIdentifiable(child_element, algorithm)

    def writeDiagEventDebounceAlgorithm(self, element: ET.Element, needs: DiagnosticEventNeeds):
        algorithm = needs.getDiagEventDebounceAlgorithm()
        if algorithm is not None:
            child_element = ET.SubElement(element, "DIAG-EVENT-DEBOUNCE-ALGORITHM")
            if isinstance(algorithm, DiagEventDebounceMonitorInternal):
                self.setDiagEventDebounceMonitorInternal(child_element, algorithm)
            else:
                self.notImplemented("Unsupported DiagEventDebounceAlgorithm <%s>" % type(algorithm))

    def setDiagnosticEventNeeds(self, element: ET.Element, needs: DiagnosticEventNeeds):
        child_element = ET.SubElement(element, "DIAGNOSTIC-EVENT-NEEDS")
        self.logger.debug("write DiagnosticEventNeeds %s" % needs.getShortName())
        self.writeIdentifiable(child_element, needs)
        self.writeDiagEventDebounceAlgorithm(child_element, needs)
        self.setChildElementOptionalLiteral(child_element, "DTC-KIND", needs.getDtcKind())
        self.setChildElementOptionalIntegerValue(child_element, "UDS-DTC-NUMBER", needs.getUdsDtcNumber())

    def setDiagnosticEventInfoNeeds(self, element: ET.Element, needs: DiagnosticEventInfoNeeds):
        child_element = ET.SubElement(element, "DIAGNOSTIC-EVENT-INFO-NEEDS")
        self.logger.debug("write DiagnosticEventNeeds %s" % needs.getShortName())
        self.writeIdentifiable(child_element, needs)
        self.setChildElementOptionalPositiveInteger(child_element, "UDS-DTC-NUMBER", needs.getUdsDtcNumber())

    def setCryptoServiceNeeds(self, element: ET.Element, needs: CryptoServiceNeeds):
        child_element = ET.SubElement(element, "CRYPTO-SERVICE-NEEDS")
        self.logger.debug("write CryptoServiceNeeds %s" % needs.getShortName())
        self.writeIdentifiable(child_element, needs)
        self.setChildElementOptionalPositiveInteger(child_element, "MAXIMUM-KEY-LENGTH", needs.getMaximumKeyLength())

    def setEcuStateMgrUserNeeds(self, element: ET.Element, needs: EcuStateMgrUserNeeds):
        child_element = ET.SubElement(element, "ECU-STATE-MGR-USER-NEEDS")
        self.logger.debug("write EcuStateMgrUserNeeds %s" % needs.getShortName())
        self.writeIdentifiable(child_element, needs)

    def writeSwcServiceDependencyServiceNeeds(self, element: ET.Element, parent: SwcServiceDependency):
        needs = parent.getServiceNeeds()
        if len(needs) > 0:
            child_element = ET.SubElement(element, "SERVICE-NEEDS")
            for need in needs:
                if isinstance(need, NvBlockNeeds):
                    self.setNvBlockNeeds(child_element, need)
                elif isinstance(need, DiagnosticCommunicationManagerNeeds):
                    self.setDiagnosticCommunicationManagerNeeds(child_element, need)
                elif isinstance(need, DiagnosticRoutineNeeds):
                    self.setDiagnosticRoutineNeeds(child_element, need)
                elif isinstance(need, DiagnosticValueNeeds):
                    self.setDiagnosticValueNeeds(child_element, need)
                elif isinstance(need, DiagnosticEventNeeds):
                    self.setDiagnosticEventNeeds(child_element, need)
                elif isinstance(need, DiagnosticEventInfoNeeds):
                    self.setDiagnosticEventInfoNeeds(child_element, need)
                elif isinstance(need, CryptoServiceNeeds):
                    self.setCryptoServiceNeeds(child_element, need)
                elif isinstance(need, EcuStateMgrUserNeeds):
                    self.setEcuStateMgrUserNeeds(child_element, need)
                else:
                    self.notImplemented("Unsupported service needs <%s>" % type(need))

    def writeSwcServiceDependency(self, element: ET.Element, dependency: SwcServiceDependency):
        child_element = ET.SubElement(element, "SWC-SERVICE-DEPENDENCY")
        self.writeServiceDependency(child_element, dependency)
        self.writeSwcServiceDependencyAssignedData(child_element, dependency)
        self.writeSwcServiceDependencyAssignedPorts(child_element, dependency)
        self.writeSwcServiceDependencyServiceNeeds(child_element, dependency)

    def writeSwcInternalBehaviorServiceDependencies(self, element: ET.Element, behavior: SwcInternalBehavior):
        dependencies = behavior.getSwcServiceDependencies()
        if len(dependencies) > 0:
            child_element = ET.SubElement(element, "SERVICE-DEPENDENCYS")
            for dependency in dependencies:
                if isinstance(dependency, SwcServiceDependency):
                    self.writeSwcServiceDependency(child_element, dependency)
                else:
                    self.notImplemented("Unsupported ServiceDependency <%s>" % type(dependency))

    def setIncludedDataTypeSets(self, element: ET.Element, sets: List[IncludedDataTypeSet]):
        if len(sets) > 0:
            include_data_type_sets_tag = ET.SubElement(element, "INCLUDED-DATA-TYPE-SETS")
            for set in sets:
                child_element = ET.SubElement(include_data_type_sets_tag, "INCLUDED-DATA-TYPE-SET")
                self.writeARObjectAttributes(child_element, set)
                type_refs = set.getDataTypeRefs()
                if len(type_refs) > 0:
                    data_type_refs_tag = ET.SubElement(child_element, "DATA-TYPE-REFS")
                    for type_ref in type_refs:
                        self.setChildElementOptionalRefType(data_type_refs_tag, "DATA-TYPE-REF", type_ref)

    def writeIncludedModeDeclarationGroupSet(self, element: ET.Element, set: IncludedModeDeclarationGroupSet):
        if set is not None:
            child_element = ET.SubElement(element, "INCLUDED-MODE-DECLARATION-GROUP-SET")
            refs = set.getModeDeclarationGroupRefs()
            if len(refs) > 0:
                refs_tag = ET.SubElement(child_element, "MODE-DECLARATION-GROUP-REFS")
                for ref in refs:
                    self.setChildElementOptionalRefType(refs_tag, "MODE-DECLARATION-GROUP-REF", ref)
            self.setChildElementOptionalLiteral(child_element, "PREFIX", set.getPrefix())

    def writeSwcInternalBehaviorIncludedModeDeclarationGroupSets(self, element: ET.Element, behavior: SwcInternalBehavior):
        group_sets = behavior.getIncludedModeDeclarationGroupSets()
        if len(group_sets) > 0:
            child_element = ET.SubElement(element, "INCLUDED-MODE-DECLARATION-GROUP-SETS")
            for group_set in group_sets:
                if isinstance(group_set, IncludedModeDeclarationGroupSet):
                    self.writeIncludedModeDeclarationGroupSet(child_element, group_set)
                else:
                    self.notImplemented("Unsupported IncludedModeDeclarationGroupSet <%s>" % type(group_set))

    def writeSwcInternalBehavior(self, element: ET.Element, behavior: SwcInternalBehavior):
        self.logger.debug("writeSwInternalBehavior %s" % behavior.getShortName())
        child_element = ET.SubElement(element, "SWC-INTERNAL-BEHAVIOR")
        self.writeInternalBehavior(child_element, behavior)

        self.writeSwcInternalBehaviorArTypedPerInstanceMemories(child_element, behavior)
        self.writeSwcInternalBehaviorEvents(child_element, behavior)
        self.writeSwcInternalBehaviorExplicitInterRunnableVariables(child_element, behavior)
        self.setChildElementOptionalLiteral(child_element, "HANDLE-TERMINATION-AND-RESTART", behavior.getHandleTerminationAndRestart())
        self.setIncludedDataTypeSets(child_element, behavior.getIncludedDataTypeSets())
        self.writeSwcInternalBehaviorIncludedModeDeclarationGroupSets(child_element, behavior)
        self.writeSwcInternalBehaviorPerInstanceMemories(child_element, behavior)
        self.writeSwcInternalBehaviorParameterDataPrototypes(child_element, "PER-INSTANCE-PARAMETERS", behavior.getPerInstanceParameters())
        self.writeSwcInternalBehaviorPortAPIOptions(child_element, behavior)
        self.writeSwcInternalBehaviorRunnables(child_element, behavior)
        self.writeSwcInternalBehaviorServiceDependencies(child_element, behavior)
        self.writeSwcInternalBehaviorParameterDataPrototypes(child_element, "SHARED-PARAMETERS", behavior.getSharedParameters())
        self.setChildElementOptionalBooleanValue(child_element, "SUPPORTS-MULTIPLE-INSTANTIATION", behavior.getSupportsMultipleInstantiation())

    def writeAtomicSwComponentTypeInternalBehaviors(self, element: ET.Element, behavior: InternalBehavior):
        if behavior is not None:
            behaviors_tag = ET.SubElement(element, "INTERNAL-BEHAVIORS")
            if isinstance(behavior, SwcInternalBehavior):
                self.writeSwcInternalBehavior(behaviors_tag, behavior)
            else:
                self.notImplemented("Unsupported Internal Behaviors <%s>" % type(behavior))

    def writeAtomicSwComponentType(self, element: ET.Element, sw_component: AtomicSwComponentType):
        self.writeSwComponentType(element, sw_component)
        self.writeAtomicSwComponentTypeInternalBehaviors(element, sw_component.getInternalBehavior())

    def writeComplexDeviceDriverSwComponentType(self, element: ET.Element, sw_component: ComplexDeviceDriverSwComponentType):
        self.logger.debug("writeComplexDeviceDriverSwComponentType %s" % sw_component.getShortName())
        child_element = ET.SubElement(element, "COMPLEX-DEVICE-DRIVER-SW-COMPONENT-TYPE")
        self.writeAtomicSwComponentType(child_element, sw_component)

    def writeArtifactDescriptors(self, element: ET.Element, code_desc: Code):
        artifact_descriptors = code_desc.getArtifactDescriptors()
        if len(artifact_descriptors) > 0:
            artifact_descs_tag = ET.SubElement(element, "ARTIFACT-DESCRIPTORS")
            for artifact_desc in artifact_descriptors:
                artifact_desc_tag = ET.SubElement(artifact_descs_tag, "AUTOSAR-ENGINEERING-OBJECT")
                self.logger.debug("writeArtifactDescriptor %s", artifact_desc.short_label)
                self.writeARObjectAttributes(artifact_desc_tag, artifact_desc)
                self.setChildElementOptionalLiteral(artifact_desc_tag, "SHORT-LABEL", artifact_desc.short_label)
                self.setChildElementOptionalLiteral(artifact_desc_tag, "CATEGORY", artifact_desc.category)

    def writeCode(self, element: ET.SubElement, code_desc: Code):
        # self.logger.debug("Write Code %s" % code_desc.getShortName())
        child_element = ET.SubElement(element, "CODE")
        self.writeIdentifiable(child_element, code_desc)
        self.writeArtifactDescriptor(child_element, code_desc)

    def writeCodeDescriptors(self, element: ET.Element, impl: Implementation):
        descs = impl.getCodeDescriptors()
        if len(descs) > 0:
            child_element = ET.SubElement(element, "CODE-DESCRIPTORS")
            for desc in descs:
                if isinstance(desc, Code):
                    self.writeCode(child_element, desc)
                else:
                    self.notImplemented("Unsupported Code Descriptor <%s>" % type(desc))

    def setMemorySectionOptions(self, element: ET.Element, options: List[ARLiteral]):
        if len(options) > 0:
            child_element = ET.SubElement(element, "OPTIONS")
            for option in options:
                self.setChildElementOptionalLiteral(child_element, "OPTION", option)
            
    def writeMemorySections(self, element: ET.Element, consumption: ResourceConsumption):
        memory_sections = consumption.getMemorySections()
        if len(memory_sections) > 0:
            sections_tag = ET.SubElement(element, "MEMORY-SECTIONS")
            for memory_section in memory_sections:
                child_element = ET.SubElement(sections_tag, "MEMORY-SECTION")
                self.writeIdentifiable(child_element, memory_section)
                self.setChildElementOptionalLiteral(child_element, "ALIGNMENT", memory_section.getAlignment())
                self.setChildElementOptionalLiteral(child_element, "MEM-CLASS-SYMBOL", memory_section.getMemClassSymbol())
                self.setMemorySectionOptions(child_element, memory_section.getOptions())
                self.setChildElementOptionalNumericalValue(child_element, "SIZE", memory_section.getSize())
                self.setChildElementOptionalRefType(child_element, "SW-ADDRMETHOD-REF", memory_section.getSwAddrMethodRef())
                self.setChildElementOptionalLiteral(child_element, "SYMBOL", memory_section.getSymbol())
                self.logger.debug("Write MemorySection %s" % memory_section.getShortName())

    def setStackUsage(self, element: ET.Element, usage: StackUsage):
        self.logger.debug("Write StackUsage %s" % usage.getShortName())
        self.writeIdentifiable(element, usage)

    def setRoughEstimateStackUsage(self, element: ET.Element, usage: RoughEstimateStackUsage):
        if usage is not None:
            child_element = ET.SubElement(element, "ROUGH-ESTIMATE-STACK-USAGE")
            self.setStackUsage(child_element, usage)
            self.setChildElementOptionalPositiveInteger(child_element, "MEMORY-CONSUMPTION", usage.getMemoryConsumption())

    def writeStackUsages(self, element: ET.Element, usages: List[StackUsage]):
        if len(usages) > 0:
            child_element = ET.SubElement(element, "STACK-USAGES")
            for usage in usages:
                if isinstance(usage, RoughEstimateStackUsage):
                    self.setRoughEstimateStackUsage(child_element, usage)
                else:
                    self.notImplemented("Unsupported Stack Usages: <%s>" % type(usage))

    def setResourceConsumption(self, element: ET.Element, consumption: ResourceConsumption):
        if consumption is not None:
            child_element = ET.SubElement(element, "RESOURCE-CONSUMPTION")
            self.writeIdentifiable(child_element, consumption)
            self.writeMemorySections(child_element, consumption)
            self.writeStackUsages(child_element, consumption.getStackUsages())

    def writeImplementation(self, element: ET.Element, impl: Implementation):
        self.writeIdentifiable(element, impl)
        self.writeCodeDescriptors(element, impl)
        self.setChildElementOptionalLiteral(element, "PROGRAMMING-LANGUAGE", impl.getProgrammingLanguage())
        self.setResourceConsumption(element, impl.getResourceConsumption())
        self.setChildElementOptionalLiteral(element, "SW-VERSION", impl.getSwVersion())
        self.setChildElementOptionalRefType(element, "SWC-BSW-MAPPING-REF", impl.getSwcBswMappingRef())
        self.setChildElementOptionalLiteral(element, "USED-CODE-GENERATOR", impl.getUsedCodeGenerator())
        self.setChildElementOptionalNumericalValue(element, "VENDOR-ID", impl.getVendorId())

    def writeSwcImplementation(self, element: ET.Element, impl: SwcImplementation):
        self.logger.debug("writeSwcImplementation %s" % impl.getShortName())
        child_element = ET.SubElement(element, "SWC-IMPLEMENTATION")
        self.writeImplementation(child_element, impl)
        self.setChildElementOptionalRefType(child_element, "BEHAVIOR-REF", impl.getBehaviorRef())

    def writeEndToEndDescriptionDataIds(self, element: ET.Element, parent: EndToEndDescription):
        data_ids = parent.getDataIds()
        if len(data_ids) > 0:
            child_element = ET.SubElement(element, "DATA-IDS")
            for data_id in data_ids:
                self.setChildElementOptionalNumericalValue(child_element, "DATA-ID", data_id)
    
    def setEndToEndDescription(self, element: ET.Element, key: str, desc: EndToEndDescription):
        if desc is not None:
            child_element = ET.SubElement(element, key)
            self.writeARObjectAttributes(child_element, desc)
            self.setChildElementOptionalLiteral(child_element, "CATEGORY", desc.getCategory())
            self.writeEndToEndDescriptionDataIds(child_element, desc)
            self.setChildElementOptionalPositiveInteger(child_element, "DATA-ID-MODE", desc.getDataIdMode())
            self.setChildElementOptionalPositiveInteger(child_element, "DATA-LENGTH", desc.getDataLength())
            self.setChildElementOptionalPositiveInteger(child_element, "MAX-DELTA-COUNTER-INIT", desc.getMaxDeltaCounterInit())
            self.setChildElementOptionalPositiveInteger(child_element, "CRC-OFFSET", desc.getCrcOffset())
            self.setChildElementOptionalPositiveInteger(child_element, "COUNTER-OFFSET", desc.getCounterOffset())

    def setVariableDataPrototypeInSystemInstanceRef(self, element: ET.Element, key: str, instance_ref: VariableDataPrototypeInSystemInstanceRef):
        if instance_ref is not None:
            child_element = ET.SubElement(element, key)
            for ref in instance_ref.getContextComponentRefs():
                self.setChildElementOptionalRefType(child_element, "CONTEXT-COMPONENT-REF", ref)
            self.setChildElementOptionalRefType(child_element, "CONTEXT-COMPOSITION-REF", instance_ref.getContextCompositionRef())
            self.setChildElementOptionalRefType(child_element, "CONTEXT-PORT-REF", instance_ref.getContextPortRef())
            self.setChildElementOptionalRefType(child_element, "TARGET-DATA-PROTOTYPE-REF", instance_ref.getTargetDataPrototypeRef())

    def writeEndToEndProtectionVariablePrototype(self, element: ET.Element, prototype: EndToEndProtectionVariablePrototype):
        if prototype is not None:
            child_element = ET.SubElement(element, "END-TO-END-PROTECTION-VARIABLE-PROTOTYPE")
            self.writeARObjectAttributes(child_element, prototype)
            irefs = prototype.getReceiverIrefs()
            if len(irefs) > 0:
                child_element = ET.SubElement(child_element, "RECEIVER-IREFS")
                for iref in irefs:
                    self.setVariableDataPrototypeInSystemInstanceRef(child_element, "RECEIVER-IREF", iref)
            self.setVariableDataPrototypeInSystemInstanceRef(child_element, "SENDER-IREF", prototype.senderIRef)

    def writeEndToEndProtectionEndToEndProtectionVariablePrototypes(self, element: ET.Element, protection: EndToEndProtection):
        prototypes = protection.getEndToEndProtectionVariablePrototypes()
        if len(prototypes) > 0:
            child_element = ET.SubElement(element, "END-TO-END-PROTECTION-VARIABLE-PROTOTYPES")
            for prototype in prototypes:
                if isinstance(prototype, EndToEndProtectionVariablePrototype):
                    self.writeEndToEndProtectionVariablePrototype(child_element, prototype)
                else:
                    self.notImplemented("Unsupported End To End Protection Variable Prototype <%s>" % type(prototype))

    def writeEndToEndProtectionISignalIPdu(self, element: ET.Element, ipdu: EndToEndProtectionISignalIPdu):
        if ipdu is not None:
            child_element = ET.SubElement(element, "END-TO-END-PROTECTION-I-SIGNAL-I-PDU")
            self.setChildElementOptionalIntegerValue(child_element, "DATA-OFFSET", ipdu.getDataOffset())
            self.setChildElementOptionalRefType(child_element, "I-SIGNAL-GROUP-REF", ipdu.getISignalGroupRef())
            self.setChildElementOptionalRefType(child_element, "I-SIGNAL-I-PDU-REF", ipdu.getISignalIPduRef())

    def writeEndToEndProtectionEndToEndProtectionISignalIPdus(self, element: ET.Element, protection: EndToEndProtection):
        ipdus = protection.getEndToEndProtectionISignalIPdus()
        if len(ipdus) > 0:
            child_element = ET.SubElement(element, "END-TO-END-PROTECTION-I-SIGNAL-I-PDUS")
            for ipdu in ipdus:
                if isinstance(ipdu, EndToEndProtectionISignalIPdu):
                    self.writeEndToEndProtectionISignalIPdu(child_element, ipdu)
                else:
                    self.notImplemented("Unsupported EndToEndProtectionISignalIPdu <%s>" % type(ipdu))

    def writeEndToEndProtection(self, element: ET.Element, protection: EndToEndProtection):
        if protection is not None:
            child_element = ET.SubElement(element, "END-TO-END-PROTECTION")
            self.writeIdentifiable(child_element, protection)
            self.setEndToEndDescription(child_element, "END-TO-END-PROFILE", protection.getEndToEndProfile())
            self.writeEndToEndProtectionEndToEndProtectionISignalIPdus(child_element, protection)
            self.writeEndToEndProtectionEndToEndProtectionVariablePrototypes(child_element, protection)

    def writeEndToEndProtections(self, element: ET.Element, protection_set: EndToEndProtectionSet):
        protections = protection_set.getEndToEndProtections()
        if len(protections) > 0:
            child_element = ET.SubElement(element, "END-TO-END-PROTECTIONS")
            for protection in protections:
                if isinstance(protection, EndToEndProtection):
                    self.writeEndToEndProtection(child_element, protection)

    def writeEndToEndProtectionSet(self, element: ET.Element, protection_set: EndToEndProtectionSet):
        self.logger.debug("writeEndToEndProtectionSet %s" % protection_set.getShortName())
        child_element = ET.SubElement(element, "END-TO-END-PROTECTION-SET")
        self.writeIdentifiable(child_element, protection_set)
        self.writeEndToEndProtections(child_element, protection_set)

    def writeAutosarDataPrototype(self, element: ET.Element, prototype: AutosarDataPrototype):
        self.writeDataPrototype(element, prototype)
        self.setChildElementOptionalRefType(element, "TYPE-TREF", prototype.typeTRef)

    def writeVariableDataPrototype(self, element: ET.Element, prototype: VariableDataPrototype):
        self.logger.debug("writeVariableDataPrototype %s" % prototype.getShortName())
        child_element = ET.SubElement(element, "VARIABLE-DATA-PROTOTYPE")
        self.writeAutosarDataPrototype(child_element, prototype)
        self.setValueSpecification(child_element, "INIT-VALUE", prototype.getInitValue())

    def writeSenderReceiverInterfaceDataElements(self, element: ET.Element, sr_interface: SenderReceiverInterface):
        data_elements = sr_interface.getDataElements()
        if len(data_elements) > 0:
            data_elements_tag = ET.SubElement(element, "DATA-ELEMENTS")
            for data_element in data_elements:
                if isinstance(data_element, VariableDataPrototype):
                    self.writeVariableDataPrototype(data_elements_tag, data_element)
                else:
                    self.notImplemented("Unsupported Data Element <%s>" % type(data_element))

    def writeSenderReceiverInterfaceInvalidationPolicies(self, element: ET.Element, sr_interface: SenderReceiverInterface):
        policies = sr_interface.getInvalidationPolicies()
        if len(policies) > 0:
            policies_tag = ET.SubElement(element, "INVALIDATION-POLICYS")
            for policy in policies:
                child_element = ET.SubElement(policies_tag, "INVALIDATION-POLICY")
                self.setChildElementOptionalRefType(child_element, "DATA-ELEMENT-REF", policy.getDataElementRef())
                self.setChildElementOptionalLiteral(child_element, "HANDLE-INVALID", policy.getHandleInvalid())

    def writeSenderReceiverInterface(self, element: ET.Element, sr_interface: SenderReceiverInterface):
        self.logger.debug("writeSenderReceiverInterface %s" % sr_interface.getShortName())
        child_element = ET.SubElement(element, "SENDER-RECEIVER-INTERFACE")
        self.writeIdentifiable(child_element, sr_interface)
        self.setChildElementOptionalBooleanValue(child_element, "IS-SERVICE", sr_interface.getIsService())
        self.writeSenderReceiverInterfaceDataElements(child_element, sr_interface)
        self.writeSenderReceiverInterfaceInvalidationPolicies(child_element, sr_interface)

    def writeBswModuleDescriptionImplementedEntryRefs(self, element: ET.Element, desc: BswModuleDescription):
        refs = desc.getImplementedEntryRefs()
        if len(refs) > 0:
            entries_tag = ET.SubElement(element, "PROVIDED-ENTRYS")
            for ref in refs:
                entry_tag = ET.SubElement(entries_tag, "BSW-MODULE-ENTRY-REF-CONDITIONAL")
                self.setChildElementOptionalRefType(entry_tag, "BSW-MODULE-ENTRY-REF", ref)

    def writeModeDeclarationGroupPrototype(self, element: ET.Element, prototype: ModeDeclarationGroupPrototype):
        child_element = ET.SubElement(element, "MODE-DECLARATION-GROUP-PROTOTYPE")
        self.writeIdentifiable(child_element, prototype)
        self.setChildElementOptionalRefType(child_element, "TYPE-TREF", prototype.getTypeTRef())

    def writeBswModuleDescriptionProvidedModeGroups(self, element: ET.Element, parent: BswModuleDescription):
        mode_groups = parent.getProvidedModeGroups()
        if len(mode_groups) > 0:
            child_element = ET.SubElement(element, "PROVIDED-MODE-GROUPS")
            for mode_group in mode_groups:
                if isinstance(mode_group, ModeDeclarationGroupPrototype):
                    self.writeModeDeclarationGroupPrototype(child_element, mode_group)
                else:
                    self.notImplemented("Unsupported ProvidedModeGroup <%s>" % type(mode_group))

    def writeBswModuleDescriptionRequiredModeGroups(self, element: ET.Element, desc: BswModuleDescription):
        mode_groups = desc.getRequiredModeGroups()
        if len(mode_groups) > 0:
            child_element = ET.SubElement(element, "REQUIRED-MODE-GROUPS")
            for mode_group in mode_groups:
                if isinstance(mode_group, ModeDeclarationGroupPrototype):
                    self.writeModeDeclarationGroupPrototype(child_element, mode_group)
                else:
                    self.notImplemented("Unsupported ProvidedModeGroup <%s>" % type(mode_group))

    def writeCanEnterExclusiveAreaRefs(self, element: ET.Element, entity: ExecutableEntity):
        refs = entity.getCanEnterExclusiveAreaRefs()
        if len(refs) > 0:
            child_element = ET.SubElement(element, "CAN-ENTER-EXCLUSIVE-AREA-REFS")
            for ref in refs:
                self.setChildElementOptionalRefType(child_element, "CAN-ENTER-EXCLUSIVE-AREA-REF", ref)

    def writeExecutableEntity(self, element: ET.Element, entity: ExecutableEntity):
        self.writeIdentifiable(element, entity)
        self.writeCanEnterExclusiveAreaRefs(element, entity)
        self.setChildElementOptionalFloatValue(element, "MINIMUM-START-INTERVAL", entity.getMinimumStartInterval())
        self.setChildElementOptionalRefType(element, "SW-ADDR-METHOD-REF", entity.getSwAddrMethodRef())

    def writeBswModuleEntityManagedModeGroups(self, element: ET.Element, entity: BswModuleEntity):
        mode_group_refs = entity.getManagedModeGroupRefs()
        if len(mode_group_refs) > 0:
            mode_groups_tag = ET.SubElement(element, "MANAGED-MODE-GROUPS")
            for mode_group_ref in mode_group_refs:
                child_element = ET.SubElement(mode_groups_tag, "MODE-DECLARATION-GROUP-PROTOTYPE-REF-CONDITIONAL")
                self.setChildElementOptionalRefType(child_element, "MODE-DECLARATION-GROUP-PROTOTYPE-REF", mode_group_ref)

    def writeBswVariableAccess(self, element: ET.Element, access: BswVariableAccess):
        if access is not None:
            child_element = ET.SubElement(element, "BSW-VARIABLE-ACCESS")
            self.writeReferrable(child_element, access)
            self.setChildElementOptionalRefType(child_element, "ACCESSED-VARIABLE-REF", access.getAccessedVariableRef())
    
    def writeBswModuleEntityDataSendPoints(self, element: ET.Element, entity: BswModuleEntity):
        points = entity.getDataSendPoints()
        if len(points) > 0:
            child_element = ET.SubElement(element, "DATA-SEND-POINTS")
            for point in points:
                if isinstance(point, BswVariableAccess):
                    self.writeBswVariableAccess(child_element, point)
                else:
                    self.notImplemented("Unsupported Data Send Point <%s>" % type(point))

    def writeBswModuleEntityDataReceivePoints(self, element: ET.Element, entity: BswModuleEntity):
        points = entity.getDataReceivePoints()
        if len(points) > 0:
            child_element = ET.SubElement(element, "DATA-RECEIVE-POINTS")
            for point in points:
                if isinstance(point, BswVariableAccess):
                    self.writeBswVariableAccess(child_element, point)
                else:
                    self.notImplemented("Unsupported Data Receive Point <%s>" % type(point))

    def writeBswModuleEntityIssuedTriggerRefs(self, element: ET.Element, entity: BswModuleEntity):
        refs = entity.getIssuedTriggerRefs()
        if len(refs) > 0:
            child_element = ET.SubElement(element, "ISSUED-TRIGGERS")
            for ref in refs:
                cond_tag = ET.SubElement(child_element, "TRIGGER-REF-CONDITIONAL")
                self.setChildElementOptionalRefType(cond_tag, "TRIGGER-REF", ref)

    def writeBswModuleEntityActivationPointRefs(self, element: ET.Element, entity: BswModuleEntity):
        refs = entity.getActivationPointRefs()
        if len(refs) > 0:
            child_element = ET.SubElement(element, "ACTIVATION-POINTS")
            for ref in refs:
                cond_tag = ET.SubElement(child_element, "BSW-INTERNAL-TRIGGERING-POINT-REF-CONDITIONAL")
                self.setChildElementOptionalRefType(cond_tag, "BSW-INTERNAL-TRIGGERING-POINT-REF", ref)

    def writeBswModuleCallPoint(self, element: ET.Element, point: BswModuleCallPoint):
        self.writeReferrable(element, point)

    def writeBswAsynchronousServerCallPoint(self, element: ET.Element, point: BswAsynchronousServerCallPoint):
        child_element = ET.SubElement(element, "BSW-ASYNCHRONOUS-SERVER-CALL-POINT")
        self.writeBswModuleCallPoint(child_element, point)
        self.setChildElementOptionalRefType(child_element, "CALLED-ENTRY-REF", point.getCalledEntryRef())

    def writeBswModuleEntityCallPoints(self, element: ET.Element, entity: BswModuleEntity):
        points = entity.getCallPoints()
        if len(points) > 0:
            child_element = ET.SubElement(element, "CALL-POINTS")
            for point in points:
                if isinstance(point, BswAsynchronousServerCallPoint):
                    self.writeBswAsynchronousServerCallPoint(child_element, point)
                else:
                    self.notImplemented("Unsupported Call Point <%s>" % type(point))

    def writeBswModuleEntity(self, element: ET.Element, entity: BswModuleEntity):
        self.writeExecutableEntity(element, entity)
        self.writeBswModuleEntityActivationPointRefs(element, entity)
        self.writeBswModuleEntityCallPoints(element, entity)
        self.writeBswModuleEntityDataSendPoints(element, entity)
        self.writeBswModuleEntityDataReceivePoints(element, entity)
        self.setChildElementOptionalRefType(element, "IMPLEMENTED-ENTRY-REF", entity.implementedEntryRef)
        self.writeBswModuleEntityManagedModeGroups(element, entity)
        self.writeBswModuleEntityIssuedTriggerRefs(element, entity)

    def writeBswCalledEntity(self, element: ET.Element, entity: BswCalledEntity):
        self.logger.debug("Write BswCalledEntity <%s>" % entity.getShortName())
        child_element = ET.SubElement(element, "BSW-CALLED-ENTITY")
        self.writeBswModuleEntity(child_element, entity)

    def writeBswSchedulableEntity(self, element: ET.Element, entity: BswSchedulableEntity):
        self.logger.debug("Write BswSchedulableEntity <%s>" % entity.getShortName())
        child_element = ET.SubElement(element, "BSW-SCHEDULABLE-ENTITY")
        self.writeBswModuleEntity(child_element, entity)

    def setBswInterruptEntity(self, element: ET.Element, entity: BswInterruptEntity):
        self.logger.debug("Write BswInterruptEntity <%s>" % entity.getShortName())
        child_element = ET.SubElement(element, "BSW-INTERRUPT-ENTITY")
        self.writeBswModuleEntity(child_element, entity)
        self.setChildElementOptionalLiteral(child_element, "INTERRUPT-CATEGORY", entity.getInterruptCategory())
        self.setChildElementOptionalLiteral(child_element, "INTERRUPT-SOURCE", entity.getInterruptSource())

    def writeBswInternalBehaviorEntities(self, element: ET.Element, parent: BswInternalBehavior):
        entities = parent.getBswModuleEntities()
        if len(entities) > 0:
            child_element = ET.SubElement(element, "ENTITYS")
            for entity in entities:
                if isinstance(entity, BswCalledEntity):
                    self.writeBswCalledEntity(child_element, entity)
                elif isinstance(entity, BswSchedulableEntity):
                    self.writeBswSchedulableEntity(child_element, entity)
                elif isinstance(entity, BswInterruptEntity):
                    self.setBswInterruptEntity(child_element, entity)
                else:
                    self.notImplemented("Unsupported BswModuleEntity <%s>" % type(entity))

    def writeBswEvent(self, element: ET.Element, event: BswEvent):
        self.writeIdentifiable(element, event)
        self.setChildElementOptionalRefType(element, "STARTS-ON-EVENT-REF", event.startsOnEventRef)

    def writeBswScheduleEvent(self, element: ET.Element, event: BswScheduleEvent):
        self.writeBswEvent(element, event)

    def writeBswTimingEvent(self, element: ET.Element, event: BswTimingEvent):
        self.logger.debug("Write BswTimingEvent <%s>" % event.getShortName())
        child_element = ET.SubElement(element, "BSW-TIMING-EVENT")
        self.writeBswScheduleEvent(child_element, event)
        self.setChildElementOptionalTimeValue(child_element, "PERIOD", event.getPeriod())

    def writeBswBackgroundEvent(self, element: ET.Element, event: BswBackgroundEvent):
        self.logger.debug("Write BswTimingEvent <%s>" % event.getShortName())
        child_element = ET.SubElement(element, "BSW-BACKGROUND-EVENT")
        self.writeBswScheduleEvent(child_element, event)

    def writeBswInternalTriggerOccurredEvent(self, element: ET.Element, event: BswInternalTriggerOccurredEvent):
        self.logger.debug("Write BswInternalTriggerOccurredEvent <%s>" % event.getShortName())
        child_element = ET.SubElement(element, "BSW-INTERNAL-TRIGGER-OCCURRED-EVENT")
        self.writeBswScheduleEvent(child_element, event)
        self.setChildElementOptionalRefType(child_element, "EVENT-SOURCE-REF", event.getEventSourceRef())

    def writeBswExternalTriggerOccurredEvent(self, element: ET.Element, event: BswExternalTriggerOccurredEvent):
        self.logger.debug("Write BswExternalTriggerOccurredEvent <%s>" % event.getShortName())
        child_element = ET.SubElement(element, "BSW-EXTERNAL-TRIGGER-OCCURRED-EVENT")
        self.writeBswScheduleEvent(child_element, event)
        self.setChildElementOptionalRefType(child_element, "TRIGGER-REF", event.getTriggerRef())

    def writeBswDataReceivedEvent(self, element: ET.Element, event: BswDataReceivedEvent):
        self.logger.debug("Write BswDataReceivedEvent <%s>" % event.getShortName())
        # Read the Inherit BswScheduleEvent
        child_element = ET.SubElement(element, "BSW-DATA-RECEIVED-EVENT")
        self.writeBswScheduleEvent(child_element, event)
        self.setChildElementOptionalRefType(child_element, "DATA-REF", event.getDataRef())

    def writeBswOperationInvokedEvent(self, element: ET.Element, event: BswOperationInvokedEvent):
        self.logger.debug("Write BswOperationInvokedEvent <%s>" % event.getShortName())
        # Read the Inherit BswScheduleEvent
        child_element = ET.SubElement(element, "BSW-OPERATION-INVOKED-EVENT")
        self.writeBswEvent(child_element, event)
        self.setChildElementOptionalRefType(child_element, "ENTRY-REF", event.getEntryRef())

    def writeBswInternalBehaviorEvents(self, element: ET.Element, parent: BswInternalBehavior):
        events = parent.getBswEvents()
        if len(events) > 0:
            child_element = ET.SubElement(element, "EVENTS")
            for event in events:
                if isinstance(event, BswTimingEvent):
                    self.writeBswTimingEvent(child_element, event)
                elif isinstance(event, BswBackgroundEvent):
                    self.writeBswBackgroundEvent(child_element, event)
                elif isinstance(event, BswInternalTriggerOccurredEvent):
                    self.writeBswInternalTriggerOccurredEvent(child_element, event)
                elif isinstance(event, BswExternalTriggerOccurredEvent):
                    self.writeBswExternalTriggerOccurredEvent(child_element, event)
                elif isinstance(event, BswDataReceivedEvent):
                    self.writeBswDataReceivedEvent(child_element, event)
                elif isinstance(event, BswOperationInvokedEvent):
                    self.writeBswOperationInvokedEvent(child_element, event)
                else:
                    self.notImplemented("Unsupported BswModuleEntity <%s>" % type(event))

    def setBswModeSenderPolicy(self, element: ET.Element, policy: BswModeSenderPolicy):
        child_element = ET.SubElement(element, "BSW-MODE-SENDER-POLICY")
        self.setChildElementOptionalRefType(child_element, "PROVIDED-MODE-GROUP-REF", policy.getProvidedModeGroupRef())
        self.setChildElementOptionalNumericalValue(child_element, "QUEUE-LENGTH", policy.getQueueLength())

    def writeBswInternalBehaviorModeSenderPolicy(self, element: ET.Element, parent: BswInternalBehavior):
        policies = parent.getModeSenderPolicies()
        if len(policies) > 0:
            child_element = ET.SubElement(element, "MODE-SENDER-POLICYS")
            for policy in policies:
                if isinstance(policy, BswModeSenderPolicy):
                    self.setBswModeSenderPolicy(child_element, policy)
                else:
                    self.notImplemented("Unsupported ModeSenderPolicy type <%s>." % type(policy))

    def writeBswInternalBehaviorIncludedModeDeclarationGroupSets(self, element: ET.Element, behavior: BswInternalBehavior):
        group_sets = behavior.getIncludedModeDeclarationGroupSets()
        if len(group_sets) > 0:
            child_element = ET.SubElement(element, "INCLUDED-MODE-DECLARATION-GROUP-SETS")
            for group_set in group_sets:
                self.writeIncludedModeDeclarationGroupSet(child_element, group_set)

    def writeBswApiOptions(self, element: ET.Element, options: BswApiOptions):
        self.writeARObjectAttributes(element, options)
        self.setChildElementOptionalBooleanValue(element, "ENABLE-TAKE-ADDRESS", options.getEnableTakeAddress())

    def writeBswDataReceptionPolicy(self, element: ET.Element, policy: BswDataReceptionPolicy):
        self.writeBswApiOptions(element, policy)
        self.setChildElementOptionalRefType(element, "RECEIVED-DATA-REF", policy.getReceivedDataRef())

    def writeBswQueuedDataReceptionPolicy(self, element: ET.Element, policy: BswQueuedDataReceptionPolicy):
        child_element = ET.SubElement(element, "BSW-QUEUED-DATA-RECEPTION-POLICY")
        self.writeBswDataReceptionPolicy(child_element, policy)
        self.setChildElementOptionalPositiveInteger(child_element, "QUEUE-LENGTH", policy.getQueueLength())

    def writeBswInternalBehaviorReceptionPolicies(self, element: ET.Element, behavior: BswInternalBehavior):
        policies = behavior.getReceptionPolicies()
        if len(policies) > 0:
            child_element = ET.SubElement(element, "RECEPTION-POLICYS")
            for policy in policies:
                if isinstance(policy, BswQueuedDataReceptionPolicy):
                    self.writeBswQueuedDataReceptionPolicy(child_element, policy)
                else:
                    self.notImplemented("Unsupported Reception Policies <%s>" % type(policy))

    def writeBswInternalTriggeringPoint(self, element: ET.Element, point: BswInternalTriggeringPoint):
        child_element = ET.SubElement(element, "BSW-INTERNAL-TRIGGERING-POINT")
        self.writeIdentifiable(child_element, point)

    def writeBswInternalBehaviorInternalTriggeringPoints(self, element: ET.Element, behavior: BswInternalBehavior):
        points = behavior.getInternalTriggeringPoints()
        if len(points) > 0:
            child_element = ET.SubElement(element, "INTERNAL-TRIGGERING-POINTS")
            for point in points:
                if isinstance(point, BswInternalTriggeringPoint):
                    self.writeBswInternalTriggeringPoint(child_element, point)
                else:
                    self.notImplemented("Unsupported Internal Triggering Points <%s>" % type(point))

    def writeBswInternalBehavior(self, element: ET.Element, behavior: BswInternalBehavior):
        child_element = ET.SubElement(element, "BSW-INTERNAL-BEHAVIOR")
        self.writeInternalBehavior(child_element, behavior)
        self.writeBswInternalBehaviorInternalTriggeringPoints(child_element, behavior)
        self.writeBswInternalBehaviorEntities(child_element, behavior)
        self.writeBswInternalBehaviorEvents(child_element, behavior)
        self.writeBswInternalBehaviorModeSenderPolicy(child_element, behavior)
        self.writeBswInternalBehaviorIncludedModeDeclarationGroupSets(child_element, behavior)
        self.writeBswInternalBehaviorReceptionPolicies(child_element, behavior)

    def writeBswModuleDescriptionInternalBehaviors(self, element: ET.Element, desc: BswModuleDescription):
        behaviors = desc.getInternalBehaviors()
        if len(behaviors) > 0:
            child_element = ET.SubElement(element, "INTERNAL-BEHAVIORS")
            for behavior in behaviors:
                if isinstance(behavior, BswInternalBehavior):
                    self.writeBswInternalBehavior(child_element, behavior)
                else:
                    self.notImplemented("Unsupported Internal Behavior <%s>" % type(behavior))

    def writeTrigger(self, element: ET.Element, trigger: Trigger):
        child_element = ET.SubElement(element, "TRIGGER")
        self.writeIdentifiable(child_element, trigger)

    def writeBswModuleDescriptionReleasedTriggers(self, element: ET.Element, desc: BswModuleDescription):
        triggers = desc.getReleasedTriggers()
        if len(triggers) > 0:
            child_element = ET.SubElement(element, "RELEASED-TRIGGERS")
            for trigger in triggers:
                if isinstance(trigger, Trigger):
                    self.writeTrigger(child_element, trigger)
                else:
                    self.notImplemented("Unsupported Released Trigger <%s>" % type(trigger))

    def writeBswModuleDescriptionRequiredTriggers(self, element: ET.Element, desc: BswModuleDescription):
        triggers = desc.getRequiredTriggers()
        if len(triggers) > 0:
            child_element = ET.SubElement(element, "REQUIRED-TRIGGERS")
            for trigger in triggers:
                if isinstance(trigger, Trigger):
                    self.writeTrigger(child_element, trigger)
                else:
                    self.notImplemented("Unsupported Required Trigger <%s>" % type(trigger))

    def writeBswModuleDescriptionProvidedDatas(self, element: ET.Element, desc: BswModuleDescription):
        datas = desc.getProvidedDatas()
        if len(datas) > 0:
            child_element = ET.SubElement(element, "PROVIDED-DATAS")
            for data in datas:
                if isinstance(data, VariableDataPrototype):
                    self.writeVariableDataPrototype(child_element, data)
                else:
                    self.notImplemented("Unsupported Provided Data <%s>" % type(data))

    def writeBswModuleDescriptionRequiredDatas(self, element: ET.Element, desc: BswModuleDescription):
        datas = desc.getRequiredDatas()
        if len(datas) > 0:
            child_element = ET.SubElement(element, "REQUIRED-DATAS")
            for data in datas:
                if isinstance(data, VariableDataPrototype):
                    self.writeVariableDataPrototype(child_element, data)
                else:
                    self.notImplemented("Unsupported Required Data <%s>" % type(data))

    def writeBswModuleClientServerEntry(self, element: ET.Element, entry: BswModuleClientServerEntry):
        if entry is not None:
            child_element = ET.SubElement(element, "BSW-MODULE-CLIENT-SERVER-ENTRY")
            self.writeReferrable(child_element, entry)
            self.setChildElementOptionalRefType(child_element, "ENCAPSULATED-ENTRY-REF", entry.getEncapsulatedEntryRef())
            self.setChildElementOptionalBooleanValue(child_element, "IS-REENTRANT", entry.getIsReentrant())
            self.setChildElementOptionalBooleanValue(child_element, "IS-SYNCHRONOUS", entry.getIsSynchronous())

    def writeBswModuleDescriptionProvidedClientServerEntries(self, element: ET.Element, desc: BswModuleDescription):
        entries = desc.getProvidedClientServerEntries()
        if len(entries) > 0:
            child_element = ET.SubElement(element, "PROVIDED-CLIENT-SERVER-ENTRYS")
            for entry in entries:
                if isinstance(entry, BswModuleClientServerEntry):
                    self.writeBswModuleClientServerEntry(child_element, entry)
                else:
                    self.notImplemented("Unsupported Provided Client Server Entry <%s>" % type(entry))

    def writeBswModuleDescriptionRequiredClientServerEntries(self, element: ET.Element, desc: BswModuleDescription):
        entries = desc.getRequiredClientServerEntries()
        if len(entries) > 0:
            child_element = ET.SubElement(element, "REQUIRED-CLIENT-SERVER-ENTRYS")
            for entry in entries:
                if isinstance(entry, BswModuleClientServerEntry):
                    self.writeBswModuleClientServerEntry(child_element, entry)
                else:
                    self.notImplemented("Unsupported Provided Client Server Entry <%s>" % type(entry))

    def writeBswModuleDescription(self, element: ET.Element, desc: BswModuleDescription):
        self.logger.debug("writeBswModuleDescription %s" % desc.getShortName())
        child_element = ET.SubElement(element, "BSW-MODULE-DESCRIPTION")
        self.writeIdentifiable(child_element, desc)
        self.setChildElementOptionalNumericalValue(child_element, "MODULE-ID", desc.getModuleId())
        self.writeBswModuleDescriptionImplementedEntryRefs(child_element, desc)
        self.writeBswModuleDescriptionProvidedModeGroups(child_element, desc)
        self.writeBswModuleDescriptionRequiredModeGroups(child_element, desc)
        self.writeBswModuleDescriptionProvidedClientServerEntries(child_element, desc)
        self.writeBswModuleDescriptionRequiredClientServerEntries(child_element, desc)
        self.writeBswModuleDescriptionProvidedDatas(child_element, desc)
        self.writeBswModuleDescriptionRequiredDatas(child_element, desc)
        self.writeBswModuleDescriptionInternalBehaviors(child_element, desc)
        self.writeBswModuleDescriptionReleasedTriggers(child_element, desc)

    def setSwServiceArg(self, element: ET.Element, arg: SwServiceArg):
        self.logger.debug("Set SwServiceArg <%s>" % arg.getShortName())
        if arg is not None:
            child_element = ET.SubElement(element, "SW-SERVICE-ARG")
            self.writeIdentifiable(child_element, arg)
            self.setChildElementOptionalLiteral(child_element, "DIRECTION", arg.getDirection())
            self.setSwDataDefProps(child_element, "SW-DATA-DEF-PROPS", arg.getSwDataDefProps())

    def writeBswModuleEntryArguments(self, element: ET.Element, entry: BswModuleEntry):
        arguments = entry.getArguments()
        if len(arguments) > 0:
            child_element = ET.SubElement(element, "ARGUMENTS")
            for argument in arguments:
                self.setSwServiceArg(child_element, argument)

    def writeBswModuleEntry(self, element: ET.Element, entry: BswModuleEntry):
        self.logger.debug("writeBswModuleDescription %s" % entry.getShortName())
        child_element = ET.SubElement(element, "BSW-MODULE-ENTRY")
        self.writeIdentifiable(child_element, entry)
        self.setChildElementOptionalNumericalValue(child_element, "SERVICE-ID", entry.getServiceId())
        self.setChildElementOptionalBooleanValue(child_element, "IS-REENTRANT", entry.getIsReentrant())
        self.setChildElementOptionalBooleanValue(child_element, "IS-SYNCHRONOUS", entry.getIsSynchronous())
        self.setChildElementOptionalLiteral(child_element, "CALL-TYPE", entry.getCallType())
        self.setChildElementOptionalLiteral(child_element, "EXECUTION-CONTEXT", entry.getExecutionContext())
        self.setChildElementOptionalLiteral(child_element, "SW-SERVICE-IMPL-POLICY", entry.getSwServiceImplPolicy())
        self.writeBswModuleEntryArguments(child_element, entry)

    def setSwcBswRunnableMapping(self, element: ET.SubElement, mapping: SwcBswRunnableMapping):
        child_element = ET.SubElement(element, "SWC-BSW-RUNNABLE-MAPPING")
        self.setChildElementOptionalRefType(child_element, "BSW-ENTITY-REF", mapping.getBswEntityRef())
        self.setChildElementOptionalRefType(child_element, "SWC-RUNNABLE-REF", mapping.getSwcRunnableRef())

    def writeSwcBswRunnableMappings(self, element: ET.Element, parent: SwcBswMapping):
        runnable_mappings = parent.getRunnableMappings()
        if len(runnable_mappings) > 0:
            child_element = ET.SubElement(element, "RUNNABLE-MAPPINGS")
            for mapping in runnable_mappings:
                if isinstance(mapping, SwcBswRunnableMapping):
                    self.setSwcBswRunnableMapping(child_element, mapping)
                else:
                    self.notImplemented("Unsupported Runnable Mapping <%s>" % type(mapping))

    def writeSwcBswMapping(self, element: ET.Element, mapping: SwcBswMapping):
        self.logger.debug("writeBswModuleDescription %s" % mapping.getShortName())
        child_element = ET.SubElement(element, "SWC-BSW-MAPPING")
        self.writeIdentifiable(child_element, mapping)
        self.setChildElementOptionalRefType(child_element, "BSW-BEHAVIOR-REF", mapping.getBswBehaviorRef())
        self.writeSwcBswRunnableMappings(child_element, mapping)
        self.setChildElementOptionalRefType(child_element, "SWC-BEHAVIOR-REF", mapping.getSwcBehaviorRef())

    def writeEngineeringObject(self, element: ET.Element, engineering_obj: EngineeringObject):
        self.writeARObjectAttributes(element, engineering_obj)
        self.setChildElementOptionalLiteral(element, "SHORT-LABEL", engineering_obj.short_label)
        self.setChildElementOptionalLiteral(element, "CATEGORY", engineering_obj.category)
        
    def writeAutosarEngineeringObject(self, element: ET.Element, obj: AutosarEngineeringObject):
        # self.logger.debug("write ArtifactDescriptor %s", obj.short_label)
        child_element = ET.SubElement(element, "AUTOSAR-ENGINEERING-OBJECT")
        self.writeEngineeringObject(child_element, obj)

    def writeArtifactDescriptor(self, element: ET.Element, code_desc: Code):
        artifact_descs = code_desc.getArtifactDescriptors()
        if len(artifact_descs) > 0:
            child_element = ET.SubElement(element, "ARTIFACT-DESCRIPTORS")
            for artifact_desc in artifact_descs:
                if isinstance(artifact_desc, AutosarEngineeringObject):
                    self.writeAutosarEngineeringObject(child_element, artifact_desc)
                else:
                    self.notImplemented("Unsupported Artifact descriptor <%s>" % type(artifact_desc))

    def writeBswImplementationVendorSpecificModuleDefRefs(self, element: ET.Element, parent: BswImplementation):
        refs = parent.getVendorSpecificModuleDefRefs()
        if len(refs) > 0:
            child_element = ET.SubElement(element, "VENDOR-SPECIFIC-MODULE-DEF-REFS")
            if child_element is not None:
                for ref in refs:
                    self.setChildElementOptionalRefType(child_element, "VENDOR-SPECIFIC-MODULE-DEF-REF", ref)

    def writeBswImplementation(self, element: ET.Element, impl: BswImplementation):
        self.logger.debug("writeBswModuleDescription %s" % impl.getShortName())
        child_element = ET.SubElement(element, "BSW-IMPLEMENTATION")
        self.writeImplementation(child_element, impl)
        self.setChildElementOptionalLiteral(child_element, "AR-RELEASE-VERSION", impl.getArReleaseVersion())
        self.setChildElementOptionalRefType(child_element, "BEHAVIOR-REF", impl.getBehaviorRef())
        self.setChildElementOptionalLiteral(child_element, "VENDOR-API-INFIX", impl.getVendorApiInfix())
        self.writeBswImplementationVendorSpecificModuleDefRefs(child_element, impl)

    def writeImplementationDataTypeElements(self, element: ET.Element, parent: ImplementationDataType):
        sub_elements = parent.getImplementationDataTypeElements()
        if len(sub_elements) > 0:
            sub_elements_tag = ET.SubElement(element, "SUB-ELEMENTS")
            for type_element in sub_elements:
                child_element = ET.SubElement(sub_elements_tag, "IMPLEMENTATION-DATA-TYPE-ELEMENT")
                self.writeIdentifiable(child_element, type_element)
                self.setChildElementOptionalLiteral(child_element, "ARRAY-SIZE", type_element.getArraySize())
                self.setChildElementOptionalLiteral(child_element, "ARRAY-SIZE-HANDLING", type_element.getArraySizeHandling())
                self.setChildElementOptionalLiteral(child_element, "ARRAY-SIZE-SEMANTICS", type_element.getArraySizeSemantics())
                self.writeImplementationDataTypeElements(child_element, type_element)
                self.setSwDataDefProps(child_element, "SW-DATA-DEF-PROPS", type_element.getSwDataDefProps())

    def writeImplementationProps(self, element: ET.Element, props: ImplementationProps):
        self.writeReferrable(element, props)
        self.setChildElementOptionalLiteral(element, "SYMBOL", props.getSymbol())

    def writeSymbolProps(self, element: ET.Element, props: SymbolProps):
        if props is not None:
            child_element = ET.SubElement(element, "SYMBOL-PROPS")
            self.writeImplementationProps(child_element, props)

    def writeImplementationDataTypeSymbolProps(self, element: ET.Element, data_type: ImplementationDataType):
        self.writeSymbolProps(element, data_type.getSymbolProps())

    def writeImplementationDataType(self, element: ET.Element, data_type: ImplementationDataType):
        self.logger.debug("writeImplementationDataType %s" % data_type.getShortName())
        child_element = ET.SubElement(element, "IMPLEMENTATION-DATA-TYPE")
        self.setAutosarDataType(child_element, data_type)
        self.setChildElementOptionalLiteral(child_element, "DYNAMIC-ARRAY-SIZE-PROFILE", data_type.getDynamicArraySizeProfile())
        self.writeImplementationDataTypeElements(child_element, data_type)
        self.writeImplementationDataTypeSymbolProps(child_element, data_type)
        self.setChildElementOptionalLiteral(child_element, "TYPE-EMITTER", data_type.getTypeEmitter())

    def writeArgumentDataPrototype(self, element: ET.Element, prototype: ArgumentDataPrototype):
        child_element = ET.SubElement(element, "ARGUMENT-DATA-PROTOTYPE")
        self.writeAutosarDataPrototype(child_element, prototype)
        self.setChildElementOptionalLiteral(child_element, "DIRECTION", prototype.getDirection())
        self.setChildElementOptionalLiteral(child_element, "SERVER-ARGUMENT-IMPL-POLICY", prototype.getServerArgumentImplPolicy())

    def writeClientServerOperationArguments(self, element: ET.Element, parent: ClientServerOperation):
        arguments = parent.getArguments()
        if len(arguments) > 0:
            child_element = ET.SubElement(element, "ARGUMENTS")
            for argument in arguments:
                if isinstance(argument, ArgumentDataPrototype):
                    self.writeArgumentDataPrototype(child_element, argument)
                else:
                    self.notImplemented("Unsupported Argument <%s>" % type(argument))

    def writeClientServerOperationPossibleErrorRefs(self, element: ET.Element, parent: ClientServerOperation):
        error_refs = parent.getPossibleErrorRefs()
        if len(error_refs) > 0:
            child_element = ET.SubElement(element, "POSSIBLE-ERROR-REFS")
            for error_ref in error_refs:
                self.setChildElementOptionalRefType(child_element, "POSSIBLE-ERROR-REF", error_ref)

    def writeClientServerOperation(self, element: ET.Element, operation: ClientServerOperation):
        self.logger.debug("writeClientServerOperation %s" % operation.getShortName())
        child_element = ET.SubElement(element, "CLIENT-SERVER-OPERATION")
        self.writeIdentifiable(child_element, operation)
        self.writeClientServerOperationArguments(child_element, operation)
        self.writeClientServerOperationPossibleErrorRefs(child_element, operation)

    def writeClientServerInterfaceOperations(self, element: ET.Element, parent: ClientServerInterface):
        operations = parent.getOperations()
        if len(operations) > 0:
            operations_tag = ET.SubElement(element, "OPERATIONS")
            for operation in operations:
                if isinstance(operation, ClientServerOperation):
                    self.writeClientServerOperation(operations_tag, operation)
                else:
                    self.notImplemented("Unsupported Operation <%s>" % type(operation))

    def writeApplicationError(self, element: ET.Element, error: ApplicationError):
        self.logger.debug("writeApplicationError %s" % error.getShortName())
        child_element = ET.SubElement(element, "APPLICATION-ERROR")
        self.writeIdentifiable(child_element, error)
        self.setChildElementOptionalNumericalValue(child_element, "ERROR-CODE", error.error_code)

    def writePossibleErrors(self, element: ET.Element, parent: ClientServerInterface):
        errors = parent.getPossibleErrors()
        if len(errors) > 0:
            errors_tag = ET.SubElement(element, "POSSIBLE-ERRORS")
            for error in errors:
                if isinstance(error, ApplicationError):
                    self.writeApplicationError(errors_tag, error)
                else:
                    self.notImplemented("Unsupported PossibleError %s" % type(error))

    def writePortInterface(self, element: ET.Element, port_interface: PortInterface):
        self.writeIdentifiable(element, port_interface)
        self.setChildElementOptionalBooleanValue(element, "IS-SERVICE", port_interface.isService)
        self.setChildElementOptionalLiteral(element, "SERVICE-KIND", port_interface.serviceKind)

    def writeDataInterface(self, element: ET.Element, interface: DataInterface):
        self.writePortInterface(element, interface)

    def writeParameterInterface(self, element: ET.Element, interface: ParameterInterface):
        self.logger.debug("Write ParameterInterface %s" % interface.getShortName())
        child_element = ET.SubElement(element, "PARAMETER-INTERFACE")
        self.writeDataInterface(child_element, interface)
        self.writeSwcInternalBehaviorParameterDataPrototypes(child_element, "PARAMETERS", interface.getParameters())

    def writeClientServerInterface(self, element: ET.Element, cs_interface: ClientServerInterface):
        self.logger.debug("writeClientServerInterface %s" % cs_interface.getShortName())
        child_element = ET.SubElement(element, "CLIENT-SERVER-INTERFACE")
        self.writePortInterface(child_element, cs_interface)
        self.writeClientServerInterfaceOperations(child_element, cs_interface)
        self.writePossibleErrors(child_element, cs_interface)

    def writeApplicationSwComponentType(self, element: ET.Element, sw_component: ApplicationSwComponentType):
        self.logger.debug("writeApplicationSwComponentType %s" % sw_component.getShortName())
        child_element = ET.SubElement(element, "APPLICATION-SW-COMPONENT-TYPE")
        self.writeAtomicSwComponentType(child_element, sw_component)

    def writeEcuAbstractionSwComponentType(self, element: ET.Element, sw_component: EcuAbstractionSwComponentType):
        self.logger.debug("writeEcuAbstractionSwComponentType %s" % sw_component.getShortName())
        child_element = ET.SubElement(element, "ECU-ABSTRACTION-SW-COMPONENT-TYPE")
        self.writeAtomicSwComponentType(child_element, sw_component)

    def setApplicationArrayElement(self, element: ET.Element, array_element: ApplicationArrayElement):
        if array_element is not None:
            child_element = ET.SubElement(element, "ELEMENT")
            self.writeApplicationCompositeElementDataPrototype(child_element, array_element)
            self.setChildElementOptionalLiteral(child_element, "ARRAY-SIZE-HANDLING", array_element.getArraySizeHandling())
            self.setChildElementOptionalLiteral(child_element, "ARRAY-SIZE-SEMANTICS", array_element.getArraySizeSemantics())
            self.setChildElementOptionalNumericalValue(child_element, "MAX-NUMBER-OF-ELEMENTS", array_element.getMaxNumberOfElements())

    def writeApplicationArrayDataType(self, element: ET.Element, data_type: ApplicationArrayDataType):
        self.logger.debug("writeApplicationArrayDataType %s" % data_type.getShortName())
        child_element = ET.SubElement(element, "APPLICATION-ARRAY-DATA-TYPE")
        self.setApplicationCompositeDataType(child_element, data_type)
        self.setChildElementOptionalLiteral(child_element, "DYNAMIC-ARRAY-SIZE-PROFILE", data_type.getDynamicArraySizeProfile())
        self.setApplicationArrayElement(child_element, data_type.element)

    def setSwRecordLayoutV(self, element: ET.Element, key: str, layout_v: SwRecordLayoutV):
        if layout_v is not None:
            child_element = ET.SubElement(element, key)
            self.setChildElementOptionalLiteral(child_element, "SHORT-LABEL", layout_v.getShortLabel())
            self.setChildElementOptionalRefType(child_element, "BASE-TYPE-REF", layout_v.getBaseTypeRef())
            self.setChildElementOptionalLiteral(child_element, "SW-RECORD-LAYOUT-V-AXIS", layout_v.getSwRecordLayoutVAxis())
            self.setChildElementOptionalLiteral(child_element, "SW-RECORD-LAYOUT-V-PROP", layout_v.getSwRecordLayoutVProp())
            self.setChildElementOptionalLiteral(child_element, "SW-RECORD-LAYOUT-V-INDEX", layout_v.getSwRecordLayoutVIndex())

    def writeSwRecordLayoutGroupSwRecordLayoutGroupContentType(self, element: ET.Element, group: SwRecordLayoutGroup):
        content = group.getSwRecordLayoutGroupContentType()
        self.setSwRecordLayoutGroup(element, "SW-RECORD-LAYOUT-GROUP", content.getSwRecordLayoutGroup())
        self.setSwRecordLayoutV(element, "SW-RECORD-LAYOUT-V", content.getSwRecordLayoutV())

    def setSwRecordLayoutGroup(self, element: ET.Element, key: str, group: SwRecordLayoutGroup):
        if group is not None:
            child_element = ET.SubElement(element, key)
            self.setChildElementOptionalLiteral(child_element, "SHORT-LABEL", group.getShortLabel())
            self.setChildElementOptionalLiteral(child_element, "CATEGORY", group.getCategory())
            self.setChildElementOptionalLiteral(child_element, "SW-RECORD-LAYOUT-GROUP-AXIS", group.getSwRecordLayoutGroupAxis())
            self.setChildElementOptionalLiteral(child_element, "SW-RECORD-LAYOUT-GROUP-INDEX", group.getSwRecordLayoutGroupIndex())
            self.setChildElementOptionalLiteral(child_element, "SW-RECORD-LAYOUT-GROUP-FROM", group.getSwRecordLayoutGroupFrom())
            self.setChildElementOptionalLiteral(child_element, "SW-RECORD-LAYOUT-GROUP-TO", group.getSwRecordLayoutGroupTo())
            self.setChildElementOptionalIntegerValue(child_element, "SW-RECORD-LAYOUT-GROUP-STEP", group.getSwRecordLayoutGroupStep())
            self.writeSwRecordLayoutGroupSwRecordLayoutGroupContentType(child_element, group)

    def writeSwRecordLayout(self, element: ET.Element, layout: SwRecordLayout):
        self.logger.debug("writeSwRecordLayout %s" % layout.getShortName())
        child_element = ET.SubElement(element, "SW-RECORD-LAYOUT")
        self.writeIdentifiable(child_element, layout)
        self.setSwRecordLayoutGroup(child_element, "SW-RECORD-LAYOUT-GROUP", layout.getSwRecordLayoutGroup())

    def writeSwAddrMethod(self, element: ET.Element, method: SwAddrMethod):
        self.logger.debug("writeSwAddrMethod %s" % method.getShortName())
        child_element = ET.SubElement(element, "SW-ADDR-METHOD")
        self.writeIdentifiable(child_element, method)
        self.setChildElementOptionalLiteral(child_element, "MEMORY-ALLOCATION-KEYWORD-POLICY", method.getMemoryAllocationKeywordPolicy())
        options = method.getOptions()
        if len(options) > 0:
            options_tag = ET.SubElement(child_element, "OPTIONS")
            for option in options:
                self.setChildElementOptionalLiteral(options_tag, "OPTION", option)
        self.setChildElementOptionalLiteral(child_element, "SECTION-INITIALIZATION-POLICY", method.getSectionInitializationPolicy())
        self.setChildElementOptionalLiteral(child_element, "SECTION-TYPE", method.getSectionType())

    def writeTriggerInterface(self, element: ET.Element, trigger_if: TriggerInterface):
        self.logger.debug("writeTriggerInterface %s" % trigger_if.getShortName())
        # child_element = ET.SubElement(element, "TRIGGER-INTERFACE")
        # self.writePortInterface()

    def writeServiceSwComponentType(self, element: ET.Element, sw_component: ServiceSwComponentType):
        self.logger.debug("writeServiceSwComponentType %s" % sw_component.getShortName())
        child_element = ET.SubElement(element, "SERVICE-SW-COMPONENT-TYPE")
        self.writeAtomicSwComponentType(child_element, sw_component)

    def writeDataTypeMaps(self, element: ET.Element, parent: DataTypeMappingSet):
        maps = parent.getDataTypeMaps()
        if len(maps) > 0:
            maps_tag = ET.SubElement(element, "DATA-TYPE-MAPS")
            for map in maps:
                child_element = ET.SubElement(maps_tag, "DATA-TYPE-MAP")
                self.writeARObjectAttributes(child_element, map)
                self.setChildElementOptionalRefType(child_element, "APPLICATION-DATA-TYPE-REF", map.getApplicationDataTypeRef())
                self.setChildElementOptionalRefType(child_element, "IMPLEMENTATION-DATA-TYPE-REF", map.getImplementationDataTypeRef())

    def writeModeRequestTypeMaps(self, element: ET.Element, parent: DataTypeMappingSet):
        maps = parent.getModeRequestTypeMaps()
        if len(maps) > 0:
            maps_tag = ET.SubElement(element, "MODE-REQUEST-TYPE-MAPS")
            for map in maps:
                child_element = ET.SubElement(maps_tag, "MODE-REQUEST-TYPE-MAP")
                self.writeARObjectAttributes(child_element, map)
                self.setChildElementOptionalRefType(child_element, "IMPLEMENTATION-DATA-TYPE-REF", map.getImplementationDataTypeRef())
                self.setChildElementOptionalRefType(child_element, "MODE-GROUP-REF", map.getModeGroupRef())

    def writeDataTypeMappingSet(self, element: ET.Element, mapping_set: DataTypeMappingSet):
        self.logger.debug("writeDataTypeMappingSet %s" % mapping_set.getShortName())
        child_element = ET.SubElement(element, "DATA-TYPE-MAPPING-SET")
        self.writeIdentifiable(child_element, mapping_set)
        self.writeDataTypeMaps(child_element, mapping_set)
        self.writeModeRequestTypeMaps(child_element, mapping_set)

    def setModeDeclaration(self, element: ET.Element, mode_declaration: ModeDeclaration):
        child_element = ET.SubElement(element, "MODE-DECLARATION")
        self.writeIdentifiable(child_element, mode_declaration)
        self.setChildElementOptionalNumericalValue(child_element, "VALUE", mode_declaration.getValue())

    def writeModeDeclarationGroupModeDeclaration(self, element: ET.Element, parent: ModeDeclarationGroup):
        mode_declarations = parent.getModeDeclarations()
        if len(mode_declarations) > 0:
            child_element = ET.SubElement(element, "MODE-DECLARATIONS")
            for mode_declaration in mode_declarations:
                self.setModeDeclaration(child_element, mode_declaration)

    def writeModeDeclarationGroup(self, element: ET.Element, group: ModeDeclarationGroup):
        self.logger.debug("writeModeDeclarationGroup %s" % group.getShortName())
        child_element = ET.SubElement(element, "MODE-DECLARATION-GROUP")
        self.writeIdentifiable(child_element, group)
        self.setChildElementOptionalRefType(child_element, "INITIAL-MODE-REF", group.initialModeRef)
        self.writeModeDeclarationGroupModeDeclaration(child_element, group)
        self.setChildElementOptionalNumericalValue(child_element, "ON-TRANSITION-VALUE", group.getOnTransitionValue())

    def writeModeSwitchInterfaceModeGroup(self, element: ET.Element, parent: ModeSwitchInterface):
        mode_groups = parent.getModeGroups()
        if len(mode_groups) > 0:
            mode_group = mode_groups[0]
            child_element = ET.SubElement(element, "MODE-GROUP")
            self.writeIdentifiable(child_element, mode_group)
            self.setChildElementOptionalRefType(child_element, "TYPE-TREF", mode_group.type_tref)

    def writeModeSwitchInterface(self, element: ET.Element, mode_interface: ModeSwitchInterface):
        self.logger.debug("writeModeSwitchInterface %s" % mode_interface.getShortName())
        child_element = ET.SubElement(element, "MODE-SWITCH-INTERFACE")
        self.writePortInterface(child_element, mode_interface)
        self.writeModeSwitchInterfaceModeGroup(child_element, mode_interface)

    def setEOCExecutableEntityRefSuccessorRefs(self, element: ET.Element, successor_refs: List[RefType]):
        if len(successor_refs) > 0:
            child_element = ET.SubElement(element, "SUCCESSOR-REFS")
            for successor_ref in successor_refs:
                self.setChildElementOptionalRefType(child_element, "SUCCESSOR-REF", successor_ref)

    def writeEOCExecutableEntityRef(self, element: ET.Element, entity_ref: EOCExecutableEntityRef):
        child_element = ET.SubElement(element, "EOC-EXECUTABLE-ENTITY-REF")
        self.writeIdentifiable(child_element, entity_ref)
        self.setEOCExecutableEntityRefSuccessorRefs(child_element, entity_ref.getSuccessorRefs())

    def writeExecutionOrderConstraintOrderedElement(self, element: ET.Element, constraint: ExecutionOrderConstraint):
        order_elements = constraint.getOrderedElements()
        if len(order_elements) > 0:
            child_element = ET.SubElement(element, "ORDERED-ELEMENTS")
            for order_element in order_elements:
                if isinstance(order_element, EOCExecutableEntityRef):
                    self.writeEOCExecutableEntityRef(child_element, order_element)
                else:
                    self.notImplemented("Unsupported order element <%s>" % type(order_element))

    def writeExecutionOrderConstraint(self, element: ET.Element, constraint: ExecutionOrderConstraint):
        self.logger.debug("writeExecutionOrderConstraint %s" % constraint.getShortName())
        child_element = ET.SubElement(element, "EXECUTION-ORDER-CONSTRAINT")
        self.writeIdentifiable(child_element, constraint)
        self.writeExecutionOrderConstraintOrderedElement(child_element, constraint)

    def writeTimingRequirements(self, element: ET.Element, extension: TimingExtension):
        requirements = extension.getTimingRequirements()
        if len(requirements) > 0:
            child_element = ET.SubElement(element, "TIMING-REQUIREMENTS")
            for requirement in requirements:
                if isinstance(requirement, ExecutionOrderConstraint):
                    self.writeExecutionOrderConstraint(child_element, requirement)
                else:
                    self.notImplemented("Unsupported timing requirement <%s>" % type(requirement))

    def writeTimingExtension(self, element: ET.Element, extension: TimingExtension):
        self.writeTimingRequirements(element, extension)

    def writeSwcTiming(self, element: ET.Element, timing: SwcTiming):
        self.logger.debug("writeSWcTiming %s" % timing.getShortName())
        child_element = ET.SubElement(element, "SWC-TIMING")
        self.writeIdentifiable(child_element, timing)
        self.writeTimingExtension(child_element, timing)

    def writePduToFrameMappings(self, element: ET.Element, parent: Frame):
        mappings = parent.getPduToFrameMappings()
        if len(mappings) > 0:
            mappings_tags = ET.SubElement(element, "PDU-TO-FRAME-MAPPINGS")
            for mapping in mappings:
                child_element = ET.SubElement(mappings_tags, "PDU-TO-FRAME-MAPPING")
                self.writeIdentifiable(child_element, mapping)
                self.setChildElementOptionalLiteral(child_element, "PACKING-BYTE-ORDER", mapping.packingByteOrder)
                self.setChildElementOptionalRefType(child_element, "PDU-REF", mapping.pduRef)
                self.setChildElementOptionalNumericalValue(child_element, "START-POSITION", mapping.startPosition)

    def writeFrame(self, element: ET.Element, frame: Frame):
        self.writeIdentifiable(element, frame)
        self.setChildElementOptionalNumericalValue(element, "FRAME-LENGTH", frame.frameLength)
        self.writePduToFrameMappings(element, frame)

    def writeLinUnconditionalFrame(self, element: ET.Element, frame: LinUnconditionalFrame):
        self.logger.debug("LinUnconditionalFrame %s" % frame.getShortName())
        child_element = ET.SubElement(element, "LIN-UNCONDITIONAL-FRAME")
        self.writeFrame(child_element, frame)

    def writeNmNode(self, element: ET.Element, nm_node: NmNode):
        self.writeIdentifiable(element, nm_node)
        self.setChildElementOptionalRefType(element, "CONTROLLER-REF", nm_node.getControllerRef())
        self.setChildElementOptionalRefType(element, "NM-IF-ECU-REF", nm_node.getNmIfEcuRef())
        self.setChildElementOptionalBooleanValue(element, "NM-PASSIVE-MODE-ENABLED", nm_node.getNmPassiveModeEnabled())
        self.setChildElementOptionalNumericalValue(element, "NM-NODE-ID", nm_node.getNmNodeId())

        refs = nm_node.getRxNmPduRefs()
        if len(refs) > 0:
            refs_tag = ET.SubElement(element, "RX-NM-PDU-REFS")
            for ref in refs:
                self.setChildElementOptionalRefType(refs_tag, "RX-NM-PDU-REF", ref)

        refs = nm_node.getTxNmPduRefs()
        if len(refs) > 0:
            refs_tag = ET.SubElement(element, "TX-NM-PDU-REFS")
            for ref in refs:
                self.setChildElementOptionalRefType(refs_tag, "TX-NM-PDU-REF", ref)

    def writeCanNmNode(self, element: ET.Element, nm_node: CanNmNode):
        self.logger.debug("write CanNmNode %s" % nm_node.getShortName())
        child_element = ET.SubElement(element, "CAN-NM-NODE")
        self.writeNmNode(child_element, nm_node)
        self.setChildElementOptionalBooleanValue(child_element, "NM-CAR-WAKE-UP-RX-ENABLED", nm_node.getNmCarWakeUpRxEnabled())
        self.setChildElementOptionalFloatValue(child_element, "NM-MSG-CYCLE-OFFSET", nm_node.getNmMsgCycleOffset())
        self.setChildElementOptionalFloatValue(child_element, "NM-MSG-REDUCED-TIME", nm_node.getNmMsgReducedTime())
        self.setChildElementRxIdentifierRange(child_element, "NM-RANGE-CONFIG", nm_node.getNmRangeConfig())

    def writeUdpNmNode(self, element: ET.Element, nm_node: UdpNmNode):
        self.logger.debug("write UdpNmNode %s" % nm_node.getShortName())
        child_element = ET.SubElement(element, "UDP-NM-NODE")
        self.writeNmNode(child_element, nm_node)
        self.setChildElementOptionalTimeValue(child_element, "NM-MSG-CYCLE-OFFSET", nm_node.getNmMsgCycleOffset())

    def writeNmClusterNmNodes(self, element: ET.Element, parent: NmCluster):
        nodes = parent.getNmNodes()
        if len(nodes) > 0:
            child_element = ET.SubElement(element, "NM-NODES")
            for node in nodes:
                if isinstance(node, CanNmNode):
                    self.writeCanNmNode(child_element, node)
                elif isinstance(node, UdpNmNode):
                    self.writeUdpNmNode(child_element, node)
                else:
                    self.notImplemented("Unsupported Nm Node <%s>" % type(node))

    def writeCanNmClusterCoupling(self, element: ET.Element, coupling: CanNmClusterCoupling):
        child_element = ET.SubElement(element, "CAN-NM-CLUSTER-COUPLING")
        refs = coupling.getCoupledClusterRefs()
        if len(refs) > 0:
            refs_tag = ET.SubElement(child_element, "COUPLED-CLUSTER-REFS")
            for ref in refs:
                self.setChildElementOptionalRefType(refs_tag, "COUPLED-CLUSTER-REF", ref)
        self.setChildElementOptionalBooleanValue(child_element, "NM-BUSLOAD-REDUCTION-ENABLED", coupling.getNmBusloadReductionEnabled())
        self.setChildElementOptionalBooleanValue(child_element, "NM-IMMEDIATE-RESTART-ENABLED", coupling.getNmImmediateRestartEnabled())

    def writeUdpNmClusterCoupling(self, element: ET.Element, coupling: UdpNmClusterCoupling):
        child_element = ET.SubElement(element, "UDP-NM-CLUSTER-COUPLING")
        refs = coupling.getCoupledClusterRefs()
        if len(refs) > 0:
            refs_tag = ET.SubElement(child_element, "COUPLED-CLUSTER-REFS")
            for ref in refs:
                self.setChildElementOptionalRefType(refs_tag, "COUPLED-CLUSTER-REF", ref)
        self.setChildElementOptionalBooleanValue(child_element, "NM-IMMEDIATE-RESTART-ENABLED", coupling.getNmImmediateRestartEnabled())

    def writeNmConfigNmClusterCouplings(self, element: ET.Element, config: NmConfig):
        self.logger.debug("Write NmConfigNmClusterCouplings <%s>" % config.getShortName())
        couplings = config.getNmClusterCouplings()
        if len(couplings) > 0:
            child_element = ET.SubElement(element, "NM-CLUSTER-COUPLINGS")
            for coupling in couplings:
                if isinstance(coupling, CanNmClusterCoupling):
                    self.writeCanNmClusterCoupling(child_element, coupling)
                elif isinstance(coupling, UdpNmClusterCoupling):
                    self.writeUdpNmClusterCoupling(child_element, coupling)
                else:
                    self.notImplemented("Unsupported Nm Cluster Coupling <%s>" % type(coupling))

    def writeNmCluster(self, element: ET.Element, cluster: NmCluster):
        self.logger.debug("Write NmCluster <%s>" % cluster.getShortName())
        self.writeIdentifiable(element, cluster)
        self.setChildElementOptionalRefType(element, "COMMUNICATION-CLUSTER-REF", cluster.communicationClusterRef)
        self.setChildElementOptionalNumericalValue(element, "NM-CHANNEL-ID", cluster.nmChannelId)
        self.setChildElementOptionalBooleanValue(element, "NM-CHANNEL-SLEEP-MASTER", cluster.nmChannelSleepMaster)
        self.writeNmClusterNmNodes(element, cluster)
        self.setChildElementOptionalBooleanValue(element, "NM-SYNCHRONIZING-NETWORK", cluster.getNmSynchronizingNetwork())

    def writeCanNmCluster(self, element: ET.Element, cluster: CanNmCluster):
        self.logger.debug("Write CanNmCluster <%s>" % cluster.getShortName())
        child_element = ET.SubElement(element, "CAN-NM-CLUSTER")
        self.writeNmCluster(child_element, cluster)

        self.setChildElementOptionalBooleanValue(child_element, "NM-BUSLOAD-REDUCTION-ACTIVE", cluster.getNmBusloadReductionActive())
        self.setChildElementOptionalBooleanValue(child_element, "NM-CAR-WAKE-UP-RX-ENABLED", cluster.getNmCarWakeUpRxEnabled())
        self.setChildElementOptionalNumericalValue(child_element, "NM-CBV-POSITION", cluster.getNmCbvPosition())
        self.setChildElementOptionalBooleanValue(child_element, "NM-CHANNEL-ACTIVE", cluster.getNmChannelActive())
        self.setChildElementOptionalFloatValue(child_element, "NM-IMMEDIATE-NM-CYCLE-TIME", cluster.getNmImmediateNmCycleTime())
        self.setChildElementOptionalNumericalValue(child_element, "NM-IMMEDIATE-NM-TRANSMISSIONS", cluster.getNmImmediateNmTransmissions())
        self.setChildElementOptionalFloatValue(child_element, "NM-MESSAGE-TIMEOUT-TIME", cluster.getNmMessageTimeoutTime())
        self.setChildElementOptionalFloatValue(child_element, "NM-MSG-CYCLE-TIME", cluster.getNmMsgCycleTime())
        self.setChildElementOptionalFloatValue(child_element, "NM-NETWORK-TIMEOUT", cluster.getNmNetworkTimeout())
        self.setChildElementOptionalNumericalValue(child_element, "NM-NID-POSITION", cluster.getNmNidPosition())
        self.setChildElementOptionalFloatValue(child_element, "NM-REMOTE-SLEEP-INDICATION-TIME", cluster.getNmRemoteSleepIndicationTime())
        self.setChildElementOptionalFloatValue(child_element, "NM-REPEAT-MESSAGE-TIME", cluster.getNmRepeatMessageTime())
        self.setChildElementOptionalNumericalValue(child_element, "NM-USER-DATA-LENGTH", cluster.getNmUserDataLength())
        self.setChildElementOptionalFloatValue(child_element, "NM-WAIT-BUS-SLEEP-TIME", cluster.getNmWaitBusSleepTime())

    def writeUdpNmCluster(self, element: ET.Element, cluster: UdpNmCluster):
        self.logger.debug("Write UdpNmCluster <%s>" % cluster.getShortName())
        child_element = ET.SubElement(element, "UDP-NM-CLUSTER")
        self.writeNmCluster(child_element, cluster)
        self.setChildElementOptionalIntegerValue(child_element, "NM-CBV-POSITION", cluster.getNmCbvPosition())
        self.setChildElementOptionalBooleanValue(child_element, "NM-CHANNEL-ACTIVE", cluster.getNmChannelActive())
        self.setChildElementOptionalTimeValue(child_element, "NM-IMMEDIATE-NM-CYCLE-TIME", cluster.getNmImmediateNmCycleTime())
        self.setChildElementOptionalPositiveInteger(child_element, "NM-IMMEDIATE-NM-TRANSMISSIONS", cluster.getNmImmediateNmTransmissions())
        self.setChildElementOptionalTimeValue(child_element, "NM-MESSAGE-TIMEOUT-TIME", cluster.getNmMessageTimeoutTime())
        self.setChildElementOptionalTimeValue(child_element, "NM-MSG-CYCLE-TIME", cluster.getNmMsgCycleTime())
        self.setChildElementOptionalTimeValue(child_element, "NM-NETWORK-TIMEOUT", cluster.getNmNetworkTimeout())
        self.setChildElementOptionalIntegerValue(child_element, "NM-NID-POSITION", cluster.getNmNidPosition())
        self.setChildElementOptionalTimeValue(child_element, "NM-REMOTE-SLEEP-INDICATION-TIME", cluster.getNmRemoteSleepIndicationTime())
        self.setChildElementOptionalTimeValue(child_element, "NM-REPEAT-MESSAGE-TIME", cluster.getNmRepeatMessageTime())
        self.setChildElementOptionalTimeValue(child_element, "NM-WAIT-BUS-SLEEP-TIME", cluster.getNmWaitBusSleepTime())
        self.setChildElementOptionalRefType(child_element, "VLAN-REF", cluster.getVlanRef())

    def writeNmConfigNmClusters(self, element: ET.Element, parent: NmConfig):
        clusters = parent.getNmClusters()
        if len(clusters) > 0:
            child_element = ET.SubElement(element, "NM-CLUSTERS")
            for cluster in clusters:
                if isinstance(cluster, CanNmCluster):
                    self.writeCanNmCluster(child_element, cluster)
                elif isinstance(cluster, UdpNmCluster):
                    self.writeUdpNmCluster(child_element, cluster)
                else:
                    self.notImplemented("Unsupported Nm Cluster <%s>" % type(cluster))

    def writeUdpNmEcu(self, element: ET.Element, ecu: UdpNmEcu):
        if ecu is not None:
            child_element = ET.SubElement(element, "UDP-NM-ECU")
            self.setChildElementOptionalBooleanValue(child_element, "NM-SYNCHRONIZATION-POINT-ENABLED", ecu.getNmSynchronizationPointEnabled())

    def writeBusDependentNmEcus(self, element: ET.Element, nm_ecu: NmEcu):
        dependent_nm_ecus = nm_ecu.getBusDependentNmEcus()
        if len(dependent_nm_ecus) > 0:
            child_element = ET.SubElement(element, "BUS-DEPENDENT-NM-ECUS")
            for dependent_nm_ecu in dependent_nm_ecus:
                if isinstance(dependent_nm_ecu, UdpNmEcu):
                    self.writeUdpNmEcu(child_element, dependent_nm_ecu)
                else:
                    self.notImplemented("Unsupported BusDependentNmEcu <%s>" % type(dependent_nm_ecu))

    def writeNmEcu(self, element: ET.Element, nm_ecu: NmEcu):
        child_element = ET.SubElement(element, "NM-ECU")
        self.writeIdentifiable(child_element, nm_ecu)
        self.writeBusDependentNmEcus(child_element, nm_ecu)
        self.setChildElementOptionalRefType(child_element, "ECU-INSTANCE-REF", nm_ecu.getEcuInstanceRef())
        self.setChildElementOptionalBooleanValue(child_element, "NM-BUS-SYNCHRONIZATION-ENABLED", nm_ecu.getNmBusSynchronizationEnabled())
        self.setChildElementOptionalBooleanValue(child_element, "NM-COM-CONTROL-ENABLED", nm_ecu.getNmComControlEnabled())
        self.setChildElementOptionalBooleanValue(child_element, "NM-NODE-DETECTION-ENABLED", nm_ecu.getNmNodeDetectionEnabled())
        self.setChildElementOptionalBooleanValue(child_element, "NM-NODE-ID-ENABLED", nm_ecu.getNmNodeIdEnabled())
        self.setChildElementOptionalBooleanValue(child_element, "NM-PDU-RX-INDICATION-ENABLED", nm_ecu.getNmPduRxIndicationEnabled())
        self.setChildElementOptionalBooleanValue(child_element, "NM-REMOTE-SLEEP-IND-ENABLED", nm_ecu.getNmRemoteSleepIndEnabled())
        self.setChildElementOptionalBooleanValue(child_element, "NM-REPEAT-MSG-IND-ENABLED", nm_ecu.getNmRepeatMsgIndEnabled())
        self.setChildElementOptionalBooleanValue(child_element, "NM-STATE-CHANGE-IND-ENABLED", nm_ecu.getNmStateChangeIndEnabled())
        self.setChildElementOptionalBooleanValue(child_element, "NM-USER-DATA-ENABLED", nm_ecu.getNmUserDataEnabled())

    def writeNmConfigNmIfEcus(self, element: ET.Element, nm_config: NmConfig):
        ecus = nm_config.getNmIfEcus()
        if len(ecus) > 0:
            child_element = ET.SubElement(element, "NM-IF-ECUS")
            for ecu in ecus:
                if isinstance(ecu, NmEcu):
                    self.writeNmEcu(child_element, ecu)
                else:
                    self.notImplemented("Unsupported NmIfEcus <%s>" % type(ecu))

    def writeNmConfig(self, element: ET.Element, config: NmConfig):
        self.logger.debug("Write NmConfig <%s>" % config.getShortName())
        child_element = ET.SubElement(element, "NM-CONFIG")
        self.writeIdentifiable(child_element, config)
        self.writeNmConfigNmClusters(child_element, config)
        self.writeNmConfigNmClusterCouplings(child_element, config)
        self.writeNmConfigNmIfEcus(child_element, config)

    def writeISignalToIPduMapping(self, element: ET.Element, mapping: ISignalToIPduMapping):
        if mapping is not None:
            child_element = ET.SubElement(element, "I-SIGNAL-TO-I-PDU-MAPPING")
            self.writeIdentifiable(child_element, mapping)
            self.setChildElementOptionalRefType(child_element, "I-SIGNAL-REF", mapping.getISignalRef())
            self.setChildElementOptionalLiteral(child_element, "PACKING-BYTE-ORDER", mapping.getPackingByteOrder())
            self.setChildElementOptionalIntegerValue(child_element, "START-POSITION", mapping.getStartPosition())
            self.setChildElementOptionalLiteral(child_element, "TRANSFER-PROPERTY", mapping.getTransferProperty())
        
    def writeNmPduISignalToIPduMappings(self, element: ET.Element, pdu: NmPdu):
        mappings = pdu.getISignalToIPduMappings()
        if len(mappings) > 0:
            child_element = ET.SubElement(element, "I-SIGNAL-TO-I-PDU-MAPPINGS")
            for mapping in mappings:
                if isinstance(mapping, ISignalToIPduMapping):
                    self.writeISignalToIPduMapping(child_element, mapping)
                else:
                    self.notImplemented("Unsupported ISignalToIPduMapping <%s>" % type(mapping))

    def writeNmPdu(self, element: ET.Element, pdu: NmPdu):
        self.logger.debug("Write NmPdu <%s>" % pdu.getShortName())
        child_element = ET.SubElement(element, "NM-PDU")
        self.writePdu(child_element, pdu)
        self.writeNmPduISignalToIPduMappings(child_element, pdu)
        self.setChildElementOptionalIntegerValue(child_element, "UNUSED-BIT-PATTERN", pdu.getUnusedBitPattern())

    def writeNPdu(self, element: ET.Element, pdu: NPdu):
        self.logger.debug("Write NPdu <%s>" % pdu.getShortName())
        child_element = ET.SubElement(element, "N-PDU")
        self.writePdu(child_element, pdu)

    def writeDcmIPdu(self, element: ET.Element, pdu: DcmIPdu):
        self.logger.debug("Write DcmIPdu <%s>" % pdu.getShortName())
        child_element = ET.SubElement(element, "DCM-I-PDU")
        self.writeIPdu(child_element, pdu)
        self.setChildElementOptionalLiteral(child_element, "DIAG-PDU-TYPE", pdu.getDiagPduType())

    def setSecureCommunicationProps(self, element: ET.Element, key: str, props: SecureCommunicationProps):
        if props is not None:
            child_element = ET.SubElement(element, key)
            self.setChildElementOptionalPositiveInteger(child_element, "AUTH-DATA-FRESHNESS-LENGTH", props.getAuthDataFreshnessLength())
            self.setChildElementOptionalPositiveInteger(child_element, "AUTH-DATA-FRESHNESS-START-POSITION", props.getAuthDataFreshnessStartPosition())     # noqa E501
            self.setChildElementOptionalPositiveInteger(child_element, "AUTH-INFO-TX-LENGTH", props.getAuthInfoTxLength())
            self.setChildElementOptionalPositiveInteger(child_element, "AUTHENTICATION-BUILD-ATTEMPTS", props.getAuthenticationBuildAttempts())
            self.setChildElementOptionalPositiveInteger(child_element, "AUTHENTICATION-RETRIES", props.getAuthenticationRetries())
            self.setChildElementOptionalPositiveInteger(child_element, "DATA-ID", props.getDataId())
            self.setChildElementOptionalPositiveInteger(child_element, "FRESHNESS-VALUE-ID", props.getFreshnessValueId())
            self.setChildElementOptionalPositiveInteger(child_element, "FRESHNESS-VALUE-LENGTH", props.getFreshnessValueLength())
            self.setChildElementOptionalPositiveInteger(child_element, "FRESHNESS-VALUE-TX-LENGTH", props.getFreshnessValueTxLength())

    def writeSecuredIPdu(self, element: ET.Element, i_pdu: SecuredIPdu):
        self.logger.debug("Write SecuredIPdu <%s>" % i_pdu.getShortName())
        child_element = ET.SubElement(element, "SECURED-I-PDU")
        self.writeIPdu(child_element, i_pdu)
        self.setChildElementOptionalRefType(child_element, "AUTHENTICATION-PROPS-REF", i_pdu.getAuthenticationPropsRef())
        self.setChildElementOptionalRefType(child_element, "FRESHNESS-PROPS-REF", i_pdu.getFreshnessPropsRef())
        self.setChildElementOptionalRefType(child_element, "PAYLOAD-REF", i_pdu.getPayloadRef())
        self.setSecureCommunicationProps(child_element, "SECURE-COMMUNICATION-PROPS", i_pdu.getSecureCommunicationProps())
        self.setChildElementOptionalBooleanValue(child_element, "USE-AS-CRYPTOGRAPHIC-I-PDU", i_pdu.getUseAsCryptographicIPdu())

    def writeTpConfig(self, element: ET.Element, config: TpConfig):
        self.writeIdentifiable(element, config)
        self.setChildElementOptionalRefType(element, "COMMUNICATION-CLUSTER-REF", config.getCommunicationClusterRef())

    def writeCanTpAddress(self, element: ET.Element, address: CanTpAddress):
        if address is not None:
            child_element = ET.SubElement(element, "CAN-TP-ADDRESS")
            self.writeIdentifiable(child_element, address)
            self.setChildElementOptionalIntegerValue(child_element, "TP-ADDRESS", address.getTpAddress())
            self.setChildElementOptionalIntegerValue(child_element, "TP-ADDRESS-EXTENSION-VALUE", address.getTpAddressExtensionValue())

    def writeCanTpConfigTpAddresses(self, element: ET.Element, config: CanTpConfig):
        addresses = config.getTpAddresses()
        if len(addresses) > 0:
            child_element = ET.SubElement(element, "TP-ADDRESSS")
            for address in addresses:
                if isinstance(address, CanTpAddress):
                    self.writeCanTpAddress(child_element, address)
                else:
                    self.notImplemented("Unsupported TpAddress <%s>" % type(address))

    def writeCanTpChannel(self, element: ET.Element, channel: CanTpChannel):
        if channel is not None:
            child_element = ET.SubElement(element, "CAN-TP-CHANNEL")
            self.writeIdentifiable(child_element, channel)
            self.setChildElementOptionalPositiveInteger(child_element, "CHANNEL-ID", channel.getChannelId())
            self.setChildElementOptionalLiteral(child_element, "CHANNEL-MODE", channel.getChannelMode())

    def writeCanTpConfigTpChannels(self, element: ET.Element, config: CanTpConfig):
        channels = config.getTpChannels()
        if len(channels) > 0:
            child_element = ET.SubElement(element, "TP-CHANNELS")
            for channel in channels:
                if isinstance(channel, CanTpChannel):
                    self.writeCanTpChannel(child_element, channel)
                else:
                    self.notImplemented("Unsupported TpChannel <%s>" % type(channel))

    def writeTpConnection(self, element: ET.Element, connection: TpConnection):
        self.writeARObjectAttributes(element, connection)
        ident = connection.getIdent()
        if ident is not None:
            child_element = ET.SubElement(element, "IDENT")
            self.writeReferrable(child_element, ident)

    def writeTpConnectionReceiverRefs(self, element: ET.Element, connection: CanTpConnection):
        refs = connection.getReceiverRefs()
        if len(refs) > 0:
            child_element = ET.SubElement(element, "RECEIVER-REFS")
            for ref in refs:
                self.setChildElementOptionalRefType(child_element, "RECEIVER-REF", ref)

    def writeCanTpConnection(self, element: ET.Element, connection: CanTpConnection):
        if connection is not None:
            child_element = ET.SubElement(element, "CAN-TP-CONNECTION")
            self.writeTpConnection(child_element, connection)
            self.setChildElementOptionalLiteral(child_element, "ADDRESSING-FORMAT", connection.getAddressingFormat())
            self.setChildElementOptionalRefType(child_element, "CAN-TP-CHANNEL-REF", connection.getCanTpChannelRef())
            self.setChildElementOptionalBooleanValue(child_element, "CANCELLATION", connection.getCancellation())
            self.setChildElementOptionalRefType(child_element, "DATA-PDU-REF", connection.getDataPduRef())
            self.setChildElementOptionalRefType(child_element, "FLOW-CONTROL-PDU-REF", connection.getFlowControlPduRef())
            self.setChildElementOptionalIntegerValue(child_element, "MAX-BLOCK-SIZE", connection.getMaxBlockSize())
            self.setChildElementOptionalRefType(child_element, "MULTICAST-REF", connection.getMulticastRef())
            self.setChildElementOptionalBooleanValue(child_element, "PADDING-ACTIVATION", connection.getPaddingActivation())
            self.writeTpConnectionReceiverRefs(child_element, connection)
            self.setChildElementOptionalLiteral(child_element, "TA-TYPE", connection.getTaType())
            self.setChildElementOptionalTimeValue(child_element, "TIMEOUT-BR", connection.getTimeoutBr())
            self.setChildElementOptionalTimeValue(child_element, "TIMEOUT-BS", connection.getTimeoutBs())
            self.setChildElementOptionalTimeValue(child_element, "TIMEOUT-CR", connection.getTimeoutCr())
            self.setChildElementOptionalTimeValue(child_element, "TIMEOUT-CS", connection.getTimeoutCs())
            self.setChildElementOptionalRefType(child_element, "TP-SDU-REF", connection.getTpSduRef())
            self.setChildElementOptionalRefType(child_element, "TRANSMITTER-REF", connection.getTransmitterRef())

    def writeCanTpConfigTpConnections(self, element: ET.Element, config: CanTpConfig):
        connections = config.getTpConnections()
        if len(connections) > 0:
            child_element = ET.SubElement(element, "TP-CONNECTIONS")
            for connection in connections:
                if isinstance(connection, CanTpConnection):
                    self.writeCanTpConnection(child_element, connection)
                else:
                    self.notImplemented("Unsupported TpConnection <%s>" % type(connection))

    def writeCanTpEcu(self, element: ET.Element, tp_ecu: CanTpEcu):
        if tp_ecu is not None:
            child_element = ET.SubElement(element, "CAN-TP-ECU")
            self.setChildElementOptionalTimeValue(child_element, "CYCLE-TIME-MAIN-FUNCTION", tp_ecu.getCycleTimeMainFunction())
            self.setChildElementOptionalRefType(child_element, "ECU-INSTANCE-REF", tp_ecu.getEcuInstanceRef())

    def writeCanTpConfigTpEcus(self, element: ET.Element, config: CanTpConfig):
        tp_ecus = config.getTpEcus()
        if len(tp_ecus) > 0:
            child_element = ET.SubElement(element, "TP-ECUS")
            for tp_ecu in tp_ecus:
                if isinstance(tp_ecu, CanTpEcu):
                    self.writeCanTpEcu(child_element, tp_ecu)
                else:
                    self.notImplemented("Unsupported TpEcu <%s>" % type(tp_ecu))

    def writeCanTpNode(self, element: ET.Element, tp_node: CanTpNode):
        if tp_node is not None:
            child_element = ET.SubElement(element, "CAN-TP-NODE")
            self.writeIdentifiable(child_element, tp_node)
            self.setChildElementOptionalRefType(child_element, "CONNECTOR-REF", tp_node.getConnectorRef())
            self.setChildElementOptionalIntegerValue(child_element, "MAX-FC-WAIT", tp_node.getMaxFcWait())
            self.setChildElementOptionalTimeValue(child_element, "ST-MIN", tp_node.getStMin())
            self.setChildElementOptionalTimeValue(child_element, "TIMEOUT-AR", tp_node.getTimeoutAr())
            self.setChildElementOptionalTimeValue(child_element, "TIMEOUT-AS", tp_node.getTimeoutAs())
            self.setChildElementOptionalRefType(child_element, "TP-ADDRESS-REF", tp_node.getTpAddressRef())

    def writeCanTpConfigTpNodes(self, element: ET.Element, config: CanTpConfig):
        tp_nodes = config.getTpNodes()
        if len(tp_nodes) > 0:
            child_element = ET.SubElement(element, "TP-NODES")
            for tp_node in tp_nodes:
                if isinstance(tp_node, CanTpNode):
                    self.writeCanTpNode(child_element, tp_node)
                else:
                    self.notImplemented("Unsupported TpNode <%s>" % type(tp_node))

    def writeCanTpConfig(self, element: ET.Element, config: CanTpConfig):
        self.logger.debug("Write CanTpConfig <%s>" % config.getShortName())
        child_element = ET.SubElement(element, "CAN-TP-CONFIG")
        self.writeTpConfig(child_element, config)
        self.writeCanTpConfigTpAddresses(child_element, config)
        self.writeCanTpConfigTpChannels(child_element, config)
        self.writeCanTpConfigTpConnections(child_element, config)
        self.writeCanTpConfigTpEcus(child_element, config)
        self.writeCanTpConfigTpNodes(child_element, config)

    def writeTpAddress(self, element: ET.Element, address: TpAddress):
        if address is not None:
            child_element = ET.SubElement(element, "TP-ADDRESS")
            self.writeIdentifiable(child_element, address)
            self.setChildElementOptionalIntegerValue(child_element, "TP-ADDRESS", address.getTpAddress())

    def writeLinTpConfigTpAddresses(self, element: ET.Element, config: CanTpConfig):
        addresses = config.getTpAddresses()
        if len(addresses) > 0:
            child_element = ET.SubElement(element, "TP-ADDRESSS")
            for address in addresses:
                if isinstance(address, TpAddress):
                    self.writeTpAddress(child_element, address)
                else:
                    self.notImplemented("Unsupported TpAddress <%s>" % type(address))

    def writeLinTpConnection(self, element: ET.Element, connection: LinTpConnection):
        if connection is not None:
            child_element = ET.SubElement(element, "LIN-TP-CONNECTION")
            self.writeTpConnection(child_element, connection)
            self.setChildElementOptionalRefType(child_element, "DATA-PDU-REF", connection.getDataPduRef())
            self.setChildElementOptionalRefType(child_element, "FLOW-CONTROL-REF", connection.getFlowControlRef())
            self.setChildElementOptionalRefType(child_element, "LIN-TP-N-SDU-REF", connection.getLinTpNSduRef())
            self.writeTpConnectionReceiverRefs(child_element, connection)
            self.setChildElementOptionalTimeValue(child_element, "TIMEOUT-AS", connection.getTimeoutAs())
            self.setChildElementOptionalTimeValue(child_element, "TIMEOUT-CR", connection.getTimeoutCr())
            self.setChildElementOptionalTimeValue(child_element, "TIMEOUT-CS", connection.getTimeoutCs())
            self.setChildElementOptionalRefType(child_element, "TRANSMITTER-REF", connection.getTransmitterRef())

    def writeLinTpConfigTpConnections(self, element: ET.Element, config: LinTpConfig):
        connections = config.getTpConnections()
        if len(connections) > 0:
            child_element = ET.SubElement(element, "TP-CONNECTIONS")
            for connection in connections:
                if isinstance(connection, LinTpConnection):
                    self.writeLinTpConnection(child_element, connection)
                else:
                    self.notImplemented("Unsupported TpConnection <%s>" % type(connection))

    def writeLinTpNode(self, element: ET.Element, tp_node: LinTpNode):
        if tp_node is not None:
            child_element = ET.SubElement(element, "LIN-TP-NODE")
            self.writeIdentifiable(child_element, tp_node)
            self.setChildElementOptionalRefType(child_element, "CONNECTOR-REF", tp_node.getConnectorRef())
            self.setChildElementOptionalBooleanValue(element, "DROP-NOT-REQUESTED-NAD", tp_node.getDropNotRequestedNad())
            self.setChildElementOptionalTimeValue(child_element, "P-2-MAX", tp_node.getP2Max())
            self.setChildElementOptionalTimeValue(child_element, "P-2-TIMING", tp_node.getP2Timing())
            self.setChildElementOptionalRefType(child_element, "TP-ADDRESS-REF", tp_node.getTpAddressRef())

    def writeLinTpConfigTpNodes(self, element: ET.Element, config: LinTpConfig):
        tp_nodes = config.getTpNodes()
        if len(tp_nodes) > 0:
            child_element = ET.SubElement(element, "TP-NODES")
            for tp_node in tp_nodes:
                if isinstance(tp_node, LinTpNode):
                    self.writeLinTpNode(child_element, tp_node)
                else:
                    self.notImplemented("Unsupported TpNode <%s>" % type(tp_node))

    def writeLinTpConfig(self, element: ET.Element, config: LinTpConfig):
        self.logger.debug("Write LinTpConfig <%s>" % config.getShortName())
        child_element = ET.SubElement(element, "LIN-TP-CONFIG")
        self.writeTpConfig(child_element, config)
        self.writeLinTpConfigTpAddresses(child_element, config)
        self.writeLinTpConfigTpConnections(child_element, config)
        self.writeLinTpConfigTpNodes(child_element, config)

    def writeFrameTriggering(self, element: ET.Element, triggering: FrameTriggering):
        self.writeIdentifiable(element, triggering)
        ref_list = triggering.getFramePortRefs()
        if len(ref_list) > 0:
            frame_port_refs_tag = ET.SubElement(element, "FRAME-PORT-REFS")
            for ref in ref_list:
                self.setChildElementOptionalRefType(frame_port_refs_tag, "FRAME-PORT-REF", ref)
        self.setChildElementOptionalRefType(element, "FRAME-REF", triggering.getFrameRef())

        refs = triggering.getPduTriggeringRefs()
        if len(refs) > 0:
            triggerings_tag = ET.SubElement(element, "PDU-TRIGGERINGS")
            for ref in refs:
                child_element = ET.SubElement(triggerings_tag, 'PDU-TRIGGERING-REF-CONDITIONAL')
                self.setChildElementOptionalRefType(child_element, "PDU-TRIGGERING-REF", ref)

    def writeCanFrameTriggering(self, element: ET.Element, triggering: CanFrameTriggering):
        self.logger.debug("WRite CanFrameTriggering %s" % triggering.getShortName())
        child_element = ET.SubElement(element, "CAN-FRAME-TRIGGERING")
        self.writeFrameTriggering(child_element, triggering)
        self.setChildElementOptionalLiteral(child_element, "CAN-ADDRESSING-MODE", triggering.getCanAddressingMode())
        self.setChildElementOptionalBooleanValue(child_element, "CAN-FD-FRAME-SUPPORT", triggering.getCanFdFrameSupport())
        self.setChildElementOptionalLiteral(child_element, "CAN-FRAME-RX-BEHAVIOR", triggering.getCanFrameRxBehavior())
        self.setChildElementOptionalLiteral(child_element, "CAN-FRAME-TX-BEHAVIOR", triggering.getCanFrameTxBehavior())
        self.setChildElementOptionalNumericalValue(child_element, "IDENTIFIER", triggering.getIdentifier())
        self.setChildElementRxIdentifierRange(child_element, "RX-IDENTIFIER-RANGE", triggering.getRxIdentifierRange())

    def writeLinFrameTriggering(self, element: ET.Element, triggering: LinFrameTriggering):
        self.logger.debug("Write LinFrameTriggering %s" % triggering.getShortName())
        child_element = ET.SubElement(element, "LIN-FRAME-TRIGGERING")
        self.writeFrameTriggering(child_element, triggering)
        self.setChildElementOptionalNumericalValue(child_element, "IDENTIFIER", triggering.getIdentifier())
        self.setChildElementOptionalLiteral(child_element, "LIN-CHECKSUM", triggering.getLinChecksum())

    def writeCommunicationCycle(self, element: ET.Element, cycle: CommunicationCycle):
        self.writeARObjectAttributes(element, cycle)

    def writeCycleRepetition(self, element: ET.Element, cycle: CycleRepetition):
        if cycle is not None:
            child_element = ET.SubElement(element, "CYCLE-REPETITION")
            self.writeCommunicationCycle(child_element, cycle)
            self.setChildElementOptionalIntegerValue(child_element, "BASE-CYCLE", cycle.getBaseCycle())
            self.setChildElementOptionalLiteral(child_element, "CYCLE-REPETITION", cycle.getCycleRepetition())
        
    def writeFlexrayAbsolutelyScheduledTimingCommunicationCycle(self, element: ET.Element, timing: FlexrayAbsolutelyScheduledTiming):
        cycle = timing.getCommunicationCycle()
        if cycle is not None:
            child_element = ET.SubElement(element, "COMMUNICATION-CYCLE")
            if isinstance(cycle, CycleRepetition):
                self.writeCycleRepetition(child_element, cycle)
            else:
                self.notImplemented("Unsupported CommunicationCycle <%s>" % type(child_element))

    def writeFlexrayAbsolutelyScheduledTiming(self, element: ET.Element, timing: FlexrayAbsolutelyScheduledTiming):
        if timing is not None:
            child_element = ET.SubElement(element, "FLEXRAY-ABSOLUTELY-SCHEDULED-TIMING")
            self.writeARObjectAttributes(child_element, timing)
            self.writeFlexrayAbsolutelyScheduledTimingCommunicationCycle(child_element, timing)
            self.setChildElementOptionalPositiveInteger(child_element, "SLOT-ID", timing.getSlotID())

    def writeFlexrayFrameTriggeringAbsolutelyScheduledTimings(self, element: ET.Element, triggering: FlexrayFrameTriggering):
        timings = triggering.getAbsolutelyScheduledTimings()
        if len(timings) > 0:
            child_element = ET.SubElement(element, "ABSOLUTELY-SCHEDULED-TIMINGS")
            for timing in timings:
                if isinstance(timing, FlexrayAbsolutelyScheduledTiming):
                    self.writeFlexrayAbsolutelyScheduledTiming(child_element, timing)
                else:
                    self.notImplemented("Unsupported AbsolutelyScheduledTiming <%s>" % type(timing))

    def writeFlexrayFrameTriggering(self, element: ET.Element, triggering: FlexrayFrameTriggering):
        self.logger.debug("Write FlexrayFrameTriggering %s" % triggering.getShortName())
        child_element = ET.SubElement(element, "FLEXRAY-FRAME-TRIGGERING")
        self.writeFrameTriggering(child_element, triggering)
        self.writeFlexrayFrameTriggeringAbsolutelyScheduledTimings(child_element, triggering)
        self.setChildElementOptionalBooleanValue(child_element, "ALLOW-DYNAMIC-L-SDU-LENGTH", triggering.getAllowDynamicLSduLength())
        self.setChildElementOptionalPositiveInteger(child_element, "MESSAGE-ID", triggering.getMessageId())
        self.setChildElementOptionalBooleanValue(child_element, "PAYLOAD-PREAMBLE-INDICATOR", triggering.getPayloadPreambleIndicator())

    def writeISignalTriggering(self, element: ET.Element, triggering: ISignalTriggering):
        self.logger.debug("Write ISignalTriggering %s" % triggering.getShortName())
        child_element = ET.SubElement(element, "I-SIGNAL-TRIGGERING")
        self.writeIdentifiable(child_element, triggering)
        self.setChildElementOptionalRefType(child_element, "I-SIGNAL-GROUP-REF", triggering.getISignalGroupRef())
        ref_list = triggering.getISignalPortRefs()
        if len(ref_list) > 0:
            i_signal_port_refs_tag = ET.SubElement(child_element, "I-SIGNAL-PORT-REFS")
            for ref in ref_list:
                self.setChildElementOptionalRefType(i_signal_port_refs_tag, "I-SIGNAL-PORT-REF", ref)
        self.setChildElementOptionalRefType(child_element, "I-SIGNAL-REF", triggering.getISignalRef())

    def writePduTriggering(self, element: ET.Element, triggering: PduTriggering):
        self.logger.debug("Write PduTriggering %s" % triggering.getShortName())
        child_element = ET.SubElement(element, "PDU-TRIGGERING")
        self.writeIdentifiable(child_element, triggering)
        ref_list = triggering.getIPduPortRefs()
        if len(ref_list) > 0:
            i_signal_port_refs_tag = ET.SubElement(child_element, "I-PDU-PORT-REFS")
            for ref in ref_list:
                self.setChildElementOptionalRefType(i_signal_port_refs_tag, "I-PDU-PORT-REF", ref)
        self.setChildElementOptionalRefType(child_element, "I-PDU-REF", triggering.getIPduRef())

        refs = triggering.getISignalTriggeringRefs()
        if len(refs) > 0:
            triggerings_tag = ET.SubElement(child_element, "I-SIGNAL-TRIGGERINGS")
            for ref in refs:
                child_element = ET.SubElement(triggerings_tag, 'I-SIGNAL-TRIGGERING-REF-CONDITIONAL')
                self.setChildElementOptionalRefType(child_element, "I-SIGNAL-TRIGGERING-REF", ref)

    def writePhysicalChannelCommConnectorRefs(self, element, channel):
        connectors = channel.getCommConnectorRefs()
        if len(connectors) > 0:
            connectors_tag = ET.SubElement(element, "COMM-CONNECTORS")
            for connector in connectors:
                child_element = ET.SubElement(connectors_tag, 'COMMUNICATION-CONNECTOR-REF-CONDITIONAL')
                self.setChildElementOptionalRefType(child_element, "COMMUNICATION-CONNECTOR-REF", connector)

    def writePhysicalChannelFrameTriggerings(self, element, channel):
        triggerings = channel.getFrameTriggerings()
        if len(triggerings) > 0:
            triggerings_tag = ET.SubElement(element, "FRAME-TRIGGERINGS")
            for triggering in triggerings:
                if isinstance(triggering, CanFrameTriggering):
                    self.writeCanFrameTriggering(triggerings_tag, triggering)
                elif isinstance(triggering, LinFrameTriggering):
                    self.writeLinFrameTriggering(triggerings_tag, triggering)
                elif isinstance(triggering, FlexrayFrameTriggering):
                    self.writeFlexrayFrameTriggering(triggerings_tag, triggering)
                else:
                    self.notImplemented("Unsupported Frame Triggering <%s>" % type(triggering))

    def writePhysicalChannelISignalTriggerings(self, element, channel):
        triggerings = channel.getISignalTriggerings()
        if len(triggerings) > 0:
            triggerings_tag = ET.SubElement(element, "I-SIGNAL-TRIGGERINGS")
            for triggering in triggerings:
                if isinstance(triggering, ISignalTriggering):
                    self.writeISignalTriggering(triggerings_tag, triggering)
                else:
                    self.notImplemented("Unsupported ISignalTriggering <%s>" % type(triggering))

    def writePhysicalChannelPduTriggerings(self, element, channel):
        triggerings = channel.getPduTriggerings()
        if len(triggerings) > 0:
            triggerings_tag = ET.SubElement(element, "PDU-TRIGGERINGS")
            for triggering in triggerings:
                if isinstance(triggering, PduTriggering):
                    self.writePduTriggering(triggerings_tag, triggering)
                else:
                    self.notImplemented("Unsupported PduTriggering <%s>" % type(triggering))

    def writePhysicalChannel(self, element: ET.Element, channel: PhysicalChannel):
        self.writeIdentifiable(element, channel)

        self.writePhysicalChannelCommConnectorRefs(element, channel)
        self.writePhysicalChannelFrameTriggerings(element, channel)
        self.writePhysicalChannelISignalTriggerings(element, channel)
        self.writePhysicalChannelPduTriggerings(element, channel)

    def writeCanPhysicalChannel(self, element: ET.Element, channel: CanPhysicalChannel):
        self.logger.debug("Set CanPhysicalChannel %s" % channel.getShortName())
        child_element = ET.SubElement(element, "CAN-PHYSICAL-CHANNEL")
        self.writePhysicalChannel(child_element, channel)

    def writeScheduleTableEntry(self, element: ET.Element, entry: ScheduleTableEntry):
        self.setChildElementOptionalTimeValue(element, "DELAY", entry.getDelay())
        self.setChildElementOptionalIntegerValue(element, "POSITION-IN-TABLE", entry.getPositionInTable())

    def setApplicationEntry(self, element: ET.Element, key: str, entry: ApplicationEntry):
        if entry is not None:
            child_element = ET.SubElement(element, key)
            self.writeScheduleTableEntry(child_element, entry)
            self.setChildElementOptionalRefType(child_element, "FRAME-TRIGGERING-REF", entry.getFrameTriggeringRef())

    def writeLinScheduleTableTableEntries(self, element: ET.Element, table: LinScheduleTable):
        entries = table.getTableEntries()
        if len(entries) > 0:
            child_element = ET.SubElement(element, "TABLE-ENTRYS")
            for entry in entries:
                if isinstance(entry, ApplicationEntry):
                    self.setApplicationEntry(child_element, "APPLICATION-ENTRY", entry)
                else:
                    self.notImplemented("Unsupported Schedule Table <%s>" % type(entry))

    def writeLinScheduleTable(self, element: ET.Element, table: LinScheduleTable):
        child_element = ET.SubElement(element, "LIN-SCHEDULE-TABLE")
        self.writeIdentifiable(child_element, table)
        self.setChildElementOptionalLiteral(child_element, "RESUME-POSITION", table.getResumePosition())
        self.setChildElementOptionalLiteral(child_element, "RUN-MODE", table.getRunMode())
        self.writeLinScheduleTableTableEntries(child_element, table)

    def writeLinPhysicalChannelScheduleTables(self, element: ET.Element, channel: LinPhysicalChannel):
        tables = channel.getScheduleTables()
        if len(tables) > 0:
            child_element = ET.SubElement(element, "SCHEDULE-TABLES")
            for table in tables:
                if isinstance(table, LinScheduleTable):
                    self.writeLinScheduleTable(child_element, table)
                else:
                    self.notImplemented("Unsupported Schedule Table <%s>" % type(table))

    def writeLinPhysicalChannel(self, element: ET.Element, channel: LinPhysicalChannel):
        self.logger.debug("Set LinPhysicalChannel %s" % channel.getShortName())
        child_element = ET.SubElement(element, "LIN-PHYSICAL-CHANNEL")
        self.writePhysicalChannel(child_element, channel)
        self.writeLinPhysicalChannelScheduleTables(child_element, channel)

    def setIpv6Configuration(self, element: ET.Element, configuration: Ipv6Configuration):
        if configuration is not None:
            child_element = ET.SubElement(element, "IPV-6-CONFIGURATION")
            self.setChildElementOptionalPositiveInteger(child_element, "ASSIGNMENT-PRIORITY", configuration.getAssignmentPriority())
            self.setChildElementOptionalLiteral(child_element, "DEFAULT-ROUTER", configuration.getDefaultRouter())
            self.setChildElementOptionalBooleanValue(child_element, "ENABLE-ANYCAST", configuration.getEnableAnycast())
            self.setChildElementOptionalPositiveInteger(child_element, "HOP-COUNT", configuration.getHopCount())
            self.setChildElementOptionalPositiveInteger(child_element, "IP-ADDRESS-PREFIX-LENGTH", configuration.getIpAddressPrefixLength())
            self.setChildElementOptionalLiteral(child_element, "IPV-6-ADDRESS", configuration.getIpv6Address())
            self.setChildElementOptionalLiteral(child_element, "IPV-6-ADDRESS-SOURCE", configuration.getIpv6AddressSource())

    def writeNetworkEndPointNetworkEndPointAddresses(self, element: ET.Element, addresses: List[NetworkEndpointAddress]):
        if len(addresses) > 0:
            child_element = ET.SubElement(element, "NETWORK-ENDPOINT-ADDRESSES")
            for address in addresses:
                if isinstance(address, Ipv6Configuration):
                    self.setIpv6Configuration(child_element, address)
                else:
                    self.notImplemented("Unsupported Network EndPoint Address <%s>" % type(address))

    def setDoIpEntity(self, element: ET.Element, key: str, entity: DoIpEntity):
        if entity is not None:
            child_element = ET.SubElement(element, key)
            self.setChildElementOptionalLiteral(child_element, "DO-IP-ENTITY-ROLE", entity.getDoIpEntityRole())

    def setInfrastructureServices(self, element: ET.Element, key: str, services: InfrastructureServices):
        if services is not None:
            child_element = ET.SubElement(element, key)
            self.setDoIpEntity(child_element, "DO-IP-ENTITY", services.getDoIpEntity())

    def writeNetworkEndPoint(self, element: ET.Element, end_point: NetworkEndpoint):
        self.logger.debug("Set NetworkEndpoint %s" % end_point.getShortName())
        child_element = ET.SubElement(element, "NETWORK-ENDPOINT")
        self.writeIdentifiable(child_element, end_point)
        self.setInfrastructureServices(child_element, "INFRASTRUCTURE-SERVICES", end_point.getInfrastructureServices())
        self.writeNetworkEndPointNetworkEndPointAddresses(child_element, end_point.getNetworkEndpointAddresses())
        self.setChildElementOptionalPositiveInteger(child_element, "PRIORITY", end_point.getPriority())

    def writeEthernetPhysicalChannelNetworkEndPoints(self, element: ET.Element, end_points: List[NetworkEndpoint]):
        if len(end_points) > 0:
            child_element = ET.SubElement(element, "NETWORK-ENDPOINTS")
            for end_point in end_points:
                self.writeNetworkEndPoint(child_element, end_point)

    def setSocketConnectionIpduIdentifier(self, element: ET.Element, identifier: SocketConnectionIpduIdentifier):
        if identifier is not None:
            child_element = ET.SubElement(element, "SOCKET-CONNECTION-IPDU-IDENTIFIER")
            self.setChildElementOptionalPositiveInteger(child_element, "HEADER-ID", identifier.getHeaderId())
            self.setChildElementOptionalLiteral(child_element, "PDU-COLLECTION-SEMANTICS", identifier.getPduCollectionSemantics())
            self.setChildElementOptionalLiteral(child_element, "PDU-COLLECTION-TRIGGER", identifier.getPduCollectionTrigger())
            self.setChildElementOptionalRefType(child_element, "PDU-REF", identifier.getPduRef())
            self.setChildElementOptionalRefType(child_element, "PDU-TRIGGERING-REF", identifier.getPduTriggeringRef())

    def setSocketConnectionPdus(self, element: ET.Element, key: str, pdus: List[SocketConnectionIpduIdentifier]):
        if len(pdus) > 0:
            child_element = ET.SubElement(element, key)
            for pdu in pdus:
                if isinstance(pdu, SocketConnectionIpduIdentifier):
                    self.setSocketConnectionIpduIdentifier(child_element, pdu)
                else:
                    self.notImplemented("Unsupported Pdu <%s>" % type(pdu))

    def setSocketConnection(self, element: ET.Element, connection: SocketConnection):
        if connection is not None:
            child_element = ET.SubElement(element, "SOCKET-CONNECTION")
            self.setChildElementOptionalBooleanValue(child_element, "CLIENT-IP-ADDR-FROM-CONNECTION-REQUEST", connection.getClientIpAddrFromConnectionRequest())    # noqa E501
            self.setChildElementOptionalBooleanValue(child_element, "CLIENT-PORT-FROM-CONNECTION-REQUEST", connection.getClientPortFromConnectionRequest())         # noqa E501
            self.setChildElementOptionalRefType(child_element, "CLIENT-PORT-REF", connection.getClientPortRef())
            self.setSocketConnectionPdus(child_element, "PDUS", connection.getPdus())
            self.setChildElementOptionalPositiveInteger(child_element, "PDU-COLLECTION-MAX-BUFFER-SIZE", connection.getPduCollectionMaxBufferSize())
            self.setChildElementOptionalTimeValue(child_element, "PDU-COLLECTION-TIMEOUT", connection.getPduCollectionTimeout())
            self.setChildElementOptionalLiteral(child_element, "RUNTIME-IP-ADDRESS-CONFIGURATION", connection.getRuntimeIpAddressConfiguration())
            self.setChildElementOptionalLiteral(child_element, "RUNTIME-PORT-CONFIGURATION", connection.getRuntimePortConfiguration())
            self.setChildElementOptionalLiteral(child_element, "SHORT-LABEL", connection.getShortLabel())

    def writeSocketConnectionBundleConnections(self, element: ET.Element, bundle: SocketConnectionBundle):
        connections = bundle.getBundledConnections()
        if len(connections) > 0:
            child_element = ET.SubElement(element, "BUNDLED-CONNECTIONS")
            for connection in connections:
                if isinstance(connection, SocketConnection):
                    self.setSocketConnection(child_element, connection)
                else:
                    self.notImplemented("Unsupported Bundled Connection <%s>" % type(connection))

    def writeSocketConnectionBundle(self, element: ET.Element, bundle: SocketConnectionBundle):
        if bundle is not None:
            child_element = ET.SubElement(element, "SOCKET-CONNECTION-BUNDLE")
            self.writeReferrable(child_element, bundle)
            self.writeSocketConnectionBundleConnections(child_element, bundle)
            self.setChildElementOptionalRefType(child_element, "SERVER-PORT-REF", bundle.getServerPortRef())

    def writeSoAdConfigConnectionBundles(self, element: ET.Element, config: SoAdConfig):
        bundles = config.getConnectionBundles()
        if len(bundles) > 0:
            child_element = ET.SubElement(element, "CONNECTION-BUNDLES")
            for bundle in bundles:
                if isinstance(bundle, SocketConnectionBundle):
                    self.writeSocketConnectionBundle(child_element, bundle)
                else:
                    self.notImplemented("Unsupported Connection Bundle <%s>" % type(bundle))

    def setTpPort(self, element: ET.SubElement, key: str, port: TpPort):
        if port is not None:
            child_element = ET.SubElement(element, key)
            self.setChildElementOptionalBooleanValue(child_element, "DYNAMICALLY-ASSIGNED", port.getDynamicallyAssigned())
            self.setChildElementOptionalPositiveInteger(child_element, "PORT-NUMBER", port.getPortNumber())

    def writeUdpTp(self, element: ET.Element, tp: UdpTp):
        child_element = ET.SubElement(element, "UDP-TP")
        self.setTpPort(child_element, "UDP-TP-PORT", tp.getUdpTpPort())

    def writeTcpTp(self, element: ET.Element, tp: TcpTp):
        child_element = ET.SubElement(element, "TCP-TP")
        self.setChildElementOptionalTimeValue(child_element, "KEEP-ALIVE-INTERVAL", tp.getKeepAliveInterval())
        self.setChildElementOptionalPositiveInteger(child_element, "KEEP-ALIVE-PROBES-MAX", tp.getKeepAliveProbesMax())
        self.setChildElementOptionalTimeValue(child_element, "KEEP-ALIVE-TIME", tp.getKeepAliveTime())
        self.setChildElementOptionalBooleanValue(child_element, "KEEP-ALIVES", tp.getKeepAlives())
        self.setChildElementOptionalLiteral(child_element, "NAGLES-ALGORITHM", tp.getNaglesAlgorithm())
        self.setTpPort(child_element, "TCP-TP-PORT", tp.getTcpTpPort())

    def writeGenericTp(self, element: ET.Element, tp: GenericTp):
        child_element = ET.SubElement(element, "GENERIC-TP")
        self.setChildElementOptionalLiteral(child_element, "TP-ADDRESS", tp.getTpAddress())
        self.setChildElementOptionalLiteral(child_element, "TP-TECHNOLOGY", tp.getTpTechnology())

    def writeTransportProtocolConfiguration(self, element: ET.Element, configuration: TransportProtocolConfiguration):
        if configuration is not None:
            child_element = ET.SubElement(element, "TP-CONFIGURATION")
            if isinstance(configuration, UdpTp):
                self.writeUdpTp(child_element, configuration)
            elif isinstance(configuration, TcpTp):
                self.writeTcpTp(child_element, configuration)
            elif isinstance(configuration, GenericTp):
                self.writeGenericTp(child_element, configuration)
            else:
                self.notImplemented("Unsupported TransportProtocolConfiguration <%s>" % type(configuration))

        return configuration
    
    def writeConsumedEventGroupRoutingGroupRefs(self, element: ET.Element, group: ConsumedEventGroup):
        refs = group.getRoutingGroupRefs()
        if len(refs) > 0:
            child_element = ET.SubElement(element, "ROUTING-GROUP-REFS")
            for ref in refs:
                self.setChildElementOptionalRefType(child_element, "ROUTING-GROUP-REF", ref)

    def setRequestResponseDelay(self, element: ET.Element, key: str, delay: RequestResponseDelay):
        if delay is not None:
            child_element = ET.SubElement(element, key)
            self.setChildElementOptionalTimeValue(child_element, "MAX-VALUE", delay.getMaxValue())
            self.setChildElementOptionalTimeValue(child_element, "MIN-VALUE", delay.getMinValue())

    def setSdClientConfig(self, element: ET.Element, key: str, config: SdClientConfig):
        if config is not None:
            child_element = ET.SubElement(element, key)

            self.setChildElementOptionalPositiveInteger(child_element, "CLIENT-SERVICE-MAJOR-VERSION", config.getClientServiceMajorVersion())
            self.setChildElementOptionalPositiveInteger(child_element, "CLIENT-SERVICE-MINOR-VERSION", config.getClientServiceMinorVersion())
            self.setInitialSdDelayConfig(child_element, "INITIAL-FIND-BEHAVIOR", config.getInitialFindBehavior())
            self.setRequestResponseDelay(child_element, "REQUEST-RESPONSE-DELAY", config.getRequestResponseDelay())
            self.setChildElementOptionalPositiveInteger(child_element, "TTL", config.getTtl())
    
    def writeConsumedEventGroup(self, element: ET.Element, group: ConsumedEventGroup):
        if group is not None:
            child_element = ET.SubElement(element, "CONSUMED-EVENT-GROUP")
            self.writeIdentifiable(child_element, group)
            self.setChildElementOptionalRefType(child_element, "APPLICATION-ENDPOINT-REF", group.getApplicationEndpointRef())
            self.setChildElementOptionalPositiveInteger(child_element, "EVENT-GROUP-IDENTIFIER", group.getEventGroupIdentifier())
            self.writeConsumedEventGroupRoutingGroupRefs(child_element, group)
            self.setSdClientConfig(child_element, "SD-CLIENT-CONFIG", group.getSdClientConfig())
    
    def writeConsumedServiceInstanceConsumedEventGroups(self, element: ET.Element, instance: ConsumedServiceInstance):
        groups = instance.getConsumedEventGroups()
        if len(groups) > 0:
            child_element = ET.SubElement(element, "CONSUMED-EVENT-GROUPS")
            for group in groups:
                if isinstance(group, ConsumedEventGroup):
                    self.writeConsumedEventGroup(child_element, group)
                else:
                    self.notImplemented("Unsupported ConsumedEventGroups <%s>" % type(group))
    
    def writeConsumedServiceInstance(self, element: ET.Element, instance: ConsumedServiceInstance):
        if instance is not None:
            child_element = ET.SubElement(element, "CONSUMED-SERVICE-INSTANCE")
            self.writeIdentifiable(child_element, instance)
            self.writeConsumedServiceInstanceConsumedEventGroups(child_element, instance)
            self.setChildElementOptionalRefType(child_element, "PROVIDED-SERVICE-INSTANCE-REF", instance.getProvidedServiceInstanceRef())
            self.setSdClientConfig(child_element, "SD-CLIENT-CONFIG", instance.getSdClientConfig())
    
    def writeSocketAddressApplicationEndpointConsumedServiceInstances(self, element: ET.Element, end_point: ApplicationEndpoint):
        instances = end_point.getConsumedServiceInstances()
        if len(instances) > 0:
            child_element = ET.SubElement(element, "CONSUMED-SERVICE-INSTANCES")
            for instance in instances:
                if isinstance(instance, ConsumedServiceInstance):
                    self.writeConsumedServiceInstance(child_element, instance)
                else:
                    self.notImplemented("Unsupported ConsumedServiceInstances <%s>" % type(instance))

    def setInitialSdDelayConfig(self, element: ET.Element, key: str, config: InitialSdDelayConfig):
        if config is not None:
            child_element = ET.SubElement(element, key)
            self.setChildElementOptionalTimeValue(child_element, "INITIAL-DELAY-MAX-VALUE", config.getInitialDelayMaxValue())
            self.setChildElementOptionalTimeValue(child_element, "INITIAL-DELAY-MIN-VALUE", config.getInitialDelayMinValue())
            self.setChildElementOptionalTimeValue(child_element, "INITIAL-REPETITIONS-BASE-DELAY", config.getInitialRepetitionsBaseDelay())
            self.setChildElementOptionalPositiveInteger(child_element, "INITIAL-REPETITIONS-MAX", config.getInitialRepetitionsMax())

    def setSdServerConfig(self, element: ET.Element, key: str, config: SdServerConfig):
        if config is not None:
            child_element = ET.SubElement(element, key)
            self.setInitialSdDelayConfig(child_element, "INITIAL-OFFER-BEHAVIOR", config.getInitialOfferBehavior())
            self.setChildElementOptionalTimeValue(child_element, "OFFER-CYCLIC-DELAY", config.getOfferCyclicDelay())
            self.setRequestResponseDelay(child_element, "REQUEST-RESPONSE-DELAY", config.getRequestResponseDelay())
            self.setChildElementOptionalPositiveInteger(child_element, "SERVER-SERVICE-MAJOR-VERSION", config.getServerServiceMajorVersion())
            self.setChildElementOptionalPositiveInteger(child_element, "SERVER-SERVICE-MINOR-VERSION", config.getServerServiceMinorVersion())
            self.setChildElementOptionalPositiveInteger(child_element, "TTL", config.getTtl())

    def writeEventHandler(self, element: ET.Element, handler: EventHandler):
        if handler is not None:
            child_element = ET.SubElement(element, "EVENT-HANDLER")
            self.writeIdentifiable(child_element, handler)
            self.setChildElementOptionalRefType(child_element, "APPLICATION-ENDPOINT-REF", handler.getApplicationEndpointRef())
            
            refs = handler.getConsumedEventGroupRefs()
            if len(refs) > 0:
                refs_tag = ET.SubElement(child_element, "CONSUMED-EVENT-GROUP-REFS")
                for ref in refs:
                    self.setChildElementOptionalRefType(refs_tag, "CONSUMED-EVENT-GROUP-REF", ref)

            self.setChildElementOptionalPositiveInteger(child_element, "MULTICAST-THRESHOLD", handler.getMulticastThreshold())

            refs = handler.getRoutingGroupRefs()
            if len(refs) > 0:
                refs_tag = ET.SubElement(child_element, "ROUTING-GROUP-REFS")
                for ref in refs:
                    self.setChildElementOptionalRefType(refs_tag, "ROUTING-GROUP-REF", ref)
            self.setSdServerConfig(child_element, "SD-SERVER-CONFIG", handler.getSdServerConfig())

    def writeProvidedServiceInstanceEventHandlers(self, element: ET.Element, instance: ProvidedServiceInstance):
        handlers = instance.getEventHandlers()
        if len(handlers) > 0:
            child_element = ET.SubElement(element, "EVENT-HANDLERS")
            for handler in handlers:
                if isinstance(handler, EventHandler):
                    self.writeEventHandler(child_element, handler)
                else:
                    self.notImplemented("Unsupported Event Handler <%s>" % type(handler))

    def writeProvidedServiceInstance(self, element: ET.Element, instance: ProvidedServiceInstance):
        if instance is not None:
            child_element = ET.SubElement(element, "PROVIDED-SERVICE-INSTANCE")
            self.writeIdentifiable(child_element, instance)
            self.writeProvidedServiceInstanceEventHandlers(child_element, instance)
            self.setChildElementOptionalPositiveInteger(child_element, "INSTANCE-IDENTIFIER", instance.getInstanceIdentifier())
            self.setSdServerConfig(child_element, "SD-SERVER-CONFIG", instance.getSdServerConfig())
            self.setChildElementOptionalPositiveInteger(child_element, "SERVICE-IDENTIFIER", instance.getServiceIdentifier())

    def writeSocketAddressApplicationEndpointProvidedServiceInstance(self, element: ET.Element, end_point: ApplicationEndpoint):
        instances = end_point.getProvidedServiceInstances()
        if len(instances) > 0:
            child_element = ET.SubElement(element, "PROVIDED-SERVICE-INSTANCES")
            for instance in instances:
                if isinstance(instance, ProvidedServiceInstance):
                    self.writeProvidedServiceInstance(child_element, instance)
                else:
                    self.notImplemented("Unsupported ConsumedServiceInstances <%s>" % type(instance))

    def writeSocketAddressApplicationEndpoint(self, element: ET.Element, address: SocketAddress):
        end_point = address.getApplicationEndpoint()
        if end_point is not None:
            child_element = ET.SubElement(element, "APPLICATION-ENDPOINT")
            self.writeIdentifiable(child_element, end_point)
            self.writeSocketAddressApplicationEndpointConsumedServiceInstances(child_element, end_point)
            self.setChildElementOptionalRefType(child_element, "NETWORK-ENDPOINT-REF", end_point.getNetworkEndpointRef())
            self.setChildElementOptionalPositiveInteger(child_element, "PRIORITY", end_point.getPriority())
            self.writeSocketAddressApplicationEndpointProvidedServiceInstance(child_element, end_point)
            self.writeTransportProtocolConfiguration(child_element, end_point.getTpConfiguration())

    def writeSocketAddressMulticastConnectorRefs(self, element: ET.Element, address: SocketAddress):
        refs = address.getMulticastConnectorRefs()
        if len(refs) > 0:
            child_element = ET.SubElement(element, "MULTICAST-CONNECTOR-REFS")
            for ref in refs:
                self.setChildElementOptionalRefType(child_element, "MULTICAST-CONNECTOR-REF", ref)

    def writeSocketAddress(self, element: ET.Element, address: SocketAddress):
        child_element = ET.SubElement(element, "SOCKET-ADDRESS")
        self.writeIdentifiable(child_element, address)
        self.writeSocketAddressApplicationEndpoint(child_element, address)
        self.writeSocketAddressMulticastConnectorRefs(child_element, address)
        self.setChildElementOptionalRefType(child_element, "CONNECTOR-REF", address.getConnectorRef())
        self.setChildElementOptionalPositiveInteger(child_element, "PORT-ADDRESS", address.getPortAddress())

    def writeSoAdConfigSocketAddresses(self, element: ET.Element, config: SoAdConfig):
        addresses = config.getSocketAddresses()
        if len(addresses) > 0:
            child_element = ET.SubElement(element, "SOCKET-ADDRESSS")
            for address in addresses:
                if isinstance(address, SocketAddress):
                    self.writeSocketAddress(child_element, address)
                else:
                    self.notImplemented("Unsupported Socket Address <%s>" % type(address))

    def writeSoAdConfig(self, element: ET.Element, key: str, config: SoAdConfig):
        if config is not None:
            child_element = ET.SubElement(element, key)
            self.writeSoAdConfigConnectionBundles(child_element, config)
            self.writeSoAdConfigSocketAddresses(child_element, config)

    def writeEthernetPhysicalChannelVlan(self, element: ET.Element, channel: EthernetPhysicalChannel):
        vlan = channel.getVlan()
        if vlan is not None:
            child_element = ET.SubElement(element, "VLAN")
            self.writeIdentifiable(child_element, vlan)
            self.setChildElementOptionalPositiveInteger(child_element, "VLAN-IDENTIFIER", vlan.getVlanIdentifier())

    def writeEthernetPhysicalChannel(self, element: ET.Element, channel: EthernetPhysicalChannel):
        self.logger.debug("Set EthernetPhysicalChannel %s" % channel.getShortName())
        child_element = ET.SubElement(element, "ETHERNET-PHYSICAL-CHANNEL")
        self.writePhysicalChannel(child_element, channel)
        self.writeEthernetPhysicalChannelNetworkEndPoints(child_element, channel.getNetworkEndpoints())
        self.writeSoAdConfig(child_element, "SO-AD-CONFIG", channel.getSoAdConfig())
        self.writeEthernetPhysicalChannelVlan(child_element, channel)

    def writeFlexrayPhysicalChannel(self, element: ET.Element, channel: FlexrayPhysicalChannel):
        self.logger.debug("Set FlexrayPhysicalChannel %s" % channel.getShortName())
        child_element = ET.SubElement(element, "FLEXRAY-PHYSICAL-CHANNEL")
        self.writePhysicalChannel(child_element, channel)
        self.setChildElementOptionalLiteral(child_element, "CHANNEL-NAME", channel.getChannelName())

    def writeCommunicationClusterPhysicalChannels(self, element: ET.Element, cluster: CommunicationCluster):
        channels = cluster.getPhysicalChannels()
        if len(channels) > 0:
            child_element = ET.SubElement(element, "PHYSICAL-CHANNELS")
            for channel in channels:
                if isinstance(channel, CanPhysicalChannel):
                    self.writeCanPhysicalChannel(child_element, channel)
                elif isinstance(channel, LinPhysicalChannel):
                    self.writeLinPhysicalChannel(child_element, channel)
                elif isinstance(channel, EthernetPhysicalChannel):
                    self.writeEthernetPhysicalChannel(child_element, channel)
                elif isinstance(channel, FlexrayPhysicalChannel):
                    self.writeFlexrayPhysicalChannel(child_element, channel)
                else:
                    self.notImplemented("Unsupported Physical Channel <%s>" % type(channel))

    def writeCommunicationCluster(self, element: ET.Element, cluster: CommunicationCluster):
        self.setChildElementOptionalNumericalValue(element, "BAUDRATE", cluster.getBaudrate())
        self.writeCommunicationClusterPhysicalChannels(element, cluster)
        self.setChildElementOptionalLiteral(element, "PROTOCOL-NAME", cluster.getProtocolName())
        self.setChildElementOptionalLiteral(element, "PROTOCOL-VERSION", cluster.getProtocolVersion())

    def setCanClusterBusOffRecovery(self, element: ET.Element, key: str, recovery: CanClusterBusOffRecovery):
        if recovery is not None:
            child_element = ET.SubElement(element, key)
            self.setChildElementOptionalPositiveInteger(child_element, "BOR-COUNTER-L-1-TO-L-2", recovery.getBorCounterL1ToL2())
            self.setChildElementOptionalTimeValue(child_element, "BOR-TIME-L-1", recovery.getBorTimeL1())
            self.setChildElementOptionalTimeValue(child_element, "BOR-TIME-L-2", recovery.getBorTimeL2())

    def writeAbstractCanCluster(self, element: ET.Element, cluster: AbstractCanCluster):
        self.setCanClusterBusOffRecovery(element, "BUS-OFF-RECOVERY", cluster.getBusOffRecovery())
        self.setChildElementOptionalNumericalValue(element, "CAN-FD-BAUDRATE", cluster.getCanFdBaudrate())
        self.setChildElementOptionalNumericalValue(element, "SPEED", cluster.getSpeed())

    def writeLinCluster(self, element: ET.Element, cluster: LinCluster):
        if cluster is not None:
            self.logger.debug("LinCluster %s" % cluster.getShortName())
            child_element = ET.SubElement(element, "LIN-CLUSTER")
            self.writeIdentifiable(child_element, cluster)
            
            child_element = ET.SubElement(child_element, "LIN-CLUSTER-VARIANTS")
            child_element = ET.SubElement(child_element, "LIN-CLUSTER-CONDITIONAL")
            self.writeCommunicationCluster(child_element, cluster)

    def writeCanCluster(self, element: ET.Element, cluster: CanCluster):
        if cluster is not None:
            self.logger.debug("CanCluster %s" % cluster.getShortName())
            child_element = ET.SubElement(element, "CAN-CLUSTER")
            self.writeIdentifiable(child_element, cluster)

            child_element = ET.SubElement(child_element, "CAN-CLUSTER-VARIANTS")
            child_element = ET.SubElement(child_element, "CAN-CLUSTER-CONDITIONAL")
            self.writeCommunicationCluster(child_element, cluster)
            self.writeAbstractCanCluster(child_element, cluster)

    def writeFlexrayCluster(self, element: ET.Element, cluster: FlexrayCluster):
        if cluster is not None:
            self.logger.debug("Write FlexrayCluster <%s>" % cluster.getShortName())
            child_element = ET.SubElement(element, "FLEXRAY-CLUSTER")
            self.writeIdentifiable(child_element, cluster)

            child_element = ET.SubElement(child_element, "FLEXRAY-CLUSTER-VARIANTS")
            child_element = ET.SubElement(child_element, "FLEXRAY-CLUSTER-CONDITIONAL")
            self.writeCommunicationCluster(child_element, cluster)

            self.setChildElementOptionalIntegerValue(child_element, "ACTION-POINT-OFFSET", cluster.getActionPointOffset())
            self.setChildElementOptionalTimeValue(child_element, "BIT", cluster.getBit())
            self.setChildElementOptionalIntegerValue(child_element, "CAS-RX-LOW-MAX", cluster.getCasRxLowMax())
            self.setChildElementOptionalIntegerValue(child_element, "COLD-START-ATTEMPTS", cluster.getColdStartAttempts())
            self.setChildElementOptionalTimeValue(child_element, "CYCLE", cluster.getCycle())
            self.setChildElementOptionalIntegerValue(child_element, "CYCLE-COUNT-MAX", cluster.getCycleCountMax())
            self.setChildElementOptionalBooleanValue(child_element, "DETECT-NIT-ERROR", cluster.getDetectNitError())
            self.setChildElementOptionalIntegerValue(child_element, "DYNAMIC-SLOT-IDLE-PHASE", cluster.getDynamicSlotIdlePhase())
            self.setChildElementOptionalIntegerValue(child_element, "IGNORE-AFTER-TX", cluster.getIgnoreAfterTx())
            self.setChildElementOptionalIntegerValue(child_element, "LISTEN-NOISE", cluster.getListenNoise())
            self.setChildElementOptionalIntegerValue(child_element, "MACRO-PER-CYCLE", cluster.getMacroPerCycle())
            self.setChildElementOptionalTimeValue(child_element, "MACROTICK-DURATION", cluster.getMacrotickDuration())
            self.setChildElementOptionalIntegerValue(child_element, "MAX-WITHOUT-CLOCK-CORRECTION-FATAL", cluster.getMaxWithoutClockCorrectionFatal())
            self.setChildElementOptionalIntegerValue(child_element, "MAX-WITHOUT-CLOCK-CORRECTION-PASSIVE", cluster.getMaxWithoutClockCorrectionPassive())  # noqa E501
            self.setChildElementOptionalIntegerValue(child_element, "MINISLOT-ACTION-POINT-OFFSET", cluster.getMinislotActionPointOffset())
            self.setChildElementOptionalIntegerValue(child_element, "MINISLOT-DURATION", cluster.getMinislotDuration())
            self.setChildElementOptionalIntegerValue(child_element, "NETWORK-IDLE-TIME", cluster.getNetworkIdleTime())
            self.setChildElementOptionalIntegerValue(child_element, "NETWORK-MANAGEMENT-VECTOR-LENGTH", cluster.getNetworkManagementVectorLength())
            self.setChildElementOptionalIntegerValue(child_element, "NUMBER-OF-MINISLOTS", cluster.getNumberOfMinislots())
            self.setChildElementOptionalIntegerValue(child_element, "NUMBER-OF-STATIC-SLOTS", cluster.getNumberOfStaticSlots())
            self.setChildElementOptionalIntegerValue(child_element, "OFFSET-CORRECTION-START", cluster.getOffsetCorrectionStart())
            self.setChildElementOptionalIntegerValue(child_element, "PAYLOAD-LENGTH-STATIC", cluster.getPayloadLengthStatic())
            self.setChildElementOptionalIntegerValue(child_element, "SAFETY-MARGIN", cluster.getSafetyMargin())
            self.setChildElementOptionalTimeValue(child_element, "SAMPLE-CLOCK-PERIOD", cluster.getSampleClockPeriod())
            self.setChildElementOptionalIntegerValue(child_element, "STATIC-SLOT-DURATION", cluster.getStaticSlotDuration())
            self.setChildElementOptionalIntegerValue(child_element, "SYNC-FRAME-ID-COUNT-MAX", cluster.getSyncFrameIdCountMax())
            self.setChildElementOptionalIntegerValue(child_element, "TRANSMISSION-START-SEQUENCE-DURATION", cluster.getTransmissionStartSequenceDuration()) # noqa E501
            self.setChildElementOptionalIntegerValue(child_element, "WAKEUP-RX-IDLE", cluster.getWakeupRxIdle())
            self.setChildElementOptionalIntegerValue(child_element, "WAKEUP-RX-LOW", cluster.getWakeupRxLow())
            self.setChildElementOptionalIntegerValue(child_element, "WAKEUP-RX-WINDOW", cluster.getWakeupRxWindow())
            self.setChildElementOptionalIntegerValue(child_element, "WAKEUP-TX-ACTIVE", cluster.getWakeupTxActive())
            self.setChildElementOptionalIntegerValue(child_element, "WAKEUP-TX-IDLE", cluster.getWakeupTxIdle())

    def writeCollectionElementRefs(self, element: ET.Element, collection: Collection):
        refs = collection.getElementRefs()
        if len(refs) > 0:
            child_element = ET.SubElement(element, "ELEMENT-REFS")
            for ref in refs:
                self.setChildElementOptionalRefType(child_element, "ELEMENT-REF", ref)

    def writeCollectionSourceElementRefs(self, element: ET.Element, collection: Collection):
        refs = collection.getSourceElementRefs()
        if len(refs) > 0:
            child_element = ET.SubElement(element, "SOURCE-ELEMENT-REFS")
            for ref in refs:
                self.setChildElementOptionalRefType(child_element, "SOURCE-ELEMENT-REF", ref)

    def writeCollection(self, element: ET.Element, collection: Collection):
        if collection is not None:
            child_element = ET.SubElement(element, "COLLECTION")
            self.writeARElement(child_element, collection)
            self.setChildElementOptionalLiteral(child_element, "AUTO-COLLECT", collection.getAutoCollect())
            self.setChildElementOptionalLiteral(child_element, "ELEMENT-ROLE", collection.getElementRole())
            self.writeCollectionElementRefs(child_element, collection)
            self.writeCollectionSourceElementRefs(child_element, collection)

    def writeKeywordClassifications(self, element: ET.Element, keyword: Keyword):
        classifications = keyword.getClassifications()
        if len(classifications) > 0:
            child_element = ET.SubElement(element, "CLASSIFICATIONS")
            for classification in classifications:
                self.setChildElementOptionalLiteral(child_element, "CLASSIFICATION", classification)

    def writeKeyword(self, element: ET.Element, keyword: Keyword):
        if keyword is not None:
            # self.logger.debug("Write Keyword <%s>" % keyword.getShortName())
            child_element = ET.SubElement(element, "KEYWORD")
            self.writeIdentifiable(child_element, keyword)
            self.setChildElementOptionalLiteral(child_element, "ABBR-NAME", keyword.getAbbrName())
            self.writeKeywordClassifications(child_element, keyword)

    def writeKeywordSetKeywords(self, element: ET.Element, keyword_set: KeywordSet):
        keywords = keyword_set.getKeywords()
        if len(keywords) > 0:
            child_element = ET.SubElement(element, "KEYWORDS")
            for keyword in keywords:
                if isinstance(keyword, Keyword):
                    self.writeKeyword(child_element, keyword)
                else:
                    self.notImplemented("Unsupported Keyword <%s>" % type(keyword))

    def writeKeywordSet(self, element: ET.Element, keyword_set: KeywordSet):
        if keyword_set is not None:
            self.logger.debug("Write KeywordSet <%s>" % keyword_set.getShortName())
            child_element = ET.SubElement(element, "KEYWORD-SET")
            self.writeARElement(child_element, keyword_set)
            self.writeKeywordSetKeywords(child_element, keyword_set)

    def writePortPrototypeBlueprint(self, element: ET.Element, blueprint: PortPrototypeBlueprint):
        if blueprint is not None:
            self.logger.debug("Write PortPrototypeBlueprint <%s>" % blueprint.getShortName())
            child_element = ET.SubElement(element, "PORT-PROTOTYPE-BLUEPRINT")
            self.writeARElement(child_element, blueprint)
            self.setChildElementOptionalRefType(child_element, "INTERFACE-REF", blueprint.getInterfaceRef())

    def writeMacMulticastGroup(self, element: ET.Element, group: MacMulticastGroup):
        if group is not None:
            child_element = ET.SubElement(element, "MAC-MULTICAST-GROUP")
            self.writeIdentifiable(child_element, group)
            self.setChildElementOptionalLiteral(child_element, "MAC-MULTICAST-ADDRESS", group.getMacMulticastAddress())

    def writeEthernetClusterMacMulticastGroups(self, element: ET.Element, cluster: EthernetCluster):
        groups = cluster.getMacMulticastGroups()
        if len(groups) > 0:
            child_element = ET.SubElement(element, "MAC-MULTICAST-GROUPS")
            for group in groups:
                if isinstance(group, MacMulticastGroup):
                    self.writeMacMulticastGroup(child_element, group)
                else:
                    self.notImplemented("Unsupported assigned data type <%s>" % type(group))

    def writeEthernetCluster(self, element: ET.Element, cluster: EthernetCluster):
        self.logger.debug("Set EthernetCluster %s" % cluster.getShortName())
        child_element = ET.SubElement(element, "ETHERNET-CLUSTER")
        self.writeARElement(child_element, cluster)

        child_element = ET.SubElement(child_element, "ETHERNET-CLUSTER-VARIANTS")
        child_element = ET.SubElement(child_element, "ETHERNET-CLUSTER-CONDITIONAL")
        self.writeCommunicationCluster(child_element, cluster)
        self.writeEthernetClusterMacMulticastGroups(child_element, cluster)

    def writeCanFrame(self, element: ET.Element, frame: CanFrame):
        self.logger.debug("Write CanFrame %s" % frame.getShortName())
        child_element = ET.SubElement(element, "CAN-FRAME")
        self.writeFrame(child_element, frame)

    def writeCommConnectorPort(self, element: ET.Element, port: CommConnectorPort):
        self.writeIdentifiable(element, port)
        self.setChildElementOptionalLiteral(element, "COMMUNICATION-DIRECTION", port.getCommunicationDirection())

    def writeFramePort(self, element: ET.Element, port: FramePort):
        child_element = ET.SubElement(element, "FRAME-PORT")
        self.writeCommConnectorPort(child_element, port)

    def writeIPduPort(self, element: ET.Element, port: IPduPort):
        child_element = ET.SubElement(element, "I-PDU-PORT")
        self.writeCommConnectorPort(child_element, port)
        self.setChildElementOptionalPositiveInteger(child_element, "KEY-ID", port.getKeyId())
        self.setChildElementOptionalBooleanValue(child_element, "RX-SECURITY-VERIFICATION", port.getRxSecurityVerification())
        self.setChildElementOptionalBooleanValue(child_element, "USE-AUTH-DATA-FRESHNESS", port.getUseAuthDataFreshness())

    def writeISignalPort(self, element: ET.Element, port: ISignalPort):
        child_element = ET.SubElement(element, "I-SIGNAL-PORT")
        self.writeCommConnectorPort(child_element, port)
        self.setChildElementOptionalTimeValue(child_element, "TIMEOUT", port.getTimeout())

    def writeCommunicationConnectorEcuCommPortInstances(self, element: ET.Element, connector: CommunicationConnector):
        self.logger.debug("write EcuCommPortInstances of CommunicationConnector %s" % connector.getShortName())
        ports = connector.getEcuCommPortInstances()
        if len(ports) > 0:
            instances_tag = ET.SubElement(element, "ECU-COMM-PORT-INSTANCES")
            for port in ports:
                if isinstance(port, FramePort):
                    self.writeFramePort(instances_tag, port)
                elif isinstance(port, IPduPort):
                    self.writeIPduPort(instances_tag, port)
                elif isinstance(port, ISignalPort):
                    self.writeISignalPort(instances_tag, port)
                else:
                    self.notImplemented("Unsupported CommConnectorPort <%s>" % type(port))

    def writeCommunicationController(self, element: ET.Element, controller: CommunicationController):
        self.setChildElementOptionalBooleanValue(element, "WAKE-UP-BY-CONTROLLER-SUPPORTED", controller.getWakeUpByControllerSupported())

    def setCanControllerFdConfiguration(self, element: ET.Element, key: str, configuration: CanControllerFdConfiguration):
        if configuration is not None:
            pass
            # child_element = ET.SubElement(element, key)
            # TODO: need to implemented
    
    def setCanControllerFdConfigurationRequirements(self, element: ET.Element, key: str, requirements: CanControllerFdConfigurationRequirements):
        if requirements is not None:
            child_element = ET.SubElement(element, key)
            self.setChildElementOptionalIntegerValue(child_element, "MAX-NUMBER-OF-TIME-QUANTA-PER-BIT", requirements.getMaxNumberOfTimeQuantaPerBit())     # noqa E501
            self.setChildElementOptionalFloatValue(child_element, "MAX-SAMPLE-POINT", requirements.getMaxSamplePoint())
            self.setChildElementOptionalFloatValue(child_element, "MAX-SYNC-JUMP-WIDTH", requirements.getMaxSyncJumpWidth())
            self.setChildElementOptionalTimeValue(child_element, "MAX-TRCV-DELAY-COMPENSATION-OFFSET", requirements.getMaxTrcvDelayCompensationOffset())    # noqa E501
            self.setChildElementOptionalIntegerValue(child_element, "MIN-NUMBER-OF-TIME-QUANTA-PER-BIT", requirements.getMinNumberOfTimeQuantaPerBit())     # noqa E501
            self.setChildElementOptionalFloatValue(child_element, "MIN-SAMPLE-POINT", requirements.getMinSamplePoint())
            self.setChildElementOptionalFloatValue(child_element, "MIN-SYNC-JUMP-WIDTH", requirements.getMinSyncJumpWidth())
            self.setChildElementOptionalTimeValue(child_element, "MIN-TRCV-DELAY-COMPENSATION-OFFSET", requirements.getMinTrcvDelayCompensationOffset())    # noqa E501
            self.setChildElementOptionalBooleanValue(child_element, "TX-BIT-RATE-SWITCH", requirements.getTxBitRateSwitch())

    def writeAbstractCanCommunicationControllerAttributes(self, element: ET.Element, attributes: AbstractCanCommunicationControllerAttributes):
        self.setCanControllerFdConfiguration(element, "CAN-CONTROLLER-FD-CONFIGURATION", attributes.getCanControllerFdAttributes())
        self.setCanControllerFdConfigurationRequirements(element, "CAN-CONTROLLER-FD-REQUIREMENTS", attributes.getCanControllerFdRequirements())

    def writeCanControllerConfigurationRequirements(self, element: ET.Element, requirements: CanControllerConfigurationRequirements):
        if requirements is not None:
            child_element = ET.SubElement(element, "CAN-CONTROLLER-CONFIGURATION-REQUIREMENTS")
            self.writeAbstractCanCommunicationControllerAttributes(child_element, requirements)
            self.setChildElementOptionalIntegerValue(child_element, "MAX-NUMBER-OF-TIME-QUANTA-PER-BIT", requirements.getMaxNumberOfTimeQuantaPerBit())     # noqa E501
            self.setChildElementOptionalFloatValue(child_element, "MAX-SAMPLE-POINT", requirements.getMaxSamplePoint())
            self.setChildElementOptionalFloatValue(child_element, "MAX-SYNC-JUMP-WIDTH", requirements.getMaxSyncJumpWidth())
            self.setChildElementOptionalIntegerValue(child_element, "MIN-NUMBER-OF-TIME-QUANTA-PER-BIT", requirements.getMinNumberOfTimeQuantaPerBit())     # noqa E501
            self.setChildElementOptionalFloatValue(child_element, "MIN-SAMPLE-POINT", requirements.getMinSamplePoint())
            self.setChildElementOptionalFloatValue(child_element, "MIN-SYNC-JUMP-WIDTH", requirements.getMinSyncJumpWidth())

    def writeAbstractCanCommunicationControllerCanControllerAttributes(self, element: ET.SubElement, controller: AbstractCanCommunicationController):
        attributes = controller.getCanControllerAttributes()
        if attributes is not None:
            child_element = ET.SubElement(element, "CAN-CONTROLLER-ATTRIBUTES")
            if isinstance(attributes, CanControllerConfigurationRequirements):
                self.writeCanControllerConfigurationRequirements(child_element, attributes)
            else:
                self.notImplemented("Unsupported CanControllerAttributes <%s>" % type(attributes))

    def writeAbstractCanCommunicationController(self, element: ET.Element, controller: AbstractCanCommunicationController):
        self.writeCommunicationController(element, controller)
        self.writeAbstractCanCommunicationControllerCanControllerAttributes(element, controller)

    def writeCanCommunicationController(self, element: ET.Element, controller: CanCommunicationController):
        child_element = ET.SubElement(element, "CAN-COMMUNICATION-CONTROLLER")
        self.logger.debug("Write CanCommunicationController %s" % controller.getShortName())
        self.writeIdentifiable(child_element, controller)
        variants_tag = ET.SubElement(child_element, "CAN-COMMUNICATION-CONTROLLER-VARIANTS")
        cond_tag = ET.SubElement(variants_tag, "CAN-COMMUNICATION-CONTROLLER-CONDITIONAL")
        self.writeAbstractCanCommunicationController(cond_tag, controller)

    def writeCouplingPortSchedulerCouplingPortStructuralElement(self, element: ET.Element, item: CouplingPortStructuralElement):
        self.writeIdentifiable(element, item)

    def writeCouplingPortFifo(self, element: ET.Element, fifo: CouplingPortFifo):
        if fifo is not None:
            child_element = ET.SubElement(element, "COUPLING-PORT-FIFO")
            self.writeCouplingPortSchedulerCouplingPortStructuralElement(child_element, fifo)

    def writeCouplingPortScheduler(self, element: ET.Element, scheduler: CouplingPortScheduler):
        if scheduler is not None:
            child_element = ET.SubElement(element, "COUPLING-PORT-SCHEDULER")
            self.writeCouplingPortSchedulerCouplingPortStructuralElement(child_element, scheduler)
            self.setChildElementOptionalLiteral(child_element, "PORT-SCHEDULER", scheduler.getPortScheduler())

    def writeCouplingPortDetailsCouplingPortStructuralElements(self, element: ET.Element, details: CouplingPortDetails):
        items = details.getCouplingPortStructuralElements()
        if len(items) > 0:
            child_element = ET.SubElement(element, "COUPLING-PORT-STRUCTURAL-ELEMENTS")
            for item in items:
                if isinstance(item, CouplingPortFifo):
                    self.writeCouplingPortFifo(child_element, item)
                elif isinstance(item, CouplingPortScheduler):
                    self.writeCouplingPortScheduler(child_element, item)
                else:
                    self.notImplemented("Unsupported CouplingPortStructuralElement <%s>" % type(item))
    
    def writeEthernetPriorityRegeneration(self, element: ET.Element, regeneration: EthernetPriorityRegeneration):
        if regeneration is not None:
            child_element = ET.SubElement(element, "ETHERNET-PRIORITY-REGENERATION")
            self.writeReferrable(child_element, regeneration)
            self.setChildElementOptionalPositiveInteger(child_element, "INGRESS-PRIORITY", regeneration.getIngressPriority())
            self.setChildElementOptionalPositiveInteger(child_element, "REGENERATED-PRIORITY", regeneration.getRegeneratedPriority())

    def writeCouplingPortDetailsEthernetPriorityRegenerations(self, element: ET.Element, details: CouplingPortDetails):
        regenerations = details.getEthernetPriorityRegenerations()
        if len(regenerations) > 0:
            child_element = ET.SubElement(element, "ETHERNET-PRIORITY-REGENERATIONS")
            for regeneration in regenerations:
                if isinstance(regeneration, EthernetPriorityRegeneration):
                    self.writeEthernetPriorityRegeneration(child_element, regeneration)
                else:
                    self.notImplemented("Unsupported EthernetPriorityRegeneration <%s>" % type(regeneration))

    def setCouplingPortDetails(self, element: ET.Element, key: str, details: CouplingPortDetails):
        if details is not None:
            child_element = ET.SubElement(element, key)
            self.writeCouplingPortDetailsCouplingPortStructuralElements(child_element, details)
            self.writeCouplingPortDetailsEthernetPriorityRegenerations(child_element, details)
            self.setChildElementOptionalRefType(child_element, "LAST-EGRESS-SCHEDULER-REF", details.getLastEgressSchedulerRef())

    def writeVlanMembership(self, element: ET.Element, membership: VlanMembership):
        if membership is not None:
            child_element = ET.SubElement(element, "VLAN-MEMBERSHIP")
            self.setChildElementOptionalLiteral(child_element, "SEND-ACTIVITY", membership.getSendActivity())
            self.setChildElementOptionalRefType(child_element, "VLAN-REF", membership.getVlanRef())
    
    def writeCouplingPortVlanMemberships(self, element: ET.Element, port: CouplingPort):
        memberships = port.getVlanMemberships()
        if len(memberships) > 0:
            child_element = ET.SubElement(element, "VLAN-MEMBERSHIPS")
            for membership in memberships:
                if isinstance(membership, VlanMembership):
                    self.writeVlanMembership(child_element, membership)
                else:
                    self.notImplemented("Unsupported VlanMembership <%s>" % type(membership))

    def writeCouplingPort(self, element: ET.Element, port: CouplingPort):
        child_element = ET.SubElement(element, "COUPLING-PORT")
        self.writeIdentifiable(child_element, port)
        self.setCouplingPortDetails(child_element, "COUPLING-PORT-DETAILS", port.getCouplingPortDetails())
        self.setChildElementOptionalLiteral(child_element, "MAC-LAYER-TYPE", port.getMacLayerType())
        self.writeCouplingPortVlanMemberships(child_element, port)

    def writeEthernetCommunicationControllerCouplingPorts(self, element: ET.Element, controller: EthernetCommunicationController):
        ports = controller.getCouplingPorts()
        if len(ports) > 0:
            child_element = ET.SubElement(element, "COUPLING-PORTS")
            for port in ports:
                if isinstance(port, CouplingPort):
                    self.writeCouplingPort(child_element, port)
                else:
                    self.notImplemented("Unsupported Coupling Port <%s>" % type(port))

    def writeEthernetCommunicationController(self, element: ET.Element, controller: EthernetCommunicationController):
        child_element = ET.SubElement(element, "ETHERNET-COMMUNICATION-CONTROLLER")
        self.logger.debug("Write EthernetCommunicationController %s" % controller.getShortName())
        self.writeIdentifiable(child_element, controller)
        variants_tag = ET.SubElement(child_element, "ETHERNET-COMMUNICATION-CONTROLLER-VARIANTS")
        cond_tag = ET.SubElement(variants_tag, "ETHERNET-COMMUNICATION-CONTROLLER-CONDITIONAL")
        self.writeCommunicationController(cond_tag, controller)
        self.writeEthernetCommunicationControllerCouplingPorts(cond_tag, controller)

    def writeEcuInstanceCommControllers(self, element: ET.Element, instance: EcuInstance):
        controllers = instance.getCommControllers()
        if len(controllers) > 0:
            child_element = ET.SubElement(element, "COMM-CONTROLLERS")
            for controller in controllers:
                if isinstance(controller, CanCommunicationController):
                    self.writeCanCommunicationController(child_element, controller)
                elif isinstance(controller, EthernetCommunicationController):
                    self.writeEthernetCommunicationController(child_element, controller)
                elif isinstance(controller, LinMaster):
                    self.writeLinMaster(child_element, controller)
                elif isinstance(controller, FlexrayCommunicationController):
                    self.writeFlexrayCommunicationController(child_element, controller)
                else:
                    self.notImplemented("Unsupported Communication Controller <%s>" % type(controller))

    def writeCommunicationConnector(self, element: ET.Element, connector: CommunicationConnector):
        self.writeIdentifiable(element, connector)
        self.setChildElementOptionalRefType(element, "COMM-CONTROLLER-REF", connector.getCommControllerRef())
        self.writeCommunicationConnectorEcuCommPortInstances(element, connector)
        self.setChildElementOptionalLiteral(element, "PNC-GATEWAY-TYPE", connector.getPncGatewayType())

    def writeCanCommunicationConnector(self, element: ET.Element, connector: CanCommunicationConnector):
        self.logger.debug("Write CanCommunicationConnector %s" % connector.getShortName())
        self.writeCommunicationConnector(element, connector)

    def writeEthernetCommunicationConnectorNetworkEndpointRefs(self, element: ET.Element, connector: EthernetCommunicationConnector):
        refs = connector.getNetworkEndpointRefs()
        if len(refs) > 0:
            child_element = ET.SubElement(element, "NETWORK-ENDPOINT-REFS")
            for ref in refs:
                self.setChildElementOptionalRefType(child_element, "NETWORK-ENDPOINT-REF", ref)

    def writeEthernetCommunicationConnector(self, element: ET.Element, connector: EthernetCommunicationConnector):
        self.logger.debug("Write EthernetCommunicationConnector %s" % connector.getShortName())
        self.writeCommunicationConnector(element, connector)
        self.setChildElementOptionalPositiveInteger(element, "MAXIMUM-TRANSMISSION-UNIT", connector.getMaximumTransmissionUnit())
        self.writeEthernetCommunicationConnectorNetworkEndpointRefs(element, connector)

    def writeLinCommunicationConnector(self, element: ET.Element, connector: LinCommunicationConnector):
        self.logger.debug("Write LinCommunicationConnector %s" % connector.getShortName())
        self.writeCommunicationConnector(element, connector)

    def writeFlexrayCommunicationConnector(self, element: ET.Element, connector: FlexrayCommunicationConnector):
        self.logger.debug("Write FlexrayCommunicationConnector %s" % connector.getShortName())
        self.writeCommunicationConnector(element, connector)

    def writeEcuInstanceConnectors(self, element: ET.Element, instance: EcuInstance):
        connectors = instance.getConnectors()
        if len(connectors) > 0:
            connectors_tag = ET.SubElement(element, "CONNECTORS")
            for connector in connectors:
                if isinstance(connector, CanCommunicationConnector):
                    child_element = ET.SubElement(connectors_tag, "CAN-COMMUNICATION-CONNECTOR")
                    self.writeCanCommunicationConnector(child_element, connector)
                elif isinstance(connector, EthernetCommunicationConnector):
                    child_element = ET.SubElement(connectors_tag, "ETHERNET-COMMUNICATION-CONNECTOR")
                    self.writeEthernetCommunicationConnector(child_element, connector)
                elif isinstance(connector, LinCommunicationConnector):
                    child_element = ET.SubElement(connectors_tag, "LIN-COMMUNICATION-CONNECTOR")
                    self.writeLinCommunicationConnector(child_element, connector)
                elif isinstance(connector, FlexrayCommunicationConnector):
                    child_element = ET.SubElement(connectors_tag, "FLEXRAY-COMMUNICATION-CONNECTOR")
                    self.writeFlexrayCommunicationConnector(child_element, connector)
                else:
                    self.notImplemented("Unsupported Communication connector <%s>" % type(connector))

    def writeEcuInstanceAssociatedComIPduGroupRefs(self, element: ET.Element, instance: EcuInstance):
        refs = instance.getAssociatedComIPduGroupRefs()
        if len(refs) > 0:
            child_element = ET.SubElement(element, "ASSOCIATED-COM-I-PDU-GROUP-REFS")
            for ref in refs:
                self.setChildElementOptionalRefType(child_element, "ASSOCIATED-COM-I-PDU-GROUP-REF", ref)

    def writeEcuInstance(self, element: ET.Element, instance: EcuInstance):
        self.logger.debug("EcuInstance %s" % instance.getShortName())
        child_element = ET.SubElement(element, "ECU-INSTANCE")
        self.writeIdentifiable(child_element, instance)
        self.writeEcuInstanceAssociatedComIPduGroupRefs(child_element, instance)
        self.setChildElementOptionalTimeValue(child_element, "COM-CONFIGURATION-GW-TIME-BASE", instance.getComConfigurationGwTimeBase())
        self.setChildElementOptionalTimeValue(child_element, "COM-CONFIGURATION-RX-TIME-BASE", instance.getComConfigurationRxTimeBase())
        self.setChildElementOptionalTimeValue(child_element, "COM-CONFIGURATION-TX-TIME-BASE", instance.getComConfigurationTxTimeBase())
        self.setChildElementOptionalBooleanValue(child_element, "COM-ENABLE-MDT-FOR-CYCLIC-TRANSMISSION", instance.getComEnableMDTForCyclicTransmission())      # noqa E501
        self.writeEcuInstanceCommControllers(child_element, instance)
        self.writeEcuInstanceConnectors(child_element, instance)
        self.setChildElementOptionalIntegerValue(child_element, "DIAGNOSTIC-ADDRESS", instance.getDiagnosticAddress())
        self.setChildElementOptionalBooleanValue(child_element, "SLEEP-MODE-SUPPORTED", instance.getSleepModeSupported())
        self.setChildElementOptionalBooleanValue(child_element, "WAKE-UP-OVER-BUS-SUPPORTED", instance.getWakeUpOverBusSupported())

    def writeSystemSignalGroup(self, element: ET.Element, group: SystemSignalGroup):
        self.logger.debug("Write SystemSignalGroup %s" % group.getShortName())
        child_element = ET.SubElement(element, "SYSTEM-SIGNAL-GROUP")
        self.writeIdentifiable(child_element, group)
        signal_refs = group.getSystemSignalRefs()
        if len(signal_refs) > 0:
            signal_refs_tag = ET.SubElement(child_element, "SYSTEM-SIGNAL-REFS")
            for signal_ref in signal_refs:
                self.setChildElementOptionalRefType(signal_refs_tag, "SYSTEM-SIGNAL-REF", signal_ref)

    def writeSenderReceiverToSignalMapping(self, element: ET.Element, mapping: SenderReceiverToSignalMapping):
        child_element = ET.SubElement(element, "SENDER-RECEIVER-TO-SIGNAL-MAPPING")
        self.setChildElementOptionalLiteral(child_element, "COMMUNICATION-DIRECTION", mapping.getCommunicationDirection())
        self.setVariableDataPrototypeInSystemInstanceRef(child_element, "DATA-ELEMENT-IREF", mapping.getDataElementIRef())
        self.setChildElementOptionalRefType(child_element, "SYSTEM-SIGNAL-REF", mapping.getSystemSignalRef())

    def writeSenderRecCompositeTypeMapping(self, element: ET.Element, mapping: SenderRecCompositeTypeMapping):
        self.writeARObjectAttributes(element, mapping)

    def writeSenderRecRecordElementMapping(self, element: ET.Element, mapping: SenderRecRecordElementMapping):
        if mapping is not None:
            child_element = ET.SubElement(element, "SENDER-REC-RECORD-ELEMENT-MAPPING")
            self.writeARObjectAttributes(child_element, mapping)
            self.setChildElementOptionalRefType(child_element, "APPLICATION-RECORD-ELEMENT-REF", mapping.getApplicationRecordElementRef())
            self.setChildElementOptionalRefType(child_element, "IMPLEMENTATION-RECORD-ELEMENT-REF", mapping.getImplementationRecordElementRef())
            self.setChildElementOptionalRefType(child_element, "SYSTEM-SIGNAL-REF", mapping.getSystemSignalRef())

    def writeSenderRecArrayTypeMappingRecordElementMapping(self, element: ET.Element, mapping: SenderRecRecordTypeMapping):
        record_element_mappings = mapping.getRecordElementMappings()
        if len(record_element_mappings) > 0:
            child_element = ET.SubElement(element, "RECORD-ELEMENT-MAPPINGS")
            for record_element_mapping in record_element_mappings:
                if isinstance(record_element_mapping, SenderRecRecordElementMapping):
                    self.writeSenderRecRecordElementMapping(child_element, record_element_mapping)
                else:
                    self.notImplemented("Unsupported RecordElementMapping %s" % type(record_element_mapping))
    
    def writeSenderRecRecordTypeMapping(self, element: ET.Element, mapping: SenderRecRecordTypeMapping):
        if mapping is not None:
            child_element = ET.SubElement(element, "SENDER-REC-RECORD-TYPE-MAPPING")
            self.writeSenderRecCompositeTypeMapping(child_element, mapping)
            self.writeSenderRecArrayTypeMappingRecordElementMapping(child_element, mapping)

    def writeSenderReceiverToSignalGroupMappingTypeMapping(self, element: ET.Element, mapping: SenderReceiverToSignalGroupMapping):
        type_mapping = mapping.getTypeMapping()
        if type_mapping is not None:
            child_element = ET.SubElement(element, "TYPE-MAPPING")
            if isinstance(type_mapping, SenderRecRecordTypeMapping):
                self.writeSenderRecRecordTypeMapping(child_element, type_mapping)
            else:
                self.notImplemented("Unsupported Type Mapping %s" % type(type_mapping))

    def writeSenderReceiverToSignalGroupMapping(self, element: ET.Element, mapping: SenderReceiverToSignalGroupMapping):
        child_element = ET.SubElement(element, "SENDER-RECEIVER-TO-SIGNAL-GROUP-MAPPING")
        self.setVariableDataPrototypeInSystemInstanceRef(child_element, "DATA-ELEMENT-IREF", mapping.getDataElementIRef())
        self.setChildElementOptionalRefType(child_element, "SIGNAL-GROUP-REF", mapping.getSignalGroupRef())
        self.writeSenderReceiverToSignalGroupMappingTypeMapping(child_element, mapping)
    
    def writeSystemMappingDataMappings(self, element: ET.Element, system_mapping: SystemMapping):
        data_mappings = system_mapping.getDataMappings()
        if len(data_mappings) > 0:
            child_element = ET.SubElement(element, "DATA-MAPPINGS")
            for data_mapping in data_mappings:
                if isinstance(data_mapping, SenderReceiverToSignalMapping):
                    self.writeSenderReceiverToSignalMapping(child_element, data_mapping)
                elif isinstance(data_mapping, SenderReceiverToSignalGroupMapping):
                    self.writeSenderReceiverToSignalGroupMapping(child_element, data_mapping)
                else:
                    self.notImplemented("Unsupported Data Mapping %s" % type(data_mapping))
                
    def setSwcToEcuMapping(self, element: ET.Element, mapping: SwcToEcuMapping):
        child_element = ET.SubElement(element, "SWC-TO-ECU-MAPPING")
        self.writeIdentifiable(child_element, mapping)
        irefs = mapping.getComponentIRefs()
        if len(irefs) > 0:
            irefs_tag = ET.SubElement(child_element, "COMPONENT-IREFS")
            for iref in irefs:
                self.setComponentInSystemInstanceRef(irefs_tag, "COMPONENT-IREF", iref)
        self.setChildElementOptionalRefType(child_element, "ECU-INSTANCE-REF", mapping.getEcuInstanceRef())
                
    def writeSystemMappingSwMappings(self, element: ET.Element, system_mapping: SystemMapping):
        sw_mappings = system_mapping.getSwMappings()
        if len(sw_mappings) > 0:
            child_element = ET.SubElement(element, "SW-MAPPINGS")
            for sw_mapping in sw_mappings:
                if isinstance(sw_mapping, SwcToEcuMapping):
                    self.setSwcToEcuMapping(child_element, sw_mapping)
                else:
                    self.notImplemented("Unsupported Sw Mapping %s" % type(sw_mapping))

    def writeEcuMapping(self, element: ET.Element, mapping: ECUMapping):
        self.logger.debug("Write ECUMapping <%s>" % mapping.getShortName())
        if mapping is not None:
            child_element = ET.SubElement(element, "ECU-MAPPING")
            self.writeIdentifiable(child_element, mapping)
            self.setChildElementOptionalRefType(child_element, "ECU-INSTANCE-REF", mapping.getEcuInstanceRef())
            self.setChildElementOptionalRefType(child_element, "ECU-REF", mapping.getEcuRef())

    def writeSystemMappingEcuResourceMappings(self, element: ET.Element, mapping: SystemMapping):
        ecu_resource_mappings = mapping.getEcuResourceMappings()
        if len(ecu_resource_mappings) > 0:
            child_element = ET.SubElement(element, "ECU-RESOURCE-MAPPINGS")
            for ecu_resource_mapping in ecu_resource_mappings:
                if isinstance(ecu_resource_mapping, ECUMapping):
                    self.writeEcuMapping(child_element, ecu_resource_mapping)
                else:
                    self.notImplemented("Unsupported Sw Mapping %s" % type(ecu_resource_mapping))

    def writeSwcToImplMapping(self, element: ET.Element, mapping: SwcToImplMapping):
        if mapping is not None:
            child_element = ET.SubElement(element, "SWC-TO-IMPL-MAPPING")
            self.writeIdentifiable(child_element, mapping)
            self.setChildElementOptionalRefType(child_element, "COMPONENT-IMPLEMENTATION-REF", mapping.getComponentImplementationRef())
            irefs = mapping.getComponentIRefs()
            if len(irefs) > 0:
                irefs_tag = ET.SubElement(child_element, "COMPONENT-IREFS")
                for iref in irefs:
                    self.setComponentInSystemInstanceRef(irefs_tag, "COMPONENT-IREF", iref)

    def writeSystemMappingSwImplMappings(self, element: ET.Element, mapping: SystemMapping):
        sw_impl_mappings = mapping.getSwImplMappings()
        if len(sw_impl_mappings) > 0:
            child_element = ET.SubElement(element, "SW-IMPL-MAPPINGS")
            for sw_impl_mapping in sw_impl_mappings:
                if isinstance(sw_impl_mapping, SwcToImplMapping):
                    self.writeSwcToImplMapping(child_element, sw_impl_mapping)
                else:
                    self.notImplemented("Unsupported SwImplMapping <%s>" % type(sw_impl_mapping))

    def writeSystemMapping(self, element: ET.Element, mapping: SystemMapping):
        self.logger.debug("Write SystemMapping <%s>" % mapping.getShortName())
        child_element = ET.SubElement(element, "SYSTEM-MAPPING")
        self.writeIdentifiable(child_element, mapping)
        self.writeSystemMappingDataMappings(child_element, mapping)
        self.writeSystemMappingEcuResourceMappings(child_element, mapping)
        self.writeSystemMappingSwImplMappings(child_element, mapping)
        self.writeSystemMappingSwMappings(child_element, mapping)

    def writeSystemMappings(self, element: ET.Element, system: System):
        mappings = system.getMappings()
        if len(mappings) > 0:
            mappings_tag = ET.SubElement(element, "MAPPINGS")
            for mapping in mappings:
                if isinstance(mapping, SystemMapping):
                    self.writeSystemMapping(mappings_tag, mapping)
                else:
                    self.notImplemented("Unsupported Mapping %s" % type(mapping))
                
    def writeRootSwCompositionPrototype(self, element: ET.Element, system: System):
        prototype = system.getRootSoftwareComposition()
        if prototype is not None:
            self.logger.debug("Write RootSwCompositionPrototype <%s>" % prototype.getShortName())
            child_element = ET.SubElement(element, "ROOT-SOFTWARE-COMPOSITIONS")
            child_element = ET.SubElement(child_element, "ROOT-SW-COMPOSITION-PROTOTYPE")
            self.writeIdentifiable(child_element, prototype)
            self.setChildElementOptionalRefType(child_element, "FLAT-MAP-REF", prototype.getFlatMapRef())
            self.setChildElementOptionalRefType(child_element, "SOFTWARE-COMPOSITION-TREF", prototype.getSoftwareCompositionTRef())

    def writeSystemFibexElementRefs(self, element: ET.Element, system: System):
        refs = system.getFibexElementRefs()
        if len(refs) > 0:
            fibex_elements_tag = ET.SubElement(element, "FIBEX-ELEMENTS")
            for ref in refs:
                child_element = ET.SubElement(fibex_elements_tag, "FIBEX-ELEMENT-REF-CONDITIONAL")
                self.setChildElementOptionalRefType(child_element, "FIBEX-ELEMENT-REF", ref)
                
    def writeSystem(self, element: ET.Element, system: System):
        self.logger.debug("Write System %s" % system.getShortName())
        child_element = ET.SubElement(element, "SYSTEM")
        self.writeARElement(child_element, system)
        self.setChildElementOptionalLiteral(child_element, "ECU-EXTRACT-VERSION", system.getEcuExtractVersion())
        self.writeSystemFibexElementRefs(child_element, system)
        self.writeSystemMappings(child_element, system)
        self.writeRootSwCompositionPrototype(child_element, system)
        self.setChildElementOptionalRevisionLabelString(child_element, "SYSTEM-VERSION", system.getSystemVersion())

    def writePhysicalDimension(self, element: ET.Element, dimension: PhysicalDimension):
        self.logger.debug("Set PhysicalDimension %s" % dimension.getShortName())
        child_element = ET.SubElement(element, "PHYSICAL-DIMENSION")
        self.writeARElement(child_element, dimension)
        self.setChildElementOptionalNumericalValue(child_element, "LENGTH-EXP", dimension.getLengthExp())
        self.setChildElementOptionalNumericalValue(child_element, "LUMINOUS-INTENSITY-EXP", dimension.getLuminousIntensityExp())
        self.setChildElementOptionalNumericalValue(child_element, "MASS-EXP", dimension.getMassExp())
        self.setChildElementOptionalNumericalValue(child_element, "MOLAR-AMOUNT-EXP", dimension.getMolarAmountExp())
        self.setChildElementOptionalNumericalValue(child_element, "TEMPERATURE-EXP", dimension.getTemperatureExp())
        self.setChildElementOptionalNumericalValue(child_element, "TIME-EXP", dimension.getTimeExp())
        self.setChildElementOptionalNumericalValue(child_element, "CURRENT-EXP", dimension.getCurrentExp())

    def setFlatInstanceDescriptor(self, element: ET.Element, desc: FlatInstanceDescriptor):
        self.logger.debug("Set FlatInstanceDescriptor %s" % desc.getShortName())
        child_element = ET.SubElement(element, "FLAT-INSTANCE-DESCRIPTOR")
        self.writeIdentifiable(child_element, desc)
        self.setAnyInstanceRef(child_element, "UPSTREAM-REFERENCE-IREF", desc.getUpstreamReferenceIRef())
        self.setAnyInstanceRef(child_element, "ECU-EXTRACT-REFERENCE-IREF", desc.getEcuExtractReferenceIRef())

    def writeFlatMapInstances(self, element: ET.Element, map: FlatMap):
        instances = map.getInstances()
        if len(instances) > 0:
            child_element = ET.SubElement(element, "INSTANCES")
            for instance in instances:
                if isinstance(instance, FlatInstanceDescriptor):
                    self.setFlatInstanceDescriptor(child_element, instance)
                else:
                    self.notImplemented("Unsupported Flat Map Instances <%s>" % type(instance))

    def writeFlatMap(self, element: ET.Element, map: FlatMap):
        self.logger.debug("Set FlatMap %s" % map.getShortName())
        child_element = ET.SubElement(element, "FLAT-MAP")
        self.writeARElement(child_element, map)
        self.writeFlatMapInstances(child_element, map)

    def setDataPrototypeMapping(self, element: ET.Element, mapping: DataPrototypeMapping):
        child_element = ET.SubElement(element, "DATA-PROTOTYPE-MAPPING")
        self.setChildElementOptionalRefType(child_element, "FIRST-DATA-PROTOTYPE-REF", mapping.getFirstDataPrototypeRef())
        self.setChildElementOptionalRefType(child_element, "SECOND-DATA-PROTOTYPE-REF", mapping.getSecondDataPrototypeRef())

    def setDataPrototypeMappings(self, element: ET.Element, key: str, mappings: List[DataPrototypeMapping]):
        if len(mappings) > 0:
            child_element = ET.SubElement(element, key)
            for mapping in mappings:
                self.setDataPrototypeMapping(child_element, mapping)

    def writeVariableAndParameterInterfaceMapping(self, element: ET.Element, mapping: VariableAndParameterInterfaceMapping):
        # self.logger.debug("Write VariableAndParameterInterfaceMapping %s" % mapping.getShortName())
        child_element = ET.SubElement(element, "VARIABLE-AND-PARAMETER-INTERFACE-MAPPING")
        self.writeIdentifiable(child_element, mapping)
        self.setDataPrototypeMappings(child_element, "DATA-MAPPINGS", mapping.getDataMappings())

    def writeClientServerOperationMapping(self, element: ET.Element, mapping: ClientServerOperationMapping):
        child_element = ET.SubElement(element, "CLIENT-SERVER-OPERATION-MAPPING")
        self.setChildElementOptionalRefType(child_element, "FIRST-OPERATION-REF", mapping.getFirstOperationRef())
        self.setChildElementOptionalRefType(child_element, "SECOND-OPERATION-REF", mapping.getSecondOperationRef())

    def writeClientServerInterfaceMappingOperationMappings(self, element: ET.Element, mapping: ClientServerInterfaceMapping):
        operation_mappings = mapping.getOperationMappings()
        if len(operation_mappings) > 0:
            child_element = ET.SubElement(element, "OPERATION-MAPPINGS")
            for operation_mapping in operation_mappings:
                if isinstance(operation_mapping, ClientServerOperationMapping):
                    self.writeClientServerOperationMapping(child_element, operation_mapping)
                else:
                    self.notImplemented("Unsupported Operation Mapping <%s>" % type(operation_mapping))

    def writeClientServerInterfaceMapping(self, element: ET.Element, mapping: ClientServerInterfaceMapping):
        # self.logger.debug("Read ClientServerInterfaceMapping %s" % mapping.getShortName())
        if mapping is not None:
            child_element = ET.SubElement(element, "CLIENT-SERVER-INTERFACE-MAPPING")
            self.writeIdentifiable(child_element, mapping)
            self.writeClientServerInterfaceMappingOperationMappings(child_element, mapping)

    def writePortInterfaceMappings(self, element: ET.Element, mapping_set: PortInterfaceMappingSet):
        mappings = mapping_set.getPortInterfaceMappings()
        if len(mappings) > 0:
            child_element = ET.SubElement(element, "PORT-INTERFACE-MAPPINGS")
            for mapping in mappings:
                if isinstance(mapping, VariableAndParameterInterfaceMapping):
                    self.writeVariableAndParameterInterfaceMapping(child_element, mapping)
                elif isinstance(mapping, ClientServerInterfaceMapping):
                    self.writeClientServerInterfaceMapping(child_element, mapping)
                else:
                    self.notImplemented("Unsupported PortInterfaceMapping <%s>" % type(mapping))

    def writePortInterfaceMappingSet(self, element: ET.Element, mapping_set: PortInterfaceMappingSet):
        self.logger.debug("Set PortInterfaceMappingSet %s" % mapping_set.getShortName())
        child_element = ET.SubElement(element, "PORT-INTERFACE-MAPPING-SET")
        self.writeARElement(child_element, mapping_set)
        self.writePortInterfaceMappings(child_element, mapping_set)

    def setISignalMappings(self, element: ET.Element, mappings: List[ISignalMapping]):
        if len(mappings) > 0:
            mappings_tag = ET.SubElement(element, "SIGNAL-MAPPINGS")
            for mapping in mappings:
                child_element = ET.SubElement(mappings_tag, "I-SIGNAL-MAPPING")
                self.setChildElementOptionalRefType(child_element, "SOURCE-SIGNAL-REF", mapping.getSourceSignalRef())
                self.setChildElementOptionalRefType(child_element, "TARGET-SIGNAL-REF", mapping.getTargetSignalRef())

    def setTargetIPduRef(self, element: ET.Element, key: str, i_pdu_ref: TargetIPduRef):
        if i_pdu_ref is not None:
            child_element = ET.SubElement(element, key)
            self.setChildElementOptionalRefType(child_element, "TARGET-I-PDU-REF", i_pdu_ref.getTargetIPdu())

    def setIPduMappings(self, element: ET.Element, mappings: List[IPduMapping]):
        if len(mappings) > 0:
            mappings_tag = ET.SubElement(element, "I-PDU-MAPPINGS")
            for mapping in mappings:
                child_element = ET.SubElement(mappings_tag, "I-PDU-MAPPING")
                self.setChildElementOptionalRefType(child_element, "SOURCE-I-PDU-REF", mapping.getSourceIpduRef())
                self.setTargetIPduRef(child_element, "TARGET-I-PDU", mapping.getTargetIPdu())

    def writeGateway(self, element: ET.Element, gateway: Gateway):
        self.logger.debug("Gateway %s" % gateway.getShortName())
        child_element = ET.SubElement(element, "GATEWAY")
        self.writeIdentifiable(child_element, gateway)
        self.setChildElementOptionalRefType(child_element, "ECU-REF", gateway.ecuRef)
        self.setIPduMappings(child_element, gateway.getIPduMappings())
        self.setISignalMappings(child_element, gateway.getSignalMappings())

    def writeISignal(self, element: ET.Element, signal: ISignal):
        self.logger.debug("ISignal %s" % signal.getShortName())
        child_element = ET.SubElement(element, "I-SIGNAL")
        self.writeIdentifiable(child_element, signal)
        self.setChildElementOptionalLiteral(child_element, "DATA-TYPE-POLICY", signal.getDataTypePolicy())
        self.setChildElementOptionalLiteral(child_element, "I-SIGNAL-TYPE", signal.getISignalType())
        self.setValueSpecification(child_element, "INIT-VALUE", signal.getInitValue())
        self.setChildElementOptionalNumericalValue(child_element, "LENGTH", signal.getLength())
        self.setSwDataDefProps(child_element, "NETWORK-REPRESENTATION-PROPS", signal.getNetworkRepresentationProps())
        self.setChildElementOptionalRefType(child_element, "SYSTEM-SIGNAL-REF", signal.getSystemSignalRef())

    def writeEcucValueCollectionEcucValues(self, element: ET.Element, collection: EcucValueCollection):
        value_refs = collection.getEcucValueRefs()
        if len(value_refs) > 0:
            ecuc_values_tag = ET.SubElement(element, "ECUC-VALUES")
            for value_ref in value_refs:
                child_element = ET.SubElement(ecuc_values_tag, "ECUC-MODULE-CONFIGURATION-VALUES-REF-CONDITIONAL")
                self.setChildElementOptionalRefType(child_element, "ECUC-MODULE-CONFIGURATION-VALUES-REF", value_ref)

    def writeEcucValueCollection(self, element: ET.Element, collection: EcucValueCollection):
        self.logger.debug("EcucValueCollection %s" % collection.getShortName())
        child_element = ET.SubElement(element, "ECUC-VALUE-COLLECTION")
        self.writeIdentifiable(child_element, collection)
        self.setChildElementOptionalRefType(child_element, "ECU-EXTRACT-REF", collection.getEcuExtractRef())
        self.writeEcucValueCollectionEcucValues(child_element, collection)

    def writeEcucContainerValueSubContainers(self, element: ET.Element, container: EcucContainerValue):
        sub_containers = container.getSubContainers()
        if len(sub_containers) > 0:
            sub_containers_tag = ET.SubElement(element, "SUB-CONTAINERS")
            for sub_container in sub_containers:
                if isinstance(sub_container, EcucContainerValue):
                    self.writeEcucContainValue(sub_containers_tag, sub_container)
                else:
                    self.notImplemented("Unsupported Sub Container %s" % type(container))
                
    def writeEcucParameterValue(self, element: ET.Element, param_value: EcucParameterValue):
        self.setChildElementOptionalRefType(element, "DEFINITION-REF", param_value.getDefinitionRef())
        self.setAnnotations(element, param_value.getAnnotations())

    def setEcucTextualParamValue(self, element: ET.Element, param_value: EcucTextualParamValue):
        child_element = ET.SubElement(element, "ECUC-TEXTUAL-PARAM-VALUE")
        self.writeEcucParameterValue(child_element, param_value)
        self.setChildElementOptionalLiteral(child_element, "VALUE", param_value.getValue())

    def setEcucNumericalParamValue(self, element: ET.Element, param_value: EcucNumericalParamValue):
        child_element = ET.SubElement(element, "ECUC-NUMERICAL-PARAM-VALUE")
        self.writeEcucParameterValue(child_element, param_value)
        self.setChildElementOptionalNumericalValue(child_element, "VALUE", param_value.getValue())
                
    def writeEcucContainerValueParameterValues(self, element: ET.Element, container_value: EcucContainerValue):
        param_values = container_value.getParameterValues()
        if len(param_values) > 0:
            child_element = ET.SubElement(element, "PARAMETER-VALUES")
            for param_value in param_values:
                if isinstance(param_value, EcucTextualParamValue):
                    self.setEcucTextualParamValue(child_element, param_value)
                elif isinstance(param_value, EcucNumericalParamValue):
                    self.setEcucNumericalParamValue(child_element, param_value)
                else:
                    self.notImplemented("Unsupported EcucParameterValue <%s>" % type(param_value))
                
    def writeEcucAbstractReferenceValue(self, element: ET.Element, value: EcucAbstractReferenceValue):
        self.setChildElementOptionalRefType(element, "DEFINITION-REF", value.getDefinitionRef())
        self.setAnnotations(element, value.getAnnotations())

    def setEcucReferenceValue(self, element: ET.Element, value=EcucReferenceValue()):
        child_element = ET.SubElement(element, "ECUC-REFERENCE-VALUE")
        self.writeEcucAbstractReferenceValue(child_element, value)
        self.setChildElementOptionalRefType(child_element, "VALUE-REF", value.getValueRef())
        return value
    
    def setAnyInstanceRef(self, element: ET.Element, key, instance_ref: AnyInstanceRef):
        if instance_ref is not None:
            child_element = ET.SubElement(element, key)
            self.setChildElementOptionalRefType(child_element, "BASE-REF", instance_ref.getBaseRef())
            for ref in instance_ref.getContextElementRefs():
                self.setChildElementOptionalRefType(child_element, "CONTEXT-ELEMENT-REF", ref)
            self.setChildElementOptionalRefType(child_element, "TARGET-REF", instance_ref.getTargetRef())
        return instance_ref
    
    def setEcucInstanceReferenceValue(self, element: ET.Element, value: EcucInstanceReferenceValue):
        child_element = ET.SubElement(element, "ECUC-INSTANCE-REFERENCE-VALUE")
        self.writeEcucAbstractReferenceValue(child_element, value)
        self.setAnyInstanceRef(child_element, "VALUE-IREF", value.getValueIRef())
        return value
    
    def writeEcucContainerValueReferenceValues(self, element: ET.Element, container_value: EcucContainerValue):
        reference_values = container_value.getReferenceValues()
        if len(reference_values) > 0:
            child_element = ET.SubElement(element, "REFERENCE-VALUES")
            for reference_value in reference_values:
                if isinstance(reference_value, EcucReferenceValue):
                    self.setEcucReferenceValue(child_element, reference_value)
                elif isinstance(reference_value, EcucInstanceReferenceValue):
                    self.setEcucInstanceReferenceValue(child_element, reference_value)
                else:
                    self.notImplemented("Unsupported EcucParameterValue <%s>" % type(reference_value))

    def writeEcucContainValue(self, element: ET.Element, container_value: EcucContainerValue):
        self.logger.debug("EcucContainerValue %s" % container_value.getShortName())
        child_element = ET.SubElement(element, "ECUC-CONTAINER-VALUE")
        self.writeIdentifiable(child_element, container_value)
        self.setChildElementOptionalRefType(child_element, "DEFINITION-REF", container_value.getDefinitionRef())
        self.writeEcucContainerValueParameterValues(child_element, container_value)
        self.writeEcucContainerValueReferenceValues(child_element, container_value)
        self.writeEcucContainerValueSubContainers(child_element, container_value)

    def writeEcucModuleConfigurationValuesContainers(self, element: ET.Element, value: EcucModuleConfigurationValues):
        containers = value.getContainers()
        if len(containers) > 0:
            containers_tag = ET.SubElement(element, "CONTAINERS")
            for container in containers:
                if isinstance(container, EcucContainerValue):
                    self.writeEcucContainValue(containers_tag, container)
                else:
                    self.notImplemented("Unsupported Container %s" % type(container))

    def writeEcucModuleConfigurationValues(self, element: ET.Element, values: EcucModuleConfigurationValues):
        self.logger.debug("EcucModuleConfigurationValues %s" % values.getShortName())
        child_element = ET.SubElement(element, "ECUC-MODULE-CONFIGURATION-VALUES")
        self.writeIdentifiable(child_element, values)
        self.setChildElementOptionalRefType(child_element, "DEFINITION-REF", values.getDefinitionRef())
        self.setChildElementOptionalLiteral(child_element, "IMPLEMENTATION-CONFIG-VARIANT", values.getImplementationConfigVariant())
        self.setChildElementOptionalRefType(child_element, "MODULE-DESCRIPTION-REF", values.getModuleDescriptionRef())
        self.writeEcucModuleConfigurationValuesContainers(child_element, values)

    def writeISignalGroupISignalRef(self, element: ET.Element, group: ISignalGroup):
        signal_refs = group.getISignalRefs()
        if len(signal_refs) > 0:
            child_element = ET.SubElement(element, "I-SIGNAL-REFS")
            for signal_ref in signal_refs:
                self.setChildElementOptionalRefType(child_element, "I-SIGNAL-REF", signal_ref)

    def writeISignalGroupComBasedSignalGroupTransformation(self, element: ET.Element, group: ISignalGroup):
        refs = group.getComBasedSignalGroupTransformationRefs()
        if len(refs) > 0:
            com_based_element = ET.SubElement(element, "COM-BASED-SIGNAL-GROUP-TRANSFORMATIONS")
            cond_element = ET.SubElement(com_based_element, "DATA-TRANSFORMATION-REF-CONDITIONAL")
            for ref in refs:
                self.setChildElementOptionalRefType(cond_element, "DATA-TRANSFORMATION-REF", ref)

    def writeTransformationISignalProps(self, element: ET.Element, props: TransformationISignalProps):
        self.writeDescribable(element, props)

    def writeEndToEndTransformationISignalPropsDataIds(self, element: ET.Element, props: EndToEndTransformationISignalProps):
        ids = props.getDataIds()
        if len(ids) > 0:
            child_element = ET.SubElement(element, "DATA-IDS")
            for id in ids:
                self.setChildElementOptionalPositiveInteger(child_element, "DATA-ID", id)

    def writeEndToEndTransformationISignalProps(self, element: ET.Element, props: EndToEndTransformationISignalProps):
        if props is not None:
            props_element = ET.SubElement(element, "END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS")
            variant_element = ET.SubElement(props_element, "END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS-VARIANTS")
            child_element = ET.SubElement(variant_element, "END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS-CONDITIONAL")
            self.writeTransformationISignalProps(child_element, props)
            self.setChildElementOptionalRefType(child_element, "TRANSFORMER-REF", props.getTransformerRef())
            self.writeEndToEndTransformationISignalPropsDataIds(child_element, props)
            self.setChildElementOptionalPositiveInteger(child_element, "DATA-LENGTH", props.getDataLength())

    def writeISignalGroupTransformationISignalProps(self, element: ET.Element, group: ISignalGroup):
        props = group.getTransformationISignalProps()
        if props is not None:
            child_element = ET.SubElement(element, "TRANSFORMATION-I-SIGNAL-PROPSS")
            if isinstance(props, EndToEndTransformationISignalProps):
                self.writeEndToEndTransformationISignalProps(child_element, props)
            else:
                self.notImplemented("Unsupported TransformationISignalProps %s" % type(props))

    def writeISignalGroup(self, element: ET.Element, group: ISignalGroup):
        self.logger.debug("ISignalGroup %s" % group.getShortName())
        child_element = ET.SubElement(element, "I-SIGNAL-GROUP")
        self.writeIdentifiable(child_element, group)
        self.writeISignalGroupComBasedSignalGroupTransformation(child_element, group)
        self.writeISignalGroupISignalRef(child_element, group)
        self.setChildElementOptionalRefType(child_element, "SYSTEM-SIGNAL-GROUP-REF", group.getSystemSignalGroupRef())
        self.writeISignalGroupTransformationISignalProps(child_element, group)

    def writeISignalIPduGroup(self, element: ET.Element, group: ISignalIPduGroup):
        self.logger.debug("Set ISignalIPduGroup %s" % group.getShortName())
        child_element = ET.SubElement(element, "I-SIGNAL-I-PDU-GROUP")
        self.writeIdentifiable(child_element, group)
        self.setChildElementOptionalLiteral(child_element, "COMMUNICATION-DIRECTION", group.getCommunicationDirection())
        self.setChildElementOptionalLiteral(child_element, "COMMUNICATION-MODE", group.getCommunicationMode())
        group_refs = group.getContainedISignalIPduGroupRefs()
        if len(group_refs) > 0:
            pdu_refs_tag = ET.SubElement(child_element, "CONTAINED-I-SIGNAL-I-PDU-GROUP-REFS")
            for pdu_ref in group_refs:
                self.setChildElementOptionalRefType(pdu_refs_tag, "CONTAINED-I-SIGNAL-I-PDU-GROUP-REF", pdu_ref)
        pdu_refs = group.getISignalIPduRefs()
        if len(pdu_refs) > 0:
            pdu_refs_tag = ET.SubElement(child_element, "I-SIGNAL-I-PDUS")
            for pdu_ref in pdu_refs:
                ref_conditional_tag = ET.SubElement(pdu_refs_tag, "I-SIGNAL-I-PDU-REF-CONDITIONAL")
                self.setChildElementOptionalRefType(ref_conditional_tag, "I-SIGNAL-I-PDU-REF", pdu_ref)

    def writeSystemSignal(self, element: ET.Element, signal: SystemSignal):
        self.logger.debug("SystemSignal %s" % signal.getShortName())
        child_element = ET.SubElement(element, "SYSTEM-SIGNAL")
        self.writeIdentifiable(child_element, signal)
        self.setChildElementOptionalBooleanValue(child_element, "DYNAMIC-LENGTH", signal.getDynamicLength())
        self.setSwDataDefProps(child_element, "PHYSICAL-PROPS", signal.getPhysicalProps())

    def writeGenericEthernetFrame(self, element: ET.Element, frame: GenericEthernetFrame):
        self.logger.debug("Write GenericEthernetFrame %s" % frame.getShortName())
        child_element = ET.SubElement(element, "ETHERNET-FRAME")
        self.writeFrame(child_element, frame)

    def setLifeCyclePeriod(self, element: ET.Element, key: str, period: LifeCyclePeriod):
        if period is not None:
            child_element = ET.SubElement(element, key)
            self.setChildElementOptionalRevisionLabelString(child_element, "AR-RELEASE-VERSION", period.getArReleaseVersion())

    def writeLifeCycleInfoUseInsteadRefs(self, element: ET.Element, info: LifeCycleInfo):
        refs = info.getUseInsteadRefs()
        if len(refs) > 0:
            child_element = ET.SubElement(element, "USE-INSTEAD-REFS")
            for ref in refs:
                self.setChildElementOptionalRefType(child_element, "USE-INSTEAD-REF", ref)

    def writeLifeCycleInfo(self, element: ET.Element, info: LifeCycleInfo):
        if info is not None:
            child_element = ET.SubElement(element, "LIFE-CYCLE-INFO")
            self.writeARObjectAttributes(child_element, info)
            self.setChildElementOptionalRefType(child_element, "LC-OBJECT-REF", info.getLcObjectRef())
            self.setChildElementOptionalRefType(child_element, "LC-STATE-REF", info.getLcStateRef())
            self.setLifeCyclePeriod(child_element, "PERIOD-BEGIN", info.getPeriodBegin())
            self.writeDocumentationBlock(child_element, "REMARK", info.getRemark())
            self.writeLifeCycleInfoUseInsteadRefs(child_element, info)

    def writeLifeCycleInfoSetLifeCycleInfos(self, element: ET.Element, info_set: LifeCycleInfoSet):
        infos = info_set.getLifeCycleInfos()
        if len(infos) > 0:
            child_element = ET.SubElement(element, "LIFE-CYCLE-INFOS")
            for info in infos:
                if isinstance(info, LifeCycleInfo):
                    self.writeLifeCycleInfo(child_element, info)
                else:
                    self.notImplemented("Unsupported Life Cycle Info <%s>" % type(info))

    def writeLifeCycleInfoSet(self, element: ET.Element, info_set: LifeCycleInfoSet):
        if info_set is not None:
            self.logger.debug("Write LifeCycleInfoSet %s" % info_set.getShortName())
            child_element = ET.SubElement(element, "LIFE-CYCLE-INFO-SET")
            self.writeIdentifiable(child_element, info_set)
            self.setChildElementOptionalRefType(child_element, "DEFAULT-LC-STATE-REF", info_set.getDefaultLcStateRef())
            self.writeLifeCycleInfoSetLifeCycleInfos(child_element, info_set)
            self.setChildElementOptionalRefType(child_element, "USED-LIFE-CYCLE-STATE-DEFINITION-GROUP-REF",
                                                info_set.getUsedLifeCycleStateDefinitionGroupRef())

    def writeDiagnosticConnectionFunctionalRequestRefs(self, element: ET.Element, connection: DiagnosticConnection):
        refs = connection.getFunctionalRequestRefs()
        if len(refs) > 0:
            refs_tag = ET.SubElement(element, "FUNCTIONAL-REQUEST-REFS")
            for ref in refs:
                self.setChildElementOptionalRefType(refs_tag, "FUNCTIONAL-REQUEST-REF", ref)

    def writeDiagnosticConnection(self, element: ET.Element, connection: DiagnosticConnection):
        self.logger.debug("Write DiagnosticConnection %s" % connection.getShortName())
        child_element = ET.SubElement(element, "DIAGNOSTIC-CONNECTION")
        self.writeIdentifiable(child_element, connection)
        self.writeDiagnosticConnectionFunctionalRequestRefs(child_element, connection)
        self.setChildElementOptionalRefType(child_element, "PHYSICAL-REQUEST-REF", connection.getPhysicalRequestRef())
        self.setChildElementOptionalRefType(child_element, "RESPONSE-REF", connection.getResponseOnEventRef())

    def writeDiagnosticServiceTableDiagnosticConnectionRefs(self, element: ET.Element, table: DiagnosticServiceTable):
        refs = table.getDiagnosticConnectionRefs()
        if len(refs) > 0:
            refs_tag = ET.SubElement(element, "DIAGNOSTIC-CONNECTIONS")
            for ref in refs:
                child_element = ET.SubElement(refs_tag, "DIAGNOSTIC-CONNECTION-REF-CONDITIONAL")
                self.setChildElementOptionalRefType(child_element, "DIAGNOSTIC-CONNECTION-REF", ref)

    def writeDiagnosticServiceTable(self, element: ET.Element, table: DiagnosticServiceTable):
        self.logger.debug("Write DiagnosticServiceTable %s" % table.getShortName())
        child_element = ET.SubElement(element, "DIAGNOSTIC-SERVICE-TABLE")
        self.writeIdentifiable(child_element, table)
        self.writeDiagnosticServiceTableDiagnosticConnectionRefs(child_element, table)
        self.setChildElementOptionalRefType(child_element, "ECU-INSTANCE-REF", table.getEcuInstanceRef())

    def writePdu(self, element: ET.Element, pdu: Pdu):
        self.writeIdentifiable(element, pdu)
        self.setChildElementOptionalBooleanValue(element, "HAS-DYNAMIC-LENGTH", pdu.getHasDynamicLength())
        self.setChildElementOptionalNumericalValue(element, "LENGTH", pdu.getLength())

    def writeIPdu(self, element: ET.Element, pdu: IPdu):
        self.writePdu(element, pdu)

    def writeSegmentPosition(self, element: ET.Element, position: SegmentPosition):
        if position is not None:
            child_element = ET.SubElement(element, "SEGMENT-POSITION")
            self.setChildElementOptionalLiteral(child_element, "SEGMENT-BYTE-ORDER", position.getSegmentByteOrder())
            self.setChildElementOptionalIntegerValue(child_element, "SEGMENT-LENGTH", position.getSegmentLength())
            self.setChildElementOptionalIntegerValue(child_element, "SEGMENT-POSITION", position.getSegmentPosition())

    def writeMultiplexedPartSegmentPositions(self, element: ET.Element, part: MultiplexedPart):
        positions = part.getSegmentPositions()
        if len(positions) > 0:
            child_element = ET.SubElement(element, "SEGMENT-POSITIONS")
            for position in positions:
                if isinstance(position, SegmentPosition):
                    self.writeSegmentPosition(child_element, position)
                else:
                    self.notImplemented("Unsupported DynamicPart <%s>" % type(position))

    def writeMultiplexedPart(self, element: ET.Element, part: MultiplexedPart):
        self.writeMultiplexedPartSegmentPositions(element, part)

    def writeDynamicPartAlternative(self, element: ET.Element, alternative: DynamicPartAlternative):
        if alternative is not None:
            child_element = ET.SubElement(element, "DYNAMIC-PART-ALTERNATIVE")
            self.setChildElementOptionalRefType(child_element, "I-PDU-REF", alternative.getIPduRef())
            self.setChildElementOptionalBooleanValue(child_element, "INITIAL-DYNAMIC-PART", alternative.getInitialDynamicPart())
            self.setChildElementOptionalIntegerValue(child_element, "SELECTOR-FIELD-CODE", alternative.getSelectorFieldCode())

    def writeDynamicPartDynamicPartAlternatives(self, element: ET.Element, part: DynamicPart):
        alternatives = part.getDynamicPartAlternatives()
        if len(alternatives) > 0:
            child_element = ET.SubElement(element, "DYNAMIC-PART-ALTERNATIVES")
            for alternative in alternatives:
                if isinstance(alternative, DynamicPartAlternative):
                    self.writeDynamicPartAlternative(child_element, alternative)
                else:
                    self.notImplemented("Unsupported DynamicPartAlternative <%s>" % type(alternative))

    def writeDynamicPart(self, element: ET.Element, part: DynamicPart):
        child_element = ET.SubElement(element, "DYNAMIC-PART")
        self.writeMultiplexedPart(child_element, part)
        self.writeDynamicPartDynamicPartAlternatives(child_element, part)

    def writeMultiplexedIPduDynamicParts(self, element: ET.Element, ipdu: MultiplexedIPdu):
        part = ipdu.getDynamicPart()
        if part is not None:
            child_element = ET.SubElement(element, "DYNAMIC-PARTS")
            if isinstance(part, DynamicPart):
                self.writeDynamicPart(child_element, part)
            else:
                self.notImplemented("Unsupported DynamicPart <%s>" % type(part))

    def writeStaticPart(self, element: ET.Element, part: StaticPart):
        child_element = ET.SubElement(element, "STATIC-PART")
        self.writeMultiplexedPart(child_element, part)
        self.setChildElementOptionalRefType(child_element, "I-PDU-REF", part.getIPduRef())

    def writeMultiplexedIPduStaticParts(self, element: ET.Element, ipdu: MultiplexedIPdu):
        part = ipdu.getStaticPart()
        if part is not None:
            child_element = ET.SubElement(element, "STATIC-PARTS")
            if isinstance(part, StaticPart):
                self.writeStaticPart(child_element, part)
            else:
                self.notImplemented("Unsupported StaticPart <%s>" % type(part))

    def writeMultiplexedIPdu(self, element: ET.Element, ipdu: MultiplexedIPdu):
        self.logger.debug("Write MultiplexedIPdu <%s>" % ipdu.getShortName())
        child_element = ET.SubElement(element, "MULTIPLEXED-I-PDU")
        self.writeIPdu(child_element, ipdu)
        self.writeMultiplexedIPduDynamicParts(child_element, ipdu)
        self.setChildElementOptionalLiteral(child_element, "SELECTOR-FIELD-BYTE-ORDER", ipdu.getSelectorFieldByteOrder())
        self.setChildElementOptionalIntegerValue(child_element, "SELECTOR-FIELD-LENGTH", ipdu.getSelectorFieldLength())
        self.setChildElementOptionalIntegerValue(child_element, "SELECTOR-FIELD-START-POSITION", ipdu.getSelectorFieldStartPosition())
        self.writeMultiplexedIPduStaticParts(child_element, ipdu)
        self.setChildElementOptionalLiteral(child_element, "TRIGGER-MODE", ipdu.getTriggerMode())
        self.setChildElementOptionalIntegerValue(child_element, "UNUSED-BIT-PATTERN", ipdu.getUnusedBitPattern())

    def writeUserDefinedIPdu(self, element: ET.Element, ipdu: UserDefinedIPdu):
        self.logger.debug("Write UserDefinedIPdu <%s>" % ipdu.getShortName())
        child_element = ET.SubElement(element, "USER-DEFINED-I-PDU")
        self.writeIPdu(child_element, ipdu)
        self.setChildElementOptionalLiteral(child_element, "CDD-TYPE", ipdu.getCddType())

    def writeUserDefinedPdu(self, element: ET.Element, pdu: UserDefinedPdu):
        self.logger.debug("Write UserDefinedPdu <%s>" % pdu.getShortName())
        child_element = ET.SubElement(element, "USER-DEFINED-PDU")
        self.writePdu(child_element, pdu)
        self.setChildElementOptionalLiteral(child_element, "CDD-TYPE", pdu.getCddType())

    def writeGeneralPurposePdu(self, element: ET.Element, pdu: GeneralPurposePdu):
        self.logger.debug("Write GeneralPurposePdu <%s>" % pdu.getShortName())
        child_element = ET.SubElement(element, "GENERAL-PURPOSE-PDU")
        self.writePdu(child_element, pdu)

    def writeGeneralPurposeIPdu(self, element: ET.Element, i_pdu: GeneralPurposeIPdu):
        self.logger.debug("Write GeneralPurposeIPdu <%s>" % i_pdu.getShortName())
        child_element = ET.SubElement(element, "GENERAL-PURPOSE-I-PDU")
        self.writeIPdu(child_element, i_pdu)

    def writeSecureCommunicationAuthenticationProps(self, element: ET.Element, props: SecureCommunicationAuthenticationProps):
        chile_element = ET.SubElement(element, "SECURE-COMMUNICATION-AUTHENTICATION-PROPS")
        self.writeIdentifiable(chile_element, props)
        self.setChildElementOptionalLiteral(chile_element, "AUTH-ALGORITHM", props.getAuthAlgorithm())
        self.setChildElementOptionalPositiveInteger(chile_element, "AUTH-INFO-TX-LENGTH", props.getAuthInfoTxLength())

    def writeSecureCommunicationPropsSetAuthenticationProps(self, element: ET.Element, props_set: SecureCommunicationPropsSet):
        propses = props_set.getAuthenticationProps()
        if len(propses) > 0:
            child_element = ET.SubElement(element, "AUTHENTICATION-PROPSS")
            for props in propses:
                if isinstance(props, SecureCommunicationAuthenticationProps):
                    self.writeSecureCommunicationAuthenticationProps(child_element, props)
                else:
                    self.notImplemented("Unsupported AuthenticationProps <%s>" % type(props))

    def writeSecureCommunicationFreshnessProps(self, element: ET.Element, props: SecureCommunicationFreshnessProps):
        child_element = ET.SubElement(element, "SECURE-COMMUNICATION-FRESHNESS-PROPS")
        self.writeIdentifiable(child_element, props)
        self.setChildElementOptionalLiteral(child_element, "FRESHNESS-VALUE-LENGTH", props.getFreshnessValueLength())
        self.setChildElementOptionalPositiveInteger(child_element, "FRESHNESS-VALUE-TX-LENGTH", props.getFreshnessValueTxLength())

    def writeSecureCommunicationPropsSetFreshnessProps(self, element: ET.Element, props_set: SecureCommunicationPropsSet):
        propses = props_set.getFreshnessProps()
        if len(propses) > 0:
            child_element = ET.SubElement(element, "FRESHNESS-PROPSS")
            for props in propses:
                if isinstance(props, SecureCommunicationFreshnessProps):
                    self.writeSecureCommunicationFreshnessProps(child_element, props)
                else:
                    self.notImplemented("Unsupported FreshnessProps <%s>" % type(props))

    def writeSecureCommunicationPropsSet(self, element: ET.Element, set: SecureCommunicationPropsSet):
        self.logger.debug("Write SecureCommunicationPropsSet %s" % set.getShortName())
        child_element = ET.SubElement(element, "SECURE-COMMUNICATION-PROPS-SET")
        self.writeIdentifiable(child_element, set)
        self.writeSecureCommunicationPropsSetAuthenticationProps(child_element, set)
        self.writeSecureCommunicationPropsSetFreshnessProps(child_element, set)

    def writeSoAdRoutingGroup(self, element: ET.Element, group: SoAdRoutingGroup):
        self.logger.debug("Write SoAdRoutingGroup <%s>" % group.getShortName())
        child_element = ET.SubElement(element, "SO-AD-ROUTING-GROUP")
        self.writeIdentifiable(child_element, group)
        self.setChildElementOptionalLiteral(child_element, "EVENT-GROUP-CONTROL-TYPE", group.getEventGroupControlType())

    def writeDoIpLogicAddress(self, element: ET.Element, address: DoIpLogicAddress):
        if address is not None:
            child_element = ET.SubElement(element, "DO-IP-LOGIC-ADDRESS")
            self.writeIdentifiable(child_element, address)
            self.setChildElementOptionalIntegerValue(child_element, "ADDRESS", address.getAddress())

    def writeDoIpTpConfigDoIpLogicAddresses(self, element: ET.Element, config: DoIpTpConfig):
        addresses = config.getDoIpLogicAddresses()
        if len(addresses) > 0:
            child_element = ET.SubElement(element, "DO-IP-LOGIC-ADDRESSS")
            for address in addresses:
                if isinstance(address, DoIpLogicAddress):
                    self.writeDoIpLogicAddress(child_element, address)
                else:
                    self.notImplemented("Unsupported DoIpLogicAddress <%s>" % type(address))

    def writeDoIpTpConnection(self, element: ET.Element, connection: DoIpTpConnection):
        if connection is not None:
            child_element = ET.SubElement(element, "DO-IP-TP-CONNECTION")
            self.writeTpConnection(child_element, connection)
            self.setChildElementOptionalRefType(child_element, "DO-IP-SOURCE-ADDRESS-REF", connection.getDoIpSourceAddressRef())
            self.setChildElementOptionalRefType(child_element, "DO-IP-TARGET-ADDRESS-REF", connection.getDoIpTargetAddressRef())
            self.setChildElementOptionalRefType(child_element, "TP-SDU-REF", connection.getTpSduRef())

    def writeDoIpTpConfigTpConnections(self, element: ET.Element, config: DoIpTpConfig):
        connections = config.getTpConnections()
        if len(connections) > 0:
            child_element = ET.SubElement(element, "TP-CONNECTIONS")
            for address in connections:
                if isinstance(address, DoIpTpConnection):
                    self.writeDoIpTpConnection(child_element, address)
                else:
                    self.notImplemented("Unsupported TpConnection <%s>" % type(address))

    def writeDoIpTpConfig(self, element: ET.Element, config: DoIpTpConfig):
        self.logger.debug("Write DoIpTpConfig <%s>" % config.getShortName())
        child_element = ET.SubElement(element, "DO-IP-TP-CONFIG")
        self.writeTpConfig(child_element, config)
        self.writeDoIpTpConfigDoIpLogicAddresses(child_element, config)
        self.writeDoIpTpConfigTpConnections(child_element, config)

    def writeHwDescriptionEntityHwCategoryRefs(self, element: ET.Element, entity: HwDescriptionEntity):
        refs = entity.getHwCategoryRefs()
        if len(refs) > 0:
            child_element = ET.SubElement(element, "HW-CATEGORY-REFS")
            for ref in refs:
                self.setChildElementOptionalRefType(child_element, "HW-CATEGORY-REF", ref)

    def writeHwDescriptionEntity(self, element: ET.Element, entity: HwDescriptionEntity):
        self.writeARElement(element, entity)
        self.writeHwDescriptionEntityHwCategoryRefs(element, entity)

    def writeHwPinGroup(self, element: ET.SubElement, pin_group: HwPinGroup):
        if pin_group is not None:
            child_element = ET.SubElement(element, "HW-PIN-GROUP")
            self.writeHwDescriptionEntity(child_element, pin_group)

    def writeHwElementHwPinGroups(self, element: ET.Element, hw_element: HwElement):
        pin_groups = hw_element.getHwPinGroups()
        if len(pin_groups) > 0:
            child_element = ET.SubElement(element, "HW-PIN-GROUPS")
            for pin_group in pin_groups:
                if isinstance(pin_group, HwPinGroup):
                    self.writeHwPinGroup(child_element, pin_group)
                else:
                    self.notImplemented("Unsupported Hw Pin Group <%s>" % type(pin_group))

    def writeHwElement(self, element: ET.Element, hw_element: HwElement):
        if hw_element is not None:
            self.logger.debug("Write HwElement <%s>" % hw_element.getShortName())
            child_element = ET.SubElement(element, "HW-ELEMENT")
            self.writeHwDescriptionEntity(child_element, hw_element)
            self.writeHwElementHwPinGroups(child_element, hw_element)

    def writeHwAttributeDef(self, element: ET.Element, attribute_def: HwAttributeDef):
        if attribute_def is not None:
            child_element = ET.SubElement(element, "HW-ATTRIBUTE-DEF")
            self.writeIdentifiable(child_element, attribute_def)
            self.setChildElementOptionalRefType(child_element, "UNIT-REF", attribute_def.getUnitRef())

    def writeHwCategoryHwAttributeDef(self, element: ET.Element, hw_category: HwCategory):
        attribute_defs = hw_category.getHwAttributeDefs()
        if len(attribute_defs) > 0:
            child_element = ET.SubElement(element, "HW-ATTRIBUTE-DEFS")
            for attribute_def in attribute_defs:
                if isinstance(attribute_def, HwAttributeDef):
                    self.writeHwAttributeDef(child_element, attribute_def)
                else:
                    self.notImplemented("Unsupported Hw Attribute Defs <%s>" % type(attribute_def))

    def writeHwCategory(self, element: ET.Element, hw_category: HwCategory):
        self.logger.debug("write HwCategory <%s>" % hw_category.getShortName())
        child_element = ET.SubElement(element, "HW-CATEGORY")
        self.writeARElement(child_element, hw_category)
        self.writeHwCategoryHwAttributeDef(child_element, hw_category)

    def writeHwType(self, element: ET.Element, type: HwType):
        self.logger.debug("Write HwType <%s>" % type.getShortName())
        child_element = ET.SubElement(element, "HW-TYPE")
        self.writeARElement(child_element, type)

    def writeLinCommunicationController(self, element: ET.Element, controller: LinCommunicationController):
        self.writeCommunicationController(element, controller)
        self.setChildElementOptionalLiteral(element, "PROTOCOL-VERSION", controller.getProtocolVersion())

    def writeLinMaster(self, element: ET.Element, controller: LinMaster):
        self.logger.debug("Write LinMaster <%s>" % controller.getShortName())
        child_element = ET.SubElement(element, "LIN-MASTER")
        self.writeIdentifiable(child_element, controller)
        variants_tag = ET.SubElement(child_element, "LIN-MASTER-VARIANTS")
        cond_tag = ET.SubElement(variants_tag, "LIN-MASTER-CONDITIONAL")
        self.writeLinCommunicationController(cond_tag, controller)
        self.setChildElementOptionalTimeValue(cond_tag, "TIME-BASE", controller.getTimeBase())
        self.setChildElementOptionalTimeValue(cond_tag, "TIME-BASE-JITTER", controller.getTimeBaseJitter())

    def writeISignalToPduMappings(self, element: ET.Element, parent: ISignalIPdu):
        mappings = parent.getISignalToPduMappings()
        if len(mappings) > 0:
            mappings_tag = ET.SubElement(element, "I-SIGNAL-TO-PDU-MAPPINGS")
            for mapping in mappings:
                child_element = ET.SubElement(mappings_tag, "I-SIGNAL-TO-I-PDU-MAPPING")
                self.writeIdentifiable(child_element, mapping)
                self.setChildElementOptionalRefType(child_element, "I-SIGNAL-REF", mapping.getISignalRef())
                self.setChildElementOptionalRefType(child_element, "I-SIGNAL-GROUP-REF", mapping.getISignalGroupRef())
                self.setChildElementOptionalLiteral(child_element, "PACKING-BYTE-ORDER", mapping.getPackingByteOrder())
                self.setChildElementOptionalNumericalValue(child_element, "START-POSITION", mapping.getStartPosition())
                self.setChildElementOptionalLiteral(child_element, "TRANSFER-PROPERTY", mapping.getTransferProperty())
                self.setChildElementOptionalNumericalValue(child_element, "UPDATE-INDICATION-BIT-POSITION", mapping.getUpdateIndicationBitPosition())
    
    def setDataFilter(self, element: ET.Element, key: str, filter: DataFilter):
        if filter is not None:
            child_element = ET.SubElement(element, key)
            self.setChildElementOptionalLiteral(child_element, "DATA-FILTER-TYPE", filter.getDataFilterType())
            self.setChildElementOptionalIntegerValue(child_element, "MASK", filter.getMask())
            self.setChildElementOptionalIntegerValue(child_element, "X", filter.getX())

    def setTransmissionModeConditions(self, element: ET.Element, key: str, conditions: List[TransmissionModeCondition]):
        if len(conditions) > 0:
            conditions_tag = ET.SubElement(element, key)
            for condition in conditions:
                child_element = ET.SubElement(conditions_tag, "TRANSMISSION-MODE-CONDITION")
                self.setDataFilter(child_element, "DATA-FILTER", condition.getDataFilter())
                self.setChildElementOptionalRefType(child_element, "I-SIGNAL-IN-I-PDU-REF", condition.getISignalInIPduRef())

    def setTimeRangeType(self, element: ET.Element, key: str, time_range: TimeRangeType):
        if time_range is not None:
            child_element = ET.SubElement(element, key)
            self.setChildElementOptionalTimeValue(child_element, "VALUE", time_range.getValue())

    def setEventControlledTiming(self, element: ET.Element, key: str, timing: EventControlledTiming):
        if timing is not None:
            child_element = ET.SubElement(element, key)
            self.setChildElementOptionalIntegerValue(child_element, "NUMBER-OF-REPETITIONS", timing.getNumberOfRepetitions())
            self.setTimeRangeType(child_element, "REPETITION-PERIOD", timing.getRepetitionPeriod())
            
    def setCyclicTiming(self, element: ET.Element, key: str, timing: CyclicTiming):
        if timing is not None:
            child_element = ET.SubElement(element, key)
            self.setTimeRangeType(child_element, "TIME-OFFSET", timing.getTimeOffset())
            self.setTimeRangeType(child_element, "TIME-PERIOD", timing.getTimePeriod())

    def setTransmissionModeTiming(self, element: ET.Element, key: str, timing: TransmissionModeTiming):
        if timing is not None:
            self.logger.debug("Set TransmissionModeTiming of <%s>" % key)
            child_element = ET.SubElement(element, key)
            self.setCyclicTiming(child_element, "CYCLIC-TIMING", timing.getCyclicTiming())
            self.setEventControlledTiming(child_element, "EVENT-CONTROLLED-TIMING", timing.getEventControlledTiming())

    def setTransmissionModeDeclaration(self, element: ET.Element, key: str, decl: TransmissionModeDeclaration):
        if decl is not None:
            child_element = ET.SubElement(element, key)
            self.setTransmissionModeConditions(child_element, "TRANSMISSION-MODE-CONDITIONS", decl.getTransmissionModeConditions())
            self.setTransmissionModeTiming(child_element, "TRANSMISSION-MODE-FALSE-TIMING", decl.getTransmissionModeFalseTiming())
            self.setTransmissionModeTiming(child_element, "TRANSMISSION-MODE-TRUE-TIMING", decl.getTransmissionModeTrueTiming())

    def setISignalIPduIPduTimingSpecification(self, element: ET.Element, timing: IPduTiming):
        if timing is not None:
            spec_tag = ET.SubElement(element, "I-PDU-TIMING-SPECIFICATIONS")
            child_element = ET.SubElement(spec_tag, "I-PDU-TIMING")
            self.setChildElementOptionalTimeValue(child_element, "MINIMUM-DELAY", timing.getMinimumDelay())
            self.setTransmissionModeDeclaration(child_element, "TRANSMISSION-MODE-DECLARATION", timing.getTransmissionModeDeclaration())

    def writeISignalIPdu(self, element: ET.Element, ipdu: ISignalIPdu):
        self.logger.debug("ISignalIPdu %s" % ipdu.getShortName())
        child_element = ET.SubElement(element, "I-SIGNAL-I-PDU")
        self.writeIdentifiable(child_element, ipdu)
        self.setChildElementOptionalNumericalValue(child_element, "LENGTH", ipdu.getLength())
        self.setISignalIPduIPduTimingSpecification(child_element, ipdu.getIPduTimingSpecification())
        self.writeISignalToPduMappings(child_element, ipdu)
        self.setChildElementOptionalIntegerValue(child_element, "UNUSED-BIT-PATTERN", ipdu.getUnusedBitPattern())

    def writeFlexrayFrame(self, element: ET.Element, frame: FlexrayFrame):
        if frame is not None:
            self.logger.debug("Write FlexrayFrame <%s>" % frame.getShortName())
            child_element = ET.SubElement(element, "FLEXRAY-FRAME")
            self.writeFrame(child_element, frame)

    def writeFlexrayCommunicationController(self, element: ET.Element, controller: FlexrayCommunicationController):
        if controller is not None:
            self.logger.debug("Write FlexrayCommunicationController <%s>" % controller.getShortName())
            controller_element = ET.SubElement(element, "FLEXRAY-COMMUNICATION-CONTROLLER")
            self.writeIdentifiable(controller_element, controller)
            variant_element = ET.SubElement(controller_element, "FLEXRAY-COMMUNICATION-CONTROLLER-VARIANTS")
            child_element = ET.SubElement(variant_element, "FLEXRAY-COMMUNICATION-CONTROLLER-CONDITIONAL")
            self.writeCommunicationController(controller_element, controller)
            self.setChildElementOptionalIntegerValue(child_element, "ACCEPTED-STARTUP-RANGE", controller.getAcceptedStartupRange())
            self.setChildElementOptionalBooleanValue(child_element, "ALLOW-HALT-DUE-TO-CLOCK", controller.getAllowHaltDueToClock())
            self.setChildElementOptionalIntegerValue(child_element, "ALLOW-PASSIVE-TO-ACTIVE", controller.getAllowPassiveToActive())
            self.setChildElementOptionalIntegerValue(child_element, "CLUSTER-DRIFT-DAMPING", controller.getClusterDriftDamping())
            self.setChildElementOptionalIntegerValue(child_element, "DECODING-CORRECTION", controller.getDecodingCorrection())
            self.setChildElementOptionalIntegerValue(child_element, "DELAY-COMPENSATION-A", controller.getDelayCompensationA())
            self.setChildElementOptionalIntegerValue(child_element, "DELAY-COMPENSATION-B", controller.getDelayCompensationB())
            self.setChildElementOptionalBooleanValue(child_element, "KEY-SLOT-ONLY-ENABLED", controller.getKeySlotOnlyEnabled())
            self.setChildElementOptionalBooleanValue(child_element, "KEY-SLOT-USED-FOR-START-UP", controller.getKeySlotUsedForStartUp())
            self.setChildElementOptionalBooleanValue(child_element, "KEY-SLOT-USED-FOR-SYNC", controller.getKeySlotUsedForSync())
            self.setChildElementOptionalIntegerValue(child_element, "LATEST-TX", controller.getLatestTX())
            self.setChildElementOptionalIntegerValue(child_element, "LISTEN-TIMEOUT", controller.getListenTimeout())
            self.setChildElementOptionalIntegerValue(child_element, "MACRO-INITIAL-OFFSET-A", controller.getMacroInitialOffsetA())
            self.setChildElementOptionalIntegerValue(child_element, "MACRO-INITIAL-OFFSET-B", controller.getMacroInitialOffsetB())
            self.setChildElementOptionalIntegerValue(child_element, "MAXIMUM-DYNAMIC-PAYLOAD-LENGTH", controller.getMaximumDynamicPayloadLength())
            self.setChildElementOptionalIntegerValue(child_element, "MICRO-INITIAL-OFFSET-A", controller.getMicroInitialOffsetA())
            self.setChildElementOptionalIntegerValue(child_element, "MICRO-INITIAL-OFFSET-B", controller.getMicroInitialOffsetB())
            self.setChildElementOptionalIntegerValue(child_element, "MICRO-PER-CYCLE", controller.getMicroPerCycle())
            self.setChildElementOptionalTimeValue(child_element, "MICROTICK-DURATION", controller.getMicrotickDuration())
            self.setChildElementOptionalIntegerValue(child_element, "OFFSET-CORRECTION-OUT", controller.getOffsetCorrectionOut())
            self.setChildElementOptionalIntegerValue(child_element, "RATE-CORRECTION-OUT", controller.getRateCorrectionOut())
            self.setChildElementOptionalIntegerValue(child_element, "SAMPLES-PER-MICROTICK", controller.getSamplesPerMicrotick())
            self.setChildElementOptionalIntegerValue(child_element, "WAKE-UP-PATTERN", controller.getWakeUpPattern())

    def writeDataTransformationTransformerChainRefs(self, element: ET.Element, dtf: DataTransformation):
        refs = dtf.getTransformerChainRefs()
        if len(refs) > 0:
            child_element = ET.SubElement(element, "TRANSFORMER-CHAIN-REFS")
            for ref in refs:
                self.setChildElementOptionalRefType(child_element, "TRANSFORMER-CHAIN-REF", ref)

    def writeDataTransformation(self, element: ET.Element, dtf: DataTransformation):
        if dtf is not None:
            child_element = ET.SubElement(element, "DATA-TRANSFORMATION")
            self.writeIdentifiable(child_element, dtf)
            self.setChildElementOptionalBooleanValue(child_element, "EXECUTE-DESPITE-DATA-UNAVAILABILITY", dtf.getExecuteDespiteDataUnavailability())
            self.writeDataTransformationTransformerChainRefs(child_element, dtf)

    def writeDataTransformationSetDataTransformations(self, element: ET.Element, dtf_set: DataTransformationSet):
        dtfs = dtf_set.getDataTransformations()
        if len(dtfs) > 0:
            child_element = ET.SubElement(element, "DATA-TRANSFORMATIONS")
            for dtf in dtfs:
                if isinstance(dtf, DataTransformation):
                    self.writeDataTransformation(child_element, dtf)
                else:
                    self.notImplemented("Unsupported DataTransformation <%s>" % type(dtf))

    def writeDataTransformationSetTransformationTechnologies(self, element: ET.Element, dtf_set: DataTransformationSet):
        techs = dtf_set.getTransformationTechnologies()
        if len(techs) > 0:
            child_element = ET.SubElement(element, "TRANSFORMATION-TECHNOLOGYS")
            for tech in techs:
                if isinstance(tech, TransformationTechnology):
                    self.writeTransformationTechnology(child_element, tech)
                else:
                    self.notImplemented("Unsupported TransformationTechnology <%s>" % type(tech))

    def writeBufferPropertiesBufferComputation(self, element: ET.Element, properties: BufferProperties):
        computation = properties.getBufferComputation()
        if computation is not None:
            self.setCompuScale(element, "BUFFER-COMPUTATION", computation)

    def setBufferProperties(self, element: ET.Element, key: str, properties: BufferProperties):
        if properties is not None:
            child_element = ET.SubElement(element, key)
            self.writeBufferPropertiesBufferComputation(child_element, properties)
            self.setChildElementOptionalIntegerValue(child_element, "HEADER-LENGTH", properties.getHeaderLength())
            self.setChildElementOptionalBooleanValue(child_element, "IN-PLACE", properties.getInPlace())

    def writeDescribable(self, element: ET.Element, desc: Describable):
        self.writeARObjectAttributes(element, desc)
    
    def writeTransformationDescription(self, element: ET.Element, desc: TransformationDescription):
        self.writeDescribable(element, desc)
    
    def writeEndToEndTransformationDescription(self, element: ET.Element, desc: EndToEndTransformationDescription):
        if desc is not None:
            child_element = ET.SubElement(element, "END-TO-END-TRANSFORMATION-DESCRIPTION")
            self.writeTransformationDescription(child_element, desc)
            self.setChildElementOptionalLiteral(child_element, "DATA-ID-MODE", desc.getDataIdMode())
            self.setChildElementOptionalPositiveInteger(child_element, "MAX-DELTA-COUNTER", desc.getMaxDeltaCounter())
            self.setChildElementOptionalPositiveInteger(child_element, "MAX-ERROR-STATE-INIT", desc.getMaxErrorStateInit())
            self.setChildElementOptionalPositiveInteger(child_element, "MAX-ERROR-STATE-INVALID", desc.getMaxErrorStateInvalid())
            self.setChildElementOptionalPositiveInteger(child_element, "MAX-ERROR-STATE-VALID", desc.getMaxErrorStateValid())
            self.setChildElementOptionalPositiveInteger(child_element, "MAX-NO-NEW-OR-REPEATED-DATA", desc.getMaxNoNewOrRepeatedData())
            self.setChildElementOptionalPositiveInteger(child_element, "MIN-OK-STATE-INIT", desc.getMinOkStateInit())
            self.setChildElementOptionalPositiveInteger(child_element, "MIN-OK-STATE-INVALID", desc.getMinOkStateInvalid())
            self.setChildElementOptionalPositiveInteger(child_element, "MIN-OK-STATE-VALID", desc.getMinOkStateValid())
            self.setChildElementOptionalLiteral(child_element, "PROFILE-BEHAVIOR", desc.getProfileBehavior())
            self.setChildElementOptionalLiteral(child_element, "PROFILE-NAME", desc.getProfileName())
            self.setChildElementOptionalPositiveInteger(child_element, "SYNC-COUNTER-INIT", desc.getSyncCounterInit())
            self.setChildElementOptionalPositiveInteger(child_element, "UPPER-HEADER-BITS-TO-SHIFT", desc.getUpperHeaderBitsToShift())
            self.setChildElementOptionalPositiveInteger(child_element, "WINDOW-SIZE-INIT", desc.getWindowSizeInit())
            self.setChildElementOptionalPositiveInteger(child_element, "WINDOW-SIZE-INVALID", desc.getWindowSizeInvalid())
            self.setChildElementOptionalPositiveInteger(child_element, "WINDOW-SIZE-VALID", desc.getWindowSizeValid())

    def writeTransformationTechnologyTransformationDescriptions(self, element: ET.Element, tech: TransformationTechnology):
        desc = tech.getTransformationDescription()
        if desc is not None:
            child_element = ET.SubElement(element, "TRANSFORMATION-DESCRIPTIONS")
            if isinstance(desc, EndToEndTransformationDescription):
                self.writeEndToEndTransformationDescription(child_element, desc)
            else:
                self.notImplemented("Unsupported TransformationDescription <%s>" % type(desc))

    def writeTransformationTechnology(self, element: ET.Element, tech: TransformationTechnology):
        if tech is not None:
            child_element = ET.SubElement(element, "TRANSFORMATION-TECHNOLOGY")
            self.writeIdentifiable(child_element, tech)
            self.setBufferProperties(child_element, "BUFFER-PROPERTIES", tech.getBufferProperties())
            self.setChildElementOptionalBooleanValue(child_element, "NEEDS-ORIGINAL-DATA", tech.getNeedsOriginalData())
            self.setChildElementOptionalLiteral(child_element, "PROTOCOL", tech.getProtocol())
            self.writeTransformationTechnologyTransformationDescriptions(child_element, tech)
            self.setChildElementOptionalLiteral(child_element, "TRANSFORMER-CLASS", tech.getTransformerClass())
            self.setChildElementOptionalLiteral(child_element, "VERSION", tech.getVersion())

    def writeDataTransformationSet(self, element: ET.Element, dtf_set: DataTransformationSet):
        if dtf_set is not None:
            child_element = ET.SubElement(element, "DATA-TRANSFORMATION-SET")
            self.writeIdentifiable(child_element, dtf_set)
            self.writeDataTransformationSetDataTransformations(child_element, dtf_set)
            self.writeDataTransformationSetTransformationTechnologies(child_element, dtf_set)

    def writeARPackageElement(self, element: ET.Element, ar_element: ARElement):
        if isinstance(ar_element, ComplexDeviceDriverSwComponentType):
            self.writeComplexDeviceDriverSwComponentType(element, ar_element)
        elif isinstance(ar_element, SwcImplementation):
            self.writeSwcImplementation(element, ar_element)
        elif isinstance(ar_element, CompositionSwComponentType):
            self.writeCompositionSwComponentType(element, ar_element)
        elif isinstance(ar_element, ApplicationPrimitiveDataType):
            self.writeApplicationPrimitiveDataType(element, ar_element)
        elif isinstance(ar_element, ApplicationRecordDataType):
            self.writeApplicationRecordDataType(element, ar_element)
        elif isinstance(ar_element, SwBaseType):
            self.writeSwBaseType(element, ar_element)
        elif isinstance(ar_element, CompuMethod):
            self.writeCompuMethod(element, ar_element)
        elif isinstance(ar_element, ConstantSpecification):
            self.writeConstantSpecification(element, ar_element)
        elif isinstance(ar_element, DataConstr):
            self.writeDataConstr(element, ar_element)
        elif isinstance(ar_element, EndToEndProtectionSet):
            self.writeEndToEndProtectionSet(element, ar_element)
        elif isinstance(ar_element, SenderReceiverInterface):
            self.writeSenderReceiverInterface(element, ar_element)
        elif isinstance(ar_element, Unit):
            self.writeUnit(element, ar_element)
        elif isinstance(ar_element, BswModuleDescription):
            self.writeBswModuleDescription(element, ar_element)
        elif isinstance(ar_element, BswModuleEntry):
            self.writeBswModuleEntry(element, ar_element)
        elif isinstance(ar_element, SwcBswMapping):
            self.writeSwcBswMapping(element, ar_element)
        elif isinstance(ar_element, BswImplementation):
            self.writeBswImplementation(element, ar_element)
        elif isinstance(ar_element, ImplementationDataType):
            self.writeImplementationDataType(element, ar_element)
        elif isinstance(ar_element, ClientServerInterface):
            self.writeClientServerInterface(element, ar_element)
        elif isinstance(ar_element, ApplicationSwComponentType):
            self.writeApplicationSwComponentType(element, ar_element)
        elif isinstance(ar_element, EcuAbstractionSwComponentType):
            self.writeEcuAbstractionSwComponentType(element, ar_element)
        elif isinstance(ar_element, ApplicationArrayDataType):
            self.writeApplicationArrayDataType(element, ar_element)
        elif isinstance(ar_element, SwRecordLayout):
            self.writeSwRecordLayout(element, ar_element)
        elif isinstance(ar_element, SwAddrMethod):
            self.writeSwAddrMethod(element, ar_element)
        elif isinstance(ar_element, TriggerInterface):
            self.writeTriggerInterface(element, ar_element)
        elif isinstance(ar_element, ServiceSwComponentType):
            self.writeServiceSwComponentType(element, ar_element)
        elif isinstance(ar_element, DataTypeMappingSet):
            self.writeDataTypeMappingSet(element, ar_element)
        elif isinstance(ar_element, ModeDeclarationGroup):
            self.writeModeDeclarationGroup(element, ar_element)
        elif isinstance(ar_element, ModeSwitchInterface):
            self.writeModeSwitchInterface(element, ar_element)
        elif isinstance(ar_element, SwcTiming):
            self.writeSwcTiming(element, ar_element)
        elif isinstance(ar_element, LinUnconditionalFrame):
            self.writeLinUnconditionalFrame(element, ar_element)
        elif isinstance(ar_element, NmConfig):
            self.writeNmConfig(element, ar_element)
        elif isinstance(ar_element, NmPdu):
            self.writeNmPdu(element, ar_element)
        elif isinstance(ar_element, NPdu):
            self.writeNPdu(element, ar_element)
        elif isinstance(ar_element, DcmIPdu):
            self.writeDcmIPdu(element, ar_element)
        elif isinstance(ar_element, SecuredIPdu):
            self.writeSecuredIPdu(element, ar_element)
        elif isinstance(ar_element, CanTpConfig):
            self.writeCanTpConfig(element, ar_element)
        elif isinstance(ar_element, LinTpConfig):
            self.writeLinTpConfig(element, ar_element)
        elif isinstance(ar_element, LinCluster):
            self.writeLinCluster(element, ar_element)
        elif isinstance(ar_element, CanCluster):
            self.writeCanCluster(element, ar_element)
        elif isinstance(ar_element, CanFrame):
            self.writeCanFrame(element, ar_element)
        elif isinstance(ar_element, Gateway):
            self.writeGateway(element, ar_element)
        elif isinstance(ar_element, ISignal):
            self.writeISignal(element, ar_element)
        elif isinstance(ar_element, System):
            self.writeSystem(element, ar_element)
        elif isinstance(ar_element, EcuInstance):
            self.writeEcuInstance(element, ar_element)
        elif isinstance(ar_element, ISignalIPdu):
            self.writeISignalIPdu(element, ar_element)
        elif isinstance(ar_element, SystemSignal):
            self.writeSystemSignal(element, ar_element)
        elif isinstance(ar_element, ParameterInterface):
            self.writeParameterInterface(element, ar_element)
        elif isinstance(ar_element, GenericEthernetFrame):
            self.writeGenericEthernetFrame(element, ar_element)
        elif isinstance(ar_element, LifeCycleInfoSet):
            self.writeLifeCycleInfoSet(element, ar_element)
        elif isinstance(ar_element, PhysicalDimension):
            self.writePhysicalDimension(element, ar_element)
        elif isinstance(ar_element, FlatMap):
            self.writeFlatMap(element, ar_element)
        elif isinstance(ar_element, PortInterfaceMappingSet):
            self.writePortInterfaceMappingSet(element, ar_element)
        elif isinstance(ar_element, EthernetCluster):
            self.writeEthernetCluster(element, ar_element)
        elif isinstance(ar_element, ISignalIPduGroup):
            self.writeISignalIPduGroup(element, ar_element)
        elif isinstance(ar_element, DiagnosticConnection):
            self.writeDiagnosticConnection(element, ar_element)
        elif isinstance(ar_element, DiagnosticServiceTable):
            self.writeDiagnosticServiceTable(element, ar_element)
        elif isinstance(ar_element, MultiplexedIPdu):
            self.writeMultiplexedIPdu(element, ar_element)
        elif isinstance(ar_element, UserDefinedIPdu):
            self.writeUserDefinedIPdu(element, ar_element)
        elif isinstance(ar_element, UserDefinedPdu):
            self.writeUserDefinedPdu(element, ar_element)
        elif isinstance(ar_element, GeneralPurposePdu):
            self.writeGeneralPurposePdu(element, ar_element)
        elif isinstance(ar_element, GeneralPurposeIPdu):
            self.writeGeneralPurposeIPdu(element, ar_element)
        elif isinstance(ar_element, SecureCommunicationPropsSet):
            self.writeSecureCommunicationPropsSet(element, ar_element)
        elif isinstance(ar_element, SoAdRoutingGroup):
            self.writeSoAdRoutingGroup(element, ar_element)
        elif isinstance(ar_element, DoIpTpConfig):
            self.writeDoIpTpConfig(element, ar_element)
        elif isinstance(ar_element, HwElement):
            self.writeHwElement(element, ar_element)
        elif isinstance(ar_element, HwCategory):
            self.writeHwCategory(element, ar_element)
        elif isinstance(ar_element, HwType):
            self.writeHwType(element, ar_element)
        elif isinstance(ar_element, DataTransformationSet):
            self.writeDataTransformationSet(element, ar_element)
        elif isinstance(ar_element, FlexrayFrame):
            self.writeFlexrayFrame(element, ar_element)
        elif isinstance(ar_element, ISignalGroup):
            self.writeISignalGroup(element, ar_element)
        elif isinstance(ar_element, SystemSignalGroup):
            self.writeSystemSignalGroup(element, ar_element)
        elif isinstance(ar_element, FlexrayCluster):
            self.writeFlexrayCluster(element, ar_element)
        elif isinstance(ar_element, Collection):
            self.writeCollection(element, ar_element)
        elif isinstance(ar_element, KeywordSet):
            self.writeKeywordSet(element, ar_element)
        elif isinstance(ar_element, PortPrototypeBlueprint):
            self.writePortPrototypeBlueprint(element, ar_element)
        else:
            self.notImplemented("Unsupported Elements of ARPackage <%s>" % type(ar_element))

    def writeReferenceBases(self, element: ET.Element, bases: List[ReferenceBase]):
        self.logger.debug("Write ReferenceBases")
        if len(bases) > 0:
            bases_tag = ET.SubElement(element, "REFERENCE-BASES")
            for base in bases:
                child_element = ET.SubElement(bases_tag, "REFERENCE-BASE")
                self.setChildElementOptionalLiteral(child_element, "SHORT-LABEL", base.getShortLabel())
                self.setChildElementOptionalBooleanValue(child_element, "IS-DEFAULT", base.getIsDefault())
                self.setChildElementOptionalBooleanValue(child_element, "IS-GLOBAL", base.getIsDefault())
                self.setChildElementOptionalBooleanValue(child_element, "BASE-IS-THIS-PACKAGE", base.getBaseIsThisPackage())
                self.setChildElementOptionalRefType(child_element, "PACKAGE-REF", base.getPackageRef())

    def writeARPackage(self, element: ET.Element, pkg: ARPackage):
        self.logger.debug("Write ARPackage %s" % pkg.getFullName())
        child_element = ET.SubElement(element, "AR-PACKAGE")

        self.writeIdentifiable(child_element, pkg)
        self.writeReferenceBases(child_element, pkg.getReferenceBases())
        self.writeARPackageElements(child_element, pkg)
        self.writeARPackages(child_element, pkg.getARPackages())

    def writeARPackageElements(self, element: ET.Element, pkg: ARPackage):
        if pkg.getTotalElement() > 0:
            elements_tag = ET.SubElement(element, "ELEMENTS")

            for ar_element in pkg.getElements():
                if not isinstance(ar_element, ARPackage):
                    self.writeARPackageElement(elements_tag, ar_element)

    def writeARPackages(self, element: ET.Element, pkgs: List[ARPackage]):
        if len(pkgs) > 0:
            child_element = ET.SubElement(element, "AR-PACKAGES")
            for pkg in pkgs:
                if isinstance(pkg, ARPackage):
                    self.writeARPackage(child_element, pkg)
                else:
                    self.notImplemented("Unsupported ARPackage <%s>" % type(pkg))

    def save(self, filename, document: AUTOSAR):
        self.logger.info("Saving %s ..." % filename)

        root = ET.Element("AUTOSAR", self.nsmap)
        root.attrib["xmlns:xsi"] = "http://www.w3.org/2001/XMLSchema-instance"
        if document.schema_location is not None:
            root.attrib["xsi:schemaLocation"] = document.schema_location
        else:
            root.attrib["xsi:schemaLocation"] = "http://autosar.org/schema/r4.0 AUTOSAR_4-0-3.xsd"
        
        self.setAdminData(root, document.getAdminData())
        self.writeARPackages(root, document.getARPackages())

        self.saveToFile(filename, root)
