"""
Test suite for EthernetTopology classes in AUTOSAR System Template.

This module contains comprehensive unit tests for Ethernet communication topology classes
including Ethernet clusters, communication controllers, connectors, and related components.
Each test validates the functionality, inheritance, and setter/getter methods
of the respective classes.
"""

import inspect
from typing import List, Optional, get_type_hints

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Describable, Identifiable, Referrable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, RefType, TimeValue
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.TagWithOptionalValue import TagWithOptionalValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    CouplingPort,
    CouplingPortConnection,
    CouplingPortDetails,
    CouplingPortFifo,
    CouplingPortRatePolicy,
    CouplingPortRatePolicyActionEnum,
    CouplingPortRoleEnum,
    CouplingPortScheduler,
    CouplingPortShaper,
    CouplingPortStructuralElement,
    CouplingPortTrafficClassAssignment,
    DhcpServerConfiguration,
    DoIpEntity,
    DoIpEntityRoleEnum,
    EthernetCluster,
    EthernetCommunicationConnector,
    EthernetCommunicationController,
    EthernetConnectionNegotiationEnum,
    EthernetCouplingPortSchedulerEnum,
    EthernetMacLayerTypeEnum,
    EthernetPhysicalChannel,
    EthernetPhysicalLayerTypeEnum,
    EthernetPriorityRegeneration,
    EthernetSwitchVlanIngressTagEnum,
    GlobalTimeCouplingPortProps,
    InfrastructureServices,
    IpAddressKeepEnum,
    Ipv4Configuration,
    Ipv4DhcpServerConfiguration,
    Ipv6AddressSourceEnum,
    Ipv6Configuration,
    Ipv6DhcpServerConfiguration,
    MacMulticastGroup,
    NetworkEndpoint,
    NetworkEndpointAddress,
    OrderedMaster,
    PlcaProps,
    SdClientConfig,
    TimeSyncClientConfiguration,
    TimeSynchronization,
    TimeSyncServerConfiguration,
    TimeSyncTechnologyEnum,
    VlanMembership,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import InitialSdDelayConfig, RequestResponseDelay, SoAdConfig
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import CommunicationCluster, FibexElement


def _pos_int(text):
    value = PositiveInteger()
    value.setValue(text)
    return value


class MockParent(ARObject):
    """
    Mock parent class for testing purposes.

    This class extends ARObject to provide a concrete implementation
    that can be used as a parent for testing classes that require
    an ARObject instance during initialization.
    """

    def __init__(self):
        super().__init__()


