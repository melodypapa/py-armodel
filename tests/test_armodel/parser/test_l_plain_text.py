"""Reader tests for the LPlainText class (AUTOSAR_FO_TPS_GenericStructureTemplate, Table 9.96)."""

import xml.etree.ElementTree as ET

from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel import LPlainText
from armodel.parser.arxml_parser import ARXMLParser


class TestLPlainTextParser:
    def test_read_l10_reads_l_plain_text(self):
        """The L-10 element (MultiLanguagePlainText.l10, Table 9.95 aggr of type LPlainText) must parse as LPlainText."""
        parser = ARXMLParser()
        element = ET.fromstring('<ROOT xmlns="http://autosar.org/schema/r4.0">' "<MULTI-LANGUAGE-PLAIN-TEXT>" '<L-10 L="EN">plain text</L-10>' "</MULTI-LANGUAGE-PLAIN-TEXT>" "</ROOT>")

        paragraph = parser.getMultiLanguagePlainText(element, "MULTI-LANGUAGE-PLAIN-TEXT")

        assert paragraph is not None
        l10 = paragraph.getL10s()[0]
        assert isinstance(l10, LPlainText)
        assert l10.getL() == "EN"
        assert l10.getValue() == "plain text"

    def test_read_used_languages_path(self):
        """The AdminData.usedLanguages consume path reads the same L-10 content."""
        parser = ARXMLParser()
        element = ET.fromstring('<ROOT xmlns="http://autosar.org/schema/r4.0">' "<USED-LANGUAGES>" '<L-10 L="DE">verwendete Sprachen</L-10>' "</USED-LANGUAGES>" "</ROOT>")

        paragraph = parser.getMultiLanguagePlainText(element, "USED-LANGUAGES")

        assert paragraph is not None
        l10 = paragraph.getL10s()[0]
        assert isinstance(l10, LPlainText)
        assert l10.getL() == "DE"
        assert l10.getValue() == "verwendete Sprachen"

    def test_read_multiple_l10s(self):
        """l10 is a 1..* aggregation: multiple L-10 elements keep order and values."""
        parser = ARXMLParser()
        element = ET.fromstring('<MULTI-LANGUAGE-PLAIN-TEXT xmlns="http://autosar.org/schema/r4.0">' '<L-10 L="EN">first</L-10>' '<L-10 L="DE">zweite</L-10>' "</MULTI-LANGUAGE-PLAIN-TEXT>")

        l10s = parser.getLPlainTexts(element, "L-10")

        assert len(l10s) == 2
        assert all(isinstance(l10, LPlainText) for l10 in l10s)
        assert l10s[0].getL() == "EN"
        assert l10s[0].getValue() == "first"
        assert l10s[1].getL() == "DE"
        assert l10s[1].getValue() == "zweite"

    def test_read_l10_without_l_attrib(self):
        parser = ARXMLParser()
        element = ET.fromstring('<ROOT xmlns="http://autosar.org/schema/r4.0">' "<MULTI-LANGUAGE-PLAIN-TEXT>" "<L-10>no language</L-10>" "</MULTI-LANGUAGE-PLAIN-TEXT>" "</ROOT>")

        paragraph = parser.getMultiLanguagePlainText(element, "MULTI-LANGUAGE-PLAIN-TEXT")

        l10 = paragraph.getL10s()[0]
        assert l10.getL() is None
        assert l10.getValue() == "no language"

    def test_read_missing_and_empty_wrapper(self):
        """A missing key yields None; an empty MULTI-LANGUAGE-PLAIN-TEXT wrapper yields an empty l10 list."""
        parser = ARXMLParser()
        element = ET.fromstring('<ROOT xmlns="http://autosar.org/schema/r4.0">' "<MULTI-LANGUAGE-PLAIN-TEXT></MULTI-LANGUAGE-PLAIN-TEXT>" "</ROOT>")

        assert parser.getMultiLanguagePlainText(element, "NOT-THERE") is None

        paragraph = parser.getMultiLanguagePlainText(element, "MULTI-LANGUAGE-PLAIN-TEXT")
        assert paragraph is not None
        assert paragraph.getL10s() == []
