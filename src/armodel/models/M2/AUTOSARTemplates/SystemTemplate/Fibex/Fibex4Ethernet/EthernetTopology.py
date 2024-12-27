from typing import List

from ......M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from ......M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, Integer, MacAddressString, PositiveInteger, RefType, TimeValue
from ......M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from ......M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import CommunicationCluster, CommunicationConnector, CommunicationController

class MacMulticastGroup(Identifiable):
    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        self.macMulticastAddress = None                                     # type: MacAddressString

    def getMacMulticastAddress(self):
        return self.macMulticastAddress

    def setMacMulticastAddress(self, value):
        if value is not None:
            self.macMulticastAddress = value
        return self
class EthernetCluster(CommunicationCluster):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)
        
        self.couplingPorts = []                                             # type: List[CouplingPortConnection]
        self.couplingPortStartupActiveTime = None                           # type: TimeValue
        self.couplingPortSwitchoffDelay = None                              # type: TimeValue
        self.macMulticastGroups = []                                        # type: List[MacMulticastGroup]

    def getCouplingPorts(self):
        return self.couplingPorts

    def addCouplingPort(self, value):
        if value is not None:
            self.couplingPorts.append(value)
        return self

    def getCouplingPortStartupActiveTime(self):
        return self.couplingPortStartupActiveTime

    def setCouplingPortStartupActiveTime(self, value):
        if value is not None:
            self.couplingPortStartupActiveTime = value
        return self

    def getCouplingPortSwitchoffDelay(self):
        return self.couplingPortSwitchoffDelay

    def setCouplingPortSwitchoffDelay(self, value):
        if value is not None:
            self.couplingPortSwitchoffDelay = value
        return self

    def getMacMulticastGroups(self):
        return self.macMulticastGroups

    def createMacMulticastGroup(self, short_name: str) -> MacMulticastGroup:
        if (short_name not in self.elements):
            group = MacMulticastGroup(self, short_name)
            self.addElement(group)
            self.macMulticastGroups.append(group)
        return self.getElement(short_name)

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
    
class RequestResponseDelay(ARObject):
    def __init__(self):
        super().__init__()

        self.maxValue = None                                        # type: TimeValue
        self.minValue = None                                        # type: TimeValue

    def getMaxValue(self):
        return self.maxValue

    def setMaxValue(self, value):
        if value is not None:
            self.maxValue = value
        return self

    def getMinValue(self):
        return self.minValue

    def setMinValue(self, value):
        if value is not None:
            self.minValue = value
        return self

class InitialSdDelayConfig(ARObject):
    def __init__(self):
        super().__init__()

        self.initialDelayMaxValue = None                            # type: TimeValue
        self.initialDelayMinValue = None                            # type: TimeValue
        self.initialRepetitionsBaseDelay = None                     # type: TimeValue
        self.initialRepetitionsMax = None                           # type: PositiveInteger

    def getInitialDelayMaxValue(self):
        return self.initialDelayMaxValue

    def setInitialDelayMaxValue(self, value):
        if value is not None:
            self.initialDelayMaxValue = value
        return self

    def getInitialDelayMinValue(self):
        return self.initialDelayMinValue

    def setInitialDelayMinValue(self, value):
        if value is not None:
            self.initialDelayMinValue = value
        return self

    def getInitialRepetitionsBaseDelay(self):
        return self.initialRepetitionsBaseDelay

    def setInitialRepetitionsBaseDelay(self, value):
        if value is not None:
            self.initialRepetitionsBaseDelay = value
        return self

    def getInitialRepetitionsMax(self):
        return self.initialRepetitionsMax

    def setInitialRepetitionsMax(self, value):
        if value is not None:
            self.initialRepetitionsMax = value
        return self

    
class SdClientConfig(ARObject):
    def __init__(self):
        super().__init__()

        self.capabilityRecord = None                                # type: TagWithOptionalValue
        self.clientServiceMajorVersion = None                       # type: PositiveInteger
        self.clientServiceMinorVersion = None                       # type: PositiveInteger
        self.initialFindBehavior = None                             # type: InitialSdDelayConfig
        self.requestResponseDelay = None                            # type: RequestResponseDelay
        self.ttl = None                                             # type: PositiveInteger

    def getClientServiceMajorVersion(self):
        return self.clientServiceMajorVersion

    def setClientServiceMajorVersion(self, value):
        if value is not None:
            self.clientServiceMajorVersion = value
        return self

    def getClientServiceMinorVersion(self):
        return self.clientServiceMinorVersion

    def setClientServiceMinorVersion(self, value):
        if value is not None:
            self.clientServiceMinorVersion = value
        return self

    def getInitialFindBehavior(self):
        return self.initialFindBehavior

    def setInitialFindBehavior(self, value):
        if value is not None:
            self.initialFindBehavior = value
        return self

    def getRequestResponseDelay(self):
        return self.requestResponseDelay

    def setRequestResponseDelay(self, value):
        if value is not None:
            self.requestResponseDelay = value
        return self

    def getTtl(self):
        return self.ttl

    def setTtl(self, value):
        if value is not None:
            self.ttl = value
        return self


