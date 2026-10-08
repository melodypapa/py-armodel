"""Writer/reader round-trip tests for NetworkSegmentIdentification (Table 9.3, p.859)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    NetworkSegmentIdentification,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    DateTime,
    PositiveInteger,
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
    props = NetworkSegmentIdentification()
    props.setTimestamp(DateTime().setValue("2024-01-01T00:00:00Z"))
    segment_id = PositiveInteger()
    segment_id.setValue("7")
    props.setNetworkSegmentId(segment_id)
    return props


class TestWriteNetworkSegmentIdentification:
    def test_write_all_fields(self, writer):
        """
        The helper emits the NETWORK-SEGMENT-ID element with the T attribute and the identifier.
        """
        parent = ET.Element("GLOBAL-TIME-DOMAIN")
        writer.writeNetworkSegmentIdentification(parent, _new_props())

        node = parent.find("NETWORK-SEGMENT-ID")
        assert node is not None
        assert node.attrib["T"] == "2024-01-01T00:00:00Z"
        identifier = node.find("NETWORK-SEGMENT-ID")
        assert identifier is not None
        assert identifier.text == "7"

    def test_write_empty_fields(self, writer):
        """
        An unset attribute emits an empty element with no identifier.
        """
        parent = ET.Element("GLOBAL-TIME-DOMAIN")
        writer.writeNetworkSegmentIdentification(parent, NetworkSegmentIdentification())

        node = parent.find("NETWORK-SEGMENT-ID")
        assert node is not None
        assert node.find("NETWORK-SEGMENT-ID") is None


class TestNetworkSegmentIdentificationRoundTrip:
    def test_round_trip_preserves_all_values(self, writer, parser):
        """
        Write -> serialize -> parse keeps the timestamp attribute and the identifier value.
        """
        parent = ET.Element("GLOBAL-TIME-DOMAIN")
        writer.writeNetworkSegmentIdentification(parent, _new_props())
        xml = ET.tostring(parent, encoding="unicode")

        parsed_element = ET.fromstring("<WRAP xmlns='%s'>%s</WRAP>" % (NS, xml))[0]
        props = parser.readNetworkSegmentIdentification(parsed_element[0], NetworkSegmentIdentification())

        assert props.getTimestamp().getValue() == "2024-01-01T00:00:00Z"
        assert props.getNetworkSegmentId().getValue() == 7
