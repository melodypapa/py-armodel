"""Reader tests for the ARList class (AUTOSAR_FO_TPS_GenericStructureTemplate, Table 9.8 — spec class name List).

The LIST element is consumed by the ARList-owned helpers (parser getListElements /
writer setListElement). Per the XSD (AUTOSAR_00052.xsd group LIST L78451) a LIST
carries ITEM children (aggr item, 1..*) and the TYPE attribute (attr type,
LIST-ENUM--SIMPLE wire values NUMBER/UNNUMBER).
"""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import VariationPoint
from armodel.models.M2.MSR.Documentation.BlockElements.ListElements import ARList, Item, ListEnum
from armodel.parser.arxml_parser import ARXMLParser


class TestARListParser:
    def test_read_list_reads_items_as_item_objects(self):
        """The item aggr (Table 9.8: Item 1..*) must parse as Item objects whose itemContents carries the payload (xml.roleElement=true on item / roleElement=false on Item.itemContents → the DocumentationBlock content renders inline inside <ITEM>)."""
        parser = ARXMLParser()
        element = ET.fromstring(
            '<DOCUMENTATION-BLOCK xmlns="http://autosar.org/schema/r4.0">'
            '<LIST TYPE="UNNUMBER">'
            '<ITEM><P><L-1 L="EN">first item</L-1></P></ITEM>'
            '<ITEM><P><L-1 L="EN">second item</L-1></P></ITEM>'
            "</LIST>"
            "</DOCUMENTATION-BLOCK>"
        )

        lists = parser.getListElements(element, "LIST")

        assert len(lists) == 1
        items = lists[0].getItems()
        assert len(items) == 2
        assert all(isinstance(item, Item) for item in items)
        assert items[0].getItemContents() is not None
        assert items[0].getItemContents().getPs()[0].getL1s()[0].getValue() == "first item"
        assert items[1].getItemContents().getPs()[0].getL1s()[0].getValue() == "second item"

    def test_read_list_type_wire_to_model(self):
        """The TYPE attribute carries the XSD LIST-ENUM--SIMPLE wire token; the ListEnum literal is already that same uppercase token (Table 9.10 renders it lowercase in prose only), so the reader maps it through unchanged."""
        parser = ARXMLParser()
        element = ET.fromstring('<DOCUMENTATION-BLOCK xmlns="http://autosar.org/schema/r4.0">' '<LIST TYPE="UNNUMBER"><ITEM><P><L-1 L="EN">x</L-1></P></ITEM></LIST>' "</DOCUMENTATION-BLOCK>")

        ar_list = parser.getListElements(element, "LIST")[0]

        assert isinstance(ar_list.getType(), ListEnum)
        assert ar_list.getType().getValue() == ListEnum.UNNUMBER

    def test_read_list_without_type(self):
        """type is 0..1: a LIST without the TYPE attribute reads as None."""
        parser = ARXMLParser()
        element = ET.fromstring('<DOCUMENTATION-BLOCK xmlns="http://autosar.org/schema/r4.0">' '<LIST><ITEM><P><L-1 L="EN">x</L-1></P></ITEM></LIST>' "</DOCUMENTATION-BLOCK>")

        ar_list = parser.getListElements(element, "LIST")[0]

        assert ar_list.getType() is None

    def test_read_list_paginateable_attributes(self):
        """Base accessors (Table 9.8 Base row → Paginateable) remain read on the LIST element."""
        parser = ARXMLParser()
        element = ET.fromstring(
            '<DOCUMENTATION-BLOCK xmlns="http://autosar.org/schema/r4.0">' '<LIST BREAK="BREAK" KEEP-WITH-PREVIOUS="KEEP">' '<ITEM><P><L-1 L="EN">x</L-1></P></ITEM>' "</LIST>" "</DOCUMENTATION-BLOCK>"
        )

        ar_list = parser.getListElements(element, "LIST")[0]

        assert ar_list.getBreak().getValue() == "BREAK"
        assert ar_list.getKeepWithPrevious().getValue() == "KEEP"

    def test_read_nested_list_inside_item(self):
        """The item Note: "lists can be arbitrarily nested" — a nested LIST inside the item payload round-trips through itemContents."""
        parser = ARXMLParser()
        element = ET.fromstring(
            '<DOCUMENTATION-BLOCK xmlns="http://autosar.org/schema/r4.0">'
            '<LIST TYPE="NUMBER">'
            "<ITEM>"
            '<P><L-1 L="EN">outer</L-1></P>'
            '<LIST TYPE="UNNUMBER">'
            '<ITEM><P><L-1 L="EN">inner</L-1></P></ITEM>'
            "</LIST>"
            "</ITEM>"
            "</LIST>"
            "</DOCUMENTATION-BLOCK>"
        )

        ar_list = parser.getListElements(element, "LIST")[0]

        item = ar_list.getItems()[0]
        assert isinstance(item, Item)
        nested = item.getItemContents().getLists()[0]
        assert isinstance(nested, ARList)
        assert nested.getType().getValue() == ListEnum.UNNUMBER
        assert nested.getItems()[0].getItemContents().getPs()[0].getL1s()[0].getValue() == "inner"

    def test_read_empty_list(self):
        """item mult is 1..* in the model but the XSD group allows minOccurs=0: a LIST with no ITEM children reads with no items (empty-wrapper case)."""
        parser = ARXMLParser()
        element = ET.fromstring('<DOCUMENTATION-BLOCK xmlns="http://autosar.org/schema/r4.0"><LIST TYPE="UNNUMBER"/></DOCUMENTATION-BLOCK>')

        ar_list = parser.getListElements(element, "LIST")[0]

        assert ar_list.getItems() == []

    def test_read_list_variation_point(self):
        """Rule 0020: the R23-11 XSD LIST group (AUTOSAR_00052.xsd L78465) carries VARIATION-POINT with mmt.qualifiedName="List.variationPoint" / xml.sequenceOffset=10000, so the reader (getListElements) must dispatch it onto the ARList."""
        parser = ARXMLParser()
        element = ET.fromstring(
            '<DOCUMENTATION-BLOCK xmlns="http://autosar.org/schema/r4.0">'
            '<LIST TYPE="UNNUMBER">'
            '<ITEM><P><L-1 L="EN">x</L-1></P></ITEM>'
            "<VARIATION-POINT><SHORT-LABEL>VP1</SHORT-LABEL></VARIATION-POINT>"
            "</LIST>"
            "</DOCUMENTATION-BLOCK>"
        )

        ar_list = parser.getListElements(element, "LIST")[0]

        assert ar_list.getVariationPoint() is not None
        assert ar_list.getVariationPoint().getShortLabel().getValue() == "VP1"
        assert ar_list.getItems()[0].getItemContents().getPs()[0].getL1s()[0].getValue() == "x"

    def test_read_list_without_variation_point(self):
        """VARIATION-POINT is 0..1: a LIST without it reads with variationPoint None."""
        parser = ARXMLParser()
        element = ET.fromstring('<DOCUMENTATION-BLOCK xmlns="http://autosar.org/schema/r4.0"><LIST TYPE="UNNUMBER"><ITEM><P><L-1 L="EN">x</L-1></P></ITEM></LIST></DOCUMENTATION-BLOCK>')

        assert parser.getListElements(element, "LIST")[0].getVariationPoint() is None

    def test_read_list_variation_point_is_variation_point_object(self):
        """The dispatched value is a VariationPoint (not a bare element) so its members round-trip."""
        parser = ARXMLParser()
        element = ET.fromstring(
            '<DOCUMENTATION-BLOCK xmlns="http://autosar.org/schema/r4.0">' "<LIST>" "<VARIATION-POINT><SHORT-LABEL>VP2</SHORT-LABEL></VARIATION-POINT>" "</LIST>" "</DOCUMENTATION-BLOCK>"
        )

        ar_list = parser.getListElements(element, "LIST")[0]

        assert isinstance(ar_list.getVariationPoint(), VariationPoint)

    def test_read_item_variation_point(self):
        """Rule 0020: the R23-11 XSD ITEM group (AUTOSAR_00052.xsd, mmt.qualifiedName="Item.variationPoint" / xml.sequenceOffset=10000) carries VARIATION-POINT, so the ITEM reader must dispatch it onto the Item (the consume path is ARList-owned)."""
        parser = ARXMLParser()
        element = ET.fromstring(
            '<DOCUMENTATION-BLOCK xmlns="http://autosar.org/schema/r4.0">'
            '<LIST TYPE="UNNUMBER">'
            '<ITEM><P><L-1 L="EN">x</L-1></P>'
            "<VARIATION-POINT><SHORT-LABEL>IVP</SHORT-LABEL></VARIATION-POINT></ITEM>"
            "</LIST>"
            "</DOCUMENTATION-BLOCK>"
        )

        item = parser.getListElements(element, "LIST")[0].getItems()[0]

        assert item.getVariationPoint() is not None
        assert item.getVariationPoint().getShortLabel().getValue() == "IVP"
        assert item.getItemContents().getPs()[0].getL1s()[0].getValue() == "x"

    def test_read_item_without_variation_point(self):
        """Item.variationPoint is 0..1: an ITEM without it reads with variationPoint None."""
        parser = ARXMLParser()
        element = ET.fromstring('<DOCUMENTATION-BLOCK xmlns="http://autosar.org/schema/r4.0"><LIST TYPE="UNNUMBER"><ITEM><P><L-1 L="EN">x</L-1></P></ITEM></LIST></DOCUMENTATION-BLOCK>')

        assert parser.getListElements(element, "LIST")[0].getItems()[0].getVariationPoint() is None
