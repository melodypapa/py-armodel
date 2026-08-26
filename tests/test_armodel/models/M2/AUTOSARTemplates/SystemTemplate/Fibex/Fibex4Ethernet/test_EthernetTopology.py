"""
Test suite for EthernetTopology classes in AUTOSAR System Template.

This module contains comprehensive unit tests for Ethernet communication topology classes
including Ethernet clusters, communication controllers, connectors, and related components.
Each test validates the functionality, inheritance, and setter/getter methods
of the respective classes.
"""

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Describable, Identifiable, Referrable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, RefType, TimeValue
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.TagWithOptionalValue import TagWithOptionalValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    CouplingPort,
    CouplingPortDetails,
    CouplingPortFifo,
    EthernetPhysicalLayerTypeEnum,
    EthernetSwitchVlanIngressTagEnum,
    CouplingPortScheduler,
    CouplingPortStructuralElement,
    CouplingPortTrafficClassAssignment,
    CouplingPortRoleEnum,
    DhcpServerConfiguration,
    EthernetConnectionNegotiationEnum,
    EthernetMacLayerTypeEnum,
    DoIpEntity,
    EthernetCluster,
    EthernetCommunicationConnector,
    EthernetCommunicationController,
    EthernetPriorityRegeneration,
    InfrastructureServices,
    InitialSdDelayConfig,
    IpAddressKeepEnum,
    Ipv4Configuration,
    Ipv4DhcpServerConfiguration,
    Ipv6AddressSourceEnum,
    Ipv6Configuration,
    Ipv6DhcpServerConfiguration,
    MacMulticastGroup,
    NetworkEndpoint,
    NetworkEndpointAddress,
    RequestResponseDelay,
    SdClientConfig,
    TimeSyncClientConfiguration,
    TimeSyncTechnologyEnum,
    TimeSynchronization,
    TimeSyncServerConfiguration,
    VlanMembership,
)


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
        Test the CouplingPortStructuralElement abstract class.
        """
        parent = MockParent()

        # Test that abstract class cannot be instantiated directly
        with pytest.raises(TypeError):
            CouplingPortStructuralElement(parent, "TestElement")

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
        Test the SdClientConfig class initialization and methods (XSD SD-CLIENT-CONFIG group;
        obsolete class, no R23-11 table).
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


class TestEthernetConnectionNegotiationEnum:
    """Test cases for EthernetConnectionNegotiationEnum (Table 3.55, p.110)."""

    def test_enum_values(self):
        assert list(EthernetConnectionNegotiationEnum().getEnumValues()) == ["auto", "master", "slave"]
        assert EthernetConnectionNegotiationEnum.AUTO == "auto"
        assert EthernetConnectionNegotiationEnum.MASTER == "master"
        assert EthernetConnectionNegotiationEnum.SLAVE == "slave"


class TestCouplingPortRoleEnum:
    """Test cases for CouplingPortRoleEnum (Table F.38)."""

    def test_enum_values(self):
        assert list(CouplingPortRoleEnum().getEnumValues()) == ["hostPort", "upLinkPort", "standardPort"]
        assert CouplingPortRoleEnum.HOST_PORT == "hostPort"
        assert CouplingPortRoleEnum.UP_LINK_PORT == "upLinkPort"
        assert CouplingPortRoleEnum.STANDARD_PORT == "standardPort"


class TestEthernetMacLayerTypeEnum:
    """Test cases for EthernetMacLayerTypeEnum (Table 3.56, p.110)."""

    def test_enum_values(self):
        assert list(EthernetMacLayerTypeEnum().getEnumValues()) == ["xGMII", "xMII", "xXGMII"]
        assert EthernetMacLayerTypeEnum.XGMII == "xGMII"
        assert EthernetMacLayerTypeEnum.XMII == "xMII"
        assert EthernetMacLayerTypeEnum.XXGMII == "xXGMII"


class Test_Fibex4EthernetNetworkEndpoint:
    """Test cases for the NetworkEndpoint classes relocated to Fibex4Ethernet.EthernetTopology."""

    def test_NetworkEndpointAddress(self):
        """Test NetworkEndpointAddress abstract class instantiation."""
        with pytest.raises(TypeError):
            NetworkEndpointAddress()

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

        result = config.setIpAddressKeepBehavior("keep")
        assert config.getIpAddressKeepBehavior() == "keep"
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
        assert config.getIpAddressKeepBehavior().getValue() == "storePersistently"
        assert isinstance(config.getIpAddressKeepBehavior(), IpAddressKeepEnum)
        assert result == config  # Test method chaining

        # None no-op for ipAddressKeepBehavior
        result = config.setIpAddressKeepBehavior(None)
        assert config.getIpAddressKeepBehavior().getValue() == "storePersistently"

        result = config.setIpAddressPrefixLength(64)
        assert config.getIpAddressPrefixLength() == 64
        assert result == config  # Test method chaining

        result = config.setIpv6Address("2001:db8::1")
        assert config.getIpv6Address() == "2001:db8::1"
        assert result == config  # Test method chaining

        source = Ipv6AddressSourceEnum().setValue(Ipv6AddressSourceEnum.LINK_LOCAL)
        result = config.setIpv6AddressSource(source)
        assert config.getIpv6AddressSource() is source
        assert config.getIpv6AddressSource().getValue() == "linkLocal"
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
        """Test TimeSyncClientConfiguration class functionality."""
        config = TimeSyncClientConfiguration()

        assert isinstance(config, ARObject)

        # Test default values
        assert config.getOrderedMasters() == []
        assert config.getTimeSyncTechnology() is None

        # Test setter/getter methods with method chaining
        result = config.setTimeSyncTechnology("IEEE_1588")
        assert config.getTimeSyncTechnology() == "IEEE_1588"
        assert result == config  # Test method chaining

        # Test adding ordered masters with method chaining
        result = config.addOrderedMaster("master1")
        assert config.getOrderedMasters() == ["master1"]
        assert result == config  # Test method chaining

        result = config.addOrderedMaster("master2")
        assert config.getOrderedMasters() == ["master1", "master2"]
        assert result == config  # Test method chaining

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

        autosar = AUTOSAR.getInstance()
        ar_package = autosar.createARPackage("TEST")
        server_config = TimeSyncServerConfiguration(ar_package, "time_sync_server")
        result = sync.setTimeSyncServer(server_config)
        assert sync.getTimeSyncServer() == server_config
        assert result == sync  # Test method chaining

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
    """Test cases for EthernetPhysicalLayerTypeEnum (Table 3.57, p.111)."""

    def test_enum_values(self):
        assert list(EthernetPhysicalLayerTypeEnum().getEnumValues()) == [
            "1000BASE-T",
            "1000BASE-T1",
            "100BASE-T1",
            "100BASE-TX",
            "10BASE-T1S",
            "IEEE802-11P",
        ]
        assert EthernetPhysicalLayerTypeEnum._1000BASE_T == "1000BASE-T"
        assert EthernetPhysicalLayerTypeEnum._1000BASE_T1 == "1000BASE-T1"
        assert EthernetPhysicalLayerTypeEnum._100BASE_T1 == "100BASE-T1"
        assert EthernetPhysicalLayerTypeEnum._100BASE_TX == "100BASE-TX"
        assert EthernetPhysicalLayerTypeEnum._10BASE_T1S == "10BASE-T1S"
        assert EthernetPhysicalLayerTypeEnum.I_EEE802_11P == "IEEE802-11P"


class TestEthernetSwitchVlanIngressTagEnum:
    """Test cases for EthernetSwitchVlanIngressTagEnum (Table 3.58, p.111)."""

    def test_enum_values(self):
        assert list(EthernetSwitchVlanIngressTagEnum().getEnumValues()) == [
            "forwardAsIs",
            "dropUntagged",
        ]
        assert EthernetSwitchVlanIngressTagEnum.FORWARD_AS_IS == "forwardAsIs"
        assert EthernetSwitchVlanIngressTagEnum.DROP_UNTAGGED == "dropUntagged"


class TestTimeSyncTechnologyEnum:
    """Test cases for TimeSyncTechnologyEnum (Table 6.149, p.471)."""

    def test_enum_values(self):
        assert list(TimeSyncTechnologyEnum().getEnumValues()) == [
            "AVB-IEEE-802-1-AS",
            "NTP-RFC-958",
            "PTP-IEEE-1588-2002",
            "PTP-IEEE-1588-2008",
        ]
        assert TimeSyncTechnologyEnum.AVB_IEEE802_1AS == "AVB-IEEE-802-1-AS"
        assert TimeSyncTechnologyEnum.NTP_RFC958 == "NTP-RFC-958"
        assert TimeSyncTechnologyEnum.PTP_IEEE1588_2002 == "PTP-IEEE-1588-2002"
        assert TimeSyncTechnologyEnum.PTP_IEEE1588_2008 == "PTP-IEEE-1588-2008"
