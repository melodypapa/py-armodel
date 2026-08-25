"""Phase G: targeted tests for uncovered communication and network handlers."""

import logging
import xml.etree.ElementTree as ET
from unittest.mock import MagicMock

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
            "<SHORT-NAME>canCluster</SHORT-NAME>" "<CAN-CLUSTER-VARIANTS>" "<CAN-CLUSTER-CONDITIONAL>" "<BAUDRATE>500000</BAUDRATE>" "</CAN-CLUSTER-CONDITIONAL>" "</CAN-CLUSTER-VARIANTS>",
            root_tag="CAN-CLUSTER",
        )
        parser.readCanCluster(element, cluster)
        assert cluster.getShortName() == "canCluster"

    def test_readCanCluster_sets_baudrate(self, parser):
        from armodel.models import CanCluster

        cluster = CanCluster(parent=_autosar_root(), short_name="c")
        element = _snip(
            "<SHORT-NAME>c</SHORT-NAME>" "<CAN-CLUSTER-VARIANTS>" "<CAN-CLUSTER-CONDITIONAL>" "<BAUDRATE>500000</BAUDRATE>" "</CAN-CLUSTER-CONDITIONAL>" "</CAN-CLUSTER-VARIANTS>",
            root_tag="CAN-CLUSTER",
        )
        parser.readCanCluster(element, cluster)
        assert cluster.getBaudrate() is not None

    def test_readCanCluster_sets_canXlBaudrate(self, parser):
        from armodel.models import CanCluster

        cluster = CanCluster(parent=_autosar_root(), short_name="c")
        element = _snip(
            "<SHORT-NAME>c</SHORT-NAME>" "<CAN-CLUSTER-VARIANTS>" "<CAN-CLUSTER-CONDITIONAL>" "<CAN-XL-BAUDRATE>10000000</CAN-XL-BAUDRATE>" "</CAN-CLUSTER-CONDITIONAL>" "</CAN-CLUSTER-VARIANTS>",
            root_tag="CAN-CLUSTER",
        )
        parser.readCanCluster(element, cluster)
        assert cluster.getCanXlBaudrate() is not None
        assert cluster.getCanXlBaudrate().getValue() == 10000000

    def test_readCanCluster_sets_canFdBaudrate(self, parser):
        from armodel.models import CanCluster

        cluster = CanCluster(parent=_autosar_root(), short_name="c")
        element = _snip(
            "<SHORT-NAME>c</SHORT-NAME>" "<CAN-CLUSTER-VARIANTS>" "<CAN-CLUSTER-CONDITIONAL>" "<CAN-FD-BAUDRATE>2000000</CAN-FD-BAUDRATE>" "</CAN-CLUSTER-CONDITIONAL>" "</CAN-CLUSTER-VARIANTS>",
            root_tag="CAN-CLUSTER",
        )
        parser.readCanCluster(element, cluster)
        assert cluster.getCanFdBaudrate() is not None
        assert cluster.getCanFdBaudrate().getValue() == 2000000

    def test_getCanClusterBusOffRecovery_sets_borTimeL1(self, parser):

        element = _snip(
            "<BUS-OFF-RECOVERY>" "<BOR-TIME-L-1>0.1</BOR-TIME-L-1>" "</BUS-OFF-RECOVERY>",
            root_tag="ROOT",
        )
        recovery = parser.getCanClusterBusOffRecovery(element, "BUS-OFF-RECOVERY")
        assert recovery is not None
        assert recovery.getBorTimeL1() is not None
        assert recovery.getBorTimeL1().getValue() == 0.1

    def test_getCanClusterBusOffRecovery_sets_borTimeL2(self, parser):

        element = _snip(
            "<BUS-OFF-RECOVERY>" "<BOR-TIME-L-2>0.2</BOR-TIME-L-2>" "</BUS-OFF-RECOVERY>",
            root_tag="ROOT",
        )
        recovery = parser.getCanClusterBusOffRecovery(element, "BUS-OFF-RECOVERY")
        assert recovery is not None
        assert recovery.getBorTimeL2() is not None
        assert recovery.getBorTimeL2().getValue() == 0.2

    def test_getCanClusterBusOffRecovery_sets_borCounterL1ToL2(self, parser):

        element = _snip(
            "<BUS-OFF-RECOVERY>" "<BOR-COUNTER-L-1-TO-L-2>10</BOR-COUNTER-L-1-TO-L-2>" "</BUS-OFF-RECOVERY>",
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
            "<BUS-OFF-RECOVERY>" "<BOR-TIME-L-1>0.1</BOR-TIME-L-1>" "</BUS-OFF-RECOVERY>",
            root_tag="CAN-CLUSTER-CONDITIONAL",
        )
        parser.readAbstractCanCluster(element, cluster)
        assert cluster.getBusOffRecovery() is not None

    def test_readCommunicationClusterPhysicalChannels_canPhysical(self, parser):
        from armodel.models import CanCluster

        cluster = CanCluster(parent=_autosar_root(), short_name="c")
        element = _snip(
            "<PHYSICAL-CHANNELS>" "<CAN-PHYSICAL-CHANNEL><SHORT-NAME>ch1</SHORT-NAME></CAN-PHYSICAL-CHANNEL>" "</PHYSICAL-CHANNELS>",
            root_tag="CAN-CLUSTER-CONDITIONAL",
        )
        parser.readCommunicationClusterPhysicalChannels(element, cluster)
        assert len(cluster.getPhysicalChannels()) == 1

    def test_readCommunicationClusterPhysicalChannels_unsupported_warns(self, warning_parser, caplog):
        from armodel.models import CanCluster

        cluster = CanCluster(parent=_autosar_root(), short_name="c")
        element = _snip(
            "<PHYSICAL-CHANNELS><BAD/></PHYSICAL-CHANNELS>",
            root_tag="CAN-CLUSTER-CONDITIONAL",
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readCommunicationClusterPhysicalChannels(element, cluster)
        assert any("Unsupported Physical Channel" in r.getMessage() for r in caplog.records)

    def test_readCanPhysicalChannel_reads_channel(self, parser):
        from armodel.models import CanCluster, CanPhysicalChannel

        cluster = CanCluster(parent=_autosar_root(), short_name="c")
        channel = CanPhysicalChannel(parent=cluster, short_name="ch")
        element = _snip("<SHORT-NAME>ch</SHORT-NAME>", root_tag="CAN-PHYSICAL-CHANNEL")
        parser.readCanPhysicalChannel(element, channel)
        assert channel.getShortName() == "ch"

    def test_readCommunicationCluster_sets_protocol(self, parser):
        from armodel.models import CanCluster

        cluster = CanCluster(parent=_autosar_root(), short_name="c")
        element = _snip(
            "<BAUDRATE>500000</BAUDRATE>" "<PROTOCOL-NAME>CAN</PROTOCOL-NAME>" "<PROTOCOL-VERSION>2.0</PROTOCOL-VERSION>",
            root_tag="CAN-CLUSTER-CONDITIONAL",
        )
        parser.readCommunicationCluster(element, cluster)
        assert cluster.getBaudrate() is not None
        assert cluster.getBaudrate().getValue() == 500000
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
            "<SHORT-NAME>linCluster</SHORT-NAME>" "<LIN-CLUSTER-VARIANTS>" "<LIN-CLUSTER-CONDITIONAL>" "<BAUDRATE>20000</BAUDRATE>" "</LIN-CLUSTER-CONDITIONAL>" "</LIN-CLUSTER-VARIANTS>",
            root_tag="LIN-CLUSTER",
        )
        parser.readLinCluster(element, cluster)
        assert cluster.getShortName() == "linCluster"

    def test_readLinCluster_sets_baudrate(self, parser):
        from armodel.models import LinCluster

        cluster = LinCluster(parent=_autosar_root(), short_name="l")
        element = _snip(
            "<SHORT-NAME>l</SHORT-NAME>" "<LIN-CLUSTER-VARIANTS>" "<LIN-CLUSTER-CONDITIONAL>" "<BAUDRATE>20000</BAUDRATE>" "</LIN-CLUSTER-CONDITIONAL>" "</LIN-CLUSTER-VARIANTS>",
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
        from armodel.models import LinCluster, LinPhysicalChannel

        cluster = LinCluster(parent=_autosar_root(), short_name="l")
        channel = LinPhysicalChannel(parent=cluster, short_name="ch")
        element = _snip("<SHORT-NAME>ch</SHORT-NAME>", root_tag="LIN-PHYSICAL-CHANNEL")
        parser.readLinPhysicalChannel(element, channel)
        assert channel.getShortName() == "ch"

    def test_readLinScheduleTable_sets_properties(self, parser):
        from armodel.models import LinCluster, LinPhysicalChannel, LinScheduleTable

        cluster = LinCluster(parent=_autosar_root(), short_name="l")
        channel = LinPhysicalChannel(parent=cluster, short_name="ch")
        table = LinScheduleTable(parent=channel, short_name="tbl")
        element = _snip(
            "<SHORT-NAME>tbl</SHORT-NAME>" "<RESUME-POSITION>enabled</RESUME-POSITION>" "<RUN-MODE>continuous</RUN-MODE>",
            root_tag="LIN-SCHEDULE-TABLE",
        )
        parser.readLinScheduleTable(element, table)
        assert table.getResumePosition() is not None
        assert table.getResumePosition().getValue() == "enabled"
        assert table.getRunMode() is not None
        assert table.getRunMode().getValue() == "continuous"

    def test_readLinPhysicalChannelScheduleTables_creates_table(self, parser):
        from armodel.models import LinCluster, LinPhysicalChannel

        cluster = LinCluster(parent=_autosar_root(), short_name="l")
        channel = LinPhysicalChannel(parent=cluster, short_name="ch")
        element = _snip(
            "<SCHEDULE-TABLES>" "<LIN-SCHEDULE-TABLE><SHORT-NAME>tbl</SHORT-NAME></LIN-SCHEDULE-TABLE>" "</SCHEDULE-TABLES>",
            root_tag="LIN-PHYSICAL-CHANNEL",
        )
        parser.readLinPhysicalChannelScheduleTables(element, channel)
        assert len(channel.getScheduleTables()) == 1

    def test_readLinPhysicalChannelScheduleTables_unsupported_warns(self, warning_parser, caplog):
        from armodel.models import LinCluster, LinPhysicalChannel

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
        from armodel.models import LinCluster, LinFrameTriggering, LinPhysicalChannel

        cluster = LinCluster(parent=_autosar_root(), short_name="l")
        channel = LinPhysicalChannel(parent=cluster, short_name="ch")
        triggering = LinFrameTriggering(parent=channel, short_name="ft")
        element = _snip(
            "<SHORT-NAME>ft</SHORT-NAME>" "<IDENTIFIER>1</IDENTIFIER>" "<LIN-CHECKSUM>enhanced</LIN-CHECKSUM>",
            root_tag="LIN-FRAME-TRIGGERING",
        )
        parser.readLinFrameTriggering(element, triggering)
        assert triggering.getIdentifier() is not None
        assert triggering.getIdentifier().getValue() == 1
        assert triggering.getLinChecksum() is not None
        assert triggering.getLinChecksum().getValue() == "enhanced"

    def test_getApplicationEntry_returns_entry(self, parser):

        element = _snip(
            "<DELAY>0.01</DELAY>" "<POSITION-IN-TABLE>1</POSITION-IN-TABLE>" "<FRAME-TRIGGERING-REF DEST='FRAME-TRIGGERING'>/ft</FRAME-TRIGGERING-REF>",
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
            "<SHORT-NAME>fr</SHORT-NAME>" "<FLEXRAY-CLUSTER-VARIANTS>" "<FLEXRAY-CLUSTER-CONDITIONAL>" "<CYCLE>0.005</CYCLE>" "</FLEXRAY-CLUSTER-CONDITIONAL>" "</FLEXRAY-CLUSTER-VARIANTS>",
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
        assert cluster.getDetectNitError().getValue()

    def test_readFlexrayCluster_all_attrs(self, parser):
        from armodel.models import FlexrayCluster

        cluster = FlexrayCluster(parent=_autosar_root(), short_name="fr")
        element = _snip(
            "<SHORT-NAME>fr</SHORT-NAME>"
            "<FLEXRAY-CLUSTER-VARIANTS>"
            "<FLEXRAY-CLUSTER-CONDITIONAL>"
            "<ACTION-POINT-OFFSET>2</ACTION-POINT-OFFSET>"
            "<BIT>0.1</BIT>"
            "<CAS-RX-LOW-MAX>10</CAS-RX-LOW-MAX>"
            "<COLD-START-ATTEMPTS>8</COLD-START-ATTEMPTS>"
            "<CYCLE>0.005</CYCLE>"
            "<CYCLE-COUNT-MAX>64</CYCLE-COUNT-MAX>"
            "<DETECT-NIT-ERROR>true</DETECT-NIT-ERROR>"
            "<DYNAMIC-SLOT-IDLE-PHASE>2</DYNAMIC-SLOT-IDLE-PHASE>"
            "<IGNORE-AFTER-TX>5</IGNORE-AFTER-TX>"
            "<LISTEN-NOISE>3</LISTEN-NOISE>"
            "<MACRO-PER-CYCLE>36</MACRO-PER-CYCLE>"
            "<MACROTICK-DURATION>0.001</MACROTICK-DURATION>"
            "<MAX-WITHOUT-CLOCK-CORRECTION-FATAL>2</MAX-WITHOUT-CLOCK-CORRECTION-FATAL>"
            "<MAX-WITHOUT-CLOCK-CORRECTION-PASSIVE>3</MAX-WITHOUT-CLOCK-CORRECTION-PASSIVE>"
            "<MINISLOT-ACTION-POINT-OFFSET>1</MINISLOT-ACTION-POINT-OFFSET>"
            "<MINISLOT-DURATION>10</MINISLOT-DURATION>"
            "<NETWORK-IDLE-TIME>20</NETWORK-IDLE-TIME>"
            "<NETWORK-MANAGEMENT-VECTOR-LENGTH>12</NETWORK-MANAGEMENT-VECTOR-LENGTH>"
            "<NUMBER-OF-MINISLOTS>790</NUMBER-OF-MINISLOTS>"
            "<NUMBER-OF-STATIC-SLOTS>70</NUMBER-OF-STATIC-SLOTS>"
            "<OFFSET-CORRECTION-START>2</OFFSET-CORRECTION-START>"
            "<PAYLOAD-LENGTH-STATIC>16</PAYLOAD-LENGTH-STATIC>"
            "<SAFETY-MARGIN>2</SAFETY-MARGIN>"
            "<SAMPLE-CLOCK-PERIOD>0.05</SAMPLE-CLOCK-PERIOD>"
            "<STATIC-SLOT-DURATION>100</STATIC-SLOT-DURATION>"
            "<SYMBOL-WINDOW>101</SYMBOL-WINDOW>"
            "<SYMBOL-WINDOW-ACTION-POINT-OFFSET>102</SYMBOL-WINDOW-ACTION-POINT-OFFSET>"
            "<SYNC-FRAME-ID-COUNT-MAX>15</SYNC-FRAME-ID-COUNT-MAX>"
            "<TRANCEIVER-STANDBY-DELAY>0.5</TRANCEIVER-STANDBY-DELAY>"
            "<TRANSMISSION-START-SEQUENCE-DURATION>4</TRANSMISSION-START-SEQUENCE-DURATION>"
            "<WAKEUP-RX-IDLE>60</WAKEUP-RX-IDLE>"
            "<WAKEUP-RX-LOW>180</WAKEUP-RX-LOW>"
            "<WAKEUP-RX-WINDOW>300</WAKEUP-RX-WINDOW>"
            "<WAKEUP-TX-ACTIVE>60</WAKEUP-TX-ACTIVE>"
            "<WAKEUP-TX-IDLE>180</WAKEUP-TX-IDLE>"
            "</FLEXRAY-CLUSTER-CONDITIONAL>"
            "</FLEXRAY-CLUSTER-VARIANTS>",
            root_tag="FLEXRAY-CLUSTER",
        )
        parser.readFlexrayCluster(element, cluster)
        assert cluster.getActionPointOffset().getValue() == 2
        assert cluster.getBit().getValue() == pytest.approx(0.1)
        assert cluster.getCasRxLowMax().getValue() == 10
        assert cluster.getColdStartAttempts().getValue() == 8
        assert cluster.getCycle().getValue() == pytest.approx(0.005)
        assert cluster.getCycleCountMax().getValue() == 64
        assert cluster.getDetectNitError().getValue() is True
        assert cluster.getDynamicSlotIdlePhase().getValue() == 2
        assert cluster.getIgnoreAfterTx().getValue() == 5
        assert cluster.getListenNoise().getValue() == 3
        assert cluster.getMacroPerCycle().getValue() == 36
        assert cluster.getMacrotickDuration().getValue() == pytest.approx(0.001)
        assert cluster.getMaxWithoutClockCorrectionFatal().getValue() == 2
        assert cluster.getMaxWithoutClockCorrectionPassive().getValue() == 3
        assert cluster.getMinislotActionPointOffset().getValue() == 1
        assert cluster.getMinislotDuration().getValue() == 10
        assert cluster.getNetworkIdleTime().getValue() == 20
        assert cluster.getNetworkManagementVectorLength().getValue() == 12
        assert cluster.getNumberOfMinislots().getValue() == 790
        assert cluster.getNumberOfStaticSlots().getValue() == 70
        assert cluster.getOffsetCorrectionStart().getValue() == 2
        assert cluster.getPayloadLengthStatic().getValue() == 16
        assert cluster.getSafetyMargin().getValue() == 2
        assert cluster.getSampleClockPeriod().getValue() == pytest.approx(0.05)
        assert cluster.getStaticSlotDuration().getValue() == 100
        assert cluster.getSymbolWindow().getValue() == 101
        assert cluster.getSymbolWindowActionPointOffset().getValue() == 102
        assert cluster.getSyncFrameIdCountMax().getValue() == 15
        assert cluster.getTranceiverStandbyDelay().getValue() == pytest.approx(0.5)
        assert cluster.getTransmissionStartSequenceDuration().getValue() == 4
        assert cluster.getWakeupRxIdle().getValue() == 60
        assert cluster.getWakeupRxLow().getValue() == 180
        assert cluster.getWakeupRxWindow().getValue() == 300
        assert cluster.getWakeupTxActive().getValue() == 60
        assert cluster.getWakeupTxIdle().getValue() == 180

    def test_readFlexrayPhysicalChannel_sets_channelName(self, parser):
        from armodel.models import FlexrayCluster, FlexrayPhysicalChannel

        cluster = FlexrayCluster(parent=_autosar_root(), short_name="fr")
        channel = FlexrayPhysicalChannel(parent=cluster, short_name="ch")
        element = _snip(
            "<SHORT-NAME>ch</SHORT-NAME>" "<CHANNEL-NAME>A</CHANNEL-NAME>",
            root_tag="FLEXRAY-PHYSICAL-CHANNEL",
        )
        parser.readFlexrayPhysicalChannel(element, channel)
        assert channel.getChannelName() is not None
        assert channel.getChannelName().getValue() == "A"

    def test_readFlexrayFrameTriggering_sets_messageId(self, parser):
        from armodel.models import FlexrayCluster, FlexrayFrameTriggering, FlexrayPhysicalChannel

        cluster = FlexrayCluster(parent=_autosar_root(), short_name="fr")
        channel = FlexrayPhysicalChannel(parent=cluster, short_name="ch")
        triggering = FlexrayFrameTriggering(parent=channel, short_name="ft")
        element = _snip(
            "<SHORT-NAME>ft</SHORT-NAME>" "<MESSAGE-ID>100</MESSAGE-ID>" "<ALLOW-DYNAMIC-L-SDU-LENGTH>true</ALLOW-DYNAMIC-L-SDU-LENGTH>",
            root_tag="FLEXRAY-FRAME-TRIGGERING",
        )
        parser.readFlexrayFrameTriggering(element, triggering)
        assert triggering.getMessageId() is not None
        assert triggering.getMessageId().getValue() == 100

    def test_readCycleRepetition_sets_baseCycle(self, parser):
        from armodel.models import CycleRepetition

        cycle = CycleRepetition()
        element = _snip(
            "<BASE-CYCLE>1</BASE-CYCLE>" "<CYCLE-REPETITION>1</CYCLE-REPETITION>",
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

    def test_readFlexrayFrameTriggeringAbsolutelyScheduledTimings_creates_timing(self, parser):
        from armodel.models import FlexrayCluster, FlexrayFrameTriggering, FlexrayPhysicalChannel

        cluster = FlexrayCluster(parent=_autosar_root(), short_name="fr")
        channel = FlexrayPhysicalChannel(parent=cluster, short_name="ch")
        triggering = FlexrayFrameTriggering(parent=channel, short_name="ft")
        element = _snip(
            "<ABSOLUTELY-SCHEDULED-TIMINGS>" "<FLEXRAY-ABSOLUTELY-SCHEDULED-TIMING>" "<SLOT-ID>5</SLOT-ID>" "</FLEXRAY-ABSOLUTELY-SCHEDULED-TIMING>" "</ABSOLUTELY-SCHEDULED-TIMINGS>",
            root_tag="FLEXRAY-FRAME-TRIGGERING",
        )
        parser.readFlexrayFrameTriggeringAbsolutelyScheduledTimings(element, triggering)
        assert len(triggering.getAbsolutelyScheduledTimings()) == 1

    def test_readTtcanAbsolutelyScheduledTiming_sets_fields(self, parser):
        from armodel.models import TtcanAbsolutelyScheduledTiming

        timing = TtcanAbsolutelyScheduledTiming()
        element = _snip(
            "<COMMUNICATION-CYCLE>"
            "<CYCLE-REPETITION>"
            "<BASE-CYCLE>1</BASE-CYCLE>"
            "<CYCLE-REPETITION>cyclic</CYCLE-REPETITION>"
            "</CYCLE-REPETITION>"
            "</COMMUNICATION-CYCLE>"
            "<TIME-MARK>16</TIME-MARK>"
            "<TRIGGER>RX-TRIGGER</TRIGGER>",
            root_tag="TTCAN-ABSOLUTELY-SCHEDULED-TIMING",
        )
        parser.readTtcanAbsolutelyScheduledTiming(element, timing)
        assert timing.getCommunicationCycle() is not None
        assert timing.getCommunicationCycle().getBaseCycle().getValue() == 1
        assert timing.getCommunicationCycle().getCycleRepetition().getValue() == "cyclic"
        assert timing.getTimeMark().getValue() == 16
        assert timing.getTrigger().getValue() == "RX-TRIGGER"


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

    def test_readEthernetClusterMacMulticastGroups_unsupported_warns(self, warning_parser, caplog):
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
        from armodel.models import EthernetCluster, MacMulticastGroup

        cluster = EthernetCluster(parent=_autosar_root(), short_name="eth")
        group = MacMulticastGroup(parent=cluster, short_name="mcg")
        element = _snip(
            "<SHORT-NAME>mcg</SHORT-NAME>" "<MAC-MULTICAST-ADDRESS>01:02:03:04:05:06</MAC-MULTICAST-ADDRESS>",
            root_tag="MAC-MULTICAST-GROUP",
        )
        parser.readMacMulticastGroup(element, group)
        assert group.getMacMulticastAddress() is not None
        assert group.getMacMulticastAddress().getValue() == "01:02:03:04:05:06"

    def test_readEthernetPhysicalChannel_reads_channel(self, parser):
        from armodel.models import EthernetCluster, EthernetPhysicalChannel

        cluster = EthernetCluster(parent=_autosar_root(), short_name="eth")
        channel = EthernetPhysicalChannel(parent=cluster, short_name="ch")
        element = _snip("<SHORT-NAME>ch</SHORT-NAME>", root_tag="ETHERNET-PHYSICAL-CHANNEL")
        parser.readEthernetPhysicalChannel(element, channel)
        assert channel.getShortName() == "ch"

    def test_readEthernetPhysicalChannelVlan_creates_vlan(self, parser):
        from armodel.models import EthernetCluster, EthernetPhysicalChannel

        cluster = EthernetCluster(parent=_autosar_root(), short_name="eth")
        channel = EthernetPhysicalChannel(parent=cluster, short_name="ch")
        element = _snip(
            "<VLAN>" "<SHORT-NAME>vlan1</SHORT-NAME>" "<VLAN-IDENTIFIER>100</VLAN-IDENTIFIER>" "</VLAN>",
            root_tag="ETHERNET-PHYSICAL-CHANNEL",
        )
        parser.readEthernetPhysicalChannelVlan(element, channel)
        assert channel.getVlan() is not None

    def test_readEthernetPhysicalChannelNetworkEndPoints_creates_endpoint(self, parser):
        from armodel.models import EthernetCluster, EthernetPhysicalChannel

        cluster = EthernetCluster(parent=_autosar_root(), short_name="eth")
        channel = EthernetPhysicalChannel(parent=cluster, short_name="ch")
        element = _snip(
            "<NETWORK-ENDPOINTS>" "<NETWORK-ENDPOINT>" "<SHORT-NAME>ne1</SHORT-NAME>" "<PRIORITY>1</PRIORITY>" "</NETWORK-ENDPOINT>" "</NETWORK-ENDPOINTS>",
            root_tag="ETHERNET-PHYSICAL-CHANNEL",
        )
        parser.readEthernetPhysicalChannelNetworkEndPoints(element, channel)
        assert len(channel.getNetworkEndpoints()) == 1

    def test_readNetworkEndPoint_sets_priority(self, parser):
        from armodel.models import EthernetCluster, EthernetPhysicalChannel, NetworkEndpoint

        cluster = EthernetCluster(parent=_autosar_root(), short_name="eth")
        channel = EthernetPhysicalChannel(parent=cluster, short_name="ch")
        endpoint = NetworkEndpoint(parent=channel, short_name="ne")
        element = _snip(
            "<SHORT-NAME>ne</SHORT-NAME>" "<PRIORITY>1</PRIORITY>",
            root_tag="NETWORK-ENDPOINT",
        )
        parser.readNetworkEndPoint(element, endpoint)
        assert endpoint.getPriority() is not None
        assert endpoint.getPriority().getValue() == 1

    def test_getIpv6Configuration_sets_ipv6Address(self, parser):
        element = _snip(
            "<IPV-6-ADDRESS>fe80::1</IPV-6-ADDRESS>" "<IPV-6-ADDRESS-SOURCE>manual</IPV-6-ADDRESS-SOURCE>" "<IP-ADDRESS-PREFIX-LENGTH>64</IP-ADDRESS-PREFIX-LENGTH>",
            root_tag="IPV-6-CONFIGURATION",
        )
        config = parser.getIpv6Configuration(element)
        assert config is not None
        assert config.getIpv6Address() is not None
        assert config.getIpv6Address().getValue() == "fe80::1"

    def test_readNetworkEndPointNetworkEndPointAddress_adds_ipv6(self, parser):
        from armodel.models import EthernetCluster, EthernetPhysicalChannel, NetworkEndpoint

        cluster = EthernetCluster(parent=_autosar_root(), short_name="eth")
        channel = EthernetPhysicalChannel(parent=cluster, short_name="ch")
        endpoint = NetworkEndpoint(parent=channel, short_name="ne")
        element = _snip(
            "<NETWORK-ENDPOINT-ADDRESSES>" "<IPV-6-CONFIGURATION>" "<IPV-6-ADDRESS>fe80::1</IPV-6-ADDRESS>" "</IPV-6-CONFIGURATION>" "</NETWORK-ENDPOINT-ADDRESSES>",
            root_tag="NETWORK-ENDPOINT",
        )
        parser.readNetworkEndPointNetworkEndPointAddress(element, endpoint)
        assert len(endpoint.getNetworkEndpointAddresses()) == 1

    def test_getDoIpEntity_sets_role(self, parser):
        element = _snip(
            "<INFRASTRUCTURE-SERVICES>" "<DO-IP-ENTITY>" "<DO-IP-ENTITY-ROLE>server</DO-IP-ENTITY-ROLE>" "</DO-IP-ENTITY>" "</INFRASTRUCTURE-SERVICES>",
            root_tag="ROOT",
        )
        services = parser.getInfrastructureServices(element, "INFRASTRUCTURE-SERVICES")
        assert services is not None
        assert services.getDoIpEntity() is not None
        assert services.getDoIpEntity().getDoIpEntityRole() is not None
        assert services.getDoIpEntity().getDoIpEntityRole().getValue() == "server"

    def test_readEthernetPhysicalChannel_sets_soAdConfig(self, parser):
        from armodel.models import EthernetCluster, EthernetPhysicalChannel

        cluster = EthernetCluster(parent=_autosar_root(), short_name="eth")
        channel = EthernetPhysicalChannel(parent=cluster, short_name="ch")
        element = _snip(
            "<SHORT-NAME>ch</SHORT-NAME>" "<SO-AD-CONFIG>" "<CONNECTION-BUNDLES></CONNECTION-BUNDLES>" "<SOCKET-ADDRESSS></SOCKET-ADDRESSS>" "</SO-AD-CONFIG>",
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

    def test_readEthernetPhysicalChannelNetworkEndPoints_unsupported_warns(self, warning_parser, caplog):
        from armodel.models import EthernetCluster, EthernetPhysicalChannel

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
            "<SO-AD-CONFIG>" "<CONNECTION-BUNDLES></CONNECTION-BUNDLES>" "<SOCKET-ADDRESSS></SOCKET-ADDRESSS>" "</SO-AD-CONFIG>",
            root_tag="ROOT",
        )
        config = parser.getSoAdConfig(element, "SO-AD-CONFIG")
        assert config is not None

    def test_readSoAdConfigSocketAddresses_creates_address(self, parser):
        from armodel.models import SoAdConfig

        config = SoAdConfig()
        element = _snip(
            "<SOCKET-ADDRESSS>" "<SOCKET-ADDRESS>" "<SHORT-NAME>sa1</SHORT-NAME>" "<PORT-ADDRESS>5000</PORT-ADDRESS>" "</SOCKET-ADDRESS>" "</SOCKET-ADDRESSS>",
            root_tag="SO-AD-CONFIG",
        )
        parser.readSoAdConfigSocketAddresses(element, config)
        assert len(config.getSocketAddresses()) == 1

    def test_readSoAdConfigSocketAddresses_unsupported_warns(self, warning_parser, caplog):
        from armodel.models import SoAdConfig

        config = SoAdConfig()
        element = _snip(
            "<SOCKET-ADDRESSS><BAD/></SOCKET-ADDRESSS>",
            root_tag="SO-AD-CONFIG",
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readSoAdConfigSocketAddresses(element, config)
        assert any("Unsupported Socket Address" in r.getMessage() for r in caplog.records)

    def test_readSocketAddress_sets_differentiatedServiceField(self, parser):
        from armodel.models import SoAdConfig, SocketAddress

        config = SoAdConfig()
        address = SocketAddress(parent=config, short_name="sa")
        element = _snip(
            "<SHORT-NAME>sa</SHORT-NAME>" "<DIFFERENTIATED-SERVICE-FIELD>46</DIFFERENTIATED-SERVICE-FIELD>",
            root_tag="SOCKET-ADDRESS",
        )
        parser.readSocketAddress(element, address)
        assert address.getDifferentiatedServiceField() is not None
        assert address.getDifferentiatedServiceField().getValue() == 46

    def test_readSocketAddressApplicationEndpoint_creates_endpoint(self, parser):
        from armodel.models import SoAdConfig, SocketAddress

        config = SoAdConfig()
        address = SocketAddress(parent=config, short_name="sa")
        element = _snip(
            "<APPLICATION-ENDPOINT>" "<SHORT-NAME>ae1</SHORT-NAME>" "<PRIORITY>1</PRIORITY>" "</APPLICATION-ENDPOINT>",
            root_tag="SOCKET-ADDRESS",
        )
        parser.readSocketAddressApplicationEndpoint(element, address)
        assert address.getApplicationEndpoint() is not None

    def test_readSocketAddressMulticastConnectorRefs_adds_ref(self, parser):
        from armodel.models import SoAdConfig, SocketAddress

        config = SoAdConfig()
        address = SocketAddress(parent=config, short_name="sa")
        element = _snip(
            "<MULTICAST-CONNECTOR-REFS>" "<MULTICAST-CONNECTOR-REF DEST='COMMUNICATION-CONNECTOR'>/mc</MULTICAST-CONNECTOR-REF>" "</MULTICAST-CONNECTOR-REFS>",
            root_tag="SOCKET-ADDRESS",
        )
        parser.readSocketAddressMulticastConnectorRefs(element, address)
        assert len(address.getMulticastConnectorRefs()) == 1

    def test_readConsumedServiceInstanceConsumedEventGroups_creates_group(self, parser):
        from armodel.models import ApplicationEndpoint, ConsumedServiceInstance, SoAdConfig, SocketAddress

        config = SoAdConfig()
        address = SocketAddress(parent=config, short_name="sa")
        endpoint = ApplicationEndpoint(parent=address, short_name="ae")
        instance = ConsumedServiceInstance(parent=endpoint, short_name="csi")
        element = _snip(
            "<CONSUMED-EVENT-GROUPS>" "<CONSUMED-EVENT-GROUP>" "<SHORT-NAME>ceg</SHORT-NAME>" "<EVENT-GROUP-IDENTIFIER>1</EVENT-GROUP-IDENTIFIER>" "</CONSUMED-EVENT-GROUP>" "</CONSUMED-EVENT-GROUPS>",
            root_tag="CONSUMED-SERVICE-INSTANCE",
        )
        parser.readConsumedServiceInstanceConsumedEventGroups(element, instance)
        assert len(instance.getConsumedEventGroups()) == 1

    def test_readConsumedEventGroup_sets_eventGroupIdentifier(self, parser):
        from armodel.models import ApplicationEndpoint, ConsumedEventGroup, ConsumedServiceInstance, SoAdConfig, SocketAddress

        config = SoAdConfig()
        address = SocketAddress(parent=config, short_name="sa")
        endpoint = ApplicationEndpoint(parent=address, short_name="ae")
        instance = ConsumedServiceInstance(parent=endpoint, short_name="csi")
        group = ConsumedEventGroup(parent=instance, short_name="ceg")
        element = _snip(
            "<SHORT-NAME>ceg</SHORT-NAME>" "<EVENT-GROUP-IDENTIFIER>1</EVENT-GROUP-IDENTIFIER>",
            root_tag="CONSUMED-EVENT-GROUP",
        )
        parser.readConsumedEventGroup(element, group)
        assert group.getEventGroupIdentifier() is not None
        assert group.getEventGroupIdentifier().getValue() == 1

    def test_readConsumedEventGroupRoutingGroupRefs_adds_ref(self, parser):
        from armodel.models import ApplicationEndpoint, ConsumedEventGroup, ConsumedServiceInstance, SoAdConfig, SocketAddress

        config = SoAdConfig()
        address = SocketAddress(parent=config, short_name="sa")
        endpoint = ApplicationEndpoint(parent=address, short_name="ae")
        instance = ConsumedServiceInstance(parent=endpoint, short_name="csi")
        group = ConsumedEventGroup(parent=instance, short_name="ceg")
        element = _snip(
            "<ROUTING-GROUP-REFS>" "<ROUTING-GROUP-REF DEST='SO-AD-ROUTING-GROUP'>/rg</ROUTING-GROUP-REF>" "</ROUTING-GROUP-REFS>",
            root_tag="CONSUMED-EVENT-GROUP",
        )
        parser.readConsumedEventGroupRoutingGroupRefs(element, group)
        assert len(group.getRoutingGroupRefs()) == 1

    def test_getSdClientConfig_sets_ttl(self, parser):
        element = _snip(
            "<SD-CLIENT-CONFIG>" "<TTL>3600</TTL>" "</SD-CLIENT-CONFIG>",
            root_tag="ROOT",
        )
        config = parser.getSdClientConfig(element, "SD-CLIENT-CONFIG")
        assert config is not None
        assert config.getTtl() is not None
        assert config.getTtl().getValue() == 3600

    def test_getSdServerConfig_sets_ttl(self, parser):
        element = _snip(
            "<SD-SERVER-CONFIG>" "<TTL>3600</TTL>" "</SD-SERVER-CONFIG>",
            root_tag="ROOT",
        )
        config = parser.getSdServerConfig(element, "SD-SERVER-CONFIG")
        assert config is not None
        assert config.getTtl() is not None
        assert config.getTtl().getValue() == 3600

    def test_readProvidedServiceInstanceEventHandlers_creates_handler(self, parser):
        from armodel.models import ApplicationEndpoint, ProvidedServiceInstance, SoAdConfig, SocketAddress

        config = SoAdConfig()
        address = SocketAddress(parent=config, short_name="sa")
        endpoint = ApplicationEndpoint(parent=address, short_name="ae")
        instance = ProvidedServiceInstance(parent=endpoint, short_name="psi")
        element = _snip(
            "<EVENT-HANDLERS>" "<EVENT-HANDLER>" "<SHORT-NAME>eh</SHORT-NAME>" "<MULTICAST-THRESHOLD>10</MULTICAST-THRESHOLD>" "</EVENT-HANDLER>" "</EVENT-HANDLERS>",
            root_tag="PROVIDED-SERVICE-INSTANCE",
        )
        parser.readProvidedServiceInstanceEventHandlers(element, instance)
        assert len(instance.getEventHandlers()) == 1

    def test_readEventHandler_sets_multicastThreshold(self, parser):
        from armodel.models import ApplicationEndpoint, EventHandler, ProvidedServiceInstance, SoAdConfig, SocketAddress

        config = SoAdConfig()
        address = SocketAddress(parent=config, short_name="sa")
        endpoint = ApplicationEndpoint(parent=address, short_name="ae")
        instance = ProvidedServiceInstance(parent=endpoint, short_name="psi")
        handler = EventHandler(parent=instance, short_name="eh")
        element = _snip(
            "<SHORT-NAME>eh</SHORT-NAME>" "<MULTICAST-THRESHOLD>10</MULTICAST-THRESHOLD>",
            root_tag="EVENT-HANDLER",
        )
        parser.readEventHandler(element, handler)
        assert handler.getMulticastThreshold() is not None
        assert handler.getMulticastThreshold().getValue() == 10

    def test_readProvidedServiceInstance_sets_serviceIdentifier(self, parser):
        from armodel.models import ApplicationEndpoint, ProvidedServiceInstance, SoAdConfig, SocketAddress

        config = SoAdConfig()
        address = SocketAddress(parent=config, short_name="sa")
        endpoint = ApplicationEndpoint(parent=address, short_name="ae")
        instance = ProvidedServiceInstance(parent=endpoint, short_name="psi")
        element = _snip(
            "<SHORT-NAME>psi</SHORT-NAME>" "<SERVICE-IDENTIFIER>1234</SERVICE-IDENTIFIER>" "<INSTANCE-IDENTIFIER>1</INSTANCE-IDENTIFIER>",
            root_tag="PROVIDED-SERVICE-INSTANCE",
        )
        parser.readProvidedServiceInstance(element, instance)
        assert instance.getServiceIdentifier() is not None
        assert instance.getServiceIdentifier().getValue() == 1234

    def test_readSoAdConfigConnectionBundles_creates_bundle(self, parser):
        from armodel.models import SoAdConfig

        config = SoAdConfig()
        element = _snip(
            "<CONNECTION-BUNDLES>" "<SOCKET-CONNECTION-BUNDLE>" "<SHORT-NAME>scb</SHORT-NAME>" "</SOCKET-CONNECTION-BUNDLE>" "</CONNECTION-BUNDLES>",
            root_tag="SO-AD-CONFIG",
        )
        parser.readSoAdConfigConnectionBundles(element, config)
        assert len(config.getConnectionBundles()) == 1

    def test_readSocketConnectionBundleConnections_creates_connection(self, parser):
        from armodel.models import SoAdConfig

        config = SoAdConfig()
        bundle = config.createSocketConnectionBundle("scb")
        element = _snip(
            "<BUNDLED-CONNECTIONS>" "<SOCKET-CONNECTION>" "<SHORT-LABEL>conn1</SHORT-LABEL>" "</SOCKET-CONNECTION>" "</BUNDLED-CONNECTIONS>",
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
            "<HEADER-ID>100</HEADER-ID>" "<PDU-REF DEST='I-PDU'>/pdu</PDU-REF>",
            root_tag="SOCKET-CONNECTION-IPDU-IDENTIFIER",
        )
        ident = parser.getSocketConnectionIpduIdentifier(element)
        assert ident is not None
        assert ident.getHeaderId() is not None
        assert ident.getHeaderId().getValue() == 100

    def test_getSocketConnectionPdus_returns_list(self, parser):
        element = _snip(
            "<PDUS>" "<SOCKET-CONNECTION-IPDU-IDENTIFIER>" "<HEADER-ID>100</HEADER-ID>" "</SOCKET-CONNECTION-IPDU-IDENTIFIER>" "</PDUS>",
            root_tag="SOCKET-CONNECTION",
        )
        pdus = parser.getSocketConnectionPdus(element)
        assert len(pdus) == 1

    def test_readConsumedServiceInstanceConsumedEventGroups_unsupported_warns(self, warning_parser, caplog):
        from armodel.models import ApplicationEndpoint, ConsumedServiceInstance, SoAdConfig, SocketAddress

        config = SoAdConfig()
        address = SocketAddress(parent=config, short_name="sa")
        endpoint = ApplicationEndpoint(parent=address, short_name="ae")
        instance = ConsumedServiceInstance(parent=endpoint, short_name="csi")
        element = _snip(
            "<CONSUMED-EVENT-GROUPS><BAD/></CONSUMED-EVENT-GROUPS>",
            root_tag="CONSUMED-SERVICE-INSTANCE",
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readConsumedServiceInstanceConsumedEventGroups(element, instance)
        assert any("Unsupported ConsumedEventGroups" in r.getMessage() for r in caplog.records)

    def test_getInitialSdDelayConfig_sets_initialDelayMaxValue(self, parser):
        element = _snip(
            "<INITIAL-FIND-BEHAVIOR>"
            "<INITIAL-DELAY-MAX-VALUE>0.1</INITIAL-DELAY-MAX-VALUE>"
            "<INITIAL-DELAY-MIN-VALUE>0.01</INITIAL-DELAY-MIN-VALUE>"
            "<INITIAL-REPETITIONS-BASE-DELAY>0.05</INITIAL-REPETITIONS-BASE-DELAY>"
            "<INITIAL-REPETITIONS-MAX>3</INITIAL-REPETITIONS-MAX>"
            "</INITIAL-FIND-BEHAVIOR>",
            root_tag="ROOT",
        )
        config = parser.getInitialSdDelayConfig(element, "INITIAL-FIND-BEHAVIOR")
        assert config is not None
        assert config.getInitialDelayMaxValue() is not None
        assert config.getInitialDelayMaxValue().getValue() == 0.1

    def test_getRequestResponseDelay_sets_maxValue(self, parser):
        element = _snip(
            "<REQUEST-RESPONSE-DELAY>" "<MAX-VALUE>0.1</MAX-VALUE>" "<MIN-VALUE>0.01</MIN-VALUE>" "</REQUEST-RESPONSE-DELAY>",
            root_tag="ROOT",
        )
        delay = parser.getRequestResponseDelay(element, "REQUEST-RESPONSE-DELAY")
        assert delay is not None
        assert delay.getMaxValue() is not None
        assert delay.getMaxValue().getValue() == 0.1


class TestTransportProtocolHandlers:
    def test_getTpPort_sets_portNumber(self, parser):
        element = _snip(
            "<TP-PORT>" "<PORT-NUMBER>5000</PORT-NUMBER>" "<DYNAMICALLY-ASSIGNED>true</DYNAMICALLY-ASSIGNED>" "</TP-PORT>",
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
            "<UDP-TP-PORT>" "<PORT-NUMBER>5000</PORT-NUMBER>" "</UDP-TP-PORT>",
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
            "<TCP-TP-PORT>" "<PORT-NUMBER>5000</PORT-NUMBER>" "</TCP-TP-PORT>" "<KEEP-ALIVES>true</KEEP-ALIVES>" "<NAGLES-ALGORITHM>enabled</NAGLES-ALGORITHM>",
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
            "<KEEP-ALIVES>true</KEEP-ALIVES>" "<TCP-TP-PORT></TCP-TP-PORT>",
            root_tag="TCP-TP",
        )
        parser.readTcpTp(element, tp)
        assert tp.getKeepAlives() is not None
        assert tp.getKeepAlives().getValue()

    def test_readTcpTp_sets_keepAliveTime(self, parser):
        from armodel.models import TcpTp

        tp = TcpTp()
        element = _snip(
            "<KEEP-ALIVE-TIME>30</KEEP-ALIVE-TIME>" "<TCP-TP-PORT></TCP-TP-PORT>",
            root_tag="TCP-TP",
        )
        parser.readTcpTp(element, tp)
        assert tp.getKeepAliveTime() is not None
        assert tp.getKeepAliveTime().getValue() == 30

    def test_readGenericTp_sets_tpTechnology(self, parser):
        from armodel.models import GenericTp

        tp = GenericTp()
        element = _snip(
            "<TP-TECHNOLOGY>UDP</TP-TECHNOLOGY>" "<TP-ADDRESS>192.168.1.1</TP-ADDRESS>",
            root_tag="GENERIC-TP",
        )
        parser.readGenericTp(element, tp)
        assert tp.getTpTechnology() is not None
        assert tp.getTpTechnology().getValue() == "UDP"

    def test_getTransportProtocolConfiguration_udp(self, parser):
        element = _snip(
            "<TP-CONFIGURATION>" "<UDP-TP>" "<UDP-TP-PORT><PORT-NUMBER>5000</PORT-NUMBER></UDP-TP-PORT>" "</UDP-TP>" "</TP-CONFIGURATION>",
            root_tag="ROOT",
        )
        config = parser.getTransportProtocolConfiguration(element, "TP-CONFIGURATION")
        assert config is not None

    def test_getTransportProtocolConfiguration_tcp(self, parser):
        element = _snip(
            "<TP-CONFIGURATION>" "<TCP-TP>" "<TCP-TP-PORT><PORT-NUMBER>5000</PORT-NUMBER></TCP-TP-PORT>" "</TCP-TP>" "</TP-CONFIGURATION>",
            root_tag="ROOT",
        )
        config = parser.getTransportProtocolConfiguration(element, "TP-CONFIGURATION")
        assert config is not None

    def test_getTransportProtocolConfiguration_generic(self, parser):
        element = _snip(
            "<TP-CONFIGURATION>" "<GENERIC-TP>" "<TP-TECHNOLOGY>UDP</TP-TECHNOLOGY>" "</GENERIC-TP>" "</TP-CONFIGURATION>",
            root_tag="ROOT",
        )
        config = parser.getTransportProtocolConfiguration(element, "TP-CONFIGURATION")
        assert config is not None

    def test_getTransportProtocolConfiguration_unsupported_warns(self, warning_parser, caplog):
        element = _snip(
            "<TP-CONFIGURATION><BAD/></TP-CONFIGURATION>",
            root_tag="ROOT",
        )
        with caplog.at_level(logging.ERROR):
            config = warning_parser.getTransportProtocolConfiguration(element, "TP-CONFIGURATION")
        assert config is None
        assert any("Unsupported TransportProtocolConfiguration" in r.getMessage() for r in caplog.records)


class TestFrameAndPduHandlers:
    def test_readFrameTriggering_sets_frameRef(self, parser):
        from armodel.models import CanCluster, CanFrameTriggering, CanPhysicalChannel

        cluster = CanCluster(parent=_autosar_root(), short_name="c")
        channel = CanPhysicalChannel(parent=cluster, short_name="ch")
        triggering = CanFrameTriggering(parent=channel, short_name="ft")
        element = _snip(
            "<SHORT-NAME>ft</SHORT-NAME>" "<FRAME-REF DEST='FRAME'>/frame</FRAME-REF>",
            root_tag="CAN-FRAME-TRIGGERING",
        )
        parser.readFrameTriggering(element, triggering)
        assert triggering.getFrameRef().getValue() == "/frame"

    def test_readFrameTriggering_adds_framePortRefs(self, parser):
        from armodel.models import CanCluster, CanFrameTriggering, CanPhysicalChannel

        cluster = CanCluster(parent=_autosar_root(), short_name="c")
        channel = CanPhysicalChannel(parent=cluster, short_name="ch")
        triggering = CanFrameTriggering(parent=channel, short_name="ft")
        element = _snip(
            "<SHORT-NAME>ft</SHORT-NAME>" "<FRAME-PORT-REFS>" "<FRAME-PORT-REF DEST='FRAME-PORT'>/fp</FRAME-PORT-REF>" "</FRAME-PORT-REFS>",
            root_tag="CAN-FRAME-TRIGGERING",
        )
        parser.readFrameTriggering(element, triggering)
        assert len(triggering.getFramePortRefs()) == 1

    def test_readCanFrameTriggering_sets_canAddressingMode(self, parser):
        from armodel.models import CanCluster, CanFrameTriggering, CanPhysicalChannel

        cluster = CanCluster(parent=_autosar_root(), short_name="c")
        channel = CanPhysicalChannel(parent=cluster, short_name="ch")
        triggering = CanFrameTriggering(parent=channel, short_name="ft")
        element = _snip(
            "<SHORT-NAME>ft</SHORT-NAME>" "<CAN-ADDRESSING-MODE>standard</CAN-ADDRESSING-MODE>" "<IDENTIFIER><VALUE>100</VALUE></IDENTIFIER>",
            root_tag="CAN-FRAME-TRIGGERING",
        )
        parser.readCanFrameTriggering(element, triggering)
        assert triggering.getCanAddressingMode() is not None
        assert triggering.getCanAddressingMode().getValue() == "standard"

    def test_readCanFrameTriggering_sets_masks_and_j1939(self, parser):
        from armodel.models import CanCluster, CanFrameTriggering, CanPhysicalChannel

        cluster = CanCluster(parent=_autosar_root(), short_name="c")
        channel = CanPhysicalChannel(parent=cluster, short_name="ch")
        triggering = CanFrameTriggering(parent=channel, short_name="ft")
        element = _snip(
            "<SHORT-NAME>ft</SHORT-NAME>" "<J-1939-REQUESTABLE>true</J-1939-REQUESTABLE>" "<RX-MASK>511</RX-MASK>" "<TX-MASK>255</TX-MASK>",
            root_tag="CAN-FRAME-TRIGGERING",
        )
        parser.readCanFrameTriggering(element, triggering)
        assert triggering.getJ1939requestable() is not None
        assert triggering.getJ1939requestable().getValue()
        assert triggering.getRxMask().getValue() == 511
        assert triggering.getTxMask().getValue() == 255

    def test_readCanFrameTriggering_sets_identifier(self, parser):
        from armodel.models import CanCluster, CanFrameTriggering, CanPhysicalChannel

        cluster = CanCluster(parent=_autosar_root(), short_name="c")
        channel = CanPhysicalChannel(parent=cluster, short_name="ch")
        triggering = CanFrameTriggering(parent=channel, short_name="ft")
        element = _snip(
            "<SHORT-NAME>ft</SHORT-NAME>" "<IDENTIFIER>100</IDENTIFIER>",
            root_tag="CAN-FRAME-TRIGGERING",
        )
        parser.readCanFrameTriggering(element, triggering)
        assert triggering.getIdentifier() is not None
        assert triggering.getIdentifier().getValue() == 100

    def test_readPduTriggering_sets_ipduRef(self, parser):
        from armodel.models import CanCluster, CanPhysicalChannel, PduTriggering

        cluster = CanCluster(parent=_autosar_root(), short_name="c")
        channel = CanPhysicalChannel(parent=cluster, short_name="ch")
        triggering = PduTriggering(parent=channel, short_name="pt")
        element = _snip(
            "<SHORT-NAME>pt</SHORT-NAME>" "<I-PDU-REF DEST='I-PDU'>/pdu</I-PDU-REF>",
            root_tag="PDU-TRIGGERING",
        )
        parser.readPduTriggering(element, triggering)
        assert triggering.getIPduRef().getValue() == "/pdu"

    def test_readPduTriggering_adds_ipduPortRefs(self, parser):
        from armodel.models import CanCluster, CanPhysicalChannel, PduTriggering

        cluster = CanCluster(parent=_autosar_root(), short_name="c")
        channel = CanPhysicalChannel(parent=cluster, short_name="ch")
        triggering = PduTriggering(parent=channel, short_name="pt")
        element = _snip(
            "<SHORT-NAME>pt</SHORT-NAME>" "<I-PDU-PORT-REFS>" "<I-PDU-PORT-REF DEST='I-PDU-PORT'>/ip</I-PDU-PORT-REF>" "</I-PDU-PORT-REFS>",
            root_tag="PDU-TRIGGERING",
        )
        parser.readPduTriggering(element, triggering)
        assert len(triggering.getIPduPortRefs()) == 1

    def test_readISignalTriggering_sets_iSignalRef(self, parser):
        from armodel.models import CanCluster, CanPhysicalChannel, ISignalTriggering

        cluster = CanCluster(parent=_autosar_root(), short_name="c")
        channel = CanPhysicalChannel(parent=cluster, short_name="ch")
        triggering = ISignalTriggering(parent=channel, short_name="st")
        element = _snip(
            "<SHORT-NAME>st</SHORT-NAME>" "<I-SIGNAL-REF DEST='I-SIGNAL'>/sig</I-SIGNAL-REF>",
            root_tag="I-SIGNAL-TRIGGERING",
        )
        parser.readISignalTriggering(element, triggering)
        assert triggering.getISignalRef().getValue() == "/sig"

    def test_readPhysicalChannelFrameTriggerings_can(self, parser):
        from armodel.models import CanCluster, CanPhysicalChannel

        cluster = CanCluster(parent=_autosar_root(), short_name="c")
        channel = CanPhysicalChannel(parent=cluster, short_name="ch")
        element = _snip(
            "<FRAME-TRIGGERINGS>" "<CAN-FRAME-TRIGGERING>" "<SHORT-NAME>ft</SHORT-NAME>" "</CAN-FRAME-TRIGGERING>" "</FRAME-TRIGGERINGS>",
            root_tag="CAN-PHYSICAL-CHANNEL",
        )
        parser.readPhysicalChannelFrameTriggerings(element, channel)
        assert len(channel.getFrameTriggerings()) == 1

    def test_readPhysicalChannelFrameTriggerings_lin(self, parser):
        from armodel.models import LinCluster, LinPhysicalChannel

        cluster = LinCluster(parent=_autosar_root(), short_name="l")
        channel = LinPhysicalChannel(parent=cluster, short_name="ch")
        element = _snip(
            "<FRAME-TRIGGERINGS>" "<LIN-FRAME-TRIGGERING>" "<SHORT-NAME>ft</SHORT-NAME>" "</LIN-FRAME-TRIGGERING>" "</FRAME-TRIGGERINGS>",
            root_tag="LIN-PHYSICAL-CHANNEL",
        )
        parser.readPhysicalChannelFrameTriggerings(element, channel)
        assert len(channel.getFrameTriggerings()) == 1

    def test_readPhysicalChannelFrameTriggerings_flexray(self, parser):
        from armodel.models import FlexrayCluster, FlexrayPhysicalChannel

        cluster = FlexrayCluster(parent=_autosar_root(), short_name="fr")
        channel = FlexrayPhysicalChannel(parent=cluster, short_name="ch")
        element = _snip(
            "<FRAME-TRIGGERINGS>" "<FLEXRAY-FRAME-TRIGGERING>" "<SHORT-NAME>ft</SHORT-NAME>" "</FLEXRAY-FRAME-TRIGGERING>" "</FRAME-TRIGGERINGS>",
            root_tag="FLEXRAY-PHYSICAL-CHANNEL",
        )
        parser.readPhysicalChannelFrameTriggerings(element, channel)
        assert len(channel.getFrameTriggerings()) == 1

    def test_readPhysicalChannelFrameTriggerings_unsupported_warns(self, warning_parser, caplog):
        from armodel.models import CanCluster, CanPhysicalChannel

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
        from armodel.models import CanCluster, CanPhysicalChannel

        cluster = CanCluster(parent=_autosar_root(), short_name="c")
        channel = CanPhysicalChannel(parent=cluster, short_name="ch")
        element = _snip(
            "<PDU-TRIGGERINGS>" "<PDU-TRIGGERING>" "<SHORT-NAME>pt</SHORT-NAME>" "</PDU-TRIGGERING>" "</PDU-TRIGGERINGS>",
            root_tag="CAN-PHYSICAL-CHANNEL",
        )
        parser.readPhysicalChannelPduTriggerings(element, channel)
        assert len(channel.getPduTriggerings()) == 1

    def test_readPhysicalChannelISignalTriggerings_creates_triggering(self, parser):
        from armodel.models import CanCluster, CanPhysicalChannel

        cluster = CanCluster(parent=_autosar_root(), short_name="c")
        channel = CanPhysicalChannel(parent=cluster, short_name="ch")
        element = _snip(
            "<I-SIGNAL-TRIGGERINGS>" "<I-SIGNAL-TRIGGERING>" "<SHORT-NAME>st</SHORT-NAME>" "</I-SIGNAL-TRIGGERING>" "</I-SIGNAL-TRIGGERINGS>",
            root_tag="CAN-PHYSICAL-CHANNEL",
        )
        parser.readPhysicalChannelISignalTriggerings(element, channel)
        assert len(channel.getISignalTriggerings()) == 1

    def test_readPhysicalChannelCommConnectorRefs_adds_ref(self, parser):
        from armodel.models import CanCluster, CanPhysicalChannel

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
            "<SHORT-NAME>pdu</SHORT-NAME>" "<LENGTH>8</LENGTH>",
            root_tag="NM-PDU",
        )
        parser.readPdu(element, pdu)
        assert pdu.getLength() is not None
        assert pdu.getLength().getValue() == 8

    def test_readIPdu_inherits_from_pdu(self, parser):
        from armodel.models import NPdu

        pdu = NPdu(parent=_autosar_root(), short_name="npdu")
        element = _snip(
            "<SHORT-NAME>npdu</SHORT-NAME>" "<LENGTH>8</LENGTH>",
            root_tag="N-PDU",
        )
        parser.readNPdu(element, pdu)
        assert pdu.getLength() is not None
        assert pdu.getLength().getValue() == 8

    def test_readNmPdu_sets_unusedBitPattern(self, parser):
        from armodel.models import NmPdu

        pdu = NmPdu(parent=_autosar_root(), short_name="nmPdu")
        element = _snip(
            "<SHORT-NAME>nmPdu</SHORT-NAME>" "<UNUSED-BIT-PATTERN>0xFF</UNUSED-BIT-PATTERN>",
            root_tag="NM-PDU",
        )
        parser.readNmPdu(element, pdu)
        assert pdu.getUnusedBitPattern() is not None
        assert pdu.getUnusedBitPattern().getValue() == 0xFF

    def test_readDcmIPdu_sets_diagPduType(self, parser):
        from armodel.models import DcmIPdu

        pdu = DcmIPdu(parent=_autosar_root(), short_name="dcmPdu")
        element = _snip(
            "<SHORT-NAME>dcmPdu</SHORT-NAME>" "<DIAG-PDU-TYPE>request</DIAG-PDU-TYPE>",
            root_tag="DCM-I-PDU",
        )
        parser.readDcmIPdu(element, pdu)
        assert pdu.getDiagPduType() is not None
        assert pdu.getDiagPduType().getValue() == "request"

    def test_readIPdu_sets_containedIPduProps(self, parser):
        from armodel.models import GeneralPurposeIPdu

        ipdu = GeneralPurposeIPdu(parent=_autosar_root(), short_name="ipdu")
        element = _snip(
            "<SHORT-NAME>ipdu</SHORT-NAME>"
            "<CONTAINED-I-PDU-PROPS>"
            "<COLLECTION-SEMANTICS>lastIsBest</COLLECTION-SEMANTICS>"
            "<HEADER-ID-LONG-HEADER>100</HEADER-ID-LONG-HEADER>"
            "<HEADER-ID-SHORT-HEADER>50</HEADER-ID-SHORT-HEADER>"
            "<OFFSET>4</OFFSET>"
            "<TIMEOUT>10</TIMEOUT>"
            "<TRIGGER>onChange</TRIGGER>"
            "<UPDATE-INDICATION-BIT-POSITION>7</UPDATE-INDICATION-BIT-POSITION>"
            "</CONTAINED-I-PDU-PROPS>",
            root_tag="GENERAL-PURPOSE-I-PDU",
        )
        parser.readIPdu(element, ipdu)
        props = ipdu.getContainedIPduProps()
        assert props is not None
        assert props.getCollectionSemantics().getValue() == "lastIsBest"
        assert props.getHeaderIdLongHeader().getValue() == 100
        assert props.getHeaderIdShortHeader().getValue() == 50
        assert props.getOffset().getValue() == 4
        assert props.getTimeout().getValue() == 10
        assert props.getTrigger().getValue() == "onChange"
        assert props.getUpdateIndicationBitPosition().getValue() == 7

    def test_readIPdu_absent_containedIPduProps_stays_none(self, parser):
        from armodel.models import GeneralPurposeIPdu

        ipdu = GeneralPurposeIPdu(parent=_autosar_root(), short_name="ipdu")
        element = _snip("<SHORT-NAME>ipdu</SHORT-NAME>", root_tag="GENERAL-PURPOSE-I-PDU")
        parser.readIPdu(element, ipdu)
        assert ipdu.getContainedIPduProps() is None


class TestISignalAndGroupHandlers:
    def test_readISignal_sets_length(self, parser):
        from armodel.models import ISignal

        signal = ISignal(parent=_autosar_root(), short_name="sig")
        element = _snip(
            "<SHORT-NAME>sig</SHORT-NAME>" "<LENGTH>8</LENGTH>" "<I-SIGNAL-TYPE>signal</I-SIGNAL-TYPE>",
            root_tag="I-SIGNAL",
        )
        parser.readISignal(element, signal)
        assert signal.getLength() is not None
        assert signal.getLength().getValue() == 8

    def test_readISignal_sets_systemSignalRef(self, parser):
        from armodel.models import ISignal

        signal = ISignal(parent=_autosar_root(), short_name="sig")
        element = _snip(
            "<SHORT-NAME>sig</SHORT-NAME>" "<SYSTEM-SIGNAL-REF DEST='SYSTEM-SIGNAL'>/ss</SYSTEM-SIGNAL-REF>",
            root_tag="I-SIGNAL",
        )
        parser.readISignal(element, signal)
        assert signal.getSystemSignalRef().getValue() == "/ss"

    def test_readISignal_sets_dataTransformationRef(self, parser):
        from armodel.models import ISignal

        signal = ISignal(parent=_autosar_root(), short_name="sig")
        element = _snip(
            "<SHORT-NAME>sig</SHORT-NAME>"
            "<DATA-TRANSFORMATIONS><DATA-TRANSFORMATION-REF-CONDITIONAL><DATA-TRANSFORMATION-REF DEST='DATA-TRANSFORMATION'>/dt</DATA-TRANSFORMATION-REF></DATA-TRANSFORMATION-REF-CONDITIONAL></DATA-TRANSFORMATIONS>",
            root_tag="I-SIGNAL",
        )
        parser.readISignal(element, signal)
        assert signal.getDataTransformationRef().getValue() == "/dt"

    def test_readISignal_sets_timeoutSubstitutionValue(self, parser):
        from armodel.models import ISignal

        signal = ISignal(parent=_autosar_root(), short_name="sig")
        element = _snip(
            "<SHORT-NAME>sig</SHORT-NAME>" "<TIMEOUT-SUBSTITUTION-VALUE><TEXT-VALUE-SPECIFICATION><SHORT-LABEL>t</SHORT-LABEL></TEXT-VALUE-SPECIFICATION></TIMEOUT-SUBSTITUTION-VALUE>",
            root_tag="I-SIGNAL",
        )
        parser.readISignal(element, signal)
        assert signal.getTimeoutSubstitutionValue() is not None

    def test_readISignal_sets_transformationISignalProps(self, parser):
        from armodel.models import ISignal

        signal = ISignal(parent=_autosar_root(), short_name="sig")
        element = _snip(
            "<SHORT-NAME>sig</SHORT-NAME>"
            "<TRANSFORMATION-I-SIGNAL-PROPSS><END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS><END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS-VARIANTS><END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS-CONDITIONAL><TRANSFORMER-REF DEST='TRANSFORMATION-PROPS'>/tr</TRANSFORMER-REF></END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS-CONDITIONAL></END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS-VARIANTS></END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS></TRANSFORMATION-I-SIGNAL-PROPSS>",
            root_tag="I-SIGNAL",
        )
        parser.readISignal(element, signal)
        assert len(signal.getTransformationISignalProps()) == 1

    def test_readISignal_sets_iSignalProps(self, parser):
        from armodel.models import ISignal

        signal = ISignal(parent=_autosar_root(), short_name="sig")
        element = _snip(
            "<SHORT-NAME>sig</SHORT-NAME>" "<I-SIGNAL-PROPS><HANDLE-OUT-OF-RANGE>DEFAULT</HANDLE-OUT-OF-RANGE></I-SIGNAL-PROPS>",
            root_tag="I-SIGNAL",
        )
        parser.readISignal(element, signal)
        props = signal.getISignalProps()
        assert props is not None
        assert props.getHandleOutOfRange().getValue() == "DEFAULT"

    def test_readISignal_does_not_set_iSignalProps_when_absent(self, parser):
        from armodel.models import ISignal

        signal = ISignal(parent=_autosar_root(), short_name="sig")
        element = _snip(
            "<SHORT-NAME>sig</SHORT-NAME>" "<LENGTH>8</LENGTH>",
            root_tag="I-SIGNAL",
        )
        parser.readISignal(element, signal)
        assert signal.getISignalProps() is None

    def test_readISignalGroup_sets_systemSignalGroupRef(self, parser):
        from armodel.models import ISignalGroup

        group = ISignalGroup(parent=_autosar_root(), short_name="sigGroup")
        element = _snip(
            "<SHORT-NAME>sigGroup</SHORT-NAME>" "<SYSTEM-SIGNAL-GROUP-REF DEST='SYSTEM-SIGNAL-GROUP'>/ssg</SYSTEM-SIGNAL-GROUP-REF>",
            root_tag="I-SIGNAL-GROUP",
        )
        parser.readISignalGroup(element, group)
        assert group.getSystemSignalGroupRef().getValue() == "/ssg"

    def test_readISignalGroupISignalRef_adds_ref(self, parser):
        from armodel.models import ISignalGroup

        group = ISignalGroup(parent=_autosar_root(), short_name="sigGroup")
        element = _snip(
            "<I-SIGNAL-REFS>" "<I-SIGNAL-REF DEST='I-SIGNAL'>/sig1</I-SIGNAL-REF>" "</I-SIGNAL-REFS>",
            root_tag="I-SIGNAL-GROUP",
        )
        parser.readISignalGroupISignalRef(element, group)
        assert len(group.getISignalRefs()) == 1

    def test_getDataFilter_sets_dataFilterType(self, parser):
        element = _snip(
            "<DATA-FILTER>" "<DATA-FILTER-TYPE>mask</DATA-FILTER-TYPE>" "<MASK>255</MASK>" "</DATA-FILTER>",
            root_tag="ROOT",
        )
        filter = parser.getDataFilter(element, "DATA-FILTER")
        assert filter is not None
        assert filter.getDataFilterType().getValue() == "mask"

    def test_getTransmissionModeTiming_sets_cyclicTiming(self, parser):
        element = _snip(
            "<TRANSMISSION-MODE-TIMING>" "<CYCLIC-TIMING>" "<TIME-PERIOD>" "<VALUE>" "<VALUE>0.1</VALUE>" "</VALUE>" "</TIME-PERIOD>" "</CYCLIC-TIMING>" "</TRANSMISSION-MODE-TIMING>",
            root_tag="ROOT",
        )
        timing = parser.getTransmissionModeTiming(element, "TRANSMISSION-MODE-TIMING")
        assert timing is not None
        assert timing.getCyclicTiming() is not None

    def test_getCyclicTiming_sets_timePeriod(self, parser):
        element = _snip(
            "<CYCLIC-TIMING>" "<TIME-PERIOD>" "<VALUE>" "<VALUE>0.1</VALUE>" "</VALUE>" "</TIME-PERIOD>" "</CYCLIC-TIMING>",
            root_tag="ROOT",
        )
        timing = parser.getCyclicTiming(element, "CYCLIC-TIMING")
        assert timing is not None

    def test_getEventControlledTiming_sets_numberOfRepetitions(self, parser):
        element = _snip(
            "<EVENT-CONTROLLED-TIMING>" "<NUMBER-OF-REPETITIONS>5</NUMBER-OF-REPETITIONS>" "</EVENT-CONTROLLED-TIMING>",
            root_tag="ROOT",
        )
        timing = parser.getEventControlledTiming(element, "EVENT-CONTROLLED-TIMING")
        assert timing is not None
        assert timing.getNumberOfRepetitions().getValue() == 5

    def test_readISignalIPdu_sets_length(self, parser):
        from armodel.models import ISignalIPdu

        ipdu = ISignalIPdu(parent=_autosar_root(), short_name="isignalPdu")
        element = _snip(
            "<SHORT-NAME>isignalPdu</SHORT-NAME>" "<LENGTH>64</LENGTH>",
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
            "<SHORT-NAME>isignalPdu</SHORT-NAME>" "<UNUSED-BIT-PATTERN>0x00</UNUSED-BIT-PATTERN>",
            root_tag="I-SIGNAL-I-PDU",
        )
        parser.readISignalIPdu(element, ipdu)
        assert ipdu.getUnusedBitPattern().getValue() == 0


class TestISignalIPduIPduTimingSpecification:
    def test_get_sets_minimum_delay_and_declaration(self, parser):
        element = _snip(
            "<I-PDU-TIMING-SPECIFICATIONS>"
            "<I-PDU-TIMING>"
            "<MINIMUM-DELAY>0.05</MINIMUM-DELAY>"
            "<TRANSMISSION-MODE-DECLARATION>"
            "<SHORT-NAME>decl</SHORT-NAME>"
            "<TRANSMISSION-MODE-TRUE-TIMING>"
            "<CYCLIC-TIMING><TIME-PERIOD><VALUE><VALUE>0.1</VALUE></VALUE></TIME-PERIOD></CYCLIC-TIMING>"
            "</TRANSMISSION-MODE-TRUE-TIMING>"
            "</TRANSMISSION-MODE-DECLARATION>"
            "</I-PDU-TIMING>"
            "</I-PDU-TIMING-SPECIFICATIONS>",
            root_tag="I-SIGNAL-I-PDU",
        )
        timing = parser.getISignalIPduIPduTimingSpecification(element)
        assert timing is not None
        assert timing.getMinimumDelay().getValue() == 0.05
        assert timing.getTransmissionModeDeclaration() is not None

    def test_get_absent_returns_none(self, parser):
        element = _snip("<SHORT-NAME>ipdu</SHORT-NAME>", root_tag="I-SIGNAL-I-PDU")
        timing = parser.getISignalIPduIPduTimingSpecification(element)
        assert timing is None


class TestEndToEndProtectionHandlers:
    def test_getEndToEndDescription_sets_category(self, parser):
        element = _snip(
            "<END-TO-END-PROFILE>" "<CATEGORY>CRC8</CATEGORY>" "<DATA-ID-MODE>1</DATA-ID-MODE>" "<DATA-LENGTH>8</DATA-LENGTH>" "</END-TO-END-PROFILE>",
            root_tag="ROOT",
        )
        desc = parser.getEndToEndDescription(element, "END-TO-END-PROFILE")
        assert desc is not None
        assert desc.getCategory().getValue() == "CRC8"

    def test_getEndToEndDescription_sets_dataIdMode(self, parser):
        element = _snip(
            "<END-TO-END-PROFILE>" "<DATA-ID-MODE>1</DATA-ID-MODE>" "</END-TO-END-PROFILE>",
            root_tag="ROOT",
        )
        desc = parser.getEndToEndDescription(element, "END-TO-END-PROFILE")
        assert desc.getDataIdMode().getValue() == 1

    def test_readEndToEndDescriptionDataIds_adds_dataId(self, parser):
        from armodel.models import EndToEndDescription

        desc = EndToEndDescription()
        element = _snip(
            "<DATA-IDS>" "<DATA-ID>1</DATA-ID>" "<DATA-ID>2</DATA-ID>" "</DATA-IDS>",
            root_tag="END-TO-END-PROFILE",
        )
        parser.readEndToEndDescriptionDataIds(element, desc)
        assert len(desc.getDataIds()) == 2

    def test_readEndToEndProtection_sets_short_name(self, parser):
        from armodel.models import EndToEndProtection, EndToEndProtectionSet

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
            "<DATA-OFFSET>8</DATA-OFFSET>" "<I-SIGNAL-I-PDU-REF DEST='I-SIGNAL-I-PDU'>/ipdu</I-SIGNAL-I-PDU-REF>",
            root_tag="END-TO-END-PROTECTION-I-SIGNAL-I-PDU",
        )
        parser.readEndToEndProtectionISignalIPdu(element, ipdu)
        assert ipdu.getDataOffset().getValue() == 8

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
            "<SENDER-IREF>" "<TARGET-DATA-PROTOTYPE-REF DEST='VARIABLE-DATA-PROTOTYPE'>/vdp</TARGET-DATA-PROTOTYPE-REF>" "</SENDER-IREF>",
            root_tag="END-TO-END-PROTECTION-VARIABLE-PROTOTYPE",
        )
        parser.readEndToEndProtectionVariablePrototype(element, proto)
        assert proto.senderIRef is not None

    def test_readEndToEndProtectionVariablePrototype_adds_receiverIref(self, parser):
        from armodel.models import EndToEndProtectionVariablePrototype

        proto = EndToEndProtectionVariablePrototype()
        element = _snip(
            "<RECEIVER-IREFS>" "<RECEIVER-IREF>" "<TARGET-DATA-PROTOTYPE-REF DEST='VARIABLE-DATA-PROTOTYPE'>/vdp1</TARGET-DATA-PROTOTYPE-REF>" "</RECEIVER-IREF>" "</RECEIVER-IREFS>",
            root_tag="END-TO-END-PROTECTION-VARIABLE-PROTOTYPE",
        )
        parser.readEndToEndProtectionVariablePrototype(element, proto)
        assert len(proto.getReceiverIrefs()) == 1

    def test_readEndToEndProtectionEndToEndProtectionVariablePrototypes_creates(self, parser):
        from armodel.models import EndToEndProtection, EndToEndProtectionSet

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
        parser.readEndToEndProtectionEndToEndProtectionVariablePrototypes(element, protection)
        assert len(protection.getEndToEndProtectionVariablePrototypes()) == 1

    def test_readEndToEndProtectionEndToEndProtectionVariablePrototypes_unsupported_warns(self, warning_parser, caplog):
        from armodel.models import EndToEndProtection, EndToEndProtectionSet

        set = EndToEndProtectionSet(parent=_autosar_root(), short_name="e2eSet")
        protection = EndToEndProtection(parent=set, short_name="e2e")
        element = _snip(
            "<END-TO-END-PROTECTION-VARIABLE-PROTOTYPES><BAD/></END-TO-END-PROTECTION-VARIABLE-PROTOTYPES>",
            root_tag="END-TO-END-PROTECTION",
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readEndToEndProtectionEndToEndProtectionVariablePrototypes(element, protection)
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
            "<NM-CLUSTERS>" "<CAN-NM-CLUSTER>" "<SHORT-NAME>cnm</SHORT-NAME>" "</CAN-NM-CLUSTER>" "</NM-CLUSTERS>",
            root_tag="NM-CONFIG",
        )
        parser.readNmConfigNmClusters(element, config)
        assert len(config.getNmClusters()) == 1

    def test_readNmConfigNmClusters_udpNmCluster(self, parser):
        from armodel.models import NmConfig

        config = NmConfig(parent=_autosar_root(), short_name="nmConfig")
        element = _snip(
            "<NM-CLUSTERS>" "<UDP-NM-CLUSTER>" "<SHORT-NAME>unm</SHORT-NAME>" "</UDP-NM-CLUSTER>" "</NM-CLUSTERS>",
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
        from armodel.models import CanNmCluster, NmConfig

        config = NmConfig(parent=_autosar_root(), short_name="nmConfig")
        cluster = CanNmCluster(parent=config, short_name="cnm")
        element = _snip(
            "<SHORT-NAME>cnm</SHORT-NAME>" "<NM-BUSLOAD-REDUCTION-ACTIVE>true</NM-BUSLOAD-REDUCTION-ACTIVE>" "<NM-CHANNEL-ACTIVE>true</NM-CHANNEL-ACTIVE>",
            root_tag="CAN-NM-CLUSTER",
        )
        parser.readCanNmCluster(element, cluster)
        assert cluster.getNmBusloadReductionActive().getValue()

    def test_readUdpNmCluster_sets_nmChannelActive(self, parser):
        from armodel.models import NmConfig, UdpNmCluster

        config = NmConfig(parent=_autosar_root(), short_name="nmConfig")
        cluster = UdpNmCluster(parent=config, short_name="unm")
        element = _snip(
            "<SHORT-NAME>unm</SHORT-NAME>" "<NM-CHANNEL-ACTIVE>true</NM-CHANNEL-ACTIVE>",
            root_tag="UDP-NM-CLUSTER",
        )
        parser.readUdpNmCluster(element, cluster)
        assert cluster.getNmChannelActive().getValue()

    def test_readNmCluster_sets_communicationClusterRef(self, parser):
        from armodel.models import CanNmCluster, NmConfig

        config = NmConfig(parent=_autosar_root(), short_name="nmConfig")
        cluster = CanNmCluster(parent=config, short_name="cnm")
        element = _snip(
            "<SHORT-NAME>cnm</SHORT-NAME>" "<COMMUNICATION-CLUSTER-REF DEST='CAN-CLUSTER'>/cc</COMMUNICATION-CLUSTER-REF>",
            root_tag="CAN-NM-CLUSTER",
        )
        parser.readNmCluster(element, cluster)
        assert cluster.getCommunicationClusterRef().getValue() == "/cc"

    def test_readNmClusterNmNodes_canNmNode(self, parser):
        from armodel.models import CanNmCluster, NmConfig

        config = NmConfig(parent=_autosar_root(), short_name="nmConfig")
        cluster = CanNmCluster(parent=config, short_name="cnm")
        element = _snip(
            "<NM-NODES>" "<CAN-NM-NODE>" "<SHORT-NAME>node</SHORT-NAME>" "</CAN-NM-NODE>" "</NM-NODES>",
            root_tag="CAN-NM-CLUSTER",
        )
        parser.readNmClusterNmNodes(element, cluster)
        assert len(cluster.getNmNodes()) == 1

    def test_readNmClusterNmNodes_udpNmNode(self, parser):
        from armodel.models import NmConfig, UdpNmCluster

        config = NmConfig(parent=_autosar_root(), short_name="nmConfig")
        cluster = UdpNmCluster(parent=config, short_name="unm")
        element = _snip(
            "<NM-NODES>" "<UDP-NM-NODE>" "<SHORT-NAME>node</SHORT-NAME>" "</UDP-NM-NODE>" "</NM-NODES>",
            root_tag="UDP-NM-CLUSTER",
        )
        parser.readNmClusterNmNodes(element, cluster)
        assert len(cluster.getNmNodes()) == 1

    def test_readNmClusterNmNodes_unsupported_warns(self, warning_parser, caplog):
        from armodel.models import CanNmCluster, NmConfig

        config = NmConfig(parent=_autosar_root(), short_name="nmConfig")
        cluster = CanNmCluster(parent=config, short_name="cnm")
        element = _snip(
            "<NM-NODES><BAD/></NM-NODES>",
            root_tag="CAN-NM-CLUSTER",
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readNmClusterNmNodes(element, cluster)
        assert any("Unsupported Nm Node" in r.getMessage() for r in caplog.records)

    def test_readNmClusterNmNodes_j1939NmNode(self, parser):
        from armodel.models import J1939NmCluster, NmConfig

        config = NmConfig(parent=_autosar_root(), short_name="nmConfig")
        cluster = J1939NmCluster(parent=config, short_name="jnm")
        element = _snip(
            "<NM-NODES>" "<J-1939-NM-NODE>" "<SHORT-NAME>node</SHORT-NAME>" "</J-1939-NM-NODE>" "</NM-NODES>",
            root_tag="J-1939-NM-CLUSTER",
        )
        parser.readNmClusterNmNodes(element, cluster)
        assert len(cluster.getNmNodes()) == 1
        assert cluster.getNmNodes()[0].getShortName() == "node"

    def test_readJ1939NmNode_sets_addressConfigurationCapability(self, parser):
        from armodel.models import J1939NmCluster, J1939NmNode, NmConfig

        config = NmConfig(parent=_autosar_root(), short_name="nmConfig")
        cluster = J1939NmCluster(parent=config, short_name="jnm")
        node = J1939NmNode(parent=cluster, short_name="node")
        element = _snip(
            "<SHORT-NAME>node</SHORT-NAME>" "<ADDRESS-CONFIGURATION-CAPABILITY>J-1939-NM-SCA</ADDRESS-CONFIGURATION-CAPABILITY>",
            root_tag="J-1939-NM-NODE",
        )
        parser.readJ1939NmNode(element, node)
        assert node.getAddressConfigurationCapability().getValue() == "J-1939-NM-SCA"

    def test_readJ1939NmNode_sets_nodeName(self, parser):
        from armodel.models import J1939NmCluster, J1939NmNode, NmConfig

        config = NmConfig(parent=_autosar_root(), short_name="nmConfig")
        cluster = J1939NmCluster(parent=config, short_name="jnm")
        node = J1939NmNode(parent=cluster, short_name="node")
        element = _snip(
            "<SHORT-NAME>node</SHORT-NAME>" "<NODE-NAME>" "<ARBITRARY-ADDRESS-CAPABLE>true</ARBITRARY-ADDRESS-CAPABLE>" "<MANUFACTURER-CODE>305</MANUFACTURER-CODE>" "</NODE-NAME>",
            root_tag="J-1939-NM-NODE",
        )
        parser.readJ1939NmNode(element, node)
        node_name = node.getNodeName()
        assert node_name is not None
        assert node_name.getArbitraryAddressCapable().getValue() is True
        assert node_name.getManufacturerCode().getValue() == 305

    def test_readCanNmNode_sets_nmNodeId(self, parser):
        from armodel.models import CanNmCluster, CanNmNode, NmConfig

        config = NmConfig(parent=_autosar_root(), short_name="nmConfig")
        cluster = CanNmCluster(parent=config, short_name="cnm")
        node = CanNmNode(parent=cluster, short_name="node")
        element = _snip(
            "<SHORT-NAME>node</SHORT-NAME>" "<NM-NODE-ID>1</NM-NODE-ID>" "<NM-PASSIVE-MODE-ENABLED>false</NM-PASSIVE-MODE-ENABLED>",
            root_tag="CAN-NM-NODE",
        )
        parser.readCanNmNode(element, node)
        assert node.getNmNodeId().getValue() == 1

    def test_readNmNode_sets_controllerRef(self, parser):
        from armodel.models import CanNmCluster, CanNmNode, NmConfig

        config = NmConfig(parent=_autosar_root(), short_name="nmConfig")
        cluster = CanNmCluster(parent=config, short_name="cnm")
        node = CanNmNode(parent=cluster, short_name="node")
        element = _snip(
            "<SHORT-NAME>node</SHORT-NAME>" "<CONTROLLER-REF DEST='COMMUNICATION-CONTROLLER'>/ctrl</CONTROLLER-REF>",
            root_tag="CAN-NM-NODE",
        )
        parser.readNmNode(element, node)
        assert node.getControllerRef().getValue() == "/ctrl"

    def test_readNmNode_adds_rxNmPduRef(self, parser):
        from armodel.models import CanNmCluster, CanNmNode, NmConfig

        config = NmConfig(parent=_autosar_root(), short_name="nmConfig")
        cluster = CanNmCluster(parent=config, short_name="cnm")
        node = CanNmNode(parent=cluster, short_name="node")
        element = _snip(
            "<SHORT-NAME>node</SHORT-NAME>" "<RX-NM-PDU-REFS>" "<RX-NM-PDU-REF DEST='NM-PDU'>/rx</RX-NM-PDU-REF>" "</RX-NM-PDU-REFS>",
            root_tag="CAN-NM-NODE",
        )
        parser.readNmNode(element, node)
        assert len(node.getRxNmPduRefs()) == 1

    def test_readNmNode_adds_txNmPduRef(self, parser):
        from armodel.models import CanNmCluster, CanNmNode, NmConfig

        config = NmConfig(parent=_autosar_root(), short_name="nmConfig")
        cluster = CanNmCluster(parent=config, short_name="cnm")
        node = CanNmNode(parent=cluster, short_name="node")
        element = _snip(
            "<SHORT-NAME>node</SHORT-NAME>" "<TX-NM-PDU-REFS>" "<TX-NM-PDU-REF DEST='NM-PDU'>/tx</TX-NM-PDU-REF>" "</TX-NM-PDU-REFS>",
            root_tag="CAN-NM-NODE",
        )
        parser.readNmNode(element, node)
        assert len(node.getTxNmPduRefs()) == 1

    def test_readNmNode_sets_coord_attrs(self, parser):
        from armodel.models import CanNmCluster, CanNmNode, NmConfig

        config = NmConfig(parent=_autosar_root(), short_name="nmConfig")
        cluster = CanNmCluster(parent=config, short_name="cnm")
        node = CanNmNode(parent=cluster, short_name="node")
        element = _snip(
            "<SHORT-NAME>node</SHORT-NAME>" "<NM-COORD-CLUSTER>2</NM-COORD-CLUSTER>" "<NM-COORDINATOR-ROLE>active</NM-COORDINATOR-ROLE>",
            root_tag="CAN-NM-NODE",
        )
        parser.readNmNode(element, node)
        assert node.getNmCoordCluster().getValue() == 2
        assert node.getNmCoordinatorRole().getValue() == "active"

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
            "<NM-CLUSTER-COUPLINGS>" "<CAN-NM-CLUSTER-COUPLING>" "<NM-BUSLOAD-REDUCTION-ENABLED>true</NM-BUSLOAD-REDUCTION-ENABLED>" "</CAN-NM-CLUSTER-COUPLING>" "</NM-CLUSTER-COUPLINGS>",
            root_tag="NM-CONFIG",
        )
        parser.readNmConfigNmClusterCouplings(element, config)
        assert len(config.getNmClusterCouplings()) == 1

    def test_readNmConfigNmClusterCouplings_udp(self, parser):
        from armodel.models import NmConfig

        config = NmConfig(parent=_autosar_root(), short_name="nmConfig")
        element = _snip(
            "<NM-CLUSTER-COUPLINGS>" "<UDP-NM-CLUSTER-COUPLING>" "<NM-IMMEDIATE-RESTART-ENABLED>true</NM-IMMEDIATE-RESTART-ENABLED>" "</UDP-NM-CLUSTER-COUPLING>" "</NM-CLUSTER-COUPLINGS>",
            root_tag="NM-CONFIG",
        )
        parser.readNmConfigNmClusterCouplings(element, config)
        assert len(config.getNmClusterCouplings()) == 1

    def test_readNmConfigNmIfEcus_creates_ecu(self, parser):
        from armodel.models import NmConfig

        config = NmConfig(parent=_autosar_root(), short_name="nmConfig")
        element = _snip(
            "<NM-IF-ECUS>" "<NM-ECU>" "<SHORT-NAME>ecu</SHORT-NAME>" "</NM-ECU>" "</NM-IF-ECUS>",
            root_tag="NM-CONFIG",
        )
        parser.readNmConfigNmIfEcus(element, config)
        assert len(config.getNmIfEcus()) == 1

    def test_readNmEcu_sets_ecuInstanceRef(self, parser):
        from armodel.models import NmConfig, NmEcu

        config = NmConfig(parent=_autosar_root(), short_name="nmConfig")
        ecu = NmEcu(parent=config, short_name="ecu")
        element = _snip(
            "<SHORT-NAME>ecu</SHORT-NAME>" "<ECU-INSTANCE-REF DEST='ECU-INSTANCE'>/ei</ECU-INSTANCE-REF>" "<NM-BUS-SYNCHRONIZATION-ENABLED>true</NM-BUS-SYNCHRONIZATION-ENABLED>",
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
            "<TP-ADDRESSS>" "<CAN-TP-ADDRESS>" "<SHORT-NAME>addr</SHORT-NAME>" "<TP-ADDRESS>1</TP-ADDRESS>" "</CAN-TP-ADDRESS>" "</TP-ADDRESSS>",
            root_tag="CAN-TP-CONFIG",
        )
        parser.readCanTpConfigTpAddresses(element, config)
        assert len(config.getTpAddresses()) == 1

    def test_readCanTpAddress_sets_tpAddress(self, parser):
        from armodel.models import CanTpAddress, CanTpConfig

        config = CanTpConfig(parent=_autosar_root(), short_name="canTp")
        addr = CanTpAddress(parent=config, short_name="addr")
        element = _snip(
            "<SHORT-NAME>addr</SHORT-NAME>" "<TP-ADDRESS>1</TP-ADDRESS>" "<TP-ADDRESS-EXTENSION-VALUE>0</TP-ADDRESS-EXTENSION-VALUE>",
            root_tag="CAN-TP-ADDRESS",
        )
        parser.readCanTpAddress(element, addr)
        assert addr.getTpAddress().getValue() == 1

    def test_readCanTpConfigTpChannels_creates_channel(self, parser):
        from armodel.models import CanTpConfig

        config = CanTpConfig(parent=_autosar_root(), short_name="canTp")
        element = _snip(
            "<TP-CHANNELS>" "<CAN-TP-CHANNEL>" "<SHORT-NAME>ch</SHORT-NAME>" "<CHANNEL-ID>1</CHANNEL-ID>" "<CHANNEL-MODE>full</CHANNEL-MODE>" "</CAN-TP-CHANNEL>" "</TP-CHANNELS>",
            root_tag="CAN-TP-CONFIG",
        )
        parser.readCanTpConfigTpChannels(element, config)
        assert len(config.getTpChannels()) == 1

    def test_readCanTpChannel_sets_channelId(self, parser):
        from armodel.models import CanTpChannel, CanTpConfig

        config = CanTpConfig(parent=_autosar_root(), short_name="canTp")
        channel = CanTpChannel(parent=config, short_name="ch")
        element = _snip(
            "<SHORT-NAME>ch</SHORT-NAME>" "<CHANNEL-ID>1</CHANNEL-ID>" "<CHANNEL-MODE>full</CHANNEL-MODE>",
            root_tag="CAN-TP-CHANNEL",
        )
        parser.readCanTpChannel(element, channel)
        assert channel.getChannelId().getValue() == 1

    def test_readCanTpConfigTpNodes_creates_node(self, parser):
        from armodel.models import CanTpConfig

        config = CanTpConfig(parent=_autosar_root(), short_name="canTp")
        element = _snip(
            "<TP-NODES>" "<CAN-TP-NODE>" "<SHORT-NAME>node</SHORT-NAME>" "<MAX-FC-WAIT>10</MAX-FC-WAIT>" "</CAN-TP-NODE>" "</TP-NODES>",
            root_tag="CAN-TP-CONFIG",
        )
        parser.readCanTpConfigTpNodes(element, config)
        assert len(config.getTpNodes()) == 1

    def test_readCanTpNode_sets_maxFcWait(self, parser):
        from armodel.models import CanTpConfig, CanTpNode

        config = CanTpConfig(parent=_autosar_root(), short_name="canTp")
        node = CanTpNode(parent=config, short_name="node")
        element = _snip(
            "<SHORT-NAME>node</SHORT-NAME>" "<MAX-FC-WAIT>10</MAX-FC-WAIT>" "<ST-MIN>0.01</ST-MIN>",
            root_tag="CAN-TP-NODE",
        )
        parser.readCanTpNode(element, node)
        assert node.getMaxFcWait().getValue() == 10

    def test_readCanTpConfigTpConnections_creates_connection(self, parser):
        from armodel.models import CanTpConfig

        config = CanTpConfig(parent=_autosar_root(), short_name="canTp")
        element = _snip(
            "<TP-CONNECTIONS>" "<CAN-TP-CONNECTION>" "<IDENT><SHORT-NAME>conn</SHORT-NAME></IDENT>" "<ADDRESSING-FORMAT>standard</ADDRESSING-FORMAT>" "</CAN-TP-CONNECTION>" "</TP-CONNECTIONS>",
            root_tag="CAN-TP-CONFIG",
        )
        parser.readCanTpConfigTpConnections(element, config)
        assert len(config.getTpConnections()) == 1

    def test_readCanTpConnection_sets_addressingFormat(self, parser):
        from armodel.models import CanTpConnection

        conn = CanTpConnection()
        element = _snip(
            "<IDENT><SHORT-NAME>conn</SHORT-NAME></IDENT>" "<ADDRESSING-FORMAT>standard</ADDRESSING-FORMAT>" "<MAX-BLOCK-SIZE>8</MAX-BLOCK-SIZE>",
            root_tag="CAN-TP-CONNECTION",
        )
        parser.readCanTpConnection(element, conn)
        assert conn.getAddressingFormat().getValue() == "standard"

    def test_readCanTpConfigTpEcus_creates_ecu(self, parser):
        from armodel.models import CanTpConfig

        config = CanTpConfig(parent=_autosar_root(), short_name="canTp")
        element = _snip(
            "<TP-ECUS>" "<CAN-TP-ECU>" "<ECU-INSTANCE-REF DEST='ECU-INSTANCE'>/ei</ECU-INSTANCE-REF>" "</CAN-TP-ECU>" "</TP-ECUS>",
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
            "<TP-ADDRESSS>" "<TP-ADDRESS>" "<SHORT-NAME>addr</SHORT-NAME>" "<TP-ADDRESS>1</TP-ADDRESS>" "</TP-ADDRESS>" "</TP-ADDRESSS>",
            root_tag="LIN-TP-CONFIG",
        )
        parser.readLinTpConfigTpAddresses(element, config)
        assert len(config.getTpAddresses()) == 1

    def test_readTpAddress_sets_tpAddress(self, parser):
        from armodel.models import LinTpConfig, TpAddress

        config = LinTpConfig(parent=_autosar_root(), short_name="linTp")
        addr = TpAddress(parent=config, short_name="addr")
        element = _snip(
            "<SHORT-NAME>addr</SHORT-NAME>" "<TP-ADDRESS>1</TP-ADDRESS>",
            root_tag="TP-ADDRESS",
        )
        parser.readTpAddress(element, addr)
        assert addr.getTpAddress().getValue() == 1

    def test_readLinTpConfigTpNodes_creates_node(self, parser):
        from armodel.models import LinTpConfig

        config = LinTpConfig(parent=_autosar_root(), short_name="linTp")
        element = _snip(
            "<TP-NODES>" "<LIN-TP-NODE>" "<SHORT-NAME>node</SHORT-NAME>" "<P-2-MAX>0.05</P-2-MAX>" "</LIN-TP-NODE>" "</TP-NODES>",
            root_tag="LIN-TP-CONFIG",
        )
        parser.readLinTpConfigTpNodes(element, config)
        assert len(config.getTpNodes()) == 1

    def test_readLinTpNode_sets_p2Max(self, parser):
        from armodel.models import LinTpConfig, LinTpNode

        config = LinTpConfig(parent=_autosar_root(), short_name="linTp")
        node = LinTpNode(parent=config, short_name="node")
        element = _snip(
            "<SHORT-NAME>node</SHORT-NAME>" "<P-2-MAX>0.05</P-2-MAX>" "<P-2-TIMING>0.01</P-2-TIMING>",
            root_tag="LIN-TP-NODE",
        )
        parser.readLinTpNode(element, node)
        assert node.getP2Max().getValue() == 0.05

    def test_readLinTpConnection_sets_timeoutAs(self, parser):
        from armodel.models import LinTpConnection

        conn = LinTpConnection()
        element = _snip(
            "<IDENT><SHORT-NAME>conn</SHORT-NAME></IDENT>" "<TIMEOUT-AS>0.1</TIMEOUT-AS>",
            root_tag="LIN-TP-CONNECTION",
        )
        parser.readLinTpConnection(element, conn)
        assert conn.getTimeoutAs().getValue() == 0.1

    def test_readTpConfig_sets_communicationClusterRef(self, parser):
        from armodel.models import CanTpConfig

        config = CanTpConfig(parent=_autosar_root(), short_name="canTp")
        element = _snip(
            "<SHORT-NAME>canTp</SHORT-NAME>" "<COMMUNICATION-CLUSTER-REF DEST='CAN-CLUSTER'>/cc</COMMUNICATION-CLUSTER-REF>",
            root_tag="CAN-TP-CONFIG",
        )
        parser.readTpConfig(element, config)
        assert config.getCommunicationClusterRef().getValue() == "/cc"

    def test_readCanTpConfigTpConnections_unsupported_warns(self, warning_parser, caplog):
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

    def test_readEcuInstance_sets_ref_lists(self, parser):
        from armodel.models import EcuInstance

        instance = EcuInstance(parent=_autosar_root(), short_name="ecu")
        element = _snip(
            "<SHORT-NAME>ecu</SHORT-NAME>"
            "<ASSOCIATED-CONSUMED-PROVIDED-SERVICE-INSTANCE-GROUP-REFS><ASSOCIATED-CONSUMED-PROVIDED-SERVICE-INSTANCE-GROUP-REF DEST='CONSUMED-PROVIDED-SERVICE-INSTANCE-GROUP'>/g1</ASSOCIATED-CONSUMED-PROVIDED-SERVICE-INSTANCE-GROUP-REF></ASSOCIATED-CONSUMED-PROVIDED-SERVICE-INSTANCE-GROUP-REFS>"
            "<ASSOCIATED-PDUR-I-PDU-GROUP-REFS><ASSOCIATED-PDUR-I-PDU-GROUP-REF DEST='PDUR-I-PDU-GROUP'>/g2</ASSOCIATED-PDUR-I-PDU-GROUP-REF></ASSOCIATED-PDUR-I-PDU-GROUP-REFS>"
            "<ECU-TASK-PROXY-REFS><ECU-TASK-PROXY-REF DEST='OS-TASK-PROXY'>/t1</ECU-TASK-PROXY-REF></ECU-TASK-PROXY-REFS>"
            "<FIREWALL-RULE-REFS><FIREWALL-RULE-REF DEST='STATE-DEPENDENT-FIREWALL'>/f1</FIREWALL-RULE-REF></FIREWALL-RULE-REFS>",
            root_tag="ECU-INSTANCE",
        )
        parser.readEcuInstance(element, instance)
        assert [r.getValue() for r in instance.getAssociatedConsumedProvidedServiceInstanceGroupRefs()] == ["/g1"]
        assert [r.getValue() for r in instance.getAssociatedPdurIPduGroupRefs()] == ["/g2"]
        assert [r.getValue() for r in instance.getEcuTaskProxyRefs()] == ["/t1"]
        assert [r.getValue() for r in instance.getFirewallRuleRefs()] == ["/f1"]

    def test_readEcuInstance_sets_scalars(self, parser):
        from armodel.models import EcuInstance

        instance = EcuInstance(parent=_autosar_root(), short_name="ecu")
        element = _snip(
            "<SHORT-NAME>ecu</SHORT-NAME>"
            "<CHANNEL-SYNCHRONOUS-WAKEUP>true</CHANNEL-SYNCHRONOUS-WAKEUP>"
            "<ETH-SWITCH-PORT-GROUP-DERIVATION>true</ETH-SWITCH-PORT-GROUP-DERIVATION>"
            "<PNC-NM-REQUEST>true</PNC-NM-REQUEST>"
            "<PNC-SYNCHRONOUS-WAKEUP>true</PNC-SYNCHRONOUS-WAKEUP>"
            "<PNC-PREPARE-SLEEP-TIMER>0.1</PNC-PREPARE-SLEEP-TIMER>"
            "<PN-RESET-TIME>0.2</PN-RESET-TIME>"
            "<TCP-IP-ICMP-PROPS DEST='ETH-TCP-IP-ICMP-PROPS'>/icmp</TCP-IP-ICMP-PROPS>"
            "<TCP-IP-PROPS DEST='ETH-TCP-IP-PROPS'>/tcp</TCP-IP-PROPS>"
            "<V-2-X-SUPPORTED>V-2-X-NOT-SUPPORTED</V-2-X-SUPPORTED>"
            "<SLEEP-MODE-SUPPORTED>true</SLEEP-MODE-SUPPORTED>"
            "<WAKE-UP-OVER-BUS-SUPPORTED>false</WAKE-UP-OVER-BUS-SUPPORTED>",
            root_tag="ECU-INSTANCE",
        )
        parser.readEcuInstance(element, instance)
        assert instance.getChannelSynchronousWakeup().getValue() is True
        assert instance.getEthSwitchPortGroupDerivation().getValue() is True
        assert instance.getPncNmRequest().getValue() is True
        assert instance.getPncSynchronousWakeup().getValue() is True
        assert instance.getPncPrepareSleepTimer().getValue() == 0.1
        assert instance.getPnResetTime().getValue() == 0.2
        assert instance.getTcpIpIcmpPropsRef().getValue() == "/icmp"
        assert instance.getTcpIpPropsRef().getValue() == "/tcp"
        assert instance.getV2xSupported().getValue() == "V-2-X-NOT-SUPPORTED"
        assert instance.getSleepModeSupported().getValue() is True
        assert instance.getWakeUpOverBusSupported().getValue() is False

    def test_readEcuInstanceCommControllers_can(self, parser):
        from armodel.models import EcuInstance

        instance = EcuInstance(parent=_autosar_root(), short_name="ecu")
        element = _snip(
            "<COMM-CONTROLLERS>" "<CAN-COMMUNICATION-CONTROLLER>" "<SHORT-NAME>ctrl</SHORT-NAME>" "</CAN-COMMUNICATION-CONTROLLER>" "</COMM-CONTROLLERS>",
            root_tag="ECU-INSTANCE",
        )
        parser.readEcuInstanceCommControllers(element, instance)
        assert len(instance.getCommControllers()) == 1

    def test_readEcuInstanceCommControllers_ethernet(self, parser):
        from armodel.models import EcuInstance

        instance = EcuInstance(parent=_autosar_root(), short_name="ecu")
        element = _snip(
            "<COMM-CONTROLLERS>" "<ETHERNET-COMMUNICATION-CONTROLLER>" "<SHORT-NAME>ctrl</SHORT-NAME>" "</ETHERNET-COMMUNICATION-CONTROLLER>" "</COMM-CONTROLLERS>",
            root_tag="ECU-INSTANCE",
        )
        parser.readEcuInstanceCommControllers(element, instance)
        assert len(instance.getCommControllers()) == 1

    def test_readEcuInstanceCommControllers_lin(self, parser):
        from armodel.models import EcuInstance

        instance = EcuInstance(parent=_autosar_root(), short_name="ecu")
        element = _snip(
            "<COMM-CONTROLLERS>" "<LIN-MASTER>" "<SHORT-NAME>ctrl</SHORT-NAME>" "</LIN-MASTER>" "</COMM-CONTROLLERS>",
            root_tag="ECU-INSTANCE",
        )
        parser.readEcuInstanceCommControllers(element, instance)
        assert len(instance.getCommControllers()) == 1

    def test_readEcuInstanceCommControllers_flexray(self, parser):
        from armodel.models import EcuInstance

        instance = EcuInstance(parent=_autosar_root(), short_name="ecu")
        element = _snip(
            "<COMM-CONTROLLERS>" "<FLEXRAY-COMMUNICATION-CONTROLLER>" "<SHORT-NAME>ctrl</SHORT-NAME>" "</FLEXRAY-COMMUNICATION-CONTROLLER>" "</COMM-CONTROLLERS>",
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
        from armodel.models import CanCommunicationController, EcuInstance

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
        from armodel.models import EcuInstance, EthernetCommunicationController

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
        from armodel.models import EcuInstance, LinMaster

        instance = EcuInstance(parent=_autosar_root(), short_name="ecu")
        ctrl = LinMaster(parent=instance, short_name="ctrl")
        element = _snip(
            "<SHORT-NAME>ctrl</SHORT-NAME>" "<LIN-MASTER-VARIANTS>" "<LIN-MASTER-CONDITIONAL>" "<PROTOCOL-VERSION>2.0</PROTOCOL-VERSION>" "</LIN-MASTER-CONDITIONAL>" "</LIN-MASTER-VARIANTS>",
            root_tag="LIN-MASTER",
        )
        parser.readLinMaster(element, ctrl)
        assert ctrl.getShortName() == "ctrl"

    def test_readFlexrayCommunicationController_sets_short_name(self, parser):
        from armodel.models import EcuInstance, FlexrayCommunicationController

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

    def test_readFlexrayCommunicationController_all_attrs(self, parser):
        from armodel.models import EcuInstance, FlexrayCommunicationController

        instance = EcuInstance(parent=_autosar_root(), short_name="ecu")
        ctrl = FlexrayCommunicationController(parent=instance, short_name="ctrl")
        element = _snip(
            "<SHORT-NAME>ctrl</SHORT-NAME>"
            "<FLEXRAY-COMMUNICATION-CONTROLLER-VARIANTS>"
            "<FLEXRAY-COMMUNICATION-CONTROLLER-CONDITIONAL>"
            "<ACCEPTED-STARTUP-RANGE>10</ACCEPTED-STARTUP-RANGE>"
            "<ALLOW-HALT-DUE-TO-CLOCK>true</ALLOW-HALT-DUE-TO-CLOCK>"
            "<ALLOW-PASSIVE-TO-ACTIVE>5</ALLOW-PASSIVE-TO-ACTIVE>"
            "<CLUSTER-DRIFT-DAMPING>2</CLUSTER-DRIFT-DAMPING>"
            "<DECODING-CORRECTION>3</DECODING-CORRECTION>"
            "<DELAY-COMPENSATION-A>4</DELAY-COMPENSATION-A>"
            "<DELAY-COMPENSATION-B>5</DELAY-COMPENSATION-B>"
            "<EXTERNAL-SYNC>true</EXTERNAL-SYNC>"
            "<EXTERN-OFFSET-CORRECTION>6</EXTERN-OFFSET-CORRECTION>"
            "<EXTERN-RATE-CORRECTION>7</EXTERN-RATE-CORRECTION>"
            "<FALL-BACK-INTERNAL>false</FALL-BACK-INTERNAL>"
            "<FLEXRAY-FIFOS>"
            "<FLEXRAY-FIFO-CONFIGURATION>"
            "<BASE-CYCLE>1</BASE-CYCLE>"
            "<FIFO-DEPTH>8</FIFO-DEPTH>"
            "</FLEXRAY-FIFO-CONFIGURATION>"
            "</FLEXRAY-FIFOS>"
            "<KEY-SLOT-ID>1</KEY-SLOT-ID>"
            "<KEY-SLOT-ONLY-ENABLED>true</KEY-SLOT-ONLY-ENABLED>"
            "<KEY-SLOT-USED-FOR-START-UP>true</KEY-SLOT-USED-FOR-START-UP>"
            "<KEY-SLOT-USED-FOR-SYNC>false</KEY-SLOT-USED-FOR-SYNC>"
            "<LATEST-TX>20</LATEST-TX>"
            "<LISTEN-TIMEOUT>100</LISTEN-TIMEOUT>"
            "<MACRO-INITIAL-OFFSET-A>30</MACRO-INITIAL-OFFSET-A>"
            "<MACRO-INITIAL-OFFSET-B>31</MACRO-INITIAL-OFFSET-B>"
            "<MAXIMUM-DYNAMIC-PAYLOAD-LENGTH>128</MAXIMUM-DYNAMIC-PAYLOAD-LENGTH>"
            "<MICRO-INITIAL-OFFSET-A>1</MICRO-INITIAL-OFFSET-A>"
            "<MICRO-INITIAL-OFFSET-B>2</MICRO-INITIAL-OFFSET-B>"
            "<MICRO-PER-CYCLE>5000</MICRO-PER-CYCLE>"
            "<MICROTICK-DURATION>0.00001</MICROTICK-DURATION>"
            "<NM-VECTOR-EARLY-UPDATE>true</NM-VECTOR-EARLY-UPDATE>"
            "<OFFSET-CORRECTION-OUT>50</OFFSET-CORRECTION-OUT>"
            "<RATE-CORRECTION-OUT>60</RATE-CORRECTION-OUT>"
            "<SAMPLES-PER-MICROTICK>2</SAMPLES-PER-MICROTICK>"
            "<SECOND-KEY-SLOT-ID>3</SECOND-KEY-SLOT-ID>"
            "<TWO-KEY-SLOT-MODE>true</TWO-KEY-SLOT-MODE>"
            "<WAKE-UP-PATTERN>0</WAKE-UP-PATTERN>"
            "</FLEXRAY-COMMUNICATION-CONTROLLER-CONDITIONAL>"
            "</FLEXRAY-COMMUNICATION-CONTROLLER-VARIANTS>",
            root_tag="FLEXRAY-COMMUNICATION-CONTROLLER",
        )
        parser.readFlexrayCommunicationController(element, ctrl)

        assert ctrl.getAcceptedStartupRange().getValue() == 10
        assert ctrl.getAllowHaltDueToClock().getValue() is True
        assert ctrl.getAllowPassiveToActive().getValue() == 5
        assert ctrl.getClusterDriftDamping().getValue() == 2
        assert ctrl.getDecodingCorrection().getValue() == 3
        assert ctrl.getDelayCompensationA().getValue() == 4
        assert ctrl.getDelayCompensationB().getValue() == 5
        assert ctrl.getExternalSync().getValue() is True
        assert ctrl.getExternOffsetCorrection().getValue() == 6
        assert ctrl.getExternRateCorrection().getValue() == 7
        assert ctrl.getFallBackInternal().getValue() is False
        assert len(ctrl.getFlexrayFifos()) == 1
        fifo = ctrl.getFlexrayFifos()[0]
        assert fifo.getBaseCycle().getValue() == 1
        assert fifo.getFifoDepth().getValue() == 8
        assert ctrl.getKeySlotID().getValue() == 1
        assert ctrl.getKeySlotOnlyEnabled().getValue() is True
        assert ctrl.getKeySlotUsedForStartUp().getValue() is True
        assert ctrl.getKeySlotUsedForSync().getValue() is False
        assert ctrl.getLatestTX().getValue() == 20
        assert ctrl.getListenTimeout().getValue() == 100
        assert ctrl.getMacroInitialOffsetA().getValue() == 30
        assert ctrl.getMacroInitialOffsetB().getValue() == 31
        assert ctrl.getMaximumDynamicPayloadLength().getValue() == 128
        assert ctrl.getMicroInitialOffsetA().getValue() == 1
        assert ctrl.getMicroInitialOffsetB().getValue() == 2
        assert ctrl.getMicroPerCycle().getValue() == 5000
        assert ctrl.getMicrotickDuration().getValue() == pytest.approx(0.00001)
        assert ctrl.getNmVectorEarlyUpdate().getValue() is True
        assert ctrl.getOffsetCorrectionOut().getValue() == 50
        assert ctrl.getRateCorrectionOut().getValue() == 60
        assert ctrl.getSamplesPerMicrotick().getValue() == 2
        assert ctrl.getSecondKeySlotId().getValue() == 3
        assert ctrl.getTwoKeySlotMode().getValue() is True
        assert ctrl.getWakeUpPattern().getValue() == 0

    def test_readFlexrayCommunicationController_empty_fifos(self, parser):
        from armodel.models import EcuInstance, FlexrayCommunicationController

        instance = EcuInstance(parent=_autosar_root(), short_name="ecu")
        ctrl = FlexrayCommunicationController(parent=instance, short_name="ctrl")
        element = _snip(
            "<SHORT-NAME>ctrl</SHORT-NAME>"
            "<FLEXRAY-COMMUNICATION-CONTROLLER-VARIANTS>"
            "<FLEXRAY-COMMUNICATION-CONTROLLER-CONDITIONAL>"
            "<FLEXRAY-FIFOS>"
            "</FLEXRAY-FIFOS>"
            "</FLEXRAY-COMMUNICATION-CONTROLLER-CONDITIONAL>"
            "</FLEXRAY-COMMUNICATION-CONTROLLER-VARIANTS>",
            root_tag="FLEXRAY-COMMUNICATION-CONTROLLER",
        )
        parser.readFlexrayCommunicationController(element, ctrl)
        assert ctrl.getFlexrayFifos() == []

    def test_readEcuInstanceConnectors_can(self, parser):
        from armodel.models import EcuInstance

        instance = EcuInstance(parent=_autosar_root(), short_name="ecu")
        element = _snip(
            "<CONNECTORS>" "<CAN-COMMUNICATION-CONNECTOR>" "<SHORT-NAME>conn</SHORT-NAME>" "</CAN-COMMUNICATION-CONNECTOR>" "</CONNECTORS>",
            root_tag="ECU-INSTANCE",
        )
        parser.readEcuInstanceConnectors(element, instance)
        assert len(instance.getConnectors()) == 1

    def test_readEcuInstanceConnectors_ethernet(self, parser):
        from armodel.models import EcuInstance

        instance = EcuInstance(parent=_autosar_root(), short_name="ecu")
        element = _snip(
            "<CONNECTORS>" "<ETHERNET-COMMUNICATION-CONNECTOR>" "<SHORT-NAME>conn</SHORT-NAME>" "</ETHERNET-COMMUNICATION-CONNECTOR>" "</CONNECTORS>",
            root_tag="ECU-INSTANCE",
        )
        parser.readEcuInstanceConnectors(element, instance)
        assert len(instance.getConnectors()) == 1

    def test_readEcuInstanceConnectors_lin(self, parser):
        from armodel.models import EcuInstance

        instance = EcuInstance(parent=_autosar_root(), short_name="ecu")
        element = _snip(
            "<CONNECTORS>" "<LIN-COMMUNICATION-CONNECTOR>" "<SHORT-NAME>conn</SHORT-NAME>" "</LIN-COMMUNICATION-CONNECTOR>" "</CONNECTORS>",
            root_tag="ECU-INSTANCE",
        )
        parser.readEcuInstanceConnectors(element, instance)
        assert len(instance.getConnectors()) == 1

    def test_readEcuInstanceConnectors_flexray(self, parser):
        from armodel.models import EcuInstance

        instance = EcuInstance(parent=_autosar_root(), short_name="ecu")
        element = _snip(
            "<CONNECTORS>" "<FLEXRAY-COMMUNICATION-CONNECTOR>" "<SHORT-NAME>conn</SHORT-NAME>" "</FLEXRAY-COMMUNICATION-CONNECTOR>" "</CONNECTORS>",
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
        from armodel.models import CanCommunicationConnector, EcuInstance

        instance = EcuInstance(parent=_autosar_root(), short_name="ecu")
        conn = CanCommunicationConnector(parent=instance, short_name="conn")
        element = _snip(
            "<SHORT-NAME>conn</SHORT-NAME>" "<COMM-CONTROLLER-REF DEST='COMMUNICATION-CONTROLLER'>/ctrl</COMM-CONTROLLER-REF>" "<PNC-GATEWAY-TYPE>active</PNC-GATEWAY-TYPE>",
            root_tag="CAN-COMMUNICATION-CONNECTOR",
        )
        parser.readCommunicationConnector(element, conn)
        assert conn.getCommControllerRef().getValue() == "/ctrl"

    def test_readEthernetCommunicationConnector_sets_maximumTransmissionUnit(self, parser):
        from armodel.models import EcuInstance, EthernetCommunicationConnector

        instance = EcuInstance(parent=_autosar_root(), short_name="ecu")
        conn = EthernetCommunicationConnector(parent=instance, short_name="conn")
        element = _snip(
            "<SHORT-NAME>conn</SHORT-NAME>" "<MAXIMUM-TRANSMISSION-UNIT>1500</MAXIMUM-TRANSMISSION-UNIT>",
            root_tag="ETHERNET-COMMUNICATION-CONNECTOR",
        )
        parser.readEthernetCommunicationConnector(element, conn)
        assert conn.getMaximumTransmissionUnit().getValue() == 1500

    def test_readEthernetCommunicationConnectorNetworkEndpointRefs_adds_ref(self, parser):
        from armodel.models import EcuInstance, EthernetCommunicationConnector

        instance = EcuInstance(parent=_autosar_root(), short_name="ecu")
        conn = EthernetCommunicationConnector(parent=instance, short_name="conn")
        element = _snip(
            "<NETWORK-ENDPOINT-REFS>" "<NETWORK-ENDPOINT-REF DEST='NETWORK-ENDPOINT'>/ne</NETWORK-ENDPOINT-REF>" "</NETWORK-ENDPOINT-REFS>",
            root_tag="ETHERNET-COMMUNICATION-CONNECTOR",
        )
        parser.readEthernetCommunicationConnectorNetworkEndpointRefs(element, conn)
        assert len(conn.getNetworkEndpointRefs()) == 1

    def test_readCommunicationConnectorEcuCommPortInstances_framePort(self, parser):
        from armodel.models import CanCommunicationConnector, EcuInstance

        instance = EcuInstance(parent=_autosar_root(), short_name="ecu")
        conn = CanCommunicationConnector(parent=instance, short_name="conn")
        element = _snip(
            "<ECU-COMM-PORT-INSTANCES>" "<FRAME-PORT>" "<SHORT-NAME>fp</SHORT-NAME>" "<COMMUNICATION-DIRECTION>in</COMMUNICATION-DIRECTION>" "</FRAME-PORT>" "</ECU-COMM-PORT-INSTANCES>",
            root_tag="CAN-COMMUNICATION-CONNECTOR",
        )
        parser.readCommunicationConnectorEcuCommPortInstances(element, conn)
        assert len(conn.getEcuCommPortInstances()) == 1

    def test_readCommunicationConnectorEcuCommPortInstances_ipduPort(self, parser):
        from armodel.models import EcuInstance, EthernetCommunicationConnector

        instance = EcuInstance(parent=_autosar_root(), short_name="ecu")
        conn = EthernetCommunicationConnector(parent=instance, short_name="conn")
        element = _snip(
            "<ECU-COMM-PORT-INSTANCES>" "<I-PDU-PORT>" "<SHORT-NAME>ip</SHORT-NAME>" "<KEY-ID>1</KEY-ID>" "</I-PDU-PORT>" "</ECU-COMM-PORT-INSTANCES>",
            root_tag="ETHERNET-COMMUNICATION-CONNECTOR",
        )
        parser.readCommunicationConnectorEcuCommPortInstances(element, conn)
        assert len(conn.getEcuCommPortInstances()) == 1

    def test_readCommunicationConnectorEcuCommPortInstances_iSignalPort(self, parser):
        from armodel.models import CanCommunicationConnector, EcuInstance

        instance = EcuInstance(parent=_autosar_root(), short_name="ecu")
        conn = CanCommunicationConnector(parent=instance, short_name="conn")
        element = _snip(
            "<ECU-COMM-PORT-INSTANCES>" "<I-SIGNAL-PORT>" "<SHORT-NAME>sp</SHORT-NAME>" "<TIMEOUT><VALUE>0.1</VALUE></TIMEOUT>" "</I-SIGNAL-PORT>" "</ECU-COMM-PORT-INSTANCES>",
            root_tag="CAN-COMMUNICATION-CONNECTOR",
        )
        parser.readCommunicationConnectorEcuCommPortInstances(element, conn)
        assert len(conn.getEcuCommPortInstances()) == 1

    def test_readCommunicationConnectorEcuCommPortInstances_unsupported_raises(self, parser):
        from armodel.models import CanCommunicationConnector, EcuInstance

        instance = EcuInstance(parent=_autosar_root(), short_name="ecu")
        conn = CanCommunicationConnector(parent=instance, short_name="conn")
        element = _snip(
            "<ECU-COMM-PORT-INSTANCES><BAD/></ECU-COMM-PORT-INSTANCES>",
            root_tag="CAN-COMMUNICATION-CONNECTOR",
        )
        with pytest.raises(Exception):
            parser.readCommunicationConnectorEcuCommPortInstances(element, conn)

    def test_readCommunicationConnector_sets_optional_attributes(self, parser):
        from armodel.models import CanCommunicationConnector, EcuInstance

        instance = EcuInstance(parent=_autosar_root(), short_name="ecu")
        conn = CanCommunicationConnector(parent=instance, short_name="conn")
        element = _snip(
            "<SHORT-NAME>conn</SHORT-NAME>"
            "<CREATE-ECU-WAKEUP-SOURCE>true</CREATE-ECU-WAKEUP-SOURCE>"
            "<DYNAMIC-PNC-TO-CHANNEL-MAPPING-ENABLED>false</DYNAMIC-PNC-TO-CHANNEL-MAPPING-ENABLED>"
            "<PNC-FILTER-ARRAY-MASKS>"
            "<PNC-FILTER-ARRAY-MASK>255</PNC-FILTER-ARRAY-MASK>"
            "<PNC-FILTER-ARRAY-MASK>1</PNC-FILTER-ARRAY-MASK>"
            "</PNC-FILTER-ARRAY-MASKS>"
            "<PNC-GATEWAY-TYPE>active</PNC-GATEWAY-TYPE>",
            root_tag="CAN-COMMUNICATION-CONNECTOR",
        )
        parser.readCommunicationConnector(element, conn)
        assert conn.getCreateEcuWakeupSource().getValue() is True
        assert conn.getDynamicPncToChannelMappingEnabled().getValue() is False
        assert conn.getPncFilterArrayMasks() == [255, 1]
        assert conn.getPncGatewayType().getValue() == "active"

    def test_readFramePort_sets_communicationDirection(self, parser):
        from armodel.models import CanCommunicationConnector, EcuInstance, FramePort

        instance = EcuInstance(parent=_autosar_root(), short_name="ecu")
        conn = CanCommunicationConnector(parent=instance, short_name="conn")
        port = FramePort(parent=conn, short_name="fp")
        element = _snip(
            "<SHORT-NAME>fp</SHORT-NAME>" "<COMMUNICATION-DIRECTION>in</COMMUNICATION-DIRECTION>",
            root_tag="FRAME-PORT",
        )
        parser.readFramePort(element, port)
        assert port.getCommunicationDirection().getValue() == "in"

    def test_readIPduPort_sets_keyId(self, parser):
        from armodel.models import EcuInstance, EthernetCommunicationConnector, IPduPort

        instance = EcuInstance(parent=_autosar_root(), short_name="ecu")
        conn = EthernetCommunicationConnector(parent=instance, short_name="conn")
        port = IPduPort(parent=conn, short_name="ip")
        element = _snip(
            "<SHORT-NAME>ip</SHORT-NAME>" "<KEY-ID>1</KEY-ID>" "<RX-SECURITY-VERIFICATION>true</RX-SECURITY-VERIFICATION>",
            root_tag="I-PDU-PORT",
        )
        parser.readIPduPort(element, port)
        assert port.getKeyId().getValue() == 1

    def test_readISignalPort_sets_timeout(self, parser):
        from armodel.models import CanCommunicationConnector, EcuInstance, ISignalPort

        instance = EcuInstance(parent=_autosar_root(), short_name="ecu")
        conn = CanCommunicationConnector(parent=instance, short_name="conn")
        port = ISignalPort(parent=conn, short_name="sp")
        element = _snip(
            "<SHORT-NAME>sp</SHORT-NAME>" "<TIMEOUT>0.1</TIMEOUT>",
            root_tag="I-SIGNAL-PORT",
        )
        parser.readISignalPort(element, port)
        assert port.getTimeout().getValue() == 0.1

    def test_readEcuInstanceAssociatedComIPduGroupRefs_adds_ref(self, parser):
        from armodel.models import EcuInstance

        instance = EcuInstance(parent=_autosar_root(), short_name="ecu")
        element = _snip(
            "<ASSOCIATED-COM-I-PDU-GROUP-REFS>" "<ASSOCIATED-COM-I-PDU-GROUP-REF DEST='I-PDU-GROUP'>/grp</ASSOCIATED-COM-I-PDU-GROUP-REF>" "</ASSOCIATED-COM-I-PDU-GROUP-REFS>",
            root_tag="ECU-INSTANCE",
        )
        parser.readEcuInstanceAssociatedComIPduGroupRefs(element, instance)
        assert len(instance.getAssociatedComIPduGroupRefs()) == 1

    def test_readCommunicationController_sets_wakeUpByControllerSupported(self, parser):
        from armodel.models import EcuInstance, EthernetCommunicationController

        instance = EcuInstance(parent=_autosar_root(), short_name="ecu")
        ctrl = EthernetCommunicationController(parent=instance, short_name="ctrl")
        element = _snip(
            "<WAKE-UP-BY-CONTROLLER-SUPPORTED>true</WAKE-UP-BY-CONTROLLER-SUPPORTED>",
            root_tag="ETHERNET-COMMUNICATION-CONTROLLER-CONDITIONAL",
        )
        parser.readCommunicationController(element, ctrl)
        assert ctrl.getWakeUpByControllerSupported().getValue()

    def test_readEthernetCommunicationControllerCouplingPorts_creates_port(self, parser):
        from armodel.models import EcuInstance, EthernetCommunicationController

        instance = EcuInstance(parent=_autosar_root(), short_name="ecu")
        ctrl = EthernetCommunicationController(parent=instance, short_name="ctrl")
        element = _snip(
            "<COUPLING-PORTS>" "<COUPLING-PORT>" "<SHORT-NAME>cp</SHORT-NAME>" "</COUPLING-PORT>" "</COUPLING-PORTS>",
            root_tag="ETHERNET-COMMUNICATION-CONTROLLER-CONDITIONAL",
        )
        parser.readEthernetCommunicationControllerCouplingPorts(element, ctrl)
        assert len(ctrl.getCouplingPorts()) == 1

    def test_readCouplingPort_sets_macLayerType(self, parser):
        from armodel.models import CouplingPort, EcuInstance, EthernetCommunicationController

        instance = EcuInstance(parent=_autosar_root(), short_name="ecu")
        ctrl = EthernetCommunicationController(parent=instance, short_name="ctrl")
        port = CouplingPort(parent=ctrl, short_name="cp")
        element = _snip(
            "<SHORT-NAME>cp</SHORT-NAME>" "<MAC-LAYER-TYPE>ethernet</MAC-LAYER-TYPE>",
            root_tag="COUPLING-PORT",
        )
        parser.readCouplingPort(element, port)
        assert port.getMacLayerType().getValue() == "ethernet"


# ===========================================================================
# Merged from test_arxml_parser_ecuc_values_gaps.py
# Signal/Transformation handlers (L5186-5229) - the non-ECUC subset.
# ===========================================================================


def _make_pkg():
    return _autosar_root().createARPackage("Pkg")


def _make_physical_dimension(short_name="PhysDim"):
    pkg = _make_pkg()
    return pkg.createPhysicalDimension(short_name)


def _make_isignal_group(short_name="ISignalGroup"):
    pkg = _make_pkg()
    return pkg.createISignalGroup(short_name)


class TestReadPhysicalDimension:
    """Tests for readPhysicalDimension (L5186-5196)."""

    def test_with_all_exponents(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        dim = _make_physical_dimension("PhysDim")
        element = _snip(
            """
            <SHORT-NAME>PhysDim</SHORT-NAME>
            <LENGTH-EXP>1</LENGTH-EXP>
            <LUMINOUS-INTENSITY-EXP>2</LUMINOUS-INTENSITY-EXP>
            <MASS-EXP>3</MASS-EXP>
            <MOLAR-AMOUNT-EXP>4</MOLAR-AMOUNT-EXP>
            <TEMPERATURE-EXP>5</TEMPERATURE-EXP>
            <TIME-EXP>6</TIME-EXP>
            <CURRENT-EXP>7</CURRENT-EXP>
            """,
            root_tag="PHYSICAL-DIMENSION",
        )
        parser.readPhysicalDimension(element, dim)
        assert dim.getLengthExp() is not None
        assert dim.getLuminousIntensityExp() is not None
        assert dim.getMassExp() is not None
        assert dim.getMolarAmountExp() is not None
        assert dim.getTemperatureExp() is not None
        assert dim.getTimeExp() is not None
        assert dim.getCurrentExp() is not None

    def test_without_exponents(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        dim = _make_physical_dimension("EmptyDim")
        element = _snip(
            """
            <SHORT-NAME>EmptyDim</SHORT-NAME>
            """,
            root_tag="PHYSICAL-DIMENSION",
        )
        parser.readPhysicalDimension(element, dim)
        assert dim.getLengthExp() is None
        assert dim.getLuminousIntensityExp() is None
        assert dim.getMassExp() is None
        assert dim.getMolarAmountExp() is None
        assert dim.getTemperatureExp() is None
        assert dim.getTimeExp() is None
        assert dim.getCurrentExp() is None


class TestReadISignalGroupISignalRef:
    """Tests for readISignalGroupISignalRef (L5197-5199)."""

    def test_reads_signal_refs(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        group = _make_isignal_group("ISignalGroup")
        element = _snip(
            """
            <I-SIGNAL-REFS>
                <I-SIGNAL-REF DEST="I-SIGNAL">/sig/Signal1</I-SIGNAL-REF>
                <I-SIGNAL-REF DEST="I-SIGNAL">/sig/Signal2</I-SIGNAL-REF>
            </I-SIGNAL-REFS>
            """,
            root_tag="I-SIGNAL-GROUP",
        )
        parser.readISignalGroupISignalRef(element, group)
        refs = group.getISignalRefs()
        assert len(refs) == 2

    def test_empty_signal_refs(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        group = _make_isignal_group("ISignalGroup")
        element = _snip(
            """
            <I-SIGNAL-REFS>
            </I-SIGNAL-REFS>
            """,
            root_tag="I-SIGNAL-GROUP",
        )
        parser.readISignalGroupISignalRef(element, group)
        assert len(group.getISignalRefs()) == 0


class TestReadISignalGroupComBasedSignalGroupTransformation:
    """Tests for readISignalGroupComBasedSignalGroupTransformation (L5201-5203)."""

    def test_reads_transformation_ref(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        group = _make_isignal_group("ISignalGroup")
        element = _snip(
            """
            <COM-BASED-SIGNAL-GROUP-TRANSFORMATIONS>
                <DATA-TRANSFORMATION-REF-CONDITIONAL>
                    <DATA-TRANSFORMATION-REF DEST="DATA-TRANSFORMATION">/trans/Trans1</DATA-TRANSFORMATION-REF>
                </DATA-TRANSFORMATION-REF-CONDITIONAL>
            </COM-BASED-SIGNAL-GROUP-TRANSFORMATIONS>
            """,
            root_tag="I-SIGNAL-GROUP",
        )
        parser.readISignalGroupComBasedSignalGroupTransformation(element, group)
        ref = group.getComBasedSignalGroupTransformationRef()
        assert ref is not None
        assert ref.getValue() == "/trans/Trans1"

    def test_empty_transformations(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        group = _make_isignal_group("ISignalGroup")
        element = _snip(
            """
            <COM-BASED-SIGNAL-GROUP-TRANSFORMATIONS>
            </COM-BASED-SIGNAL-GROUP-TRANSFORMATIONS>
            """,
            root_tag="I-SIGNAL-GROUP",
        )
        parser.readISignalGroupComBasedSignalGroupTransformation(element, group)
        assert group.getComBasedSignalGroupTransformationRef() is None


class TestReadTransformationISignalProps:
    """Tests for readTransformationISignalProps (L5205-5206)."""

    def test_reads_arobject_attributes(self, parser):
        from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import (
            EndToEndTransformationISignalProps,
        )

        AUTOSAR.getInstance().setARRelease("R23-11")
        props = EndToEndTransformationISignalProps()
        element = ET.fromstring(
            f"<END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS-CONDITIONAL " f"xmlns='{NS}' T='2024-01-01T00:00:00' UUID='abc-123'>" f"</END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS-CONDITIONAL>"
        )
        parser.readTransformationISignalProps(element, props)
        assert props.timestamp == "2024-01-01T00:00:00"
        assert props.uuid == "abc-123"

    def test_without_arobject_attributes(self, parser):
        from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import (
            EndToEndTransformationISignalProps,
        )

        AUTOSAR.getInstance().setARRelease("R23-11")
        props = EndToEndTransformationISignalProps()
        element = _snip(
            "",
            root_tag="END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS-CONDITIONAL",
        )
        parser.readTransformationISignalProps(element, props)
        assert props.timestamp is None
        assert props.uuid is None


class TestReadEndToEndTransformationISignalPropsDataIds:
    """Tests for readEndToEndTransformationISignalPropsDataIds (L5208-5211)."""

    def test_with_data_ids(self, parser):
        from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import (
            EndToEndTransformationISignalProps,
        )

        AUTOSAR.getInstance().setARRelease("R23-11")
        props = EndToEndTransformationISignalProps()
        element = _snip(
            """
            <DATA-IDS>
                <DATA-ID>1</DATA-ID>
            </DATA-IDS>
            """,
            root_tag="END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS-CONDITIONAL",
        )
        parser.readEndToEndTransformationISignalPropsDataIds(element, props)
        data_ids = props.getDataIds()
        assert len(data_ids) == 1

    def test_without_data_ids(self, parser):
        from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import (
            EndToEndTransformationISignalProps,
        )

        AUTOSAR.getInstance().setARRelease("R23-11")
        props = EndToEndTransformationISignalProps()
        element = _snip(
            "",
            root_tag="END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS-CONDITIONAL",
        )
        parser.readEndToEndTransformationISignalPropsDataIds(element, props)
        assert len(props.getDataIds()) == 0


class TestReadEndToEndTransformationISignalProps:
    """Tests for readEndToEndTransformationISignalProps (L5213-5219)."""

    def test_full_handler_with_all_fields(self, parser):
        from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import (
            EndToEndTransformationISignalProps,
        )

        AUTOSAR.getInstance().setARRelease("R23-11")
        props = EndToEndTransformationISignalProps()
        element = _snip(
            """
            <END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS-VARIANTS>
                <END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS-CONDITIONAL>
                    <CS-ERROR-REACTION>autonomous</CS-ERROR-REACTION>
                    <TRANSFORMER-REF DEST="TRANSFORMATION-TECHNOLOGY">/trans/Tech1</TRANSFORMER-REF>
                    <DATA-IDS>
                        <DATA-ID>1</DATA-ID>
                    </DATA-IDS>
                    <DATA-LENGTH>64</DATA-LENGTH>
                </END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS-CONDITIONAL>
            </END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS-VARIANTS>
            """,
            root_tag="END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS",
        )
        parser.readEndToEndTransformationISignalProps(element, props)
        assert props.getCsErrorReaction().getValue() == "autonomous"
        assert props.getTransformerRef() is not None
        assert len(props.getDataIds()) == 1
        assert props.getDataLength() is not None

    def test_without_variants_element(self, parser):
        from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import (
            EndToEndTransformationISignalProps,
        )

        AUTOSAR.getInstance().setARRelease("R23-11")
        props = EndToEndTransformationISignalProps()
        element = _snip(
            "",
            root_tag="END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS",
        )
        parser.readEndToEndTransformationISignalProps(element, props)
        assert props.getCsErrorReaction() is None
        assert props.getTransformerRef() is None
        assert len(props.getDataIds()) == 0
        assert props.getDataLength() is None

    def test_minimal_variants_only_transformer_ref(self, parser):
        from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import (
            EndToEndTransformationISignalProps,
        )

        AUTOSAR.getInstance().setARRelease("R23-11")
        props = EndToEndTransformationISignalProps()
        element = _snip(
            """
            <END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS-VARIANTS>
                <END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS-CONDITIONAL>
                    <TRANSFORMER-REF DEST="TRANSFORMATION-TECHNOLOGY">/trans/Tech1</TRANSFORMER-REF>
                </END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS-CONDITIONAL>
            </END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS-VARIANTS>
            """,
            root_tag="END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS",
        )
        parser.readEndToEndTransformationISignalProps(element, props)
        assert props.getCsErrorReaction() is None
        assert props.getTransformerRef() is not None
        assert len(props.getDataIds()) == 0
        assert props.getDataLength() is None


class TestReadISignalGroupTransformationISignalProps:
    """Tests for readISignalGroupTransformationISignalProps (L5221-5229)."""

    def test_reads_end_to_end_transformation_props(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        group = _make_isignal_group("ISignalGroup")
        element = _snip(
            """
            <TRANSFORMATION-I-SIGNAL-PROPSS>
                <END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS>
                    <END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS-VARIANTS>
                        <END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS-CONDITIONAL>
                            <TRANSFORMER-REF DEST="TRANSFORMATION-TECHNOLOGY">/trans/Tech1</TRANSFORMER-REF>
                            <DATA-IDS>
                                <DATA-ID>1</DATA-ID>
                            </DATA-IDS>
                            <DATA-LENGTH>32</DATA-LENGTH>
                        </END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS-CONDITIONAL>
                    </END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS-VARIANTS>
                </END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS>
            </TRANSFORMATION-I-SIGNAL-PROPSS>
            """,
            root_tag="I-SIGNAL-GROUP",
        )
        parser.readISignalGroupTransformationISignalProps(element, group)
        props_list = group.getTransformationISignalProps()
        assert len(props_list) == 1
        props = props_list[0]
        assert props.getTransformerRef() is not None
        assert len(props.getDataIds()) == 1
        assert props.getDataLength() is not None

    def test_empty_transformation_props(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        group = _make_isignal_group("ISignalGroup")
        element = _snip(
            """
            <TRANSFORMATION-I-SIGNAL-PROPSS>
            </TRANSFORMATION-I-SIGNAL-PROPSS>
            """,
            root_tag="I-SIGNAL-GROUP",
        )
        parser.readISignalGroupTransformationISignalProps(element, group)
        assert group.getTransformationISignalProps() == []

    def test_unsupported_type_warning(self, warning_parser, caplog):
        AUTOSAR.getInstance().setARRelease("R23-11")
        group = _make_isignal_group("ISignalGroup")
        element = _snip(
            """
            <TRANSFORMATION-I-SIGNAL-PROPSS>
                <UNKNOWN-TRANSFORMATION-PROPS>
                    <SHORT-NAME>Unknown</SHORT-NAME>
                </UNKNOWN-TRANSFORMATION-PROPS>
                <END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS>
                    <END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS-VARIANTS>
                        <END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS-CONDITIONAL>
                            <TRANSFORMER-REF DEST="TRANSFORMATION-TECHNOLOGY">/trans/Tech1</TRANSFORMER-REF>
                        </END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS-CONDITIONAL>
                    </END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS-VARIANTS>
                </END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS>
            </TRANSFORMATION-I-SIGNAL-PROPSS>
            """,
            root_tag="I-SIGNAL-GROUP",
        )
        import logging

        with caplog.at_level(logging.ERROR):
            warning_parser.readISignalGroupTransformationISignalProps(element, group)
        assert any("Unsupported TransformationISignalProps" in rec.getMessage() for rec in caplog.records)
        props_list = group.getTransformationISignalProps()
        assert len(props_list) == 1
        assert props_list[0].getTransformerRef() is not None


# === Migrated from test_arxml_parser_remaining_gaps.py ===


class TestFrameAndFlexrayTriggering:
    def test_readFrameTriggering_adds_pdu_triggering_ref(self, parser):
        from armodel.models import CanFrameTriggering

        triggering = CanFrameTriggering(parent=MagicMock(), short_name="Cft")
        element = _snip(
            "<PDU-TRIGGERINGS>" "<PDU-TRIGGERING-REF-CONDITIONAL>" '<PDU-TRIGGERING-REF DEST="PDU-TRIGGERING">/pt</PDU-TRIGGERING-REF>' "</PDU-TRIGGERING-REF-CONDITIONAL>" "</PDU-TRIGGERINGS>"
        )
        parser.readFrameTriggering(element, triggering)
        assert len(triggering.getPduTriggeringRefs()) == 1

    def test_readFlexrayAbsolutelyScheduledTimingCommunicationCycle_cycle(self, parser):
        from armodel.models import FlexrayAbsolutelyScheduledTiming

        timing = FlexrayAbsolutelyScheduledTiming()
        element = _snip(
            "<COMMUNICATION-CYCLE>" "<CYCLE-REPETITION>" "<BASE-CYCLE>1</BASE-CYCLE>" "<CYCLE-REPETITION>CYCLE-REPETITION-1</CYCLE-REPETITION>" "</CYCLE-REPETITION>" "</COMMUNICATION-CYCLE>"
        )
        parser.readFlexrayAbsolutelyScheduledTimingCommunicationCycle(element, timing)
        assert timing.getCommunicationCycle() is not None

    def test_readFlexrayAbsolutelyScheduledTimingCommunicationCycle_unsupported_warns(self, warning_parser, caplog):
        from armodel.models import FlexrayAbsolutelyScheduledTiming

        timing = FlexrayAbsolutelyScheduledTiming()
        element = _snip("<COMMUNICATION-CYCLE><BAD/></COMMUNICATION-CYCLE>")
        with caplog.at_level(logging.ERROR):
            warning_parser.readFlexrayAbsolutelyScheduledTimingCommunicationCycle(element, timing)
        assert any("Unsupported CommunicationCycle" in r.getMessage() for r in caplog.records)

    def test_readFlexrayFrameTriggeringAbsolutelyScheduledTimings_unsupported_warns(self, warning_parser, caplog):
        from armodel.models import FlexrayFrameTriggering

        triggering = FlexrayFrameTriggering(parent=MagicMock(), short_name="Fft")
        element = _snip("<ABSOLUTELY-SCHEDULED-TIMINGS><BAD/></ABSOLUTELY-SCHEDULED-TIMINGS>")
        with caplog.at_level(logging.ERROR):
            warning_parser.readFlexrayFrameTriggeringAbsolutelyScheduledTimings(element, triggering)
        assert any("Unsupported AbsolutelyScheduledTiming" in r.getMessage() for r in caplog.records)

    def test_getFlexrayFifoRange_sets_rangeMax_and_rangeMin(self, parser):
        element = _snip(
            "<FLEXRAY-FIFO-RANGE>" "<RANGE-MAX>200</RANGE-MAX>" "<RANGE-MIN>100</RANGE-MIN>" "</FLEXRAY-FIFO-RANGE>",
            root_tag="ROOT",
        )
        fifo_range = parser.getFlexrayFifoRange(element, "FLEXRAY-FIFO-RANGE")
        assert fifo_range is not None
        assert fifo_range.getRangeMax().getValue() == 200
        assert fifo_range.getRangeMin().getValue() == 100

    def test_getFlexrayFifoRange_absent_returns_none(self, parser):
        element = _snip("", root_tag="ROOT")
        assert parser.getFlexrayFifoRange(element, "FLEXRAY-FIFO-RANGE") is None

    def test_getFlexrayFifoConfiguration_reads_fields(self, parser):
        element = _snip(
            "<FLEXRAY-FIFO-CONFIGURATION>"
            "<ADMIT-WITHOUT-MESSAGE-ID>true</ADMIT-WITHOUT-MESSAGE-ID>"
            "<BASE-CYCLE>2</BASE-CYCLE>"
            "<CHANNEL-REF DEST='FLEXRAY-PHYSICAL-CHANNEL'>/FlexrayCluster/ChannelA</CHANNEL-REF>"
            "<CYCLE-REPETITION>4</CYCLE-REPETITION>"
            "<FIFO-DEPTH>8</FIFO-DEPTH>"
            "<FLEXRAY-FIFO-RANGE><RANGE-MAX>200</RANGE-MAX><RANGE-MIN>100</RANGE-MIN></FLEXRAY-FIFO-RANGE>"
            "<MSG-ID-MASK>16</MSG-ID-MASK>"
            "<MSG-ID-MATCH>32</MSG-ID-MATCH>"
            "</FLEXRAY-FIFO-CONFIGURATION>",
            root_tag="ROOT",
        )
        config = parser.getFlexrayFifoConfiguration(element, "FLEXRAY-FIFO-CONFIGURATION")
        assert config is not None
        assert config.getAdmitWithoutMessageId().getValue() is True
        assert config.getBaseCycle().getValue() == 2
        assert config.getChannelRef().getValue() == "/FlexrayCluster/ChannelA"
        assert config.getCycleRepetition().getValue() == 4
        assert config.getFifoDepth().getValue() == 8
        ranges = config.getFlexrayFifoRanges()
        assert len(ranges) == 1
        assert ranges[0].getRangeMax().getValue() == 200
        assert ranges[0].getRangeMin().getValue() == 100
        assert config.getMsgIdMask().getValue() == 16
        assert config.getMsgIdMatch().getValue() == 32

    def test_getFlexrayFifoConfiguration_absent_returns_none(self, parser):
        element = _snip("", root_tag="ROOT")
        assert parser.getFlexrayFifoConfiguration(element, "FLEXRAY-FIFO-CONFIGURATION") is None


# ==================== PduTriggering / PhysicalChannel (L3084, L3112, L3121, L3148-3152) ====================


# === Migrated from test_arxml_parser_remaining_gaps.py ===


class TestPduAndPhysicalChannel:
    def test_readPduTriggering_adds_isignal_triggering_ref(self, parser):
        from armodel.models import PduTriggering

        triggering = PduTriggering(parent=MagicMock(), short_name="Pt")
        element = _snip(
            "<I-SIGNAL-TRIGGERINGS>"
            "<I-SIGNAL-TRIGGERING-REF-CONDITIONAL>"
            '<I-SIGNAL-TRIGGERING-REF DEST="I-SIGNAL-TRIGGERING">/ist</I-SIGNAL-TRIGGERING-REF>'
            "</I-SIGNAL-TRIGGERING-REF-CONDITIONAL>"
            "</I-SIGNAL-TRIGGERINGS>"
        )
        parser.readPduTriggering(element, triggering)
        assert len(triggering.getISignalTriggeringRefs()) == 1

    def test_readPhysicalChannelFrameTriggerings_unsupported_warns(self, warning_parser, caplog):
        from armodel.models import CanPhysicalChannel

        channel = CanPhysicalChannel(parent=MagicMock(), short_name="Ch")
        element = _snip("<FRAME-TRIGGERINGS><BAD/></FRAME-TRIGGERINGS>")
        with caplog.at_level(logging.ERROR):
            warning_parser.readPhysicalChannelFrameTriggerings(element, channel)
        assert any("Unsupported Frame Triggering" in r.getMessage() for r in caplog.records)

    def test_readPhysicalChannelPduTriggerings_unsupported_warns(self, warning_parser, caplog):
        from armodel.models import CanPhysicalChannel

        channel = CanPhysicalChannel(parent=MagicMock(), short_name="Ch")
        element = _snip("<PDU-TRIGGERINGS><BAD/></PDU-TRIGGERINGS>")
        with caplog.at_level(logging.ERROR):
            warning_parser.readPhysicalChannelPduTriggerings(element, channel)
        assert any("Unsupported Frame Triggering" in r.getMessage() for r in caplog.records)

    def test_readPhysicalChannelISignalTriggerings_unsupported_warns(self, warning_parser, caplog):
        from armodel.models import CanPhysicalChannel

        channel = CanPhysicalChannel(parent=MagicMock(), short_name="Ch")
        element = _snip("<I-SIGNAL-TRIGGERINGS><BAD/></I-SIGNAL-TRIGGERINGS>")
        with caplog.at_level(logging.ERROR):
            warning_parser.readPhysicalChannelISignalTriggerings(element, channel)
        assert any("Unsupported Frame Triggering" in r.getMessage() for r in caplog.records)

    def test_readLinScheduleTableTableEntries_application_entry(self, parser):
        from armodel.models import LinScheduleTable

        table = LinScheduleTable(parent=MagicMock(), short_name="St")
        element = _snip(
            "<TABLE-ENTRYS>"
            "<APPLICATION-ENTRY>"
            "<SHORT-NAME>ae</SHORT-NAME>"
            "<DELAY>0.1</DELAY>"
            "<POSITION-IN-TABLE>1</POSITION-IN-TABLE>"
            '<FRAME-TRIGGERING-REF DEST="FRAME-TRIGGERING">/ft</FRAME-TRIGGERING-REF>'
            "</APPLICATION-ENTRY>"
            "</TABLE-ENTRYS>"
        )
        parser.readLinScheduleTableTableEntries(element, table)
        assert len(table.getTableEntries()) == 1

    def test_readLinScheduleTableTableEntries_unsupported_warns(self, warning_parser, caplog):
        from armodel.models import LinScheduleTable

        table = LinScheduleTable(parent=MagicMock(), short_name="St")
        element = _snip("<TABLE-ENTRYS><BAD/></TABLE-ENTRYS>")
        with caplog.at_level(logging.ERROR):
            warning_parser.readLinScheduleTableTableEntries(element, table)
        assert any("Unsupported Schedule Table" in r.getMessage() for r in caplog.records)


# ==================== SocketConnection (L3239, L3250, L3264, L3277) ====================


# === Migrated from test_arxml_parser_remaining_gaps.py ===


class TestSocketConnection:
    def test_getSocketConnectionPdus_unsupported_warns(self, warning_parser, caplog):
        element = _snip("<PDUS><BAD/></PDUS>")
        with caplog.at_level(logging.ERROR):
            result = warning_parser.getSocketConnectionPdus(element)
        assert result == []
        assert any("Unsupported Pdu" in r.getMessage() for r in caplog.records)

    def test_getSocketConnection_with_pdus(self, parser):
        element = _snip(
            "<CLIENT-IP-ADDR-FROM-CONNECTION-REQUEST>true</CLIENT-IP-ADDR-FROM-CONNECTION-REQUEST>"
            "<PDUS>"
            "<SOCKET-CONNECTION-IPDU-IDENTIFIER>"
            "<SHORT-NAME>p</SHORT-NAME>"
            '<TP-CONFIG-REF DEST="I-PDU-REF">/ipdu</TP-CONFIG-REF>'
            "</SOCKET-CONNECTION-IPDU-IDENTIFIER>"
            "</PDUS>"
        )
        result = parser.getSocketConnection(element)
        assert result is not None
        assert len(result.getPdus()) == 1

    def test_readSocketConnectionBundleConnections_unsupported_warns(self, warning_parser, caplog):
        from armodel.models import SocketConnectionBundle

        bundle = SocketConnectionBundle(parent=MagicMock(), short_name="Scb")
        element = _snip("<BUNDLED-CONNECTIONS><BAD/></BUNDLED-CONNECTIONS>")
        with caplog.at_level(logging.ERROR):
            warning_parser.readSocketConnectionBundleConnections(element, bundle)
        assert any("Unsupported Bundled Connection" in r.getMessage() for r in caplog.records)

    def test_readSoAdConfigConnectionBundles_unsupported_warns(self, warning_parser, caplog):
        from armodel.models import SoAdConfig

        config = SoAdConfig()
        element = _snip("<CONNECTION-BUNDLES><BAD/></CONNECTION-BUNDLES>")
        with caplog.at_level(logging.ERROR):
            warning_parser.readSoAdConfigConnectionBundles(element, config)
        assert any("Unsupported Connection Bundle" in r.getMessage() for r in caplog.records)


# ==================== ServiceInstance (L3363-3366, L3370-3375, L3405, L3408, L3418, L3429-3434) ====================


# === Migrated from test_arxml_parser_remaining_gaps.py ===


class TestSystemSignalGroup:
    def test_readSystemSignalGroup_adds_refs(self, parser):
        from armodel.models import SystemSignalGroup

        group = SystemSignalGroup(parent=MagicMock(), short_name="Ssg")
        element = _snip(
            "<SYSTEM-SIGNAL-REFS>" '<SYSTEM-SIGNAL-REF DEST="SYSTEM-SIGNAL">/s1</SYSTEM-SIGNAL-REF>' '<SYSTEM-SIGNAL-REF DEST="SYSTEM-SIGNAL">/s2</SYSTEM-SIGNAL-REF>' "</SYSTEM-SIGNAL-REFS>"
        )
        parser.readSystemSignalGroup(element, group)
        assert len(group.getSystemSignalRefs()) == 2
        assert group.getSystemSignalRefs()[0].getValue() == "/s1"
        assert group.getSystemSignalRefs()[1].getValue() == "/s2"

    def test_readSystemSignalGroup_adds_transforming_ref(self, parser):
        from armodel.models import SystemSignalGroup

        group = SystemSignalGroup(parent=MagicMock(), short_name="Ssg")
        element = _snip('<TRANSFORMING-SYSTEM-SIGNAL-REF DEST="SYSTEM-SIGNAL">/trans</TRANSFORMING-SYSTEM-SIGNAL-REF>')
        parser.readSystemSignalGroup(element, group)
        assert group.getTransformingSystemSignalRef() is not None
        assert group.getTransformingSystemSignalRef().getValue() == "/trans"

    def test_readSystemSignalGroup_absent_transforming_ref_stays_none(self, parser):
        from armodel.models import SystemSignalGroup

        group = SystemSignalGroup(parent=MagicMock(), short_name="Ssg")
        element = _snip("<SHORT-NAME>Ssg</SHORT-NAME>")
        parser.readSystemSignalGroup(element, group)
        assert group.getTransformingSystemSignalRef() is None


# ==================== ISignalIPduGroup (L5351, L5360, L5362) ====================


# === Migrated from test_arxml_parser_remaining_gaps.py ===


class TestISignalIPduGroup:
    def test_getISignalIPduRefs_returns_refs(self, parser):
        element = _snip(
            "<I-SIGNAL-I-PDUS>" "<I-SIGNAL-I-PDU-REF-CONDITIONAL>" '<I-SIGNAL-I-PDU-REF DEST="I-SIGNAL-I-PDU">/p1</I-SIGNAL-I-PDU-REF>' "</I-SIGNAL-I-PDU-REF-CONDITIONAL>" "</I-SIGNAL-I-PDUS>"
        )
        result = parser.getISignalIPduRefs(element)
        assert len(result) == 1

    def test_readISignalIPduGroup_adds_contained_ref(self, parser):
        from armodel.models import ISignalIPduGroup

        group = ISignalIPduGroup(parent=MagicMock(), short_name="Isg")
        element = _snip(
            "<COMMUNICATION-DIRECTION>IN</COMMUNICATION-DIRECTION>"
            "<COMMUNICATION-MODE>SEND</COMMUNICATION-MODE>"
            "<CONTAINED-I-SIGNAL-I-PDU-GROUP-REFS>"
            '<CONTAINED-I-SIGNAL-I-PDU-GROUP-REF DEST="I-SIGNAL-I-PDU-GROUP">/g</CONTAINED-I-SIGNAL-I-PDU-GROUP-REF>'
            "</CONTAINED-I-SIGNAL-I-PDU-GROUP-REFS>"
        )
        parser.readISignalIPduGroup(element, group)
        assert group.getCommunicationDirection() is not None
        assert len(group.getContainedISignalIPduGroupRefs()) == 1

    def test_readISignalIPduGroup_adds_i_signal_i_pdu_ref(self, parser):
        from armodel.models import ISignalIPduGroup

        group = ISignalIPduGroup(parent=MagicMock(), short_name="Isg")
        element = _snip(
            "<I-SIGNAL-I-PDUS>" "<I-SIGNAL-I-PDU-REF-CONDITIONAL>" '<I-SIGNAL-I-PDU-REF DEST="I-SIGNAL-I-PDU">/p1</I-SIGNAL-I-PDU-REF>' "</I-SIGNAL-I-PDU-REF-CONDITIONAL>" "</I-SIGNAL-I-PDUS>"
        )
        parser.readISignalIPduGroup(element, group)
        assert len(group.getISignalIPduRefs()) == 1


# ==================== SystemMapping (L5437, L5451, L5466, L5483) ====================
