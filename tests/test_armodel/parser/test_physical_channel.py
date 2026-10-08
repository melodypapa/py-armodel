"""Parser tests for PhysicalChannel (Table 3.7, p.59).

XML element order per XSD group PHYSICAL-CHANNEL: COMM-CONNECTORS,
FRAME-TRIGGERINGS, I-SIGNAL-TRIGGERINGS, MANAGED-PHYSICAL-CHANNEL-REFS,
PDU-TRIGGERINGS.
Coverage runs through the PHYSICAL-CHANNELS dispatch on
readCommunicationClusterPhysicalChannels.
"""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanCommunication import CanFrameTriggering
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology import CanPhysicalChannel
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetFrame import EthernetFrameTriggering
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication import LinFrameTriggering
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (
    ISignalTriggering,
    PduTriggering,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import CanCluster
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"

FULL_CHANNEL = (
    "<PHYSICAL-CHANNELS>"
    "<CAN-PHYSICAL-CHANNEL>"
    "<SHORT-NAME>ch</SHORT-NAME>"
    "<COMM-CONNECTORS>"
    "<COMMUNICATION-CONNECTOR-REF-CONDITIONAL>"
    "<COMMUNICATION-CONNECTOR-REF DEST='CAN-COMMUNICATION-CONNECTOR'>/ecu/can_conn</COMMUNICATION-CONNECTOR-REF>"
    "</COMMUNICATION-CONNECTOR-REF-CONDITIONAL>"
    "</COMM-CONNECTORS>"
    "<FRAME-TRIGGERINGS>"
    "<CAN-FRAME-TRIGGERING>"
    "<SHORT-NAME>can_ft</SHORT-NAME>"
    "<FRAME-REF DEST='CAN-FRAME'>/cluster/frames/frame1</FRAME-REF>"
    "</CAN-FRAME-TRIGGERING>"
    "<ETHERNET-FRAME-TRIGGERING>"
    "<SHORT-NAME>eth_ft</SHORT-NAME>"
    "</ETHERNET-FRAME-TRIGGERING>"
    "<LIN-FRAME-TRIGGERING>"
    "<SHORT-NAME>lin_ft</SHORT-NAME>"
    "</LIN-FRAME-TRIGGERING>"
    "</FRAME-TRIGGERINGS>"
    "<I-SIGNAL-TRIGGERINGS>"
    "<I-SIGNAL-TRIGGERING>"
    "<SHORT-NAME>ist</SHORT-NAME>"
    "</I-SIGNAL-TRIGGERING>"
    "</I-SIGNAL-TRIGGERINGS>"
    "<MANAGED-PHYSICAL-CHANNEL-REFS>"
    "<MANAGED-PHYSICAL-CHANNEL-REF DEST='FLEXRAY-PHYSICAL-CHANNEL'>/cluster/ch2</MANAGED-PHYSICAL-CHANNEL-REF>"
    "</MANAGED-PHYSICAL-CHANNEL-REFS>"
    "<PDU-TRIGGERINGS>"
    "<PDU-TRIGGERING>"
    "<SHORT-NAME>pdt</SHORT-NAME>"
    "</PDU-TRIGGERING>"
    "</PDU-TRIGGERINGS>"
    "</CAN-PHYSICAL-CHANNEL>"
    "</PHYSICAL-CHANNELS>"
)

BARE_CHANNEL = "<PHYSICAL-CHANNELS>" "<CAN-PHYSICAL-CHANNEL>" "<SHORT-NAME>ch</SHORT-NAME>" "</CAN-PHYSICAL-CHANNEL>" "</PHYSICAL-CHANNELS>"


def _read_into_cluster(inner):
    root = ET.fromstring("<ROOT xmlns='%s'>%s</ROOT>" % (NS, inner))
    pkg = AUTOSAR.getInstance().createARPackage("Pkg")
    cluster = CanCluster(pkg, "Cluster")
    ARXMLParser().readCommunicationClusterPhysicalChannels(root, cluster)
    return cluster


class TestReadPhysicalChannel:
    def test_dispatch_creates_channel_with_short_name(self, parser):
        cluster = _read_into_cluster(BARE_CHANNEL)
        channels = cluster.getPhysicalChannels()
        assert len(channels) == 1
        assert channels[0].getShortName() == "ch"

    def test_reads_comm_connector_ref_conditional(self, parser):
        cluster = _read_into_cluster(FULL_CHANNEL)
        channel = cluster.getPhysicalChannels()[0]
        refs = channel.getCommConnectorRefs()
        assert len(refs) == 1
        assert refs[0].getValue() == "/ecu/can_conn"
        assert refs[0].getDest() == "CAN-COMMUNICATION-CONNECTOR"

    def test_reads_frame_triggerings_of_all_four_subtypes_in_document_order(self, parser):
        cluster = _read_into_cluster(FULL_CHANNEL)
        channel = cluster.getPhysicalChannels()[0]
        triggerings = channel.getFrameTriggerings()
        assert [type(t) for t in triggerings] == [CanFrameTriggering, EthernetFrameTriggering, LinFrameTriggering]
        assert [t.getShortName() for t in triggerings] == ["can_ft", "eth_ft", "lin_ft"]

    def test_reads_can_frame_triggering_frame_ref(self, parser):
        cluster = _read_into_cluster(FULL_CHANNEL)
        channel = cluster.getPhysicalChannels()[0]
        can_ft = channel.getFrameTriggerings()[0]
        assert can_ft.getFrameRef() is not None
        assert can_ft.getFrameRef().getValue() == "/cluster/frames/frame1"
        assert can_ft.getFrameRef().getDest() == "CAN-FRAME"

    def test_reads_isignal_triggerings_with_values(self, parser):
        cluster = _read_into_cluster(FULL_CHANNEL)
        channel = cluster.getPhysicalChannels()[0]
        triggerings = channel.getISignalTriggerings()
        assert len(triggerings) == 1
        assert isinstance(triggerings[0], ISignalTriggering)
        assert triggerings[0].getShortName() == "ist"

    def test_reads_managed_physical_channel_refs(self, parser):
        cluster = _read_into_cluster(FULL_CHANNEL)
        channel = cluster.getPhysicalChannels()[0]
        refs = channel.getManagedPhysicalChannelRefs()
        assert len(refs) == 1
        assert refs[0].getValue() == "/cluster/ch2"
        assert refs[0].getDest() == "FLEXRAY-PHYSICAL-CHANNEL"

    def test_reads_pdu_triggerings_with_values(self, parser):
        cluster = _read_into_cluster(FULL_CHANNEL)
        channel = cluster.getPhysicalChannels()[0]
        triggerings = channel.getPduTriggerings()
        assert len(triggerings) == 1
        assert isinstance(triggerings[0], PduTriggering)
        assert triggerings[0].getShortName() == "pdt"

    def test_reads_channel_without_optional_elements_to_empty_fields(self, parser):
        cluster = _read_into_cluster(BARE_CHANNEL)
        channel = cluster.getPhysicalChannels()[0]
        assert channel.getCommConnectorRefs() == []
        assert channel.getFrameTriggerings() == []
        assert channel.getISignalTriggerings() == []
        assert channel.getManagedPhysicalChannelRefs() == []
        assert channel.getPduTriggerings() == []


class TestReadCanPhysicalChannelDispatch:
    """Table 3.21: the CAN-PHYSICAL-CHANNEL dispatch branch constructs the concrete CanPhysicalChannel (Rule 0001.7 dispatch coverage)."""

    def test_dispatch_creates_can_physical_channel_instance(self, parser):
        cluster = _read_into_cluster(BARE_CHANNEL)
        channel = cluster.getPhysicalChannels()[0]

        assert isinstance(channel, CanPhysicalChannel)
        assert channel.getShortName() == "ch"
        assert channel.getCommConnectorRefs() == []
