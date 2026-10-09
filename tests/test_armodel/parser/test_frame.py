"""Tests for Frame reader (Table 6.78: Frame).

The FRAME group of AUTOSAR_00052.xsd (l.62960) owns two children in sequence
order — FRAME-LENGTH (INTEGER, 0..1) and the PDU-TO-FRAME-MAPPINGS wrapper
(0..1, unbounded PDU-TO-FRAME-MAPPING choice). readFrame must call
readIdentifiable exactly once for the inherited levels (S/T,
SHORT-NAME-FRAGMENTS, UUID, CATEGORY, ADMIN-DATA, DESC) and read the own
children via the model mutators.
"""

import xml.etree.cElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Integer
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanCommunication import CanFrame

_NS = "http://autosar.org/schema/r4.0"

_UUID_VALUE = "7c3a5b6c-7d8e-49a0-b1c2-3d4e5f6a7b8e"


def _snip(inner: str) -> ET.Element:
    return ET.fromstring("<CAN-FRAME xmlns='%s'>%s</CAN-FRAME>" % (_NS, inner))


def test_read_frame_frame_length(parser):
    element = _snip("<SHORT-NAME>MyFrame</SHORT-NAME>" "<FRAME-LENGTH>100</FRAME-LENGTH>")
    frame = CanFrame(None, "MyFrame")
    parser.readCanFrame(element, frame)
    assert isinstance(frame.getFrameLength(), Integer)
    assert frame.getFrameLength().getValue() == 100


def test_read_frame_frame_length_absent(parser):
    element = _snip("<SHORT-NAME>MyFrame</SHORT-NAME>")
    frame = CanFrame(None, "MyFrame")
    parser.readCanFrame(element, frame)
    assert frame.getFrameLength() is None
    assert frame.getPduToFrameMappings() == []


def test_read_frame_pdu_to_frame_mapping(parser):
    element = _snip(
        "<SHORT-NAME>MyFrame</SHORT-NAME>"
        "<PDU-TO-FRAME-MAPPINGS>"
        "<PDU-TO-FRAME-MAPPING>"
        "<SHORT-NAME>Map1</SHORT-NAME>"
        "<START-POSITION>8</START-POSITION>"
        "</PDU-TO-FRAME-MAPPING>"
        "</PDU-TO-FRAME-MAPPINGS>"
    )
    frame = CanFrame(None, "MyFrame")
    parser.readCanFrame(element, frame)
    mappings = frame.getPduToFrameMappings()
    assert len(mappings) == 1
    assert mappings[0].getShortName() == "Map1"
    assert mappings[0].getStartPosition().getValue() == 8


def test_read_frame_mapping_full(parser):
    element = _snip(
        "<SHORT-NAME>MyFrame</SHORT-NAME>"
        "<PDU-TO-FRAME-MAPPINGS>"
        "<PDU-TO-FRAME-MAPPING>"
        "<SHORT-NAME>Map1</SHORT-NAME>"
        "<PACKING-BYTE-ORDER>MOST-SIGNIFICANT-BYTE-FIRST</PACKING-BYTE-ORDER>"
        "<PDU-REF DEST='NM-PDU'>/pdus/NmPdu1</PDU-REF>"
        "<START-POSITION>8</START-POSITION>"
        "<UPDATE-INDICATION-BIT-POSITION>7</UPDATE-INDICATION-BIT-POSITION>"
        "</PDU-TO-FRAME-MAPPING>"
        "</PDU-TO-FRAME-MAPPINGS>"
    )
    frame = CanFrame(None, "MyFrame")
    parser.readCanFrame(element, frame)
    mapping = frame.getPduToFrameMappings()[0]
    assert mapping.getPackingByteOrder().getValue() == "MOST-SIGNIFICANT-BYTE-FIRST"
    assert mapping.getPduRef().getValue() == "/pdus/NmPdu1"
    assert mapping.getPduRef().getDest() == "NM-PDU"
    assert mapping.getStartPosition().getValue() == 8
    assert mapping.getUpdateIndicationBitPosition().getValue() == 7


def test_read_frame_empty_wrapper_list(parser):
    element = _snip("<SHORT-NAME>MyFrame</SHORT-NAME>" "<PDU-TO-FRAME-MAPPINGS/>")
    frame = CanFrame(None, "MyFrame")
    parser.readCanFrame(element, frame)
    assert frame.getPduToFrameMappings() == []


def test_read_frame_base_level_attributes(parser):
    element = ET.fromstring(
        "<CAN-FRAME xmlns='%s' UUID='%s' S='5' T='2025-04-04T00:00:00Z'>" "<SHORT-NAME>MyFrame</SHORT-NAME>" "<CATEGORY>someCategory</CATEGORY>" "</CAN-FRAME>" % (_NS, _UUID_VALUE)
    )
    frame = CanFrame(None, "MyFrame")
    parser.readCanFrame(element, frame)
    assert frame.getUuid().getValue() == _UUID_VALUE
    assert frame.getChecksum().getValue() == "5"
    assert frame.getTimestamp().getValue() == "2025-04-04T00:00:00Z"
    assert frame.getCategory().getValue() == "someCategory"


def test_read_frame_mapping_document_order(parser):
    element = _snip(
        "<SHORT-NAME>MyFrame</SHORT-NAME>"
        "<PDU-TO-FRAME-MAPPINGS>"
        "<PDU-TO-FRAME-MAPPING>"
        "<SHORT-NAME>Bravo</SHORT-NAME>"
        "</PDU-TO-FRAME-MAPPING>"
        "<PDU-TO-FRAME-MAPPING>"
        "<SHORT-NAME>Alpha</SHORT-NAME>"
        "</PDU-TO-FRAME-MAPPING>"
        "</PDU-TO-FRAME-MAPPINGS>"
    )
    frame = CanFrame(None, "MyFrame")
    parser.readCanFrame(element, frame)
    mappings = frame.getPduToFrameMappings()
    assert [m.getShortName() for m in mappings] == ["Bravo", "Alpha"]
