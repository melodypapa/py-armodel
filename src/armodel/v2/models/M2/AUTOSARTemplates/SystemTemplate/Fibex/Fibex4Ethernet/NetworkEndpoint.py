# This module contains AUTOSAR System Template classes for network endpoints
# It defines IP configuration, network addresses, and communication protocols for networked ECUs

from abc import ABC
from typing import List, Union

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
    Referrable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Ip4AddressString,
    Ip6AddressString,
    PositiveInteger,
    String,
    TimeValue,
)


class NetworkEndpointAddress(ARObject, ABC):
    """
    Abstract base class for network endpoint addresses, defining the
    common properties and behavior for different types of network
    addresses (IPv4, IPv6, etc.) used in AUTOSAR communication.
    """
    def __init__(self) -> None:
        if type(self) is NetworkEndpointAddress:
            raise TypeError("NetworkEndpointAddress is an abstract class.")

        super().__init__()

class Ipv4Configuration(NetworkEndpointAddress):
    """
    Defines IPv4 network configuration properties for a network endpoint,
    including IP addresses, network masks, DNS server addresses, and
    TTL settings for IPv4 communication.
    """
    def __init__(self) -> None:
        super().__init__()

        self.assignmentPriority: Union[Union[PositiveInteger, None] , None] = None
        self.defaultGateway: Union[Union[Ip4AddressString, None] , None] = None
        self.dnsServerAddresses: List[Ip4AddressString] = []
        self.ipAddressKeepBehavior = None
        self.ipv4Address: Union[Union[Ip4AddressString, None] , None] = None
        self.ipv4AddressSource = None
        self.networkMask: Union[Union[Ip4AddressString, None] , None] = None
        self.ttl: Union[Union[PositiveInteger, None] , None] = None

    def getAssignmentPriority(self):
        return self.assignmentPriority

    def setAssignmentPriority(self, value):
        self.assignmentPriority = value
        return self

    def getDefaultGateway(self):
        return self.defaultGateway

    def setDefaultGateway(self, value):
        self.defaultGateway = value
        return self

    def getDnsServerAddresses(self):
        return self.dnsServerAddresses

    def addDnsServerAddress(self, value):
        self.dnsServerAddresses.append(value)
        return self

    def getIpAddressKeepBehavior(self):
        return self.ipAddressKeepBehavior

    def setIpAddressKeepBehavior(self, value):
        self.ipAddressKeepBehavior = value
        return self

    def getIpv4Address(self):
        return self.ipv4Address

    def setIpv4Address(self, value):
        self.ipv4Address = value
        return self

    def getIpv4AddressSource(self):
        return self.ipv4AddressSource

    def setIpv4AddressSource(self, value):
        self.ipv4AddressSource = value
        return self

    def getNetworkMask(self):
        return self.networkMask

    def setNetworkMask(self, value):
        self.networkMask = value
        return self

    def getTtl(self):
        return self.ttl

    def setTtl(self, value):
        self.ttl = value
        return self

class Ipv6Configuration(NetworkEndpointAddress):
    """
    Defines IPv6 network configuration properties for a network endpoint,
    including IPv6 addresses, default router, DNS server addresses,
    and IPv6-specific communication parameters.
    """
    def __init__(self) -> None:
        super().__init__()

        self.assignmentPriority: Union[Union[PositiveInteger, None] , None] = None
        self.defaultRouter: Union[Union[Ip6AddressString, None] , None] = None
        self.dnsServerAddresses: List[Ip6AddressString] = []
        self.enableAnycast: Union[Union[Boolean, None] , None] = None
        self.hopCount: Union[Union[PositiveInteger, None] , None] = None
        self.ipAddressKeepBehavior = None
        self.ipAddressPrefixLength: Union[Union[PositiveInteger, None] , None] = None
        self.ipv6Address: Union[Union[Ip6AddressString, None] , None] = None
        self.ipv6AddressSource = None

    def getAssignmentPriority(self):
        return self.assignmentPriority

    def setAssignmentPriority(self, value):
        self.assignmentPriority = value
        return self

    def getDefaultRouter(self):
        return self.defaultRouter

    def setDefaultRouter(self, value):
        self.defaultRouter = value
        return self

    def getDnsServerAddresses(self):
        return self.dnsServerAddresses

    def setDnsServerAddresses(self, value):
        self.dnsServerAddresses = value
        return self

    def getEnableAnycast(self):
        return self.enableAnycast

    def setEnableAnycast(self, value):
        self.enableAnycast = value
        return self

    def getHopCount(self):
        return self.hopCount

    def setHopCount(self, value):
        self.hopCount = value
        return self

    def getIpAddressKeepBehavior(self):
        return self.ipAddressKeepBehavior

    def setIpAddressKeepBehavior(self, value):
        self.ipAddressKeepBehavior = value
        return self

    def getIpAddressPrefixLength(self):
        return self.ipAddressPrefixLength

    def setIpAddressPrefixLength(self, value):
        self.ipAddressPrefixLength = value
        return self

    def getIpv6Address(self):
        return self.ipv6Address

    def setIpv6Address(self, value):
        self.ipv6Address = value
        return self

    def getIpv6AddressSource(self):
        return self.ipv6AddressSource

    def setIpv6AddressSource(self, value):
        self.ipv6AddressSource = value
        return self

