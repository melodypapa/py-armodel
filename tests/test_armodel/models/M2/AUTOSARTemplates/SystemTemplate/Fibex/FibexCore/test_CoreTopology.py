import typing

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, TimeValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanCommunication import CanFrameTriggering
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.NetworkEndpoint import NetworkEndpoint
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Flexray.FlexrayCommunication import FlexrayFrameTriggering
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication import LinFrameTriggering, LinScheduleTable
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (
    CommConnectorPort,
    CommunicationDirectionType,
    FramePort,
    IPduPort,
    IPduSignalProcessingEnum,
    ISignalPort,
    ISignalTriggering,
    PduTriggering,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import (
    AbstractCanCluster,
    AbstractCanPhysicalChannel,
    CanCluster,
    CanClusterBusOffRecovery,
    CanPhysicalChannel,
    CommunicationCluster,
    CommunicationConnector,
    CommunicationController,
    CommunicationCycle,
    CycleCounter,
    CycleRepetition,
    CycleRepetitionType,
    EthernetPhysicalChannel,
    FlexrayChannelName,
    FlexrayPhysicalChannel,
    LinPhysicalChannel,
    PhysicalChannel,
    PncGatewayTypeEnum,
    VlanConfig,
)


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
        with pytest.raises(TypeError):
            PhysicalChannel(parent, "test_physical_channel")

    def test_AbstractCanPhysicalChannel(self):
        """Test AbstractCanPhysicalChannel abstract class instantiation."""
        parent = MockParent()
        with pytest.raises(TypeError):
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
        with pytest.raises(TypeError):
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
        with pytest.raises(TypeError):
            AbstractCanCluster(parent, "test_abstract_can_cluster")

        # Verify inherited accessors via a concrete subclass (CanCluster).
        cluster = CanCluster(parent, "test_can_cluster_base")

        assert cluster.getBusOffRecovery() is None
        assert cluster.getCanFdBaudrate() is None
        assert cluster.getCanXlBaudrate() is None
        assert not hasattr(cluster, "getSpeed")  # no fabricated SPEED member (Rule 0001.3)

        recovery = CanClusterBusOffRecovery()
        assert cluster == cluster.setBusOffRecovery(recovery)
        assert cluster.getBusOffRecovery() == recovery

        assert cluster == cluster.setCanFdBaudrate(500000)
        assert cluster.getCanFdBaudrate() == 500000
        assert cluster == cluster.setCanXlBaudrate(10000000)
        assert cluster.getCanXlBaudrate() == 10000000

    def test_CanCluster(self):
        """Test CanCluster class functionality."""
        parent = MockParent()
        cluster = CanCluster(parent, "test_can_cluster")

        assert isinstance(cluster, AbstractCanCluster)
        assert isinstance(cluster, CommunicationCluster)

        # Test default values
        assert cluster.getBusOffRecovery() is None
        assert cluster.getCanFdBaudrate() is None
        assert cluster.getCanXlBaudrate() is None

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

    def test_CommunicationController(self):
        """Test CommunicationController abstract class instantiation."""
        parent = MockParent()
        with pytest.raises(TypeError):
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
        with pytest.raises(TypeError):
            CommConnectorPort(parent, "test_comm_connector_port")

    def test_CommConnectorPort_base_properties(self):
        parent = MockParent()
        port = FramePort(parent, "test_frame_port")

        assert isinstance(port, CommConnectorPort)

        # Test default values
        assert port.getCommunicationDirection() is None

        # Test setter/getter methods with method chaining - with actual value
        direction = CommunicationDirectionType()
        direction.setValue(CommunicationDirectionType.ENUM_IN)
        assert port == port.setCommunicationDirection(direction)
        assert port.getCommunicationDirection() == direction

        # Test None no-op (guarded setter must not overwrite an existing value)
        assert port == port.setCommunicationDirection(None)
        assert port.getCommunicationDirection() == direction

        # Test 0..1 Optional typing contract (getter/setter agree on Optional[T])
        hints = typing.get_type_hints(FramePort.getCommunicationDirection)
        assert hints["return"] == typing.Optional[CommunicationDirectionType]
        hints = typing.get_type_hints(FramePort.setCommunicationDirection)
        assert hints["value"] == typing.Optional[CommunicationDirectionType]
        assert hints["return"] == CommConnectorPort

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
        direction = CommunicationDirectionType()
        direction.setValue(CommunicationDirectionType.ENUM_IN)
        port.setCommunicationDirection(direction)
        assert port.getCommunicationDirection() == direction
        assert port == port.setCommunicationDirection(direction)  # Test method chaining

    def test_IPduSignalProcessingEnum(self):
        """Test IPduSignalProcessingEnum enum functionality."""
        enum = IPduSignalProcessingEnum()
        assert enum is not None
        assert IPduSignalProcessingEnum.ENUM_DEFERRED in enum.getEnumValues()
        assert IPduSignalProcessingEnum.ENUM_IMMEDIATE in enum.getEnumValues()
        assert IPduSignalProcessingEnum.ENUM_DEFERRED == "deferred"
        assert IPduSignalProcessingEnum.ENUM_IMMEDIATE == "immediate"

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

        # Test None no-op (guarded setter must not overwrite an existing value)
        controller.setWakeUpByControllerSupported(True)
        assert controller == controller.setWakeUpByControllerSupported(None)
        assert controller.getWakeUpByControllerSupported() is True  # Should remain unchanged

    def test_IPduPort(self):
        """Test IPduPort class functionality."""
        parent = MockParent()
        port = IPduPort(parent, "test_ipdu_port")

        assert isinstance(port, CommConnectorPort)

        # Test default values
        assert port.getIPduSignalProcessing() is None
        assert port.getRxSecurityVerification() is None
        assert port.getTimestampRxAcceptanceWindow() is None
        assert port.getUseAuthDataFreshness() is None

        # keyId is removed upstream (atp.Status="removed") and must not be modeled
        assert not hasattr(port, "keyId")
        assert not hasattr(port, "getKeyId")
        assert not hasattr(port, "setKeyId")

        # Test setter/getter methods with method chaining - with actual values
        processing = IPduSignalProcessingEnum()
        processing.setValue(IPduSignalProcessingEnum.ENUM_IMMEDIATE)
        assert port == port.setIPduSignalProcessing(processing)
        assert port.getIPduSignalProcessing() == processing

        rx_security = Boolean()
        rx_security.setValue(True)
        assert port == port.setRxSecurityVerification(rx_security)
        assert port.getRxSecurityVerification().getValue() is True

        window = TimeValue()
        window.setValue("0.05")
        assert port == port.setTimestampRxAcceptanceWindow(window)
        assert float(port.getTimestampRxAcceptanceWindow().getValue()) == 0.05

        use_auth = Boolean()
        use_auth.setValue(False)
        assert port == port.setUseAuthDataFreshness(use_auth)
        assert port.getUseAuthDataFreshness().getValue() is False

        # Test None no-op (guarded setters must not overwrite existing values)
        assert port == port.setIPduSignalProcessing(None)
        assert port.getIPduSignalProcessing() == processing
        assert port == port.setRxSecurityVerification(None)
        assert port.getRxSecurityVerification().getValue() is True
        assert port == port.setTimestampRxAcceptanceWindow(None)
        assert float(port.getTimestampRxAcceptanceWindow().getValue()) == 0.05
        assert port == port.setUseAuthDataFreshness(None)
        assert port.getUseAuthDataFreshness().getValue() is False

        # Test 0..1 Optional typing contract (getter/setter agree on Optional[T])
        hints = typing.get_type_hints(IPduPort.getIPduSignalProcessing)
        assert hints["return"] == typing.Optional[IPduSignalProcessingEnum]
        hints = typing.get_type_hints(IPduPort.setIPduSignalProcessing)
        assert hints["value"] == typing.Optional[IPduSignalProcessingEnum]
        assert hints["return"] == IPduPort

        for getter, setter, value_type in [
            ("getRxSecurityVerification", "setRxSecurityVerification", Boolean),
            ("getTimestampRxAcceptanceWindow", "setTimestampRxAcceptanceWindow", TimeValue),
            ("getUseAuthDataFreshness", "setUseAuthDataFreshness", Boolean),
        ]:
            hints = typing.get_type_hints(getattr(IPduPort, getter))
            assert hints["return"] == typing.Optional[value_type]
            hints = typing.get_type_hints(getattr(IPduPort, setter))
            assert hints["value"] == typing.Optional[value_type]
            assert hints["return"] == IPduPort

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
        with pytest.raises(TypeError):
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

        # Test None no-op (guarded setters must not overwrite an existing value)
        assert cluster == cluster.setBaudrate(None)
        assert cluster.getBaudrate() == 500000  # Should remain unchanged
        assert cluster == cluster.setProtocolName(None)
        assert cluster.getProtocolName() == "CAN"  # Should remain unchanged
        assert cluster == cluster.setProtocolVersion(None)
        assert cluster.getProtocolVersion() == "2.0A"  # Should remain unchanged

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
