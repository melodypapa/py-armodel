import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameTokens,
    String,
    ViewTokens,
)
from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView import ChapterEnumBreak, KeepWithPreviousEnum
from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel import LParagraph
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import MultiLanguageParagraph
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


def _build_paragraph() -> MultiLanguageParagraph:
    paragraph = MultiLanguageParagraph()
    paragraph.setSi(NameTokens().setValue("semantic"))
    paragraph.setView(ViewTokens().setValue("view-a"))
    paragraph.setBreak(ChapterEnumBreak().setValue(ChapterEnumBreak.BREAK))
    paragraph.setKeepWithPrevious(KeepWithPreviousEnum().setValue(KeepWithPreviousEnum.KEEP))
    paragraph.setHelpEntry(String().setValue("help-topic"))
    l1 = LParagraph()
    l1.setL("EN")
    l1.setValue("paragraph text")
    paragraph.addL1(l1)
    return paragraph


class TestMultiLanguageParagraph:
    def test_set_multi_language_paragraphs(self):
        root = ET.Element("ROOT")

        ARXMLWriter().setMultiLanguageParagraphs(root, "P", [_build_paragraph()])
        element = root.find("P")

        assert element is not None
        assert element.attrib["SI"] == "semantic"
        assert element.attrib["VIEW"] == "view-a"
        assert element.attrib["BREAK"] == "BREAK"
        assert element.attrib["KEEP-WITH-PREVIOUS"] == "KEEP"
        assert element.attrib["HELP-ENTRY"] == "help-topic"
        l1_element = element.find("L-1")
        assert l1_element.text == "paragraph text"
        assert l1_element.attrib["L"] == "EN"

    def test_set_multi_language_paragraphs_minimal(self):
        root = ET.Element("ROOT")

        ARXMLWriter().setMultiLanguageParagraphs(root, "P", [MultiLanguageParagraph()])
        element = root.find("P")

        assert element is not None
        assert "SI" not in element.attrib
        assert "VIEW" not in element.attrib
        assert "BREAK" not in element.attrib
        assert "KEEP-WITH-PREVIOUS" not in element.attrib
        assert "HELP-ENTRY" not in element.attrib
        assert element.find("L-1") is None

    def test_write_then_read_roundtrip(self):
        root = ET.Element("ROOT")
        ARXMLWriter().setMultiLanguageParagraphs(root, "P", [_build_paragraph()])

        wrapped = '<ROOT xmlns="http://autosar.org/schema/r4.0">' + ET.tostring(root.find("P"), encoding="unicode") + "</ROOT>"
        paragraphs = ARXMLParser().getMultiLanguageParagraphs(ET.fromstring(wrapped), "P")

        assert len(paragraphs) == 1
        paragraph = paragraphs[0]
        assert paragraph.getSi().getValue() == "semantic"
        assert paragraph.getView().getValue() == "view-a"
        assert paragraph.getBreak().getValue() == "BREAK"
        assert paragraph.getKeepWithPrevious().getValue() == "KEEP"
        assert paragraph.getHelpEntry().getValue() == "help-topic"
        assert paragraph.getL1s()[0].getValue() == "paragraph text"
        assert paragraph.getL1s()[0].getL() == "EN"
