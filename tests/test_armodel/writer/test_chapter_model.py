"""Writer tests for the ChapterModel class (AUTOSAR_FO_TPS_GenericStructureTemplate, Table 9.59)."""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import String
from armodel.models.M2.MSR.Documentation.Chapters import (
    Chapter,
    ChapterContent,
    ChapterModel,
    ChapterOrMsrQuery,
    Topic1,
    TopicContent,
    TopicContentOrMsrQuery,
    TopicOrMsrQuery,
)
from armodel.models.M2.MSR.Documentation.MsrQuery import MsrQueryChapter, MsrQueryProps, MsrQueryTopic1
from armodel.models.M2.MSR.Documentation.TextModel.BlockElements import DocumentationBlock
from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel import LParagraph
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import MultiLanguageParagraph
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


def _parent():
    document = AUTOSAR.getInstance()
    return document.createARPackage("AUTOSAR")


def _build_full_chapter_model() -> ChapterModel:
    parent = _parent()

    paragraph = MultiLanguageParagraph()
    l1 = LParagraph()
    l1.setL("EN")
    l1.setValue("chapter content")
    paragraph.addL1(l1)
    block = DocumentationBlock()
    block.addP(paragraph)

    topic_props = MsrQueryProps().setMsrQueryName(String().setValue("topic-query"))
    chapter_props = MsrQueryProps().setMsrQueryName(String().setValue("chapter-query"))

    return (
        ChapterModel()
        .setChapterContent(ChapterContent().setTopicContent(TopicContentOrMsrQuery().setTopicContent(TopicContent().setBlockLevelContent(block))))
        .setTopic1(TopicOrMsrQuery().addTopic1(Topic1(parent, "TopicA")).addTopic1(Topic1(parent, "TopicB")).setMsrQueryTopic1(MsrQueryTopic1().setMsrQueryProps(topic_props)))
        .setChapter(ChapterOrMsrQuery().addChapter(Chapter(parent, "ChapterA")).addChapter(Chapter(parent, "ChapterB")).setMsrQueryChapter(MsrQueryChapter().setMsrQueryProps(chapter_props)))
    )


class TestChapterModelWriter:
    def test_write_wraps_in_chapter_model_element(self):
        """The chapter model is serialized under a CHAPTER-MODEL wrapper element (XSD element CHAPTER-MODEL)."""
        element = ET.Element("CHAPTER")

        ARXMLWriter().writeChapterModel(element, _build_full_chapter_model())

        written = element.find("CHAPTER-MODEL")
        assert written is not None
        assert written.find("CHAPTER-CONTENT/TOPIC-CONTENT/DOCUMENTATION-BLOCK/P/L-1").text == "chapter content"
        assert written.find("MSR-QUERY-TOPIC-1/MSR-QUERY-PROPS/MSR-QUERY-NAME").text == "topic-query"
        assert written.find("MSR-QUERY-CHAPTER/MSR-QUERY-PROPS/MSR-QUERY-NAME").text == "chapter-query"

    def test_write_payload_element_order(self):
        """XSD group CHAPTER-MODEL order: CHAPTER-CONTENT payload first, then the TOPIC-OR-MSR-QUERY payloads (TOPIC-1, MSR-QUERY-TOPIC-1), then the CHAPTER-OR-MSR-QUERY payloads (CHAPTER, MSR-QUERY-CHAPTER)."""
        element = ET.Element("CHAPTER")

        ARXMLWriter().writeChapterModel(element, _build_full_chapter_model())

        written = element.find("CHAPTER-MODEL")
        assert [child.tag for child in written] == [
            "CHAPTER-CONTENT",
            "TOPIC-1",
            "TOPIC-1",
            "MSR-QUERY-TOPIC-1",
            "CHAPTER",
            "CHAPTER",
            "MSR-QUERY-CHAPTER",
        ]

    def test_write_empty_chapter_model(self):
        """An empty ChapterModel still writes the CHAPTER-MODEL wrapper with no payload children (round-trips as an empty wrapper)."""
        element = ET.Element("CHAPTER")

        ARXMLWriter().writeChapterModel(element, ChapterModel())

        written = element.find("CHAPTER-MODEL")
        assert written is not None
        assert list(written) == []

    def test_chapter_model_write_read_roundtrip(self):
        writer_element = ET.Element("CHAPTER")
        ARXMLWriter().writeChapterModel(writer_element, _build_full_chapter_model())
        writer_element.attrib["xmlns"] = "http://autosar.org/schema/r4.0"
        parsed = ET.fromstring(ET.tostring(writer_element, encoding="unicode"))
        model_element = parsed[0]
        assert model_element.tag.endswith("CHAPTER-MODEL")

        result = ARXMLParser().readChapterModel(model_element, None)

        assert result.getChapterContent().getTopicContent().getTopicContent().getBlockLevelContent().getPs()[0].getL1s()[0].getValue() == "chapter content"
        topic1 = result.getTopic1()
        assert [topic.getShortName() for topic in topic1.getTopic1s()] == ["TopicA", "TopicB"]
        assert topic1.getMsrQueryTopic1().getMsrQueryProps().getMsrQueryName().getValue() == "topic-query"
        chapter = result.getChapter()
        assert [sub_chapter.getShortName() for sub_chapter in chapter.getChapters()] == ["ChapterA", "ChapterB"]
        assert chapter.getMsrQueryChapter().getMsrQueryProps().getMsrQueryName().getValue() == "chapter-query"
