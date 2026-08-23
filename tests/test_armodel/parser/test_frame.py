"""Tests for Frame reader (Table 6.78: Frame)."""

import xml.etree.cElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Integer
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanCommunication import CanFrame

_NS = "http://autosar.org/schema/r4.0"


def _snip(inner: str) -> ET.Element:
    return ET.fromstring("<CAN-FRAME xmlns='%s'>%s</CAN-FRAME>" % (_NS, inner))


def test_read_frame_frame_length(parser):
    element = _snip("<SHORT-NAME>MyFrame</SHORT-NAME>" "<FRAME-LENGTH>100</FRAME-LENGTH>")
    frame = CanFrame(None, "MyFrame")
    parser.readCanFrame(element, frame)
    assert isinstance(frame.getFrameLength(), Integer)
    assert frame.getFrameLength().getValue() == 100


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
