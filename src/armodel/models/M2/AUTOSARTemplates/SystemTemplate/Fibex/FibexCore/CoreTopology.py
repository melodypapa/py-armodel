from abc import ABC
from enum import Enum
from typing import TYPE_CHECKING, List

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Flexray.FlexrayCommunication import FlexrayFrameTriggering
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Filter import DataFilter
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AREnum, Boolean, Integer, PositiveInteger
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveUnlimitedInteger, RefType, TimeValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanCommunication import CanFrameTriggering
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication import LinFrameTriggering, LinScheduleTable
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.NetworkEndpoint import NetworkEndpoint
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import FibexElement, FrameTriggering, ISignalTriggering, PduTriggering

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import EthernetCommunicationConnector, EthernetCommunicationController
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology import CanCommunicationConnector, CanCommunicationController
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Flexray.FlexrayTopology import FlexrayCommunicationConnector, FlexrayCommunicationController
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinTopology import LinCommunicationConnector, LinMaster


class CommunicationCycle(ARObject, ABC):
    """
    Abstract base class for communication cycles, defining common
    properties for different types of communication timing cycles
    in the AUTOSAR communication system.
    """

    def __init__(self):
        if type(self) is CommunicationCycle:
            raise TypeError("CommunicationCycle is an abstract class.")
        super().__init__()


class CycleCounter(CommunicationCycle):
    """
    Defines a counter for communication cycles, specifying the
    count value for cycle tracking in timed communication systems.
    """
    def __init__(self):
        super().__init__()

        self.CycleCounter: Integer = None

    def getCycleCounter(self):
        return self.CycleCounter

    def setCycleCounter(self, value):
        if value is not None:
            self.CycleCounter = value
        return self


class CycleRepetitionType(AREnum):
    """
    Enumeration defining types of cycle repetitions in communication
    scheduling, specifying how communication cycles are repeated
    over time.
    """
    def __init__(self):
        super().__init__([])


class CycleRepetition(CommunicationCycle):
    """
    Defines repetition properties for communication cycles,
    specifying base cycle and repetition pattern for cyclic
    communication scheduling.
    """
    def __init__(self):
        super().__init__()

        self.BaseCycle: Integer = None
        self.CycleRepetition: CycleRepetitionType = None

    def getBaseCycle(self):
        return self.BaseCycle

    def setBaseCycle(self, value):
        if value is not None:
            self.BaseCycle = value
        return self

    def getCycleRepetition(self):
        return self.CycleRepetition

    def setCycleRepetition(self, value):
        if value is not None:
            self.CycleRepetition = value
        return self


