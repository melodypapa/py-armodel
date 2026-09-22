"""Writer round-trip tests for HwPortMapping (Table 3.135, p.183).

XML element order per XSD group HW-PORT-MAPPING:
COMMUNICATION-CONNECTOR-REF, HW-COMMUNICATION-PORT-REF.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.ECUResourceMapping import HwPortMapping
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _ref(dest, value):
    ref = RefType()
    ref.setDest(dest)
    ref.setValue(value)
    return ref


def _new_mapping():
    mapping = HwPortMapping()
    mapping.setCommunicationConnectorRef(_ref("COMMUNICATION-CONNECTOR", "/System/Connectors/Conn1"))
    mapping.setHwCommunicationPortRef(_ref("HW-PIN-GROUP", "/EcuResource/HwPinGroups/Port1"))
    return mapping


class TestWriteHwPortMapping:
    def test_write_all_fields(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeHwPortMapping(parent, _new_mapping())
        node = parent.find("HW-PORT-MAPPING")
        assert node is not None
        connector_ref = node.find("COMMUNICATION-CONNECTOR-REF")
        assert connector_ref.text == "/System/Connectors/Conn1"
        assert connector_ref.attrib["DEST"] == "COMMUNICATION-CONNECTOR"
        port_ref = node.find("HW-COMMUNICATION-PORT-REF")
        assert port_ref.text == "/EcuResource/HwPinGroups/Port1"
        assert port_ref.attrib["DEST"] == "HW-PIN-GROUP"
        children = [child.tag for child in node]
        assert children == ["COMMUNICATION-CONNECTOR-REF", "HW-COMMUNICATION-PORT-REF"]

    def test_write_empty_fields_omits_optional_tags(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeHwPortMapping(parent, HwPortMapping())
        node = parent.find("HW-PORT-MAPPING")
        assert node is not None
        assert len(list(node)) == 0

    def test_round_trip_preserves_all_values(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeHwPortMapping(parent, _new_mapping())
        root = ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))
        parsed = ARXMLParser().readHwPortMapping(root[0])
        assert parsed.getCommunicationConnectorRef().getValue() == "/System/Connectors/Conn1"
        assert parsed.getCommunicationConnectorRef().getDest() == "COMMUNICATION-CONNECTOR"
        assert parsed.getHwCommunicationPortRef().getValue() == "/EcuResource/HwPinGroups/Port1"
        assert parsed.getHwCommunicationPortRef().getDest() == "HW-PIN-GROUP"
