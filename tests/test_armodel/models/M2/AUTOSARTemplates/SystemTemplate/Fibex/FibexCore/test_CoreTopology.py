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
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanCommunication import CanFrameTriggering
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication import LinFrameTriggering, LinScheduleTable
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.NetworkEndpoint import NetworkEndpoint
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Flexray.FlexrayCommunication import FlexrayFrameTriggering
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import ISignalTriggering, PduTriggering


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


class Test_FibexCoreTopology:
    """Test cases for FibexCore Topology classes."""
    
    def test_CommunicationCycle(self):
        """Test CommunicationCycle abstract class functionality."""
        # Test that CommunicationCycle cannot be instantiated directly
        with pytest.raises(TypeError, match="CommunicationCycle is an abstract class"):
            CommunicationCycle()
        
        # Test that a concrete subclass can be instantiated
        cycle = CycleCounter()
        assert isinstance(cycle, ARObject)
        assert isinstance(cycle, CommunicationCycle)

    def test_CycleCounter(self):
        """Test CycleCounter class functionality."""
        counter = CycleCounter()

        assert isinstance(counter, CommunicationCycle)
        
        # Test default values
        assert counter.getCycleCounter() is None
        
        # Test setter/getter methods with method chaining - with None
        assert counter == counter.setCycleCounter(None)  # Test method chaining with None
        assert counter.getCycleCounter() is None  # Should remain None

        # Test setter/getter methods with method chaining - with actual value
        counter.setCycleCounter(10)
        assert counter.getCycleCounter() == 10
        assert counter == counter.setCycleCounter(10)  # Test method chaining

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

        # Test setter/getter methods with method chaining - with None
        assert repetition == repetition.setBaseCycle(None)  # Test method chaining with None
        assert repetition.getBaseCycle() is None  # Should remain None

        assert repetition == repetition.setCycleRepetition(None)  # Test method chaining with None
        assert repetition.getCycleRepetition() is None  # Should remain None

        # Test setter/getter methods with method chaining - with actual value
        repetition.setBaseCycle(5)
        assert repetition.getBaseCycle() == 5
        assert repetition == repetition.setBaseCycle(5)  # Test method chaining

        enum = CycleRepetitionType()
        repetition.setCycleRepetition(enum)
        assert repetition.getCycleRepetition() == enum
        assert repetition == repetition.setCycleRepetition(enum)  # Test method chaining

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

        # Test setter/getter methods with method chaining - with None
        assert channel == channel.setBusIdleTimeoutPeriod(None)  # Test method chaining with None
        assert channel.getBusIdleTimeoutPeriod() is None  # Should remain None

        # Test setter/getter methods with method chaining - with actual value
        period = 1000
        channel.setBusIdleTimeoutPeriod(period)
        assert channel.getBusIdleTimeoutPeriod() == period
        assert channel == channel.setBusIdleTimeoutPeriod(period)  # Test method chaining

        # Test schedule table creation
        schedule_table = channel.createLinScheduleTable("test_schedule")
        assert isinstance(schedule_table, LinScheduleTable)
        assert len(channel.getScheduleTables()) == 1

    def test_VlanConfig(self):
        """Test VlanConfig class functionality."""
        parent = MockParent()
        config = VlanConfig(parent, "test_vlan_config")

        assert isinstance(config, Identifiable)
        
        # Test default values
        assert config.getVlanIdentifier() is None
        
        # Test setter/getter methods with method chaining - with None
        assert config == config.setVlanIdentifier(None)  # Test method chaining with None
        assert config.getVlanIdentifier() is None  # Should remain None

        # Test setter/getter methods with method chaining - with actual value
        config.setVlanIdentifier(100)
        assert config.getVlanIdentifier() == 100
        assert config == config.setVlanIdentifier(100)  # Test method chaining

    def test_EthernetPhysicalChannel(self):
        """Test EthernetPhysicalChannel class functionality."""
        parent = MockParent()
        channel = EthernetPhysicalChannel(parent, "test_ethernet_physical_channel")

        assert isinstance(channel, PhysicalChannel)

        # Test default values
        assert channel.getNetworkEndpoints() == []
        assert channel.getSoAdConfig() is None
        assert channel.getVlan() is None

        # Test setter/getter methods with method chaining
        soad_config = object()
        channel.setSoAdConfig(soad_config)
        assert channel.getSoAdConfig() == soad_config
        assert channel == channel.setSoAdConfig(soad_config)  # Test method chaining

        # Test network endpoint creation
        endpoint = channel.createNetworkEndPoint("test_endpoint")
        assert isinstance(endpoint, NetworkEndpoint)
        assert len(channel.getNetworkEndpoints()) == 1

        # Test VLAN config creation
        vlan_config = channel.createVlanConfig("test_vlan")
        assert isinstance(vlan_config, VlanConfig)
        assert channel.getVlan() == vlan_config

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

        # Test default values
        assert channel.getChannelName() is None

        # Test setter/getter methods with method chaining - with None
        assert channel == channel.setChannelName(None)  # Test method chaining with None
        assert channel.getChannelName() is None  # Should remain None

        # Test setter/getter methods with method chaining - with actual value
        channel.setChannelName(FlexrayChannelName.CHANNEL_A)
        assert channel.getChannelName() == FlexrayChannelName.CHANNEL_A
        assert channel == channel.setChannelName(FlexrayChannelName.CHANNEL_A)  # Test method chaining

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

        # Test setter/getter methods with method chaining - with None
        assert recovery == recovery.setBorCounterL1ToL2(None)  # Test method chaining with None
        assert recovery.getBorCounterL1ToL2() is None  # Should remain None

        assert recovery == recovery.setBorTimeL1(None)  # Test method chaining with None
        assert recovery.getBorTimeL1() is None  # Should remain None

        assert recovery == recovery.setBorTimeL2(None)  # Test method chaining with None
        assert recovery.getBorTimeL2() is None  # Should remain None

        assert recovery == recovery.setBorTimeTxEnsured(None)  # Test method chaining with None
        assert recovery.getBorTimeTxEnsured() is None  # Should remain None

        assert recovery == recovery.setMainFunctionPeriod(None)  # Test method chaining with None
        assert recovery.getMainFunctionPeriod() is None  # Should remain None

        # Test setter/getter methods with method chaining - with actual values
        recovery.setBorCounterL1ToL2(5)
        assert recovery.getBorCounterL1ToL2() == 5
        assert recovery == recovery.setBorCounterL1ToL2(5)  # Test method chaining

        recovery.setBorTimeL1(1000)
        assert recovery.getBorTimeL1() == 1000
        assert recovery == recovery.setBorTimeL1(1000)  # Test method chaining

        recovery.setBorTimeL2(2000)
        assert recovery.getBorTimeL2() == 2000
        assert recovery == recovery.setBorTimeL2(2000)  # Test method chaining

        recovery.setBorTimeTxEnsured(3000)
        assert recovery.getBorTimeTxEnsured() == 3000
        assert recovery == recovery.setBorTimeTxEnsured(3000)  # Test method chaining

        recovery.setMainFunctionPeriod(4000)
        assert recovery.getMainFunctionPeriod() == 4000
        assert recovery == recovery.setMainFunctionPeriod(4000)  # Test method chaining

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

        # Test default values
        assert cluster.getBusOffRecovery() is None
        assert cluster.getCanFdBaudrate() is None
        assert cluster.getCanXlBaudrate() is None
        assert cluster.getSpeed() is None

        # Test setter/getter methods with method chaining
        recovery = CanClusterBusOffRecovery()
        cluster.setBusOffRecovery(recovery)
        assert cluster.getBusOffRecovery() == recovery
        assert cluster == cluster.setBusOffRecovery(recovery)  # Test method chaining

        cluster.setCanFdBaudrate(500000)
        assert cluster.getCanFdBaudrate() == 500000
        assert cluster == cluster.setCanFdBaudrate(500000)  # Test method chaining

        cluster.setCanXlBaudrate(10000000)
        assert cluster.getCanXlBaudrate() == 10000000
        assert cluster == cluster.setCanXlBaudrate(10000000)  # Test method chaining

        cluster.setSpeed(125000)
        assert cluster.getSpeed() == 125000
        assert cluster == cluster.setSpeed(125000)  # Test method chaining

    def test_LinCluster(self):
        """Test LinCluster class functionality."""
        parent = MockParent()
        cluster = LinCluster(parent, "test_lin_cluster")

        assert isinstance(cluster, CommunicationCluster)

        # Test default values
        assert cluster.getBaudrate() is None
        assert cluster.getProtocolName() is None
        assert cluster.getProtocolVersion() is None

        # Test setter/getter methods with method chaining
        cluster.setBaudrate(19200)
        assert cluster.getBaudrate() == 19200
        assert cluster == cluster.setBaudrate(19200)  # Test method chaining

        cluster.setProtocolName("LIN")
        assert cluster.getProtocolName() == "LIN"
        assert cluster == cluster.setProtocolName("LIN")  # Test method chaining

        cluster.setProtocolVersion("2.2")
        assert cluster.getProtocolVersion() == "2.2"
        assert cluster == cluster.setProtocolVersion("2.2")  # Test method chaining

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

        # Test default values
        assert port.getCommunicationDirection() is None

        # Test setter/getter methods with method chaining - with None
        assert port == port.setCommunicationDirection(None)  # Test method chaining with None
        assert port.getCommunicationDirection() is None  # Should remain None

        # Test setter/getter methods with method chaining - with actual value
        port.setCommunicationDirection(CommunicationDirectionType.ENUM_IN)
        assert port.getCommunicationDirection() == CommunicationDirectionType.ENUM_IN
        assert port == port.setCommunicationDirection(CommunicationDirectionType.ENUM_IN)  # Test method chaining

    def test_IPduSignalProcessingEnum(self):
        """Test IPduSignalProcessingEnum enum functionality."""
        # Check that both enum values exist
        assert hasattr(IPduSignalProcessingEnum, 'ENUM_DEFERRED')
        assert hasattr(IPduSignalProcessingEnum, 'ENUM_IMMEDIATE')
        assert IPduSignalProcessingEnum.ENUM_DEFERRED.value == "deferred"
        assert IPduSignalProcessingEnum.ENUM_IMMEDIATE.value == "immediate"

    def test_CommunicationController_methods(self):
        """Test CommunicationController concrete implementation methods."""
        class ConcreteCommunicationController(CommunicationController):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        parent = MockParent()
        controller = ConcreteCommunicationController(parent, "test_communication_controller")

        # Test default values
        assert controller.getWakeUpByControllerSupported() is None

        # Test setter/getter methods with method chaining - with None
        controller.setWakeUpByControllerSupported(None)
        assert controller.getWakeUpByControllerSupported() is None
        assert controller == controller.setWakeUpByControllerSupported(None)  # Test method chaining

        # Test setter/getter methods with method chaining - with actual value
        controller.setWakeUpByControllerSupported(True)
        assert controller.getWakeUpByControllerSupported() is True
        assert controller == controller.setWakeUpByControllerSupported(True)  # Test method chaining

    def test_IPduPort(self):
        """Test IPduPort class functionality."""
        parent = MockParent()
        port = IPduPort(parent, "test_ipdu_port")

        assert isinstance(port, CommConnectorPort)

        # Test default values
        assert port.getIPduSignalProcessing() is None
        assert port.getKeyId() is None
        assert port.getRxSecurityVerification() is None
        assert port.getTimestampRxAcceptanceWindow() is None
        assert port.getUseAuthDataFreshness() is None

        # Test setter/getter methods with method chaining - with None
        assert port == port.setIPduSignalProcessing(None)  # Test method chaining with None
        assert port.getIPduSignalProcessing() is None  # Should remain None

        assert port == port.setKeyId(None)  # Test method chaining with None
        assert port.getKeyId() is None  # Should remain None

        assert port == port.setRxSecurityVerification(None)  # Test method chaining with None
        assert port.getRxSecurityVerification() is None  # Should remain None

        assert port == port.setTimestampRxAcceptanceWindow(None)  # Test method chaining with None
        assert port.getTimestampRxAcceptanceWindow() is None  # Should remain None

        assert port == port.setUseAuthDataFreshness(None)  # Test method chaining with None
        assert port.getUseAuthDataFreshness() is None  # Should remain None

        # Test setter/getter methods with method chaining - with actual values
        port.setIPduSignalProcessing(IPduSignalProcessingEnum.ENUM_IMMEDIATE)
        assert port.getIPduSignalProcessing() == IPduSignalProcessingEnum.ENUM_IMMEDIATE
        assert port == port.setIPduSignalProcessing(IPduSignalProcessingEnum.ENUM_IMMEDIATE)  # Test method chaining

        port.setKeyId(1)
        assert port.getKeyId() == 1
        assert port == port.setKeyId(1)  # Test method chaining

        port.setRxSecurityVerification(True)
        assert port.getRxSecurityVerification() is True
        assert port == port.setRxSecurityVerification(True)  # Test method chaining

        port.setTimestampRxAcceptanceWindow(1000)
        assert port.getTimestampRxAcceptanceWindow() == 1000
        assert port == port.setTimestampRxAcceptanceWindow(1000)  # Test method chaining

        port.setUseAuthDataFreshness(False)
        assert port.getUseAuthDataFreshness() is False
        assert port == port.setUseAuthDataFreshness(False)  # Test method chaining

    def test_ISignalPort(self):
        """Test ISignalPort class functionality."""
        parent = MockParent()
        port = ISignalPort(parent, "test_isignal_port")

        assert isinstance(port, CommConnectorPort)

        # Test default values
        assert port.getDataFilter() is None
        assert port.getDdsQosProfileRef() is None
        assert port.getFirstTimeout() is None
        assert port.getHandleInvalid() is None
        assert port.getTimeout() is None

        # Test setter/getter methods with method chaining - with None
        assert port == port.setDataFilter(None)  # Test method chaining with None
        assert port.getDataFilter() is None  # Should remain None

        assert port == port.setDdsQosProfileRef(None)  # Test method chaining with None
        assert port.getDdsQosProfileRef() is None  # Should remain None

        assert port == port.setFirstTimeout(None)  # Test method chaining with None
        assert port.getFirstTimeout() is None  # Should remain None

        assert port == port.setHandleInvalid(None)  # Test method chaining with None
        assert port.getHandleInvalid() is None  # Should remain None

        assert port == port.setTimeout(None)  # Test method chaining with None
        assert port.getTimeout() is None  # Should remain None

        # Test setter/getter methods with method chaining - with actual values
        data_filter = object()
        port.setDataFilter(data_filter)
        assert port.getDataFilter() == data_filter
        assert port == port.setDataFilter(data_filter)  # Test method chaining

        ref = object()
        port.setDdsQosProfileRef(ref)
        assert port.getDdsQosProfileRef() == ref
        assert port == port.setDdsQosProfileRef(ref)  # Test method chaining

        port.setFirstTimeout(500)
        assert port.getFirstTimeout() == 500
        assert port == port.setFirstTimeout(500)  # Test method chaining

        port.setHandleInvalid("IGNORE")
        assert port.getHandleInvalid() == "IGNORE"
        assert port == port.setHandleInvalid("IGNORE")  # Test method chaining

        port.setTimeout(1000)
        assert port.getTimeout() == 1000
        assert port == port.setTimeout(1000)  # Test method chaining

    def test_CommunicationConnector(self):
        """Test CommunicationConnector abstract class instantiation."""
        parent = MockParent()
        with pytest.raises(NotImplementedError):
            CommunicationConnector(parent, "test_communication_connector")

    def test_PhysicalChannel_methods(self):
        """Test PhysicalChannel concrete implementation methods."""
        class ConcretePhysicalChannel(PhysicalChannel):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        parent = MockParent()
        channel = ConcretePhysicalChannel(parent, "test_physical_channel")

        # Test default values
        assert channel.getCommConnectorRefs() == []
        assert channel.getFrameTriggerings() == []
        assert channel.getISignalTriggerings() == []
        assert channel.getManagedPhysicalChannelRefs() == []
        assert channel.getPduTriggerings() == []

        # Test setter/getter methods with method chaining
        ref1 = object()
        channel.addCommConnectorRef(ref1)
        assert ref1 in channel.getCommConnectorRefs()
        assert channel == channel.addCommConnectorRef(ref1)  # Test method chaining

        ref2 = object()
        channel.addManagedPhysicalChannelRef(ref2)
        assert ref2 in channel.getManagedPhysicalChannelRefs()
        assert channel == channel.addManagedPhysicalChannelRef(ref2)  # Test method chaining

        # Test frame triggering creation methods
        can_triggering = channel.createCanFrameTriggering("can_triggering")
        assert isinstance(can_triggering, CanFrameTriggering)
        assert len(channel.getFrameTriggerings()) >= 1  # At least one triggering created

        lin_triggering = channel.createLinFrameTriggering("lin_triggering")
        assert isinstance(lin_triggering, LinFrameTriggering)
        assert len(channel.getFrameTriggerings()) >= 2  # Another triggering created

        flexray_triggering = channel.createFlexrayFrameTriggering("flexray_triggering")
        assert isinstance(flexray_triggering, FlexrayFrameTriggering)
        assert len(channel.getFrameTriggerings()) >= 3  # Another triggering created

        # Test ISignalTriggering creation
        isignal_triggering = channel.createISignalTriggering("isignal_triggering")
        assert isinstance(isignal_triggering, ISignalTriggering)
        assert len(channel.getISignalTriggerings()) >= 1  # At least one ISignalTriggering created

        # Test PduTriggering creation
        pdu_triggering = channel.createPduTriggering("pdu_triggering")
        assert isinstance(pdu_triggering, PduTriggering)
        assert len(channel.getPduTriggerings()) >= 1  # At least one PduTriggering created

    def test_CommunicationCluster_methods(self):
        """Test CommunicationCluster concrete implementation methods."""
        class ConcreteCommunicationCluster(CommunicationCluster):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        parent = MockParent()
        cluster = ConcreteCommunicationCluster(parent, "test_communication_cluster")

        # Test default values
        assert cluster.getBaudrate() is None
        assert cluster.getProtocolName() is None
        assert cluster.getProtocolVersion() is None
        assert cluster.getPhysicalChannels() == []

        # Test setter/getter methods with method chaining
        cluster.setBaudrate(500000)
        assert cluster.getBaudrate() == 500000
        assert cluster == cluster.setBaudrate(500000)  # Test method chaining

        cluster.setProtocolName("CAN")
        assert cluster.getProtocolName() == "CAN"
        assert cluster == cluster.setProtocolName("CAN")  # Test method chaining

        cluster.setProtocolVersion("2.0A")
        assert cluster.getProtocolVersion() == "2.0A"
        assert cluster == cluster.setProtocolVersion("2.0A")  # Test method chaining

        # Test physical channel creation methods
        can_channel = cluster.createCanPhysicalChannel("can_channel")
        assert isinstance(can_channel, CanPhysicalChannel)
        assert len(cluster.getPhysicalChannels()) >= 1  # At least one channel created
        assert len(cluster.getCanPhysicalChannels()) >= 1  # At least one CAN channel

        lin_channel = cluster.createLinPhysicalChannel("lin_channel")
        assert isinstance(lin_channel, LinPhysicalChannel)
        assert len(cluster.getPhysicalChannels()) >= 2  # Another channel created
        assert len(cluster.getLinPhysicalChannels()) >= 1  # At least one LIN channel

        eth_channel = cluster.createEthernetPhysicalChannel("eth_channel")
        assert isinstance(eth_channel, EthernetPhysicalChannel)
        assert len(cluster.getPhysicalChannels()) >= 3  # Another channel created
        assert len(cluster.getEthernetPhysicalChannels()) >= 1  # At least one Ethernet channel

        flexray_channel = cluster.createFlexrayPhysicalChannel("flexray_channel")
        assert isinstance(flexray_channel, FlexrayPhysicalChannel)
        assert len(cluster.getPhysicalChannels()) >= 4  # Another channel created

    def test_CommunicationConnector_methods(self):
        """Test CommunicationConnector concrete implementation methods."""
        class ConcreteCommunicationConnector(CommunicationConnector):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        parent = MockParent()
        connector = ConcreteCommunicationConnector(parent, "test_communication_connector")

        # Test default values
        assert connector.getCommControllerRef() is None
        assert connector.getCreateEcuWakeupSource() is None
        assert connector.getDynamicPncToChannelMappingEnabled() is None
        assert connector.getEcuCommPortInstances() == []
        assert connector.getPncFilterArrayMasks() == []
        assert connector.getPncGatewayType() is None

        # Test setter/getter methods with method chaining
        ref1 = object()
        connector.setCommControllerRef(ref1)
        assert connector.getCommControllerRef() == ref1
        assert connector == connector.setCommControllerRef(ref1)  # Test method chaining

        connector.setCreateEcuWakeupSource(True)
        assert connector.getCreateEcuWakeupSource() is True
        assert connector == connector.setCreateEcuWakeupSource(True)  # Test method chaining

        connector.setDynamicPncToChannelMappingEnabled(False)
        assert connector.getDynamicPncToChannelMappingEnabled() is False
        assert connector == connector.setDynamicPncToChannelMappingEnabled(False)  # Test method chaining

        connector.setPncGatewayType(PncGatewayTypeEnum.ENUM_ACTIVE)
        assert connector.getPncGatewayType() == PncGatewayTypeEnum.ENUM_ACTIVE
        assert connector == connector.setPncGatewayType(PncGatewayTypeEnum.ENUM_ACTIVE)  # Test method chaining

        # Test PNC filter array mask methods
        connector.addPncFilterArrayMask(0xFF)
        assert 0xFF in connector.getPncFilterArrayMasks()
        assert connector == connector.addPncFilterArrayMask(0xFF)  # Test method chaining

        # Test port creation methods
        frame_port = connector.createFramePort("frame_port")
        assert isinstance(frame_port, FramePort)
        assert len(connector.getEcuCommPortInstances()) >= 1  # At least one port created

        ipdu_port = connector.createIPduPort("ipdu_port")
        assert isinstance(ipdu_port, IPduPort)
        assert len(connector.getEcuCommPortInstances()) >= 2  # Another port created

        isignal_port = connector.createISignalPort("isignal_port")
        assert isinstance(isignal_port, ISignalPort)
        assert len(connector.getEcuCommPortInstances()) >= 3  # Another port created