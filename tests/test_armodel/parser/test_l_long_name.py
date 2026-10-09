"""Reader tests for the LLongName class (AUTOSAR_FO_TPS_GenericStructureTemplate, Table 4.8)."""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import String
from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel import LLongName
from armodel.parser.arxml_parser import ARXMLParser


class TestLLongNameParser:
    def test_read_l4_reads_blueprint_value(self):
        """The BLUEPRINT-VALUE XML attribute (XSD 00052 attributeGroup L-LONG-NAME) must populate blueprintValue (Table 4.8)."""
        parser = ARXMLParser()
        element = ET.fromstring(
            '<ROOT xmlns="http://autosar.org/schema/r4.0">'
            "<MULTI-LANGUAGE-LONG-NAME>"
            '<L-4 L="EN" BLUEPRINT-VALUE="blueprint documentation">long name text</L-4>'
            "</MULTI-LANGUAGE-LONG-NAME>"
            "</ROOT>"
        )

        long_name = parser.getMultilanguageLongName(element, "MULTI-LANGUAGE-LONG-NAME")

        assert long_name is not None
        l4 = long_name.getL4s()[0]
        assert isinstance(l4, LLongName)
        assert isinstance(l4.getBlueprintValue(), String)
        assert l4.getBlueprintValue().getValue() == "blueprint documentation"
        assert l4.getValue() == "long name text"
        assert l4.getL() == "EN"

    def test_read_l4_without_blueprint_value(self):
        parser = ARXMLParser()
        element = ET.fromstring('<ROOT xmlns="http://autosar.org/schema/r4.0">' "<MULTI-LANGUAGE-LONG-NAME>" '<L-4 L="DE">ohne blueprint</L-4>' "</MULTI-LANGUAGE-LONG-NAME>" "</ROOT>")

        long_name = parser.getMultilanguageLongName(element, "MULTI-LANGUAGE-LONG-NAME")

        assert long_name.getL4s()[0].getBlueprintValue() is None
        assert long_name.getL4s()[0].getValue() == "ohne blueprint"
