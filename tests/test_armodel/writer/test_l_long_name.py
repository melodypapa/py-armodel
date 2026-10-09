"""Writer tests for the LLongName class (AUTOSAR_FO_TPS_GenericStructureTemplate, Table 4.8)."""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import String
from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel import LLongName
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import MultilanguageLongName
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


def _build_l_long_name() -> LLongName:
    l4 = LLongName()
    l4.setL("EN")
    l4.setValue("long name text")
    l4.setBlueprintValue(String().setValue("blueprint documentation"))
    return l4


class TestLLongNameWriter:
    def test_write_l4_writes_blueprint_value_attribute(self):
        """blueprintValue must be written as the BLUEPRINT-VALUE XML attribute (XSD 00052 attributeGroup L-LONG-NAME, xml.attribute=true)."""
        element = ET.Element("MULTI-LANGUAGE-LONG-NAME")

        ARXMLWriter().setMultiLongName(element, "MULTI-LANGUAGE-LONG-NAME", MultilanguageLongName().addL4(_build_l_long_name()))

        written = element.find("MULTI-LANGUAGE-LONG-NAME/L-4")
        assert written is not None
        assert written.attrib["L"] == "EN"
        assert written.attrib["BLUEPRINT-VALUE"] == "blueprint documentation"
        assert written.text == "long name text"

    def test_write_l4_without_blueprint_value_omits_attribute(self):
        element = ET.Element("MULTI-LANGUAGE-LONG-NAME")
        l4 = LLongName()
        l4.setL("DE")
        l4.setValue("ohne blueprint")

        ARXMLWriter().setMultiLongName(element, "MULTI-LANGUAGE-LONG-NAME", MultilanguageLongName().addL4(l4))

        written = element.find("MULTI-LANGUAGE-LONG-NAME/L-4")
        assert written is not None
        assert "BLUEPRINT-VALUE" not in written.attrib
        assert written.attrib["L"] == "DE"

    def test_l_long_name_write_read_roundtrip(self):
        writer_element = ET.Element("ROOT")
        ARXMLWriter().setMultiLongName(writer_element, "MULTI-LANGUAGE-LONG-NAME", MultilanguageLongName().addL4(_build_l_long_name()))
        writer_element.attrib["xmlns"] = "http://autosar.org/schema/r4.0"
        parsed = ET.fromstring(ET.tostring(writer_element, encoding="unicode"))

        result = ARXMLParser().getMultilanguageLongName(parsed, "MULTI-LANGUAGE-LONG-NAME")

        assert result is not None
        l4 = result.getL4s()[0]
        assert isinstance(l4, LLongName)
        assert l4.getL() == "EN"
        assert l4.getValue() == "long name text"
        assert isinstance(l4.getBlueprintValue(), String)
        assert l4.getBlueprintValue().getValue() == "blueprint documentation"
