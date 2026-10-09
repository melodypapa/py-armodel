"""Tests for the readJ1939TpNode handler (R23-11 J1939TpNode, Table 6.270, p.626).

XSD element order (J-1939-TP-NODE group, AUTOSAR_00052.xsd l.75910): CONNECTOR-REF,
TP-ADDRESS-REF, then VARIATION-POINT (sequenceOffset 10000, last).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols import J1939TpNode
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"

NODE_XML = (
    "<J-1939-TP-NODE>"
    "<SHORT-NAME>Node1</SHORT-NAME>"
    '<CONNECTOR-REF DEST="COMMUNICATION-CONNECTOR">/Topology/Connector1</CONNECTOR-REF>'
    '<TP-ADDRESS-REF DEST="TP-ADDRESS">/TpConfigs/Config1/TpAddress1</TP-ADDRESS-REF>'
    "<VARIATION-POINT />"
    "</J-1939-TP-NODE>"
)

EMPTY_NODE_XML = "<J-1939-TP-NODE><SHORT-NAME>Node1</SHORT-NAME></J-1939-TP-NODE>"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str) -> ET.Element:
    xml = "<ROOT xmlns='%s'>%s</ROOT>" % (NS, inner)
    return ET.fromstring(xml)


def _node() -> J1939TpNode:
    package = AUTOSAR.getInstance().createARPackage("TpConfigs")
    return J1939TpNode(package, "Node1")


class TestReadJ1939TpNode:
    def test_read_full(self):
        node = _node()
        root = _snip(NODE_XML)
        ARXMLParser().readJ1939TpNode(root[0], node)

        assert node.getShortName() == "Node1"

        connector_ref = node.getConnectorRef()
        assert connector_ref.getValue() == "/Topology/Connector1"
        assert connector_ref.getDest() == "COMMUNICATION-CONNECTOR"

        tp_address_ref = node.getTpAddressRef()
        assert tp_address_ref.getValue() == "/TpConfigs/Config1/TpAddress1"
        assert tp_address_ref.getDest() == "TP-ADDRESS"

        assert node.getVariationPoint() is not None

    def test_read_empty(self):
        node = _node()
        root = _snip(EMPTY_NODE_XML)
        ARXMLParser().readJ1939TpNode(root[0], node)

        assert node.getConnectorRef() is None
        assert node.getTpAddressRef() is None
        assert node.getVariationPoint() is None
