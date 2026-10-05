"""Writer round-trip tests for TargetIPduRef (AUTOSAR_CP_TPS_SystemTemplate Table 8.4, p.841).

setTargetIPduRef writes the XSD group TARGET-I-PDU-REF (00052.xsd L120230):
DEFAULT-VALUE (PDU-MAPPING-DEFAULT-VALUE wrapper carrying DEFAULT-VALUE-ELEMENTS,
emitted only when non-empty) first, then TARGET-I-PDU-REF (REF + DEST
PDU-TRIGGERING); no VARIATION-POINT in the complexType.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DateTime, Integer, RefType, String
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


def _ref(value, dest="PDU-TRIGGERING"):
    ref = RefType()
    ref.setValue(value)
    ref.setDest(dest)
    return ref


def _new_target(with_elements=True):
    target = TargetIPduRef()
    target.setChecksum(String().setValue("1234"))
    target.setTimestamp(DateTime().setValue("2024-01-01T00:00:00Z"))
    target.setTargetIPduRef(_ref("/Cluster/PT_Target"))
    if with_elements:
        default_value = PduMappingDefaultValue()
        element = DefaultValueElement()
        element.setElementByteValue(_int(171))
        element.setElementPosition(_int(0))
        default_value.addDefaultValueElement(element)
        target.setDefaultValue(default_value)
    return target


class TestSetTargetIPduRef:
    def test_write_content_in_xsd_order(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().setTargetIPduRef(parent, "TARGET-I-PDU", _new_target())

        node = parent.find("TARGET-I-PDU")
        assert node is not None
        children = [child.tag for child in node]
        assert children == ["DEFAULT-VALUE", "TARGET-I-PDU-REF"]
        assert node.find("TARGET-I-PDU-REF").text == "/Cluster/PT_Target"
        assert node.find("TARGET-I-PDU-REF").attrib["DEST"] == "PDU-TRIGGERING"

        elements = node.findall("DEFAULT-VALUE/DEFAULT-VALUE-ELEMENTS/DEFAULT-VALUE-ELEMENT")
        assert len(elements) == 1
        assert elements[0].find("ELEMENT-BYTE-VALUE").text == "171"
        assert elements[0].find("ELEMENT-POSITION").text == "0"
        assert node.get("S") == "1234"
        assert node.get("T") == "2024-01-01T00:00:00Z"

    def test_write_ref_only_omits_default_value(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().setTargetIPduRef(parent, "TARGET-I-PDU", _new_target(with_elements=False))

        node = parent.find("TARGET-I-PDU")
        assert node.find("DEFAULT-VALUE") is None
        assert node.find("TARGET-I-PDU-REF").text == "/Cluster/PT_Target"

    def test_write_none_is_noop(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().setTargetIPduRef(parent, "TARGET-I-PDU", None)

        assert len(list(parent)) == 0

    def test_round_trip_preserves_all_values(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().setTargetIPduRef(parent, "TARGET-I-PDU", _new_target())
        reparsed = ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))

        target = ARXMLParser().getTargetIPduRef(reparsed, "TARGET-I-PDU")

        assert target.getTargetIPduRef().getValue() == "/Cluster/PT_Target"
        assert target.getTargetIPduRef().getDest() == "PDU-TRIGGERING"
        elements = target.getDefaultValue().getDefaultValueElements()
        assert len(elements) == 1
        assert elements[0].getElementByteValue().getValue() == 171
        assert elements[0].getElementPosition().getValue() == 0
        assert target.getChecksum().getValue() == "1234"
        assert target.getTimestamp().getValue() == "2024-01-01T00:00:00Z"
