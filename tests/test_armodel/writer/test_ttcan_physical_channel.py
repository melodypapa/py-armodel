"""Writer round-trip tests for TtcanPhysicalChannel (Table 3.26, p.77).

The class has no own attribute rows and its XSD group TTCAN-PHYSICAL-CHANNEL
(AUTOSAR_00052.xsd line 127126) is an empty <xsd:sequence/>: the concrete level
contributes no XML elements of its own. writeTtcanPhysicalChannel emits the
TTCAN-PHYSICAL-CHANNEL element and calls the base writePhysicalChannel helper
exactly once. The class is emitted as a concrete element of the
CommunicationClusterContent PHYSICAL-CHANNELS choice (line 20220, Rule 0001.7):
dispatch coverage runs through writeCommunicationClusterPhysicalChannels.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology import TtcanPhysicalChannel
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import CanCluster
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"

XSD_ORDER = ["COMM-CONNECTORS", "FRAME-TRIGGERINGS", "I-SIGNAL-TRIGGERINGS", "MANAGED-PHYSICAL-CHANNEL-REFS", "PDU-TRIGGERINGS"]


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
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
    channel = TtcanPhysicalChannel(MockParent(), "ttcan_ch")
    channel.addCommConnectorRef(_ref("/ecu/ttcan_conn", "TTCAN-COMMUNICATION-CONNECTOR"))
    can_ft = channel.createCanFrameTriggering("can_ft")
    can_ft.setFrameRef(_ref("/cluster/frames/frame1", "CAN-FRAME"))
    channel.createISignalTriggering("ist")
    channel.addManagedPhysicalChannelRef(_ref("/cluster/ttcan_ch2", "TTCAN-PHYSICAL-CHANNEL"))
    channel.createPduTriggering("pdt")
    return channel


def _bare_channel():
    return TtcanPhysicalChannel(MockParent(), "ttcan_ch")


def _write_channel(channel):
    parent = ET.Element("PARENT")
    ARXMLWriter().writeTtcanPhysicalChannel(parent, channel)
    return parent


def _namespaced_channel_tag(parent):
    xml_text = ET.tostring(parent, encoding="unicode")
    namespaced = ET.fromstring(xml_text.replace(parent[0].tag, "%s xmlns='%s'" % (parent[0].tag, NS), 1))
    return namespaced[0]


class TestWriteTtcanPhysicalChannel:
    def test_write_all_five_wrappers_in_xsd_order(self, writer):
        parent = _write_channel(_full_channel())
        channel_tag = parent.find("TTCAN-PHYSICAL-CHANNEL")
        assert channel_tag is not None
        tags = [child.tag for child in channel_tag]
        assert tags == ["SHORT-NAME"] + XSD_ORDER

    def test_write_field_values(self, writer):
        parent = _write_channel(_full_channel())
        channel_tag = parent.find("TTCAN-PHYSICAL-CHANNEL")

        comm_connectors = channel_tag.find("COMM-CONNECTORS")
        assert comm_connectors is not None
        conditional = comm_connectors.find("COMMUNICATION-CONNECTOR-REF-CONDITIONAL")
        assert conditional is not None
        comm_ref = conditional.find("COMMUNICATION-CONNECTOR-REF")
        assert comm_ref.get("DEST") == "TTCAN-COMMUNICATION-CONNECTOR"
        assert comm_ref.text == "/ecu/ttcan_conn"

        frame_triggerings = channel_tag.find("FRAME-TRIGGERINGS")
        assert frame_triggerings is not None
        assert frame_triggerings.find("CAN-FRAME-TRIGGERING/SHORT-NAME").text == "can_ft"
        frame_ref = frame_triggerings.find("CAN-FRAME-TRIGGERING/FRAME-REF")
        assert frame_ref.get("DEST") == "CAN-FRAME"
        assert frame_ref.text == "/cluster/frames/frame1"

        isignal_triggerings = channel_tag.find("I-SIGNAL-TRIGGERINGS")
        assert isignal_triggerings is not None
        assert isignal_triggerings.find("I-SIGNAL-TRIGGERING/SHORT-NAME").text == "ist"

        managed_refs = channel_tag.find("MANAGED-PHYSICAL-CHANNEL-REFS")
        assert managed_refs is not None
        managed_ref = managed_refs.find("MANAGED-PHYSICAL-CHANNEL-REF")
        assert managed_ref.get("DEST") == "TTCAN-PHYSICAL-CHANNEL"
        assert managed_ref.text == "/cluster/ttcan_ch2"

        pdu_triggerings = channel_tag.find("PDU-TRIGGERINGS")
        assert pdu_triggerings is not None
        assert pdu_triggerings.find("PDU-TRIGGERING/SHORT-NAME").text == "pdt"

    def test_write_omits_empty_wrappers_and_optional_elements(self, writer):
        parent = _write_channel(_bare_channel())
        channel_tag = parent.find("TTCAN-PHYSICAL-CHANNEL")
        assert channel_tag is not None
        assert [child.tag for child in channel_tag] == ["SHORT-NAME"]
        assert channel_tag.find("COMM-CONNECTORS") is None
        assert channel_tag.find("FRAME-TRIGGERINGS") is None
        assert channel_tag.find("I-SIGNAL-TRIGGERINGS") is None
        assert channel_tag.find("MANAGED-PHYSICAL-CHANNEL-REFS") is None
        assert channel_tag.find("PDU-TRIGGERINGS") is None

    def test_round_trip_full(self, writer, parser):
        parent = _write_channel(_full_channel())
        reloaded = _bare_channel()
        parser.readTtcanPhysicalChannel(_namespaced_channel_tag(parent), reloaded)

        assert isinstance(reloaded, TtcanPhysicalChannel)

        comm_refs = reloaded.getCommConnectorRefs()
        assert len(comm_refs) == 1
        assert comm_refs[0].getValue() == "/ecu/ttcan_conn"
        assert comm_refs[0].getDest() == "TTCAN-COMMUNICATION-CONNECTOR"

        triggerings = reloaded.getFrameTriggerings()
        assert [t.getShortName() for t in triggerings] == ["can_ft"]
        assert triggerings[0].getFrameRef().getValue() == "/cluster/frames/frame1"
        assert triggerings[0].getFrameRef().getDest() == "CAN-FRAME"

        isignal_triggerings = reloaded.getISignalTriggerings()
        assert len(isignal_triggerings) == 1
        assert isignal_triggerings[0].getShortName() == "ist"

        managed_refs = reloaded.getManagedPhysicalChannelRefs()
        assert len(managed_refs) == 1
        assert managed_refs[0].getValue() == "/cluster/ttcan_ch2"
        assert managed_refs[0].getDest() == "TTCAN-PHYSICAL-CHANNEL"

        pdu_triggerings = reloaded.getPduTriggerings()
        assert len(pdu_triggerings) == 1
        assert pdu_triggerings[0].getShortName() == "pdt"

    def test_round_trip_empty(self, writer, parser):
        parent = _write_channel(_bare_channel())
        reloaded = _bare_channel()
        parser.readTtcanPhysicalChannel(_namespaced_channel_tag(parent), reloaded)

        assert reloaded.getCommConnectorRefs() == []
        assert reloaded.getFrameTriggerings() == []
        assert reloaded.getISignalTriggerings() == []
        assert reloaded.getManagedPhysicalChannelRefs() == []
        assert reloaded.getPduTriggerings() == []


class TestWriteCommunicationClusterTtcanDispatch:
    """Table 3.26: the PHYSICAL-CHANNELS writer dispatch emits TTCAN-PHYSICAL-CHANNEL for a TtcanPhysicalChannel instance (Rule 0001.7)."""

    def test_dispatch_emits_ttcan_physical_channel_element(self, writer):
        pkg = AUTOSAR.getInstance().createARPackage("Pkg")
        cluster = CanCluster(pkg, "Cluster")
        cluster.createTtcanPhysicalChannel("ttcan_ch")

        parent = ET.Element("PARENT")
        writer.writeCommunicationClusterPhysicalChannels(parent, cluster)
        channels = parent.find("PHYSICAL-CHANNELS")
        assert channels is not None
        assert len(channels.findall("TTCAN-PHYSICAL-CHANNEL")) == 1
        assert channels.find("TTCAN-PHYSICAL-CHANNEL/SHORT-NAME").text == "ttcan_ch"
