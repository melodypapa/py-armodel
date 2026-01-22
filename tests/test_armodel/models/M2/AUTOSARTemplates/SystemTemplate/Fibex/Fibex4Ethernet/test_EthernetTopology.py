"""
Test suite for EthernetTopology classes in AUTOSAR System Template.

This module contains comprehensive unit tests for Ethernet communication topology classes
including Ethernet clusters, communication controllers, connectors, and related components.
Each test validates the functionality, inheritance, and setter/getter methods
of the respective classes.
"""

import pytest
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    MacMulticastGroup,
    EthernetCluster,
    CouplingPortStructuralElement,
    CouplingPortFifo,
    CouplingPortScheduler,
    EthernetPriorityRegeneration,
    CouplingPortDetails,
    VlanMembership,
    CouplingPort,
    EthernetCommunicationController,
    EthernetCommunicationConnector,
    RequestResponseDelay,
    InitialSdDelayConfig,
    SdClientConfig
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject


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
        Test the EthernetCluster class initialization and methods.
        """
        parent = MockParent()
        cluster = EthernetCluster(parent, "TestCluster")
        
        assert cluster.getShortName() == "TestCluster"
        assert cluster.getCouplingPorts() == []
        assert cluster.getCouplingPortStartupActiveTime() is None
        assert cluster.getCouplingPortSwitchoffDelay() is None
        assert cluster.getMacMulticastGroups() == []
        
        # Test setting timing values with method chaining
        test_time = 100
        result = cluster.setCouplingPortStartupActiveTime(test_time)
        assert cluster.getCouplingPortStartupActiveTime() == test_time
        assert result == cluster  # Test method chaining

        result = cluster.setCouplingPortSwitchoffDelay(test_time)
        assert cluster.getCouplingPortSwitchoffDelay() == test_time
        assert result == cluster  # Test method chaining
        
        # Test adding coupling port
        result = cluster.addCouplingPort("port1")
        assert cluster.getCouplingPorts() == ["port1"]
        assert result == cluster  # Test method chaining
        
        # Test creating MAC multicast group
        test_group = cluster.createMacMulticastGroup("TestMulticastGroup")
        assert isinstance(test_group, MacMulticastGroup)
        assert test_group.getShortName() == "TestMulticastGroup"

    def test_coupling_port_structural_element(self):
        """
        Test the CouplingPortStructuralElement abstract class.
        """
        parent = MockParent()
        
        # Test that abstract class cannot be instantiated directly
        with pytest.raises(NotImplementedError):
            CouplingPortStructuralElement(parent, "TestElement")

    def test_coupling_port_fifo(self):
        """
        Test the CouplingPortFifo class initialization and methods.
        """
        parent = MockParent()
        fifo = CouplingPortFifo(parent, "TestFifo")
        
        assert fifo.getShortName() == "TestFifo"
        assert fifo.getAssignedTrafficClasses() == []
        assert fifo.getMinimumFifoLength() is None
        assert fifo.getShaper() is None
        assert fifo.getTrafficClassPreemptionSupport() is None
        
        # Test adding traffic class with method chaining
        result = fifo.addAssignedTrafficClass(5)
        assert fifo.getAssignedTrafficClasses() == [5]
        assert result == fifo  # Test method chaining
        
        # Test setting minimum FIFO length with method chaining
        result = fifo.setMinimumFifoLength(1024)
        assert fifo.getMinimumFifoLength() == 1024
        assert result == fifo  # Test method chaining

        # Test setting shaper with method chaining
        result = fifo.setShaper("shaper_obj")
        assert fifo.getShaper() == "shaper_obj"
        assert result == fifo  # Test method chaining

        # Test setting traffic class preemption support with method chaining
        result = fifo.setTrafficClassPreemptionSupport("support")
        assert fifo.getTrafficClassPreemptionSupport() == "support"
        assert result == fifo  # Test method chaining

    def test_coupling_port_scheduler(self):
        """
        Test the CouplingPortScheduler class initialization and methods.
        """
        parent = MockParent()
        scheduler = CouplingPortScheduler(parent, "TestScheduler")
        
        assert scheduler.getShortName() == "TestScheduler"
        assert scheduler.getPredecessorRefs() == []
        assert scheduler.getPortScheduler() is None
        
        # Test adding predecessor reference with method chaining
        result = scheduler.addPredecessorRef("TestRef")
        assert scheduler.getPredecessorRefs() == ["TestRef"]
        assert result == scheduler  # Test method chaining
        
        # Test setting port scheduler with method chaining
        result = scheduler.setPortScheduler("RoundRobin")
        assert scheduler.getPortScheduler() == "RoundRobin"
        assert result == scheduler  # Test method chaining

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
        Test the CouplingPortDetails class initialization and methods.
        """
        details = CouplingPortDetails()
        
        assert details.getCouplingPortStructuralElements() == []
        assert details.getDefaultTrafficClass() is None
        assert details.getEthernetPriorityRegenerations() == []
        assert details.getEthernetTrafficClassAssignments() == []
        assert details.getFramePreemptionSupport() is None
        assert details.getGlobalTimeProps() is None
        assert details.getLastEgressSchedulerRef() is None
        assert details.getRatePolicies() == []
        assert details.getVlanTranslationTables() == []
        
        # Test setting default traffic class with method chaining
        result = details.setDefaultTrafficClass(5)
        assert details.getDefaultTrafficClass() == 5
        assert result == details  # Test method chaining

        # Test frame preemption support with method chaining
        result = details.setFramePreemptionSupport(True)
        assert details.getFramePreemptionSupport() is True
        assert result == details  # Test method chaining

        # Test global time props with method chaining
        result = details.setGlobalTimeProps("time_props")
        assert details.getGlobalTimeProps() == "time_props"
        assert result == details  # Test method chaining

        # Test last egress scheduler ref with method chaining
        result = details.setLastEgressSchedulerRef("scheduler_ref")
        assert details.getLastEgressSchedulerRef() == "scheduler_ref"
        assert result == details  # Test method chaining

        # Test ethernet traffic class assignments with method chaining
        result = details.setEthernetTrafficClassAssignments(["assignment1"])
        assert details.getEthernetTrafficClassAssignments() == ["assignment1"]
        assert result == details  # Test method chaining

        # Test rate policies with method chaining
        result = details.setRatePolicies(["policy1"])
        assert details.getRatePolicies() == ["policy1"]
        assert result == details  # Test method chaining

        # Test vlan translation tables with method chaining
        result = details.setVlanTranslationTables(["table1"])
        assert details.getVlanTranslationTables() == ["table1"]
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

        # Test setting ethernet priority regenerations with method chaining
        result = details.setEthernetPriorityRegenerations(["regen1", "regen2"])
        assert details.getEthernetPriorityRegenerations() == ["regen1", "regen2"]
        assert result == details  # Test method chaining

    def test_vlan_membership(self):
        """
        Test the VlanMembership class initialization and methods.
        """
        membership = VlanMembership()
        
        assert membership.getDefaultPriority() is None
        assert membership.getDhcpAddressAssignment() is None
        assert membership.getSendActivity() is None
        assert membership.getVlanRef() is None
        
        # Test setting values with method chaining
        result = membership.setDefaultPriority(3)
        assert membership.getDefaultPriority() == 3
        assert result == membership  # Test method chaining

        result = membership.setSendActivity("Tagged")
        assert membership.getSendActivity() == "Tagged"
        assert result == membership  # Test method chaining

        result = membership.setVlanRef("Vlan100")
        assert membership.getVlanRef() == "Vlan100"
        assert result == membership  # Test method chaining

        result = membership.setDhcpAddressAssignment("dhcp_config")
        assert membership.getDhcpAddressAssignment() == "dhcp_config"
        assert result == membership  # Test method chaining

    def test_coupling_port(self):
        """
        Test the CouplingPort class initialization and methods.
        """
        parent = MockParent()
        port = CouplingPort(parent, "TestPort")
        
        assert port.getShortName() == "TestPort"
        assert port.getConnectionNegotiationBehavior() is None
        assert port.getCouplingPortDetails() is None
        assert port.getCouplingPortRole() is None
        assert port.getDefaultVlanRef() is None
        assert port.getMacAddressVlanAssignments() == []
        assert port.getMacLayerType() is None
        assert port.getMacMulticastAddressRefs() == []
        assert port.getMacSecProps() == []
        assert port.getPhysicalLayerType() is None
        assert port.getPlcaProps() is None
        assert port.getPncMappingRefs() == []
        assert port.getReceiveActivity() is None
        assert port.getVlanMemberships() == []
        assert port.getWakeupSleepOnDatalineConfigRef() is None
        
        # Test setting values with method chaining
        result = port.setConnectionNegotiationBehavior("Auto")
        assert port.getConnectionNegotiationBehavior() == "Auto"
        assert result == port  # Test method chaining

        result = port.setCouplingPortRole("Master")
        assert port.getCouplingPortRole() == "Master"
        assert result == port  # Test method chaining

        result = port.setCouplingPortDetails("details_obj")
        assert port.getCouplingPortDetails() == "details_obj"
        assert result == port  # Test method chaining

        result = port.setDefaultVlanRef("vlan_ref")
        assert port.getDefaultVlanRef() == "vlan_ref"
        assert result == port  # Test method chaining

        result = port.setMacLayerType("type")
        assert port.getMacLayerType() == "type"
        assert result == port  # Test method chaining

        result = port.setPhysicalLayerType("phy_type")
        assert port.getPhysicalLayerType() == "phy_type"
        assert result == port  # Test method chaining

        result = port.setPlcaProps("plca_props")
        assert port.getPlcaProps() == "plca_props"
        assert result == port  # Test method chaining

        result = port.setWakeupSleepOnDatalineConfigRef("wakeup_ref")
        assert port.getWakeupSleepOnDatalineConfigRef() == "wakeup_ref"
        assert result == port  # Test method chaining

        result = port.setReceiveActivity("activity")
        assert port.getReceiveActivity() == "activity"
        assert result == port  # Test method chaining

        # Test adding MAC multicast address refs with method chaining
        result = port.setMacMulticastAddressRefs(["ref1", "ref2"])
        assert port.getMacMulticastAddressRefs() == ["ref1", "ref2"]
        assert result == port  # Test method chaining

        # Test adding MAC sec props with method chaining
        result = port.setMacSecProps(["sec1", "sec2"])
        assert port.getMacSecProps() == ["sec1", "sec2"]
        assert result == port  # Test method chaining

        # Test adding PNC mapping refs with method chaining
        result = port.setPncMappingRefs(["pnc1", "pnc2"])
        assert port.getPncMappingRefs() == ["pnc1", "pnc2"]
        assert result == port  # Test method chaining

        # Test adding MAC address VLAN assignments with method chaining
        result = port.setMacAddressVlanAssignments(["vlan1", "vlan2"])
        assert port.getMacAddressVlanAssignments() == ["vlan1", "vlan2"]
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
        Test the EthernetCommunicationConnector class initialization and methods.
        """
        parent = MockParent()
        connector = EthernetCommunicationConnector(parent, "TestConnector")
        
        assert connector.getShortName() == "TestConnector"
        assert connector.getEthIpPropsRef() is None
        assert connector.getMaximumTransmissionUnit() is None
        assert connector.getNeighborCacheSize() is None
        assert connector.getNetworkEndpointRefs() == []
        assert connector.getPathMtuEnabled() is None
        assert connector.getPathMtuTimeout() is None
        
        # Test setting values with method chaining
        result = connector.setEthIpPropsRef("EthIpPropsRef")
        assert connector.getEthIpPropsRef() == "EthIpPropsRef"
        assert result == connector  # Test method chaining

        result = connector.setMaximumTransmissionUnit(1500)
        assert connector.getMaximumTransmissionUnit() == 1500
        assert result == connector  # Test method chaining

        result = connector.setNeighborCacheSize(100)
        assert connector.getNeighborCacheSize() == 100
        assert result == connector  # Test method chaining

        result = connector.setPathMtuEnabled(True)
        assert connector.getPathMtuEnabled() is True
        assert result == connector  # Test method chaining

        result = connector.setPathMtuTimeout("timeout_val")
        assert connector.getPathMtuTimeout() == "timeout_val"
        assert result == connector  # Test method chaining

        # Test adding network endpoint reference with method chaining
        result = connector.addNetworkEndpointRef("EndpointRef1")
        assert connector.getNetworkEndpointRefs() == ["EndpointRef1"]
        assert result == connector  # Test method chaining

        result = connector.addNetworkEndpointRef("EndpointRef2")
        assert connector.getNetworkEndpointRefs() == ["EndpointRef1", "EndpointRef2"]
        assert result == connector  # Test method chaining

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

    def test_sd_client_config(self):
        """
        Test the SdClientConfig class initialization and methods.
        """
        config = SdClientConfig()
    
        # Note: SdClientConfig doesn't have getCapabilityRecord() method
        # Check other properties that exist
        assert config.getClientServiceMajorVersion() is None
        assert config.getClientServiceMinorVersion() is None
        assert config.getInitialFindBehavior() is None
        assert config.getRequestResponseDelay() is None
        assert config.getTtl() is None
        
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