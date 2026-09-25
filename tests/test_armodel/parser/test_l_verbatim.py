"""Reader tests for the LVerbatim class (AUTOSAR_FO_TPS_GenericStructureTemplate, Table 9.89)."""

import xml.etree.ElementTree as ET

from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel import LVerbatim
from armodel.parser.arxml_parser import ARXMLParser


class TestLVerbatimParser:
    def test_read_l5_reads_l_verbatim(self):
        """The L-5 element (MultiLanguageVerbatim.l5, Table 9.5 aggr of type LVerbatim) must parse as LVerbatim."""
        parser = ARXMLParser()
        element = ET.fromstring('<ROOT xmlns="http://autosar.org/schema/r4.0">' "<MULTI-LANGUAGE-VERBATIM>" '<L-5 L="EN">verbatim text</L-5>' "</MULTI-LANGUAGE-VERBATIM>" "</ROOT>")

        verbatim = parser.getMultiLanguageVerbatim(element, "MULTI-LANGUAGE-VERBATIM")

        assert verbatim is not None
        l5 = verbatim.getL5s()[0]
        assert isinstance(l5, LVerbatim)
        assert l5.getL() == "EN"
        assert l5.getValue() == "verbatim text"

    def test_read_verbatim_consume_path(self):
        """The figure/formula/block consume path reads the L-5 content from a VERBATIM wrapper element."""
        parser = ARXMLParser()
        element = ET.fromstring('<ROOT xmlns="http://autosar.org/schema/r4.0">' "<VERBATIM>" '<L-5 L="DE">Beibehaltener Text</L-5>' "</VERBATIM>" "</ROOT>")

        verbatim = parser.getMultiLanguageVerbatim(element, "VERBATIM")

        assert verbatim is not None
        l5 = verbatim.getL5s()[0]
        assert isinstance(l5, LVerbatim)
        assert l5.getL() == "DE"
        assert l5.getValue() == "Beibehaltener Text"

    def test_read_multiple_l5s(self):
        """l5 is a 1..* aggregation: multiple L-5 elements keep order and values."""
        parser = ARXMLParser()
        element = ET.fromstring('<ROOT xmlns="http://autosar.org/schema/r4.0">' "<MULTI-LANGUAGE-VERBATIM>" '<L-5 L="EN">first</L-5>' '<L-5 L="DE">zweite</L-5>' "</MULTI-LANGUAGE-VERBATIM>" "</ROOT>")

        verbatim = parser.getMultiLanguageVerbatim(element, "MULTI-LANGUAGE-VERBATIM")

        l5s = verbatim.getL5s()
        assert len(l5s) == 2
        assert all(isinstance(l5, LVerbatim) for l5 in l5s)
        assert l5s[0].getL() == "EN"
        assert l5s[0].getValue() == "first"
        assert l5s[1].getL() == "DE"
        assert l5s[1].getValue() == "zweite"

    def test_read_l5_without_l_attrib(self):
        parser = ARXMLParser()
        element = ET.fromstring('<ROOT xmlns="http://autosar.org/schema/r4.0">' "<MULTI-LANGUAGE-VERBATIM>" "<L-5>no language</L-5>" "</MULTI-LANGUAGE-VERBATIM>" "</ROOT>")

        verbatim = parser.getMultiLanguageVerbatim(element, "MULTI-LANGUAGE-VERBATIM")

        l5 = verbatim.getL5s()[0]
        assert l5.getL() is None
        assert l5.getValue() == "no language"

    def test_read_missing_and_empty_wrapper(self):
        """A missing key yields None; an empty MULTI-LANGUAGE-VERBATIM wrapper yields an empty l5 list."""
        parser = ARXMLParser()
        element = ET.fromstring('<ROOT xmlns="http://autosar.org/schema/r4.0">' "<MULTI-LANGUAGE-VERBATIM></MULTI-LANGUAGE-VERBATIM>" "</ROOT>")

        assert parser.getMultiLanguageVerbatim(element, "NOT-THERE") is None

        verbatim = parser.getMultiLanguageVerbatim(element, "MULTI-LANGUAGE-VERBATIM")
        assert verbatim is not None
        assert verbatim.getL5s() == []
