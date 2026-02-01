# This module contains AUTOSAR System Template classes for service instances
# It defines consumed and provided service instances, application endpoints, and SOAD configurations

from abc import ABC
from typing import List

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, PositiveInteger, RefType, String, TimeValue
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import RequestResponseDelay
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetCommunication import SocketConnection, SocketConnectionBundle

class TransportProtocolConfiguration(ARObject, ABC):
    """
    Abstract base class for transport protocol configurations,
    defining the common properties and behavior for different
    transport protocols (TCP, UDP, etc.) used in service-oriented
    communication.
    """
    def __init__(self):
        if type(self) == TransportProtocolConfiguration:
            raise TypeError("TransportProtocolConfiguration is an abstract class.")
        
        super().__init__()

class GenericTp(TransportProtocolConfiguration):
    """
    Defines generic transport protocol configuration properties,
    including address and technology specifications for custom
    transport protocol implementations.
    """
    def __init__(self):
        super().__init__()

        self.tpAddress: String = None
        self.tpTechnology: String = None

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


class TcpUdpConfig(TransportProtocolConfiguration, ABC):
    """
    Abstract base class for TCP and UDP transport protocol configurations,
    defining common properties for both connection-oriented and
    connectionless transport protocols.
    """
    def __init__(self):
        if type(self) == TcpUdpConfig:
            raise TypeError("TcpUdpConfig is an abstract class.")
        
        super().__init__()

class TpPort(ARObject):
    """
    Defines properties for a transport protocol port, including
    port number and dynamic assignment capabilities for network
    communication endpoints.
    """
    def __init__(self):
        super().__init__()

        self.dynamicallyAssigned: Boolean = None
        self.portNumber: PositiveInteger = None

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
    """
    Defines UDP (User Datagram Protocol) transport protocol configuration,
    specifying UDP-specific port configuration for unreliable but fast
    datagram-based communication services.
    """
    def __init__(self):
        super().__init__()

        self.udpTpPort: TpPort = None

    def getUdpTpPort(self):
        return self.udpTpPort

    def setUdpTpPort(self, value):
        self.udpTpPort = value
        return self


class TcpTp(TcpUdpConfig):
    """
    Defines TCP (Transmission Control Protocol) transport protocol configuration,
    specifying TCP-specific properties such as keep-alive settings, retransmission
    timeouts, and flow control parameters for reliable connection-oriented communication.
    """
    def __init__(self):
        super().__init__()

        self.keepAliveInterval: TimeValue = None
        self.keepAliveProbesMax: PositiveInteger = None
        self.keepAlives: Boolean = None
        self.keepAliveTime: TimeValue = None
        self.naglesAlgorithm: Boolean = None
        self.receiveWindowMin: PositiveInteger = None
        self.tcpRetransmissionTimeout: TimeValue = None
        self.tcpTpPort: TpPort = None

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
    
class AbstractServiceInstance(Identifiable, ABC):
    """
    Abstract base class for service instances, defining common properties
    for both consumed and provided services in the AUTOSAR service-oriented
    architecture.
    """
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) == AbstractServiceInstance:
            raise TypeError("AbstractServiceInstance is an abstract class.")
        
        super().__init__(parent, short_name)

        self.capabilityRecords: List = []      # type: List[TagWithOptionalValue]
        self.majorVersion: PositiveInteger = None
        self.methodActivationRoutingGroup = None        # type: PduActivationRoutingGroup
        self.routingGroupRefs: List[RefType] = []                              # type: List[RefType]

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
    """
    Defines a consumed event group for service-oriented communication,
    specifying how events are consumed by service clients including
    application endpoint references and event group identifiers.
    """
    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        self.applicationEndpointRef: RefType = None
        self.autoRequire: Boolean = None
        self.eventGroupIdentifier: PositiveInteger = None
        self.eventMulticastAddressRefs: List[RefType] = []
        self.pduActivationRoutingGroups: List = []
        self.priority: PositiveInteger = None
        self.routingGroupRefs: List[RefType] = []
        self.sdClientConfig = None
        self.sdClientTimerConfigRef: RefType = None

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
    """
    Represents a consumed service instance in the AUTOSAR service-oriented
    architecture, defining how services are consumed by clients including
    provider references, service identifiers, and client configuration.
    """
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.allowedServiceProviderRefs: List[RefType] = []
        self.autoRequire: Boolean = None
        self.blocklistedVersions: List = []
        self.consumedEventGroups: List[ConsumedEventGroup] = []
        self.eventMulticastSubscriptionAddressRef: RefType = None
        self.instanceIdentifier = None
        self.localUnicastAddressRefs: List[RefType] = []
        self.minorVersion = None
        self.providedServiceInstanceRef: RefType = None
        self.remoteUnicastAddressRefs: List[RefType] = []
        self.sdClientConfig = None
        self.sdClientTimerConfigRef: RefType = None
        self.serviceIdentifier: PositiveInteger = None
        self.versionDrivenFindBehavior = None     

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
    
