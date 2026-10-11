"""Writer tests for the Chapter class (AUTOSAR_FO_TPS_GenericStructureTemplate, Table 9.58)."""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import String
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import VariationPoint
from armodel.models.M2.MSR.Documentation.Chapters import Chapter, ChapterModel
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


def _parent():
    document = AUTOSAR.getInstance()
    return document.createARPackage("AUTOSAR")


def _build_full_chapter() -> Chapter:
    chapter = Chapter(_parent(), "ChapterA")
    chapter.setHelpEntry(String().setValue("chapter.help.entry"))
    chapter.setChapterModel(ChapterModel())
    chapter.setVariationPoint(VariationPoint())
    return chapter


def _reparse(element: ET.Element) -> Chapter:
    """Serialize the parent element, re-parse it and hand the inner CHAPTER to the reader."""
    element.attrib["xmlns"] = "http://autosar.org/schema/r4.0"
    parsed = ET.fromstring(ET.tostring(element, encoding="unicode"))
    chapter_element = parsed[0]
    assert chapter_element.tag.endswith("CHAPTER")
    return ARXMLParser().readChapter(chapter_element, _parent())


class TestChapterWriter:
    def test_write_wraps_in_tag_name_element(self):
        """writeChapter emits under the caller-supplied tag name (CHAPTER for ChapterOrMsrQuery.chapter, the SW-*-NOTES tags for the SwComponentDocumentation pre-defined slots)."""
        element = ET.Element("CHAPTER")
        ARXMLWriter().writeChapter(element, _build_full_chapter(), "SW-FEATURE-DEF")

        written = element.find("SW-FEATURE-DEF")
        assert written is not None
        assert written.find("SHORT-NAME").text == "ChapterA"
        assert written.get("HELP-ENTRY") == "chapter.help.entry"

    def test_write_payload_element_order(self):
        """XSD group CHAPTER (00052 L16355) is <choice: CHAPTER-MODEL> then VARIATION-POINT (sequenceOffset=10000);
        VARIATION-POINT must therefore be emitted after CHAPTER-MODEL, not at the Identifiable level."""
        element = ET.Element("CHAPTER")
        ARXMLWriter().writeChapter(element, _build_full_chapter(), "CHAPTER")

        written = element.find("CHAPTER")
        assert [child.tag for child in written] == ["SHORT-NAME", "CHAPTER-MODEL", "VARIATION-POINT"]

    def test_write_empty_chapter(self):
        """An empty Chapter still writes the wrapper with only SHORT-NAME — no CHAPTER-MODEL, no VARIATION-POINT."""
        element = ET.Element("CHAPTER")
        ARXMLWriter().writeChapter(element, Chapter(_parent(), "BareChapter"), "CHAPTER")

        written = element.find("CHAPTER")
        assert [child.tag for child in written] == ["SHORT-NAME"]

    def test_chapter_write_read_roundtrip(self):
        element = ET.Element("SW-COMPONENT-DOCUMENTATION")
        ARXMLWriter().writeChapter(element, _build_full_chapter(), "CHAPTER")

        result = _reparse(element)

        assert result.getShortName() == "ChapterA"
        assert result.getHelpEntry().getValue() == "chapter.help.entry"
        assert result.getChapterModel() is not None
        assert result.getVariationPoint() is not None

    def test_incoming_variation_point_is_read(self):
        """A VARIATION-POINT arriving on the wire is read onto the Chapter, not only written from the model."""
        element = ET.Element("SW-COMPONENT-DOCUMENTATION")
        ARXMLWriter().writeChapter(element, Chapter(_parent(), "IncomingVP"), "CHAPTER")
        written = element.find("CHAPTER")
        vp_element = ET.SubElement(written, "VARIATION-POINT")
        ET.SubElement(vp_element, "SHORT-LABEL").text = "incoming variation point"
        ET.SubElement(vp_element, "DESC").text = "variation point description"

        result = _reparse(element)

        assert result.getVariationPoint() is not None
        assert result.getVariationPoint().getShortLabel().getValue() == "incoming variation point"
        assert result.getVariationPoint().getDesc() is not None
