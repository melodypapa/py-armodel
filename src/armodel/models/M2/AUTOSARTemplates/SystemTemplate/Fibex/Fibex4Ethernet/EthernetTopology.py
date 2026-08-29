from __future__ import annotations

from abc import ABC
from typing import TYPE_CHECKING, List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Describable, Identifiable, Referrable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
    ARLiteral,
    Boolean,
    Integer,
    Ip4AddressString,
    Ip6AddressString,
    MacAddressString,
    PositiveInteger,
    RefType,
    String,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.TagWithOptionalValue import TagWithOptionalValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import CommunicationCluster, CommunicationConnector
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import CommunicationController
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication import MacSecProps

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import (
        ConsumedServiceInstance,
        ProvidedServiceInstance,
        TransportProtocolConfiguration,
    )


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
    Ethernet-specific cluster attributes.
    """

    # EthernetCluster method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.47, p.103
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                          [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] addCouplingPortConnection         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getCouplingPortConnections        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] getCouplingPortStartupActiveTime  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setCouplingPortStartupActiveTime  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getCouplingPortSwitchoffDelay     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setCouplingPortSwitchoffDelay     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] createMacMulticastGroup           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMacMulticastGroups             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Specification of connections between CouplingElements and EcuInstances.
        self.couplingPortConnections: List[CouplingPortConnection] = []

        # The attribute specifies the time in second a coupling port is switched on to enable the host ECU (ECU that maintains an Ethernet switch) to listen to the network for potential network management requests.
        self.couplingPortStartupActiveTime: Optional[TimeValue] = None

        # Switch off delay for CouplingPorts in seconds. It denotes the delay of switching off couplingPorts after the request to switch off a couplingPort was issued. (e.g. switch off of Ethernet switch ports).
        self.couplingPortSwitchoffDelay: Optional[TimeValue] = None

        # MacMulticastGroup that is defined for the Subnet (EthernetCluster).
        self.macMulticastGroups: List[MacMulticastGroup] = []

    def addCouplingPortConnection(self, value: Optional[CouplingPortConnection]) -> "EthernetCluster":
        """
        Specification of connections between CouplingElements and EcuInstances.
        A None value is a no-op and does not append to couplingPortConnections.
        """
        if value is not None:
            self.couplingPortConnections.append(value)
        return self

    def getCouplingPortConnections(self) -> List[CouplingPortConnection]:
        """Specification of connections between CouplingElements and EcuInstances."""
        return self.couplingPortConnections

    def getCouplingPortStartupActiveTime(self) -> Optional[TimeValue]:
        """The attribute specifies the time in second a coupling port is switched on to enable the host ECU (ECU that maintains an Ethernet switch) to listen to the network for potential network management requests."""
        return self.couplingPortStartupActiveTime

    def setCouplingPortStartupActiveTime(self, value: Optional[TimeValue]) -> "EthernetCluster":
        """
        The attribute specifies the time in second a coupling port is switched on to enable the host ECU (ECU that maintains an Ethernet switch) to listen to the network for potential network management requests.
        A None value is a no-op and does not overwrite an existing couplingPortStartupActiveTime.
        """
        if value is not None:
            self.couplingPortStartupActiveTime = value
        return self

    def getCouplingPortSwitchoffDelay(self) -> Optional[TimeValue]:
        """Switch off delay for CouplingPorts in seconds. It denotes the delay of switching off couplingPorts after the request to switch off a couplingPort was issued. (e.g. switch off of Ethernet switch ports)."""
        return self.couplingPortSwitchoffDelay

    def setCouplingPortSwitchoffDelay(self, value: Optional[TimeValue]) -> "EthernetCluster":
        """
        Switch off delay for CouplingPorts in seconds. It denotes the delay of switching off couplingPorts after the request to switch off a couplingPort was issued. (e.g. switch off of Ethernet switch ports).
        A None value is a no-op and does not overwrite an existing couplingPortSwitchoffDelay.
        """
        if value is not None:
            self.couplingPortSwitchoffDelay = value
        return self

    def createMacMulticastGroup(self, short_name: str) -> MacMulticastGroup:
        """MacMulticastGroup that is defined for the Subnet (EthernetCluster)."""
        if short_name not in self.elements:
            group = MacMulticastGroup(self, short_name)
            self.addElement(group)
            self.macMulticastGroups.append(group)
        return self.getElement(short_name)

    def getMacMulticastGroups(self) -> List[MacMulticastGroup]:
        """MacMulticastGroup that is defined for the Subnet (EthernetCluster)."""
        return self.macMulticastGroups


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


class CouplingPortAbstractShaper(Identifiable, ABC):
    """Abstract class for the definition of coupling port shapers."""

    # CouplingPortAbstractShaper method parity checklist:
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    _shaper_registry = {}

    @classmethod
    def registerShaper(cls, xml_tag: str, shaper_cls):
        cls._shaper_registry[xml_tag] = shaper_cls

    @classmethod
    def getShaperClass(cls, xml_tag: str):
        return cls._shaper_registry.get(xml_tag)

    @classmethod
    def getShaperTag(cls, shaper_cls):
        for tag, shaper_class in cls._shaper_registry.items():
            if shaper_class is shaper_cls:
                return tag
        return None

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is CouplingPortAbstractShaper:
            raise TypeError("CouplingPortAbstractShaper is an abstract class.")

        super().__init__(parent, short_name)


class CouplingPortFifo(CouplingPortStructuralElement):
    """
    Defines a FIFO for the CouplingPort egress structure.
    """

    # CouplingPortFifo method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.68, p.124
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] addAssignedTrafficClass      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getAssignedTrafficClasses    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] getMinimumFifoLength         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMinimumFifoLength         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getShaper                    [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] setShaper                    [x] impl  [x] docstring  [x] test  [x] reader  [x] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Defines a set of Traffic Classes which shall be handled by this FIFO. range: 0-7
        self.assignedTrafficClasses: List[PositiveInteger] = []

        # FIFO minimum length in Byte. An actual configuration/ hardware may use a bigger value.
        self.minimumFifoLength: Optional[PositiveInteger] = None

        # Definition of the shaper to be used for the processing of this FIFO.
        self.shaper: Optional[CouplingPortAbstractShaper] = None

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

    def getShaper(self) -> Optional[CouplingPortAbstractShaper]:
        """Definition of the shaper to be used for the processing of this FIFO."""
        return self.shaper

    def setShaper(self, value: Optional[CouplingPortAbstractShaper]) -> "CouplingPortFifo":
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
    # Spec verified: R23-11
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
    # [x] addRatePolicy                       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getRatePolicies                     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer

    def __init__(self):
        super().__init__()

        # Collects all the structural parts at which a CouplingPort may be configurable.
        self.couplingPortStructuralElements: List[CouplingPortStructuralElement] = []

        # Defines a priority regeneration where the ingress priority is replaced by regenerated priority.
        self.ethernetPriorityRegenerations: List[EthernetPriorityRegeneration] = []

        # Defines the ingress port to EthernetTrafficClass assignment.
        self.ethernetTrafficClassAssignments: List[CouplingPortTrafficClassAssignment] = []

        # Specifies properties for the usage of the CouplingPort in the scope of Global Time Sync.
        self.globalTimeProps: Optional[GlobalTimeCouplingPortProps] = None

        # Defines which CouplingPortScheduler is the last in the egress port structure.
        self.lastEgressSchedulerRef: Optional[RefType] = None

        # Rate policies to be applied for this CouplingPort.
        self.ratePolicies: List[CouplingPortRatePolicy] = []

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

    def getGlobalTimeProps(self) -> Optional[GlobalTimeCouplingPortProps]:
        """Specifies properties for the usage of the CouplingPort in the scope of Global Time Sync."""
        return self.globalTimeProps

    def setGlobalTimeProps(self, value: Optional[GlobalTimeCouplingPortProps]) -> "CouplingPortDetails":
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

    def addRatePolicy(self, value: Optional[CouplingPortRatePolicy]) -> "CouplingPortDetails":
        """
        Rate policies to be applied for this CouplingPort.
        A None value is a no-op and does not append to ratePolicies.
        """
        if value is not None:
            self.ratePolicies.append(value)
        return self

    def getRatePolicies(self) -> List[CouplingPortRatePolicy]:
        """Rate policies to be applied for this CouplingPort."""
        return self.ratePolicies


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
    A CouplingPort is used to connect a CouplingElement with an EcuInstance or two CouplingElements with each other via a CouplingPortConnection. Optionally, the CouplingPort may also have a reference to a macMulticastGroup and a defaultVLAN.
    """

    # CouplingPort method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.54, p.110
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                             [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getConnectionNegotiationBehavior     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setConnectionNegotiationBehavior     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getCouplingPortDetails               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setCouplingPortDetails               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getCouplingPortRole                  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setCouplingPortRole                  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getDefaultVlanRef                    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setDefaultVlanRef                    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMacLayerType                      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMacLayerType                      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] addMacMulticastAddressRef            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMacMulticastAddressRefs           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addMacSecProps                       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMacSecProps                       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] getPhysicalLayerType                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setPhysicalLayerType                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getPlcaProps                         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setPlcaProps                         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] addPncMappingRef                     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getPncMappingRefs                    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] getReceiveActivity                   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setReceiveActivity                   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] addVlanMembership                    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getVlanMemberships                   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] getVlanModifierRef                   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setVlanModifierRef                   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getWakeupSleepOnDatalineConfigRef    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setWakeupSleepOnDatalineConfigRef    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Specifies the connection negotiation of the CouplingPort.
        self.connectionNegotiationBehavior: Optional[EthernetConnectionNegotiationEnum] = None

        # Defines more details of a CouplingPort in case a more specific configuration is required.
        self.couplingPortDetails: Optional[CouplingPortDetails] = None

        # Defines the role this CouplingPort takes in the context of the CouplingElement.
        self.couplingPortRole: Optional[CouplingPortRoleEnum] = None

        # The vLanIdentifier of the referenced VLAN is the Default-PVID (port VLAN ID). A Port VLAN ID is a default VLAN ID that is assigned to an access CouplingPort to designate the VLAN segment to which this port is connected. Also, if a CouplingPort has not been configured with any VLAN memberships, the virtual switch's Port VLAN ID (pvid) becomes the default VLAN ID for the ports connection. This identifier/tag is added for incoming untagged messages at the port (ingress tagging). For outgoing messages with this identifier, the tag is removed at the port (egress untagging, depending on the Vlan
        self.defaultVlanRef: Optional[RefType] = None

        # Specifies the mac layer type of the CouplingPort.
        self.macLayerType: Optional[EthernetMacLayerTypeEnum] = None

        # Assigns a set of MAC-Multicast-Addresses which are addressable via this CouplingPort. This is a static pre-configuration and further addresses may be learned during runtime.
        self.macMulticastAddressRefs: List[RefType] = []

        # Properties to configure MACsec (Media access control security) and the MKA (MACsec Key Agreement) for the CouplingPort (PHY).
        self.macSecProps: List[MacSecProps] = []

        # Specifies the physical layer type of the CouplingPort.
        self.physicalLayerType: Optional[EthernetPhysicalLayerTypeEnum] = None

        # Optional properties for configuration of PLCA (Physical Layer Collision Avoidance) in case 10-BASE-T1S Ethernet is used and PLCA is enabled on the Coupling Port (PHY).
        self.plcaProps: Optional[PlcaProps] = None

        # Reference to the partial networks this CouplingPort participates in.
        self.pncMappingRefs: List[RefType] = []

        # Defines the handling of frames at the ingress port.
        self.receiveActivity: Optional[EthernetSwitchVlanIngressTagEnum] = None

        # Messages of VLANs that are defined here can be communicated via the CouplingPort.
        self.vlanMemberships: List[VlanMembership] = []

        # All incoming messages at this CouplingPort shall be tagged with this VLAN Id. This tagging is performed regardless whether the message already has a VLAN tag or is untagged, an existing VLAN tag will be overwritten. This feature is XOR with CoupligPort.defaultVlan.
        self.vlanModifierRef: Optional[RefType] = None

        # Optional reference to EthernetWakeupSleepOnDatalineConfig.
        self.wakeupSleepOnDatalineConfigRef: Optional[RefType] = None

    def getConnectionNegotiationBehavior(self) -> Optional[EthernetConnectionNegotiationEnum]:
        """Specifies the connection negotiation of the CouplingPort."""
        return self.connectionNegotiationBehavior

    def setConnectionNegotiationBehavior(self, value: Optional[EthernetConnectionNegotiationEnum]) -> "CouplingPort":
        """
        Specifies the connection negotiation of the CouplingPort.
        A None value is a no-op and does not overwrite an existing connectionNegotiationBehavior.
        """
        if value is not None:
            self.connectionNegotiationBehavior = value
        return self

    def getCouplingPortDetails(self) -> Optional[CouplingPortDetails]:
        """Defines more details of a CouplingPort in case a more specific configuration is required."""
        return self.couplingPortDetails

    def setCouplingPortDetails(self, value: Optional[CouplingPortDetails]) -> "CouplingPort":
        """
        Defines more details of a CouplingPort in case a more specific configuration is required.
        A None value is a no-op and does not overwrite an existing couplingPortDetails.
        """
        if value is not None:
            self.couplingPortDetails = value
        return self

    def getCouplingPortRole(self) -> Optional[CouplingPortRoleEnum]:
        """Defines the role this CouplingPort takes in the context of the CouplingElement."""
        return self.couplingPortRole

    def setCouplingPortRole(self, value: Optional[CouplingPortRoleEnum]) -> "CouplingPort":
        """
        Defines the role this CouplingPort takes in the context of the CouplingElement.
        A None value is a no-op and does not overwrite an existing couplingPortRole.
        """
        if value is not None:
            self.couplingPortRole = value
        return self

    def getDefaultVlanRef(self) -> Optional[RefType]:
        """The vLanIdentifier of the referenced VLAN is the Default-PVID (port VLAN ID). A Port VLAN ID is a default VLAN ID that is assigned to an access CouplingPort to designate the VLAN segment to which this port is connected. Also, if a CouplingPort has not been configured with any VLAN memberships, the virtual switch's Port VLAN ID (pvid) becomes the default VLAN ID for the ports connection. This identifier/tag is added for incoming untagged messages at the port (ingress tagging). For outgoing messages with this identifier, the tag is removed at the port (egress untagging, depending on the Vlan"""
        return self.defaultVlanRef

    def setDefaultVlanRef(self, value: Optional[RefType]) -> "CouplingPort":
        """
        The vLanIdentifier of the referenced VLAN is the Default-PVID (port VLAN ID). A Port VLAN ID is a default VLAN ID that is assigned to an access CouplingPort to designate the VLAN segment to which this port is connected. Also, if a CouplingPort has not been configured with any VLAN memberships, the virtual switch's Port VLAN ID (pvid) becomes the default VLAN ID for the ports connection. This identifier/tag is added for incoming untagged messages at the port (ingress tagging). For outgoing messages with this identifier, the tag is removed at the port (egress untagging, depending on the Vlan
        A None value is a no-op and does not overwrite an existing defaultVlanRef.
        """
        if value is not None:
            self.defaultVlanRef = value
        return self

    def getMacLayerType(self) -> Optional[EthernetMacLayerTypeEnum]:
        """Specifies the mac layer type of the CouplingPort."""
        return self.macLayerType

    def setMacLayerType(self, value: Optional[EthernetMacLayerTypeEnum]) -> "CouplingPort":
        """
        Specifies the mac layer type of the CouplingPort.
        A None value is a no-op and does not overwrite an existing macLayerType.
        """
        if value is not None:
            self.macLayerType = value
        return self

    def addMacMulticastAddressRef(self, ref: Optional[RefType]) -> "CouplingPort":
        """
        Assigns a set of MAC-Multicast-Addresses which are addressable via this CouplingPort. This is a static pre-configuration and further addresses may be learned during runtime.
        A None value is a no-op and does not append to macMulticastAddressRefs.
        """
        if ref is not None:
            self.macMulticastAddressRefs.append(ref)
        return self

    def getMacMulticastAddressRefs(self) -> List[RefType]:
        """Assigns a set of MAC-Multicast-Addresses which are addressable via this CouplingPort. This is a static pre-configuration and further addresses may be learned during runtime."""
        return self.macMulticastAddressRefs

    def addMacSecProps(self, value: Optional[MacSecProps]) -> "CouplingPort":
        """
        Properties to configure MACsec (Media access control security) and the MKA (MACsec Key Agreement) for the CouplingPort (PHY).
        A None value is a no-op and does not append to macSecProps.
        """
        if value is not None:
            self.macSecProps.append(value)
        return self

    def getMacSecProps(self) -> List[MacSecProps]:
        """Properties to configure MACsec (Media access control security) and the MKA (MACsec Key Agreement) for the CouplingPort (PHY)."""
        return self.macSecProps

    def getPhysicalLayerType(self) -> Optional[EthernetPhysicalLayerTypeEnum]:
        """Specifies the physical layer type of the CouplingPort."""
        return self.physicalLayerType

    def setPhysicalLayerType(self, value: Optional[EthernetPhysicalLayerTypeEnum]) -> "CouplingPort":
        """
        Specifies the physical layer type of the CouplingPort.
        A None value is a no-op and does not overwrite an existing physicalLayerType.
        """
        if value is not None:
            self.physicalLayerType = value
        return self

    def getPlcaProps(self) -> Optional[PlcaProps]:
        """Optional properties for configuration of PLCA (Physical Layer Collision Avoidance) in case 10-BASE-T1S Ethernet is used and PLCA is enabled on the Coupling Port (PHY)."""
        return self.plcaProps

    def setPlcaProps(self, value: Optional[PlcaProps]) -> "CouplingPort":
        """
        Optional properties for configuration of PLCA (Physical Layer Collision Avoidance) in case 10-BASE-T1S Ethernet is used and PLCA is enabled on the Coupling Port (PHY).
        A None value is a no-op and does not overwrite an existing plcaProps.
        """
        if value is not None:
            self.plcaProps = value
        return self

    def addPncMappingRef(self, ref: Optional[RefType]) -> "CouplingPort":
        """
        Reference to the partial networks this CouplingPort participates in.
        A None value is a no-op and does not append to pncMappingRefs.
        """
        if ref is not None:
            self.pncMappingRefs.append(ref)
        return self

    def getPncMappingRefs(self) -> List[RefType]:
        """Reference to the partial networks this CouplingPort participates in."""
        return self.pncMappingRefs

    def getReceiveActivity(self) -> Optional[EthernetSwitchVlanIngressTagEnum]:
        """Defines the handling of frames at the ingress port."""
        return self.receiveActivity

    def setReceiveActivity(self, value: Optional[EthernetSwitchVlanIngressTagEnum]) -> "CouplingPort":
        """
        Defines the handling of frames at the ingress port.
        A None value is a no-op and does not overwrite an existing receiveActivity.
        """
        if value is not None:
            self.receiveActivity = value
        return self

    def addVlanMembership(self, value: Optional[VlanMembership]) -> "CouplingPort":
        """
        Messages of VLANs that are defined here can be communicated via the CouplingPort.
        A None value is a no-op and does not append to vlanMemberships.
        """
        if value is not None:
            self.vlanMemberships.append(value)
        return self

    def getVlanMemberships(self) -> List[VlanMembership]:
        """Messages of VLANs that are defined here can be communicated via the CouplingPort."""
        return self.vlanMemberships

    def getVlanModifierRef(self) -> Optional[RefType]:
        """All incoming messages at this CouplingPort shall be tagged with this VLAN Id. This tagging is performed regardless whether the message already has a VLAN tag or is untagged, an existing VLAN tag will be overwritten. This feature is XOR with CoupligPort.defaultVlan."""
        return self.vlanModifierRef

    def setVlanModifierRef(self, value: Optional[RefType]) -> "CouplingPort":
        """
        All incoming messages at this CouplingPort shall be tagged with this VLAN Id. This tagging is performed regardless whether the message already has a VLAN tag or is untagged, an existing VLAN tag will be overwritten. This feature is XOR with CoupligPort.defaultVlan.
        A None value is a no-op and does not overwrite an existing vlanModifierRef.
        """
        if value is not None:
            self.vlanModifierRef = value
        return self

    def getWakeupSleepOnDatalineConfigRef(self) -> Optional[RefType]:
        """Optional reference to EthernetWakeupSleepOnDatalineConfig."""
        return self.wakeupSleepOnDatalineConfigRef

    def setWakeupSleepOnDatalineConfigRef(self, value: Optional[RefType]) -> "CouplingPort":
        """
        Optional reference to EthernetWakeupSleepOnDatalineConfig.
        A None value is a no-op and does not overwrite an existing wakeupSleepOnDatalineConfigRef.
        """
        if value is not None:
            self.wakeupSleepOnDatalineConfigRef = value
        return self


