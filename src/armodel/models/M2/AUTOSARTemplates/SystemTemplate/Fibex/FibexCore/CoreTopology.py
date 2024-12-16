from abc import ABCMeta
from enum import Enum
from typing import List


from ......M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from ......M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARFloat, Boolean, PositiveInteger, RefType, ARLiteral, TimeValue
from ......M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from ......M2.AUTOSARTemplates.SWComponentTemplate.Communication import HandleInvalidEnum
from ......M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanCommunication import CanFrameTriggering
from ......M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication import LinFrameTriggering
from ......M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import FibexElement, FrameTriggering, ISignalTriggering, PduTriggering
from ......M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.NetworkEndpoint import NetworkEndpoint

class PhysicalChannel (Identifiable, metaclass = ABCMeta):
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) == PhysicalChannel:
            raise NotImplementedError("PhysicalChannel is an abstract class.")
        
        super().__init__(parent, short_name)

        self.commConnectorRefs = []                     # type: List[RefType]
        self.managedPhysicalChannelRefs = []            # type: List[RefType]

    def getCommConnectorRefs(self):
        return self.commConnectorRefs

    def addCommConnectorRef(self, value):
        self.commConnectorRefs.append(value)
        return self

    def getFrameTriggerings(self) -> List[FrameTriggering]:
        return list(sorted(filter(lambda a: isinstance(a, FrameTriggering), self.elements.values()), key= lambda o:o.getShortName()))

    def createCanFrameTriggering(self, short_name: str):
        if (short_name not in self.elements):
            triggering = CanFrameTriggering(self, short_name)
            self.addElement(triggering)
        return self.getElement(short_name)
    
    def createLinFrameTriggering(self, short_name: str):
        if (short_name not in self.elements):
            triggering = LinFrameTriggering(self, short_name)
            self.addElement(triggering)
        return self.getElement(short_name)

    def getISignalTriggerings(self) -> List[ISignalTriggering]:
        return list(sorted(filter(lambda a: isinstance(a, ISignalTriggering), self.elements.values()), key= lambda o:o.getShortName()))

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
        return list(sorted(filter(lambda a: isinstance(a, PduTriggering), self.elements.values()), key= lambda o:o.getShortName()))

    def createPduTriggering(self, short_name: str):
        if (short_name not in self.elements):
            triggering = PduTriggering(self, short_name)
            self.addElement(triggering)
        return self.getElement(short_name)

class AbstractCanPhysicalChannel(PhysicalChannel, metaclass = ABCMeta):
    def __init__(self, parent, short_name):
        if type(self) == ARObject:
            raise NotImplementedError("AbstractCanPhysicalChannel is an abstract class.")
         
        super().__init__(parent, short_name)

class CanPhysicalChannel(AbstractCanPhysicalChannel):
    def __init__(self, parent, short_name):
        super().__init__(parent, short_name) 

class LinPhysicalChannel(PhysicalChannel):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

class EthernetPhysicalChannel(PhysicalChannel):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.networkEndpoints = []                              # type: List[NetworkEndpoint]
        self.soAdConfig = None                                  # type: SoAdConfig
        self.vlan = None                                        # type: VlanConfig

    def getNetworkEndpoints(self):
        return self.networkEndpoints

    def createNetworkEndPoint(self, short_name:str) -> NetworkEndpoint:
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

    def setVlan(self, value):
        self.vlan = value
        return self         

class CommunicationCluster(FibexElement, metaclass = ABCMeta):
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) == CommunicationCluster:
            raise NotImplementedError("CommunicationCluster is an abstract class.")
        
        super().__init__(parent, short_name)

        self.baudrate = None                # type: ARFloat
        self.protocolName = None            # type: ARLiteral
        self.protocolVersion = None         # type: ARLiteral

    def getBaudrate(self):
        return self.baudrate

    def setBaudrate(self, value):
        self.baudrate = value
        return self

    def getPhysicalChannels(self) -> List[PhysicalChannel]:
        return list(sorted(filter(lambda a: isinstance(a, PhysicalChannel), self.elements.values()), key= lambda o:o.getShortName()))
    
    def getCanPhysicalChannels(self) -> List[CanPhysicalChannel]:
        return list(sorted(filter(lambda a: isinstance(a, CanPhysicalChannel), self.elements.values()), key= lambda o:o.getShortName()))
    
    def getLinPhysicalChannels(self) -> List[LinPhysicalChannel]:
        return list(sorted(filter(lambda a: isinstance(a, LinPhysicalChannel), self.elements.values()), key= lambda o:o.getShortName()))
    
    def getEthernetPhysicalChannels(self) -> List[EthernetPhysicalChannel]:
        return list(sorted(filter(lambda a: isinstance(a, EthernetPhysicalChannel), self.elements.values()), key= lambda o:o.getShortName()))
    
    def createCanPhysicalChannel(self, short_name: str):
        if (short_name not in self.elements):
            channel = CanPhysicalChannel(self, short_name)
            self.addElement(channel)
        return self.getElement(short_name)
    
    def createLinPhysicalChannel(self, short_name: str):
        if (short_name not in self.elements):
            channel = LinPhysicalChannel(self, short_name)
            self.addElement(channel)
        return self.getElement(short_name)
    
    def createEthernetPhysicalChannel(self, short_name: str):
        if (short_name not in self.elements):
            channel = EthernetPhysicalChannel(self, short_name)
            self.addElement(channel)
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
    
