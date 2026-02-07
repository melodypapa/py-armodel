from abc import ABC
from typing import Union

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
    Referrable,
)
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import (
    CommunicationCluster,
    CommunicationConnector,
    CommunicationController,
)


class MacMulticastGroup(Identifiable):
    """
    Represents a MAC multicast group used in Ethernet communication,
    defining multicast addresses that can be used for group-based
    communication in the network topology.
    """
    def __init__(self, parent, short_name) -> None:
        super().__init__(parent, short_name)

        self.macMulticastAddress: Union[MacAddressString, None] = None

    def getMacMulticastAddress(self):
        return self.macMulticastAddress

    def setMacMulticastAddress(self, value):
        if value is not None:
            self.macMulticastAddress = value
        return self


class EthernetCluster(CommunicationCluster):
    """
    Defines an Ethernet communication cluster in the system topology,
    specifying properties for Ethernet network communication including
    coupling ports, startup timing, and multicast group configurations.
    """
    def __init__(self, parent: ARObject, short_name: str) -> None:
        super().__init__(parent, short_name)

        self.couplingPorts = []                                             # type: List[CouplingPortConnection]
        self.couplingPortStartupActiveTime: Union[TimeValue, None] = None
        self.couplingPortSwitchoffDelay: Union[TimeValue, None] = None
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


class CouplingPortStructuralElement(Identifiable, ABC):
    """
    Abstract base class for coupling port structural elements in Ethernet
    switches and bridges, defining common properties and behavior for
    various types of coupling port components.
    """
    def __init__(self, parent: ARObject, short_name: str) -> None:
        if type(self) is CouplingPortStructuralElement:
            raise TypeError("CouplingPortStructuralElement is an abstract class.")

        super().__init__(parent, short_name)


class CouplingPortFifo(CouplingPortStructuralElement):
    """
    Defines a FIFO (First In, First Out) buffer for coupling ports in
    Ethernet switches, specifying traffic class assignments, minimum
    buffer lengths, and preemption support properties.
    """
    def __init__(self, parent: ARObject, short_name: str) -> None:
        super().__init__(parent, short_name)

        self.assignedTrafficClasses = []                            # type: List[PositiveInteger]
        self.minimumFifoLength: Union[PositiveInteger, None] = None
        self.shaper: Union[CouplingPortAbstractShaper, None] = None
        self.trafficClassPreemptionSupport: Union[EthernetCouplingPortPreemptionEnum, None] = None

    def getAssignedTrafficClasses(self):
        return self.assignedTrafficClasses

    def addAssignedTrafficClass(self, value):
        if value is not None:
            self.assignedTrafficClasses.append(value)
        return self

    def getMinimumFifoLength(self):
        return self.minimumFifoLength

    def setMinimumFifoLength(self, value):
        if value is not None:
            self.minimumFifoLength = value
        return self

    def getShaper(self):
        return self.shaper

    def setShaper(self, value):
        if value is not None:
            self.shaper = value
        return self

    def getTrafficClassPreemptionSupport(self):
        return self.trafficClassPreemptionSupport

    def setTrafficClassPreemptionSupport(self, value):
        if value is not None:
            self.trafficClassPreemptionSupport = value
        return self


class CouplingPortScheduler(CouplingPortStructuralElement):
    """
    Defines a scheduler for coupling ports in Ethernet switches,
    specifying scheduling algorithms and predecessor relationships
    for managing traffic flow through the coupling ports.
    """
    def __init__(self, parent, short_name) -> None:
        super().__init__(parent, short_name)

        self.portScheduler: Union[EthernetCouplingPortSchedulerEnum, None] = None
        self.predecessorRefs = []                                   # type: List[RefType]

    def getPortScheduler(self):
        return self.portScheduler

    def setPortScheduler(self, value):
        if value is not None:
            self.portScheduler = value
        return self

    def getPredecessorRefs(self):
        return self.predecessorRefs

    def addPredecessorRef(self, value):
        if value is not None:
            self.predecessorRefs.append(value)
        return self


