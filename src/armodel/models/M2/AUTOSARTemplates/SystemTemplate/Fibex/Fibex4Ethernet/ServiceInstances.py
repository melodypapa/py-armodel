from abc import ABCMeta
from typing import List

from ......M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetCommunication import SocketConnection, SocketConnectionBundle
from ......M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, PositiveInteger, RefType, String, TimeValue
from ......M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from ......M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject


class TransportProtocolConfiguration(ARObject, metaclass = ABCMeta):
    def __init__(self):
        if type(self) == TransportProtocolConfiguration:
            raise NotImplementedError("TransportProtocolConfiguration is an abstract class.")
        
        super().__init__()

class GenericTp(TransportProtocolConfiguration):
    def __init__(self):
        super().__init__()

        self.tpAddress = None                                   # type: String
        self.tpTechnology = None                                # type: String

    def getTpAddress(self):
        return self.tpAddress

    def setTpAddress(self, value):
        self.tpAddress = value
        return self

    def getTpTechnology(self):
        return self.tpTechnology

    def setTpTechnology(self, value):
        self.tpTechnology = value
        return self


class TcpUdpConfig(TransportProtocolConfiguration, metaclass = ABCMeta):
    def __init__(self):
        if type(self) == TcpUdpConfig:
            raise NotImplementedError("TcpUdpConfig is an abstract class.")
        
        super().__init__()

class TpPort(ARObject):
    def __init__(self):
        super().__init__()

        self.dynamicallyAssigned = None                         # type: Boolean
        self.portNumber = None                                  # type: PositiveInteger

    def getDynamicallyAssigned(self):
        return self.dynamicallyAssigned

    def setDynamicallyAssigned(self, value):
        self.dynamicallyAssigned = value
        return self

    def getPortNumber(self):
        return self.portNumber

    def setPortNumber(self, value):
        self.portNumber = value
        return self


class UdpTp(TcpUdpConfig):
    def __init__(self):
        super().__init__()

        self.udpTpPort = None                                   # type: TpPort

    def getUdpTpPort(self):
        return self.udpTpPort

    def setUdpTpPort(self, value):
        self.udpTpPort = value
        return self


class TcpTp(TcpUdpConfig):
    def __init__(self):
        super().__init__()

        self.keepAliveInterval = None                           # type: TimeValue
        self.keepAliveProbesMax = None                          # type: PositiveInteger
        self.keepAlives = None                                  # type: Boolean
        self.keepAliveTime = None                               # type: TimeValue
        self.naglesAlgorithm = None                             # type: Boolean
        self.receiveWindowMin = None                            # type: PositiveInteger
        self.tcpRetransmissionTimeout = None                    # type: TimeValue
        self.tcpTpPort = None                                   # type: TpPort

    def getKeepAliveInterval(self):
        return self.keepAliveInterval

    def setKeepAliveInterval(self, value):
        self.keepAliveInterval = value
        return self

    def getKeepAliveProbesMax(self):
        return self.keepAliveProbesMax

    def setKeepAliveProbesMax(self, value):
        self.keepAliveProbesMax = value
        return self

    def getKeepAlives(self):
        return self.keepAlives

    def setKeepAlives(self, value):
        self.keepAlives = value
        return self

    def getKeepAliveTime(self):
        return self.keepAliveTime

    def setKeepAliveTime(self, value):
        self.keepAliveTime = value
        return self

    def getNaglesAlgorithm(self):
        return self.naglesAlgorithm

    def setNaglesAlgorithm(self, value):
        self.naglesAlgorithm = value
        return self

    def getReceiveWindowMin(self):
        return self.receiveWindowMin

    def setReceiveWindowMin(self, value):
        self.receiveWindowMin = value
        return self

    def getTcpRetransmissionTimeout(self):
        return self.tcpRetransmissionTimeout

    def setTcpRetransmissionTimeout(self, value):
        self.tcpRetransmissionTimeout = value
        return self

    def getTcpTpPort(self):
        return self.tcpTpPort

    def setTcpTpPort(self, value):
        self.tcpTpPort = value
        return self
    
class AbstractServiceInstance(Identifiable, metaclass = ABCMeta):
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) == AbstractServiceInstance:
            raise NotImplementedError("AbstractServiceInstance is an abstract class.")
        
        super().__init__(parent, short_name)

        # type: List[TagWithOptionalValue]
        self.capabilityRecords = []
        self.majorVersion = None                                # type: PositiveInteger
        # type: PduActivationRoutingGroup
        self.methodActivationRoutingGroup = None
        self.routingGroupRefs = []                              # type: List[RefType]

    def getCapabilityRecords(self):
        return self.capabilityRecords

    def addCapabilityRecord(self, value):
        if value is not None:
            self.capabilityRecords.append(value)
        return self

    def getMajorVersion(self):
        return self.majorVersion

    def setMajorVersion(self, value):
        if value is not None:
            self.majorVersion = value
        return self

    def getMethodActivationRoutingGroup(self):
        return self.methodActivationRoutingGroup

    def setMethodActivationRoutingGroup(self, value):
        if value is not None:
            self.methodActivationRoutingGroup = value
        return self

    def getRoutingGroupRefs(self):
        return self.routingGroupRefs

    def addRoutingGroupRef(self, value):
        if value is not None:
            self.routingGroupRefs.append(value)
        return self
    
