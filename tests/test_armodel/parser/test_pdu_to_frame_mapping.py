"""Parser tests for PduToFrameMapping (Table 6.29, p.347).

The PDU-TO-FRAME-MAPPING group of AUTOSAR_00052.xsd (l.88686) owns four
children in sequence order — PACKING-BYTE-ORDER (BYTE-ORDER-ENUM), PDU-REF
(REF with required DEST of PDU--SUBTYPES-ENUM), START-POSITION (INTEGER),
UPDATE-INDICATION-BIT-POSITION (INTEGER) — plus the VARIATION-POINT slot
(xml.sequenceOffset=10000, Applicable for: Frame.pduToFrameMapping). The
PDU-TO-FRAME-MAPPING complexType (l.88745) stacks the inherited groups
AR-OBJECT .. IDENTIFIABLE, then the own group. The tests exercise
readPduToFrameMappings, which must call readIdentifiable exactly once for the
inherited levels (S/T, UUID, SHORT-NAME-FRAGMENTS) and read the own children
via the model mutators.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (
    Frame,
    PduToFrameMapping,
)
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"

UUID_VALUE = "7c3a5b6c-7d8e-49a0-b1c2-3d4e5f6a7b8e"


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


class TestReadPduToFrameMapping:
    def test_read_full(self):
        xml = f"""<CAN-FRAME xmlns='{NS}'>
            <PDU-TO-FRAME-MAPPINGS>
                <PDU-TO-FRAME-MAPPING>
                    <SHORT-NAME>Map1</SHORT-NAME>
                    <PACKING-BYTE-ORDER>MOST-SIGNIFICANT-BYTE-FIRST</PACKING-BYTE-ORDER>
                    <PDU-REF DEST='NM-PDU'>/pdus/NmPdu1</PDU-REF>
                    <START-POSITION>8</START-POSITION>
                    <UPDATE-INDICATION-BIT-POSITION>7</UPDATE-INDICATION-BIT-POSITION>
                </PDU-TO-FRAME-MAPPING>
            </PDU-TO-FRAME-MAPPINGS>
        </CAN-FRAME>"""
        frame = ConcreteFrame(None, "MyFrame")
        ARXMLParser().readPduToFrameMappings(ET.fromstring(xml), frame)

        mappings = frame.getPduToFrameMappings()
        assert len(mappings) == 1
        mapping = mappings[0]
        assert isinstance(mapping, PduToFrameMapping)
        assert mapping.getShortName() == "Map1"
        assert mapping.getPackingByteOrder() is not None
        assert mapping.getPackingByteOrder().getValue() == "MOST-SIGNIFICANT-BYTE-FIRST"
        assert mapping.getPduRef() is not None
        assert mapping.getPduRef().getValue() == "/pdus/NmPdu1"
        assert mapping.getPduRef().getDest() == "NM-PDU"
        assert mapping.getStartPosition() is not None
        assert mapping.getStartPosition().getValue() == 8
        assert mapping.getUpdateIndicationBitPosition() is not None
        assert mapping.getUpdateIndicationBitPosition().getValue() == 7

    def test_read_minimal(self):
        xml = f"""<CAN-FRAME xmlns='{NS}'>
            <PDU-TO-FRAME-MAPPINGS>
                <PDU-TO-FRAME-MAPPING>
                    <SHORT-NAME>Map1</SHORT-NAME>
                </PDU-TO-FRAME-MAPPING>
            </PDU-TO-FRAME-MAPPINGS>
        </CAN-FRAME>"""
        frame = ConcreteFrame(None, "MyFrame")
        ARXMLParser().readPduToFrameMappings(ET.fromstring(xml), frame)

        mapping = frame.getPduToFrameMappings()[0]
        assert mapping.getPackingByteOrder() is None
        assert mapping.getPduRef() is None
        assert mapping.getStartPosition() is None
        assert mapping.getUpdateIndicationBitPosition() is None

    def test_read_empty_wrapper_list(self):
        xml = f"<CAN-FRAME xmlns='{NS}'><PDU-TO-FRAME-MAPPINGS/></CAN-FRAME>"
        frame = ConcreteFrame(None, "MyFrame")
        ARXMLParser().readPduToFrameMappings(ET.fromstring(xml), frame)

        assert frame.getPduToFrameMappings() == []

    def test_read_base_level_attributes(self):
        xml = f"""<CAN-FRAME xmlns='{NS}'>
            <PDU-TO-FRAME-MAPPINGS>
                <PDU-TO-FRAME-MAPPING UUID='{UUID_VALUE}' S='5' T='2025-04-04T00:00:00Z'>
                    <SHORT-NAME>Map1</SHORT-NAME>
                    <VARIATION-POINT/>
                </PDU-TO-FRAME-MAPPING>
            </PDU-TO-FRAME-MAPPINGS>
        </CAN-FRAME>"""
        frame = ConcreteFrame(None, "MyFrame")
        ARXMLParser().readPduToFrameMappings(ET.fromstring(xml), frame)

        mapping = frame.getPduToFrameMappings()[0]
        assert mapping.getUuid().getValue() == UUID_VALUE
        assert mapping.getChecksum().getValue() == "5"
        assert mapping.getTimestamp().getValue() == "2025-04-04T00:00:00Z"
        assert mapping.getVariationPoint() is not None
