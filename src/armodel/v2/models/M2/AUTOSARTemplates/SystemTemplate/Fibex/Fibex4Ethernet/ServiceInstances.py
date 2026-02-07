# This module contains AUTOSAR System Template classes for service instances
# It defines consumed and provided service instances, application endpoints, and SOAD configurations

from abc import ABC
from typing import List, Union

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
    Boolean,
    PositiveInteger,
    RefType,
    String,
    TimeValue,
)
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetCommunication import (
    PduActivationRoutingGroup,
    RequestResponseDelay,
    SocketConnectionBundle,
)


class TransportProtocolConfiguration(ARObject, ABC):
    """
    Abstract base class for transport protocol configurations,
    defining the common properties and behavior for different
    transport protocols (TCP, UDP, etc.) used in service-oriented
    communication.
    """
    def __init__(self) -> None:
        if type(self) is TransportProtocolConfiguration:
            raise TypeError("TransportProtocolConfiguration is an abstract class.")

        super().__init__()

class GenericTp(TransportProtocolConfiguration):
    """
    Defines generic transport protocol configuration properties,
    including address and technology specifications for custom
    transport protocol implementations.
    """
    def __init__(self) -> None:
        super().__init__()

        self.tpAddress: Union[Union[String, None] , None] = None
        self.tpTechnology: Union[Union[String, None] , None] = None

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
    def __init__(self) -> None:
        if type(self) is TcpUdpConfig:
            raise TypeError("TcpUdpConfig is an abstract class.")

        super().__init__()

