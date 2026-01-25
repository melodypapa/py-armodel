from typing import List
import xml.etree.ElementTree as ET
import os




from ..models.M2.MSR.AsamHdo.AdminData import AdminData, DocRevision, Modification
from ..models.M2.MSR.AsamHdo.BaseTypes import BaseTypeDirectDefinition, SwBaseType
from ..models.M2.MSR.AsamHdo.Constraints.GlobalConstraints import DataConstrRule, InternalConstrs, PhysConstrs, DataConstr
from ..models.M2.MSR.AsamHdo.ComputationMethod import CompuConstContent, CompuConstFormulaContent, CompuConstNumericContent, CompuMethod, Compu
from ..models.M2.MSR.AsamHdo.ComputationMethod import CompuConst, CompuConstTextContent, CompuNominatorDenominator, CompuRationalCoeffs, CompuScale
from ..models.M2.MSR.AsamHdo.ComputationMethod import CompuScaleConstantContents, CompuScaleRationalFormula, CompuScales
from ..models.M2.MSR.AsamHdo.SpecialData import Sdg, Sd
from ..models.M2.MSR.AsamHdo.Units import PhysicalDimension, Unit
from ..models.M2.MSR.CalibrationData.CalibrationValue import SwValueCont, SwValues
from ..models.M2.MSR.DataDictionary.AuxillaryObjects import SwAddrMethod
from ..models.M2.MSR.DataDictionary.DataDefProperties import SwDataDefProps, SwPointerTargetProps
from ..models.M2.MSR.DataDictionary.CalibrationParameter import SwCalprmAxis
from ..models.M2.MSR.DataDictionary.Axis import SwAxisGrouped, SwAxisIndividual
from ..models.M2.MSR.DataDictionary.RecordLayout import SwRecordLayout, SwRecordLayoutGroupContent, SwRecordLayoutV
from ..models.M2.MSR.DataDictionary.DataDefProperties import ValueList
from ..models.M2.MSR.DataDictionary.RecordLayout import SwRecordLayoutGroup
from ..models.M2.MSR.DataDictionary.CalibrationParameter import SwCalprmAxisSet
from ..models.M2.MSR.DataDictionary.ServiceProcessTask import SwServiceArg
from ..models.M2.MSR.Documentation.Annotation import Annotation, GeneralAnnotation
from ..models.M2.MSR.Documentation.BlockElements.Figure import Graphic, LGraphic, MlFigure
from ..models.M2.MSR.Documentation.TextModel.BlockElements import DocumentationBlock
from ..models.M2.MSR.Documentation.TextModel.BlockElements.ListElements import ARList
from ..models.M2.MSR.Documentation.TextModel.LanguageDataModel import LLongName, LOverviewParagraph, LParagraph, LanguageSpecific
from ..models.M2.MSR.Documentation.TextModel.MultilanguageData import MultiLanguageOverviewParagraph, MultiLanguageParagraph, MultiLanguagePlainText
from ..models.M2.MSR.Documentation.TextModel.MultilanguageData import MultilanguageLongName
from ..models.M2.MSR.Documentation.TextModel.BlockElements.PaginationAndView import DocumentViewSelectable, Paginateable


from ..models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from ..models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior import BswApiOptions, BswAsynchronousServerCallPoint, BswBackgroundEvent
from ..models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior import BswSynchronousServerCallPoint
from ..models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior import BswCalledEntity, BswDataReceivedEvent, BswModuleCallPoint
from ..models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior import BswInternalTriggeringPoint, BswOperationInvokedEvent
from ..models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior import BswDataReceptionPolicy, BswExternalTriggerOccurredEvent, BswInternalBehavior
from ..models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior import BswInternalTriggerOccurredEvent, BswInterruptEntity, BswModeSwitchEvent
from ..models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior import BswModuleEntity, BswQueuedDataReceptionPolicy, BswSchedulableEntity
from ..models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior import BswScheduleEvent, BswModeSenderPolicy, BswTimingEvent, BswVariableAccess
from ..models.M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces import BswModuleClientServerEntry, BswModuleEntry
from ..models.M2.AUTOSARTemplates.BswModuleTemplate.BswImplementation import BswImplementation
from ..models.M2.AUTOSARTemplates.BswModuleTemplate.BswOverview import BswModuleDescription
from ..models.M2.AUTOSARTemplates.CommonStructure import ApplicationValueSpecification, ArrayValueSpecification, ConstantReference
from ..models.M2.AUTOSARTemplates.CommonStructure import ConstantSpecification, NumericalValueSpecification, RecordValueSpecification
from ..models.M2.AUTOSARTemplates.CommonStructure import TextValueSpecification, ValueSpecification
from ..models.M2.AUTOSARTemplates.CommonStructure.Filter import DataFilter
from ..models.M2.AUTOSARTemplates.CommonStructure.FlatMap import FlatInstanceDescriptor, FlatMap
from ..models.M2.AUTOSARTemplates.CommonStructure.Implementation import ImplementationProps, Code
from ..models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior import ExecutableEntity, InternalBehavior
from ..models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration import ModeDeclarationGroup, ModeDeclarationGroupPrototypeMapping
from ..models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration import ModeRequestTypeMap, ModeDeclarationGroupPrototype
from ..models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption import ResourceConsumption
from ..models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.MemorySectionUsage import MemorySection
from ..models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.StackUsage import RoughEstimateStackUsage, StackUsage
from ..models.M2.AUTOSARTemplates.CommonStructure.SwcBswMapping import SwcBswMapping, SwcBswRunnableMapping
from ..models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import CryptoServiceNeeds, DiagEventDebounceMonitorInternal, DltUserNeeds, ServiceNeeds
from ..models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import DiagnosticCapabilityElement, DtcStatusChangeNotificationNeeds
from ..models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import DiagnosticCommunicationManagerNeeds, DiagnosticEventInfoNeeds
from ..models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import DiagnosticEventNeeds, DiagnosticRoutineNeeds, DiagnosticValueNeeds
from ..models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import EcuStateMgrUserNeeds, NvBlockNeeds, RoleBasedDataAssignment
from ..models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import RoleBasedDataTypeAssignment, ServiceDependency
from ..models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.BlueprintDedicated.PortPrototypeBlueprint import PortPrototypeBlueprint
from ..models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.Keyword import Keyword, KeywordSet
from ..models.M2.AUTOSARTemplates.CommonStructure.Implementation import Implementation
from ..models.M2.AUTOSARTemplates.CommonStructure.ImplementationDataTypes import ImplementationDataType, ImplementationDataTypeElement
from ..models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.ExecutionOrderConstraint import ExecutionOrderConstraint
from ..models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.TimingExtensions import SwcTiming, TimingExtension
from ..models.M2.AUTOSARTemplates.CommonStructure.TriggerDeclaration import Trigger
from ..models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticContribution import DiagnosticServiceTable
from ..models.M2.AUTOSARTemplates.ECUCDescriptionTemplate import EcucAbstractReferenceValue, EcucContainerValue
from ..models.M2.AUTOSARTemplates.ECUCDescriptionTemplate import EcucInstanceReferenceValue
from ..models.M2.AUTOSARTemplates.ECUCDescriptionTemplate import EcucModuleConfigurationValues, EcucNumericalParamValue, EcucParameterValue
from ..models.M2.AUTOSARTemplates.ECUCDescriptionTemplate import EcucReferenceValue, EcucTextualParamValue, EcucValueCollection
from ..models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucDefinitionElement, EcucModuleDef
from ..models.M2.AUTOSARTemplates.EcuResourceTemplate import HwDescriptionEntity, HwElement, HwPinGroup
from ..models.M2.AUTOSARTemplates.EcuResourceTemplate.HwElementCategory import HwAttributeDef, HwCategory, HwType
from ..models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucAbstractConfigurationClass, EcucAbstractInternalReferenceDef
from ..models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucFunctionNameDef, EcucReferenceDef
from ..models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucAbstractReferenceDef, EcucSymbolicNameReferenceDef
from ..models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucAbstractStringParamDef, EcucBooleanParamDef
from ..models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucValueConfigurationClass
from ..models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucCommonAttributes, EcucEnumerationLiteralDef, EcucEnumerationParamDef
from ..models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucFloatParamDef, EcucIntegerParamDef
from ..models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucChoiceContainerDef, EcucStringParamDef
from ..models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucContainerDef, EcucParameterDef
from ..models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucMultiplicityConfigurationClass, EcucParamConfContainerDef
from ..models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.AnyInstanceRef import AnyInstanceRef
from ..models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ElementCollection import Collection
from ..models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import ARElement, Describable, Identifiable
from ..models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Referrable, MultilanguageReferrable
from ..models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.EngineeringObject import AutosarEngineeringObject, EngineeringObject
from ..models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARPackage, ReferenceBase
from ..models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType, ARLiteral
from ..models.M2.AUTOSARTemplates.GenericStructure.LifeCycles import LifeCycleInfo, LifeCycleInfoSet, LifeCyclePeriod
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes import ApplicationPrimitiveDataType, ApplicationRecordDataType
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes import ApplicationArrayDataType, ApplicationCompositeDataType
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes import ApplicationDataType, AutosarDataType, DataTypeMap, DataTypeMappingSet
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.EndToEndProtection import EndToEndProtectionISignalIPdu, EndToEndProtectionSet
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.EndToEndProtection import EndToEndDescription, EndToEndProtection
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.EndToEndProtection import EndToEndProtectionVariablePrototype
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.InstanceRefs import POperationInAtomicSwcInstanceRef, PPortInCompositionInstanceRef
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.InstanceRefs import ROperationInAtomicSwcInstanceRef, RPortInCompositionInstanceRef
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.InstanceRefs import ApplicationCompositeElementInPortInterfaceInstanceRef
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import CompositeNetworkRepresentation, ModeSwitchedAckRequest, NvProvideComSpec
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import NvRequireComSpec, PPortComSpec, RPortComSpec
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import TransformationComSpecProps, UserDefinedTransformationComSpecProps
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import TransmissionAcknowledgementRequest
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import ClientComSpec, ModeSwitchReceiverComSpec, ModeSwitchSenderComSpec
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import NonqueuedReceiverComSpec, NonqueuedSenderComSpec, ParameterRequireComSpec
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import QueuedReceiverComSpec, QueuedSenderComSpec, ReceiverComSpec, SenderComSpec
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import ServerComSpec
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.Components import AbstractProvidedPortPrototype, AbstractRequiredPortPrototype, PRPortPrototype
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.Components import ApplicationSwComponentType, ComplexDeviceDriverSwComponentType
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.Composition import CompositionSwComponentType
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.Components import EcuAbstractionSwComponentType, PortGroup
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.Components import SensorActuatorSwComponentType, ServiceSwComponentType, SwComponentType
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.Components import SymbolProps, PPortPrototype, RPortPrototype
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.Components import AtomicSwComponentType
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs import InnerPortGroupInCompositionInstanceRef
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs import ModeGroupInAtomicSwcInstanceRef
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs import PModeGroupInAtomicSwcInstanceRef
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs import RModeGroupInAtomicSWCInstanceRef
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs import RModeInAtomicSwcInstanceRef
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs import RVariableInAtomicSwcInstanceRef
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.Composition import AssemblySwConnector, DelegationSwConnector, SwComponentPrototype, SwConnector
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes import ApplicationCompositeElementDataPrototype
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes import ApplicationRecordElement, AutosarDataPrototype
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes import DataPrototype, ParameterDataPrototype, VariableDataPrototype
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import ArgumentDataPrototype, ClientServerInterface, ClientServerInterfaceMapping
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import ModeDeclarationMapping
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import ModeDeclarationMappingSet, ModeInterfaceMapping
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import ClientServerOperation, ClientServerOperationMapping
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import DataPrototypeMapping, InvalidationPolicy, ModeSwitchInterface
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import ParameterInterface, PortInterface, PortInterfaceMappingSet
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import SenderReceiverInterface, TriggerInterface, DataInterface
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import VariableAndParameterInterfaceMapping
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.SwcImplementation import SwcImplementation
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior import RunnableEntity, RunnableEntityArgument, SwcInternalBehavior
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.AutosarVariableRef import AutosarVariableRef
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements import ParameterAccess
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.IncludedDataTypes import IncludedDataTypeSet
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.InstanceRefsUsage import AutosarParameterRef, ParameterInAtomicSWCTypeInstanceRef
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.InstanceRefsUsage import VariableInAtomicSWCTypeInstanceRef
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ModeDeclarationGroup import IncludedModeDeclarationGroupSet
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ModeDeclarationGroup import ModeAccessPoint, ModeSwitchPoint
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.PortAPIOptions import PortAPIOption, PortDefinedArgumentValue
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents import AsynchronousServerCallReturnsEvent, BackgroundEvent
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents import DataSendCompletedEvent
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents import DataReceivedEvent, InitEvent, InternalTriggerOccurredEvent
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents import ModeSwitchedAckEvent, OperationInvokedEvent, RTEEvent
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents import SwcModeSwitchEvent, TimingEvent
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ServerCall import ServerCallPoint
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ServiceMapping import RoleBasedPortAssignment, SwcServiceDependency

from ..models.M2.AUTOSARTemplates.SystemTemplate import SwcToEcuMapping, System, SystemMapping
from ..models.M2.AUTOSARTemplates.SystemTemplate.DataMapping import SenderRecCompositeTypeMapping
from ..models.M2.AUTOSARTemplates.SystemTemplate.DataMapping import SenderRecRecordElementMapping, SenderRecRecordTypeMapping
from ..models.M2.AUTOSARTemplates.SystemTemplate.DataMapping import SenderReceiverToSignalGroupMapping, SenderReceiverToSignalMapping
from ..models.M2.AUTOSARTemplates.SystemTemplate.DiagnosticConnection import DiagnosticConnection
from ..models.M2.AUTOSARTemplates.SystemTemplate.ECUResourceMapping import ECUMapping
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
from ..models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.NetworkEndpoint import NetworkEndpoint
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
from ..models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import DcmIPdu, DynamicPart, DynamicPartAlternative, Frame
from ..models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import FrameTriggering, GeneralPurposeIPdu, GeneralPurposePdu
from ..models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import IPdu, IPduTiming, ISignal, ISignalGroup, ISignalIPdu
from ..models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import ISignalIPduGroup, ISignalToIPduMapping, ISignalTriggering
from ..models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import MultiplexedIPdu, MultiplexedPart, NPdu, NmPdu, Pdu
from ..models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import PduTriggering, SecureCommunicationAuthenticationProps
from ..models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import SecureCommunicationFreshnessProps, SecureCommunicationProps
from ..models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import SecureCommunicationPropsSet, SecuredIPdu, SegmentPosition
from ..models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import StaticPart, SystemSignal, SystemSignalGroup
from ..models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import UserDefinedIPdu, UserDefinedPdu
from ..models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import AbstractCanCluster, CanCluster, CanClusterBusOffRecovery
from ..models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import FlexrayPhysicalChannel, CycleRepetition, CommunicationCycle
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

from .abstract_arxml_parser import AbstractARXMLParser

# Import specialized parsers
from .parsers.common_structure_parser import CommonStructureParser
from .parsers.datatype_parser import DataTypeParser
from .parsers.port_interface_parser import PortInterfaceParser
from .parsers.component_parser import ComponentParser
from .parsers.behavior_parser import BehaviorParser
from .parsers.bsw_module_parser import BswModuleParser
from .parsers.system_template_parser import SystemTemplateParser
from .parsers.ecuc_parser import EcucParser
from .parsers.network_management_parser import NetworkManagementParser


