import pytest

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement import (
    NmClusterCoupling,
    CanNmClusterCoupling,
    FlexrayNmClusterCoupling,
    NmNode,
    CanNmNode,
    FlexrayNmNode,
    J1939NmNode,
    UdpNmNode,
    BusspecificNmEcu,
    CanNmEcu,
    FlexrayNmEcu,
    J1939NmEcu,
    UdpNmEcu,
    NmEcu,
    NmConfig,
    NmCluster,
    CanNmCluster,
    FlexrayNmCluster,
    J1939NmCluster,
    UdpNmClusterCoupling,
    UdpNmCluster
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanCommunication import RxIdentifierRange
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import FibexElement


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


class Test_NetworkManagement:
    """Test cases for NetworkManagement-related classes."""
    
    def test_NmClusterCoupling(self):
        """Test NmClusterCoupling abstract class instantiation."""
        with pytest.raises(NotImplementedError):
            NmClusterCoupling()

    def test_CanNmClusterCoupling(self):
        """Test CanNmClusterCoupling class functionality."""
        coupling = CanNmClusterCoupling()

        assert isinstance(coupling, NmClusterCoupling)
        
        # Test default values
        assert coupling.getCoupledClusterRefs() == []
        assert coupling.getNmBusloadReductionEnabled() is None
        assert coupling.getNmImmediateRestartEnabled() is None
        
        # Test setter/getter methods
        mock_ref1 = "ref1"
        mock_ref2 = "ref2"
        coupling.addCoupledClusterRef(mock_ref1)
        coupling.addCoupledClusterRef(mock_ref2)
        assert coupling.getCoupledClusterRefs() == [mock_ref1, mock_ref2]
        
        coupling.setNmBusloadReductionEnabled(True)
        assert coupling.getNmBusloadReductionEnabled() is True
        
        coupling.setNmImmediateRestartEnabled(False)
        assert coupling.getNmImmediateRestartEnabled() is False

    def test_FlexrayNmClusterCoupling(self):
        """Test FlexrayNmClusterCoupling class functionality."""
        coupling = FlexrayNmClusterCoupling()

        assert isinstance(coupling, NmClusterCoupling)
        
        # Test default values
        assert coupling.getCoupledClusterRefs() == []
        assert coupling.getNmScheduleVariant() is None
        
        # Test setter/getter methods
        mock_ref1 = "ref1"
        coupling.addCoupledClusterRef(mock_ref1)
        assert coupling.getCoupledClusterRefs() == [mock_ref1]
        
        coupling.setNmScheduleVariant("variant")
        assert coupling.getNmScheduleVariant() == "variant"

    def test_NmNode(self):
        """Test NmNode abstract class instantiation."""
        parent = MockParent()
        with pytest.raises(NotImplementedError):
            NmNode(parent, "test_nm_node")

    def test_CanNmNode(self):
        """Test CanNmNode class functionality."""
        parent = MockParent()
        node = CanNmNode(parent, "test_can_nm_node")

        assert isinstance(node, NmNode)

        # Test default values
        assert node.getAllNmMessagesKeepAwake() is None
        assert node.getNmCarWakeUpFilterEnabled() is None
        assert node.getNmCarWakeUpRxEnabled() is None
        assert node.getNmMsgCycleOffset() is None
        assert node.getNmMsgReducedTime() is None
        assert node.getNmRangeConfig() is None

        # Test setter/getter methods
        node.setAllNmMessagesKeepAwake(True)
        assert node.getAllNmMessagesKeepAwake() is True

        node.setNmCarWakeUpFilterEnabled(False)
        assert node.getNmCarWakeUpFilterEnabled() is False

        node.setNmCarWakeUpRxEnabled(True)
        assert node.getNmCarWakeUpRxEnabled() is True

        node.setNmMsgCycleOffset("cycle_offset")
        assert node.getNmMsgCycleOffset() == "cycle_offset"

        node.setNmMsgReducedTime("reduced_time")
        assert node.getNmMsgReducedTime() == "reduced_time"

        # Test setNmRangeConfig method (line 217)
        mock_range = RxIdentifierRange()
        node.setNmRangeConfig(mock_range)
        assert node.getNmRangeConfig() == mock_range

    def test_FlexrayNmNode(self):
        """Test FlexrayNmNode class functionality."""
        parent = MockParent()
        node = FlexrayNmNode(parent, "test_flexray_nm_node")

        assert isinstance(node, NmNode)

    def test_J1939NmNode(self):
        """Test J1939NmNode class functionality."""
        parent = MockParent()
        node = J1939NmNode(parent, "test_j1939_nm_node")

        assert isinstance(node, NmNode)

    def test_UdpNmNode(self):
        """Test UdpNmNode class functionality."""
        parent = MockParent()
        node = UdpNmNode(parent, "test_udp_nm_node")

        assert isinstance(node, NmNode)
        
        # Test default values
        assert node.getAllNmMessagesKeepAwake() is None
        assert node.getNmMsgCycleOffset() is None
        
        # Test setter/getter methods
        node.setAllNmMessagesKeepAwake(True)
        assert node.getAllNmMessagesKeepAwake() is True
        
        node.setNmMsgCycleOffset("time_value")
        assert node.getNmMsgCycleOffset() == "time_value"

    def test_BusspecificNmEcu(self):
        """Test BusspecificNmEcu abstract class instantiation."""
        with pytest.raises(NotImplementedError):
            BusspecificNmEcu()

    def test_CanNmEcu(self):
        """Test CanNmEcu class functionality."""
        ecu = CanNmEcu()

        assert isinstance(ecu, BusspecificNmEcu)

    def test_FlexrayNmEcu(self):
        """Test FlexrayNmEcu class functionality."""
        ecu = FlexrayNmEcu()

        assert isinstance(ecu, BusspecificNmEcu)

    def test_J1939NmEcu(self):
        """Test J1939NmEcu class functionality."""
        ecu = J1939NmEcu()

        assert isinstance(ecu, BusspecificNmEcu)

    def test_UdpNmEcu(self):
        """Test UdpNmEcu class functionality."""
        ecu = UdpNmEcu()

        assert isinstance(ecu, BusspecificNmEcu)
        
        # Test default values
        assert ecu.getNmSynchronizationPointEnabled() is None
        
        # Test setter/getter methods
        ecu.setNmSynchronizationPointEnabled(True)
        assert ecu.getNmSynchronizationPointEnabled() is True

    def test_NmEcu(self):
        """Test NmEcu class functionality."""
        parent = MockParent()
        ecu = NmEcu(parent, "test_nm_ecu")

        assert isinstance(ecu, Identifiable)
        
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
        
        # Test setter/getter methods
        mock_ecu_ref = "mock_ecu_ref"
        ecu.setEcuInstanceRef(mock_ecu_ref)
        assert ecu.getEcuInstanceRef() == mock_ecu_ref
        
        ecu.setNmBusSynchronizationEnabled(True)
        assert ecu.getNmBusSynchronizationEnabled() is True
        
        ecu.setNmComControlEnabled(False)
        assert ecu.getNmComControlEnabled() is False
        
        # Test adding bus dependent NM ECUs
        mock_bus_ecu = CanNmEcu()
        ecu.addBusDependentNmEcu(mock_bus_ecu)
        assert ecu.getBusDependentNmEcus() == [mock_bus_ecu]

    def test_NmConfig(self):
        """Test NmConfig class functionality."""
        parent = MockParent()
        config = NmConfig(parent, "test_nm_config")

        assert isinstance(config, FibexElement)
        
        # Test default values
        assert config.getNmClusterCouplings() == []
        assert config.getNmIfEcus() == []

    def test_NmCluster(self):
        """Test NmCluster abstract class functionality."""
        parent = MockParent()
        cluster = CanNmCluster(parent, "test_nm_cluster")

        assert isinstance(cluster, Identifiable)

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

    def test_CanNmCluster(self):
        """Test CanNmCluster class functionality."""
        parent = MockParent()
        cluster = CanNmCluster(parent, "test_can_nm_cluster")

        assert isinstance(cluster, NmCluster)

    def test_FlexrayNmCluster(self):
        """Test FlexrayNmCluster class functionality."""
        parent = MockParent()
        cluster = FlexrayNmCluster(parent, "test_flexray_nm_cluster")

        assert isinstance(cluster, NmCluster)

    def test_J1939NmCluster(self):
        """Test J1939NmCluster class functionality."""
        parent = MockParent()
        cluster = J1939NmCluster(parent, "test_j1939_nm_cluster")

        assert isinstance(cluster, NmCluster)

    def test_UdpNmClusterCoupling(self):
        """Test UdpNmClusterCoupling class functionality."""
        coupling = UdpNmClusterCoupling()

        assert isinstance(coupling, NmClusterCoupling)
        
        # Test default values
        assert coupling.getCoupledClusterRefs() == []
        assert coupling.getNmImmediateRestartEnabled() is None
        
        # Test setter/getter methods
        mock_ref = "mock_ref"
        coupling.addCoupledClusterRef(mock_ref)
        assert coupling.getCoupledClusterRefs() == [mock_ref]
        
        coupling.setNmImmediateRestartEnabled(True)
        assert coupling.getNmImmediateRestartEnabled() is True

    def test_UdpNmCluster(self):
        """Test UdpNmCluster class functionality."""
        parent = MockParent()
        cluster = UdpNmCluster(parent, "test_udp_nm_cluster")

        assert isinstance(cluster, NmCluster)
        
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
        
        # Test setter/getter methods
        cluster.setNmCbvPosition(5)
        assert cluster.getNmCbvPosition() == 5
        
        cluster.setNmChannelActive(True)
        assert cluster.getNmChannelActive() is True
        
        cluster.setVlanRef("vlan_ref")
        assert cluster.getVlanRef() == "vlan_ref"

    def test_NmConfig_create_can_nm_cluster(self):
        """Test NmConfig.createCanNmCluster method (lines 460-463)."""
        parent = MockParent()
        config = NmConfig(parent, "test_nm_config")

        cluster = config.createCanNmCluster("TestCanCluster")
        assert cluster is not None
        assert cluster.short_name == "TestCanCluster"
        assert cluster in config.elements

        # Test that creating the same cluster again returns the existing one
        cluster2 = config.createCanNmCluster("TestCanCluster")
        assert cluster2 == cluster

    def test_NmConfig_create_udp_nm_cluster(self):
        """Test NmConfig.createUdpNmCluster method (lines 466-469)."""
        parent = MockParent()
        config = NmConfig(parent, "test_nm_config")

        cluster = config.createUdpNmCluster("TestUdpCluster")
        assert cluster is not None
        assert cluster.short_name == "TestUdpCluster"
        assert cluster in config.elements

        # Test that creating the same cluster again returns the existing one
        cluster2 = config.createUdpNmCluster("TestUdpCluster")
        assert cluster2 == cluster

    def test_NmConfig_get_can_nm_clusters(self):
        """Test NmConfig.getCanNmClusters method (line 472)."""
        parent = MockParent()
        config = NmConfig(parent, "test_nm_config")

        cluster1 = config.createCanNmCluster("Cluster1")
        cluster2 = config.createCanNmCluster("Cluster2")

        can_clusters = config.getCanNmClusters()
        assert len(can_clusters) == 2
        assert cluster1 in can_clusters
        assert cluster2 in can_clusters

    def test_NmConfig_get_udp_nm_clusters(self):
        """Test NmConfig.getUdpNmClusters method (line 475)."""
        parent = MockParent()
        config = NmConfig(parent, "test_nm_config")

        cluster1 = config.createUdpNmCluster("Cluster1")
        cluster2 = config.createUdpNmCluster("Cluster2")

        udp_clusters = config.getUdpNmClusters()
        assert len(udp_clusters) == 2
        assert cluster1 in udp_clusters
        assert cluster2 in udp_clusters

    def test_NmConfig_get_nm_clusters(self):
        """Test NmConfig.getNmClusters method (line 478)."""
        parent = MockParent()
        config = NmConfig(parent, "test_nm_config")

        can_cluster = config.createCanNmCluster("CanCluster")
        udp_cluster = config.createUdpNmCluster("UdpCluster")

        nm_clusters = config.getNmClusters()
        assert len(nm_clusters) == 2
        assert can_cluster in nm_clusters
        assert udp_cluster in nm_clusters

    def test_NmConfig_add_nm_cluster_couplings(self):
        """Test NmConfig.addNmClusterCouplings method."""
        parent = MockParent()
        config = NmConfig(parent, "test_nm_config")

        coupling = CanNmClusterCoupling()
        result = config.addNmClusterCouplings(coupling)

        assert coupling in config.getNmClusterCouplings()
        assert result == config

    def test_NmConfig_create_nm_ecu(self):
        """Test NmConfig.createNmEcu method (lines 491-495)."""
        parent = MockParent()
        config = NmConfig(parent, "test_nm_config")

        ecu = config.createNmEcu("TestNmEcu")
        assert ecu is not None
        assert ecu.short_name == "TestNmEcu"
        assert ecu in config.elements
        assert ecu in config.getNmIfEcus()

        # Test that creating the same ECU again returns the existing one
        ecu2 = config.createNmEcu("TestNmEcu")
        assert ecu2 == ecu

    def test_NmCluster_create_can_nm_node(self):
        """Test NmCluster.createCanNmNode method (lines 538-543)."""
        parent = MockParent()
        cluster = CanNmCluster(parent, "test_cluster")

        node = cluster.createCanNmNode("TestCanNode")
        assert node is not None
        assert node.short_name == "TestCanNode"
        assert node in cluster.elements
        assert node in cluster.getNmNodes()

        # Test that creating the same node again returns the existing one
        node2 = cluster.createCanNmNode("TestCanNode")
        assert node2 == node

    def test_NmCluster_read_udp_nm_node(self):
        """Test NmCluster.readUdpNmNode method (lines 545-550)."""
        parent = MockParent()
        cluster = UdpNmCluster(parent, "test_cluster")

        node = cluster.readUdpNmNode("TestUdpNode")
        assert node is not None
        assert node.short_name == "TestUdpNode"
        assert node in cluster.elements
        assert node in cluster.getNmNodes()

        # Test that reading the same node again returns the existing one
        node2 = cluster.readUdpNmNode("TestUdpNode")
        assert node2 == node

    def test_NmCluster_get_can_nm_nodes(self):
        """Test NmCluster.getCanNmNodes method."""
        parent = MockParent()
        cluster = CanNmCluster(parent, "test_cluster")

        node1 = cluster.createCanNmNode("Node1")
        node2 = cluster.createCanNmNode("Node2")

        can_nodes = cluster.getCanNmNodes()
        assert len(can_nodes) == 2
        assert node1 in can_nodes
        assert node2 in can_nodes

    def test_NmCluster_get_udp_nm_nodes(self):
        """Test NmCluster.getUdpNmNodes method (line 556)."""
        parent = MockParent()
        cluster = UdpNmCluster(parent, "test_cluster")

        node1 = cluster.readUdpNmNode("Node1")
        node2 = cluster.readUdpNmNode("Node2")

        udp_nodes = cluster.getUdpNmNodes()
        assert len(udp_nodes) == 2
        assert node1 in udp_nodes
        assert node2 in udp_nodes