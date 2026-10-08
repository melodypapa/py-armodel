"""Reader tests for NetworkSegmentIdentification (Table 9.3, p.859)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    NetworkSegmentIdentification,
)
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def parser():
    return ARXMLParser()


class TestReadNetworkSegmentIdentification:
    def test_read_network_segment_id(self, parser):
        """
        The NETWORK-SEGMENT-ID element is read into the networkSegmentId field.
        """
        element = ET.fromstring("<NETWORK-SEGMENT-ID xmlns='%s' T='2024-01-01T00:00:00Z'>" "<NETWORK-SEGMENT-ID>7</NETWORK-SEGMENT-ID>" "</NETWORK-SEGMENT-ID>" % NS)

        props = parser.readNetworkSegmentIdentification(element, NetworkSegmentIdentification())

        assert props.getTimestamp() is not None
        assert props.getNetworkSegmentId() is not None
        assert props.getNetworkSegmentId().getValue() == 7

    def test_read_empty_element(self, parser):
        """
        An empty NETWORK-SEGMENT-ID element leaves the attribute unset.
        """
        element = ET.fromstring("<NETWORK-SEGMENT-ID xmlns='%s'></NETWORK-SEGMENT-ID>" % NS)

        props = parser.readNetworkSegmentIdentification(element, NetworkSegmentIdentification())

        assert props.getNetworkSegmentId() is None