class PhysicalChannel (Identifiable, ABC):
    """
    Abstract base class for physical communication channels,
    defining common properties for different types of physical
    communication media including connector references and
    frame triggering mechanisms.
    """
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is PhysicalChannel:
            raise TypeError("PhysicalChannel is an abstract class.")
        
        super().__init__(parent, short_name)

        self.commConnectorRefs: List[RefType] = []
        self.frameTriggerings: List[FrameTriggering] = []
        self.managedPhysicalChannelRefs: List[RefType] = []

    def getCommConnectorRefs(self):
        return self.commConnectorRefs

    def addCommConnectorRef(self, value):
        self.commConnectorRefs.append(value)
        return self

    def getFrameTriggerings(self) -> List[FrameTriggering]:
        return list(sorted(filter(lambda a: isinstance(a, FrameTriggering), self.elements), key=lambda o: o.getShortName()))

    def createCanFrameTriggering(self, short_name: str) -> CanFrameTriggering:
        if (short_name not in self.elements):
            triggering = CanFrameTriggering(self, short_name)
            self.addElement(triggering)
            self.frameTriggerings.append(triggering)
        return self.getElement(short_name)
    
    def createLinFrameTriggering(self, short_name: str) -> LinFrameTriggering:
        if (short_name not in self.elements):
            triggering = LinFrameTriggering(self, short_name)
            self.addElement(triggering)
            self.frameTriggerings.append(triggering)
        return self.getElement(short_name)
    
    def createFlexrayFrameTriggering(self, short_name: str) -> FlexrayFrameTriggering:
        if (short_name not in self.elements):
            triggering = FlexrayFrameTriggering(self, short_name)
            self.addElement(triggering)
            self.frameTriggerings.append(triggering)
        return self.getElement(short_name)

    def getISignalTriggerings(self) -> List[ISignalTriggering]:
        return list(sorted(filter(lambda a: isinstance(a, ISignalTriggering), self.elements), key=lambda o: o.getShortName()))

    def createISignalTriggering(self, short_name: str):
        if (short_name not in self.elements):
            triggering = ISignalTriggering(self, short_name)
            self.addElement(triggering)
        return self.getElement(short_name)

    def getManagedPhysicalChannelRefs(self):
        return self.managedPhysicalChannelRefs

    def addManagedPhysicalChannelRef(self, value):
        self.managedPhysicalChannelRefs.append(value)
        return self
    
    def getPduTriggerings(self) -> List[PduTriggering]:
        return list(sorted(filter(lambda a: isinstance(a, PduTriggering), self.elements), key=lambda o: o.getShortName()))

    def createPduTriggering(self, short_name: str):
        if (short_name not in self.elements):
            triggering = PduTriggering(self, short_name)
            self.addElement(triggering)
        return self.getElement(short_name)


class AbstractCanPhysicalChannel(PhysicalChannel, ABC):
    """
    Abstract base class for CAN physical channels, defining
    common properties for CAN-specific physical communication
    channels in the AUTOSAR system.
    """
    def __init__(self, parent, short_name):
        if type(self) is AbstractCanPhysicalChannel:
            raise TypeError("AbstractCanPhysicalChannel is an abstract class.")
         
        super().__init__(parent, short_name)


class CanPhysicalChannel(AbstractCanPhysicalChannel):
    """
    Represents a CAN physical channel in the communication system,
    implementing specific properties for CAN bus communication
    including frame triggering and connector management.
    """
    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)


class LinPhysicalChannel(PhysicalChannel):
    """
    Represents a LIN physical channel in the communication system,
    defining LIN-specific properties including bus idle timeout
    and schedule tables for LIN network communication.
    """
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.busIdleTimeoutPeriod: TimeValue = None
        self.scheduleTables: List[LinScheduleTable] = []

    def getBusIdleTimeoutPeriod(self):
        return self.busIdleTimeoutPeriod

    def setBusIdleTimeoutPeriod(self, value):
        if value is not None:
            self.busIdleTimeoutPeriod = value
        return self

    def getScheduleTables(self):
        return self.scheduleTables

    def createLinScheduleTable(self, short_name: str) -> LinScheduleTable:
        if (short_name not in self.elements):
            end_point = LinScheduleTable(self, short_name)
            self.addElement(end_point)
            self.scheduleTables.append(end_point)
        return self.getElement(short_name)


class VlanConfig(Identifiable):
    """
    Defines Virtual LAN (VLAN) configuration properties,
    specifying VLAN identifiers for network segmentation
    and traffic management in Ethernet communication.
    """
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.vlanIdentifier: PositiveInteger = None

    def getVlanIdentifier(self):
        return self.vlanIdentifier

    def setVlanIdentifier(self, value):
        if value is not None:
            self.vlanIdentifier = value
        return self


class EthernetPhysicalChannel(PhysicalChannel):
    """
    Represents an Ethernet physical channel in the communication system,
    defining Ethernet-specific properties including network endpoints,
    Socket Adaptor (SoAd) configuration, and VLAN settings.
    """
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.networkEndpoints: List[NetworkEndpoint] = []
        self.soAdConfig = None
        self.vlan: VlanConfig = None

    def getNetworkEndpoints(self):
        return self.networkEndpoints

    def createNetworkEndPoint(self, short_name: str) -> NetworkEndpoint:
        if (short_name not in self.elements):
            end_point = NetworkEndpoint(self, short_name)
            self.addElement(end_point)
            self.networkEndpoints.append(end_point)
        return self.getElement(short_name)

    def getSoAdConfig(self):
        return self.soAdConfig

    def setSoAdConfig(self, value):
        self.soAdConfig = value
        return self

    def getVlan(self):
        return self.vlan

    def createVlanConfig(self, short_name: str) -> VlanConfig:
        if (short_name not in self.elements):
            config = VlanConfig(self, short_name)
            self.vlan = config
            self.addElement(config)
        return self.getElement(short_name)


