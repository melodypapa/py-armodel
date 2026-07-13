# This module contains AUTOSAR System Template classes for Ethernet communication
# It defines socket connections, connection bundles, and service instances for Ethernet networking

from typing import List
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, Identifier, PositiveInteger, RefType, TimeValue
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Describable, Referrable
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import FibexElement

class SocketConnection(Describable):
    """
    Represents a socket connection in the Ethernet communication system,
    defining properties for TCP/IP communication including IP addresses,
    ports, PDU handling, and timeout configurations for network connections.
    """
    # SocketConnection method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getAllowedIPv6ExtHeadersRef  [x] impl  [ ] docstring  [ ] test
    # [ ] setAllowedIPv6ExtHeadersRef  [x] impl  [ ] docstring  [ ] test
    # [ ] getAllowedTcpOptionsRef      [x] impl  [ ] docstring  [ ] test
    # [ ] setAllowedTcpOptionsRef      [x] impl  [ ] docstring  [ ] test
    # [ ] getClientIpAddrFromConnectionRequest [x] impl  [ ] docstring  [ ] test
    # [ ] setClientIpAddrFromConnectionRequest [x] impl  [ ] docstring  [ ] test
    # [ ] getClientPortRef             [x] impl  [ ] docstring  [ ] test
    # [ ] setClientPortRef             [x] impl  [ ] docstring  [ ] test
    # [ ] getClientPortFromConnectionRequest [x] impl  [ ] docstring  [ ] test
    # [ ] setClientPortFromConnectionRequest [x] impl  [ ] docstring  [ ] test
    # [ ] getPdus                      [x] impl  [ ] docstring  [ ] test
    # [ ] addPdu                       [x] impl  [ ] docstring  [ ] test
    # [ ] getPduSocketConnectionIpdus  [x] impl  [ ] docstring  [ ] test
    # [ ] addPduSocketConnectionIpdu   [x] impl  [ ] docstring  [ ] test
    # [ ] getPduCollectionMaxBufferSize [x] impl  [ ] docstring  [ ] test
    # [ ] setPduCollectionMaxBufferSize [x] impl  [ ] docstring  [ ] test
    # [ ] getPduCollectionTimeout      [x] impl  [ ] docstring  [ ] test
    # [ ] setPduCollectionTimeout      [x] impl  [ ] docstring  [ ] test
    # [ ] getRuntimeIpAddressConfiguration [x] impl  [ ] docstring  [ ] test
    # [ ] setRuntimeIpAddressConfiguration [x] impl  [ ] docstring  [ ] test
    # [ ] getRuntimePortConfiguration  [x] impl  [ ] docstring  [ ] test
    # [ ] setRuntimePortConfiguration  [x] impl  [ ] docstring  [ ] test
    # [ ] getShortLabel                [x] impl  [ ] docstring  [ ] test
    # [ ] setShortLabel                [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()

        self.allowedIPv6ExtHeadersRef: RefType = None
        self.allowedTcpOptionsRef: RefType = None
        self.clientIpAddrFromConnectionRequest: Boolean = None
        self.clientPortRef: RefType = None
        self.clientPortFromConnectionRequest: Boolean = None
        self.pdus: List[SocketConnectionIpduIdentifier] = []
        self.pduSocketConnectionIpdus: List[Identifier] = []
        self.pduCollectionMaxBufferSize: PositiveInteger = None
        self.pduCollectionTimeout: TimeValue = None
        self.runtimeIpAddressConfiguration = None
        self.runtimePortConfiguration = None
        self.shortLabel: Identifier = None

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
    """
    Identifies an IPDU (Interaction Protocol Data Unit) within a socket connection,
    defining header IDs, timeout values, collection semantics, and references
    to PDUs and triggering mechanisms for Ethernet communication.
    """
    # SocketConnectionIpduIdentifier method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getHeaderId                  [x] impl  [ ] docstring  [ ] test
    # [ ] setHeaderId                  [x] impl  [ ] docstring  [ ] test
    # [ ] getPduCollectionPduTimeout   [x] impl  [ ] docstring  [ ] test
    # [ ] setPduCollectionPduTimeout   [x] impl  [ ] docstring  [ ] test
    # [ ] getPduCollectionSemantics    [x] impl  [ ] docstring  [ ] test
    # [ ] setPduCollectionSemantics    [x] impl  [ ] docstring  [ ] test
    # [ ] getPduCollectionTrigger      [x] impl  [ ] docstring  [ ] test
    # [ ] setPduCollectionTrigger      [x] impl  [ ] docstring  [ ] test
    # [ ] getPduRef                    [x] impl  [ ] docstring  [ ] test
    # [ ] setPduRef                    [x] impl  [ ] docstring  [ ] test
    # [ ] getPduTriggeringRef          [x] impl  [ ] docstring  [ ] test
    # [ ] setPduTriggeringRef          [x] impl  [ ] docstring  [ ] test
    # [ ] getRoutingGroupRefs          [x] impl  [ ] docstring  [ ] test
    # [ ] setRoutingGroupRefs          [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()

        self.headerId: PositiveInteger = None
        self.pduCollectionPduTimeout: TimeValue = None
        self.pduCollectionSemantics = None
        self.pduCollectionTrigger = None
        self.PduRef: RefType = None
        self.pduTriggeringRef: RefType = None
        self.routingGroupRefs: List[RefType] = []


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
    """
    Groups multiple socket connections into a bundle for managing related
    Ethernet communications, including differentiated services, flow labels,
    and UDP checksum handling configurations.
    """
    # SocketConnectionBundle method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getBundledConnections        [x] impl  [ ] docstring  [ ] test
    # [ ] addBundledConnection         [x] impl  [ ] docstring  [ ] test
    # [ ] getDifferentiatedServiceField [x] impl  [ ] docstring  [ ] test
    # [ ] setDifferentiatedServiceField [x] impl  [ ] docstring  [ ] test
    # [ ] getFlowLabel                 [x] impl  [ ] docstring  [ ] test
    # [ ] setFlowLabel                 [x] impl  [ ] docstring  [ ] test
    # [ ] getPathMtuDiscoveryEnabled   [x] impl  [ ] docstring  [ ] test
    # [ ] setPathMtuDiscoveryEnabled   [x] impl  [ ] docstring  [ ] test
    # [ ] getPdus                      [x] impl  [ ] docstring  [ ] test
    # [ ] setPdus                      [x] impl  [ ] docstring  [ ] test
    # [ ] getServerPortRef             [x] impl  [ ] docstring  [ ] test
    # [ ] setServerPortRef             [x] impl  [ ] docstring  [ ] test
    # [ ] getUdpChecksumHandling       [x] impl  [ ] docstring  [ ] test
    # [ ] setUdpChecksumHandling       [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.bundledConnections: List[SocketConnection] = []
        self.differentiatedServiceField: PositiveInteger = None
        self.flowLabel: PositiveInteger = None
        self.pathMtuDiscoveryEnabled: Boolean = None
        self.pdus: List[SocketConnectionIpduIdentifier] = []
        self.serverPortRef: RefType = None
        self.udpChecksumHandling = None                                                           # type: UdpChecksumCalculationEnum

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

class SoAdRoutingGroup(FibexElement):
    """
    Defines a routing group for the Socket Adaptor (SoAd) module,
    specifying how Ethernet communication is organized and controlled
    within the AUTOSAR communication system.
    """
    # SoAdRoutingGroup method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getEventGroupControlType     [x] impl  [ ] docstring  [ ] test
    # [ ] setEventGroupControlType     [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.eventGroupControlType = None     # type: EventGroupControlTypeEnum

    def getEventGroupControlType(self):
        return self.eventGroupControlType

    def setEventGroupControlType(self, value):
        if value is not None:
            self.eventGroupControlType = value
        return self