class InitialSdDelayConfig(ARObject):
    """
    Configures initial delay parameters for Service Discovery (SD)
    operations, defining the timing behavior for initial service
    discovery attempts and repetitions.
    """
    def __init__(self):
        super().__init__()

        self.initialDelayMaxValue: TimeValue = None
        self.initialDelayMinValue: TimeValue = None
        self.initialRepetitionsBaseDelay: TimeValue = None
        self.initialRepetitionsMax: PositiveInteger = None

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

    
class SdServerConfig(ARObject):
    """
    Configures Service Discovery (SD) server properties, specifying
    service advertisement behavior, timing parameters, and version
    information for service providers in the network.
    """
    def __init__(self):
        super().__init__()

        self.capabilityRecords: List = []                             # type: List[TagWithOptionalValue]
        self.initialOfferBehavior: InitialSdDelayConfig = None
        self.offerCyclicDelay: TimeValue = None
        self.requestResponseDelay: RequestResponseDelay = None
        self.serverServiceMajorVersion: PositiveInteger = None
        self.serverServiceMinorVersion: PositiveInteger = None
        self.ttl: PositiveInteger = None

    def getCapabilityRecords(self):
        return self.capabilityRecords

    def setCapabilityRecords(self, value):
        if value is not None:
            self.capabilityRecords = value
        return self

    def getInitialOfferBehavior(self):
        return self.initialOfferBehavior

    def setInitialOfferBehavior(self, value):
        if value is not None:
            self.initialOfferBehavior = value
        return self

    def getOfferCyclicDelay(self):
        return self.offerCyclicDelay

    def setOfferCyclicDelay(self, value):
        if value is not None:
            self.offerCyclicDelay = value
        return self

    def getRequestResponseDelay(self):
        return self.requestResponseDelay

    def setRequestResponseDelay(self, value):
        if value is not None:
            self.requestResponseDelay = value
        return self

    def getServerServiceMajorVersion(self):
        return self.serverServiceMajorVersion

    def setServerServiceMajorVersion(self, value):
        if value is not None:
            self.serverServiceMajorVersion = value
        return self

    def getServerServiceMinorVersion(self):
        return self.serverServiceMinorVersion

    def setServerServiceMinorVersion(self, value):
        if value is not None:
            self.serverServiceMinorVersion = value
        return self

    def getTtl(self):
        return self.ttl

    def setTtl(self, value):
        if value is not None:
            self.ttl = value
        return self

    
class EventHandler(Identifiable):
    """
    Defines an event handler for service-oriented communication,
    specifying how events are processed by service providers including
    application endpoint references and service discovery configuration.
    """
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.applicationEndpointRef: RefType = None
        self.consumedEventGroupRefs: List[RefType] = []
        self.multicastThreshold: PositiveInteger = None
        self.routingGroupRefs: List[RefType] = []
        self.sdServerConfig = None

    def getApplicationEndpointRef(self):
        return self.applicationEndpointRef

    def setApplicationEndpointRef(self, value):
        if value is not None:
            self.applicationEndpointRef = value
        return self

    def getConsumedEventGroupRefs(self):
        return self.consumedEventGroupRefs

    def addConsumedEventGroupRef(self, value):
        if value is not None:
            self.consumedEventGroupRefs.append(value)
        return self

    def getMulticastThreshold(self):
        return self.multicastThreshold

    def setMulticastThreshold(self, value):
        if value is not None:
            self.multicastThreshold = value
        return self

    def getRoutingGroupRefs(self):
        return self.routingGroupRefs

    def addRoutingGroupRef(self, value):
        if value is not None:
            self.routingGroupRefs.append(value)
        return self

    def getSdServerConfig(self):
        return self.sdServerConfig

    def setSdServerConfig(self, value):
        if value is not None:
            self.sdServerConfig = value
        return self


