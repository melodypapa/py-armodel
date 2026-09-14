"""Reader tests for the Std inline text element."""

import xml.etree.ElementTree as ET

from armodel.parser.arxml_parser import ARXMLParser


class TestStdParser:
    def test_read_std_parses_all_attributes(self):
        parent = ET.fromstring(
            '<PARENT xmlns="http://autosar.org/schema/r4.0"><STD DATE="2026-09-12" POSITION="section 1" STATE="final" SUBTITLE="standard"><URL>https://example.com/std</URL></STD></PARENT>'
        )

        std = ARXMLParser().getStd(parent, "STD")

        assert std.getDate().getValue() == "2026-09-12"
        assert std.getPosition().getValue() == "section 1"
        assert std.getState().getValue() == "final"
        assert std.getSubtitle().getValue() == "standard"
        assert std.getUrl().getValue().getText() == "https://example.com/std"

    def test_read_std_without_element_returns_none(self):
        parent = ET.fromstring('<PARENT xmlns="http://autosar.org/schema/r4.0"/>')

        assert ARXMLParser().getStd(parent, "STD") is None
