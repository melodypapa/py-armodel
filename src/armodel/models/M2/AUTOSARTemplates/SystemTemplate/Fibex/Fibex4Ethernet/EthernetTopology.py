from __future__ import annotations

from abc import ABC
from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Describable, Identifiable, Referrable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Ip4AddressString, Ip6AddressString, PositiveInteger, RefType, TimeValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import CommunicationCluster, CommunicationConnector
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import CommunicationController


class MacMulticastGroup(Identifiable):
    """
    Represents a MAC multicast group used in Ethernet communication,
    defining multicast addresses that can be used for group-based
    communication in the network topology.
    """

    # MacMulticastGroup method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getMacMulticastAddress       [x] impl  [ ] docstring  [ ] test
    # [ ] setMacMulticastAddress       [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        self.macMulticastAddress = None  # type: MacAddressString

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

    # EthernetCluster method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getCouplingPorts             [x] impl  [ ] docstring  [ ] test
    # [ ] addCouplingPort              [x] impl  [ ] docstring  [ ] test
    # [ ] getCouplingPortStartupActiveTime [x] impl  [ ] docstring  [ ] test
    # [ ] setCouplingPortStartupActiveTime [x] impl  [ ] docstring  [ ] test
    # [ ] getCouplingPortSwitchoffDelay [x] impl  [ ] docstring  [ ] test
    # [ ] setCouplingPortSwitchoffDelay [x] impl  [ ] docstring  [ ] test
    # [ ] getMacMulticastGroups        [x] impl  [ ] docstring  [ ] test
    # [ ] createMacMulticastGroup      [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.couplingPorts = []  # type: List[CouplingPortConnection]
        self.couplingPortStartupActiveTime = None  # type: TimeValue
        self.couplingPortSwitchoffDelay = None  # type: TimeValue
        self.macMulticastGroups = []  # type: List[MacMulticastGroup]

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
        if short_name not in self.elements:
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

    # CouplingPortStructuralElement method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is CouplingPortStructuralElement:
            raise TypeError("CouplingPortStructuralElement is an abstract class.")

        super().__init__(parent, short_name)


class CouplingPortFifo(CouplingPortStructuralElement):
    """
    Defines a FIFO for the CouplingPort egress structure.
    """

    # CouplingPortFifo method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.68, p.124
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] addAssignedTrafficClass      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getAssignedTrafficClasses    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] getMinimumFifoLength         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMinimumFifoLength         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getShaper                    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setShaper                    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Defines a set of Traffic Classes which shall be handled by this FIFO. range: 0-7
        self.assignedTrafficClasses: List[PositiveInteger] = []

        # FIFO minimum length in Byte. An actual configuration/ hardware may use a bigger value.
        self.minimumFifoLength: Optional[PositiveInteger] = None

        # Definition of the shaper to be used for the processing of this FIFO.
        self.shaper: Optional[ARObject] = None

    def addAssignedTrafficClass(self, value: Optional[PositiveInteger]) -> "CouplingPortFifo":
        """
        Defines a set of Traffic Classes which shall be handled by this FIFO. range: 0-7
        A None value is a no-op and does not append to assignedTrafficClasses.
        """
        if value is not None:
            self.assignedTrafficClasses.append(value)
        return self

    def getAssignedTrafficClasses(self) -> List[PositiveInteger]:
        """Defines a set of Traffic Classes which shall be handled by this FIFO. range: 0-7"""
        return self.assignedTrafficClasses

    def getMinimumFifoLength(self) -> Optional[PositiveInteger]:
        """FIFO minimum length in Byte. An actual configuration/ hardware may use a bigger value."""
        return self.minimumFifoLength

    def setMinimumFifoLength(self, value: Optional[PositiveInteger]) -> "CouplingPortFifo":
        """
        FIFO minimum length in Byte. An actual configuration/ hardware may use a bigger value.
        A None value is a no-op and does not overwrite an existing minimumFifoLength.
        """
        if value is not None:
            self.minimumFifoLength = value
        return self

    def getShaper(self) -> Optional[ARObject]:
        """Definition of the shaper to be used for the processing of this FIFO."""
        return self.shaper

    def setShaper(self, value: Optional[ARObject]) -> "CouplingPortFifo":
        """
        Definition of the shaper to be used for the processing of this FIFO.
        A None value is a no-op and does not overwrite an existing shaper.
        """
        if value is not None:
            self.shaper = value
        return self


