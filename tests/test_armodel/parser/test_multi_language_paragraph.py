import xml.etree.ElementTree as ET

from armodel.parser.arxml_parser import ARXMLParser


class TestMultiLanguageParagraph:
    def test_get_multi_language_paragraphs(self):
        element = ET.fromstring(
            '<ROOT xmlns="http://autosar.org/schema/r4.0">'
            '<P SI="semantic" VIEW="view-a" BREAK="BREAK" KEEP-WITH-PREVIOUS="KEEP" HELP-ENTRY="help-topic">'
            "<L-1 L='EN'>paragraph text</L-1>"
            "</P>"
            "</ROOT>"
        )

        paragraphs = ARXMLParser().getMultiLanguageParagraphs(element, "P")

        assert len(paragraphs) == 1
        paragraph = paragraphs[0]
        assert paragraph.getSi().getValue() == "semantic"
        assert paragraph.getView().getValue() == "view-a"
        assert paragraph.getBreak().getValue() == "BREAK"
        assert paragraph.getKeepWithPrevious().getValue() == "KEEP"
        assert paragraph.getHelpEntry().getValue() == "help-topic"
        assert paragraph.getL1s()[0].getValue() == "paragraph text"
        assert paragraph.getL1s()[0].getL() == "EN"

    def test_get_multi_language_paragraphs_minimal(self):
        element = ET.fromstring('<ROOT xmlns="http://autosar.org/schema/r4.0"><P /></ROOT>')

        paragraphs = ARXMLParser().getMultiLanguageParagraphs(element, "P")

        assert len(paragraphs) == 1
        paragraph = paragraphs[0]
        assert paragraph.getSi() is None
        assert paragraph.getView() is None
        assert paragraph.getBreak() is None
        assert paragraph.getKeepWithPrevious() is None
        assert paragraph.getHelpEntry() is None
        assert paragraph.getL1s() == []
