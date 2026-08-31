"""
Tests for writing SenderReceiverInterface META-DATA-ITEM-SETS elements — Table 4.5 (metaDataItemSet aggr).

Round-trip counterpart: tests/test_armodel/parser/test_sender_receiver_interface_meta_data_item_sets.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants import (
    TextValueSpecification,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ARLiteral,
    PositiveInteger,
    RefType,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import (
    MetaDataItem,
    MetaDataItemSet,
    SenderReceiverInterface,
)
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def writer():
    """Create ARXML writer instance."""
    AUTOSAR.getInstance().new()
    return ARXMLWriter()


def _ref(value: str, dest: str = "VARIABLE-DATA-PROTOTYPE") -> RefType:
    ref = RefType()
    ref.setValue(value)
    ref.setDest(dest)
    return ref


def _sr_interface() -> SenderReceiverInterface:
    AUTOSAR.getInstance().new()
    ar_root = AUTOSAR.getInstance().createARPackage("AUTOSAR")
    return SenderReceiverInterface(ar_root, "sr_iface")


class TestWriteSenderReceiverInterfaceMetaDataItemSets:
    """
    Test writeSenderReceiverInterfaceMetaDataItemSets (SenderReceiverInterface.metaDataItemSet, Table 4.5).
    """

    def test_write_field_values(self, writer):
        """
        Test that a MetaDataItemSet is written with DATA-ELEMENT-REFS and the
        ordered META-DATA-ITEMS including LENGTH and META-DATA-ITEM-TYPE values.
        """
        sr_interface = _sr_interface()
        mapping_set = MetaDataItemSet()
        mapping_set.addDataElementRef(_ref("/AUTOSAR/sr_iface/de1"))
        mapping_set.addDataElementRef(_ref("/AUTOSAR/sr_iface/de2"))

        item1 = MetaDataItem()
        item1.setLength(PositiveInteger().setValue(8))
        value_spec = TextValueSpecification()
        value_spec.setValue(ARLiteral().setValue("uint8"))
        item1.setMetaDataItemType(value_spec)

        item2 = MetaDataItem()
        item2.setLength(PositiveInteger().setValue(4))

        mapping_set.addMetaDataItem(item1)
        mapping_set.addMetaDataItem(item2)
        sr_interface.addMetaDataItemSet(mapping_set)

        element = ET.Element("PARENT")
        writer.writeSenderReceiverInterfaceMetaDataItemSets(element, sr_interface)

        wrapper = element.find("META-DATA-ITEM-SETS")
        assert wrapper is not None

        set_tag = wrapper.find("META-DATA-ITEM-SET")
        assert set_tag is not None

        refs_tag = set_tag.find("DATA-ELEMENT-REFS")
        assert refs_tag is not None
        refs = refs_tag.findall("DATA-ELEMENT-REF")
        assert len(refs) == 2
        assert refs[0].text == "/AUTOSAR/sr_iface/de1"
        assert refs[0].attrib["DEST"] == "VARIABLE-DATA-PROTOTYPE"
        assert refs[1].text == "/AUTOSAR/sr_iface/de2"

        items_tag = set_tag.find("META-DATA-ITEMS")
        assert items_tag is not None
        items = items_tag.findall("META-DATA-ITEM")
        assert len(items) == 2
        assert items[0].find("LENGTH").text == "8"
        assert items[0].find("META-DATA-ITEM-TYPE/VALUE").text == "uint8"
        assert items[1].find("LENGTH").text == "4"
        assert items[1].find("META-DATA-ITEM-TYPE") is None

    def test_write_empty(self, writer):
        """
        Test that a SenderReceiverInterface without MetaDataItemSets writes
        no META-DATA-ITEM-SETS wrapper.
        """
        sr_interface = _sr_interface()

        element = ET.Element("PARENT")
        writer.writeSenderReceiverInterfaceMetaDataItemSets(element, sr_interface)

        assert element.find("META-DATA-ITEM-SETS") is None
