"""Writer tests for the PredefinedChapter class (AUTOSAR_FO_TPS_GenericStructureTemplate, Table 9.62)."""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.StereotypeMixins import VariationPointCapable
from armodel.models.M2.MSR.Documentation.Chapters import ChapterContent, ChapterModel, PredefinedChapter
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


def _full_predefined_chapter() -> PredefinedChapter:
    chapter_model = ChapterModel()
    chapter_model.setChapterContent(ChapterContent())
    return PredefinedChapter().setChapterModel(chapter_model)


class TestPredefinedChapterWriter:
    def test_write_emits_chapter_model_in_place(self):
        """PredefinedChapter owns no wrapper element: writePredefinedChapter emits the ARObject attributes and the
        CHAPTER-MODEL payload straight into the caller's element (XSD group PREDEFINED-CHAPTER, 00052 L8739)."""
        element = ET.Element("DOCUMENTATION-CONTENT")
        ARXMLWriter().writePredefinedChapter(element, _full_predefined_chapter())

        assert [child.tag for child in element] == ["CHAPTER-MODEL"]

    def test_write_empty_predefined_chapter(self):
        """An empty PredefinedChapter writes nothing — no CHAPTER-MODEL wrapper for an unset attribute."""
        element = ET.Element("DOCUMENTATION-CONTENT")
        ARXMLWriter().writePredefinedChapter(element, PredefinedChapter())

        assert list(element) == []

    def test_write_none_is_a_no_op(self):
        """writePredefinedChapter returns early on None (the 0..1 aggregator slot is unset)."""
        element = ET.Element("DOCUMENTATION-CONTENT")
        ARXMLWriter().writePredefinedChapter(element, None)

        assert list(element) == []

    def test_predefined_chapter_write_read_roundtrip(self):
        element = ET.Element("DOCUMENTATION-CONTENT")
        ARXMLWriter().writePredefinedChapter(element, _full_predefined_chapter())
        element.attrib["xmlns"] = "http://autosar.org/schema/r4.0"
        parsed = ET.fromstring(ET.tostring(element, encoding="unicode"))

        result = ARXMLParser().readPredefinedChapter(parsed)

        assert isinstance(result, PredefinedChapter)
        assert result.getChapterModel() is not None
        assert result.getChapterModel().getChapterContent() is not None
        assert result.getChapterModel().getTopic1() is None

    def test_incoming_chapter_model_is_read(self):
        """A CHAPTER-MODEL arriving on the wire populates the model, not only the write direction."""
        element = ET.Element("DOCUMENTATION-CONTENT")
        ET.SubElement(element, "CHAPTER-MODEL")
        element.attrib["xmlns"] = "http://autosar.org/schema/r4.0"
        parsed = ET.fromstring(ET.tostring(element, encoding="unicode"))

        result = ARXMLParser().readPredefinedChapter(parsed)

        assert result.getChapterModel() is not None
        assert isinstance(result.getChapterModel(), ChapterModel)

    def test_predefined_chapter_is_not_variation_point_capable(self):
        """XSD group PREDEFINED-CHAPTER declares no VARIATION-POINT (unlike group CHAPTER), and the class does not
        inherit VariationPointCapable — so no variation point is modeled or serialized for it."""
        assert not isinstance(PredefinedChapter(), VariationPointCapable)
