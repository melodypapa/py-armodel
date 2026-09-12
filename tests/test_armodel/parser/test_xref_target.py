"""Reader tests for the XrefTarget inline text element."""

import xml.etree.ElementTree as ET

from armodel.parser.arxml_parser import ARXMLParser


class TestXrefTargetParser:
    def test_read_xref_target_parses_inherited_content(self):
        parent = ET.fromstring('<PARENT xmlns="http://autosar.org/schema/r4.0"><XREF-TARGET><SHORT-NAME>TARGET</SHORT-NAME><LONG-NAME-1>Target label</LONG-NAME-1></XREF-TARGET></PARENT>')

        target = ARXMLParser().getXrefTarget(parent, "XREF-TARGET")

        assert target.getShortName() == "TARGET"
        assert target.getLongName1().getValue().getValue() == "Target label"

    def test_read_xref_target_without_element_returns_none(self):
        parent = ET.fromstring('<PARENT xmlns="http://autosar.org/schema/r4.0"/>')

        assert ARXMLParser().getXrefTarget(parent, "XREF-TARGET") is None
