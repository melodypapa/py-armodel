import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, Integer, RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement import (
    BusspecificNmEcu,
    CanNmCluster,
    CanNmClusterCoupling,
    CanNmEcu,
    CanNmNode,
    FlexrayNmCluster,
    FlexrayNmClusterCoupling,
    FlexrayNmEcu,
    FlexrayNmNode,
    J1939NmAddressConfigurationCapabilityEnum,
    J1939NmCluster,
    J1939NmEcu,
    J1939NmNode,
    J1939NodeName,
    NmClusterCoupling,
    NmConfig,
    NmCoordinatorRoleEnum,
    NmEcu,
    NmNode,
    UdpNmCluster,
    UdpNmClusterCoupling,
    UdpNmEcu,
    UdpNmNode,
)


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


class TestNetworkManagement:
    """
    Test class for NetworkManagement module functionality.
    This class contains test methods for validating the behavior of
    network management classes, including their initialization,
    inheritance relationships, and property accessors.
    """

    def test_nm_cluster_coupling_abstract(self):
        """
        Test NmClusterCoupling abstract class functionality.
        """
        with pytest.raises(TypeError):
            NmClusterCoupling()

    def test_can_nm_cluster_coupling(self):
        """
        Test CanNmClusterCoupling class functionality with method chaining and None handling.
        """
        coupling = CanNmClusterCoupling()

        # Test constructor
        assert coupling is not None

        # Test default values
        assert coupling.getCoupledClusterRefs() == []
        assert coupling.getNmBusloadReductionEnabled() is None
        assert coupling.getNmImmediateRestartEnabled() is None

        # Test setter/getter methods with method chaining
        coupling.setNmBusloadReductionEnabled(True)
        assert coupling.getNmBusloadReductionEnabled() is True
        assert coupling == coupling.setNmBusloadReductionEnabled(True)

        coupling.setNmImmediateRestartEnabled(False)
        assert coupling.getNmImmediateRestartEnabled() is False
        assert coupling == coupling.setNmImmediateRestartEnabled(False)

        # Test addCoupledClusterRef
        coupling.addCoupledClusterRef("cluster_ref")
        assert "cluster_ref" in coupling.getCoupledClusterRefs()
        assert coupling == coupling.addCoupledClusterRef("cluster_ref2")

    def test_flexray_nm_cluster_coupling(self):
        """
        Test FlexrayNmClusterCoupling class functionality with method chaining and None handling.
        """
        coupling = FlexrayNmClusterCoupling()

        # Test constructor
        assert coupling is not None

        # Test default values
        assert coupling.getCoupledClusterRefs() == []
        assert coupling.getNmScheduleVariant() is None

        # Test setter/getter methods with method chaining
        coupling.setNmScheduleVariant("variant1")
        assert coupling.getNmScheduleVariant() == "variant1"
        assert coupling == coupling.setNmScheduleVariant("variant1")

        # Test addCoupledClusterRef
        coupling.addCoupledClusterRef("cluster_ref")
        assert "cluster_ref" in coupling.getCoupledClusterRefs()
        assert coupling == coupling.addCoupledClusterRef("cluster_ref2")

    def test_nm_node_abstract(self):
        """
        Test NmNode abstract class functionality.
        """
        with pytest.raises(TypeError):
            NmNode(MockParent(), "test_nm_node")
        """
        Test NmNode abstract class functionality.
        """
        with pytest.raises(TypeError):
            NmNode(MockParent(), "test_nm_node")

    def test_can_nm_node(self):
        """
        Test CanNmNode class functionality with method chaining and None handling.
        """
        parent = MockParent()
        node = CanNmNode(parent, "test_can_nm_node")

        # Test constructor
        assert node is not None

        # Test default values
        assert node.getControllerRef() is None
        assert node.getNmCoordCluster() is None
        assert node.getNmCoordinatorRole() is None
        assert node.getNmIfEcuRef() is None
        assert node.getNmNodeId() is None
        assert node.getNmPassiveModeEnabled() is None
        assert node.getRxNmPduRefs() == []
        assert node.getTxNmPduRefs() == []
        assert node.getAllNmMessagesKeepAwake() is None
        assert node.getNmCarWakeUpFilterEnabled() is None
        assert node.getNmCarWakeUpRxEnabled() is None
        assert node.getNmMsgCycleOffset() is None
        assert node.getNmMsgReducedTime() is None
        assert node.getNmRangeConfig() is None

        # Test setter/getter methods with method chaining
        node.setControllerRef("controller_ref")
        assert node.getControllerRef() == "controller_ref"
        assert node == node.setControllerRef("controller_ref")

        node.setNmCoordCluster(1)
        assert node.getNmCoordCluster() == 1
        assert node == node.setNmCoordCluster(1)

        node.setNmCoordinatorRole("role")
        assert node.getNmCoordinatorRole() == "role"
        assert node == node.setNmCoordinatorRole("role")

        node.setNmIfEcuRef("ecu_ref")
        assert node.getNmIfEcuRef() == "ecu_ref"
        assert node == node.setNmIfEcuRef("ecu_ref")

        node.setNmNodeId(2)
        assert node.getNmNodeId() == 2
        assert node == node.setNmNodeId(2)

        node.setNmPassiveModeEnabled(True)
        assert node.getNmPassiveModeEnabled() is True
        assert node == node.setNmPassiveModeEnabled(True)

        # Test add methods
        node.addRxNmPduRef("rx_ref")
        assert "rx_ref" in node.getRxNmPduRefs()
        assert node == node.addRxNmPduRef("rx_ref2")

        node.addTxNmPduRef("tx_ref")
        assert "tx_ref" in node.getTxNmPduRefs()
        assert node == node.addTxNmPduRef("tx_ref2")

        # Test CAN-specific methods
        node.setAllNmMessagesKeepAwake(True)
        assert node.getAllNmMessagesKeepAwake() is True
        assert node == node.setAllNmMessagesKeepAwake(True)

        node.setNmCarWakeUpFilterEnabled(True)
        assert node.getNmCarWakeUpFilterEnabled() is True
        assert node == node.setNmCarWakeUpFilterEnabled(True)

        node.setNmCarWakeUpRxEnabled(True)
        assert node.getNmCarWakeUpRxEnabled() is True
        assert node == node.setNmCarWakeUpRxEnabled(True)

        node.setNmMsgCycleOffset(10)
        assert node.getNmMsgCycleOffset() == 10
        assert node == node.setNmMsgCycleOffset(10)

        node.setNmMsgReducedTime(20)
        assert node.getNmMsgReducedTime() == 20
        assert node == node.setNmMsgReducedTime(20)

    def test_flexray_nm_node(self):
        """
        Test FlexrayNmNode class functionality.
        """
        parent = MockParent()
        node = FlexrayNmNode(parent, "test_flexray_nm_node")

        # Test constructor
        assert node is not None

        # Test default values inherited from NmNode
        assert node.getControllerRef() is None
        assert node.getNmCoordCluster() is None
        assert node.getNmCoordinatorRole() is None
        assert node.getNmIfEcuRef() is None
        assert node.getNmNodeId() is None
        assert node.getNmPassiveModeEnabled() is None
        assert node.getRxNmPduRefs() == []
        assert node.getTxNmPduRefs() == []

    def test_j1939_nm_node(self):
        """
        Test J1939NmNode class functionality.
        """
        parent = MockParent()
        node = J1939NmNode(parent, "test_j1939_nm_node")

        # Test constructor
        assert node is not None

        # Test default values inherited from NmNode
        assert node.getControllerRef() is None
        assert node.getNmCoordCluster() is None
        assert node.getNmCoordinatorRole() is None
        assert node.getNmIfEcuRef() is None
        assert node.getNmNodeId() is None
        assert node.getNmPassiveModeEnabled() is None
        assert node.getRxNmPduRefs() == []
        assert node.getTxNmPduRefs() == []

    def test_udp_nm_node(self):
        """
        Test UdpNmNode class functionality with method chaining and None handling.
        """
        parent = MockParent()
        node = UdpNmNode(parent, "test_udp_nm_node")

        # Test constructor
        assert node is not None

        # Test default values
        assert node.getControllerRef() is None
        assert node.getNmCoordCluster() is None
        assert node.getNmCoordinatorRole() is None
        assert node.getNmIfEcuRef() is None
        assert node.getNmNodeId() is None
        assert node.getNmPassiveModeEnabled() is None
        assert node.getRxNmPduRefs() == []
        assert node.getTxNmPduRefs() == []
        assert node.getAllNmMessagesKeepAwake() is None
        assert node.getNmMsgCycleOffset() is None

        # Test setter/getter methods with method chaining - with None values
        assert node == node.setAllNmMessagesKeepAwake(None)
        assert node.getAllNmMessagesKeepAwake() is None

        assert node == node.setNmMsgCycleOffset(None)
        assert node.getNmMsgCycleOffset() is None

        # Test setter/getter methods with method chaining - with actual values
        node.setAllNmMessagesKeepAwake(True)
        assert node.getAllNmMessagesKeepAwake() is True
        assert node == node.setAllNmMessagesKeepAwake(True)

        node.setNmMsgCycleOffset(10)
        assert node.getNmMsgCycleOffset() == 10
        assert node == node.setNmMsgCycleOffset(10)

    def test_busspecific_nm_ecu_abstract(self):
        """
        Test BusspecificNmEcu abstract class functionality.
        """
        with pytest.raises(TypeError):
            BusspecificNmEcu()


