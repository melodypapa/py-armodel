"""Reader tests for the Xref inline text element."""

from xml.etree import ElementTree as ET

from armodel.parser.arxml_parser import ARXMLParser


class TestXrefParser:
    def test_get_xref_reads_nested_members_and_attributes(self):
        element = ET.fromstring(
            '<XREF xmlns="http://autosar.org/schema/r4.0" S="checksum" T="2024-01-01T00:00:00Z" RESOLUTION-POLICY="SLOPPY" '
            'SHOW-CONTENT="SHOW-CONTENT" SHOW-RESOURCE-SHORT-NAME="NO-SHOW-SHORT-NAME" '
            'SHOW-SEE="SHOW-SEE"><LABEL-1>Replacement</LABEL-1><REFERRABLE-REF DEST="AR-PACKAGE">/A/B</REFERRABLE-REF></XREF>'
        )

        xref = ARXMLParser().getXref(element, ".")

        assert xref.getChecksum().getValue() == "checksum"
        assert xref.getLabel1().getValue().getValue() == "Replacement"
        assert xref.getReferrableRef().getValue() == "/A/B"
        assert xref.getReferrableRef().getDest() == "AR-PACKAGE"
        assert xref.getResolutionPolicy().getValue() == "SLOPPY"
        assert xref.getShowContent().getValue() == "SHOW-CONTENT"
        assert xref.getShowResourceShortName().getValue() == "NO-SHOW-SHORT-NAME"
        assert xref.getShowSee().getValue() == "SHOW-SEE"

    def test_get_xref_returns_none_for_missing_element(self):
        assert ARXMLParser().getXref(ET.fromstring("<PARENT />"), "XREF") is None
