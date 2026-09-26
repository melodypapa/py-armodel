"""Reader tests for MixedContentForOverviewParagraph (AUTOSAR_FO_TPS_GenericStructureTemplate, Table 9.3) via its L-2 consumer element."""

import xml.etree.ElementTree as ET

from armodel.models.M2.MSR.Documentation.TextModel.InlineTextElements import Br, EmphasisText, IndexEntry, Superscript, Tt, Xref, XrefTarget
from armodel.models.M2.MSR.Documentation.TextModel.SingleLanguageData import SlOverviewParagraph
from armodel.parser.arxml_parser import ARXMLParser

_L2_WITH_CHILDREN = (
    '<ROOT xmlns="http://autosar.org/schema/r4.0">'
    "<MULTI-LANGUAGE-OVERVIEW-PARAGRAPH>"
    '<L-2 L="EN" SUB="sub text" SUP="sup text">overview text'
    "<BR/>"
    '<E COLOR="blue">emphasized overview</E>'
    "<IE>index entry</IE>"
    '<TRACE-REF DEST="TRACEABLE">traceable-obj</TRACE-REF>'
    "<TT>technical term</TT>"
    "<XREF/>"
    "<XREF-TARGET><SHORT-NAME>TARGET</SHORT-NAME></XREF-TARGET>"
    "</L-2>"
    "</MULTI-LANGUAGE-OVERVIEW-PARAGRAPH>"
    "</ROOT>"
)


class TestMixedContentForOverviewParagraphParser:
    def test_read_l2_reads_mixed_content_children(self):
        """The L-2 complexType composes MIXED-CONTENT-FOR-OVERVIEW-PARAGRAPH (XSD 00052 L76250) — the BR/E/IE/TRACE-REF/TT/XREF/XREF-TARGET child elements and the SUB/SUP XML attributes (Kind=attr, family convention) must populate the base members (Table 9.3)."""
        parser = ARXMLParser()
        element = ET.fromstring(_L2_WITH_CHILDREN)

        paragraph = parser.getMultiLanguageOverviewParagraph(element, "MULTI-LANGUAGE-OVERVIEW-PARAGRAPH")

        assert paragraph is not None
        l2 = paragraph.getL2s()[0]
        assert isinstance(l2.getBr(), Br)
        assert isinstance(l2.getE(), EmphasisText)
        assert l2.getE().getValue().getValue() == "emphasized overview"
        assert isinstance(l2.getIe(), IndexEntry)
        assert l2.getIe().getValue().getValue() == "index entry"
        assert isinstance(l2.getSub(), Superscript)
        assert l2.getSub().getValue() == "sub text"
        assert isinstance(l2.getSup(), Superscript)
        assert l2.getSup().getValue() == "sup text"
        assert l2.getTraceRef().getValue() == "traceable-obj"
        assert l2.getTraceRef().getDest() == "TRACEABLE"
        assert isinstance(l2.getTt(), Tt)
        assert l2.getTt().getValue().getValue() == "technical term"
        assert isinstance(l2.getXref(), Xref)
        assert isinstance(l2.getXrefTarget(), XrefTarget)

    def test_read_l2_without_mixed_content_children(self):
        parser = ARXMLParser()
        element = ET.fromstring(
            '<ROOT xmlns="http://autosar.org/schema/r4.0">' "<MULTI-LANGUAGE-OVERVIEW-PARAGRAPH>" '<L-2 L="DE">plain overview</L-2>' "</MULTI-LANGUAGE-OVERVIEW-PARAGRAPH>" "</ROOT>"
        )

        paragraph = parser.getMultiLanguageOverviewParagraph(element, "MULTI-LANGUAGE-OVERVIEW-PARAGRAPH")

        l2 = paragraph.getL2s()[0]
        assert l2.getValue() == "plain overview"
        assert l2.getBr() is None
        assert l2.getE() is None
        assert l2.getIe() is None
        assert l2.getSub() is None
        assert l2.getSup() is None
        assert l2.getTraceRef() is None
        assert l2.getTt() is None
        assert l2.getXref() is None
        assert l2.getXrefTarget() is None

    def test_read_l2_mixed_content_via_get_l_overview_paragraphs(self):
        """The IndentSample consume path (getLOverviewParagraphs) must populate the mixed content too."""
        parser = ARXMLParser()
        element = ET.fromstring(
            '<MULTI-LANGUAGE-OVERVIEW-PARAGRAPH xmlns="http://autosar.org/schema/r4.0">' '<L-2 L="EN">overview text<TT>technical term</TT></L-2>' "</MULTI-LANGUAGE-OVERVIEW-PARAGRAPH>"
        )

        l2s = parser.getLOverviewParagraphs(element, "L-2")

        assert len(l2s) == 1
        assert l2s[0].getTt() is not None
        assert l2s[0].getTt().getValue().getValue() == "technical term"


class TestReadSlOverviewParagraph:
    def test_read_l2_reads_ft_sl_overview_paragraph(self):
        """The FT child element (type SL-OVERVIEW-PARAGRAPH, XSD 00052 L81345) must populate the ft member with a SlOverviewParagraph carrying its L attribute, text and own mixed content (Table E.70)."""
        parser = ARXMLParser()
        element = ET.fromstring(
            '<ROOT xmlns="http://autosar.org/schema/r4.0">'
            "<MULTI-LANGUAGE-OVERVIEW-PARAGRAPH>"
            '<L-2 L="EN">overview text'
            '<FT L="DE">footnote text<TT>term in footnote</TT></FT>'
            "<BR/>"
            "</L-2>"
            "</MULTI-LANGUAGE-OVERVIEW-PARAGRAPH>"
            "</ROOT>"
        )

        paragraph = parser.getMultiLanguageOverviewParagraph(element, "MULTI-LANGUAGE-OVERVIEW-PARAGRAPH")

        assert paragraph is not None
        l2 = paragraph.getL2s()[0]
        assert l2.getValue() == "overview text"
        footnote = l2.getFt()
        assert isinstance(footnote, SlOverviewParagraph)
        assert footnote.getValue() == "footnote text"
        assert footnote.getL() == "DE"
        assert isinstance(footnote.getTt(), Tt)
        assert footnote.getTt().getValue().getValue() == "term in footnote"

    def test_read_l2_without_ft_leaves_ft_none(self):
        parser = ARXMLParser()
        element = ET.fromstring(
            '<ROOT xmlns="http://autosar.org/schema/r4.0">' "<MULTI-LANGUAGE-OVERVIEW-PARAGRAPH>" '<L-2 L="EN">overview text</L-2>' "</MULTI-LANGUAGE-OVERVIEW-PARAGRAPH>" "</ROOT>"
        )

        paragraph = parser.getMultiLanguageOverviewParagraph(element, "MULTI-LANGUAGE-OVERVIEW-PARAGRAPH")

        l2 = paragraph.getL2s()[0]
        assert l2.getValue() == "overview text"
        assert l2.getFt() is None
