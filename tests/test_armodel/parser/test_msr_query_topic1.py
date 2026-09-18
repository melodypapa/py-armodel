"""Reader tests for MsrQueryTopic1 (AUTOSAR_FO_TPS_GenericStructureTemplate, Table 9.83)."""

import xml.etree.ElementTree as ET

from armodel.parser.arxml_parser import ARXMLParser


class TestMsrQueryTopic1Parser:
    def test_get_msr_query_topic1_reads_all_members(self):
        parser = ARXMLParser()
        element = ET.fromstring(
            '<PARENT xmlns="http://autosar.org/schema/r4.0">'
            '<MSR-QUERY-TOPIC-1 S="checksum" T="timestamp" SI="si" VIEW="view" BREAK="BREAK" KEEP-WITH-PREVIOUS="KEEP">'
            "<MSR-QUERY-PROPS><MSR-QUERY-NAME>topic-query</MSR-QUERY-NAME></MSR-QUERY-PROPS>"
            "<MSR-QUERY-RESULT-TOPIC-1><TOPIC-1><SHORT-NAME>topic-1</SHORT-NAME></TOPIC-1></MSR-QUERY-RESULT-TOPIC-1>"
            "</MSR-QUERY-TOPIC-1></PARENT>"
        )

        result = parser.getMsrQueryTopic1(element, "MSR-QUERY-TOPIC-1")

        assert result is not None
        assert result.getChecksum().getValue() == "checksum"
        assert result.getTimestamp().getValue() == "timestamp"
        assert result.getSi().getValue() == "si"
        assert result.getView().getValue() == "view"
        assert result.getBreak().getValue() == "BREAK"
        assert result.getKeepWithPrevious().getValue() == "KEEP"
        assert result.getMsrQueryProps().getMsrQueryName().getValue() == "topic-query"
        assert result.getMsrQueryResultTopic1().getTopic1s()[0].getShortName() == "topic-1"

    def test_get_msr_query_topic1_empty_returns_object(self):
        parser = ARXMLParser()
        element = ET.fromstring('<PARENT xmlns="http://autosar.org/schema/r4.0"><MSR-QUERY-TOPIC-1/></PARENT>')

        result = parser.getMsrQueryTopic1(element, "MSR-QUERY-TOPIC-1")

        assert result is not None
        assert result.getMsrQueryProps() is None
        assert result.getMsrQueryResultTopic1() is None

    def test_get_msr_query_topic1_missing_returns_none(self):
        parser = ARXMLParser()
        element = ET.fromstring('<PARENT xmlns="http://autosar.org/schema/r4.0"/>')

        assert parser.getMsrQueryTopic1(element, "MSR-QUERY-TOPIC-1") is None
