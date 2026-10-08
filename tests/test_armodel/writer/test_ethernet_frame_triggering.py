"""Writer round-trip tests for EthernetFrameTriggering (Table 6.230, p.578)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetFrame import EthernetFrameTriggering
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _ref(value, dest):
    ref = RefType()
    ref.setValue(value)
    ref.setDest(dest)
    return ref


def _full_triggering():
    triggering = EthernetFrameTriggering(parent=AUTOSAR.getInstance(), short_name="eth_ft")
    triggering.setFrameRef(_ref("/cluster/frames/eth_frame", "ETHERNET-FRAME"))
    triggering.addFramePortRef(_ref("/ecus/sender/frame_port", "FRAME-PORT-INSTANCE-REF"))
    triggering.addFramePortRef(_ref("/ecus/receiver/frame_port", "FRAME-PORT-INSTANCE-REF"))
    triggering.addPduTriggeringRef(_ref("/cluster/ch/pdu_triggering", "PDU-TRIGGERING"))
    return triggering


def _bare_triggering():
    return EthernetFrameTriggering(parent=AUTOSAR.getInstance(), short_name="eth_ft")


def test_write_ethernet_frame_triggering_xml():
    triggering = _full_triggering()
    parent = ET.Element("ROOT")
    ARXMLWriter().writeEthernetFrameTriggering(parent, triggering)

    elem = parent.find("ETHERNET-FRAME-TRIGGERING")
    assert elem is not None
    assert elem.find("SHORT-NAME").text == "eth_ft"

    frame_port_refs = elem.find("FRAME-PORT-REFS")
    assert frame_port_refs is not None
    ports = frame_port_refs.findall("FRAME-PORT-REF")
    assert [ref.text for ref in ports] == ["/ecus/sender/frame_port", "/ecus/receiver/frame_port"]
    assert all(ref.get("DEST") == "FRAME-PORT-INSTANCE-REF" for ref in ports)

    frame_ref = elem.find("FRAME-REF")
    assert frame_ref is not None
    assert frame_ref.get("DEST") == "ETHERNET-FRAME"
    assert frame_ref.text == "/cluster/frames/eth_frame"

    pdu_triggerings = elem.find("PDU-TRIGGERINGS")
    assert pdu_triggerings is not None
    conditional = pdu_triggerings.find("PDU-TRIGGERING-REF-CONDITIONAL")
    assert conditional is not None
    assert conditional.find("PDU-TRIGGERING-REF").text == "/cluster/ch/pdu_triggering"


def test_write_omits_empty_wrappers_and_optional_elements():
    parent = ET.Element("ROOT")
    ARXMLWriter().writeEthernetFrameTriggering(parent, _bare_triggering())

    elem = parent.find("ETHERNET-FRAME-TRIGGERING")
    assert elem is not None
    assert elem.find("SHORT-NAME").text == "eth_ft"
    assert elem.find("FRAME-PORT-REFS") is None
    assert elem.find("FRAME-REF") is None
    assert elem.find("PDU-TRIGGERINGS") is None


def test_round_trip_full():
    parent = ET.Element("ROOT")
    ARXMLWriter().writeEthernetFrameTriggering(parent, _full_triggering())

    xml_text = ET.tostring(parent[0], encoding="unicode")
    namespaced = ET.fromstring(xml_text.replace(parent[0].tag, "%s xmlns='%s'" % (parent[0].tag, NS), 1))

    reloaded = EthernetFrameTriggering(parent=AUTOSAR.getInstance(), short_name="eth_ft")
    ARXMLParser().readEthernetFrameTriggering(namespaced, reloaded)

    assert reloaded.getFrameRef().getValue() == "/cluster/frames/eth_frame"
    assert reloaded.getFrameRef().getDest() == "ETHERNET-FRAME"
    assert [r.getValue() for r in reloaded.getFramePortRefs()] == ["/ecus/sender/frame_port", "/ecus/receiver/frame_port"]
    assert [r.getValue() for r in reloaded.getPduTriggeringRefs()] == ["/cluster/ch/pdu_triggering"]
