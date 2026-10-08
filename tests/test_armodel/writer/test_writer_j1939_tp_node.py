"""Tests for the writeJ1939TpNode handler (R23-11 J1939TpNode, Table 6.270, p.626)."""

import xml.etree.cElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols import J1939TpNode
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"

XSD_CHILD_ORDER = [
    "CONNECTOR-REF",
    "TP-ADDRESS-REF",
]


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _ref(value):
    ref = RefType()
    ref.setValue(value)
    return ref


def _fill_node(node: J1939TpNode) -> J1939TpNode:
    node.setConnectorRef(_ref("/Topology/Connector1"))
    node.setTpAddressRef(_ref("/TpConfigs/Config1/TpAddress1"))
    return node


def _with_ns(parent: ET.Element) -> ET.Element:
    return ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


class TestWriteJ1939TpNode:
    def test_children_in_xsd_order(self):
        node = _fill_node(J1939TpNode(AUTOSAR.getInstance().createARPackage("TpConfigs"), "Node1"))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeJ1939TpNode(parent, node)

        child = parent.find("J-1939-TP-NODE")
        assert child is not None
        child_tags = [element.tag for element in child if element.tag != "SHORT-NAME"]
        assert child_tags == XSD_CHILD_ORDER

    def test_empty_node_writes_no_elements(self):
        node = J1939TpNode(AUTOSAR.getInstance().createARPackage("TpConfigs"), "Node1")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeJ1939TpNode(parent, node)

        child = parent.find("J-1939-TP-NODE")
        assert child is not None
        assert [element.tag for element in child if element.tag != "SHORT-NAME"] == []

    def test_round_trip(self):
        node = _fill_node(J1939TpNode(AUTOSAR.getInstance().createARPackage("TpConfigs"), "Node1"))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeJ1939TpNode(parent, node)

        reloaded = J1939TpNode(AUTOSAR.getInstance().createARPackage("TpConfigs"), "Node1")
        ARXMLParser().readJ1939TpNode(_with_ns(parent)[0], reloaded)

        assert reloaded.getShortName() == "Node1"
        assert reloaded.getConnectorRef().getValue() == "/Topology/Connector1"
        assert reloaded.getTpAddressRef().getValue() == "/TpConfigs/Config1/TpAddress1"

    def test_round_trip_empty(self):
        node = J1939TpNode(AUTOSAR.getInstance().createARPackage("TpConfigs"), "Node1")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeJ1939TpNode(parent, node)

        reloaded = J1939TpNode(AUTOSAR.getInstance().createARPackage("TpConfigs"), "Node1")
        ARXMLParser().readJ1939TpNode(_with_ns(parent)[0], reloaded)

        assert reloaded.getConnectorRef() is None
        assert reloaded.getTpAddressRef() is None