class FlexrayChannelName(AREnum):
    """
    Enumeration defining names for FlexRay channels,
    specifying the available channel designations
    in FlexRay communication systems.
    """
    CHANNEL_A = "channelA"
    channel_B = "channelB"

    def __init__(self):
        super().__init__([
            FlexrayChannelName.CHANNEL_A,
            FlexrayChannelName.channel_B
        ])


class FlexrayPhysicalChannel(PhysicalChannel):
    """
    Represents a FlexRay physical channel in the communication system,
    defining FlexRay-specific properties including channel name
    designation for dual-channel FlexRay communication.
    """
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.channelName = None                                     # type: FlexrayChannelName

    def getChannelName(self):
        return self.channelName

    def setChannelName(self, value):
        if value is not None:
            self.channelName = value
        return self


class CommunicationCluster(FibexElement, ABC):
    """
    Abstract base class for communication clusters, defining
    common properties for different types of communication
    networks including baud rate, protocol specifications,
    and physical channel management.
    """
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is CommunicationCluster:
            raise TypeError("CommunicationCluster is an abstract class.")
        
        super().__init__(parent, short_name)

        self.baudrate = None                    # type: ARFloat
        self.physicalChannel: List[PhysicalChannel] = []
        self.protocolName = None                # type: ARLiteral
        self.protocolVersion = None             # type: ARLiteral

    def getBaudrate(self):
        return self.baudrate

    def setBaudrate(self, value):
        self.baudrate = value
        return self

    def getPhysicalChannels(self) -> List[PhysicalChannel]:
        return list(sorted(filter(lambda a: isinstance(a, PhysicalChannel), self.elements), key=lambda o: o.getShortName()))
    
    def getCanPhysicalChannels(self) -> List[CanPhysicalChannel]:
        return list(sorted(filter(lambda a: isinstance(a, CanPhysicalChannel), self.elements), key=lambda o: o.getShortName()))
    
    def getLinPhysicalChannels(self) -> List[LinPhysicalChannel]:
        return list(sorted(filter(lambda a: isinstance(a, LinPhysicalChannel), self.elements), key=lambda o: o.getShortName()))
    
    def getEthernetPhysicalChannels(self) -> List[EthernetPhysicalChannel]:
        return list(sorted(filter(lambda a: isinstance(a, EthernetPhysicalChannel), self.elements), key=lambda o: o.getShortName()))
    
    def createCanPhysicalChannel(self, short_name: str):
        if (short_name not in self.elements):
            channel = CanPhysicalChannel(self, short_name)
            self.addElement(channel)
            self.physicalChannel.append(channel)
        return self.getElement(short_name)
    
    def createLinPhysicalChannel(self, short_name: str):
        if (short_name not in self.elements):
            channel = LinPhysicalChannel(self, short_name)
            self.addElement(channel)
            self.physicalChannel.append(channel)
        return self.getElement(short_name)
    
    def createEthernetPhysicalChannel(self, short_name: str):
        if (short_name not in self.elements):
            channel = EthernetPhysicalChannel(self, short_name)
            self.addElement(channel)
            self.physicalChannel.append(channel)
        return self.getElement(short_name)
    
    def createFlexrayPhysicalChannel(self, short_name: str):
        if (short_name not in self.elements):
            channel = FlexrayPhysicalChannel(self, short_name)
            self.addElement(channel)
            self.physicalChannel.append(channel)
        return self.getElement(short_name)

    def getProtocolName(self):
        return self.protocolName

    def setProtocolName(self, value):
        self.protocolName = value
        return self

    def getProtocolVersion(self):
        return self.protocolVersion

    def setProtocolVersion(self, value):
        self.protocolVersion = value
        return self


