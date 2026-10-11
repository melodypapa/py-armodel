"""Writer tests for the ChapterModel class (AUTOSAR_FO_TPS_GenericStructureTemplate, Table 9.59).

Wrapper note: <CHAPTER-MODEL> is a repo-invented synthetic wrapper — AUTOSAR_00052 declares
complexType CHAPTER-MODEL (sequence{AR-OBJECT, CHAPTER-MODEL} + attributeGroup AR-OBJECT) but no
element references it, reaching it only through the inlined group ref. It stands for ChapterModel
alone, so ChapterModel owns the wrapper's ARObject attributes (S/T). The two inlined groups it
contains — TopicOrMsrQuery and ChapterOrMsrQuery — deliberately do not write ARObject, since they
share that element and cannot each own S/T.
"""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DateTime
from armodel.models.M2.MSR.Documentation.Chapters import ChapterContent, ChapterModel, TopicContent, TopicContentOrMsrQuery
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


def _parent():
    return AUTOSAR.getInstance().createARPackage("AUTOSAR")


def _full_model() -> ChapterModel:
    model = ChapterModel()
    model.setTimestamp(DateTime().setValue("2024-01-01T00:00:00+00:00"))
    model.setChapterContent(ChapterContent().setTopicContent(TopicContentOrMsrQuery().setTopicContent(TopicContent())))
    return model


def _reparse(element: ET.Element) -> ChapterModel:
    element.attrib["xmlns"] = "http://autosar.org/schema/r4.0"
    parsed = ET.fromstring(ET.tostring(element, encoding="unicode"))
    model_element = parsed[0]
    assert model_element.tag.endswith("CHAPTER-MODEL")
    return ARXMLParser().readChapterModel(model_element, _parent())


class TestChapterModelWriter:
    def test_write_wraps_in_chapter_model_element(self):
        """writeChapterModel owns its CHAPTER-MODEL wrapper element."""
        element = ET.Element("CHAPTER")
        ARXMLWriter().writeChapterModel(element, _full_model())

        written = element.find("CHAPTER-MODEL")
        assert written is not None
        assert written.find("CHAPTER-CONTENT") is not None

    def test_write_empty_chapter_model(self):
        """An empty ChapterModel still writes the wrapper — no payload children."""
        element = ET.Element("CHAPTER")
        ARXMLWriter().writeChapterModel(element, ChapterModel())

        written = element.find("CHAPTER-MODEL")
        assert list(written) == []

    def test_chapter_model_arobject_level_round_trips(self):
        """XSD complexType CHAPTER-MODEL includes the AR-OBJECT group, and the CHAPTER-MODEL wrapper stands
        for ChapterModel alone, so its own T timestamp must survive the round-trip (Rule 0025 — a class
        whose own entry point never calls readARObject/writeARObject silently loses S/T)."""
        element = ET.Element("CHAPTER")
        ARXMLWriter().writeChapterModel(element, _full_model())

        written = element.find("CHAPTER-MODEL")
        assert written.get("T") == "2024-01-01T00:00:00+00:00"

        result = _reparse(element)
        assert result.getTimestamp() is not None

    def test_incoming_timestamp_is_read(self):
        """A T attribute already on the wire is read onto the ChapterModel, not only written."""
        element = ET.Element("CHAPTER")
        ARXMLWriter().writeChapterModel(element, ChapterModel())
        element.find("CHAPTER-MODEL").set("T", "2024-05-05T00:00:00+00:00")

        result = _reparse(element)

        assert result.getTimestamp() is not None

    def test_payload_is_split_into_per_member_helpers(self):
        """readChapterModel / writeChapterModel dispatch one helper per aggregated member, in XSD
        sequenceOffset order (chapterContent 30 < topic1 170 < chapter 200) — Rule 0001.7 + 0001.11."""
        from armodel.parser.arxml_parser import ARXMLParser
        from armodel.writer.arxml_writer import ARXMLWriter

        for name in ("readChapterModelChapterContent", "readChapterModelTopic1", "readChapterModelChapter"):
            assert callable(getattr(ARXMLParser, name)), name
        for name in ("writeChapterModelChapterContent", "writeChapterModelTopic1", "writeChapterModelChapter"):
            assert callable(getattr(ARXMLWriter, name)), name

    def test_chapter_model_write_read_roundtrip(self):
        element = ET.Element("CHAPTER")
        ARXMLWriter().writeChapterModel(element, _full_model())

        result = _reparse(element)

        assert result.getChapterContent() is not None
        assert result.getChapterContent().getTopicContent() is not None
        assert result.getTopic1() is None
        assert result.getChapter() is None
