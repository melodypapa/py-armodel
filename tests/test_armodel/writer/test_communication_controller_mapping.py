"""Writer round-trip tests for CommunicationControllerMapping (Table 3.134, p.183).

XML element order per XSD group COMMUNICATION-CONTROLLER-MAPPING:
COMMUNICATION-CONTROLLER-REF, HW-COMMUNICATION-CONTROLLER-REF.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.ECUResourceMapping import CommunicationControllerMapping
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
    mapping = CommunicationControllerMapping()
    mapping.setCommunicationControllerRef(_ref("COMMUNICATION-CONTROLLER", "/System/Controllers/Ctrl1"))
    mapping.setHwCommunicationControllerRef(_ref("HW-ELEMENT", "/EcuResource/HwElements/Mcu"))
    return mapping


class TestWriteCommunicationControllerMapping:
    def test_write_all_fields(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeCommunicationControllerMapping(parent, _new_mapping())
        node = parent.find("COMMUNICATION-CONTROLLER-MAPPING")
        assert node is not None
        controller_ref = node.find("COMMUNICATION-CONTROLLER-REF")
        assert controller_ref.text == "/System/Controllers/Ctrl1"
        assert controller_ref.attrib["DEST"] == "COMMUNICATION-CONTROLLER"
        hw_ref = node.find("HW-COMMUNICATION-CONTROLLER-REF")
        assert hw_ref.text == "/EcuResource/HwElements/Mcu"
        assert hw_ref.attrib["DEST"] == "HW-ELEMENT"
        children = [child.tag for child in node]
        assert children == ["COMMUNICATION-CONTROLLER-REF", "HW-COMMUNICATION-CONTROLLER-REF"]

    def test_write_empty_fields_omits_optional_tags(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeCommunicationControllerMapping(parent, CommunicationControllerMapping())
        node = parent.find("COMMUNICATION-CONTROLLER-MAPPING")
        assert node is not None
        assert len(list(node)) == 0

    def test_round_trip_preserves_all_values(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeCommunicationControllerMapping(parent, _new_mapping())
        root = ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))
        parsed = ARXMLParser().readCommunicationControllerMapping(root[0])
        assert parsed.getCommunicationControllerRef().getValue() == "/System/Controllers/Ctrl1"
        assert parsed.getCommunicationControllerRef().getDest() == "COMMUNICATION-CONTROLLER"
        assert parsed.getHwCommunicationControllerRef().getValue() == "/EcuResource/HwElements/Mcu"
        assert parsed.getHwCommunicationControllerRef().getDest() == "HW-ELEMENT"