class CanClusterBusOffRecovery(ARObject):
    """
    Defines bus off recovery properties for CAN clusters,
    specifying timing and counter configurations for
    CAN controller recovery after bus off conditions.
    """
    def __init__(self):
        super().__init__()

        self.borCounterL1ToL2: PositiveInteger = None
        self.borTimeL1: TimeValue = None
        self.borTimeL2: TimeValue = None
        self.borTimeTxEnsured: TimeValue = None
        self.mainFunctionPeriod: TimeValue = None

    def getBorCounterL1ToL2(self):
        return self.borCounterL1ToL2

    def setBorCounterL1ToL2(self, value):
        if value is not None:
            self.borCounterL1ToL2 = value
        return self

    def getBorTimeL1(self):
        return self.borTimeL1

    def setBorTimeL1(self, value):
        if value is not None:
            self.borTimeL1 = value
        return self

    def getBorTimeL2(self):
        return self.borTimeL2

    def setBorTimeL2(self, value):
        if value is not None:
            self.borTimeL2 = value
        return self

    def getBorTimeTxEnsured(self):
        return self.borTimeTxEnsured

    def setBorTimeTxEnsured(self, value):
        if value is not None:
            self.borTimeTxEnsured = value
        return self

    def getMainFunctionPeriod(self):
        return self.mainFunctionPeriod

    def setMainFunctionPeriod(self, value):
        if value is not None:
            self.mainFunctionPeriod = value
        return self


class AbstractCanCluster(CommunicationCluster, ABC):
    """
    Abstract base class for CAN clusters, extending communication
    clusters with CAN-specific properties including FD and XL
    baud rates and speed configurations.
    """
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is AbstractCanCluster:
            raise TypeError("AbstractCanCluster is an abstract class.")
        
        super().__init__(parent, short_name)

        self.busOffRecovery: CanClusterBusOffRecovery = None
        self.canFdBaudrate: PositiveUnlimitedInteger = None
        self.canXlBaudrate: PositiveUnlimitedInteger = None
        self.speed: PositiveUnlimitedInteger = None

    def getBusOffRecovery(self):
        return self.busOffRecovery

    def setBusOffRecovery(self, value):
        self.busOffRecovery = value
        return self

    def getCanFdBaudrate(self):
        return self.canFdBaudrate

    def setCanFdBaudrate(self, value):
        self.canFdBaudrate = value
        return self

    def getCanXlBaudrate(self):
        return self.canXlBaudrate

    def setCanXlBaudrate(self, value):
        self.canXlBaudrate = value
        return self

    def getSpeed(self):
        return self.speed

    def setSpeed(self, value):
        self.speed = value
        return self


class CanCluster(AbstractCanCluster):
    """
    Represents a CAN cluster in the communication system,
    implementing specific properties for CAN network
    communication including timing and error recovery.
    """
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class LinCluster(CommunicationCluster):
    """
    Represents a LIN cluster in the communication system,
    implementing specific properties for LIN network
    communication including scheduling and timing management.
    """
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class CommunicationController(Identifiable, ABC):
    """
    Abstract base class for communication controllers,
    defining common properties for different types of
    communication hardware controllers in the system.
    """
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is CommunicationController:
            raise TypeError("CommunicationController is an abstract class.")
        
        super().__init__(parent, short_name)

        self.wakeUpByControllerSupported: Boolean = None

    def getWakeUpByControllerSupported(self):
        return self.wakeUpByControllerSupported

    def setWakeUpByControllerSupported(self, value):
        self.wakeUpByControllerSupported = value
        return self


