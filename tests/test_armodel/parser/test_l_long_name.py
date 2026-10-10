"""Reader tests for the LLongName class (AUTOSAR_FO_TPS_GenericStructureTemplate, Table 4.8)."""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import String
from armodel.models.M2.MSR.Documentation.TextModel.InlineTextElements import EmphasisText, IndexEntry, Superscript, Tt
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

    def test_read_mixed_content_group_populates_e_ie_tt_sup_sub(self):
        """readMixedContentForLongName must populate all five Table 4.9 attributes."""
        parser = ARXMLParser()
        element = ET.fromstring(
            '<ROOT xmlns="http://autosar.org/schema/r4.0">'
            "<MULTI-LANGUAGE-LONG-NAME>"
            '<L-4 L="EN" SUP="up" SUB="down">long name text'
            '<TT TYPE="TT">term</TT>'
            "<E>emphasis</E>"
            "<IE>entry</IE>"
            "</L-4>"
            "</MULTI-LANGUAGE-LONG-NAME>"
            "</ROOT>"
        )

        long_name = parser.getMultilanguageLongName(element, "MULTI-LANGUAGE-LONG-NAME")

        assert long_name is not None
        l4 = long_name.getL4s()[0]
        assert isinstance(l4.getTt(), Tt)
        assert l4.getTt().getValue().getValue() == "term"
        assert l4.getTt().getType().getValue() == "TT"
        assert isinstance(l4.getE(), EmphasisText)
        assert l4.getE().getValue().getValue() == "emphasis"
        assert isinstance(l4.getIe(), IndexEntry)
        assert l4.getIe().getValue().getValue() == "entry"
        assert isinstance(l4.getSup(), Superscript)
        assert l4.getSup().getValue() == "up"
        assert isinstance(l4.getSub(), Superscript)
        assert l4.getSub().getValue() == "down"

    def test_read_mixed_content_group_leaves_unset_attributes_none(self):
        parser = ARXMLParser()
        element = ET.fromstring('<ROOT xmlns="http://autosar.org/schema/r4.0">' "<MULTI-LANGUAGE-LONG-NAME>" '<L-4 L="DE">plain</L-4>' "</MULTI-LANGUAGE-LONG-NAME>" "</ROOT>")

        l4 = parser.getMultilanguageLongName(element, "MULTI-LANGUAGE-LONG-NAME").getL4s()[0]

        assert l4.getTt() is None
        assert l4.getE() is None
        assert l4.getIe() is None
        assert l4.getSup() is None
        assert l4.getSub() is None