class TestEthernetTopology:
    """
    Test class for EthernetTopology module functionality.

    This class contains test methods for validating the behavior of
    Ethernet communication topology classes, including their initialization,
    inheritance relationships, and property accessors.
    """

    def test_mac_multicast_group(self):
        """
        Test the MacMulticastGroup class initialization and methods.
        """
        parent = MockParent()
        group = MacMulticastGroup(parent, "TestGroup")

        assert group.getShortName() == "TestGroup"
        assert group.getMacMulticastAddress() is None

        # Test setting MAC multicast address
        test_address = "01:02:03:04:05:06"
        result = group.setMacMulticastAddress(test_address)
        assert group.getMacMulticastAddress() == test_address
        assert result == group  # Test method chaining

    def test_ethernet_cluster(self):
        """
        Test the EthernetCluster class initialization and methods (Table 3.47).
        """
        parent = MockParent()
        cluster = EthernetCluster(parent, "TestCluster")

        assert cluster.getShortName() == "TestCluster"
        assert cluster.getCouplingPortConnections() == []
        assert cluster.getCouplingPortStartupActiveTime() is None
        assert cluster.getCouplingPortSwitchoffDelay() is None
        assert cluster.getMacMulticastGroups() == []

        # Test setting timing values with method chaining and None no-ops
        test_time = 100
        result = cluster.setCouplingPortStartupActiveTime(test_time)
        assert cluster.getCouplingPortStartupActiveTime() == test_time
        assert result == cluster  # Test method chaining

        result = cluster.setCouplingPortStartupActiveTime(None)
        assert cluster.getCouplingPortStartupActiveTime() == test_time

        result = cluster.setCouplingPortSwitchoffDelay(test_time)
        assert cluster.getCouplingPortSwitchoffDelay() == test_time
        assert result == cluster  # Test method chaining

        # Test adding coupling port connection with method chaining and None no-op
        connection = MockParent()
        result = cluster.addCouplingPortConnection(connection)
        assert cluster.getCouplingPortConnections() == [connection]
        assert result == cluster  # Test method chaining

        cluster.addCouplingPortConnection(None)
        assert cluster.getCouplingPortConnections() == [connection]

        # Test creating MAC multicast group
        test_group = cluster.createMacMulticastGroup("TestMulticastGroup")
        assert isinstance(test_group, MacMulticastGroup)
        assert test_group.getShortName() == "TestMulticastGroup"

    def test_coupling_port_structural_element(self):
        """
        Test the CouplingPortStructuralElement abstract class (Table 3.64, p.122).
        """
        parent = MockParent()

        # Test that abstract class cannot be instantiated directly
        with pytest.raises(TypeError):
            CouplingPortStructuralElement(parent, "TestElement")

    def test_coupling_port_structural_element_docstring_is_spec_note(self):
        """Class docstring carries the spec Note verbatim (Table 3.64, p.122)."""
        assert CouplingPortStructuralElement.__doc__.strip() == "General class to define structural elements a CouplingPort may consist of."

    def test_coupling_port_structural_element_init_has_no_docstring(self):
        assert CouplingPortStructuralElement.__init__.__doc__ is None

    def test_coupling_port_structural_element_subclasses(self):
        assert issubclass(CouplingPortFifo, CouplingPortStructuralElement)
        assert issubclass(CouplingPortScheduler, CouplingPortStructuralElement)

    def test_coupling_port_fifo(self):
        """
        Test the CouplingPortFifo class initialization and methods (Table 3.68).
        """
        parent = MockParent()
        fifo = CouplingPortFifo(parent, "TestFifo")

        assert fifo.getShortName() == "TestFifo"
        assert fifo.getAssignedTrafficClasses() == []
        assert fifo.getMinimumFifoLength() is None
        assert fifo.getShaper() is None

        # Test adding traffic class with method chaining and None no-op
        result = fifo.addAssignedTrafficClass(5)
        assert fifo.getAssignedTrafficClasses() == [5]
        assert result == fifo  # Test method chaining

        fifo.addAssignedTrafficClass(None)
        assert fifo.getAssignedTrafficClasses() == [5]

        # Test setting minimum FIFO length with method chaining
        result = fifo.setMinimumFifoLength(1024)
        assert fifo.getMinimumFifoLength() == 1024
        assert result == fifo  # Test method chaining

        # None no-op for minimumFifoLength
        result = fifo.setMinimumFifoLength(None)
        assert fifo.getMinimumFifoLength() == 1024

        # Test setting shaper with method chaining
        shaper = MockParent()
        result = fifo.setShaper(shaper)
        assert fifo.getShaper() is shaper
        assert result == fifo  # Test method chaining

        # None no-op for shaper
        result = fifo.setShaper(None)
        assert fifo.getShaper() is shaper

    def test_coupling_port_fifo_removed_members(self):
        """
        trafficClassPreemptionSupport is absent from the R23-11 Table 3.68 and XSD group (Rule 0015).
        """
        fifo = CouplingPortFifo(MockParent(), "TestFifo")
        assert not hasattr(fifo, "trafficClassPreemptionSupport")

    def test_coupling_port_fifo_docstrings_are_spec_notes(self):
        """Accessors carry the Table 3.68 (p.124) Notes verbatim, incl. the shaper Tags tail."""
        class_note = "Defines a FIFO for the CouplingPort egress structure."
        assigned_note = "Defines a set of Traffic Classes which shall be handled by this FIFO. range: 0-7"
        minimum_note = "FIFO minimum length in Byte. An actual configuration/ hardware may use a bigger value."
        shaper_note = "Definition of the shaper to be used for the processing of this FIFO. Tags: atp.Status=candidate"
        assert inspect.cleandoc(CouplingPortFifo.__doc__).strip() == class_note
        assert inspect.cleandoc(CouplingPortFifo.addAssignedTrafficClass.__doc__).strip() == assigned_note + "\nA None value is a no-op and does not append to assignedTrafficClasses."
        assert inspect.cleandoc(CouplingPortFifo.getAssignedTrafficClasses.__doc__).strip() == assigned_note
        assert inspect.cleandoc(CouplingPortFifo.getMinimumFifoLength.__doc__).strip() == minimum_note
        assert inspect.cleandoc(CouplingPortFifo.setMinimumFifoLength.__doc__).strip() == minimum_note + "\nA None value is a no-op and does not overwrite an existing minimumFifoLength."
        assert inspect.cleandoc(CouplingPortFifo.getShaper.__doc__).strip() == shaper_note
        assert inspect.cleandoc(CouplingPortFifo.setShaper.__doc__).strip() == shaper_note + "\nA None value is a no-op and does not overwrite an existing shaper."

    def test_coupling_port_fifo_member_order_matches_spec(self):
        """Member order matches the Table 3.68 (p.124) displayed order."""
        source = inspect.getsource(CouplingPortFifo.__init__)
        indexes = [source.index("self.%s:" % member) for member in ("assignedTrafficClasses", "minimumFifoLength", "shaper")]
        assert indexes == sorted(indexes)

    def test_coupling_port_scheduler(self):
        """
        Test the CouplingPortScheduler class initialization and methods (Table 3.65, p.123).
        """
        parent = MockParent()
        scheduler = CouplingPortScheduler(parent, "TestScheduler")

        assert scheduler.getShortName() == "TestScheduler"
        assert scheduler.getPredecessorRefs() == []
        assert scheduler.getPortScheduler() is None

    def test_coupling_port_scheduler_docstring_is_spec_note(self):
        """Class docstring carries the spec Note verbatim (Table 3.65, p.123)."""
        assert CouplingPortScheduler.__doc__.strip() == "Defines a scheduler for the CouplingPort egress structure."

    def test_coupling_port_scheduler_init_has_no_docstring(self):
        assert CouplingPortScheduler.__init__.__doc__ is None

    def test_coupling_port_scheduler_get_set_port_scheduler(self):
        from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import EthernetCouplingPortSchedulerEnum

        scheduler = CouplingPortScheduler(MockParent(), "S1")
        value = EthernetCouplingPortSchedulerEnum()
        value.setValue("WEIGHTED-ROUND-ROBIN")
        assert scheduler.setPortScheduler(value) is scheduler
        assert scheduler.getPortScheduler() is value
        assert scheduler.getPortScheduler().getValue() == "WEIGHTED-ROUND-ROBIN"

    def test_coupling_port_scheduler_set_port_scheduler_none_no_op(self):
        from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import EthernetCouplingPortSchedulerEnum

        scheduler = CouplingPortScheduler(MockParent(), "S1")
        value = EthernetCouplingPortSchedulerEnum()
        value.setValue("STRICT-PRIORITY")
        scheduler.setPortScheduler(value)
        scheduler.setPortScheduler(None)
        assert scheduler.getPortScheduler().getValue() == "STRICT-PRIORITY"

    def test_coupling_port_scheduler_add_predecessor_refs(self):
        scheduler = CouplingPortScheduler(MockParent(), "S1")
        ref1 = RefType()
        ref1.setDest("COUPLING-PORT-FIFO")
        ref1.setValue("/Fifos/Fifo1")
        ref2 = RefType()
        ref2.setDest("COUPLING-PORT-SCHEDULER")
        ref2.setValue("/Schedulers/Sched1")

        result = scheduler.addPredecessorRef(ref1)
        assert result is scheduler
        scheduler.addPredecessorRef(ref2)

        refs = scheduler.getPredecessorRefs()
        assert len(refs) == 2
        assert refs[0].getValue() == "/Fifos/Fifo1"
        assert refs[0].getDest() == "COUPLING-PORT-FIFO"
        assert refs[1].getValue() == "/Schedulers/Sched1"

    def test_coupling_port_scheduler_add_predecessor_ref_none_no_op(self):
        scheduler = CouplingPortScheduler(MockParent(), "S1")
        ref1 = RefType()
        ref1.setValue("/Fifos/Fifo1")
        scheduler.addPredecessorRef(ref1)
        scheduler.addPredecessorRef(None)
        assert len(scheduler.getPredecessorRefs()) == 1

    def test_ethernet_priority_regeneration(self):
        """
        Test the EthernetPriorityRegeneration class initialization and methods.
        """
        parent = MockParent()
        regeneration = EthernetPriorityRegeneration(parent, "TestRegeneration")

        assert regeneration.getShortName() == "TestRegeneration"
        assert regeneration.getIngressPriority() is None
        assert regeneration.getRegeneratedPriority() is None

        # Test setting priorities with method chaining
        result = regeneration.setIngressPriority(3)
        assert regeneration.getIngressPriority() == 3
        assert result == regeneration  # Test method chaining

        result = regeneration.setRegeneratedPriority(7)
        assert regeneration.getRegeneratedPriority() == 7
        assert result == regeneration  # Test method chaining

    def test_coupling_port_details(self):
        """
        Test the CouplingPortDetails class initialization and methods (Table 3.63).
        """
        details = CouplingPortDetails()

        assert details.getCouplingPortStructuralElements() == []
        assert details.getEthernetPriorityRegenerations() == []
        assert details.getEthernetTrafficClassAssignments() == []
        assert details.getGlobalTimeProps() is None
        assert details.getLastEgressSchedulerRef() is None

        # Test creating coupling port fifo with method chaining
        fifo = details.createCouplingPortFifo("TestFifo")
        assert fifo.getShortName() == "TestFifo"
        assert fifo in details.getCouplingPortStructuralElements()

        # Test creating coupling port scheduler with method chaining
        scheduler = details.createCouplingPortScheduler("TestScheduler")
        assert scheduler.getShortName() == "TestScheduler"
        assert scheduler in details.getCouplingPortStructuralElements()

        # Test creating ethernet priority regeneration with method chaining
        regeneration = details.createEthernetPriorityRegeneration("TestRegeneration")
        assert regeneration.getShortName() == "TestRegeneration"
        assert regeneration in details.getEthernetPriorityRegenerations()

        # Test adding ethernet traffic class assignment with method chaining
        assignment = CouplingPortTrafficClassAssignment(details, "TestAssignment")
        result = details.addEthernetTrafficClassAssignment(assignment)
        assert details.getEthernetTrafficClassAssignments() == [assignment]
        assert result == details  # Test method chaining

        result = details.addEthernetTrafficClassAssignment(None)
        assert details.getEthernetTrafficClassAssignments() == [assignment]

        # Test global time props with method chaining
        time_props = MockParent()
        result = details.setGlobalTimeProps(time_props)
        assert details.getGlobalTimeProps() is time_props
        assert result == details  # Test method chaining

        # None no-op for globalTimeProps
        result = details.setGlobalTimeProps(None)
        assert details.getGlobalTimeProps() is time_props

        # Test last egress scheduler ref with method chaining
        ref = RefType()
        result = details.setLastEgressSchedulerRef(ref)
        assert details.getLastEgressSchedulerRef() is ref
        assert result == details  # Test method chaining

        # Test creating coupling port fifo with method chaining
        fifo = details.createCouplingPortFifo("TestFifo")
        assert fifo.getShortName() == "TestFifo"
        assert fifo in details.getCouplingPortStructuralElements()

        # Test creating coupling port scheduler with method chaining
        scheduler = details.createCouplingPortScheduler("TestScheduler")
        assert scheduler.getShortName() == "TestScheduler"
        assert scheduler in details.getCouplingPortStructuralElements()

        # Test creating ethernet priority regeneration with method chaining
        regen = details.createEthernetPriorityRegeneration("TestRegen")
        assert regen.getShortName() == "TestRegen"
        assert regen in details.getEthernetPriorityRegenerations()

    def test_vlan_membership(self):
        """
        Test the VlanMembership class initialization and methods (Table 3.59, p.112).
        """
        membership = VlanMembership()

        assert membership.getDefaultPriority() is None
        assert membership.getDhcpAddressAssignment() is None
        assert membership.getSendActivity() is None
        assert membership.getVlanRef() is None

    def test_vlan_membership_docstring_is_spec_note(self):
        """Class docstring carries the spec Note verbatim (Table 3.59, p.112)."""
        assert VlanMembership.__doc__.strip() == (
            "Static logical channel or VLAN binding to a switch-port. " "The reference to an EthernetPhysicalChannel without a VLAN defined represents the handling of untagged frames."
        )

    def test_vlan_membership_init_has_no_docstring(self):
        assert VlanMembership.__init__.__doc__ is None

    def test_vlan_membership_get_set_default_priority(self):
        membership = VlanMembership()
        priority = PositiveInteger()
        priority.setValue(5)
        assert membership.setDefaultPriority(priority) is membership
        assert membership.getDefaultPriority() is priority
        assert membership.getDefaultPriority().getValue() == 5
        membership.setDefaultPriority(None)
        assert membership.getDefaultPriority() is priority

    def test_vlan_membership_get_set_send_activity(self):
        from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import EthernetSwitchVlanEgressTaggingEnum

        membership = VlanMembership()
        value = EthernetSwitchVlanEgressTaggingEnum()
        value.setValue("SENT-TAGGED")
        assert membership.setSendActivity(value) is membership
        assert membership.getSendActivity() is value
        membership.setSendActivity(None)
        assert membership.getSendActivity() is value

    def test_vlan_membership_get_set_vlan_ref(self):
        membership = VlanMembership()
        ref = RefType()
        ref.setDest("ETHERNET-PHYSICAL-CHANNEL")
        ref.setValue("/Clusters/Ch1")
        assert membership.setVlanRef(ref) is membership
        assert membership.getVlanRef() is ref
        assert membership.getVlanRef().getDest() == "ETHERNET-PHYSICAL-CHANNEL"
        membership.setVlanRef(None)
        assert membership.getVlanRef() is ref

    def test_vlan_membership_get_set_dhcp_address_assignment(self):
        membership = VlanMembership()
        config = DhcpServerConfiguration()
        assert membership.setDhcpAddressAssignment(config) is membership
        assert membership.getDhcpAddressAssignment() is config
        membership.setDhcpAddressAssignment(None)
        assert membership.getDhcpAddressAssignment() is config

    def test_ethernet_switch_vlan_egress_tagging_enum(self):
        """EthernetSwitchVlanEgressTaggingEnum members, wire values and docstring (Table 3.78, p.130, R23-11)."""
        from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import EthernetSwitchVlanEgressTaggingEnum

        assert EthernetSwitchVlanEgressTaggingEnum.NOT_SENT == "NOT-SENT"
        assert EthernetSwitchVlanEgressTaggingEnum.SENT_TAGGED == "SENT-TAGGED"
        assert EthernetSwitchVlanEgressTaggingEnum.SENT_UNTAGGED == "SENT-UNTAGGED"
        assert list(EthernetSwitchVlanEgressTaggingEnum().getEnumValues()) == ["NOT-SENT", "SENT-TAGGED", "SENT-UNTAGGED"]

        not_sent = EthernetSwitchVlanEgressTaggingEnum().setValue(EthernetSwitchVlanEgressTaggingEnum.NOT_SENT)
        assert not_sent.getValue() == EthernetSwitchVlanEgressTaggingEnum.NOT_SENT

        sent_tagged = EthernetSwitchVlanEgressTaggingEnum().setValue(EthernetSwitchVlanEgressTaggingEnum.SENT_TAGGED)
        assert sent_tagged.getValue() == EthernetSwitchVlanEgressTaggingEnum.SENT_TAGGED

        sent_untagged = EthernetSwitchVlanEgressTaggingEnum().setValue(EthernetSwitchVlanEgressTaggingEnum.SENT_UNTAGGED)
        assert sent_untagged.getValue() == EthernetSwitchVlanEgressTaggingEnum.SENT_UNTAGGED

        assert inspect.cleandoc(EthernetSwitchVlanEgressTaggingEnum.__doc__) == "Defines the VLAN tag sending behavior."

    def test_coupling_port(self):
        """
        Test the CouplingPort class initialization and methods (Table 3.54).
        """
        parent = MockParent()
        port = CouplingPort(parent, "TestPort")

        assert port.getShortName() == "TestPort"
        assert port.getConnectionNegotiationBehavior() is None
        assert port.getCouplingPortDetails() is None
        assert port.getCouplingPortRole() is None
        assert port.getDefaultVlanRef() is None
        assert port.getMacLayerType() is None
        assert port.getMacMulticastAddressRefs() == []
        assert port.getMacSecProps() == []
        assert port.getPhysicalLayerType() is None
        assert port.getPlcaProps() is None
        assert port.getPncMappingRefs() == []
        assert port.getReceiveActivity() is None
        assert port.getVlanMemberships() == []
        assert port.getVlanModifierRef() is None
        assert port.getWakeupSleepOnDatalineConfigRef() is None

        # Test setting values with method chaining
        result = port.setConnectionNegotiationBehavior("Auto")
        assert port.getConnectionNegotiationBehavior() == "Auto"
        assert result == port  # Test method chaining

        result = port.setCouplingPortRole("Master")
        assert port.getCouplingPortRole() == "Master"
        assert result == port  # Test method chaining

        details = CouplingPortDetails()
        result = port.setCouplingPortDetails(details)
        assert port.getCouplingPortDetails() is details
        assert result == port  # Test method chaining

        # None no-op for couplingPortDetails
        result = port.setCouplingPortDetails(None)
        assert port.getCouplingPortDetails() is details

        vlan_ref = RefType()
        result = port.setDefaultVlanRef(vlan_ref)
        assert port.getDefaultVlanRef() is vlan_ref
        assert result == port  # Test method chaining

        result = port.setMacLayerType("type")
        assert port.getMacLayerType() == "type"
        assert result == port  # Test method chaining

        result = port.setPhysicalLayerType("phy_type")
        assert port.getPhysicalLayerType() == "phy_type"
        assert result == port  # Test method chaining

        plca_props = MockParent()
        result = port.setPlcaProps(plca_props)
        assert port.getPlcaProps() is plca_props
        assert result == port  # Test method chaining

        result = port.setWakeupSleepOnDatalineConfigRef("wakeup_ref")
        assert port.getWakeupSleepOnDatalineConfigRef() == "wakeup_ref"
        assert result == port  # Test method chaining

        result = port.setReceiveActivity("activity")
        assert port.getReceiveActivity() == "activity"
        assert result == port  # Test method chaining

        modifier_ref = RefType()
        result = port.setVlanModifierRef(modifier_ref)
        assert port.getVlanModifierRef() is modifier_ref
        assert result == port  # Test method chaining

        # None no-op for vlanModifierRef
        result = port.setVlanModifierRef(None)
        assert port.getVlanModifierRef() is modifier_ref

        # Test adding MAC multicast address refs with method chaining and None no-op
        ref1 = RefType()
        result = port.addMacMulticastAddressRef(ref1)
        assert port.getMacMulticastAddressRefs() == [ref1]
        assert result == port  # Test method chaining

        port.addMacMulticastAddressRef(None)
        assert port.getMacMulticastAddressRefs() == [ref1]

        # Test adding MAC sec props with method chaining
        mac_sec = MockParent()
        result = port.addMacSecProps(mac_sec)
        assert port.getMacSecProps() == [mac_sec]
        assert result == port  # Test method chaining

        # Test adding PNC mapping refs with method chaining
        pnc_ref = RefType()
        result = port.addPncMappingRef(pnc_ref)
        assert port.getPncMappingRefs() == [pnc_ref]
        assert result == port  # Test method chaining

        # Test adding VLAN membership with method chaining
        membership = VlanMembership()
        result = port.addVlanMembership(membership)
        assert port.getVlanMemberships() == [membership]
        assert result == port  # Test method chaining

    def test_ethernet_communication_controller(self):
        """
        Test the EthernetCommunicationController class initialization and methods.
        """
        parent = MockParent()
        controller = EthernetCommunicationController(parent, "TestController")

        assert controller.getShortName() == "TestController"
        assert controller.getCanXlConfigRef() is None
        assert controller.getCouplingPorts() == []
        assert controller.getMacLayerType() is None
        assert controller.getMacUnicastAddress() is None
        assert controller.getMaximumReceiveBufferLength() is None
        assert controller.getMaximumTransmitBufferLength() is None
        assert controller.getSlaveActAsPassiveCommunicationSlave() is None
        assert controller.getSlaveQualifiedUnexpectedLinkDownTime() is None

        # Test setting values with method chaining
        result = controller.setCanXlConfigRef("CanXlConfigRef")
        assert controller.getCanXlConfigRef() == "CanXlConfigRef"
        assert result == controller  # Test method chaining

        result = controller.setMacLayerType("TypeA")
        assert controller.getMacLayerType() == "TypeA"
        assert result == controller  # Test method chaining

        result = controller.setMacUnicastAddress("unicast_addr")
        assert controller.getMacUnicastAddress() == "unicast_addr"
        assert result == controller  # Test method chaining

        result = controller.setMaximumReceiveBufferLength(2048)
        assert controller.getMaximumReceiveBufferLength() == 2048
        assert result == controller  # Test method chaining

        result = controller.setMaximumTransmitBufferLength(2048)
        assert controller.getMaximumTransmitBufferLength() == 2048
        assert result == controller  # Test method chaining

        result = controller.setSlaveActAsPassiveCommunicationSlave(True)
        assert controller.getSlaveActAsPassiveCommunicationSlave() is True
        assert result == controller  # Test method chaining

        result = controller.setSlaveQualifiedUnexpectedLinkDownTime("time_val")
        assert controller.getSlaveQualifiedUnexpectedLinkDownTime() == "time_val"
        assert result == controller  # Test method chaining

        # Test creating coupling port
        coupling_port = controller.createCouplingPort("TestCouplingPort")
        assert coupling_port.getShortName() == "TestCouplingPort"

    def test_ethernet_communication_connector(self):
        """
        Test the EthernetCommunicationConnector class initialization and methods (Table 3.62).
        """
        parent = MockParent()
        connector = EthernetCommunicationConnector(parent, "TestConnector")

        assert connector.getShortName() == "TestConnector"
        assert connector.getEthIpPropsRef() is None
        assert connector.getMaximumTransmissionUnit() is None
        assert connector.getNeighborCacheSize() is None
        assert connector.getPathMtuEnabled() is None
        assert connector.getPathMtuTimeout() is None

        # Test setting values with method chaining and None no-ops
        result = connector.setEthIpPropsRef("EthIpPropsRef")
        assert connector.getEthIpPropsRef() == "EthIpPropsRef"
        assert result == connector  # Test method chaining

        # None no-op for ethIpPropsRef
        result = connector.setEthIpPropsRef(None)
        assert connector.getEthIpPropsRef() == "EthIpPropsRef"

        result = connector.setMaximumTransmissionUnit(1500)
        assert connector.getMaximumTransmissionUnit() == 1500
        assert result == connector  # Test method chaining

        result = connector.setNeighborCacheSize(100)
        assert connector.getNeighborCacheSize() == 100
        assert result == connector  # Test method chaining

        result = connector.setPathMtuEnabled(True)
        assert connector.getPathMtuEnabled() is True
        assert result == connector  # Test method chaining

        # None no-op for pathMtuEnabled
        result = connector.setPathMtuEnabled(None)
        assert connector.getPathMtuEnabled() is True

        result = connector.setPathMtuTimeout("timeout_val")
        assert connector.getPathMtuTimeout() == "timeout_val"
        assert result == connector  # Test method chaining

    def test_ethernet_communication_connector_removed_members(self):
        """
        networkEndpointRefs is atp.Status=removed since 4.3.1 and absent from Table 3.62 (Rule 0015);
        apApplicationEndpoint/canXlPropsRefs/ipV6PathMtu*/pncFilterDataMask are not in the R23-11 table.
        """
        connector = EthernetCommunicationConnector(MockParent(), "TestConnector")
        assert not hasattr(connector, "networkEndpointRefs")

    def test_request_response_delay(self):
        """
        Test the RequestResponseDelay class initialization and methods.
        """
        delay = RequestResponseDelay()

        assert delay.getMaxValue() is None
        assert delay.getMinValue() is None

        # Test setting values with method chaining
        result = delay.setMaxValue(5000)
        assert delay.getMaxValue() == 5000
        assert result == delay  # Test method chaining

        result = delay.setMinValue(1000)
        assert delay.getMinValue() == 1000
        assert result == delay  # Test method chaining

    def test_initial_sd_delay_config(self):
        """
        Test the InitialSdDelayConfig class initialization and methods.
        """
        config = InitialSdDelayConfig()

        assert config.getInitialDelayMaxValue() is None
        assert config.getInitialDelayMinValue() is None
        assert config.getInitialRepetitionsBaseDelay() is None
        assert config.getInitialRepetitionsMax() is None

        # Test setting values with method chaining
        result = config.setInitialDelayMaxValue(2000)
        assert config.getInitialDelayMaxValue() == 2000
        assert result == config  # Test method chaining

        result = config.setInitialDelayMinValue(100)
        assert config.getInitialDelayMinValue() == 100
        assert result == config  # Test method chaining

        result = config.setInitialRepetitionsBaseDelay(500)
        assert config.getInitialRepetitionsBaseDelay() == 500
        assert result == config  # Test method chaining

        result = config.setInitialRepetitionsMax(3)
        assert config.getInitialRepetitionsMax() == 3
        assert result == config  # Test method chaining

    def test_dhcp_server_configuration(self):
        """
        Test the DhcpServerConfiguration class initialization and methods.
        """
        config = DhcpServerConfiguration()

        assert config.getIpv4DhcpServerConfiguration() is None
        assert config.getIpv6DhcpServerConfiguration() is None

        # Test setting IPv4 configuration with method chaining
        ipv4 = Ipv4DhcpServerConfiguration()
        result = config.setIpv4DhcpServerConfiguration(ipv4)
        assert config.getIpv4DhcpServerConfiguration() is ipv4
        assert result == config  # Test method chaining

        # Test None no-op for IPv4 configuration
        result = config.setIpv4DhcpServerConfiguration(None)
        assert config.getIpv4DhcpServerConfiguration() is ipv4

        # Test setting IPv6 configuration with method chaining
        ipv6 = Ipv6DhcpServerConfiguration()
        result = config.setIpv6DhcpServerConfiguration(ipv6)
        assert config.getIpv6DhcpServerConfiguration() is ipv6
        assert result == config  # Test method chaining

        # Test None no-op for IPv6 configuration
        result = config.setIpv6DhcpServerConfiguration(None)
        assert config.getIpv6DhcpServerConfiguration() is ipv6

    def test_ipv4_dhcp_server_configuration_initialization(self):
        """
        Test the Ipv4DhcpServerConfiguration class initialization (Table 3.80).
        """
        config = Ipv4DhcpServerConfiguration()

        assert isinstance(config, Describable)
        assert config.getAddressRangeLowerBound() is None
        assert config.getAddressRangeUpperBound() is None
        assert config.getDefaultGateway() is None
        assert config.getDefaultLeaseTime() is None
        assert config.getDnsServerAddresses() == []
        assert config.getNetworkMask() is None

    def test_ipv4_dhcp_server_configuration_get_set(self):
        """
        Test the Ipv4DhcpServerConfiguration getters/setters (Table 3.80).
        """
        config = Ipv4DhcpServerConfiguration()

        result = config.setAddressRangeLowerBound("192.168.0.100")
        assert config.getAddressRangeLowerBound() == "192.168.0.100"
        assert result == config  # Test method chaining

        # Test None no-op for addressRangeLowerBound
        result = config.setAddressRangeLowerBound(None)
        assert config.getAddressRangeLowerBound() == "192.168.0.100"

        result = config.setAddressRangeUpperBound("192.168.0.200")
        assert config.getAddressRangeUpperBound() == "192.168.0.200"
        assert result == config  # Test method chaining

        # Test None no-op for addressRangeUpperBound
        result = config.setAddressRangeUpperBound(None)
        assert config.getAddressRangeUpperBound() == "192.168.0.200"

        result = config.setDefaultGateway("192.168.0.1")
        assert config.getDefaultGateway() == "192.168.0.1"
        assert result == config  # Test method chaining

        # Test None no-op for defaultGateway
        result = config.setDefaultGateway(None)
        assert config.getDefaultGateway() == "192.168.0.1"

        lease_time = TimeValue().setValue("3600")
        result = config.setDefaultLeaseTime(lease_time)
        assert config.getDefaultLeaseTime() == lease_time
        assert result == config  # Test method chaining

        # Test None no-op for defaultLeaseTime
        result = config.setDefaultLeaseTime(None)
        assert config.getDefaultLeaseTime() == lease_time

        result = config.setNetworkMask("255.255.255.0")
        assert config.getNetworkMask() == "255.255.255.0"
        assert result == config  # Test method chaining

        # Test None no-op for networkMask
        result = config.setNetworkMask(None)
        assert config.getNetworkMask() == "255.255.255.0"

    def test_ipv4_dhcp_server_configuration_dns_server_addresses(self):
        """
        Test the Ipv4DhcpServerConfiguration dnsServerAddresses list (Table 3.80).
        """
        config = Ipv4DhcpServerConfiguration()

        assert config.getDnsServerAddresses() == []

        result = config.addDnsServerAddress("8.8.8.8")
        assert config.getDnsServerAddresses() == ["8.8.8.8"]
        assert result == config  # Test method chaining

        config.addDnsServerAddress("8.8.4.4")
        assert config.getDnsServerAddresses() == ["8.8.8.8", "8.8.4.4"]

        # Test None no-op for dnsServerAddresses
        config.addDnsServerAddress(None)
        assert config.getDnsServerAddresses() == ["8.8.8.8", "8.8.4.4"]

    def test_ipv6_dhcp_server_configuration_initialization(self):
        """
        Test the Ipv6DhcpServerConfiguration class initialization (Table 3.81).
        """
        config = Ipv6DhcpServerConfiguration()

        assert isinstance(config, Describable)
        assert config.getAddressRangeLowerBound() is None
        assert config.getAddressRangeUpperBound() is None
        assert config.getDefaultGateway() is None
        assert config.getDefaultLeaseTime() is None
        assert config.getDnsServerAddresses() == []
        assert config.getNetworkMask() is None

    def test_ipv6_dhcp_server_configuration_get_set(self):
        """
        Test the Ipv6DhcpServerConfiguration getters/setters (Table 3.81).
        """
        config = Ipv6DhcpServerConfiguration()

        result = config.setAddressRangeLowerBound("fe80::1")
        assert config.getAddressRangeLowerBound() == "fe80::1"
        assert result == config  # Test method chaining

        # Test None no-op for addressRangeLowerBound
        result = config.setAddressRangeLowerBound(None)
        assert config.getAddressRangeLowerBound() == "fe80::1"

        result = config.setAddressRangeUpperBound("fe80::2")
        assert config.getAddressRangeUpperBound() == "fe80::2"
        assert result == config  # Test method chaining

        # Test None no-op for addressRangeUpperBound
        result = config.setAddressRangeUpperBound(None)
        assert config.getAddressRangeUpperBound() == "fe80::2"

        result = config.setDefaultGateway("fe80::ffff")
        assert config.getDefaultGateway() == "fe80::ffff"
        assert result == config  # Test method chaining

        # Test None no-op for defaultGateway
        result = config.setDefaultGateway(None)
        assert config.getDefaultGateway() == "fe80::ffff"

        lease_time = TimeValue().setValue("3600")
        result = config.setDefaultLeaseTime(lease_time)
        assert config.getDefaultLeaseTime() == lease_time
        assert result == config  # Test method chaining

        # Test None no-op for defaultLeaseTime
        result = config.setDefaultLeaseTime(None)
        assert config.getDefaultLeaseTime() == lease_time

        result = config.setNetworkMask("ffff:ffff:ffff:ffff::")
        assert config.getNetworkMask() == "ffff:ffff:ffff:ffff::"
        assert result == config  # Test method chaining

        # Test None no-op for networkMask
        result = config.setNetworkMask(None)
        assert config.getNetworkMask() == "ffff:ffff:ffff:ffff::"

    def test_ipv6_dhcp_server_configuration_dns_server_addresses(self):
        """
        Test the Ipv6DhcpServerConfiguration dnsServerAddresses list (Table 3.81).
        """
        config = Ipv6DhcpServerConfiguration()

        assert config.getDnsServerAddresses() == []

        result = config.addDnsServerAddress("2001:db8::53")
        assert config.getDnsServerAddresses() == ["2001:db8::53"]
        assert result == config  # Test method chaining

        config.addDnsServerAddress("2001:db8::54")
        assert config.getDnsServerAddresses() == ["2001:db8::53", "2001:db8::54"]

        # Test None no-op for dnsServerAddresses
        config.addDnsServerAddress(None)
        assert config.getDnsServerAddresses() == ["2001:db8::53", "2001:db8::54"]

    def test_coupling_port_traffic_class_assignment(self):
        """
        Test the CouplingPortTrafficClassAssignment class initialization and methods.
        """
        parent = MockParent()
        assignment = CouplingPortTrafficClassAssignment(parent, "TestAssignment")

        assert assignment.getShortName() == "TestAssignment"
        assert assignment.getPriorities() == []
        assert assignment.getTrafficClass() is None

        # Test setting traffic class with method chaining
        tc = PositiveInteger()
        tc.setValue("3")
        result = assignment.setTrafficClass(tc)
        assert assignment.getTrafficClass() is tc
        assert result == assignment

        # Test None no-op for traffic class
        result = assignment.setTrafficClass(None)
        assert assignment.getTrafficClass() is tc

        # Test adding priorities with method chaining
        p1 = PositiveInteger()
        p1.setValue("1")
        p2 = PositiveInteger()
        p2.setValue("2")
        result = assignment.addPriority(p1)
        assert assignment.getPriorities() == [p1]
        assert result == assignment

        assignment.addPriority(p2)
        assert assignment.getPriorities() == [p1, p2]

        # Test None no-op for priorities
        assignment.addPriority(None)
        assert assignment.getPriorities() == [p1, p2]

    def test_sd_client_config(self):
        """
        Test the SdClientConfig class initialization and methods
        (R4.3.1 AUTOSAR_TPS_SystemTemplate, Table 6.172, p.356).
        """
        config = SdClientConfig()

        assert isinstance(config, ARObject)
        assert config.getCapabilityRecords() == []
        assert config.getClientServiceMajorVersion() is None
        assert config.getClientServiceMinorVersion() is None
        assert config.getInitialFindBehavior() is None
        assert config.getRequestResponseDelay() is None
        assert config.getTtl() is None

        # Test capability records with method chaining and None no-op
        record = TagWithOptionalValue()
        result = config.addCapabilityRecord(record)
        assert config.getCapabilityRecords() == [record]
        assert result == config  # Test method chaining

        config.addCapabilityRecord(None)
        assert config.getCapabilityRecords() == [record]

        # Test setting values with method chaining
        result = config.setClientServiceMajorVersion(1)
        assert config.getClientServiceMajorVersion() == 1
        assert result == config  # Test method chaining

        result = config.setClientServiceMinorVersion(2)
        assert config.getClientServiceMinorVersion() == 2
        assert result == config  # Test method chaining

        result = config.setTtl(5000)
        assert config.getTtl() == 5000
        assert result == config  # Test method chaining

        initial_config = InitialSdDelayConfig()
        result = config.setInitialFindBehavior(initial_config)
        assert config.getInitialFindBehavior() == initial_config
        assert result == config  # Test method chaining

        delay = RequestResponseDelay()
        result = config.setRequestResponseDelay(delay)
        assert config.getRequestResponseDelay() == delay
        assert result == config  # Test method chaining


