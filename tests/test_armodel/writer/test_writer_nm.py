"""Tests for writer network management handlers."""
import xml.etree.cElementTree as ET
import pytest
from armodel.writer.arxml_writer import ARXMLWriter
from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (  # noqa: E501
    ARBoolean, ARFloat, ARLiteral, ARNumerical, ARPositiveInteger,
    Integer, PositiveInteger, RefType, TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication import (  # noqa: E501
    LinUnconditionalFrame,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanCommunication import (  # noqa: E501
    RxIdentifierRange,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement import (  # noqa: E501
    CanNmCluster, CanNmClusterCoupling, CanNmNode, NmConfig, NmEcu,
    UdpNmCluster, UdpNmClusterCoupling, UdpNmEcu, UdpNmNode,
)


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def writer():
    AUTOSAR.getInstance().new()
    return ARXMLWriter()


def _parent():
    return ET.Element("PARENT")


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


def _ref(val="/path/ref", dest=None, base=None):
    r = RefType()
    r.value = val
    if dest is not None:
        r.dest = dest
    if base is not None:
        r.base = base
    return r


def _bool(val=True):
    b = ARBoolean()
    b.setValue(val)
    return b


def _numerical(val=1):
    n = ARNumerical()
    n.setValue(val)
    return n


def _int(val=1):
    i = Integer()
    i.setValue(val)
    return i


def _pos_int(val=1):
    i = PositiveInteger()
    i.setValue(val)
    return i


def _ar_pos_int(val=1):
    i = ARPositiveInteger()
    i.setValue(val)
    return i


def _float(val=1.5):
    f = ARFloat()
    f.setValue(val)
    return f


def _time(val=2.5):
    t = TimeValue()
    t.setValue(val)
    return t


def _literal(val="lit"):
    l = ARLiteral()
    l.setValue(val)
    return l


class TestWritePduToFrameMappings:
    def test_no_mappings(self, writer):
        frame = LinUnconditionalFrame(MockParent(), "frame")
        parent = _parent()
        writer.writePduToFrameMappings(parent, frame)
        assert len(parent) == 0

    def test_with_mappings(self, writer):
        frame = LinUnconditionalFrame(MockParent(), "frame")
        mapping = frame.createPduToFrameMapping("mapping")
        mapping.setPackingByteOrder(_literal("OPAQUE"))
        mapping.setPduRef(_ref("/pdus/p1", dest="PDU"))
        mapping.setStartPosition(_numerical(0))
        parent = _parent()
        writer.writePduToFrameMappings(parent, frame)
        assert parent.find("PDU-TO-FRAME-MAPPINGS") is not None
        mappings_tag = parent.find("PDU-TO-FRAME-MAPPINGS")
        assert mappings_tag.find("PDU-TO-FRAME-MAPPING") is not None
        m = mappings_tag.find("PDU-TO-FRAME-MAPPING")
        assert m.find("PACKING-BYTE-ORDER") is not None
        assert m.find("PDU-REF") is not None
        assert m.find("START-POSITION") is not None


class TestWriteFrame:
    def test_write_frame_with_length(self, writer):
        frame = LinUnconditionalFrame(MockParent(), "frame")
        frame.setFrameLength(_numerical(8))
        parent = _parent()
        writer.writeFrame(parent, frame)
        assert parent.find("SHORT-NAME") is not None
        assert parent.find("FRAME-LENGTH") is not None

    def test_write_frame_without_length(self, writer):
        frame = LinUnconditionalFrame(MockParent(), "frame")
        parent = _parent()
        writer.writeFrame(parent, frame)
        assert parent.find("FRAME-LENGTH") is None


class TestWriteLinUnconditionalFrame:
    def test_creates_lin_unconditional_frame(self, writer):
        frame = LinUnconditionalFrame(MockParent(), "lin_frame")
        frame.setFrameLength(_numerical(4))
        parent = _parent()
        writer.writeLinUnconditionalFrame(parent, frame)
        assert parent.find("LIN-UNCONDITIONAL-FRAME") is not None
        child = parent.find("LIN-UNCONDITIONAL-FRAME")
        assert child.find("SHORT-NAME") is not None
        assert child.find("FRAME-LENGTH") is not None


class TestWriteNmNode:
    def test_basic_nm_node(self, writer):
        node = CanNmNode(MockParent(), "nm_node")
        node.setControllerRef(_ref("/ctrl/c1", dest="CAN-CONTROLLER"))
        node.setNmIfEcuRef(_ref("/ecus/e1", dest="NM-ECU"))
        node.setNmPassiveModeEnabled(_bool(False))
        node.setNmNodeId(_numerical(1))
        parent = _parent()
        writer.writeNmNode(parent, node)
        assert parent.find("SHORT-NAME") is not None
        assert parent.find("CONTROLLER-REF") is not None
        assert parent.find("NM-IF-ECU-REF") is not None
        assert parent.find("NM-PASSIVE-MODE-ENABLED") is not None
        assert parent.find("NM-NODE-ID") is not None

    def test_nm_node_with_pdu_refs(self, writer):
        node = CanNmNode(MockParent(), "nm_node")
        node.addRxNmPduRef(_ref("/rx/p1", dest="NM-PDU"))
        node.addRxNmPduRef(_ref("/rx/p2", dest="NM-PDU"))
        node.addTxNmPduRefs(_ref("/tx/p1", dest="NM-PDU"))
        parent = _parent()
        writer.writeNmNode(parent, node)
        rx_refs = parent.find("RX-NM-PDU-REFS")
        assert rx_refs is not None
        assert len(rx_refs.findall("RX-NM-PDU-REF")) == 2
        tx_refs = parent.find("TX-NM-PDU-REFS")
        assert tx_refs is not None
        assert len(tx_refs.findall("TX-NM-PDU-REF")) == 1


class TestWriteCanNmNode:
    def test_writes_can_nm_node(self, writer):
        node = CanNmNode(MockParent(), "can_nm_node")
        node.setNmCarWakeUpRxEnabled(_bool(True))
        node.setNmMsgCycleOffset(_float(0.1))
        node.setNmMsgReducedTime(_float(0.2))
        rx_range = RxIdentifierRange()
        rx_range.setLowerCanId(_ar_pos_int(0x100))
        rx_range.setUpperCanId(_ar_pos_int(0x1FF))
        node.setNmRangeConfig(rx_range)
        parent = _parent()
        writer.writeCanNmNode(parent, node)
        assert parent.find("CAN-NM-NODE") is not None
        child = parent.find("CAN-NM-NODE")
        assert child.find("NM-CAR-WAKE-UP-RX-ENABLED") is not None
        assert child.find("NM-MSG-CYCLE-OFFSET") is not None
        assert child.find("NM-MSG-REDUCED-TIME") is not None
        assert child.find("NM-RANGE-CONFIG") is not None
        rc = child.find("NM-RANGE-CONFIG")
        assert rc.find("LOWER-CAN-ID") is not None
        assert rc.find("UPPER-CAN-ID") is not None


class TestWriteUdpNmNode:
    def test_writes_udp_nm_node(self, writer):
        node = UdpNmNode(MockParent(), "udp_nm_node")
        node.setNmMsgCycleOffset(_time(0.5))
        parent = _parent()
        writer.writeUdpNmNode(parent, node)
        assert parent.find("UDP-NM-NODE") is not None
        child = parent.find("UDP-NM-NODE")
        assert child.find("NM-MSG-CYCLE-OFFSET") is not None


class TestWriteNmClusterNmNodes:
    def test_empty_nodes(self, writer):
        cluster = CanNmCluster(MockParent(), "cluster")
        parent = _parent()
        writer.writeNmClusterNmNodes(parent, cluster)
        assert len(parent) == 0

    def test_with_can_and_udp_nodes(self, writer):
        cluster = CanNmCluster(MockParent(), "cluster")
        cluster.createCanNmNode("can_node")
        cluster.readUdpNmNode("udp_node")
        parent = _parent()
        writer.writeNmClusterNmNodes(parent, cluster)
        nodes_tag = parent.find("NM-NODES")
        assert nodes_tag is not None
        assert nodes_tag.find("CAN-NM-NODE") is not None
        assert nodes_tag.find("UDP-NM-NODE") is not None


class TestWriteCanNmClusterCoupling:
    def test_basic_coupling(self, writer):
        coupling = CanNmClusterCoupling()
        coupling.setNmBusloadReductionEnabled(_bool(True))
        coupling.setNmImmediateRestartEnabled(_bool(False))
        parent = _parent()
        writer.writeCanNmClusterCoupling(parent, coupling)
        assert parent.find("CAN-NM-CLUSTER-COUPLING") is not None
        child = parent.find("CAN-NM-CLUSTER-COUPLING")
        assert child.find("NM-BUSLOAD-REDUCTION-ENABLED") is not None
        assert child.find("NM-IMMEDIATE-RESTART-ENABLED") is not None

    def test_with_coupled_refs(self, writer):
        coupling = CanNmClusterCoupling()
        coupling.addCoupledClusterRef(_ref("/cl/c1", dest="NM-CLUSTER"))
        coupling.addCoupledClusterRef(_ref("/cl/c2", dest="NM-CLUSTER"))
        parent = _parent()
        writer.writeCanNmClusterCoupling(parent, coupling)
        child = parent.find("CAN-NM-CLUSTER-COUPLING")
        refs_tag = child.find("COUPLED-CLUSTER-REFS")
        assert refs_tag is not None
        assert len(refs_tag.findall("COUPLED-CLUSTER-REF")) == 2


class TestWriteUdpNmClusterCoupling:
    def test_basic_coupling(self, writer):
        coupling = UdpNmClusterCoupling()
        coupling.setNmImmediateRestartEnabled(_bool(True))
        parent = _parent()
        writer.writeUdpNmClusterCoupling(parent, coupling)
        assert parent.find("UDP-NM-CLUSTER-COUPLING") is not None
        child = parent.find("UDP-NM-CLUSTER-COUPLING")
        assert child.find("NM-IMMEDIATE-RESTART-ENABLED") is not None

    def test_with_coupled_refs(self, writer):
        coupling = UdpNmClusterCoupling()
        coupling.addCoupledClusterRef(_ref("/cl/u1", dest="NM-CLUSTER"))
        parent = _parent()
        writer.writeUdpNmClusterCoupling(parent, coupling)
        child = parent.find("UDP-NM-CLUSTER-COUPLING")
        refs_tag = child.find("COUPLED-CLUSTER-REFS")
        assert refs_tag is not None
        assert len(refs_tag.findall("COUPLED-CLUSTER-REF")) == 1


class TestWriteNmConfigNmClusterCouplings:
    def test_empty(self, writer):
        config = NmConfig(MockParent(), "nm_config")
        parent = _parent()
        writer.writeNmConfigNmClusterCouplings(parent, config)
        assert len(parent) == 0

    def test_with_couplings(self, writer):
        config = NmConfig(MockParent(), "nm_config")
        can_c = CanNmClusterCoupling()
        can_c.setNmBusloadReductionEnabled(_bool(True))
        udp_c = UdpNmClusterCoupling()
        udp_c.setNmImmediateRestartEnabled(_bool(True))
        config.addNmClusterCouplings(can_c)
        config.addNmClusterCouplings(udp_c)
        parent = _parent()
        writer.writeNmConfigNmClusterCouplings(parent, config)
        couplings_tag = parent.find("NM-CLUSTER-COUPLINGS")
        assert couplings_tag is not None
        assert couplings_tag.find("CAN-NM-CLUSTER-COUPLING") is not None
        assert couplings_tag.find("UDP-NM-CLUSTER-COUPLING") is not None


class TestWriteNmCluster:
    def test_basic_cluster(self, writer):
        cluster = CanNmCluster(MockParent(), "cluster")
        cluster.setCommunicationClusterRef(_ref("/cc/c1"))
        cluster.setNmChannelId(_numerical(2))
        cluster.setNmChannelSleepMaster(_bool(True))
        cluster.setNmSynchronizingNetwork(_bool(False))
        parent = _parent()
        writer.writeNmCluster(parent, cluster)
        assert parent.find("SHORT-NAME") is not None
        assert parent.find("COMMUNICATION-CLUSTER-REF") is not None
        assert parent.find("NM-CHANNEL-ID") is not None
        assert parent.find("NM-CHANNEL-SLEEP-MASTER") is not None
        assert parent.find("NM-SYNCHRONIZING-NETWORK") is not None


class TestWriteCanNmCluster:
    def test_full_cluster(self, writer):
        cluster = CanNmCluster(MockParent(), "can_cluster")
        cluster.setCommunicationClusterRef(_ref("/cc/c1"))
        cluster.setNmChannelId(_numerical(1))
        cluster.setNmChannelSleepMaster(_bool(True))
        cluster.setNmSynchronizingNetwork(_bool(True))
        cluster.setNmBusloadReductionActive(_bool(True))
        cluster.setNmCarWakeUpRxEnabled(_bool(False))
        cluster.setNmCbvPosition(_numerical(3))
        cluster.setNmChannelActive(_bool(True))
        cluster.setNmImmediateNmCycleTime(_float(0.01))
        cluster.setNmImmediateNmTransmissions(_numerical(5))
        cluster.setNmMessageTimeoutTime(_float(1.0))
        cluster.setNmMsgCycleTime(_float(0.1))
        cluster.setNmNetworkTimeout(_float(2.0))
        cluster.setNmNidPosition(_numerical(4))
        cluster.setNmRemoteSleepIndicationTime(_float(1.5))
        cluster.setNmRepeatMessageTime(_float(0.5))
        cluster.setNmUserDataLength(_numerical(8))
        cluster.setNmWaitBusSleepTime(_float(0.2))
        parent = _parent()
        writer.writeCanNmCluster(parent, cluster)
        assert parent.find("CAN-NM-CLUSTER") is not None
        c = parent.find("CAN-NM-CLUSTER")
        assert c.find("NM-BUSLOAD-REDUCTION-ACTIVE") is not None
        assert c.find("NM-CAR-WAKE-UP-RX-ENABLED") is not None
        assert c.find("NM-CBV-POSITION") is not None
        assert c.find("NM-CHANNEL-ACTIVE") is not None
        assert c.find("NM-IMMEDIATE-NM-CYCLE-TIME") is not None
        assert c.find("NM-IMMEDIATE-NM-TRANSMISSIONS") is not None
        assert c.find("NM-MESSAGE-TIMEOUT-TIME") is not None
        assert c.find("NM-MSG-CYCLE-TIME") is not None
        assert c.find("NM-NETWORK-TIMEOUT") is not None
        assert c.find("NM-NID-POSITION") is not None
        assert c.find("NM-REMOTE-SLEEP-INDICATION-TIME") is not None
        assert c.find("NM-REPEAT-MESSAGE-TIME") is not None
        assert c.find("NM-USER-DATA-LENGTH") is not None
        assert c.find("NM-WAIT-BUS-SLEEP-TIME") is not None


class TestWriteUdpNmCluster:
    def test_full_cluster(self, writer):
        cluster = UdpNmCluster(MockParent(), "udp_cluster")
        cluster.setCommunicationClusterRef(_ref("/cc/u1"))
        cluster.setNmChannelId(_numerical(2))
        cluster.setNmChannelSleepMaster(_bool(False))
        cluster.setNmSynchronizingNetwork(_bool(True))
        cluster.setNmCbvPosition(_int(2))
        cluster.setNmChannelActive(_bool(True))
        cluster.setNmImmediateNmCycleTime(_time(0.05))
        cluster.setNmImmediateNmTransmissions(_pos_int(3))
        cluster.setNmMessageTimeoutTime(_time(1.0))
        cluster.setNmMsgCycleTime(_time(0.1))
        cluster.setNmNetworkTimeout(_time(2.0))
        cluster.setNmNidPosition(_int(6))
        cluster.setNmRemoteSleepIndicationTime(_time(1.5))
        cluster.setNmRepeatMessageTime(_time(0.5))
        cluster.setNmWaitBusSleepTime(_time(0.2))
        cluster.setVlanRef(_ref("/vlan/v1", dest="VLAN"))
        parent = _parent()
        writer.writeUdpNmCluster(parent, cluster)
        assert parent.find("UDP-NM-CLUSTER") is not None
        c = parent.find("UDP-NM-CLUSTER")
        assert c.find("NM-CBV-POSITION") is not None
        assert c.find("NM-CHANNEL-ACTIVE") is not None
        assert c.find("NM-IMMEDIATE-NM-CYCLE-TIME") is not None
        assert c.find("NM-IMMEDIATE-NM-TRANSMISSIONS") is not None
        assert c.find("NM-MESSAGE-TIMEOUT-TIME") is not None
        assert c.find("NM-MSG-CYCLE-TIME") is not None
        assert c.find("NM-NETWORK-TIMEOUT") is not None
        assert c.find("NM-NID-POSITION") is not None
        assert c.find("NM-REMOTE-SLEEP-INDICATION-TIME") is not None
        assert c.find("NM-REPEAT-MESSAGE-TIME") is not None
        assert c.find("NM-WAIT-BUS-SLEEP-TIME") is not None
        assert c.find("VLAN-REF") is not None


class TestWriteNmConfigNmClusters:
    def test_empty(self, writer):
        config = NmConfig(MockParent(), "nm_config")
        parent = _parent()
        writer.writeNmConfigNmClusters(parent, config)
        assert len(parent) == 0

    def test_with_clusters(self, writer):
        config = NmConfig(MockParent(), "nm_config")
        config.createCanNmCluster("can_cluster")
        config.createUdpNmCluster("udp_cluster")
        parent = _parent()
        writer.writeNmConfigNmClusters(parent, config)
        clusters_tag = parent.find("NM-CLUSTERS")
        assert clusters_tag is not None
        assert clusters_tag.find("CAN-NM-CLUSTER") is not None
        assert clusters_tag.find("UDP-NM-CLUSTER") is not None


class TestWriteUdpNmEcu:
    def test_none(self, writer):
        parent = _parent()
        writer.writeUdpNmEcu(parent, None)
        assert len(parent) == 0

    def test_with_ecu(self, writer):
        ecu = UdpNmEcu()
        ecu.setNmSynchronizationPointEnabled(_bool(True))
        parent = _parent()
        writer.writeUdpNmEcu(parent, ecu)
        assert parent.find("UDP-NM-ECU") is not None
        assert parent.find("UDP-NM-ECU").find(
            "NM-SYNCHRONIZATION-POINT-ENABLED") is not None


class TestWriteBusDependentNmEcus:
    def test_empty(self, writer):
        nm_ecu = NmEcu(MockParent(), "nm_ecu")
        parent = _parent()
        writer.writeBusDependentNmEcus(parent, nm_ecu)
        assert len(parent) == 0

    def test_with_udp_nm_ecu(self, writer):
        nm_ecu = NmEcu(MockParent(), "nm_ecu")
        nm_ecu.addBusDependentNmEcu(UdpNmEcu())
        parent = _parent()
        writer.writeBusDependentNmEcus(parent, nm_ecu)
        assert parent.find("BUS-DEPENDENT-NM-ECUS") is not None
        deps = parent.find("BUS-DEPENDENT-NM-ECUS")
        assert deps.find("UDP-NM-ECU") is not None


class TestWriteNmEcu:
    def test_full_nm_ecu(self, writer):
        nm_ecu = NmEcu(MockParent(), "nm_ecu")
        nm_ecu.setEcuInstanceRef(_ref("/ecu/i1", dest="ECU-INSTANCE"))
        nm_ecu.setNmBusSynchronizationEnabled(_bool(True))
        nm_ecu.setNmComControlEnabled(_bool(True))
        nm_ecu.setNmNodeDetectionEnabled(_bool(False))
        nm_ecu.setNmNodeIdEnabled(_bool(True))
        nm_ecu.setNmPduRxIndicationEnabled(_bool(False))
        nm_ecu.setNmRemoteSleepIndEnabled(_bool(True))
        nm_ecu.setNmRepeatMsgIndEnabled(_bool(False))
        nm_ecu.setNmStateChangeIndEnabled(_bool(True))
        nm_ecu.setNmUserDataEnabled(_bool(False))
        parent = _parent()
        writer.writeNmEcu(parent, nm_ecu)
        assert parent.find("NM-ECU") is not None
        c = parent.find("NM-ECU")
        assert c.find("ECU-INSTANCE-REF") is not None
        assert c.find("NM-BUS-SYNCHRONIZATION-ENABLED") is not None
        assert c.find("NM-COM-CONTROL-ENABLED") is not None
        assert c.find("NM-NODE-DETECTION-ENABLED") is not None
        assert c.find("NM-NODE-ID-ENABLED") is not None
        assert c.find("NM-PDU-RX-INDICATION-ENABLED") is not None
        assert c.find("NM-REMOTE-SLEEP-IND-ENABLED") is not None
        assert c.find("NM-REPEAT-MSG-IND-ENABLED") is not None
        assert c.find("NM-STATE-CHANGE-IND-ENABLED") is not None
        assert c.find("NM-USER-DATA-ENABLED") is not None

    def test_nm_ecu_with_dependent(self, writer):
        nm_ecu = NmEcu(MockParent(), "nm_ecu")
        udp = UdpNmEcu()
        udp.setNmSynchronizationPointEnabled(_bool(True))
        nm_ecu.addBusDependentNmEcu(udp)
        parent = _parent()
        writer.writeNmEcu(parent, nm_ecu)
        c = parent.find("NM-ECU")
        assert c.find("BUS-DEPENDENT-NM-ECUS") is not None


class TestWriteNmConfigNmIfEcus:
    def test_empty(self, writer):
        config = NmConfig(MockParent(), "nm_config")
        parent = _parent()
        writer.writeNmConfigNmIfEcus(parent, config)
        assert len(parent) == 0

    def test_with_ecus(self, writer):
        config = NmConfig(MockParent(), "nm_config")
        config.createNmEcu("nm_ecu_1")
        parent = _parent()
        writer.writeNmConfigNmIfEcus(parent, config)
        assert parent.find("NM-IF-ECUS") is not None
        assert parent.find("NM-IF-ECUS").find("NM-ECU") is not None


class TestWriteNmConfig:
    def test_full_config(self, writer):
        config = NmConfig(MockParent(), "nm_config")
        config.createCanNmCluster("can_cluster")
        config.createUdpNmCluster("udp_cluster")
        can_c = CanNmClusterCoupling()
        can_c.setNmBusloadReductionEnabled(_bool(True))
        config.addNmClusterCouplings(can_c)
        config.createNmEcu("nm_ecu")
        parent = _parent()
        writer.writeNmConfig(parent, config)
        assert parent.find("NM-CONFIG") is not None
        cfg = parent.find("NM-CONFIG")
        assert cfg.find("SHORT-NAME") is not None
        assert cfg.find("NM-CLUSTERS") is not None
        assert cfg.find("NM-CLUSTER-COUPLINGS") is not None
        assert cfg.find("NM-IF-ECUS") is not None
