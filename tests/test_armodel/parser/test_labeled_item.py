"""Reader tests for LabeledItem (AUTOSAR_FO_TPS_GenericStructureTemplate, Table 9.12).

The reader entry point getLabeledItem must populate helpEntry, the inline itemContents
payload, itemLabel, the inherited Paginateable attributes and the VariationPointCapable
mixin — asserting field values and the concrete type, not just wrapper presence.
"""

import xml.etree.ElementTree as ET

from armodel.models.M2.MSR.Documentation.BlockElements.ListElements import LabeledItem
from armodel.parser.arxml_parser import ARXMLParser

NS = "{http://autosar.org/schema/r4.0}"


def _block(inner):
    return ET.fromstring('<DOCUMENTATION-BLOCK xmlns="http://autosar.org/schema/r4.0">' + inner + "</DOCUMENTATION-BLOCK>")


def _labeled_item_element(attrs="", inner=""):
    block = _block(f"<LABELED-LIST><LABELED-ITEM {attrs}>{inner}</LABELED-ITEM></LABELED-LIST>")
    return block.find(f".//{NS}LABELED-ITEM")


class TestLabeledItemParser:
    def test_read_full_labeled_item_populates_all_members(self):
        """HELP-ENTRY, ITEM-LABEL, the inline itemContents payload, the Paginateable attributes and VARIATION-POINT all land on the model (field values, not wrapper presence)."""
        parser = ARXMLParser()
        element = _labeled_item_element(
            'HELP-ENTRY="li1" SI="SIVAL"',
            '<ITEM-LABEL><L-2 L="EN">lbl1</L-2></ITEM-LABEL>' '<P><L-1 L="EN">c1</L-1></P>' "<VARIATION-POINT><SHORT-LABEL>DVP</SHORT-LABEL></VARIATION-POINT>",
        )

        labeled_item = parser.getLabeledItem(element)

        assert isinstance(labeled_item, LabeledItem)
        assert labeled_item.getHelpEntry().getValue() == "li1"
        assert labeled_item.getSi().getValue() == "SIVAL"
        assert labeled_item.getItemLabel().getL2s()[0].getValue() == "lbl1"
        assert labeled_item.getItemContents().getPs()[0].getL1s()[0].getValue() == "c1"
        assert labeled_item.getVariationPoint().getShortLabel().getValue() == "DVP"

    def test_read_empty_labeled_item_leaves_optional_members_unset(self):
        """An empty <LABELED-ITEM/> reads with helpEntry/itemLabel/variationPoint unset and an empty inline DocumentationBlock (the XSD choice is minOccurs=0, so the reader materializes a block — the NOTE/TRACEABLE-TEXT house behaviour)."""
        parser = ARXMLParser()

        labeled_item = parser.getLabeledItem(_labeled_item_element())

        assert isinstance(labeled_item, LabeledItem)
        assert labeled_item.getHelpEntry() is None
        assert labeled_item.getItemLabel() is None
        assert labeled_item.getVariationPoint() is None
        contents = labeled_item.getItemContents()
        assert contents is not None
        assert contents.getPs() == []

    def test_read_labeled_item_through_labeled_list(self):
        """The consumer path getLabeledList populates each LABELED-ITEM through getLabeledItem (Rule 0001.7)."""
        parser = ARXMLParser()
        element = _block('<LABELED-LIST><LABELED-ITEM HELP-ENTRY="li1"><ITEM-LABEL><L-2 L="EN">lbl1</L-2></ITEM-LABEL>' '<P><L-1 L="EN">c1</L-1></P></LABELED-ITEM></LABELED-LIST>')

        items = parser.getLabeledList(element, "LABELED-LIST").getLabeledItems()

        assert len(items) == 1
        assert items[0].getHelpEntry().getValue() == "li1"
        assert items[0].getItemContents().getPs()[0].getL1s()[0].getValue() == "c1"
