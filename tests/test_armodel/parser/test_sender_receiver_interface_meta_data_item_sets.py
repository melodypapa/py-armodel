"""
Tests for parsing SenderReceiverInterface META-DATA-ITEM-SETS elements — Table 4.5 (metaDataItemSet aggr).

Round-trip counterpart: tests/test_armodel/writer/test_sender_receiver_interface_meta_data_item_sets.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import (
    MetaDataItemSet,
    SenderReceiverInterface,
)
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def parser():
    """Create ARXML parser instance."""
    AUTOSAR.getInstance().new()
    return ARXMLParser()


def _sr_interface() -> SenderReceiverInterface:
    AUTOSAR.getInstance().new()
    ar_root = AUTOSAR.getInstance().createARPackage("AUTOSAR")
    return SenderReceiverInterface(ar_root, "sr_iface")


class TestReadSenderReceiverInterfaceMetaDataItemSets:
    """
    Test readSenderReceiverInterfaceMetaDataItemSets (SenderReceiverInterface.metaDataItemSet, Table 4.5).
    """

    def test_read_field_values(self, parser):
        """
        Test that a META-DATA-ITEM-SET populates dataElementRefs and the ordered
        metaDataItems with LENGTH and META-DATA-ITEM-TYPE values.
        """
        sr_interface = _sr_interface()
        element = ET.fromstring(
            f"""<SENDER-RECEIVER-INTERFACE xmlns='{NS}'>
                <META-DATA-ITEM-SETS>
                    <META-DATA-ITEM-SET>
                        <DATA-ELEMENT-REFS>
                            <DATA-ELEMENT-REF DEST='VARIABLE-DATA-PROTOTYPE'>/AUTOSAR/sr_iface/de1</DATA-ELEMENT-REF>
                            <DATA-ELEMENT-REF DEST='VARIABLE-DATA-PROTOTYPE'>/AUTOSAR/sr_iface/de2</DATA-ELEMENT-REF>
                        </DATA-ELEMENT-REFS>
                        <META-DATA-ITEMS>
                            <META-DATA-ITEM>
                                <LENGTH>8</LENGTH>
                                <META-DATA-ITEM-TYPE>
                                    <VALUE>uint8</VALUE>
                                </META-DATA-ITEM-TYPE>
                            </META-DATA-ITEM>
                            <META-DATA-ITEM>
                                <LENGTH>4</LENGTH>
                            </META-DATA-ITEM>
                        </META-DATA-ITEMS>
                    </META-DATA-ITEM-SET>
                </META-DATA-ITEM-SETS>
            </SENDER-RECEIVER-INTERFACE>"""
        )

        parser.readSenderReceiverInterfaceMetaDataItemSets(element, sr_interface)

        sets = sr_interface.getMetaDataItemSets()
        assert len(sets) == 1
        mapping_set = sets[0]
        assert isinstance(mapping_set, MetaDataItemSet)

        refs = mapping_set.getDataElementRefs()
        assert len(refs) == 2
        assert refs[0].getValue() == "/AUTOSAR/sr_iface/de1"
        assert refs[0].getDest() == "VARIABLE-DATA-PROTOTYPE"
        assert refs[1].getValue() == "/AUTOSAR/sr_iface/de2"

        items = mapping_set.getMetaDataItems()
        assert len(items) == 2
        assert items[0].getLength().getValue() == 8
        assert items[0].getMetaDataItemType().getValue().getValue() == "uint8"
        assert items[1].getLength().getValue() == 4
        assert items[1].getMetaDataItemType() is None

    def test_read_multiple_sets(self, parser):
        """
        Test that multiple META-DATA-ITEM-SET elements are all appended in order.
        """
        sr_interface = _sr_interface()
        element = ET.fromstring(
            f"""<SENDER-RECEIVER-INTERFACE xmlns='{NS}'>
                <META-DATA-ITEM-SETS>
                    <META-DATA-ITEM-SET>
                        <DATA-ELEMENT-REFS>
                            <DATA-ELEMENT-REF DEST='VARIABLE-DATA-PROTOTYPE'>/AUTOSAR/sr_iface/de1</DATA-ELEMENT-REF>
                        </DATA-ELEMENT-REFS>
                    </META-DATA-ITEM-SET>
                    <META-DATA-ITEM-SET/>
                </META-DATA-ITEM-SETS>
            </SENDER-RECEIVER-INTERFACE>"""
        )

        parser.readSenderReceiverInterfaceMetaDataItemSets(element, sr_interface)

        sets = sr_interface.getMetaDataItemSets()
        assert len(sets) == 2
        assert sets[0].getDataElementRefs()[0].getValue() == "/AUTOSAR/sr_iface/de1"
        assert sets[1].getDataElementRefs() == []
        assert sets[1].getMetaDataItems() == []

    def test_read_empty_wrapper_list(self, parser):
        """
        Test that a SENDER-RECEIVER-INTERFACE without META-DATA-ITEM-SETS
        leaves the list empty.
        """
        sr_interface = _sr_interface()
        element = ET.fromstring(f"<SENDER-RECEIVER-INTERFACE xmlns='{NS}'></SENDER-RECEIVER-INTERFACE>")

        parser.readSenderReceiverInterfaceMetaDataItemSets(element, sr_interface)

        assert sr_interface.getMetaDataItemSets() == []
