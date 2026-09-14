import xml.etree.ElementTree as ET

from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel import SlParagraph


class TestReadSlParagraph:
    def test_reads_value_language_and_mixed_content(self, parser):
        element = ET.fromstring('<SL-PARAGRAPH xmlns="http://autosar.org/schema/r4.0" UUID="u1" L="en" S="true">text<TT>term</TT></SL-PARAGRAPH>')

        paragraph = SlParagraph()
        parser.readSlParagraph(element, paragraph)

        assert paragraph.getValue() == "text"
        assert paragraph.getL() == "en"
        assert paragraph.getTt() is not None
        assert paragraph.getTt().getValue().getValue() == "term"

    def test_reads_footnote(self, parser):
        element = ET.fromstring('<SL-PARAGRAPH xmlns="http://autosar.org/schema/r4.0">text<FT>footnote</FT></SL-PARAGRAPH>')

        paragraph = SlParagraph()
        parser.readSlParagraph(element, paragraph)

        assert paragraph.getFt() is not None
        assert paragraph.getFt().getValue() == "footnote"

    def test_reads_empty_optional_content(self, parser):
        paragraph = SlParagraph()

        parser.readSlParagraph(ET.fromstring('<SL-PARAGRAPH xmlns="http://autosar.org/schema/r4.0"/>'), paragraph)

        assert paragraph.getValue() == ""
        assert paragraph.getL() is None
        assert paragraph.getTt() is None
