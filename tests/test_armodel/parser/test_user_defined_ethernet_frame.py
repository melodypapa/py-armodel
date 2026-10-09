"""Parser tests for UserDefinedEthernetFrame (Table 6.232, p.579)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetFrame import AbstractEthernetFrame, UserDefinedEthernetFrame
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def parser():
    AUTOSAR.getInstance().new()
    return ARXMLParser()


def _snip(inner: str) -> ET.Element:
    return ET.fromstring(f"<ROOT xmlns='{NS}'>{inner}</ROOT>")


def test_read_user_defined_ethernet_frame_fields(parser):
    xml = """
      <USER-DEFINED-ETHERNET-FRAME>
        <SHORT-NAME>UserFrame</SHORT-NAME>
        <FRAME-LENGTH>64</FRAME-LENGTH>
      </USER-DEFINED-ETHERNET-FRAME>
    """
    root = _snip(xml)
    element = parser.find(root, "USER-DEFINED-ETHERNET-FRAME")
    frame = UserDefinedEthernetFrame(parent=AUTOSAR.getInstance(), short_name="UserFrame")
    parser.readUserDefinedEthernetFrame(element, frame)

    assert isinstance(frame, AbstractEthernetFrame)
    assert frame.getShortName() == "UserFrame"
    assert frame.getFrameLength() is not None
    assert frame.getFrameLength().getValue() == 64
    assert frame.getPduToFrameMappings() == []


def test_read_user_defined_ethernet_frame_empty(parser):
    root = _snip("<USER-DEFINED-ETHERNET-FRAME><SHORT-NAME>EmptyFrame</SHORT-NAME></USER-DEFINED-ETHERNET-FRAME>")
    element = parser.find(root, "USER-DEFINED-ETHERNET-FRAME")
    frame = UserDefinedEthernetFrame(parent=AUTOSAR.getInstance(), short_name="EmptyFrame")
    parser.readUserDefinedEthernetFrame(element, frame)

    assert isinstance(frame, AbstractEthernetFrame)
    assert frame.getFrameLength() is None
    assert frame.getPduToFrameMappings() == []


def test_ar_package_dispatch(parser, tmp_path):
    document = AUTOSAR.getInstance()
    document.setARRelease("R23-11")
    path = tmp_path / "user_defined_frame.arxml"
    path.write_text(
        """<?xml version='1.0' encoding='utf-8'?>
        <AUTOSAR xmlns='%s'>
          <AR-PACKAGES>
            <AR-PACKAGE>
              <SHORT-NAME>Frames</SHORT-NAME>
              <ELEMENTS>
                <USER-DEFINED-ETHERNET-FRAME>
                  <SHORT-NAME>DispatchedFrame</SHORT-NAME>
                  <FRAME-LENGTH>128</FRAME-LENGTH>
                </USER-DEFINED-ETHERNET-FRAME>
              </ELEMENTS>
            </AR-PACKAGE>
          </AR-PACKAGES>
        </AUTOSAR>"""
        % NS,
        encoding="utf-8",
    )
    ARXMLParser().load(str(path), document)

    frame = document.find("/Frames/DispatchedFrame")
    assert isinstance(frame, UserDefinedEthernetFrame)
    assert frame.getFrameLength() is not None
    assert frame.getFrameLength().getValue() == 128