class TestSdClientConfigSpecSync:
    """Spec-sync checks for SdClientConfig (R4.3.1 AUTOSAR_TPS_SystemTemplate, Table 6.172, p.356)."""

    def test_docstring_is_spec_note_verbatim(self):
        assert SdClientConfig.__doc__.strip() == "Client configuration for Service-Discovery."

    def test_init_has_no_docstring(self):
        assert SdClientConfig.__init__.__doc__ is None

    def test_defaults_in_spec_displayed_order(self):
        config = SdClientConfig()
        assert config.getCapabilityRecords() == []
        assert config.getClientServiceMajorVersion() is None
        assert config.getClientServiceMinorVersion() is None
        assert config.getInitialFindBehavior() is None
        assert config.getRequestResponseDelay() is None
        assert config.getTtl() is None
        assert list(config.__dict__.keys())[-6:] == ["capabilityRecords", "clientServiceMajorVersion", "clientServiceMinorVersion", "initialFindBehavior", "requestResponseDelay", "ttl"]

    def test_get_set_round_trip_same_instance_and_none_noop(self):
        config = SdClientConfig()
        major = PositiveInteger()
        major.setValue(15)
        minor = PositiveInteger()
        minor.setValue(3)
        ttl = PositiveInteger()
        ttl.setValue(255)
        initial = InitialSdDelayConfig()
        delay = RequestResponseDelay()
        assert config.setClientServiceMajorVersion(major) is config
        assert config.setClientServiceMinorVersion(minor) is config
        assert config.setInitialFindBehavior(initial) is config
        assert config.setRequestResponseDelay(delay) is config
        assert config.setTtl(ttl) is config
        assert config.getClientServiceMajorVersion() is major
        assert config.getClientServiceMinorVersion() is minor
        assert config.getInitialFindBehavior() is initial
        assert config.getRequestResponseDelay() is delay
        assert config.getTtl() is ttl
        config.setClientServiceMajorVersion(None)
        config.setClientServiceMinorVersion(None)
        config.setInitialFindBehavior(None)
        config.setRequestResponseDelay(None)
        config.setTtl(None)
        config.addCapabilityRecord(None)
        assert config.getClientServiceMajorVersion() is major
        assert config.getClientServiceMinorVersion() is minor
        assert config.getInitialFindBehavior() is initial
        assert config.getRequestResponseDelay() is delay
        assert config.getTtl() is ttl
        assert config.getCapabilityRecords() == []

    def test_capability_record_adder(self):
        config = SdClientConfig()
        record = TagWithOptionalValue()
        assert config.addCapabilityRecord(record) is config
        assert config.getCapabilityRecords() == [record]

    def test_accessor_docstrings_verbatim(self):
        note = (
            "A sequence of records to store arbitrary name/value pairs conveying additional information about the named service. "
            "Capability records shall only be existing if the respective SdClientConfig is composed by a ConsumedServiceInstance (see constr_3260)."
        )
        assert SdClientConfig.getCapabilityRecords.__doc__.strip() == note
        assert SdClientConfig.getClientServiceMajorVersion.__doc__.strip() == "Major version number of the Service."
        assert SdClientConfig.getClientServiceMinorVersion.__doc__.strip() == "Minor version number of the Service."
        assert SdClientConfig.getInitialFindBehavior.__doc__.strip() == "Controls initial find behavior of clients."
        assert SdClientConfig.getRequestResponseDelay.__doc__.strip() == "Maximum/Minimum allowable response delay to entries received by multicast in seconds."
        assert SdClientConfig.getTtl.__doc__.strip() == "TTL for Request and Subscribe messages."