class ConsumedEventGroup(Identifiable):
    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        self.applicationEndpointRef = None                                          # type: RefType
        self.autoRequire = None                                                     # type: Boolean
        self.eventGroupIdentifier = None                                            # type: PositiveInteger
        self.eventMulticastAddressRefs = []                                         # type: List[RefType]
        self.pduActivationRoutingGroups = []                                        # type: List[PduActivationRoutingGroup]
        self.priority = None                                                        # type: PositiveInteger
        self.routingGroupRefs = []                                                  # type: List[RefType]
        self.sdClientConfig = None                                                  # type: SdClientConfig
        self.sdClientTimerConfigRef = None                                          # type: RefType

    def getApplicationEndpointRef(self):
        return self.applicationEndpointRef

    def setApplicationEndpointRef(self, value):
        if value is not None:
            self.applicationEndpointRef = value
        return self

    def getAutoRequire(self):
        return self.autoRequire

    def setAutoRequire(self, value):
        if value is not None:
            self.autoRequire = value
        return self

    def getEventGroupIdentifier(self):
        return self.eventGroupIdentifier

    def setEventGroupIdentifier(self, value):
        if value is not None:
            self.eventGroupIdentifier = value
        return self

    def getEventMulticastAddressRefs(self):
        return self.eventMulticastAddressRefs

    def addEventMulticastAddressRef(self, value):
        if value is not None:
            self.eventMulticastAddressRefs.append(value)
        return self

    def getPduActivationRoutingGroups(self):
        return self.pduActivationRoutingGroups

    def setPduActivationRoutingGroups(self, value):
        if value is not None:
            self.pduActivationRoutingGroups = value
        return self

    def getPriority(self):
        return self.priority

    def setPriority(self, value):
        if value is not None:
            self.priority = value
        return self

    def getRoutingGroupRefs(self):
        return self.routingGroupRefs

    def addRoutingGroupRef(self, value):
        if value is not None:
            self.routingGroupRefs.append(value)
        return self

    def getSdClientConfig(self):
        return self.sdClientConfig

    def setSdClientConfig(self, value):
        if value is not None:
            self.sdClientConfig = value
        return self

    def getSdClientTimerConfigRef(self):
        return self.sdClientTimerConfigRef

    def setSdClientTimerConfigRef(self, value):
        if value is not None:
            self.sdClientTimerConfigRef = value
        return self


