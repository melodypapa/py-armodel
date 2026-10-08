"""Writer/reader round-trip tests for UserDefinedTransformationProps (Table 7.29, p.829)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Identifier, String
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import UserDefinedTransformationProps
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
    props = UserDefinedTransformationProps(None, "userDefinedProps")
    props.setUuid(String().setValue("2b3c4d5e-6f7a-4899-baab-1d2e3f4a5b6c"))
    props.setCategory(Identifier().setValue("custom"))
    return props


class TestWriteUserDefinedTransformationProps:
    def test_write_identifiable_level(self, writer):
        """
        The helper writes the Identifiable level (UUID attribute, SHORT-NAME, CATEGORY) onto
        the USER-DEFINED-TRANSFORMATION-PROPS element passed by the caller; the class owns no
        further elements.
        """
        element = ET.Element("USER-DEFINED-TRANSFORMATION-PROPS")
        writer.writeUserDefinedTransformationProps(element, _new_props())

        assert element.attrib["UUID"] == "2b3c4d5e-6f7a-4899-baab-1d2e3f4a5b6c"
        assert element.find("SHORT-NAME").text == "userDefinedProps"
        assert element.find("CATEGORY").text == "custom"
        assert [child.tag for child in element] == ["SHORT-NAME", "CATEGORY"]

    def test_write_empty_element(self, writer):
        """
        An unset instance emits no content beyond the SHORT-NAME.
        """
        element = ET.Element("USER-DEFINED-TRANSFORMATION-PROPS")
        writer.writeUserDefinedTransformationProps(element, UserDefinedTransformationProps(None, "userDefinedProps"))

        assert [child.tag for child in element] == ["SHORT-NAME"]
        assert element.find("CATEGORY") is None
        assert element.find("DESC") is None


class TestUserDefinedTransformationPropsRoundTrip:
    def test_round_trip_preserves_identifiable_level(self, writer, parser):
        """
        Write -> serialize -> parse keeps the Identifiable-level content.
        """
        element = ET.Element("USER-DEFINED-TRANSFORMATION-PROPS")
        writer.writeUserDefinedTransformationProps(element, _new_props())
        xml = ET.tostring(element, encoding="unicode")

        parsed_element = ET.fromstring("<WRAP xmlns='%s'>%s</WRAP>" % (NS, xml))[0]
        props = parser.readUserDefinedTransformationProps(parsed_element, UserDefinedTransformationProps(None, "userDefinedProps"))

        assert props.getShortName() == "userDefinedProps"
        assert props.getUuid().getValue() == "2b3c4d5e-6f7a-4899-baab-1d2e3f4a5b6c"
        assert props.getCategory().getValue() == "custom"