class AbstractCanCluster(CommunicationCluster, metaclass = ABCMeta):
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) == AbstractCanCluster:
            raise NotImplementedError("AbstractCanCluster is an abstract class.")
        
        super().__init__(parent, short_name)

        self.busOffRecovery = None
        self.canFdBaudrate = None
        self.canXlBaudrate = None
        self.speed = None

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

class CommunicationController(Identifiable, metaclass = ABCMeta):
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) == CommunicationController:
            raise NotImplementedError("CommunicationController is an abstract class.")
        
        super().__init__(parent, short_name)

        self.wakeUpByControllerSupported = None                         # type: Boolean

    def getWakeUpByControllerSupported(self):
        return self.wakeUpByControllerSupported

    def setWakeUpByControllerSupported(self, value):
        self.wakeUpByControllerSupported = value
        return self
    
class PncGatewayTypeEnum(Enum):
    ENUM_ACTIVE = "active"
    ENUM_NONE = "none"
    ENUM_PASSIVE = "passive"

class CommunicationDirectionType(Enum):
    ENUM_IN = "in"
    ENUM_OUT = "out"

class CommConnectorPort(Identifiable, metaclass = ABCMeta):
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) == CommConnectorPort:
            raise NotImplementedError("CommConnectorPort is an abstract class.")
        
        super().__init__(parent, short_name)

        # type: CommunicationDirectionType
        self.communicationDirection = None

    def getCommunicationDirection(self) -> CommunicationDirectionType:
        return self.communicationDirection

    def setCommunicationDirection(self, value: CommunicationDirectionType):
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

        # type: IPduSignalProcessingEnum
        self.iPduSignalProcessing = None
        self.rxSecurityVerification = None                              # type: Boolean
        self.timestampRxAcceptanceWindow = None                         # type: TimeValue
        self.useAuthDataFreshness = None                                # type: Boolean

    def getIPduSignalProcessing(self):
        return self.iPduSignalProcessing

    def setIPduSignalProcessing(self, value):
        self.iPduSignalProcessing = value
        return self

    def getRxSecurityVerification(self):
        return self.rxSecurityVerification

    def setRxSecurityVerification(self, value):
        self.rxSecurityVerification = value
        return self

    def getTimestampRxAcceptanceWindow(self):
        return self.timestampRxAcceptanceWindow

    def setTimestampRxAcceptanceWindow(self, value):
        self.timestampRxAcceptanceWindow = value
        return self

    def getUseAuthDataFreshness(self):
        return self.useAuthDataFreshness

    def setUseAuthDataFreshness(self, value):
        self.useAuthDataFreshness = value
        return self

class ISignalPort(CommConnectorPort):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)
        
        # type: DataFilter
        self.dataFilter = None
        self.ddsQosProfileRef = None                                    # type: RefType
        # type: TimeValue
        self.firstTimeout = None
        # type: HandleInvalidEnum
        self.handleInvalid = None

    def getDataFilter(self):
        return self.dataFilter

    def setDataFilter(self, value):
        self.dataFilter = value
        return self

    def getDdsQosProfileRef(self):
        return self.ddsQosProfileRef

    def setDdsQosProfileRef(self, value):
        self.ddsQosProfileRef = value
        return self

    def getFirstTimeout(self):
        return self.firstTimeout

    def setFirstTimeout(self, value):
        self.firstTimeout = value
        return self

    def getHandleInvalid(self):
        return self.handleInvalid

    def setHandleInvalid(self, value):
        self.handleInvalid = value
        return self

class CommunicationConnector(Identifiable, metaclass = ABCMeta):
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) == CommunicationConnector:
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
        return list(sorted(filter(lambda a: isinstance(a, CommConnectorPort), self.elements.values()), key= lambda o:o.getShortName()))

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

        