class TestBusspecificNmEcu:
    """Spec-driven tests for the abstract BusspecificNmEcu (Table 6.301)."""

    def test_abstract(self):
        """BusspecificNmEcu is abstract and cannot be instantiated directly."""
        with pytest.raises(TypeError):
            BusspecificNmEcu()

    def test_subclasses_inherit_base(self):
        """Every spec subclass instantiates and is a BusspecificNmEcu."""
        for subclass in (CanNmEcu, FlexrayNmEcu, J1939NmEcu, UdpNmEcu):
            ecu = subclass()
            assert isinstance(ecu, BusspecificNmEcu)
            assert isinstance(ecu, ARObject)

    def test_can_nm_ecu(self):
        """
        Test CanNmEcu class functionality.
        """
        ecu = CanNmEcu()

        # Test constructor
        assert ecu is not None

    def test_flexray_nm_ecu(self):
        """
        Test FlexrayNmEcu class functionality.
        """
        ecu = FlexrayNmEcu()

        # Test constructor
        assert ecu is not None

    def test_j1939_nm_ecu(self):
        """
        Test J1939NmEcu class functionality.
        """
        ecu = J1939NmEcu()

        # Test constructor
        assert ecu is not None

    def test_udp_nm_ecu(self):
        """
        Test UdpNmEcu class functionality with method chaining and None handling.
        """
        ecu = UdpNmEcu()

        # Test constructor
        assert ecu is not None

        # Test default values
        assert ecu.getNmSynchronizationPointEnabled() is None

        # Test setter/getter methods with method chaining - with None values
        assert ecu == ecu.setNmSynchronizationPointEnabled(None)
        assert ecu.getNmSynchronizationPointEnabled() is None

        # Test setter/getter methods with method chaining - with actual values
        ecu.setNmSynchronizationPointEnabled(True)
        assert ecu.getNmSynchronizationPointEnabled() is True
        assert ecu == ecu.setNmSynchronizationPointEnabled(True)

    def test_nm_ecu(self):
        """
        Test NmEcu class functionality with method chaining and None handling.
        """
        parent = MockParent()
        ecu = NmEcu(parent, "test_nm_ecu")

        # Test constructor
        assert ecu is not None

        # Test default values
        assert ecu.getBusDependentNmEcus() == []
        assert ecu.getEcuInstanceRef() is None
        assert ecu.getNmBusSynchronizationEnabled() is None
        assert ecu.getNmComControlEnabled() is None
        assert ecu.getNmCoordinator() is None
        assert ecu.getNmCycletimeMainFunction() is None
        assert ecu.getNmNodeDetectionEnabled() is None
        assert ecu.getNmNodeIdEnabled() is None
        assert ecu.getNmPduRxIndicationEnabled() is None
        assert ecu.getNmRemoteSleepIndEnabled() is None
        assert ecu.getNmRepeatMsgIndEnabled() is None
        assert ecu.getNmStateChangeIndEnabled() is None
        assert ecu.getNmUserDataEnabled() is None

        # Test setter/getter methods with method chaining - with None values
        assert ecu == ecu.setEcuInstanceRef(None)
        assert ecu.getEcuInstanceRef() is None

        assert ecu == ecu.setNmBusSynchronizationEnabled(None)
        assert ecu.getNmBusSynchronizationEnabled() is None

        assert ecu == ecu.setNmComControlEnabled(None)
        assert ecu.getNmComControlEnabled() is None

        assert ecu == ecu.setNmCoordinator(None)
        assert ecu.getNmCoordinator() is None

        assert ecu == ecu.setNmCycletimeMainFunction(None)
        assert ecu.getNmCycletimeMainFunction() is None

        assert ecu == ecu.setNmNodeDetectionEnabled(None)
        assert ecu.getNmNodeDetectionEnabled() is None

        assert ecu == ecu.setNmNodeIdEnabled(None)
        assert ecu.getNmNodeIdEnabled() is None

        assert ecu == ecu.setNmPduRxIndicationEnabled(None)
        assert ecu.getNmPduRxIndicationEnabled() is None

        assert ecu == ecu.setNmRemoteSleepIndEnabled(None)
        assert ecu.getNmRemoteSleepIndEnabled() is None

        assert ecu == ecu.setNmRepeatMsgIndEnabled(None)
        assert ecu.getNmRepeatMsgIndEnabled() is None

        assert ecu == ecu.setNmStateChangeIndEnabled(None)
        assert ecu.getNmStateChangeIndEnabled() is None

        assert ecu == ecu.setNmUserDataEnabled(None)
        assert ecu.getNmUserDataEnabled() is None

        # Test setter/getter methods with method chaining - with actual values
        ecu.setEcuInstanceRef("ecu_ref")
        assert ecu.getEcuInstanceRef() == "ecu_ref"
        assert ecu == ecu.setEcuInstanceRef("ecu_ref")

        ecu.setNmBusSynchronizationEnabled(True)
        assert ecu.getNmBusSynchronizationEnabled() is True
        assert ecu == ecu.setNmBusSynchronizationEnabled(True)

        ecu.setNmComControlEnabled(True)
        assert ecu.getNmComControlEnabled() is True
        assert ecu == ecu.setNmComControlEnabled(True)

        ecu.setNmCoordinator("coordinator")
        assert ecu.getNmCoordinator() == "coordinator"
        assert ecu == ecu.setNmCoordinator("coordinator")

        ecu.setNmCycletimeMainFunction(100)
        assert ecu.getNmCycletimeMainFunction() == 100
        assert ecu == ecu.setNmCycletimeMainFunction(100)

        ecu.setNmNodeDetectionEnabled(True)
        assert ecu.getNmNodeDetectionEnabled() is True
        assert ecu == ecu.setNmNodeDetectionEnabled(True)

        ecu.setNmNodeIdEnabled(True)
        assert ecu.getNmNodeIdEnabled() is True
        assert ecu == ecu.setNmNodeIdEnabled(True)

        ecu.setNmPduRxIndicationEnabled(True)
        assert ecu.getNmPduRxIndicationEnabled() is True
        assert ecu == ecu.setNmPduRxIndicationEnabled(True)

        ecu.setNmRemoteSleepIndEnabled(True)
        assert ecu.getNmRemoteSleepIndEnabled() is True
        assert ecu == ecu.setNmRemoteSleepIndEnabled(True)

        ecu.setNmRepeatMsgIndEnabled(True)
        assert ecu.getNmRepeatMsgIndEnabled() is True
        assert ecu == ecu.setNmRepeatMsgIndEnabled(True)

        ecu.setNmStateChangeIndEnabled(True)
        assert ecu.getNmStateChangeIndEnabled() is True
        assert ecu == ecu.setNmStateChangeIndEnabled(True)

        ecu.setNmUserDataEnabled(True)
        assert ecu.getNmUserDataEnabled() is True
        assert ecu == ecu.setNmUserDataEnabled(True)

        # Test addBusDependentNmEcu
        can_ecu = CanNmEcu()
        ecu.addBusDependentNmEcu(can_ecu)
        assert can_ecu in ecu.getBusDependentNmEcus()
        assert ecu == ecu.addBusDependentNmEcu(can_ecu)

    def test_nm_config(self):
        """
        Test NmConfig class functionality.
        """
        parent = MockParent()
        config = NmConfig(parent, "test_nm_config")

        # Test constructor
        assert config is not None

        # Test default values
        assert config.getNmClusterCouplings() == []
        assert config.getNmIfEcus() == []

        # Test addNmClusterCouplings
        coupling = CanNmClusterCoupling()
        config.addNmClusterCouplings(coupling)
        assert coupling in config.getNmClusterCouplings()
        assert config == config.addNmClusterCouplings(coupling)

    def test_nm_cluster_abstract(self):
        """
        Test NmCluster abstract class functionality.
        """
        parent = MockParent()
        cluster = CanNmCluster(parent, "test_nm_cluster")

        # Test constructor
        assert cluster is not None

        # Test default values
        assert cluster.getCommunicationClusterRef() is None
        assert cluster.getNmChannelId() is None
        assert cluster.getNmChannelSleepMaster() is None
        assert cluster.getNmNodes() == []
        assert cluster.getNmNodeDetectionEnabled() is None
        assert cluster.getNmNodeIdEnabled() is None
        assert cluster.getNmPncParticipation() is None
        assert cluster.getNmRepeatMsgIndEnabled() is None
        assert cluster.getNmSynchronizingNetwork() is None

        # Test setter/getter methods with method chaining
        cluster.setCommunicationClusterRef("cluster_ref")
        assert cluster.getCommunicationClusterRef() == "cluster_ref"
        assert cluster == cluster.setCommunicationClusterRef("cluster_ref")

        cluster.setNmChannelId(1)
        assert cluster.getNmChannelId() == 1
        assert cluster == cluster.setNmChannelId(1)

        cluster.setNmChannelSleepMaster("master")
        assert cluster.getNmChannelSleepMaster() == "master"
        assert cluster == cluster.setNmChannelSleepMaster("master")

        cluster.setNmNodeDetectionEnabled(True)
        assert cluster.getNmNodeDetectionEnabled() is True
        assert cluster == cluster.setNmNodeDetectionEnabled(True)

        cluster.setNmNodeIdEnabled(True)
        assert cluster.getNmNodeIdEnabled() is True
        assert cluster == cluster.setNmNodeIdEnabled(True)

        cluster.setNmPncParticipation("participation")
        assert cluster.getNmPncParticipation() == "participation"
        assert cluster == cluster.setNmPncParticipation("participation")

        cluster.setNmRepeatMsgIndEnabled(True)
        assert cluster.getNmRepeatMsgIndEnabled() is True
        assert cluster == cluster.setNmRepeatMsgIndEnabled(True)

        cluster.setNmSynchronizingNetwork("network")
        assert cluster.getNmSynchronizingNetwork() == "network"
        assert cluster == cluster.setNmSynchronizingNetwork("network")

        # Test createCanNmNode
        can_node = cluster.createCanNmNode("can_node")
        assert isinstance(can_node, CanNmNode)
        assert can_node in cluster.getCanNmNodes()

    def test_can_nm_cluster(self):
        """
        Test CanNmCluster class functionality with method chaining and None handling.
        """
        parent = MockParent()
        cluster = CanNmCluster(parent, "test_can_nm_cluster")

        # Test constructor
        assert cluster is not None

        # Test default values
        assert cluster.getNmBusloadReductionActive() is None
        assert cluster.getNmCarWakeUpBitPosition() is None
        assert cluster.getNmCarWakeUpFilterNodeId() is None
        assert cluster.getNmCarWakeUpRxEnabled() is None
        assert cluster.getNmCbvPosition() is None
        assert cluster.getNmChannelActive() is None
        assert cluster.getNmImmediateNmCycleTime() is None
        assert cluster.getNmImmediateNmTransmissions() is None
        assert cluster.getNmMessageTimeoutTime() is None
        assert cluster.getNmMsgCycleTime() is None
        assert cluster.getNmNetworkTimeout() is None
        assert cluster.getNmNidPosition() is None
        assert cluster.getNmRemoteSleepIndicationTime() is None
        assert cluster.getNmRepeatMessageTime() is None
        assert cluster.getNmUserDataLength() is None
        assert cluster.getNmWaitBusSleepTime() is None

        # Test setter/getter methods with method chaining
        cluster.setNmBusloadReductionActive(True)
        assert cluster.getNmBusloadReductionActive() is True
        assert cluster == cluster.setNmBusloadReductionActive(True)

        cluster.setNmCarWakeUpBitPosition(1)
        assert cluster.getNmCarWakeUpBitPosition() == 1
        assert cluster == cluster.setNmCarWakeUpBitPosition(1)

        cluster.setNmCarWakeUpFilterNodeId(2)
        assert cluster.getNmCarWakeUpFilterNodeId() == 2
        assert cluster == cluster.setNmCarWakeUpFilterNodeId(2)

        cluster.setNmCarWakeUpRxEnabled(True)
        assert cluster.getNmCarWakeUpRxEnabled() is True
        assert cluster == cluster.setNmCarWakeUpRxEnabled(True)

        cluster.setNmCbvPosition(3)
        assert cluster.getNmCbvPosition() == 3
        assert cluster == cluster.setNmCbvPosition(3)

        cluster.setNmChannelActive(True)
        assert cluster.getNmChannelActive() is True
        assert cluster == cluster.setNmChannelActive(True)

        cluster.setNmImmediateNmCycleTime(10)
        assert cluster.getNmImmediateNmCycleTime() == 10
        assert cluster == cluster.setNmImmediateNmCycleTime(10)

        cluster.setNmImmediateNmTransmissions(5)
        assert cluster.getNmImmediateNmTransmissions() == 5
        assert cluster == cluster.setNmImmediateNmTransmissions(5)

        cluster.setNmMessageTimeoutTime(20)
        assert cluster.getNmMessageTimeoutTime() == 20
        assert cluster == cluster.setNmMessageTimeoutTime(20)

        cluster.setNmMsgCycleTime(30)
        assert cluster.getNmMsgCycleTime() == 30
        assert cluster == cluster.setNmMsgCycleTime(30)

        cluster.setNmNetworkTimeout(40)
        assert cluster.getNmNetworkTimeout() == 40
        assert cluster == cluster.setNmNetworkTimeout(40)

        cluster.setNmNidPosition(4)
        assert cluster.getNmNidPosition() == 4
        assert cluster == cluster.setNmNidPosition(4)

        cluster.setNmRemoteSleepIndicationTime(50)
        assert cluster.getNmRemoteSleepIndicationTime() == 50
        assert cluster == cluster.setNmRemoteSleepIndicationTime(50)

        cluster.setNmRepeatMessageTime(60)
        assert cluster.getNmRepeatMessageTime() == 60
        assert cluster == cluster.setNmRepeatMessageTime(60)

        cluster.setNmUserDataLength(8)
        assert cluster.getNmUserDataLength() == 8
        assert cluster == cluster.setNmUserDataLength(8)

        cluster.setNmWaitBusSleepTime(70)
        assert cluster.getNmWaitBusSleepTime() == 70
        assert cluster == cluster.setNmWaitBusSleepTime(70)

    def test_flexray_nm_cluster(self):
        """
        Test FlexrayNmCluster class functionality.
        """
        parent = MockParent()
        cluster = FlexrayNmCluster(parent, "test_flexray_nm_cluster")

        # Test constructor
        assert cluster is not None

        # Test default values inherited from NmCluster
        assert cluster.getCommunicationClusterRef() is None
        assert cluster.getNmChannelId() is None
        assert cluster.getNmChannelSleepMaster() is None
        assert cluster.getNmNodes() == []
        assert cluster.getNmNodeDetectionEnabled() is None
        assert cluster.getNmNodeIdEnabled() is None
        assert cluster.getNmPncParticipation() is None
        assert cluster.getNmRepeatMsgIndEnabled() is None
        assert cluster.getNmSynchronizingNetwork() is None

    def test_j1939_nm_cluster(self):
        """
        Test J1939NmCluster class functionality.
        """
        parent = MockParent()
        cluster = J1939NmCluster(parent, "test_j1939_nm_cluster")

        # Test constructor
        assert cluster is not None

        # Test default values inherited from NmCluster
        assert cluster.getCommunicationClusterRef() is None
        assert cluster.getNmChannelId() is None
        assert cluster.getNmChannelSleepMaster() is None
        assert cluster.getNmNodes() == []
        assert cluster.getNmNodeDetectionEnabled() is None
        assert cluster.getNmNodeIdEnabled() is None
        assert cluster.getNmPncParticipation() is None
        assert cluster.getNmRepeatMsgIndEnabled() is None
        assert cluster.getNmSynchronizingNetwork() is None

    def test_udp_nm_cluster_coupling(self):
        """
        Test UdpNmClusterCoupling class functionality with method chaining and None handling.
        """
        coupling = UdpNmClusterCoupling()

        # Test constructor
        assert coupling is not None

        # Test default values
        assert coupling.getCoupledClusterRefs() == []
        assert coupling.getNmImmediateRestartEnabled() is None

        # Test setter/getter methods with method chaining - with None values
        assert coupling == coupling.setNmImmediateRestartEnabled(None)
        assert coupling.getNmImmediateRestartEnabled() is None

        # Test setter/getter methods with method chaining - with actual values
        coupling.setNmImmediateRestartEnabled(True)
        assert coupling.getNmImmediateRestartEnabled() is True
        assert coupling == coupling.setNmImmediateRestartEnabled(True)

        # Test addCoupledClusterRef
        coupling.addCoupledClusterRef("cluster_ref")
        assert "cluster_ref" in coupling.getCoupledClusterRefs()
        assert coupling == coupling.addCoupledClusterRef("cluster_ref2")

    def test_udp_nm_cluster(self):
        """
        Test UdpNmCluster class functionality with method chaining and None handling.
        """
        parent = MockParent()
        cluster = UdpNmCluster(parent, "test_udp_nm_cluster")

        # Test constructor
        assert cluster is not None

        # Test default values
        assert cluster.getNmCbvPosition() is None
        assert cluster.getNmChannelActive() is None
        assert cluster.getNmImmediateNmCycleTime() is None
        assert cluster.getNmImmediateNmTransmissions() is None
        assert cluster.getNmMessageTimeoutTime() is None
        assert cluster.getNmMsgCycleTime() is None
        assert cluster.getNmNetworkTimeout() is None
        assert cluster.getNmNidPosition() is None
        assert cluster.getNmRemoteSleepIndicationTime() is None
        assert cluster.getNmRepeatMessageTime() is None
        assert cluster.getNmWaitBusSleepTime() is None
        assert cluster.getVlanRef() is None

        # Test setter/getter methods with method chaining - with None values
        assert cluster == cluster.setNmCbvPosition(None)
        assert cluster.getNmCbvPosition() is None

        assert cluster == cluster.setNmChannelActive(None)
        assert cluster.getNmChannelActive() is None

        assert cluster == cluster.setNmImmediateNmCycleTime(None)
        assert cluster.getNmImmediateNmCycleTime() is None

        assert cluster == cluster.setNmImmediateNmTransmissions(None)
        assert cluster.getNmImmediateNmTransmissions() is None

        assert cluster == cluster.setNmMessageTimeoutTime(None)
        assert cluster.getNmMessageTimeoutTime() is None

        assert cluster == cluster.setNmMsgCycleTime(None)
        assert cluster.getNmMsgCycleTime() is None

        assert cluster == cluster.setNmNetworkTimeout(None)
        assert cluster.getNmNetworkTimeout() is None

        assert cluster == cluster.setNmNidPosition(None)
        assert cluster.getNmNidPosition() is None

        assert cluster == cluster.setNmRemoteSleepIndicationTime(None)
        assert cluster.getNmRemoteSleepIndicationTime() is None

        assert cluster == cluster.setNmRepeatMessageTime(None)
        assert cluster.getNmRepeatMessageTime() is None

        assert cluster == cluster.setNmWaitBusSleepTime(None)
        assert cluster.getNmWaitBusSleepTime() is None

        assert cluster == cluster.setVlanRef(None)
        assert cluster.getVlanRef() is None

        # Test setter/getter methods with method chaining - with actual values
        cluster.setNmCbvPosition(5)
        assert cluster.getNmCbvPosition() == 5
        assert cluster == cluster.setNmCbvPosition(5)

        cluster.setNmChannelActive(True)
        assert cluster.getNmChannelActive() is True
        assert cluster == cluster.setNmChannelActive(True)

        cluster.setNmImmediateNmCycleTime(10)
        assert cluster.getNmImmediateNmCycleTime() == 10
        assert cluster == cluster.setNmImmediateNmCycleTime(10)

        cluster.setNmImmediateNmTransmissions(3)
        assert cluster.getNmImmediateNmTransmissions() == 3
        assert cluster == cluster.setNmImmediateNmTransmissions(3)

        cluster.setNmMessageTimeoutTime(20)
        assert cluster.getNmMessageTimeoutTime() == 20
        assert cluster == cluster.setNmMessageTimeoutTime(20)

        cluster.setNmMsgCycleTime(30)
        assert cluster.getNmMsgCycleTime() == 30
        assert cluster == cluster.setNmMsgCycleTime(30)

        cluster.setNmNetworkTimeout(40)
        assert cluster.getNmNetworkTimeout() == 40
        assert cluster == cluster.setNmNetworkTimeout(40)

        cluster.setNmNidPosition(6)
        assert cluster.getNmNidPosition() == 6
        assert cluster == cluster.setNmNidPosition(6)

        cluster.setNmRemoteSleepIndicationTime(50)
        assert cluster.getNmRemoteSleepIndicationTime() == 50
        assert cluster == cluster.setNmRemoteSleepIndicationTime(50)

        cluster.setNmRepeatMessageTime(60)
        assert cluster.getNmRepeatMessageTime() == 60
        assert cluster == cluster.setNmRepeatMessageTime(60)

        cluster.setNmWaitBusSleepTime(70)
        assert cluster.getNmWaitBusSleepTime() == 70
        assert cluster == cluster.setNmWaitBusSleepTime(70)

        cluster.setVlanRef("vlan_ref")
        assert cluster.getVlanRef() == "vlan_ref"
        assert cluster == cluster.setVlanRef("vlan_ref")


