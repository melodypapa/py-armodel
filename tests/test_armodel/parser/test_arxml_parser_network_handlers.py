"""Phase G: targeted tests for uncovered communication and network handlers."""

import logging
import xml.etree.ElementTree as ET
import pytest
from armodel.models import AUTOSAR
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


@pytest.fixture
def warning_parser():
    AUTOSAR.getInstance().new()
    return ARXMLParser(options={"warning": True})


def _snip(inner: str, root_tag: str = "ROOT") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


def _autosar_root():
    return AUTOSAR.getInstance()


class TestCanClusterHandlers:
    def test_readCanCluster_sets_short_name(self, parser):
        from armodel.models import CanCluster
        cluster = CanCluster(parent=_autosar_root(), short_name="canCluster")
        element = _snip(
            "<SHORT-NAME>canCluster</SHORT-NAME>"
            "<CAN-CLUSTER-VARIANTS>"
            "<CAN-CLUSTER-CONDITIONAL>"
            "<BAUDRATE>500000</BAUDRATE>"
            "</CAN-CLUSTER-CONDITIONAL>"
            "</CAN-CLUSTER-VARIANTS>",
            root_tag="CAN-CLUSTER",
        )
        parser.readCanCluster(element, cluster)
        assert cluster.getShortName() == "canCluster"

    def test_readCanCluster_sets_baudrate(self, parser):
        from armodel.models import CanCluster
        cluster = CanCluster(parent=_autosar_root(), short_name="c")
        element = _snip(
            "<SHORT-NAME>c</SHORT-NAME>"
            "<CAN-CLUSTER-VARIANTS>"
            "<CAN-CLUSTER-CONDITIONAL>"
            "<BAUDRATE>500000</BAUDRATE>"
            "</CAN-CLUSTER-CONDITIONAL>"
            "</CAN-CLUSTER-VARIANTS>",
            root_tag="CAN-CLUSTER",
        )
        parser.readCanCluster(element, cluster)
        assert cluster.getBaudrate() is not None

    def test_readCanCluster_sets_speed(self, parser):
        from armodel.models import CanCluster
        cluster = CanCluster(parent=_autosar_root(), short_name="c")
        element = _snip(
            "<SHORT-NAME>c</SHORT-NAME>"
            "<CAN-CLUSTER-VARIANTS>"
            "<CAN-CLUSTER-CONDITIONAL>"
            "<SPEED>100000</SPEED>"
            "</CAN-CLUSTER-CONDITIONAL>"
            "</CAN-CLUSTER-VARIANTS>",
            root_tag="CAN-CLUSTER",
        )
        parser.readCanCluster(element, cluster)
        assert cluster.getSpeed() is not None
        assert cluster.getSpeed().getValue() == 100000

    def test_readCanCluster_sets_canFdBaudrate(self, parser):
        from armodel.models import CanCluster
        cluster = CanCluster(parent=_autosar_root(), short_name="c")
        element = _snip(
            "<SHORT-NAME>c</SHORT-NAME>"
            "<CAN-CLUSTER-VARIANTS>"
            "<CAN-CLUSTER-CONDITIONAL>"
            "<CAN-FD-BAUDRATE>2000000</CAN-FD-BAUDRATE>"
            "</CAN-CLUSTER-CONDITIONAL>"
            "</CAN-CLUSTER-VARIANTS>",
            root_tag="CAN-CLUSTER",
        )
        parser.readCanCluster(element, cluster)
        assert cluster.getCanFdBaudrate() is not None
        assert cluster.getCanFdBaudrate().getValue() == 2000000

    def test_getCanClusterBusOffRecovery_sets_borTimeL1(self, parser):
        from armodel.models import CanClusterBusOffRecovery
        element = _snip(
            "<BUS-OFF-RECOVERY>"
            "<BOR-TIME-L-1>0.1</BOR-TIME-L-1>"
            "</BUS-OFF-RECOVERY>",
            root_tag="ROOT",
        )
        recovery = parser.getCanClusterBusOffRecovery(element, "BUS-OFF-RECOVERY")
        assert recovery is not None
        assert recovery.getBorTimeL1() is not None
        assert recovery.getBorTimeL1().getValue() == 0.1

    def test_getCanClusterBusOffRecovery_sets_borTimeL2(self, parser):
        from armodel.models import CanClusterBusOffRecovery
        element = _snip(
            "<BUS-OFF-RECOVERY>"
            "<BOR-TIME-L-2>0.2</BOR-TIME-L-2>"
            "</BUS-OFF-RECOVERY>",
            root_tag="ROOT",
        )
        recovery = parser.getCanClusterBusOffRecovery(element, "BUS-OFF-RECOVERY")
        assert recovery is not None
        assert recovery.getBorTimeL2() is not None
        assert recovery.getBorTimeL2().getValue() == 0.2

    def test_getCanClusterBusOffRecovery_sets_borCounterL1ToL2(self, parser):
        from armodel.models import CanClusterBusOffRecovery
        element = _snip(
            "<BUS-OFF-RECOVERY>"
            "<BOR-COUNTER-L-1-TO-L-2>10</BOR-COUNTER-L-1-TO-L-2>"
            "</BUS-OFF-RECOVERY>",
            root_tag="ROOT",
        )
        recovery = parser.getCanClusterBusOffRecovery(element, "BUS-OFF-RECOVERY")
        assert recovery is not None
        assert recovery.getBorCounterL1ToL2() is not None
        assert recovery.getBorCounterL1ToL2().getValue() == 10

    def test_readAbstractCanCluster_with_busOffRecovery(self, parser):
        from armodel.models import CanCluster
        cluster = CanCluster(parent=_autosar_root(), short_name="c")
        element = _snip(
            "<BUS-OFF-RECOVERY>"
            "<BOR-TIME-L-1>0.1</BOR-TIME-L-1>"
            "</BUS-OFF-RECOVERY>",
            root_tag="CAN-CLUSTER-CONDITIONAL",
        )
        parser.readAbstractCanCluster(element, cluster)
        assert cluster.getBusOffRecovery() is not None

    def test_readCommunicationClusterPhysicalChannels_canPhysical(
        self, parser
    ):
        from armodel.models import CanCluster
        cluster = CanCluster(parent=_autosar_root(), short_name="c")
        element = _snip(
            "<PHYSICAL-CHANNELS>"
            "<CAN-PHYSICAL-CHANNEL><SHORT-NAME>ch1</SHORT-NAME></CAN-PHYSICAL-CHANNEL>"
            "</PHYSICAL-CHANNELS>",
            root_tag="CAN-CLUSTER-CONDITIONAL",
        )
        parser.readCommunicationClusterPhysicalChannels(element, cluster)
        assert len(cluster.getPhysicalChannels()) == 1

    def test_readCommunicationClusterPhysicalChannels_unsupported_warns(
        self, warning_parser, caplog
    ):
        from armodel.models import CanCluster
        cluster = CanCluster(parent=_autosar_root(), short_name="c")
        element = _snip(
            "<PHYSICAL-CHANNELS><BAD/></PHYSICAL-CHANNELS>",
            root_tag="CAN-CLUSTER-CONDITIONAL",
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readCommunicationClusterPhysicalChannels(
                element, cluster
            )
        assert any("Unsupported Physical Channel" in r.getMessage() for r in caplog.records)

    def test_readCanPhysicalChannel_reads_channel(self, parser):
        from armodel.models import CanPhysicalChannel
        from armodel.models import CanCluster
        cluster = CanCluster(parent=_autosar_root(), short_name="c")
        channel = CanPhysicalChannel(parent=cluster, short_name="ch")
        element = _snip("<SHORT-NAME>ch</SHORT-NAME>", root_tag="CAN-PHYSICAL-CHANNEL")
        parser.readCanPhysicalChannel(element, channel)
        assert channel.getShortName() == "ch"

    def test_readCommunicationCluster_sets_protocol(self, parser):
        from armodel.models import CanCluster
        cluster = CanCluster(parent=_autosar_root(), short_name="c")
        element = _snip(
            "<PROTOCOL-NAME>CAN</PROTOCOL-NAME>"
            "<PROTOCOL-VERSION>2.0</PROTOCOL-VERSION>",
            root_tag="CAN-CLUSTER-CONDITIONAL",
        )
        parser.readCommunicationCluster(element, cluster)
        assert cluster.getProtocolName() is not None
        assert cluster.getProtocolName().getValue() == "CAN"
        assert cluster.getProtocolVersion() is not None
        assert cluster.getProtocolVersion().getValue() == "2.0"

    def test_readCanCluster_without_conditional_variant(self, parser):
        from armodel.models import CanCluster
        cluster = CanCluster(parent=_autosar_root(), short_name="c")
        element = _snip("<SHORT-NAME>c</SHORT-NAME>", root_tag="CAN-CLUSTER")
        parser.readCanCluster(element, cluster)
        assert cluster.getShortName() == "c"


class TestLinClusterHandlers:
    def test_readLinCluster_sets_short_name(self, parser):
        from armodel.models import LinCluster
        cluster = LinCluster(parent=_autosar_root(), short_name="linCluster")
        element = _snip(
            "<SHORT-NAME>linCluster</SHORT-NAME>"
            "<LIN-CLUSTER-VARIANTS>"
            "<LIN-CLUSTER-CONDITIONAL>"
            "<BAUDRATE>20000</BAUDRATE>"
            "</LIN-CLUSTER-CONDITIONAL>"
            "</LIN-CLUSTER-VARIANTS>",
            root_tag="LIN-CLUSTER",
        )
        parser.readLinCluster(element, cluster)
        assert cluster.getShortName() == "linCluster"

    def test_readLinCluster_sets_baudrate(self, parser):
        from armodel.models import LinCluster
        cluster = LinCluster(parent=_autosar_root(), short_name="l")
        element = _snip(
            "<SHORT-NAME>l</SHORT-NAME>"
            "<LIN-CLUSTER-VARIANTS>"
            "<LIN-CLUSTER-CONDITIONAL>"
            "<BAUDRATE>20000</BAUDRATE>"
            "</LIN-CLUSTER-CONDITIONAL>"
            "</LIN-CLUSTER-VARIANTS>",
            root_tag="LIN-CLUSTER",
        )
        parser.readLinCluster(element, cluster)
        assert cluster.getBaudrate() is not None
        assert cluster.getBaudrate().getValue() == 20000

    def test_readLinCluster_without_conditional_variant(self, parser):
        from armodel.models import LinCluster
        cluster = LinCluster(parent=_autosar_root(), short_name="l")
        element = _snip("<SHORT-NAME>l</SHORT-NAME>", root_tag="LIN-CLUSTER")
        parser.readLinCluster(element, cluster)
        assert cluster.getShortName() == "l"

    def test_readLinPhysicalChannel_reads_channel(self, parser):
        from armodel.models import LinPhysicalChannel
        from armodel.models import LinCluster
        cluster = LinCluster(parent=_autosar_root(), short_name="l")
        channel = LinPhysicalChannel(parent=cluster, short_name="ch")
        element = _snip("<SHORT-NAME>ch</SHORT-NAME>", root_tag="LIN-PHYSICAL-CHANNEL")
        parser.readLinPhysicalChannel(element, channel)
        assert channel.getShortName() == "ch"

    def test_readLinScheduleTable_sets_properties(self, parser):
        from armodel.models import LinScheduleTable
        from armodel.models import LinPhysicalChannel
        from armodel.models import LinCluster
        cluster = LinCluster(parent=_autosar_root(), short_name="l")
        channel = LinPhysicalChannel(parent=cluster, short_name="ch")
        table = LinScheduleTable(parent=channel, short_name="tbl")
        element = _snip(
            "<SHORT-NAME>tbl</SHORT-NAME>"
            "<RESUME-POSITION>enabled</RESUME-POSITION>"
            "<RUN-MODE>continuous</RUN-MODE>",
            root_tag="LIN-SCHEDULE-TABLE",
        )
        parser.readLinScheduleTable(element, table)
        assert table.getResumePosition() is not None
        assert table.getResumePosition().getValue() == "enabled"
        assert table.getRunMode() is not None
        assert table.getRunMode().getValue() == "continuous"

    def test_readLinPhysicalChannelScheduleTables_creates_table(self, parser):
        from armodel.models import LinPhysicalChannel
        from armodel.models import LinCluster
        cluster = LinCluster(parent=_autosar_root(), short_name="l")
        channel = LinPhysicalChannel(parent=cluster, short_name="ch")
        element = _snip(
            "<SCHEDULE-TABLES>"
            "<LIN-SCHEDULE-TABLE><SHORT-NAME>tbl</SHORT-NAME></LIN-SCHEDULE-TABLE>"
            "</SCHEDULE-TABLES>",
            root_tag="LIN-PHYSICAL-CHANNEL",
        )
        parser.readLinPhysicalChannelScheduleTables(element, channel)
        assert len(channel.getScheduleTables()) == 1

    def test_readLinPhysicalChannelScheduleTables_unsupported_warns(
        self, warning_parser, caplog
    ):
        from armodel.models import LinPhysicalChannel
        from armodel.models import LinCluster
        cluster = LinCluster(parent=_autosar_root(), short_name="l")
        channel = LinPhysicalChannel(parent=cluster, short_name="ch")
        element = _snip(
            "<SCHEDULE-TABLES><BAD/></SCHEDULE-TABLES>",
            root_tag="LIN-PHYSICAL-CHANNEL",
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readLinPhysicalChannelScheduleTables(element, channel)
        assert any("Unsupported Schedule Table" in r.getMessage() for r in caplog.records)

    def test_readLinFrameTriggering_sets_identifier(self, parser):
        from armodel.models import LinFrameTriggering
        from armodel.models import LinPhysicalChannel
        from armodel.models import LinCluster
        cluster = LinCluster(parent=_autosar_root(), short_name="l")
        channel = LinPhysicalChannel(parent=cluster, short_name="ch")
        triggering = LinFrameTriggering(parent=channel, short_name="ft")
        element = _snip(
            "<SHORT-NAME>ft</SHORT-NAME>"
            "<IDENTIFIER>1</IDENTIFIER>"
            "<LIN-CHECKSUM>enhanced</LIN-CHECKSUM>",
            root_tag="LIN-FRAME-TRIGGERING",
        )
        parser.readLinFrameTriggering(element, triggering)
        assert triggering.getIdentifier() is not None
        assert triggering.getIdentifier().getValue() == 1
        assert triggering.getLinChecksum() is not None
        assert triggering.getLinChecksum().getValue() == "enhanced"

    def test_getApplicationEntry_returns_entry(self, parser):
        from armodel.models import ApplicationEntry
        element = _snip(
            "<DELAY>0.01</DELAY>"
            "<POSITION-IN-TABLE>1</POSITION-IN-TABLE>"
            "<FRAME-TRIGGERING-REF DEST='FRAME-TRIGGERING'>/ft</FRAME-TRIGGERING-REF>",
            root_tag="APPLICATION-ENTRY",
        )
        entry = parser.getApplicationEntry(element, "APPLICATION-ENTRY")
        assert entry is not None
        assert entry.getDelay() is not None
        assert entry.getDelay().getValue() == 0.01


class TestFlexrayClusterHandlers:
    def test_readFlexrayCluster_sets_short_name(self, parser):
        from armodel.models import FlexrayCluster
        cluster = FlexrayCluster(parent=_autosar_root(), short_name="frCluster")
        element = _snip(
            "<SHORT-NAME>frCluster</SHORT-NAME>"
            "<FLEXRAY-CLUSTER-VARIANTS>"
            "<FLEXRAY-CLUSTER-CONDITIONAL>"
            "<BAUDRATE><VALUE>10000000</VALUE></BAUDRATE>"
            "</FLEXRAY-CLUSTER-CONDITIONAL>"
            "</FLEXRAY-CLUSTER-VARIANTS>",
            root_tag="FLEXRAY-CLUSTER",
        )
        parser.readFlexrayCluster(element, cluster)
        assert cluster.getShortName() == "frCluster"

    def test_readFlexrayCluster_sets_cycle(self, parser):
        from armodel.models import FlexrayCluster
        cluster = FlexrayCluster(parent=_autosar_root(), short_name="fr")
        element = _snip(
            "<SHORT-NAME>fr</SHORT-NAME>"
            "<FLEXRAY-CLUSTER-VARIANTS>"
            "<FLEXRAY-CLUSTER-CONDITIONAL>"
            "<CYCLE>0.005</CYCLE>"
            "</FLEXRAY-CLUSTER-CONDITIONAL>"
            "</FLEXRAY-CLUSTER-VARIANTS>",
            root_tag="FLEXRAY-CLUSTER",
        )
        parser.readFlexrayCluster(element, cluster)
        assert cluster.getCycle() is not None
        assert cluster.getCycle().getValue() == 0.005

    def test_readFlexrayCluster_sets_actionPointOffset(self, parser):
        from armodel.models import FlexrayCluster
        cluster = FlexrayCluster(parent=_autosar_root(), short_name="fr")
        element = _snip(
            "<SHORT-NAME>fr</SHORT-NAME>"
            "<FLEXRAY-CLUSTER-VARIANTS>"
            "<FLEXRAY-CLUSTER-CONDITIONAL>"
            "<ACTION-POINT-OFFSET>2</ACTION-POINT-OFFSET>"
            "</FLEXRAY-CLUSTER-CONDITIONAL>"
            "</FLEXRAY-CLUSTER-VARIANTS>",
            root_tag="FLEXRAY-CLUSTER",
        )
        parser.readFlexrayCluster(element, cluster)
        assert cluster.getActionPointOffset() is not None
        assert cluster.getActionPointOffset().getValue() == 2

    def test_readFlexrayCluster_sets_numberOfStaticSlots(self, parser):
        from armodel.models import FlexrayCluster
        cluster = FlexrayCluster(parent=_autosar_root(), short_name="fr")
        element = _snip(
            "<SHORT-NAME>fr</SHORT-NAME>"
            "<FLEXRAY-CLUSTER-VARIANTS>"
            "<FLEXRAY-CLUSTER-CONDITIONAL>"
            "<NUMBER-OF-STATIC-SLOTS>100</NUMBER-OF-STATIC-SLOTS>"
            "</FLEXRAY-CLUSTER-CONDITIONAL>"
            "</FLEXRAY-CLUSTER-VARIANTS>",
            root_tag="FLEXRAY-CLUSTER",
        )
        parser.readFlexrayCluster(element, cluster)
        assert cluster.getNumberOfStaticSlots() is not None
        assert cluster.getNumberOfStaticSlots().getValue() == 100

    def test_readFlexrayCluster_sets_detectNitError(self, parser):
        from armodel.models import FlexrayCluster
        cluster = FlexrayCluster(parent=_autosar_root(), short_name="fr")
        element = _snip(
            "<SHORT-NAME>fr</SHORT-NAME>"
            "<FLEXRAY-CLUSTER-VARIANTS>"
            "<FLEXRAY-CLUSTER-CONDITIONAL>"
            "<DETECT-NIT-ERROR>true</DETECT-NIT-ERROR>"
            "</FLEXRAY-CLUSTER-CONDITIONAL>"
            "</FLEXRAY-CLUSTER-VARIANTS>",
            root_tag="FLEXRAY-CLUSTER",
        )
        parser.readFlexrayCluster(element, cluster)
        assert cluster.getDetectNitError() is not None
        assert cluster.getDetectNitError().getValue() == True

    def test_readFlexrayPhysicalChannel_sets_channelName(self, parser):
        from armodel.models import FlexrayPhysicalChannel
        from armodel.models import FlexrayCluster
        cluster = FlexrayCluster(parent=_autosar_root(), short_name="fr")
        channel = FlexrayPhysicalChannel(parent=cluster, short_name="ch")
        element = _snip(
            "<SHORT-NAME>ch</SHORT-NAME>"
            "<CHANNEL-NAME>A</CHANNEL-NAME>",
            root_tag="FLEXRAY-PHYSICAL-CHANNEL",
        )
        parser.readFlexrayPhysicalChannel(element, channel)
        assert channel.getChannelName() is not None
        assert channel.getChannelName().getValue() == "A"

    def test_readFlexrayFrameTriggering_sets_messageId(self, parser):
        from armodel.models import FlexrayFrameTriggering
        from armodel.models import FlexrayPhysicalChannel
        from armodel.models import FlexrayCluster
        cluster = FlexrayCluster(parent=_autosar_root(), short_name="fr")
        channel = FlexrayPhysicalChannel(parent=cluster, short_name="ch")
        triggering = FlexrayFrameTriggering(parent=channel, short_name="ft")
        element = _snip(
            "<SHORT-NAME>ft</SHORT-NAME>"
            "<MESSAGE-ID>100</MESSAGE-ID>"
            "<ALLOW-DYNAMIC-L-SDU-LENGTH>true</ALLOW-DYNAMIC-L-SDU-LENGTH>",
            root_tag="FLEXRAY-FRAME-TRIGGERING",
        )
        parser.readFlexrayFrameTriggering(element, triggering)
        assert triggering.getMessageId() is not None
        assert triggering.getMessageId().getValue() == 100

    def test_readCycleRepetition_sets_baseCycle(self, parser):
        from armodel.models import CycleRepetition
        cycle = CycleRepetition()
        element = _snip(
            "<BASE-CYCLE>1</BASE-CYCLE>"
            "<CYCLE-REPETITION>1</CYCLE-REPETITION>",
            root_tag="CYCLE-REPETITION",
        )
        parser.readCycleRepetition(element, cycle)
        assert cycle.getBaseCycle() is not None
        assert cycle.getBaseCycle().getValue() == 1
        assert cycle.getCycleRepetition() is not None
        assert cycle.getCycleRepetition().getValue() == "1"

    def test_readFlexrayAbsolutelyScheduledTiming_sets_slotId(self, parser):
        from armodel.models import FlexrayAbsolutelyScheduledTiming
        timing = FlexrayAbsolutelyScheduledTiming()
        element = _snip(
            "<SLOT-ID>5</SLOT-ID>",
            root_tag="FLEXRAY-ABSOLUTELY-SCHEDULED-TIMING",
        )
        parser.readFlexrayAbsolutelyScheduledTiming(element, timing)
        assert timing.getSlotID() is not None
        assert timing.getSlotID().getValue() == 5

    def test_readFlexrayFrameTriggeringAbsolutelyScheduledTimings_creates_timing(
        self, parser
    ):
        from armodel.models import FlexrayFrameTriggering
        from armodel.models import FlexrayPhysicalChannel
        from armodel.models import FlexrayCluster
        cluster = FlexrayCluster(parent=_autosar_root(), short_name="fr")
        channel = FlexrayPhysicalChannel(parent=cluster, short_name="ch")
        triggering = FlexrayFrameTriggering(parent=channel, short_name="ft")
        element = _snip(
            "<ABSOLUTELY-SCHEDULED-TIMINGS>"
            "<FLEXRAY-ABSOLUTELY-SCHEDULED-TIMING>"
            "<SLOT-ID>5</SLOT-ID>"
            "</FLEXRAY-ABSOLUTELY-SCHEDULED-TIMING>"
            "</ABSOLUTELY-SCHEDULED-TIMINGS>",
            root_tag="FLEXRAY-FRAME-TRIGGERING",
        )
        parser.readFlexrayFrameTriggeringAbsolutelyScheduledTimings(
            element, triggering
        )
        assert len(triggering.getAbsolutelyScheduledTimings()) == 1


class TestEthernetClusterHandlers:
    def test_readEthernetCluster_sets_short_name(self, parser):
        from armodel.models import EthernetCluster
        cluster = EthernetCluster(parent=_autosar_root(), short_name="ethCluster")
        element = _snip(
            "<SHORT-NAME>ethCluster</SHORT-NAME>"
            "<ETHERNET-CLUSTER-VARIANTS>"
            "<ETHERNET-CLUSTER-CONDITIONAL>"
            "<BAUDRATE><VALUE>100000000</VALUE></BAUDRATE>"
            "</ETHERNET-CLUSTER-CONDITIONAL>"
            "</ETHERNET-CLUSTER-VARIANTS>",
            root_tag="ETHERNET-CLUSTER",
        )
        parser.readEthernetCluster(element, cluster)
        assert cluster.getShortName() == "ethCluster"

    def test_readEthernetCluster_sets_baudrate(self, parser):
        from armodel.models import EthernetCluster
        cluster = EthernetCluster(parent=_autosar_root(), short_name="eth")
        element = _snip(
            "<SHORT-NAME>eth</SHORT-NAME>"
            "<ETHERNET-CLUSTER-VARIANTS>"
            "<ETHERNET-CLUSTER-CONDITIONAL>"
            "<BAUDRATE>100000000</BAUDRATE>"
            "</ETHERNET-CLUSTER-CONDITIONAL>"
            "</ETHERNET-CLUSTER-VARIANTS>",
            root_tag="ETHERNET-CLUSTER",
        )
        parser.readEthernetCluster(element, cluster)
        assert cluster.getBaudrate() is not None
        assert cluster.getBaudrate().getValue() == 100000000

    def test_readEthernetClusterMacMulticastGroups_creates_group(self, parser):
        from armodel.models import EthernetCluster
        cluster = EthernetCluster(parent=_autosar_root(), short_name="eth")
        element = _snip(
            "<MAC-MULTICAST-GROUPS>"
            "<MAC-MULTICAST-GROUP>"
            "<SHORT-NAME>mcg</SHORT-NAME>"
            "<MAC-MULTICAST-ADDRESS>01:02:03:04:05:06</MAC-MULTICAST-ADDRESS>"
            "</MAC-MULTICAST-GROUP>"
            "</MAC-MULTICAST-GROUPS>",
            root_tag="ETHERNET-CLUSTER-CONDITIONAL",
        )
        parser.readEthernetClusterMacMulticastGroups(element, cluster)
        assert len(cluster.getMacMulticastGroups()) == 1

    def test_readEthernetClusterMacMulticastGroups_unsupported_warns(
        self, warning_parser, caplog
    ):
        from armodel.models import EthernetCluster
        cluster = EthernetCluster(parent=_autosar_root(), short_name="eth")
        element = _snip(
            "<MAC-MULTICAST-GROUPS><BAD/></MAC-MULTICAST-GROUPS>",
            root_tag="ETHERNET-CLUSTER-CONDITIONAL",
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readEthernetClusterMacMulticastGroups(element, cluster)
        assert any("Unsupported assigned data type" in r.getMessage() for r in caplog.records)

    def test_readMacMulticastGroup_sets_address(self, parser):
        from armodel.models import MacMulticastGroup
        from armodel.models import EthernetCluster
        cluster = EthernetCluster(parent=_autosar_root(), short_name="eth")
        group = MacMulticastGroup(parent=cluster, short_name="mcg")
        element = _snip(
            "<SHORT-NAME>mcg</SHORT-NAME>"
            "<MAC-MULTICAST-ADDRESS>01:02:03:04:05:06</MAC-MULTICAST-ADDRESS>",
            root_tag="MAC-MULTICAST-GROUP",
        )
        parser.readMacMulticastGroup(element, group)
        assert group.getMacMulticastAddress() is not None
        assert group.getMacMulticastAddress().getValue() == "01:02:03:04:05:06"

    def test_readEthernetPhysicalChannel_reads_channel(self, parser):
        from armodel.models import EthernetPhysicalChannel
        from armodel.models import EthernetCluster
        cluster = EthernetCluster(parent=_autosar_root(), short_name="eth")
        channel = EthernetPhysicalChannel(parent=cluster, short_name="ch")
        element = _snip("<SHORT-NAME>ch</SHORT-NAME>", root_tag="ETHERNET-PHYSICAL-CHANNEL")
        parser.readEthernetPhysicalChannel(element, channel)
        assert channel.getShortName() == "ch"

    def test_readEthernetPhysicalChannelVlan_creates_vlan(self, parser):
        from armodel.models import EthernetPhysicalChannel
        from armodel.models import EthernetCluster
        cluster = EthernetCluster(parent=_autosar_root(), short_name="eth")
        channel = EthernetPhysicalChannel(parent=cluster, short_name="ch")
        element = _snip(
            "<VLAN>"
            "<SHORT-NAME>vlan1</SHORT-NAME>"
            "<VLAN-IDENTIFIER>100</VLAN-IDENTIFIER>"
            "</VLAN>",
            root_tag="ETHERNET-PHYSICAL-CHANNEL",
        )
        parser.readEthernetPhysicalChannelVlan(element, channel)
        assert channel.getVlan() is not None

    def test_readEthernetPhysicalChannelNetworkEndPoints_creates_endpoint(
        self, parser
    ):
        from armodel.models import EthernetPhysicalChannel
        from armodel.models import EthernetCluster
        cluster = EthernetCluster(parent=_autosar_root(), short_name="eth")
        channel = EthernetPhysicalChannel(parent=cluster, short_name="ch")
        element = _snip(
            "<NETWORK-ENDPOINTS>"
            "<NETWORK-ENDPOINT>"
            "<SHORT-NAME>ne1</SHORT-NAME>"
            "<PRIORITY>1</PRIORITY>"
            "</NETWORK-ENDPOINT>"
            "</NETWORK-ENDPOINTS>",
            root_tag="ETHERNET-PHYSICAL-CHANNEL",
        )
        parser.readEthernetPhysicalChannelNetworkEndPoints(element, channel)
        assert len(channel.getNetworkEndpoints()) == 1

    def test_readNetworkEndPoint_sets_priority(self, parser):
        from armodel.models import NetworkEndpoint
        from armodel.models import EthernetPhysicalChannel
        from armodel.models import EthernetCluster
        cluster = EthernetCluster(parent=_autosar_root(), short_name="eth")
        channel = EthernetPhysicalChannel(parent=cluster, short_name="ch")
        endpoint = NetworkEndpoint(parent=channel, short_name="ne")
        element = _snip(
            "<SHORT-NAME>ne</SHORT-NAME>"
            "<PRIORITY>1</PRIORITY>",
            root_tag="NETWORK-ENDPOINT",
        )
        parser.readNetworkEndPoint(element, endpoint)
        assert endpoint.getPriority() is not None
        assert endpoint.getPriority().getValue() == 1

    def test_getIpv6Configuration_sets_ipv6Address(self, parser):
        element = _snip(
            "<IPV-6-ADDRESS>fe80::1</IPV-6-ADDRESS>"
            "<IPV-6-ADDRESS-SOURCE>manual</IPV-6-ADDRESS-SOURCE>"
            "<IP-ADDRESS-PREFIX-LENGTH>64</IP-ADDRESS-PREFIX-LENGTH>",
            root_tag="IPV-6-CONFIGURATION",
        )
        config = parser.getIpv6Configuration(element)
        assert config is not None
        assert config.getIpv6Address() is not None
        assert config.getIpv6Address().getValue() == "fe80::1"

    def test_readNetworkEndPointNetworkEndPointAddress_adds_ipv6(self, parser):
        from armodel.models import NetworkEndpoint
        from armodel.models import EthernetPhysicalChannel
        from armodel.models import EthernetCluster
        cluster = EthernetCluster(parent=_autosar_root(), short_name="eth")
        channel = EthernetPhysicalChannel(parent=cluster, short_name="ch")
        endpoint = NetworkEndpoint(parent=channel, short_name="ne")
        element = _snip(
            "<NETWORK-ENDPOINT-ADDRESSES>"
            "<IPV-6-CONFIGURATION>"
            "<IPV-6-ADDRESS>fe80::1</IPV-6-ADDRESS>"
            "</IPV-6-CONFIGURATION>"
            "</NETWORK-ENDPOINT-ADDRESSES>",
            root_tag="NETWORK-ENDPOINT",
        )
        parser.readNetworkEndPointNetworkEndPointAddress(element, endpoint)
        assert len(endpoint.getNetworkEndpointAddresses()) == 1

    def test_getDoIpEntity_sets_role(self, parser):
        element = _snip(
            "<DO-IP-ENTITY>"
            "<DO-IP-ENTITY-ROLE>server</DO-IP-ENTITY-ROLE>"
            "</DO-IP-ENTITY>",
            root_tag="INFRASTRUCTURE-SERVICES",
        )
        services = parser.getInfrastructureServices(element, "INFRASTRUCTURE-SERVICES")
        assert services is not None
        assert services.getDoIpEntity() is not None
        assert services.getDoIpEntity().getDoIpEntityRole() is not None
        assert services.getDoIpEntity().getDoIpEntityRole().getValue() == "server"

    def test_readEthernetPhysicalChannel_sets_soAdConfig(self, parser):
        from armodel.models import EthernetPhysicalChannel
        from armodel.models import EthernetCluster
        cluster = EthernetCluster(parent=_autosar_root(), short_name="eth")
        channel = EthernetPhysicalChannel(parent=cluster, short_name="ch")
        element = _snip(
            "<SHORT-NAME>ch</SHORT-NAME>"
            "<SO-AD-CONFIG>"
            "<CONNECTION-BUNDLES></CONNECTION-BUNDLES>"
            "<SOCKET-ADDRESSS></SOCKET-ADDRESSS>"
            "</SO-AD-CONFIG>",
            root_tag="ETHERNET-PHYSICAL-CHANNEL",
        )
        parser.readEthernetPhysicalChannel(element, channel)
        assert channel.getSoAdConfig() is not None

    def test_readEthernetCluster_without_conditional_variant(self, parser):
        from armodel.models import EthernetCluster
        cluster = EthernetCluster(parent=_autosar_root(), short_name="eth")
        element = _snip("<SHORT-NAME>eth</SHORT-NAME>", root_tag="ETHERNET-CLUSTER")
        parser.readEthernetCluster(element, cluster)
        assert cluster.getShortName() == "eth"

    def test_readEthernetPhysicalChannelNetworkEndPoints_unsupported_warns(
        self, warning_parser, caplog
    ):
        from armodel.models import EthernetPhysicalChannel
        from armodel.models import EthernetCluster
        cluster = EthernetCluster(parent=_autosar_root(), short_name="eth")
        channel = EthernetPhysicalChannel(parent=cluster, short_name="ch")
        element = _snip(
            "<NETWORK-ENDPOINT-ADDRESSES><BAD/></NETWORK-ENDPOINT-ADDRESSES>",
            root_tag="NETWORK-ENDPOINT",
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readNetworkEndPointNetworkEndPointAddress(element, channel)
        assert any("Unsupported Network EndPoint Address" in r.getMessage() for r in caplog.records)


class TestSoAdAndSocketHandlers:
    def test_getSoAdConfig_returns_config(self, parser):
        element = _snip(
            "<SO-AD-CONFIG>"
            "<CONNECTION-BUNDLES></CONNECTION-BUNDLES>"
            "<SOCKET-ADDRESSS></SOCKET-ADDRESSS>"
            "</SO-AD-CONFIG>",
            root_tag="ROOT",
        )
        config = parser.getSoAdConfig(element, "SO-AD-CONFIG")
        assert config is not None

    def test_readSoAdConfigSocketAddresses_creates_address(self, parser):
        from armodel.models import SoAdConfig
        config = SoAdConfig()
        element = _snip(
            "<SOCKET-ADDRESSS>"
            "<SOCKET-ADDRESS>"
            "<SHORT-NAME>sa1</SHORT-NAME>"
            "<PORT-ADDRESS>5000</PORT-ADDRESS>"
            "</SOCKET-ADDRESS>"
            "</SOCKET-ADDRESSS>",
            root_tag="SO-AD-CONFIG",
        )
        parser.readSoAdConfigSocketAddresses(element, config)
        assert len(config.getSocketAddresses()) == 1

    def test_readSoAdConfigSocketAddresses_unsupported_warns(
        self, warning_parser, caplog
    ):
        from armodel.models import SoAdConfig
        config = SoAdConfig()
        element = _snip(
            "<SOCKET-ADDRESSS><BAD/></SOCKET-ADDRESSS>",
            root_tag="SO-AD-CONFIG",
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readSoAdConfigSocketAddresses(element, config)
        assert any("Unsupported Socket Address" in r.getMessage() for r in caplog.records)

    def test_readSocketAddress_sets_portAddress(self, parser):
        from armodel.models import SocketAddress
        from armodel.models import SoAdConfig
        config = SoAdConfig()
        address = SocketAddress(parent=config, short_name="sa")
        element = _snip(
            "<SHORT-NAME>sa</SHORT-NAME>"
            "<PORT-ADDRESS>5000</PORT-ADDRESS>",
            root_tag="SOCKET-ADDRESS",
        )
        parser.readSocketAddress(element, address)
        assert address.getPortAddress() is not None
        assert address.getPortAddress().getValue() == 5000

    def test_readSocketAddressApplicationEndpoint_creates_endpoint(self, parser):
        from armodel.models import SocketAddress
        from armodel.models import SoAdConfig
        config = SoAdConfig()
        address = SocketAddress(parent=config, short_name="sa")
        element = _snip(
            "<APPLICATION-ENDPOINT>"
            "<SHORT-NAME>ae1</SHORT-NAME>"
            "<PRIORITY>1</PRIORITY>"
            "</APPLICATION-ENDPOINT>",
            root_tag="SOCKET-ADDRESS",
        )
        parser.readSocketAddressApplicationEndpoint(element, address)
        assert len(address.getApplicationEndpoint()) == 1

    def test_readSocketAddressMulticastConnectorRefs_adds_ref(self, parser):
        from armodel.models import SocketAddress
        from armodel.models import SoAdConfig
        config = SoAdConfig()
        address = SocketAddress(parent=config, short_name="sa")
        element = _snip(
            "<MULTICAST-CONNECTOR-REFS>"
            "<MULTICAST-CONNECTOR-REF DEST='COMMUNICATION-CONNECTOR'>/mc</MULTICAST-CONNECTOR-REF>"
            "</MULTICAST-CONNECTOR-REFS>",
            root_tag="SOCKET-ADDRESS",
        )
        parser.readSocketAddressMulticastConnectorRefs(element, address)
        assert len(address.getMulticastConnectorRefs()) == 1

    def test_readConsumedServiceInstanceConsumedEventGroups_creates_group(
        self, parser
    ):
        from armodel.models import ConsumedServiceInstance
        from armodel.models import ApplicationEndpoint
        from armodel.models import SocketAddress
        from armodel.models import SoAdConfig
        config = SoAdConfig()
        address = SocketAddress(parent=config, short_name="sa")
        endpoint = ApplicationEndpoint(parent=address, short_name="ae")
        instance = ConsumedServiceInstance(parent=endpoint, short_name="csi")
        element = _snip(
            "<CONSUMED-EVENT-GROUPS>"
            "<CONSUMED-EVENT-GROUP>"
            "<SHORT-NAME>ceg</SHORT-NAME>"
            "<EVENT-GROUP-IDENTIFIER>1</EVENT-GROUP-IDENTIFIER>"
            "</CONSUMED-EVENT-GROUP>"
            "</CONSUMED-EVENT-GROUPS>",
            root_tag="CONSUMED-SERVICE-INSTANCE",
        )
        parser.readConsumedServiceInstanceConsumedEventGroups(element, instance)
        assert len(instance.getConsumedEventGroups()) == 1

    def test_readConsumedEventGroup_sets_eventGroupIdentifier(self, parser):
        from armodel.models import ConsumedEventGroup
        from armodel.models import ConsumedServiceInstance
        from armodel.models import ApplicationEndpoint
        from armodel.models import SocketAddress
        from armodel.models import SoAdConfig
        config = SoAdConfig()
        address = SocketAddress(parent=config, short_name="sa")
        endpoint = ApplicationEndpoint(parent=address, short_name="ae")
        instance = ConsumedServiceInstance(parent=endpoint, short_name="csi")
        group = ConsumedEventGroup(parent=instance, short_name="ceg")
        element = _snip(
            "<SHORT-NAME>ceg</SHORT-NAME>"
            "<EVENT-GROUP-IDENTIFIER>1</EVENT-GROUP-IDENTIFIER>",
            root_tag="CONSUMED-EVENT-GROUP",
        )
        parser.readConsumedEventGroup(element, group)
        assert group.getEventGroupIdentifier() is not None
        assert group.getEventGroupIdentifier().getValue() == 1

    def test_readConsumedEventGroupRoutingGroupRefs_adds_ref(self, parser):
        from armodel.models import ConsumedEventGroup
        from armodel.models import ConsumedServiceInstance
        from armodel.models import ApplicationEndpoint
        from armodel.models import SocketAddress
        from armodel.models import SoAdConfig
        config = SoAdConfig()
        address = SocketAddress(parent=config, short_name="sa")
        endpoint = ApplicationEndpoint(parent=address, short_name="ae")
        instance = ConsumedServiceInstance(parent=endpoint, short_name="csi")
        group = ConsumedEventGroup(parent=instance, short_name="ceg")
        element = _snip(
            "<ROUTING-GROUP-REFS>"
            "<ROUTING-GROUP-REF DEST='SO-AD-ROUTING-GROUP'>/rg</ROUTING-GROUP-REF>"
            "</ROUTING-GROUP-REFS>",
            root_tag="CONSUMED-EVENT-GROUP",
        )
        parser.readConsumedEventGroupRoutingGroupRefs(element, group)
        assert len(group.getRoutingGroupRefs()) == 1

    def test_getSdClientConfig_sets_ttl(self, parser):
        element = _snip(
            "<SD-CLIENT-CONFIG>"
            "<TTL>3600</TTL>"
            "</SD-CLIENT-CONFIG>",
            root_tag="ROOT",
        )
        config = parser.getSdClientConfig(element, "SD-CLIENT-CONFIG")
        assert config is not None
        assert config.getTtl() is not None
        assert config.getTtl().getValue() == 3600

    def test_getSdServerConfig_sets_ttl(self, parser):
        element = _snip(
            "<SD-SERVER-CONFIG>"
            "<TTL>3600</TTL>"
            "</SD-SERVER-CONFIG>",
            root_tag="ROOT",
        )
        config = parser.getSdServerConfig(element, "SD-SERVER-CONFIG")
        assert config is not None
        assert config.getTtl() is not None
        assert config.getTtl().getValue() == 3600

    def test_readProvidedServiceInstanceEventHandlers_creates_handler(
        self, parser
    ):
        from armodel.models import ProvidedServiceInstance
        from armodel.models import ApplicationEndpoint
        from armodel.models import SocketAddress
        from armodel.models import SoAdConfig
        config = SoAdConfig()
        address = SocketAddress(parent=config, short_name="sa")
        endpoint = ApplicationEndpoint(parent=address, short_name="ae")
        instance = ProvidedServiceInstance(parent=endpoint, short_name="psi")
        element = _snip(
            "<EVENT-HANDLERS>"
            "<EVENT-HANDLER>"
            "<SHORT-NAME>eh</SHORT-NAME>"
            "<MULTICAST-THRESHOLD>10</MULTICAST-THRESHOLD>"
            "</EVENT-HANDLER>"
            "</EVENT-HANDLERS>",
            root_tag="PROVIDED-SERVICE-INSTANCE",
        )
        parser.readProvidedServiceInstanceEventHandlers(element, instance)
        assert len(instance.getEventHandlers()) == 1

    def test_readEventHandler_sets_multicastThreshold(self, parser):
        from armodel.models import EventHandler
        from armodel.models import ProvidedServiceInstance
        from armodel.models import ApplicationEndpoint
        from armodel.models import SocketAddress
        from armodel.models import SoAdConfig
        config = SoAdConfig()
        address = SocketAddress(parent=config, short_name="sa")
        endpoint = ApplicationEndpoint(parent=address, short_name="ae")
        instance = ProvidedServiceInstance(parent=endpoint, short_name="psi")
        handler = EventHandler(parent=instance, short_name="eh")
        element = _snip(
            "<SHORT-NAME>eh</SHORT-NAME>"
            "<MULTICAST-THRESHOLD>10</MULTICAST-THRESHOLD>",
            root_tag="EVENT-HANDLER",
        )
        parser.readEventHandler(element, handler)
        assert handler.getMulticastThreshold() is not None
        assert handler.getMulticastThreshold().getValue() == 10

    def test_readProvidedServiceInstance_sets_serviceIdentifier(self, parser):
        from armodel.models import ProvidedServiceInstance
        from armodel.models import ApplicationEndpoint
        from armodel.models import SocketAddress
        from armodel.models import SoAdConfig
        config = SoAdConfig()
        address = SocketAddress(parent=config, short_name="sa")
        endpoint = ApplicationEndpoint(parent=address, short_name="ae")
        instance = ProvidedServiceInstance(parent=endpoint, short_name="psi")
        element = _snip(
            "<SHORT-NAME>psi</SHORT-NAME>"
            "<SERVICE-IDENTIFIER>1234</SERVICE-IDENTIFIER>"
            "<INSTANCE-IDENTIFIER>1</INSTANCE-IDENTIFIER>",
            root_tag="PROVIDED-SERVICE-INSTANCE",
        )
        parser.readProvidedServiceInstance(element, instance)
        assert instance.getServiceIdentifier() is not None
        assert instance.getServiceIdentifier().getValue() == 1234

    def test_readSoAdConfigConnectionBundles_creates_bundle(self, parser):
        from armodel.models import SoAdConfig
        config = SoAdConfig()
        element = _snip(
            "<CONNECTION-BUNDLES>"
            "<SOCKET-CONNECTION-BUNDLE>"
            "<SHORT-NAME>scb</SHORT-NAME>"
            "</SOCKET-CONNECTION-BUNDLE>"
            "</CONNECTION-BUNDLES>",
            root_tag="SO-AD-CONFIG",
        )
        parser.readSoAdConfigConnectionBundles(element, config)
        assert len(config.getConnectionBundles()) == 1

    def test_readSocketConnectionBundleConnections_creates_connection(self, parser):
        from armodel.models import SocketConnectionBundle
        from armodel.models import SoAdConfig
        config = SoAdConfig()
        bundle = config.createSocketConnectionBundle("scb")
        element = _snip(
            "<BUNDLED-CONNECTIONS>"
            "<SOCKET-CONNECTION>"
            "<SHORT-LABEL>conn1</SHORT-LABEL>"
            "</SOCKET-CONNECTION>"
            "</BUNDLED-CONNECTIONS>",
            root_tag="SOCKET-CONNECTION-BUNDLE",
        )
        parser.readSocketConnectionBundleConnections(element, bundle)
        assert len(bundle.getBundledConnections()) == 1

    def test_getSocketConnection_sets_shortLabel(self, parser):
        element = _snip(
            "<SHORT-LABEL>conn1</SHORT-LABEL>",
            root_tag="SOCKET-CONNECTION",
        )
        conn = parser.getSocketConnection(element)
        assert conn is not None
        assert conn.getShortLabel() is not None
        assert conn.getShortLabel().getValue() == "conn1"

    def test_getSocketConnectionIpduIdentifier_sets_headerId(self, parser):
        element = _snip(
            "<HEADER-ID>100</HEADER-ID>"
            "<PDU-REF DEST='I-PDU'>/pdu</PDU-REF>",
            root_tag="SOCKET-CONNECTION-IPDU-IDENTIFIER",
        )
        ident = parser.getSocketConnectionIpduIdentifier(element)
        assert ident is not None
        assert ident.getHeaderId() is not None
        assert ident.getHeaderId().getValue() == 100

    def test_getSocketConnectionPdus_returns_list(self, parser):
        element = _snip(
            "<PDUS>"
            "<SOCKET-CONNECTION-IPDU-IDENTIFIER>"
            "<HEADER-ID>100</HEADER-ID>"
            "</SOCKET-CONNECTION-IPDU-IDENTIFIER>"
            "</PDUS>",
            root_tag="SOCKET-CONNECTION",
        )
        pdus = parser.getSocketConnectionPdus(element)
        assert len(pdus) == 1

    def test_readConsumedServiceInstanceConsumedEventGroups_unsupported_warns(
        self, warning_parser, caplog
    ):
        from armodel.models import ConsumedServiceInstance
        from armodel.models import ApplicationEndpoint
        from armodel.models import SocketAddress
        from armodel.models import SoAdConfig
        config = SoAdConfig()
        address = SocketAddress(parent=config, short_name="sa")
        endpoint = ApplicationEndpoint(parent=address, short_name="ae")
        instance = ConsumedServiceInstance(parent=endpoint, short_name="csi")
        element = _snip(
            "<CONSUMED-EVENT-GROUPS><BAD/></CONSUMED-EVENT-GROUPS>",
            root_tag="CONSUMED-SERVICE-INSTANCE",
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readConsumedServiceInstanceConsumedEventGroups(
                element, instance
            )
        assert any("Unsupported ConsumedEventGroups" in r.getMessage() for r in caplog.records)

    def test_getInitialSdDelayConfig_sets_initialDelayMaxValue(self, parser):
        element = _snip(
            "<INITIAL-DELAY-MAX-VALUE>0.1</INITIAL-DELAY-MAX-VALUE>"
            "<INITIAL-DELAY-MIN-VALUE>0.01</INITIAL-DELAY-MIN-VALUE>"
            "<INITIAL-REPETITIONS-BASE-DELAY>0.05</INITIAL-REPETITIONS-BASE-DELAY>"
            "<INITIAL-REPETITIONS-MAX>3</INITIAL-REPETITIONS-MAX>",
            root_tag="INITIAL-FIND-BEHAVIOR",
        )
        config = parser.getInitialSdDelayConfig(element, "INITIAL-FIND-BEHAVIOR")
        assert config is not None
        assert config.getInitialDelayMaxValue() is not None
        assert config.getInitialDelayMaxValue().getValue() == 0.1

    def test_getRequestResponseDelay_sets_maxValue(self, parser):
        element = _snip(
            "<MAX-VALUE>0.1</MAX-VALUE>"
            "<MIN-VALUE>0.01</MIN-VALUE>",
            root_tag="REQUEST-RESPONSE-DELAY",
        )
        delay = parser.getRequestResponseDelay(element, "REQUEST-RESPONSE-DELAY")
        assert delay is not None
        assert delay.getMaxValue() is not None
        assert delay.getMaxValue().getValue() == 0.1


class TestTransportProtocolHandlers:
    def test_getTpPort_sets_portNumber(self, parser):
        element = _snip(
            "<TP-PORT>"
            "<PORT-NUMBER>5000</PORT-NUMBER>"
            "<DYNAMICALLY-ASSIGNED>true</DYNAMICALLY-ASSIGNED>"
            "</TP-PORT>",
            root_tag="ROOT",
        )
        port = parser.getTpPort(element, "TP-PORT")
        assert port is not None
        assert port.getPortNumber() is not None
        assert port.getPortNumber().getValue() == 5000

    def test_readUdpTp_sets_udpTpPort(self, parser):
        from armodel.models import UdpTp
        tp = UdpTp()
        element = _snip(
            "<UDP-TP-PORT>"
            "<PORT-NUMBER>5000</PORT-NUMBER>"
            "</UDP-TP-PORT>",
            root_tag="UDP-TP",
        )
        parser.readUdpTp(element, tp)
        assert tp.getUdpTpPort() is not None
        assert tp.getUdpTpPort().getPortNumber() is not None
        assert tp.getUdpTpPort().getPortNumber().getValue() == 5000

    def test_readTcpTp_sets_tcpTpPort(self, parser):
        from armodel.models import TcpTp
        tp = TcpTp()
        element = _snip(
            "<TCP-TP-PORT>"
            "<PORT-NUMBER>5000</PORT-NUMBER>"
            "</TCP-TP-PORT>"
            "<KEEP-ALIVES>true</KEEP-ALIVES>"
            "<NAGLES-ALGORITHM>enabled</NAGLES-ALGORITHM>",
            root_tag="TCP-TP",
        )
        parser.readTcpTp(element, tp)
        assert tp.getTcpTpPort() is not None
        assert tp.getTcpTpPort().getPortNumber() is not None
        assert tp.getTcpTpPort().getPortNumber().getValue() == 5000

    def test_readTcpTp_sets_keepAlives(self, parser):
        from armodel.models import TcpTp
        tp = TcpTp()
        element = _snip(
            "<KEEP-ALIVES>true</KEEP-ALIVES>"
            "<TCP-TP-PORT></TCP-TP-PORT>",
            root_tag="TCP-TP",
        )
        parser.readTcpTp(element, tp)
        assert tp.getKeepAlives() is not None
        assert tp.getKeepAlives().getValue() == True

    def test_readTcpTp_sets_keepAliveTime(self, parser):
        from armodel.models import TcpTp
        tp = TcpTp()
        element = _snip(
            "<KEEP-ALIVE-TIME>30</KEEP-ALIVE-TIME>"
            "<TCP-TP-PORT></TCP-TP-PORT>",
            root_tag="TCP-TP",
        )
        parser.readTcpTp(element, tp)
        assert tp.getKeepAliveTime() is not None
        assert tp.getKeepAliveTime().getValue() == 30

    def test_readGenericTp_sets_tpTechnology(self, parser):
        from armodel.models import GenericTp
        tp = GenericTp()
        element = _snip(
            "<TP-TECHNOLOGY>UDP</TP-TECHNOLOGY>"
            "<TP-ADDRESS>192.168.1.1</TP-ADDRESS>",
            root_tag="GENERIC-TP",
        )
        parser.readGenericTp(element, tp)
        assert tp.getTpTechnology() is not None
        assert tp.getTpTechnology().getValue() == "UDP"

    def test_getTransportProtocolConfiguration_udp(self, parser):
        element = _snip(
            "<TP-CONFIGURATION>"
            "<UDP-TP>"
            "<UDP-TP-PORT><PORT-NUMBER>5000</PORT-NUMBER></UDP-TP-PORT>"
            "</UDP-TP>"
            "</TP-CONFIGURATION>",
            root_tag="ROOT",
        )
        config = parser.getTransportProtocolConfiguration(
            element, "TP-CONFIGURATION"
        )
        assert config is not None

    def test_getTransportProtocolConfiguration_tcp(self, parser):
        element = _snip(
            "<TP-CONFIGURATION>"
            "<TCP-TP>"
            "<TCP-TP-PORT><PORT-NUMBER>5000</PORT-NUMBER></TCP-TP-PORT>"
            "</TCP-TP>"
            "</TP-CONFIGURATION>",
            root_tag="ROOT",
        )
        config = parser.getTransportProtocolConfiguration(
            element, "TP-CONFIGURATION"
        )
        assert config is not None

    def test_getTransportProtocolConfiguration_generic(self, parser):
        element = _snip(
            "<TP-CONFIGURATION>"
            "<GENERIC-TP>"
            "<TP-TECHNOLOGY>UDP</TP-TECHNOLOGY>"
            "</GENERIC-TP>"
            "</TP-CONFIGURATION>",
            root_tag="ROOT",
        )
        config = parser.getTransportProtocolConfiguration(
            element, "TP-CONFIGURATION"
        )
        assert config is not None

    def test_getTransportProtocolConfiguration_unsupported_warns(
        self, warning_parser, caplog
    ):
        element = _snip(
            "<TP-CONFIGURATION><BAD/></TP-CONFIGURATION>",
            root_tag="ROOT",
        )
        with caplog.at_level(logging.ERROR):
            config = warning_parser.getTransportProtocolConfiguration(
                element, "TP-CONFIGURATION"
            )
        assert config is None
        assert any("Unsupported TransportProtocolConfiguration" in r.getMessage() for r in caplog.records)


class TestFrameAndPduHandlers:
    def test_readFrameTriggering_sets_frameRef(self, parser):
        from armodel.models import CanFrameTriggering
        from armodel.models import CanPhysicalChannel
        from armodel.models import CanCluster
        cluster = CanCluster(parent=_autosar_root(), short_name="c")
        channel = CanPhysicalChannel(parent=cluster, short_name="ch")
        triggering = CanFrameTriggering(parent=channel, short_name="ft")
        element = _snip(
            "<SHORT-NAME>ft</SHORT-NAME>"
            "<FRAME-REF DEST='FRAME'>/frame</FRAME-REF>",
            root_tag="CAN-FRAME-TRIGGERING",
        )
        parser.readFrameTriggering(element, triggering)
        assert triggering.getFrameRef().getValue() == "/frame"

    def test_readFrameTriggering_adds_framePortRefs(self, parser):
        from armodel.models import CanFrameTriggering
        from armodel.models import CanPhysicalChannel
        from armodel.models import CanCluster
        cluster = CanCluster(parent=_autosar_root(), short_name="c")
        channel = CanPhysicalChannel(parent=cluster, short_name="ch")
        triggering = CanFrameTriggering(parent=channel, short_name="ft")
        element = _snip(
            "<SHORT-NAME>ft</SHORT-NAME>"
            "<FRAME-PORT-REFS>"
            "<FRAME-PORT-REF DEST='FRAME-PORT'>/fp</FRAME-PORT-REF>"
            "</FRAME-PORT-REFS>",
            root_tag="CAN-FRAME-TRIGGERING",
        )
        parser.readFrameTriggering(element, triggering)
        assert len(triggering.getFramePortRefs()) == 1

    def test_readCanFrameTriggering_sets_canAddressingMode(self, parser):
        from armodel.models import CanFrameTriggering
        from armodel.models import CanPhysicalChannel
        from armodel.models import CanCluster
        cluster = CanCluster(parent=_autosar_root(), short_name="c")
        channel = CanPhysicalChannel(parent=cluster, short_name="ch")
        triggering = CanFrameTriggering(parent=channel, short_name="ft")
        element = _snip(
            "<SHORT-NAME>ft</SHORT-NAME>"
            "<CAN-ADDRESSING-MODE>standard</CAN-ADDRESSING-MODE>"
            "<IDENTIFIER><VALUE>100</VALUE></IDENTIFIER>",
            root_tag="CAN-FRAME-TRIGGERING",
        )
        parser.readCanFrameTriggering(element, triggering)
        assert triggering.getCanAddressingMode() is not None
        assert triggering.getCanAddressingMode().getValue() == "standard"

    def test_readCanFrameTriggering_sets_canFdFrameSupport(self, parser):
        from armodel.models import CanFrameTriggering
        from armodel.models import CanPhysicalChannel
        from armodel.models import CanCluster
        cluster = CanCluster(parent=_autosar_root(), short_name="c")
        channel = CanPhysicalChannel(parent=cluster, short_name="ch")
        triggering = CanFrameTriggering(parent=channel, short_name="ft")
        element = _snip(
            "<SHORT-NAME>ft</SHORT-NAME>"
            "<CAN-FD-FRAME-SUPPORT>true</CAN-FD-FRAME-SUPPORT>",
            root_tag="CAN-FRAME-TRIGGERING",
        )
        parser.readCanFrameTriggering(element, triggering)
        assert triggering.getCanFdFrameSupport() is not None
        assert triggering.getCanFdFrameSupport().getValue() == True

    def test_readCanFrameTriggering_sets_identifier(self, parser):
        from armodel.models import CanFrameTriggering
        from armodel.models import CanPhysicalChannel
        from armodel.models import CanCluster
        cluster = CanCluster(parent=_autosar_root(), short_name="c")
        channel = CanPhysicalChannel(parent=cluster, short_name="ch")
        triggering = CanFrameTriggering(parent=channel, short_name="ft")
        element = _snip(
            "<SHORT-NAME>ft</SHORT-NAME>"
            "<IDENTIFIER><VALUE>100</VALUE></IDENTIFIER>",
            root_tag="CAN-FRAME-TRIGGERING",
        )
        parser.readCanFrameTriggering(element, triggering)
        assert triggering.getIdentifier() is not None
        assert triggering.getIdentifier().getValue() == 100

    def test_readPduTriggering_sets_ipduRef(self, parser):
        from armodel.models import PduTriggering
        from armodel.models import CanPhysicalChannel
        from armodel.models import CanCluster
        cluster = CanCluster(parent=_autosar_root(), short_name="c")
        channel = CanPhysicalChannel(parent=cluster, short_name="ch")
        triggering = PduTriggering(parent=channel, short_name="pt")
        element = _snip(
            "<SHORT-NAME>pt</SHORT-NAME>"
            "<I-PDU-REF DEST='I-PDU'>/pdu</I-PDU-REF>",
            root_tag="PDU-TRIGGERING",
        )
        parser.readPduTriggering(element, triggering)
        assert triggering.getIPduRef().getValue() == "/pdu"

    def test_readPduTriggering_adds_ipduPortRefs(self, parser):
        from armodel.models import PduTriggering
        from armodel.models import CanPhysicalChannel
        from armodel.models import CanCluster
        cluster = CanCluster(parent=_autosar_root(), short_name="c")
        channel = CanPhysicalChannel(parent=cluster, short_name="ch")
        triggering = PduTriggering(parent=channel, short_name="pt")
        element = _snip(
            "<SHORT-NAME>pt</SHORT-NAME>"
            "<I-PDU-PORT-REFS>"
            "<I-PDU-PORT-REF DEST='I-PDU-PORT'>/ip</I-PDU-PORT-REF>"
            "</I-PDU-PORT-REFS>",
            root_tag="PDU-TRIGGERING",
        )
        parser.readPduTriggering(element, triggering)
        assert len(triggering.getIPduPortRefs()) == 1

    def test_readISignalTriggering_sets_iSignalRef(self, parser):
        from armodel.models import ISignalTriggering
        from armodel.models import CanPhysicalChannel
        from armodel.models import CanCluster
        cluster = CanCluster(parent=_autosar_root(), short_name="c")
        channel = CanPhysicalChannel(parent=cluster, short_name="ch")
        triggering = ISignalTriggering(parent=channel, short_name="st")
        element = _snip(
            "<SHORT-NAME>st</SHORT-NAME>"
            "<I-SIGNAL-REF DEST='I-SIGNAL'>/sig</I-SIGNAL-REF>",
            root_tag="I-SIGNAL-TRIGGERING",
        )
        parser.readISignalTriggering(element, triggering)
        assert triggering.getISignalRef().getValue() == "/sig"

    def test_readPhysicalChannelFrameTriggerings_can(self, parser):
        from armodel.models import CanPhysicalChannel
        from armodel.models import CanCluster
        cluster = CanCluster(parent=_autosar_root(), short_name="c")
        channel = CanPhysicalChannel(parent=cluster, short_name="ch")
        element = _snip(
            "<FRAME-TRIGGERINGS>"
            "<CAN-FRAME-TRIGGERING>"
            "<SHORT-NAME>ft</SHORT-NAME>"
            "</CAN-FRAME-TRIGGERING>"
            "</FRAME-TRIGGERINGS>",
            root_tag="CAN-PHYSICAL-CHANNEL",
        )
        parser.readPhysicalChannelFrameTriggerings(element, channel)
        assert len(channel.getFrameTriggerings()) == 1

    def test_readPhysicalChannelFrameTriggerings_lin(self, parser):
        from armodel.models import LinPhysicalChannel
        from armodel.models import LinCluster
        cluster = LinCluster(parent=_autosar_root(), short_name="l")
        channel = LinPhysicalChannel(parent=cluster, short_name="ch")
        element = _snip(
            "<FRAME-TRIGGERINGS>"
            "<LIN-FRAME-TRIGGERING>"
            "<SHORT-NAME>ft</SHORT-NAME>"
            "</LIN-FRAME-TRIGGERING>"
            "</FRAME-TRIGGERINGS>",
            root_tag="LIN-PHYSICAL-CHANNEL",
        )
        parser.readPhysicalChannelFrameTriggerings(element, channel)
        assert len(channel.getFrameTriggerings()) == 1

    def test_readPhysicalChannelFrameTriggerings_flexray(self, parser):
        from armodel.models import FlexrayPhysicalChannel
        from armodel.models import FlexrayCluster
        cluster = FlexrayCluster(parent=_autosar_root(), short_name="fr")
        channel = FlexrayPhysicalChannel(parent=cluster, short_name="ch")
        element = _snip(
            "<FRAME-TRIGGERINGS>"
            "<FLEXRAY-FRAME-TRIGGERING>"
            "<SHORT-NAME>ft</SHORT-NAME>"
            "</FLEXRAY-FRAME-TRIGGERING>"
            "</FRAME-TRIGGERINGS>",
            root_tag="FLEXRAY-PHYSICAL-CHANNEL",
        )
        parser.readPhysicalChannelFrameTriggerings(element, channel)
        assert len(channel.getFrameTriggerings()) == 1

    def test_readPhysicalChannelFrameTriggerings_unsupported_warns(
        self, warning_parser, caplog
    ):
        from armodel.models import CanPhysicalChannel
        from armodel.models import CanCluster
        cluster = CanCluster(parent=_autosar_root(), short_name="c")
        channel = CanPhysicalChannel(parent=cluster, short_name="ch")
        element = _snip(
            "<FRAME-TRIGGERINGS><BAD/></FRAME-TRIGGERINGS>",
            root_tag="CAN-PHYSICAL-CHANNEL",
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readPhysicalChannelFrameTriggerings(element, channel)
        assert any("Unsupported Frame Triggering" in r.getMessage() for r in caplog.records)

    def test_readPhysicalChannelPduTriggerings_creates_triggering(self, parser):
        from armodel.models import CanPhysicalChannel
        from armodel.models import CanCluster
        cluster = CanCluster(parent=_autosar_root(), short_name="c")
        channel = CanPhysicalChannel(parent=cluster, short_name="ch")
        element = _snip(
            "<PDU-TRIGGERINGS>"
            "<PDU-TRIGGERING>"
            "<SHORT-NAME>pt</SHORT-NAME>"
            "</PDU-TRIGGERING>"
            "</PDU-TRIGGERINGS>",
            root_tag="CAN-PHYSICAL-CHANNEL",
        )
        parser.readPhysicalChannelPduTriggerings(element, channel)
        assert len(channel.getPduTriggerings()) == 1

    def test_readPhysicalChannelISignalTriggerings_creates_triggering(self, parser):
        from armodel.models import CanPhysicalChannel
        from armodel.models import CanCluster
        cluster = CanCluster(parent=_autosar_root(), short_name="c")
        channel = CanPhysicalChannel(parent=cluster, short_name="ch")
        element = _snip(
            "<I-SIGNAL-TRIGGERINGS>"
            "<I-SIGNAL-TRIGGERING>"
            "<SHORT-NAME>st</SHORT-NAME>"
            "</I-SIGNAL-TRIGGERING>"
            "</I-SIGNAL-TRIGGERINGS>",
            root_tag="CAN-PHYSICAL-CHANNEL",
        )
        parser.readPhysicalChannelISignalTriggerings(element, channel)
        assert len(channel.getISignalTriggerings()) == 1

    def test_readPhysicalChannelCommConnectorRefs_adds_ref(self, parser):
        from armodel.models import CanPhysicalChannel
        from armodel.models import CanCluster
        cluster = CanCluster(parent=_autosar_root(), short_name="c")
        channel = CanPhysicalChannel(parent=cluster, short_name="ch")
        element = _snip(
            "<COMM-CONNECTORS>"
            "<COMMUNICATION-CONNECTOR-REF-CONDITIONAL>"
            "<COMMUNICATION-CONNECTOR-REF DEST='COMMUNICATION-CONNECTOR'>/cc</COMMUNICATION-CONNECTOR-REF>"
            "</COMMUNICATION-CONNECTOR-REF-CONDITIONAL>"
            "</COMM-CONNECTORS>",
            root_tag="CAN-PHYSICAL-CHANNEL",
        )
        parser.readPhysicalChannelCommConnectorRefs(element, channel)
        assert len(channel.getCommConnectorRefs()) == 1

    def test_readPdu_sets_length(self, parser):
        from armodel.models import NmPdu
        pdu = NmPdu(parent=_autosar_root(), short_name="pdu")
        element = _snip(
            "<SHORT-NAME>pdu</SHORT-NAME>"
            "<LENGTH><VALUE>8</VALUE></LENGTH>",
            root_tag="NM-PDU",
        )
        parser.readPdu(element, pdu)
        assert pdu.getLength() is not None
        assert pdu.getLength().getValue() == 8

    def test_readIPdu_inherits_from_pdu(self, parser):
        from armodel.models import NPdu
        pdu = NPdu(parent=_autosar_root(), short_name="npdu")
        element = _snip(
            "<SHORT-NAME>npdu</SHORT-NAME>"
            "<LENGTH><VALUE>8</VALUE></LENGTH>",
            root_tag="N-PDU",
        )
        parser.readNPdu(element, pdu)
        assert pdu.getLength() is not None
        assert pdu.getLength().getValue() == 8

    def test_readNmPdu_sets_unusedBitPattern(self, parser):
        from armodel.models import NmPdu
        pdu = NmPdu(parent=_autosar_root(), short_name="nmPdu")
        element = _snip(
            "<SHORT-NAME>nmPdu</SHORT-NAME>"
            "<UNUSED-BIT-PATTERN>0xFF</UNUSED-BIT-PATTERN>",
            root_tag="NM-PDU",
        )
        parser.readNmPdu(element, pdu)
        assert pdu.getUnusedBitPattern() is not None
        assert pdu.getUnusedBitPattern().getValue() == 0xFF

    def test_readDcmIPdu_sets_diagPduType(self, parser):
        from armodel.models import DcmIPdu
        pdu = DcmIPdu(parent=_autosar_root(), short_name="dcmPdu")
        element = _snip(
            "<SHORT-NAME>dcmPdu</SHORT-NAME>"
            "<DIAG-PDU-TYPE>request</DIAG-PDU-TYPE>",
            root_tag="DCM-I-PDU",
        )
        parser.readDcmIPdu(element, pdu)
        assert pdu.getDiagPduType() is not None
        assert pdu.getDiagPduType().getValue() == "request"


class TestISignalAndGroupHandlers:
    def test_readISignal_sets_length(self, parser):
        from armodel.models import ISignal
        signal = ISignal(parent=_autosar_root(), short_name="sig")
        element = _snip(
            "<SHORT-NAME>sig</SHORT-NAME>"
            "<LENGTH><VALUE>8</VALUE></LENGTH>"
            "<I-SIGNAL-TYPE>signal</I-SIGNAL-TYPE>",
            root_tag="I-SIGNAL",
        )
        parser.readISignal(element, signal)
        assert signal.getLength() is not None
        assert signal.getLength().getValue() == 8

    def test_readISignal_sets_systemSignalRef(self, parser):
        from armodel.models import ISignal
        signal = ISignal(parent=_autosar_root(), short_name="sig")
        element = _snip(
            "<SHORT-NAME>sig</SHORT-NAME>"
            "<SYSTEM-SIGNAL-REF DEST='SYSTEM-SIGNAL'>/ss</SYSTEM-SIGNAL-REF>",
            root_tag="I-SIGNAL",
        )
        parser.readISignal(element, signal)
        assert signal.getSystemSignalRef().getValue() == "/ss"

    def test_readISignalGroup_sets_systemSignalGroupRef(self, parser):
        from armodel.models import ISignalGroup
        group = ISignalGroup(parent=_autosar_root(), short_name="sigGroup")
        element = _snip(
            "<SHORT-NAME>sigGroup</SHORT-NAME>"
            "<SYSTEM-SIGNAL-GROUP-REF DEST='SYSTEM-SIGNAL-GROUP'>/ssg</SYSTEM-SIGNAL-GROUP-REF>",
            root_tag="I-SIGNAL-GROUP",
        )
        parser.readISignalGroup(element, group)
        assert group.getSystemSignalGroupRef().getValue() == "/ssg"

    def test_readISignalGroupISignalRef_adds_ref(self, parser):
        from armodel.models import ISignalGroup
        group = ISignalGroup(parent=_autosar_root(), short_name="sigGroup")
        element = _snip(
            "<I-SIGNAL-REFS>"
            "<I-SIGNAL-REF DEST='I-SIGNAL'>/sig1</I-SIGNAL-REF>"
            "</I-SIGNAL-REFS>",
            root_tag="I-SIGNAL-GROUP",
        )
        parser.readISignalGroupISignalRef(element, group)
        assert len(group.getISignalRefs()) == 1

    def test_getDataFilter_sets_dataFilterType(self, parser):
        element = _snip(
            "<DATA-FILTER>"
            "<DATA-FILTER-TYPE>mask</DATA-FILTER-TYPE>"
            "<MASK>255</MASK>"
            "</DATA-FILTER>",
            root_tag="ROOT",
        )
        filter = parser.getDataFilter(element, "DATA-FILTER")
        assert filter is not None
        assert filter.getDataFilterType() == "mask"

    def test_getTransmissionModeTiming_sets_cyclicTiming(self, parser):
        element = _snip(
            "<TRANSMISSION-MODE-TIMING>"
            "<CYCLIC-TIMING>"
            "<TIME-PERIOD>"
            "<VALUE>"
            "<VALUE>0.1</VALUE>"
            "</VALUE>"
            "</TIME-PERIOD>"
            "</CYCLIC-TIMING>"
            "</TRANSMISSION-MODE-TIMING>",
            root_tag="ROOT",
        )
        timing = parser.getTransmissionModeTiming(element, "TRANSMISSION-MODE-TIMING")
        assert timing is not None
        assert timing.getCyclicTiming() is not None

    def test_getCyclicTiming_sets_timePeriod(self, parser):
        element = _snip(
            "<CYCLIC-TIMING>"
            "<TIME-PERIOD>"
            "<VALUE>"
            "<VALUE>0.1</VALUE>"
            "</VALUE>"
            "</TIME-PERIOD>"
            "</CYCLIC-TIMING>",
            root_tag="ROOT",
        )
        timing = parser.getCyclicTiming(element, "CYCLIC-TIMING")
        assert timing is not None

    def test_getEventControlledTiming_sets_numberOfRepetitions(self, parser):
        element = _snip(
            "<EVENT-CONTROLLED-TIMING>"
            "<NUMBER-OF-REPETITIONS>5</NUMBER-OF-REPETITIONS>"
            "</EVENT-CONTROLLED-TIMING>",
            root_tag="ROOT",
        )
        timing = parser.getEventControlledTiming(element, "EVENT-CONTROLLED-TIMING")
        assert timing is not None
        assert timing.getNumberOfRepetitions() == 5

    def test_readISignalIPdu_sets_length(self, parser):
        from armodel.models import ISignalIPdu
        ipdu = ISignalIPdu(parent=_autosar_root(), short_name="isignalPdu")
        element = _snip(
            "<SHORT-NAME>isignalPdu</SHORT-NAME>"
            "<LENGTH><VALUE>64</VALUE></LENGTH>",
            root_tag="I-SIGNAL-I-PDU",
        )
        parser.readISignalIPdu(element, ipdu)
        assert ipdu.getLength().getValue() == 64

    def test_readISignalToPduMappings_creates_mapping(self, parser):
        from armodel.models import ISignalIPdu
        ipdu = ISignalIPdu(parent=_autosar_root(), short_name="isignalPdu")
        element = _snip(
            "<I-SIGNAL-TO-PDU-MAPPINGS>"
            "<I-SIGNAL-TO-I-PDU-MAPPING>"
            "<SHORT-NAME>mapping</SHORT-NAME>"
            "<START-POSITION><VALUE>0</VALUE></START-POSITION>"
            "</I-SIGNAL-TO-I-PDU-MAPPING>"
            "</I-SIGNAL-TO-PDU-MAPPINGS>",
            root_tag="I-SIGNAL-I-PDU",
        )
        parser.readISignalToPduMappings(element, ipdu)
        assert len(ipdu.getISignalToPduMappings()) == 1

    def test_readISignalIPdu_sets_unusedBitPattern(self, parser):
        from armodel.models import ISignalIPdu
        ipdu = ISignalIPdu(parent=_autosar_root(), short_name="isignalPdu")
        element = _snip(
            "<SHORT-NAME>isignalPdu</SHORT-NAME>"
            "<UNUSED-BIT-PATTERN>0x00</UNUSED-BIT-PATTERN>",
            root_tag="I-SIGNAL-I-PDU",
        )
        parser.readISignalIPdu(element, ipdu)
        assert ipdu.getUnusedBitPattern() == 0


class TestEndToEndProtectionHandlers:
    def test_getEndToEndDescription_sets_category(self, parser):
        element = _snip(
            "<END-TO-END-PROFILE>"
            "<CATEGORY>CRC8</CATEGORY>"
            "<DATA-ID-MODE>1</DATA-ID-MODE>"
            "<DATA-LENGTH>8</DATA-LENGTH>"
            "</END-TO-END-PROFILE>",
            root_tag="ROOT",
        )
        desc = parser.getEndToEndDescription(element, "END-TO-END-PROFILE")
        assert desc is not None
        assert desc.getCategory() == "CRC8"

    def test_getEndToEndDescription_sets_dataIdMode(self, parser):
        element = _snip(
            "<END-TO-END-PROFILE>"
            "<DATA-ID-MODE>1</DATA-ID-MODE>"
            "</END-TO-END-PROFILE>",
            root_tag="ROOT",
        )
        desc = parser.getEndToEndDescription(element, "END-TO-END-PROFILE")
        assert desc.getDataIdMode() == 1

    def test_readEndToEndDescriptionDataIds_adds_dataId(self, parser):
        from armodel.models import EndToEndDescription
        desc = EndToEndDescription()
        element = _snip(
            "<DATA-IDS>"
            "<DATA-ID>1</DATA-ID>"
            "<DATA-ID>2</DATA-ID>"
            "</DATA-IDS>",
            root_tag="END-TO-END-PROFILE",
        )
        parser.readEndToEndDescriptionDataIds(element, desc)
        assert len(desc.getDataIds()) == 2

    def test_readEndToEndProtection_sets_short_name(self, parser):
        from armodel.models import EndToEndProtectionSet
        from armodel.models import EndToEndProtection
        set = EndToEndProtectionSet(parent=_autosar_root(), short_name="e2eSet")
        protection = EndToEndProtection(parent=set, short_name="e2e")
        element = _snip(
            "<SHORT-NAME>e2e</SHORT-NAME>",
            root_tag="END-TO-END-PROTECTION",
        )
        parser.readIdentifiable(element, protection)
        assert protection.getShortName() == "e2e"

    def test_readEndToEndProtectionISignalIPdu_sets_dataOffset(self, parser):
        from armodel.models import EndToEndProtectionISignalIPdu
        ipdu = EndToEndProtectionISignalIPdu()
        element = _snip(
            "<DATA-OFFSET>8</DATA-OFFSET>"
            "<I-SIGNAL-I-PDU-REF DEST='I-SIGNAL-I-PDU'>/ipdu</I-SIGNAL-I-PDU-REF>",
            root_tag="END-TO-END-PROTECTION-I-SIGNAL-I-PDU",
        )
        parser.readEndToEndProtectionISignalIPdu(element, ipdu)
        assert ipdu.getDataOffset() == 8

    def test_readEndToEndProtectionISignalIPdu_sets_iSignalIPduRef(self, parser):
        from armodel.models import EndToEndProtectionISignalIPdu
        ipdu = EndToEndProtectionISignalIPdu()
        element = _snip(
            "<I-SIGNAL-I-PDU-REF DEST='I-SIGNAL-I-PDU'>/ipdu</I-SIGNAL-I-PDU-REF>",
            root_tag="END-TO-END-PROTECTION-I-SIGNAL-I-PDU",
        )
        parser.readEndToEndProtectionISignalIPdu(element, ipdu)
        assert ipdu.getISignalIPduRef().getValue() == "/ipdu"

    def test_readEndToEndProtectionVariablePrototype_sets_senderIRef(self, parser):
        from armodel.models import EndToEndProtectionVariablePrototype
        proto = EndToEndProtectionVariablePrototype()
        element = _snip(
            "<SENDER-IREF>"
            "<TARGET-DATA-PROTOTYPE-REF DEST='VARIABLE-DATA-PROTOTYPE'>/vdp</TARGET-DATA-PROTOTYPE-REF>"
            "</SENDER-IREF>",
            root_tag="END-TO-END-PROTECTION-VARIABLE-PROTOTYPE",
        )
        parser.readEndToEndProtectionVariablePrototype(element, proto)
        assert proto.senderIRef is not None

    def test_readEndToEndProtectionVariablePrototype_adds_receiverIref(self, parser):
        from armodel.models import EndToEndProtectionVariablePrototype
        proto = EndToEndProtectionVariablePrototype()
        element = _snip(
            "<RECEIVER-IREFS>"
            "<RECEIVER-IREF>"
            "<TARGET-DATA-PROTOTYPE-REF DEST='VARIABLE-DATA-PROTOTYPE'>/vdp1</TARGET-DATA-PROTOTYPE-REF>"
            "</RECEIVER-IREF>"
            "</RECEIVER-IREFS>",
            root_tag="END-TO-END-PROTECTION-VARIABLE-PROTOTYPE",
        )
        parser.readEndToEndProtectionVariablePrototype(element, proto)
        assert len(proto.getReceiverIrefs()) == 1

    def test_readEndToEndProtectionEndToEndProtectionVariablePrototypes_creates(
        self, parser
    ):
        from armodel.models import EndToEndProtection
        from armodel.models import EndToEndProtectionSet
        set = EndToEndProtectionSet(parent=_autosar_root(), short_name="e2eSet")
        protection = EndToEndProtection(parent=set, short_name="e2e")
        element = _snip(
            "<END-TO-END-PROTECTION-VARIABLE-PROTOTYPES>"
            "<END-TO-END-PROTECTION-VARIABLE-PROTOTYPE>"
            "<SHORT-NAME>proto</SHORT-NAME>"
            "</END-TO-END-PROTECTION-VARIABLE-PROTOTYPE>"
            "</END-TO-END-PROTECTION-VARIABLE-PROTOTYPES>",
            root_tag="END-TO-END-PROTECTION",
        )
        parser.readEndToEndProtectionEndToEndProtectionVariablePrototypes(
            element, protection
        )
        assert len(protection.getEndToEndProtectionVariablePrototypes()) == 1

    def test_readEndToEndProtectionEndToEndProtectionVariablePrototypes_unsupported_warns(
        self, warning_parser, caplog
    ):
        from armodel.models import EndToEndProtection
        from armodel.models import EndToEndProtectionSet
        set = EndToEndProtectionSet(parent=_autosar_root(), short_name="e2eSet")
        protection = EndToEndProtection(parent=set, short_name="e2e")
        element = _snip(
            "<END-TO-END-PROTECTION-VARIABLE-PROTOTYPES><BAD/></END-TO-END-PROTECTION-VARIABLE-PROTOTYPES>",
            root_tag="END-TO-END-PROTECTION",
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readEndToEndProtectionEndToEndProtectionVariablePrototypes(
                element, protection
            )
        assert any("Unsupported End To End Protection Variable Prototype" in r.getMessage() for r in caplog.records)

    def test_readEndToEndProtectionSet_sets_short_name(self, parser):
        from armodel.models import EndToEndProtectionSet
        set = EndToEndProtectionSet(parent=_autosar_root(), short_name="e2eSet")
        element = _snip("<SHORT-NAME>e2eSet</SHORT-NAME>", root_tag="END-TO-END-PROTECTION-SET")
        parser.readIdentifiable(element, set)
        assert set.getShortName() == "e2eSet"


class TestNmConfigHandlers:
    def test_readNmConfig_sets_short_name(self, parser):
        from armodel.models import NmConfig
        config = NmConfig(parent=_autosar_root(), short_name="nmConfig")
        element = _snip("<SHORT-NAME>nmConfig</SHORT-NAME>", root_tag="NM-CONFIG")
        parser.readIdentifiable(element, config)
        assert config.getShortName() == "nmConfig"

    def test_readNmConfigNmClusters_canNmCluster(self, parser):
        from armodel.models import NmConfig
        config = NmConfig(parent=_autosar_root(), short_name="nmConfig")
        element = _snip(
            "<NM-CLUSTERS>"
            "<CAN-NM-CLUSTER>"
            "<SHORT-NAME>cnm</SHORT-NAME>"
            "</CAN-NM-CLUSTER>"
            "</NM-CLUSTERS>",
            root_tag="NM-CONFIG",
        )
        parser.readNmConfigNmClusters(element, config)
        assert len(config.getNmClusters()) == 1

    def test_readNmConfigNmClusters_udpNmCluster(self, parser):
        from armodel.models import NmConfig
        config = NmConfig(parent=_autosar_root(), short_name="nmConfig")
        element = _snip(
            "<NM-CLUSTERS>"
            "<UDP-NM-CLUSTER>"
            "<SHORT-NAME>unm</SHORT-NAME>"
            "</UDP-NM-CLUSTER>"
            "</NM-CLUSTERS>",
            root_tag="NM-CONFIG",
        )
        parser.readNmConfigNmClusters(element, config)
        assert len(config.getNmClusters()) == 1

    def test_readNmConfigNmClusters_unsupported_raises(self, parser):
        from armodel.models import NmConfig
        config = NmConfig(parent=_autosar_root(), short_name="nmConfig")
        element = _snip(
            "<NM-CLUSTERS><BAD/></NM-CLUSTERS>",
            root_tag="NM-CONFIG",
        )
        with pytest.raises(Exception):
            parser.readNmConfigNmClusters(element, config)

    def test_readCanNmCluster_sets_nmBusloadReductionActive(self, parser):
        from armodel.models import CanNmCluster
        from armodel.models import NmConfig
        config = NmConfig(parent=_autosar_root(), short_name="nmConfig")
        cluster = CanNmCluster(parent=config, short_name="cnm")
        element = _snip(
            "<SHORT-NAME>cnm</SHORT-NAME>"
            "<NM-BUSLOAD-REDUCTION-ACTIVE>true</NM-BUSLOAD-REDUCTION-ACTIVE>"
            "<NM-CHANNEL-ACTIVE>true</NM-CHANNEL-ACTIVE>",
            root_tag="CAN-NM-CLUSTER",
        )
        parser.readCanNmCluster(element, cluster)
        assert cluster.getNmBusloadReductionActive() == True

    def test_readUdpNmCluster_sets_nmChannelActive(self, parser):
        from armodel.models import UdpNmCluster
        from armodel.models import NmConfig
        config = NmConfig(parent=_autosar_root(), short_name="nmConfig")
        cluster = UdpNmCluster(parent=config, short_name="unm")
        element = _snip(
            "<SHORT-NAME>unm</SHORT-NAME>"
            "<NM-CHANNEL-ACTIVE>true</NM-CHANNEL-ACTIVE>",
            root_tag="UDP-NM-CLUSTER",
        )
        parser.readUdpNmCluster(element, cluster)
        assert cluster.getNmChannelActive() == True

    def test_readNmCluster_sets_communicationClusterRef(self, parser):
        from armodel.models import CanNmCluster
        from armodel.models import NmConfig
        config = NmConfig(parent=_autosar_root(), short_name="nmConfig")
        cluster = CanNmCluster(parent=config, short_name="cnm")
        element = _snip(
            "<SHORT-NAME>cnm</SHORT-NAME>"
            "<COMMUNICATION-CLUSTER-REF DEST='CAN-CLUSTER'>/cc</COMMUNICATION-CLUSTER-REF>",
            root_tag="CAN-NM-CLUSTER",
        )
        parser.readNmCluster(element, cluster)
        assert cluster.getCommunicationClusterRef().getValue() == "/cc"

    def test_readNmClusterNmNodes_canNmNode(self, parser):
        from armodel.models import CanNmCluster
        from armodel.models import NmConfig
        config = NmConfig(parent=_autosar_root(), short_name="nmConfig")
        cluster = CanNmCluster(parent=config, short_name="cnm")
        element = _snip(
            "<NM-NODES>"
            "<CAN-NM-NODE>"
            "<SHORT-NAME>node</SHORT-NAME>"
            "</CAN-NM-NODE>"
            "</NM-NODES>",
            root_tag="CAN-NM-CLUSTER",
        )
        parser.readNmClusterNmNodes(element, cluster)
        assert len(cluster.getNmNodes()) == 1

    def test_readNmClusterNmNodes_udpNmNode(self, parser):
        from armodel.models import UdpNmCluster
        from armodel.models import NmConfig
        config = NmConfig(parent=_autosar_root(), short_name="nmConfig")
        cluster = UdpNmCluster(parent=config, short_name="unm")
        element = _snip(
            "<NM-NODES>"
            "<UDP-NM-NODE>"
            "<SHORT-NAME>node</SHORT-NAME>"
            "</UDP-NM-NODE>"
            "</NM-NODES>",
            root_tag="UDP-NM-CLUSTER",
        )
        parser.readNmClusterNmNodes(element, cluster)
        assert len(cluster.getNmNodes()) == 1

    def test_readNmClusterNmNodes_unsupported_warns(self, warning_parser, caplog):
        from armodel.models import CanNmCluster
        from armodel.models import NmConfig
        config = NmConfig(parent=_autosar_root(), short_name="nmConfig")
        cluster = CanNmCluster(parent=config, short_name="cnm")
        element = _snip(
            "<NM-NODES><BAD/></NM-NODES>",
            root_tag="CAN-NM-CLUSTER",
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readNmClusterNmNodes(element, cluster)
        assert any("Unsupported Nm Node" in r.getMessage() for r in caplog.records)

    def test_readCanNmNode_sets_nmNodeId(self, parser):
        from armodel.models import CanNmNode
        from armodel.models import CanNmCluster
        from armodel.models import NmConfig
        config = NmConfig(parent=_autosar_root(), short_name="nmConfig")
        cluster = CanNmCluster(parent=config, short_name="cnm")
        node = CanNmNode(parent=cluster, short_name="node")
        element = _snip(
            "<SHORT-NAME>node</SHORT-NAME>"
            "<NM-NODE-ID><VALUE>1</VALUE></NM-NODE-ID>"
            "<NM-PASSIVE-MODE-ENABLED>false</NM-PASSIVE-MODE-ENABLED>",
            root_tag="CAN-NM-NODE",
        )
        parser.readCanNmNode(element, node)
        assert node.getNmNodeId().getValue() == 1

    def test_readNmNode_sets_controllerRef(self, parser):
        from armodel.models import CanNmNode
        from armodel.models import CanNmCluster
        from armodel.models import NmConfig
        config = NmConfig(parent=_autosar_root(), short_name="nmConfig")
        cluster = CanNmCluster(parent=config, short_name="cnm")
        node = CanNmNode(parent=cluster, short_name="node")
        element = _snip(
            "<SHORT-NAME>node</SHORT-NAME>"
            "<CONTROLLER-REF DEST='COMMUNICATION-CONTROLLER'>/ctrl</CONTROLLER-REF>",
            root_tag="CAN-NM-NODE",
        )
        parser.readNmNode(element, node)
        assert node.getControllerRef().getValue() == "/ctrl"

    def test_readNmNode_adds_rxNmPduRef(self, parser):
        from armodel.models import CanNmNode
        from armodel.models import CanNmCluster
        from armodel.models import NmConfig
        config = NmConfig(parent=_autosar_root(), short_name="nmConfig")
        cluster = CanNmCluster(parent=config, short_name="cnm")
        node = CanNmNode(parent=cluster, short_name="node")
        element = _snip(
            "<SHORT-NAME>node</SHORT-NAME>"
            "<RX-NM-PDU-REFS>"
            "<RX-NM-PDU-REF DEST='NM-PDU'>/rx</RX-NM-PDU-REF>"
            "</RX-NM-PDU-REFS>",
            root_tag="CAN-NM-NODE",
        )
        parser.readNmNode(element, node)
        assert len(node.getRxNmPduRefs()) == 1

    def test_readNmNode_adds_txNmPduRef(self, parser):
        from armodel.models import CanNmNode
        from armodel.models import CanNmCluster
        from armodel.models import NmConfig
        config = NmConfig(parent=_autosar_root(), short_name="nmConfig")
        cluster = CanNmCluster(parent=config, short_name="cnm")
        node = CanNmNode(parent=cluster, short_name="node")
        element = _snip(
            "<SHORT-NAME>node</SHORT-NAME>"
            "<TX-NM-PDU-REFS>"
            "<TX-NM-PDU-REF DEST='NM-PDU'>/tx</TX-NM-PDU-REF>"
            "</TX-NM-PDU-REFS>",
            root_tag="CAN-NM-NODE",
        )
        parser.readNmNode(element, node)
        assert len(node.getTxNmPduRefs()) == 1

    def test_getCanNmClusterCoupling_adds_coupledClusterRef(self, parser):
        element = _snip(
            "<COUPLED-CLUSTER-REFS>"
            "<COUPLED-CLUSTER-REF DEST='NM-CLUSTER'>/cluster</COUPLED-CLUSTER-REF>"
            "</COUPLED-CLUSTER-REFS>"
            "<NM-BUSLOAD-REDUCTION-ENABLED>true</NM-BUSLOAD-REDUCTION-ENABLED>",
            root_tag="CAN-NM-CLUSTER-COUPLING",
        )
        coupling = parser.getCanNmClusterCoupling(element)
        assert len(coupling.getCoupledClusterRefs()) == 1

    def test_getUdpNmClusterCoupling_adds_coupledClusterRef(self, parser):
        element = _snip(
            "<COUPLED-CLUSTER-REFS>"
            "<COUPLED-CLUSTER-REF DEST='NM-CLUSTER'>/cluster</COUPLED-CLUSTER-REF>"
            "</COUPLED-CLUSTER-REFS>"
            "<NM-IMMEDIATE-RESTART-ENABLED>true</NM-IMMEDIATE-RESTART-ENABLED>",
            root_tag="UDP-NM-CLUSTER-COUPLING",
        )
        coupling = parser.getUdpNmClusterCoupling(element)
        assert len(coupling.getCoupledClusterRefs()) == 1

    def test_readNmConfigNmClusterCouplings_can(self, parser):
        from armodel.models import NmConfig
        config = NmConfig(parent=_autosar_root(), short_name="nmConfig")
        element = _snip(
            "<NM-CLUSTER-COUPLINGS>"
            "<CAN-NM-CLUSTER-COUPLING>"
            "<NM-BUSLOAD-REDUCTION-ENABLED>true</NM-BUSLOAD-REDUCTION-ENABLED>"
            "</CAN-NM-CLUSTER-COUPLING>"
            "</NM-CLUSTER-COUPLINGS>",
            root_tag="NM-CONFIG",
        )
        parser.readNmConfigNmClusterCouplings(element, config)
        assert len(config.getNmClusterCouplings()) == 1

    def test_readNmConfigNmClusterCouplings_udp(self, parser):
        from armodel.models import NmConfig
        config = NmConfig(parent=_autosar_root(), short_name="nmConfig")
        element = _snip(
            "<NM-CLUSTER-COUPLINGS>"
            "<UDP-NM-CLUSTER-COUPLING>"
            "<NM-IMMEDIATE-RESTART-ENABLED>true</NM-IMMEDIATE-RESTART-ENABLED>"
            "</UDP-NM-CLUSTER-COUPLING>"
            "</NM-CLUSTER-COUPLINGS>",
            root_tag="NM-CONFIG",
        )
        parser.readNmConfigNmClusterCouplings(element, config)
        assert len(config.getNmClusterCouplings()) == 1

    def test_readNmConfigNmIfEcus_creates_ecu(self, parser):
        from armodel.models import NmConfig
        config = NmConfig(parent=_autosar_root(), short_name="nmConfig")
        element = _snip(
            "<NM-IF-ECUS>"
            "<NM-ECU>"
            "<SHORT-NAME>ecu</SHORT-NAME>"
            "</NM-ECU>"
            "</NM-IF-ECUS>",
            root_tag="NM-CONFIG",
        )
        parser.readNmConfigNmIfEcus(element, config)
        assert len(config.getNmIfEcus()) == 1

    def test_readNmEcu_sets_ecuInstanceRef(self, parser):
        from armodel.models import NmEcu
        from armodel.models import NmConfig
        config = NmConfig(parent=_autosar_root(), short_name="nmConfig")
        ecu = NmEcu(parent=config, short_name="ecu")
        element = _snip(
            "<SHORT-NAME>ecu</SHORT-NAME>"
            "<ECU-INSTANCE-REF DEST='ECU-INSTANCE'>/ei</ECU-INSTANCE-REF>"
            "<NM-BUS-SYNCHRONIZATION-ENABLED>true</NM-BUS-SYNCHRONIZATION-ENABLED>",
            root_tag="NM-ECU",
        )
        parser.readNmEcu(element, ecu)
        assert ecu.getEcuInstanceRef().getValue() == "/ei"


class TestCanTpAndLinTpHandlers:
    def test_readCanTpConfig_sets_short_name(self, parser):
        from armodel.models import CanTpConfig
        config = CanTpConfig(parent=_autosar_root(), short_name="canTp")
        element = _snip("<SHORT-NAME>canTp</SHORT-NAME>", root_tag="CAN-TP-CONFIG")
        parser.readIdentifiable(element, config)
        assert config.getShortName() == "canTp"

    def test_readCanTpConfigTpAddresses_creates_address(self, parser):
        from armodel.models import CanTpConfig
        config = CanTpConfig(parent=_autosar_root(), short_name="canTp")
        element = _snip(
            "<TP-ADDRESSS>"
            "<CAN-TP-ADDRESS>"
            "<SHORT-NAME>addr</SHORT-NAME>"
            "<TP-ADDRESS>1</TP-ADDRESS>"
            "</CAN-TP-ADDRESS>"
            "</TP-ADDRESSS>",
            root_tag="CAN-TP-CONFIG",
        )
        parser.readCanTpConfigTpAddresses(element, config)
        assert len(config.getTpAddresses()) == 1

    def test_readCanTpAddress_sets_tpAddress(self, parser):
        from armodel.models import CanTpAddress
        from armodel.models import CanTpConfig
        config = CanTpConfig(parent=_autosar_root(), short_name="canTp")
        addr = CanTpAddress(parent=config, short_name="addr")
        element = _snip(
            "<SHORT-NAME>addr</SHORT-NAME>"
            "<TP-ADDRESS>1</TP-ADDRESS>"
            "<TP-ADDRESS-EXTENSION-VALUE>0</TP-ADDRESS-EXTENSION-VALUE>",
            root_tag="CAN-TP-ADDRESS",
        )
        parser.readCanTpAddress(element, addr)
        assert addr.getTpAddress() == 1

    def test_readCanTpConfigTpChannels_creates_channel(self, parser):
        from armodel.models import CanTpConfig
        config = CanTpConfig(parent=_autosar_root(), short_name="canTp")
        element = _snip(
            "<TP-CHANNELS>"
            "<CAN-TP-CHANNEL>"
            "<SHORT-NAME>ch</SHORT-NAME>"
            "<CHANNEL-ID>1</CHANNEL-ID>"
            "<CHANNEL-MODE>full</CHANNEL-MODE>"
            "</CAN-TP-CHANNEL>"
            "</TP-CHANNELS>",
            root_tag="CAN-TP-CONFIG",
        )
        parser.readCanTpConfigTpChannels(element, config)
        assert len(config.getTpChannels()) == 1

    def test_readCanTpChannel_sets_channelId(self, parser):
        from armodel.models import CanTpChannel
        from armodel.models import CanTpConfig
        config = CanTpConfig(parent=_autosar_root(), short_name="canTp")
        channel = CanTpChannel(parent=config, short_name="ch")
        element = _snip(
            "<SHORT-NAME>ch</SHORT-NAME>"
            "<CHANNEL-ID>1</CHANNEL-ID>"
            "<CHANNEL-MODE>full</CHANNEL-MODE>",
            root_tag="CAN-TP-CHANNEL",
        )
        parser.readCanTpChannel(element, channel)
        assert channel.getChannelId() == 1

    def test_readCanTpConfigTpNodes_creates_node(self, parser):
        from armodel.models import CanTpConfig
        config = CanTpConfig(parent=_autosar_root(), short_name="canTp")
        element = _snip(
            "<TP-NODES>"
            "<CAN-TP-NODE>"
            "<SHORT-NAME>node</SHORT-NAME>"
            "<MAX-FC-WAIT>10</MAX-FC-WAIT>"
            "</CAN-TP-NODE>"
            "</TP-NODES>",
            root_tag="CAN-TP-CONFIG",
        )
        parser.readCanTpConfigTpNodes(element, config)
        assert len(config.getTpNodes()) == 1

    def test_readCanTpNode_sets_maxFcWait(self, parser):
        from armodel.models import CanTpNode
        from armodel.models import CanTpConfig
        config = CanTpConfig(parent=_autosar_root(), short_name="canTp")
        node = CanTpNode(parent=config, short_name="node")
        element = _snip(
            "<SHORT-NAME>node</SHORT-NAME>"
            "<MAX-FC-WAIT>10</MAX-FC-WAIT>"
            "<ST-MIN><VALUE>0.01</VALUE></ST-MIN>",
            root_tag="CAN-TP-NODE",
        )
        parser.readCanTpNode(element, node)
        assert node.getMaxFcWait() == 10

    def test_readCanTpConfigTpConnections_creates_connection(self, parser):
        from armodel.models import CanTpConfig
        config = CanTpConfig(parent=_autosar_root(), short_name="canTp")
        element = _snip(
            "<TP-CONNECTIONS>"
            "<CAN-TP-CONNECTION>"
            "<IDENT><SHORT-NAME>conn</SHORT-NAME></IDENT>"
            "<ADDRESSING-FORMAT>standard</ADDRESSING-FORMAT>"
            "</CAN-TP-CONNECTION>"
            "</TP-CONNECTIONS>",
            root_tag="CAN-TP-CONFIG",
        )
        parser.readCanTpConfigTpConnections(element, config)
        assert len(config.getTpConnections()) == 1

    def test_readCanTpConnection_sets_addressingFormat(self, parser):
        from armodel.models import CanTpConnection
        conn = CanTpConnection()
        element = _snip(
            "<IDENT><SHORT-NAME>conn</SHORT-NAME></IDENT>"
            "<ADDRESSING-FORMAT>standard</ADDRESSING-FORMAT>"
            "<MAX-BLOCK-SIZE>8</MAX-BLOCK-SIZE>",
            root_tag="CAN-TP-CONNECTION",
        )
        parser.readCanTpConnection(element, conn)
        assert conn.getAddressingFormat() == "standard"

    def test_readCanTpConfigTpEcus_creates_ecu(self, parser):
        from armodel.models import CanTpConfig
        config = CanTpConfig(parent=_autosar_root(), short_name="canTp")
        element = _snip(
            "<TP-ECUS>"
            "<CAN-TP-ECU>"
            "<ECU-INSTANCE-REF DEST='ECU-INSTANCE'>/ei</ECU-INSTANCE-REF>"
            "</CAN-TP-ECU>"
            "</TP-ECUS>",
            root_tag="CAN-TP-CONFIG",
        )
        parser.readCanTpConfigTpEcus(element, config)
        assert len(config.getTpEcus()) == 1

    def test_readTpConnection_creates_ident(self, parser):
        from armodel.models import CanTpConnection
        conn = CanTpConnection()
        element = _snip(
            "<IDENT><SHORT-NAME>conn</SHORT-NAME></IDENT>",
            root_tag="CAN-TP-CONNECTION",
        )
        parser.readTpConnection(element, conn)
        assert conn.getIdent() is not None

    def test_readLinTpConfig_sets_short_name(self, parser):
        from armodel.models import LinTpConfig
        config = LinTpConfig(parent=_autosar_root(), short_name="linTp")
        element = _snip("<SHORT-NAME>linTp</SHORT-NAME>", root_tag="LIN-TP-CONFIG")
        parser.readIdentifiable(element, config)
        assert config.getShortName() == "linTp"

    def test_readLinTpConfigTpAddresses_creates_address(self, parser):
        from armodel.models import LinTpConfig
        config = LinTpConfig(parent=_autosar_root(), short_name="linTp")
        element = _snip(
            "<TP-ADDRESSS>"
            "<TP-ADDRESS>"
            "<SHORT-NAME>addr</SHORT-NAME>"
            "<TP-ADDRESS>1</TP-ADDRESS>"
            "</TP-ADDRESS>"
            "</TP-ADDRESSS>",
            root_tag="LIN-TP-CONFIG",
        )
        parser.readLinTpConfigTpAddresses(element, config)
        assert len(config.getTpAddresses()) == 1

    def test_readTpAddress_sets_tpAddress(self, parser):
        from armodel.models import TpAddress
        from armodel.models import LinTpConfig
        config = LinTpConfig(parent=_autosar_root(), short_name="linTp")
        addr = TpAddress(parent=config, short_name="addr")
        element = _snip(
            "<SHORT-NAME>addr</SHORT-NAME>"
            "<TP-ADDRESS>1</TP-ADDRESS>",
            root_tag="TP-ADDRESS",
        )
        parser.readTpAddress(element, addr)
        assert addr.getTpAddress() == 1

    def test_readLinTpConfigTpNodes_creates_node(self, parser):
        from armodel.models import LinTpConfig
        config = LinTpConfig(parent=_autosar_root(), short_name="linTp")
        element = _snip(
            "<TP-NODES>"
            "<LIN-TP-NODE>"
            "<SHORT-NAME>node</SHORT-NAME>"
            "<P-2-MAX><VALUE>0.05</VALUE></P-2-MAX>"
            "</LIN-TP-NODE>"
            "</TP-NODES>",
            root_tag="LIN-TP-CONFIG",
        )
        parser.readLinTpConfigTpNodes(element, config)
        assert len(config.getTpNodes()) == 1

    def test_readLinTpNode_sets_p2Max(self, parser):
        from armodel.models import LinTpNode
        from armodel.models import LinTpConfig
        config = LinTpConfig(parent=_autosar_root(), short_name="linTp")
        node = LinTpNode(parent=config, short_name="node")
        element = _snip(
            "<SHORT-NAME>node</SHORT-NAME>"
            "<P-2-MAX><VALUE>0.05</VALUE></P-2-MAX>"
            "<P-2-TIMING><VALUE>0.01</VALUE></P-2-TIMING>",
            root_tag="LIN-TP-NODE",
        )
        parser.readLinTpNode(element, node)
        assert node.getP2Max().getValue() == 0.05

    def test_readLinTpConnection_sets_timeoutAs(self, parser):
        from armodel.models import LinTpConnection
        conn = LinTpConnection()
        element = _snip(
            "<IDENT><SHORT-NAME>conn</SHORT-NAME></IDENT>"
            "<TIMEOUT-AS><VALUE>0.1</VALUE></TIMEOUT-AS>",
            root_tag="LIN-TP-CONNECTION",
        )
        parser.readLinTpConnection(element, conn)
        assert conn.getTimeoutAs().getValue() == 0.1

    def test_readTpConfig_sets_communicationClusterRef(self, parser):
        from armodel.models import CanTpConfig
        config = CanTpConfig(parent=_autosar_root(), short_name="canTp")
        element = _snip(
            "<SHORT-NAME>canTp</SHORT-NAME>"
            "<COMMUNICATION-CLUSTER-REF DEST='CAN-CLUSTER'>/cc</COMMUNICATION-CLUSTER-REF>",
            root_tag="CAN-TP-CONFIG",
        )
        parser.readTpConfig(element, config)
        assert config.getCommunicationClusterRef().getValue() == "/cc"

    def test_readCanTpConfigTpConnections_unsupported_warns(
        self, warning_parser, caplog
    ):
        from armodel.models import CanTpConfig
        config = CanTpConfig(parent=_autosar_root(), short_name="canTp")
        element = _snip(
            "<TP-CONNECTIONS><BAD/></TP-CONNECTIONS>",
            root_tag="CAN-TP-CONFIG",
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readCanTpConfigTpConnections(element, config)
        assert any("Unsupported TpConnection" in r.getMessage() for r in caplog.records)


class TestEcuInstanceHandlers:
    def test_readEcuInstance_sets_short_name(self, parser):
        from armodel.models import EcuInstance
        instance = EcuInstance(parent=_autosar_root(), short_name="ecu")
        element = _snip("<SHORT-NAME>ecu</SHORT-NAME>", root_tag="ECU-INSTANCE")
        parser.readIdentifiable(element, instance)
        assert instance.getShortName() == "ecu"

    def test_readEcuInstance_sets_diagnosticAddress(self, parser):
        from armodel.models import EcuInstance
        instance = EcuInstance(parent=_autosar_root(), short_name="ecu")
        element = _snip(
            "<SHORT-NAME>ecu</SHORT-NAME>"
            "<DIAGNOSTIC-ADDRESS>0x01</DIAGNOSTIC-ADDRESS>"
            "<SLEEP-MODE-SUPPORTED>true</SLEEP-MODE-SUPPORTED>",
            root_tag="ECU-INSTANCE",
        )
        parser.readEcuInstance(element, instance)
        assert instance.getDiagnosticAddress() == 0x01

    def test_readEcuInstanceCommControllers_can(self, parser):
        from armodel.models import EcuInstance
        instance = EcuInstance(parent=_autosar_root(), short_name="ecu")
        element = _snip(
            "<COMM-CONTROLLERS>"
            "<CAN-COMMUNICATION-CONTROLLER>"
            "<SHORT-NAME>ctrl</SHORT-NAME>"
            "</CAN-COMMUNICATION-CONTROLLER>"
            "</COMM-CONTROLLERS>",
            root_tag="ECU-INSTANCE",
        )
        parser.readEcuInstanceCommControllers(element, instance)
        assert len(instance.getCommControllers()) == 1

    def test_readEcuInstanceCommControllers_ethernet(self, parser):
        from armodel.models import EcuInstance
        instance = EcuInstance(parent=_autosar_root(), short_name="ecu")
        element = _snip(
            "<COMM-CONTROLLERS>"
            "<ETHERNET-COMMUNICATION-CONTROLLER>"
            "<SHORT-NAME>ctrl</SHORT-NAME>"
            "</ETHERNET-COMMUNICATION-CONTROLLER>"
            "</COMM-CONTROLLERS>",
            root_tag="ECU-INSTANCE",
        )
        parser.readEcuInstanceCommControllers(element, instance)
        assert len(instance.getCommControllers()) == 1

    def test_readEcuInstanceCommControllers_lin(self, parser):
        from armodel.models import EcuInstance
        instance = EcuInstance(parent=_autosar_root(), short_name="ecu")
        element = _snip(
            "<COMM-CONTROLLERS>"
            "<LIN-MASTER>"
            "<SHORT-NAME>ctrl</SHORT-NAME>"
            "</LIN-MASTER>"
            "</COMM-CONTROLLERS>",
            root_tag="ECU-INSTANCE",
        )
        parser.readEcuInstanceCommControllers(element, instance)
        assert len(instance.getCommControllers()) == 1

    def test_readEcuInstanceCommControllers_flexray(self, parser):
        from armodel.models import EcuInstance
        instance = EcuInstance(parent=_autosar_root(), short_name="ecu")
        element = _snip(
            "<COMM-CONTROLLERS>"
            "<FLEXRAY-COMMUNICATION-CONTROLLER>"
            "<SHORT-NAME>ctrl</SHORT-NAME>"
            "</FLEXRAY-COMMUNICATION-CONTROLLER>"
            "</COMM-CONTROLLERS>",
            root_tag="ECU-INSTANCE",
        )
        parser.readEcuInstanceCommControllers(element, instance)
        assert len(instance.getCommControllers()) == 1

    def test_readEcuInstanceCommControllers_unsupported_raises(self, parser):
        from armodel.models import EcuInstance
        instance = EcuInstance(parent=_autosar_root(), short_name="ecu")
        element = _snip(
            "<COMM-CONTROLLERS><BAD/></COMM-CONTROLLERS>",
            root_tag="ECU-INSTANCE",
        )
        with pytest.raises(Exception):
            parser.readEcuInstanceCommControllers(element, instance)

    def test_readCanCommunicationController_sets_short_name(self, parser):
        from armodel.models import CanCommunicationController
        from armodel.models import EcuInstance
        instance = EcuInstance(parent=_autosar_root(), short_name="ecu")
        ctrl = CanCommunicationController(parent=instance, short_name="ctrl")
        element = _snip(
            "<SHORT-NAME>ctrl</SHORT-NAME>"
            "<CAN-COMMUNICATION-CONTROLLER-VARIANTS>"
            "<CAN-COMMUNICATION-CONTROLLER-CONDITIONAL>"
            "</CAN-COMMUNICATION-CONTROLLER-CONDITIONAL>"
            "</CAN-COMMUNICATION-CONTROLLER-VARIANTS>",
            root_tag="CAN-COMMUNICATION-CONTROLLER",
        )
        parser.readCanCommunicationController(element, ctrl)
        assert ctrl.getShortName() == "ctrl"

    def test_readEthernetCommunicationController_sets_short_name(self, parser):
        from armodel.models import EthernetCommunicationController
        from armodel.models import EcuInstance
        instance = EcuInstance(parent=_autosar_root(), short_name="ecu")
        ctrl = EthernetCommunicationController(parent=instance, short_name="ctrl")
        element = _snip(
            "<SHORT-NAME>ctrl</SHORT-NAME>"
            "<ETHERNET-COMMUNICATION-CONTROLLER-VARIANTS>"
            "<ETHERNET-COMMUNICATION-CONTROLLER-CONDITIONAL>"
            "</ETHERNET-COMMUNICATION-CONTROLLER-CONDITIONAL>"
            "</ETHERNET-COMMUNICATION-CONTROLLER-VARIANTS>",
            root_tag="ETHERNET-COMMUNICATION-CONTROLLER",
        )
        parser.readEthernetCommunicationController(element, ctrl)
        assert ctrl.getShortName() == "ctrl"

    def test_readLinMaster_sets_short_name(self, parser):
        from armodel.models import LinMaster
        from armodel.models import EcuInstance
        instance = EcuInstance(parent=_autosar_root(), short_name="ecu")
        ctrl = LinMaster(parent=instance, short_name="ctrl")
        element = _snip(
            "<SHORT-NAME>ctrl</SHORT-NAME>"
            "<LIN-MASTER-VARIANTS>"
            "<LIN-MASTER-CONDITIONAL>"
            "<PROTOCOL-VERSION>2.0</PROTOCOL-VERSION>"
            "</LIN-MASTER-CONDITIONAL>"
            "</LIN-MASTER-VARIANTS>",
            root_tag="LIN-MASTER",
        )
        parser.readLinMaster(element, ctrl)
        assert ctrl.getShortName() == "ctrl"

    def test_readFlexrayCommunicationController_sets_short_name(self, parser):
        from armodel.models import FlexrayCommunicationController
        from armodel.models import EcuInstance
        instance = EcuInstance(parent=_autosar_root(), short_name="ecu")
        ctrl = FlexrayCommunicationController(parent=instance, short_name="ctrl")
        element = _snip(
            "<SHORT-NAME>ctrl</SHORT-NAME>"
            "<FLEXRAY-COMMUNICATION-CONTROLLER-VARIANTS>"
            "<FLEXRAY-COMMUNICATION-CONTROLLER-CONDITIONAL>"
            "</FLEXRAY-COMMUNICATION-CONTROLLER-CONDITIONAL>"
            "</FLEXRAY-COMMUNICATION-CONTROLLER-VARIANTS>",
            root_tag="FLEXRAY-COMMUNICATION-CONTROLLER",
        )
        parser.readFlexrayCommunicationController(element, ctrl)
        assert ctrl.getShortName() == "ctrl"

    def test_readEcuInstanceConnectors_can(self, parser):
        from armodel.models import EcuInstance
        instance = EcuInstance(parent=_autosar_root(), short_name="ecu")
        element = _snip(
            "<CONNECTORS>"
            "<CAN-COMMUNICATION-CONNECTOR>"
            "<SHORT-NAME>conn</SHORT-NAME>"
            "</CAN-COMMUNICATION-CONNECTOR>"
            "</CONNECTORS>",
            root_tag="ECU-INSTANCE",
        )
        parser.readEcuInstanceConnectors(element, instance)
        assert len(instance.getConnectors()) == 1

    def test_readEcuInstanceConnectors_ethernet(self, parser):
        from armodel.models import EcuInstance
        instance = EcuInstance(parent=_autosar_root(), short_name="ecu")
        element = _snip(
            "<CONNECTORS>"
            "<ETHERNET-COMMUNICATION-CONNECTOR>"
            "<SHORT-NAME>conn</SHORT-NAME>"
            "</ETHERNET-COMMUNICATION-CONNECTOR>"
            "</CONNECTORS>",
            root_tag="ECU-INSTANCE",
        )
        parser.readEcuInstanceConnectors(element, instance)
        assert len(instance.getConnectors()) == 1

    def test_readEcuInstanceConnectors_lin(self, parser):
        from armodel.models import EcuInstance
        instance = EcuInstance(parent=_autosar_root(), short_name="ecu")
        element = _snip(
            "<CONNECTORS>"
            "<LIN-COMMUNICATION-CONNECTOR>"
            "<SHORT-NAME>conn</SHORT-NAME>"
            "</LIN-COMMUNICATION-CONNECTOR>"
            "</CONNECTORS>",
            root_tag="ECU-INSTANCE",
        )
        parser.readEcuInstanceConnectors(element, instance)
        assert len(instance.getConnectors()) == 1

    def test_readEcuInstanceConnectors_flexray(self, parser):
        from armodel.models import EcuInstance
        instance = EcuInstance(parent=_autosar_root(), short_name="ecu")
        element = _snip(
            "<CONNECTORS>"
            "<FLEXRAY-COMMUNICATION-CONNECTOR>"
            "<SHORT-NAME>conn</SHORT-NAME>"
            "</FLEXRAY-COMMUNICATION-CONNECTOR>"
            "</CONNECTORS>",
            root_tag="ECU-INSTANCE",
        )
        parser.readEcuInstanceConnectors(element, instance)
        assert len(instance.getConnectors()) == 1

    def test_readEcuInstanceConnectors_unsupported_warns(self, warning_parser, caplog):
        from armodel.models import EcuInstance
        instance = EcuInstance(parent=_autosar_root(), short_name="ecu")
        element = _snip(
            "<CONNECTORS><BAD/></CONNECTORS>",
            root_tag="ECU-INSTANCE",
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readEcuInstanceConnectors(element, instance)
        assert any("Unsupported Communication Connector" in r.getMessage() for r in caplog.records)

    def test_readCommunicationConnector_sets_commControllerRef(self, parser):
        from armodel.models import CanCommunicationConnector
        from armodel.models import EcuInstance
        instance = EcuInstance(parent=_autosar_root(), short_name="ecu")
        conn = CanCommunicationConnector(parent=instance, short_name="conn")
        element = _snip(
            "<SHORT-NAME>conn</SHORT-NAME>"
            "<COMM-CONTROLLER-REF DEST='COMMUNICATION-CONTROLLER'>/ctrl</COMM-CONTROLLER-REF>"
            "<PNC-GATEWAY-TYPE>active</PNC-GATEWAY-TYPE>",
            root_tag="CAN-COMMUNICATION-CONNECTOR",
        )
        parser.readCommunicationConnector(element, conn)
        assert conn.getCommControllerRef().getValue() == "/ctrl"

    def test_readEthernetCommunicationConnector_sets_maximumTransmissionUnit(
        self, parser
    ):
        from armodel.models import EthernetCommunicationConnector
        from armodel.models import EcuInstance
        instance = EcuInstance(parent=_autosar_root(), short_name="ecu")
        conn = EthernetCommunicationConnector(parent=instance, short_name="conn")
        element = _snip(
            "<SHORT-NAME>conn</SHORT-NAME>"
            "<MAXIMUM-TRANSMISSION-UNIT>1500</MAXIMUM-TRANSMISSION-UNIT>",
            root_tag="ETHERNET-COMMUNICATION-CONNECTOR",
        )
        parser.readEthernetCommunicationConnector(element, conn)
        assert conn.getMaximumTransmissionUnit() == 1500

    def test_readEthernetCommunicationConnectorNetworkEndpointRefs_adds_ref(
        self, parser
    ):
        from armodel.models import EthernetCommunicationConnector
        from armodel.models import EcuInstance
        instance = EcuInstance(parent=_autosar_root(), short_name="ecu")
        conn = EthernetCommunicationConnector(parent=instance, short_name="conn")
        element = _snip(
            "<NETWORK-ENDPOINT-REFS>"
            "<NETWORK-ENDPOINT-REF DEST='NETWORK-ENDPOINT'>/ne</NETWORK-ENDPOINT-REF>"
            "</NETWORK-ENDPOINT-REFS>",
            root_tag="ETHERNET-COMMUNICATION-CONNECTOR",
        )
        parser.readEthernetCommunicationConnectorNetworkEndpointRefs(element, conn)
        assert len(conn.getNetworkEndpointRefs()) == 1

    def test_readCommunicationConnectorEcuCommPortInstances_framePort(self, parser):
        from armodel.models import CanCommunicationConnector
        from armodel.models import EcuInstance
        instance = EcuInstance(parent=_autosar_root(), short_name="ecu")
        conn = CanCommunicationConnector(parent=instance, short_name="conn")
        element = _snip(
            "<ECU-COMM-PORT-INSTANCES>"
            "<FRAME-PORT>"
            "<SHORT-NAME>fp</SHORT-NAME>"
            "<COMMUNICATION-DIRECTION>in</COMMUNICATION-DIRECTION>"
            "</FRAME-PORT>"
            "</ECU-COMM-PORT-INSTANCES>",
            root_tag="CAN-COMMUNICATION-CONNECTOR",
        )
        parser.readCommunicationConnectorEcuCommPortInstances(element, conn)
        assert len(conn.getEcuCommPortInstances()) == 1

    def test_readCommunicationConnectorEcuCommPortInstances_ipduPort(self, parser):
        from armodel.models import EthernetCommunicationConnector
        from armodel.models import EcuInstance
        instance = EcuInstance(parent=_autosar_root(), short_name="ecu")
        conn = EthernetCommunicationConnector(parent=instance, short_name="conn")
        element = _snip(
            "<ECU-COMM-PORT-INSTANCES>"
            "<I-PDU-PORT>"
            "<SHORT-NAME>ip</SHORT-NAME>"
            "<KEY-ID>1</KEY-ID>"
            "</I-PDU-PORT>"
            "</ECU-COMM-PORT-INSTANCES>",
            root_tag="ETHERNET-COMMUNICATION-CONNECTOR",
        )
        parser.readCommunicationConnectorEcuCommPortInstances(element, conn)
        assert len(conn.getEcuCommPortInstances()) == 1

    def test_readCommunicationConnectorEcuCommPortInstances_iSignalPort(self, parser):
        from armodel.models import CanCommunicationConnector
        from armodel.models import EcuInstance
        instance = EcuInstance(parent=_autosar_root(), short_name="ecu")
        conn = CanCommunicationConnector(parent=instance, short_name="conn")
        element = _snip(
            "<ECU-COMM-PORT-INSTANCES>"
            "<I-SIGNAL-PORT>"
            "<SHORT-NAME>sp</SHORT-NAME>"
            "<TIMEOUT><VALUE>0.1</VALUE></TIMEOUT>"
            "</I-SIGNAL-PORT>"
            "</ECU-COMM-PORT-INSTANCES>",
            root_tag="CAN-COMMUNICATION-CONNECTOR",
        )
        parser.readCommunicationConnectorEcuCommPortInstances(element, conn)
        assert len(conn.getEcuCommPortInstances()) == 1

    def test_readCommunicationConnectorEcuCommPortInstances_unsupported_raises(
        self, parser
    ):
        from armodel.models import CanCommunicationConnector
        from armodel.models import EcuInstance
        instance = EcuInstance(parent=_autosar_root(), short_name="ecu")
        conn = CanCommunicationConnector(parent=instance, short_name="conn")
        element = _snip(
            "<ECU-COMM-PORT-INSTANCES><BAD/></ECU-COMM-PORT-INSTANCES>",
            root_tag="CAN-COMMUNICATION-CONNECTOR",
        )
        with pytest.raises(Exception):
            parser.readCommunicationConnectorEcuCommPortInstances(element, conn)

    def test_readFramePort_sets_communicationDirection(self, parser):
        from armodel.models import FramePort
        from armodel.models import CanCommunicationConnector
        from armodel.models import EcuInstance
        instance = EcuInstance(parent=_autosar_root(), short_name="ecu")
        conn = CanCommunicationConnector(parent=instance, short_name="conn")
        port = FramePort(parent=conn, short_name="fp")
        element = _snip(
            "<SHORT-NAME>fp</SHORT-NAME>"
            "<COMMUNICATION-DIRECTION>in</COMMUNICATION-DIRECTION>",
            root_tag="FRAME-PORT",
        )
        parser.readFramePort(element, port)
        assert port.getCommunicationDirection() == "in"

    def test_readIPduPort_sets_keyId(self, parser):
        from armodel.models import IPduPort
        from armodel.models import EthernetCommunicationConnector
        from armodel.models import EcuInstance
        instance = EcuInstance(parent=_autosar_root(), short_name="ecu")
        conn = EthernetCommunicationConnector(parent=instance, short_name="conn")
        port = IPduPort(parent=conn, short_name="ip")
        element = _snip(
            "<SHORT-NAME>ip</SHORT-NAME>"
            "<KEY-ID>1</KEY-ID>"
            "<RX-SECURITY-VERIFICATION>true</RX-SECURITY-VERIFICATION>",
            root_tag="I-PDU-PORT",
        )
        parser.readIPduPort(element, port)
        assert port.getKeyId() == 1

    def test_readISignalPort_sets_timeout(self, parser):
        from armodel.models import ISignalPort
        from armodel.models import CanCommunicationConnector
        from armodel.models import EcuInstance
        instance = EcuInstance(parent=_autosar_root(), short_name="ecu")
        conn = CanCommunicationConnector(parent=instance, short_name="conn")
        port = ISignalPort(parent=conn, short_name="sp")
        element = _snip(
            "<SHORT-NAME>sp</SHORT-NAME>"
            "<TIMEOUT><VALUE>0.1</VALUE></TIMEOUT>",
            root_tag="I-SIGNAL-PORT",
        )
        parser.readISignalPort(element, port)
        assert port.getTimeout().getValue() == 0.1

    def test_readEcuInstanceAssociatedComIPduGroupRefs_adds_ref(self, parser):
        from armodel.models import EcuInstance
        instance = EcuInstance(parent=_autosar_root(), short_name="ecu")
        element = _snip(
            "<ASSOCIATED-COM-I-PDU-GROUP-REFS>"
            "<ASSOCIATED-COM-I-PDU-GROUP-REF DEST='I-PDU-GROUP'>/grp</ASSOCIATED-COM-I-PDU-GROUP-REF>"
            "</ASSOCIATED-COM-I-PDU-GROUP-REFS>",
            root_tag="ECU-INSTANCE",
        )
        parser.readEcuInstanceAssociatedComIPduGroupRefs(element, instance)
        assert len(instance.getAssociatedComIPduGroupRefs()) == 1

    def test_readCommunicationController_sets_wakeUpByControllerSupported(self, parser):
        from armodel.models import EthernetCommunicationController
        from armodel.models import EcuInstance
        instance = EcuInstance(parent=_autosar_root(), short_name="ecu")
        ctrl = EthernetCommunicationController(parent=instance, short_name="ctrl")
        element = _snip(
            "<WAKE-UP-BY-CONTROLLER-SUPPORTED>true</WAKE-UP-BY-CONTROLLER-SUPPORTED>",
            root_tag="ETHERNET-COMMUNICATION-CONTROLLER-CONDITIONAL",
        )
        parser.readCommunicationController(element, ctrl)
        assert ctrl.getWakeUpByControllerSupported() == True

    def test_readEthernetCommunicationControllerCouplingPorts_creates_port(self, parser):
        from armodel.models import EthernetCommunicationController
        from armodel.models import EcuInstance
        instance = EcuInstance(parent=_autosar_root(), short_name="ecu")
        ctrl = EthernetCommunicationController(parent=instance, short_name="ctrl")
        element = _snip(
            "<COUPLING-PORTS>"
            "<COUPLING-PORT>"
            "<SHORT-NAME>cp</SHORT-NAME>"
            "</COUPLING-PORT>"
            "</COUPLING-PORTS>",
            root_tag="ETHERNET-COMMUNICATION-CONTROLLER-CONDITIONAL",
        )
        parser.readEthernetCommunicationControllerCouplingPorts(element, ctrl)
        assert len(ctrl.getCouplingPorts()) == 1

    def test_readCouplingPort_sets_macLayerType(self, parser):
        from armodel.models import CouplingPort
        from armodel.models import EthernetCommunicationController
        from armodel.models import EcuInstance
        instance = EcuInstance(parent=_autosar_root(), short_name="ecu")
        ctrl = EthernetCommunicationController(parent=instance, short_name="ctrl")
        port = CouplingPort(parent=ctrl, short_name="cp")
        element = _snip(
            "<SHORT-NAME>cp</SHORT-NAME>"
            "<MAC-LAYER-TYPE>ethernet</MAC-LAYER-TYPE>",
            root_tag="COUPLING-PORT",
        )
        parser.readCouplingPort(element, port)
        assert port.getMacLayerType() == "ethernet"