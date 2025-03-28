from abc import ABCMeta
from enum import Enum
from typing import List

from ......M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Flexray.FlexrayCommunication import FlexrayFrameTriggering
from ......M2.AUTOSARTemplates.CommonStructure.Filter import DataFilter
from ......M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from ......M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from ......M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AREnum, ARFloat, Boolean, Integer, PositiveInteger
from ......M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveUnlimitedInteger, RefType, ARLiteral, TimeValue
from ......M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanCommunication import CanFrameTriggering
from ......M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication import LinFrameTriggering, LinScheduleTable
from ......M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.NetworkEndpoint import NetworkEndpoint
from ......M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import FibexElement, FrameTriggering, ISignalTriggering, PduTriggering


class CommunicationCycle(ARObject):
    def __init__(self):
        super().__init__()


class CycleCounter(CommunicationCycle):
    def __init__(self):
        super().__init__()

        self.CycleCounter = None                            # type: Integer

    def getCycleCounter(self):
        return self.CycleCounter

    def setCycleCounter(self, value):
        if value is not None:
            self.CycleCounter = value
        return self


class CycleRepetitionType(AREnum):
    def __init__(self):
        super().__init__([])


class CycleRepetition(CommunicationCycle):
    def __init__(self):
        super().__init__()

        self.BaseCycle = None                               # type: Integer
        self.CycleRepetition = None                         # type: CycleRepetitionType

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


class PhysicalChannel (Identifiable, metaclass=ABCMeta):
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is PhysicalChannel:
            raise NotImplementedError("PhysicalChannel is an abstract class.")
        
        super().__init__(parent, short_name)

        self.commConnectorRefs = []                     # type: List[RefType]
        self.frameTriggerings = []                      # type: List[FrameTriggering]
        self.managedPhysicalChannelRefs = []            # type: List[RefType]

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


class AbstractCanPhysicalChannel(PhysicalChannel, metaclass=ABCMeta):
    def __init__(self, parent, short_name):
        if type(self) is AbstractCanPhysicalChannel:
            raise NotImplementedError("AbstractCanPhysicalChannel is an abstract class.")
         
        super().__init__(parent, short_name)


class CanPhysicalChannel(AbstractCanPhysicalChannel):
    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)


class LinPhysicalChannel(PhysicalChannel):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.busIdleTimeoutPeriod = None                        # type: TimeValue
        # type: List[LinScheduleTable]
        self.scheduleTables = []

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
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.vlanIdentifier = None                              # type: PositiveInteger

    def getVlanIdentifier(self):
        return self.vlanIdentifier

    def setVlanIdentifier(self, value):
        if value is not None:
            self.vlanIdentifier = value
        return self


class EthernetPhysicalChannel(PhysicalChannel):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.networkEndpoints = []                              # type: List[NetworkEndpoint]
        self.soAdConfig = None                                  # type: SoAdConfig
        self.vlan = None                                        # type: VlanConfig

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
    CHANNEL_A = "channelA"
    channel_B = "channelB"

    def __init__(self):
        super().__init__([
            FlexrayChannelName.CHANNEL_A,
            FlexrayChannelName.channel_B
        ])


class FlexrayPhysicalChannel(PhysicalChannel):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.channelName = None                                     # type: FlexrayChannelName

    def getChannelName(self):
        return self.channelName

    def setChannelName(self, value):
        if value is not None:
            self.channelName = value
        return self


class CommunicationCluster(FibexElement, metaclass=ABCMeta):
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is CommunicationCluster:
            raise NotImplementedError("CommunicationCluster is an abstract class.")
        
        super().__init__(parent, short_name)

        self.baudrate = None                    # type: ARFloat
        self.physicalChannel = []               # type: List[PhysicalChannel]
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
    def __init__(self):
        super().__init__()

        self.borCounterL1ToL2 = None                            # type: PositiveInteger
        self.borTimeL1 = None                                   # type: TimeValue
        self.borTimeL2 = None                                   # type: TimeValue
        self.borTimeTxEnsured = None                            # type: TimeValue
        self.mainFunctionPeriod = None                          # type: TimeValue

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


class AbstractCanCluster(CommunicationCluster, metaclass=ABCMeta):
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is AbstractCanCluster:
            raise NotImplementedError("AbstractCanCluster is an abstract class.")
        
        super().__init__(parent, short_name)

        self.busOffRecovery = None                              # type: CanClusterBusOffRecovery
        self.canFdBaudrate = None                               # type: PositiveUnlimitedInteger
        self.canXlBaudrate = None                               # type: PositiveUnlimitedInteger
        self.speed = None                                       # type: PositiveUnlimitedInteger

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
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class LinCluster(CommunicationCluster):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class CommunicationController(Identifiable, metaclass=ABCMeta):
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is CommunicationController:
            raise NotImplementedError("CommunicationController is an abstract class.")
        
        super().__init__(parent, short_name)

        self.wakeUpByControllerSupported = None                         # type: Boolean

    def getWakeUpByControllerSupported(self):
        return self.wakeUpByControllerSupported

    def setWakeUpByControllerSupported(self, value):
        self.wakeUpByControllerSupported = value
        return self


class PncGatewayTypeEnum(AREnum):
    ENUM_ACTIVE = "active"
    ENUM_NONE = "none"
    ENUM_PASSIVE = "passive"

    def __init__(self):
        super().__init__([])


class CommunicationDirectionType(AREnum):
    ENUM_IN = "in"
    ENUM_OUT = "out"

    def __init__(self):
        super().__init__([])


class CommConnectorPort(Identifiable, metaclass=ABCMeta):
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is CommConnectorPort:
            raise NotImplementedError("CommConnectorPort is an abstract class.")
        
        super().__init__(parent, short_name)
        
        self.communicationDirection = None                                                  # type: CommunicationDirectionType

    def getCommunicationDirection(self):
        return self.communicationDirection

    def setCommunicationDirection(self, value):
        if value is not None:
            self.communicationDirection = value
        return self


class FramePort(CommConnectorPort):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class IPduSignalProcessingEnum(Enum):
    ENUM_DEFERRED = "deferred"
    ENUM_IMMEDIATE = "immediate"


class IPduPort(CommConnectorPort):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)
        
        self.iPduSignalProcessing = None                                # type: IPduSignalProcessingEnum
        self.keyId = None                                               # type: PositiveInteger
        self.rxSecurityVerification = None                              # type: Boolean
        self.timestampRxAcceptanceWindow = None                         # type: TimeValue
        self.useAuthDataFreshness = None                                # type: Boolean

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
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)
        
        self.dataFilter = None                                          # type: DataFilter
        self.ddsQosProfileRef = None                                    # type: RefType
        self.firstTimeout = None                                        # type: TimeValue
        self.handleInvalid = None                                       # type: HandleInvalidEnum
        self.timeout = None                                             # type: TimeValue

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


class CommunicationConnector(Identifiable, metaclass=ABCMeta):
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is CommunicationConnector:
            raise NotImplementedError("CommunicationConnector is an abstract class.")
        
        super().__init__(parent, short_name)

        self.commControllerRef = None                                   # type: RefType
        self.createEcuWakeupSource = None                               # type: Boolean
        self.dynamicPncToChannelMappingEnabled = None                   # type: Boolean
        self.ecuCommPortInstances = []                                  # type: List[CommConnectorPort]
        self.pncFilterArrayMasks = []                                   # type: List[PositiveInteger]
        self.pncGatewayType = None                                      # type: PncGatewayTypeEnum

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
