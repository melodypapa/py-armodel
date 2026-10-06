"""Writer round-trip tests for FlexrayCluster (Table 3.29, p.81).

XML element order per XSD FLEXRAY-CLUSTER: heritage groups (SHORT-NAME via
writeIdentifiable) first, then the FLEXRAY-CLUSTER group's FLEXRAY-CLUSTER-VARIANTS/
FLEXRAY-CLUSTER-CONDITIONAL wrapper carrying the inherited COMMUNICATION-CLUSTER content
in sequenceOffset order (BAUDRATE, PHYSICAL-CHANNELS, PROTOCOL-NAME, PROTOCOL-VERSION)
followed by this class's FLEXRAY-CLUSTER-CONTENT (ACTION-POINT-OFFSET .. WAKEUP-TX-IDLE).
writeFlexrayCluster calls writeIdentifiable on the outer element and the reusable
writeCommunicationCluster helper exactly once on the CONDITIONAL wrapper.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, Float, Integer, PositiveUnlimitedInteger, String, TimeValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Flexray.FlexrayTopology import FlexrayCluster
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"

XSD_ORDER = [
    "BAUDRATE",
    "PROTOCOL-NAME",
    "PROTOCOL-VERSION",
    "ACTION-POINT-OFFSET",
    "BIT",
    "CAS-RX-LOW-MAX",
    "COLD-START-ATTEMPTS",
    "CYCLE",
    "CYCLE-COUNT-MAX",
    "DETECT-NIT-ERROR",
    "DYNAMIC-SLOT-IDLE-PHASE",
    "IGNORE-AFTER-TX",
    "LISTEN-NOISE",
    "MACRO-PER-CYCLE",
    "MACROTICK-DURATION",
    "MAX-WITHOUT-CLOCK-CORRECTION-FATAL",
    "MAX-WITHOUT-CLOCK-CORRECTION-PASSIVE",
    "MINISLOT-ACTION-POINT-OFFSET",
    "MINISLOT-DURATION",
    "NETWORK-IDLE-TIME",
    "NETWORK-MANAGEMENT-VECTOR-LENGTH",
    "NUMBER-OF-MINISLOTS",
    "NUMBER-OF-STATIC-SLOTS",
    "OFFSET-CORRECTION-START",
    "PAYLOAD-LENGTH-STATIC",
    "SAFETY-MARGIN",
    "SAMPLE-CLOCK-PERIOD",
    "STATIC-SLOT-DURATION",
    "SYMBOL-WINDOW",
    "SYMBOL-WINDOW-ACTION-POINT-OFFSET",
    "SYNC-FRAME-ID-COUNT-MAX",
    "TRANCEIVER-STANDBY-DELAY",
    "TRANSMISSION-START-SEQUENCE-DURATION",
    "WAKEUP-RX-IDLE",
    "WAKEUP-RX-LOW",
    "WAKEUP-RX-WINDOW",
    "WAKEUP-TX-ACTIVE",
    "WAKEUP-TX-IDLE",
]

# (accessor stem, XSD element, construction type, setValue argument, expected value)
OWN_VALUES = [
    ("ActionPointOffset", "ACTION-POINT-OFFSET", Integer, "2", 2),
    ("Bit", "BIT", TimeValue, "0.1", 0.1),
    ("CasRxLowMax", "CAS-RX-LOW-MAX", Integer, "10", 10),
    ("ColdStartAttempts", "COLD-START-ATTEMPTS", Integer, "8", 8),
    ("Cycle", "CYCLE", TimeValue, "0.005", 0.005),
    ("CycleCountMax", "CYCLE-COUNT-MAX", Integer, "63", 63),
    ("DetectNitError", "DETECT-NIT-ERROR", Boolean, True, True),
    ("DynamicSlotIdlePhase", "DYNAMIC-SLOT-IDLE-PHASE", Integer, "2", 2),
    ("IgnoreAfterTx", "IGNORE-AFTER-TX", Integer, "5", 5),
    ("ListenNoise", "LISTEN-NOISE", Integer, "3", 3),
    ("MacroPerCycle", "MACRO-PER-CYCLE", Integer, "36", 36),
    ("MacrotickDuration", "MACROTICK-DURATION", TimeValue, "0.001", 0.001),
    ("MaxWithoutClockCorrectionFatal", "MAX-WITHOUT-CLOCK-CORRECTION-FATAL", Integer, "2", 2),
    ("MaxWithoutClockCorrectionPassive", "MAX-WITHOUT-CLOCK-CORRECTION-PASSIVE", Integer, "3", 3),
    ("MinislotActionPointOffset", "MINISLOT-ACTION-POINT-OFFSET", Integer, "1", 1),
    ("MinislotDuration", "MINISLOT-DURATION", Integer, "10", 10),
    ("NetworkIdleTime", "NETWORK-IDLE-TIME", Integer, "20", 20),
    ("NetworkManagementVectorLength", "NETWORK-MANAGEMENT-VECTOR-LENGTH", Integer, "12", 12),
    ("NumberOfMinislots", "NUMBER-OF-MINISLOTS", Integer, "790", 790),
    ("NumberOfStaticSlots", "NUMBER-OF-STATIC-SLOTS", Integer, "70", 70),
    ("OffsetCorrectionStart", "OFFSET-CORRECTION-START", Integer, "2", 2),
    ("PayloadLengthStatic", "PAYLOAD-LENGTH-STATIC", Integer, "16", 16),
    ("SafetyMargin", "SAFETY-MARGIN", Integer, "2", 2),
    ("SampleClockPeriod", "SAMPLE-CLOCK-PERIOD", TimeValue, "0.05", 0.05),
    ("StaticSlotDuration", "STATIC-SLOT-DURATION", Integer, "100", 100),
    ("SymbolWindow", "SYMBOL-WINDOW", Integer, "101", 101),
    ("SymbolWindowActionPointOffset", "SYMBOL-WINDOW-ACTION-POINT-OFFSET", Integer, "102", 102),
    ("SyncFrameIdCountMax", "SYNC-FRAME-ID-COUNT-MAX", Integer, "15", 15),
    ("TranceiverStandbyDelay", "TRANCEIVER-STANDBY-DELAY", Float, "0.5", 0.5),
    ("TransmissionStartSequenceDuration", "TRANSMISSION-START-SEQUENCE-DURATION", Integer, "4", 4),
    ("WakeupRxIdle", "WAKEUP-RX-IDLE", Integer, "60", 60),
    ("WakeupRxLow", "WAKEUP-RX-LOW", Integer, "180", 180),
    ("WakeupRxWindow", "WAKEUP-RX-WINDOW", Integer, "300", 300),
    ("WakeupTxActive", "WAKEUP-TX-ACTIVE", Integer, "60", 60),
    ("WakeupTxIdle", "WAKEUP-TX-IDLE", Integer, "180", 180),
]


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _parent():
    return ET.Element("PARENT")


def _unlimited_int(text):
    value = PositiveUnlimitedInteger()
    value.setValue(text)
    return value


def _new_cluster(name):
    pkg = AUTOSAR.getInstance().createARPackage("Pkg")
    return FlexrayCluster(pkg, name)


def _full_cluster():
    cluster = _new_cluster("Cluster")
    cluster.setBaudrate(_unlimited_int("500000"))
    cluster.setProtocolName(String().setValue("FLEXRAY"))
    cluster.setProtocolVersion(String().setValue("10.0"))
    for stem, _tag, typ, value, _expected in OWN_VALUES:
        getattr(cluster, "set" + stem)(typ().setValue(value))
    return cluster


def _write_flexray_cluster(cluster):
    parent = _parent()
    ARXMLWriter().writeFlexrayCluster(parent, cluster)
    return parent


def _namespaced_first_child(parent):
    xml_text = ET.tostring(parent, encoding="unicode")
    namespaced = ET.fromstring(xml_text.replace(parent[0].tag, "%s xmlns='%s'" % (parent[0].tag, NS), 1))
    return namespaced[0]


class TestWriteFlexrayCluster:
    def test_entry_point_emits_short_name_and_wrapper(self):
        parent = _write_flexray_cluster(_full_cluster())
        flexray_cluster = parent.find("FLEXRAY-CLUSTER")

        assert flexray_cluster.find("SHORT-NAME").text == "Cluster"
        assert flexray_cluster.find("FLEXRAY-CLUSTER-VARIANTS/FLEXRAY-CLUSTER-CONDITIONAL") is not None

    def test_entry_point_writes_inherited_levels_in_xsd_order_exactly_once(self):
        parent = _write_flexray_cluster(_full_cluster())
        flexray_cluster = parent.find("FLEXRAY-CLUSTER")
        conditional = flexray_cluster.find("FLEXRAY-CLUSTER-VARIANTS/FLEXRAY-CLUSTER-CONDITIONAL")

        assert [child.tag for child in conditional] == XSD_ORDER

        all_tags = [child.tag for child in flexray_cluster.iter()]
        for tag in XSD_ORDER:
            assert all_tags.count(tag) == 1, tag

    def test_entry_point_writes_field_values(self):
        parent = _write_flexray_cluster(_full_cluster())
        conditional = parent.find("FLEXRAY-CLUSTER/FLEXRAY-CLUSTER-VARIANTS/FLEXRAY-CLUSTER-CONDITIONAL")

        assert conditional.find("BAUDRATE").text == "500000"
        assert conditional.find("PROTOCOL-NAME").text == "FLEXRAY"
        assert conditional.find("PROTOCOL-VERSION").text == "10.0"
        for _stem, tag, _typ, _value, expected in OWN_VALUES:
            assert conditional.find(tag).text == ("true" if expected is True else str(expected)), tag

    def test_bare_cluster_emits_short_name_and_empty_wrapper(self):
        parent = _write_flexray_cluster(_new_cluster("Cluster"))
        flexray_cluster = parent.find("FLEXRAY-CLUSTER")

        assert flexray_cluster.find("SHORT-NAME").text == "Cluster"
        conditional = flexray_cluster.find("FLEXRAY-CLUSTER-VARIANTS/FLEXRAY-CLUSTER-CONDITIONAL")
        assert conditional is not None
        assert len(conditional) == 0

    def test_round_trip_full_through_flexray_cluster(self):
        parent = _write_flexray_cluster(_full_cluster())
        reloaded = _new_cluster("Cluster")
        ARXMLParser().readFlexrayCluster(_namespaced_first_child(parent), reloaded)

        assert reloaded.getShortName() == "Cluster"
        assert reloaded.getBaudrate().getValue() == 500000
        assert reloaded.getProtocolName().getValue() == "FLEXRAY"
        assert reloaded.getProtocolVersion().getValue() == "10.0"
        for stem, _tag, _typ, _value, expected in OWN_VALUES:
            assert getattr(reloaded, "get" + stem)().getValue() == expected, stem

    def test_round_trip_empty_through_flexray_cluster(self):
        parent = _write_flexray_cluster(_new_cluster("Cluster"))
        reloaded = _new_cluster("Cluster")
        ARXMLParser().readFlexrayCluster(_namespaced_first_child(parent), reloaded)

        assert reloaded.getShortName() == "Cluster"
        assert reloaded.getBaudrate() is None
        assert reloaded.getProtocolName() is None
        assert reloaded.getProtocolVersion() is None
        assert reloaded.getActionPointOffset() is None
        assert reloaded.getCycle() is None
        assert reloaded.getWakeupTxIdle() is None