class TestEthernetConnectionNegotiationEnum:
    """Test cases for EthernetConnectionNegotiationEnum (CP_TPS_SystemTemplate Table 3.55, p.110, R23-11)."""

    def test_member_presence_and_values(self):
        assert EthernetConnectionNegotiationEnum.AUTO == "AUTO"
        assert EthernetConnectionNegotiationEnum.MASTER == "MASTER"
        assert EthernetConnectionNegotiationEnum.SLAVE == "SLAVE"
        assert list(EthernetConnectionNegotiationEnum().getEnumValues()) == ["AUTO", "MASTER", "SLAVE"]

    def test_instantiability_round_trip(self):
        auto = EthernetConnectionNegotiationEnum().setValue(EthernetConnectionNegotiationEnum.AUTO)
        assert auto.getValue() == EthernetConnectionNegotiationEnum.AUTO

        master = EthernetConnectionNegotiationEnum().setValue(EthernetConnectionNegotiationEnum.MASTER)
        assert master.getValue() == EthernetConnectionNegotiationEnum.MASTER

        slave = EthernetConnectionNegotiationEnum().setValue(EthernetConnectionNegotiationEnum.SLAVE)
        assert slave.getValue() == EthernetConnectionNegotiationEnum.SLAVE

    def test_class_docstring_note(self):
        assert inspect.cleandoc(EthernetConnectionNegotiationEnum.__doc__) == "Specifies connection negotiation types of Ethernet transceiver links."


class TestCouplingPortRoleEnum:
    """Test cases for CouplingPortRoleEnum (Table F.38)."""

    def test_enum_values(self):
        assert list(CouplingPortRoleEnum().getEnumValues()) == ["HOST-PORT", "STANDARD-PORT", "UP-LINK-PORT"]
        assert CouplingPortRoleEnum.HOST_PORT == "HOST-PORT"
        assert CouplingPortRoleEnum.UP_LINK_PORT == "UP-LINK-PORT"
        assert CouplingPortRoleEnum.STANDARD_PORT == "STANDARD-PORT"


class TestEthernetMacLayerTypeEnum:
    """Test cases for EthernetMacLayerTypeEnum (CP_TPS_SystemTemplate Table 3.56, p.110, R23-11)."""

    def test_member_presence_and_values(self):
        assert EthernetMacLayerTypeEnum.XMII == "X-MII"
        assert EthernetMacLayerTypeEnum.XGMII == "XG-MII"
        assert EthernetMacLayerTypeEnum.XXGMII == "XXG-MII"
        assert list(EthernetMacLayerTypeEnum().getEnumValues()) == ["X-MII", "XG-MII", "XXG-MII"]

    def test_instantiability_round_trip(self):
        xmii = EthernetMacLayerTypeEnum().setValue(EthernetMacLayerTypeEnum.XMII)
        assert xmii.getValue() == EthernetMacLayerTypeEnum.XMII

        xgmii = EthernetMacLayerTypeEnum().setValue(EthernetMacLayerTypeEnum.XGMII)
        assert xgmii.getValue() == EthernetMacLayerTypeEnum.XGMII

        xxgmii = EthernetMacLayerTypeEnum().setValue(EthernetMacLayerTypeEnum.XXGMII)
        assert xxgmii.getValue() == EthernetMacLayerTypeEnum.XXGMII

    def test_class_docstring_note(self):
        assert inspect.cleandoc(EthernetMacLayerTypeEnum.__doc__) == "Specifies MAC (Media Access Control) Layer types."


class TestEthernetCouplingPortSchedulerEnum:
    """Test cases for EthernetCouplingPortSchedulerEnum (CP_TPS_SystemTemplate Table 3.66, p.123, R23-11)."""

    def test_member_presence_and_values(self):
        assert EthernetCouplingPortSchedulerEnum.DEFICIT_ROUND_ROBIN == "DEFICIT-ROUND-ROBIN"
        assert EthernetCouplingPortSchedulerEnum.STRICT_PRIORITY == "STRICT-PRIORITY"
        assert EthernetCouplingPortSchedulerEnum.WEIGHTED_ROUND_ROBIN == "WEIGHTED-ROUND-ROBIN"
        assert list(EthernetCouplingPortSchedulerEnum().getEnumValues()) == ["DEFICIT-ROUND-ROBIN", "STRICT-PRIORITY", "WEIGHTED-ROUND-ROBIN"]

    def test_instantiability_round_trip(self):
        deficit_round_robin = EthernetCouplingPortSchedulerEnum().setValue(EthernetCouplingPortSchedulerEnum.DEFICIT_ROUND_ROBIN)
        assert deficit_round_robin.getValue() == EthernetCouplingPortSchedulerEnum.DEFICIT_ROUND_ROBIN

        strict_priority = EthernetCouplingPortSchedulerEnum().setValue(EthernetCouplingPortSchedulerEnum.STRICT_PRIORITY)
        assert strict_priority.getValue() == EthernetCouplingPortSchedulerEnum.STRICT_PRIORITY

        weighted_round_robin = EthernetCouplingPortSchedulerEnum().setValue(EthernetCouplingPortSchedulerEnum.WEIGHTED_ROUND_ROBIN)
        assert weighted_round_robin.getValue() == EthernetCouplingPortSchedulerEnum.WEIGHTED_ROUND_ROBIN

    def test_class_docstring_note(self):
        assert inspect.cleandoc(EthernetCouplingPortSchedulerEnum.__doc__) == "Defines the schedule algorithm to be used."