class TestNmNode:
    """Spec-driven tests for the abstract NmNode via a concrete subclass."""

    def _make_node(self):
        return CanNmNode(MockParent(), "test_nm_node")

    def test_abstract(self):
        """NmNode is abstract and cannot be instantiated directly."""
        with pytest.raises(TypeError):
            NmNode(MockParent(), "nm_node")

    def test_initialization(self):
        """NmNode defaults are None and empty lists."""
        node = self._make_node()
        assert node.getControllerRef() is None
        assert node.getNmCoordCluster() is None
        assert node.getNmCoordinatorRole() is None
        assert node.getNmIfEcuRef() is None
        assert node.getNmNodeId() is None
        assert node.getNmPassiveModeEnabled() is None
        assert node.getRxNmPduRefs() == []
        assert node.getTxNmPduRefs() == []

    def test_get_set_controller_ref(self):
        """controller ref get/set with method chaining and None no-op."""
        node = self._make_node()
        ref = RefType()
        ref.setDest("CAN-CONTROLLER").setValue("/ctrl/c1")
        assert node == node.setControllerRef(ref)
        assert node.getControllerRef() == ref
        assert node == node.setControllerRef(None)
        assert node.getControllerRef() == ref

    def test_get_set_nm_coord_cluster(self):
        """nmCoordCluster get/set with method chaining and None no-op."""
        node = self._make_node()
        value = Integer()
        value.setValue(3)
        assert node == node.setNmCoordCluster(value)
        assert node.getNmCoordCluster() == value
        assert node == node.setNmCoordCluster(None)
        assert node.getNmCoordCluster() == value

    def test_get_set_nm_coordinator_role(self):
        """nmCoordinatorRole get/set with enum value, chaining and None no-op."""
        node = self._make_node()
        role = NmCoordinatorRoleEnum()
        role.setValue(NmCoordinatorRoleEnum.ACTIVE)
        assert node == node.setNmCoordinatorRole(role)
        assert node.getNmCoordinatorRole() == role
        assert node == node.setNmCoordinatorRole(None)
        assert node.getNmCoordinatorRole() == role

    def test_get_set_nm_if_ecu_ref(self):
        """nmIfEcuRef get/set with method chaining and None no-op."""
        node = self._make_node()
        ref = RefType()
        ref.setDest("NM-ECU").setValue("/ecus/e1")
        assert node == node.setNmIfEcuRef(ref)
        assert node.getNmIfEcuRef() == ref
        assert node == node.setNmIfEcuRef(None)
        assert node.getNmIfEcuRef() == ref

    def test_get_set_nm_node_id(self):
        """nmNodeId get/set with method chaining and None no-op."""
        node = self._make_node()
        value = Integer()
        value.setValue(1)
        assert node == node.setNmNodeId(value)
        assert node.getNmNodeId() == value
        assert node == node.setNmNodeId(None)
        assert node.getNmNodeId() == value

    def test_get_set_nm_passive_mode_enabled(self):
        """nmPassiveModeEnabled get/set with chaining and None no-op."""
        node = self._make_node()
        value = Boolean()
        value.setValue(True)
        assert node == node.setNmPassiveModeEnabled(value)
        assert node.getNmPassiveModeEnabled() == value
        assert node == node.setNmPassiveModeEnabled(None)
        assert node.getNmPassiveModeEnabled() == value

    def test_add_rx_nm_pdu_ref(self):
        """addRxNmPduRef appends and getRxNmPduRefs returns the refs."""
        node = self._make_node()
        ref = RefType()
        ref.setDest("NM-PDU").setValue("/rx/p1")
        assert node == node.addRxNmPduRef(ref)
        assert node.getRxNmPduRefs() == [ref]

    def test_add_tx_nm_pdu_ref(self):
        """addTxNmPduRef appends and getTxNmPduRefs returns the refs."""
        node = self._make_node()
        ref = RefType()
        ref.setDest("NM-PDU").setValue("/tx/p1")
        assert node == node.addTxNmPduRef(ref)
        assert node.getTxNmPduRefs() == [ref]


