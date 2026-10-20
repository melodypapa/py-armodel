"""Reader tests for the DocumentationBlock list-item helpers (DefItem / LabeledItem / IndentSample).

These helpers are consumed through the DocumentationBlock path. R23-11 (AUTOSAR_00052.xsd)
declares their attributes as HELP-ENTRY (attributeGroups DEF-ITEM / LABELED-ITEM) and
ITEM-LABEL-POS (attributeGroup INDENT-SAMPLE) — not the HELPENTRY / ITEMLABELPOS spellings
this reader used to look for. getDefItem must also be handed the DEF-ITEM element itself,
not the enclosing DEF-LIST.
"""

import xml.etree.ElementTree as ET

from armodel.models.M2.MSR.Documentation.BlockElements.ListElements import ItemLabelPosEnum
from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView import ChapterEnumBreak, KeepWithPreviousEnum
from armodel.parser.arxml_parser import ARXMLParser


def _block(inner):
    return ET.fromstring('<DOCUMENTATION-BLOCK xmlns="http://autosar.org/schema/r4.0">' + inner + "</DOCUMENTATION-BLOCK>")


class TestDocumentationListItemHelpersReader:
    def test_reads_def_item_from_its_own_element(self):
        """getDefItem must read the DEF-ITEM element (SHORT-NAME, DEF payload, HELP-ENTRY, VARIATION-POINT) — not the enclosing DEF-LIST."""
        parser = ARXMLParser()
        element = _block(
            '<DEF-LIST><DEF-ITEM HELP-ENTRY="def-topic"><SHORT-NAME>d1</SHORT-NAME>'
            '<DEF><P><L-1 L="EN">def text</L-1></P></DEF>'
            "<VARIATION-POINT><SHORT-LABEL>DVP</SHORT-LABEL></VARIATION-POINT>"
            "</DEF-ITEM></DEF-LIST>"
        )

        def_item = parser.readDefList(element, "DEF-LIST").getDefItems()[0]

        assert def_item.getShortName() == "d1"
        assert def_item.getHelpEntry().getValue() == "def-topic"
        assert def_item.getDef().getPs()[0].getL1s()[0].getValue() == "def text"
        assert def_item.getVariationPoint().getShortLabel().getValue() == "DVP"

    def test_reads_help_entry_on_labeled_item(self):
        """attributeGroup LABELED-ITEM declares HELP-ENTRY (AUTOSAR_00052.xsd)."""
        parser = ARXMLParser()
        element = _block('<LABELED-LIST><LABELED-ITEM HELP-ENTRY="li-topic">' '<ITEM-LABEL><L-2 L="EN">lbl</L-2></ITEM-LABEL>' '<P><L-1 L="EN">c</L-1></P>' "</LABELED-ITEM></LABELED-LIST>")

        labeled_item = parser.getLabeledList(element, "LABELED-LIST").getLabeledItems()[0]

        assert labeled_item.getHelpEntry().getValue() == "li-topic"
        assert labeled_item.getItemLabel().getL2s()[0].getValue() == "lbl"
        assert labeled_item.getItemContents().getPs()[0].getL1s()[0].getValue() == "c"

    def test_reads_item_label_pos_on_indent_sample(self):
        """attributeGroup INDENT-SAMPLE declares ITEM-LABEL-POS (AUTOSAR_00052.xsd)."""
        parser = ARXMLParser()
        element = _block('<LABELED-LIST><INDENT-SAMPLE ITEM-LABEL-POS="NEWLINE"><L-2 L="EN">sample</L-2></INDENT-SAMPLE></LABELED-LIST>')

        indent_sample = parser.getLabeledList(element, "LABELED-LIST").getIndentSample()

        assert indent_sample.getItemLabelPos().getValue() == ItemLabelPosEnum.NEWLINE
        assert indent_sample.getL2s()[0].getValue() == "sample"

    def test_reads_def_item_inherited_multilanguage_and_paginateable_state(self):
        """The Base row includes MultilanguageReferrable, DocumentViewSelectable and Paginateable: LONG-NAME and SI/VIEW/BREAK/KEEP-WITH-PREVIOUS are read from DEF-ITEM."""
        parser = ARXMLParser()
        element = _block(
            '<DEF-LIST><DEF-ITEM SI="SIVAL" VIEW="VIEWVAL" BREAK="BREAK" KEEP-WITH-PREVIOUS="KEEP">'
            "<SHORT-NAME>d3</SHORT-NAME>"
            '<LONG-NAME><L-4 L="EN">Definition</L-4></LONG-NAME>'
            '<DEF><P><L-1 L="EN">x</L-1></P></DEF>'
            "</DEF-ITEM></DEF-LIST>"
        )

        def_item = parser.readDefList(element, "DEF-LIST").getDefItems()[0]

        assert def_item.getLongName().getL4s()[0].getValue() == "Definition"
        assert def_item.getSi().getValue() == "SIVAL"
        assert def_item.getView().getValue() == "VIEWVAL"
        assert def_item.getBreak().getValue() == ChapterEnumBreak.BREAK
        assert def_item.getKeepWithPrevious().getValue() == KeepWithPreviousEnum.KEEP

    def test_reads_def_item_without_help_entry(self):
        """HELP-ENTRY is 0..1: a DEF-ITEM without it reads with helpEntry None while still reading its own DEF payload."""
        parser = ARXMLParser()
        element = _block('<DEF-LIST><DEF-ITEM><SHORT-NAME>d2</SHORT-NAME><DEF><P><L-1 L="EN">x</L-1></P></DEF></DEF-ITEM></DEF-LIST>')

        def_item = parser.readDefList(element, "DEF-LIST").getDefItems()[0]

        assert def_item.getHelpEntry() is None
        assert def_item.getShortName() == "d2"
        assert def_item.getDef().getPs()[0].getL1s()[0].getValue() == "x"
