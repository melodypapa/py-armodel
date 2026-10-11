"""Writer tests for the ChapterOrMsrQuery class (AUTOSAR_FO_TPS_GenericStructureTemplate, Table 9.81).

Multiplicity note: the PDF `Mult.` column renders `1` for `chapter`, but XSD group
CHAPTER-OR-MSR-QUERY (00052) declares `pureMM.maxOccurs="-1"` (unbounded) and the wire format
permits N CHAPTER elements per choice. Confirmed by the user at the TopicOrMsrQuery 9b (2026-10-11)
that the XSD-backed list shape is authoritative, so multiple chapters are written and round-tripped.
"""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DateTime, String
from armodel.models.M2.MSR.Documentation.Chapters import Chapter, ChapterModel, ChapterOrMsrQuery, Topic1, TopicOrMsrQuery
from armodel.models.M2.MSR.Documentation.MsrQuery import MsrQueryChapter, MsrQueryProps
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


def _parent():
    return AUTOSAR.getInstance().createARPackage("AUTOSAR")


def _full_query() -> ChapterOrMsrQuery:
    query = ChapterOrMsrQuery()
    query.setTimestamp(DateTime().setValue("2024-01-01T00:00:00+00:00"))
    query.addChapter(Chapter(_parent(), "NestedA"))
    query.addChapter(Chapter(_parent(), "NestedB"))
    query.setMsrQueryChapter(MsrQueryChapter().setMsrQueryProps(MsrQueryProps().setMsrQueryName(String().setValue("chapter-query"))))
    return query


def _reparse(element: ET.Element) -> ChapterModel:
    element.attrib["xmlns"] = "http://autosar.org/schema/r4.0"
    parsed = ET.fromstring(ET.tostring(element, encoding="unicode"))
    return ARXMLParser().readChapterModel(parsed[0], _parent())


class TestChapterOrMsrQueryWriter:
    def test_write_emits_chapters_and_msr_query_in_place(self):
        """ChapterOrMsrQuery owns no wrapper element: XSD complexType CHAPTER-OR-MSR-QUERY is an inline
        choice, so writeChapterModel splices CHAPTER / MSR-QUERY-CHAPTER into the CHAPTER-MODEL element."""
        element = ET.Element("CHAPTER")
        ARXMLWriter().writeChapterModel(element, ChapterModel().setChapter(_full_query()))

        written = element.find("CHAPTER-MODEL")
        assert [child.tag for child in written] == ["CHAPTER", "CHAPTER", "MSR-QUERY-CHAPTER"]
        assert [c.find("SHORT-NAME").text for c in written.findall("CHAPTER")] == ["NestedA", "NestedB"]

    def test_write_empty_chapter_or_msr_query(self):
        """An empty ChapterOrMsrQuery contributes no payload children to CHAPTER-MODEL."""
        element = ET.Element("CHAPTER")
        ARXMLWriter().writeChapterModel(element, ChapterModel().setChapter(ChapterOrMsrQuery()))

        written = element.find("CHAPTER-MODEL")
        assert list(written) == []

    def test_chapter_or_msr_query_does_not_write_arobject_onto_shared_wrapper(self):
        """ChapterOrMsrQuery's inherited ARObject level is deliberately NOT written onto the shared
        CHAPTER-MODEL element.

        <CHAPTER-MODEL> is a repo-invented synthetic wrapper (there is no <xsd:element
        name="CHAPTER-MODEL"> in 00052; the schema inlines <xsd:group ref="AR:CHAPTER-MODEL"> into
        the owning element, whose attributeGroup already carries AR-OBJECT). ChapterModel,
        TopicOrMsrQuery and ChapterOrMsrQuery therefore share ONE element, and writing ARObject
        attributes from more than one of them silently discards the others (last writer wins).
        """
        element = ET.Element("CHAPTER")
        ARXMLWriter().writeChapterModel(element, ChapterModel().setChapter(_full_query()))

        written = element.find("CHAPTER-MODEL")
        assert written.get("T") is None
        assert written.get("S") is None

    def test_shared_wrapper_is_not_overwritten_by_sibling_groups(self):
        """Regression guard for the shared-element collision: with a distinct T set on both the
        ChapterOrMsrQuery and its sibling TopicOrMsrQuery, neither may overwrite the wrapper's
        attributes. See the synthetic-wrapper note in Chapters.py."""
        query = ChapterOrMsrQuery()
        query.setTimestamp(DateTime().setValue("2024-01-01T00:00:00+00:00"))
        query.addChapter(Chapter(_parent(), "NestedA"))
        topic_query = TopicOrMsrQuery()
        topic_query.setTimestamp(DateTime().setValue("2024-02-02T00:00:00+00:00"))
        topic_query.addTopic1(Topic1(_parent(), "TopicA"))

        element = ET.Element("CHAPTER")
        ARXMLWriter().writeChapterModel(element, ChapterModel().setChapter(query).setTopic1(topic_query))

        assert element.find("CHAPTER-MODEL").get("T") is None

    def test_chapter_or_msr_query_write_read_roundtrip(self):
        element = ET.Element("CHAPTER")
        ARXMLWriter().writeChapterModel(element, ChapterModel().setChapter(_full_query()))

        result = _reparse(element)

        query = result.getChapter()
        assert query is not None
        assert [chapter.getShortName() for chapter in query.getChapters()] == ["NestedA", "NestedB"]
        assert query.getMsrQueryChapter() is not None
        assert query.getMsrQueryChapter().getMsrQueryProps().getMsrQueryName().getValue() == "chapter-query"