class Test_NmCoordinatorRoleEnum:
    """Test cases for NmCoordinatorRoleEnum class."""

    def test_members(self):
        """Test NmCoordinatorRoleEnum member values."""
        enum = NmCoordinatorRoleEnum()
        values = enum.getEnumValues()
        assert NmCoordinatorRoleEnum.ACTIVE == "active"
        assert NmCoordinatorRoleEnum.PASSIVE == "passive"
        assert NmCoordinatorRoleEnum.ACTIVE in values
        assert NmCoordinatorRoleEnum.PASSIVE in values

    def test_set_value(self):
        """Test NmCoordinatorRoleEnum value assignment."""
        enum = NmCoordinatorRoleEnum()
        enum.setValue(NmCoordinatorRoleEnum.ACTIVE)
        assert enum.getValue() == "active"


class Test_J1939NmAddressConfigurationCapabilityEnum:
    """Spec-driven tests for the J1939NmAddressConfigurationCapabilityEnum."""

    def test_members(self):
        """The five literals exist with the serialized XML form as value."""
        enum = J1939NmAddressConfigurationCapabilityEnum()
        values = enum.getEnumValues()
        assert J1939NmAddressConfigurationCapabilityEnum.J1939NM_AAC == "J-1939-NM-AAC"
        assert J1939NmAddressConfigurationCapabilityEnum.J1939NM_CCA == "J-1939-NM-CCA"
        assert J1939NmAddressConfigurationCapabilityEnum.J1939NM_NCA == "J-1939-NM-NCA"
        assert J1939NmAddressConfigurationCapabilityEnum.J1939NM_SCA == "J-1939-NM-SCA"
        assert J1939NmAddressConfigurationCapabilityEnum.J1939NM_SVCA == "J-1939-NM-SVCA"
        assert J1939NmAddressConfigurationCapabilityEnum.J1939NM_AAC in values
        assert J1939NmAddressConfigurationCapabilityEnum.J1939NM_CCA in values
        assert J1939NmAddressConfigurationCapabilityEnum.J1939NM_NCA in values
        assert J1939NmAddressConfigurationCapabilityEnum.J1939NM_SCA in values
        assert J1939NmAddressConfigurationCapabilityEnum.J1939NM_SVCA in values

    def test_set_value(self):
        """Value assignment with a typed enum instance."""
        enum = J1939NmAddressConfigurationCapabilityEnum()
        enum.setValue(J1939NmAddressConfigurationCapabilityEnum.J1939NM_AAC)
        assert enum.getValue() == "J-1939-NM-AAC"