class ARXMLParser(AbstractARXMLParser):
    def __init__(self, options=None) -> None:
        super().__init__(options)

        # Initialize specialized parsers
        self._common_parser = CommonStructureParser(options)
        self._datatype_parser = DataTypeParser(options, self)
        self._port_interface_parser = PortInterfaceParser(options, self)
        self._component_parser = ComponentParser(options)
        self._behavior_parser = BehaviorParser(options)
        self._bsw_module_parser = BswModuleParser(options)
        self._system_template_parser = SystemTemplateParser(options)
        self._ecuc_parser = EcucParser(options)
        self._network_management_parser = NetworkManagementParser(options)

        # Create parser registry for element routing
        # This will be populated incrementally as we migrate methods
        self._parser_registry = {
            # Common structure
            'AR-ARPACKAGE': self._common_parser,

            # Data types (populated during migration)
            'APPLICATION-PRIMITIVE-DATA-TYPE': self._datatype_parser,
            'APPLICATION-RECORD-DATA-TYPE': self._datatype_parser,
            'APPLICATION-ARRAY-DATA-TYPE': self._datatype_parser,
            'IMPLEMENTATION-DATA-TYPE': self._datatype_parser,
            'COMPU-METHOD': self._datatype_parser,
            'DATA-CONSTR': self._datatype_parser,
            'UNIT': self._datatype_parser,

            # Port interfaces (populated during migration)
            'SENDER-RECEIVER-INTERFACE': self._port_interface_parser,
            'CLIENT-SERVER-INTERFACE': self._port_interface_parser,
            'MODE-SWITCH-INTERFACE': self._port_interface_parser,
            'PARAMETER-INTERFACE': self._port_interface_parser,
            'TRIGGER-INTERFACE': self._port_interface_parser,
            'DATA-INTERFACE': self._port_interface_parser,
            'MODE-DECLARATION-GROUP': self._port_interface_parser,
            'PORT-INTERFACE-MAPPING-SET': self._port_interface_parser,
            'PORT-PROTOTYPE-BLUEPRINT': self._port_interface_parser,

            # Components (populated during migration)
            # 'APPLICATION-SW-COMPONENT-TYPE': self._component_parser,

            # Behaviors (populated during migration)
            # 'SWC-INTERNAL-BEHAVIOR': self._behavior_parser,

            # BSW modules (populated during migration)
            # 'BSW-MODULE-DESCRIPTION': self._bsw_module_parser,

            # System (populated during migration)
            # 'SYSTEM': self._system_template_parser,

            # ECUC (populated during migration)
            # 'ECUC-VALUE-COLLECTION': self._ecuc_parser,

            # Network management (populated during migration)
            # 'NM-CONFIG': self._network_management_parser,
        }

    # Add helper method to get parser by tag
    def _get_parser_instance(self, tag: str):
        """Get specialized parser instance for element tag."""
        if tag in self._parser_registry:
            return self._parser_registry[tag]
        return None

    def getChildElementRxIdentifierRange(self, element: ET.Element, key: str) -> RxIdentifierRange:
        child_element = self.find(element, key)
        range = None
        if child_element is not None:
            range = RxIdentifierRange()
            range.setLowerCanId(self.getChildElementOptionalNumericalValue(child_element, "LOWER-CAN-ID")) \
                 .setUpperCanId(self.getChildElementOptionalNumericalValue(child_element, "UPPER-CAN-ID"))
        return range

    def readSd(self, element: ET.Element, sdg: Sdg):
        """Delegate to CommonStructureParser."""
        return self._common_parser.readSd(element, sdg)

    def readSdgCaption(self, element: ET.Element, sdg: Sdg):
        """Delegate to CommonStructureParser."""
        return self._common_parser.readSdgCaption(element, sdg)

    def readSdgSdxRefs(self, element: ET.SubElement, sdg: Sdg):
        """Delegate to CommonStructureParser."""
        return self._common_parser.readSdgSdxRefs(element, sdg)

    def getSdg(self, element: ET.Element) -> Sdg:
        """Delegate to CommonStructureParser."""
        return self._common_parser.getSdg(element)

    def readAdminDataSdgs(self, element: ET.Element, admin_data: AdminData):
        """Delegate to CommonStructureParser."""
        return self._common_parser.readAdminDataSdgs(element, admin_data)

    def readModification(self, element: ET.Element, modification: Modification):
        """Delegate to CommonStructureParser."""
        return self._common_parser.readModification(element, modification)

    def readDocRevisionModifications(self, element: ET.Element, revision: DocRevision):
        """Delegate to CommonStructureParser."""
        return self._common_parser.readDocRevisionModifications(
            element, revision
        )

    def readDocRevision(self, element: ET.Element, revision: DocRevision):
        """Delegate to CommonStructureParser."""
        return self._common_parser.readDocRevision(element, revision)

    def readAdminDataDocRevisions(self, element: ET.Element, admin_data: AdminData):
        """Delegate to CommonStructureParser."""
        return self._common_parser.readAdminDataDocRevisions(
            element, admin_data
        )

    def getAdminData(self, element: ET.Element, key: str) -> AdminData:
        """Delegate to CommonStructureParser."""
        return self._common_parser.getAdminData(element, key)

    def readReferrable(self, element: ET.Element, referrable: Referrable):
        """Delegate to CommonStructureParser."""
        return self._common_parser.readReferrable(element, referrable)

    def readMultilanguageReferrable(self, element: ET.Element, referrable: MultilanguageReferrable):
        """Delegate to CommonStructureParser."""
        return self._common_parser.readMultilanguageReferrable(
            element, referrable
        )

    def readIdentifiable(self, element: ET.Element, identifiable: Identifiable):
        """Delegate to CommonStructureParser."""
        return self._common_parser.readIdentifiable(element, identifiable)

    def readARElement(self, element: ET.Element, ar_element: ARElement):
        """Delegate to CommonStructureParser."""
        return self._common_parser.readARElement(element, ar_element)

    def readLLongName(self, element: ET.Element, long_name: MultilanguageLongName):
        """Delegate to CommonStructureParser."""
        return self._common_parser.readLLongName(element, long_name)

    def getMultilanguageLongName(self, element: ET.Element, key: str) -> MultilanguageLongName:
        """Delegate to CommonStructureParser."""
        return self._common_parser.getMultilanguageLongName(element, key)

    def readLOverviewParagraph(self, element: ET.Element, paragraph: MultiLanguageOverviewParagraph):
        """Delegate to CommonStructureParser."""
        return self._common_parser.readLOverviewParagraph(element, paragraph)

    def getMultiLanguageOverviewParagraph(self, element: ET.Element, key: str) -> MultiLanguageOverviewParagraph:
        """Delegate to CommonStructureParser."""
        return self._common_parser.getMultiLanguageOverviewParagraph(
            element, key
        )
    
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
        if (child_element is not None):
            instance_ref = AutosarVariableRef()
            self.readARObjectAttributes(child_element, instance_ref)
            instance_ref.setAutosarVariableIRef(self.getVariableInAtomicSWCTypeInstanceRef(self.find(child_element, "AUTOSAR-VARIABLE-IREF")))
            instance_ref.setLocalVariableRef(self.getChildElementOptionalRefType(child_element, "LOCAL-VARIABLE-REF"))
        return instance_ref

    def _readVariableAccesses(self, element: ET.Element, parent: RunnableEntity, key: str):
        for child_element in self.findall(element, "%s/VARIABLE-ACCESS" % key):
            short_name = self.getShortName(child_element)

            # self.logger.debug("Read VariableAccesses %s" % short_name)

            if (key == "DATA-RECEIVE-POINT-BY-ARGUMENTS"):
                variable_access = parent.createDataReceivePointByArgument(short_name)
                variable_access.setAccessedVariableRef(self.getAutosarVariableRef(child_element, "ACCESSED-VARIABLE"))
            elif (key == "DATA-RECEIVE-POINT-BY-VALUES"):
                variable_access = parent.createDataReceivePointByValue(short_name)
                variable_access.setAccessedVariableRef(self.getAutosarVariableRef(child_element, "ACCESSED-VARIABLE"))
            elif (key == "DATA-READ-ACCESSS"):
                variable_access = parent.createDataReadAccess(short_name)
                variable_access.setAccessedVariableRef(self.getAutosarVariableRef(child_element, "ACCESSED-VARIABLE"))
            elif (key == "DATA-WRITE-ACCESSS"):
                variable_access = parent.createDataWriteAccess(short_name)
                variable_access.setAccessedVariableRef(self.getAutosarVariableRef(child_element, "ACCESSED-VARIABLE"))
            elif (key == "DATA-SEND-POINTS"):
                variable_access = parent.createDataSendPoint(short_name)
                variable_access.setAccessedVariableRef(self.getAutosarVariableRef(child_element, "ACCESSED-VARIABLE"))
            elif (key == "WRITTEN-LOCAL-VARIABLES"):
                variable_access = parent.createWrittenLocalVariable(short_name)
                variable_access.setAccessedVariableRef(self.getAutosarVariableRef(child_element, "ACCESSED-VARIABLE"))
            elif (key == "READ-LOCAL-VARIABLES"):
                variable_access = parent.createReadLocalVariable(short_name)
                variable_access.setAccessedVariableRef(self.getAutosarVariableRef(child_element, "ACCESSED-VARIABLE"))
            else:
                self.notImplemented("Unsupported Variable Accesss <%s>" % key)

            self.readIdentifiable(child_element, variable_access)

    def readBswModuleDescriptionImplementedEntryRefs(self, element: ET.Element, parent: BswModuleDescription):
        for child_element in self.findall(element, "PROVIDED-ENTRYS/BSW-MODULE-ENTRY-REF-CONDITIONAL"):
            ref = self.getChildElementOptionalRefType(child_element, "BSW-MODULE-ENTRY-REF")
            if (ref is not None):
                parent.addImplementedEntryRef(ref)
            # self.logger.debug("ImplementedEntry <%s> of BswModuleDescription <%s> has been added", ref.value, parent.getShortName())

    def readModeDeclarationGroupPrototype(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readModeDeclarationGroupPrototype(*args, **kwargs)


    def readBswModuleDescriptionProvidedModeGroups(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readBswModuleDescriptionProvidedModeGroups(*args, **kwargs)


    def readBswModuleDescriptionRequiredModeGroups(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readBswModuleDescriptionRequiredModeGroups(*args, **kwargs)


    def readCanEnterExclusiveAreaRefs(self, element: ET.Element, entity: ExecutableEntity):
        for ref in self.getChildElementRefTypeList(element, "CAN-ENTER-EXCLUSIVE-AREA-REFS/CAN-ENTER-EXCLUSIVE-AREA-REF"):
            entity.addCanEnterExclusiveAreaRef(ref)

    def readExecutableEntity(self, element: ET.Element, entity: ExecutableEntity):
        # self.logger.debug("Read ExecutableEntity %s" % entity.getShortName())
        self.readIdentifiable(element, entity)
        self.readCanEnterExclusiveAreaRefs(element, entity)
        entity.setMinimumStartInterval(self.getChildElementOptionalFloatValue(element, "MINIMUM-START-INTERVAL")) \
              .setSwAddrMethodRef(self.getChildElementOptionalRefType(element, "SW-ADDR-METHOD-REF"))

    def readBswModuleEntityManagedModeGroups(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readBswModuleEntityManagedModeGroups(*args, **kwargs)


    def readBswEvent(self, element: ET.Element, event: BswScheduleEvent):
        event.startsOnEventRef = self.getChildElementOptionalRefType(element, "STARTS-ON-EVENT-REF")

    def readBswScheduleEvent(self, element, event: BswScheduleEvent):
        self.readBswEvent(element, event)

    def readBswModeSwitchEvent(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readBswModeSwitchEvent(*args, **kwargs)


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
        policy.setProvidedModeGroupRef(self.getChildElementOptionalRefType(element, "PROVIDED-MODE-GROUP-REF"))
        policy.setQueueLength(self.getChildElementOptionalNumericalValue(element, "QUEUE-LENGTH"))
        return policy

    def readBswInternalBehaviorModeSenderPolicy(self, element: ET.Element, parent: BswInternalBehavior):
        for child_element in self.findall(element, "MODE-SENDER-POLICYS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "BSW-MODE-SENDER-POLICY":
                parent.addModeSenderPolicy(self.getBswModeSenderPolicy(child_element))
            else:
                self.raiseError("Unsupported ModeSenderPolicy type <%s>." % tag_name)

    def readDataTypeMappingRefs(self, element: ET.Element, behavior: InternalBehavior):
        """Delegate to DataTypeParser."""
        return self._datatype_parser.readDataTypeMappingRefs(element, behavior)

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
        self.readDataTypeMappingRefs(element, behavior)
        self.readInternalBehaviorStaticMemories(element, behavior)

    def getRoleBasedDataAssignment(self, element: ET.Element) -> RoleBasedDataAssignment:
        assignment = RoleBasedDataAssignment()
        assignment.setRole(self.getChildElementOptionalLiteral(element, "ROLE")) \
                  .setUsedDataElement(self.getAutosarVariableRef(element, "USED-DATA-ELEMENT")) \
                  .setUsedParameterElement(self.getAutosarParameterRef(element, "USED-PARAMETER-ELEMENT")) \
                  .setUsedPimRef(self.getChildElementOptionalRefType(element, "USED-PIM-REF"))
        return assignment
    
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
            if (tag_name == "ROLE-BASED-DATA-TYPE-ASSIGNMENT"):
                dependency.addAssignedDataType(self.getRoleBasedDataTypeAssignment(child_element))
            else:
                self.notImplemented("Unsupported assigned data type <%s>" % tag_name)

    def readSwcServiceDependencyAssignedData(self, element: ET.Element, dependency: SwcServiceDependency):
        for child_element in self.findall(element, "ASSIGNED-DATAS/*"):
            tag_name = self.getTagName(child_element)
            if (tag_name == "ROLE-BASED-DATA-ASSIGNMENT"):
                dependency.AddAssignedData(self.getRoleBasedDataAssignment(child_element))
            else:
                self.raiseError("Unsupported assigned data <%s>" % tag_name)

    def readSwcServiceDependencyAssignedPorts(self, element: ET.Element, dependency: SwcServiceDependency):
        for child_element in self.findall(element, "ASSIGNED-PORTS/*"):
            tag_name = self.getTagName(child_element)
            if (tag_name == "ROLE-BASED-PORT-ASSIGNMENT"):
                dependency.AddAssignedPort(self.getRoleBasedPortAssignment(child_element))
            else:
                self.raiseError("Unsupported assigned ports <%s>" % tag_name)

    def readServiceNeeds(self, element: ET.Element, needs: ServiceNeeds):
        self.readIdentifiable(element, needs)

    def readNvBlockNeeds(self, element: ET.Element, needs: NvBlockNeeds):
        # self.logger.debug("Read NvBlockNeeds <%s>" % needs.getShortName())
        self.readServiceNeeds(element, needs)
        needs.setCalcRamBlockCrc(self.getChildElementOptionalBooleanValue(element, "CALC-RAM-BLOCK-CRC")) \
             .setCheckStaticBlockId(self.getChildElementOptionalBooleanValue(element, "CHECK-STATIC-BLOCK-ID")) \
             .setNDataSets(self.getChildElementOptionalNumericalValue(element, "N-DATA-SETS")) \
             .setNRomBlocks(self.getChildElementOptionalNumericalValue(element, "N-ROM-BLOCKS")) \
             .setRamBlockStatusControl(self.getChildElementOptionalLiteral(element, "RAM-BLOCK-STATUS-CONTROL")) \
             .setReadonly(self.getChildElementOptionalBooleanValue(element, "READONLY")) \
             .setReliability(self.getChildElementOptionalLiteral(element, "RELIABILITY")) \
             .setResistantToChangedSw(self.getChildElementOptionalBooleanValue(element, "RESISTANT-TO-CHANGED-SW")) \
             .setRestoreAtStart(self.getChildElementOptionalBooleanValue(element, "RESTORE-AT-START")) \
             .setStoreAtShutdown(self.getChildElementOptionalBooleanValue(element, "STORE-AT-SHUTDOWN")) \
             .setStoreCyclic(self.getChildElementOptionalBooleanValue(element, "STORE-CYCLIC")) \
             .setStoreEmergency(self.getChildElementOptionalBooleanValue(element, "STORE-EMERGENCY")) \
             .setStoreImmediate(self.getChildElementOptionalBooleanValue(element, "STORE-IMMEDIATE")) \
             .setUseAutoValidationAtShutDown(self.getChildElementOptionalBooleanValue(element, "USE-AUTO-VALIDATION-AT-SHUT-DOWN")) \
             .setUseCRCCompMechanism(self.getChildElementOptionalBooleanValue(element, "USE-CRC-COMP-MECHANISM")) \
             .setWriteOnlyOnce(self.getChildElementOptionalBooleanValue(element, "WRITE-ONLY-ONCE")) \
             .setWriteVerification(self.getChildElementOptionalBooleanValue(element, "WRITE-VERIFICATION")) \
             .setWritingFrequency(self.getChildElementOptionalPositiveInteger(element, "WRITING-FREQUENCY")) \
             .setWritingPriority(self.getChildElementOptionalLiteral(element, "WRITING-PRIORITY"))
        
    def readDiagnosticCapabilityElement(self, element: ET.Element, needs: DiagnosticCapabilityElement):
        self.readServiceNeeds(element, needs)
        
    def readDiagnosticCommunicationManagerNeeds(self, element: ET.Element, needs: DiagnosticCommunicationManagerNeeds):
        # self.logger.debug("Read DiagnosticCommunicationManagerNeeds <%s>" % needs.getShortName())
        self.readDiagnosticCapabilityElement(element, needs)
        needs.setServiceRequestCallbackType(self.getChildElementOptionalLiteral(element, "SERVICE-REQUEST-CALLBACK-TYPE"))

    def readDiagnosticRoutineNeeds(self, element: ET.Element, needs: DiagnosticRoutineNeeds):
        # self.logger.debug("Read DiagnosticRoutineNeeds %s" % needs.getShortName())
        self.readDiagnosticCapabilityElement(element, needs)
        needs.setDiagRoutineType(self.getChildElementOptionalLiteral(element, "DIAG-ROUTINE-TYPE")) \
             .setRidNumber(self.getChildElementOptionalIntegerValue(element, "RID-NUMBER"))

    def readDiagnosticValueNeeds(self, element: ET.Element, needs: DiagnosticValueNeeds):
        # self.logger.debug("Read DiagnosticValueNeeds %s" % needs.getShortName())
        self.readDiagnosticCapabilityElement(element, needs)
        needs.setDataLength(self.getChildElementOptionalPositiveInteger(element, "DATA-LENGTH")) \
             .setDiagnosticValueAccess(self.getChildElementOptionalLiteral(element, "DIAGNOSTIC-VALUE-ACCESS")) \
             .setDidNumber(self.getChildElementOptionalIntegerValue(element, "DID-NUMBER")) \
             .setFixedLength(self.getChildElementOptionalBooleanValue(element, "FIXED-LENGTH")) \
             .setProcessingStyle(self.getChildElementOptionalLiteral(element, "PROCESSING-STYLE"))
        
    def readDiagEventDebounceMonitorInternal(self, element: ET.Element, algorithm: DiagEventDebounceMonitorInternal):
        self.readDiagnosticCapabilityElement(element, algorithm)
        
    def readDiagEventDebounceAlgorithm(self, element: ET.Element, needs: DiagnosticEventNeeds):
        for child_element in self.findall(element, "DIAG-EVENT-DEBOUNCE-ALGORITHM/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "DIAG-EVENT-DEBOUNCE-MONITOR-INTERNAL":
                algorithm = needs.createDiagEventDebounceMonitorInternal(self.getShortName(child_element))
                self.readDiagEventDebounceMonitorInternal(child_element, algorithm)
            else:
                self.notImplemented("Unsupported DiagEventDebounceAlgorithm <%s>" % tag_name)
    
    def readDiagnosticEventNeeds(self, element: ET.Element, needs: DiagnosticEventNeeds):
        # self.logger.debug("Read DiagnosticEventNeeds <%s>" % needs.getShortName())
        self.readDiagnosticCapabilityElement(element, needs)
        self.readDiagEventDebounceAlgorithm(element, needs)
        needs.setDtcKind(self.getChildElementOptionalLiteral(element, "DTC-KIND")) \
             .setUdsDtcNumber(self.getChildElementOptionalIntegerValue(element, "UDS-DTC-NUMBER"))
        
    def readDiagnosticEventInfoNeeds(self, element: ET.Element, needs: DiagnosticEventInfoNeeds):
        # self.logger.debug("Read DiagnosticEventInfoNeeds <%s>" % needs.getShortName())
        self.readDiagnosticCapabilityElement(element, needs)
        needs.setDtcKind(self.getChildElementOptionalLiteral(element, "DTC-KIND"))
        needs.setUdsDtcNumber(self.getChildElementOptionalPositiveInteger(element, "UDS-DTC-NUMBER"))

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
            else:
                self.notImplemented("Unsupported service needs <%s>" % tag_name)

    def readSwcServiceDependency(self, element: ET.Element, parent: SwcInternalBehavior):
        short_name = self.getShortName(element)
        dependency = parent.createSwcServiceDependency(short_name)
        # self.logger.debug("Read SwcServiceDependency %s" % short_name)
        self.readServiceDependency(element, dependency)
        self.readSwcServiceDependencyAssignedData(element, dependency)
        self.readSwcServiceDependencyAssignedPorts(element, dependency)
        self.readSwcServiceDependencyServiceNeeds(element, dependency)

    def readSwcInternalBehaviorServiceDependencies(self, element: ET.Element, parent: SwcInternalBehavior):
        for child_element in self.findall(element, "SERVICE-DEPENDENCYS/*"):
            tag_name = self.getTagName(child_element)
            if (tag_name == "SWC-SERVICE-DEPENDENCY"):
                self.readSwcServiceDependency(child_element, parent)
            else:
                self.notImplemented("Unsupported Service Dependencies <%s>" % tag_name)

    def getIncludedDataTypeSets(self, element: ET.Element) -> List[IncludedDataTypeSet]:
        include_data_type_sets = []
        for child_element in self.findall(element, "INCLUDED-DATA-TYPE-SETS/INCLUDED-DATA-TYPE-SET"):
            include_data_type_set = IncludedDataTypeSet()
            self.readARObjectAttributes(child_element, include_data_type_set)
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

    def readIncludedModeDeclarationGroupSet(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readIncludedModeDeclarationGroupSet(*args, **kwargs)


    def readSwcInternalBehaviorIncludedModeDeclarationGroupSets(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readSwcInternalBehaviorIncludedModeDeclarationGroupSets(*args, **kwargs)


    def readSwcInternalBehavior(self, element: ET.Element, behavior: SwcInternalBehavior):
        # read the internal behavior
        self.readInternalBehavior(element, behavior)
        
        # read the extra SwcInternalBehavior
        self.readSwcInternalBehaviorArTypedPerInstanceMemories(element, behavior)
        self.readSwcInternalBehaviorEvents(element, behavior)
        self.readSwcInternalBehaviorExplicitInterRunnableVariables(element, behavior)
        behavior.setHandleTerminationAndRestart(self.getChildElementOptionalLiteral(element, "HANDLE-TERMINATION-AND-RESTART"))
        self.readSwcInternalBehaviorIncludedModeDeclarationGroupSets(element, behavior)
        self.readSwcInternalBehaviorPerInstanceMemories(element, behavior)
        self.readSwcInternalBehaviorPerInstanceParameters(element, behavior)
        self.readSwcInternalBehaviorPortAPIOptions(element, behavior)
        self.readSwcInternalBehaviorRunnables(element, behavior)
        self.readSwcInternalBehaviorServiceDependencies(element, behavior)
        self.readSwcInternalBehaviorSharedParameters(element, behavior)
        behavior.setSupportsMultipleInstantiation(self.getChildElementOptionalBooleanValue(element, "SUPPORTS-MULTIPLE-INSTANTIATION"))

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
        for ref in self.getChildElementRefTypeList(element, "ACTIVATION-POINTS/BSW-INTERNAL-TRIGGERING-POINT-REF-CONDITIONAL/BSW-INTERNAL-TRIGGERING-POINT-REF"):   # noqa E501
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
        entity.setInterruptCategory(self.getChildElementOptionalLiteral(element, "INTERRUPT-CATEGORY")) \
              .setInterruptSource(self.getChildElementOptionalLiteral(element, "INTERRUPT-SOURCE"))
    
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
        entry.setEncapsulatedEntryRef(self.getChildElementOptionalRefType(element, "ENCAPSULATED-ENTRY-REF")) \
             .setIsReentrant(self.getChildElementOptionalBooleanValue(element, "IS-REENTRANT")) \
             .setIsSynchronous(self.getChildElementOptionalBooleanValue(element, "IS-SYNCHRONOUS"))

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
        self.readBswModuleDescriptionImplementedEntryRefs(element, desc)
        self.readBswModuleDescriptionProvidedModeGroups(element, desc)
        self.readBswModuleDescriptionRequiredModeGroups(element, desc)
        self.readBswModuleDescriptionProvidedClientServerEntries(element, desc)
        self.readBswModuleDescriptionRequiredClientServerEntries(element, desc)
        self.readBswModuleDescriptionProvidedDatas(element, desc)
        self.readBswModuleDescriptionRequiredDatas(element, desc)
        self.readBswModuleDescriptionBswInternalBehaviors(element, desc)
        self.readBswModuleDescriptionRequiredTriggers(element, desc)

    def readSwServiceArg(self, element: ET.Element, arg: SwServiceArg):
        self.readIdentifiable(element, arg)
        arg.setDirection(self.getChildElementOptionalLiteral(element, "DIRECTION")) \
           .setSwDataDefProps(self.getSwDataDefProps(element, "SW-DATA-DEF-PROPS"))

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
        self.readBswModuleEntryReturnType(element, entry)

    def readEngineeringObject(self, element: ET.Element, engineering_obj: EngineeringObject):
        self.readARObjectAttributes(element, engineering_obj)
        engineering_obj.setShortLabel(self.getChildElementOptionalLiteral(element, "SHORT-LABEL")) \
                       .setCategory(self.getChildElementOptionalLiteral(element, "CATEGORY"))
        
    def getAutosarEngineeringObject(self, element: ET.Element) -> AutosarEngineeringObject:
        obj = AutosarEngineeringObject()
        self.readEngineeringObject(element, obj)
        # self.logger.debug("Get AutosarEngineeringObject %s", obj.short_label)
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

    def readMemorySectionOptions(self, element: ET.Element, section: MemorySection):
        child_element = self.find(element, "OPTIONS")
        if child_element is not None:
            for value in self.getChildElementLiteralValueList(child_element, "OPTION"):
                section.addOption(value)

    def readMemorySections(self, element: ET.Element, consumption: ResourceConsumption):
        for child_element in self.findall(element, "MEMORY-SECTIONS/MEMORY-SECTION"):
            memory_section = consumption.createMemorySection(self.getShortName(child_element))
            self.readIdentifiable(child_element, memory_section)
            memory_section.setAlignment(self.getChildElementOptionalLiteral(child_element, "ALIGNMENT")) \
                          .setMemClassSymbol(self.getChildElementOptionalLiteral(child_element, "MEM-CLASS-SYMBOL"))
            self.readMemorySectionOptions(child_element, memory_section)
            memory_section.setSize(self.getChildElementOptionalNumericalValue(child_element, "SIZE")) \
                          .setSwAddrMethodRef(self.getChildElementOptionalRefType(child_element, "SW-ADDRMETHOD-REF")) \
                          .setSymbol(self.getChildElementOptionalLiteral(child_element, "SYMBOL"))
            # self.logger.debug("read MemorySections %s" % memory_section.getShortName())

    def readStackUsage(self, element: ET.Element, usage: StackUsage):
        self.logger.debug("read StackUsage %s" % usage.getShortName())
        self.readIdentifiable(element, usage)

    def readRoughEstimateStackUsage(self, element: ET.Element, usage: RoughEstimateStackUsage):
        self.readStackUsage(element, usage)
        usage.setMemoryConsumption(self.getChildElementOptionalPositiveInteger(element, "MEMORY-CONSUMPTION"))

    def readStackUsages(self, element: ET.Element, consumption: ResourceConsumption):
        for child_element in self.findall(element, "STACK-USAGES/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "ROUGH-ESTIMATE-STACK-USAGE":
                usage = consumption.createRoughEstimateStackUsage(self.getShortName(child_element))
                self.readRoughEstimateStackUsage(child_element, usage)
            else:
                self.notImplemented("Unsupported Stack Usages: <%s>" % tag_name)

    def readResourceConsumption(self, element: ET.Element, impl: Implementation):
        child_element = self.find(element, "RESOURCE-CONSUMPTION")
        if (child_element is not None):
            consumption = impl.createResourceConsumption(self.getShortName(child_element))
            self.readIdentifiable(child_element, consumption)
            self.readMemorySections(child_element, consumption)
            self.readStackUsages(child_element, consumption)

    def readImplementation(self, element: ET.Element, impl: Implementation):
        self.readIdentifiable(element, impl)
        self.readCodeDescriptor(element, impl)
        impl.setProgrammingLanguage(self.getChildElementOptionalLiteral(element, "PROGRAMMING-LANGUAGE"))
        self.readResourceConsumption(element, impl)
        impl.setSwVersion(self.getChildElementOptionalLiteral(element, "SW-VERSION")) \
            .setSwcBswMappingRef(self.getChildElementOptionalRefType(element, "SWC-BSW-MAPPING-REF")) \
            .setUsedCodeGenerator(self.getChildElementOptionalLiteral(element, "USED-CODE-GENERATOR")) \
            .setVendorId(self.getChildElementOptionalNumericalValue(element, "VENDOR-ID"))

    def readBswImplementationVendorSpecificModuleDefRefs(self, element: ET.Element, impl: BswImplementation):
        child_element = self.find(element, "VENDOR-SPECIFIC-MODULE-DEF-REFS")
        if child_element is not None:
            for ref in self.getChildElementRefTypeList(child_element, "VENDOR-SPECIFIC-MODULE-DEF-REF"):
                impl.addVendorSpecificModuleDefRef(ref)

    def readBswImplementation(self, element: ET.Element, impl: BswImplementation):
        self.logger.debug("Read BswImplementation <%s>" % impl.getShortName())
        self.readImplementation(element, impl)
        impl.setArReleaseVersion(self.getChildElementOptionalLiteral(element, "AR-RELEASE-VERSION")) \
            .setBehaviorRef(self.getChildElementOptionalRefType(element, "BEHAVIOR-REF")) \
            .setVendorApiInfix(self.getChildElementOptionalLiteral(element, "VENDOR-API-INFIX"))
        self.readBswImplementationVendorSpecificModuleDefRefs(element, impl)
        AUTOSAR.getInstance().addImplementationBehaviorMap(impl.getFullName(), impl.getBehaviorRef().getValue())

    def readSwcImplementation(self, element: ET.Element, impl: SwcImplementation):
        self.logger.debug("Read SwcImplementation <%s>" % impl.getShortName())
        self.readImplementation(element, impl)
        impl.setBehaviorRef(self.getChildElementOptionalRefType(element, "BEHAVIOR-REF"))
        AUTOSAR.getInstance().addImplementationBehaviorMap(impl.getFullName(), impl.getBehaviorRef().getValue())

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
            parameter_iref.setBaseRef(self.getChildElementOptionalRefType(child_element, "BASE-REF"))
            parameter_iref.setContextDataPrototypeRef(self.getChildElementOptionalRefType(child_element, "CONTEXT-DATA-PROTOTYPE-REF"))
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
        if (child_element is not None):
            operation_iref = ROperationInAtomicSwcInstanceRef()
            self.readARObjectAttributes(child_element, operation_iref)
            operation_iref.setContextRPortRef(self.getChildElementOptionalRefType(child_element, "CONTEXT-R-PORT-REF")) \
                          .setTargetRequiredOperationRef(self.getChildElementOptionalRefType(child_element, "TARGET-REQUIRED-OPERATION-REF"))
            parent.setOperationIRef(operation_iref)

    def readRVariableInAtomicSwcInstanceRef(self, element: ET.Element, parent: DataReceivedEvent):
        child_element = self.find(element, "DATA-IREF")
        if (child_element is not None):
            data_iref = RVariableInAtomicSwcInstanceRef()
            data_iref.setContextRPortRef(self.getChildElementOptionalRefType(child_element, "CONTEXT-R-PORT-REF")) \
                     .setTargetDataElementRef(self.getChildElementOptionalRefType(child_element, "TARGET-DATA-ELEMENT-REF"))
            parent.setDataIRef(data_iref)

    def readRModeInAtomicSwcInstanceRef(self, element: ET.Element, parent: SwcModeSwitchEvent):
        for child_element in self.findall(element, "MODE-IREFS/MODE-IREF"):
            mode_iref = RModeInAtomicSwcInstanceRef()
            mode_iref.setContextPortRef(self.getChildElementOptionalRefType(child_element, "CONTEXT-PORT-REF")) \
                     .setContextModeDeclarationGroupPrototypeRef(self.getChildElementOptionalRefType(child_element, "CONTEXT-MODE-DECLARATION-GROUP-PROTOTYPE-REF")) \
                     .setTargetModeDeclarationRef(self.getChildElementOptionalRefType(child_element, "TARGET-MODE-DECLARATION-REF"))            # NOQA E501
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

    def readModeGroupInAtomicSwcInstanceRef(self, element: ET.Element, instance_ref: ModeGroupInAtomicSwcInstanceRef):
        instance_ref.setBaseRef(self.getChildElementOptionalRefType(element, "BASE-REF")) \
                    .setContextPortRef(self.getChildElementOptionalRefType(element, "CONTEXT-PORT-REF"))

    def readRModeGroupInAtomicSWCInstanceRef(self, element: ET.Element, instance_ref: RModeGroupInAtomicSWCInstanceRef):
        self.readModeGroupInAtomicSwcInstanceRef(element, instance_ref)
        instance_ref.setContextRPortRef(self.getChildElementOptionalRefType(element, "CONTEXT-R-PORT-REF")) \
                    .setTargetModeGroupRef(self.getChildElementOptionalRefType(element, "TARGET-MODE-GROUP-REF"))

    def readPModeGroupInAtomicSWCInstanceRef(self, element: ET.Element, instance_ref: PModeGroupInAtomicSwcInstanceRef):
        self.readModeGroupInAtomicSwcInstanceRef(element, instance_ref)
        instance_ref.setContextPPortRef(self.getChildElementOptionalRefType(element, "CONTEXT-P-PORT-REF")) \
                    .setTargetModeGroupRef(self.getChildElementOptionalRefType(element, "TARGET-MODE-GROUP-REF"))

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

    def readModeAccessPoint(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readModeAccessPoint(*args, **kwargs)


    def readRunnableEntityModeAccessPoints(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readRunnableEntityModeAccessPoints(*args, **kwargs)


    def readModeSwitchPointModeGroupIRef(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readModeSwitchPointModeGroupIRef(*args, **kwargs)


    def readModeSwitchPoint(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readModeSwitchPoint(*args, **kwargs)


    def readRunnableEntityModeSwitchPoints(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readRunnableEntityModeSwitchPoints(*args, **kwargs)


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
        self.readRunnableEntityModeAccessPoints(element, entity)
        self.readRunnableEntityModeSwitchPoints(element, entity)
        self.readRunnableEntityParameterAccesses(element, entity)
        self.readRunnableEntityReadLocalVariables(element, entity)
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
        instance_ref.setBaseRef(self.getChildElementOptionalRefType(element, "BASE-REF")) \
            .setContextPortRef(self.getChildElementOptionalRefType(element, "CONTEXT-PORT-REF")) \
            .setContextModeDeclarationGroupPrototypeRef(self.getChildElementOptionalRefType(element, "CONTEXT-MODE-DECLARATION-GROUP-PROTOTYPE-REF")) \
            .setTargetModeDeclarationRef(self.getChildElementOptionalRefType(element, "TARGET-MODE-DECLARATION-REF"))       # NOQA E501
        return instance_ref

    def readRTEEvent(self, element: ET.Element, event: RTEEvent):
        self.readIdentifiable(element, event)
        event.startOnEventRef = self.getChildElementOptionalRefType(element, "START-ON-EVENT-REF")
        for child_element in self.findall(element, "DISABLED-MODE-IREFS/DISABLED-MODE-IREF"):
            iref = self.getRModeInAtomicSwcInstanceRef(child_element)
            event.addDisabledModeIRef(iref)

    def readPOperationIRef(self, element: ET.Element, key: str, parent: OperationInvokedEvent):
        child_element = self.find(element, key)
        if (child_element is not None):
            operation_iref = POperationInAtomicSwcInstanceRef()
            self.readARObjectAttributes(child_element, operation_iref)
            operation_iref.setContextPPortRef(self.getChildElementRefType(parent.getShortName(), child_element, "CONTEXT-P-PORT-REF")) \
                          .setTargetProvidedOperationRef(self.getChildElementRefType(parent.getShortName(), child_element, "TARGET-PROVIDED-OPERATION-REF"))    # NOQA E501
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
            memory.setInitValue(self.getChildElementOptionalLiteral(child_element, "INIT-VALUE")) \
                  .setSwDataDefProps(self.getSwDataDefProps(child_element, "SW-DATA-DEF-PROPS")) \
                  .setType(self.getChildElementOptionalLiteral(child_element, "TYPE")) \
                  .setTypeDefinition(self.getChildElementOptionalLiteral(child_element, "TYPE-DEFINITION"))

    def readAutosarDataPrototype(self, element: ET.Element, prototype: AutosarDataPrototype):
        self.readDataPrototype(element, prototype)
        prototype.setTypeTRef(self.getChildElementOptionalRefType(element, "TYPE-TREF"))

    def readParameterDataPrototype(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readParameterDataPrototype(*args, **kwargs)


    def readSwcInternalBehaviorPerInstanceParameters(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readSwcInternalBehaviorPerInstanceParameters(*args, **kwargs)


    def readPortDefinedArgumentValue(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readPortDefinedArgumentValue(*args, **kwargs)


    def readSwcInternalBehaviorPortAPIOptions(self, element: ET.Element, behavior: SwcInternalBehavior):
        for child_element in self.findall(element, "PORT-API-OPTIONS/PORT-API-OPTION"):
            option = PortAPIOption()
            option.setEnableTakeAddress(self.getChildElementOptionalBooleanValue(child_element, "ENABLE-TAKE-ADDRESS")) \
                  .setErrorHandling(self.getChildElementOptionalLiteral(child_element, "ERROR-HANDLING")) \
                  .setIndirectAPI(self.getChildElementOptionalBooleanValue(child_element, "INDIRECT-API")) \
                  .setPortRef(self.getChildElementOptionalRefType(child_element, "PORT-REF"))
            for argument_value_tag in self.findall(child_element, "PORT-ARG-VALUES/PORT-DEFINED-ARGUMENT-VALUE"):
                option.addPortArgValue(self.readPortDefinedArgumentValue(argument_value_tag))
            behavior.addPortAPIOption(option)
            
    def readTimingEvent(self, element: ET.Element, event: TimingEvent):
        # self.logger.debug("Read TimingEvent <%s>" % event.getShortName())
        self.readRTEEvent(element, event)
        event.setOffset(self.getChildElementOptionalTimeValue(element, "OFFSET")) \
             .setPeriod(self.getChildElementOptionalTimeValue(element, "PERIOD"))

    def readDataReceivedEvent(self, element: ET.Element, event: DataReceivedEvent):
        # self.logger.debug("Read DataReceivedEvent <%s>" % event.getShortName())
        self.readRTEEvent(element, event)
        self.readRVariableInAtomicSwcInstanceRef(element, event)

    def readSwcModeSwitchEvent(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readSwcModeSwitchEvent(*args, **kwargs)


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
        event.setActivationReasonRepresentationRef(self.getChildElementOptionalRefType(element, "EVENT-SOURCE-REF"))

    def readModeSwitchedAckEvent(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readModeSwitchedAckEvent(*args, **kwargs)


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
            props.setTargetCategory(self.getChildElementOptionalLiteral(child_element, "TARGET-CATEGORY")) \
                 .setSwDataDefProps(self.getSwDataDefProps(child_element, "SW-DATA-DEF-PROPS"))
        return props

    def readSwPointerTargetProps(self, element: ET.Element, parent: SwDataDefProps):
        child_element = self.find(element, "SW-POINTER-TARGET-PROPS")
        if child_element is not None:
            sw_pointer_target_props = SwPointerTargetProps()
            sw_pointer_target_props.setTargetCategory(self.getChildElementOptionalLiteral(child_element, "TARGET-CATEGORY")) \
                                   .setSwDataDefProps(self.getSwDataDefProps(child_element, "SW-DATA-DEF-PROPS"))
            parent.swPointerTargetProps = sw_pointer_target_props

    def readLanguageSpecific(self, element: ET.Element, specific: LanguageSpecific):
        """Delegate to CommonStructureParser."""
        return self._common_parser.readLanguageSpecific(element, specific)

    def getLParagraphs(self, element: ET.Element, key: str) -> List[LParagraph]:
        """Delegate to CommonStructureParser."""
        return self._common_parser.getLParagraphs(element, key)

    def getMultiLanguageParagraphs(self, element: ET.Element, key: str) -> List[MultiLanguageParagraph]:
        """Delegate to CommonStructureParser."""
        return self._common_parser.getMultiLanguageParagraphs(element, key)

    def getLPlainTexts(self, element: ET.Element, key: str) -> List[LParagraph]:
        """Delegate to CommonStructureParser."""
        return self._common_parser.getLPlainTexts(element, key)

    def getListElements(self, element: ET.Element, key: str) -> List[ARList]:
        """Delegate to CommonStructureParser."""
        return self._common_parser.getListElements(element, key)

    def getGraphic(self, element: ET.Element, key: str) -> Graphic:
        """Delegate to CommonStructureParser."""
        return self._common_parser.getGraphic(element, key)

    def readMlFigureLGraphics(self, element: ET.Element, figure: MlFigure):
        """Delegate to CommonStructureParser."""
        return self._common_parser.readMlFigureLGraphics(element, figure)

    def readDocumentViewSelectable(self, element: ET.Element, selectable: DocumentViewSelectable):
        """Delegate to CommonStructureParser."""
        return self._common_parser.readDocumentViewSelectable(
            element, selectable
        )

    def readPaginateable(self, element: ET.Element, paginateable: Paginateable):
        """Delegate to CommonStructureParser."""
        return self._common_parser.readPaginateable(element, paginateable)

    def readMlFigure(self, element: ET.Element, figure: MlFigure):
        """Delegate to CommonStructureParser."""
        return self._common_parser.readMlFigure(element, figure)

    def getMlFigures(self, element: ET.Element, key: str) -> List[MlFigure]:
        """Delegate to CommonStructureParser."""
        return self._common_parser.getMlFigures(element, key)

    def getMultiLanguagePlainText(self, element: ET.Element, key: str) -> MultiLanguagePlainText:
        """Delegate to CommonStructureParser."""
        return self._common_parser.getMultiLanguagePlainText(element, key)

    def readDocumentationBlock(self, element: ET.Element, block: DocumentationBlock):
        """Delegate to CommonStructureParser."""
        return self._common_parser.readDocumentationBlock(element, block)

    def getDocumentationBlock(self, element: ET.Element, key: str) -> DocumentationBlock:
        """Delegate to CommonStructureParser."""
        return self._common_parser.getDocumentationBlock(element, key)

    def getDocumentationBlockList(self, element: ET.Element, key: str) -> List[DocumentationBlock]:
        """Delegate to CommonStructureParser."""
        return self._common_parser.getDocumentationBlockList(element, key)

    def readGeneralAnnotation(self, element: ET.Element, annotation: GeneralAnnotation):
        """Delegate to CommonStructureParser."""
        return self._common_parser.readGeneralAnnotation(element, annotation)

    def getAnnotations(self, element: ET.Element) -> List[Annotation]:
        """Delegate to CommonStructureParser."""
        return self._common_parser.getAnnotations(element)

    def getSwAxisIndividual(self, element: ET.Element) -> SwAxisIndividual:
        props = SwAxisIndividual()
        self.readARObjectAttributes(element, props)
        props.setInputVariableTypeRef(self.getChildElementOptionalRefType(element, "INPUT-VARIABLE-TYPE-REF")) \
             .setCompuMethodRef(self.getChildElementOptionalRefType(element, "COMPU-METHOD-REF")) \
             .setSwMaxAxisPoints(self.getChildElementOptionalNumericalValue(element, "SW-MAX-AXIS-POINTS")) \
             .setSwMinAxisPoints(self.getChildElementOptionalNumericalValue(element, "SW-MIN-AXIS-POINTS")) \
             .setDataConstrRef(self.getChildElementOptionalRefType(element, "DATA-CONSTR-REF"))
        return props
    
    def getSwAxisGrouped(self, element: ET.Element) -> SwAxisGrouped:
        props = SwAxisGrouped()
        props.setSharedAxisTypeRef(self.getChildElementOptionalRefType(element, "SHARED-AXIS-TYPE-REF"))
        return props

    def getSwCalprmAxis(self, element: ET.Element) -> SwCalprmAxis:
        axis = SwCalprmAxis()
        axis.sw_axis_index = self.getChildElementOptionalNumericalValue(element, "SW-AXIS-INDEX")
        axis.category = self.getChildElementOptionalLiteral(element, "CATEGORY")
        child_element = self.find(element, "SW-AXIS-INDIVIDUAL")
        if child_element is not None:
            axis.sw_calprm_axis_type_props = self.getSwAxisIndividual(child_element)
        child_element = self.find(element, "SW-AXIS-GROUPED")
        if child_element is not None:
            axis.sw_calprm_axis_type_props = self.getSwAxisGrouped(child_element)
        
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

                sw_data_def_props.setBaseTypeRef(self.getChildElementOptionalRefType(conditional_tag, "BASE-TYPE-REF")) \
                                 .setDataConstrRef(self.getChildElementOptionalRefType(conditional_tag, "DATA-CONSTR-REF")) \
                                 .setCompuMethodRef(self.getChildElementOptionalRefType(conditional_tag, "COMPU-METHOD-REF")) \
                                 .setSwAddrMethodRef(self.getChildElementOptionalRefType(conditional_tag, "SW-ADDR-METHOD-REF")) \
                                 .setSwImplPolicy(self.getChildElementOptionalLiteral(conditional_tag, "SW-IMPL-POLICY")) \
                                 .setSwIntendedResolution(self.getChildElementOptionalNumericalValue(conditional_tag, "SW-INTENDED-RESOLUTION")) \
                                 .setImplementationDataTypeRef(self.getChildElementOptionalRefType(conditional_tag, "IMPLEMENTATION-DATA-TYPE-REF")) \
                                 .setStepSize(self.getChildElementOptionalFloatValue(conditional_tag, "STEP-SIZE")) \
                                 .setSwCalibrationAccess(self.getChildElementOptionalLiteral(conditional_tag, "SW-CALIBRATION-ACCESS")) \
                                 .setSwCalprmAxisSet(self.getSwCalprmAxisSet(conditional_tag, "SW-CALPRM-AXIS-SET")) \
                                 .setSwPointerTargetProps(self.getSwPointerTargetProps(conditional_tag, "SW-POINTER-TARGET-PROPS")) \
                                 .setSwRecordLayoutRef(self.getChildElementOptionalRefType(conditional_tag, "SW-RECORD-LAYOUT-REF")) \
                                 .setValueAxisDataTypeRef(self.getChildElementOptionalRefType(conditional_tag, "VALUE-AXIS-DATA-TYPE-REF")) \
                                 .setUnitRef(self.getChildElementOptionalRefType(conditional_tag, "UNIT-REF"))
                self.readSwDataDefProsInvalidValue(conditional_tag, sw_data_def_props)
                # self.readSwPointerTargetProps(conditional_tag, sw_data_def_props)
                self.readARObjectAttributes(conditional_tag, sw_data_def_props.conditional)
        return sw_data_def_props

    def readAutosarDataType(self, element: ET.Element, data_type: AutosarDataType):
        """Delegate to DataTypeParser."""
        return self._datatype_parser.readAutosarDataType(element, data_type)

    def readApplicationPrimitiveDataType(self, element: ET.Element, data_type: ApplicationPrimitiveDataType):
        """Delegate to DataTypeParser."""
        return self._datatype_parser.readApplicationPrimitiveDataType(
            element, data_type
        )

    def readApplicationRecordElement(self, element: ET.Element, record_element: ApplicationRecordElement):
        """Delegate to DataTypeParser."""
        return self._datatype_parser.readApplicationRecordElement(
            element, record_element
        )

    def readApplicationRecordDataTypeElements(self, element: ET.Element, parent: ApplicationRecordDataType):
        """Delegate to DataTypeParser."""
        return self._datatype_parser.readApplicationRecordDataTypeElements(
            element, parent
        )

    def readApplicationRecordDataType(self, element: ET.Element, data_type: ApplicationRecordDataType):
        """Delegate to DataTypeParser."""
        return self._datatype_parser.readApplicationRecordDataType(
            element, data_type
        )

    def readImplementationDataTypeElement(self, element: ET.Element, impl_data_type_element: ImplementationDataTypeElement):
        """Delegate to DataTypeParser."""
        return self._datatype_parser.readImplementationDataTypeElement(
            element, impl_data_type_element
        )

    def readImplementationDataTypeSubElements(self, element: ET.Element, parent: ImplementationDataType):
        """Delegate to DataTypeParser."""
        return self._datatype_parser.readImplementationDataTypeSubElements(
            element, parent
        )

    def readImplementationDataType(self, element: ET.Element, data_type: ImplementationDataType):
        """Delegate to DataTypeParser."""
        return self._datatype_parser.readImplementationDataType(
            element, data_type
        )

    def readBaseTypeDirectDefinition(self, element: ET.Element, definition: BaseTypeDirectDefinition):
        definition.setBaseTypeSize(self.getChildElementOptionalNumericalValue(element, "BASE-TYPE-SIZE")) \
                  .setBaseTypeEncoding(self.getChildElementOptionalLiteral(element, "BASE-TYPE-ENCODING")) \
                  .setByteOrder(self.getChildElementOptionalLiteral(element, "BYTE-ORDER")) \
                  .setMemAlignment(self.getChildElementOptionalNumericalValue(element, "MEM-ALIGNMENT")) \
                  .setNativeDeclaration(self.getChildElementOptionalLiteral(element, "NATIVE-DECLARATION"))

    def readSwBaseType(self, element: ET.Element, data_type: SwBaseType):
        self.logger.debug("Read SwBaseType <%s>" % data_type.getShortName())
        self.readIdentifiable(element, data_type)
        self.readBaseTypeDirectDefinition(element, data_type.getBaseTypeDefinition())

    def getApplicationCompositeElementInPortInterfaceInstanceRef(self, element: ET.Element, key: str) \
            -> ApplicationCompositeElementInPortInterfaceInstanceRef:
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
        representation.setLeafElementIRef(self.getApplicationCompositeElementInPortInterfaceInstanceRef(element, "LEAF-ELEMENT-IREF")) \
                      .setNetworkRepresentation(self.getSwDataDefProps(element, "NETWORK-REPRESENTATION"))
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
            cont.setUnitRef(self.getChildElementOptionalRefType(child_element, "UNIT-REF")) \
                .setSwArraysize(self.getValueList(child_element, "SW-ARRAYSIZE")) \
                .setSwValuesPhys(self.getSwValues(child_element, "SW-VALUES-PHYS"))
        return cont
    
    def readApplicationValueSpecification(self, element: ET.Element, value_spec: ApplicationValueSpecification):
        self.readValueSpecification(element, value_spec)
        value_spec.setCategory(self.getChildElementOptionalLiteral(element, "CATEGORY")) \
                  .setSwValueCont(self.getSwValueCont(element))

        self.logger.debug("readApplicationValueSpecification Category %s" % value_spec.category)

    def getChildValueSpecification(self, element: ET.Element, key: str) -> ValueSpecification:
        value_spec = None
        child_element = self.find(element, key + "/*")
        if child_element is not None:
            value_spec = self.getValueSpecification(child_element, self.getTagName(child_element))
        return value_spec

    def getInitValue(self, element: ET.Element) -> ValueSpecification:
        return self.getChildValueSpecification(element, "INIT-VALUE")

    def readRPortComSpec(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readRPortComSpec(*args, **kwargs)


    def getClientComSpec(self, element: ET.Element) -> ClientComSpec:
        com_spec = ClientComSpec()
        self.readRPortComSpec(element, com_spec)
        com_spec.operationRef = self.getChildElementOptionalRefType(element, "OPERATION-REF")
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
        com_spec.setEnableUpdated(self.getChildElementOptionalBooleanValue(element, "ENABLE-UPDATE"))
        com_spec.setHandleNeverReceived(self.getChildElementOptionalBooleanValue(element, "HANDLE-NEVER-RECEIVED"))
        com_spec.setFilter(self.getDataFilter(element, "FILTER"))
        com_spec.setHandleTimeoutType(self.getChildElementOptionalLiteral(element, "HANDLE-TIMEOUT-TYPE"))
        com_spec.setInitValue(self.getInitValue(element))
        return com_spec

    def readRequiredComSpec(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readRequiredComSpec(*args, **kwargs)


    def readAbstractRequiredPortPrototype(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readAbstractRequiredPortPrototype(*args, **kwargs)


    def readPPortPrototype(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readPPortPrototype(*args, **kwargs)


    def readAbstractProvidedPortPrototype(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readAbstractProvidedPortPrototype(*args, **kwargs)


    def readRPortPrototype(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readRPortPrototype(*args, **kwargs)


    def readPRPortPrototype(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readPRPortPrototype(*args, **kwargs)


    def readSwComponentTypePorts(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readSwComponentTypePorts(*args, **kwargs)


    def readTransmissionAcknowledgementRequest(self, element: ET.Element) -> TransmissionAcknowledgementRequest:
        child_element = self.find(element, "TRANSMISSION-ACKNOWLEDGE")
        if (child_element is not None):
            acknowledge = TransmissionAcknowledgementRequest()
            self.readARObjectAttributes(child_element, acknowledge)
            acknowledge.timeout = self.getChildElementOptionalFloatValue(child_element, "TIMEOUT")
            return acknowledge
        return None

    def readSenderComSpec(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readSenderComSpec(*args, **kwargs)


    def getNonqueuedSenderComSpec(self, element: ET.Element) -> NonqueuedSenderComSpec:
        com_spec = NonqueuedSenderComSpec()
        self.readSenderComSpec(element, com_spec)
        com_spec.setInitValue(self.getInitValue(element))
        return com_spec

    def readTransformationComSpecProps(self, element: ET.Element, props: TransformationComSpecProps):
        self.readARObjectAttributes(element, props)

    def readUserDefinedTransformationComSpecProps(self, element: ET.Element, props: UserDefinedTransformationComSpecProps):
        self.readTransformationComSpecProps(element, props)

    def readServerComSpecTransformationComSpecProps(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readServerComSpecTransformationComSpecProps(*args, **kwargs)


    def readPPortComSpec(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readPPortComSpec(*args, **kwargs)


    def getServerComSpec(self, element: ET.Element) -> ServerComSpec:
        com_spec = ServerComSpec()
        self.readPPortComSpec(element, com_spec)
        com_spec.setOperationRef(self.getChildElementOptionalRefType(element, "OPERATION-REF"))
        com_spec.setQueueLength(self.getChildElementOptionalNumericalValue(element, "QUEUE-LENGTH"))
        self.readServerComSpecTransformationComSpecProps(element, com_spec)
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

    def readProvidedComSpec(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readProvidedComSpec(*args, **kwargs)


    def readPortGroupInnerGroupIRefs(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readPortGroupInnerGroupIRefs(*args, **kwargs)


    def readPortGroupOuterPortRefs(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readPortGroupOuterPortRefs(*args, **kwargs)


    def readPortGroup(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readPortGroup(*args, **kwargs)


    def readSwComponentTypePortGroups(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readSwComponentTypePortGroups(*args, **kwargs)


    def readSwComponentType(self, element: ET.Element, parent: SwComponentType):
        self.readIdentifiable(element, parent)
        self.readSwComponentTypePorts(element, parent)
        self.readSwComponentTypePortGroups(element, parent)

    def readAtomicSwComponentType(self, element, parent: AtomicSwComponentType):
        self.readSwComponentType(element, parent)
        self.readAtomicSwComponentTypeSwcInternalBehavior(element, parent)

    def readEcuAbstractionSwComponentType(self, element, sw_component: EcuAbstractionSwComponentType):
        self.logger.debug("Read EcuAbstractionSwComponentType <%s>" % sw_component.getShortName())
        self.readAtomicSwComponentType(element, sw_component)

    def readApplicationSwComponentType(self, element: ET.Element, sw_component: ApplicationSwComponentType):
        self.logger.debug("Read ApplicationSwComponentType <%s>" % sw_component.getShortName())
        self.readAtomicSwComponentType(element, sw_component)

    def readComplexDeviceDriverSwComponentType(self, element: ET.Element, type: ComplexDeviceDriverSwComponentType):
        self.logger.debug("Read ComplexDeviceDriverSwComponentType <%s>" % type.getShortName())
        self.readAtomicSwComponentType(element, type)

    def readSensorActuatorSwComponentType(self, element: ET.Element, sw_component: SensorActuatorSwComponentType):
        self.logger.debug("Read SensorActuatorSwComponentType <%s>" % sw_component.getShortName())
        self.readAtomicSwComponentType(element, sw_component)

    def readServiceSwComponentType(self, element: ET.Element, sw_component: ServiceSwComponentType):
        self.logger.debug("Read ServiceSwComponentType <%s>" % sw_component.getShortName())
        self.readAtomicSwComponentType(element, sw_component)

    def readPPortInCompositionInstanceRef(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readPPortInCompositionInstanceRef(*args, **kwargs)


    def readRPortInCompositionInstanceRef(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readRPortInCompositionInstanceRef(*args, **kwargs)


    def readAssemblySwConnectorProviderIRef(self, element: ET.Element, parent: AssemblySwConnector):
        child_element = self.find(element, "PROVIDER-IREF")
        if (child_element is not None):
            provide_iref = PPortInCompositionInstanceRef()
            self.readARObjectAttributes(child_element, provide_iref)
            self.readPPortInCompositionInstanceRef(child_element, provide_iref)
            parent.setProviderIRef(provide_iref)

    def readAssemblySwConnectorRequesterIRef(self, element: ET.Element, parent: AssemblySwConnector):
        child_element = self.find(element, "REQUESTER-IREF")
        if (child_element is not None):
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
            else:
                self.notImplemented("Unsupported SwConnector <%s>" % tag_name)

    def readDelegationSwConnectorInnerPortIRef(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readDelegationSwConnectorInnerPortIRef(*args, **kwargs)


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
        """Delegate to DataTypeParser."""
        return self._datatype_parser.readCompositionSwComponentTypeDataTypeMappingSet(
            element, parent
        )

    def readCompositionSwComponentType(self, element: ET.Element, type: CompositionSwComponentType):
        self.logger.debug("Read CompositionSwComponentType: <%s>" % type.getShortName())
        self.readSwComponentType(element, type)
        self.readCompositionSwComponentTypeComponents(element, type)
        self.readCompositionSwComponentTypeSwConnectors(element, type)
        self.readCompositionSwComponentTypeDataTypeMappingSet(element, type)
        AUTOSAR.getInstance().addCompositionSwComponentType(type)

    def readDataTypeMaps(self, element: ET.Element, parent: DataTypeMappingSet):
        """Delegate to DataTypeParser."""
        return self._datatype_parser.readDataTypeMaps(element, parent)

    def readModeRequestTypeMaps(self, element: ET.Element, parent: DataTypeMappingSet):
        """Delegate to DataTypeParser."""
        return self._datatype_parser.readModeRequestTypeMaps(element, parent)

    def readDataTypeMappingSet(self, element: ET.Element, mapping_set: DataTypeMappingSet):
        """Delegate to DataTypeParser."""
        return self._datatype_parser.readDataTypeMappingSet(element, mapping_set)

    def readSenderReceiverInterfaceDataElements(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readSenderReceiverInterfaceDataElements(*args, **kwargs)


    def readSenderReceiverInterfaceInvalidationPolicies(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readSenderReceiverInterfaceInvalidationPolicies(*args, **kwargs)


    def readInvalidationPolicys(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readInvalidationPolicys(*args, **kwargs)


    def readSenderReceiverInterface(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readSenderReceiverInterface(*args, **kwargs)


    def readArgumentDataPrototype(self, element: ET.Element, prototype: ArgumentDataPrototype):
        self.readAutosarDataPrototype(element, prototype)
        prototype.setDirection(self.getChildElementOptionalLiteral(element, "DIRECTION")) \
                 .setServerArgumentImplPolicy(self.getChildElementOptionalLiteral(element, "SERVER-ARGUMENT-IMPL-POLICY"))

    def readClientServerOperationArguments(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readClientServerOperationArguments(*args, **kwargs)


    def readPossibleErrorRefs(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readPossibleErrorRefs(*args, **kwargs)


    def readClientServerOperation(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readClientServerOperation(*args, **kwargs)


    def readClientServerInterfaceOperations(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readClientServerInterfaceOperations(*args, **kwargs)


    def readPossibleErrors(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readPossibleErrors(*args, **kwargs)


    def readPortInterface(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readPortInterface(*args, **kwargs)


    def readParameterInterfaceParameters(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readParameterInterfaceParameters(*args, **kwargs)


    def readDataInterface(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readDataInterface(*args, **kwargs)


    def readParameterInterface(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readParameterInterface(*args, **kwargs)


    def readClientServerInterface(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readClientServerInterface(*args, **kwargs)


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
        if (child_element is not None):
            compu_const = CompuConst()
            self.readARObjectAttributes(child_element, compu_const)
            compu_const.setCompuConstContentType(self.getCompuConstContent(child_element))
        return compu_const

    def readCompuConst(self, element: ET.Element, parent: CompuScale):
        """Delegate to DataTypeParser."""
        return self._datatype_parser.readCompuConst(element, parent)

    def readCompuNominatorDenominator(self, element: ET.Element, key: str, parent: CompuNominatorDenominator):
        """Delegate to DataTypeParser."""
        return self._datatype_parser.readCompuNominatorDenominator(
            element, key, parent
        )

    def readCompuRationCoeffs(self, element: ET.Element, parent: CompuScale):
        """Delegate to DataTypeParser."""
        return self._datatype_parser.readCompuRationCoeffs(element, parent)

    def readCompuScaleContents(self, element: ET.Element, parent: CompuScale):
        """Delegate to DataTypeParser."""
        return self._datatype_parser.readCompuScaleContents(element, parent)

    def readCompuScale(self, element: ET.Element, compu_scale: CompuScale):
        """Delegate to DataTypeParser."""
        return self._datatype_parser.readCompuScale(element, compu_scale)

    def getCompuScales(self, element: ET.Element) -> CompuScales:
        compu_scales = None
        compu_scales_tag = self.find(element, "COMPU-SCALES")
        if compu_scales_tag is not None:
            compu_scales = CompuScales()
            for child_element in self.findall(compu_scales_tag, 'COMPU-SCALE'):
                compu_scale = CompuScale()
                self.readCompuScale(child_element, compu_scale)
                compu_scales.addCompuScale(compu_scale)
        return compu_scales
    
    def getCompu(self, element: ET.Element, key: str) -> Compu:
        child_element = self.find(element, key)
        compu = None
        if (child_element is not None):
            compu = Compu()
            self.readARObjectAttributes(child_element, compu)
            compu.setCompuContent(self.getCompuScales(child_element))
            compu.setCompuDefaultValue(self.getCompuConst(child_element, "COMPU-DEFAULT-VALUE"))
        return compu

    def readCompuMethod(self, element: ET.Element, compu_method: CompuMethod):
        """Delegate to DataTypeParser."""
        return self._datatype_parser.readCompuMethod(element, compu_method)

    def readSwcBswMappingSwcBswRunnableMappings(self, element: ET.Element, parent: SwcBswMapping):
        for child_element in self.findall(element, "RUNNABLE-MAPPINGS/SWC-BSW-RUNNABLE-MAPPING"):
            mapping = SwcBswRunnableMapping()
            mapping.setBswEntityRef(self.getChildElementOptionalRefType(child_element, "BSW-ENTITY-REF")) \
                   .setSwcRunnableRef(self.getChildElementOptionalRefType(child_element, "SWC-RUNNABLE-REF"))
            parent.addRunnableMapping(mapping)

    def readSwcBswMapping(self, element: ET.Element, mapping: SwcBswMapping):
        self.logger.debug("Read SwcBswMapping <%s>" % mapping.getShortName())
        self.readIdentifiable(element, mapping)
        mapping.setBswBehaviorRef(self.getChildElementOptionalRefType(element, "BSW-BEHAVIOR-REF"))
        self.readSwcBswMappingSwcBswRunnableMappings(element, mapping)
        mapping.setSwcBehaviorRef(self.getChildElementOptionalRefType(element, "SWC-BEHAVIOR-REF"))

    def readValueSpecification(self, element: ET.Element, value_spec: ValueSpecification):
        self.readARObjectAttributes(element, value_spec)
        value_spec.setShortLabel(self.getChildElementOptionalLiteral(element, "SHORT-LABEL"))
        # self.logger.debug("read ValueSpecification")

    def getApplicationValueSpecification(self, element: ET.Element) -> ApplicationValueSpecification:
        value_spec = ApplicationValueSpecification()
        self.readValueSpecification(element, value_spec)
        value_spec.setCategory(self.getChildElementOptionalLiteral(element, "CATEGORY")) \
                  .setShortLabel(self.getChildElementOptionalLiteral(element, "SHORT-LABEL")) \
                  .setSwValueCont(self.getSwValueCont(element))
        return value_spec
    
    def getNumericalValueSpecification(self, element: ET.Element) -> NumericalValueSpecification:
        value_spec = NumericalValueSpecification()
        self.readValueSpecification(element, value_spec)
        value_spec.setShortLabel(self.getChildElementOptionalLiteral(element, "SHORT-LABEL")) \
                  .setValue(self.getChildElementOptionalNumericalValue(element, "VALUE"))
        return value_spec
    
    def getTextValueSpecification(self, element: ET.Element) -> TextValueSpecification:
        # self.logger.debug("Get TextValueSpecification")
        value_spec = TextValueSpecification()
        self.readValueSpecification(element, value_spec)
        value_spec.setShortLabel(self.getChildElementOptionalLiteral(element, "SHORT-LABEL")) \
                  .setValue(self.getChildElementOptionalLiteral(element, "VALUE"))
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
        """Delegate to DataTypeParser."""
        return self._datatype_parser.readInternalConstrs(element, parent)

    def readPhysConstrs(self, element: ET.Element, parent: DataConstrRule):
        """Delegate to DataTypeParser."""
        return self._datatype_parser.readPhysConstrs(element, parent)

    def readDataConstrRule(self, element: ET.Element, parent: DataConstr):
        """Delegate to DataTypeParser."""
        return self._datatype_parser.readDataConstrRule(element, parent)

    def readDataConstr(self, element: ET.Element, constr: DataConstr):
        """Delegate to DataTypeParser."""
        return self._datatype_parser.readDataConstr(element, constr)

    def readUnit(self, element: ET.Element, unit: Unit):
        """Delegate to DataTypeParser."""
        return self._datatype_parser.readUnit(element, unit)

    def readEndToEndDescriptionDataIds(self, element: ET.Element, parent: EndToEndDescription):
        child_element = self.find(element, "DATA-IDS")
        if child_element is not None:
            for value in self.getChildElementNumericalValueList(child_element, "DATA-ID"):
                parent.addDataId(value)

    def getEndToEndDescription(self, element: ET.Element, key: str) -> EndToEndDescription:
        child_element = self.find(element, key)
        desc = None
        if (child_element is not None):
            desc = EndToEndDescription()
            self.readARObjectAttributes(child_element, desc)
            desc.setCategory(self.getChildElementOptionalLiteral(child_element, "CATEGORY"))
            self.readEndToEndDescriptionDataIds(child_element, desc)
            desc.setDataIdMode(self.getChildElementOptionalPositiveInteger(child_element, "DATA-ID-MODE")) \
                .setDataLength(self.getChildElementOptionalPositiveInteger(child_element, "DATA-LENGTH")) \
                .setMaxDeltaCounterInit(self.getChildElementOptionalPositiveInteger(child_element, "MAX-DELTA-COUNTER-INIT")) \
                .setCrcOffset(self.getChildElementOptionalPositiveInteger(child_element, "CRC-OFFSET")) \
                .setCounterOffset(self.getChildElementOptionalPositiveInteger(child_element, "COUNTER-OFFSET"))
        return desc
    
    def getVariableDataPrototypeInSystemInstanceRef(self, element: ET.Element) -> VariableDataPrototypeInSystemInstanceRef:
        instance_ref = None
        if element is not None:
            instance_ref = VariableDataPrototypeInSystemInstanceRef()
            for ref in self.getChildElementRefTypeList(element, "CONTEXT-COMPONENT-REF"):
                instance_ref.addContextComponentRef(ref)
            instance_ref.setContextCompositionRef(self.getChildElementOptionalRefType(element, "CONTEXT-COMPOSITION-REF")) \
                        .setContextPortRef(self.getChildElementOptionalRefType(element, "CONTEXT-PORT-REF")) \
                        .setTargetDataPrototypeRef(self.getChildElementOptionalRefType(element, "TARGET-DATA-PROTOTYPE-REF"))
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
        ipdu.setDataOffset(self.getChildElementOptionalIntegerValue(element, "DATA-OFFSET")) \
            .setISignalGroupRef(self.getChildElementOptionalRefType(element, "I-SIGNAL-GROUP-REF")) \
            .setISignalIPduRef(self.getChildElementOptionalRefType(element, "I-SIGNAL-I-PDU-REF"))

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
        """Delegate to DataTypeParser."""
        return self._datatype_parser.readImplementationProps(element, props)

    def readSymbolProps(self, element: ET.Element, props: SymbolProps):
        """Delegate to DataTypeParser."""
        return self._datatype_parser.readSymbolProps(element, props)

    def readImplementationDataTypeSymbolProps(self, element: ET.Element, data_type: ImplementationDataType):
        """Delegate to DataTypeParser."""
        return self._datatype_parser.readImplementationDataTypeSymbolProps(
            element, data_type
        )

    def readApplicationDataType(self, element: ET.Element, data_type: ApplicationDataType):
        """Delegate to DataTypeParser."""
        return self._datatype_parser.readApplicationDataType(element, data_type)

    def readApplicationCompositeDataType(self, element: ET.Element, data_type: ApplicationCompositeDataType):
        """Delegate to DataTypeParser."""
        return self._datatype_parser.readApplicationCompositeDataType(
            element, data_type
        )

    def readDataPrototype(self, element: ET.Element, prototype: DataPrototype):
        """Delegate to DataTypeParser."""
        return self._datatype_parser.readDataPrototype(element, prototype)

    def readApplicationCompositeElementDataPrototype(self, element: ET.Element, prototype: ApplicationCompositeElementDataPrototype):
        """Delegate to DataTypeParser."""
        return self._datatype_parser.readApplicationCompositeElementDataPrototype(
            element, prototype
        )

    def readApplicationArrayElement(self, element: ET.Element, parent: ApplicationArrayDataType):
        """Delegate to DataTypeParser."""
        return self._datatype_parser.readApplicationArrayElement(element, parent)

    def readApplicationArrayDataType(self, element: ET.Element, data_type: ApplicationArrayDataType):
        """Delegate to DataTypeParser."""
        return self._datatype_parser.readApplicationArrayDataType(element, data_type)

    def getSwRecordLayoutV(self, element: ET.Element, key: str) -> SwRecordLayoutV:
        child_element = self.find(element, key)
        layout_v = None
        if child_element is not None:
            layout_v = SwRecordLayoutV()
            layout_v.setShortLabel(self.getChildElementOptionalLiteral(child_element, "SHORT-LABEL")) \
                    .setBaseTypeRef(self.getChildElementOptionalRefType(child_element, "BASE-TYPE-REF")) \
                    .setSwRecordLayoutVAxis(self.getChildElementOptionalLiteral(child_element, "SW-RECORD-LAYOUT-V-AXIS")) \
                    .setSwRecordLayoutVProp(self.getChildElementOptionalLiteral(child_element, "SW-RECORD-LAYOUT-V-PROP")) \
                    .setSwRecordLayoutVIndex(self.getChildElementOptionalLiteral(child_element, "SW-RECORD-LAYOUT-V-INDEX"))
        return layout_v
    
    def readSwRecordLayoutGroupSwRecordLayoutGroupContentType(self, element: ET.Element, group: SwRecordLayoutGroup):
        content = SwRecordLayoutGroupContent()
        content.setSwRecordLayoutGroup(self.getSwRecordLayoutGroup(element, "SW-RECORD-LAYOUT-GROUP")) \
               .setSwRecordLayoutV(self.getSwRecordLayoutV(element, "SW-RECORD-LAYOUT-V"))
        group.setSwRecordLayoutGroupContentType(content)

    def getSwRecordLayoutGroup(self, element: ET.Element, key: str) -> SwRecordLayoutGroup:
        child_element = self.find(element, key)
        group = None
        if child_element is not None:
            group = SwRecordLayoutGroup()
            group.setShortLabel(self.getChildElementOptionalLiteral(child_element, "SHORT-LABEL")) \
                 .setCategory(self.getChildElementOptionalLiteral(child_element, "CATEGORY")) \
                 .setSwRecordLayoutGroupAxis(self.getChildElementOptionalLiteral(child_element, "SW-RECORD-LAYOUT-GROUP-AXIS")) \
                 .setSwRecordLayoutGroupIndex(self.getChildElementOptionalLiteral(child_element, "SW-RECORD-LAYOUT-GROUP-INDEX")) \
                 .setSwRecordLayoutGroupFrom(self.getChildElementOptionalLiteral(child_element, "SW-RECORD-LAYOUT-GROUP-FROM")) \
                 .setSwRecordLayoutGroupStep(self.getChildElementOptionalIntegerValue(child_element, "SW-RECORD-LAYOUT-GROUP-STEP")) \
                 .setSwRecordLayoutGroupTo(self.getChildElementOptionalLiteral(child_element, "SW-RECORD-LAYOUT-GROUP-TO"))
            self.readSwRecordLayoutGroupSwRecordLayoutGroupContentType(child_element, group)
            
        return group

    def readSwRecordLayout(self, element: ET.Element, layout: SwRecordLayout):
        self.logger.debug("Read SwRecordLayout <%s>" % layout.getShortName())
        self.readIdentifiable(element, layout)
        layout.setSwRecordLayoutGroup(self.getSwRecordLayoutGroup(element, "SW-RECORD-LAYOUT-GROUP"))

    def readSwAddrMethod(self, element: ET.Element, method: SwAddrMethod):
        self.logger.debug("Read SwAddrMethod <%s>" % method.getShortName())
        self.readIdentifiable(element, method)
        method.setMemoryAllocationKeywordPolicy(self.getChildElementOptionalLiteral(element, "MEMORY-ALLOCATION-KEYWORD-POLICY"))
        for option in self.getChildElementLiteralValueList(element, "OPTIONS/OPTION"):
            method.addOption(option)
        method.setSectionInitializationPolicy(self.getChildElementOptionalLiteral(element, "SECTION-INITIALIZATION-POLICY")) \
              .setSectionType(self.getChildElementOptionalLiteral(element, "SECTION-TYPE"))

    def readTriggerInterface(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readTriggerInterface(*args, **kwargs)


    def readModeDeclarationGroupModeDeclaration(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readModeDeclarationGroupModeDeclaration(*args, **kwargs)


    def readModeDeclarationGroup(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readModeDeclarationGroup(*args, **kwargs)


    def readModeSwitchInterfaceModeGroup(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readModeSwitchInterfaceModeGroup(*args, **kwargs)


    def readModeSwitchInterface(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readModeSwitchInterface(*args, **kwargs)


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

    def readFrameTriggering(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readFrameTriggering(*args, **kwargs)


    def readCanFrameTriggering(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readCanFrameTriggering(*args, **kwargs)


    def readLinFrameTriggering(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readLinFrameTriggering(*args, **kwargs)


    def readCommunicationCycle(self, element: ET.Element, cycle: CommunicationCycle):
        self.readARObjectAttributes(element, cycle)
        
    def readCycleRepetition(self, element: ET.Element, cycle: CycleRepetition):
        self.readCommunicationCycle(element, cycle)
        cycle.setBaseCycle(self.getChildElementOptionalIntegerValue(element, "BASE-CYCLE")) \
             .setCycleRepetition(self.getChildElementOptionalLiteral(element, "CYCLE-REPETITION"))
        
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
        
    def readFlexrayFrameTriggeringAbsolutelyScheduledTimings(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readFlexrayFrameTriggeringAbsolutelyScheduledTimings(*args, **kwargs)


    def readFlexrayFrameTriggering(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readFlexrayFrameTriggering(*args, **kwargs)


    def readISignalTriggering(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readISignalTriggering(*args, **kwargs)


    def readPduTriggering(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readPduTriggering(*args, **kwargs)


    def readPhysicalChannelCommConnectorRefs(self, element: ET.Element, channel: PhysicalChannel):
        for child_element in self.findall(element, 'COMM-CONNECTORS/COMMUNICATION-CONNECTOR-REF-CONDITIONAL'):
            channel.addCommConnectorRef(self.getChildElementOptionalRefType(child_element, "COMMUNICATION-CONNECTOR-REF"))

    def readPhysicalChannelFrameTriggerings(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readPhysicalChannelFrameTriggerings(*args, **kwargs)


    def readPhysicalChannelISignalTriggerings(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readPhysicalChannelISignalTriggerings(*args, **kwargs)


    def readPhysicalChannelPduTriggerings(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readPhysicalChannelPduTriggerings(*args, **kwargs)


    def readPhysicalChannel(self, element: ET.Element, channel: PhysicalChannel):
        self.readIdentifiable(element, channel)

        self.readPhysicalChannelCommConnectorRefs(element, channel)
        self.readPhysicalChannelFrameTriggerings(element, channel)
        self.readPhysicalChannelISignalTriggerings(element, channel)
        self.readPhysicalChannelPduTriggerings(element, channel)

    def readCanPhysicalChannel(self, element: ET.Element, channel: CanPhysicalChannel):
        self.readPhysicalChannel(element, channel)

    def readScheduleTableEntry(self, element: ET.Element, entry: ScheduleTableEntry):
        entry.setDelay(self.getChildElementOptionalTimeValue(element, "DELAY")) \
             .setPositionInTable(self.getChildElementOptionalIntegerValue(element, "POSITION-IN-TABLE"))

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
        table.setResumePosition(self.getChildElementOptionalLiteral(element, "RESUME-POSITION")) \
             .setRunMode(self.getChildElementOptionalLiteral(element, "RUN-MODE"))
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
            configuration.setAssignmentPriority(self.getChildElementOptionalPositiveInteger(element, "ASSIGNMENT-PRIORITY")) \
                         .setDefaultRouter(self.getChildElementOptionalLiteral(element, "DEFAULT-ROUTER")) \
                         .setEnableAnycast(self.getChildElementOptionalBooleanValue(element, "ENABLE-ANYCAST")) \
                         .setHopCount(self.getChildElementOptionalPositiveInteger(element, "HOP-COUNT")) \
                         .setIpAddressPrefixLength(self.getChildElementOptionalPositiveInteger(element, "IP-ADDRESS-PREFIX-LENGTH")) \
                         .setIpv6Address(self.getChildElementOptionalLiteral(element, "IPV-6-ADDRESS")) \
                         .setIpv6AddressSource(self.getChildElementOptionalLiteral(element, "IPV-6-ADDRESS-SOURCE"))
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
            identifier.setHeaderId(self.getChildElementOptionalPositiveInteger(element, "HEADER-ID")) \
                      .setPduCollectionSemantics(self.getChildElementOptionalLiteral(element, "PDU-COLLECTION-SEMANTICS")) \
                      .setPduCollectionTrigger(self.getChildElementOptionalLiteral(element, "PDU-COLLECTION-TRIGGER")) \
                      .setPduRef(self.getChildElementOptionalRefType(element, "PDU-REF")) \
                      .setPduTriggeringRef(self.getChildElementOptionalRefType(element, "PDU-TRIGGERING-REF"))
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
            connection.setClientIpAddrFromConnectionRequest(self.getChildElementOptionalBooleanValue(element, "CLIENT-IP-ADDR-FROM-CONNECTION-REQUEST")) \
                      .setClientPortFromConnectionRequest(self.getChildElementOptionalBooleanValue(element, "CLIENT-PORT-FROM-CONNECTION-REQUEST")) \
                      .setClientPortRef(self.getChildElementOptionalRefType(element, "CLIENT-PORT-REF"))            # NOQA E501
            for pdu in self.getSocketConnectionPdus(element):
                connection.addPdu(pdu)
            connection.setPduCollectionMaxBufferSize(self.getChildElementOptionalPositiveInteger(element, "PDU-COLLECTION-MAX-BUFFER-SIZE")) \
                      .setPduCollectionTimeout(self.getChildElementOptionalTimeValue(element, "PDU-COLLECTION-TIMEOUT")) \
                      .setRuntimeIpAddressConfiguration(self.getChildElementOptionalLiteral(element, "RUNTIME-IP-ADDRESS-CONFIGURATION")) \
                      .setRuntimePortConfiguration(self.getChildElementOptionalLiteral(element, "RUNTIME-PORT-CONFIGURATION")) \
                      .setShortLabel(self.getChildElementOptionalLiteral(element, "SHORT-LABEL"))
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
            port.setDynamicallyAssigned(self.getChildElementOptionalBooleanValue(child_element, "DYNAMICALLY-ASSIGNED")) \
                .setPortNumber(self.getChildElementOptionalPositiveInteger(child_element, "PORT-NUMBER"))
        return port

    def readUdpTp(self, element: ET.Element, tp: UdpTp):
        tp.setUdpTpPort(self.getTpPort(element, "UDP-TP-PORT"))

    def readTcpTp(self, element: ET.Element, tp: TcpTp):
        tp.setKeepAliveInterval(self.getChildElementOptionalTimeValue(element, "KEEP-ALIVE-INTERVAL")) \
          .setKeepAliveProbesMax(self.getChildElementOptionalPositiveInteger(element, "KEEP-ALIVE-PROBES-MAX")) \
          .setKeepAliveTime(self.getChildElementOptionalTimeValue(element, "KEEP-ALIVE-TIME")) \
          .setKeepAlives(self.getChildElementOptionalBooleanValue(element, "KEEP-ALIVES")) \
          .setNaglesAlgorithm(self.getChildElementOptionalLiteral(element, "NAGLES-ALGORITHM")) \
          .setTcpTpPort(self.getTpPort(element, "TCP-TP-PORT"))

    def readGenericTp(self, element: ET.Element, tp: GenericTp):
        tp.setTpAddress(self.getChildElementOptionalLiteral(element, "TP-ADDRESS")) \
          .setTpTechnology(self.getChildElementOptionalLiteral(element, "TP-TECHNOLOGY"))

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
            delay.setMaxValue(self.getChildElementOptionalTimeValue(child_element, "MAX-VALUE")) \
                 .setMinValue(self.getChildElementOptionalTimeValue(child_element, "MIN-VALUE"))
        return delay

    def getSdClientConfig(self, element: ET.Element, key: str) -> SdClientConfig:
        config = None
        child_element = self.find(element, key)
        if child_element is not None:
            config = SdClientConfig()
            config.setClientServiceMajorVersion(self.getChildElementOptionalPositiveInteger(child_element, "CLIENT-SERVICE-MAJOR-VERSION")) \
                  .setClientServiceMinorVersion(self.getChildElementOptionalPositiveInteger(child_element, "CLIENT-SERVICE-MINOR-VERSION")) \
                  .setInitialFindBehavior(self.getInitialSdDelayConfig(child_element, "INITIAL-FIND-BEHAVIOR")) \
                  .setRequestResponseDelay(self.getRequestResponseDelay(child_element, "REQUEST-RESPONSE-DELAY")) \
                  .setTtl(self.getChildElementOptionalPositiveInteger(child_element, "TTL"))
        return config
    
    def readConsumedEventGroup(self, element: ET.Element, group: ConsumedEventGroup):
        self.readIdentifiable(element, group)
        group.setApplicationEndpointRef(self.getChildElementOptionalRefType(element, "APPLICATION-ENDPOINT-REF")) \
             .setEventGroupIdentifier(self.getChildElementOptionalPositiveInteger(element, "EVENT-GROUP-IDENTIFIER"))
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
            config.setInitialDelayMaxValue(self.getChildElementOptionalTimeValue(child_element, "INITIAL-DELAY-MAX-VALUE")) \
                  .setInitialDelayMinValue(self.getChildElementOptionalTimeValue(child_element, "INITIAL-DELAY-MIN-VALUE")) \
                  .setInitialRepetitionsBaseDelay(self.getChildElementOptionalTimeValue(child_element, "INITIAL-REPETITIONS-BASE-DELAY")) \
                  .setInitialRepetitionsMax(self.getChildElementOptionalPositiveInteger(child_element, "INITIAL-REPETITIONS-MAX"))
        return config
    
    def getSdServerConfig(self, element: ET.Element, key: str) -> SdServerConfig:
        config = None
        child_element = self.find(element, key)
        if child_element is not None:
            config = SdServerConfig()
            config.setInitialOfferBehavior(self.getInitialSdDelayConfig(child_element, "INITIAL-OFFER-BEHAVIOR")) \
                  .setOfferCyclicDelay(self.getChildElementOptionalTimeValue(child_element, "OFFER-CYCLIC-DELAY")) \
                  .setRequestResponseDelay(self.getRequestResponseDelay(child_element, "REQUEST-RESPONSE-DELAY")) \
                  .setServerServiceMajorVersion(self.getChildElementOptionalPositiveInteger(child_element, "SERVER-SERVICE-MAJOR-VERSION")) \
                  .setServerServiceMinorVersion(self.getChildElementOptionalPositiveInteger(child_element, "SERVER-SERVICE-MINOR-VERSION")) \
                  .setTtl(self.getChildElementOptionalPositiveInteger(child_element, "TTL"))
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
        instance.setInstanceIdentifier(self.getChildElementOptionalPositiveInteger(element, "INSTANCE-IDENTIFIER")) \
                .setSdServerConfig(self.getSdServerConfig(element, "SD-SERVER-CONFIG")) \
                .setServiceIdentifier(self.getChildElementOptionalPositiveInteger(element, "SERVICE-IDENTIFIER"))

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
            end_point.setNetworkEndpointRef(self.getChildElementOptionalRefType(child_element, "NETWORK-ENDPOINT-REF")) \
                     .setPriority(self.getChildElementOptionalPositiveInteger(child_element, "PRIORITY"))
            self.readSocketAddressApplicationEndpointProvidedServiceInstance(child_element, end_point)
            end_point.setTpConfiguration(self.getTransportProtocolConfiguration(child_element, "TP-CONFIGURATION"))
            
    def readSocketAddressMulticastConnectorRefs(self, element: ET.Element, address: SocketAddress):
        for ref in self.getChildElementRefTypeList(element, "MULTICAST-CONNECTOR-REFS/MULTICAST-CONNECTOR-REF"):
            address.addMulticastConnectorRef(ref)

    def readSocketAddress(self, element: ET.Element, address: SocketAddress):
        self.readIdentifiable(element, address)
        self.readSocketAddressApplicationEndpoint(element, address)
        self.readSocketAddressMulticastConnectorRefs(element, address)
        address.setConnectorRef(self.getChildElementOptionalRefType(element, "CONNECTOR-REF")) \
               .setPortAddress(self.getChildElementOptionalPositiveInteger(element, "PORT-ADDRESS"))

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
        cluster.setProtocolName(self.getChildElementOptionalLiteral(element, "PROTOCOL-NAME")) \
               .setProtocolVersion(self.getChildElementOptionalLiteral(element, "PROTOCOL-VERSION"))
        
    def getCanClusterBusOffRecovery(self, element: ET.Element, key: str) -> CanClusterBusOffRecovery:
        recovery = None
        child_element = self.find(element, key)
        if child_element is not None:
            recovery = CanClusterBusOffRecovery()
            recovery.setBorCounterL1ToL2(self.getChildElementOptionalPositiveInteger(child_element, "BOR-COUNTER-L-1-TO-L-2")) \
                    .setBorTimeL1(self.getChildElementOptionalTimeValue(child_element, "BOR-TIME-L-1")) \
                    .setBorTimeL2(self.getChildElementOptionalTimeValue(child_element, "BOR-TIME-L-2"))
        return recovery
        
    def readAbstractCanCluster(self, element: ET.Element, cluster: AbstractCanCluster):
        self.readCommunicationCluster(element, cluster)
        cluster.setBusOffRecovery(self.getCanClusterBusOffRecovery(element, "BUS-OFF-RECOVERY")) \
               .setCanFdBaudrate(self.getChildElementOptionalNumericalValue(element, "CAN-FD-BAUDRATE")) \
               .setSpeed(self.getChildElementOptionalNumericalValue(element, "SPEED"))

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
            cluster.setActionPointOffset(self.getChildElementOptionalIntegerValue(child_element, "ACTION-POINT-OFFSET")) \
                   .setBit(self.getChildElementOptionalTimeValue(child_element, "BIT")) \
                   .setCasRxLowMax(self.getChildElementOptionalIntegerValue(child_element, "CAS-RX-LOW-MAX")) \
                   .setColdStartAttempts(self.getChildElementOptionalIntegerValue(child_element, "COLD-START-ATTEMPTS")) \
                   .setCycle(self.getChildElementOptionalTimeValue(child_element, "CYCLE")) \
                   .setCycleCountMax(self.getChildElementOptionalIntegerValue(child_element, "CYCLE-COUNT-MAX")) \
                   .setDetectNitError(self.getChildElementOptionalBooleanValue(child_element, "DETECT-NIT-ERROR")) \
                   .setDynamicSlotIdlePhase(self.getChildElementOptionalIntegerValue(child_element, "DYNAMIC-SLOT-IDLE-PHASE")) \
                   .setIgnoreAfterTx(self.getChildElementOptionalIntegerValue(child_element, "IGNORE-AFTER-TX")) \
                   .setListenNoise(self.getChildElementOptionalIntegerValue(child_element, "LISTEN-NOISE")) \
                   .setMacroPerCycle(self.getChildElementOptionalIntegerValue(child_element, "MACRO-PER-CYCLE")) \
                   .setMacrotickDuration(self.getChildElementOptionalTimeValue(child_element, "MACROTICK-DURATION")) \
                   .setMaxWithoutClockCorrectionFatal(self.getChildElementOptionalIntegerValue(child_element, "MAX-WITHOUT-CLOCK-CORRECTION-FATAL")) \
                   .setMaxWithoutClockCorrectionPassive(self.getChildElementOptionalIntegerValue(child_element, "MAX-WITHOUT-CLOCK-CORRECTION-PASSIVE")) \
                   .setMinislotActionPointOffset(self.getChildElementOptionalIntegerValue(child_element, "MINISLOT-ACTION-POINT-OFFSET")) \
                   .setMinislotDuration(self.getChildElementOptionalIntegerValue(child_element, "MINISLOT-DURATION")) \
                   .setNetworkIdleTime(self.getChildElementOptionalIntegerValue(child_element, "NETWORK-IDLE-TIME")) \
                   .setNetworkManagementVectorLength(self.getChildElementOptionalIntegerValue(child_element, "NETWORK-MANAGEMENT-VECTOR-LENGTH")) \
                   .setNumberOfMinislots(self.getChildElementOptionalIntegerValue(child_element, "NUMBER-OF-MINISLOTS")) \
                   .setNumberOfStaticSlots(self.getChildElementOptionalIntegerValue(child_element, "NUMBER-OF-STATIC-SLOTS")) \
                   .setOffsetCorrectionStart(self.getChildElementOptionalIntegerValue(child_element, "OFFSET-CORRECTION-START")) \
                   .setPayloadLengthStatic(self.getChildElementOptionalIntegerValue(child_element, "PAYLOAD-LENGTH-STATIC")) \
                   .setSafetyMargin(self.getChildElementOptionalIntegerValue(child_element, "SAFETY-MARGIN")) \
                   .setSampleClockPeriod(self.getChildElementOptionalTimeValue(child_element, "SAMPLE-CLOCK-PERIOD")) \
                   .setStaticSlotDuration(self.getChildElementOptionalIntegerValue(child_element, "STATIC-SLOT-DURATION")) \
                   .setSyncFrameIdCountMax(self.getChildElementOptionalIntegerValue(child_element, "SYNC-FRAME-ID-COUNT-MAX")) \
                   .setTransmissionStartSequenceDuration(self.getChildElementOptionalIntegerValue(child_element, "TRANSMISSION-START-SEQUENCE-DURATION")) \
                   .setWakeupRxIdle(self.getChildElementOptionalIntegerValue(child_element, "WAKEUP-RX-IDLE")) \
                   .setWakeupRxLow(self.getChildElementOptionalIntegerValue(child_element, "WAKEUP-RX-LOW")) \
                   .setWakeupRxWindow(self.getChildElementOptionalIntegerValue(child_element, "WAKEUP-RX-WINDOW")) \
                   .setWakeupTxActive(self.getChildElementOptionalIntegerValue(child_element, "WAKEUP-TX-ACTIVE")) \
                   .setWakeupTxIdle(self.getChildElementOptionalIntegerValue(child_element, "WAKEUP-TX-IDLE"))            # noqa E501

    def readMacMulticastGroup(self, element: ET.Element, group: MacMulticastGroup):
        self.readIdentifiable(element, group)
        group.setMacMulticastAddress(self.getChildElementOptionalLiteral(element, "MAC-MULTICAST-ADDRESS",))

    def readEthernetClusterMacMulticastGroups(self, element: ET.Element, cluster: EthernetCluster):
        for child_element in self.findall(element, "MAC-MULTICAST-GROUPS/*"):
            tag_name = self.getTagName(child_element)
            if (tag_name == "MAC-MULTICAST-GROUP"):
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
        connection.setPhysicalRequestRef(self.getChildElementOptionalRefType(element, "PHYSICAL-REQUEST-REF")) \
                  .setResponseOnEventRef(self.getChildElementOptionalRefType(element, "RESPONSE-REF"))
        
    def readDiagnosticServiceTableDiagnosticConnectionRefs(self, element: ET.Element, table: DiagnosticServiceTable):
        for ref in self.getChildElementRefTypeList(element, "DIAGNOSTIC-CONNECTIONS/DIAGNOSTIC-CONNECTION-REF-CONDITIONAL/DIAGNOSTIC-CONNECTION-REF"):
            table.addDiagnosticConnectionRef(ref)
        
    def readDiagnosticServiceTable(self, element: ET.Element, table: DiagnosticServiceTable):
        self.logger.debug("Read DiagnosticServiceTable <%s>" % table.getShortName())
        self.readIdentifiable(element, table)
        self.readDiagnosticServiceTableDiagnosticConnectionRefs(element, table)
        table.setEcuInstanceRef(self.getChildElementOptionalRefType(element, "ECU-INSTANCE-REF"))

    def readSegmentPosition(self, element: ET.Element, position: SegmentPosition):
        position.setSegmentByteOrder(self.getChildElementOptionalLiteral(element, "SEGMENT-BYTE-ORDER")) \
                .setSegmentLength(self.getChildElementOptionalIntegerValue(element, "SEGMENT-LENGTH")) \
                .setSegmentPosition(self.getChildElementOptionalIntegerValue(element, "SEGMENT-POSITION"))

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
        alternative.setIPduRef(self.getChildElementOptionalRefType(element, "I-PDU-REF")) \
                   .setInitialDynamicPart(self.getChildElementOptionalBooleanValue(element, "INITIAL-DYNAMIC-PART")) \
                   .setSelectorFieldCode(self.getChildElementOptionalIntegerValue(element, "SELECTOR-FIELD-CODE"))

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
        ipdu.setSelectorFieldByteOrder(self.getChildElementOptionalLiteral(element, "SELECTOR-FIELD-BYTE-ORDER")) \
            .setSelectorFieldLength(self.getChildElementOptionalIntegerValue(element, "SELECTOR-FIELD-LENGTH")) \
            .setSelectorFieldStartPosition(self.getChildElementOptionalIntegerValue(element, "SELECTOR-FIELD-START-POSITION"))
        self.readMultiplexedIPduStaticParts(element, ipdu)
        ipdu.setTriggerMode(self.getChildElementOptionalLiteral(element, "TRIGGER-MODE")) \
            .setUnusedBitPattern(self.getChildElementOptionalIntegerValue(element, "UNUSED-BIT-PATTERN"))

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
        props.setAuthAlgorithm(self.getChildElementOptionalLiteral(element, "AUTH-ALGORITHM")) \
             .setAuthInfoTxLength(self.getChildElementOptionalPositiveInteger(element, "AUTH-INFO-TX-LENGTH"))

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
        props.setFreshnessValueLength(self.getChildElementOptionalLiteral(element, "FRESHNESS-VALUE-LENGTH")) \
             .setFreshnessValueTxLength(self.getChildElementOptionalPositiveInteger(element, "FRESHNESS-VALUE-TX-LENGTH"))

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
        connection.setDoIpSourceAddressRef(self.getChildElementOptionalRefType(element, "DO-IP-SOURCE-ADDRESS-REF")) \
                  .setDoIpTargetAddressRef(self.getChildElementOptionalRefType(element, "DO-IP-TARGET-ADDRESS-REF")) \
                  .setTpSduRef(self.getChildElementOptionalRefType(element, "TP-SDU-REF"))

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

    def readHwDescriptionEntity(self, element: ET.Element, entity: HwDescriptionEntity):
        self.readARElement(element, entity)
        self.readHwDescriptionEntityHwCategoryRefs(element, entity)

    def readHwPinGroup(self, element: ET.SubElement, pin_group: HwPinGroup):
        self.readHwDescriptionEntity(element, pin_group)

    def readHwElementHwPinGroups(self, element: ET.Element, hw_element: HwElement):
        for child_element in self.findall(element, "HW-PIN-GROUPS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "HW-PIN-GROUP":
                pin_group = hw_element.createHwPinGroup(self.getShortName(child_element))
                self.readHwPinGroup(child_element, pin_group)
            else:
                self.notImplemented("Unsupported Hw Pin Group <%s>" % tag_name)

    def readHwElement(self, element: ET.Element, hw_element: HwElement):
        self.logger.debug("Read HwElement <%s>" % hw_element.getShortName())
        self.readHwDescriptionEntity(element, hw_element)
        self.readHwElementHwPinGroups(element, hw_element)

    def readHwAttributeDef(self, element: ET.Element, attribute_def: HwAttributeDef):
        self.readIdentifiable(element, attribute_def)
        attribute_def.setUnitRef(self.getChildElementOptionalRefType(element, "UNIT-REF"))

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
        self.readARElement(element, type)

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
        pdu.setHasDynamicLength(self.getChildElementOptionalBooleanValue(element, "HAS-DYNAMIC-LENGTH")) \
           .setLength(self.getChildElementOptionalNumericalValue(element, "LENGTH"))
        
    def readISignalToIPduMapping(self, element: ET.Element, mapping: ISignalToIPduMapping):
        self.readIdentifiable(element, mapping)
        mapping.setISignalRef(self.getChildElementOptionalRefType(element, "I-SIGNAL-REF")) \
               .setPackingByteOrder(self.getChildElementOptionalLiteral(element, "PACKING-BYTE-ORDER")) \
               .setStartPosition(self.getChildElementOptionalIntegerValue(element, "START-POSITION")) \
               .setTransferProperty(self.getChildElementOptionalLiteral(element, "TRANSFER-PROPERTY"))
        
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

    def readIPdu(self, element: ET.Element, pdu: IPdu):
        self.readPdu(element, pdu)

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
            props.setAuthDataFreshnessLength(self.getChildElementOptionalPositiveInteger(child_element, "AUTH-DATA-FRESHNESS-LENGTH")) \
                 .setAuthDataFreshnessStartPosition(self.getChildElementOptionalPositiveInteger(child_element, "AUTH-DATA-FRESHNESS-START-POSITION")) \
                 .setAuthInfoTxLength(self.getChildElementOptionalPositiveInteger(child_element, "AUTH-INFO-TX-LENGTH")) \
                 .setAuthenticationBuildAttempts(self.getChildElementOptionalPositiveInteger(child_element, "AUTHENTICATION-BUILD-ATTEMPTS")) \
                 .setAuthenticationRetries(self.getChildElementOptionalPositiveInteger(child_element, "AUTHENTICATION-RETRIES")) \
                 .setDataId(self.getChildElementOptionalPositiveInteger(child_element, "DATA-ID")) \
                 .setFreshnessValueId(self.getChildElementOptionalPositiveInteger(child_element, "FRESHNESS-VALUE-ID")) \
                 .setFreshnessValueLength(self.getChildElementOptionalPositiveInteger(child_element, "FRESHNESS-VALUE-LENGTH")) \
                 .setFreshnessValueTxLength(self.getChildElementOptionalPositiveInteger(child_element, "FRESHNESS-VALUE-TX-LENGTH"))            # NOQA E501
        return props

    def readSecuredIPdu(self, element: ET.Element, i_pdu: SecuredIPdu):
        self.logger.debug("Read SecuredIPdu <%s>" % i_pdu.getShortName())
        self.readIPdu(element, i_pdu)
        i_pdu.setAuthenticationPropsRef(self.getChildElementOptionalRefType(element, "AUTHENTICATION-PROPS-REF")) \
             .setFreshnessPropsRef(self.getChildElementOptionalRefType(element, "FRESHNESS-PROPS-REF")) \
             .setPayloadRef(self.getChildElementOptionalRefType(element, "PAYLOAD-REF")) \
             .setSecureCommunicationProps(self.getSecureCommunicationProps(element, "SECURE-COMMUNICATION-PROPS")) \
             .setUseAsCryptographicIPdu(self.getChildElementOptionalBooleanValue(element, "USE-AS-CRYPTOGRAPHIC-I-PDU"))

    def readNmNode(self, element: ET.Element, nm_node: NmNode):
        self.readIdentifiable(element, nm_node)

        nm_node.setControllerRef(self.getChildElementOptionalRefType(element, "CONTROLLER-REF")) \
               .setNmIfEcuRef(self.getChildElementOptionalRefType(element, "NM-IF-ECU-REF")) \
               .setNmPassiveModeEnabled(self.getChildElementOptionalBooleanValue(element, "NM-PASSIVE-MODE-ENABLED")) \
               .setNmNodeId(self.getChildElementOptionalNumericalValue(element, "NM-NODE-ID"))
        for ref in self.getChildElementRefTypeList(element, "RX-NM-PDU-REFS/RX-NM-PDU-REF"):
            nm_node.addRxNmPduRef(ref)
        for ref in self.getChildElementRefTypeList(element, "TX-NM-PDU-REFS/TX-NM-PDU-REF"):
            nm_node.addTxNmPduRefs(ref)

    def readCanNmNode(self, element: ET.Element, nm_node: CanNmNode):
        self.logger.debug("Read CanNmNode <%s>" % nm_node.getShortName())
        self.readNmNode(element, nm_node)
        nm_node.setNmCarWakeUpRxEnabled(self.getChildElementOptionalBooleanValue(element, "NM-CAR-WAKE-UP-RX-ENABLED")) \
               .setNmMsgCycleOffset(self.getChildElementOptionalFloatValue(element, "NM-MSG-CYCLE-OFFSET")) \
               .setNmMsgReducedTime(self.getChildElementOptionalFloatValue(element, "NM-MSG-REDUCED-TIME")) \
               .setNmRangeConfig(self.getChildElementRxIdentifierRange(element, "NM-RANGE-CONFIG"))
        
    def readUdpNmNode(self, element: ET.Element, nm_node: UdpNmNode):
        self.logger.debug("Read UdpNmNode <%s>" % nm_node.getShortName())
        self.readNmNode(element, nm_node)
        nm_node.setNmMsgCycleOffset(self.getChildElementOptionalTimeValue(element, "NM-MSG-CYCLE-OFFSET"))

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
            else:
                self.notImplemented("Unsupported Nm Node <%s>" % tag_name)

    def getCanNmClusterCoupling(self, element: ET.Element) -> CanNmClusterCoupling:
        coupling = CanNmClusterCoupling()
        for ref in self.getChildElementRefTypeList(element, "COUPLED-CLUSTER-REFS/COUPLED-CLUSTER-REF"):
            coupling.addCoupledClusterRef(ref)
        coupling.setNmBusloadReductionEnabled(self.getChildElementOptionalBooleanValue(element, "NM-BUSLOAD-REDUCTION-ENABLED")) \
                .setNmImmediateRestartEnabled(self.getChildElementOptionalBooleanValue(element, "NM-IMMEDIATE-RESTART-ENABLED"))
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
        cluster.setCommunicationClusterRef(self.getChildElementOptionalRefType(element, "COMMUNICATION-CLUSTER-REF")) \
               .setNmChannelId(self.getChildElementOptionalNumericalValue(element, "NM-CHANNEL-ID")) \
               .setNmChannelSleepMaster(self.getChildElementOptionalBooleanValue(element, "NM-CHANNEL-SLEEP-MASTER"))
        self.readNmClusterNmNodes(element, cluster)
        cluster.setNmSynchronizingNetwork(self.getChildElementOptionalBooleanValue(element, "NM-SYNCHRONIZING-NETWORK"))

    def readCanNmCluster(self, element: ET.Element, cluster: CanNmCluster):
        self.logger.debug("Read CanNmCluster <%s>" % cluster.getShortName())
        self.readNmCluster(element, cluster)
        cluster.setNmBusloadReductionActive(self.getChildElementOptionalBooleanValue(element, "NM-BUSLOAD-REDUCTION-ACTIVE")) \
               .setNmCarWakeUpRxEnabled(self.getChildElementOptionalBooleanValue(element, "NM-CAR-WAKE-UP-RX-ENABLED")) \
               .setNmCbvPosition(self.getChildElementOptionalNumericalValue(element, "NM-CBV-POSITION")) \
               .setNmChannelActive(self.getChildElementOptionalBooleanValue(element, "NM-CHANNEL-ACTIVE")) \
               .setNmImmediateNmCycleTime(self.getChildElementOptionalFloatValue(element, "NM-IMMEDIATE-NM-CYCLE-TIME")) \
               .setNmImmediateNmTransmissions(self. getChildElementOptionalNumericalValue(element, "NM-IMMEDIATE-NM-TRANSMISSIONS")) \
               .setNmMessageTimeoutTime(self.getChildElementOptionalFloatValue(element, "NM-MESSAGE-TIMEOUT-TIME")) \
               .setNmMsgCycleTime(self.getChildElementOptionalFloatValue(element, "NM-MSG-CYCLE-TIME")) \
               .setNmNetworkTimeout(self.getChildElementOptionalFloatValue(element, "NM-NETWORK-TIMEOUT")) \
               .setNmNidPosition(self. getChildElementOptionalNumericalValue(element, "NM-NID-POSITION")) \
               .setNmRemoteSleepIndicationTime(self.getChildElementOptionalFloatValue(element, "NM-REMOTE-SLEEP-INDICATION-TIME")) \
               .setNmRepeatMessageTime(self.getChildElementOptionalFloatValue(element, "NM-REPEAT-MESSAGE-TIME")) \
               .setNmUserDataLength(self. getChildElementOptionalNumericalValue(element, "NM-USER-DATA-LENGTH")) \
               .setNmWaitBusSleepTime(self.getChildElementOptionalFloatValue(element, "NM-WAIT-BUS-SLEEP-TIME"))
        
    def readUdpNmCluster(self, element: ET.Element, cluster: UdpNmCluster):
        self.logger.debug("Read UdpNmCluster %s" % cluster.getShortName())
        self.readNmCluster(element, cluster)
        cluster.setNmCbvPosition(self.getChildElementOptionalIntegerValue(element, "NM-CBV-POSITION")) \
               .setNmChannelActive(self.getChildElementOptionalBooleanValue(element, "NM-CHANNEL-ACTIVE")) \
               .setNmImmediateNmCycleTime(self.getChildElementOptionalTimeValue(element, "NM-IMMEDIATE-NM-CYCLE-TIME")) \
               .setNmImmediateNmTransmissions(self.getChildElementOptionalPositiveInteger(element, "NM-IMMEDIATE-NM-TRANSMISSIONS")) \
               .setNmMessageTimeoutTime(self.getChildElementOptionalTimeValue(element, "NM-MESSAGE-TIMEOUT-TIME")) \
               .setNmMsgCycleTime(self.getChildElementOptionalTimeValue(element, "NM-MSG-CYCLE-TIME")) \
               .setNmNetworkTimeout(self.getChildElementOptionalTimeValue(element, "NM-NETWORK-TIMEOUT")) \
               .setNmNidPosition(self.getChildElementOptionalIntegerValue(element, "NM-NID-POSITION")) \
               .setNmRemoteSleepIndicationTime(self.getChildElementOptionalTimeValue(element, "NM-REMOTE-SLEEP-INDICATION-TIME")) \
               .setNmRepeatMessageTime(self.getChildElementOptionalTimeValue(element, "NM-REPEAT-MESSAGE-TIME")) \
               .setNmWaitBusSleepTime(self.getChildElementOptionalTimeValue(element, "NM-WAIT-BUS-SLEEP-TIME")) \
               .setVlanRef(self.getChildElementOptionalRefType(element, "VLAN-REF"))
        
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
        nm_ecu.setEcuInstanceRef(self.getChildElementOptionalRefType(element, "ECU-INSTANCE-REF")) \
              .setNmBusSynchronizationEnabled(self.getChildElementOptionalBooleanValue(element, "NM-BUS-SYNCHRONIZATION-ENABLED")) \
              .setNmComControlEnabled(self.getChildElementOptionalBooleanValue(element, "NM-COM-CONTROL-ENABLED")) \
              .setNmNodeDetectionEnabled(self.getChildElementOptionalBooleanValue(element, "NM-NODE-DETECTION-ENABLED")) \
              .setNmNodeIdEnabled(self.getChildElementOptionalBooleanValue(element, "NM-NODE-ID-ENABLED")) \
              .setNmPduRxIndicationEnabled(self.getChildElementOptionalBooleanValue(element, "NM-PDU-RX-INDICATION-ENABLED")) \
              .setNmRemoteSleepIndEnabled(self.getChildElementOptionalBooleanValue(element, "NM-REMOTE-SLEEP-IND-ENABLED")) \
              .setNmRepeatMsgIndEnabled(self.getChildElementOptionalBooleanValue(element, "NM-REPEAT-MSG-IND-ENABLED")) \
              .setNmStateChangeIndEnabled(self.getChildElementOptionalBooleanValue(element, "NM-STATE-CHANGE-IND-ENABLED")) \
              .setNmUserDataEnabled(self.getChildElementOptionalBooleanValue(element, "NM-USER-DATA-ENABLED"))

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
        address.setTpAddress(self.getChildElementOptionalIntegerValue(element, "TP-ADDRESS")) \
               .setTpAddressExtensionValue(self.getChildElementOptionalIntegerValue(element, "TP-ADDRESS-EXTENSION-VALUE"))

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
        channel.setChannelId(self.getChildElementOptionalPositiveInteger(element, "CHANNEL-ID")) \
               .setChannelMode(self.getChildElementOptionalLiteral(element, "CHANNEL-MODE"))

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
        connection.setAddressingFormat(self.getChildElementOptionalLiteral(element, "ADDRESSING-FORMAT")) \
                  .setCanTpChannelRef(self.getChildElementOptionalRefType(element, "CAN-TP-CHANNEL-REF")) \
                  .setCancellation(self.getChildElementOptionalBooleanValue(element, "CANCELLATION")) \
                  .setDataPduRef(self.getChildElementOptionalRefType(element, "DATA-PDU-REF")) \
                  .setFlowControlPduRef(self.getChildElementOptionalRefType(element, "FLOW-CONTROL-PDU-REF")) \
                  .setMaxBlockSize(self.getChildElementOptionalIntegerValue(element, "MAX-BLOCK-SIZE")) \
                  .setMulticastRef(self.getChildElementOptionalRefType(element, "MULTICAST-REF")) \
                  .setPaddingActivation(self.getChildElementOptionalBooleanValue(element, "PADDING-ACTIVATION"))
        self.readTpConnectionReceiverRefs(element, connection)
        connection.setTaType(self.getChildElementOptionalLiteral(element, "TA-TYPE")) \
                  .setTimeoutBr(self.getChildElementOptionalTimeValue(element, "TIMEOUT-BR")) \
                  .setTimeoutBs(self.getChildElementOptionalTimeValue(element, "TIMEOUT-BS")) \
                  .setTimeoutCr(self.getChildElementOptionalTimeValue(element, "TIMEOUT-CR")) \
                  .setTimeoutCs(self.getChildElementOptionalTimeValue(element, "TIMEOUT-CS")) \
                  .setTpSduRef(self.getChildElementOptionalRefType(element, "TP-SDU-REF")) \
                  .setTransmitterRef(self.getChildElementOptionalRefType(element, "TRANSMITTER-REF"))

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
        tp_ecu.setCycleTimeMainFunction(self.getChildElementOptionalTimeValue(element, "CYCLE-TIME-MAIN-FUNCTION")) \
              .setEcuInstanceRef(self.getChildElementOptionalRefType(element, "ECU-INSTANCE-REF"))

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
        tp_node.setConnectorRef(self.getChildElementOptionalRefType(element, "CONNECTOR-REF")) \
               .setMaxFcWait(self.getChildElementOptionalIntegerValue(element, "MAX-FC-WAIT")) \
               .setStMin(self.getChildElementOptionalTimeValue(element, "ST-MIN")) \
               .setTimeoutAr(self.getChildElementOptionalTimeValue(element, "TIMEOUT-AR")) \
               .setTimeoutAs(self.getChildElementOptionalTimeValue(element, "TIMEOUT-AS")) \
               .setTpAddressRef(self.getChildElementOptionalRefType(element, "TP-ADDRESS-REF"))

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
        connection.setDataPduRef(self.getChildElementOptionalRefType(element, "DATA-PDU-REF")) \
                  .setFlowControlRef(self.getChildElementOptionalRefType(element, "FLOW-CONTROL-REF")) \
                  .setLinTpNSduRef(self.getChildElementOptionalRefType(element, "LIN-TP-N-SDU-REF"))
        self.readTpConnectionReceiverRefs(element, connection)
        connection.setTimeoutAs(self.getChildElementOptionalTimeValue(element, "TIMEOUT-AS")) \
                  .setTimeoutCr(self.getChildElementOptionalTimeValue(element, "TIMEOUT-CR")) \
                  .setTimeoutCs(self.getChildElementOptionalTimeValue(element, "TIMEOUT-CS")) \
                  .setTransmitterRef(self.getChildElementOptionalRefType(element, "TRANSMITTER-REF"))

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
        tp_node.setConnectorRef(self.getChildElementOptionalRefType(element, "CONNECTOR-REF")) \
               .setDropNotRequestedNad(self.getChildElementOptionalBooleanValue(element, "DROP-NOT-REQUESTED-NAD")) \
               .setP2Max(self.getChildElementOptionalTimeValue(element, "P-2-MAX")) \
               .setP2Timing(self.getChildElementOptionalTimeValue(element, "P-2-TIMING")) \
               .setTpAddressRef(self.getChildElementOptionalRefType(element, "TP-ADDRESS-REF"))

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
            controller.setAcceptedStartupRange(self.getChildElementOptionalIntegerValue(child_element, "ACCEPTED-STARTUP-RANGE")) \
                      .setAllowHaltDueToClock(self.getChildElementOptionalBooleanValue(child_element, "ALLOW-HALT-DUE-TO-CLOCK")) \
                      .setAllowPassiveToActive(self.getChildElementOptionalIntegerValue(child_element, "ALLOW-PASSIVE-TO-ACTIVE")) \
                      .setClusterDriftDamping(self.getChildElementOptionalIntegerValue(child_element, "CLUSTER-DRIFT-DAMPING")) \
                      .setDecodingCorrection(self.getChildElementOptionalIntegerValue(child_element, "DECODING-CORRECTION")) \
                      .setDelayCompensationA(self.getChildElementOptionalIntegerValue(child_element, "DELAY-COMPENSATION-A")) \
                      .setDelayCompensationB(self.getChildElementOptionalIntegerValue(child_element, "DELAY-COMPENSATION-B")) \
                      .setKeySlotOnlyEnabled(self.getChildElementOptionalBooleanValue(child_element, "KEY-SLOT-ONLY-ENABLED")) \
                      .setKeySlotUsedForStartUp(self.getChildElementOptionalBooleanValue(child_element, "KEY-SLOT-USED-FOR-START-UP")) \
                      .setKeySlotUsedForSync(self.getChildElementOptionalBooleanValue(child_element, "KEY-SLOT-USED-FOR-SYNC")) \
                      .setLatestTX(self.getChildElementOptionalIntegerValue(child_element, "LATEST-TX")) \
                      .setListenTimeout(self.getChildElementOptionalIntegerValue(child_element, "LISTEN-TIMEOUT")) \
                      .setMacroInitialOffsetA(self.getChildElementOptionalIntegerValue(child_element, "MACRO-INITIAL-OFFSET-A")) \
                      .setMacroInitialOffsetB(self.getChildElementOptionalIntegerValue(child_element, "MACRO-INITIAL-OFFSET-B")) \
                      .setMaximumDynamicPayloadLength(self.getChildElementOptionalIntegerValue(child_element, "MAXIMUM-DYNAMIC-PAYLOAD-LENGTH")) \
                      .setMicroInitialOffsetA(self.getChildElementOptionalIntegerValue(child_element, "MICRO-INITIAL-OFFSET-A")) \
                      .setMicroInitialOffsetB(self.getChildElementOptionalIntegerValue(child_element, "MICRO-INITIAL-OFFSET-B")) \
                      .setMicroPerCycle(self.getChildElementOptionalIntegerValue(child_element, "MICRO-PER-CYCLE")) \
                      .setMicrotickDuration(self.getChildElementOptionalTimeValue(child_element, "MICROTICK-DURATION")) \
                      .setOffsetCorrectionOut(self.getChildElementOptionalIntegerValue(child_element, "OFFSET-CORRECTION-OUT")) \
                      .setRateCorrectionOut(self.getChildElementOptionalIntegerValue(child_element, "RATE-CORRECTION-OUT")) \
                      .setSamplesPerMicrotick(self.getChildElementOptionalIntegerValue(child_element, "SAMPLES-PER-MICROTICK")) \
                      .setWakeUpPattern(self.getChildElementOptionalIntegerValue(child_element, "WAKE-UP-PATTERN"))

    def readDataTransformationTransformerChainRefs(self, element: ET.Element, dtf: DataTransformation):
        for ref in self.getChildElementRefTypeList(element, "TRANSFORMER-CHAIN-REFS/TRANSFORMER-CHAIN-REF"):
            dtf.addTransformerChainRef(ref)

    def readDataTransformation(self, element: ET.Element, dtf: DataTransformation):
        self.readIdentifiable(element, dtf)
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

    def readBufferPropertiesBufferComputation(self, element: ET.Element, properties: BufferProperties):
        child_element = self.find(element, "BUFFER-COMPUTATION")
        if child_element is not None:
            scale = CompuScale()
            self.readCompuScale(child_element, scale)
            properties.setBufferComputation(scale)

    def getBufferProperties(self, element: ET.Element, key: str) -> BufferProperties:
        properties = None
        child_element = self.find(element, key)
        if child_element is not None:
            properties = BufferProperties()
            self.readBufferPropertiesBufferComputation(child_element, properties)
            properties.setHeaderLength(self.getChildElementOptionalIntegerValue(child_element, "HEADER-LENGTH")) \
                      .setInPlace(self.getChildElementOptionalBooleanValue(child_element, "IN-PLACE"))
        return properties
    
    def readDescribable(self, element: ET.Element, desc: Describable):
        self.readARObjectAttributes(element, desc)
    
    def readTransformationDescription(self, element: ET.Element, desc: TransformationDescription):
        self.readDescribable(element, desc)
    
    def readEndToEndTransformationDescription(self, element: ET.Element, desc: EndToEndTransformationDescription):
        self.readTransformationDescription(element, desc)
        desc.setDataIdMode(self.getChildElementOptionalLiteral(element, "DATA-ID-MODE")) \
            .setMaxDeltaCounter(self.getChildElementOptionalPositiveInteger(element, "MAX-DELTA-COUNTER")) \
            .setMaxErrorStateInit(self.getChildElementOptionalPositiveInteger(element, "MAX-ERROR-STATE-INIT")) \
            .setMaxErrorStateInvalid(self.getChildElementOptionalPositiveInteger(element, "MAX-ERROR-STATE-INVALID")) \
            .setMaxErrorStateValid(self.getChildElementOptionalPositiveInteger(element, "MAX-ERROR-STATE-VALID")) \
            .setMaxNoNewOrRepeatedData(self.getChildElementOptionalPositiveInteger(element, "MAX-NO-NEW-OR-REPEATED-DATA")) \
            .setMinOkStateInit(self.getChildElementOptionalPositiveInteger(element, "MIN-OK-STATE-INIT")) \
            .setMinOkStateInvalid(self.getChildElementOptionalPositiveInteger(element, "MIN-OK-STATE-INVALID")) \
            .setMinOkStateValid(self.getChildElementOptionalPositiveInteger(element, "MIN-OK-STATE-VALID")) \
            .setProfileBehavior(self.getChildElementOptionalLiteral(element, "PROFILE-BEHAVIOR")) \
            .setProfileName(self.getChildElementOptionalLiteral(element, "PROFILE-NAME")) \
            .setSyncCounterInit(self.getChildElementOptionalPositiveInteger(element, "SYNC-COUNTER-INIT")) \
            .setUpperHeaderBitsToShift(self.getChildElementOptionalPositiveInteger(element, "UPPER-HEADER-BITS-TO-SHIFT")) \
            .setWindowSizeInit(self.getChildElementOptionalPositiveInteger(element, "WINDOW-SIZE-INIT")) \
            .setWindowSizeInvalid(self.getChildElementOptionalPositiveInteger(element, "WINDOW-SIZE-INVALID")) \
            .setWindowSizeValid(self.getChildElementOptionalPositiveInteger(element, "WINDOW-SIZE-VALID"))

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
        tech.setBufferProperties(self.getBufferProperties(element, "BUFFER-PROPERTIES")) \
            .setNeedsOriginalData(self.getChildElementOptionalBooleanValue(element, "NEEDS-ORIGINAL-DATA")) \
            .setProtocol(self.getChildElementOptionalLiteral(element, "PROTOCOL"))
        self.readTransformationTechnologyTransformationDescriptions(element, tech)
        tech.setTransformerClass(self.getChildElementOptionalLiteral(element, "TRANSFORMER-CLASS")) \
            .setVersion(self.getChildElementOptionalLiteral(element, "VERSION"))

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

    def readCollectionElementRefs(self, element: ET.Element, collection: Collection):
        for ref in self.getChildElementRefTypeList(element, "ELEMENT-REFS/ELEMENT-REF"):
            collection.addElementRef(ref)

    def readCollectionSourceElementRefs(self, element: ET.Element, collection: Collection):
        for ref in self.getChildElementRefTypeList(element, "SOURCE-ELEMENT-REFS/SOURCE-ELEMENT-REF"):
            collection.addSourceElementRef(ref)

    def readCollection(self, element: ET.Element, collection: Collection):
        self.logger.debug("Read Collection <%s>" % collection.getShortName())
        self.readARElement(element, collection)
        collection.setAutoCollect(self.getChildElementOptionalLiteral(element, "AUTO-COLLECT")) \
                  .setElementRole(self.getChildElementOptionalLiteral(element, "ELEMENT-ROLE"))
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

    def readPortPrototypeBlueprint(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readPortPrototypeBlueprint(*args, **kwargs)


    def readModeDeclarationMappingFirstModeRefs(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readModeDeclarationMappingFirstModeRefs(*args, **kwargs)


    def readModeDeclarationMapping(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readModeDeclarationMapping(*args, **kwargs)


    def readModeDeclarationMappingSetModeDeclarationMappings(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readModeDeclarationMappingSetModeDeclarationMappings(*args, **kwargs)


    def readModeDeclarationMappingSet(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readModeDeclarationMappingSet(*args, **kwargs)


    def readEcucDefinitionElement(self, element: ET.Element, def_element: EcucDefinitionElement):
        self.readIdentifiable(element, def_element)
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
        for cfg_class in self.getEcucMultiplicityConfigurationClasses(element):
            container_def.addMultiplicityConfigClass(cfg_class)
        container_def.setPostBuildVariantMultiplicity(self.getChildElementOptionalBooleanValue(element, "POST-BUILD-VARIANT-MULTIPLICITY"))
        container_def.setRequiresIndex(self.getChildElementOptionalBooleanValue(element, "REQUIRES-INDEX"))
        container_def.setMultipleConfigurationContainer(self.getChildElementOptionalBooleanValue(element, "MULTIPLE-CONFIGURATION-CONTAINER"))

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
        param_def.setDerivation(self.getChildElementOptionalLiteral(element, "DERIVATION"))
        param_def.setSymbolicNameValue(self.getChildElementOptionalBooleanValue(element, "SYMBOLIC-NAME-VALUE"))
        param_def.setWithAuto(self.getChildElementOptionalBooleanValue(element, "WITH-AUTO"))
        
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
        self.readEcucAbstractStringParamDef(element, param_def)

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
        self.readEcucAbstractStringParamDef(element, ref_def)
        child_element = self.find(element, "ECUC-FUNCTION-NAME-DEF-VARIANTS/ECUC-FUNCTION-NAME-DEF-CONDITIONAL")
        if child_element is not None:
            ref_def.setDefaultValue(self.getChildElementOptionalLiteral(child_element, "DEFAULT-VALUE"))
            ref_def.setMinLength(self.getChildElementOptionalIntegerValue(child_element, "MIN-LENGTH"))
            ref_def.setMaxLength(self.getChildElementOptionalIntegerValue(child_element, "MAX-LENGTH"))

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
            else:
                self.notImplemented("Unsupported Parameter <%s>" % tag_name)

    def readEcucAbstractReferenceDef(self, element: ET.Element, ref_def: EcucAbstractReferenceDef):
        self.readEcucCommonAttributes(element, ref_def)
        ref_def.setWithAuto(self.getChildElementOptionalBooleanValue(element, "WITH-AUTO"))

    def readEcucAbstractInternalReferenceDef(self, element: ET.Element, ref_def: EcucAbstractInternalReferenceDef):
        self.readEcucAbstractReferenceDef(element, ref_def)

    def readEcucSymbolicNameReferenceDef(self, element: ET.Element, ref_def: EcucSymbolicNameReferenceDef):
        self.readEcucAbstractInternalReferenceDef(element, ref_def)
        ref_def.setDestinationRef(self.getChildElementOptionalRefType(element, "DESTINATION-REF"))

    def readEcucReferenceDef(self, element: ET.Element, ref_def: EcucReferenceDef):
        self.readEcucAbstractInternalReferenceDef(element, ref_def)
        ref_def.setDestinationRef(self.getChildElementOptionalRefType(element, "DESTINATION-REF"))

    def readEcucContainerDefReferences(self, element: ET.Element, container_def: EcucParamConfContainerDef):
        for child_element in self.findall(element, "REFERENCES/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "ECUC-SYMBOLIC-NAME-REFERENCE-DEF":
                ref_def = container_def.createEcucSymbolicNameReferenceDef(self.getShortName(child_element))
                self.readEcucSymbolicNameReferenceDef(child_element, ref_def)
            elif tag_name == "ECUC-REFERENCE-DEF":
                ref_def = container_def.createEcucReferenceDef(self.getShortName(child_element))
                self.readEcucReferenceDef(child_element, ref_def)
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
        module_def.setPostBuildVariantSupport(self.getChildElementOptionalBooleanValue(element, "POST-BUILD-VARIANT-SUPPORT"))
        self.readEcucModuleDefSupportedConfigVariants(element, module_def)
        self.readEcucModuleDefContainers(element, module_def)

    def readCommunicationController(self, element: ET.Element, controller: CommunicationController):
        controller.setWakeUpByControllerSupported(self.getChildElementOptionalBooleanValue(element, "WAKE-UP-BY-CONTROLLER-SUPPORTED"))

    def getCanControllerFdConfiguration(self, element: ET.Element, key: str) -> CanControllerFdConfiguration:
        configuration = None
        child_element = self.find(element, key)
        if child_element is not None:
            configuration = CanControllerFdConfiguration()
            # TODO: need to implemented
        return configuration
    
    def getCanControllerFdConfigurationRequirements(self, element: ET.Element, key: str) -> CanControllerFdConfigurationRequirements:
        requirements = None
        child_element = self.find(element, key)
        if child_element is not None:
            requirements = CanControllerFdConfigurationRequirements()
            requirements.setMaxNumberOfTimeQuantaPerBit(self.getChildElementOptionalIntegerValue(child_element, "MAX-NUMBER-OF-TIME-QUANTA-PER-BIT")) \
                        .setMaxSamplePoint(self.getChildElementOptionalFloatValue(child_element, "MAX-SAMPLE-POINT")) \
                        .setMaxSyncJumpWidth(self.getChildElementOptionalFloatValue(child_element, "MAX-SYNC-JUMP-WIDTH")) \
                        .setMaxTrcvDelayCompensationOffset(self.getChildElementOptionalTimeValue(child_element, "MAX-TRCV-DELAY-COMPENSATION-OFFSET")) \
                        .setMinNumberOfTimeQuantaPerBit(self.getChildElementOptionalIntegerValue(child_element, "MIN-NUMBER-OF-TIME-QUANTA-PER-BIT")) \
                        .setMinSamplePoint(self.getChildElementOptionalFloatValue(child_element, "MIN-SAMPLE-POINT")) \
                        .setMinSyncJumpWidth(self.getChildElementOptionalFloatValue(child_element, "MIN-SYNC-JUMP-WIDTH")) \
                        .setMinTrcvDelayCompensationOffset(self.getChildElementOptionalTimeValue(child_element, "MIN-TRCV-DELAY-COMPENSATION-OFFSET")) \
                        .setTxBitRateSwitch(self.getChildElementOptionalBooleanValue(child_element, "TX-BIT-RATE-SWITCH"))      # NOQA E501
        return requirements

    def readAbstractCanCommunicationControllerAttributes(self, element: ET.Element, attributes: AbstractCanCommunicationControllerAttributes):
        attributes.setCanControllerFdAttributes(self.getCanControllerFdConfiguration(element, "CAN-CONTROLLER-FD-CONFIGURATION")) \
                  .setCanControllerFdRequirements(self.getCanControllerFdConfigurationRequirements(element, "CAN-CONTROLLER-FD-REQUIREMENTS"))

    def readCanControllerConfigurationRequirements(self, element: ET.Element, requirements: CanControllerConfigurationRequirements):
        self.readAbstractCanCommunicationControllerAttributes(element, requirements)
        requirements.setMaxNumberOfTimeQuantaPerBit(self.getChildElementOptionalIntegerValue(element, "MAX-NUMBER-OF-TIME-QUANTA-PER-BIT")) \
                    .setMaxSamplePoint(self.getChildElementOptionalFloatValue(element, "MAX-SAMPLE-POINT")) \
                    .setMaxSyncJumpWidth(self.getChildElementOptionalFloatValue(element, "MAX-SYNC-JUMP-WIDTH")) \
                    .setMinNumberOfTimeQuantaPerBit(self.getChildElementOptionalIntegerValue(element, "MIN-NUMBER-OF-TIME-QUANTA-PER-BIT")) \
                    .setMinSamplePoint(self.getChildElementOptionalFloatValue(element, "MIN-SAMPLE-POINT")) \
                    .setMinSyncJumpWidth(self.getChildElementOptionalFloatValue(element, "MIN-SYNC-JUMP-WIDTH"))

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

    def readCouplingPortSchedulerCouplingPortStructuralElement(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readCouplingPortSchedulerCouplingPortStructuralElement(*args, **kwargs)


    def readCouplingPortFifo(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readCouplingPortFifo(*args, **kwargs)


    def readCouplingPortScheduler(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readCouplingPortScheduler(*args, **kwargs)


    def readCouplingPortDetailsCouplingPortStructuralElements(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readCouplingPortDetailsCouplingPortStructuralElements(*args, **kwargs)


    def readEthernetPriorityRegeneration(self, element: ET.Element, regeneration: EthernetPriorityRegeneration):
        regeneration.setIngressPriority(self.getChildElementOptionalPositiveInteger(element, "INGRESS-PRIORITY")) \
                    .setRegeneratedPriority(self.getChildElementOptionalPositiveInteger(element, "REGENERATED-PRIORITY"))

    def readCouplingPortDetailsEthernetPriorityRegenerations(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readCouplingPortDetailsEthernetPriorityRegenerations(*args, **kwargs)


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
        membership.setSendActivity(self.getChildElementOptionalLiteral(element, "SEND-ACTIVITY")) \
                  .setVlanRef(self.getChildElementOptionalRefType(element, "VLAN-REF"))
    
    def readCouplingPortVlanMemberships(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readCouplingPortVlanMemberships(*args, **kwargs)


    def readCouplingPort(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readCouplingPort(*args, **kwargs)


    def readEthernetCommunicationControllerCouplingPorts(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readEthernetCommunicationControllerCouplingPorts(*args, **kwargs)


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
            controller.setTimeBase(self.getChildElementOptionalTimeValue(child_element, "TIME-BASE")) \
                      .setTimeBaseJitter(self.getChildElementOptionalTimeValue(child_element, "TIME-BASE-JITTER"))

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

    def readCommConnectorPort(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readCommConnectorPort(*args, **kwargs)


    def readFramePort(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readFramePort(*args, **kwargs)


    def readIPduPort(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readIPduPort(*args, **kwargs)


    def readISignalPort(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readISignalPort(*args, **kwargs)


    def readCommunicationConnectorEcuCommPortInstances(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readCommunicationConnectorEcuCommPortInstances(*args, **kwargs)


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

    def readEcuInstance(self, element: ET.Element, instance: EcuInstance):
        self.logger.debug("Read EcuInstance <%s>" % instance.getShortName())
        self.readIdentifiable(element, instance)
        self.readEcuInstanceAssociatedComIPduGroupRefs(element, instance)
        instance.setComConfigurationGwTimeBase(self.getChildElementOptionalTimeValue(element, "COM-CONFIGURATION-GW-TIME-BASE")) \
                .setComConfigurationRxTimeBase(self.getChildElementOptionalTimeValue(element, "COM-CONFIGURATION-RX-TIME-BASE")) \
                .setComConfigurationTxTimeBase(self.getChildElementOptionalTimeValue(element, "COM-CONFIGURATION-TX-TIME-BASE")) \
                .setComEnableMDTForCyclicTransmission(self.getChildElementOptionalBooleanValue(element, "COM-ENABLE-MDT-FOR-CYCLIC-TRANSMISSION"))
        self.readEcuInstanceCommControllers(element, instance)
        self.readEcuInstanceConnectors(element, instance)
        instance.setDiagnosticAddress(self.getChildElementOptionalIntegerValue(element, "DIAGNOSTIC-ADDRESS")) \
                .setSleepModeSupported(self.getChildElementOptionalBooleanValue(element, "SLEEP-MODE-SUPPORTED")) \
                .setWakeUpOverBusSupported(self.getChildElementOptionalBooleanValue(element, "WAKE-UP-OVER-BUS-SUPPORTED"))

    '''
    def getFrameMappings(self, element: ET.Element) -> List[FrameMapping]:
        mappings = []
        for child_element in self.findall(element, 'FRAME-MAPPINGS/'):
            mapping = FrameMapping()
            mapping.sourceFrameRef = self.getChildElementOptionalRefType(child_element, "SOURCE-FRAME-REF")
            mapping.targetFrameRef = self.getChildElementOptionalRefType(child_element, "TARGET-FRAME-REF")
            mappings.append(mapping)
        return mappings
    '''

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
            mapping.setSourceIpduRef(self.getChildElementOptionalRefType(child_element, "SOURCE-I-PDU-REF")) \
                   .setTargetIPdu(self.getTargetIPduRef(child_element, "TARGET-I-PDU"))
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
        signal.setDataTypePolicy(self.getChildElementOptionalLiteral(element, "DATA-TYPE-POLICY")) \
              .setISignalType(self.getChildElementOptionalLiteral(element, "I-SIGNAL-TYPE")) \
              .setInitValue(self.getInitValue(element)) \
              .setLength(self.getChildElementOptionalNumericalValue(element, "LENGTH")) \
              .setNetworkRepresentationProps(self.getSwDataDefProps(element, "NETWORK-REPRESENTATION-PROPS")) \
              .setSystemSignalRef(self.getChildElementOptionalRefType(element, "SYSTEM-SIGNAL-REF"))

    def readEcucValueCollectionEcucValues(self, element: ET.Element, parent: EcucValueCollection):
        for child_element in self.findall(element, "ECUC-VALUES/ECUC-MODULE-CONFIGURATION-VALUES-REF-CONDITIONAL"):
            ref = self.getChildElementOptionalRefType(child_element, "ECUC-MODULE-CONFIGURATION-VALUES-REF")
            if (ref is not None):
                parent.addEcucValueRef(ref)
            self.logger.debug("EcucValue <%s> of EcucValueCollection <%s> has been added", ref.value, parent.getShortName())

    def readEcucValueCollection(self, element: ET.Element, collection: EcucValueCollection):
        self.logger.debug("Read EcucValueCollection <%s>" % collection.getShortName())
        self.readIdentifiable(element, collection)
        collection.setEcuExtractRef(self.getChildElementOptionalRefType(element, "ECU-EXTRACT-REF"))
        self.readEcucValueCollectionEcucValues(element, collection)

    def readEcucParameterValue(self, element: ET.Element, param_value: EcucParameterValue):
        param_value.setDefinitionRef(self.getChildElementOptionalRefType(element, "DEFINITION-REF"))
        for annotation in self.getAnnotations(element):
            param_value.addAnnotation(annotation)

    def getEcucTextualParamValue(self, element: ET.Element) -> EcucTextualParamValue:
        param_value = EcucTextualParamValue()
        self.readEcucParameterValue(element, param_value)
        param_value.setValue(self.getChildElementOptionalLiteral(element, "VALUE"))
        return param_value

    def getEcucNumericalParamValue(self, element: ET.Element) -> EcucNumericalParamValue:
        param_value = EcucNumericalParamValue()
        self.readEcucParameterValue(element, param_value)
        param_value.setValue(self.getChildElementOptionalNumericalValue(element, "VALUE"))
        return param_value

    def readEcucContainerValueParameterValues(self, element: ET.Element, container_value: EcucContainerValue):
        for child_element in self.findall(element, "PARAMETER-VALUES/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "ECUC-TEXTUAL-PARAM-VALUE":
                container_value.addParameterValue(self.getEcucTextualParamValue(child_element))
            elif tag_name == "ECUC-NUMERICAL-PARAM-VALUE":
                container_value.addParameterValue(self.getEcucNumericalParamValue(child_element))
            else:
                self.notImplemented("Unsupported EcucParameterValue <%s>" % tag_name)
            
    def readEcucAbstractReferenceValue(self, element: ET.Element, value: EcucAbstractReferenceValue):
        value.setDefinitionRef(self.getChildElementOptionalRefType(element, "DEFINITION-REF"))
        for annotation in self.getAnnotations(element):
            value.addAnnotation(annotation)

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
        values.setDefinitionRef(self.getChildElementOptionalRefType(element, "DEFINITION-REF"))
        values.setImplementationConfigVariant(self.getChildElementOptionalLiteral(element, "IMPLEMENTATION-CONFIG-VARIANT"))
        values.setModuleDescriptionRef(self.getChildElementOptionalRefType(element, "MODULE-DESCRIPTION-REF"))
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
        for ref in self.getChildElementRefTypeList(element, "COM-BASED-SIGNAL-GROUP-TRANSFORMATIONS/DATA-TRANSFORMATION-REF-CONDITIONAL/DATA-TRANSFORMATION-REF"):      # noqa E501
            group.addComBasedSignalGroupTransformationRef(ref)

    def readTransformationISignalProps(self, element: ET.Element, props: TransformationISignalProps):
        self.readDescribable(element, props)

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
                group.setTransformationISignalProps(props)
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
        signal.setDynamicLength(self.getChildElementOptionalBooleanValue(element, "DYNAMIC-LENGTH")) \
              .setPhysicalProps(self.getSwDataDefProps(element, "PHYSICAL-PROPS"))

    def readSystemSignalGroup(self, element: ET.Element, group: SystemSignalGroup):
        self.logger.debug("Read SystemSignalGroup <%s>" % group.getShortName())
        self.readIdentifiable(element, group)
        for ref_type in self.getChildElementRefTypeList(element, "SYSTEM-SIGNAL-REFS/SYSTEM-SIGNAL-REF"):
            group.addSystemSignalRefs(ref_type)

    def readISignalToPduMappings(self, element: ET.Element, parent: ISignalIPdu):
        for child_element in self.findall(element, "I-SIGNAL-TO-PDU-MAPPINGS/I-SIGNAL-TO-I-PDU-MAPPING"):
            short_name = self.getShortName(child_element)
            mapping = parent.createISignalToPduMappings(short_name)
            self.readIdentifiable(child_element, mapping)
            mapping.setISignalRef(self.getChildElementOptionalRefType(child_element, "I-SIGNAL-REF")) \
                   .setISignalGroupRef(self.getChildElementOptionalRefType(child_element, "I-SIGNAL-GROUP-REF")) \
                   .setPackingByteOrder(self.getChildElementOptionalLiteral(child_element, "PACKING-BYTE-ORDER")) \
                   .setStartPosition(self.getChildElementOptionalNumericalValue(child_element, "START-POSITION")) \
                   .setTransferProperty(self.getChildElementOptionalLiteral(child_element, "TRANSFER-PROPERTY")) \
                   .setUpdateIndicationBitPosition(self.getChildElementOptionalNumericalValue(child_element, "UPDATE-INDICATION-BIT-POSITION"))
    
    def getDataFilter(self, element: ET.Element, key: str) -> DataFilter:
        filter = None
        child_element = self.find(element, key)
        if child_element is not None:
            filter = DataFilter()
            filter.setDataFilterType(self.getChildElementOptionalLiteral(child_element, "DATA-FILTER-TYPE")) \
                  .setMask(self.getChildElementOptionalIntegerValue(child_element, "MASK")) \
                  .setX(self.getChildElementOptionalIntegerValue(child_element, "X"))

        return filter
            
    def getTransmissionModeConditions(self, element: ET.Element, key: str) -> List[TransmissionModeCondition]:
        result = []
        child_elements = self.findall(element, key)
        for child_element in child_elements:
            condition = TransmissionModeCondition()
            condition.setDataFilter(self.getDataFilter(child_element, "DATA-FILTER")) \
                     .setISignalInIPduRef(self.getChildElementOptionalRefType(child_element, "I-SIGNAL-IN-I-PDU-REF"))
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
            timing.setTimeOffset(self.getTimeRangeType(child_element, "TIME-OFFSET")) \
                  .setTimePeriod(self.getTimeRangeType(child_element, "TIME-PERIOD"))
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
            timing.setCyclicTiming(self.getCyclicTiming(child_element, "CYCLIC-TIMING")) \
                  .setEventControlledTiming(self.getEventControlledTiming(child_element, "EVENT-CONTROLLED-TIMING"))
        return timing

    def getTransmissionModeDeclaration(self, element: ET.Element, key: str) -> TransmissionModeDeclaration:
        decl = None
        child_element = self.find(element, key)
        if child_element is not None:
            decl = TransmissionModeDeclaration()
            for condition in self.getTransmissionModeConditions(child_element, "TRANSMISSION-MODE-CONDITIONS/TRANSMISSION-MODE-CONDITION"):
                decl.addTransmissionModeCondition(condition)
            decl.setTransmissionModeFalseTiming(self.getTransmissionModeTiming(child_element, "TRANSMISSION-MODE-FALSE-TIMING")) \
                .setTransmissionModeTrueTiming(self.getTransmissionModeTiming(child_element, "TRANSMISSION-MODE-TRUE-TIMING"))
        return decl

    def getISignalIPduIPduTimingSpecification(self, element: ET.Element) -> IPduTiming:
        timing = None
        child_element = self.find(element, "I-PDU-TIMING-SPECIFICATIONS/I-PDU-TIMING")
        if child_element is not None:
            timing = IPduTiming()
            timing.setMinimumDelay(self.getChildElementOptionalTimeValue(child_element, "MINIMUM-DELAY")) \
                  .setTransmissionModeDeclaration(self.getTransmissionModeDeclaration(child_element, "TRANSMISSION-MODE-DECLARATION"))
        return timing

    def readISignalIPdu(self, element: ET.Element, ipdu: ISignalIPdu):
        self.logger.debug("Read ISignalIPdu <%s>" % ipdu.getShortName())
        self.readIdentifiable(element, ipdu)
        ipdu.setLength(self.getChildElementOptionalNumericalValue(element, "LENGTH")) \
            .setIPduTimingSpecification(self.getISignalIPduIPduTimingSpecification(element))
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
        group.setCommunicationDirection(self.getChildElementOptionalLiteral(element, "COMMUNICATION-DIRECTION")) \
             .setCommunicationMode(self.getChildElementOptionalLiteral(element, "COMMUNICATION-MODE"))
        for ref_type in self.getChildElementRefTypeList(element, "CONTAINED-I-SIGNAL-I-PDU-GROUP-REFS/CONTAINED-I-SIGNAL-I-PDU-GROUP-REF"):
            group.addContainedISignalIPduGroupRef(ref_type)
        for ref_type in self.getISignalIPduRefs(element):
            group.addISignalIPduRef(ref_type)

    def readSenderReceiverToSignalMapping(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readSenderReceiverToSignalMapping(*args, **kwargs)


    def readSenderRecCompositeTypeMapping(self, element: ET.Element, mapping: SenderRecCompositeTypeMapping):
        self.readARObjectAttributes(element, mapping)

    def readSenderRecRecordElementMapping(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readSenderRecRecordElementMapping(*args, **kwargs)


    def readSenderRecArrayTypeMappingRecordElementMapping(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readSenderRecArrayTypeMappingRecordElementMapping(*args, **kwargs)


    def readSenderRecRecordTypeMapping(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readSenderRecRecordTypeMapping(*args, **kwargs)


    def readSenderReceiverToSignalGroupMappingTypeMapping(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readSenderReceiverToSignalGroupMappingTypeMapping(*args, **kwargs)


    def readSenderReceiverToSignalGroupMapping(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readSenderReceiverToSignalGroupMapping(*args, **kwargs)


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
        mapping.setEcuInstanceRef(self.getChildElementOptionalRefType(element, "ECU-INSTANCE-REF")) \
               .setEcuRef(self.getChildElementOptionalRefType(element, "ECU-REF"))

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
            prototype.setFlatMapRef(self.getChildElementOptionalRefType(child_element, "FLAT-MAP-REF")) \
                     .setSoftwareCompositionTRef(self.getChildElementOptionalRefType(child_element, "SOFTWARE-COMPOSITION-TREF"))
            try:
                AUTOSAR.getInstance().setRootSwCompositionPrototype(prototype)
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
        AUTOSAR.getInstance().addSystem(system)

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
        info.setLcObjectRef(self.getChildElementOptionalRefType(element, "LC-OBJECT-REF")) \
            .setLcStateRef(self.getChildElementOptionalRefType(element, "LC-STATE-REF")) \
            .setPeriodBegin(self.getLifeCyclePeriod(element, "PERIOD-BEGIN")) \
            .setRemark(self.getDocumentationBlock(element, "REMARK"))
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
        desc.setUpstreamReferenceIRef(self.getAnyInstanceRef(element, "UPSTREAM-REFERENCE-IREF")) \
            .setEcuExtractReferenceIRef(self.getAnyInstanceRef(element, "ECU-EXTRACT-REFERENCE-IREF"))

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
            mapping.setFirstDataPrototypeRef(self.getChildElementOptionalRefType(child_element, "FIRST-DATA-PROTOTYPE-REF")) \
                   .setSecondDataPrototypeRef(self.getChildElementOptionalRefType(child_element, "SECOND-DATA-PROTOTYPE-REF"))
            mappings.append(mapping)
        return mappings

    def readVariableAndParameterInterfaceMapping(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readVariableAndParameterInterfaceMapping(*args, **kwargs)


    def readClientServerOperationMapping(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readClientServerOperationMapping(*args, **kwargs)


    def readClientServerInterfaceMappingOperationMappings(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readClientServerInterfaceMappingOperationMappings(*args, **kwargs)


    def readClientServerInterfaceMapping(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readClientServerInterfaceMapping(*args, **kwargs)


    def readModeInterfaceMappingModeMapping(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readModeInterfaceMappingModeMapping(*args, **kwargs)


    def readModeInterfaceMapping(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readModeInterfaceMapping(*args, **kwargs)


    def readPortInterfaceMappings(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readPortInterfaceMappings(*args, **kwargs)


    def readPortInterfaceMappingSet(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readPortInterfaceMappingSet(*args, **kwargs)


    def readARPackageElements(self, element: ET.Element, parent: ARPackage):
        for child_element in self.findall(element, "ELEMENTS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "COMPOSITION-SW-COMPONENT-TYPE":
                type = parent.createCompositionSwComponentType(self.getShortName(child_element))
                self.readCompositionSwComponentType(child_element, type)
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
            else:
                self.notImplemented("Unsupported Element type of ARPackage <%s>" % tag_name)

    def readReferenceBases(self, element: ET.Element, parent: ARPackage):
        for child_element in self.findall(element, "REFERENCE-BASES/REFERENCE-BASE"):
            base = ReferenceBase()
            base.setShortLabel(self.getChildElementOptionalLiteral(child_element, "SHORT-LABEL")) \
                .setIsDefault(self.getChildElementOptionalBooleanValue(child_element, "IS-DEFAULT")) \
                .setIsGlobal(self.getChildElementOptionalBooleanValue(child_element, "IS-GLOBAL")) \
                .setBaseIsThisPackage(self.getChildElementOptionalBooleanValue(child_element, "BASE-IS-THIS-PACKAGE")) \
                .setPackageRef(self.getChildElementOptionalRefType(child_element, "PACKAGE-REF"))
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
        if (self.getPureTagName(root.tag) != "AUTOSAR"):
            self.raiseError("Invalid ARXML file <%s>" % filename)

        self.getAUTOSARInfo(root, document)
        document.setAdminData(self.getAdminData(root, "ADMIN-DATA"))
        self.readARPackages(root, document)

        document.reload()
