"""Writer tests for the LOverviewParagraph class (AUTOSAR_FO_TPS_GenericStructureTemplate, Table 9.91)."""

import xml.etree.ElementTree as ET

from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel import LOverviewParagraph
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import MultiLanguageOverviewParagraph
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


def _build_l_overview_paragraph() -> LOverviewParagraph:
    l2 = LOverviewParagraph()
    l2.setL("EN")
    l2.setValue("overview text")
    l2.setBlueprintValue("blueprint documentation")
    return l2


class TestLOverviewParagraphWriter:
    def test_write_l2_writes_blueprint_value_attribute(self):
        """blueprintValue must be written as the BLUEPRINT-VALUE XML attribute (XSD 00052 attributeGroup L-OVERVIEW-PARAGRAPH, xml.attribute=true)."""
        element = ET.Element("MULTI-LANGUAGE-OVERVIEW-PARAGRAPH")

        ARXMLWriter().setMultiLanguageOverviewParagraph(element, "MULTI-LANGUAGE-OVERVIEW-PARAGRAPH", MultiLanguageOverviewParagraph().addL2(_build_l_overview_paragraph()))

        written = element.find("MULTI-LANGUAGE-OVERVIEW-PARAGRAPH/L-2")
        assert written is not None
        assert written.attrib["L"] == "EN"
        assert written.attrib["BLUEPRINT-VALUE"] == "blueprint documentation"
        assert written.text == "overview text"

    def test_write_l2_without_blueprint_value_omits_attribute(self):
        element = ET.Element("MULTI-LANGUAGE-OVERVIEW-PARAGRAPH")
        l2 = LOverviewParagraph()
        l2.setL("DE")
        l2.setValue("ohne blueprint")

        ARXMLWriter().setMultiLanguageOverviewParagraph(element, "MULTI-LANGUAGE-OVERVIEW-PARAGRAPH", MultiLanguageOverviewParagraph().addL2(l2))

        written = element.find("MULTI-LANGUAGE-OVERVIEW-PARAGRAPH/L-2")
        assert written is not None
        assert "BLUEPRINT-VALUE" not in written.attrib
        assert written.attrib["L"] == "DE"

    def test_l_overview_paragraph_write_read_roundtrip(self):
        writer_element = ET.Element("ROOT")
        ARXMLWriter().setMultiLanguageOverviewParagraph(writer_element, "MULTI-LANGUAGE-OVERVIEW-PARAGRAPH", MultiLanguageOverviewParagraph().addL2(_build_l_overview_paragraph()))
        writer_element.attrib["xmlns"] = "http://autosar.org/schema/r4.0"
        parsed = ET.fromstring(ET.tostring(writer_element, encoding="unicode"))

        result = ARXMLParser().getMultiLanguageOverviewParagraph(parsed, "MULTI-LANGUAGE-OVERVIEW-PARAGRAPH")

        assert result is not None
        l2 = result.getL2s()[0]
        assert isinstance(l2, LOverviewParagraph)
        assert l2.getL() == "EN"
        assert l2.getValue() == "overview text"
        assert l2.getBlueprintValue() == "blueprint documentation"
