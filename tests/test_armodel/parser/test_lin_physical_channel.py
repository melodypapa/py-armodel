"""Parser tests for LinPhysicalChannel (Table 3.46, p.100).

The XSD group LIN-PHYSICAL-CHANNEL (AUTOSAR_00052.xsd line 77544) contributes
BUS-IDLE-TIMEOUT-PERIOD and the SCHEDULE-TABLES wrapper (choice of
LIN-SCHEDULE-TABLE) in that sequenceOffset order. readLinPhysicalChannel calls
the base readPhysicalChannel helper exactly once. The class is consumed as a
concrete element of the CommunicationClusterContent PHYSICAL-CHANNELS choice
(line 20219, Rule 0001.7): dispatch coverage runs through the
LIN-PHYSICAL-CHANNEL branch on readCommunicationClusterPhysicalChannels.
"""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology import CanPhysicalChannel
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication import LinScheduleTable
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinTopology import LinCluster, LinPhysicalChannel
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"

LIN_FULL_CHANNEL = (
    "<PHYSICAL-CHANNELS>"
    "<LIN-PHYSICAL-CHANNEL>"
    "<SHORT-NAME>lin_ch</SHORT-NAME>"
    "<COMM-CONNECTORS>"
    "<COMMUNICATION-CONNECTOR-REF-CONDITIONAL>"
    "<COMMUNICATION-CONNECTOR-REF DEST='LIN-COMMUNICATION-CONNECTOR'>/ecu/lin_conn</COMMUNICATION-CONNECTOR-REF>"
    "</COMMUNICATION-CONNECTOR-REF-CONDITIONAL>"
    "</COMM-CONNECTORS>"
    "<BUS-IDLE-TIMEOUT-PERIOD>0.5</BUS-IDLE-TIMEOUT-PERIOD>"
    "<SCHEDULE-TABLES>"
    "<LIN-SCHEDULE-TABLE><SHORT-NAME>table1</SHORT-NAME></LIN-SCHEDULE-TABLE>"
    "<LIN-SCHEDULE-TABLE><SHORT-NAME>table2</SHORT-NAME></LIN-SCHEDULE-TABLE>"
    "</SCHEDULE-TABLES>"
    "</LIN-PHYSICAL-CHANNEL>"
    "</PHYSICAL-CHANNELS>"
)

LIN_BARE_CHANNEL = "<PHYSICAL-CHANNELS>" "<LIN-PHYSICAL-CHANNEL>" "<SHORT-NAME>lin_ch</SHORT-NAME>" "</LIN-PHYSICAL-CHANNEL>" "</PHYSICAL-CHANNELS>"

LIN_EMPTY_SCHEDULE_TABLES = "<PHYSICAL-CHANNELS>" "<LIN-PHYSICAL-CHANNEL>" "<SHORT-NAME>lin_ch</SHORT-NAME>" "<SCHEDULE-TABLES/>" "</LIN-PHYSICAL-CHANNEL>" "</PHYSICAL-CHANNELS>"


def _read_into_cluster(inner):
    root = ET.fromstring("<ROOT xmlns='%s'>%s</ROOT>" % (NS, inner))
    pkg = AUTOSAR.getInstance().createARPackage("Pkg")
    cluster = LinCluster(pkg, "Cluster")
    ARXMLParser().readCommunicationClusterPhysicalChannels(root, cluster)
    return cluster


