"""Reader tests for MsrQueryP1 (AUTOSAR_FO_TPS_GenericStructureTemplate, Table 9.82)."""

import xml.etree.ElementTree as ET

from armodel.parser.arxml_parser import ARXMLParser


class TestMsrQueryP1Parser:
    def test_get_msr_query_p1_reads_all_members(self):
        parser = ARXMLParser()
        element = ET.fromstring(
            '<PARENT xmlns="http://autosar.org/schema/r4.0">'
            '<MSR-QUERY-P-1 S="checksum" T="timestamp" SI="si" VIEW="view" BREAK="BREAK" KEEP-WITH-PREVIOUS="KEEP">'
            "<MSR-QUERY-PROPS><MSR-QUERY-NAME>paragraph-query</MSR-QUERY-NAME></MSR-QUERY-PROPS>"
            "<TOPIC-CONTENT><DOCUMENTATION-BLOCK/></TOPIC-CONTENT>"
            "</MSR-QUERY-P-1></PARENT>"
        )

        result = parser.getMsrQueryP1(element, "MSR-QUERY-P-1")

        assert result is not None
        assert result.getChecksum().getValue() == "checksum"
        assert result.getTimestamp().getValue() == "timestamp"
        assert result.getSi().getValue() == "si"
        assert result.getView().getValue() == "view"
        assert result.getBreak().getValue() == "BREAK"
        assert result.getKeepWithPrevious().getValue() == "KEEP"
        assert result.getMsrQueryProps().getMsrQueryName().getValue() == "paragraph-query"
        assert result.getMsrQueryResultP1() is not None

    def test_get_msr_query_p1_empty_returns_object(self):
        parser = ARXMLParser()
        element = ET.fromstring('<PARENT xmlns="http://autosar.org/schema/r4.0"><MSR-QUERY-P-1/></PARENT>')

        result = parser.getMsrQueryP1(element, "MSR-QUERY-P-1")

        assert result is not None
        assert result.getMsrQueryProps() is None
        assert result.getMsrQueryResultP1() is None

    def test_get_msr_query_p1_missing_returns_none(self):
        parser = ARXMLParser()
        element = ET.fromstring('<PARENT xmlns="http://autosar.org/schema/r4.0"/>')

        assert parser.getMsrQueryP1(element, "MSR-QUERY-P-1") is None