class EthernetPriorityRegeneration(Referrable):
    """
    Defines priority regeneration rules for Ethernet traffic,
    specifying how ingress priorities are mapped to regenerated
    priorities for traffic management in the network.
    """
    def __init__(self, parent, short_name) -> None:
        super().__init__(parent, short_name)

        self.ingressPriority: Union[PositiveInteger, None] = None
        self.regeneratedPriority: Union[PositiveInteger, None] = None

    def getIngressPriority(self):
        return self.ingressPriority

    def setIngressPriority(self, value):
        if value is not None:
            self.ingressPriority = value
        return self

    def getRegeneratedPriority(self):
        return self.regeneratedPriority

    def setRegeneratedPriority(self, value):
        if value is not None:
            self.regeneratedPriority = value
        return self


class CouplingPortDetails(ARObject):
    """
    Contains detailed configuration information for coupling ports
    in Ethernet switches, including traffic class assignments, frame
    preemption support, and VLAN translation tables.
    """

    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass

    def __init__(self) -> None:
        super().__init__()

        self.couplingPortStructuralElements = []                    # type: List[CouplingPortStructuralElement]
        self.defaultTrafficClass: Union[PositiveInteger, None] = None
        self.ethernetPriorityRegenerations = []                     # type: List[EthernetPriorityRegeneration]
        self.ethernetTrafficClassAssignments = []                   # type: List[CouplingPortTrafficClassAssignment]
        self.framePreemptionSupport: Union[Boolean, None] = None
        self.globalTimeProps: Union[GlobalTimeCouplingPortProps, None] = None
        self.lastEgressSchedulerRef: Union[RefType, None] = None
        self.ratePolicies = []                                      # type: List[CouplingPortRatePolicy]
        self.vlanTranslationTables = []                             # type: List[EthernetVlanTranslationTable]

    def getCouplingPortStructuralElements(self):
        return self.couplingPortStructuralElements

    def createCouplingPortFifo(self, short_name: str) -> CouplingPortFifo:
        fifo = CouplingPortFifo(self, short_name)
        self.couplingPortStructuralElements.append(fifo)
        return fifo

    def createCouplingPortScheduler(self, short_name: str) -> CouplingPortScheduler:
        scheduler = CouplingPortScheduler(self, short_name)
        self.couplingPortStructuralElements.append(scheduler)
        return scheduler

    def createEthernetPriorityRegeneration(self, short_name: str) -> EthernetPriorityRegeneration:
        regeneration = EthernetPriorityRegeneration(self, short_name)
        self.ethernetPriorityRegenerations.append(regeneration)
        return regeneration

    def getDefaultTrafficClass(self):
        return self.defaultTrafficClass

    def setDefaultTrafficClass(self, value):
        if value is not None:
            self.defaultTrafficClass = value
        return self

    def getEthernetPriorityRegenerations(self):
        return self.ethernetPriorityRegenerations

    def setEthernetPriorityRegenerations(self, value):
        if value is not None:
            self.ethernetPriorityRegenerations = value
        return self

    def getEthernetTrafficClassAssignments(self):
        return self.ethernetTrafficClassAssignments

    def setEthernetTrafficClassAssignments(self, value):
        if value is not None:
            self.ethernetTrafficClassAssignments = value
        return self

    def getFramePreemptionSupport(self):
        return self.framePreemptionSupport

    def setFramePreemptionSupport(self, value):
        if value is not None:
            self.framePreemptionSupport = value
        return self

    def getGlobalTimeProps(self):
        return self.globalTimeProps

    def setGlobalTimeProps(self, value):
        if value is not None:
            self.globalTimeProps = value
        return self

    def getLastEgressSchedulerRef(self):
        return self.lastEgressSchedulerRef

    def setLastEgressSchedulerRef(self, value):
        if value is not None:
            self.lastEgressSchedulerRef = value
        return self

    def getRatePolicies(self):
        return self.ratePolicies

    def setRatePolicies(self, value):
        if value is not None:
            self.ratePolicies = value
        return self

    def getVlanTranslationTables(self):
        return self.vlanTranslationTables

    def setVlanTranslationTables(self, value):
        if value is not None:
            self.vlanTranslationTables = value
        return self