class DoIpEntity(ARObject):
    """
    Defines properties for a DoIP (Diagnostics over IP) entity,
    specifying the role and behavior of DoIP-enabled devices in
    the network for diagnostic communication purposes.
    """

    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass

    def __init__(self) -> None:
        super().__init__()

        self.doIpEntityRole = None                                  # type: DoIpEntityRoleEnum

    def getDoIpEntityRole(self):
        return self.doIpEntityRole

    def setDoIpEntityRole(self, value):
        if value is not None:
            self.doIpEntityRole = value
        return self

class TimeSyncClientConfiguration(ARObject):
    """
    Configures time synchronization client properties, defining
    ordered master relationships and time synchronization
    technology settings for network time coordination.
    """

    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass

    def __init__(self) -> None:
        super().__init__()

        self.orderedMasters = []
        self.timeSyncTechnology = None                              # type: TimeSyncTechnologyEnum

    def getOrderedMasters(self):
        return self.orderedMasters

    def addOrderedMaster(self, value):
        if value is not None:
            self.orderedMasters.append(value)
        return self

    def getTimeSyncTechnology(self):
        return self.timeSyncTechnology

    def setTimeSyncTechnology(self, value):
        if value is not None:
            self.timeSyncTechnology = value
        return self


class TimeSyncServerConfiguration(Referrable):
    """
    Configures time synchronization server properties, specifying
    priority, synchronization intervals, and time synchronization
    identifiers for network time coordination services.
    """
    def __init__(self, parent: ARObject, short_name: str) -> None:
        super().__init__(parent, short_name)

        self.priority: Union[Union[PositiveInteger, None] , None] = None
        self.syncInterval: Union[Union[TimeValue, None] , None] = None
        self.timeSyncServerIdentifier: Union[Union[String, None] , None] = None
        self.timeSyncTechnology = None                              # type: TimeSyncTechnologyEnum

    def getPriority(self):
        return self.priority

    def setPriority(self, value):
        if value is not None:
            self.priority = value
        return self

    def getSyncInterval(self):
        return self.syncInterval

    def setSyncInterval(self, value):
        if value is not None:
            self.syncInterval = value
        return self

    def getTimeSyncServerIdentifier(self):
        return self.timeSyncServerIdentifier

    def setTimeSyncServerIdentifier(self, value):
        if value is not None:
            self.timeSyncServerIdentifier = value
        return self

    def getTimeSyncTechnology(self):
        return self.timeSyncTechnology

    def setTimeSyncTechnology(self, value):
        if value is not None:
            self.timeSyncTechnology = value
        return self


class TimeSynchronization(ARObject):
    """
    Defines time synchronization configuration for network entities,
    including both client and server configurations for coordinated
    timing across the AUTOSAR system network.
    """

    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass

    def __init__(self) -> None:
        super().__init__()

        self.timeSyncClient: Union[Union[TimeSyncClientConfiguration, None] , None] = None
        self.timeSyncServer: Union[Union[TimeSyncServerConfiguration, None] , None] = None

    def getTimeSyncClient(self):
        return self.timeSyncClient

    def setTimeSyncClient(self, value):
        if value is not None:
            self.timeSyncClient = value
        return self

    def getTimeSyncServer(self):
        return self.timeSyncServer

    def setTimeSyncServer(self, value):
        if value is not None:
            self.timeSyncServer = value
        return self


class InfrastructureServices(ARObject):
    """
    Defines infrastructure services available at a network endpoint,
    including DoIP capabilities and time synchronization services
    for network management and coordination.
    """

    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass

    def __init__(self) -> None:
        super().__init__()

        self.doIpEntity: Union[Union[DoIpEntity, None] , None] = None
        self.timeSynchronization: Union[Union[TimeSynchronization, None] , None] = None

    def getDoIpEntity(self):
        return self.doIpEntity

    def setDoIpEntity(self, value):
        self.doIpEntity = value
        return self

    def getTimeSynchronization(self):
        return self.timeSynchronization

    def setTimeSynchronization(self, value):
        self.timeSynchronization = value
        return self

class NetworkEndpoint(Identifiable):
    """
    Represents a network endpoint in the AUTOSAR system, defining
    IP configuration, infrastructure services, and network address
    properties for communication nodes in the network.
    """
    def __init__(self, parent: ARObject, short_name: str) -> None:
        super().__init__(parent, short_name)

        self.fullyQualifiedDomainName: Union[Union[String, None] , None] = None
        self.infrastructureServices: Union[Union[InfrastructureServices, None] , None] = None
        self.ipSecConfig = None
        self.networkEndpointAddresses: List[NetworkEndpointAddress] = []
        self.priority: Union[Union[PositiveInteger, None] , None] = None

    def getFullyQualifiedDomainName(self):
        return self.fullyQualifiedDomainName

    def setFullyQualifiedDomainName(self, value):
        self.fullyQualifiedDomainName = value
        return self

    def getInfrastructureServices(self):
        return self.infrastructureServices

    def setInfrastructureServices(self, value):
        self.infrastructureServices = value
        return self

    def getIpSecConfig(self):
        return self.ipSecConfig

    def setIpSecConfig(self, value):
        self.ipSecConfig = value
        return self

    def getNetworkEndpointAddresses(self):
        return self.networkEndpointAddresses

    def addNetworkEndpointAddress(self, value):
        self.networkEndpointAddresses.append(value)
        return self

    def getPriority(self):
        return self.priority

    def setPriority(self, value):
        self.priority = value
        return self
