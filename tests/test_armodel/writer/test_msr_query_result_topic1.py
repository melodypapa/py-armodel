"""Writer tests for MsrQueryResultTopic1 (AUTOSAR_FO_TPS_GenericStructureTemplate, Table 9.88)."""

import xml.etree.ElementTree as ET

from armodel.models.M2.MSR.Documentation.Chapters import Topic1
from armodel.models.M2.MSR.Documentation.MsrQuery import MsrQueryResultTopic1
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


def _build_full_result() -> MsrQueryResultTopic1:
    result = MsrQueryResultTopic1()
    result.addTopic1(Topic1(None, "topic-1"))
    result.addTopic1(Topic1(None, "topic-2"))
    return result


class TestMsrQueryResultTopic1Writer:
    def test_set_msr_query_result_topic1_writes_topic_children(self):
        element = ET.Element("PARENT")

        ARXMLWriter().setMsrQueryResultTopic1(element, "MSR-QUERY-RESULT-TOPIC-1", _build_full_result())

        written = element.find("MSR-QUERY-RESULT-TOPIC-1")
        assert written is not None
        topics = written.findall("TOPIC-1")
        assert len(topics) == 2
        assert topics[0].find("SHORT-NAME").text == "topic-1"
        assert topics[1].find("SHORT-NAME").text == "topic-2"

    def test_set_msr_query_result_topic1_empty_omits_children(self):
        element = ET.Element("PARENT")

        ARXMLWriter().setMsrQueryResultTopic1(element, "MSR-QUERY-RESULT-TOPIC-1", MsrQueryResultTopic1())

        written = element.find("MSR-QUERY-RESULT-TOPIC-1")
        assert written is not None
        assert written.findall("TOPIC-1") == []

    def test_set_msr_query_result_topic1_none_is_noop(self):
        element = ET.Element("PARENT")

        ARXMLWriter().setMsrQueryResultTopic1(element, "MSR-QUERY-RESULT-TOPIC-1", None)

        assert element.find("MSR-QUERY-RESULT-TOPIC-1") is None

    def test_msr_query_result_topic1_write_read_roundtrip(self):
        writer_element = ET.Element("PARENT")
        ARXMLWriter().setMsrQueryResultTopic1(writer_element, "MSR-QUERY-RESULT-TOPIC-1", _build_full_result())

        writer_element.attrib["xmlns"] = "http://autosar.org/schema/r4.0"
        parsed = ET.fromstring(ET.tostring(writer_element, encoding="unicode"))

        result = ARXMLParser().getMsrQueryResultTopic1(parsed, "MSR-QUERY-RESULT-TOPIC-1")

        topics = result.getTopic1s()
        assert len(topics) == 2
        assert topics[0].getShortName() == "topic-1"
        assert topics[1].getShortName() == "topic-2"