class PncGatewayTypeEnum(AREnum):
    """
    Enumeration defining types of PNC (Partial Network Cluster)
    gateways, specifying the gateway behavior in partial
    network communication management.
    """
    ENUM_ACTIVE = "active"
    ENUM_NONE = "none"
    ENUM_PASSIVE = "passive"

    def __init__(self):
        super().__init__([
            PncGatewayTypeEnum.ENUM_ACTIVE,
            PncGatewayTypeEnum.ENUM_NONE,
            PncGatewayTypeEnum.ENUM_PASSIVE
        ])


class CommunicationDirectionType(AREnum):
    """
    Enumeration defining communication direction types,
    specifying whether communication is inbound or outbound.
    """
    ENUM_IN = "in"
    ENUM_OUT = "out"

    def __init__(self):
        super().__init__([
            CommunicationDirectionType.ENUM_IN,
            CommunicationDirectionType.ENUM_OUT
        ])


class CommConnectorPort(Identifiable, ABC):
    """
    Abstract base class for communication connector ports,
    defining common properties for different types of
    communication ports including direction and processing.
    """
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is CommConnectorPort:
            raise TypeError("CommConnectorPort is an abstract class.")
        
        super().__init__(parent, short_name)
        
        self.communicationDirection: CommunicationDirectionType = None

    def getCommunicationDirection(self):
        return self.communicationDirection

    def setCommunicationDirection(self, value):
        if value is not None:
            self.communicationDirection = value
        return self


class FramePort(CommConnectorPort):
    """
    Represents a frame port for communication connectors,
    handling frame-based communication at the connector level.
    """
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class IPduSignalProcessingEnum(Enum):
    """
    Enumeration defining types of IPDU signal processing,
    specifying whether signal processing is deferred or immediate.
    """
    ENUM_DEFERRED = "deferred"
    ENUM_IMMEDIATE = "immediate"


class IPduPort(CommConnectorPort):
    """
    Represents an IPDU port for communication connectors,
    handling Interaction Protocol Data Unit communication
    with specific processing and security properties.
    """
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)
        
        self.iPduSignalProcessing: IPduSignalProcessingEnum = None
        self.keyId: PositiveInteger = None
        self.rxSecurityVerification: Boolean = None
        self.timestampRxAcceptanceWindow: TimeValue = None
        self.useAuthDataFreshness: Boolean = None

    def getIPduSignalProcessing(self):
        return self.iPduSignalProcessing

    def setIPduSignalProcessing(self, value):
        if value is not None:
            self.iPduSignalProcessing = value
        return self

    def getKeyId(self):
        return self.keyId

    def setKeyId(self, value):
        if value is not None:
            self.keyId = value
        return self

    def getRxSecurityVerification(self):
        return self.rxSecurityVerification

    def setRxSecurityVerification(self, value):
        if value is not None:
            self.rxSecurityVerification = value
        return self

    def getTimestampRxAcceptanceWindow(self):
        return self.timestampRxAcceptanceWindow

    def setTimestampRxAcceptanceWindow(self, value):
        if value is not None:
            self.timestampRxAcceptanceWindow = value
        return self

    def getUseAuthDataFreshness(self):
        return self.useAuthDataFreshness

    def setUseAuthDataFreshness(self, value):
        if value is not None:
            self.useAuthDataFreshness = value
        return self


class ISignalPort(CommConnectorPort):
    """
    Represents an interaction signal port for communication connectors,
    handling interaction signal communication with filtering,
    timeout, and validity handling properties.
    """
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)
        
        self.dataFilter: DataFilter = None
        self.ddsQosProfileRef: RefType = None
        self.firstTimeout: TimeValue = None
        self.handleInvalid = None
        self.timeout: TimeValue = None

    def getDataFilter(self):
        return self.dataFilter

    def setDataFilter(self, value):
        if value is not None:
            self.dataFilter = value
        return self

    def getDdsQosProfileRef(self):
        return self.ddsQosProfileRef

    def setDdsQosProfileRef(self, value):
        if value is not None:
            self.ddsQosProfileRef = value
        return self

    def getFirstTimeout(self):
        return self.firstTimeout

    def setFirstTimeout(self, value):
        if value is not None:
            self.firstTimeout = value
        return self

    def getHandleInvalid(self):
        return self.handleInvalid

    def setHandleInvalid(self, value):
        if value is not None:
            self.handleInvalid = value
        return self

    def getTimeout(self):
        return self.timeout

    def setTimeout(self, value):
        if value is not None:
            self.timeout = value
        return self


