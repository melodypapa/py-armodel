"""Writer round-trip tests for PduToFrameMapping (Table 6.29, p.347).

Serialized through writePduToFrameMappings; the PDU-TO-FRAME-MAPPING group of
AUTOSAR_00052.xsd (l.88686) owns four children in sequence order —
PACKING-BYTE-ORDER (BYTE-ORDER-ENUM), PDU-REF (REF with required DEST of
PDU--SUBTYPES-ENUM), START-POSITION (INTEGER), UPDATE-INDICATION-BIT-POSITION
(INTEGER) — plus the VARIATION-POINT slot (xml.sequenceOffset=10000, written
by writeIdentifiable). The wrapper PDU-TO-FRAME-MAPPINGS is emitted only when
non-empty. The tests exercise writePduToFrameMappings, which must dispatch to
writeIdentifiable exactly once for the inherited levels (S/T, UUID) and emit
the own children in XSD sequence order.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ByteOrderEnum,
    DateTime,
    Integer,
    RefType,
    String,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (
    Frame,
    PduToFrameMapping,
)
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"

UUID_VALUE = "7c3a5b6c-7d8e-49a0-b1c2-3d4e5f6a7b8e"

XSD_CHILD_ORDER = [
    "PACKING-BYTE-ORDER",
    "PDU-REF",
    "START-POSITION",
    "UPDATE-INDICATION-BIT-POSITION",
]


class ConcreteFrame(Frame):
    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _with_ns(element: ET.Element) -> ET.Element:
    return ET.fromstring(ET.tostring(element).decode("utf-8").replace("<CAN-FRAME>", "<CAN-FRAME xmlns='%s'>" % NS, 1))


def _populate(frame: Frame) -> PduToFrameMapping:
    mapping = frame.createPduToFrameMapping("Map1")

    order = ByteOrderEnum()
    order.setValue(ByteOrderEnum.MOST_SIGNIFICANT_BYTE_FIRST)
    mapping.setPackingByteOrder(order)

    ref = RefType()
    ref.setValue("/pdus/NmPdu1")
    ref.setDest("NM-PDU")
    mapping.setPduRef(ref)

    mapping.setStartPosition(Integer().setValue("8"))
    mapping.setUpdateIndicationBitPosition(Integer().setValue("7"))
    return mapping


def _write_mappings_element(frame: Frame) -> ET.Element:
    parent = ET.Element("CAN-FRAME")
    ARXMLWriter().writePduToFrameMappings(parent, frame)
    return parent


class TestWritePduToFrameMapping:
    def test_write_empty_wrapper_list(self):
        frame = ConcreteFrame(None, "MyFrame")

        parent = _write_mappings_element(frame)
        assert parent.find("PDU-TO-FRAME-MAPPINGS") is None

    def test_write_full_child_order_matches_xsd(self):
        frame = ConcreteFrame(None, "MyFrame")
        _populate(frame)

        parent = _write_mappings_element(frame)
        wrapper = parent.find("PDU-TO-FRAME-MAPPINGS")
        assert wrapper is not None
        node = wrapper.find("PDU-TO-FRAME-MAPPING")
        tags = [child.tag for child in node]
        assert [tag for tag in tags if tag in XSD_CHILD_ORDER] == XSD_CHILD_ORDER

    def test_write_full_field_values(self):
        frame = ConcreteFrame(None, "MyFrame")
        _populate(frame)

        parent = _write_mappings_element(frame)
        node = parent.find("PDU-TO-FRAME-MAPPINGS/PDU-TO-FRAME-MAPPING")
        assert node.find("SHORT-NAME").text == "Map1"
        assert node.find("PACKING-BYTE-ORDER").text == "MOST-SIGNIFICANT-BYTE-FIRST"
        assert node.find("PDU-REF").text == "/pdus/NmPdu1"
        assert node.find("PDU-REF").attrib["DEST"] == "NM-PDU"
        assert node.find("START-POSITION").text == "8"
        assert node.find("UPDATE-INDICATION-BIT-POSITION").text == "7"

    def test_round_trip_full(self):
        frame = ConcreteFrame(None, "MyFrame")
        _populate(frame)

        parent = _write_mappings_element(frame)
        reloaded = ConcreteFrame(None, "MyFrame")
        ARXMLParser().readPduToFrameMappings(_with_ns(parent), reloaded)

        mappings = reloaded.getPduToFrameMappings()
        assert len(mappings) == 1
        mapping = mappings[0]
        assert mapping.getShortName() == "Map1"
        assert mapping.getPackingByteOrder().getValue() == "MOST-SIGNIFICANT-BYTE-FIRST"
        assert mapping.getPduRef().getValue() == "/pdus/NmPdu1"
        assert mapping.getPduRef().getDest() == "NM-PDU"
        assert mapping.getStartPosition().getValue() == 8
        assert mapping.getUpdateIndicationBitPosition().getValue() == 7

    def test_round_trip_base_level_attributes(self):
        frame = ConcreteFrame(None, "MyFrame")
        mapping = _populate(frame)
        mapping.setUuid(String().setValue(UUID_VALUE))
        mapping.setChecksum(String().setValue("5"))
        mapping.setTimestamp(DateTime().setValue("2025-04-04T00:00:00Z"))

        parent = _write_mappings_element(frame)
        node = parent.find("PDU-TO-FRAME-MAPPINGS/PDU-TO-FRAME-MAPPING")
        assert node.attrib["UUID"] == UUID_VALUE
        assert node.attrib["S"] == "5"
        assert node.attrib["T"] == "2025-04-04T00:00:00Z"

        reloaded = ConcreteFrame(None, "MyFrame")
        ARXMLParser().readPduToFrameMappings(_with_ns(parent), reloaded)

        reloaded_mapping = reloaded.getPduToFrameMappings()[0]
        assert reloaded_mapping.getUuid().getValue() == UUID_VALUE
        assert reloaded_mapping.getChecksum().getValue() == "5"
        assert reloaded_mapping.getTimestamp().getValue() == "2025-04-04T00:00:00Z"

    def test_round_trip_empty(self):
        frame = ConcreteFrame(None, "MyFrame")

        parent = _write_mappings_element(frame)
        reloaded = ConcreteFrame(None, "MyFrame")
        ARXMLParser().readPduToFrameMappings(_with_ns(parent), reloaded)

        assert reloaded.getPduToFrameMappings() == []
