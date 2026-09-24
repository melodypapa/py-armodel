"""Reader tests for the LOverviewParagraph class (AUTOSAR_FO_TPS_GenericStructureTemplate, Table 9.91)."""

import xml.etree.ElementTree as ET

from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel import LOverviewParagraph
from armodel.parser.arxml_parser import ARXMLParser


class TestLOverviewParagraphParser:
    def test_read_l2_reads_blueprint_value(self):
        """The BLUEPRINT-VALUE XML attribute (XSD 00052 attributeGroup L-OVERVIEW-PARAGRAPH) must populate blueprintValue (Table 9.91)."""
        parser = ARXMLParser()
        element = ET.fromstring(
            '<ROOT xmlns="http://autosar.org/schema/r4.0">'
            "<MULTI-LANGUAGE-OVERVIEW-PARAGRAPH>"
            '<L-2 L="EN" BLUEPRINT-VALUE="blueprint documentation">overview text</L-2>'
            "</MULTI-LANGUAGE-OVERVIEW-PARAGRAPH>"
            "</ROOT>"
        )

        paragraph = parser.getMultiLanguageOverviewParagraph(element, "MULTI-LANGUAGE-OVERVIEW-PARAGRAPH")

        assert paragraph is not None
        l2 = paragraph.getL2s()[0]
        assert isinstance(l2, LOverviewParagraph)
        assert l2.getBlueprintValue() == "blueprint documentation"
        assert l2.getValue() == "overview text"
        assert l2.getL() == "EN"

    def test_read_l2_via_get_l_overview_paragraphs(self):
        """The IndentSample consume path (getLOverviewParagraphs) must also carry BLUEPRINT-VALUE."""
        parser = ARXMLParser()
        element = ET.fromstring(
            '<MULTI-LANGUAGE-OVERVIEW-PARAGRAPH xmlns="http://autosar.org/schema/r4.0">'
            '<L-2 L="EN" BLUEPRINT-VALUE="blueprint documentation">overview text</L-2>'
            "</MULTI-LANGUAGE-OVERVIEW-PARAGRAPH>"
        )

        l2s = parser.getLOverviewParagraphs(element, "L-2")

        assert len(l2s) == 1
        assert l2s[0].getBlueprintValue() == "blueprint documentation"
        assert l2s[0].getValue() == "overview text"

    def test_read_l2_without_blueprint_value(self):
        parser = ARXMLParser()
        element = ET.fromstring(
            '<ROOT xmlns="http://autosar.org/schema/r4.0">' "<MULTI-LANGUAGE-OVERVIEW-PARAGRAPH>" '<L-2 L="DE">ohne blueprint</L-2>' "</MULTI-LANGUAGE-OVERVIEW-PARAGRAPH>" "</ROOT>"
        )

        paragraph = parser.getMultiLanguageOverviewParagraph(element, "MULTI-LANGUAGE-OVERVIEW-PARAGRAPH")

        assert paragraph.getL2s()[0].getBlueprintValue() is None
        assert paragraph.getL2s()[0].getValue() == "ohne blueprint"
