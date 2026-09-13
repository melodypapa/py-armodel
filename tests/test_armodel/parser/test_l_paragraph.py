import xml.etree.ElementTree as ET

from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel import LParagraph


class TestReadLParagraph:
    def test_reads_value_language_and_mixed_content(self, parser):
        element = ET.fromstring('<P xmlns="http://autosar.org/schema/r4.0">' '<L-1 L="en">text<TT>term</TT></L-1>' "</P>")

        paragraphs = parser.getLParagraphs(element, "L-1")

        assert len(paragraphs) == 1
        l1 = paragraphs[0]
        assert isinstance(l1, LParagraph)
        assert l1.getValue() == "text"
        assert l1.getL() == "en"
        assert l1.getTt() is not None
        assert l1.getTt().getValue().getValue() == "term"

    def test_reads_footnote(self, parser):
        element = ET.fromstring('<P xmlns="http://autosar.org/schema/r4.0">' "<L-1>text<FT>footnote</FT></L-1>" "</P>")

        paragraphs = parser.getLParagraphs(element, "L-1")

        assert len(paragraphs) == 1
        assert paragraphs[0].getFt() is not None
        assert paragraphs[0].getFt().getValue() == "footnote"

    def test_reads_empty_optional_content(self, parser):
        element = ET.fromstring('<P xmlns="http://autosar.org/schema/r4.0"><L-1/></P>')

        paragraphs = parser.getLParagraphs(element, "L-1")

        assert len(paragraphs) == 1
        l1 = paragraphs[0]
        assert l1.getValue() == ""
        assert l1.getL() is None
        assert l1.getTt() is None
