"""Reader tests for MixedContentForVerbatim (AUTOSAR_FO_TPS_GenericStructureTemplate, Table 9.6) via its L-5 consumer element."""

import xml.etree.ElementTree as ET

from armodel.models.M2.MSR.Documentation.TextModel.InlineTextElements import Br, EmphasisText, Tt, Xref
from armodel.parser.arxml_parser import ARXMLParser

_L5_WITH_CHILDREN = (
    '<ROOT xmlns="http://autosar.org/schema/r4.0">'
    "<MULTI-LANGUAGE-VERBATIM>"
    '<L-5 L="EN">verbatim text'
    "<BR/>"
    '<E COLOR="blue">emphasized verbatim</E>'
    "<TT>technical term</TT>"
    "<XREF/>"
    "</L-5>"
    "</MULTI-LANGUAGE-VERBATIM>"
    "</ROOT>"
)


class TestMixedContentForVerbatimParser:
    def test_read_l5_reads_mixed_content_children(self):
        """The L-5 complexType composes MIXED-CONTENT-FOR-VERBATIM (XSD 00052 L76319) — the BR/E/TT/XREF child elements must populate the base members (Table 9.6)."""
        parser = ARXMLParser()
        element = ET.fromstring(_L5_WITH_CHILDREN)

        verbatim = parser.getMultiLanguageVerbatim(element, "MULTI-LANGUAGE-VERBATIM")

        assert verbatim is not None
        l5 = verbatim.getL5s()[0]
        assert isinstance(l5.getBr(), Br)
        assert isinstance(l5.getE(), EmphasisText)
        assert l5.getE().getValue().getValue() == "emphasized verbatim"
        assert isinstance(l5.getTt(), Tt)
        assert l5.getTt().getValue().getValue() == "technical term"
        assert isinstance(l5.getXref(), Xref)

    def test_read_l5_without_mixed_content_children(self):
        parser = ARXMLParser()
        element = ET.fromstring('<ROOT xmlns="http://autosar.org/schema/r4.0">' "<MULTI-LANGUAGE-VERBATIM>" '<L-5 L="DE">plain verbatim</L-5>' "</MULTI-LANGUAGE-VERBATIM>" "</ROOT>")

        verbatim = parser.getMultiLanguageVerbatim(element, "MULTI-LANGUAGE-VERBATIM")

        l5 = verbatim.getL5s()[0]
        assert l5.getValue() == "plain verbatim"
        assert l5.getBr() is None
        assert l5.getE() is None
        assert l5.getTt() is None
        assert l5.getXref() is None

    def test_read_l5_mixed_content_via_consume_path(self):
        """The figure/formula/block consume path (VERBATIM wrapper element) must populate the mixed content too."""
        parser = ARXMLParser()
        element = ET.fromstring('<ROOT xmlns="http://autosar.org/schema/r4.0">' "<VERBATIM>" '<L-5 L="EN">verbatim text<TT>technical term</TT></L-5>' "</VERBATIM>" "</ROOT>")

        verbatim = parser.getMultiLanguageVerbatim(element, "VERBATIM")

        l5 = verbatim.getL5s()[0]
        assert l5.getTt() is not None
        assert l5.getTt().getValue().getValue() == "technical term"