class Test_Fibex4EthernetNetworkEndpoint:
    """Test cases for the NetworkEndpoint classes relocated to Fibex4Ethernet.EthernetTopology."""

    def test_NetworkEndpointAddress(self):
        """Test NetworkEndpointAddress abstract class instantiation (Table 6.135, p.464)."""
        with pytest.raises(TypeError):
            NetworkEndpointAddress()

    def test_NetworkEndpointAddress_docstring_is_spec_note(self):
        """Class docstring carries the spec Note verbatim (Table 6.135, p.464)."""
        assert (
            NetworkEndpointAddress.__doc__.strip()
            == "To build a valid network endpoint address there has to be either one MAC multicast group reference or an ipv4 configuration or an ipv6 configuration."
        )

    def test_NetworkEndpointAddress_init_has_no_docstring(self):
        assert NetworkEndpointAddress.__init__.__doc__ is None

    def test_NetworkEndpointAddress_subclasses(self):
        assert issubclass(Ipv4Configuration, NetworkEndpointAddress)
        assert issubclass(Ipv6Configuration, NetworkEndpointAddress)

    def test_Ipv4Configuration(self):
        """Test Ipv4Configuration class functionality."""
        config = Ipv4Configuration()

        assert isinstance(config, NetworkEndpointAddress)

        # Test default values
        assert config.getAssignmentPriority() is None
        assert config.getDefaultGateway() is None
        assert config.getDnsServerAddresses() == []
        assert config.getIpAddressKeepBehavior() is None
        assert config.getIpv4Address() is None
        assert config.getIpv4AddressSource() is None
        assert config.getNetworkMask() is None
        assert config.getTtl() is None

        # Test setter/getter methods with method chaining
        result = config.setAssignmentPriority(1)
        assert config.getAssignmentPriority() == 1
        assert result == config  # Test method chaining

        result = config.setDefaultGateway("192.168.1.254")
        assert config.getDefaultGateway() == "192.168.1.254"
        assert result == config  # Test method chaining

        result = config.setIpAddressKeepBehavior(IpAddressKeepEnum.STORE_PERSISTENTLY)
        assert config.getIpAddressKeepBehavior() == IpAddressKeepEnum.STORE_PERSISTENTLY
        assert result == config  # Test method chaining

        result = config.setIpv4Address("192.168.1.1")
        assert config.getIpv4Address() == "192.168.1.1"
        assert result == config  # Test method chaining

        result = config.setIpv4AddressSource("dhcp")
        assert config.getIpv4AddressSource() == "dhcp"
        assert result == config  # Test method chaining

        result = config.setNetworkMask("255.255.255.0")
        assert config.getNetworkMask() == "255.255.255.0"
        assert result == config  # Test method chaining

        result = config.setTtl(64)
        assert config.getTtl() == 64
        assert result == config  # Test method chaining

        # Test adding DNS server addresses with method chaining
        result = config.addDnsServerAddress("8.8.8.8")
        assert config.getDnsServerAddresses() == ["8.8.8.8"]
        assert result == config  # Test method chaining

        result = config.addDnsServerAddress("8.8.4.4")
        assert config.getDnsServerAddresses() == ["8.8.8.8", "8.8.4.4"]
        assert result == config  # Test method chaining

    def test_Ipv6Configuration(self):
        """Test Ipv6Configuration class functionality (Table 6.139, p.466)."""
        config = Ipv6Configuration()

        assert isinstance(config, NetworkEndpointAddress)

        # Test default values
        assert config.getAssignmentPriority() is None
        assert config.getDefaultRouter() is None
        assert config.getDnsServerAddresses() == []
        assert config.getEnableAnycast() is None
        assert config.getHopCount() is None
        assert config.getIpAddressKeepBehavior() is None
        assert config.getIpAddressPrefixLength() is None
        assert config.getIpv6Address() is None
        assert config.getIpv6AddressSource() is None

        # Test setter/getter methods with method chaining and None no-ops
        result = config.setAssignmentPriority(2)
        assert config.getAssignmentPriority() == 2
        assert result == config  # Test method chaining

        result = config.setDefaultRouter("2001:db8::1")
        assert config.getDefaultRouter() == "2001:db8::1"
        assert result == config  # Test method chaining

        result = config.setEnableAnycast(True)
        assert config.getEnableAnycast() is True
        assert result == config  # Test method chaining

        result = config.setHopCount(64)
        assert config.getHopCount() == 64
        assert result == config  # Test method chaining

        keep = IpAddressKeepEnum().setValue(IpAddressKeepEnum.STORE_PERSISTENTLY)
        result = config.setIpAddressKeepBehavior(keep)
        assert config.getIpAddressKeepBehavior() is keep
        assert config.getIpAddressKeepBehavior().getValue() == IpAddressKeepEnum.STORE_PERSISTENTLY
        assert isinstance(config.getIpAddressKeepBehavior(), IpAddressKeepEnum)
        assert result == config  # Test method chaining

        # None no-op for ipAddressKeepBehavior
        result = config.setIpAddressKeepBehavior(None)
        assert config.getIpAddressKeepBehavior().getValue() == IpAddressKeepEnum.STORE_PERSISTENTLY

        result = config.setIpAddressPrefixLength(64)
        assert config.getIpAddressPrefixLength() == 64
        assert result == config  # Test method chaining

        result = config.setIpv6Address("2001:db8::1")
        assert config.getIpv6Address() == "2001:db8::1"
        assert result == config  # Test method chaining

        source = Ipv6AddressSourceEnum().setValue(Ipv6AddressSourceEnum.LINK_LOCAL)
        result = config.setIpv6AddressSource(source)
        assert config.getIpv6AddressSource() is source
        assert config.getIpv6AddressSource().getValue() == Ipv6AddressSourceEnum.LINK_LOCAL
        assert isinstance(config.getIpv6AddressSource(), Ipv6AddressSourceEnum)
        assert result == config  # Test method chaining

        # Test adding DNS server addresses with method chaining and None no-op
        result = config.addDnsServerAddress("2001:4860:4860::8888")
        assert config.getDnsServerAddresses() == ["2001:4860:4860::8888"]
        assert result == config  # Test method chaining

        config.addDnsServerAddress("2001:4860:4860::8844")
        assert config.getDnsServerAddresses() == ["2001:4860:4860::8888", "2001:4860:4860::8844"]

        config.addDnsServerAddress(None)
        assert config.getDnsServerAddresses() == ["2001:4860:4860::8888", "2001:4860:4860::8844"]

    def test_DoIpEntity(self):
        """Test DoIpEntity class functionality."""
        entity = DoIpEntity()

        assert isinstance(entity, ARObject)

        # Test default values
        assert entity.getDoIpEntityRole() is None

        # Test setter/getter methods with method chaining
        result = entity.setDoIpEntityRole("tester")
        assert entity.getDoIpEntityRole() == "tester"
        assert result == entity  # Test method chaining

    def test_TimeSyncClientConfiguration(self):
        """Test TimeSyncClientConfiguration class functionality (Table 6.146, p.470)."""
        config = TimeSyncClientConfiguration()

        assert isinstance(config, ARObject)

        # Test default values
        assert config.getOrderedMasters() == []
        assert config.getTimeSyncTechnology() is None

    def test_TimeSyncClientConfiguration_docstring_is_spec_note(self):
        """Class docstring carries the spec Note verbatim (Table 6.146, p.470)."""
        assert TimeSyncClientConfiguration.__doc__.strip() == "Defines the configuration of the time synchronisation client."

    def test_TimeSyncClientConfiguration_init_has_no_docstring(self):
        assert TimeSyncClientConfiguration.__init__.__doc__ is None

    def test_TimeSyncClientConfiguration_set_time_sync_technology(self):
        from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import TimeSyncTechnologyEnum

        config = TimeSyncClientConfiguration()
        value = TimeSyncTechnologyEnum()
        value.setValue("IEEE_802.1AS")
        assert config.setTimeSyncTechnology(value) is config
        assert config.getTimeSyncTechnology() is value
        config.setTimeSyncTechnology(None)
        assert config.getTimeSyncTechnology() is value

    def test_TimeSyncClientConfiguration_add_ordered_masters(self):
        config = TimeSyncClientConfiguration()
        master1 = OrderedMaster()
        master1.setIndex(_pos_int("1"))
        master2 = OrderedMaster()
        master2.setIndex(_pos_int("2"))

        result = config.addOrderedMaster(master1)
        assert result is config
        config.addOrderedMaster(master2)

        masters = config.getOrderedMasters()
        assert masters == [master1, master2]

        config.addOrderedMaster(None)
        assert len(config.getOrderedMasters()) == 2

    def test_TimeSyncServerConfiguration(self):
        """Test TimeSyncServerConfiguration class functionality."""
        autosar = AUTOSAR.getInstance()
        ar_package = autosar.createARPackage("TEST")
        config = TimeSyncServerConfiguration(ar_package, "time_sync_config")

        assert isinstance(config, Referrable)

        # Test default values
        assert config.getShortName() == "time_sync_config"
        assert config.getPriority() is None
        assert config.getSyncInterval() is None
        assert config.getTimeSyncServerIdentifier() is None
        assert config.getTimeSyncTechnology() is None

        # Test setter/getter methods with method chaining
        result = config.setPriority(10)
        assert config.getPriority() == 10
        assert result == config  # Test method chaining

        result = config.setSyncInterval("100ms")
        assert config.getSyncInterval() == "100ms"
        assert result == config  # Test method chaining

        result = config.setTimeSyncServerIdentifier("server1")
        assert config.getTimeSyncServerIdentifier() == "server1"
        assert result == config  # Test method chaining

        result = config.setTimeSyncTechnology("IEEE_1588")
        assert config.getTimeSyncTechnology() == "IEEE_1588"
        assert result == config  # Test method chaining

    def test_TimeSynchronization(self):
        """Test TimeSynchronization class functionality."""
        sync = TimeSynchronization()

        assert isinstance(sync, ARObject)

        # Test default values
        assert sync.getTimeSyncClient() is None
        assert sync.getTimeSyncServer() is None

        # Test setter/getter methods with method chaining
        client_config = TimeSyncClientConfiguration()
        result = sync.setTimeSyncClient(client_config)
        assert sync.getTimeSyncClient() == client_config
        assert result == sync  # Test method chaining

        server_config = sync.createTimeSyncServer("time_sync_server")
        assert sync.getTimeSyncServer() == server_config
        assert server_config.getShortName() == "time_sync_server"
        assert server_config.getParent() == sync

    def test_InfrastructureServices(self):
        """Test InfrastructureServices class functionality (Table 6.144, p.469)."""
        services = InfrastructureServices()

        assert isinstance(services, ARObject)

        # Test default values
        assert services.getDoIpEntity() is None
        assert services.getTimeSynchronization() is None

        # dhcpServerConfiguration is atp.Status=removed since 4.3.1 and absent from Table 6.144 (Rule 0015)
        assert not hasattr(services, "dhcpServerConfiguration")

        # Test setter/getter methods with method chaining
        doip_entity = DoIpEntity()
        result = services.setDoIpEntity(doip_entity)
        assert services.getDoIpEntity() == doip_entity
        assert result == services  # Test method chaining

        time_sync = TimeSynchronization()
        result = services.setTimeSynchronization(time_sync)
        assert services.getTimeSynchronization() == time_sync
        assert result == services  # Test method chaining

    def test_NetworkEndpoint(self):
        """Test NetworkEndpoint class functionality."""
        parent = MockParent()
        endpoint = NetworkEndpoint(parent, "test_network_endpoint")

        assert isinstance(endpoint, Identifiable)

        # Test default values
        assert endpoint.getFullyQualifiedDomainName() is None
        assert endpoint.getInfrastructureServices() is None
        assert endpoint.getIpSecConfig() is None
        assert endpoint.getNetworkEndpointAddresses() == []
        assert endpoint.getPriority() is None

        # Test setter/getter methods with method chaining
        result = endpoint.setFullyQualifiedDomainName("example.com")
        assert endpoint.getFullyQualifiedDomainName() == "example.com"
        assert result == endpoint  # Test method chaining

        result = endpoint.setInfrastructureServices(InfrastructureServices())
        assert isinstance(endpoint.getInfrastructureServices(), InfrastructureServices)
        assert result == endpoint  # Test method chaining

        result = endpoint.setIpSecConfig("ipsec_config")
        assert endpoint.getIpSecConfig() == "ipsec_config"
        assert result == endpoint  # Test method chaining

        result = endpoint.setPriority(5)
        assert endpoint.getPriority() == 5
        assert result == endpoint  # Test method chaining

        # Test adding network endpoint addresses with method chaining
        ipv4_config = Ipv4Configuration()
        result = endpoint.addNetworkEndpointAddress(ipv4_config)
        assert endpoint.getNetworkEndpointAddresses() == [ipv4_config]
        assert result == endpoint  # Test method chaining


