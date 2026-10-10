"""Writer tests for the LLongName class (AUTOSAR_FO_TPS_GenericStructureTemplate, Table 4.8)."""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import NameToken, String
from armodel.models.M2.MSR.Documentation.TextModel.InlineTextElements import EmphasisText, IndexEntry, Superscript, Tt
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


def _build_mixed_content_l_long_name() -> LLongName:
    """An LLongName exercising the whole MIXED-CONTENT-FOR-LONG-NAME group (Table 4.9)."""
    l4 = LLongName()
    l4.setL("EN")
    l4.setValue("long name text")

    term = Tt()
    term.setValue(String().setValue("term"))
    term.setType(NameToken().setValue("TT"))
    l4.setTt(term)

    emphasis = EmphasisText()
    emphasis.setValue(String().setValue("emphasis"))
    l4.setE(emphasis)

    l4.setSup(Superscript().setValue("up"))
    l4.setSub(Superscript().setValue("down"))

    index_entry = IndexEntry()
    index_entry.setValue(String().setValue("entry"))
    l4.setIe(index_entry)
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


class TestMixedContentForLongNameWriter:
    """writeMixedContentForLongName coverage for the Table 4.9 attribute group."""

    def _write(self, l4: LLongName) -> ET.Element:
        element = ET.Element("ROOT")
        ARXMLWriter().setMultiLongName(element, "MULTI-LANGUAGE-LONG-NAME", MultilanguageLongName().addL4(l4))
        written = element.find("MULTI-LANGUAGE-LONG-NAME/L-4")
        assert written is not None
        return written

    def test_write_emits_group_elements_and_attributes(self):
        written = self._write(_build_mixed_content_l_long_name())

        assert written.find("TT") is not None
        assert written.find("E") is not None
        assert written.find("IE") is not None
        assert written.attrib["SUP"] == "up"
        assert written.attrib["SUB"] == "down"

    def test_write_omits_group_when_unset(self):
        l4 = LLongName()
        l4.setL("EN")
        l4.setValue("plain")

        written = self._write(l4)

        assert written.find("TT") is None
        assert written.find("E") is None
        assert written.find("IE") is None
        assert "SUP" not in written.attrib
        assert "SUB" not in written.attrib

    def test_mixed_content_write_read_roundtrip(self):
        writer_element = ET.Element("ROOT")
        ARXMLWriter().setMultiLongName(writer_element, "MULTI-LANGUAGE-LONG-NAME", MultilanguageLongName().addL4(_build_mixed_content_l_long_name()))
        writer_element.attrib["xmlns"] = "http://autosar.org/schema/r4.0"
        parsed = ET.fromstring(ET.tostring(writer_element, encoding="unicode"))

        result = ARXMLParser().getMultilanguageLongName(parsed, "MULTI-LANGUAGE-LONG-NAME")

        assert result is not None
        l4 = result.getL4s()[0]
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
