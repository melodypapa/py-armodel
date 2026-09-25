"""Writer tests for the LPlainText class (AUTOSAR_FO_TPS_GenericStructureTemplate, Table 9.96)."""

import xml.etree.ElementTree as ET

from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel import LPlainText
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import MultiLanguagePlainText
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


def _build_l_plain_text() -> LPlainText:
    l10 = LPlainText()
    l10.setL("EN")
    l10.setValue("plain text")
    return l10


class TestLPlainTextWriter:
    def test_write_l10_writes_l_attrib_and_text(self):
        """The l10 aggregation must serialize as the L-10 element with the L XML attribute and the text content (XSD 00052 L-PLAIN-TEXT, mixed=true)."""
        element = ET.Element("MULTI-LANGUAGE-PLAIN-TEXT")

        ARXMLWriter().setMultiLanguagePlainText(element, "MULTI-LANGUAGE-PLAIN-TEXT", MultiLanguagePlainText().addL10(_build_l_plain_text()))

        written = element.find("MULTI-LANGUAGE-PLAIN-TEXT/L-10")
        assert written is not None
        assert written.attrib["L"] == "EN"
        assert written.text == "plain text"

    def test_write_l10_without_l_omits_attrib(self):
        element = ET.Element("MULTI-LANGUAGE-PLAIN-TEXT")
        l10 = LPlainText()
        l10.setValue("no language")

        ARXMLWriter().setMultiLanguagePlainText(element, "MULTI-LANGUAGE-PLAIN-TEXT", MultiLanguagePlainText().addL10(l10))

        written = element.find("MULTI-LANGUAGE-PLAIN-TEXT/L-10")
        assert written is not None
        assert "L" not in written.attrib
        assert written.text == "no language"

    def test_write_empty_wrapper_has_no_l10_children(self):
        element = ET.Element("ROOT")

        ARXMLWriter().setMultiLanguagePlainText(element, "MULTI-LANGUAGE-PLAIN-TEXT", MultiLanguagePlainText())

        written = element.find("MULTI-LANGUAGE-PLAIN-TEXT")
        assert written is not None
        assert written.find("L-10") is None

    def test_l_plain_text_write_read_roundtrip(self):
        writer_element = ET.Element("ROOT")
        ARXMLWriter().setMultiLanguagePlainText(writer_element, "MULTI-LANGUAGE-PLAIN-TEXT", MultiLanguagePlainText().addL10(_build_l_plain_text()))
        writer_element.attrib["xmlns"] = "http://autosar.org/schema/r4.0"
        parsed = ET.fromstring(ET.tostring(writer_element, encoding="unicode"))

        result = ARXMLParser().getMultiLanguagePlainText(parsed, "MULTI-LANGUAGE-PLAIN-TEXT")

        assert result is not None
        l10 = result.getL10s()[0]
        assert isinstance(l10, LPlainText)
        assert l10.getL() == "EN"
        assert l10.getValue() == "plain text"