class TestReadLinPhysicalChannelDispatch:
    """Table 3.46: the LIN-PHYSICAL-CHANNEL dispatch branch constructs the concrete LinPhysicalChannel (Rule 0001.7 dispatch coverage)."""

    def test_dispatch_creates_lin_physical_channel_instance(self, parser):
        cluster = _read_into_cluster(LIN_BARE_CHANNEL)
        channel = cluster.getPhysicalChannels()[0]

        assert isinstance(channel, LinPhysicalChannel)
        assert channel.getShortName() == "lin_ch"
        assert channel.getCommConnectorRefs() == []
        assert channel.getBusIdleTimeoutPeriod() is None
        assert channel.getScheduleTables() == []

    def test_dispatch_keeps_can_branch_disjoint(self, parser):
        mixed = (
            "<PHYSICAL-CHANNELS>"
            "<LIN-PHYSICAL-CHANNEL><SHORT-NAME>lin_ch</SHORT-NAME></LIN-PHYSICAL-CHANNEL>"
            "<CAN-PHYSICAL-CHANNEL><SHORT-NAME>can_ch</SHORT-NAME></CAN-PHYSICAL-CHANNEL>"
            "</PHYSICAL-CHANNELS>"
        )
        cluster = _read_into_cluster(mixed)
        channels = {c.getShortName(): c for c in cluster.getPhysicalChannels()}

        assert sorted(channels.keys()) == ["can_ch", "lin_ch"]
        assert isinstance(channels["lin_ch"], LinPhysicalChannel)
        assert not isinstance(channels["lin_ch"], CanPhysicalChannel)
        assert isinstance(channels["can_ch"], CanPhysicalChannel)
        assert not isinstance(channels["can_ch"], LinPhysicalChannel)

    def test_dispatch_reads_field_values(self, parser):
        cluster = _read_into_cluster(LIN_FULL_CHANNEL)
        channel = cluster.getPhysicalChannels()[0]

        assert isinstance(channel, LinPhysicalChannel)
        assert channel.getShortName() == "lin_ch"

        bus_idle_timeout = channel.getBusIdleTimeoutPeriod()
        assert bus_idle_timeout is not None
        assert bus_idle_timeout.getValue() == 0.5

        refs = channel.getCommConnectorRefs()
        assert len(refs) == 1
        assert refs[0].getValue() == "/ecu/lin_conn"
        assert refs[0].getDest() == "LIN-COMMUNICATION-CONNECTOR"

        tables = channel.getScheduleTables()
        assert [t.getShortName() for t in tables] == ["table1", "table2"]
        assert all(isinstance(t, LinScheduleTable) for t in tables)
        assert tables[0].getParent() is channel


class TestReadLinPhysicalChannel:
    """Table 3.46: the readLinPhysicalChannel entry helper calls readPhysicalChannel exactly once and reads the LIN level in XSD order."""

    def test_entry_helper_reads_physical_channel_and_lin_level(self, parser):
        root = ET.fromstring("<ROOT xmlns='%s'>%s</ROOT>" % (NS, LIN_FULL_CHANNEL))
        pkg = AUTOSAR.getInstance().createARPackage("Pkg")
        channel = LinPhysicalChannel(pkg, "lin_ch")
        parser.readLinPhysicalChannel(root[0][0], channel)

        assert channel.getShortName() == "lin_ch"
        assert channel.getBusIdleTimeoutPeriod().getValue() == 0.5
        assert channel.getCommConnectorRefs()[0].getValue() == "/ecu/lin_conn"
        assert channel.getCommConnectorRefs()[0].getDest() == "LIN-COMMUNICATION-CONNECTOR"
        assert [t.getShortName() for t in channel.getScheduleTables()] == ["table1", "table2"]
        assert all(isinstance(t, LinScheduleTable) for t in channel.getScheduleTables())

    def test_entry_helper_reads_bare_channel_to_empty_fields(self, parser):
        root = ET.fromstring("<ROOT xmlns='%s'>%s</ROOT>" % (NS, LIN_BARE_CHANNEL))
        pkg = AUTOSAR.getInstance().createARPackage("Pkg")
        channel = LinPhysicalChannel(pkg, "lin_ch")
        parser.readLinPhysicalChannel(root[0][0], channel)

        assert channel.getShortName() == "lin_ch"
        assert channel.getBusIdleTimeoutPeriod() is None
        assert channel.getScheduleTables() == []
        assert channel.getCommConnectorRefs() == []

    def test_entry_helper_reads_empty_schedule_tables_wrapper(self, parser):
        root = ET.fromstring("<ROOT xmlns='%s'>%s</ROOT>" % (NS, LIN_EMPTY_SCHEDULE_TABLES))
        pkg = AUTOSAR.getInstance().createARPackage("Pkg")
        channel = LinPhysicalChannel(pkg, "lin_ch")
        parser.readLinPhysicalChannel(root[0][0], channel)

        assert channel.getScheduleTables() == []
