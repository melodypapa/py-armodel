"""Parser tests for TtcanPhysicalChannel (Table 3.26, p.77).

The class has no own attribute rows and its XSD group TTCAN-PHYSICAL-CHANNEL
(AUTOSAR_00052.xsd line 127126) is an empty <xsd:sequence/>: the concrete level
contributes no XML elements of its own. readTtcanPhysicalChannel calls the base
readPhysicalChannel helper exactly once. The class is consumed as a concrete
element of the CommunicationClusterContent PHYSICAL-CHANNELS choice (line 20220,
Rule 0001.7): coverage runs through the TTCAN-PHYSICAL-CHANNEL dispatch branch on
readCommunicationClusterPhysicalChannels.
"""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology import CanPhysicalChannel, TtcanPhysicalChannel
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import CanCluster
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"

TTCAN_FULL_CHANNEL = (
    "<PHYSICAL-CHANNELS>"
    "<TTCAN-PHYSICAL-CHANNEL>"
    "<SHORT-NAME>ttcan_ch</SHORT-NAME>"
    "<COMM-CONNECTORS>"
    "<COMMUNICATION-CONNECTOR-REF-CONDITIONAL>"
    "<COMMUNICATION-CONNECTOR-REF DEST='TTCAN-COMMUNICATION-CONNECTOR'>/ecu/ttcan_conn</COMMUNICATION-CONNECTOR-REF>"
    "</COMMUNICATION-CONNECTOR-REF-CONDITIONAL>"
    "</COMM-CONNECTORS>"
    "<FRAME-TRIGGERINGS>"
    "<CAN-FRAME-TRIGGERING>"
    "<SHORT-NAME>can_ft</SHORT-NAME>"
    "<FRAME-REF DEST='CAN-FRAME'>/cluster/frames/frame1</FRAME-REF>"
    "</CAN-FRAME-TRIGGERING>"
    "</FRAME-TRIGGERINGS>"
    "<I-SIGNAL-TRIGGERINGS>"
    "<I-SIGNAL-TRIGGERING>"
    "<SHORT-NAME>ist</SHORT-NAME>"
    "</I-SIGNAL-TRIGGERING>"
    "</I-SIGNAL-TRIGGERINGS>"
    "<MANAGED-PHYSICAL-CHANNEL-REFS>"
    "<MANAGED-PHYSICAL-CHANNEL-REF DEST='TTCAN-PHYSICAL-CHANNEL'>/cluster/ttcan_ch2</MANAGED-PHYSICAL-CHANNEL-REF>"
    "</MANAGED-PHYSICAL-CHANNEL-REFS>"
    "<PDU-TRIGGERINGS>"
    "<PDU-TRIGGERING>"
    "<SHORT-NAME>pdt</SHORT-NAME>"
    "</PDU-TRIGGERING>"
    "</PDU-TRIGGERINGS>"
    "</TTCAN-PHYSICAL-CHANNEL>"
    "</PHYSICAL-CHANNELS>"
)

TTCAN_BARE_CHANNEL = "<PHYSICAL-CHANNELS>" "<TTCAN-PHYSICAL-CHANNEL>" "<SHORT-NAME>ttcan_ch</SHORT-NAME>" "</TTCAN-PHYSICAL-CHANNEL>" "</PHYSICAL-CHANNELS>"


def _read_into_cluster(inner):
    root = ET.fromstring("<ROOT xmlns='%s'>%s</ROOT>" % (NS, inner))
    pkg = AUTOSAR.getInstance().createARPackage("Pkg")
    cluster = CanCluster(pkg, "Cluster")
    ARXMLParser().readCommunicationClusterPhysicalChannels(root, cluster)
    return cluster