class CommunicationConnector(Identifiable, ABC):
    """
    Abstract base class for communication connectors,
    defining common properties for connecting communication
    controllers to communication channels and managing
    port instances and gateway types.
    """
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is CommunicationConnector:
            raise TypeError("CommunicationConnector is an abstract class.")
        
        super().__init__(parent, short_name)

        self.commControllerRef: RefType = None
        self.createEcuWakeupSource: Boolean = None
        self.dynamicPncToChannelMappingEnabled: Boolean = None
        self.ecuCommPortInstances: List[CommConnectorPort] = []
        self.pncFilterArrayMasks: List[PositiveInteger] = []
        self.pncGatewayType: PncGatewayTypeEnum = None

    def getCommControllerRef(self):
        return self.commControllerRef

    def setCommControllerRef(self, value):
        self.commControllerRef = value
        return self

    def getCreateEcuWakeupSource(self):
        return self.createEcuWakeupSource

    def setCreateEcuWakeupSource(self, value):
        self.createEcuWakeupSource = value
        return self

    def getDynamicPncToChannelMappingEnabled(self):
        return self.dynamicPncToChannelMappingEnabled

    def setDynamicPncToChannelMappingEnabled(self, value):
        self.dynamicPncToChannelMappingEnabled = value
        return self

    def getEcuCommPortInstances(self):
        return list(sorted(filter(lambda a: isinstance(a, CommConnectorPort), self.elements), key=lambda o: o.getShortName()))

    def createFramePort(self, short_name) -> FramePort:
        if short_name not in self.elements:
            port = FramePort(self, short_name)
            self.addElement(port)
            self.ecuCommPortInstances.append(port)
        return self.getElement(short_name)

    def createIPduPort(self, short_name) -> IPduPort:
        if short_name not in self.elements:
            port = IPduPort(self, short_name)
            self.addElement(port)
            self.ecuCommPortInstances.append(port)
        return self.getElement(short_name)
    
    def createISignalPort(self, short_name) -> ISignalPort:
        if short_name not in self.elements:
            port = ISignalPort(self, short_name)
            self.addElement(port)
            self.ecuCommPortInstances.append(port)
        return self.getElement(short_name)

    def getPncFilterArrayMasks(self):
        return self.pncFilterArrayMasks

    def addPncFilterArrayMask(self, value):
        self.pncFilterArrayMasks.append(value)
        return self

    def getPncGatewayType(self):
        return self.pncGatewayType

    def setPncGatewayType(self, value):
        self.pncGatewayType = value
        return self