class ProvidedServiceInstance(AbstractServiceInstance):
    """
    Represents a provided service instance in the AUTOSAR service-oriented
    architecture, defining how services are provided to clients including
    service identifiers, instance identifiers, and server configuration.
    """
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.eventHandlers: List[EventHandler] = []
        self.instanceIdentifier: PositiveInteger = None
        self.priority: PositiveInteger = None
        self.sdServerConfig = None
        self.serviceIdentifier: PositiveInteger = None

    def getEventHandlers(self):
        return self.eventHandlers

    def createEventHandler(self, short_name:str) -> EventHandler:
        if short_name not in self.elements:
            instance = EventHandler(self, short_name)
            self.addElement(instance)
            self.eventHandlers.append(instance)
        return self.getElement(short_name)

    def getInstanceIdentifier(self):
        return self.instanceIdentifier

    def setInstanceIdentifier(self, value):
        if value is not None:
            self.instanceIdentifier = value
        return self

    def getPriority(self):
        return self.priority

    def setPriority(self, value):
        if value is not None:
            self.priority = value
        return self

    def getSdServerConfig(self):
        return self.sdServerConfig

    def setSdServerConfig(self, value):
        if value is not None:
            self.sdServerConfig = value
        return self

    def getServiceIdentifier(self):
        return self.serviceIdentifier

    def setServiceIdentifier(self, value):
        if value is not None:
            self.serviceIdentifier = value
        return self


class ApplicationEndpoint(Identifiable):
    """
    Defines an application endpoint for service-oriented communication,
    specifying the interface between applications and the service
    infrastructure including network endpoint references and service instances.
    """
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.consumedServiceInstances: List[ConsumedServiceInstance] = []
        self.maxNumberOfConnections: PositiveInteger = None
        self.networkEndpointRef: RefType = None
        self.priority: PositiveInteger = None
        self.providedServiceInstances: List[ProvidedServiceInstance] = []
        self.tlsCryptoMappingRef: RefType = None
        self.tpConfiguration = None

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

    def createProvidedServiceInstance(self, short_name:str) -> ProvidedServiceInstance:
        if short_name not in self.elements:
            instance = ProvidedServiceInstance(self, short_name)
            self.addElement(instance)
            self.providedServiceInstances.append(instance)
        return self.getElement(short_name)
    
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
    """
    Defines a socket address for network communication, specifying
    port addresses, connection properties, and socket configuration
    for TCP/IP communication endpoints.
    """
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.allowedIPv6ExtHeadersRef: RefType = None
        self.allowedTcpOptionsRef: RefType = None
        self.applicationEndpoint: ApplicationEndpoint = None
        self.connectorRef: RefType = None
        self.differentiatedServiceField: PositiveInteger = None
        self.flowLabel: PositiveInteger = None
        self.multicastConnectorRefs: List[RefType] = []
        self.pathMtuDiscoveryEnabled: Boolean = None
        self.pduCollectionMaxBufferSize: PositiveInteger = None
        self.pduCollectionTimeout: TimeValue = None
        self.portAddress: PositiveInteger = None
        self.staticSocketConnections = []
        self.udpChecksumHandling = None

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
    """
    Defines Socket Adaptor (SoAd) configuration, specifying socket
    connections, connection bundles, and socket address configurations
    for TCP/IP communication management in AUTOSAR systems.
    """
    def __init__(self):
        super().__init__()

        self.connections: List[SocketConnection] = []
        self.connectionBundles: List[SocketConnectionBundle] = []
        self.socketAddresses: List[SocketAddress] = []                           # type: List[SocketAddress]

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