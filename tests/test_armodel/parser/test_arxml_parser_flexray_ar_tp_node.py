"""Tests for the readFlexrayArTpNode handler (R23-11 FlexrayArTpNode, Table 6.247, p.603)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols import FlexrayArTpConfig, FlexrayArTpNode
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


def _snip(inner: str, root_tag: str = "ROOT") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


class TestReadFlexrayArTpNode:
    """Tests for readFlexrayArTpNode (R23-11 FlexrayArTpNode, Table 6.247, p.603)."""

    def test_read_full_node(self, parser):
        element = _snip(
            """
                <SHORT-NAME>Node1</SHORT-NAME>
                <CONNECTOR-REFS>
                    <CONNECTOR-REF DEST="FLEXRAY-COMMUNICATION-CONNECTOR">/Topology/C1</CONNECTOR-REF>
                    <CONNECTOR-REF DEST="FLEXRAY-COMMUNICATION-CONNECTOR">/Topology/C2</CONNECTOR-REF>
                </CONNECTOR-REFS>
                <TP-ADDRESS-REF DEST="TP-ADDRESS">/TpAddresses/Addr1</TP-ADDRESS-REF>
            """,
            root_tag="FLEXRAY-AR-TP-NODE",
        )
        package = AUTOSAR.getInstance().createARPackage("TpConfigs")
        node = FlexrayArTpNode(package, "Node1")
        parser.readFlexrayArTpNode(element, node)
        refs = node.getConnectorRefs()
        assert len(refs) == 2
        assert refs[0].getValue() == "/Topology/C1"
        assert refs[0].getDest() == "FLEXRAY-COMMUNICATION-CONNECTOR"
        assert refs[1].getValue() == "/Topology/C2"
        assert node.getTpAddressRef() is not None
        assert node.getTpAddressRef().getValue() == "/TpAddresses/Addr1"
        assert node.getTpAddressRef().getDest() == "TP-ADDRESS"
        assert node.getShortName() == "Node1"

    def test_read_empty_node(self, parser):
        element = _snip(
            """
                <SHORT-NAME>Node1</SHORT-NAME>
            """,
            root_tag="FLEXRAY-AR-TP-NODE",
        )
        package = AUTOSAR.getInstance().createARPackage("TpConfigs")
        node = FlexrayArTpNode(package, "Node1")
        parser.readFlexrayArTpNode(element, node)
        assert node.getConnectorRefs() == []
        assert node.getTpAddressRef() is None

    def test_read_via_config_dispatch(self, parser):
        element = _snip(
            """
                <SHORT-NAME>Config1</SHORT-NAME>
                <TP-NODES>
                    <FLEXRAY-AR-TP-NODE>
                        <SHORT-NAME>Node1</SHORT-NAME>
                        <CONNECTOR-REFS>
                            <CONNECTOR-REF DEST="FLEXRAY-COMMUNICATION-CONNECTOR">/Topology/C1</CONNECTOR-REF>
                        </CONNECTOR-REFS>
                        <TP-ADDRESS-REF DEST="TP-ADDRESS">/TpAddresses/Addr1</TP-ADDRESS-REF>
                    </FLEXRAY-AR-TP-NODE>
                </TP-NODES>
            """,
            root_tag="FLEXRAY-AR-TP-CONFIG",
        )
        package = AUTOSAR.getInstance().createARPackage("TpConfigs")
        config = FlexrayArTpConfig(package, "Config1")
        parser.readFlexrayArTpConfig(element, config)
        nodes = config.getTpNodes()
        assert len(nodes) == 1
        assert nodes[0].getShortName() == "Node1"
        assert len(nodes[0].getConnectorRefs()) == 1
        assert nodes[0].getTpAddressRef().getValue() == "/TpAddresses/Addr1"
