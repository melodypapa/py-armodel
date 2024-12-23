from typing import List
from ......M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from ......M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, Identifier, PositiveInteger, RefType, TimeValue
from ......M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Describable, Identifiable, Referrable

class SocketConnection(Describable):
    def __init__(self):
        super().__init__()

        self.allowedIPv6ExtHeadersRef = None                                # type: RefType
        self.allowedTcpOptionsRef = None                                    # type: RefType
        self.clientIpAddrFromConnectionRequest = None                       # type: Boolean
        self.clientPortRef = None                                           # type: RefType
        self.clientPortFromConnectionRequest = None                         # type: Boolean
        self.pdus = []                                                      # type: List[SocketConnectionIpduIdentifier]
        self.pduSocketConnectionIpdus = []                                  # type: List[Identifier]
        self.pduCollectionMaxBufferSize = None                              # type: PositiveInteger
        self.pduCollectionTimeout = None                                    # type: TimeValue
        self.runtimeIpAddressConfiguration = None                           # type: RuntimeAddressConfigurationEnum
        self.runtimePortConfiguration = None                                # type: RuntimeAddressConfigurationEnum
        self.shortLabel = None                                              # type: Identifier

    def getAllowedIPv6ExtHeadersRef(self):
        return self.allowedIPv6ExtHeadersRef

    def setAllowedIPv6ExtHeadersRef(self, value):
        self.allowedIPv6ExtHeadersRef = value
        return self

    def getAllowedTcpOptionsRef(self):
        return self.allowedTcpOptionsRef

    def setAllowedTcpOptionsRef(self, value):
        self.allowedTcpOptionsRef = value
        return self
    
    def getClientIpAddrFromConnectionRequest(self):
        return self.clientIpAddrFromConnectionRequest

    def setClientIpAddrFromConnectionRequest(self, value):
        self.clientIpAddrFromConnectionRequest = value
        return self

    def getClientPortRef(self):
        return self.clientPortRef

    def setClientPortRef(self, value):
        self.clientPortRef = value
        return self

    def getClientPortFromConnectionRequest(self):
        return self.clientPortFromConnectionRequest

    def setClientPortFromConnectionRequest(self, value):
        self.clientPortFromConnectionRequest = value
        return self
    
    def getPdus(self):
        return self.pdus

    def addPdu(self, value):
        self.pdus.append(value)
        return self

    def getPduSocketConnectionIpdus(self):
        return self.pduSocketConnectionIpdus

    def addPduSocketConnectionIpdu(self, value):
        self.pduSocketConnectionIpdus.append(value)
        return self

    def getPduCollectionMaxBufferSize(self):
        return self.pduCollectionMaxBufferSize

    def setPduCollectionMaxBufferSize(self, value):
        self.pduCollectionMaxBufferSize = value
        return self

    def getPduCollectionTimeout(self):
        return self.pduCollectionTimeout

    def setPduCollectionTimeout(self, value):
        self.pduCollectionTimeout = value
        return self

    def getRuntimeIpAddressConfiguration(self):
        return self.runtimeIpAddressConfiguration

    def setRuntimeIpAddressConfiguration(self, value):
        self.runtimeIpAddressConfiguration = value
        return self

    def getRuntimePortConfiguration(self):
        return self.runtimePortConfiguration

    def setRuntimePortConfiguration(self, value):
        self.runtimePortConfiguration = value
        return self

    def getShortLabel(self):
        return self.shortLabel

    def setShortLabel(self, value):
        self.shortLabel = value
        return self


class SocketConnectionIpduIdentifier(ARObject):
    def __init__(self):
        super().__init__()

        self.headerId = None                                                # type: PositiveInteger
        self.pduCollectionPduTimeout = None                                 # type: TimeValue
        self.pduCollectionSemantics = None                                  # type: PduCollectionSemanticsEnum
        self.pduCollectionTrigger = None                                    # type: PduCollectionTriggerEnum
        self.PduRef = None                                                  # type: RefType
        self.pduTriggeringRef = None                                        # type: RefType
        self.routingGroupRefs = []                                          # type: List[RefType]


    def getHeaderId(self):
        return self.headerId

    def setHeaderId(self, value):
        self.headerId = value
        return self

    def getPduCollectionPduTimeout(self):
        return self.pduCollectionPduTimeout

    def setPduCollectionPduTimeout(self, value):
        self.pduCollectionPduTimeout = value
        return self

    def getPduCollectionSemantics(self):
        return self.pduCollectionSemantics

    def setPduCollectionSemantics(self, value):
        self.pduCollectionSemantics = value
        return self

    def getPduCollectionTrigger(self):
        return self.pduCollectionTrigger

    def setPduCollectionTrigger(self, value):
        self.pduCollectionTrigger = value
        return self

    def getPduRef(self):
        return self.PduRef

    def setPduRef(self, value):
        self.PduRef = value
        return self

    def getPduTriggeringRef(self):
        return self.pduTriggeringRef

    def setPduTriggeringRef(self, value):
        self.pduTriggeringRef = value
        return self

    def getRoutingGroupRefs(self):
        return self.routingGroupRefs

    def setRoutingGroupRefs(self, value):
        self.routingGroupRefs = value
        return self

class SocketConnectionBundle(Referrable):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.bundledConnections = []                                        # type: List[SocketConnection]
        self.differentiatedServiceField = None                              # type: PositiveInteger
        self.flowLabel = None                                               # type: PositiveInteger
        self.pathMtuDiscoveryEnabled = None                                 # type: Boolean
        self.pdus = []                                                      # type: List[SocketConnectionIpduIdentifier]
        self.serverPortRef = None                                           # type: RefType
        self.udpChecksumHandling = None                                     # type: UdpChecksumCalculationEnum

    def getBundledConnections(self):
        return self.bundledConnections

    def addBundledConnection(self, value):
        self.bundledConnections.append(value)
        return self

    def getDifferentiatedServiceField(self):
        return self.differentiatedServiceField

    def setDifferentiatedServiceField(self, value):
        self.differentiatedServiceField = value
        return self

    def getFlowLabel(self):
        return self.flowLabel

    def setFlowLabel(self, value):
        self.flowLabel = value
        return self

    def getPathMtuDiscoveryEnabled(self):
        return self.pathMtuDiscoveryEnabled

    def setPathMtuDiscoveryEnabled(self, value):
        self.pathMtuDiscoveryEnabled = value
        return self

    def getPdus(self):
        return self.pdus

    def setPdus(self, value):
        self.pdus = value
        return self

    def getServerPortRef(self):
        return self.serverPortRef

    def setServerPortRef(self, value):
        self.serverPortRef = value
        return self

    def getUdpChecksumHandling(self):
        return self.udpChecksumHandling

    def setUdpChecksumHandling(self, value):
        self.udpChecksumHandling = value
        return self

class SoAdRoutingGroup(Identifiable):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # type: EventGroupControlTypeEnum
        self.eventGroupControlType = None

    def getEventGroupControlType(self):
        return self.eventGroupControlType

    def setEventGroupControlType(self, value):
        if value is not None:
            self.eventGroupControlType = value
        return self