class EcuInstance(FibexElement):
    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        self.associatedComIPduGroupRefs: List[RefType] = []
        self.associatedConsumedProvidedServiceInstanceGroupRefs: List[RefType] = []
        self.associatedPdurIPduGroupRefs: List[RefType] = []
        self.channelSynchronousWakeup: Boolean = None
        self.clientIdRange = None
        self.comConfigurationGwTimeBase: TimeValue = None
        self.comConfigurationRxTimeBase: TimeValue = None
        self.comConfigurationTxTimeBase: TimeValue = None
        self.comEnableMDTForCyclicTransmission: Boolean = None
        self.commControllers: List["CommunicationController"] = []
        self.connectors: List["CommunicationConnector"] = []
        self.diagnosticAddress: Integer = None
        self.dltConfig = None
        self.doIpConfig = None
        self.ecuTaskProxyRefs: List[RefType] = []
        self.ethSwitchPortGroupDerivation: Boolean = None
        self.firewallRuleRef: RefType = None
        self.partitions = []
        self.pncNmRequest: Boolean = None
        self.pncPrepareSleepTimer: TimeValue = None
        self.pncSynchronousWakeup: Boolean = None
        self.pnResetTime: TimeValue = None
        self.sleepModeSupported: Boolean = None
        self.tcpIpIcmpPropsRef: RefType = None
        self.tcpIpPropsRef: RefType = None
        self.v2xSupported = None
        self.wakeUpOverBusSupported: Boolean = None

    def getAssociatedComIPduGroupRefs(self):
        return self.associatedComIPduGroupRefs

    def addAssociatedComIPduGroupRef(self, value):
        self.associatedComIPduGroupRefs.append(value)
        return self

    def getAssociatedConsumedProvidedServiceInstanceGroupRefs(self):
        return self.associatedConsumedProvidedServiceInstanceGroupRefs

    def addAssociatedConsumedProvidedServiceInstanceGroupRef(self, value):
        self.associatedConsumedProvidedServiceInstanceGroupRefs.append(value)
        return self

    def getAssociatedPdurIPduGroupRefs(self):
        return self.associatedPdurIPduGroupRefs

    def addAssociatedPdurIPduGroupRef(self, value):
        self.associatedPdurIPduGroupRefs.append(value)
        return self

    def getChannelSynchronousWakeup(self):
        return self.channelSynchronousWakeup

    def setChannelSynchronousWakeup(self, value):
        self.channelSynchronousWakeup = value
        return self

    def getClientIdRange(self):
        return self.clientIdRange

    def setClientIdRange(self, value):
        self.clientIdRange = value
        return self

    def getComConfigurationGwTimeBase(self):
        return self.comConfigurationGwTimeBase

    def setComConfigurationGwTimeBase(self, value):
        self.comConfigurationGwTimeBase = value
        return self

    def getComConfigurationRxTimeBase(self):
        return self.comConfigurationRxTimeBase

    def setComConfigurationRxTimeBase(self, value):
        self.comConfigurationRxTimeBase = value
        return self

    def getComConfigurationTxTimeBase(self):
        return self.comConfigurationTxTimeBase

    def setComConfigurationTxTimeBase(self, value):
        self.comConfigurationTxTimeBase = value
        return self

    def getComEnableMDTForCyclicTransmission(self):
        return self.comEnableMDTForCyclicTransmission

    def setComEnableMDTForCyclicTransmission(self, value):
        self.comEnableMDTForCyclicTransmission = value
        return self

    def getCommControllers(self):
        return list(sorted(filter(lambda a: isinstance(a, CommunicationController), self.elements), key= lambda o:o.short_name))

    def createCanCommunicationController(self, short_name: str) -> "CanCommunicationController":
        if (not self.IsElementExists(short_name)):
            from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology import CanCommunicationController
            controller = CanCommunicationController(self, short_name)
            self.addElement(controller)
        return self.getElement(short_name)
    
    def createEthernetCommunicationController(self, short_name: str) -> "EthernetCommunicationController":
        if (not self.IsElementExists(short_name)):
            from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import EthernetCommunicationController
            controller = EthernetCommunicationController(self, short_name)
            self.addElement(controller)
        return self.getElement(short_name)
    
    def createLinMaster(self, short_name: str) -> "LinMaster":
        if (not self.IsElementExists(short_name)):
            from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinTopology import LinMaster
            controller = LinMaster(self, short_name)
            self.addElement(controller)
        return self.getElement(short_name)
    
    def createFlexrayCommunicationController(self, short_name: str) -> "FlexrayCommunicationController":
        if (not self.IsElementExists(short_name)):
            from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Flexray.FlexrayTopology import FlexrayCommunicationController
            controller = FlexrayCommunicationController(self, short_name)
            self.addElement(controller)
        return self.getElement(short_name)

    def getConnectors(self):
        return list(sorted(filter(lambda a: isinstance(a, CommunicationConnector), self.elements), key= lambda o:o.short_name))

    def createCanCommunicationConnector(self, short_name: str) -> "CanCommunicationConnector":
        if (not self.IsElementExists(short_name)):
            from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology import CanCommunicationConnector
            connector = CanCommunicationConnector(self, short_name)
            self.addElement(connector)
        return self.getElement(short_name)
    
    def createEthernetCommunicationConnector(self, short_name: str) -> "EthernetCommunicationConnector":
        if (not self.IsElementExists(short_name)):
            from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import EthernetCommunicationConnector
            connector = EthernetCommunicationConnector(self, short_name)
            self.addElement(connector)
        return self.getElement(short_name)
    
    def createLinCommunicationConnector(self, short_name: str) -> "LinCommunicationConnector":
        if (not self.IsElementExists(short_name)):
            from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinTopology import LinCommunicationConnector
            connector = LinCommunicationConnector(self, short_name)
            self.addElement(connector)
        return self.getElement(short_name)
    
    def createFlexrayCommunicationConnector(self, short_name: str) -> "FlexrayCommunicationConnector":
        if (not self.IsElementExists(short_name)):
            from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Flexray.FlexrayTopology import FlexrayCommunicationConnector
            connector = FlexrayCommunicationConnector(self, short_name)
            self.addElement(connector)
        return self.getElement(short_name)
    
    def getDiagnosticAddress(self):
        return self.diagnosticAddress

    def setDiagnosticAddress(self, value):
        if value is not None:
            self.diagnosticAddress = value
        return self

    def getDltConfig(self):
        return self.dltConfig

    def setDltConfig(self, value):
        self.dltConfig = value
        return self

    def getDoIpConfig(self):
        return self.doIpConfig

    def setDoIpConfig(self, value):
        self.doIpConfig = value
        return self

    def getEcuTaskProxyRefs(self):
        return self.ecuTaskProxyRefs

    def setEcuTaskProxyRefs(self, value):
        self.ecuTaskProxyRefs = value
        return self

    def getEthSwitchPortGroupDerivation(self):
        return self.ethSwitchPortGroupDerivation

    def setEthSwitchPortGroupDerivation(self, value):
        self.ethSwitchPortGroupDerivation = value
        return self

    def getFirewallRuleRef(self):
        return self.firewallRuleRef

    def setFirewallRuleRef(self, value):
        self.firewallRuleRef = value
        return self

    def getPartitions(self):
        return self.partitions

    def addPartition(self, value):
        self.partitions.append(value)
        return self

    def getPncNmRequest(self):
        return self.pncNmRequest

    def setPncNmRequest(self, value):
        self.pncNmRequest = value
        return self

    def getPncPrepareSleepTimer(self):
        return self.pncPrepareSleepTimer

    def setPncPrepareSleepTimer(self, value):
        self.pncPrepareSleepTimer = value
        return self

    def getPncSynchronousWakeup(self):
        return self.pncSynchronousWakeup

    def setPncSynchronousWakeup(self, value):
        self.pncSynchronousWakeup = value
        return self

    def getPnResetTime(self):
        return self.pnResetTime

    def setPnResetTime(self, value):
        self.pnResetTime = value
        return self

    def getSleepModeSupported(self):
        return self.sleepModeSupported

    def setSleepModeSupported(self, value):
        self.sleepModeSupported = value
        return self

    def getTcpIpIcmpPropsRef(self):
        return self.tcpIpIcmpPropsRef

    def setTcpIpIcmpPropsRef(self, value):
        self.tcpIpIcmpPropsRef = value
        return self

    def getTcpIpPropsRef(self):
        return self.tcpIpPropsRef

    def setTcpIpPropsRef(self, value):
        self.tcpIpPropsRef = value
        return self

    def getV2xSupported(self):
        return self.v2xSupported

    def setV2xSupported(self, value):
        self.v2xSupported = value
        return self

    def getWakeUpOverBusSupported(self):
        return self.wakeUpOverBusSupported

    def setWakeUpOverBusSupported(self, value):
        self.wakeUpOverBusSupported = value
        return self
