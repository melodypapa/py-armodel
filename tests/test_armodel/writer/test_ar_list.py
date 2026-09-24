"""Writer tests for the ARList class (AUTOSAR_FO_TPS_GenericStructureTemplate, Table 9.8 — spec class name List).

The LIST element is written by the ARList-owned helpers (writer setListElement /
parser getListElements). Per the XSD (AUTOSAR_00052.xsd group LIST L78451 /
attributeGroup LIST L78476) the LIST element carries ITEM children (inline
DocumentationBlock content — Item.itemContents has xml.roleElement=false) and
the TYPE attribute in the LIST-ENUM--SIMPLE wire form (NUMBER/UNNUMBER).
"""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.MSR.Documentation.BlockElements.ListElements import ARList, Item, ListEnum
from armodel.models.M2.MSR.Documentation.TextModel.BlockElements import DocumentationBlock
from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel import LParagraph
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import MultiLanguageParagraph
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


def _parent():
    return ET.Element("PARENT")


def _writer():
    AUTOSAR.getInstance().new()
    return ARXMLWriter()


def _make_paragraph(value):
    paragraph = MultiLanguageParagraph()
    l1 = LParagraph()
    l1.setL("EN")
    l1.setValue(value)
    paragraph.addL1(l1)
    return paragraph


def _make_item(value):
    item = Item()
    contents = DocumentationBlock()
    contents.addP(_make_paragraph(value))
    item.setItemContents(contents)
    return item


class TestARListWriter:
    def test_write_list_writes_type_wire_form(self):
        """The model value (Table 9.10 literal, lowercase) is written in the XSD LIST-ENUM--SIMPLE wire form (uppercase)."""
        writer = _writer()
        parent = _parent()
        ar_list = ARList()
        ar_list.setType(ListEnum().setValue(ListEnum.UNNUMBER))

        writer.setListElement(parent, "LIST", ar_list)

        assert ar_list.getType() is not None
        element = parent[0]
        assert element.tag == "LIST"
        assert element.attrib["TYPE"] == "UNNUMBER"

    def test_write_list_raw_string_type_back_compat(self):
        """A raw string set via setType (old-style caller) is passed through verbatim (back-compat branch)."""
        writer = _writer()
        parent = _parent()
        ar_list = ARList()
        ar_list.setType("number")

        writer.setListElement(parent, "LIST", ar_list)

        assert parent[0].attrib["TYPE"] == "number"

    def test_write_list_writes_item_wrapper_with_inline_content(self):
        """Each Item is written as one <ITEM> element carrying its DocumentationBlock content INLINE (Item.itemContents xml.roleElement=false)."""
        writer = _writer()
        parent = _parent()
        ar_list = ARList()
        ar_list.addItem(_make_item("first item"))
        ar_list.addItem(_make_item("second item"))

        writer.setListElement(parent, "LIST", ar_list)

        element = parent[0]
        assert element.tag == "LIST"
        item_elements = element.findall("ITEM")
        assert len(item_elements) == 2
        assert item_elements[0].find("P/L-1").text == "first item"
        assert item_elements[1].find("P/L-1").text == "second item"

    def test_write_list_documentation_block_back_compat(self):
        """A raw DocumentationBlock added via addItem (old-style flattened caller) is still written as <ITEM> content (back-compat branch)."""
        writer = _writer()
        parent = _parent()
        ar_list = ARList()
        block = DocumentationBlock()
        block.addP(_make_paragraph("legacy block"))
        ar_list.addItem(block)

        writer.setListElement(parent, "LIST", ar_list)

        element = parent[0]
        assert element.tag == "LIST"
        assert element.find("ITEM/P/L-1").text == "legacy block"

    def test_write_empty_list(self):
        """An ARList with no items writes the LIST element with no ITEM children (empty-wrapper case)."""
        writer = _writer()
        parent = _parent()
        ar_list = ARList()

        writer.setListElement(parent, "LIST", ar_list)

        element = parent[0]
        assert element.tag == "LIST"
        assert element.findall("ITEM") == []

    def test_write_read_round_trip(self):
        """Full write → parse round-trip: items come back as Item objects with field values and the type in the model form (field values, not len())."""
        ar_list = ARList()
        ar_list.setType(ListEnum().setValue(ListEnum.UNNUMBER))
        ar_list.addItem(_make_item("list item text"))

        writer_element = _parent()
        _writer().setListElement(writer_element, "LIST", ar_list)
        writer_element.attrib["xmlns"] = "http://autosar.org/schema/r4.0"
        parsed = ET.fromstring(ET.tostring(writer_element, encoding="unicode"))

        lists = ARXMLParser().getListElements(parsed, "LIST")
        assert len(lists) == 1
        round_tripped = lists[0]
        assert round_tripped.getType().getValue() == "unnumber"
        items = round_tripped.getItems()
        assert len(items) == 1
        assert isinstance(items[0], Item)
        assert items[0].getItemContents().getPs()[0].getL1s()[0].getValue() == "list item text"
