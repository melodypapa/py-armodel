"""Parser tests for AbstractEthernetFrame (Table 6.229, p.578) exercised
through its concrete subclass GenericEthernetFrame (Table 6.231).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetFrame import AbstractEthernetFrame, GenericEthernetFrame
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


def test_read_generic_ethernet_frame_fields(parser):
    xml = """
      <GENERIC-ETHERNET-FRAME>
        <SHORT-NAME>GenFrame</SHORT-NAME>
        <FRAME-LENGTH>16</FRAME-LENGTH>
        <PDU-TO-FRAME-MAPPINGS>
          <PDU-TO-FRAME-MAPPING>
            <SHORT-NAME>Map1</SHORT-NAME>
            <PDU-REF DEST="SECURED-I-PDU">/Pdus/SecuredPdu</PDU-REF>
            <START-POSITION>0</START-POSITION>
          </PDU-TO-FRAME-MAPPING>
        </PDU-TO-FRAME-MAPPINGS>
      </GENERIC-ETHERNET-FRAME>
    """
    root = _snip(xml)
    element = parser.find(root, "GENERIC-ETHERNET-FRAME")
    frame = GenericEthernetFrame(parent=AUTOSAR.getInstance(), short_name="GenFrame")
    parser.readGenericEthernetFrame(element, frame)

    assert isinstance(frame, AbstractEthernetFrame)
    assert frame.getFrameLength() is not None
    assert frame.getFrameLength().getValue() == 16

    mappings = frame.getPduToFrameMappings()
    assert len(mappings) == 1
    mapping = mappings[0]
    assert mapping.getShortName() == "Map1"
    assert mapping.getPduRef() is not None
    assert mapping.getPduRef().getValue() == "/Pdus/SecuredPdu"
    assert mapping.getPduRef().getDest() == "SECURED-I-PDU"
    assert mapping.getStartPosition() is not None
    assert mapping.getStartPosition().getValue() == 0


def test_read_generic_ethernet_frame_empty(parser):
    root = _snip("<GENERIC-ETHERNET-FRAME><SHORT-NAME>EmptyFrame</SHORT-NAME></GENERIC-ETHERNET-FRAME>")
    element = parser.find(root, "GENERIC-ETHERNET-FRAME")
    frame = GenericEthernetFrame(parent=AUTOSAR.getInstance(), short_name="EmptyFrame")
    parser.readGenericEthernetFrame(element, frame)

    assert isinstance(frame, AbstractEthernetFrame)
    assert frame.getFrameLength() is None
    assert frame.getPduToFrameMappings() == []
