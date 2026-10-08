"""Tests for the writeFlexrayArTpNode handler (R23-11 FlexrayArTpNode, Table 6.247, p.603)."""

import xml.etree.cElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols import FlexrayArTpConfig, FlexrayArTpNode
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def writer():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    return ARXMLWriter()


@pytest.fixture
def parser():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    return ARXMLParser()


def _parent():
    return ET.Element("PARENT")


def _ref(value, dest):
    ref = RefType()
    ref.setDest(dest)
    ref.setValue(value)
    return ref


def _node(short_name: str) -> FlexrayArTpNode:
    package = AUTOSAR.getInstance().createARPackage("TpConfigs")
    return FlexrayArTpNode(package, short_name)


class TestWriteFlexrayArTpNode:
    """Tests for writeFlexrayArTpNode (R23-11 FlexrayArTpNode, Table 6.247, p.603)."""

    def test_write_refs_wrapper_in_xsd_order(self, writer):
        node = _node("Node1")
        node.addConnectorRef(_ref("/Topology/C1", "FLEXRAY-COMMUNICATION-CONNECTOR"))
        node.setTpAddressRef(_ref("/TpAddresses/Addr1", "TP-ADDRESS"))
        parent = _parent()
        writer.writeFlexrayArTpNode(parent, node)
        child = parent.find("FLEXRAY-AR-TP-NODE")
        assert child is not None
        child_tags = [element.tag for element in child if element.tag != "SHORT-NAME"]
        assert child_tags == ["CONNECTOR-REFS", "TP-ADDRESS-REF"]
        refs = child.findall("CONNECTOR-REFS/CONNECTOR-REF")
        assert len(refs) == 1
        assert refs[0].text == "/Topology/C1"
        assert refs[0].get("DEST") == "FLEXRAY-COMMUNICATION-CONNECTOR"
        assert child.find("TP-ADDRESS-REF").text == "/TpAddresses/Addr1"

    def test_empty_node_writes_no_wrappers(self, writer):
        node = _node("Node1")
        parent = _parent()
        writer.writeFlexrayArTpNode(parent, node)
        child = parent.find("FLEXRAY-AR-TP-NODE")
        assert child is not None
        child_tags = [element.tag for element in child if element.tag != "SHORT-NAME"]
        assert child_tags == []

    def test_round_trip_via_config(self, writer, parser):
        config = FlexrayArTpConfig(AUTOSAR.getInstance().createARPackage("TpConfigs"), "Config1")
        node = config.createFlexrayArTpNode("Node1")
        node.addConnectorRef(_ref("/Topology/C1", "FLEXRAY-COMMUNICATION-CONNECTOR"))
        node.setTpAddressRef(_ref("/TpAddresses/Addr1", "TP-ADDRESS"))

        parent = _parent()
        writer.writeFlexrayArTpConfig(parent, config)
        xml_text = ET.tostring(parent).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1)
        assert "CONNECTOR-REFS" in xml_text

        reparsed = ET.fromstring(xml_text)[0]
        config2 = FlexrayArTpConfig(AUTOSAR.getInstance().createARPackage("TpConfigs"), "Config1")
        parser.readFlexrayArTpConfig(reparsed, config2)
        nodes = config2.getTpNodes()
        assert len(nodes) == 1
        assert nodes[0].getShortName() == "Node1"
        refs = nodes[0].getConnectorRefs()
        assert len(refs) == 1
        assert refs[0].getValue() == "/Topology/C1"
        assert refs[0].getDest() == "FLEXRAY-COMMUNICATION-CONNECTOR"
        assert nodes[0].getTpAddressRef().getValue() == "/TpAddresses/Addr1"
        assert nodes[0].getTpAddressRef().getDest() == "TP-ADDRESS"