class TestEthernetPhysicalLayerTypeEnum:
    """Test cases for EthernetPhysicalLayerTypeEnum (Table 3.57, p.111, R23-11)."""

    def test_member_presence_and_values(self):
        assert EthernetPhysicalLayerTypeEnum._1000BASE_T == "1000BASE-T"
        assert EthernetPhysicalLayerTypeEnum._1000BASE_T1 == "1000BASE-T1"
        assert EthernetPhysicalLayerTypeEnum._100BASE_T1 == "100BASE-T1"
        assert EthernetPhysicalLayerTypeEnum._100BASE_TX == "100BASE-TX"
        assert EthernetPhysicalLayerTypeEnum._10BASE_T1S == "10BASE-T1S"
        assert EthernetPhysicalLayerTypeEnum.IEEE802_11P == "IEEE802-11P"
        assert list(EthernetPhysicalLayerTypeEnum().getEnumValues()) == [
            "1000BASE-T",
            "1000BASE-T1",
            "100BASE-T1",
            "100BASE-TX",
            "10BASE-T1S",
            "IEEE802-11P",
        ]

    def test_instantiability_round_trip(self):
        t1 = EthernetPhysicalLayerTypeEnum().setValue(EthernetPhysicalLayerTypeEnum._1000BASE_T)
        assert t1.getValue() == EthernetPhysicalLayerTypeEnum._1000BASE_T

        t1s = EthernetPhysicalLayerTypeEnum().setValue(EthernetPhysicalLayerTypeEnum._10BASE_T1S)
        assert t1s.getValue() == EthernetPhysicalLayerTypeEnum._10BASE_T1S

        ieee = EthernetPhysicalLayerTypeEnum().setValue(EthernetPhysicalLayerTypeEnum.IEEE802_11P)
        assert ieee.getValue() == EthernetPhysicalLayerTypeEnum.IEEE802_11P

    def test_class_docstring_note(self):
        assert inspect.cleandoc(EthernetPhysicalLayerTypeEnum.__doc__) == "Specifies physical layer types of Ethernet transceiver links."


class TestEthernetSwitchVlanIngressTagEnum:
    """Test cases for EthernetSwitchVlanIngressTagEnum (Table 3.58, p.111, R23-11)."""

    def test_member_presence_and_values(self):
        assert EthernetSwitchVlanIngressTagEnum.DROP_UNTAGGED == "DROP-UNTAGGED"
        assert EthernetSwitchVlanIngressTagEnum.FORWARD_AS_IS == "FORWARD-AS-IS"
        assert list(EthernetSwitchVlanIngressTagEnum().getEnumValues()) == [
            EthernetSwitchVlanIngressTagEnum.DROP_UNTAGGED,
            EthernetSwitchVlanIngressTagEnum.FORWARD_AS_IS,
        ]

    def test_instantiability_round_trip(self):
        drop = EthernetSwitchVlanIngressTagEnum().setValue(EthernetSwitchVlanIngressTagEnum.DROP_UNTAGGED)
        assert drop.getValue() == EthernetSwitchVlanIngressTagEnum.DROP_UNTAGGED

        forward = EthernetSwitchVlanIngressTagEnum().setValue(EthernetSwitchVlanIngressTagEnum.FORWARD_AS_IS)
        assert forward.getValue() == EthernetSwitchVlanIngressTagEnum.FORWARD_AS_IS

    def test_class_docstring_note(self):
        assert inspect.cleandoc(EthernetSwitchVlanIngressTagEnum.__doc__) == "Defines the possible tagging behavior at an ingress port."


class TestTimeSyncTechnologyEnum:
    """Test cases for TimeSyncTechnologyEnum (Table 6.149, p.471)."""

    def test_member_presence_and_values(self):
        assert TimeSyncTechnologyEnum.AVB_IEEE802_1AS == "AVB--IEEE-802--1-AS"
        assert TimeSyncTechnologyEnum.NTP_RFC958 == "NTP--RFC-958"
        assert TimeSyncTechnologyEnum.PTP_IEEE1588_2002 == "PTP--IEEE-1588--2002"
        assert TimeSyncTechnologyEnum.PTP_IEEE1588_2008 == "PTP--IEEE-1588--2008"
        assert list(TimeSyncTechnologyEnum().getEnumValues()) == [
            TimeSyncTechnologyEnum.AVB_IEEE802_1AS,
            TimeSyncTechnologyEnum.NTP_RFC958,
            TimeSyncTechnologyEnum.PTP_IEEE1588_2002,
            TimeSyncTechnologyEnum.PTP_IEEE1588_2008,
        ]

    def test_instantiability_round_trip(self):
        avb = TimeSyncTechnologyEnum().setValue(TimeSyncTechnologyEnum.AVB_IEEE802_1AS)
        assert avb.getValue() == TimeSyncTechnologyEnum.AVB_IEEE802_1AS

        ptp = TimeSyncTechnologyEnum().setValue(TimeSyncTechnologyEnum.PTP_IEEE1588_2008)
        assert ptp.getValue() == TimeSyncTechnologyEnum.PTP_IEEE1588_2008

    def test_class_docstring_note(self):
        assert inspect.cleandoc(TimeSyncTechnologyEnum.__doc__) == "Timesynchronization. Server/Client configuration."


class TestDoIpEntityRoleEnum:
    """Test cases for DoIpEntityRoleEnum (Table 6.151, p.471)."""

    def test_enum_values(self):
        assert list(DoIpEntityRoleEnum().getEnumValues()) == [
            DoIpEntityRoleEnum.EDGE_NODE,
            DoIpEntityRoleEnum.GATEWAY,
            DoIpEntityRoleEnum.NODE,
        ]
        assert DoIpEntityRoleEnum.EDGE_NODE == "EDGE-NODE"
        assert DoIpEntityRoleEnum.GATEWAY == "GATEWAY"
        assert DoIpEntityRoleEnum.NODE == "NODE"


class TestCouplingPortRatePolicyActionEnum:
    """Test cases for CouplingPortRatePolicyActionEnum (CP_TPS_SystemTemplate Table 3.70, p.125, R23-11)."""

    def test_member_presence_and_values(self):
        assert CouplingPortRatePolicyActionEnum.DROP_FRAME == "DROP-FRAME"
        assert CouplingPortRatePolicyActionEnum.BLOCK_SOURCE == "BLOCK-SOURCE"
        assert list(CouplingPortRatePolicyActionEnum().getEnumValues()) == [
            CouplingPortRatePolicyActionEnum.DROP_FRAME,
            CouplingPortRatePolicyActionEnum.BLOCK_SOURCE,
        ]

    def test_instantiability_round_trip(self):
        drop_frame = CouplingPortRatePolicyActionEnum().setValue(CouplingPortRatePolicyActionEnum.DROP_FRAME)
        assert drop_frame.getValue() == CouplingPortRatePolicyActionEnum.DROP_FRAME

        block_source = CouplingPortRatePolicyActionEnum().setValue(CouplingPortRatePolicyActionEnum.BLOCK_SOURCE)
        assert block_source.getValue() == CouplingPortRatePolicyActionEnum.BLOCK_SOURCE

    def test_class_docstring_note(self):
        assert inspect.cleandoc(CouplingPortRatePolicyActionEnum.__doc__) == "Defines the action to be performed when a rate policy is violated."


class TestCouplingPortRatePolicy:
    """Test cases for CouplingPortRatePolicy (Table 3.69, p.124)."""

    def test_initialization(self):
        policy = CouplingPortRatePolicy()
        assert isinstance(policy, ARObject)
        assert policy.getDataLength() is None
        assert policy.getPolicyAction() is None
        assert policy.getPriority() is None
        assert policy.getTimeInterval() is None
        assert policy.getVlanRefs() == []

    def test_get_set_dataLength(self):
        policy = CouplingPortRatePolicy()
        value = PositiveInteger().setValue("1500")
        result = policy.setDataLength(value)
        assert policy.getDataLength() == value
        assert result == policy

    def test_get_set_policyAction(self):
        policy = CouplingPortRatePolicy()
        value = CouplingPortRatePolicyActionEnum().setValue(CouplingPortRatePolicyActionEnum.BLOCK_SOURCE)
        result = policy.setPolicyAction(value)
        assert policy.getPolicyAction() == value
        assert result == policy

    def test_get_set_priority(self):
        policy = CouplingPortRatePolicy()
        value = PositiveInteger().setValue("5")
        result = policy.setPriority(value)
        assert policy.getPriority() == value
        assert result == policy

    def test_get_set_timeInterval(self):
        policy = CouplingPortRatePolicy()
        value = TimeValue().setValue("0.01")
        result = policy.setTimeInterval(value)
        assert policy.getTimeInterval() == value
        assert result == policy

    def test_add_get_vLanRefs(self):
        policy = CouplingPortRatePolicy()
        ref = RefType()
        ref.setValue("/Clusters/Eth/Vlan1")
        result = policy.addVlanRef(ref)
        assert policy.getVlanRefs() == [ref]
        assert result == policy

    def test_none_no_op(self):
        policy = CouplingPortRatePolicy()
        data_length = PositiveInteger().setValue("1500")
        action = CouplingPortRatePolicyActionEnum().setValue(CouplingPortRatePolicyActionEnum.DROP_FRAME)
        priority = PositiveInteger().setValue("5")
        interval = TimeValue().setValue("0.01")
        policy.setDataLength(data_length)
        policy.setPolicyAction(action)
        policy.setPriority(priority)
        policy.setTimeInterval(interval)
        result = policy.setDataLength(None)
        policy.setPolicyAction(None)
        policy.setPriority(None)
        policy.setTimeInterval(None)
        assert policy.getDataLength() == data_length
        assert policy.getPolicyAction() == action
        assert policy.getPriority() == priority
        assert policy.getTimeInterval() == interval
        assert result == policy


class TestCouplingPortDetailsRatePolicys:
    """Test cases for CouplingPortDetails.ratePolicy aggregation (Table 3.63, p.122)."""

    def test_add_get_ratePolicies(self):
        details = CouplingPortDetails()
        policy = CouplingPortRatePolicy()
        result = details.addRatePolicy(policy)
        assert details.getRatePolicies() == [policy]
        assert result == details

    def test_add_ratePolicy_none_no_op(self):
        details = CouplingPortDetails()
        details.addRatePolicy(CouplingPortRatePolicy())
        result = details.addRatePolicy(None)
        assert len(details.getRatePolicies()) == 1
        assert result == details