class VlanMembership(ARObject):
    """
    Defines VLAN membership properties for network interfaces,
    specifying default priorities, DHCP configurations, and VLAN
    tagging behaviors for Ethernet communication.
    """

    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass

    def __init__(self) -> None:
        super().__init__()

        self.defaultPriority: Union[PositiveInteger, None] = None
        self.dhcpAddressAssignment: Union[DhcpServerConfiguration, None] = None
        self.sendActivity: Union[EthernetSwitchVlanEgressTaggingEnum, None] = None
        self.vlanRef: Union[RefType, None] = None

    def getDefaultPriority(self):
        return self.defaultPriority

    def setDefaultPriority(self, value):
        if value is not None:
            self.defaultPriority = value
        return self

    def getDhcpAddressAssignment(self):
        return self.dhcpAddressAssignment

    def setDhcpAddressAssignment(self, value):
        if value is not None:
            self.dhcpAddressAssignment = value
        return self

    def getSendActivity(self):
        return self.sendActivity

    def setSendActivity(self, value):
        if value is not None:
            self.sendActivity = value
        return self

    def getVlanRef(self):
        return self.vlanRef

    def setVlanRef(self, value):
        if value is not None:
            self.vlanRef = value
        return self


class CouplingPort(Identifiable):
    """
    Defines a coupling port in an Ethernet switch or bridge,
    specifying connection negotiation behavior, MAC layer type,
    physical layer type, and VLAN membership configurations.
    """
    def __init__(self, parent, short_name) -> None:
        super().__init__(parent, short_name)

        self.connectionNegotiationBehavior: Union[EthernetConnectionNegotiationEnum, None] = None
        self.couplingPortDetails: Union[CouplingPortDetails, None] = None
        self.couplingPortRole: Union[CouplingPortRoleEnum, None] = None
        self.defaultVlanRef: Union[RefType, None] = None
        self.macAddressVlanAssignments = []                         # type: List[MacAddressVlanMembership]
        self.macLayerType: Union[EthernetMacLayerTypeEnum, None] = None
        self.macMulticastAddressRefs = []                           # type: List[RefType]
        self.macSecProps = []                                       # type: List[MacSecProps]
        self.physicalLayerType: Union[EthernetPhysicalLayerTypeEnum, None] = None
        self.plcaProps: Union[PlcaProps, None] = None
        self.pncMappingRefs = []                                    # type: List[RefType]
        self.receiveActivity: Union[EthernetSwitchVlanIngressTagEnum, None] = None
        self.vlanMemberships = []                                   # type: List[VlanMembership]
        self.wakeupSleepOnDatalineConfigRef: Union[RefType, None] = None

    def getConnectionNegotiationBehavior(self):
        return self.connectionNegotiationBehavior

    def setConnectionNegotiationBehavior(self, value):
        if value is not None:
            self.connectionNegotiationBehavior = value
        return self

    def getCouplingPortDetails(self):
        return self.couplingPortDetails

    def setCouplingPortDetails(self, value):
        if value is not None:
            self.couplingPortDetails = value
        return self

    def getCouplingPortRole(self):
        return self.couplingPortRole

    def setCouplingPortRole(self, value):
        if value is not None:
            self.couplingPortRole = value
        return self

    def getDefaultVlanRef(self):
        return self.defaultVlanRef

    def setDefaultVlanRef(self, value):
        if value is not None:
            self.defaultVlanRef = value
        return self

    def getMacAddressVlanAssignments(self):
        return self.macAddressVlanAssignments

    def setMacAddressVlanAssignments(self, value):
        if value is not None:
            self.macAddressVlanAssignments = value
        return self

    def getMacLayerType(self):
        return self.macLayerType

    def setMacLayerType(self, value):
        if value is not None:
            self.macLayerType = value
        return self

    def getMacMulticastAddressRefs(self):
        return self.macMulticastAddressRefs

    def setMacMulticastAddressRefs(self, value):
        if value is not None:
            self.macMulticastAddressRefs = value
        return self

    def getMacSecProps(self):
        return self.macSecProps

    def setMacSecProps(self, value):
        if value is not None:
            self.macSecProps = value
        return self

    def getPhysicalLayerType(self):
        return self.physicalLayerType

    def setPhysicalLayerType(self, value):
        if value is not None:
            self.physicalLayerType = value
        return self

    def getPlcaProps(self):
        return self.plcaProps

    def setPlcaProps(self, value):
        if value is not None:
            self.plcaProps = value
        return self

    def getPncMappingRefs(self):
        return self.pncMappingRefs

    def setPncMappingRefs(self, value):
        if value is not None:
            self.pncMappingRefs = value
        return self

    def getReceiveActivity(self):
        return self.receiveActivity

    def setReceiveActivity(self, value):
        if value is not None:
            self.receiveActivity = value
        return self

    def getVlanMemberships(self):
        return self.vlanMemberships

    def addVlanMembership(self, value):
        if value is not None:
            self.vlanMemberships.append(value)
        return self

    def getWakeupSleepOnDatalineConfigRef(self):
        return self.wakeupSleepOnDatalineConfigRef

    def setWakeupSleepOnDatalineConfigRef(self, value):
        if value is not None:
            self.wakeupSleepOnDatalineConfigRef = value
        return self


