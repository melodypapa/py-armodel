"""Tests for writer frame triggering and physical channel handlers."""
import xml.etree.cElementTree as ET
from unittest.mock import MagicMock
import pytest
from armodel.writer.arxml_writer import ARXMLWriter
from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanCommunication import (  # noqa: E501
    CanFrameTriggering, RxIdentifierRange,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication import (  # noqa: E501
    ApplicationEntry, LinFrameTriggering, LinScheduleTable,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Flexray.FlexrayCommunication import (  # noqa: E501
    FlexrayAbsolutelyScheduledTiming, FlexrayFrameTriggering,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Flexray.FlexrayTopology import (  # noqa: E501
    FlexrayCluster,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (  # noqa: E501
    ISignalTriggering, PduTriggering,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import (  # noqa: E501
    CanCluster, CanClusterBusOffRecovery, CanPhysicalChannel,
    CycleRepetition, EthernetPhysicalChannel, FlexrayPhysicalChannel,
    LinCluster, LinPhysicalChannel,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetCommunication import (  # noqa: E501
    SocketConnection, SocketConnectionBundle,
    SocketConnectionIpduIdentifier,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (  # noqa: E501
    InitialSdDelayConfig, RequestResponseDelay, SdClientConfig,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.NetworkEndpoint import (  # noqa: E501
    DoIpEntity, InfrastructureServices, Ipv6Configuration, NetworkEndpoint,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import (  # noqa: E501
    ApplicationEndpoint, ConsumedEventGroup, ConsumedServiceInstance,
    EventHandler, GenericTp, ProvidedServiceInstance, SdServerConfig,
    SoAdConfig, SocketAddress, TcpTp, TpPort, UdpTp,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (  # noqa: E501
    ARBoolean, ARLiteral, Integer, PositiveInteger, RefType, TimeValue,
)


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def writer():
    AUTOSAR.getInstance().new()
    return ARXMLWriter()


def _parent():
    return ET.Element("PARENT")


def _pkg():
    return AUTOSAR.getInstance().createARPackage("Pkg")


def _literal(text):
    lit = ARLiteral()
    lit.setValue(text)
    return lit


def _boolean(val):
    b = ARBoolean()
    b.setValue(val)
    return b


def _pos_int(text):
    val = PositiveInteger()
    val.setValue(text)
    return val


def _integer(text):
    val = Integer()
    val.setValue(text)
    return val


def _time(text):
    val = TimeValue()
    val.setValue(text)
    return val


def _ref(dest, value):
    ref = RefType()
    ref.setDest(dest)
    ref.setValue(value)
    return ref


def _warning_writer():
    return ARXMLWriter(options={"warning": True})


class TestWriteFrameTriggering:
    def test_write_frame_triggering_empty(self, writer):
        pkg = _pkg()
        ft = CanFrameTriggering(pkg, "Ft")
        parent = _parent()
        writer.writeFrameTriggering(parent, ft)
        assert parent.find("SHORT-NAME") is not None

    def test_write_frame_triggering_with_refs(self, writer):
        pkg = _pkg()
        ft = CanFrameTriggering(pkg, "Ft")
        ft.addFramePortRef(_ref("FRAME-PORT", "/fp1"))
        ft.addFramePortRef(_ref("FRAME-PORT", "/fp2"))
        ft.setFrameRef(_ref("FRAME", "/frame1"))
        ft.addPduTriggeringRef(_ref("PDU-TRIGGERING", "/pt1"))
        parent = _parent()
        writer.writeFrameTriggering(parent, ft)
        refs_tag = parent.find("FRAME-PORT-REFS")
        assert refs_tag is not None
        assert len(refs_tag.findall("FRAME-PORT-REF")) == 2
        assert parent.find("FRAME-REF") is not None
        trigs = parent.find("PDU-TRIGGERINGS")
        assert trigs is not None
        assert (
            len(trigs.findall("PDU-TRIGGERING-REF-CONDITIONAL")) == 1
        )


class TestWriteCanFrameTriggering:
    def test_write_can_frame_triggering_full(self, writer):
        pkg = _pkg()
        ft = CanFrameTriggering(pkg, "CanFt")
        ft.setCanAddressingMode(_literal("STANDARD"))
        ft.setCanFdFrameSupport(_boolean("true"))
        ft.setCanFrameRxBehavior(_literal("CAN-FD"))
        ft.setCanFrameTxBehavior(_literal("CAN-FD"))
        ft.setIdentifier(_pos_int("100"))
        rng = RxIdentifierRange()
        rng.setLowerCanId(_pos_int("10"))
        rng.setUpperCanId(_pos_int("20"))
        ft.setRxIdentifierRange(rng)
        parent = _parent()
        writer.writeCanFrameTriggering(parent, ft)
        cft = parent.find("CAN-FRAME-TRIGGERING")
        assert cft is not None
        assert cft.find("CAN-ADDRESSING-MODE").text == "STANDARD"
        assert cft.find("CAN-FD-FRAME-SUPPORT").text == "true"
        assert cft.find("CAN-FRAME-RX-BEHAVIOR").text == "CAN-FD"
        assert cft.find("CAN-FRAME-TX-BEHAVIOR").text == "CAN-FD"
        assert cft.find("IDENTIFIER").text == "100"
        rng_tag = cft.find("RX-IDENTIFIER-RANGE")
        assert rng_tag is not None
        assert rng_tag.find("LOWER-CAN-ID").text == "10"
        assert rng_tag.find("UPPER-CAN-ID").text == "20"


class TestWriteLinFrameTriggering:
    def test_write_lin_frame_triggering_full(self, writer):
        pkg = _pkg()
        ft = LinFrameTriggering(pkg, "LinFt")
        ft.setIdentifier(_pos_int("5"))
        ft.setLinChecksum(_literal("CLASSIC"))
        parent = _parent()
        writer.writeLinFrameTriggering(parent, ft)
        lft = parent.find("LIN-FRAME-TRIGGERING")
        assert lft is not None
        assert lft.find("IDENTIFIER").text == "5"
        assert lft.find("LIN-CHECKSUM").text == "CLASSIC"


class TestWriteCommunicationCycle:
    def test_write_communication_cycle(self, writer):
        cycle = CycleRepetition()
        parent = _parent()
        writer.writeCommunicationCycle(parent, cycle)
        assert len(parent) == 0

    def test_write_cycle_repetition_none(self, writer):
        parent = _parent()
        writer.writeCycleRepetition(parent, None)
        assert len(parent) == 0

    def test_write_cycle_repetition_full(self, writer):
        cycle = CycleRepetition()
        cycle.setBaseCycle(_integer("2"))
        cycle.setCycleRepetition(_literal("C1"))
        parent = _parent()
        writer.writeCycleRepetition(parent, cycle)
        rep = parent.find("CYCLE-REPETITION")
        assert rep is not None
        assert rep.find("BASE-CYCLE").text == "2"
        assert rep.find("CYCLE-REPETITION").text == "C1"


class TestWriteFlexrayAbsolutelyScheduledTiming:
    def test_write_comm_cycle_no_cycle(self, writer):
        timing = FlexrayAbsolutelyScheduledTiming()
        parent = _parent()
        writer.writeFlexrayAbsolutelyScheduledTimingCommunicationCycle(
            parent, timing
        )
        assert len(parent) == 0

    def test_write_comm_cycle_with_repetition(self, writer):
        timing = FlexrayAbsolutelyScheduledTiming()
        cycle = CycleRepetition()
        cycle.setBaseCycle(_integer("1"))
        timing.setCommunicationCycle(cycle)
        parent = _parent()
        writer.writeFlexrayAbsolutelyScheduledTimingCommunicationCycle(
            parent, timing
        )
        cc = parent.find("COMMUNICATION-CYCLE")
        assert cc is not None
        assert cc.find("CYCLE-REPETITION") is not None

    def test_write_comm_cycle_unsupported_warns(self):
        w = _warning_writer()
        timing = FlexrayAbsolutelyScheduledTiming()
        timing.setCommunicationCycle("not_a_cycle")
        parent = _parent()
        w.writeFlexrayAbsolutelyScheduledTimingCommunicationCycle(
            parent, timing
        )
        assert len(parent) == 1

    def test_write_flexray_abs_scheduled_timing_none(self, writer):
        parent = _parent()
        writer.writeFlexrayAbsolutelyScheduledTiming(parent, None)
        assert len(parent) == 0

    def test_write_flexray_abs_scheduled_timing_full(self, writer):
        timing = FlexrayAbsolutelyScheduledTiming()
        cycle = CycleRepetition()
        cycle.setBaseCycle(_integer("3"))
        timing.setCommunicationCycle(cycle)
        timing.setSlotID(_pos_int("7"))
        parent = _parent()
        writer.writeFlexrayAbsolutelyScheduledTiming(parent, timing)
        tag = parent.find("FLEXRAY-ABSOLUTELY-SCHEDULED-TIMING")
        assert tag is not None
        assert tag.find("COMMUNICATION-CYCLE") is not None
        assert tag.find("SLOT-ID").text == "7"


class TestWriteFlexrayFrameTriggering:
    def test_write_flexray_ft_no_timings(self, writer):
        pkg = _pkg()
        ft = FlexrayFrameTriggering(pkg, "FlFt")
        parent = _parent()
        writer.writeFlexrayFrameTriggering(parent, ft)
        fft = parent.find("FLEXRAY-FRAME-TRIGGERING")
        assert fft is not None

    def test_write_flexray_ft_abs_timings_empty(self, writer):
        pkg = _pkg()
        ft = FlexrayFrameTriggering(pkg, "FlFt")
        parent = _parent()
        writer.writeFlexrayFrameTriggeringAbsolutelyScheduledTimings(
            parent, ft
        )
        assert len(parent) == 0

    def test_write_flexray_ft_abs_timings_warns(self):
        w = _warning_writer()
        pkg = _pkg()
        ft = FlexrayFrameTriggering(pkg, "FlFt")
        ft.addAbsolutelyScheduledTiming("not_a_timing")
        parent = _parent()
        w.writeFlexrayFrameTriggeringAbsolutelyScheduledTimings(
            parent, ft
        )
        assert len(parent) == 1

    def test_write_flexray_ft_full(self, writer):
        pkg = _pkg()
        ft = FlexrayFrameTriggering(pkg, "FlFt")
        timing = FlexrayAbsolutelyScheduledTiming()
        timing.setSlotID(_pos_int("9"))
        ft.addAbsolutelyScheduledTiming(timing)
        ft.setAllowDynamicLSduLength(_boolean("true"))
        ft.setMessageId(_pos_int("42"))
        ft.setPayloadPreambleIndicator(_boolean("false"))
        parent = _parent()
        writer.writeFlexrayFrameTriggering(parent, ft)
        fft = parent.find("FLEXRAY-FRAME-TRIGGERING")
        assert fft is not None
        timings = fft.find("ABSOLUTELY-SCHEDULED-TIMINGS")
        assert timings is not None
        assert fft.find("ALLOW-DYNAMIC-L-SDU-LENGTH").text == "true"
        assert fft.find("MESSAGE-ID").text == "42"
        assert (
            fft.find("PAYLOAD-PREAMBLE-INDICATOR").text == "false"
        )


class TestWriteISignalTriggering:
    def test_write_isignal_triggering_empty(self, writer):
        pkg = _pkg()
        st = ISignalTriggering(pkg, "St")
        parent = _parent()
        writer.writeISignalTriggering(parent, st)
        ist = parent.find("I-SIGNAL-TRIGGERING")
        assert ist is not None

    def test_write_isignal_triggering_full(self, writer):
        pkg = _pkg()
        st = ISignalTriggering(pkg, "St")
        st.setISignalGroupRef(_ref("I-SIGNAL-GROUP", "/sg"))
        st.addISignalPortRef(_ref("I-SIGNAL-PORT", "/sp1"))
        st.setISignalRef(_ref("I-SIGNAL", "/sig"))
        parent = _parent()
        writer.writeISignalTriggering(parent, st)
        ist = parent.find("I-SIGNAL-TRIGGERING")
        assert ist is not None
        assert ist.find("I-SIGNAL-GROUP-REF") is not None
        refs = ist.find("I-SIGNAL-PORT-REFS")
        assert refs is not None
        assert len(refs.findall("I-SIGNAL-PORT-REF")) == 1
        assert ist.find("I-SIGNAL-REF") is not None


class TestWritePduTriggering:
    def test_write_pdu_triggering_empty(self, writer):
        pkg = _pkg()
        pt = PduTriggering(pkg, "Pt")
        parent = _parent()
        writer.writePduTriggering(parent, pt)
        ptt = parent.find("PDU-TRIGGERING")
        assert ptt is not None

    def test_write_pdu_triggering_full(self, writer):
        pkg = _pkg()
        pt = PduTriggering(pkg, "Pt")
        pt.addIPduPortRef(_ref("I-PDU-PORT", "/pp1"))
        pt.setIPduRef(_ref("I-PDU", "/ipdu"))
        pt.addISignalTriggeringRef(_ref("I-SIGNAL-TRIGGERING", "/ist"))
        parent = _parent()
        writer.writePduTriggering(parent, pt)
        ptt = parent.find("PDU-TRIGGERING")
        assert ptt is not None
        refs = ptt.find("I-PDU-PORT-REFS")
        assert refs is not None
        assert len(refs.findall("I-PDU-PORT-REF")) == 1
        assert ptt.find("I-PDU-REF") is not None
        trigs = ptt.find("I-SIGNAL-TRIGGERINGS")
        assert trigs is not None
        assert (
            len(trigs.findall("I-SIGNAL-TRIGGERING-REF-CONDITIONAL"))
            == 1
        )


class TestWritePhysicalChannelHelpers:
    def test_write_pc_comm_connector_refs_empty(self, writer):
        pkg = _pkg()
        ch = CanPhysicalChannel(pkg, "Ch")
        parent = _parent()
        writer.writePhysicalChannelCommConnectorRefs(parent, ch)
        assert len(parent) == 0

    def test_write_pc_comm_connector_refs(self, writer):
        pkg = _pkg()
        ch = CanPhysicalChannel(pkg, "Ch")
        ch.addCommConnectorRef(_ref("COMMUNICATION-CONNECTOR", "/cc"))
        parent = _parent()
        writer.writePhysicalChannelCommConnectorRefs(parent, ch)
        conns = parent.find("COMM-CONNECTORS")
        assert conns is not None
        assert (
            len(conns.findall("COMMUNICATION-CONNECTOR-REF-CONDITIONAL"))
            == 1
        )

    def test_write_pc_frame_triggerings_warns(self):
        w = _warning_writer()
        ch = MagicMock()
        ch.getFrameTriggerings.return_value = ["not_a_triggering"]
        parent = _parent()
        w.writePhysicalChannelFrameTriggerings(parent, ch)
        assert parent.find("FRAME-TRIGGERINGS") is not None

    def test_write_pc_frame_triggerings_lin(self, writer):
        pkg = _pkg()
        ch = CanPhysicalChannel(pkg, "Ch")
        ch.createLinFrameTriggering("Lft")
        parent = _parent()
        writer.writePhysicalChannelFrameTriggerings(parent, ch)
        trig = parent.find("FRAME-TRIGGERINGS")
        assert trig is not None
        assert trig.find("LIN-FRAME-TRIGGERING") is not None

    def test_write_pc_frame_triggerings_flexray(self, writer):
        pkg = _pkg()
        ch = CanPhysicalChannel(pkg, "Ch")
        ch.createFlexrayFrameTriggering("Flft")
        parent = _parent()
        writer.writePhysicalChannelFrameTriggerings(parent, ch)
        trig = parent.find("FRAME-TRIGGERINGS")
        assert trig is not None
        assert (
            trig.find("FLEXRAY-FRAME-TRIGGERING") is not None
        )

    def test_write_pc_isignal_triggerings_warns_branch(self):
        w = _warning_writer()
        ch = MagicMock()
        ch.getISignalTriggerings.return_value = [
            "not_isignal_triggering"
        ]
        parent = _parent()
        w.writePhysicalChannelISignalTriggerings(parent, ch)
        assert parent.find("I-SIGNAL-TRIGGERINGS") is not None

    def test_write_pc_pdu_triggerings_warns_branch(self):
        w = _warning_writer()
        ch = MagicMock()
        ch.getPduTriggerings.return_value = ["not_pdu_triggering"]
        parent = _parent()
        w.writePhysicalChannelPduTriggerings(parent, ch)
        assert parent.find("PDU-TRIGGERINGS") is not None

    def test_write_pc_isignal_triggerings_warns(self):
        w = _warning_writer()
        pkg = _pkg()
        ch = CanPhysicalChannel(pkg, "Ch")
        ch.addElement(MagicMock())
        parent = _parent()
        w.writePhysicalChannelISignalTriggerings(parent, ch)
        assert len(parent) == 0

    def test_write_pc_pdu_triggerings_warns(self):
        w = _warning_writer()
        pkg = _pkg()
        ch = CanPhysicalChannel(pkg, "Ch")
        ch.addElement(MagicMock())
        parent = _parent()
        w.writePhysicalChannelPduTriggerings(parent, ch)
        assert len(parent) == 0


class TestWritePhysicalChannel:
    def test_write_physical_channel_with_triggerings(self, writer):
        pkg = _pkg()
        ch = CanPhysicalChannel(pkg, "Ch")
        ch.addCommConnectorRef(_ref("COMMUNICATION-CONNECTOR", "/cc"))
        ch.createCanFrameTriggering("Cft")
        ch.createISignalTriggering("Ist")
        ch.createPduTriggering("Pt")
        parent = _parent()
        writer.writePhysicalChannel(parent, ch)
        assert parent.find("COMM-CONNECTORS") is not None
        assert parent.find("FRAME-TRIGGERINGS") is not None
        assert parent.find("I-SIGNAL-TRIGGERINGS") is not None
        assert parent.find("PDU-TRIGGERINGS") is not None


class TestWriteCanPhysicalChannel:
    def test_write_can_physical_channel(self, writer):
        pkg = _pkg()
        ch = CanPhysicalChannel(pkg, "CanCh")
        parent = _parent()
        writer.writeCanPhysicalChannel(parent, ch)
        cpc = parent.find("CAN-PHYSICAL-CHANNEL")
        assert cpc is not None


class TestWriteScheduleTableEntry:
    def test_write_schedule_table_entry(self, writer):
        entry = ApplicationEntry()
        entry.setDelay(_time("0.01"))
        entry.setPositionInTable(_integer("1"))
        parent = _parent()
        writer.writeScheduleTableEntry(parent, entry)
        assert parent.find("DELAY").text == "0.01"
        assert parent.find("POSITION-IN-TABLE").text == "1"

    def test_set_application_entry_none(self, writer):
        parent = _parent()
        writer.setApplicationEntry(parent, "APP-ENTRY", None)
        assert len(parent) == 0

    def test_set_application_entry_full(self, writer):
        entry = ApplicationEntry()
        entry.setDelay(_time("0.02"))
        entry.setFrameTriggeringRef(_ref("FRAME-TRIGGERING", "/ft"))
        parent = _parent()
        writer.setApplicationEntry(parent, "APPLICATION-ENTRY", entry)
        ae = parent.find("APPLICATION-ENTRY")
        assert ae is not None
        assert ae.find("DELAY").text == "0.02"
        assert ae.find("FRAME-TRIGGERING-REF") is not None


class TestWriteLinScheduleTable:
    def test_write_lin_schedule_table_empty_entries(self, writer):
        pkg = _pkg()
        table = LinScheduleTable(pkg, "Table")
        table.setResumePosition(_literal("startFromBeginning"))
        table.setRunMode(_literal("RUN"))
        parent = _parent()
        writer.writeLinScheduleTable(parent, table)
        lst = parent.find("LIN-SCHEDULE-TABLE")
        assert lst is not None
        assert lst.find("RESUME-POSITION").text == "startFromBeginning"
        assert lst.find("RUN-MODE").text == "RUN"

    def test_write_lin_schedule_table_table_entries_warns(self):
        w = _warning_writer()
        pkg = _pkg()
        table = LinScheduleTable(pkg, "Table")
        table.addTableEntry("not_an_entry")
        parent = _parent()
        w.writeLinScheduleTableTableEntries(parent, table)
        assert len(parent) == 1

    def test_write_lin_schedule_table_with_entries(self, writer):
        pkg = _pkg()
        table = LinScheduleTable(pkg, "Table")
        entry = ApplicationEntry()
        entry.setDelay(_time("0.05"))
        entry.setFrameTriggeringRef(_ref("FRAME-TRIGGERING", "/ft"))
        table.addTableEntry(entry)
        parent = _parent()
        writer.writeLinScheduleTable(parent, table)
        lst = parent.find("LIN-SCHEDULE-TABLE")
        entries = lst.find("TABLE-ENTRYS")
        assert entries is not None
        assert len(entries.findall("APPLICATION-ENTRY")) == 1


class TestWriteLinPhysicalChannel:
    def test_write_lin_physical_channel_no_tables(self, writer):
        pkg = _pkg()
        ch = LinPhysicalChannel(pkg, "LinCh")
        parent = _parent()
        writer.writeLinPhysicalChannel(parent, ch)
        lpc = parent.find("LIN-PHYSICAL-CHANNEL")
        assert lpc is not None

    def test_write_lin_physical_channel_schedule_tables_warns(self):
        w = _warning_writer()
        pkg = _pkg()
        ch = LinPhysicalChannel(pkg, "LinCh")
        ch.scheduleTables.append("not_a_table")
        parent = _parent()
        w.writeLinPhysicalChannelScheduleTables(parent, ch)
        assert len(parent) == 1

    def test_write_lin_physical_channel_with_table(self, writer):
        pkg = _pkg()
        ch = LinPhysicalChannel(pkg, "LinCh")
        ch.createLinScheduleTable("Table")
        parent = _parent()
        writer.writeLinPhysicalChannel(parent, ch)
        lpc = parent.find("LIN-PHYSICAL-CHANNEL")
        tables = lpc.find("SCHEDULE-TABLES")
        assert tables is not None
        assert len(tables.findall("LIN-SCHEDULE-TABLE")) == 1


class TestWriteNetworkEndPoint:
    def test_set_ipv6_configuration_none(self, writer):
        parent = _parent()
        writer.setIpv6Configuration(parent, None)
        assert len(parent) == 0

    def test_set_ipv6_configuration_full(self, writer):
        cfg = Ipv6Configuration()
        cfg.setAssignmentPriority(_pos_int("1"))
        cfg.setDefaultRouter(_literal("router"))
        cfg.setEnableAnycast(_boolean("true"))
        cfg.setHopCount(_pos_int("64"))
        cfg.setIpAddressPrefixLength(_pos_int("48"))
        cfg.setIpv6Address(_literal("::1"))
        cfg.setIpv6AddressSource(_literal("MANUAL"))
        parent = _parent()
        writer.setIpv6Configuration(parent, cfg)
        tag = parent.find("IPV-6-CONFIGURATION")
        assert tag is not None
        assert tag.find("ASSIGNMENT-PRIORITY").text == "1"
        assert tag.find("DEFAULT-ROUTER").text == "router"
        assert tag.find("ENABLE-ANYCAST").text == "true"
        assert tag.find("HOP-COUNT").text == "64"
        assert tag.find("IP-ADDRESS-PREFIX-LENGTH").text == "48"
        assert tag.find("IPV-6-ADDRESS").text == "::1"
        assert tag.find("IPV-6-ADDRESS-SOURCE").text == "MANUAL"

    def test_write_network_end_point_addresses_empty(self, writer):
        parent = _parent()
        writer.writeNetworkEndPointNetworkEndPointAddresses(parent, [])
        assert len(parent) == 0

    def test_write_network_end_point_addresses_with_ipv6(self, writer):
        cfg = Ipv6Configuration()
        cfg.setIpv6Address(_literal("::2"))
        parent = _parent()
        writer.writeNetworkEndPointNetworkEndPointAddresses(
            parent, [cfg]
        )
        addrs = parent.find("NETWORK-ENDPOINT-ADDRESSES")
        assert addrs is not None
        assert addrs.find("IPV-6-CONFIGURATION") is not None

    def test_write_network_end_point_addresses_warns(self):
        w = _warning_writer()
        parent = _parent()
        w.writeNetworkEndPointNetworkEndPointAddresses(
            parent, ["not_an_address"]
        )
        assert len(parent) == 1

    def test_set_do_ip_entity_none(self, writer):
        parent = _parent()
        writer.setDoIpEntity(parent, "DO-IP-ENTITY", None)
        assert len(parent) == 0

    def test_set_do_ip_entity_full(self, writer):
        entity = DoIpEntity()
        entity.setDoIpEntityRole(_literal("GATEWAY"))
        parent = _parent()
        writer.setDoIpEntity(parent, "DO-IP-ENTITY", entity)
        tag = parent.find("DO-IP-ENTITY")
        assert tag is not None
        assert tag.find("DO-IP-ENTITY-ROLE").text == "GATEWAY"

    def test_set_infrastructure_services_none(self, writer):
        parent = _parent()
        writer.setInfrastructureServices(
            parent, "INFRASTRUCTURE-SERVICES", None
        )
        assert len(parent) == 0

    def test_set_infrastructure_services_full(self, writer):
        svc = InfrastructureServices()
        entity = DoIpEntity()
        entity.setDoIpEntityRole(_literal("NODE"))
        svc.setDoIpEntity(entity)
        parent = _parent()
        writer.setInfrastructureServices(
            parent, "INFRASTRUCTURE-SERVICES", svc
        )
        tag = parent.find("INFRASTRUCTURE-SERVICES")
        assert tag is not None
        assert tag.find("DO-IP-ENTITY") is not None

    def test_write_network_end_point(self, writer):
        pkg = _pkg()
        ep = NetworkEndpoint(pkg, "Ep")
        svc = InfrastructureServices()
        ep.setInfrastructureServices(svc)
        ep.addNetworkEndpointAddress(Ipv6Configuration())
        ep.setPriority(_pos_int("5"))
        parent = _parent()
        writer.writeNetworkEndPoint(parent, ep)
        ne = parent.find("NETWORK-ENDPOINT")
        assert ne is not None
        assert ne.find("INFRASTRUCTURE-SERVICES") is not None
        assert ne.find("NETWORK-ENDPOINT-ADDRESSES") is not None
        assert ne.find("PRIORITY").text == "5"

    def test_write_ethernet_pc_network_end_points_empty(self, writer):
        parent = _parent()
        writer.writeEthernetPhysicalChannelNetworkEndPoints(parent, [])
        assert len(parent) == 0

    def test_write_ethernet_pc_network_end_points(self, writer):
        pkg = _pkg()
        ep = NetworkEndpoint(pkg, "Ep")
        parent = _parent()
        writer.writeEthernetPhysicalChannelNetworkEndPoints(parent, [ep])
        tag = parent.find("NETWORK-ENDPOINTS")
        assert tag is not None
        assert tag.find("NETWORK-ENDPOINT") is not None


class TestWriteSocketConnection:
    def test_set_socket_connection_ipdu_identifier_none(self, writer):
        parent = _parent()
        writer.setSocketConnectionIpduIdentifier(parent, None)
        assert len(parent) == 0

    def test_set_socket_connection_ipdu_identifier_full(self, writer):
        ident = SocketConnectionIpduIdentifier()
        ident.setHeaderId(_pos_int("100"))
        ident.setPduCollectionSemantics(_literal("LAST"))
        ident.setPduCollectionTrigger(_literal("TRIGGER"))
        ident.setPduRef(_ref("PDU", "/pdu"))
        ident.setPduTriggeringRef(_ref("PDU-TRIGGERING", "/pt"))
        parent = _parent()
        writer.setSocketConnectionIpduIdentifier(parent, ident)
        tag = parent.find("SOCKET-CONNECTION-IPDU-IDENTIFIER")
        assert tag is not None
        assert tag.find("HEADER-ID").text == "100"
        assert tag.find("PDU-COLLECTION-SEMANTICS").text == "LAST"
        assert tag.find("PDU-COLLECTION-TRIGGER").text == "TRIGGER"
        assert tag.find("PDU-REF") is not None
        assert tag.find("PDU-TRIGGERING-REF") is not None

    def test_set_socket_connection_pdus_empty(self, writer):
        parent = _parent()
        writer.setSocketConnectionPdus(parent, "PDUS", [])
        assert len(parent) == 0

    def test_set_socket_connection_pdus_warns(self):
        w = _warning_writer()
        parent = _parent()
        w.setSocketConnectionPdus(parent, "PDUS", ["not_a_pdu"])
        assert len(parent) == 1

    def test_set_socket_connection_pdus(self, writer):
        ident = SocketConnectionIpduIdentifier()
        ident.setHeaderId(_pos_int("200"))
        parent = _parent()
        writer.setSocketConnectionPdus(parent, "PDUS", [ident])
        tag = parent.find("PDUS")
        assert tag is not None
        assert tag.find("SOCKET-CONNECTION-IPDU-IDENTIFIER") is not None

    def test_set_socket_connection_none(self, writer):
        parent = _parent()
        writer.setSocketConnection(parent, None)
        assert len(parent) == 0

    def test_set_socket_connection_full(self, writer):
        conn = SocketConnection()
        conn.setClientIpAddrFromConnectionRequest(_boolean("true"))
        conn.setClientPortFromConnectionRequest(_boolean("false"))
        conn.setClientPortRef(_ref("PORT", "/port"))
        ident = SocketConnectionIpduIdentifier()
        ident.setHeaderId(_pos_int("300"))
        conn.addPdu(ident)
        conn.setPduCollectionMaxBufferSize(_pos_int("1024"))
        conn.setPduCollectionTimeout(_time("0.5"))
        conn.setRuntimeIpAddressConfiguration(_literal("DYNAMIC"))
        conn.setRuntimePortConfiguration(_literal("DYNAMIC"))
        conn.setShortLabel(_literal("lbl"))
        parent = _parent()
        writer.setSocketConnection(parent, conn)
        sc = parent.find("SOCKET-CONNECTION")
        assert sc is not None
        assert (
            sc.find(
                "CLIENT-IP-ADDR-FROM-CONNECTION-REQUEST"
            ).text == "true"
        )
        assert (
            sc.find("CLIENT-PORT-FROM-CONNECTION-REQUEST").text
            == "false"
        )
        assert sc.find("CLIENT-PORT-REF") is not None
        assert sc.find("PDUS") is not None
        assert sc.find("PDU-COLLECTION-MAX-BUFFER-SIZE").text == "1024"
        assert sc.find("PDU-COLLECTION-TIMEOUT").text == "0.5"
        assert (
            sc.find("RUNTIME-IP-ADDRESS-CONFIGURATION").text
            == "DYNAMIC"
        )
        assert (
            sc.find("RUNTIME-PORT-CONFIGURATION").text == "DYNAMIC"
        )
        assert sc.find("SHORT-LABEL").text == "lbl"


class TestWriteSocketConnectionBundle:
    def test_write_bundle_connections_empty(self, writer):
        pkg = _pkg()
        bundle = SocketConnectionBundle(pkg, "Bundle")
        parent = _parent()
        writer.writeSocketConnectionBundleConnections(parent, bundle)
        assert len(parent) == 0

    def test_write_bundle_connections_warns(self):
        w = _warning_writer()
        pkg = _pkg()
        bundle = SocketConnectionBundle(pkg, "Bundle")
        bundle.addBundledConnection("not_a_conn")
        parent = _parent()
        w.writeSocketConnectionBundleConnections(parent, bundle)
        assert len(parent) == 1

    def test_write_bundle_connections(self, writer):
        pkg = _pkg()
        bundle = SocketConnectionBundle(pkg, "Bundle")
        conn = SocketConnection()
        conn.setShortLabel(_literal("c1"))
        bundle.addBundledConnection(conn)
        parent = _parent()
        writer.writeSocketConnectionBundleConnections(parent, bundle)
        bc = parent.find("BUNDLED-CONNECTIONS")
        assert bc is not None
        assert bc.find("SOCKET-CONNECTION") is not None

    def test_write_socket_connection_bundle_none(self, writer):
        parent = _parent()
        writer.writeSocketConnectionBundle(parent, None)
        assert len(parent) == 0

    def test_write_socket_connection_bundle_full(self, writer):
        pkg = _pkg()
        bundle = SocketConnectionBundle(pkg, "Bundle")
        conn = SocketConnection()
        conn.setShortLabel(_literal("c2"))
        bundle.addBundledConnection(conn)
        bundle.setServerPortRef(_ref("PORT", "/sport"))
        parent = _parent()
        writer.writeSocketConnectionBundle(parent, bundle)
        scb = parent.find("SOCKET-CONNECTION-BUNDLE")
        assert scb is not None
        assert scb.find("BUNDLED-CONNECTIONS") is not None
        assert scb.find("SERVER-PORT-REF") is not None

    def test_write_soad_config_connection_bundles_empty(self, writer):
        cfg = SoAdConfig()
        parent = _parent()
        writer.writeSoAdConfigConnectionBundles(parent, cfg)
        assert len(parent) == 0

    def test_write_soad_config_connection_bundles_warns(self):
        w = _warning_writer()
        cfg = SoAdConfig()
        cfg.connectionBundles.append("not_a_bundle")
        parent = _parent()
        w.writeSoAdConfigConnectionBundles(parent, cfg)
        assert len(parent) == 1

    def test_write_soad_config_connection_bundles(self, writer):
        pkg = _pkg()
        cfg = SoAdConfig()
        bundle = SocketConnectionBundle(pkg, "Bundle")
        cfg.connectionBundles.append(bundle)
        parent = _parent()
        writer.writeSoAdConfigConnectionBundles(parent, cfg)
        cb = parent.find("CONNECTION-BUNDLES")
        assert cb is not None
        assert cb.find("SOCKET-CONNECTION-BUNDLE") is not None


class TestWriteTransportProtocols:
    def test_set_tp_port_none(self, writer):
        parent = _parent()
        writer.setTpPort(parent, "UDP-TP-PORT", None)
        assert len(parent) == 0

    def test_set_tp_port_full(self, writer):
        port = TpPort()
        port.setDynamicallyAssigned(_boolean("true"))
        port.setPortNumber(_pos_int("8080"))
        parent = _parent()
        writer.setTpPort(parent, "UDP-TP-PORT", port)
        tag = parent.find("UDP-TP-PORT")
        assert tag is not None
        assert tag.find("DYNAMICALLY-ASSIGNED").text == "true"
        assert tag.find("PORT-NUMBER").text == "8080"

    def test_write_udp_tp(self, writer):
        tp = UdpTp()
        port = TpPort()
        port.setPortNumber(_pos_int("1234"))
        tp.setUdpTpPort(port)
        parent = _parent()
        writer.writeUdpTp(parent, tp)
        utp = parent.find("UDP-TP")
        assert utp is not None
        assert utp.find("UDP-TP-PORT") is not None

    def test_write_tcp_tp(self, writer):
        tp = TcpTp()
        tp.setKeepAliveInterval(_time("1.0"))
        tp.setKeepAliveProbesMax(_pos_int("3"))
        tp.setKeepAliveTime(_time("2.0"))
        tp.setKeepAlives(_boolean("true"))
        tp.setNaglesAlgorithm(_boolean("false"))
        port = TpPort()
        port.setPortNumber(_pos_int("5678"))
        tp.setTcpTpPort(port)
        parent = _parent()
        writer.writeTcpTp(parent, tp)
        ttp = parent.find("TCP-TP")
        assert ttp is not None
        assert ttp.find("KEEP-ALIVE-INTERVAL").text == "1.0"
        assert ttp.find("KEEP-ALIVE-PROBES-MAX").text == "3"
        assert ttp.find("KEEP-ALIVE-TIME").text == "2.0"
        assert ttp.find("KEEP-ALIVES").text == "true"
        assert ttp.find("NAGLES-ALGORITHM").text == "false"
        assert ttp.find("TCP-TP-PORT") is not None

    def test_write_generic_tp(self, writer):
        tp = GenericTp()
        tp.setTpAddress(_literal("addr"))
        tp.setTpTechnology(_literal("tech"))
        parent = _parent()
        writer.writeGenericTp(parent, tp)
        gtp = parent.find("GENERIC-TP")
        assert gtp is not None
        assert gtp.find("TP-ADDRESS").text == "addr"
        assert gtp.find("TP-TECHNOLOGY").text == "tech"

    def test_write_tp_configuration_none(self, writer):
        parent = _parent()
        result = writer.writeTransportProtocolConfiguration(
            parent, None
        )
        assert result is None
        assert len(parent) == 0

    def test_write_tp_configuration_udp(self, writer):
        tp = UdpTp()
        parent = _parent()
        writer.writeTransportProtocolConfiguration(parent, tp)
        cfg = parent.find("TP-CONFIGURATION")
        assert cfg is not None
        assert cfg.find("UDP-TP") is not None

    def test_write_tp_configuration_tcp(self, writer):
        tp = TcpTp()
        parent = _parent()
        writer.writeTransportProtocolConfiguration(parent, tp)
        cfg = parent.find("TP-CONFIGURATION")
        assert cfg is not None
        assert cfg.find("TCP-TP") is not None

    def test_write_tp_configuration_generic(self, writer):
        tp = GenericTp()
        parent = _parent()
        writer.writeTransportProtocolConfiguration(parent, tp)
        cfg = parent.find("TP-CONFIGURATION")
        assert cfg is not None
        assert cfg.find("GENERIC-TP") is not None

    def test_write_tp_configuration_warns(self):
        w = _warning_writer()
        parent = _parent()
        w.writeTransportProtocolConfiguration(parent, "not_a_tp")
        assert len(parent) == 1


class TestWriteConsumedEventGroup:
    def test_write_ceg_routing_group_refs_empty(self, writer):
        pkg = _pkg()
        group = ConsumedEventGroup(pkg, "Group")
        parent = _parent()
        writer.writeConsumedEventGroupRoutingGroupRefs(parent, group)
        assert len(parent) == 0

    def test_write_ceg_routing_group_refs(self, writer):
        pkg = _pkg()
        group = ConsumedEventGroup(pkg, "Group")
        group.addRoutingGroupRef(_ref("ROUTING-GROUP", "/rg"))
        parent = _parent()
        writer.writeConsumedEventGroupRoutingGroupRefs(parent, group)
        refs = parent.find("ROUTING-GROUP-REFS")
        assert refs is not None
        assert len(refs.findall("ROUTING-GROUP-REF")) == 1

    def test_set_request_response_delay_none(self, writer):
        parent = _parent()
        writer.setRequestResponseDelay(parent, "RRD", None)
        assert len(parent) == 0

    def test_set_request_response_delay_full(self, writer):
        rrd = RequestResponseDelay()
        rrd.setMaxValue(_time("1.0"))
        rrd.setMinValue(_time("0.1"))
        parent = _parent()
        writer.setRequestResponseDelay(
            parent, "REQUEST-RESPONSE-DELAY", rrd
        )
        tag = parent.find("REQUEST-RESPONSE-DELAY")
        assert tag is not None
        assert tag.find("MAX-VALUE").text == "1.0"
        assert tag.find("MIN-VALUE").text == "0.1"

    def test_set_initial_sd_delay_config_none(self, writer):
        parent = _parent()
        writer.setInitialSdDelayConfig(parent, "INIT", None)
        assert len(parent) == 0

    def test_set_initial_sd_delay_config_full(self, writer):
        cfg = InitialSdDelayConfig()
        cfg.setInitialDelayMaxValue(_time("1.5"))
        cfg.setInitialDelayMinValue(_time("0.5"))
        cfg.setInitialRepetitionsBaseDelay(_time("0.2"))
        cfg.setInitialRepetitionsMax(_pos_int("3"))
        parent = _parent()
        writer.setInitialSdDelayConfig(
            parent, "INITIAL-FIND-BEHAVIOR", cfg
        )
        tag = parent.find("INITIAL-FIND-BEHAVIOR")
        assert tag is not None
        assert tag.find("INITIAL-DELAY-MAX-VALUE").text == "1.5"
        assert tag.find("INITIAL-DELAY-MIN-VALUE").text == "0.5"
        assert (
            tag.find("INITIAL-REPETITIONS-BASE-DELAY").text == "0.2"
        )
        assert tag.find("INITIAL-REPETITIONS-MAX").text == "3"

    def test_set_sd_client_config_none(self, writer):
        parent = _parent()
        writer.setSdClientConfig(parent, "SD-CLIENT-CONFIG", None)
        assert len(parent) == 0

    def test_set_sd_client_config_full(self, writer):
        cfg = SdClientConfig()
        cfg.setClientServiceMajorVersion(_pos_int("1"))
        cfg.setClientServiceMinorVersion(_pos_int("0"))
        init = InitialSdDelayConfig()
        init.setInitialRepetitionsMax(_pos_int("2"))
        cfg.setInitialFindBehavior(init)
        rrd = RequestResponseDelay()
        rrd.setMaxValue(_time("0.5"))
        cfg.setRequestResponseDelay(rrd)
        cfg.setTtl(_pos_int("100"))
        parent = _parent()
        writer.setSdClientConfig(parent, "SD-CLIENT-CONFIG", cfg)
        tag = parent.find("SD-CLIENT-CONFIG")
        assert tag is not None
        assert tag.find("CLIENT-SERVICE-MAJOR-VERSION").text == "1"
        assert tag.find("CLIENT-SERVICE-MINOR-VERSION").text == "0"
        assert tag.find("INITIAL-FIND-BEHAVIOR") is not None
        assert tag.find("REQUEST-RESPONSE-DELAY") is not None
        assert tag.find("TTL").text == "100"

    def test_write_consumed_event_group_none(self, writer):
        parent = _parent()
        writer.writeConsumedEventGroup(parent, None)
        assert len(parent) == 0

    def test_write_consumed_event_group_full(self, writer):
        pkg = _pkg()
        group = ConsumedEventGroup(pkg, "Group")
        group.setApplicationEndpointRef(
            _ref("APPLICATION-ENDPOINT", "/ae")
        )
        group.setEventGroupIdentifier(_pos_int("7"))
        group.addRoutingGroupRef(_ref("ROUTING-GROUP", "/rg"))
        cfg = SdClientConfig()
        cfg.setTtl(_pos_int("50"))
        group.setSdClientConfig(cfg)
        parent = _parent()
        writer.writeConsumedEventGroup(parent, group)
        ceg = parent.find("CONSUMED-EVENT-GROUP")
        assert ceg is not None
        assert ceg.find("APPLICATION-ENDPOINT-REF") is not None
        assert ceg.find("EVENT-GROUP-IDENTIFIER").text == "7"
        assert ceg.find("ROUTING-GROUP-REFS") is not None
        assert ceg.find("SD-CLIENT-CONFIG") is not None


class TestWriteConsumedServiceInstance:
    def test_write_csi_consumed_event_groups_empty(self, writer):
        pkg = _pkg()
        inst = ConsumedServiceInstance(pkg, "Csi")
        parent = _parent()
        writer.writeConsumedServiceInstanceConsumedEventGroups(
            parent, inst
        )
        assert len(parent) == 0

    def test_write_csi_consumed_event_groups_warns(self):
        w = _warning_writer()
        pkg = _pkg()
        inst = ConsumedServiceInstance(pkg, "Csi")
        inst.consumedEventGroups.append("not_a_group")
        parent = _parent()
        w.writeConsumedServiceInstanceConsumedEventGroups(parent, inst)
        assert len(parent) == 1

    def test_write_csi_consumed_event_groups(self, writer):
        pkg = _pkg()
        inst = ConsumedServiceInstance(pkg, "Csi")
        inst.createConsumedEventGroup("Group")
        parent = _parent()
        writer.writeConsumedServiceInstanceConsumedEventGroups(
            parent, inst
        )
        groups = parent.find("CONSUMED-EVENT-GROUPS")
        assert groups is not None
        assert groups.find("CONSUMED-EVENT-GROUP") is not None

    def test_write_consumed_service_instance_none(self, writer):
        parent = _parent()
        writer.writeConsumedServiceInstance(parent, None)
        assert len(parent) == 0

    def test_write_consumed_service_instance_full(self, writer):
        pkg = _pkg()
        inst = ConsumedServiceInstance(pkg, "Csi")
        inst.createConsumedEventGroup("Group")
        inst.setProvidedServiceInstanceRef(
            _ref("PROVIDED-SERVICE-INSTANCE", "/psi")
        )
        cfg = SdClientConfig()
        cfg.setTtl(_pos_int("30"))
        inst.setSdClientConfig(cfg)
        parent = _parent()
        writer.writeConsumedServiceInstance(parent, inst)
        csi = parent.find("CONSUMED-SERVICE-INSTANCE")
        assert csi is not None
        assert csi.find("CONSUMED-EVENT-GROUPS") is not None
        assert csi.find("PROVIDED-SERVICE-INSTANCE-REF") is not None
        assert csi.find("SD-CLIENT-CONFIG") is not None


class TestWriteSocketAddressAppEndpointConsumedServiceInstances:
    def test_write_empty(self, writer):
        pkg = _pkg()
        ep = ApplicationEndpoint(pkg, "Ep")
        parent = _parent()
        writer.writeSocketAddressApplicationEndpointConsumedServiceInstances(  # noqa: E501
            parent, ep
        )
        assert len(parent) == 0

    def test_write_warns(self):
        w = _warning_writer()
        pkg = _pkg()
        ep = ApplicationEndpoint(pkg, "Ep")
        ep.consumedServiceInstances.append("not_a_csi")
        parent = _parent()
        w.writeSocketAddressApplicationEndpointConsumedServiceInstances(  # noqa: E501
            parent, ep
        )
        assert len(parent) == 1

    def test_write_with_instance(self, writer):
        pkg = _pkg()
        ep = ApplicationEndpoint(pkg, "Ep")
        ep.createConsumedServiceInstance("Csi")
        parent = _parent()
        writer.writeSocketAddressApplicationEndpointConsumedServiceInstances(  # noqa: E501
            parent, ep
        )
        tag = parent.find("CONSUMED-SERVICE-INSTANCES")
        assert tag is not None
        assert tag.find("CONSUMED-SERVICE-INSTANCE") is not None


class TestWriteEventHandler:
    def test_set_sd_server_config_none(self, writer):
        parent = _parent()
        writer.setSdServerConfig(parent, "SD-SERVER-CONFIG", None)
        assert len(parent) == 0

    def test_set_sd_server_config_full(self, writer):
        cfg = SdServerConfig()
        init = InitialSdDelayConfig()
        init.setInitialRepetitionsMax(_pos_int("2"))
        cfg.setInitialOfferBehavior(init)
        cfg.setOfferCyclicDelay(_time("0.5"))
        rrd = RequestResponseDelay()
        rrd.setMaxValue(_time("1.0"))
        cfg.setRequestResponseDelay(rrd)
        cfg.setServerServiceMajorVersion(_pos_int("2"))
        cfg.setServerServiceMinorVersion(_pos_int("1"))
        cfg.setTtl(_pos_int("200"))
        parent = _parent()
        writer.setSdServerConfig(parent, "SD-SERVER-CONFIG", cfg)
        tag = parent.find("SD-SERVER-CONFIG")
        assert tag is not None
        assert tag.find("INITIAL-OFFER-BEHAVIOR") is not None
        assert tag.find("OFFER-CYCLIC-DELAY").text == "0.5"
        assert tag.find("REQUEST-RESPONSE-DELAY") is not None
        assert tag.find("SERVER-SERVICE-MAJOR-VERSION").text == "2"
        assert tag.find("SERVER-SERVICE-MINOR-VERSION").text == "1"
        assert tag.find("TTL").text == "200"

    def test_write_event_handler_none(self, writer):
        parent = _parent()
        writer.writeEventHandler(parent, None)
        assert len(parent) == 0

    def test_write_event_handler_full(self, writer):
        pkg = _pkg()
        handler = EventHandler(pkg, "Handler")
        handler.setApplicationEndpointRef(
            _ref("APPLICATION-ENDPOINT", "/ae")
        )
        handler.addConsumedEventGroupRef(
            _ref("CONSUMED-EVENT-GROUP", "/ceg")
        )
        handler.setMulticastThreshold(_pos_int("5"))
        handler.addRoutingGroupRef(_ref("ROUTING-GROUP", "/rg"))
        cfg = SdServerConfig()
        cfg.setTtl(_pos_int("100"))
        handler.setSdServerConfig(cfg)
        parent = _parent()
        writer.writeEventHandler(parent, handler)
        eh = parent.find("EVENT-HANDLER")
        assert eh is not None
        assert eh.find("APPLICATION-ENDPOINT-REF") is not None
        refs = eh.find("CONSUMED-EVENT-GROUP-REFS")
        assert refs is not None
        assert (
            len(refs.findall("CONSUMED-EVENT-GROUP-REF")) == 1
        )
        assert eh.find("MULTICAST-THRESHOLD").text == "5"
        rrefs = eh.find("ROUTING-GROUP-REFS")
        assert rrefs is not None
        assert len(rrefs.findall("ROUTING-GROUP-REF")) == 1
        assert eh.find("SD-SERVER-CONFIG") is not None

    def test_write_psi_event_handlers_empty(self, writer):
        pkg = _pkg()
        inst = ProvidedServiceInstance(pkg, "Psi")
        parent = _parent()
        writer.writeProvidedServiceInstanceEventHandlers(parent, inst)
        assert len(parent) == 0

    def test_write_psi_event_handlers_warns(self):
        w = _warning_writer()
        pkg = _pkg()
        inst = ProvidedServiceInstance(pkg, "Psi")
        inst.eventHandlers.append("not_a_handler")
        parent = _parent()
        w.writeProvidedServiceInstanceEventHandlers(parent, inst)
        assert len(parent) == 1

    def test_write_psi_event_handlers(self, writer):
        pkg = _pkg()
        inst = ProvidedServiceInstance(pkg, "Psi")
        inst.createEventHandler("Handler")
        parent = _parent()
        writer.writeProvidedServiceInstanceEventHandlers(parent, inst)
        ehs = parent.find("EVENT-HANDLERS")
        assert ehs is not None
        assert ehs.find("EVENT-HANDLER") is not None

    def test_write_provided_service_instance_none(self, writer):
        parent = _parent()
        writer.writeProvidedServiceInstance(parent, None)
        assert len(parent) == 0

    def test_write_provided_service_instance_full(self, writer):
        pkg = _pkg()
        inst = ProvidedServiceInstance(pkg, "Psi")
        inst.createEventHandler("Handler")
        inst.setInstanceIdentifier(_pos_int("9"))
        cfg = SdServerConfig()
        cfg.setTtl(_pos_int("80"))
        inst.setSdServerConfig(cfg)
        inst.setServiceIdentifier(_pos_int("11"))
        parent = _parent()
        writer.writeProvidedServiceInstance(parent, inst)
        psi = parent.find("PROVIDED-SERVICE-INSTANCE")
        assert psi is not None
        assert psi.find("EVENT-HANDLERS") is not None
        assert psi.find("INSTANCE-IDENTIFIER").text == "9"
        assert psi.find("SD-SERVER-CONFIG") is not None
        assert psi.find("SERVICE-IDENTIFIER").text == "11"

    def test_write_sa_app_endpoint_psi_empty(self, writer):
        pkg = _pkg()
        ep = ApplicationEndpoint(pkg, "Ep")
        parent = _parent()
        writer.writeSocketAddressApplicationEndpointProvidedServiceInstance(  # noqa: E501
            parent, ep
        )
        assert len(parent) == 0

    def test_write_sa_app_endpoint_psi_warns(self):
        w = _warning_writer()
        pkg = _pkg()
        ep = ApplicationEndpoint(pkg, "Ep")
        ep.providedServiceInstances.append("not_a_psi")
        parent = _parent()
        w.writeSocketAddressApplicationEndpointProvidedServiceInstance(  # noqa: E501
            parent, ep
        )
        assert len(parent) == 1

    def test_write_sa_app_endpoint_psi(self, writer):
        pkg = _pkg()
        ep = ApplicationEndpoint(pkg, "Ep")
        ep.createProvidedServiceInstance("Psi")
        parent = _parent()
        writer.writeSocketAddressApplicationEndpointProvidedServiceInstance(  # noqa: E501
            parent, ep
        )
        tag = parent.find("PROVIDED-SERVICE-INSTANCES")
        assert tag is not None
        assert tag.find("PROVIDED-SERVICE-INSTANCE") is not None


class TestWriteSocketAddress:
    def test_write_sa_app_endpoint_no_endpoint(self, writer):
        pkg = _pkg()
        addr = SocketAddress(pkg, "Addr")
        parent = _parent()
        writer.writeSocketAddressApplicationEndpoint(parent, addr)
        assert len(parent) == 0

    def test_write_sa_app_endpoint_full(self, writer):
        pkg = _pkg()
        addr = SocketAddress(pkg, "Addr")
        ep = addr.createApplicationEndpoint("Ep")
        ep.createConsumedServiceInstance("Csi")
        ep.setNetworkEndpointRef(_ref("NETWORK-ENDPOINT", "/ne"))
        ep.setPriority(_pos_int("3"))
        ep.createProvidedServiceInstance("Psi")
        tp = UdpTp()
        ep.setTpConfiguration(tp)
        parent = _parent()
        writer.writeSocketAddressApplicationEndpoint(parent, addr)
        ae = parent.find("APPLICATION-ENDPOINT")
        assert ae is not None
        assert ae.find("CONSUMED-SERVICE-INSTANCES") is not None
        assert ae.find("NETWORK-ENDPOINT-REF") is not None
        assert ae.find("PRIORITY").text == "3"
        assert ae.find("PROVIDED-SERVICE-INSTANCES") is not None
        assert ae.find("TP-CONFIGURATION") is not None

    def test_write_sa_multicast_connector_refs_empty(self, writer):
        pkg = _pkg()
        addr = SocketAddress(pkg, "Addr")
        parent = _parent()
        writer.writeSocketAddressMulticastConnectorRefs(parent, addr)
        assert len(parent) == 0

    def test_write_sa_multicast_connector_refs(self, writer):
        pkg = _pkg()
        addr = SocketAddress(pkg, "Addr")
        addr.addMulticastConnectorRef(_ref("MULTICAST-CONNECTOR", "/mc"))
        parent = _parent()
        writer.writeSocketAddressMulticastConnectorRefs(parent, addr)
        refs = parent.find("MULTICAST-CONNECTOR-REFS")
        assert refs is not None
        assert len(refs.findall("MULTICAST-CONNECTOR-REF")) == 1

    def test_write_socket_address(self, writer):
        pkg = _pkg()
        addr = SocketAddress(pkg, "Addr")
        addr.createApplicationEndpoint("Ep")
        addr.addMulticastConnectorRef(_ref("MULTICAST-CONNECTOR", "/mc"))
        addr.setConnectorRef(_ref("CONNECTOR", "/conn"))
        addr.setPortAddress(_pos_int("4096"))
        parent = _parent()
        writer.writeSocketAddress(parent, addr)
        sa = parent.find("SOCKET-ADDRESS")
        assert sa is not None
        assert sa.find("APPLICATION-ENDPOINT") is not None
        assert sa.find("MULTICAST-CONNECTOR-REFS") is not None
        assert sa.find("CONNECTOR-REF") is not None
        assert sa.find("PORT-ADDRESS").text == "4096"

    def test_write_soad_config_socket_addresses_empty(self, writer):
        cfg = SoAdConfig()
        parent = _parent()
        writer.writeSoAdConfigSocketAddresses(parent, cfg)
        assert len(parent) == 0

    def test_write_soad_config_socket_addresses_warns(self):
        w = _warning_writer()
        cfg = SoAdConfig()
        cfg.socketAddresses.append("not_an_addr")
        parent = _parent()
        w.writeSoAdConfigSocketAddresses(parent, cfg)
        assert len(parent) == 1

    def test_write_soad_config_socket_addresses(self, writer):
        pkg = _pkg()
        cfg = SoAdConfig()
        addr = SocketAddress(pkg, "Addr")
        cfg.socketAddresses.append(addr)
        parent = _parent()
        writer.writeSoAdConfigSocketAddresses(parent, cfg)
        tag = parent.find("SOCKET-ADDRESSS")
        assert tag is not None
        assert tag.find("SOCKET-ADDRESS") is not None

    def test_write_soad_config_none(self, writer):
        parent = _parent()
        writer.writeSoAdConfig(parent, "SO-AD-CONFIG", None)
        assert len(parent) == 0

    def test_write_soad_config_full(self, writer):
        pkg = _pkg()
        cfg = SoAdConfig()
        bundle = SocketConnectionBundle(pkg, "Bundle")
        cfg.connectionBundles.append(bundle)
        addr = SocketAddress(pkg, "Addr")
        cfg.socketAddresses.append(addr)
        parent = _parent()
        writer.writeSoAdConfig(parent, "SO-AD-CONFIG", cfg)
        tag = parent.find("SO-AD-CONFIG")
        assert tag is not None
        assert tag.find("CONNECTION-BUNDLES") is not None
        assert tag.find("SOCKET-ADDRESSS") is not None


class TestWriteEthernetPhysicalChannel:
    def test_write_ethernet_pc_vlan_none(self, writer):
        pkg = _pkg()
        ch = EthernetPhysicalChannel(pkg, "EthCh")
        parent = _parent()
        writer.writeEthernetPhysicalChannelVlan(parent, ch)
        assert len(parent) == 0

    def test_write_ethernet_pc_vlan(self, writer):
        pkg = _pkg()
        ch = EthernetPhysicalChannel(pkg, "EthCh")
        ch.createVlanConfig("Vlan")
        parent = _parent()
        writer.writeEthernetPhysicalChannelVlan(parent, ch)
        vlan = parent.find("VLAN")
        assert vlan is not None

    def test_write_ethernet_physical_channel(self, writer):
        pkg = _pkg()
        ch = EthernetPhysicalChannel(pkg, "EthCh")
        ch.createNetworkEndPoint("Ep")
        cfg = SoAdConfig()
        ch.setSoAdConfig(cfg)
        ch.createVlanConfig("Vlan")
        parent = _parent()
        writer.writeEthernetPhysicalChannel(parent, ch)
        epc = parent.find("ETHERNET-PHYSICAL-CHANNEL")
        assert epc is not None
        assert epc.find("NETWORK-ENDPOINTS") is not None
        assert epc.find("SO-AD-CONFIG") is not None
        assert epc.find("VLAN") is not None


class TestWriteFlexrayPhysicalChannel:
    def test_write_flexray_physical_channel(self, writer):
        pkg = _pkg()
        ch = FlexrayPhysicalChannel(pkg, "FlCh")
        ch.setChannelName(_literal("channelA"))
        parent = _parent()
        writer.writeFlexrayPhysicalChannel(parent, ch)
        fpc = parent.find("FLEXRAY-PHYSICAL-CHANNEL")
        assert fpc is not None
        assert fpc.find("CHANNEL-NAME").text == "channelA"


class TestWriteCommunicationCluster:
    def test_write_comm_cluster_physical_channels_empty(self, writer):
        pkg = _pkg()
        cluster = CanCluster(pkg, "Cluster")
        parent = _parent()
        writer.writeCommunicationClusterPhysicalChannels(parent, cluster)
        assert len(parent) == 0

    def test_write_comm_cluster_physical_channels_warns(self):
        w = _warning_writer()
        pkg = _pkg()
        cluster = CanCluster(pkg, "Cluster")
        cluster.addElement(MagicMock())
        parent = _parent()
        w.writeCommunicationClusterPhysicalChannels(parent, cluster)
        assert len(parent) == 0

    def test_write_comm_cluster_physical_channels_warns_branch(
        self
    ):
        w = _warning_writer()
        cluster = MagicMock()
        cluster.getPhysicalChannels.return_value = [
            "not_a_channel"
        ]
        parent = _parent()
        w.writeCommunicationClusterPhysicalChannels(
            parent, cluster
        )
        assert parent.find("PHYSICAL-CHANNELS") is not None

    def test_write_comm_cluster_physical_channels_all_types(self, writer):
        pkg = _pkg()
        cluster = CanCluster(pkg, "Cluster")
        cluster.createCanPhysicalChannel("CanCh")
        cluster.createLinPhysicalChannel("LinCh")
        cluster.createEthernetPhysicalChannel("EthCh")
        cluster.createFlexrayPhysicalChannel("FlCh")
        parent = _parent()
        writer.writeCommunicationClusterPhysicalChannels(parent, cluster)
        channels = parent.find("PHYSICAL-CHANNELS")
        assert channels is not None
        assert len(channels.findall("CAN-PHYSICAL-CHANNEL")) == 1
        assert len(channels.findall("LIN-PHYSICAL-CHANNEL")) == 1
        assert (
            len(channels.findall("ETHERNET-PHYSICAL-CHANNEL")) == 1
        )
        assert (
            len(channels.findall("FLEXRAY-PHYSICAL-CHANNEL")) == 1
        )

    def test_write_communication_cluster(self, writer):
        pkg = _pkg()
        cluster = CanCluster(pkg, "Cluster")
        cluster.setBaudrate(_pos_int("500000"))
        cluster.setProtocolName(_literal("CAN"))
        cluster.setProtocolVersion(_literal("2.0"))
        cluster.createCanPhysicalChannel("CanCh")
        parent = _parent()
        writer.writeCommunicationCluster(parent, cluster)
        assert parent.find("BAUDRATE").text == "500000"
        assert parent.find("PROTOCOL-NAME").text == "CAN"
        assert parent.find("PROTOCOL-VERSION").text == "2.0"
        assert parent.find("PHYSICAL-CHANNELS") is not None


class TestWriteAbstractCanCluster:
    def test_set_can_cluster_bus_off_recovery_none(self, writer):
        parent = _parent()
        writer.setCanClusterBusOffRecovery(
            parent, "BUS-OFF-RECOVERY", None
        )
        assert len(parent) == 0

    def test_set_can_cluster_bus_off_recovery_full(self, writer):
        rec = CanClusterBusOffRecovery()
        rec.setBorCounterL1ToL2(_pos_int("8"))
        rec.setBorTimeL1(_time("0.1"))
        rec.setBorTimeL2(_time("0.2"))
        parent = _parent()
        writer.setCanClusterBusOffRecovery(
            parent, "BUS-OFF-RECOVERY", rec
        )
        tag = parent.find("BUS-OFF-RECOVERY")
        assert tag is not None
        assert tag.find("BOR-COUNTER-L-1-TO-L-2").text == "8"
        assert tag.find("BOR-TIME-L-1").text == "0.1"
        assert tag.find("BOR-TIME-L-2").text == "0.2"

    def test_write_abstract_can_cluster(self, writer):
        pkg = _pkg()
        cluster = CanCluster(pkg, "Cluster")
        rec = CanClusterBusOffRecovery()
        rec.setBorCounterL1ToL2(_pos_int("16"))
        cluster.setBusOffRecovery(rec)
        cluster.setCanFdBaudrate(_pos_int("2000000"))
        cluster.setSpeed(_pos_int("500000"))
        parent = _parent()
        writer.writeAbstractCanCluster(parent, cluster)
        assert parent.find("BUS-OFF-RECOVERY") is not None
        assert parent.find("CAN-FD-BAUDRATE").text == "2000000"
        assert parent.find("SPEED").text == "500000"


class TestWriteLinCluster:
    def test_write_lin_cluster_none(self, writer):
        parent = _parent()
        writer.writeLinCluster(parent, None)
        assert len(parent) == 0

    def test_write_lin_cluster_full(self, writer):
        pkg = _pkg()
        cluster = LinCluster(pkg, "LinCluster")
        cluster.setBaudrate(_pos_int("19200"))
        cluster.setProtocolName(_literal("LIN"))
        cluster.setProtocolVersion(_literal("2.1"))
        cluster.createLinPhysicalChannel("LinCh")
        parent = _parent()
        writer.writeLinCluster(parent, cluster)
        lc = parent.find("LIN-CLUSTER")
        assert lc is not None
        variants = lc.find("LIN-CLUSTER-VARIANTS")
        assert variants is not None
        cond = variants.find("LIN-CLUSTER-CONDITIONAL")
        assert cond is not None
        assert cond.find("BAUDRATE").text == "19200"
        assert cond.find("PROTOCOL-NAME").text == "LIN"
        assert cond.find("PROTOCOL-VERSION").text == "2.1"
        assert cond.find("PHYSICAL-CHANNELS") is not None


class TestWriteCanCluster:
    def test_write_can_cluster_none(self, writer):
        parent = _parent()
        writer.writeCanCluster(parent, None)
        assert len(parent) == 0

    def test_write_can_cluster_full(self, writer):
        pkg = _pkg()
        cluster = CanCluster(pkg, "CanCluster")
        cluster.setBaudrate(_pos_int("500000"))
        cluster.setProtocolName(_literal("CAN"))
        cluster.setProtocolVersion(_literal("2.0"))
        cluster.createCanPhysicalChannel("CanCh")
        rec = CanClusterBusOffRecovery()
        rec.setBorCounterL1ToL2(_pos_int("4"))
        cluster.setBusOffRecovery(rec)
        cluster.setCanFdBaudrate(_pos_int("2000000"))
        cluster.setSpeed(_pos_int("500000"))
        parent = _parent()
        writer.writeCanCluster(parent, cluster)
        cc = parent.find("CAN-CLUSTER")
        assert cc is not None
        variants = cc.find("CAN-CLUSTER-VARIANTS")
        assert variants is not None
        cond = variants.find("CAN-CLUSTER-CONDITIONAL")
        assert cond is not None
        assert cond.find("BAUDRATE").text == "500000"
        assert cond.find("PHYSICAL-CHANNELS") is not None
        assert cond.find("BUS-OFF-RECOVERY") is not None
        assert cond.find("CAN-FD-BAUDRATE").text == "2000000"
        assert cond.find("SPEED").text == "500000"


class TestWriteFlexrayCluster:
    def test_write_flexray_cluster_none(self, writer):
        parent = _parent()
        writer.writeFlexrayCluster(parent, None)
        assert len(parent) == 0

    def test_write_flexray_cluster_full(self, writer):
        pkg = _pkg()
        cluster = FlexrayCluster(pkg, "FlxCluster")
        cluster.setActionPointOffset(_pos_int("1"))
        cluster.setBit(_time("0.1"))
        cluster.setCasRxLowMax(_pos_int("10"))
        cluster.setColdStartAttempts(_pos_int("8"))
        cluster.setCycle(_time("0.005"))
        cluster.setCycleCountMax(_pos_int("64"))
        cluster.setDetectNitError(_boolean("true"))
        cluster.setDynamicSlotIdlePhase(_pos_int("2"))
        cluster.setIgnoreAfterTx(_pos_int("5"))
        cluster.setListenNoise(_pos_int("3"))
        cluster.setMacroPerCycle(_pos_int("36"))
        cluster.setMacrotickDuration(_time("0.001"))
        cluster.setMaxWithoutClockCorrectionFatal(
            _pos_int("2")
        )
        cluster.setMaxWithoutClockCorrectionPassive(
            _pos_int("3")
        )
        cluster.setMinislotActionPointOffset(_pos_int("1"))
        cluster.setMinislotDuration(_pos_int("10"))
        cluster.setNetworkIdleTime(_pos_int("20"))
        cluster.setNetworkManagementVectorLength(
            _pos_int("12")
        )
        cluster.setNumberOfMinislots(_pos_int("790"))
        cluster.setNumberOfStaticSlots(_pos_int("70"))
        cluster.setOffsetCorrectionStart(_pos_int("2"))
        cluster.setPayloadLengthStatic(_pos_int("16"))
        cluster.setSafetyMargin(_pos_int("2"))
        cluster.setSampleClockPeriod(_time("0.05"))
        cluster.setStaticSlotDuration(_pos_int("100"))
        cluster.setSyncFrameIdCountMax(_pos_int("15"))
        cluster.setTransmissionStartSequenceDuration(
            _pos_int("4")
        )
        cluster.setWakeupRxIdle(_pos_int("60"))
        cluster.setWakeupRxLow(_pos_int("180"))
        cluster.setWakeupRxWindow(_pos_int("300"))
        cluster.setWakeupTxActive(_pos_int("60"))
        cluster.setWakeupTxIdle(_pos_int("180"))
        parent = _parent()
        writer.writeFlexrayCluster(parent, cluster)
        fc = parent.find("FLEXRAY-CLUSTER")
        assert fc is not None
        variants = fc.find("FLEXRAY-CLUSTER-VARIANTS")
        assert variants is not None
        cond = variants.find("FLEXRAY-CLUSTER-CONDITIONAL")
        assert cond is not None
        assert (
            cond.find("ACTION-POINT-OFFSET").text == "1"
        )
        assert cond.find("BIT").text == "0.1"
        assert cond.find("CAS-RX-LOW-MAX").text == "10"
        assert (
            cond.find("COLD-START-ATTEMPTS").text == "8"
        )
        assert cond.find("CYCLE").text == "0.005"
        assert cond.find("CYCLE-COUNT-MAX").text == "64"
        assert (
            cond.find("DETECT-NIT-ERROR").text == "true"
        )
        assert (
            cond.find("DYNAMIC-SLOT-IDLE-PHASE").text
            == "2"
        )
        assert cond.find("IGNORE-AFTER-TX").text == "5"
        assert cond.find("LISTEN-NOISE").text == "3"
        assert cond.find("MACRO-PER-CYCLE").text == "36"
        assert (
            cond.find("MACROTICK-DURATION").text == "0.001"
        )
        assert (
            cond.find(
                "MAX-WITHOUT-CLOCK-CORRECTION-FATAL"
            ).text
            == "2"
        )
        assert (
            cond.find(
                "MAX-WITHOUT-CLOCK-CORRECTION-PASSIVE"
            ).text
            == "3"
        )
        assert (
            cond.find(
                "MINISLOT-ACTION-POINT-OFFSET"
            ).text
            == "1"
        )
        assert (
            cond.find("MINISLOT-DURATION").text == "10"
        )
        assert (
            cond.find("NETWORK-IDLE-TIME").text == "20"
        )
        assert (
            cond.find(
                "NETWORK-MANAGEMENT-VECTOR-LENGTH"
            ).text
            == "12"
        )
        assert (
            cond.find("NUMBER-OF-MINISLOTS").text == "790"
        )
        assert (
            cond.find("NUMBER-OF-STATIC-SLOTS").text
            == "70"
        )
        assert (
            cond.find("OFFSET-CORRECTION-START").text
            == "2"
        )
        assert (
            cond.find("PAYLOAD-LENGTH-STATIC").text == "16"
        )
        assert cond.find("SAFETY-MARGIN").text == "2"
        assert (
            cond.find("SAMPLE-CLOCK-PERIOD").text == "0.05"
        )
        assert (
            cond.find("STATIC-SLOT-DURATION").text == "100"
        )
        assert (
            cond.find("SYNC-FRAME-ID-COUNT-MAX").text
            == "15"
        )
        assert (
            cond.find(
                "TRANSMISSION-START-SEQUENCE-DURATION"
            ).text
            == "4"
        )
        assert cond.find("WAKEUP-RX-IDLE").text == "60"
        assert cond.find("WAKEUP-RX-LOW").text == "180"
        assert cond.find("WAKEUP-RX-WINDOW").text == "300"
        assert cond.find("WAKEUP-TX-ACTIVE").text == "60"
        assert cond.find("WAKEUP-TX-IDLE").text == "180"
