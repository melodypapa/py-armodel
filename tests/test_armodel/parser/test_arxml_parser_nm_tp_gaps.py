"""Tests for NM and LIN TP handler gaps."""
import logging
import xml.etree.ElementTree as ET
import pytest
from armodel.models import AUTOSAR
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def parser():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    return ARXMLParser()


@pytest.fixture
def warning_parser():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    return ARXMLParser(options={"warning": True})


def _snip(inner: str, root_tag: str = "ROOT") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


def _autosar_root():
    return AUTOSAR.getInstance()


class TestUdpNmEcuHandler:
    def test_readUdpNmEcu_sets_nmSynchronizationPointEnabled(self, parser):
        from armodel.models import UdpNmEcu
        ecu = UdpNmEcu()
        element = _snip(
            "<NM-SYNCHRONIZATION-POINT-ENABLED>true</NM-SYNCHRONIZATION-POINT-ENABLED>",
            root_tag="UDP-NM-ECU",
        )
        parser.readUdpNmEcu(element, ecu)
        assert ecu.getNmSynchronizationPointEnabled() is not None
        assert ecu.getNmSynchronizationPointEnabled().getValue() is True

    def test_readUdpNmEcu_without_synchronizationPointEnabled(self, parser):
        from armodel.models import UdpNmEcu
        ecu = UdpNmEcu()
        element = _snip("", root_tag="UDP-NM-ECU")
        parser.readUdpNmEcu(element, ecu)
        assert ecu.getNmSynchronizationPointEnabled() is None