class EthernetCommunicationController(CommunicationController):
    """
    Represents an Ethernet communication controller in the system,
    defining properties for MAC configuration, coupling ports,
    and communication buffer management for Ethernet networking.
    """
    def __init__(self, parent: ARObject, short_name: str) -> None:
        super().__init__(parent, short_name)

        self.canXlConfigRef: Union[RefType, None] = None
        self.couplingPorts = []                             # type: List[CouplingPort]
        self.macLayerType: Union[EthernetMacLayerTypeEnum, None] = None
        self.macUnicastAddress: Union[MacAddressString, None] = None
        self.maximumReceiveBufferLength: Union[Integer, None] = None
        self.maximumTransmitBufferLength: Union[Integer, None] = None
        self.slaveActAsPassiveCommunicationSlave: Union[Boolean, None] = None
        self.slaveQualifiedUnexpectedLinkDownTime: Union[TimeValue, None] = None

    def getCanXlConfigRef(self):
        return self.canXlConfigRef

    def setCanXlConfigRef(self, value):
        self.canXlConfigRef = value
        return self

    def getCouplingPorts(self):
        return self.couplingPorts

    def createCouplingPort(self, short_name: str) -> CouplingPort:
        if (short_name not in self.elements):
            group = CouplingPort(self, short_name)
            self.addElement(group)
            self.couplingPorts.append(group)
        return self.getElement(short_name)

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
    """
    Defines an Ethernet communication connector that links Ethernet
    controllers to communication channels, specifying MTU settings,
    network endpoint references, and path MTU configuration properties.
    """
    def __init__(self, parent: ARObject, short_name: str) -> None:
        super().__init__(parent, short_name)

        self.ethIpPropsRef: Union[RefType, None] = None
        self.maximumTransmissionUnit: Union[PositiveInteger, None] = None
        self.neighborCacheSize: Union[PositiveInteger, None] = None
        self.networkEndpointRefs = []                           # type: List[RefType]       ## 4.3.1 Version
        self.pathMtuEnabled: Union[Boolean, None] = None
        self.pathMtuTimeout: Union[TimeValue, None] = None

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

    def getNetworkEndpointRefs(self):
        return self.networkEndpointRefs

    def addNetworkEndpointRef(self, value):
        if value is not None:
            self.networkEndpointRefs.append(value)
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
    """
    Defines the delay constraints for request-response communication
    patterns in service-oriented architectures, specifying minimum
    and maximum acceptable response times.
    """

    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass

    def __init__(self) -> None:
        super().__init__()

        self.maxValue: Union[TimeValue, None] = None
        self.minValue: Union[TimeValue, None] = None

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
    """
    Configures the initial delay parameters for Service Discovery (SD)
    communication, defining minimum and maximum delay values and
    repetition timing for service announcements and requests.
    """

    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass

    def __init__(self) -> None:
        super().__init__()

        self.initialDelayMaxValue: Union[TimeValue, None] = None
        self.initialDelayMinValue: Union[TimeValue, None] = None
        self.initialRepetitionsBaseDelay: Union[TimeValue, None] = None
        self.initialRepetitionsMax: Union[PositiveInteger, None] = None

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
    """
    Configures Service Discovery (SD) client properties, including
    service version requirements, delay configurations, and TTL settings
    for service discovery communication in the network.
    """

    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass

    def __init__(self) -> None:
        super().__init__()

        self.capabilityRecord: Union[TagWithOptionalValue, None] = None
        self.clientServiceMajorVersion: Union[PositiveInteger, None] = None
        self.clientServiceMinorVersion: Union[PositiveInteger, None] = None
        self.initialFindBehavior: Union[InitialSdDelayConfig, None] = None
        self.requestResponseDelay: Union[RequestResponseDelay, None] = None
        self.ttl: Union[PositiveInteger, None] = None

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
