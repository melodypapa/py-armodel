import typing

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, TimeValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanCommunication import CanFrameTriggering
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology import (
    AbstractCanPhysicalChannel,
    CanCommunicationConnector,
    CanCommunicationController,
    CanPhysicalChannel,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import EthernetCommunicationConnector, EthernetCommunicationController, NetworkEndpoint
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Flexray.FlexrayCommunication import FlexrayFrameTriggering
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Flexray.FlexrayTopology import FlexrayCommunicationConnector, FlexrayCommunicationController
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication import LinFrameTriggering, LinScheduleTable
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinTopology import LinCommunicationConnector, LinMaster
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (
    CommConnectorPort,
    CommunicationDirectionType,
    FibexElement,
    FramePort,
    IPduPort,
    IPduSignalProcessingEnum,
    ISignalPort,
    ISignalTriggering,
    PduTriggering,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import (
    AbstractCanCluster,
    CanCluster,
    CanClusterBusOffRecovery,
    CommunicationCluster,
    CommunicationConnector,
    CommunicationController,
    CommunicationCycle,
    CycleCounter,
    CycleRepetition,
    CycleRepetitionType,
    EcuInstance,
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


def _assert_return_is(hints: dict, expected: type):
    # On Python 3.8 a module with `from __future__ import annotations` leaves
    # bare-name forward references unresolved in get_type_hints results.
    hint = hints["return"]
    if isinstance(hint, typing.ForwardRef):
        assert hint.__forward_arg__ == expected.__name__
    else:
        assert hint == expected


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
        """Test CanPhysicalChannel class functionality (Table 3.21)."""
        parent = MockParent()
        channel = CanPhysicalChannel(parent, "test_can_physical_channel")

        assert isinstance(channel, PhysicalChannel)
        assert isinstance(channel, AbstractCanPhysicalChannel)

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
        # localns is required because CommunicationDirectionType lives in CoreCommunication
        # (spec package) while CommConnectorPort lives in CoreTopology - a runtime import
        # there would create a circular import.
        localns = {"CommunicationDirectionType": CommunicationDirectionType}
        hints = typing.get_type_hints(FramePort.getCommunicationDirection, localns=localns)
        assert hints["return"] == typing.Optional[CommunicationDirectionType]
        hints = typing.get_type_hints(FramePort.setCommunicationDirection, localns=localns)
        assert hints["value"] == typing.Optional[CommunicationDirectionType]
        _assert_return_is(hints, CommConnectorPort)

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
        _assert_return_is(hints, IPduPort)

        for getter, setter, value_type in [
            ("getRxSecurityVerification", "setRxSecurityVerification", Boolean),
            ("getTimestampRxAcceptanceWindow", "setTimestampRxAcceptanceWindow", TimeValue),
            ("getUseAuthDataFreshness", "setUseAuthDataFreshness", Boolean),
        ]:
            hints = typing.get_type_hints(getattr(IPduPort, getter))
            assert hints["return"] == typing.Optional[value_type]
            hints = typing.get_type_hints(getattr(IPduPort, setter))
            assert hints["value"] == typing.Optional[value_type]
            _assert_return_is(hints, IPduPort)

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

    def test_PhysicalChannel_spec_attributes(self):
        """Test PhysicalChannel spec attributes (Table 3.7) per Rule 0001."""

        class ConcretePhysicalChannel(PhysicalChannel):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        parent = MockParent()
        channel = ConcretePhysicalChannel(parent, "test_physical_channel")

        # commConnector (ref, CommunicationConnector, *)
        assert channel.getCommConnectorRefs() == []
        ref1 = object()
        channel.addCommConnectorRef(ref1)
        assert ref1 in channel.getCommConnectorRefs()
        assert channel == channel.addCommConnectorRef(ref1)  # chaining

        # managedPhysicalChannel (ref, PhysicalChannel, *)
        assert channel.getManagedPhysicalChannelRefs() == []
        ref2 = object()
        channel.addManagedPhysicalChannelRef(ref2)
        assert ref2 in channel.getManagedPhysicalChannelRefs()
        assert channel == channel.addManagedPhysicalChannelRef(ref2)  # chaining

        # frameTriggering (aggr, FrameTriggering, *) -> dedicated list
        assert channel.getFrameTriggerings() == []
        can_triggering = channel.createCanFrameTriggering("can_triggering")
        assert isinstance(can_triggering, CanFrameTriggering)
        assert can_triggering in channel.getFrameTriggerings()
        lin_triggering = channel.createLinFrameTriggering("lin_triggering")
        assert isinstance(lin_triggering, LinFrameTriggering)
        assert len(channel.getFrameTriggerings()) == 2

        # iSignalTriggering (aggr, ISignalTriggering, *) -> dedicated list
        assert channel.getISignalTriggerings() == []
        isignal_triggering = channel.createISignalTriggering("isignal_triggering")
        assert isinstance(isignal_triggering, ISignalTriggering)
        assert isignal_triggering in channel.getISignalTriggerings()

        # pduTriggering (aggr, PduTriggering, *) -> dedicated list
        assert channel.getPduTriggerings() == []
        pdu_triggering = channel.createPduTriggering("pdu_triggering")
        assert isinstance(pdu_triggering, PduTriggering)
        assert pdu_triggering in channel.getPduTriggerings()

    def test_CommunicationConnector_methods(self):
        """Test CommunicationConnector concrete implementation methods (Table 3.4)."""

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

        # commController (ref, CommunicationController, 0..1)
        ref1 = object()
        connector.setCommControllerRef(ref1)
        assert connector.getCommControllerRef() == ref1
        assert connector == connector.setCommControllerRef(ref1)  # method chaining
        assert connector == connector.setCommControllerRef(None)  # None no-op
        assert connector.getCommControllerRef() == ref1  # unchanged

        # createEcuWakeupSource (attr, Boolean, 0..1)
        connector.setCreateEcuWakeupSource(True)
        assert connector.getCreateEcuWakeupSource().getValue() is True
        assert connector == connector.setCreateEcuWakeupSource(True)  # method chaining
        assert connector == connector.setCreateEcuWakeupSource(None)  # None no-op
        assert connector.getCreateEcuWakeupSource().getValue() is True  # unchanged

        # dynamicPncToChannelMappingEnabled (attr, Boolean, 0..1)
        connector.setDynamicPncToChannelMappingEnabled(False)
        assert connector.getDynamicPncToChannelMappingEnabled().getValue() is False
        assert connector == connector.setDynamicPncToChannelMappingEnabled(False)  # method chaining
        assert connector == connector.setDynamicPncToChannelMappingEnabled(None)  # None no-op
        assert connector.getDynamicPncToChannelMappingEnabled().getValue() is False  # unchanged

        # pncGatewayType (attr, PncGatewayTypeEnum, 0..1)
        connector.setPncGatewayType(PncGatewayTypeEnum.ENUM_ACTIVE)
        assert connector.getPncGatewayType() == PncGatewayTypeEnum.ENUM_ACTIVE
        assert connector == connector.setPncGatewayType(PncGatewayTypeEnum.ENUM_ACTIVE)  # method chaining
        assert connector == connector.setPncGatewayType(None)  # None no-op
        assert connector.getPncGatewayType() == PncGatewayTypeEnum.ENUM_ACTIVE  # unchanged

        # pncFilterArrayMask (ordered, attr, PositiveInteger, *)
        connector.addPncFilterArrayMask(0xFF)
        connector.addPncFilterArrayMask(0x01)
        assert connector.getPncFilterArrayMasks() == [0xFF, 0x01]  # ordered
        assert connector == connector.addPncFilterArrayMask(0x01)  # method chaining

        # ecuCommPortInstance (aggr, CommConnectorPort, *) -> dedicated typed list
        frame_port = connector.createFramePort("frame_port")
        assert isinstance(frame_port, FramePort)
        assert frame_port in connector.getEcuCommPortInstances()
        assert len(connector.getEcuCommPortInstances()) == 1  # exactly one port

        ipdu_port = connector.createIPduPort("ipdu_port")
        assert isinstance(ipdu_port, IPduPort)
        assert ipdu_port in connector.getEcuCommPortInstances()
        assert len(connector.getEcuCommPortInstances()) == 2

        isignal_port = connector.createISignalPort("isignal_port")
        assert isinstance(isignal_port, ISignalPort)
        assert isignal_port in connector.getEcuCommPortInstances()
        assert len(connector.getEcuCommPortInstances()) == 3

        # createXxx returns the existing element on duplicate short name
        dup = connector.createFramePort("frame_port")
        assert dup is frame_port
        assert len(connector.getEcuCommPortInstances()) == 3  # no duplicate


class Test_FibexCoreEcuInstance:
    """Test cases for FibexCore EcuInstance class."""

    def test_EcuInstance(self):
        """Test EcuInstance class functionality."""
        parent = MockParent()
        ecu = EcuInstance(parent, "test_ecu_instance")

        assert isinstance(ecu, FibexElement)

        # Test default values
        assert ecu.getAssociatedComIPduGroupRefs() == []
        assert ecu.getAssociatedConsumedProvidedServiceInstanceGroupRefs() == []
        assert ecu.getAssociatedPdurIPduGroupRefs() == []
        assert ecu.getChannelSynchronousWakeup() is None
        assert ecu.getClientIdRange() is None
        assert ecu.getComConfigurationGwTimeBase() is None
        assert ecu.getComConfigurationRxTimeBase() is None
        assert ecu.getComConfigurationTxTimeBase() is None
        assert ecu.getComEnableMDTForCyclicTransmission() is None
        assert ecu.getCommControllers() == []
        assert ecu.getConnectors() == []
        assert ecu.getDltConfig() is None
        assert ecu.getDoIpConfig() is None
        assert ecu.getEcuTaskProxyRefs() == []
        assert ecu.getEthSwitchPortGroupDerivation() is None
        assert ecu.getFirewallRuleRefs() == []
        assert ecu.getPartitions() == []
        assert ecu.getPncNmRequest() is None
        assert ecu.getPncPrepareSleepTimer() is None
        assert ecu.getPncSynchronousWakeup() is None
        assert ecu.getPnResetTime() is None
        assert ecu.getSleepModeSupported() is None
        assert ecu.getTcpIpIcmpPropsRef() is None
        assert ecu.getTcpIpPropsRef() is None
        assert ecu.getV2xSupported() is None
        assert ecu.getWakeUpOverBusSupported() is None

    def test_EcuInstance_setters_with_none_handling(self):
        """Test EcuInstance setter methods with None values and method chaining."""
        parent = MockParent()
        ecu = EcuInstance(parent, "test_ecu_instance")

        # Test setter/getter methods with method chaining - with None values
        assert ecu == ecu.setChannelSynchronousWakeup(None)
        assert ecu.getChannelSynchronousWakeup() is None

        assert ecu == ecu.setClientIdRange(None)
        assert ecu.getClientIdRange() is None

        assert ecu == ecu.setComConfigurationGwTimeBase(None)
        assert ecu.getComConfigurationGwTimeBase() is None

        assert ecu == ecu.setComConfigurationRxTimeBase(None)
        assert ecu.getComConfigurationRxTimeBase() is None

        assert ecu == ecu.setComConfigurationTxTimeBase(None)
        assert ecu.getComConfigurationTxTimeBase() is None

        assert ecu == ecu.setComEnableMDTForCyclicTransmission(None)
        assert ecu.getComEnableMDTForCyclicTransmission() is None

        assert ecu == ecu.setDltConfig(None)
        assert ecu.getDltConfig() is None

        assert ecu == ecu.setDoIpConfig(None)
        assert ecu.getDoIpConfig() is None

        assert ecu.getEcuTaskProxyRefs() == []

        assert ecu == ecu.setEthSwitchPortGroupDerivation(None)
        assert ecu.getEthSwitchPortGroupDerivation() is None

        assert ecu.getFirewallRuleRefs() == []

        assert ecu == ecu.setPncNmRequest(None)
        assert ecu.getPncNmRequest() is None

        assert ecu == ecu.setPncPrepareSleepTimer(None)
        assert ecu.getPncPrepareSleepTimer() is None

        assert ecu == ecu.setPncSynchronousWakeup(None)
        assert ecu.getPncSynchronousWakeup() is None

        assert ecu == ecu.setPnResetTime(None)
        assert ecu.getPnResetTime() is None

        assert ecu == ecu.setSleepModeSupported(None)
        assert ecu.getSleepModeSupported() is None

        assert ecu == ecu.setTcpIpIcmpPropsRef(None)
        assert ecu.getTcpIpIcmpPropsRef() is None

        assert ecu == ecu.setTcpIpPropsRef(None)
        assert ecu.getTcpIpPropsRef() is None

        assert ecu == ecu.setV2xSupported(None)
        assert ecu.getV2xSupported() is None

        assert ecu == ecu.setWakeUpOverBusSupported(None)
        assert ecu.getWakeUpOverBusSupported() is None

    def test_EcuInstance_setters_with_actual_values(self):
        """Test EcuInstance setter methods with actual values and method chaining."""
        parent = MockParent()
        ecu = EcuInstance(parent, "test_ecu_instance")

        # Test setter/getter methods with method chaining - with actual values
        ecu.setChannelSynchronousWakeup(True)
        assert ecu.getChannelSynchronousWakeup() is True
        assert ecu == ecu.setChannelSynchronousWakeup(True)

        ecu.setClientIdRange("client_range")
        assert ecu.getClientIdRange() == "client_range"
        assert ecu == ecu.setClientIdRange("client_range")

        ecu.setComConfigurationGwTimeBase(100)
        assert ecu.getComConfigurationGwTimeBase() == 100
        assert ecu == ecu.setComConfigurationGwTimeBase(100)

        ecu.setComConfigurationRxTimeBase(200)
        assert ecu.getComConfigurationRxTimeBase() == 200
        assert ecu == ecu.setComConfigurationRxTimeBase(200)

        ecu.setComConfigurationTxTimeBase(300)
        assert ecu.getComConfigurationTxTimeBase() == 300
        assert ecu == ecu.setComConfigurationTxTimeBase(300)

        ecu.setComEnableMDTForCyclicTransmission(False)
        assert ecu.getComEnableMDTForCyclicTransmission() is False
        assert ecu == ecu.setComEnableMDTForCyclicTransmission(False)

        ecu.setDltConfig("dlt_config_value")
        assert ecu.getDltConfig() == "dlt_config_value"
        assert ecu == ecu.setDltConfig("dlt_config_value")

        ecu.setDoIpConfig("doip_config_value")
        assert ecu.getDoIpConfig() == "doip_config_value"
        assert ecu == ecu.setDoIpConfig("doip_config_value")

        ecu.addEcuTaskProxyRef("task1")
        ecu.addEcuTaskProxyRef("task2")
        assert ecu.getEcuTaskProxyRefs() == ["task1", "task2"]
        assert ecu == ecu.addEcuTaskProxyRef("task3")

        ecu.setEthSwitchPortGroupDerivation(True)
        assert ecu.getEthSwitchPortGroupDerivation() is True
        assert ecu == ecu.setEthSwitchPortGroupDerivation(True)

        ecu.addFirewallRuleRef("firewall_rule")
        ecu.addFirewallRuleRef("firewall_rule2")
        assert ecu.getFirewallRuleRefs() == ["firewall_rule", "firewall_rule2"]
        assert ecu == ecu.addFirewallRuleRef("firewall_rule3")

        ecu.setPncNmRequest(True)
        assert ecu.getPncNmRequest() is True
        assert ecu == ecu.setPncNmRequest(True)

        ecu.setPncPrepareSleepTimer(500)
        assert ecu.getPncPrepareSleepTimer() == 500
        assert ecu == ecu.setPncPrepareSleepTimer(500)

        ecu.setPncSynchronousWakeup(False)
        assert ecu.getPncSynchronousWakeup() is False
        assert ecu == ecu.setPncSynchronousWakeup(False)

        ecu.setPnResetTime(600)
        assert ecu.getPnResetTime() == 600
        assert ecu == ecu.setPnResetTime(600)

        ecu.setSleepModeSupported(True)
        assert ecu.getSleepModeSupported() is True
        assert ecu == ecu.setSleepModeSupported(True)

        ecu.setTcpIpIcmpPropsRef("tcpip_icmp")
        assert ecu.getTcpIpIcmpPropsRef() == "tcpip_icmp"
        assert ecu == ecu.setTcpIpIcmpPropsRef("tcpip_icmp")

        ecu.setTcpIpPropsRef("tcpip")
        assert ecu.getTcpIpPropsRef() == "tcpip"
        assert ecu == ecu.setTcpIpPropsRef("tcpip")

        ecu.setV2xSupported(True)
        assert ecu.getV2xSupported() is True
        assert ecu == ecu.setV2xSupported(True)

        ecu.setWakeUpOverBusSupported(False)
        assert ecu.getWakeUpOverBusSupported() is False
        assert ecu == ecu.setWakeUpOverBusSupported(False)

    def test_EcuInstance_add_methods(self):
        """Test EcuInstance add methods with method chaining."""
        parent = MockParent()
        ecu = EcuInstance(parent, "test_ecu_instance")

        # Test addAssociatedComIPduGroupRef with method chaining
        ecu.addAssociatedComIPduGroupRef("com_ipdu_ref")
        assert "com_ipdu_ref" in ecu.getAssociatedComIPduGroupRefs()
        assert ecu == ecu.addAssociatedComIPduGroupRef("com_ipdu_ref2")
        assert len(ecu.getAssociatedComIPduGroupRefs()) == 2

        # Test addAssociatedConsumedProvidedServiceInstanceGroupRef with method chaining
        ecu.addAssociatedConsumedProvidedServiceInstanceGroupRef("service_instance_ref")
        assert "service_instance_ref" in ecu.getAssociatedConsumedProvidedServiceInstanceGroupRefs()
        assert ecu == ecu.addAssociatedConsumedProvidedServiceInstanceGroupRef("service_instance_ref2")
        assert len(ecu.getAssociatedConsumedProvidedServiceInstanceGroupRefs()) == 2

        # Test addAssociatedPdurIPduGroupRef with method chaining
        ecu.addAssociatedPdurIPduGroupRef("pdur_ipdu_ref")
        assert "pdur_ipdu_ref" in ecu.getAssociatedPdurIPduGroupRefs()
        assert ecu == ecu.addAssociatedPdurIPduGroupRef("pdur_ipdu_ref2")
        assert len(ecu.getAssociatedPdurIPduGroupRefs()) == 2

        # Test addPartition with method chaining
        ecu.addPartition("partition_value")
        assert "partition_value" in ecu.getPartitions()
        assert ecu == ecu.addPartition("partition_value2")
        assert len(ecu.getPartitions()) == 2

        # Test addEcuTaskProxyRef with method chaining
        ecu.addEcuTaskProxyRef("task1")
        assert "task1" in ecu.getEcuTaskProxyRefs()
        assert ecu == ecu.addEcuTaskProxyRef("task2")
        assert len(ecu.getEcuTaskProxyRefs()) == 2

        # Test addFirewallRuleRef with method chaining
        ecu.addFirewallRuleRef("firewall_rule")
        assert "firewall_rule" in ecu.getFirewallRuleRefs()
        assert ecu == ecu.addFirewallRuleRef("firewall_rule2")
        assert len(ecu.getFirewallRuleRefs()) == 2

    def test_EcuInstance_create_methods(self):
        """Test EcuInstance create methods for communication controllers and connectors."""
        parent = MockParent()
        ecu = EcuInstance(parent, "test_ecu_instance")

        # Test createCanCommunicationController
        controller = ecu.createCanCommunicationController("can_controller_1")
        assert isinstance(controller, CanCommunicationController)
        assert controller.getShortName() == "can_controller_1"
        assert controller in ecu.getCommControllers()

        # Test createEthernetCommunicationController
        eth_controller = ecu.createEthernetCommunicationController("eth_controller_1")
        assert isinstance(eth_controller, EthernetCommunicationController)
        assert eth_controller.getShortName() == "eth_controller_1"
        assert eth_controller in ecu.getCommControllers()

        # Test createLinMaster
        lin_controller = ecu.createLinMaster("lin_controller_1")
        assert isinstance(lin_controller, LinMaster)
        assert lin_controller.getShortName() == "lin_controller_1"
        assert lin_controller in ecu.getCommControllers()

        # Test createFlexrayCommunicationController
        flex_controller = ecu.createFlexrayCommunicationController("flex_controller_1")
        assert isinstance(flex_controller, FlexrayCommunicationController)
        assert flex_controller.getShortName() == "flex_controller_1"
        assert flex_controller in ecu.getCommControllers()

        # Test createCanCommunicationConnector
        connector = ecu.createCanCommunicationConnector("can_connector_1")
        assert isinstance(connector, CanCommunicationConnector)
        assert connector.getShortName() == "can_connector_1"
        assert connector in ecu.getConnectors()

        # Test createEthernetCommunicationConnector
        eth_connector = ecu.createEthernetCommunicationConnector("eth_connector_1")
        assert isinstance(eth_connector, EthernetCommunicationConnector)
        assert eth_connector.getShortName() == "eth_connector_1"
        assert eth_connector in ecu.getConnectors()

        # Test createLinCommunicationConnector
        lin_connector = ecu.createLinCommunicationConnector("lin_connector_1")
        assert isinstance(lin_connector, LinCommunicationConnector)
        assert lin_connector.getShortName() == "lin_connector_1"
        assert lin_connector in ecu.getConnectors()

        # Test createFlexrayCommunicationConnector
        flex_connector = ecu.createFlexrayCommunicationConnector("flex_connector_1")
        assert isinstance(flex_connector, FlexrayCommunicationConnector)
        assert flex_connector.getShortName() == "flex_connector_1"
        assert flex_connector in ecu.getConnectors()
