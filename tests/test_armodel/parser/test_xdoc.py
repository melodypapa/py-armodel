"""Reader tests for the Xdoc inline text element."""

import xml.etree.ElementTree as ET

from armodel.parser.arxml_parser import ARXMLParser


class TestXdocParser:
    def test_read_xdoc_parses_all_child_elements(self):
        parent = ET.fromstring(
            '<PARENT xmlns="http://autosar.org/schema/r4.0"><XDOC><NUMBER>DOC-1</NUMBER><STATE>final</STATE><DATE>2026-09-12</DATE><PUBLISHER>Publisher</PUBLISHER><URL>https://example.com/doc</URL><POSITION>section 1</POSITION></XDOC></PARENT>'
        )

        xdoc = ARXMLParser().getXdoc(parent, "XDOC")

        assert xdoc.getNumber().getValue() == "DOC-1"
        assert xdoc.getState().getValue() == "final"
        assert xdoc.getDate().getValue() == "2026-09-12"
        assert xdoc.getPublisher().getValue() == "Publisher"
        assert xdoc.getUrl().getValue().getText() == "https://example.com/doc"
        assert xdoc.getPosition().getValue() == "section 1"

    def test_read_xdoc_ignores_attribute_form(self):
        parent = ET.fromstring('<PARENT xmlns="http://autosar.org/schema/r4.0"><XDOC DATE="2026-09-12" NUMBER="DOC-1" POSITION="section 1" PUBLISHER="Publisher" STATE="final"/></PARENT>')

        xdoc = ARXMLParser().getXdoc(parent, "XDOC")

        assert xdoc.getDate() is None
        assert xdoc.getNumber() is None
        assert xdoc.getPosition() is None
        assert xdoc.getPublisher() is None
        assert xdoc.getState() is None

    def test_read_xdoc_without_element_returns_none(self):
        parent = ET.fromstring('<PARENT xmlns="http://autosar.org/schema/r4.0"/>')

        assert ARXMLParser().getXdoc(parent, "XDOC") is None
