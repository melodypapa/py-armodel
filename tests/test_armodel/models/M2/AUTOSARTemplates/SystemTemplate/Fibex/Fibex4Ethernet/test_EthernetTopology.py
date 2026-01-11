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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable


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
        group.setMacMulticastAddress(test_address)
        assert group.getMacMulticastAddress() == test_address

    def test_ethernet_cluster(self):
        """
        Test the EthernetCluster class initialization and methods.
        """
        parent = MockParent()
        cluster = EthernetCluster(parent, "TestCluster")
        
        assert cluster.getShortName() == "TestCluster"
        assert cluster.getCouplingPortStartupActiveTime() is None
        assert cluster.getCouplingPortSwitchoffDelay() is None
        
        # Test setting timing values
        test_time = 100
        cluster.setCouplingPortStartupActiveTime(test_time)
        cluster.setCouplingPortSwitchoffDelay(test_time)
        
        assert cluster.getCouplingPortStartupActiveTime() == test_time
        assert cluster.getCouplingPortSwitchoffDelay() == test_time
        
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
        
        # Test adding traffic class
        fifo.addAssignedTrafficClass(5)
        assert fifo.getAssignedTrafficClasses() == [5]
        
        # Test setting minimum FIFO length
        fifo.setMinimumFifoLength(1024)
        assert fifo.getMinimumFifoLength() == 1024

    def test_coupling_port_scheduler(self):
        """
        Test the CouplingPortScheduler class initialization and methods.
        """
        parent = MockParent()
        scheduler = CouplingPortScheduler(parent, "TestScheduler")
        
        assert scheduler.getShortName() == "TestScheduler"
        assert scheduler.getPredecessorRefs() == []
        assert scheduler.getPortScheduler() is None
        
        # Test adding predecessor reference
        scheduler.addPredecessorRef("TestRef")
        assert scheduler.getPredecessorRefs() == ["TestRef"]
        
        # Test setting port scheduler
        scheduler.setPortScheduler("RoundRobin")
        assert scheduler.getPortScheduler() == "RoundRobin"

    def test_ethernet_priority_regeneration(self):
        """
        Test the EthernetPriorityRegeneration class initialization and methods.
        """
        parent = MockParent()
        regeneration = EthernetPriorityRegeneration(parent, "TestRegeneration")
        
        assert regeneration.getShortName() == "TestRegeneration"
        assert regeneration.getIngressPriority() is None
        assert regeneration.getRegeneratedPriority() is None
        
        # Test setting priorities
        regeneration.setIngressPriority(3)
        regeneration.setRegeneratedPriority(7)
        
        assert regeneration.getIngressPriority() == 3
        assert regeneration.getRegeneratedPriority() == 7

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
        
        # Test setting default traffic class
        details.setDefaultTrafficClass(5)
        assert details.getDefaultTrafficClass() == 5
        
        # Test frame preemption support
        details.setFramePreemptionSupport(True)
        assert details.getFramePreemptionSupport() is True

    def test_vlan_membership(self):
        """
        Test the VlanMembership class initialization and methods.
        """
        membership = VlanMembership()
        
        assert membership.getDefaultPriority() is None
        assert membership.getDhcpAddressAssignment() is None
        assert membership.getSendActivity() is None
        assert membership.getVlanRef() is None
        
        # Test setting values
        membership.setDefaultPriority(3)
        membership.setSendActivity("Tagged")
        membership.setVlanRef("Vlan100")
        
        assert membership.getDefaultPriority() == 3
        assert membership.getSendActivity() == "Tagged"
        assert membership.getVlanRef() == "Vlan100"

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
        
        # Test setting values
        port.setConnectionNegotiationBehavior("Auto")
        port.setCouplingPortRole("Master")
        
        assert port.getConnectionNegotiationBehavior() == "Auto"
        assert port.getCouplingPortRole() == "Master"

        # Test adding VLAN membership
        membership = VlanMembership()
        port.addVlanMembership(membership)
        assert port.getVlanMemberships() == [membership]

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
        
        # Test setting values
        controller.setCanXlConfigRef("CanXlConfigRef")
        controller.setMacLayerType("TypeA")
        controller.setMaximumReceiveBufferLength(2048)
        controller.setMaximumTransmitBufferLength(2048)
        controller.setSlaveActAsPassiveCommunicationSlave(True)
        
        assert controller.getCanXlConfigRef() == "CanXlConfigRef"
        assert controller.getMacLayerType() == "TypeA"
        assert controller.getMaximumReceiveBufferLength() == 2048
        assert controller.getMaximumTransmitBufferLength() == 2048
        assert controller.getSlaveActAsPassiveCommunicationSlave() is True

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
        
        # Test setting values
        connector.setEthIpPropsRef("EthIpPropsRef")
        connector.setMaximumTransmissionUnit(1500)
        connector.setNeighborCacheSize(100)
        connector.setPathMtuEnabled(True)
        
        assert connector.getEthIpPropsRef() == "EthIpPropsRef"
        assert connector.getMaximumTransmissionUnit() == 1500
        assert connector.getNeighborCacheSize() == 100
        assert connector.getPathMtuEnabled() is True

        # Test adding network endpoint reference
        connector.addNetworkEndpointRef("EndpointRef1")
        connector.addNetworkEndpointRef("EndpointRef2")
        assert connector.getNetworkEndpointRefs() == ["EndpointRef1", "EndpointRef2"]

    def test_request_response_delay(self):
        """
        Test the RequestResponseDelay class initialization and methods.
        """
        delay = RequestResponseDelay()
        
        assert delay.getMaxValue() is None
        assert delay.getMinValue() is None
        
        # Test setting values
        delay.setMaxValue(5000)
        delay.setMinValue(1000)
        
        assert delay.getMaxValue() == 5000
        assert delay.getMinValue() == 1000

    def test_initial_sd_delay_config(self):
        """
        Test the InitialSdDelayConfig class initialization and methods.
        """
        config = InitialSdDelayConfig()
        
        assert config.getInitialDelayMaxValue() is None
        assert config.getInitialDelayMinValue() is None
        assert config.getInitialRepetitionsBaseDelay() is None
        assert config.getInitialRepetitionsMax() is None
        
        # Test setting values
        config.setInitialDelayMaxValue(2000)
        config.setInitialDelayMinValue(100)
        config.setInitialRepetitionsBaseDelay(500)
        config.setInitialRepetitionsMax(3)
        
        assert config.getInitialDelayMaxValue() == 2000
        assert config.getInitialDelayMinValue() == 100
        assert config.getInitialRepetitionsBaseDelay() == 500
        assert config.getInitialRepetitionsMax() == 3

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
            
            # Test setting values
            config.setClientServiceMajorVersion(1)
            config.setClientServiceMinorVersion(2)
            config.setTtl(5000)
            
            assert config.getClientServiceMajorVersion() == 1
            assert config.getClientServiceMinorVersion() == 2
            assert config.getTtl() == 5000