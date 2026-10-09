"""Writer round-trip tests for ISignalToIPduMapping (Table 6.14, p.326).

Serialized through the I-SIGNAL-TO-I-PDU-MAPPING element; child order per the
I-SIGNAL-TO-I-PDU-MAPPING group of AUTOSAR_00052.xsd (l.67391).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
    RefType,
    UnlimitedInteger,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import VariationPoint
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (
    ByteOrderEnum,
    ISignalToIPduMapping,
    TransferPropertyEnum,
)
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"

XSD_CHILD_ORDER = [
    "I-SIGNAL-GROUP-REF",
    "I-SIGNAL-REF",
    "PACKING-BYTE-ORDER",
    "START-POSITION",
    "TRANSFER-PROPERTY",
    "UPDATE-INDICATION-BIT-POSITION",
    "VARIATION-POINT",
]


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _with_ns(parent: ET.Element) -> ET.Element:
    return ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))


def _ref(value: str, dest: str) -> RefType:
    ref = RefType()
    ref.setValue(value)
    ref.setDest(dest)
    return ref


def _populate(mapping: ISignalToIPduMapping):
    mapping.setISignalGroupRef(_ref("/AUTOSAR/ISignalGroups/Group1", "I-SIGNAL-GROUP"))
    mapping.setISignalRef(_ref("/AUTOSAR/ISignals/Signal1", "I-SIGNAL"))

    byte_order = ByteOrderEnum()
    byte_order.setValue(ByteOrderEnum.MOST_SIGNIFICANT_BYTE_LAST)
    mapping.setPackingByteOrder(byte_order)

    start_position = UnlimitedInteger()
    start_position.setValue("8")
    mapping.setStartPosition(start_position)

    transfer_property = TransferPropertyEnum()
    transfer_property.setValue(TransferPropertyEnum.TRIGGERED)
    mapping.setTransferProperty(transfer_property)

    update_position = UnlimitedInteger()
    update_position.setValue("3")
    mapping.setUpdateIndicationBitPosition(update_position)

    variation_point = VariationPoint()
    variation_point.setShortLabel(Identifier().setValue("vp_label"))
    mapping.setVariationPoint(variation_point)


def _assert_full_values(mapping: ISignalToIPduMapping):
    assert mapping.getShortName() == "Mapping1"
    assert mapping.getISignalGroupRef().getValue() == "/AUTOSAR/ISignalGroups/Group1"
    assert mapping.getISignalGroupRef().getDest() == "I-SIGNAL-GROUP"
    assert mapping.getISignalRef().getValue() == "/AUTOSAR/ISignals/Signal1"
    assert mapping.getISignalRef().getDest() == "I-SIGNAL"
    assert mapping.getPackingByteOrder().getValue() == "MOST-SIGNIFICANT-BYTE-LAST"
    assert isinstance(mapping.getStartPosition(), UnlimitedInteger)
    assert mapping.getStartPosition().getValue() == 8
    assert mapping.getTransferProperty().getValue() == "TRIGGERED"
    assert isinstance(mapping.getUpdateIndicationBitPosition(), UnlimitedInteger)
    assert mapping.getUpdateIndicationBitPosition().getValue() == 3
    assert mapping.getVariationPoint() is not None
    assert mapping.getVariationPoint().getShortLabel().getValue() == "vp_label"


class TestWriteISignalToIPduMapping:
    def test_write_empty(self):
        mapping = ISignalToIPduMapping(None, "Mapping1")
        parent = ET.Element("PARENT")
        ARXMLWriter().writeISignalToIPduMapping(parent, mapping)

        node = parent.find("I-SIGNAL-TO-I-PDU-MAPPING")
        for tag in XSD_CHILD_ORDER:
            assert node.find(tag) is None, tag

    def test_write_full_child_order_matches_xsd(self):
        mapping = ISignalToIPduMapping(None, "Mapping1")
        _populate(mapping)

        parent = ET.Element("PARENT")
        ARXMLWriter().writeISignalToIPduMapping(parent, mapping)

        node = parent.find("I-SIGNAL-TO-I-PDU-MAPPING")
        tags = [child.tag for child in node]
        assert [tag for tag in tags if tag in XSD_CHILD_ORDER] == XSD_CHILD_ORDER

    def test_write_full_field_values(self):
        mapping = ISignalToIPduMapping(None, "Mapping1")
        _populate(mapping)

        parent = ET.Element("PARENT")
        ARXMLWriter().writeISignalToIPduMapping(parent, mapping)

        node = parent.find("I-SIGNAL-TO-I-PDU-MAPPING")
        group_ref = node.find("I-SIGNAL-GROUP-REF")
        assert group_ref.text == "/AUTOSAR/ISignalGroups/Group1"
        assert group_ref.get("DEST") == "I-SIGNAL-GROUP"
        signal_ref = node.find("I-SIGNAL-REF")
        assert signal_ref.text == "/AUTOSAR/ISignals/Signal1"
        assert signal_ref.get("DEST") == "I-SIGNAL"
        assert node.find("PACKING-BYTE-ORDER").text == "MOST-SIGNIFICANT-BYTE-LAST"
        assert node.find("START-POSITION").text == "8"
        assert node.find("TRANSFER-PROPERTY").text == "TRIGGERED"
        assert node.find("UPDATE-INDICATION-BIT-POSITION").text == "3"
        assert node.find("VARIATION-POINT/SHORT-LABEL").text == "vp_label"

    def test_round_trip_full(self):
        mapping = ISignalToIPduMapping(None, "Mapping1")
        _populate(mapping)

        parent = ET.Element("PARENT")
        ARXMLWriter().writeISignalToIPduMapping(parent, mapping)

        reloaded = ISignalToIPduMapping(None, "Mapping1")
        ARXMLParser().readISignalToIPduMapping(_with_ns(parent)[0], reloaded)

        _assert_full_values(reloaded)

    def test_round_trip_empty(self):
        mapping = ISignalToIPduMapping(None, "Mapping1")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeISignalToIPduMapping(parent, mapping)

        reloaded = ISignalToIPduMapping(None, "Mapping1")
        ARXMLParser().readISignalToIPduMapping(_with_ns(parent)[0], reloaded)

        assert reloaded.getISignalRef() is None
        assert reloaded.getISignalGroupRef() is None
        assert reloaded.getPackingByteOrder() is None
        assert reloaded.getStartPosition() is None
        assert reloaded.getTransferProperty() is None
        assert reloaded.getUpdateIndicationBitPosition() is None
        assert reloaded.getVariationPoint() is None
