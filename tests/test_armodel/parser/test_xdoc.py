"""Reader tests for the Xdoc inline text element."""

import xml.etree.ElementTree as ET

from armodel.parser.arxml_parser import ARXMLParser


class TestXdocParser:
    def test_read_xdoc_parses_all_attributes(self):
        parent = ET.fromstring(
            '<PARENT xmlns="http://autosar.org/schema/r4.0"><XDOC DATE="2026-09-12" NUMBER="DOC-1" POSITION="section 1" PUBLISHER="Publisher" STATE="final"><URL>https://example.com/doc</URL></XDOC></PARENT>'
        )

        xdoc = ARXMLParser().getXdoc(parent, "XDOC")

        assert xdoc.getDate().getValue() == "2026-09-12"
        assert xdoc.getNumber().getValue() == "DOC-1"
        assert xdoc.getPosition().getValue() == "section 1"
        assert xdoc.getPublisher().getValue() == "Publisher"
        assert xdoc.getState().getValue() == "final"
        assert xdoc.getUrl().getValue().getText() == "https://example.com/doc"

    def test_read_xdoc_without_element_returns_none(self):
        parent = ET.fromstring('<PARENT xmlns="http://autosar.org/schema/r4.0"/>')

        assert ARXMLParser().getXdoc(parent, "XDOC") is None
