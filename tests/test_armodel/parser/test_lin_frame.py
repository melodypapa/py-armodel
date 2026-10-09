"""Tests for LinFrame reader position in the Frame chain (Table 6.87: LinFrame).

LinFrame is abstract and declares no own attribute rows (Table 6.87 Attribute
row renders as '-'); its wire contribution is the concrete LIN-UNCONDITIONAL-FRAME
element whose reader chains readFrame (which chains readIdentifiable exactly
once for the inherited S/T, SHORT-NAME-FRAGMENTS, UUID, CATEGORY levels).
"""

import xml.etree.cElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Integer
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication import LinUnconditionalFrame

_NS = "http://autosar.org/schema/r4.0"

_UUID_VALUE = "7c3a5b6c-7d8e-49a0-b1c2-3d4e5f6a7b8e"


def _snip(inner: str, attrs: str = "") -> ET.Element:
    return ET.fromstring("<LIN-UNCONDITIONAL-FRAME xmlns='%s'%s>%s</LIN-UNCONDITIONAL-FRAME>" % (_NS, attrs, inner))


def test_read_lin_frame_frame_length(parser):
    element = _snip("<SHORT-NAME>MyLinFrame</SHORT-NAME>" "<FRAME-LENGTH>8</FRAME-LENGTH>")
    frame = LinUnconditionalFrame(None, "MyLinFrame")
    parser.readLinUnconditionalFrame(element, frame)
    assert isinstance(frame.getFrameLength(), Integer)
    assert frame.getFrameLength().getValue() == 8


def test_read_lin_frame_frame_length_absent(parser):
    element = _snip("<SHORT-NAME>MyLinFrame</SHORT-NAME>")
    frame = LinUnconditionalFrame(None, "MyLinFrame")
    parser.readLinUnconditionalFrame(element, frame)
    assert frame.getFrameLength() is None
    assert frame.getPduToFrameMappings() == []


def test_read_lin_frame_base_levels(parser):
    element = _snip("<SHORT-NAME>MyLinFrame</SHORT-NAME>", " UUID='%s'" % _UUID_VALUE)
    frame = LinUnconditionalFrame(None, "MyLinFrame")
    parser.readLinUnconditionalFrame(element, frame)
    assert frame.getUuid().getValue() == _UUID_VALUE
    assert frame.getShortName() == "MyLinFrame"
