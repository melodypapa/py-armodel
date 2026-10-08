"""Writer/reader round-trip tests for DataComProps (Table 11.10, p.903)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import DataComProps
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    DataConsistencyPolicyEnum,
    SendIndicationEnum,
    String,
)
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
    props = DataComProps()
    props.setChecksum(String().setValue("31"))
    props.setDataConsistencyPolicy(DataConsistencyPolicyEnum().setValue(DataConsistencyPolicyEnum.CONSISTENCY_MECHANISM_REQUIRED))
    props.setSendIndication(SendIndicationEnum().setValue(SendIndicationEnum.ANY_SEND_OPERATION))
    return props


class TestWriteDataComProps:
    def test_write_enum_elements_in_xsd_order(self, writer):
        """
        The helper writes the ARObject S attribute (via the inherited base helper) and the two
        Table 11.10 enum elements in the XSD DATA-COM-PROPS group order.
        """
        element = ET.Element("DATA-COM-PROPS")
        writer.writeDataComProps(element, _new_props())

        assert element.attrib["S"] == "31"
        assert [child.tag for child in element] == [
            "DATA-CONSISTENCY-POLICY",
            "SEND-INDICATION",
        ]
        assert element.find("DATA-CONSISTENCY-POLICY").text == "CONSISTENCY-MECHANISM-REQUIRED"
        assert element.find("SEND-INDICATION").text == "ANY-SEND-OPERATION"

    def test_write_empty_element(self, writer):
        """
        With no attribute content, no child elements and no S attribute are emitted.
        """
        element = ET.Element("DATA-COM-PROPS")
        writer.writeDataComProps(element, DataComProps())

        assert len(element) == 0
        assert "S" not in element.attrib


class TestDataComPropsRoundTrip:
    def test_round_trip_preserves_field_values(self, writer, parser):
        """
        Write -> serialize -> parse keeps the checksum and both enum values.
        """
        element = ET.Element("DATA-COM-PROPS")
        writer.writeDataComProps(element, _new_props())
        xml = ET.tostring(element, encoding="unicode")

        parsed_element = ET.fromstring("<WRAP xmlns='%s'>%s</WRAP>" % (NS, xml))[0]
        props = parser.readDataComProps(parsed_element, DataComProps())

        assert props.getChecksum().getValue() == "31"
        assert props.getDataConsistencyPolicy().getValue() == "CONSISTENCY-MECHANISM-REQUIRED"
        assert props.getDataConsistencyPolicy().getValue() == DataConsistencyPolicyEnum.CONSISTENCY_MECHANISM_REQUIRED
        assert props.getSendIndication().getValue() == "ANY-SEND-OPERATION"

    def test_round_trip_empty_element(self, writer, parser):
        """
        A props object without enum values round-trips unset (no enum tags emitted).
        """
        element = ET.Element("DATA-COM-PROPS")
        writer.writeDataComProps(element, DataComProps())
        xml = ET.tostring(element, encoding="unicode")

        assert "DATA-CONSISTENCY-POLICY" not in xml
        assert "SEND-INDICATION" not in xml

        parsed_element = ET.fromstring("<WRAP xmlns='%s'>%s</WRAP>" % (NS, xml))[0]
        props = parser.readDataComProps(parsed_element, DataComProps())

        assert props.getDataConsistencyPolicy() is None
        assert props.getSendIndication() is None
