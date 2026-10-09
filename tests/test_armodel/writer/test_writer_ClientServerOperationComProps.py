"""Writer/reader round-trip tests for ClientServerOperationComProps (Table 11.12, p.903)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ClientServerOperationComProps
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, String
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
    props = ClientServerOperationComProps()
    props.setChecksum(String().setValue("41"))
    props.setQueueLength(PositiveInteger().setValue("3"))
    return props


class TestWriteClientServerOperationComProps:
    def test_write_queue_length_in_xsd_order(self, writer):
        """
        The helper writes the ARObject S attribute (via the inherited base helper) and the
        Table 11.12 QUEUE-LENGTH element.
        """
        element = ET.Element("CLIENT-SERVER-OPERATION-COM-PROPS")
        writer.writeClientServerOperationComProps(element, _new_props())

        assert element.attrib["S"] == "41"
        assert [child.tag for child in element] == ["QUEUE-LENGTH"]
        assert element.find("QUEUE-LENGTH").text == "3"

    def test_write_empty_element(self, writer):
        """
        With no attribute content, no child elements and no S attribute are emitted.
        """
        element = ET.Element("CLIENT-SERVER-OPERATION-COM-PROPS")
        writer.writeClientServerOperationComProps(element, ClientServerOperationComProps())

        assert len(element) == 0
        assert "S" not in element.attrib


class TestClientServerOperationComPropsRoundTrip:
    def test_round_trip_preserves_field_values(self, writer, parser):
        """
        Write -> serialize -> parse keeps the checksum and the queue length value.
        """
        element = ET.Element("CLIENT-SERVER-OPERATION-COM-PROPS")
        writer.writeClientServerOperationComProps(element, _new_props())
        xml = ET.tostring(element, encoding="unicode")

        parsed_element = ET.fromstring("<WRAP xmlns='%s'>%s</WRAP>" % (NS, xml))[0]
        props = parser.readClientServerOperationComProps(parsed_element, ClientServerOperationComProps())

        assert props.getChecksum().getValue() == "41"
        assert props.getQueueLength().getValue() == 3

    def test_round_trip_empty_element(self, writer, parser):
        """
        A props object without queue length round-trips unset (no QUEUE-LENGTH tag emitted).
        """
        element = ET.Element("CLIENT-SERVER-OPERATION-COM-PROPS")
        writer.writeClientServerOperationComProps(element, ClientServerOperationComProps())
        xml = ET.tostring(element, encoding="unicode")

        assert "QUEUE-LENGTH" not in xml

        parsed_element = ET.fromstring("<WRAP xmlns='%s'>%s</WRAP>" % (NS, xml))[0]
        props = parser.readClientServerOperationComProps(parsed_element, ClientServerOperationComProps())

        assert props.getQueueLength() is None
