"""Writer tests for MsrQueryTopic1 (AUTOSAR_FO_TPS_GenericStructureTemplate, Table 9.83)."""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import String
from armodel.models.M2.MSR.Documentation.Chapters import Topic1
from armodel.models.M2.MSR.Documentation.MsrQuery import MsrQueryProps, MsrQueryResultTopic1, MsrQueryTopic1
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


def _build_full_topic_query() -> MsrQueryTopic1:
    result = MsrQueryResultTopic1()
    result.addTopic1(Topic1(None, "topic-1"))
    props = MsrQueryProps().setMsrQueryName(String().setValue("topic-query"))
    return MsrQueryTopic1().setMsrQueryProps(props).setMsrQueryResultTopic1(result)


class TestMsrQueryTopic1Writer:
    def test_write_msr_query_topic1_writes_members_in_xsd_order(self):
        element = ET.Element("PARENT")

        ARXMLWriter().writeMsrQueryTopic1(element, _build_full_topic_query())

        written = element.find("MSR-QUERY-TOPIC-1")
        assert written is not None
        assert [child.tag for child in written] == ["MSR-QUERY-PROPS", "MSR-QUERY-RESULT-TOPIC-1"]
        assert written.get("SI") is None
        assert written.find("MSR-QUERY-PROPS/MSR-QUERY-NAME").text == "topic-query"
        assert written.find("MSR-QUERY-RESULT-TOPIC-1/TOPIC-1/SHORT-NAME").text == "topic-1"

    def test_write_msr_query_topic1_empty_omits_optional_children(self):
        element = ET.Element("PARENT")

        ARXMLWriter().writeMsrQueryTopic1(element, MsrQueryTopic1())

        written = element.find("MSR-QUERY-TOPIC-1")
        assert written is not None
        assert list(written) == []

    def test_msr_query_topic1_write_read_roundtrip(self):
        writer_element = ET.Element("PARENT")
        ARXMLWriter().writeMsrQueryTopic1(writer_element, _build_full_topic_query())
        writer_element.attrib["xmlns"] = "http://autosar.org/schema/r4.0"
        parsed = ET.fromstring(ET.tostring(writer_element, encoding="unicode"))

        result = ARXMLParser().getMsrQueryTopic1(parsed, "MSR-QUERY-TOPIC-1")

        assert result.getMsrQueryProps().getMsrQueryName().getValue() == "topic-query"
        assert result.getMsrQueryResultTopic1().getTopic1s()[0].getShortName() == "topic-1"
