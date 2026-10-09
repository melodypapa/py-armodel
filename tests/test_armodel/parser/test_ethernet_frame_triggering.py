"""Parser tests for EthernetFrameTriggering (Table 6.230, p.578)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetFrame import EthernetFrameTriggering
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


def test_read_ethernet_frame_triggering_fields(parser):
    xml = """
      <ETHERNET-FRAME-TRIGGERING>
        <SHORT-NAME>EthTriggering</SHORT-NAME>
        <FRAME-PORT-REFS>
          <FRAME-PORT-REF DEST="FRAME-PORT-INSTANCE-REF">/Ecus/Sender/Port</FRAME-PORT-REF>
          <FRAME-PORT-REF DEST="FRAME-PORT-INSTANCE-REF">/Ecus/Receiver/Port</FRAME-PORT-REF>
        </FRAME-PORT-REFS>
        <FRAME-REF DEST="ETHERNET-FRAME">/Frames/EthFrame</FRAME-REF>
        <PDU-TRIGGERINGS>
          <PDU-TRIGGERING-REF-CONDITIONAL>
            <PDU-TRIGGERING-REF DEST="PDU-TRIGGERING">/Clusters/Ch/PduTriggering</PDU-TRIGGERING-REF>
          </PDU-TRIGGERING-REF-CONDITIONAL>
        </PDU-TRIGGERINGS>
      </ETHERNET-FRAME-TRIGGERING>
    """
    root = _snip(xml)
    element = parser.find(root, "ETHERNET-FRAME-TRIGGERING")
    triggering = EthernetFrameTriggering(parent=AUTOSAR.getInstance(), short_name="EthTriggering")
    parser.readEthernetFrameTriggering(element, triggering)

    assert triggering.getShortName() == "EthTriggering"

    frame_ref = triggering.getFrameRef()
    assert frame_ref is not None
    assert frame_ref.getValue() == "/Frames/EthFrame"
    assert frame_ref.getDest() == "ETHERNET-FRAME"

    frame_port_refs = triggering.getFramePortRefs()
    assert [ref.getValue() for ref in frame_port_refs] == ["/Ecus/Sender/Port", "/Ecus/Receiver/Port"]
    assert all(ref.getDest() == "FRAME-PORT-INSTANCE-REF" for ref in frame_port_refs)

    pdu_triggering_refs = triggering.getPduTriggeringRefs()
    assert [ref.getValue() for ref in pdu_triggering_refs] == ["/Clusters/Ch/PduTriggering"]


def test_read_ethernet_frame_triggering_empty(parser):
    xml = """
      <ETHERNET-FRAME-TRIGGERING>
        <SHORT-NAME>EthTriggering</SHORT-NAME>
      </ETHERNET-FRAME-TRIGGERING>
    """
    root = _snip(xml)
    element = parser.find(root, "ETHERNET-FRAME-TRIGGERING")
    triggering = EthernetFrameTriggering(parent=AUTOSAR.getInstance(), short_name="EthTriggering")
    parser.readEthernetFrameTriggering(element, triggering)

    assert triggering.getFrameRef() is None
    assert triggering.getFramePortRefs() == []
    assert triggering.getPduTriggeringRefs() == []