class TestReadTtcanPhysicalChannelDispatch:
    """Table 3.26: the TTCAN-PHYSICAL-CHANNEL dispatch branch constructs the concrete TtcanPhysicalChannel (Rule 0001.7 dispatch coverage)."""

    def test_dispatch_creates_ttcan_physical_channel_instance(self, parser):
        cluster = _read_into_cluster(TTCAN_BARE_CHANNEL)
        channel = cluster.getPhysicalChannels()[0]

        assert isinstance(channel, TtcanPhysicalChannel)
        assert channel.getShortName() == "ttcan_ch"
        assert channel.getCommConnectorRefs() == []

    def test_dispatch_keeps_can_branch_disjoint(self, parser):
        mixed = (
            "<PHYSICAL-CHANNELS>"
            "<TTCAN-PHYSICAL-CHANNEL><SHORT-NAME>ttcan_ch</SHORT-NAME></TTCAN-PHYSICAL-CHANNEL>"
            "<CAN-PHYSICAL-CHANNEL><SHORT-NAME>can_ch</SHORT-NAME></CAN-PHYSICAL-CHANNEL>"
            "</PHYSICAL-CHANNELS>"
        )
        cluster = _read_into_cluster(mixed)
        channels = cluster.getPhysicalChannels()

        assert [c.getShortName() for c in channels] == ["can_ch", "ttcan_ch"]
        assert isinstance(channels[0], CanPhysicalChannel)
        assert not isinstance(channels[0], TtcanPhysicalChannel)
        assert isinstance(channels[1], TtcanPhysicalChannel)
        assert not isinstance(channels[1], CanPhysicalChannel)

    def test_dispatch_reads_field_values(self, parser):
        from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanCommunication import CanFrameTriggering
        from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import ISignalTriggering, PduTriggering

        cluster = _read_into_cluster(TTCAN_FULL_CHANNEL)
        channel = cluster.getPhysicalChannels()[0]

        assert isinstance(channel, TtcanPhysicalChannel)
        assert channel.getShortName() == "ttcan_ch"

        refs = channel.getCommConnectorRefs()
        assert len(refs) == 1
        assert refs[0].getValue() == "/ecu/ttcan_conn"
        assert refs[0].getDest() == "TTCAN-COMMUNICATION-CONNECTOR"

        triggerings = channel.getFrameTriggerings()
        assert [type(t) for t in triggerings] == [CanFrameTriggering]
        assert triggerings[0].getShortName() == "can_ft"
        assert triggerings[0].getFrameRef().getValue() == "/cluster/frames/frame1"
        assert triggerings[0].getFrameRef().getDest() == "CAN-FRAME"

        isignal_triggerings = channel.getISignalTriggerings()
        assert len(isignal_triggerings) == 1
        assert isinstance(isignal_triggerings[0], ISignalTriggering)
        assert isignal_triggerings[0].getShortName() == "ist"

        managed_refs = channel.getManagedPhysicalChannelRefs()
        assert len(managed_refs) == 1
        assert managed_refs[0].getValue() == "/cluster/ttcan_ch2"
        assert managed_refs[0].getDest() == "TTCAN-PHYSICAL-CHANNEL"

        pdu_triggerings = channel.getPduTriggerings()
        assert len(pdu_triggerings) == 1
        assert isinstance(pdu_triggerings[0], PduTriggering)
        assert pdu_triggerings[0].getShortName() == "pdt"


class TestReadTtcanPhysicalChannel:
    """Table 3.26: the readTtcanPhysicalChannel entry helper calls readPhysicalChannel exactly once (no own elements to read)."""

    def test_entry_helper_reads_physical_channel_level(self, parser):
        root = ET.fromstring("<ROOT xmlns='%s'>%s</ROOT>" % (NS, TTCAN_FULL_CHANNEL))
        pkg = AUTOSAR.getInstance().createARPackage("Pkg")
        channel = TtcanPhysicalChannel(pkg, "ttcan_ch")
        parser.readTtcanPhysicalChannel(root[0][0], channel)

        assert channel.getShortName() == "ttcan_ch"
        refs = channel.getCommConnectorRefs()
        assert len(refs) == 1
        assert refs[0].getValue() == "/ecu/ttcan_conn"
        assert refs[0].getDest() == "TTCAN-COMMUNICATION-CONNECTOR"
        assert [t.getShortName() for t in channel.getFrameTriggerings()] == ["can_ft"]
        assert [t.getShortName() for t in channel.getISignalTriggerings()] == ["ist"]
        assert channel.getManagedPhysicalChannelRefs()[0].getValue() == "/cluster/ttcan_ch2"
        assert [t.getShortName() for t in channel.getPduTriggerings()] == ["pdt"]

    def test_entry_helper_reads_bare_channel_to_empty_fields(self, parser):
        root = ET.fromstring("<ROOT xmlns='%s'>%s</ROOT>" % (NS, TTCAN_BARE_CHANNEL))
        pkg = AUTOSAR.getInstance().createARPackage("Pkg")
        channel = TtcanPhysicalChannel(pkg, "ttcan_ch")
        parser.readTtcanPhysicalChannel(root[0][0], channel)

        assert channel.getShortName() == "ttcan_ch"
        assert channel.getCommConnectorRefs() == []
        assert channel.getFrameTriggerings() == []
        assert channel.getISignalTriggerings() == []
        assert channel.getManagedPhysicalChannelRefs() == []
        assert channel.getPduTriggerings() == []