class CouplingPortScheduler(CouplingPortStructuralElement):
    """
    Defines a scheduler for coupling ports in Ethernet switches,
    specifying scheduling algorithms and predecessor relationships
    for managing traffic flow through the coupling ports.
    """

    # CouplingPortScheduler method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getPortScheduler             [x] impl  [ ] docstring  [ ] test
    # [ ] setPortScheduler             [x] impl  [ ] docstring  [ ] test
    # [ ] getPredecessorRefs           [x] impl  [ ] docstring  [ ] test
    # [ ] addPredecessorRef            [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        self.portScheduler = None  # type: EthernetCouplingPortSchedulerEnum
        self.predecessorRefs = []  # type: List[RefType]

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

    # EthernetPriorityRegeneration method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getIngressPriority           [x] impl  [ ] docstring  [ ] test
    # [ ] setIngressPriority           [x] impl  [ ] docstring  [ ] test
    # [ ] getRegeneratedPriority       [x] impl  [ ] docstring  [ ] test
    # [ ] setRegeneratedPriority       [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        self.ingressPriority = None  # type: PositiveInteger
        self.regeneratedPriority = None  # type: PositiveInteger

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
    Defines details of a CouplingPort. May be used to configure the structures of a switch.
    """

    # CouplingPortDetails method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.63, p.122
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                            [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getCouplingPortStructuralElements   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] createCouplingPortFifo              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] createCouplingPortScheduler         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] createEthernetPriorityRegeneration  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getEthernetPriorityRegenerations    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addEthernetTrafficClassAssignment   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getEthernetTrafficClassAssignments  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] getGlobalTimeProps                  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setGlobalTimeProps                  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getLastEgressSchedulerRef           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setLastEgressSchedulerRef           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # Collects all the structural parts at which a CouplingPort may be configurable.
        self.couplingPortStructuralElements: List[CouplingPortStructuralElement] = []

        # Defines a priority regeneration where the ingress priority is replaced by regenerated priority.
        self.ethernetPriorityRegenerations: List[EthernetPriorityRegeneration] = []

        # Defines the ingress port to EthernetTrafficClass assignment.
        self.ethernetTrafficClassAssignments: List[CouplingPortTrafficClassAssignment] = []

        # Specifies properties for the usage of the CouplingPort in the scope of Global Time Sync.
        self.globalTimeProps: Optional[ARObject] = None

        # Defines which CouplingPortScheduler is the last in the egress port structure.
        self.lastEgressSchedulerRef: Optional[RefType] = None

    def getCouplingPortStructuralElements(self) -> List[CouplingPortStructuralElement]:
        """Collects all the structural parts at which a CouplingPort may be configurable."""
        return self.couplingPortStructuralElements

    def createCouplingPortFifo(self, short_name: str) -> CouplingPortFifo:
        """Collects all the structural parts at which a CouplingPort may be configurable."""
        fifo = CouplingPortFifo(self, short_name)
        self.couplingPortStructuralElements.append(fifo)
        return fifo

    def createCouplingPortScheduler(self, short_name: str) -> CouplingPortScheduler:
        """Collects all the structural parts at which a CouplingPort may be configurable."""
        scheduler = CouplingPortScheduler(self, short_name)
        self.couplingPortStructuralElements.append(scheduler)
        return scheduler

    def createEthernetPriorityRegeneration(self, short_name: str) -> EthernetPriorityRegeneration:
        """Defines a priority regeneration where the ingress priority is replaced by regenerated priority."""
        regeneration = EthernetPriorityRegeneration(self, short_name)
        self.ethernetPriorityRegenerations.append(regeneration)
        return regeneration

    def getEthernetPriorityRegenerations(self) -> List[EthernetPriorityRegeneration]:
        """Defines a priority regeneration where the ingress priority is replaced by regenerated priority."""
        return self.ethernetPriorityRegenerations

    def addEthernetTrafficClassAssignment(self, value: Optional[CouplingPortTrafficClassAssignment]) -> "CouplingPortDetails":
        """
        Defines the ingress port to EthernetTrafficClass assignment.
        A None value is a no-op and does not append to ethernetTrafficClassAssignments.
        """
        if value is not None:
            self.ethernetTrafficClassAssignments.append(value)
        return self

    def getEthernetTrafficClassAssignments(self) -> List[CouplingPortTrafficClassAssignment]:
        """Defines the ingress port to EthernetTrafficClass assignment."""
        return self.ethernetTrafficClassAssignments

    def getGlobalTimeProps(self) -> Optional[ARObject]:
        """Specifies properties for the usage of the CouplingPort in the scope of Global Time Sync."""
        return self.globalTimeProps

    def setGlobalTimeProps(self, value: Optional[ARObject]) -> "CouplingPortDetails":
        """
        Specifies properties for the usage of the CouplingPort in the scope of Global Time Sync.
        A None value is a no-op and does not overwrite an existing globalTimeProps.
        """
        if value is not None:
            self.globalTimeProps = value
        return self

    def getLastEgressSchedulerRef(self) -> Optional[RefType]:
        """Defines which CouplingPortScheduler is the last in the egress port structure."""
        return self.lastEgressSchedulerRef

    def setLastEgressSchedulerRef(self, value: Optional[RefType]) -> "CouplingPortDetails":
        """
        Defines which CouplingPortScheduler is the last in the egress port structure.
        A None value is a no-op and does not overwrite an existing lastEgressSchedulerRef.
        """
        if value is not None:
            self.lastEgressSchedulerRef = value
        return self


class VlanMembership(ARObject):
    """
    Defines VLAN membership properties for network interfaces,
    specifying default priorities, DHCP configurations, and VLAN
    tagging behaviors for Ethernet communication.
    """

    # VlanMembership method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getDefaultPriority           [x] impl  [ ] docstring  [ ] test
    # [ ] setDefaultPriority           [x] impl  [ ] docstring  [ ] test
    # [ ] getDhcpAddressAssignment     [x] impl  [ ] docstring  [ ] test
    # [ ] setDhcpAddressAssignment     [x] impl  [ ] docstring  [ ] test
    # [ ] getSendActivity              [x] impl  [ ] docstring  [ ] test
    # [ ] setSendActivity              [x] impl  [ ] docstring  [ ] test
    # [ ] getVlanRef                   [x] impl  [ ] docstring  [ ] test
    # [ ] setVlanRef                   [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()

        self.defaultPriority = None  # type: PositiveInteger
        self.dhcpAddressAssignment = None  # type: DhcpServerConfiguration
        self.sendActivity = None  # type: EthernetSwitchVlanEgressTaggingEnum
        self.vlanRef = None  # type: RefType

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

    # CouplingPort method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getConnectionNegotiationBehavior [x] impl  [ ] docstring  [ ] test
    # [ ] setConnectionNegotiationBehavior [x] impl  [ ] docstring  [ ] test
    # [ ] getCouplingPortDetails       [x] impl  [ ] docstring  [ ] test
    # [ ] setCouplingPortDetails       [x] impl  [ ] docstring  [ ] test
    # [ ] getCouplingPortRole          [x] impl  [ ] docstring  [ ] test
    # [ ] setCouplingPortRole          [x] impl  [ ] docstring  [ ] test
    # [ ] getDefaultVlanRef            [x] impl  [ ] docstring  [ ] test
    # [ ] setDefaultVlanRef            [x] impl  [ ] docstring  [ ] test
    # [ ] getMacAddressVlanAssignments [x] impl  [ ] docstring  [ ] test
    # [ ] setMacAddressVlanAssignments [x] impl  [ ] docstring  [ ] test
    # [ ] getMacLayerType              [x] impl  [ ] docstring  [ ] test
    # [ ] setMacLayerType              [x] impl  [ ] docstring  [ ] test
    # [ ] getMacMulticastAddressRefs   [x] impl  [ ] docstring  [ ] test
    # [ ] setMacMulticastAddressRefs   [x] impl  [ ] docstring  [ ] test
    # [ ] getMacSecProps               [x] impl  [ ] docstring  [ ] test
    # [ ] setMacSecProps               [x] impl  [ ] docstring  [ ] test
    # [ ] getPhysicalLayerType         [x] impl  [ ] docstring  [ ] test
    # [ ] setPhysicalLayerType         [x] impl  [ ] docstring  [ ] test
    # [ ] getPlcaProps                 [x] impl  [ ] docstring  [ ] test
    # [ ] setPlcaProps                 [x] impl  [ ] docstring  [ ] test
    # [ ] getPncMappingRefs            [x] impl  [ ] docstring  [ ] test
    # [ ] setPncMappingRefs            [x] impl  [ ] docstring  [ ] test
    # [ ] getReceiveActivity           [x] impl  [ ] docstring  [ ] test
    # [ ] setReceiveActivity           [x] impl  [ ] docstring  [ ] test
    # [ ] getVlanMemberships           [x] impl  [ ] docstring  [ ] test
    # [ ] addVlanMembership            [x] impl  [ ] docstring  [ ] test
    # [ ] getWakeupSleepOnDatalineConfigRef [x] impl  [ ] docstring  [ ] test
    # [ ] setWakeupSleepOnDatalineConfigRef [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        self.connectionNegotiationBehavior = None  # type: EthernetConnectionNegotiationEnum
        self.couplingPortDetails = None  # type: CouplingPortDetails
        self.couplingPortRole = None  # type: CouplingPortRoleEnum
        self.defaultVlanRef = None  # type: RefType
        self.macAddressVlanAssignments = []  # type: List[MacAddressVlanMembership]
        self.macLayerType = None  # type: EthernetMacLayerTypeEnum
        self.macMulticastAddressRefs = []  # type: List[RefType]
        self.macSecProps = []  # type: List[MacSecProps]
        self.physicalLayerType = None  # type: EthernetPhysicalLayerTypeEnum
        self.plcaProps = None  # type: PlcaProps
        self.pncMappingRefs = []  # type: List[RefType]
        self.receiveActivity = None  # type: EthernetSwitchVlanIngressTagEnum
        self.vlanMemberships = []  # type: List[VlanMembership]
        self.wakeupSleepOnDatalineConfigRef = None  # type: RefType

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

    # EthernetCommunicationController method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getCanXlConfigRef            [x] impl  [ ] docstring  [ ] test
    # [ ] setCanXlConfigRef            [x] impl  [ ] docstring  [ ] test
    # [ ] getCouplingPorts             [x] impl  [ ] docstring  [ ] test
    # [ ] createCouplingPort           [x] impl  [ ] docstring  [ ] test
    # [ ] getMacLayerType              [x] impl  [ ] docstring  [ ] test
    # [ ] setMacLayerType              [x] impl  [ ] docstring  [ ] test
    # [ ] getMacUnicastAddress         [x] impl  [ ] docstring  [ ] test
    # [ ] setMacUnicastAddress         [x] impl  [ ] docstring  [ ] test
    # [ ] getMaximumReceiveBufferLength [x] impl  [ ] docstring  [ ] test
    # [ ] setMaximumReceiveBufferLength [x] impl  [ ] docstring  [ ] test
    # [ ] getMaximumTransmitBufferLength [x] impl  [ ] docstring  [ ] test
    # [ ] setMaximumTransmitBufferLength [x] impl  [ ] docstring  [ ] test
    # [ ] getSlaveActAsPassiveCommunicationSlave [x] impl  [ ] docstring  [ ] test
    # [ ] setSlaveActAsPassiveCommunicationSlave [x] impl  [ ] docstring  [ ] test
    # [ ] getSlaveQualifiedUnexpectedLinkDownTime [x] impl  [ ] docstring  [ ] test
    # [ ] setSlaveQualifiedUnexpectedLinkDownTime [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.canXlConfigRef = None  # type: RefType
        self.couplingPorts = []  # type: List[CouplingPort]
        self.macLayerType = None  # type: EthernetMacLayerTypeEnum
        self.macUnicastAddress = None  # type: MacAddressString
        self.maximumReceiveBufferLength = None  # type: Integer
        self.maximumTransmitBufferLength = None  # type: Integer
        self.slaveActAsPassiveCommunicationSlave = None  # type: Boolean
        self.slaveQualifiedUnexpectedLinkDownTime = None  # type: TimeValue

    def getCanXlConfigRef(self):
        return self.canXlConfigRef

    def setCanXlConfigRef(self, value):
        self.canXlConfigRef = value
        return self

    def getCouplingPorts(self):
        return self.couplingPorts

    def createCouplingPort(self, short_name: str) -> CouplingPort:
        if short_name not in self.elements:
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

    # EthernetCommunicationConnector method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getEthIpPropsRef             [x] impl  [ ] docstring  [ ] test
    # [ ] setEthIpPropsRef             [x] impl  [ ] docstring  [ ] test
    # [ ] getMaximumTransmissionUnit   [x] impl  [ ] docstring  [ ] test
    # [ ] setMaximumTransmissionUnit   [x] impl  [ ] docstring  [ ] test
    # [ ] getNeighborCacheSize         [x] impl  [ ] docstring  [ ] test
    # [ ] setNeighborCacheSize         [x] impl  [ ] docstring  [ ] test
    # [ ] getNetworkEndpointRefs       [x] impl  [ ] docstring  [ ] test
    # [ ] addNetworkEndpointRef        [x] impl  [ ] docstring  [ ] test
    # [ ] getPathMtuEnabled            [x] impl  [ ] docstring  [ ] test
    # [ ] setPathMtuEnabled            [x] impl  [ ] docstring  [ ] test
    # [ ] getPathMtuTimeout            [x] impl  [ ] docstring  [ ] test
    # [ ] setPathMtuTimeout            [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.ethIpPropsRef = None  # type: RefType
        self.maximumTransmissionUnit = None  # type: PositiveInteger
        self.neighborCacheSize = None  # type: PositiveInteger
        self.networkEndpointRefs = []  # type: List[RefType]       ## 4.3.1 Version
        self.pathMtuEnabled = None  # type: Boolean
        self.pathMtuTimeout = None  # type: TimeValue

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

    # RequestResponseDelay method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getMaxValue                  [x] impl  [ ] docstring  [ ] test
    # [ ] setMaxValue                  [x] impl  [ ] docstring  [ ] test
    # [ ] getMinValue                  [x] impl  [ ] docstring  [ ] test
    # [ ] setMinValue                  [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()

        self.maxValue = None  # type: TimeValue
        self.minValue = None  # type: TimeValue

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

    # InitialSdDelayConfig method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getInitialDelayMaxValue      [x] impl  [ ] docstring  [ ] test
    # [ ] setInitialDelayMaxValue      [x] impl  [ ] docstring  [ ] test
    # [ ] getInitialDelayMinValue      [x] impl  [ ] docstring  [ ] test
    # [ ] setInitialDelayMinValue      [x] impl  [ ] docstring  [ ] test
    # [ ] getInitialRepetitionsBaseDelay [x] impl  [ ] docstring  [ ] test
    # [ ] setInitialRepetitionsBaseDelay [x] impl  [ ] docstring  [ ] test
    # [ ] getInitialRepetitionsMax     [x] impl  [ ] docstring  [ ] test
    # [ ] setInitialRepetitionsMax     [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()

        self.initialDelayMaxValue = None  # type: TimeValue
        self.initialDelayMinValue = None  # type: TimeValue
        self.initialRepetitionsBaseDelay = None  # type: TimeValue
        self.initialRepetitionsMax = None  # type: PositiveInteger

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

    # SdClientConfig method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getClientServiceMajorVersion [x] impl  [ ] docstring  [ ] test
    # [ ] setClientServiceMajorVersion [x] impl  [ ] docstring  [ ] test
    # [ ] getClientServiceMinorVersion [x] impl  [ ] docstring  [ ] test
    # [ ] setClientServiceMinorVersion [x] impl  [ ] docstring  [ ] test
    # [ ] getInitialFindBehavior       [x] impl  [ ] docstring  [ ] test
    # [ ] setInitialFindBehavior       [x] impl  [ ] docstring  [ ] test
    # [ ] getRequestResponseDelay      [x] impl  [ ] docstring  [ ] test
    # [ ] setRequestResponseDelay      [x] impl  [ ] docstring  [ ] test
    # [ ] getTtl                       [x] impl  [ ] docstring  [ ] test
    # [ ] setTtl                       [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()

        self.capabilityRecord = None  # type: TagWithOptionalValue
        self.clientServiceMajorVersion = None  # type: PositiveInteger
        self.clientServiceMinorVersion = None  # type: PositiveInteger
        self.initialFindBehavior = None  # type: InitialSdDelayConfig
        self.requestResponseDelay = None  # type: RequestResponseDelay
        self.ttl = None  # type: PositiveInteger

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


class Ipv4DhcpServerConfiguration(Describable):
    """
    Defines the configuration of a IPv4 DHCP server that runs on the network endpoint.
    """

    # Ipv4DhcpServerConfiguration method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.80, p.132
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                       [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getAddressRangeLowerBound      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setAddressRangeLowerBound      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getAddressRangeUpperBound      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setAddressRangeUpperBound      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getDefaultGateway              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setDefaultGateway              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getDefaultLeaseTime            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setDefaultLeaseTime            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getDnsServerAddresses          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addDnsServerAddress            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getNetworkMask                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setNetworkMask                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # Lower range of IP addresses to be issued to DHCP clients. IPv4 Address. Notation: 255.255.255.255.
        self.addressRangeLowerBound: Optional[Ip4AddressString] = None

        # Upper range of IP addresses to be issued to DHCP clients. Pv4 Address. Notation: 255.255.255.255.
        self.addressRangeUpperBound: Optional[Ip4AddressString] = None

        # IP address of the default gateway. Notation 255.255.255.255
        self.defaultGateway: Optional[Ip4AddressString] = None

        # Amount of time in seconds that a client may keep the IP address.
        self.defaultLeaseTime: Optional[TimeValue] = None

        # IP addresses of preconfigured DNS servers. Notation 255.255.255.255
        self.dnsServerAddresses: List[Ip4AddressString] = []

        # Default network mask to be used by DHCP clients. Notation 255.255.255.255
        self.networkMask: Optional[Ip4AddressString] = None

    def getAddressRangeLowerBound(self) -> Optional[Ip4AddressString]:
        """Lower range of IP addresses to be issued to DHCP clients. IPv4 Address. Notation: 255.255.255.255."""
        return self.addressRangeLowerBound

    def setAddressRangeLowerBound(self, value: Optional[Ip4AddressString]) -> "Ipv4DhcpServerConfiguration":
        """
        Lower range of IP addresses to be issued to DHCP clients. IPv4 Address. Notation: 255.255.255.255.
        A None value is a no-op and does not overwrite an existing addressRangeLowerBound.
        """
        if value is not None:
            self.addressRangeLowerBound = value
        return self

    def getAddressRangeUpperBound(self) -> Optional[Ip4AddressString]:
        """Upper range of IP addresses to be issued to DHCP clients. Pv4 Address. Notation: 255.255.255.255."""
        return self.addressRangeUpperBound

    def setAddressRangeUpperBound(self, value: Optional[Ip4AddressString]) -> "Ipv4DhcpServerConfiguration":
        """
        Upper range of IP addresses to be issued to DHCP clients. Pv4 Address. Notation: 255.255.255.255.
        A None value is a no-op and does not overwrite an existing addressRangeUpperBound.
        """
        if value is not None:
            self.addressRangeUpperBound = value
        return self

    def getDefaultGateway(self) -> Optional[Ip4AddressString]:
        """IP address of the default gateway. Notation 255.255.255.255"""
        return self.defaultGateway

    def setDefaultGateway(self, value: Optional[Ip4AddressString]) -> "Ipv4DhcpServerConfiguration":
        """
        IP address of the default gateway. Notation 255.255.255.255
        A None value is a no-op and does not overwrite an existing defaultGateway.
        """
        if value is not None:
            self.defaultGateway = value
        return self

    def getDefaultLeaseTime(self) -> Optional[TimeValue]:
        """Amount of time in seconds that a client may keep the IP address."""
        return self.defaultLeaseTime

    def setDefaultLeaseTime(self, value: Optional[TimeValue]) -> "Ipv4DhcpServerConfiguration":
        """
        Amount of time in seconds that a client may keep the IP address.
        A None value is a no-op and does not overwrite an existing defaultLeaseTime.
        """
        if value is not None:
            self.defaultLeaseTime = value
        return self

    def getDnsServerAddresses(self) -> List[Ip4AddressString]:
        """IP addresses of preconfigured DNS servers. Notation 255.255.255.255"""
        return self.dnsServerAddresses

    def addDnsServerAddress(self, value: Optional[Ip4AddressString]) -> "Ipv4DhcpServerConfiguration":
        """
        IP addresses of preconfigured DNS servers. Notation 255.255.255.255
        A None value is a no-op and does not append to dnsServerAddresses.
        """
        if value is not None:
            self.dnsServerAddresses.append(value)
        return self

    def getNetworkMask(self) -> Optional[Ip4AddressString]:
        """Default network mask to be used by DHCP clients. Notation 255.255.255.255"""
        return self.networkMask

    def setNetworkMask(self, value: Optional[Ip4AddressString]) -> "Ipv4DhcpServerConfiguration":
        """
        Default network mask to be used by DHCP clients. Notation 255.255.255.255
        A None value is a no-op and does not overwrite an existing networkMask.
        """
        if value is not None:
            self.networkMask = value
        return self


class Ipv6DhcpServerConfiguration(Describable):
    """
    Defines the configuration of a IPv6 DHCP server that runs on the network endpoint.
    """

    # Ipv6DhcpServerConfiguration method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.81, p.132
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                       [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getAddressRangeLowerBound      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setAddressRangeLowerBound      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getAddressRangeUpperBound      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setAddressRangeUpperBound      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getDefaultGateway              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setDefaultGateway              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getDefaultLeaseTime            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setDefaultLeaseTime            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getDnsServerAddresses          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addDnsServerAddress            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getNetworkMask                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setNetworkMask                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # Lower range of IP addresses to be issued to DHCP clients. IPv6 Address. Notation: FFFF:...:FFFF.
        self.addressRangeLowerBound: Optional[Ip6AddressString] = None

        # Upper range of IP addresses to be issued to DHCP clients. IPv6 Address. Notation: FFFF:...:FFFF.
        self.addressRangeUpperBound: Optional[Ip6AddressString] = None

        # IP address of the default gateway. Notation 255.255.255.255
        self.defaultGateway: Optional[Ip6AddressString] = None

        # Amount of time in seconds that a client may keep the IP address.
        self.defaultLeaseTime: Optional[TimeValue] = None

        # IP addresses of preconfigured DNS servers. Notation: FFFF:...:FFFF.
        self.dnsServerAddresses: List[Ip6AddressString] = []

        # Default network mask to be used by DHCP clients. Notation 255.255.255.255
        self.networkMask: Optional[Ip6AddressString] = None

    def getAddressRangeLowerBound(self) -> Optional[Ip6AddressString]:
        """Lower range of IP addresses to be issued to DHCP clients. IPv6 Address. Notation: FFFF:...:FFFF."""
        return self.addressRangeLowerBound

    def setAddressRangeLowerBound(self, value: Optional[Ip6AddressString]) -> "Ipv6DhcpServerConfiguration":
        """
        Lower range of IP addresses to be issued to DHCP clients. IPv6 Address. Notation: FFFF:...:FFFF.
        A None value is a no-op and does not overwrite an existing addressRangeLowerBound.
        """
        if value is not None:
            self.addressRangeLowerBound = value
        return self

    def getAddressRangeUpperBound(self) -> Optional[Ip6AddressString]:
        """Upper range of IP addresses to be issued to DHCP clients. IPv6 Address. Notation: FFFF:...:FFFF."""
        return self.addressRangeUpperBound

    def setAddressRangeUpperBound(self, value: Optional[Ip6AddressString]) -> "Ipv6DhcpServerConfiguration":
        """
        Upper range of IP addresses to be issued to DHCP clients. IPv6 Address. Notation: FFFF:...:FFFF.
        A None value is a no-op and does not overwrite an existing addressRangeUpperBound.
        """
        if value is not None:
            self.addressRangeUpperBound = value
        return self

    def getDefaultGateway(self) -> Optional[Ip6AddressString]:
        """IP address of the default gateway. Notation 255.255.255.255"""
        return self.defaultGateway

    def setDefaultGateway(self, value: Optional[Ip6AddressString]) -> "Ipv6DhcpServerConfiguration":
        """
        IP address of the default gateway. Notation 255.255.255.255
        A None value is a no-op and does not overwrite an existing defaultGateway.
        """
        if value is not None:
            self.defaultGateway = value
        return self

    def getDefaultLeaseTime(self) -> Optional[TimeValue]:
        """Amount of time in seconds that a client may keep the IP address."""
        return self.defaultLeaseTime

    def setDefaultLeaseTime(self, value: Optional[TimeValue]) -> "Ipv6DhcpServerConfiguration":
        """
        Amount of time in seconds that a client may keep the IP address.
        A None value is a no-op and does not overwrite an existing defaultLeaseTime.
        """
        if value is not None:
            self.defaultLeaseTime = value
        return self

    def getDnsServerAddresses(self) -> List[Ip6AddressString]:
        """IP addresses of preconfigured DNS servers. Notation: FFFF:...:FFFF."""
        return self.dnsServerAddresses

    def addDnsServerAddress(self, value: Optional[Ip6AddressString]) -> "Ipv6DhcpServerConfiguration":
        """
        IP addresses of preconfigured DNS servers. Notation: FFFF:...:FFFF.
        A None value is a no-op and does not append to dnsServerAddresses.
        """
        if value is not None:
            self.dnsServerAddresses.append(value)
        return self

    def getNetworkMask(self) -> Optional[Ip6AddressString]:
        """Default network mask to be used by DHCP clients. Notation 255.255.255.255"""
        return self.networkMask

    def setNetworkMask(self, value: Optional[Ip6AddressString]) -> "Ipv6DhcpServerConfiguration":
        """
        Default network mask to be used by DHCP clients. Notation 255.255.255.255
        A None value is a no-op and does not overwrite an existing networkMask.
        """
        if value is not None:
            self.networkMask = value
        return self


class DhcpServerConfiguration(ARObject):
    """
    Defines the configuration of DHCP servers that are running on the network endpoint. It is possible that an Ipv4DhcpServer and an Ipv6DhcpServer run on the same Ecu.
    """

    # DhcpServerConfiguration method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.79, p.131
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                          [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getIpv4DhcpServerConfiguration    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setIpv4DhcpServerConfiguration    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getIpv6DhcpServerConfiguration    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setIpv6DhcpServerConfiguration    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # Configuration of a IPv4 DHCP server that runs on the network endpoint.
        self.ipv4DhcpServerConfiguration: Optional[Ipv4DhcpServerConfiguration] = None

        # Configuration of a IPv6 DHCP server that runs on the network endpoint.
        self.ipv6DhcpServerConfiguration: Optional[Ipv6DhcpServerConfiguration] = None

    def getIpv4DhcpServerConfiguration(self) -> Optional[Ipv4DhcpServerConfiguration]:
        """Configuration of a IPv4 DHCP server that runs on the network endpoint."""
        return self.ipv4DhcpServerConfiguration

    def setIpv4DhcpServerConfiguration(self, value: Optional[Ipv4DhcpServerConfiguration]) -> "DhcpServerConfiguration":
        """
        Configuration of a IPv4 DHCP server that runs on the network endpoint.
        A None value is a no-op and does not overwrite an existing ipv4DhcpServerConfiguration.
        """
        if value is not None:
            self.ipv4DhcpServerConfiguration = value
        return self

    def getIpv6DhcpServerConfiguration(self) -> Optional[Ipv6DhcpServerConfiguration]:
        """Configuration of a IPv6 DHCP server that runs on the network endpoint."""
        return self.ipv6DhcpServerConfiguration

    def setIpv6DhcpServerConfiguration(self, value: Optional[Ipv6DhcpServerConfiguration]) -> "DhcpServerConfiguration":
        """
        Configuration of a IPv6 DHCP server that runs on the network endpoint.
        A None value is a no-op and does not overwrite an existing ipv6DhcpServerConfiguration.
        """
        if value is not None:
            self.ipv6DhcpServerConfiguration = value
        return self


class CouplingPortTrafficClassAssignment(Referrable):
    """
    Defines the assignment of Traffic Class to a frame.
    """

    # CouplingPortTrafficClassAssignment method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.75, p.128
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] addPriority               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getPriorities             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] getTrafficClass           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setTrafficClass           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        # Defines a priority which is mapped onto a Traffic Class.
        self.priorities: List[PositiveInteger] = []

        # Defines the Traffic Class which is assigned. range: 0-7
        self.trafficClass: Optional[PositiveInteger] = None

    def addPriority(self, value: Optional[PositiveInteger]) -> "CouplingPortTrafficClassAssignment":
        """
        Defines a priority which is mapped onto a Traffic Class.
        A None value is a no-op and does not append to priorities.
        """
        if value is not None:
            self.priorities.append(value)
        return self

    def getPriorities(self) -> List[PositiveInteger]:
        """Defines a priority which is mapped onto a Traffic Class."""
        return self.priorities

    def getTrafficClass(self) -> Optional[PositiveInteger]:
        """Defines the Traffic Class which is assigned. range: 0-7"""
        return self.trafficClass

    def setTrafficClass(self, value: Optional[PositiveInteger]) -> "CouplingPortTrafficClassAssignment":
        """
        Defines the Traffic Class which is assigned. range: 0-7
        A None value is a no-op and does not overwrite an existing trafficClass.
        """
        if value is not None:
            self.trafficClass = value
        return self
