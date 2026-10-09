"""Writer/reader round-trip tests for SOMEIPTransformationProps (Table 7.16, p.783)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Identifier, PositiveInteger, String
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import SOMEIPTransformationProps
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def writer():
    return ARXMLWriter()


@pytest.fixture
def parser():
    return ARXMLParser()


def _new_props():
    props = SOMEIPTransformationProps(None, "someipProps")
    props.setUuid(String().setValue("1a2b3c4d-5e6f-4789-8a9b-0c1d2e3f4a5b"))
    props.setCategory(Identifier().setValue("someip"))
    props.setAlignment(PositiveInteger().setValue("8"))
    props.setSizeOfArrayLengthField(PositiveInteger().setValue("4"))
    props.setSizeOfStringLengthField(PositiveInteger().setValue("4"))
    props.setSizeOfStructLengthField(PositiveInteger().setValue("4"))
    props.setSizeOfUnionLengthField(PositiveInteger().setValue("4"))
    return props


class TestWriteSOMEIPTransformationProps:
    def test_write_all_elements_in_xsd_order(self, writer):
        """
        The helper writes the Identifiable level and the five group elements in the XSD
        sequenceOffset order.
        """
        element = ET.Element("SOMEIP-TRANSFORMATION-PROPS")
        writer.writeSOMEIPTransformationProps(element, _new_props())

        tags = [child.tag for child in element]
        assert tags == [
            "SHORT-NAME",
            "CATEGORY",
            "ALIGNMENT",
            "SIZE-OF-ARRAY-LENGTH-FIELD",
            "SIZE-OF-STRING-LENGTH-FIELD",
            "SIZE-OF-STRUCT-LENGTH-FIELD",
            "SIZE-OF-UNION-LENGTH-FIELD",
        ]
        assert element.attrib["UUID"] == "1a2b3c4d-5e6f-4789-8a9b-0c1d2e3f4a5b"
        assert element.find("ALIGNMENT").text == "8"
        assert element.find("SIZE-OF-ARRAY-LENGTH-FIELD").text == "4"
        assert element.find("SIZE-OF-STRING-LENGTH-FIELD").text == "4"
        assert element.find("SIZE-OF-STRUCT-LENGTH-FIELD").text == "4"
        assert element.find("SIZE-OF-UNION-LENGTH-FIELD").text == "4"

    def test_write_empty_element(self, writer):
        """
        An unset instance emits no group content beyond the SHORT-NAME.
        """
        element = ET.Element("SOMEIP-TRANSFORMATION-PROPS")
        writer.writeSOMEIPTransformationProps(element, SOMEIPTransformationProps(None, "someipProps"))

        assert [child.tag for child in element] == ["SHORT-NAME"]
        assert element.find("ALIGNMENT") is None
        assert element.find("SIZE-OF-UNION-LENGTH-FIELD") is None


class TestSOMEIPTransformationPropsRoundTrip:
    def test_round_trip_preserves_field_values(self, writer, parser):
        """
        Write -> serialize -> parse keeps every field value.
        """
        element = ET.Element("SOMEIP-TRANSFORMATION-PROPS")
        writer.writeSOMEIPTransformationProps(element, _new_props())
        xml = ET.tostring(element, encoding="unicode")

        parsed_element = ET.fromstring("<WRAP xmlns='%s'>%s</WRAP>" % (NS, xml))[0]
        props = parser.readSOMEIPTransformationProps(parsed_element, SOMEIPTransformationProps(None, "someipProps"))

        assert props.getShortName() == "someipProps"
        assert props.getUuid().getValue() == "1a2b3c4d-5e6f-4789-8a9b-0c1d2e3f4a5b"
        assert props.getCategory().getValue() == "someip"
        assert props.getAlignment().getValue() == 8
        assert props.getSizeOfArrayLengthField().getValue() == 4
        assert props.getSizeOfStringLengthField().getValue() == 4
        assert props.getSizeOfStructLengthField().getValue() == 4
        assert props.getSizeOfUnionLengthField().getValue() == 4
