"""Writer tests for the TopicOrMsrQuery class (AUTOSAR_FO_TPS_GenericStructureTemplate, Table 9.80).

Multiplicity note: the PDF `Mult.` column renders `1` for `topic1`, but XSD group
TOPIC-OR-MSR-QUERY (00052) declares `pureMM.maxOccurs="-1"` (unbounded) and the wire format
permits N TOPIC-1 elements per choice. Confirmed by the user at 9b (2026-10-11) that the
XSD-backed list shape is authoritative, so multiple topics are written and round-tripped here.
"""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DateTime, String
from armodel.models.M2.MSR.Documentation.Chapters import ChapterModel, Topic1, TopicOrMsrQuery
from armodel.models.M2.MSR.Documentation.MsrQuery import MsrQueryProps, MsrQueryTopic1
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


def _parent():
    return AUTOSAR.getInstance().createARPackage("AUTOSAR")


def _full_query() -> TopicOrMsrQuery:
    query = TopicOrMsrQuery()
    query.setTimestamp(DateTime().setValue("2024-01-01T00:00:00+00:00"))
    query.addTopic1(Topic1(_parent(), "TopicA"))
    query.addTopic1(Topic1(_parent(), "TopicB"))
    query.setMsrQueryTopic1(MsrQueryTopic1().setMsrQueryProps(MsrQueryProps().setMsrQueryName(String().setValue("topic-query"))))
    return query


def _reparse(element: ET.Element) -> ChapterModel:
    element.attrib["xmlns"] = "http://autosar.org/schema/r4.0"
    parsed = ET.fromstring(ET.tostring(element, encoding="unicode"))
    return ARXMLParser().readChapterModel(parsed[0], _parent())


class TestTopicOrMsrQueryWriter:
    def test_write_emits_topics_and_msr_query_in_place(self):
        """TopicOrMsrQuery owns no wrapper element: XSD complexType TOPIC-OR-MSR-QUERY is an inline
        choice, so writeChapterModel splices TOPIC-1 / MSR-QUERY-TOPIC-1 into the CHAPTER-MODEL element."""
        element = ET.Element("CHAPTER")
        ARXMLWriter().writeChapterModel(element, ChapterModel().setTopic1(_full_query()))

        written = element.find("CHAPTER-MODEL")
        assert [child.tag for child in written] == ["TOPIC-1", "TOPIC-1", "MSR-QUERY-TOPIC-1"]
        assert [t.find("SHORT-NAME").text for t in written.findall("TOPIC-1")] == ["TopicA", "TopicB"]

    def test_write_empty_topic_or_msr_query(self):
        """An empty TopicOrMsrQuery contributes no payload children to CHAPTER-MODEL."""
        element = ET.Element("CHAPTER")
        ARXMLWriter().writeChapterModel(element, ChapterModel().setTopic1(TopicOrMsrQuery()))

        written = element.find("CHAPTER-MODEL")
        assert list(written) == []

    def test_topic_or_msr_query_arobject_level_round_trips(self):
        """TopicOrMsrQuery derives from ARObject and XSD complexType TOPIC-OR-MSR-QUERY pulls in the
        AR-OBJECT group, so the class's own T timestamp must survive the round-trip (Rule 0025 —
        a class with no read/write<Cls> helper silently loses its ARObject level)."""
        element = ET.Element("CHAPTER")
        ARXMLWriter().writeChapterModel(element, ChapterModel().setTopic1(_full_query()))

        written = element.find("CHAPTER-MODEL")
        assert written.get("T") == "2024-01-01T00:00:00+00:00"

        result = _reparse(element)
        assert result.getTopic1() is not None
        assert result.getTopic1().getTimestamp() is not None

    def test_incoming_timestamp_is_read(self):
        """A T attribute already on the wire is read onto the TopicOrMsrQuery, not only written.

        The TOPIC-1 element is included so the TOPIC-OR-MSR-QUERY group is unambiguously present:
        both TopicOrMsrQuery and ChapterModel are ARObjects sharing the same CHAPTER-MODEL element,
        so a bare T with no group payload would be indistinguishable from ChapterModel's own level.
        """
        element = ET.Element("CHAPTER")
        query = TopicOrMsrQuery()
        query.addTopic1(Topic1(_parent(), "TopicA"))
        ARXMLWriter().writeChapterModel(element, ChapterModel().setTopic1(query))
        element.find("CHAPTER-MODEL").set("T", "2024-05-05T00:00:00+00:00")

        result = _reparse(element)

        assert result.getTopic1() is not None
        assert result.getTopic1().getTimestamp() is not None

    def test_topic_or_msr_query_write_read_roundtrip(self):
        element = ET.Element("CHAPTER")
        ARXMLWriter().writeChapterModel(element, ChapterModel().setTopic1(_full_query()))

        result = _reparse(element)

        query = result.getTopic1()
        assert query is not None
        assert [topic.getShortName() for topic in query.getTopic1s()] == ["TopicA", "TopicB"]
        assert query.getMsrQueryTopic1() is not None
        assert query.getMsrQueryTopic1().getMsrQueryProps().getMsrQueryName().getValue() == "topic-query"