class TestJ1939NodeName:
    """Spec-driven tests for the J1939NodeName class."""

    def _make_node_name(self):
        return J1939NodeName()

    def test_initialization(self):
        """All J1939NodeName fields default to None."""
        node_name = self._make_node_name()
        assert node_name.getArbitraryAddressCapable() is None
        assert node_name.getEcuInstance() is None
        assert node_name.getFunction() is None
        assert node_name.getFunctionInstance() is None
        assert node_name.getIdentitiyNumber() is None
        assert node_name.getIndustryGroup() is None
        assert node_name.getManufacturerCode() is None
        assert node_name.getVehicleSystem() is None
        assert node_name.getVehicleSystemInstance() is None

    def test_get_set_arbitrary_address_capable(self):
        """arbitraryAddressCapable get/set with chaining and None no-op."""
        node_name = self._make_node_name()
        value = Boolean()
        value.setValue(True)
        assert node_name == node_name.setArbitraryAddressCapable(value)
        assert node_name.getArbitraryAddressCapable() == value
        assert node_name == node_name.setArbitraryAddressCapable(None)
        assert node_name.getArbitraryAddressCapable() == value

    def test_get_set_ecu_instance(self):
        """ecuInstance get/set with chaining and None no-op."""
        node_name = self._make_node_name()
        value = Integer()
        value.setValue(3)
        assert node_name == node_name.setEcuInstance(value)
        assert node_name.getEcuInstance() == value
        assert node_name == node_name.setEcuInstance(None)
        assert node_name.getEcuInstance() == value

    def test_get_set_function(self):
        """function get/set with chaining and None no-op."""
        node_name = self._make_node_name()
        value = Integer()
        value.setValue(128)
        assert node_name == node_name.setFunction(value)
        assert node_name.getFunction() == value
        assert node_name == node_name.setFunction(None)
        assert node_name.getFunction() == value

    def test_get_set_function_instance(self):
        """functionInstance get/set with chaining and None no-op."""
        node_name = self._make_node_name()
        value = Integer()
        value.setValue(4)
        assert node_name == node_name.setFunctionInstance(value)
        assert node_name.getFunctionInstance() == value
        assert node_name == node_name.setFunctionInstance(None)
        assert node_name.getFunctionInstance() == value

    def test_get_set_identitiy_number(self):
        """identitiyNumber get/set with chaining and None no-op."""
        node_name = self._make_node_name()
        value = Integer()
        value.setValue(1234)
        assert node_name == node_name.setIdentitiyNumber(value)
        assert node_name.getIdentitiyNumber() == value
        assert node_name == node_name.setIdentitiyNumber(None)
        assert node_name.getIdentitiyNumber() == value

    def test_get_set_industry_group(self):
        """industryGroup get/set with chaining and None no-op."""
        node_name = self._make_node_name()
        value = Integer()
        value.setValue(7)
        assert node_name == node_name.setIndustryGroup(value)
        assert node_name.getIndustryGroup() == value
        assert node_name == node_name.setIndustryGroup(None)
        assert node_name.getIndustryGroup() == value

    def test_get_set_manufacturer_code(self):
        """manufacturerCode get/set with chaining and None no-op."""
        node_name = self._make_node_name()
        value = Integer()
        value.setValue(305)
        assert node_name == node_name.setManufacturerCode(value)
        assert node_name.getManufacturerCode() == value
        assert node_name == node_name.setManufacturerCode(None)
        assert node_name.getManufacturerCode() == value

    def test_get_set_vehicle_system(self):
        """vehicleSystem get/set with chaining and None no-op."""
        node_name = self._make_node_name()
        value = Integer()
        value.setValue(2)
        assert node_name == node_name.setVehicleSystem(value)
        assert node_name.getVehicleSystem() == value
        assert node_name == node_name.setVehicleSystem(None)
        assert node_name.getVehicleSystem() == value

    def test_get_set_vehicle_system_instance(self):
        """vehicleSystemInstance get/set with chaining and None no-op."""
        node_name = self._make_node_name()
        value = Integer()
        value.setValue(1)
        assert node_name == node_name.setVehicleSystemInstance(value)
        assert node_name.getVehicleSystemInstance() == value
        assert node_name == node_name.setVehicleSystemInstance(None)
        assert node_name.getVehicleSystemInstance() == value


