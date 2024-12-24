from abc import ABCMeta
from typing import List
from ......M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from ......M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from ......M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, Ip4AddressString, Ip6AddressString, PositiveInteger, String, TimeValue

class NetworkEndpointAddress(ARObject, metaclass = ABCMeta):
    def __init__(self):
        if type(self) == NetworkEndpointAddress:
            raise NotImplementedError("NetworkEndpointAddress is an abstract class.")
        
        super().__init__()
        
class Ipv4Configuration(NetworkEndpointAddress):
    def __init__(self):
        super().__init__()

        self.assignmentPriority = None                              # type: PositiveInteger    
        self.defaultGateway = None                                  # type: Ip4AddressString
        self.dnsServerAddresses = []                                # type: List[Ip4AddressString]
        self.ipAddressKeepBehavior = None                           # type: IpAddressKeepEnum
        self.ipv4Address = None                                     # type: Ip4AddressString
        self.ipv4AddressSource = None                               # type: Ipv4AddressSourceEnum
        self.networkMask = None                                     # type: Ip4AddressString
        self.ttl = None                                             # type: PositiveInteger

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
    def __init__(self):
        super().__init__()

        self.assignmentPriority = None                              # type: PositiveInteger
        self.defaultRouter = None                                   # type: Ip6AddressString
        self.dnsServerAddresses = []                                # type: List[Ip6AddressString]
        self.enableAnycast = None                                   # type: Boolean
        self.hopCount = None                                        # type: PositiveInteger
        self.ipAddressKeepBehavior = None                           # type: IpAddressKeepEnum
        self.ipAddressPrefixLength = None                           # type: PositiveInteger
        self.ipv6Address = None                                     # type: Ip6AddressString
        self.ipv6AddressSource = None                               # type: Ipv6AddressSourceEnum

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
    def __init__(self):
        super().__init__()

        self.doIpEntityRole = None                                  # type: DoIpEntityRoleEnum

    def getDoIpEntityRole(self):
        return self.doIpEntityRole

    def setDoIpEntityRole(self, value):
        if value is not None:
            self.doIpEntityRole = value
        return self
    
class TimeSyncClientConfiguration(ARObject):
    def __init__(self):
        super().__init__()

        self.orderedMasters = []                                    # type: List[OrderedMaster]
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


class TimeSyncServerConfiguration(ARObject):
    def __init__(self):
        super().__init__()

        self.priority = None                                        # type: PositiveInteger
        self.syncInterval = None                                    # type: TimeValue
        self.timeSyncServerIdentifier = None                        # type: String
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
    def __init__(self):
        super().__init__()

        self.timeSyncClient = None                                  # type: TimeSyncClientConfiguration
        self.timeSyncServer = None                                  # type: TimeSyncServerConfiguration

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
    def __init__(self):
        super().__init__()

        self.doIpEntity = None                                      # type: DoIpEntity
        self.timeSynchronization = None                             # type: TimeSynchronization

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
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.fullyQualifiedDomainName = None                        # type: String
        self.infrastructureServices = None                          # type: InfrastructureServices
        self.ipSecConfig = None                                     # type: IPSecConfig
        self.networkEndpointAddresses = []                          # type: List[NetworkEndpointAddress]
        self.priority = None                                        # type: PositiveInteger

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