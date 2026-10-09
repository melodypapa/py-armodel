"""Parser tests for Ieee1722TpEthernetFrame (Table 6.233, p.579)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetFrame import AbstractEthernetFrame, Ieee1722TpEthernetFrame
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


def test_read_ieee1722_tp_ethernet_frame_fields(parser):
    xml = """
      <IEEE-1722-TP-ETHERNET-FRAME>
        <SHORT-NAME>IeeeFrame</SHORT-NAME>
        <RELATIVE-REPRESENTATION-TIME>0.05</RELATIVE-REPRESENTATION-TIME>
        <STREAM-IDENTIFIER>42</STREAM-IDENTIFIER>
        <SUB-TYPE>7</SUB-TYPE>
        <VERSION>2</VERSION>
      </IEEE-1722-TP-ETHERNET-FRAME>
    """
    root = _snip(xml)
    element = parser.find(root, "IEEE-1722-TP-ETHERNET-FRAME")
    frame = Ieee1722TpEthernetFrame(parent=AUTOSAR.getInstance(), short_name="IeeeFrame")
    parser.readIeee1722TpEthernetFrame(element, frame)

    assert isinstance(frame, AbstractEthernetFrame)
    assert frame.getShortName() == "IeeeFrame"
    assert frame.getRelativeRepresentationTime() is not None
    assert frame.getRelativeRepresentationTime().getValue() == 0.05
    assert frame.getStreamIdentifier() is not None
    assert frame.getStreamIdentifier().getValue() == 42
    assert frame.getSubType() is not None
    assert frame.getSubType().getValue() == 7
    assert frame.getVersion() is not None
    assert frame.getVersion().getValue() == 2


def test_read_ieee1722_tp_ethernet_frame_empty(parser):
    root = _snip("<IEEE-1722-TP-ETHERNET-FRAME><SHORT-NAME>EmptyFrame</SHORT-NAME></IEEE-1722-TP-ETHERNET-FRAME>")
    element = parser.find(root, "IEEE-1722-TP-ETHERNET-FRAME")
    frame = Ieee1722TpEthernetFrame(parent=AUTOSAR.getInstance(), short_name="EmptyFrame")
    parser.readIeee1722TpEthernetFrame(element, frame)

    assert isinstance(frame, AbstractEthernetFrame)
    assert frame.getRelativeRepresentationTime() is None
    assert frame.getStreamIdentifier() is None
    assert frame.getSubType() is None
    assert frame.getVersion() is None


def test_ar_package_dispatch(parser, tmp_path):
    document = AUTOSAR.getInstance()
    document.setARRelease("R23-11")
    path = tmp_path / "ieee1722_tp_frame.arxml"
    path.write_text(
        """<?xml version='1.0' encoding='utf-8'?>
        <AUTOSAR xmlns='%s'>
          <AR-PACKAGES>
            <AR-PACKAGE>
              <SHORT-NAME>Frames</SHORT-NAME>
              <ELEMENTS>
                <IEEE-1722-TP-ETHERNET-FRAME>
                  <SHORT-NAME>DispatchedFrame</SHORT-NAME>
                  <STREAM-IDENTIFIER>5</STREAM-IDENTIFIER>
                </IEEE-1722-TP-ETHERNET-FRAME>
              </ELEMENTS>
            </AR-PACKAGE>
          </AR-PACKAGES>
        </AUTOSAR>"""
        % NS,
        encoding="utf-8",
    )
    ARXMLParser().load(str(path), document)

    frame = document.find("/Frames/DispatchedFrame")
    assert isinstance(frame, Ieee1722TpEthernetFrame)
    assert frame.getStreamIdentifier() is not None
    assert frame.getStreamIdentifier().getValue() == 5
