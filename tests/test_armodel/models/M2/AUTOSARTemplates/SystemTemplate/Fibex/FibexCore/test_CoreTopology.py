import pytest

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import (
    CommunicationCycle,
    CycleCounter,
    CycleRepetitionType,
    CycleRepetition,
    PhysicalChannel,
    AbstractCanPhysicalChannel,
    CanPhysicalChannel,
    LinPhysicalChannel,
    VlanConfig,
    EthernetPhysicalChannel,
    FlexrayChannelName,
    FlexrayPhysicalChannel,
    CommunicationCluster,
    CanClusterBusOffRecovery,
    AbstractCanCluster,
    CanCluster,
    LinCluster,
    CommunicationController,
    PncGatewayTypeEnum,
    CommunicationDirectionType,
    CommConnectorPort,
    FramePort,
    IPduSignalProcessingEnum,
    IPduPort,
    ISignalPort,
    CommunicationConnector
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


class Test_FibexCoreTopology:
    """Test cases for FibexCore Topology classes."""
    
    def test_CommunicationCycle(self):
        """Test CommunicationCycle class functionality."""
        cycle = CommunicationCycle()

        assert isinstance(cycle, ARObject)

    def test_CycleCounter(self):
        """Test CycleCounter class functionality."""
        counter = CycleCounter()

        assert isinstance(counter, CommunicationCycle)
        
        # Test default values
        assert counter.getCycleCounter() is None
        
        # Test setter/getter methods
        counter.setCycleCounter(10)
        assert counter.getCycleCounter() == 10

    def test_CycleRepetitionType(self):
        """Test CycleRepetitionType enum functionality."""
        enum = CycleRepetitionType()
        assert enum is not None

    def test_CycleRepetition(self):
        """Test CycleRepetition class functionality."""
        repetition = CycleRepetition()

        assert isinstance(repetition, CommunicationCycle)
        
        # Test default values
        assert repetition.getBaseCycle() is None
        assert repetition.getCycleRepetition() is None

    def test_PhysicalChannel(self):
        """Test PhysicalChannel abstract class instantiation."""
        parent = MockParent()
        with pytest.raises(NotImplementedError):
            PhysicalChannel(parent, "test_physical_channel")

    def test_AbstractCanPhysicalChannel(self):
        """Test AbstractCanPhysicalChannel abstract class instantiation."""
        parent = MockParent()
        with pytest.raises(NotImplementedError):
            AbstractCanPhysicalChannel(parent, "test_abstract_can_physical_channel")

    def test_CanPhysicalChannel(self):
        """Test CanPhysicalChannel class functionality."""
        parent = MockParent()
        channel = CanPhysicalChannel(parent, "test_can_physical_channel")

        assert isinstance(channel, PhysicalChannel)

    def test_LinPhysicalChannel(self):
        """Test LinPhysicalChannel class functionality."""
        parent = MockParent()
        channel = LinPhysicalChannel(parent, "test_lin_physical_channel")

        assert isinstance(channel, PhysicalChannel)
        
        # Test default values
        assert channel.getBusIdleTimeoutPeriod() is None
        assert channel.getScheduleTables() == []

    def test_VlanConfig(self):
        """Test VlanConfig class functionality."""
        parent = MockParent()
        config = VlanConfig(parent, "test_vlan_config")

        assert isinstance(config, Identifiable)
        
        # Test default values
        assert config.getVlanIdentifier() is None
        
        # Test setter/getter methods
        config.setVlanIdentifier(100)
        assert config.getVlanIdentifier() == 100

    def test_EthernetPhysicalChannel(self):
        """Test EthernetPhysicalChannel class functionality."""
        parent = MockParent()
        channel = EthernetPhysicalChannel(parent, "test_ethernet_physical_channel")

        assert isinstance(channel, PhysicalChannel)

    def test_FlexrayChannelName(self):
        """Test FlexrayChannelName enum functionality."""
        enum = FlexrayChannelName()
        assert enum is not None
        assert FlexrayChannelName.CHANNEL_A in enum.getEnumValues()
        assert FlexrayChannelName.channel_B in enum.getEnumValues()

    def test_FlexrayPhysicalChannel(self):
        """Test FlexrayPhysicalChannel class functionality."""
        parent = MockParent()
        channel = FlexrayPhysicalChannel(parent, "test_flexray_physical_channel")

        assert isinstance(channel, PhysicalChannel)

    def test_CommunicationCluster(self):
        """Test CommunicationCluster abstract class instantiation."""
        parent = MockParent()
        with pytest.raises(NotImplementedError):
            CommunicationCluster(parent, "test_communication_cluster")

    def test_CanClusterBusOffRecovery(self):
        """Test CanClusterBusOffRecovery class functionality."""
        recovery = CanClusterBusOffRecovery()

        assert isinstance(recovery, ARObject)
        
        # Test default values
        assert recovery.getBorCounterL1ToL2() is None
        assert recovery.getBorTimeL1() is None
        assert recovery.getBorTimeL2() is None
        assert recovery.getBorTimeTxEnsured() is None
        assert recovery.getMainFunctionPeriod() is None

    def test_AbstractCanCluster(self):
        """Test AbstractCanCluster abstract class instantiation."""
        parent = MockParent()
        with pytest.raises(NotImplementedError):
            AbstractCanCluster(parent, "test_abstract_can_cluster")

    def test_CanCluster(self):
        """Test CanCluster class functionality."""
        parent = MockParent()
        cluster = CanCluster(parent, "test_can_cluster")

        assert isinstance(cluster, CommunicationCluster)

    def test_LinCluster(self):
        """Test LinCluster class functionality."""
        parent = MockParent()
        cluster = LinCluster(parent, "test_lin_cluster")

        assert isinstance(cluster, CommunicationCluster)

    def test_CommunicationController(self):
        """Test CommunicationController abstract class instantiation."""
        parent = MockParent()
        with pytest.raises(NotImplementedError):
            CommunicationController(parent, "test_communication_controller")

    def test_PncGatewayTypeEnum(self):
        """Test PncGatewayTypeEnum enum functionality."""
        enum = PncGatewayTypeEnum()
        assert enum is not None
        assert PncGatewayTypeEnum.ENUM_ACTIVE in enum.getEnumValues()
        assert PncGatewayTypeEnum.ENUM_NONE in enum.getEnumValues()
        assert PncGatewayTypeEnum.ENUM_PASSIVE in enum.getEnumValues()

    def test_CommunicationDirectionType(self):
        """Test CommunicationDirectionType enum functionality."""
        enum = CommunicationDirectionType()
        assert enum is not None
        assert CommunicationDirectionType.ENUM_IN in enum.getEnumValues()
        assert CommunicationDirectionType.ENUM_OUT in enum.getEnumValues()

    def test_CommConnectorPort(self):
        """Test CommConnectorPort abstract class instantiation."""
        parent = MockParent()
        with pytest.raises(NotImplementedError):
            CommConnectorPort(parent, "test_comm_connector_port")

    def test_FramePort(self):
        """Test FramePort class functionality."""
        parent = MockParent()
        port = FramePort(parent, "test_frame_port")

        assert isinstance(port, Identifiable)

    def test_IPduSignalProcessingEnum(self):
        """Test IPduSignalProcessingEnum enum functionality."""
        # Check that both enum values exist
        assert hasattr(IPduSignalProcessingEnum, 'ENUM_DEFERRED')
        assert hasattr(IPduSignalProcessingEnum, 'ENUM_IMMEDIATE')

    def test_IPduPort(self):
        """Test IPduPort class functionality."""
        parent = MockParent()
        port = IPduPort(parent, "test_ipdu_port")

        assert isinstance(port, CommConnectorPort)

    def test_ISignalPort(self):
        """Test ISignalPort class functionality."""
        parent = MockParent()
        port = ISignalPort(parent, "test_isignal_port")

        assert isinstance(port, CommConnectorPort)

    def test_CommunicationConnector(self):
        """Test CommunicationConnector abstract class instantiation."""
        parent = MockParent()
        with pytest.raises(NotImplementedError):
            CommunicationConnector(parent, "test_communication_connector")