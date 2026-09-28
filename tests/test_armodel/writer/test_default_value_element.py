"""Writer round-trip tests for DefaultValueElement (AUTOSAR_CP_TPS_SystemTemplate Table 8.6, p.841).

Aggregated by PduMappingDefaultValue.defaultValueElement. Element order per XSD
group DEFAULT-VALUE-ELEMENT (00052.xsd L30881): ELEMENT-BYTE-VALUE,
ELEMENT-POSITION; complexType = AR-OBJECT group + own group.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DateTime, Integer, String
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Multiplatform import DefaultValueElement
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


def _element(byte_value=None, position=None):
    element = DefaultValueElement()
    if byte_value is not None:
        element.setElementByteValue(_int(byte_value))
    if position is not None:
        element.setElementPosition(_int(position))
    return element


class TestWriteDefaultValueElement:
    def test_write_content_in_xsd_order(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDefaultValueElement(parent, _element(171, 0))

        node = parent.find("DEFAULT-VALUE-ELEMENT")
        assert node is not None
        children = [child.tag for child in node]
        assert children == ["ELEMENT-BYTE-VALUE", "ELEMENT-POSITION"]
        assert node.find("ELEMENT-BYTE-VALUE").text == "171"
        assert node.find("ELEMENT-POSITION").text == "0"

    def test_write_omits_absent_elements(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDefaultValueElement(parent, _element())

        node = parent.find("DEFAULT-VALUE-ELEMENT")
        assert node is not None
        assert len(list(node)) == 0

    def test_write_partial_element(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDefaultValueElement(parent, _element(position=5))

        node = parent.find("DEFAULT-VALUE-ELEMENT")
        assert node.find("ELEMENT-BYTE-VALUE") is None
        assert node.find("ELEMENT-POSITION").text == "5"

    def test_write_arobject_attributes(self):
        element = _element(1, 0)
        checksum = String()
        checksum.setValue("17")
        element.setChecksum(checksum)
        timestamp = DateTime()
        timestamp.setValue("2023-11-02T12:00:00+01:00")
        element.setTimestamp(timestamp)

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDefaultValueElement(parent, element)

        node = parent.find("DEFAULT-VALUE-ELEMENT")
        assert node.attrib["S"] == "17"
        assert node.attrib["T"] == "2023-11-02T12:00:00+01:00"

    def test_round_trip_preserves_all_values(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDefaultValueElement(parent, _element(204, 7))
        reparsed = ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))

        parser = ARXMLParser()
        element = DefaultValueElement()
        parser.readDefaultValueElement(parser.find(reparsed, "DEFAULT-VALUE-ELEMENT"), element)

        assert element.getElementByteValue().getValue() == 204
        assert element.getElementPosition().getValue() == 7


class TestWriteDefaultValueElementDispatch:
    def test_target_ipdu_ref_dispatch_writes_elements(self):
        from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Multiplatform import PduMappingDefaultValue, TargetIPduRef

        target = TargetIPduRef()
        default_value = PduMappingDefaultValue()
        default_value.addDefaultValueElement(_element(171, 0))
        target.setDefaultValue(default_value)

        parent = ET.Element("PARENT")
        ARXMLWriter().setTargetIPduRef(parent, "TARGET-I-PDU", target)

        elements = parent.findall("TARGET-I-PDU/DEFAULT-VALUE/DEFAULT-VALUE-ELEMENTS/DEFAULT-VALUE-ELEMENT")
        assert len(elements) == 1
        assert elements[0].find("ELEMENT-BYTE-VALUE").text == "171"
        assert elements[0].find("ELEMENT-POSITION").text == "0"
