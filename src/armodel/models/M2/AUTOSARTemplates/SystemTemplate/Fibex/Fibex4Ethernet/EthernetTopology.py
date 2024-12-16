from typing import List

from ......M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from ......M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, Integer, PositiveInteger, PositiveUnlimitedInteger, RefType, TimeValue
from ......M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from ......M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import CommunicationCluster, CommunicationConnector, CommunicationController, PhysicalChannel

class EthernetCluster(CommunicationCluster):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)
        
        self.couplingPorts = []                             # type: List[CouplingPortConnection]
        self.couplingPortStartupActiveTime = None           # type: TimeValue
        self.couplingPortSwitchoffDelay = None              # type: TimeValue
        self.macMulticastGroups = []                        # type: MacMulticastGroup

    def getCouplingPorts(self):
        return self.couplingPorts

    def setCouplingPorts(self, value):
        self.couplingPorts = value
        return self

    def getCouplingPortStartupActiveTime(self):
        return self.couplingPortStartupActiveTime

    def setCouplingPortStartupActiveTime(self, value):
        self.couplingPortStartupActiveTime = value
        return self

    def getCouplingPortSwitchoffDelay(self):
        return self.couplingPortSwitchoffDelay

    def setCouplingPortSwitchoffDelay(self, value):
        self.couplingPortSwitchoffDelay = value
        return self

    def getMacMulticastGroups(self):
        return self.macMulticastGroups

    def setMacMulticastGroups(self, value):
        self.macMulticastGroups = value
        return self
    
class CouplingPort(Identifiable):
    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        self.connectionNegotiationBehavior = None           # type: EthernetConnectionNegotiationEnum


class EthernetCommunicationController(CommunicationController):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.canXlConfigRef = None                          # type: RefType
        self.couplingPorts = []                             # type: List[CouplingPort]
        self.macLayerType = None                            # type: EthernetMacLayerTypeEnum
        self.macUnicastAddress = None                       # type: MacAddressString
        self.maximumReceiveBufferLength = None              # type: Integer
        self.maximumTransmitBufferLength = None             # type: Integer
        self.slaveActAsPassiveCommunicationSlave = None     # type: Boolean
        self.slaveQualifiedUnexpectedLinkDownTime = None    # type: TimeValue

    def getCanXlConfigRef(self):
        return self.canXlConfigRef

    def setCanXlConfigRef(self, value):
        self.canXlConfigRef = value
        return self

    def getCouplingPorts(self):
        return self.couplingPorts

    def addCouplingPort(self, value):
        self.couplingPorts.append(value)
        return self

    def getMacLayerType(self):
        return self.macLayerType

    def setMacLayerType(self, value):
        self.macLayerType = value
        return self

    def getMacUnicastAddress(self):
        return self.macUnicastAddress

    def setMacUnicastAddress(self, value):
        self.macUnicastAddress = value
        return self

    def getMaximumReceiveBufferLength(self):
        return self.maximumReceiveBufferLength

    def setMaximumReceiveBufferLength(self, value):
        self.maximumReceiveBufferLength = value
        return self

    def getMaximumTransmitBufferLength(self):
        return self.maximumTransmitBufferLength

    def setMaximumTransmitBufferLength(self, value):
        self.maximumTransmitBufferLength = value
        return self

    def getSlaveActAsPassiveCommunicationSlave(self):
        return self.slaveActAsPassiveCommunicationSlave

    def setSlaveActAsPassiveCommunicationSlave(self, value):
        self.slaveActAsPassiveCommunicationSlave = value
        return self

    def getSlaveQualifiedUnexpectedLinkDownTime(self):
        return self.slaveQualifiedUnexpectedLinkDownTime

    def setSlaveQualifiedUnexpectedLinkDownTime(self, value):
        self.slaveQualifiedUnexpectedLinkDownTime = value
        return self

class EthernetCommunicationConnector(CommunicationConnector):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.ethIpPropsRef = None                               # type: RefType
        self.maximumTransmissionUnit = None                     # type: PositiveInteger
        self.neighborCacheSize = None                           # type: PositiveInteger
        self.pathMtuEnabled = None                              # type: Boolean
        self.pathMtuTimeout = None                              # type: TimeValue

    def getEthIpPropsRef(self):
        return self.ethIpPropsRef

    def setEthIpPropsRef(self, value):
        self.ethIpPropsRef = value
        return self

    def getMaximumTransmissionUnit(self):
        return self.maximumTransmissionUnit

    def setMaximumTransmissionUnit(self, value):
        self.maximumTransmissionUnit = value
        return self

    def getNeighborCacheSize(self):
        return self.neighborCacheSize

    def setNeighborCacheSize(self, value):
        self.neighborCacheSize = value
        return self

    def getPathMtuEnabled(self):
        return self.pathMtuEnabled

    def setPathMtuEnabled(self, value):
        self.pathMtuEnabled = value
        return self

    def getPathMtuTimeout(self):
        return self.pathMtuTimeout

    def setPathMtuTimeout(self, value):
        self.pathMtuTimeout = value
        return self
    


