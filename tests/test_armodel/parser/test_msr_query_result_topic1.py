"""Reader tests for MsrQueryResultTopic1 (AUTOSAR_FO_TPS_GenericStructureTemplate, Table 9.88)."""

import xml.etree.ElementTree as ET

from armodel.parser.arxml_parser import ARXMLParser


class TestMsrQueryResultTopic1Parser:
    def test_get_msr_query_result_topic1_reads_topics(self):
        parser = ARXMLParser()
        element = ET.fromstring(
            '<PARENT xmlns="http://autosar.org/schema/r4.0">'
            '<MSR-QUERY-RESULT-TOPIC-1 S="checksum" T="timestamp">'
            '<TOPIC-1 HELP-ENTRY="help-1"><SHORT-NAME>topic-1</SHORT-NAME></TOPIC-1>'
            "<TOPIC-1><SHORT-NAME>topic-2</SHORT-NAME></TOPIC-1>"
            "</MSR-QUERY-RESULT-TOPIC-1></PARENT>"
        )

        result = parser.getMsrQueryResultTopic1(element, "MSR-QUERY-RESULT-TOPIC-1")

        assert result is not None
        assert result.getChecksum().getValue() == "checksum"
        assert result.getTimestamp().getValue() == "timestamp"
        topics = result.getTopic1s()
        assert len(topics) == 2
        assert topics[0].getShortName() == "topic-1"
        assert topics[0].getHelpEntry().getValue() == "help-1"
        assert topics[1].getShortName() == "topic-2"

    def test_get_msr_query_result_topic1_empty_returns_object(self):
        parser = ARXMLParser()
        element = ET.fromstring('<PARENT xmlns="http://autosar.org/schema/r4.0"><MSR-QUERY-RESULT-TOPIC-1/></PARENT>')

        result = parser.getMsrQueryResultTopic1(element, "MSR-QUERY-RESULT-TOPIC-1")

        assert result is not None
        assert result.getTopic1s() == []

    def test_get_msr_query_result_topic1_missing_returns_none(self):
        parser = ARXMLParser()
        element = ET.fromstring('<PARENT xmlns="http://autosar.org/schema/r4.0"/>')

        assert parser.getMsrQueryResultTopic1(element, "MSR-QUERY-RESULT-TOPIC-1") is None