class TestPlcaProps:
    """Test cases for PlcaProps (Table 3.117, p.169)."""

    def test_initialization(self):
        props = PlcaProps()
        assert props.getPlcaLocalNodeId() is None
        assert props.getPlcaMaxBurstCount() is None
        assert props.getPlcaMaxBurstTimer() is None

    def test_get_set_plcaLocalNodeId(self):
        props = PlcaProps()
        value = PositiveInteger().setValue("5")
        result = props.setPlcaLocalNodeId(value)
        assert props.getPlcaLocalNodeId() == value
        assert result == props

    def test_get_set_plcaMaxBurstCount(self):
        props = PlcaProps()
        value = PositiveInteger().setValue("3")
        result = props.setPlcaMaxBurstCount(value)
        assert props.getPlcaMaxBurstCount() == value
        assert result == props

    def test_get_set_plcaMaxBurstTimer(self):
        props = PlcaProps()
        value = PositiveInteger().setValue("10")
        result = props.setPlcaMaxBurstTimer(value)
        assert props.getPlcaMaxBurstTimer() == value
        assert result == props

    def test_none_no_op(self):
        props = PlcaProps()
        node_id = PositiveInteger().setValue("7")
        props.setPlcaLocalNodeId(node_id)
        result = props.setPlcaLocalNodeId(None)
        assert props.getPlcaLocalNodeId() == node_id
        assert result == props

        burst_count = PositiveInteger().setValue("4")
        props.setPlcaMaxBurstCount(burst_count)
        result = props.setPlcaMaxBurstCount(None)
        assert props.getPlcaMaxBurstCount() == burst_count
        assert result == props

        burst_timer = PositiveInteger().setValue("20")
        props.setPlcaMaxBurstTimer(burst_timer)
        result = props.setPlcaMaxBurstTimer(None)
        assert props.getPlcaMaxBurstTimer() == burst_timer
        assert result == props


class TestCouplingPortConnection:
    """Test cases for CouplingPortConnection (Table 3.60, p.113)."""

    def test_initialization(self):
        connection = CouplingPortConnection()
        assert connection.getFirstPortRef() is None
        assert connection.getNodePortRefs() == []
        assert connection.getPlcaLocalNodeCount() is None
        assert connection.getPlcaTransmitOpportunityTimer() is None
        assert connection.getSecondPortRef() is None

    def test_get_set_first_port(self):
        connection = CouplingPortConnection()
        ref = RefType().setValue("/Ether/CouplingPort/CP1")
        result = connection.setFirstPortRef(ref)
        assert connection.getFirstPortRef() == ref
        assert result == connection

    def test_get_set_second_port(self):
        connection = CouplingPortConnection()
        ref = RefType().setValue("/Ether/CouplingPort/CP2")
        result = connection.setSecondPortRef(ref)
        assert connection.getSecondPortRef() == ref
        assert result == connection

    def test_add_node_ports(self):
        connection = CouplingPortConnection()
        ref1 = RefType().setValue("/Ether/CouplingPort/CP1")
        ref2 = RefType().setValue("/Ether/CouplingPort/CP3")
        result = connection.addNodePortRef(ref1)
        connection.addNodePortRef(ref2)
        assert connection.getNodePortRefs() == [ref1, ref2]
        assert result == connection

    def test_add_node_port_none_no_op(self):
        connection = CouplingPortConnection()
        result = connection.addNodePortRef(None)
        assert connection.getNodePortRefs() == []
        assert result == connection

    def test_get_set_plca_local_node_count(self):
        connection = CouplingPortConnection()
        value = PositiveInteger().setValue("4")
        result = connection.setPlcaLocalNodeCount(value)
        assert connection.getPlcaLocalNodeCount() == value
        assert result == connection

    def test_get_set_plca_transmit_opportunity_timer(self):
        connection = CouplingPortConnection()
        value = PositiveInteger().setValue("100")
        result = connection.setPlcaTransmitOpportunityTimer(value)
        assert connection.getPlcaTransmitOpportunityTimer() == value
        assert result == connection

    def test_none_no_op(self):
        connection = CouplingPortConnection()

        first = RefType().setValue("/Ether/CouplingPort/CP1")
        connection.setFirstPortRef(first)
        result = connection.setFirstPortRef(None)
        assert connection.getFirstPortRef() == first
        assert result == connection

        second = RefType().setValue("/Ether/CouplingPort/CP2")
        connection.setSecondPortRef(second)
        result = connection.setSecondPortRef(None)
        assert connection.getSecondPortRef() == second
        assert result == connection

        count = PositiveInteger().setValue("4")
        connection.setPlcaLocalNodeCount(count)
        result = connection.setPlcaLocalNodeCount(None)
        assert connection.getPlcaLocalNodeCount() == count
        assert result == connection

        timer = PositiveInteger().setValue("100")
        connection.setPlcaTransmitOpportunityTimer(timer)
        result = connection.setPlcaTransmitOpportunityTimer(None)
        assert connection.getPlcaTransmitOpportunityTimer() == timer
        assert result == connection


class TestGlobalTimeCouplingPortProps:
    """Test cases for GlobalTimeCouplingPortProps (Table 9.18, p.875)."""

    def test_initialization(self):
        props = GlobalTimeCouplingPortProps()
        assert props.getPropagationDelay() is None

    def test_get_set_propagation_delay(self):
        props = GlobalTimeCouplingPortProps()
        value = TimeValue().setValue("0.005")
        result = props.setPropagationDelay(value)
        assert props.getPropagationDelay() == value
        assert result == props

    def test_none_no_op(self):
        props = GlobalTimeCouplingPortProps()
        value = TimeValue().setValue("0.005")
        props.setPropagationDelay(value)
        result = props.setPropagationDelay(None)
        assert props.getPropagationDelay() == value
        assert result == props


class TestEthernetPhysicalChannel:
    """Test cases for EthernetPhysicalChannel (Table 3.49, p.105)."""

    def test_initialization(self):
        channel = EthernetPhysicalChannel(MockParent(), "TestChannel")

        assert channel.getShortName() == "TestChannel"
        assert channel.getNetworkEndpoints() == []
        assert channel.getSoAdConfig() is None
        assert channel.getVlan() is None

    def test_class_docstring_matches_spec_note(self):
        """
        Test that the class docstring is the verbatim Table 3.49 Note plus the class-level constr rows.
        """
        expected = (
            "The EthernetPhysicalChannel represents a VLAN or an untagged channel. An untagged channel "
            "is modeled as an EthernetPhysicalChannel without an aggregated VLAN.\n"
            "\n"
            "[constr_3333] Standardized values for the attribute category of meta-class EthernetPhysicalChannel: "
            "The following values of the attribute category of metaclass EthernetPhysicalChannel are reserved by the AUTOSAR standard:\n"
            "- WIRED: This represents the usage of the EthernetPhysicalChannel in case of a wired ethernet connection\n"
            "- WIRELESS: This represents the usage of the EthernetPhysicalChannel in case of a wireless ethernet connection\n"
            "\n"
            "[constr_3334] Allowed references between EthernetPhysicalChannel and EthernetCommunicationConnector: "
            "An EthernetPhysicalChannel is only allowed to reference EthernetCommunicationConnectors in the role commConnector "
            "that have the same category value as the referencing EthernetPhysicalChannel.\n"
            "\n"
            "[constr_3365] EthernetPhysicalChannels with different category values are not allowed within an EthernetCluster: "
            "A mix of EthernetPhysicalChannels with different category values within an EthernetCluster is currently not supported by AUTOSAR.\n"
            "\n"
            "[constr_3336] EthernetPhysicalChannel.soAdConfig in case of WIRELESS EthernetPhysicalChannel: "
            "If EthernetPhysicalChannel has the category WIRELESS then the EthernetPhysicalChannel shall not aggregate the SoAdConfig."
        )
        assert inspect.cleandoc(EthernetPhysicalChannel.__doc__) == expected

    def test_create_network_endpoint(self):
        channel = EthernetPhysicalChannel(MockParent(), "TestChannel")

        end_point = channel.createNetworkEndpoint("nep1")
        assert end_point.getShortName() == "nep1"
        assert channel.getNetworkEndpoints() == [end_point]

        duplicate = channel.createNetworkEndpoint("nep1")
        assert duplicate is end_point
        assert len(channel.getNetworkEndpoints()) == 1

    def test_get_set_so_ad_config(self):
        channel = EthernetPhysicalChannel(MockParent(), "TestChannel")
        config = SoAdConfig()

        result = channel.setSoAdConfig(config)
        assert channel.getSoAdConfig() is config
        assert result == channel

        result = channel.setSoAdConfig(None)
        assert channel.getSoAdConfig() is config
        assert result == channel

    def test_create_vlan_config(self):
        channel = EthernetPhysicalChannel(MockParent(), "TestChannel")

        vlan = channel.createVlanConfig("Vlan")
        assert vlan.getShortName() == "Vlan"
        assert channel.getVlan() is vlan

        identifier = PositiveInteger().setValue("5")
        vlan.setVlanIdentifier(identifier)
        assert channel.getVlan().getVlanIdentifier() == identifier

        duplicate = channel.createVlanConfig("Vlan")
        assert duplicate is vlan
        assert channel.getVlan() is vlan


ETHERNET_CLUSTER_CLASS_NOTE = "Ethernet-specific cluster attributes. Tags: atp.recommendedPackage=CommunicationClusters"
COUPLING_PORT_CONNECTIONS_NOTE = "Specification of connections between CouplingElements and EcuInstances. Note: This atpSplitable property has no atp.Splitkey due to atpVariation (PropertySetPattern). Stereotypes: atpSplitable; atpVariation Tags: vh.latestBindingTime=postBuild"
COUPLING_PORT_STARTUP_ACTIVE_TIME_NOTE = "The attribute specifies the time in second a coupling port is switched on to enable the host ECU (ECU that maintains an Ethernet switch) to listen to the network for potential network management requests."
COUPLING_PORT_SWITCHOFF_DELAY_NOTE = "Switch off delay for CouplingPorts in seconds. It denotes the delay of switching off couplingPorts after the request to switch off a couplingPort was issued. (e.g. switch off of Ethernet switch ports)."
MAC_MULTICAST_GROUP_NOTE = "MacMulticastGroup that is defined for the Subnet (EthernetCluster)."


