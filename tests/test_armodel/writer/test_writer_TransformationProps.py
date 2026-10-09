"""Writer/reader round-trip tests for the TransformationProps reusable helper (Table 7.15, p.783)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Identifier, String
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import TransformationProps
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


class ConcreteTransformationProps(TransformationProps):
    pass


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
    props = ConcreteTransformationProps(None, "someipProps")
    props.setUuid(String().setValue("8b2f4e10-1f2a-4d3e-9c5b-0a1b2c3d4e5f"))
    props.setCategory(Identifier().setValue("someip"))
    return props


class TestWriteTransformationProps:
    def test_write_identifiable_level(self, writer):
        """
        The helper writes the Identifiable level (UUID attribute, SHORT-NAME, CATEGORY) onto the
        concrete subclass element passed by the caller.
        """
        element = ET.Element("SOMEIP-TRANSFORMATION-PROPS")
        writer.writeTransformationProps(element, _new_props())

        assert element.attrib["UUID"] == "8b2f4e10-1f2a-4d3e-9c5b-0a1b2c3d4e5f"
        assert element.find("SHORT-NAME").text == "someipProps"
        assert element.find("CATEGORY").text == "someip"

    def test_write_without_identifiable_content(self, writer):
        """
        An unset Identifiable state emits no content beyond the SHORT-NAME.
        """
        element = ET.Element("USER-DEFINED-TRANSFORMATION-PROPS")
        writer.writeTransformationProps(element, ConcreteTransformationProps(None, "userDefinedProps"))

        assert element.find("CATEGORY") is None
        assert element.find("DESC") is None


class TestTransformationPropsRoundTrip:
    def test_round_trip_preserves_identifiable_level(self, writer, parser):
        """
        Write -> serialize -> parse keeps the Identifiable-level content.
        """
        element = ET.Element("SOMEIP-TRANSFORMATION-PROPS")
        writer.writeTransformationProps(element, _new_props())
        xml = ET.tostring(element, encoding="unicode")

        parsed_element = ET.fromstring("<WRAP xmlns='%s'>%s</WRAP>" % (NS, xml))[0]
        props = parser.readTransformationProps(parsed_element, ConcreteTransformationProps(None, "someipProps"))

        assert props.getShortName() == "someipProps"
        assert props.getUuid().getValue() == "8b2f4e10-1f2a-4d3e-9c5b-0a1b2c3d4e5f"
        assert props.getCategory().getValue() == "someip"
