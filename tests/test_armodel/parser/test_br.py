"""Reader tests for the Br inline text element."""

import xml.etree.ElementTree as ET

from armodel.parser.arxml_parser import ARXMLParser


class TestBrParser:
    def test_read_br_preserves_ar_object_attributes(self):
        parent = ET.fromstring('<PARENT xmlns="http://autosar.org/schema/r4.0"><BR S="checksum" T="timestamp"/></PARENT>')
        br = ARXMLParser().getBr(parent, "BR")

        assert br.getChecksum().getValue() == "checksum"
        assert br.getTimestamp().getValue() == "timestamp"
