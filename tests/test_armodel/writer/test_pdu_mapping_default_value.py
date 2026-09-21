"""Writer round-trip tests for PduMappingDefaultValue (Table 8.5, p.841).

Aggregated by TargetIPduRef.defaultValue. Element order per XSD groups
TARGET-I-PDU-REF and PDU-MAPPING-DEFAULT-VALUE: TARGET-I-PDU-REF,
DEFAULT-VALUE-ELEMENTS (choice of DEFAULT-VALUE-ELEMENT with
ELEMENT-BYTE-VALUE, ELEMENT-POSITION).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Integer, RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Multiplatform import DefaultValueElement, PduMappingDefaultValue, TargetIPduRef
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _int(value):
    number = Integer()
    number.setValue(value)
    return number


def _element(byte_value, position):
    element = DefaultValueElement()
    element.setElementByteValue(_int(byte_value))
    element.setElementPosition(_int(position))
    return element


def _new_target():
    target = TargetIPduRef()
    ref = RefType()
    ref.setValue("/Cluster/PT_Target")
    ref.setDest("PDU-TRIGGERING")
    target.setTargetIPduRef(ref)

    default_value = PduMappingDefaultValue()
    default_value.addDefaultValueElement(_element(171, 0))
    default_value.addDefaultValueElement(_element(204, 1))
    target.setDefaultValue(default_value)
    return target


class TestWritePduMappingDefaultValue:
    def test_write_content_in_xsd_order(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().setTargetIPduRef(parent, "TARGET-I-PDU", _new_target())
        node = parent.find("TARGET-I-PDU")
        assert node is not None
        children = [child.tag for child in node]
        assert children == ["TARGET-I-PDU-REF", "DEFAULT-VALUE-ELEMENTS"]
        assert node.find("TARGET-I-PDU-REF").text == "/Cluster/PT_Target"
        elements = node.findall("DEFAULT-VALUE-ELEMENTS/DEFAULT-VALUE-ELEMENT")
        assert len(elements) == 2
        assert elements[0].find("ELEMENT-BYTE-VALUE").text == "171"
        assert elements[0].find("ELEMENT-POSITION").text == "0"
        assert elements[1].find("ELEMENT-BYTE-VALUE").text == "204"
        assert elements[1].find("ELEMENT-POSITION").text == "1"

    def test_write_without_default_value_omits_wrapper(self):
        target = TargetIPduRef()
        ref = RefType()
        ref.setValue("/Cluster/PT_Target")
        ref.setDest("PDU-TRIGGERING")
        target.setTargetIPduRef(ref)

        parent = ET.Element("PARENT")
        ARXMLWriter().setTargetIPduRef(parent, "TARGET-I-PDU", target)
        node = parent.find("TARGET-I-PDU")
        assert node.find("DEFAULT-VALUE-ELEMENTS") is None
        assert node.find("TARGET-I-PDU-REF").text == "/Cluster/PT_Target"

    def test_round_trip_preserves_all_values(self):
        target = _new_target()
        parent = ET.Element("PARENT")
        ARXMLWriter().setTargetIPduRef(parent, "TARGET-I-PDU", target)
        reparsed = ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))
        parsed = ARXMLParser().getTargetIPduRef(reparsed, "TARGET-I-PDU")

        assert parsed.getTargetIPduRef().getValue() == "/Cluster/PT_Target"
        assert parsed.getTargetIPduRef().getDest() == "PDU-TRIGGERING"
        default_value = parsed.getDefaultValue()
        assert isinstance(default_value, PduMappingDefaultValue)
        elements = default_value.getDefaultValueElements()
        assert len(elements) == 2
        assert elements[0].getElementByteValue().getValue() == 171
        assert elements[0].getElementPosition().getValue() == 0
        assert elements[1].getElementByteValue().getValue() == 204
        assert elements[1].getElementPosition().getValue() == 1