class ConsumedServiceInstance(AbstractServiceInstance):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.allowedServiceProviderRefs = []                                        # type: List[RefType]
        self.autoRequire = None                                                     # type: Boolean
        self.blocklistedVersions = []                                               # type: List[SomeipServiceVersion]
        self.consumedEventGroups = []                                               # type: List[ConsumedEventGroup]
        self.eventMulticastSubscriptionAddressRef = None                            # type: RefType
        self.instanceIdentifier = None                                              # type: AnyServiceInstanceId
        self.localUnicastAddressRefs = []                                           # type: List[RefType]
        self.minorVersion = None                                                    # type: AnyVersionString
        self.providedServiceInstanceRef = None                                      # type: RefType
        self.remoteUnicastAddressRefs = []                                          # type: List[RefType]
        self.sdClientConfig = None                                                  # type: SdClientConfig
        self.sdClientTimerConfigRef = None                                          # type: RefType
        self.serviceIdentifier = None                                               # type: PositiveInteger
        self.versionDrivenFindBehavior = None                                       # type: ServiceVersionAcceptanceKindEnum     

    def getAllowedServiceProviderRefs(self):
        return self.allowedServiceProviderRefs

    def setAllowedServiceProviderRefs(self, value):
        if value is not None:
            self.allowedServiceProviderRefs = value
        return self

    def getAutoRequire(self):
        return self.autoRequire

    def setAutoRequire(self, value):
        if value is not None:
            self.autoRequire = value
        return self

    def getBlocklistedVersions(self):
        return self.blocklistedVersions

    def setBlocklistedVersions(self, value):
        if value is not None:
            self.blocklistedVersions = value
        return self

    def getConsumedEventGroups(self):
        return self.consumedEventGroups

    def createConsumedEventGroup(self, short_name: str) -> ConsumedEventGroup:
        if short_name not in self.elements:
            group = ConsumedEventGroup(self, short_name)
            self.addElement(group)
            self.consumedEventGroups.append(group)
        return self.getElement(short_name)

    def getEventMulticastSubscriptionAddressRef(self):
        return self.eventMulticastSubscriptionAddressRef

    def setEventMulticastSubscriptionAddressRef(self, value):
        if value is not None:
            self.eventMulticastSubscriptionAddressRef = value
        return self

    def getInstanceIdentifier(self):
        return self.instanceIdentifier

    def setInstanceIdentifier(self, value):
        if value is not None:
            self.instanceIdentifier = value
        return self

    def getLocalUnicastAddressRefs(self):
        return self.localUnicastAddressRefs

    def setLocalUnicastAddressRefs(self, value):
        if value is not None:
            self.localUnicastAddressRefs = value
        return self

    def getMinorVersion(self):
        return self.minorVersion

    def setMinorVersion(self, value):
        if value is not None:
            self.minorVersion = value
        return self

    def getProvidedServiceInstanceRef(self):
        return self.providedServiceInstanceRef

    def setProvidedServiceInstanceRef(self, value):
        if value is not None:
            self.providedServiceInstanceRef = value
        return self

    def getRemoteUnicastAddressRefs(self):
        return self.remoteUnicastAddressRefs

    def setRemoteUnicastAddressRefs(self, value):
        if value is not None:
            self.remoteUnicastAddressRefs = value
        return self

    def getSdClientConfig(self):
        return self.sdClientConfig

    def setSdClientConfig(self, value):
        if value is not None:
            self.sdClientConfig = value
        return self

    def getSdClientTimerConfigRef(self):
        return self.sdClientTimerConfigRef

    def setSdClientTimerConfigRef(self, value):
        if value is not None:
            self.sdClientTimerConfigRef = value
        return self

    def getServiceIdentifier(self):
        return self.serviceIdentifier

    def setServiceIdentifier(self, value):
        if value is not None:
            self.serviceIdentifier = value
        return self

    def getVersionDrivenFindBehavior(self):
        return self.versionDrivenFindBehavior

    def setVersionDrivenFindBehavior(self, value):
        if value is not None:
            self.versionDrivenFindBehavior = value
        return self
   

class ApplicationEndpoint(Identifiable):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.consumedServiceInstances = []                      # type: List[ConsumedServiceInstance]
        self.maxNumberOfConnections = None                      # type: PositiveInteger
        self.networkEndpointRef = None                          # type: RefType
        self.priority = None                                    # type: PositiveInteger
        self.providedServiceInstances = []                      # type: List[ProvidedServiceInstance]
        self.tlsCryptoMappingRef = None                         # type: RefType
        self.tpConfiguration = None                             # type: TransportProtocolConfiguration

    def getConsumedServiceInstances(self):
        return self.consumedServiceInstances

    def createConsumedServiceInstance(self, short_name:str) -> ConsumedServiceInstance:
        if short_name not in self.elements:
            instance = ConsumedServiceInstance(self, short_name)
            self.addElement(instance)
            self.consumedServiceInstances.append(instance)
        return self.getElement(short_name)

    def getMaxNumberOfConnections(self):
        return self.maxNumberOfConnections

    def setMaxNumberOfConnections(self, value):
        self.maxNumberOfConnections = value
        return self

    def getNetworkEndpointRef(self):
        return self.networkEndpointRef

    def setNetworkEndpointRef(self, value):
        self.networkEndpointRef = value
        return self

    def getPriority(self):
        return self.priority

    def setPriority(self, value):
        self.priority = value
        return self

    def getProvidedServiceInstances(self):
        return self.providedServiceInstances

    def addProvidedServiceInstance(self, value):
        self.providedServiceInstances.append(value)
        return self

    def getTlsCryptoMappingRef(self):
        return self.tlsCryptoMappingRef

    def setTlsCryptoMappingRef(self, value):
        self.tlsCryptoMappingRef = value
        return self

    def getTpConfiguration(self):
        return self.tpConfiguration

    def setTpConfiguration(self, value):
        self.tpConfiguration = value
        return self

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
        self.portAddress = None                     # type: PositiveInteger
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

    def createApplicationEndpoint(self, short_name:str) -> ApplicationEndpoint:
        end_point = ApplicationEndpoint(self, short_name)
        self.applicationEndpoint = end_point
        return end_point

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
    
    def getPortAddress(self):
        return self.portAddress

    def setPortAddress(self, value):
        self.portAddress = value
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
        bundle = SocketConnectionBundle(self, short_name)
        self.connectionBundles.append(bundle)
        return bundle

    def setConnectionBundles(self, value):
        self.connectionBundles = value
        return self

    def getSocketAddresses(self):
        return self.socketAddresses

    def createSocketAddress(self, short_name:str) -> SocketAddress:
        address = SocketAddress(self, short_name)
        self.socketAddresses.append(address)
        return address