class TestEthernetCluster:
    """Test cases for EthernetCluster (Table 3.47, p.103)."""

    MEMBERS = [
        "couplingPortConnections",
        "couplingPortStartupActiveTime",
        "couplingPortSwitchoffDelay",
        "macMulticastGroups",
    ]

    def _make(self) -> EthernetCluster:
        return EthernetCluster(MockParent(), "test_ethernet_cluster")

    def _assert_docstring(self, method, note, noop=None):
        expected = note if noop is None else note + "\n" + noop
        assert method.__doc__ is not None
        assert inspect.cleandoc(method.__doc__).strip() == expected

    def _pin(self, getter, setter, typ, owner):
        getter_hints = get_type_hints(getter)
        assert getter_hints.get("return") == typ
        setter_hints = get_type_hints(setter)
        assert setter_hints.get("value") == typ
        assert setter_hints.get("return") is owner

    def test_inheritance(self):
        assert issubclass(EthernetCluster, CommunicationCluster)
        assert issubclass(EthernetCluster, FibexElement)
        assert issubclass(EthernetCluster, ARObject)

    def test_concrete_instantiation(self):
        cluster = EthernetCluster(MockParent(), "cluster")  # Table 3.47 carries no abstract stereotype

        assert isinstance(cluster, CommunicationCluster)

    def test_initialization(self):
        cluster = self._make()

        assert cluster.getShortName() == "test_ethernet_cluster"
        assert isinstance(cluster, CommunicationCluster)
        assert cluster.getBaudrate() is None
        assert cluster.getPhysicalChannels() == []
        assert cluster.getProtocolName() is None
        assert cluster.getProtocolVersion() is None
        assert cluster.getCouplingPortConnections() == []
        assert cluster.getCouplingPortStartupActiveTime() is None
        assert cluster.getCouplingPortSwitchoffDelay() is None
        assert cluster.getMacMulticastGroups() == []

    def test_class_docstring_is_spec_note(self):
        assert inspect.cleandoc(EthernetCluster.__doc__).strip() == ETHERNET_CLUSTER_CLASS_NOTE

    def test_init_has_no_docstring(self):
        assert EthernetCluster.__init__.__doc__ is None

    def test_member_order_matches_spec(self):
        source = inspect.getsource(EthernetCluster.__init__)
        indexes = [source.index("self.%s:" % member) for member in self.MEMBERS]
        assert indexes == sorted(indexes)

    def test_get_set_coupling_port_startup_active_time(self):
        cluster = self._make()
        value = TimeValue().setValue("100")
        assert cluster == cluster.setCouplingPortStartupActiveTime(value)
        assert cluster.getCouplingPortStartupActiveTime() == value
        assert cluster == cluster.setCouplingPortStartupActiveTime(None)
        assert cluster.getCouplingPortStartupActiveTime() == value
        self._pin(EthernetCluster.getCouplingPortStartupActiveTime, EthernetCluster.setCouplingPortStartupActiveTime, Optional[TimeValue], EthernetCluster)

    def test_coupling_port_startup_active_time_docstrings_are_spec_note(self):
        self._assert_docstring(EthernetCluster.getCouplingPortStartupActiveTime, COUPLING_PORT_STARTUP_ACTIVE_TIME_NOTE)
        self._assert_docstring(
            EthernetCluster.setCouplingPortStartupActiveTime, COUPLING_PORT_STARTUP_ACTIVE_TIME_NOTE, "A None value is a no-op and does not overwrite an existing couplingPortStartupActiveTime."
        )

    def test_get_set_coupling_port_switchoff_delay(self):
        cluster = self._make()
        value = TimeValue().setValue("0.5")
        assert cluster == cluster.setCouplingPortSwitchoffDelay(value)
        assert cluster.getCouplingPortSwitchoffDelay() == value
        assert cluster == cluster.setCouplingPortSwitchoffDelay(None)
        assert cluster.getCouplingPortSwitchoffDelay() == value
        self._pin(EthernetCluster.getCouplingPortSwitchoffDelay, EthernetCluster.setCouplingPortSwitchoffDelay, Optional[TimeValue], EthernetCluster)

    def test_coupling_port_switchoff_delay_docstrings_are_spec_note(self):
        self._assert_docstring(EthernetCluster.getCouplingPortSwitchoffDelay, COUPLING_PORT_SWITCHOFF_DELAY_NOTE)
        self._assert_docstring(
            EthernetCluster.setCouplingPortSwitchoffDelay, COUPLING_PORT_SWITCHOFF_DELAY_NOTE, "A None value is a no-op and does not overwrite an existing couplingPortSwitchoffDelay."
        )

    def test_add_coupling_port_connection(self):
        cluster = self._make()
        connection = CouplingPortConnection()
        assert cluster == cluster.addCouplingPortConnection(connection)
        assert cluster.getCouplingPortConnections() == [connection]
        cluster.addCouplingPortConnection(None)
        assert cluster.getCouplingPortConnections() == [connection]
        hints = get_type_hints(EthernetCluster.addCouplingPortConnection)
        assert hints.get("value") == Optional[CouplingPortConnection]
        assert hints.get("return") is EthernetCluster
        assert get_type_hints(EthernetCluster.getCouplingPortConnections).get("return") == List[CouplingPortConnection]

    def test_coupling_port_connection_docstrings_are_spec_note(self):
        self._assert_docstring(EthernetCluster.addCouplingPortConnection, COUPLING_PORT_CONNECTIONS_NOTE, "A None value is a no-op and does not append to couplingPortConnections.")
        self._assert_docstring(EthernetCluster.getCouplingPortConnections, COUPLING_PORT_CONNECTIONS_NOTE)

    def test_create_mac_multicast_group(self):
        cluster = self._make()
        group = cluster.createMacMulticastGroup("MulticastGroup")
        assert isinstance(group, MacMulticastGroup)
        assert group.getShortName() == "MulticastGroup"
        assert cluster.getMacMulticastGroups() == [group]
        duplicate = cluster.createMacMulticastGroup("MulticastGroup")
        assert duplicate is group
        assert cluster.getMacMulticastGroups() == [group]

    def test_mac_multicast_group_docstrings_are_spec_note(self):
        self._assert_docstring(EthernetCluster.createMacMulticastGroup, MAC_MULTICAST_GROUP_NOTE)
        self._assert_docstring(EthernetCluster.getMacMulticastGroups, MAC_MULTICAST_GROUP_NOTE)


COUPLING_PORT_CLASS_NOTE = "A CouplingPort is used to connect a CouplingElement with an EcuInstance or two CouplingElements with each other via a CouplingPortConnection. Optionally, the CouplingPort may also have a reference to a macMulticastGroup and a defaultVLAN."
DEFAULT_VLAN_NOTE = "The vLanIdentifier of the referenced VLAN is the Default-PVID (port VLAN ID). A Port VLAN ID is a default VLAN ID that is assigned to an access CouplingPort to designate the VLAN segment to which this port is connected. Also, if a CouplingPort has not been configured with any VLAN memberships, the virtual switch's Port VLAN ID (pvid) becomes the default VLAN ID for the ports connection. This identifier/tag is added for incoming untagged messages at the port (ingress tagging). For outgoing messages with this identifier, the tag is removed at the port (egress untagging, depending on the VlanMembership.sendActivity)."
PNC_MAPPING_NOTE = "Reference to the partial networks this CouplingPort participates in. Stereotypes: atpSplitable Tags: atp.Splitkey=pncMapping"


class TestCouplingPortSpecSync:
    """Spec-sync checks for CouplingPort (R23-11 CP_TPS_SystemTemplate, Table 3.54, p.110)."""

    MEMBERS = [
        "connectionNegotiationBehavior",
        "couplingPortDetails",
        "couplingPortRole",
        "defaultVlanRef",
        "macLayerType",
        "macMulticastAddressRefs",
        "macSecProps",
        "physicalLayerType",
        "plcaProps",
        "pncMappingRefs",
        "receiveActivity",
        "vlanMemberships",
        "vlanModifierRef",
        "wakeupSleepOnDatalineConfigRef",
    ]

    def _make(self) -> CouplingPort:
        return CouplingPort(MockParent(), "test_coupling_port")

    def test_inheritance(self):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.StereotypeMixins import VariationPointCapable

        assert issubclass(CouplingPort, Identifiable)
        assert issubclass(CouplingPort, VariationPointCapable)
        assert issubclass(CouplingPort, ARObject)

    def test_class_docstring_is_spec_note(self):
        assert CouplingPort.__doc__.strip() == COUPLING_PORT_CLASS_NOTE

    def test_init_has_no_docstring(self):
        assert CouplingPort.__init__.__doc__ is None

    def test_member_order_matches_spec(self):
        source = inspect.getsource(CouplingPort.__init__)
        indexes = [source.index("self.%s:" % member) for member in self.MEMBERS]
        assert indexes == sorted(indexes)

    def test_coupling_port_speed_removed_not_modelled(self):
        port = self._make()
        assert not hasattr(port, "couplingPortSpeed")

    def test_default_vlan_docstrings_are_spec_note(self):
        noop = "A None value is a no-op and does not overwrite an existing defaultVlanRef."
        assert CouplingPort.getDefaultVlanRef.__doc__.strip() == DEFAULT_VLAN_NOTE
        assert inspect.cleandoc(CouplingPort.setDefaultVlanRef.__doc__).strip() == DEFAULT_VLAN_NOTE + "\n" + noop

    def test_pnc_mapping_docstrings_carry_stereotype_tail(self):
        noop = "A None value is a no-op and does not append to pncMappingRefs."
        assert inspect.cleandoc(CouplingPort.addPncMappingRef.__doc__).strip() == PNC_MAPPING_NOTE + "\n" + noop
        assert CouplingPort.getPncMappingRefs.__doc__.strip() == PNC_MAPPING_NOTE

    def test_reader_round_trips_mac_sec_props_wrapper(self, tmp_path):
        import xml.etree.cElementTree as ET

        from armodel.parser.arxml_parser import ARXMLParser

        element = ET.fromstring(
            "<COUPLING-PORT xmlns='http://autosar.org/schema/r4.0'>"
            "<SHORT-NAME>CP1</SHORT-NAME>"
            "<MAC-SEC-PROPSS><MAC-SEC-PROPS><AUTO-START>true</AUTO-START></MAC-SEC-PROPS></MAC-SEC-PROPSS>"
            "</COUPLING-PORT>"
        )
        recovered = CouplingPort(MockParent(), "CP1")
        ARXMLParser().readCouplingPort(element, recovered)
        props = recovered.getMacSecProps()
        assert len(props) == 1
        assert props[0].getAutoStart().getValue() is True


COUPLING_PORT_SHAPER_CLASS_NOTE = "Defines a shaper for the CouplingPort egress structure. Tags: atp.Status=obsolete"
IDLE_SLOPE_NOTE = "Defines the increase of credit in bits per second for the AVB shaper. Tags: atp.Status=obsolete"
PREDECESSOR_FIFO_NOTE = "Defines the CouplingPortFifo which provides the input to this shaper. Tags: atp.Status=obsolete"


class TestCouplingPortShaper:
    """Test cases for CouplingPortShaper (Table 3.67, p.123)."""

    MEMBERS = [
        "idleSlope",
        "predecessorFifoRef",
    ]

    def _make(self) -> CouplingPortShaper:
        return CouplingPortShaper(MockParent(), "test_coupling_port_shaper")

    def _assert_docstring(self, method, note, noop=None):
        expected = note if noop is None else note + "\n" + noop
        assert method.__doc__ is not None
        assert inspect.cleandoc(method.__doc__).strip() == expected

    def _pin(self, getter, setter, typ, owner):
        getter_hints = get_type_hints(getter)
        assert getter_hints.get("return") == typ
        setter_hints = get_type_hints(setter)
        assert setter_hints.get("value") == typ
        assert setter_hints.get("return") is owner

    def test_inheritance(self):
        assert issubclass(CouplingPortShaper, CouplingPortStructuralElement)
        assert issubclass(CouplingPortShaper, Identifiable)
        assert issubclass(CouplingPortShaper, ARObject)

    def test_concrete_instantiation(self):
        shaper = self._make()

        assert shaper.getShortName() == "test_coupling_port_shaper"

    def test_initialization_defaults(self):
        shaper = self._make()

        assert shaper.getIdleSlope() is None
        assert shaper.getPredecessorFifoRef() is None

    def test_member_order_matches_spec(self):
        source = inspect.getsource(CouplingPortShaper.__init__)
        indexes = [source.index("self.%s:" % member) for member in self.MEMBERS]
        assert indexes == sorted(indexes)

    def test_class_docstring_is_spec_note(self):
        assert inspect.cleandoc(CouplingPortShaper.__doc__).strip() == COUPLING_PORT_SHAPER_CLASS_NOTE

    def test_init_has_no_docstring(self):
        assert CouplingPortShaper.__init__.__doc__ is None

    def test_get_set_idle_slope(self):
        shaper = self._make()
        value = PositiveInteger().setValue("12500000")
        assert shaper.setIdleSlope(value) is shaper
        assert shaper.getIdleSlope() is value
        shaper.setIdleSlope(None)
        assert shaper.getIdleSlope().getValue() == 12500000
        self._pin(CouplingPortShaper.getIdleSlope, CouplingPortShaper.setIdleSlope, Optional[PositiveInteger], CouplingPortShaper)

    def test_idle_slope_docstrings_are_spec_note(self):
        self._assert_docstring(CouplingPortShaper.getIdleSlope, IDLE_SLOPE_NOTE)
        self._assert_docstring(CouplingPortShaper.setIdleSlope, IDLE_SLOPE_NOTE, "A None value is a no-op and does not overwrite an existing idleSlope.")

    def test_get_set_predecessor_fifo_ref(self):
        shaper = self._make()
        ref = RefType().setValue("/Clusters/Switch/CouplingPort/Fifo1").setDest("COUPLING-PORT-FIFO")
        assert shaper.setPredecessorFifoRef(ref) is shaper
        assert shaper.getPredecessorFifoRef() is ref
        shaper.setPredecessorFifoRef(None)
        assert shaper.getPredecessorFifoRef() is ref
        self._pin(CouplingPortShaper.getPredecessorFifoRef, CouplingPortShaper.setPredecessorFifoRef, Optional[RefType], CouplingPortShaper)

    def test_predecessor_fifo_ref_docstrings_are_spec_note(self):
        self._assert_docstring(CouplingPortShaper.getPredecessorFifoRef, PREDECESSOR_FIFO_NOTE)
        self._assert_docstring(CouplingPortShaper.setPredecessorFifoRef, PREDECESSOR_FIFO_NOTE, "A None value is a no-op and does not overwrite an existing predecessorFifoRef.")

    def test_details_create_coupling_port_shaper_appends(self):
        details = CouplingPortDetails()
        shaper = details.createCouplingPortShaper("Shaper1")

        assert shaper.getShortName() == "Shaper1"
        assert details.getCouplingPortStructuralElements() == [shaper]
