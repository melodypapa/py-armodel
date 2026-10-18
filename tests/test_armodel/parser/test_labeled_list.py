"""Reader tests for LabeledList (AUTOSAR_FO_TPS_GenericStructureTemplate, Table 9.11).

The reader entry point getLabeledList must populate indentSample, the LABELED-ITEM list,
the inherited Paginateable attributes and the VariationPointCapable mixin — asserting
field values and the concrete type, not just wrapper presence.
"""

import xml.etree.ElementTree as ET

from armodel.models.M2.MSR.Documentation.BlockElements.ListElements import ItemLabelPosEnum, LabeledList
from armodel.parser.arxml_parser import ARXMLParser


def _block(inner):
    return ET.fromstring('<DOCUMENTATION-BLOCK xmlns="http://autosar.org/schema/r4.0">' + inner + "</DOCUMENTATION-BLOCK>")


class TestLabeledListParser:
    def test_read_full_labeled_list_populates_all_members(self):
        """INDENT-SAMPLE, the LABELED-ITEM list, the Paginateable attributes and VARIATION-POINT all land on the model (field values, not wrapper presence)."""
        parser = ARXMLParser()
        element = _block(
            '<LABELED-LIST SI="SIVAL" VIEW="VIEWVAL" BREAK="BREAK" KEEP-WITH-PREVIOUS="KEEP">'
            '<INDENT-SAMPLE ITEM-LABEL-POS="NEWLINE"><L-2 L="EN">sample</L-2></INDENT-SAMPLE>'
            '<LABELED-ITEM HELP-ENTRY="li1"><ITEM-LABEL><L-2 L="EN">lbl1</L-2></ITEM-LABEL>'
            '<P><L-1 L="EN">c1</L-1></P></LABELED-ITEM>'
            '<LABELED-ITEM HELP-ENTRY="li2"><ITEM-LABEL><L-2 L="EN">lbl2</L-2></ITEM-LABEL>'
            '<P><L-1 L="EN">c2</L-1></P></LABELED-ITEM>'
            "<VARIATION-POINT><SHORT-LABEL>DVP</SHORT-LABEL></VARIATION-POINT>"
            "</LABELED-LIST>"
        )

        labeled_list = parser.getLabeledList(element, "LABELED-LIST")

        assert isinstance(labeled_list, LabeledList)
        assert labeled_list.getSi().getValue() == "SIVAL"
        assert labeled_list.getView().getValue() == "VIEWVAL"
        assert labeled_list.getBreak().getValue() == "BREAK"
        assert labeled_list.getKeepWithPrevious().getValue() == "KEEP"
        indent_sample = labeled_list.getIndentSample()
        assert indent_sample is not None
        assert indent_sample.getItemLabelPos().getValue() == ItemLabelPosEnum.NEWLINE
        assert indent_sample.getL2s()[0].getValue() == "sample"
        items = labeled_list.getLabeledItems()
        assert [item.getHelpEntry().getValue() for item in items] == ["li1", "li2"]
        assert items[0].getItemLabel().getL2s()[0].getValue() == "lbl1"
        assert items[0].getItemContents().getPs()[0].getL1s()[0].getValue() == "c1"
        assert items[1].getItemContents().getPs()[0].getL1s()[0].getValue() == "c2"
        assert labeled_list.getVariationPoint().getShortLabel().getValue() == "DVP"

    def test_read_empty_wrapper(self):
        """An empty <LABELED-LIST/> yields an instance with all members unset."""
        parser = ARXMLParser()
        element = _block("<LABELED-LIST/>")

        labeled_list = parser.getLabeledList(element, "LABELED-LIST")

        assert isinstance(labeled_list, LabeledList)
        assert labeled_list.getIndentSample() is None
        assert labeled_list.getLabeledItems() == []
        assert labeled_list.getVariationPoint() is None

    def test_read_absent_wrapper_returns_none(self):
        """No LABELED-LIST child ⇒ None (the optional-aggregate contract)."""
        parser = ARXMLParser()
        element = _block('<P><L-1 L="EN">text</L-1></P>')

        assert parser.getLabeledList(element, "LABELED-LIST") is None
