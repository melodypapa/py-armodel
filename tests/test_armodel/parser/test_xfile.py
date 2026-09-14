"""Reader tests for the Xfile inline text element."""

import xml.etree.ElementTree as ET

from armodel.parser.arxml_parser import ARXMLParser


class TestXfileParser:
    def test_read_xfile_parses_all_attributes(self):
        parent = ET.fromstring('<PARENT xmlns="http://autosar.org/schema/r4.0"><XFILE><URL>https://example.com/file</URL><TOOL>generator</TOOL><TOOL-VERSION>1.2</TOOL-VERSION></XFILE></PARENT>')

        xfile = ARXMLParser().getXfile(parent, "XFILE")

        assert xfile.getTool().getValue() == "generator"
        assert xfile.getToolVersion().getValue() == "1.2"
        assert xfile.getUrl().getValue().getText() == "https://example.com/file"

    def test_read_xfile_without_element_returns_none(self):
        parent = ET.fromstring('<PARENT xmlns="http://autosar.org/schema/r4.0"/>')

        assert ARXMLParser().getXfile(parent, "XFILE") is None