class EthernetCommunicationController(CommunicationController):
    """
    Ethernet specific communication port attributes.
    """

    # EthernetCommunicationController method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.61, p.116
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                                [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getCanXlConfigRef                       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setCanXlConfigRef                       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getCouplingPorts                        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] createCouplingPort                      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMacLayerType                         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMacLayerType                         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMacUnicastAddress                    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMacUnicastAddress                    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMaximumReceiveBufferLength           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMaximumReceiveBufferLength           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMaximumTransmitBufferLength          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMaximumTransmitBufferLength          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSlaveActAsPassiveCommunicationSlave  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSlaveActAsPassiveCommunicationSlave  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSlaveQualifiedUnexpectedLinkDownTime [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSlaveQualifiedUnexpectedLinkDownTime [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # If the Ethernet frames handled by this Ethernet CommunicationController are to be tunneled through CAN XL, then this reference shall refer to the Abstract CanCommunicationController that aggregates the Can ControllerXlConfiguration of the physical CAN XL channel to be used for tunneling.
        self.canXlConfigRef: Optional[RefType] = None

        # Optional CouplingPort that can be used to connect the ECU to a CouplingElement (e.g. a switch).
        self.couplingPorts: List[CouplingPort] = []

        # Specifies the mac layer type of the ethernet controller.
        self.macLayerType: Optional[EthernetMacLayerTypeEnum] = None

        # Media Access Control address (MAC address) that uniquely identifies each EthernetCommunication Controller in the network.
        self.macUnicastAddress: Optional[MacAddressString] = None

        # Determines the maximum receive buffer length (frame length) in bytes.
        self.maximumReceiveBufferLength: Optional[Integer] = None

        # Determines the maximum transmit buffer length (frame length) in bytes.
        self.maximumTransmitBufferLength: Optional[Integer] = None

        # This attribute specifies if the EcuInstance is acting as a passive communication slave on the connected Physical Channel. This is used for EthernetCommunication Controllers that use Ethernet hardware which supports wake-up and sleep on the network (e.g. Open Alliance TC10 compliant Ethernet hardware).
        self.slaveActAsPassiveCommunicationSlave: Optional[Boolean] = None

        # This attribute specifies time when an unexpected link down is evaluated as link down and indicated to the AUTOSAR communication stack.
        self.slaveQualifiedUnexpectedLinkDownTime: Optional[TimeValue] = None

    def getCanXlConfigRef(self) -> Optional[RefType]:
        """If the Ethernet frames handled by this Ethernet CommunicationController are to be tunneled through CAN XL, then this reference shall refer to the Abstract CanCommunicationController that aggregates the Can ControllerXlConfiguration of the physical CAN XL channel to be used for tunneling."""
        return self.canXlConfigRef

    def setCanXlConfigRef(self, value: Optional[RefType]) -> "EthernetCommunicationController":
        """
        If the Ethernet frames handled by this Ethernet CommunicationController are to be tunneled through CAN XL, then this reference shall refer to the Abstract CanCommunicationController that aggregates the Can ControllerXlConfiguration of the physical CAN XL channel to be used for tunneling.
        A None value is a no-op and does not overwrite an existing canXlConfigRef.
        """
        if value is not None:
            self.canXlConfigRef = value
        return self

    def getCouplingPorts(self) -> List[CouplingPort]:
        """Optional CouplingPort that can be used to connect the ECU to a CouplingElement (e.g. a switch)."""
        return self.couplingPorts

    def createCouplingPort(self, short_name: str) -> CouplingPort:
        """Optional CouplingPort that can be used to connect the ECU to a CouplingElement (e.g. a switch)."""
        if short_name not in self.elements:
            group = CouplingPort(self, short_name)
            self.addElement(group)
            self.couplingPorts.append(group)
        return self.getElement(short_name)

    def getMacLayerType(self) -> Optional[EthernetMacLayerTypeEnum]:
        """Specifies the mac layer type of the ethernet controller."""
        return self.macLayerType

    def setMacLayerType(self, value: Optional[EthernetMacLayerTypeEnum]) -> "EthernetCommunicationController":
        """
        Specifies the mac layer type of the ethernet controller.
        A None value is a no-op and does not overwrite an existing macLayerType.
        """
        if value is not None:
            self.macLayerType = value
        return self

    def getMacUnicastAddress(self) -> Optional[MacAddressString]:
        """Media Access Control address (MAC address) that uniquely identifies each EthernetCommunication Controller in the network."""
        return self.macUnicastAddress

    def setMacUnicastAddress(self, value: Optional[MacAddressString]) -> "EthernetCommunicationController":
        """
        Media Access Control address (MAC address) that uniquely identifies each EthernetCommunication Controller in the network.
        A None value is a no-op and does not overwrite an existing macUnicastAddress.
        """
        if value is not None:
            self.macUnicastAddress = value
        return self

    def getMaximumReceiveBufferLength(self) -> Optional[Integer]:
        """Determines the maximum receive buffer length (frame length) in bytes."""
        return self.maximumReceiveBufferLength

    def setMaximumReceiveBufferLength(self, value: Optional[Integer]) -> "EthernetCommunicationController":
        """
        Determines the maximum receive buffer length (frame length) in bytes.
        A None value is a no-op and does not overwrite an existing maximumReceiveBufferLength.
        """
        if value is not None:
            self.maximumReceiveBufferLength = value
        return self

    def getMaximumTransmitBufferLength(self) -> Optional[Integer]:
        """Determines the maximum transmit buffer length (frame length) in bytes."""
        return self.maximumTransmitBufferLength

    def setMaximumTransmitBufferLength(self, value: Optional[Integer]) -> "EthernetCommunicationController":
        """
        Determines the maximum transmit buffer length (frame length) in bytes.
        A None value is a no-op and does not overwrite an existing maximumTransmitBufferLength.
        """
        if value is not None:
            self.maximumTransmitBufferLength = value
        return self

    def getSlaveActAsPassiveCommunicationSlave(self) -> Optional[Boolean]:
        """This attribute specifies if the EcuInstance is acting as a passive communication slave on the connected Physical Channel. This is used for EthernetCommunication Controllers that use Ethernet hardware which supports wake-up and sleep on the network (e.g. Open Alliance TC10 compliant Ethernet hardware)."""
        return self.slaveActAsPassiveCommunicationSlave

    def setSlaveActAsPassiveCommunicationSlave(self, value: Optional[Boolean]) -> "EthernetCommunicationController":
        """
        This attribute specifies if the EcuInstance is acting as a passive communication slave on the connected Physical Channel. This is used for EthernetCommunication Controllers that use Ethernet hardware which supports wake-up and sleep on the network (e.g. Open Alliance TC10 compliant Ethernet hardware).
        A None value is a no-op and does not overwrite an existing slaveActAsPassiveCommunicationSlave.
        """
        if value is not None:
            self.slaveActAsPassiveCommunicationSlave = value
        return self

    def getSlaveQualifiedUnexpectedLinkDownTime(self) -> Optional[TimeValue]:
        """This attribute specifies time when an unexpected link down is evaluated as link down and indicated to the AUTOSAR communication stack."""
        return self.slaveQualifiedUnexpectedLinkDownTime

    def setSlaveQualifiedUnexpectedLinkDownTime(self, value: Optional[TimeValue]) -> "EthernetCommunicationController":
        """
        This attribute specifies time when an unexpected link down is evaluated as link down and indicated to the AUTOSAR communication stack.
        A None value is a no-op and does not overwrite an existing slaveQualifiedUnexpectedLinkDownTime.
        """
        if value is not None:
            self.slaveQualifiedUnexpectedLinkDownTime = value
        return self


class EthernetCommunicationConnector(CommunicationConnector):
    """
    Ethernet specific attributes to the CommunicationConnector.
    """

    # EthernetCommunicationConnector method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.62, p.117
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                       [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getEthIpPropsRef               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setEthIpPropsRef               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMaximumTransmissionUnit     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMaximumTransmissionUnit     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getNeighborCacheSize           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setNeighborCacheSize           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getPathMtuEnabled              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setPathMtuEnabled              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getPathMtuTimeout              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setPathMtuTimeout              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # EcuInstance specific IP attributes.
        self.ethIpPropsRef: Optional[RefType] = None

        # This attribute specifies the maximum transmission unit in bytes.
        self.maximumTransmissionUnit: Optional[PositiveInteger] = None

        # This attribute specifies the size of neighbor cache or ARP table in units of entries.
        self.neighborCacheSize: Optional[PositiveInteger] = None

        # If enabled the IPv4/IPv6 processes incoming ICMP "Packet Too Big" messages and stores a MTU value for each destination address.
        self.pathMtuEnabled: Optional[Boolean] = None

        # If this value is >0 the IPv4/IPv6 will reset the MTU value stored for each destination after n seconds.
        self.pathMtuTimeout: Optional[TimeValue] = None

    def getEthIpPropsRef(self) -> Optional[RefType]:
        """EcuInstance specific IP attributes."""
        return self.ethIpPropsRef

    def setEthIpPropsRef(self, value: Optional[RefType]) -> "EthernetCommunicationConnector":
        """
        EcuInstance specific IP attributes.
        A None value is a no-op and does not overwrite an existing ethIpPropsRef.
        """
        if value is not None:
            self.ethIpPropsRef = value
        return self

    def getMaximumTransmissionUnit(self) -> Optional[PositiveInteger]:
        """This attribute specifies the maximum transmission unit in bytes."""
        return self.maximumTransmissionUnit

    def setMaximumTransmissionUnit(self, value: Optional[PositiveInteger]) -> "EthernetCommunicationConnector":
        """
        This attribute specifies the maximum transmission unit in bytes.
        A None value is a no-op and does not overwrite an existing maximumTransmissionUnit.
        """
        if value is not None:
            self.maximumTransmissionUnit = value
        return self

    def getNeighborCacheSize(self) -> Optional[PositiveInteger]:
        """This attribute specifies the size of neighbor cache or ARP table in units of entries."""
        return self.neighborCacheSize

    def setNeighborCacheSize(self, value: Optional[PositiveInteger]) -> "EthernetCommunicationConnector":
        """
        This attribute specifies the size of neighbor cache or ARP table in units of entries.
        A None value is a no-op and does not overwrite an existing neighborCacheSize.
        """
        if value is not None:
            self.neighborCacheSize = value
        return self

    def getPathMtuEnabled(self) -> Optional[Boolean]:
        """If enabled the IPv4/IPv6 processes incoming ICMP "Packet Too Big" messages and stores a MTU value for each destination address."""
        return self.pathMtuEnabled

    def setPathMtuEnabled(self, value: Optional[Boolean]) -> "EthernetCommunicationConnector":
        """
        If enabled the IPv4/IPv6 processes incoming ICMP "Packet Too Big" messages and stores a MTU value for each destination address.
        A None value is a no-op and does not overwrite an existing pathMtuEnabled.
        """
        if value is not None:
            self.pathMtuEnabled = value
        return self

    def getPathMtuTimeout(self) -> Optional[TimeValue]:
        """If this value is >0 the IPv4/IPv6 will reset the MTU value stored for each destination after n seconds."""
        return self.pathMtuTimeout

    def setPathMtuTimeout(self, value: Optional[TimeValue]) -> "EthernetCommunicationConnector":
        """
        If this value is >0 the IPv4/IPv6 will reset the MTU value stored for each destination after n seconds.
        A None value is a no-op and does not overwrite an existing pathMtuTimeout.
        """
        if value is not None:
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
    Client configuration for Service-Discovery.
    """

    # SdClientConfig method parity checklist (XSD-only class — obsolete, no R23-11 PDF table; Rule 0002:
    # attributes derived from the AUTOSAR_00052.xsd SD-CLIENT-CONFIG group; no # Spec line, no marker):
    # XSD verified: AUTOSAR_00052.xsd
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                      [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] addCapabilityRecord           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getCapabilityRecords          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] getClientServiceMajorVersion  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setClientServiceMajorVersion  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getClientServiceMinorVersion  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setClientServiceMinorVersion  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getInitialFindBehavior        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setInitialFindBehavior        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getRequestResponseDelay       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setRequestResponseDelay       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTtl                        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setTtl                        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # A sequence of records to store arbitrary name/value pairs conveying additional information about the named service.
        self.capabilityRecords: List[TagWithOptionalValue] = []

        # Major version number of the Service.
        self.clientServiceMajorVersion: Optional[PositiveInteger] = None

        # Minor version number of the Service.
        self.clientServiceMinorVersion: Optional[PositiveInteger] = None

        # Controls initial find behavior of clients.
        self.initialFindBehavior: Optional[InitialSdDelayConfig] = None

        # Maximum/Minimum allowable response delay to entries received by multicast in seconds.
        self.requestResponseDelay: Optional[RequestResponseDelay] = None

        # TTL for Request and Subscribe messages.
        self.ttl: Optional[PositiveInteger] = None

    def addCapabilityRecord(self, value: Optional[TagWithOptionalValue]) -> "SdClientConfig":
        """
        A sequence of records to store arbitrary name/value pairs conveying additional information about the named service.
        A None value is a no-op and does not append to capabilityRecords.
        """
        if value is not None:
            self.capabilityRecords.append(value)
        return self

    def getCapabilityRecords(self) -> List[TagWithOptionalValue]:
        """A sequence of records to store arbitrary name/value pairs conveying additional information about the named service."""
        return self.capabilityRecords

    def getClientServiceMajorVersion(self) -> Optional[PositiveInteger]:
        """Major version number of the Service."""
        return self.clientServiceMajorVersion

    def setClientServiceMajorVersion(self, value: Optional[PositiveInteger]) -> "SdClientConfig":
        """
        Major version number of the Service.
        A None value is a no-op and does not overwrite an existing clientServiceMajorVersion.
        """
        if value is not None:
            self.clientServiceMajorVersion = value
        return self

    def getClientServiceMinorVersion(self) -> Optional[PositiveInteger]:
        """Minor version number of the Service."""
        return self.clientServiceMinorVersion

    def setClientServiceMinorVersion(self, value: Optional[PositiveInteger]) -> "SdClientConfig":
        """
        Minor version number of the Service.
        A None value is a no-op and does not overwrite an existing clientServiceMinorVersion.
        """
        if value is not None:
            self.clientServiceMinorVersion = value
        return self

    def getInitialFindBehavior(self) -> Optional[InitialSdDelayConfig]:
        """Controls initial find behavior of clients."""
        return self.initialFindBehavior

    def setInitialFindBehavior(self, value: Optional[InitialSdDelayConfig]) -> "SdClientConfig":
        """
        Controls initial find behavior of clients.
        A None value is a no-op and does not overwrite an existing initialFindBehavior.
        """
        if value is not None:
            self.initialFindBehavior = value
        return self

    def getRequestResponseDelay(self) -> Optional[RequestResponseDelay]:
        """Maximum/Minimum allowable response delay to entries received by multicast in seconds."""
        return self.requestResponseDelay

    def setRequestResponseDelay(self, value: Optional[RequestResponseDelay]) -> "SdClientConfig":
        """
        Maximum/Minimum allowable response delay to entries received by multicast in seconds.
        A None value is a no-op and does not overwrite an existing requestResponseDelay.
        """
        if value is not None:
            self.requestResponseDelay = value
        return self

    def getTtl(self) -> Optional[PositiveInteger]:
        """TTL for Request and Subscribe messages."""
        return self.ttl

    def setTtl(self, value: Optional[PositiveInteger]) -> "SdClientConfig":
        """
        TTL for Request and Subscribe messages.
        A None value is a no-op and does not overwrite an existing ttl.
        """
        if value is not None:
            self.ttl = value
        return self


class Ipv4DhcpServerConfiguration(Describable):
    """
    Defines the configuration of a IPv4 DHCP server that runs on the network endpoint.
    """

    # Ipv4DhcpServerConfiguration method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.80, p.132
    # Spec verified: R23-11
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
    # Spec verified: R23-11
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
    # Spec verified: R23-11
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
    # Spec verified: R23-11
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


class ApplicationEndpoint(Identifiable):
    """An application endpoint is the endpoint on an Ecu in terms of application addressing (e.g. socket). The application endpoint represents e.g. the listen socket in client-server-based communication."""

    # ApplicationEndpoint method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.124, p.458
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                             [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] createConsumedServiceInstance        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getConsumedServiceInstances          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] getMaxNumberOfConnections            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMaxNumberOfConnections            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getNetworkEndpointRef                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setNetworkEndpointRef                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getPriority                          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setPriority                          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] createProvidedServiceInstance        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getProvidedServiceInstances          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] getTlsCryptoMappingRef               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setTlsCryptoMappingRef               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTpConfiguration                   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setTpConfiguration                   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Consumed service instances.
        self.consumedServiceInstances: List[ConsumedServiceInstance] = []

        # This attribute defines the maximal number of clients the Server is able to deal with in case of Service Discovery.
        self.maxNumberOfConnections: Optional[PositiveInteger] = None

        # Reference to the network address.
        self.networkEndpointRef: Optional[RefType] = None

        # Defines the frame priority where values from 0 (best effort) to 7 (highest) are allowed.
        self.priority: Optional[PositiveInteger] = None

        # Provided service instances.
        self.providedServiceInstances: List[ProvidedServiceInstance] = []

        # This reference identifies the applicable TlsCryptoServiceMapping that adds the ability for TLS-based encryption on the enclosing ApplicationEndpoint.
        self.tlsCryptoMappingRef: Optional[RefType] = None

        # Configuration of the used transport protocol.
        self.tpConfiguration: Optional[TransportProtocolConfiguration] = None

    def createConsumedServiceInstance(self, short_name: str) -> "ConsumedServiceInstance":
        """Consumed service instances."""
        from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import ConsumedServiceInstance

        if not self.IsElementExists(short_name, ConsumedServiceInstance):
            instance = ConsumedServiceInstance(self, short_name)
            self.addElement(instance)
            self.consumedServiceInstances.append(instance)
        return self.getElement(short_name, ConsumedServiceInstance)

    def getConsumedServiceInstances(self) -> List[ConsumedServiceInstance]:
        """Consumed service instances."""
        return self.consumedServiceInstances

    def getMaxNumberOfConnections(self) -> Optional[PositiveInteger]:
        """This attribute defines the maximal number of clients the Server is able to deal with in case of Service Discovery."""
        return self.maxNumberOfConnections

    def setMaxNumberOfConnections(self, value: Optional[PositiveInteger]) -> "ApplicationEndpoint":
        """
        This attribute defines the maximal number of clients the Server is able to deal with in case of Service Discovery.
        A None value is a no-op and does not overwrite an existing maxNumberOfConnections.
        """
        if value is not None:
            self.maxNumberOfConnections = value
        return self

    def getNetworkEndpointRef(self) -> Optional[RefType]:
        """Reference to the network address."""
        return self.networkEndpointRef

    def setNetworkEndpointRef(self, value: Optional[RefType]) -> "ApplicationEndpoint":
        """
        Reference to the network address.
        A None value is a no-op and does not overwrite an existing networkEndpointRef.
        """
        if value is not None:
            self.networkEndpointRef = value
        return self

    def getPriority(self) -> Optional[PositiveInteger]:
        """Defines the frame priority where values from 0 (best effort) to 7 (highest) are allowed."""
        return self.priority

    def setPriority(self, value: Optional[PositiveInteger]) -> "ApplicationEndpoint":
        """
        Defines the frame priority where values from 0 (best effort) to 7 (highest) are allowed.
        A None value is a no-op and does not overwrite an existing priority.
        """
        if value is not None:
            self.priority = value
        return self

    def createProvidedServiceInstance(self, short_name: str) -> "ProvidedServiceInstance":
        """Provided service instances."""
        from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import ProvidedServiceInstance

        if not self.IsElementExists(short_name, ProvidedServiceInstance):
            instance = ProvidedServiceInstance(self, short_name)
            self.addElement(instance)
            self.providedServiceInstances.append(instance)
        return self.getElement(short_name, ProvidedServiceInstance)

    def getProvidedServiceInstances(self) -> List[ProvidedServiceInstance]:
        """Provided service instances."""
        return self.providedServiceInstances

    def getTlsCryptoMappingRef(self) -> Optional[RefType]:
        """This reference identifies the applicable TlsCryptoServiceMapping that adds the ability for TLS-based encryption on the enclosing ApplicationEndpoint."""
        return self.tlsCryptoMappingRef

    def setTlsCryptoMappingRef(self, value: Optional[RefType]) -> "ApplicationEndpoint":
        """
        This reference identifies the applicable TlsCryptoServiceMapping that adds the ability for TLS-based encryption on the enclosing ApplicationEndpoint.
        A None value is a no-op and does not overwrite an existing tlsCryptoMappingRef.
        """
        if value is not None:
            self.tlsCryptoMappingRef = value
        return self

    def getTpConfiguration(self) -> Optional[TransportProtocolConfiguration]:
        """Configuration of the used transport protocol."""
        return self.tpConfiguration

    def setTpConfiguration(self, value: Optional[TransportProtocolConfiguration]) -> "ApplicationEndpoint":
        """
        Configuration of the used transport protocol.
        A None value is a no-op and does not overwrite an existing tpConfiguration.
        """
        if value is not None:
            self.tpConfiguration = value
        return self


class NetworkEndpointAddress(ARObject, ABC):
    """
    Abstract base class for network endpoint addresses, defining the
    common properties and behavior for different types of network
    addresses (IPv4, IPv6, etc.) used in AUTOSAR communication.
    """

    # NetworkEndpointAddress method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        if type(self) is NetworkEndpointAddress:
            raise TypeError("NetworkEndpointAddress is an abstract class.")

        super().__init__()


class Ipv4Configuration(NetworkEndpointAddress):
    """
    Defines IPv4 network configuration properties for a network endpoint,
    including IP addresses, network masks, DNS server addresses, and
    TTL settings for IPv4 communication.
    """

    # Ipv4Configuration method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getAssignmentPriority        [x] impl  [ ] docstring  [ ] test
    # [ ] setAssignmentPriority        [x] impl  [ ] docstring  [ ] test
    # [ ] getDefaultGateway            [x] impl  [ ] docstring  [ ] test
    # [ ] setDefaultGateway            [x] impl  [ ] docstring  [ ] test
    # [ ] getDnsServerAddresses        [x] impl  [ ] docstring  [ ] test
    # [ ] addDnsServerAddress          [x] impl  [ ] docstring  [ ] test
    # [ ] getIpAddressKeepBehavior     [x] impl  [ ] docstring  [ ] test
    # [ ] setIpAddressKeepBehavior     [x] impl  [ ] docstring  [ ] test
    # [ ] getIpv4Address               [x] impl  [ ] docstring  [ ] test
    # [ ] setIpv4Address               [x] impl  [ ] docstring  [ ] test
    # [ ] getIpv4AddressSource         [x] impl  [ ] docstring  [ ] test
    # [ ] setIpv4AddressSource         [x] impl  [ ] docstring  [ ] test
    # [ ] getNetworkMask               [x] impl  [ ] docstring  [ ] test
    # [ ] setNetworkMask               [x] impl  [ ] docstring  [ ] test
    # [ ] getTtl                       [x] impl  [ ] docstring  [ ] test
    # [ ] setTtl                       [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()

        self.assignmentPriority: PositiveInteger = None
        self.defaultGateway: Ip4AddressString = None
        self.dnsServerAddresses: List[Ip4AddressString] = []
        self.ipAddressKeepBehavior = None
        self.ipv4Address: Ip4AddressString = None
        self.ipv4AddressSource = None
        self.networkMask: Ip4AddressString = None
        self.ttl: PositiveInteger = None

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


class IpAddressKeepEnum(AREnum):
    """
    Defines the behavior after a dynamic IP address has been assigned.
    """

    # IpAddressKeepEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.138, p.466
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # (no methods) — enum value form serialized on Ipv4Configuration/Ipv6Configuration.ipAddressKeepBehavior

    # After a dynamic IP address has been assigned just use it for this session. Tags: atp.EnumerationLiteralIndex=0
    FORGET = "forget"

    # After a dynamic IP address has been assigned store the address persistently. Tags: atp.EnumerationLiteralIndex=1
    STORE_PERSISTENTLY = "storePersistently"

    def __init__(self):
        super().__init__(
            [
                IpAddressKeepEnum.FORGET,
                IpAddressKeepEnum.STORE_PERSISTENTLY,
            ]
        )


class Ipv6AddressSourceEnum(AREnum):
    """
    Defines how the node obtains its IPv6-Address.
    """

    # Ipv6AddressSourceEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.140, p.467
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # (no methods) — enum value form serialized on Ipv6Configuration.ipv6AddressSource

    # DHCP is a service for the automatic IP configuration of a client. Tags: atp.EnumerationLiteralIndex=0
    DHCPV6 = "dhcpv6"

    # The IP Address shall be declared manually. Tags: atp.EnumerationLiteralIndex=1
    FIXED = "fixed"

    # LinkLocal is intended only for communications within the segment of a local network (a link) or a point-to-point connection that a host is connected to. Tags: atp.EnumerationLiteralIndex=2
    LINK_LOCAL = "linkLocal"

    # Linklocal IPv6 Address Assignment using DoIP Parameters Tags: atp.EnumerationLiteralIndex=3
    LINK_LOCAL_DOIP = "LinkLocalDoIP"

    # IPv6 Stateless Autoconfiguration. Tags: atp.EnumerationLiteralIndex=4
    ROUTER_ADVERTISEMENT = "routerAdvertisement"

    def __init__(self):
        super().__init__(
            [
                Ipv6AddressSourceEnum.DHCPV6,
                Ipv6AddressSourceEnum.FIXED,
                Ipv6AddressSourceEnum.LINK_LOCAL,
                Ipv6AddressSourceEnum.LINK_LOCAL_DOIP,
                Ipv6AddressSourceEnum.ROUTER_ADVERTISEMENT,
            ]
        )


class EthernetConnectionNegotiationEnum(AREnum):
    """
    Specifies connection negotiation types of Ethernet transceiver links.
    """

    # EthernetConnectionNegotiationEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.55, p.110
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # (no methods) — enum value form serialized on CouplingPort.connectionNegotiationBehavior

    # Automatic Negotiation Tags: atp.EnumerationLiteralIndex=0
    AUTO = "auto"

    # Master Tags: atp.EnumerationLiteralIndex=1
    MASTER = "master"

    # Slave Tags: atp.EnumerationLiteralIndex=2
    SLAVE = "slave"

    def __init__(self):
        super().__init__(
            [
                EthernetConnectionNegotiationEnum.AUTO,
                EthernetConnectionNegotiationEnum.MASTER,
                EthernetConnectionNegotiationEnum.SLAVE,
            ]
        )


class CouplingPortRoleEnum(AREnum):
    """
    Defines the role a CouplingPort takes in the context of a CouplingElement.
    """

    # CouplingPortRoleEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table F.38, p.2013
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # (no methods) — enum value form serialized on CouplingPort.couplingPortRole

    # The hostPort is connected to an ECU (host ecu). The host ECU controls the connected Coupling Element (e.g. Ethernet switch). Tags: atp.EnumerationLiteralIndex=0
    HOST_PORT = "hostPort"

    # A CoupingPort can be a standardPort that is used to connect the CouplingElement with Coupling Ports outside the ECU. Tags: atp.EnumerationLiteralIndex=2
    STANDARD_PORT = "standardPort"

    # A CouplingPort can be connected to another CouplingPort of a CouplingElement located on the same ECU (CouplingElement.ecuInstance) using the CouplingPortConnection. This is used to model a cascaded switch. Tags: atp.EnumerationLiteralIndex=1
    UP_LINK_PORT = "upLinkPort"

    def __init__(self):
        super().__init__(
            [
                CouplingPortRoleEnum.HOST_PORT,
                CouplingPortRoleEnum.STANDARD_PORT,
                CouplingPortRoleEnum.UP_LINK_PORT,
            ]
        )


class EthernetMacLayerTypeEnum(AREnum):
    """
    Specifies MAC (Media Access Control) Layer types.
    """

    # EthernetMacLayerTypeEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.56, p.110
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # (no methods) — enum value form serialized on CouplingPort.macLayerType, EthernetCommunicationController.macLayerType

    # Mac layer interface (data) bandwith class 100Mbit/s and 10Mbit/s (e.g. RMII, RvMII, SMII, RvMII) Tags: atp.EnumerationLiteralIndex=0 xml.name=X-MII
    XMII = "X-MII"

    # Mac layer interface (data) bandwith class 1Gbit/s (e.g. GMII, RGMII, SGMII, RvGMII, USGMII) Tags: atp.EnumerationLiteralIndex=1 xml.name=XG-MII
    XGMII = "XG-MII"

    # Mac layer interface (data) bandwith class 10Gbit/s Tags: atp.EnumerationLiteralIndex=2 xml.name=XXG-MII
    XXGMII = "XXG-MII"

    def __init__(self):
        super().__init__(
            [
                EthernetMacLayerTypeEnum.XMII,
                EthernetMacLayerTypeEnum.XGMII,
                EthernetMacLayerTypeEnum.XXGMII,
            ]
        )


class Ipv6Configuration(NetworkEndpointAddress):
    """
    Internet Protocol version 6 (IPv6) configuration.
    """

    # Ipv6Configuration method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.139, p.466
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getAssignmentPriority        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setAssignmentPriority        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getDefaultRouter             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setDefaultRouter             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getDnsServerAddresses        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addDnsServerAddress          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getEnableAnycast             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setEnableAnycast             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getHopCount                  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setHopCount                  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getIpAddressKeepBehavior     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setIpAddressKeepBehavior     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getIpAddressPrefixLength     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setIpAddressPrefixLength     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getIpv6Address               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setIpv6Address               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getIpv6AddressSource         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setIpv6AddressSource         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # Priority of assignment (1 is highest). If a new address from an assignment method with a higher priority is available, it overwrites the IP address previously assigned by an assignment method with a lower priority.
        self.assignmentPriority: Optional[PositiveInteger] = None

        # IP address of the default router.
        self.defaultRouter: Optional[Ip6AddressString] = None

        # IP addresses of pre configured DNS servers.
        self.dnsServerAddresses: List[Ip6AddressString] = []

        # This attribute is used to enable anycast addressing (i.e. to one of multiple receivers).
        self.enableAnycast: Optional[Boolean] = None

        # The distance between two hosts. The hop count n means that n gateways separate the source host from the destination host (Range 0..255)
        self.hopCount: Optional[PositiveInteger] = None

        # Defines the lifetime of a dynamically fetched IP address.
        self.ipAddressKeepBehavior: Optional[IpAddressKeepEnum] = None

        # IPv6 prefix length defines the part of the IPv6 address that is the network prefix.
        self.ipAddressPrefixLength: Optional[PositiveInteger] = None

        # IPv6 Address. Notation: FFFF:...:FFFF. The IP Address shall be declared in case the ipv6AddressSource is FIXED and thus no auto-configuration mechanism is used.
        self.ipv6Address: Optional[Ip6AddressString] = None

        # Defines how the node obtains its IP address.
        self.ipv6AddressSource: Optional[Ipv6AddressSourceEnum] = None

    def getAssignmentPriority(self) -> Optional[PositiveInteger]:
        """Priority of assignment (1 is highest). If a new address from an assignment method with a higher priority is available, it overwrites the IP address previously assigned by an assignment method with a lower priority."""
        return self.assignmentPriority

    def setAssignmentPriority(self, value: Optional[PositiveInteger]) -> "Ipv6Configuration":
        """
        Priority of assignment (1 is highest). If a new address from an assignment method with a higher priority is available, it overwrites the IP address previously assigned by an assignment method with a lower priority.
        A None value is a no-op and does not overwrite an existing assignmentPriority.
        """
        if value is not None:
            self.assignmentPriority = value
        return self

    def getDefaultRouter(self) -> Optional[Ip6AddressString]:
        """IP address of the default router."""
        return self.defaultRouter

    def setDefaultRouter(self, value: Optional[Ip6AddressString]) -> "Ipv6Configuration":
        """
        IP address of the default router.
        A None value is a no-op and does not overwrite an existing defaultRouter.
        """
        if value is not None:
            self.defaultRouter = value
        return self

    def getDnsServerAddresses(self) -> List[Ip6AddressString]:
        """IP addresses of pre configured DNS servers."""
        return self.dnsServerAddresses

    def addDnsServerAddress(self, value: Optional[Ip6AddressString]) -> "Ipv6Configuration":
        """
        IP addresses of pre configured DNS servers.
        A None value is a no-op and does not append to dnsServerAddresses.
        """
        if value is not None:
            self.dnsServerAddresses.append(value)
        return self

    def getEnableAnycast(self) -> Optional[Boolean]:
        """This attribute is used to enable anycast addressing (i.e. to one of multiple receivers)."""
        return self.enableAnycast

    def setEnableAnycast(self, value: Optional[Boolean]) -> "Ipv6Configuration":
        """
        This attribute is used to enable anycast addressing (i.e. to one of multiple receivers).
        A None value is a no-op and does not overwrite an existing enableAnycast.
        """
        if value is not None:
            self.enableAnycast = value
        return self

    def getHopCount(self) -> Optional[PositiveInteger]:
        """The distance between two hosts. The hop count n means that n gateways separate the source host from the destination host (Range 0..255)"""
        return self.hopCount

    def setHopCount(self, value: Optional[PositiveInteger]) -> "Ipv6Configuration":
        """
        The distance between two hosts. The hop count n means that n gateways separate the source host from the destination host (Range 0..255)
        A None value is a no-op and does not overwrite an existing hopCount.
        """
        if value is not None:
            self.hopCount = value
        return self

    def getIpAddressKeepBehavior(self) -> Optional[IpAddressKeepEnum]:
        """Defines the lifetime of a dynamically fetched IP address."""
        return self.ipAddressKeepBehavior

    def setIpAddressKeepBehavior(self, value: Optional[IpAddressKeepEnum]) -> "Ipv6Configuration":
        """
        Defines the lifetime of a dynamically fetched IP address.
        A None value is a no-op and does not overwrite an existing ipAddressKeepBehavior.
        """
        if value is not None:
            self.ipAddressKeepBehavior = value
        return self

    def getIpAddressPrefixLength(self) -> Optional[PositiveInteger]:
        """IPv6 prefix length defines the part of the IPv6 address that is the network prefix."""
        return self.ipAddressPrefixLength

    def setIpAddressPrefixLength(self, value: Optional[PositiveInteger]) -> "Ipv6Configuration":
        """
        IPv6 prefix length defines the part of the IPv6 address that is the network prefix.
        A None value is a no-op and does not overwrite an existing ipAddressPrefixLength.
        """
        if value is not None:
            self.ipAddressPrefixLength = value
        return self

    def getIpv6Address(self) -> Optional[Ip6AddressString]:
        """IPv6 Address. Notation: FFFF:...:FFFF. The IP Address shall be declared in case the ipv6AddressSource is FIXED and thus no auto-configuration mechanism is used."""
        return self.ipv6Address

    def setIpv6Address(self, value: Optional[Ip6AddressString]) -> "Ipv6Configuration":
        """
        IPv6 Address. Notation: FFFF:...:FFFF. The IP Address shall be declared in case the ipv6AddressSource is FIXED and thus no auto-configuration mechanism is used.
        A None value is a no-op and does not overwrite an existing ipv6Address.
        """
        if value is not None:
            self.ipv6Address = value
        return self

    def getIpv6AddressSource(self) -> Optional[Ipv6AddressSourceEnum]:
        """Defines how the node obtains its IP address."""
        return self.ipv6AddressSource

    def setIpv6AddressSource(self, value: Optional[Ipv6AddressSourceEnum]) -> "Ipv6Configuration":
        """
        Defines how the node obtains its IP address.
        A None value is a no-op and does not overwrite an existing ipv6AddressSource.
        """
        if value is not None:
            self.ipv6AddressSource = value
        return self


class DoIpEntity(ARObject):
    """
    Defines properties for a DoIP (Diagnostics over IP) entity,
    specifying the role and behavior of DoIP-enabled devices in
    the network for diagnostic communication purposes.
    """

    # DoIpEntity method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getDoIpEntityRole            [x] impl  [ ] docstring  [ ] test
    # [ ] setDoIpEntityRole            [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()

        self.doIpEntityRole = None  # type: DoIpEntityRoleEnum

    def getDoIpEntityRole(self):
        return self.doIpEntityRole

    def setDoIpEntityRole(self, value):
        if value is not None:
            self.doIpEntityRole = value
        return self


class OrderedMaster(ARObject):
    """Element in the network endpoint list."""

    # OrderedMaster method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.148, p.470
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] getIndex                     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] setIndex                     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTimeSyncServer            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] setTimeSyncServer            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # Defines the order of the network endpoint list (e.g. 0, 1, 2, ...).
        self.index: Optional[PositiveInteger] = None

        # Reference to a master (Time Sync Server).
        self.timeSyncServer: Optional[RefType] = None

    def getIndex(self) -> Optional[PositiveInteger]:
        """Defines the order of the network endpoint list (e.g. 0, 1, 2, ...)."""
        return self.index

    def setIndex(self, value: Optional[PositiveInteger]) -> "OrderedMaster":
        """
        Defines the order of the network endpoint list (e.g. 0, 1, 2, ...).
        A None value is a no-op and does not overwrite an existing index.
        """
        if value is not None:
            self.index = value
        return self

    def getTimeSyncServer(self) -> Optional[RefType]:
        """Reference to a master (Time Sync Server)."""
        return self.timeSyncServer

    def setTimeSyncServer(self, value: Optional[RefType]) -> "OrderedMaster":
        """
        Reference to a master (Time Sync Server).
        A None value is a no-op and does not overwrite an existing timeSyncServer.
        """
        if value is not None:
            self.timeSyncServer = value
        return self


class TimeSyncClientConfiguration(ARObject):
    """
    Configures time synchronization client properties, defining
    ordered master relationships and time synchronization
    technology settings for network time coordination.
    """

    # TimeSyncClientConfiguration method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.147, p.469
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] getOrderedMasters            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addOrderedMaster             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTimeSyncTechnology        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] setTimeSyncTechnology        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        self.orderedMasters: List[OrderedMaster] = []
        self.timeSyncTechnology = None  # type: TimeSyncTechnologyEnum

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

    # TimeSyncServerConfiguration method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getPriority                  [x] impl  [ ] docstring  [ ] test
    # [ ] setPriority                  [x] impl  [ ] docstring  [ ] test
    # [ ] getSyncInterval              [x] impl  [ ] docstring  [ ] test
    # [ ] setSyncInterval              [x] impl  [ ] docstring  [ ] test
    # [ ] getTimeSyncServerIdentifier  [x] impl  [ ] docstring  [ ] test
    # [ ] setTimeSyncServerIdentifier  [x] impl  [ ] docstring  [ ] test
    # [ ] getTimeSyncTechnology        [x] impl  [ ] docstring  [ ] test
    # [ ] setTimeSyncTechnology        [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.priority: PositiveInteger = None
        self.syncInterval: TimeValue = None
        self.timeSyncServerIdentifier: String = None
        self.timeSyncTechnology = None  # type: TimeSyncTechnologyEnum

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

    # TimeSynchronization method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getTimeSyncClient            [x] impl  [ ] docstring  [ ] test
    # [ ] setTimeSyncClient            [x] impl  [ ] docstring  [ ] test
    # [ ] getTimeSyncServer            [x] impl  [ ] docstring  [ ] test
    # [ ] setTimeSyncServer            [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()

        self.timeSyncClient: TimeSyncClientConfiguration = None
        self.timeSyncServer: TimeSyncServerConfiguration = None

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
    Defines the network infrastructure services provided or consumed.
    """

    # InfrastructureServices method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.144, p.469
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getDoIpEntity                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setDoIpEntity                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTimeSynchronization       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setTimeSynchronization       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # Defines whether a infrastructure service that runs on the network endpoint is a DoIP-Entity.
        self.doIpEntity: Optional[DoIpEntity] = None

        # Defines the servers / clients in a time synchronised network.
        self.timeSynchronization: Optional[TimeSynchronization] = None

    def getDoIpEntity(self) -> Optional[DoIpEntity]:
        """Defines whether a infrastructure service that runs on the network endpoint is a DoIP-Entity."""
        return self.doIpEntity

    def setDoIpEntity(self, value: Optional[DoIpEntity]) -> "InfrastructureServices":
        """
        Defines whether a infrastructure service that runs on the network endpoint is a DoIP-Entity.
        A None value is a no-op and does not overwrite an existing doIpEntity.
        """
        if value is not None:
            self.doIpEntity = value
        return self

    def getTimeSynchronization(self) -> Optional[TimeSynchronization]:
        """Defines the servers / clients in a time synchronised network."""
        return self.timeSynchronization

    def setTimeSynchronization(self, value: Optional[TimeSynchronization]) -> "InfrastructureServices":
        """
        Defines the servers / clients in a time synchronised network.
        A None value is a no-op and does not overwrite an existing timeSynchronization.
        """
        if value is not None:
            self.timeSynchronization = value
        return self


class NetworkEndpoint(Identifiable):
    """
    Represents a network endpoint in the AUTOSAR system, defining
    IP configuration, infrastructure services, and network address
    properties for communication nodes in the network.
    """

    # NetworkEndpoint method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getFullyQualifiedDomainName  [x] impl  [ ] docstring  [ ] test
    # [ ] setFullyQualifiedDomainName  [x] impl  [ ] docstring  [ ] test
    # [ ] getInfrastructureServices    [x] impl  [ ] docstring  [ ] test
    # [ ] setInfrastructureServices    [x] impl  [ ] docstring  [ ] test
    # [ ] getIpSecConfig               [x] impl  [ ] docstring  [ ] test
    # [ ] setIpSecConfig               [x] impl  [ ] docstring  [ ] test
    # [ ] getNetworkEndpointAddresses  [x] impl  [ ] docstring  [ ] test
    # [ ] addNetworkEndpointAddress    [x] impl  [ ] docstring  [ ] test
    # [ ] getPriority                  [x] impl  [ ] docstring  [ ] test
    # [ ] setPriority                  [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.fullyQualifiedDomainName: String = None
        self.infrastructureServices: InfrastructureServices = None
        self.ipSecConfig = None
        self.networkEndpointAddresses: List[NetworkEndpointAddress] = []
        self.priority: PositiveInteger = None

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


class EthernetPhysicalLayerTypeEnum(AREnum):
    """
    Specifies physical layer types of Ethernet transceiver links.
    """

    # EthernetPhysicalLayerTypeEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.57, p.111
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # (no methods) — enum value form serialized on CouplingPort.physicalLayerType

    # Ethernet Standard (IEEE 802.3ab) to support 1Gbit/s over 4 twisted pairs. Tags: atp.EnumerationLiteralIndex=6 xml.name=1000BASE-T
    _1000BASE_T = "1000BASE-T"

    # Ethernet Standard (IEEE 802.3bp) to support 1Gbit/s over a single twisted pair cable. Tags: atp.EnumerationLiteralIndex=8 xml.name=1000BASE-T1
    _1000BASE_T1 = "1000BASE-T1"

    # Ethernet Standard (IEEE 802.3bw) to support 100Mbit/s over a single twisted pair cable. 100BASE-T1 is the IEEE Standardized version of BroadRReach. Tags: atp.EnumerationLiteralIndex=7 xml.name=100BASE-T1
    _100BASE_T1 = "100BASE-T1"

    # Ethernet Standard (IEEE 802.3u) to support 100Mbit/s over two twisted pairs. Tags: atp.EnumerationLiteralIndex=5 xml.name=100BASE-TX
    _100BASE_TX = "100BASE-TX"

    # Physical layer interface 10BASE-T1S (10Mbit/s, 2 pairs). Used for automotive. Tags: atp.EnumerationLiteralIndex=10 atp.Status=draft xml.name=10BASE-T1S
    _10BASE_T1S = "10BASE-T1S"

    # Ethernet Standard (IEEE 802.11p) to support wireless communication in vehicular environments. Tags: atp.EnumerationLiteralIndex=9 xml.name=IEEE802-11P
    I_EEE802_11P = "IEEE802-11P"

    def __init__(self):
        super().__init__(
            [
                EthernetPhysicalLayerTypeEnum._1000BASE_T,
                EthernetPhysicalLayerTypeEnum._1000BASE_T1,
                EthernetPhysicalLayerTypeEnum._100BASE_T1,
                EthernetPhysicalLayerTypeEnum._100BASE_TX,
                EthernetPhysicalLayerTypeEnum._10BASE_T1S,
                EthernetPhysicalLayerTypeEnum.I_EEE802_11P,
            ]
        )


class EthernetSwitchVlanIngressTagEnum(AREnum):
    """
    Defines the possible tagging behavior at an ingress port.
    """

    # EthernetSwitchVlanIngressTagEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.58, p.111
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # (no methods) — enum value form serialized on CouplingPort.receiveActivity

    # Forward with the same VLAN as received. Also untagged frames will be forwarded as untagged. Tags: atp.EnumerationLiteralIndex=0
    FORWARD_AS_IS = "forwardAsIs"

    # Drop if untagged. Tags: atp.EnumerationLiteralIndex=1
    DROP_UNTAGGED = "dropUntagged"

    def __init__(self):
        super().__init__(
            [
                EthernetSwitchVlanIngressTagEnum.FORWARD_AS_IS,
                EthernetSwitchVlanIngressTagEnum.DROP_UNTAGGED,
            ]
        )


class TimeSyncTechnologyEnum(AREnum):
    """
    Timesynchronization. Server/Client configuration.
    """

    # TimeSyncTechnologyEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.149, p.471
    # Spec verified: R23-11
    # (no methods) — enum value form serialized on consuming attribute

    # Ethernet AVB compliant IEEE802.1AS Precision Time Protocol Tags: atp.EnumerationLiteralIndex=0
    AVB_IEEE802_1AS = "AVB-IEEE-802-1-AS"

    # Network Time Protocol (NTP) Tags: atp.EnumerationLiteralIndex=1
    NTP_RFC958 = "NTP-RFC-958"

    # Precision Time Protocol (PTP) IEEE 1588-2002 Tags: atp.EnumerationLiteralIndex=2
    PTP_IEEE1588_2002 = "PTP-IEEE-1588-2002"

    # Precision Time Protocol (PTP) IEEE 1588-2008 Tags: atp.EnumerationLiteralIndex=3
    PTP_IEEE1588_2008 = "PTP-IEEE-1588-2008"

    def __init__(self):
        super().__init__(
            [
                TimeSyncTechnologyEnum.AVB_IEEE802_1AS,
                TimeSyncTechnologyEnum.NTP_RFC958,
                TimeSyncTechnologyEnum.PTP_IEEE1588_2002,
                TimeSyncTechnologyEnum.PTP_IEEE1588_2008,
            ]
        )


class DoIpEntityRoleEnum(AREnum):
    """
    DoIP role a network-node has.
    """

    # DoIpEntityRoleEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.151, p.471
    # Spec verified: R23-11
    # (no methods) — enum value form serialized on DoIpEntity.doIpEntityRole

    # Network node is a DoIP gateway that accepts external connections. Tags: atp.EnumerationLiteralIndex=0
    EDGE_NODE = "edgeNode"

    # Network node is a Gateway between the DoIP network and other networks. Tags: atp.EnumerationLiteralIndex=1
    GATEWAY = "gateway"

    # Network node is a DoIp node. Tags: atp.EnumerationLiteralIndex=2
    NODE = "node"

    def __init__(self):
        super().__init__(
            [
                DoIpEntityRoleEnum.EDGE_NODE,
                DoIpEntityRoleEnum.GATEWAY,
                DoIpEntityRoleEnum.NODE,
            ]
        )


class PlcaProps(ARObject):
    """
    This meta-class allows to configure the PLCA (Physical Layer Collision Avoidance) in case 10-BASE-T1S Ethernet is used and PLCA is enabled on the CouplingPort (PHY).
    """

    # PlcaProps method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.117, p.169
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                       [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getPlcaLocalNodeId             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setPlcaLocalNodeId             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getPlcaMaxBurstCount           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setPlcaMaxBurstCount           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getPlcaMaxBurstTimer           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setPlcaMaxBurstTimer           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # This attribute defines the node ID when the PLCA mode for 10BASE-T1S is used.
        self.plcaLocalNodeId: Optional[PositiveInteger] = None

        # Defines maximum packets allowed to be transmitted within a TO. This configuration can be different from one ECU to another within the PLCA mixed segment.
        self.plcaMaxBurstCount: Optional[PositiveInteger] = None

        # Limits the burst frames in bit time. This configuration can be different from one ECU to another within the PLCA mixed segment. For PLCA burst mode to work properly this timer should be set greater than one IPG.
        self.plcaMaxBurstTimer: Optional[PositiveInteger] = None

    def getPlcaLocalNodeId(self) -> Optional[PositiveInteger]:
        """This attribute defines the node ID when the PLCA mode for 10BASE-T1S is used."""
        return self.plcaLocalNodeId

    def setPlcaLocalNodeId(self, value: Optional[PositiveInteger]) -> "PlcaProps":
        """
        This attribute defines the node ID when the PLCA mode for 10BASE-T1S is used.
        A None value is a no-op and does not overwrite an existing plcaLocalNodeId.
        """
        if value is not None:
            self.plcaLocalNodeId = value
        return self

    def getPlcaMaxBurstCount(self) -> Optional[PositiveInteger]:
        """Defines maximum packets allowed to be transmitted within a TO. This configuration can be different from one ECU to another within the PLCA mixed segment."""
        return self.plcaMaxBurstCount

    def setPlcaMaxBurstCount(self, value: Optional[PositiveInteger]) -> "PlcaProps":
        """
        Defines maximum packets allowed to be transmitted within a TO. This configuration can be different from one ECU to another within the PLCA mixed segment.
        A None value is a no-op and does not overwrite an existing plcaMaxBurstCount.
        """
        if value is not None:
            self.plcaMaxBurstCount = value
        return self

    def getPlcaMaxBurstTimer(self) -> Optional[PositiveInteger]:
        """Limits the burst frames in bit time. This configuration can be different from one ECU to another within the PLCA mixed segment. For PLCA burst mode to work properly this timer should be set greater than one IPG."""
        return self.plcaMaxBurstTimer

    def setPlcaMaxBurstTimer(self, value: Optional[PositiveInteger]) -> "PlcaProps":
        """
        Limits the burst frames in bit time. This configuration can be different from one ECU to another within the PLCA mixed segment. For PLCA burst mode to work properly this timer should be set greater than one IPG.
        A None value is a no-op and does not overwrite an existing plcaMaxBurstTimer.
        """
        if value is not None:
            self.plcaMaxBurstTimer = value
        return self


class CouplingPortConnection(ARObject):
    """
    Connection between two CouplingPorts (firstPort and secondPort) or between a collection of Ports that are all referenced by the portCollection reference.
    """

    # CouplingPortConnection method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.60, p.113
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                       [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getFirstPortRef                   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setFirstPortRef                   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getNodePortRefs                   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addNodePortRef                    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getPlcaLocalNodeCount          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setPlcaLocalNodeCount          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getPlcaTransmitOpportunityTimer [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setPlcaTransmitOpportunityTimer [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSecondPortRef                  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSecondPortRef                  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # Reference to the first CouplingPort that is connected via the CouplingPortConnection.
        self.firstPortRef: Optional[RefType] = None

        # Reference to a number of CouplingPorts that are connected via the CouplingPortConnection. This reference shall be used to describe a 10BASE-T1S topology architecture where several CouplingPorts of EthernetCommunicationControllers are connected via one CouplingPortConnection. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=nodePort.couplingPort, nodePort.variation Point.shortLabel vh.latestBindingTime=postBuild
        self.nodePortRefs: List[RefType] = []

        # Defines the number of communication participants in case 10BASE-T1S and the nodePort reference is used.
        self.plcaLocalNodeCount: Optional[PositiveInteger] = None

        # Timer for the transmission in bit time to evaluate if a Transmission Opportunity is yield or not.
        self.plcaTransmitOpportunityTimer: Optional[PositiveInteger] = None

        # Reference to the second CouplingPort that is connected via the CouplingPortConnection.
        self.secondPortRef: Optional[RefType] = None

    def getFirstPortRef(self) -> Optional[RefType]:
        """Reference to the first CouplingPort that is connected via the CouplingPortConnection."""
        return self.firstPortRef

    def setFirstPortRef(self, value: Optional[RefType]) -> "CouplingPortConnection":
        """
        Reference to the first CouplingPort that is connected via the CouplingPortConnection.
        A None value is a no-op and does not overwrite an existing firstPortRef.
        """
        if value is not None:
            self.firstPortRef = value
        return self

    def getNodePortRefs(self) -> List[RefType]:
        """Reference to a number of CouplingPorts that are connected via the CouplingPortConnection. This reference shall be used to describe a 10BASE-T1S topology architecture where several CouplingPorts of EthernetCommunicationControllers are connected via one CouplingPortConnection. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=nodePort.couplingPort, nodePort.variation Point.shortLabel vh.latestBindingTime=postBuild"""
        return self.nodePortRefs

    def addNodePortRef(self, value: Optional[RefType]) -> "CouplingPortConnection":
        """
        Reference to a number of CouplingPorts that are connected via the CouplingPortConnection. This reference shall be used to describe a 10BASE-T1S topology architecture where several CouplingPorts of EthernetCommunicationControllers are connected via one CouplingPortConnection. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=nodePort.couplingPort, nodePort.variation Point.shortLabel vh.latestBindingTime=postBuild
        A None value is a no-op and does not append to nodePortRefs.
        """
        if value is not None:
            self.nodePortRefs.append(value)
        return self

    def getPlcaLocalNodeCount(self) -> Optional[PositiveInteger]:
        """Defines the number of communication participants in case 10BASE-T1S and the nodePort reference is used."""
        return self.plcaLocalNodeCount

    def setPlcaLocalNodeCount(self, value: Optional[PositiveInteger]) -> "CouplingPortConnection":
        """
        Defines the number of communication participants in case 10BASE-T1S and the nodePort reference is used.
        A None value is a no-op and does not overwrite an existing plcaLocalNodeCount.
        """
        if value is not None:
            self.plcaLocalNodeCount = value
        return self

    def getPlcaTransmitOpportunityTimer(self) -> Optional[PositiveInteger]:
        """Timer for the transmission in bit time to evaluate if a Transmission Opportunity is yield or not."""
        return self.plcaTransmitOpportunityTimer

    def setPlcaTransmitOpportunityTimer(self, value: Optional[PositiveInteger]) -> "CouplingPortConnection":
        """
        Timer for the transmission in bit time to evaluate if a Transmission Opportunity is yield or not.
        A None value is a no-op and does not overwrite an existing plcaTransmitOpportunityTimer.
        """
        if value is not None:
            self.plcaTransmitOpportunityTimer = value
        return self

    def getSecondPortRef(self) -> Optional[RefType]:
        """Reference to the second CouplingPort that is connected via the CouplingPortConnection."""
        return self.secondPortRef

    def setSecondPortRef(self, value: Optional[RefType]) -> "CouplingPortConnection":
        """
        Reference to the second CouplingPort that is connected via the CouplingPortConnection.
        A None value is a no-op and does not overwrite an existing secondPortRef.
        """
        if value is not None:
            self.secondPortRef = value
        return self


class GlobalTimeCouplingPortProps(ARObject):
    """
    Defines properties for the usage of the CouplingPort in the scope of Global Time Sync.
    """

    # GlobalTimeCouplingPortProps method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 9.18, p.875
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                       [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getPropagationDelay            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setPropagationDelay            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # If cyclic propagation delay measurement is enabled, this parameter represents the default value of the propagation delay until the first actually measured propagation delay is available. If cyclic propagation delay measurement is disabled, this parameter defines a fixed value for the propagation delay.
        self.propagationDelay: Optional[TimeValue] = None

    def getPropagationDelay(self) -> Optional[TimeValue]:
        """If cyclic propagation delay measurement is enabled, this parameter represents the default value of the propagation delay until the first actually measured propagation delay is available. If cyclic propagation delay measurement is disabled, this parameter defines a fixed value for the propagation delay."""
        return self.propagationDelay

    def setPropagationDelay(self, value: Optional[TimeValue]) -> "GlobalTimeCouplingPortProps":
        """
        If cyclic propagation delay measurement is enabled, this parameter represents the default value of the propagation delay until the first actually measured propagation delay is available. If cyclic propagation delay measurement is disabled, this parameter defines a fixed value for the propagation delay.
        A None value is a no-op and does not overwrite an existing propagationDelay.
        """
        if value is not None:
            self.propagationDelay = value
        return self


class CouplingPortRatePolicyActionEnum(AREnum):
    """
    Defines the action to be performed when a rate policy is violated.
    """

    # CouplingPortRatePolicyActionEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.70, p.125
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # (no methods) — enum value form serialized on CouplingPortRatePolicy.policyAction

    # If the rate policy is violated the frame shall be dropped. Tags: atp.EnumerationLiteralIndex=0
    DROP_FRAME = "dropFrame"

    # If the rate policy is violated the CouplingPort this CouplingPortRatePolicy is defined on shall block all frames from the MAC-Address the violation was caused by. Tags: atp.EnumerationLiteralIndex=1
    BLOCK_SOURCE = "blockSource"

    def __init__(self):
        super().__init__(
            [
                CouplingPortRatePolicyActionEnum.DROP_FRAME,
                CouplingPortRatePolicyActionEnum.BLOCK_SOURCE,
            ]
        )


class CouplingPortRatePolicy(ARObject):
    """
    Defines a rate policy on a CouplingPort.
    """

    # CouplingPortRatePolicy method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.69, p.124
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__            [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getDataLength       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setDataLength       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getPolicyAction     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setPolicyAction     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getPriority         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setPriority         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTimeInterval     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setTimeInterval     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] addVlanRef          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getVlanRefs         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer

    def __init__(self):
        super().__init__()

        # Amount of data in bytes (excluding header information) that can be received to define the rate policy.
        self.dataLength: Optional[PositiveInteger] = None

        # Defines the action to be performed when this rate policy is violated.
        self.policyAction: Optional[CouplingPortRatePolicyActionEnum] = None

        # Defines the priority which this rate policy shall be limited on. If no priority is given this rate policy is not considering priority.
        self.priority: Optional[PositiveInteger] = None

        # Time interval used to define the base of the rate policy.
        self.timeInterval: Optional[TimeValue] = None

        # Defines the VLANs this rate policy shall be limited on. If no VLAN is given this rate policy is not considering VLAN tags.
        self.vLanRefs: List[RefType] = []

    def getDataLength(self) -> Optional[PositiveInteger]:
        """Amount of data in bytes (excluding header information) that can be received to define the rate policy."""
        return self.dataLength

    def setDataLength(self, value: Optional[PositiveInteger]) -> "CouplingPortRatePolicy":
        """
        Amount of data in bytes (excluding header information) that can be received to define the rate policy.
        A None value is a no-op and does not overwrite an existing dataLength.
        """
        if value is not None:
            self.dataLength = value
        return self

    def getPolicyAction(self) -> Optional[CouplingPortRatePolicyActionEnum]:
        """Defines the action to be performed when this rate policy is violated."""
        return self.policyAction

    def setPolicyAction(self, value: Optional[CouplingPortRatePolicyActionEnum]) -> "CouplingPortRatePolicy":
        """
        Defines the action to be performed when this rate policy is violated.
        A None value is a no-op and does not overwrite an existing policyAction.
        """
        if value is not None:
            self.policyAction = value
        return self

    def getPriority(self) -> Optional[PositiveInteger]:
        """Defines the priority which this rate policy shall be limited on. If no priority is given this rate policy is not considering priority."""
        return self.priority

    def setPriority(self, value: Optional[PositiveInteger]) -> "CouplingPortRatePolicy":
        """
        Defines the priority which this rate policy shall be limited on. If no priority is given this rate policy is not considering priority.
        A None value is a no-op and does not overwrite an existing priority.
        """
        if value is not None:
            self.priority = value
        return self

    def getTimeInterval(self) -> Optional[TimeValue]:
        """Time interval used to define the base of the rate policy."""
        return self.timeInterval

    def setTimeInterval(self, value: Optional[TimeValue]) -> "CouplingPortRatePolicy":
        """
        Time interval used to define the base of the rate policy.
        A None value is a no-op and does not overwrite an existing timeInterval.
        """
        if value is not None:
            self.timeInterval = value
        return self

    def addVlanRef(self, value: Optional[RefType]) -> "CouplingPortRatePolicy":
        """
        Defines the VLANs this rate policy shall be limited on. If no VLAN is given this rate policy is not considering VLAN tags.
        A None value is a no-op and does not append to vLanRefs.
        """
        if value is not None:
            self.vLanRefs.append(value)
        return self

    def getVlanRefs(self) -> List[RefType]:
        """Defines the VLANs this rate policy shall be limited on. If no VLAN is given this rate policy is not considering VLAN tags."""
        return self.vLanRefs
