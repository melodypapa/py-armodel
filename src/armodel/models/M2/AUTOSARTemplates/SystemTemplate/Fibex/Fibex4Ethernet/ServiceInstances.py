from typing import List

from ......M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetCommunication import SocketConnection, SocketConnectionBundle
from ......M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, PositiveInteger, RefType, TimeValue
from ......M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from ......M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class SocketAddress(Identifiable):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.allowedIPv6ExtHeadersRef = None        # type: RefType
        self.allowedTcpOptionsRef = None            # type: RefType
        self.applicationEndpoint = None             # type: ApplicationEndpoint
        self.connectorRef = None                    # type: RefType
        self.differentiatedServiceField = None      # type: PositiveInteger
        self.flowLabel = None                       # type: PositiveInteger
        self.multicastConnectorRefs = []            # type: List[RefType]
        self.pathMtuDiscoveryEnabled = None         # type: Boolean
        self.pduCollectionMaxBufferSize = None      # type: PositiveInteger
        self.pduCollectionTimeout = None            # type: TimeValue
        self.staticSocketConnections = []           # type: List[StaticSocketConnection]
        self.udpChecksumHandling = None             # type: UdpChecksumCalculationEnum

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

    def getApplicationEndpoint(self):
        return self.applicationEndpoint

    def setApplicationEndpoint(self, value):
        self.applicationEndpoint = value
        return self

    def getConnectorRef(self):
        return self.connectorRef

    def setConnectorRef(self, value):
        self.connectorRef = value
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

    def getMulticastConnectorRefs(self):
        return self.multicastConnectorRefs

    def addMulticastConnectorRef(self, value):
        self.multicastConnectorRefs.append(value)
        return self

    def getPathMtuDiscoveryEnabled(self):
        return self.pathMtuDiscoveryEnabled

    def setPathMtuDiscoveryEnabled(self, value):
        self.pathMtuDiscoveryEnabled = value
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

    def getStaticSocketConnections(self):
        return self.staticSocketConnections

    def addStaticSocketConnection(self, value):
        self.staticSocketConnections.append(value)
        return self

    def getUdpChecksumHandling(self):
        return self.udpChecksumHandling

    def setUdpChecksumHandling(self, value):
        self.udpChecksumHandling = value
        return self

class SoAdConfig(ARObject):
    def __init__(self):
        super().__init__()

        self.connections = []                               # type: List[SocketConnection]
        self.connectionBundles = []                         # type: List[SocketConnectionBundle]
        self.socketAddresses = []                           # type: List[SocketAddress]

    def getConnections(self):
        return self.connections

    def setConnections(self, value):
        self.connections = value
        return self

    def getConnectionBundles(self):
        return self.connectionBundles
    
    def createSocketConnectionBundle(self, short_name:str) -> SocketConnectionBundle:
        end_point = SocketConnectionBundle(self, short_name)
        self.connectionBundles.append(end_point)
        return end_point

    def setConnectionBundles(self, value):
        self.connectionBundles = value
        return self

    def getSocketAddresses(self):
        return self.socketAddresses

    def setSocketAddresses(self, value):
        self.socketAddresses = value
        return self