class TestJ1939NmNode:
    """Spec-driven tests for the J1939NmNode class."""

    def _make_node(self):
        return J1939NmNode(MockParent(), "test_j1939_nm_node")

    def test_initialization(self):
        """J1939NmNode fields default to None."""
        node = self._make_node()
        assert node.getAddressConfigurationCapability() is None
        assert node.getNodeName() is None

    def test_get_set_address_configuration_capability(self):
        """addressConfigurationCapability get/set with typed enum instance."""
        node = self._make_node()
        value = J1939NmAddressConfigurationCapabilityEnum()
        value.setValue(J1939NmAddressConfigurationCapabilityEnum.J1939NM_SCA)
        assert node == node.setAddressConfigurationCapability(value)
        assert node.getAddressConfigurationCapability() == value
        assert node.getAddressConfigurationCapability().getValue() == "J-1939-NM-SCA"
        assert node == node.setAddressConfigurationCapability(None)
        assert node.getAddressConfigurationCapability() == value

    def test_get_set_node_name(self):
        """nodeName get/set with chaining and None no-op."""
        node = self._make_node()
        value = J1939NodeName()
        value.setArbitraryAddressCapable(Boolean().setValue(True))
        value.setManufacturerCode(Integer().setValue(305))
        assert node == node.setNodeName(value)
        assert node.getNodeName() == value
        assert node.getNodeName().getManufacturerCode().getValue() == 305
        assert node == node.setNodeName(None)
        assert node.getNodeName() == value