class TestBusDependentNmEcusHandler:
    def test_readBusDependentNmEcus_creates_udpNmEcu(self, parser):
        from armodel.models import NmEcu
        from armodel.models import NmConfig
        config = NmConfig(parent=_autosar_root(), short_name="nmConfig")
        nm_ecu = NmEcu(parent=config, short_name="ecu")
        element = _snip(
            "<BUS-DEPENDENT-NM-ECUS>"
            "<UDP-NM-ECU>"
            "<NM-SYNCHRONIZATION-POINT-ENABLED>true</NM-SYNCHRONIZATION-POINT-ENABLED>"
            "</UDP-NM-ECU>"
            "</BUS-DEPENDENT-NM-ECUS>",
            root_tag="NM-ECU",
        )
        parser.readBusDependentNmEcus(element, nm_ecu)
        dependents = nm_ecu.getBusDependentNmEcus()
        assert len(dependents) == 1
        assert dependents[0].getNmSynchronizationPointEnabled() is not None
        assert dependents[0].getNmSynchronizationPointEnabled().getValue() is True

    def test_readBusDependentNmEcus_unsupported_warns(
        self, warning_parser, caplog
    ):
        from armodel.models import NmEcu
        from armodel.models import NmConfig
        config = NmConfig(parent=_autosar_root(), short_name="nmConfig")
        nm_ecu = NmEcu(parent=config, short_name="ecu")
        element = _snip(
            "<BUS-DEPENDENT-NM-ECUS><BAD/></BUS-DEPENDENT-NM-ECUS>",
            root_tag="NM-ECU",
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readBusDependentNmEcus(element, nm_ecu)
        assert any(
            "Unsupported BusDependentNmEcu" in r.getMessage()
            for r in caplog.records
        )
        assert len(nm_ecu.getBusDependentNmEcus()) == 0

    def test_readBusDependentNmEcus_unsupported_raises(self, parser):
        from armodel.models import NmEcu
        from armodel.models import NmConfig
        config = NmConfig(parent=_autosar_root(), short_name="nmConfig")
        nm_ecu = NmEcu(parent=config, short_name="ecu")
        element = _snip(
            "<BUS-DEPENDENT-NM-ECUS><BAD/></BUS-DEPENDENT-NM-ECUS>",
            root_tag="NM-ECU",
        )
        with pytest.raises(NotImplementedError):
            parser.readBusDependentNmEcus(element, nm_ecu)


class TestLinTpConfigTpConnectionsHandler:
    def test_readLinTpConfigTpConnections_creates_connection(self, parser):
        from armodel.models import LinTpConfig
        config = LinTpConfig(parent=_autosar_root(), short_name="linTp")
        element = _snip(
            "<TP-CONNECTIONS>"
            "<LIN-TP-CONNECTION>"
            "<IDENT><SHORT-NAME>conn</SHORT-NAME></IDENT>"
            "<TIMEOUT-AS>0.1</TIMEOUT-AS>"
            "</LIN-TP-CONNECTION>"
            "</TP-CONNECTIONS>",
            root_tag="LIN-TP-CONFIG",
        )
        parser.readLinTpConfigTpConnections(element, config)
        connections = config.getTpConnections()
        assert len(connections) == 1
        assert connections[0].getTimeoutAs() is not None
        assert connections[0].getTimeoutAs().getValue() == 0.1

    def test_readLinTpConfigTpConnections_unsupported_warns(
        self, warning_parser, caplog
    ):
        from armodel.models import LinTpConfig
        config = LinTpConfig(parent=_autosar_root(), short_name="linTp")
        element = _snip(
            "<TP-CONNECTIONS><BAD/></TP-CONNECTIONS>",
            root_tag="LIN-TP-CONFIG",
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readLinTpConfigTpConnections(element, config)
        assert any(
            "Unsupported TpConnection" in r.getMessage()
            for r in caplog.records
        )
        assert len(config.getTpConnections()) == 0

    def test_readLinTpConfigTpConnections_unsupported_raises(self, parser):
        from armodel.models import LinTpConfig
        config = LinTpConfig(parent=_autosar_root(), short_name="linTp")
        element = _snip(
            "<TP-CONNECTIONS><BAD/></TP-CONNECTIONS>",
            root_tag="LIN-TP-CONFIG",
        )
        with pytest.raises(NotImplementedError):
            parser.readLinTpConfigTpConnections(element, config)

    def test_readLinTpConfigTpConnections_empty(self, parser):
        from armodel.models import LinTpConfig
        config = LinTpConfig(parent=_autosar_root(), short_name="linTp")
        element = _snip(
            "<TP-CONNECTIONS></TP-CONNECTIONS>",
            root_tag="LIN-TP-CONFIG",
        )
        parser.readLinTpConfigTpConnections(element, config)
        assert len(config.getTpConnections()) == 0


class TestLinTpNodeHandler:
    def test_readLinTpNode_sets_connectorRef(self, parser):
        from armodel.models import LinTpNode
        from armodel.models import LinTpConfig
        config = LinTpConfig(parent=_autosar_root(), short_name="linTp")
        node = LinTpNode(parent=config, short_name="node")
        element = _snip(
            "<SHORT-NAME>node</SHORT-NAME>"
            "<CONNECTOR-REF DEST='COMMUNICATION-CONNECTOR'>/conn</CONNECTOR-REF>",
            root_tag="LIN-TP-NODE",
        )
        parser.readLinTpNode(element, node)
        assert node.getConnectorRef() is not None
        assert node.getConnectorRef().getValue() == "/conn"

    def test_readLinTpNode_sets_dropNotRequestedNad(self, parser):
        from armodel.models import LinTpNode
        from armodel.models import LinTpConfig
        config = LinTpConfig(parent=_autosar_root(), short_name="linTp")
        node = LinTpNode(parent=config, short_name="node")
        element = _snip(
            "<SHORT-NAME>node</SHORT-NAME>"
            "<DROP-NOT-REQUESTED-NAD>true</DROP-NOT-REQUESTED-NAD>",
            root_tag="LIN-TP-NODE",
        )
        parser.readLinTpNode(element, node)
        assert node.getDropNotRequestedNad() is not None
        assert node.getDropNotRequestedNad().getValue() is True

    def test_readLinTpNode_sets_p2Max(self, parser):
        from armodel.models import LinTpNode
        from armodel.models import LinTpConfig
        config = LinTpConfig(parent=_autosar_root(), short_name="linTp")
        node = LinTpNode(parent=config, short_name="node")
        element = _snip(
            "<SHORT-NAME>node</SHORT-NAME>"
            "<P-2-MAX>0.05</P-2-MAX>",
            root_tag="LIN-TP-NODE",
        )
        parser.readLinTpNode(element, node)
        assert node.getP2Max() is not None
        assert node.getP2Max().getValue() == 0.05

    def test_readLinTpNode_sets_p2Timing(self, parser):
        from armodel.models import LinTpNode
        from armodel.models import LinTpConfig
        config = LinTpConfig(parent=_autosar_root(), short_name="linTp")
        node = LinTpNode(parent=config, short_name="node")
        element = _snip(
            "<SHORT-NAME>node</SHORT-NAME>"
            "<P-2-TIMING>0.01</P-2-TIMING>",
            root_tag="LIN-TP-NODE",
        )
        parser.readLinTpNode(element, node)
        assert node.getP2Timing() is not None
        assert node.getP2Timing().getValue() == 0.01

    def test_readLinTpNode_sets_tpAddressRef(self, parser):
        from armodel.models import LinTpNode
        from armodel.models import LinTpConfig
        config = LinTpConfig(parent=_autosar_root(), short_name="linTp")
        node = LinTpNode(parent=config, short_name="node")
        element = _snip(
            "<SHORT-NAME>node</SHORT-NAME>"
            "<TP-ADDRESS-REF DEST='TP-ADDRESS'>/addr</TP-ADDRESS-REF>",
            root_tag="LIN-TP-NODE",
        )
        parser.readLinTpNode(element, node)
        assert node.getTpAddressRef() is not None
        assert node.getTpAddressRef().getValue() == "/addr"

    def test_readLinTpNode_sets_all_properties(self, parser):
        from armodel.models import LinTpNode
        from armodel.models import LinTpConfig
        config = LinTpConfig(parent=_autosar_root(), short_name="linTp")
        node = LinTpNode(parent=config, short_name="node")
        element = _snip(
            "<SHORT-NAME>node</SHORT-NAME>"
            "<CONNECTOR-REF DEST='COMMUNICATION-CONNECTOR'>/conn</CONNECTOR-REF>"
            "<DROP-NOT-REQUESTED-NAD>false</DROP-NOT-REQUESTED-NAD>"
            "<P-2-MAX>0.05</P-2-MAX>"
            "<P-2-TIMING>0.01</P-2-TIMING>"
            "<TP-ADDRESS-REF DEST='TP-ADDRESS'>/addr</TP-ADDRESS-REF>",
            root_tag="LIN-TP-NODE",
        )
        parser.readLinTpNode(element, node)
        assert node.getShortName() == "node"
        assert node.getConnectorRef().getValue() == "/conn"
        assert node.getDropNotRequestedNad().getValue() is False
        assert node.getP2Max().getValue() == 0.05
        assert node.getP2Timing().getValue() == 0.01
        assert node.getTpAddressRef().getValue() == "/addr"

    def test_readLinTpNode_without_optional_fields(self, parser):
        from armodel.models import LinTpNode
        from armodel.models import LinTpConfig
        config = LinTpConfig(parent=_autosar_root(), short_name="linTp")
        node = LinTpNode(parent=config, short_name="node")
        element = _snip(
            "<SHORT-NAME>node</SHORT-NAME>",
            root_tag="LIN-TP-NODE",
        )
        parser.readLinTpNode(element, node)
        assert node.getShortName() == "node"
        assert node.getConnectorRef() is None
        assert node.getDropNotRequestedNad() is None
        assert node.getP2Max() is None
        assert node.getP2Timing() is None
        assert node.getTpAddressRef() is None


class TestLinTpConfigTpNodesHandler:
    def test_readLinTpConfigTpNodes_creates_node(self, parser):
        from armodel.models import LinTpConfig
        config = LinTpConfig(parent=_autosar_root(), short_name="linTp")
        element = _snip(
            "<TP-NODES>"
            "<LIN-TP-NODE>"
            "<SHORT-NAME>node</SHORT-NAME>"
            "<P-2-MAX>0.05</P-2-MAX>"
            "</LIN-TP-NODE>"
            "</TP-NODES>",
            root_tag="LIN-TP-CONFIG",
        )
        parser.readLinTpConfigTpNodes(element, config)
        nodes = config.getTpNodes()
        assert len(nodes) == 1
        assert nodes[0].getShortName() == "node"
        assert nodes[0].getP2Max() is not None
        assert nodes[0].getP2Max().getValue() == 0.05

    def test_readLinTpConfigTpNodes_unsupported_warns(
        self, warning_parser, caplog
    ):
        from armodel.models import LinTpConfig
        config = LinTpConfig(parent=_autosar_root(), short_name="linTp")
        element = _snip(
            "<TP-NODES><BAD/></TP-NODES>",
            root_tag="LIN-TP-CONFIG",
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readLinTpConfigTpNodes(element, config)
        assert any(
            "Unsupported TpNode" in r.getMessage()
            for r in caplog.records
        )
        assert len(config.getTpNodes()) == 0

    def test_readLinTpConfigTpNodes_unsupported_raises(self, parser):
        from armodel.models import LinTpConfig
        config = LinTpConfig(parent=_autosar_root(), short_name="linTp")
        element = _snip(
            "<TP-NODES><BAD/></TP-NODES>",
            root_tag="LIN-TP-CONFIG",
        )
        with pytest.raises(NotImplementedError):
            parser.readLinTpConfigTpNodes(element, config)

    def test_readLinTpConfigTpNodes_empty(self, parser):
        from armodel.models import LinTpConfig
        config = LinTpConfig(parent=_autosar_root(), short_name="linTp")
        element = _snip(
            "<TP-NODES></TP-NODES>",
            root_tag="LIN-TP-CONFIG",
        )
        parser.readLinTpConfigTpNodes(element, config)
        assert len(config.getTpNodes()) == 0

    def test_readLinTpConfigTpNodes_multiple_nodes(self, parser):
        from armodel.models import LinTpConfig
        config = LinTpConfig(parent=_autosar_root(), short_name="linTp")
        element = _snip(
            "<TP-NODES>"
            "<LIN-TP-NODE>"
            "<SHORT-NAME>node1</SHORT-NAME>"
            "<P-2-MAX>0.05</P-2-MAX>"
            "</LIN-TP-NODE>"
            "<LIN-TP-NODE>"
            "<SHORT-NAME>node2</SHORT-NAME>"
            "<P-2-TIMING>0.02</P-2-TIMING>"
            "</LIN-TP-NODE>"
            "</TP-NODES>",
            root_tag="LIN-TP-CONFIG",
        )
        parser.readLinTpConfigTpNodes(element, config)
        nodes = config.getTpNodes()
        assert len(nodes) == 2
        assert nodes[0].getShortName() == "node1"
        assert nodes[1].getShortName() == "node2"
