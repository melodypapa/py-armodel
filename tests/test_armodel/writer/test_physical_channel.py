"""Writer round-trip tests for PhysicalChannel (Table 3.7, p.59).

XML element order per XSD group PHYSICAL-CHANNEL: COMM-CONNECTORS,
FRAME-TRIGGERINGS, I-SIGNAL-TRIGGERINGS, MANAGED-PHYSICAL-CHANNEL-REFS,
PDU-TRIGGERINGS.
Coverage runs through the CAN-PHYSICAL-CHANNEL emission on writeCanPhysicalChannel.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology import CanPhysicalChannel
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"

XSD_ORDER = ["COMM-CONNECTORS", "FRAME-TRIGGERINGS", "I-SIGNAL-TRIGGERINGS", "MANAGED-PHYSICAL-CHANNEL-REFS", "PDU-TRIGGERINGS"]


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


@pytest.fixture(autouse=True)
def reset_autosar():
    from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR

    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def writer():
    return ARXMLWriter()


@pytest.fixture
def parser():
    return ARXMLParser()


def _ref(value, dest):
    ref = RefType()
    ref.setValue(value)
    ref.setDest(dest)
    return ref


def _full_channel():
    channel = CanPhysicalChannel(MockParent(), "ch")
    channel.addCommConnectorRef(_ref("/ecu/can_conn", "CAN-COMMUNICATION-CONNECTOR"))
    can_ft = channel.createCanFrameTriggering("can_ft")
    can_ft.setFrameRef(_ref("/cluster/frames/frame1", "CAN-FRAME"))
    channel.createEthernetFrameTriggering("eth_ft")
    channel.createLinFrameTriggering("lin_ft")
    channel.createISignalTriggering("ist")
    channel.addManagedPhysicalChannelRef(_ref("/cluster/ch2", "FLEXRAY-PHYSICAL-CHANNEL"))
    channel.createPduTriggering("pdt")
    return channel


def _bare_channel():
    return CanPhysicalChannel(MockParent(), "ch")


def _write_channel(channel):
    parent = ET.Element("PARENT")
    ARXMLWriter().writeCanPhysicalChannel(parent, channel)
    return parent


def _namespaced_channel_tag(parent):
    xml_text = ET.tostring(parent, encoding="unicode")
    namespaced = ET.fromstring(xml_text.replace(parent[0].tag, "%s xmlns='%s'" % (parent[0].tag, NS), 1))
    return namespaced[0]


class TestWritePhysicalChannel:
    def test_write_all_five_wrappers_in_xsd_order(self, writer):
        parent = _write_channel(_full_channel())
        channel_tag = parent.find("CAN-PHYSICAL-CHANNEL")
        assert channel_tag is not None
        tags = [child.tag for child in channel_tag]
        assert tags == ["SHORT-NAME"] + XSD_ORDER

    def test_write_field_values(self, writer):
        parent = _write_channel(_full_channel())
        channel_tag = parent.find("CAN-PHYSICAL-CHANNEL")

        comm_connectors = channel_tag.find("COMM-CONNECTORS")
        assert comm_connectors is not None
        conditional = comm_connectors.find("COMMUNICATION-CONNECTOR-REF-CONDITIONAL")
        assert conditional is not None
        comm_ref = conditional.find("COMMUNICATION-CONNECTOR-REF")
        assert comm_ref.get("DEST") == "CAN-COMMUNICATION-CONNECTOR"
        assert comm_ref.text == "/ecu/can_conn"

        frame_triggerings = channel_tag.find("FRAME-TRIGGERINGS")
        assert frame_triggerings is not None
        ft_tags = [child.tag for child in frame_triggerings]
        assert ft_tags == ["CAN-FRAME-TRIGGERING", "ETHERNET-FRAME-TRIGGERING", "LIN-FRAME-TRIGGERING"]
        assert frame_triggerings.find("CAN-FRAME-TRIGGERING/SHORT-NAME").text == "can_ft"
        frame_ref = frame_triggerings.find("CAN-FRAME-TRIGGERING/FRAME-REF")
        assert frame_ref.get("DEST") == "CAN-FRAME"
        assert frame_ref.text == "/cluster/frames/frame1"
        assert frame_triggerings.find("ETHERNET-FRAME-TRIGGERING/SHORT-NAME").text == "eth_ft"
        assert frame_triggerings.find("LIN-FRAME-TRIGGERING/SHORT-NAME").text == "lin_ft"

        isignal_triggerings = channel_tag.find("I-SIGNAL-TRIGGERINGS")
        assert isignal_triggerings is not None
        assert isignal_triggerings.find("I-SIGNAL-TRIGGERING/SHORT-NAME").text == "ist"

        managed_refs = channel_tag.find("MANAGED-PHYSICAL-CHANNEL-REFS")
        assert managed_refs is not None
        managed_ref = managed_refs.find("MANAGED-PHYSICAL-CHANNEL-REF")
        assert managed_ref.get("DEST") == "FLEXRAY-PHYSICAL-CHANNEL"
        assert managed_ref.text == "/cluster/ch2"

        pdu_triggerings = channel_tag.find("PDU-TRIGGERINGS")
        assert pdu_triggerings is not None
        assert pdu_triggerings.find("PDU-TRIGGERING/SHORT-NAME").text == "pdt"

    def test_write_omits_empty_wrappers_and_optional_elements(self, writer):
        parent = _write_channel(_bare_channel())
        channel_tag = parent.find("CAN-PHYSICAL-CHANNEL")
        assert channel_tag is not None
        assert channel_tag.find("COMM-CONNECTORS") is None
        assert channel_tag.find("FRAME-TRIGGERINGS") is None
        assert channel_tag.find("I-SIGNAL-TRIGGERINGS") is None
        assert channel_tag.find("MANAGED-PHYSICAL-CHANNEL-REFS") is None
        assert channel_tag.find("PDU-TRIGGERINGS") is None

    def test_round_trip_full(self, writer, parser):
        parent = _write_channel(_full_channel())
        reloaded = _bare_channel()
        parser.readCanPhysicalChannel(_namespaced_channel_tag(parent), reloaded)

        comm_refs = reloaded.getCommConnectorRefs()
        assert len(comm_refs) == 1
        assert comm_refs[0].getValue() == "/ecu/can_conn"
        assert comm_refs[0].getDest() == "CAN-COMMUNICATION-CONNECTOR"

        from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanCommunication import CanFrameTriggering
        from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetFrame import EthernetFrameTriggering
        from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication import LinFrameTriggering

        triggerings = reloaded.getFrameTriggerings()
        assert [type(t) for t in triggerings] == [CanFrameTriggering, EthernetFrameTriggering, LinFrameTriggering]
        assert [t.getShortName() for t in triggerings] == ["can_ft", "eth_ft", "lin_ft"]
        assert triggerings[0].getFrameRef().getValue() == "/cluster/frames/frame1"
        assert triggerings[0].getFrameRef().getDest() == "CAN-FRAME"

        isignal_triggerings = reloaded.getISignalTriggerings()
        assert len(isignal_triggerings) == 1
        assert isignal_triggerings[0].getShortName() == "ist"

        managed_refs = reloaded.getManagedPhysicalChannelRefs()
        assert len(managed_refs) == 1
        assert managed_refs[0].getValue() == "/cluster/ch2"
        assert managed_refs[0].getDest() == "FLEXRAY-PHYSICAL-CHANNEL"

        pdu_triggerings = reloaded.getPduTriggerings()
        assert len(pdu_triggerings) == 1
        assert pdu_triggerings[0].getShortName() == "pdt"

    def test_round_trip_empty(self, writer, parser):
        parent = _write_channel(_bare_channel())
        reloaded = _bare_channel()
        parser.readCanPhysicalChannel(_namespaced_channel_tag(parent), reloaded)

        assert reloaded.getCommConnectorRefs() == []
        assert reloaded.getFrameTriggerings() == []
        assert reloaded.getISignalTriggerings() == []
        assert reloaded.getManagedPhysicalChannelRefs() == []
        assert reloaded.getPduTriggerings() == []