class TpPort(ARObject):
    """
    Defines properties for a transport protocol port, including
    port number and dynamic assignment capabilities for network
    communication endpoints.
    """

    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass

    def __init__(self) -> None:
        super().__init__()

        self.dynamicallyAssigned: Union[Union[Boolean, None] , None] = None
        self.portNumber: Union[Union[PositiveInteger, None] , None] = None

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
    def __init__(self) -> None:
        super().__init__()

        self.udpTpPort: Union[Union[TpPort, None] , None] = None

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
    def __init__(self) -> None:
        super().__init__()

        self.keepAliveInterval: Union[Union[TimeValue, None] , None] = None
        self.keepAliveProbesMax: Union[Union[PositiveInteger, None] , None] = None
        self.keepAlives: Union[Union[Boolean, None] , None] = None
        self.keepAliveTime: Union[Union[TimeValue, None] , None] = None
        self.naglesAlgorithm: Union[Union[Boolean, None] , None] = None
        self.receiveWindowMin: Union[Union[PositiveInteger, None] , None] = None
        self.tcpRetransmissionTimeout: Union[Union[TimeValue, None] , None] = None
        self.tcpTpPort: Union[Union[TpPort, None] , None] = None

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
    def __init__(self, parent: ARObject, short_name: str) -> None:
        if type(self) is AbstractServiceInstance:
            raise TypeError("AbstractServiceInstance is an abstract class.")

        super().__init__(parent, short_name)

        self.capabilityRecords = []                                     # type: List[TagWithOptionalValue]
        self.majorVersion: Union[PositiveInteger, None] = None
        self.methodActivationRoutingGroup: Union[PduActivationRoutingGroup, None] = None
        self.routingGroupRefs = []                                      # type: List[RefType]

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
    def __init__(self, parent, short_name) -> None:
        super().__init__(parent, short_name)

        self.applicationEndpointRef: Union[Union[RefType, None] , None] = None
        self.autoRequire: Union[Union[Boolean, None] , None] = None
        self.eventGroupIdentifier: Union[Union[PositiveInteger, None] , None] = None
        self.eventMulticastAddressRefs: List[RefType] = []
        self.pduActivationRoutingGroups: List = []
        self.priority: Union[Union[PositiveInteger, None] , None] = None
        self.routingGroupRefs: List[RefType] = []
        self.sdClientConfig = None
        self.sdClientTimerConfigRef: Union[Union[RefType, None] , None] = None

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
    def __init__(self, parent: ARObject, short_name: str) -> None:
        super().__init__(parent, short_name)

        self.allowedServiceProviderRefs: List[RefType] = []
        self.autoRequire: Union[Union[Boolean, None] , None] = None
        self.blocklistedVersions: List = []
        self.consumedEventGroups: List[ConsumedEventGroup] = []
        self.eventMulticastSubscriptionAddressRef: Union[Union[RefType, None] , None] = None
        self.instanceIdentifier = None
        self.localUnicastAddressRefs: List[RefType] = []
        self.minorVersion = None
        self.providedServiceInstanceRef: Union[Union[RefType, None] , None] = None
        self.remoteUnicastAddressRefs: List[RefType] = []
        self.sdClientConfig = None
        self.sdClientTimerConfigRef: Union[Union[RefType, None] , None] = None
        self.serviceIdentifier: Union[Union[PositiveInteger, None] , None] = None
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

    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass

    def __init__(self) -> None:
        super().__init__()

        self.initialDelayMaxValue: Union[Union[TimeValue, None] , None] = None
        self.initialDelayMinValue: Union[Union[TimeValue, None] , None] = None
        self.initialRepetitionsBaseDelay: Union[Union[TimeValue, None] , None] = None
        self.initialRepetitionsMax: Union[Union[PositiveInteger, None] , None] = None

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

    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass

    def __init__(self) -> None:
        super().__init__()

        self.capabilityRecords = []                                     # type: List[TagWithOptionalValue]
        self.initialOfferBehavior: Union[InitialSdDelayConfig, None] = None
        self.offerCyclicDelay: Union[TimeValue, None] = None
        self.requestResponseDelay: Union[RequestResponseDelay, None] = None
        self.serverServiceMajorVersion: Union[PositiveInteger, None] = None
        self.serverServiceMinorVersion: Union[PositiveInteger, None] = None
        self.ttl: Union[PositiveInteger, None] = None

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
    def __init__(self, parent: ARObject, short_name: str) -> None:
        super().__init__(parent, short_name)

        self.applicationEndpointRef: Union[Union[RefType, None] , None] = None
        self.consumedEventGroupRefs: List[RefType] = []
        self.multicastThreshold: Union[Union[PositiveInteger, None] , None] = None
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
    def __init__(self, parent: ARObject, short_name: str) -> None:
        super().__init__(parent, short_name)

        self.eventHandlers: List[EventHandler] = []
        self.instanceIdentifier: Union[Union[PositiveInteger, None] , None] = None
        self.priority: Union[Union[PositiveInteger, None] , None] = None
        self.sdServerConfig = None
        self.serviceIdentifier: Union[Union[PositiveInteger, None] , None] = None

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
    def __init__(self, parent: ARObject, short_name: str) -> None:
        super().__init__(parent, short_name)

        self.consumedServiceInstances: List[ConsumedServiceInstance] = []
        self.maxNumberOfConnections: Union[Union[PositiveInteger, None] , None] = None
        self.networkEndpointRef: Union[Union[RefType, None] , None] = None
        self.priority: Union[Union[PositiveInteger, None] , None] = None
        self.providedServiceInstances: List[ProvidedServiceInstance] = []
        self.tlsCryptoMappingRef: Union[Union[RefType, None] , None] = None
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
    def __init__(self, parent: ARObject, short_name: str) -> None:
        super().__init__(parent, short_name)

        self.allowedIPv6ExtHeadersRef: Union[Union[RefType, None] , None] = None
        self.allowedTcpOptionsRef: Union[Union[RefType, None] , None] = None
        self.applicationEndpoint: Union[Union[ApplicationEndpoint, None] , None] = None
        self.connectorRef: Union[Union[RefType, None] , None] = None
        self.differentiatedServiceField: Union[Union[PositiveInteger, None] , None] = None
        self.flowLabel: Union[Union[PositiveInteger, None] , None] = None
        self.multicastConnectorRefs: List[RefType] = []
        self.pathMtuDiscoveryEnabled: Union[Union[Boolean, None] , None] = None
        self.pduCollectionMaxBufferSize: Union[Union[PositiveInteger, None] , None] = None
        self.pduCollectionTimeout: Union[Union[TimeValue, None] , None] = None
        self.portAddress: Union[Union[PositiveInteger, None] , None] = None
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

    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass

    def __init__(self) -> None:
        super().__init__()

        self.connections = []                                                   # type: List[SocketConnection]
        self.connectionBundles = []                                             # type: List[SocketConnectionBundle]
        self.socketAddresses = []                                               # type: List[SocketAddress]

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


class UdpChecksumCalculationEnum(AREnum):
    """Enumeration for UDP checksum calculation modes."""
    CALCULATE = "CALCULATE"
    DONT_CALCULATE = "DONT_CALCULATE"

    def __init__(self) -> None:
        super().__init__([
            UdpChecksumCalculationEnum.CALCULATE,
            UdpChecksumCalculationEnum.DONT_CALCULATE
        ])


class EventGroupControlTypeEnum(AREnum):
    """Enumeration for event group control types."""
    NONE = "NONE"
    CANCEL = "CANCEL"
    ACCEPT = "ACCEPT"
    STOP_OFFER = "STOP_OFFER"

    def __init__(self) -> None:
        super().__init__([
            EventGroupControlTypeEnum.NONE,
            EventGroupControlTypeEnum.CANCEL,
            EventGroupControlTypeEnum.ACCEPT,
            EventGroupControlTypeEnum.STOP_OFFER
        ])
