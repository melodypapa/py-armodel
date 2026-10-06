"""Writer round-trip tests for TtcanCluster (Table 3.24, p.76).

XML element order per XSD TTCAN-CLUSTER: heritage groups (SHORT-NAME via
writeIdentifiable) first, then the TTCAN-CLUSTER group's TTCAN-CLUSTER-VARIANTS/
TTCAN-CLUSTER-CONDITIONAL wrapper carrying the inherited COMMUNICATION-CLUSTER +
ABSTRACT-CAN-CLUSTER content in sequenceOffset order (BAUDRATE, PHYSICAL-CHANNELS,
PROTOCOL-NAME, PROTOCOL-VERSION, BUS-OFF-RECOVERY, CAN-FD-BAUDRATE, CAN-XL-BAUDRATE)
followed by this class's TTCAN-CLUSTER-CONTENT (BASIC-CYCLE-LENGTH, NTU,
OPERATION-MODE). writeTtcanCluster calls the writeAbstractCanCluster helper exactly
once.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, Integer, PositiveInteger, PositiveUnlimitedInteger, String, TimeValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology import CanClusterBusOffRecovery
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import TtcanCluster
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"

XSD_ORDER = [
    "BAUDRATE",
    "PROTOCOL-NAME",
    "PROTOCOL-VERSION",
    "BUS-OFF-RECOVERY",
    "CAN-FD-BAUDRATE",
    "CAN-XL-BAUDRATE",
    "BASIC-CYCLE-LENGTH",
    "NTU",
    "OPERATION-MODE",
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


def _new_recovery():
    recovery = CanClusterBusOffRecovery()
    recovery.setBorCounterL1ToL2(PositiveInteger().setValue("8"))
    recovery.setBorTimeL1(TimeValue().setValue("0.1"))
    return recovery


def _new_cluster(name):
    pkg = AUTOSAR.getInstance().createARPackage("Pkg")
    return TtcanCluster(pkg, name)


def _full_cluster():
    cluster = _new_cluster("Cluster")
    cluster.setBaudrate(_unlimited_int("500000"))
    cluster.setProtocolName(String().setValue("TTCAN"))
    cluster.setProtocolVersion(String().setValue("2003"))
    cluster.setBusOffRecovery(_new_recovery())
    cluster.setCanFdBaudrate(_unlimited_int("2000000"))
    cluster.setCanXlBaudrate(_unlimited_int("10000000"))
    cluster.setBasicCycleLength(Integer().setValue(19))
    cluster.setNtu(TimeValue().setValue("0.0001"))
    cluster.setOperationMode(Boolean().setValue(True))
    return cluster


def _write_ttcan_cluster(cluster):
    parent = _parent()
    ARXMLWriter().writeTtcanCluster(parent, cluster)
    return parent


def _namespaced_first_child(parent):
    xml_text = ET.tostring(parent, encoding="unicode")
    namespaced = ET.fromstring(xml_text.replace(parent[0].tag, "%s xmlns='%s'" % (parent[0].tag, NS), 1))
    return namespaced[0]


class TestWriteTtcanCluster:
    def test_entry_point_emits_short_name_and_wrapper(self):
        parent = _write_ttcan_cluster(_full_cluster())
        ttcan_cluster = parent.find("TTCAN-CLUSTER")

        assert ttcan_cluster.find("SHORT-NAME").text == "Cluster"
        assert ttcan_cluster.find("TTCAN-CLUSTER-VARIANTS/TTCAN-CLUSTER-CONDITIONAL") is not None

    def test_entry_point_writes_inherited_levels_in_xsd_order_exactly_once(self):
        parent = _write_ttcan_cluster(_full_cluster())
        ttcan_cluster = parent.find("TTCAN-CLUSTER")
        conditional = ttcan_cluster.find("TTCAN-CLUSTER-VARIANTS/TTCAN-CLUSTER-CONDITIONAL")

        assert [child.tag for child in conditional] == XSD_ORDER

        all_tags = [child.tag for child in ttcan_cluster.iter()]
        for tag in XSD_ORDER:
            assert all_tags.count(tag) == 1, tag

    def test_entry_point_writes_field_values(self):
        parent = _write_ttcan_cluster(_full_cluster())
        conditional = parent.find("TTCAN-CLUSTER/TTCAN-CLUSTER-VARIANTS/TTCAN-CLUSTER-CONDITIONAL")

        assert conditional.find("BAUDRATE").text == "500000"
        assert conditional.find("PROTOCOL-NAME").text == "TTCAN"
        assert conditional.find("PROTOCOL-VERSION").text == "2003"
        assert conditional.find("CAN-FD-BAUDRATE").text == "2000000"

        assert conditional.find("BASIC-CYCLE-LENGTH").text == "19"
        assert conditional.find("NTU").text == "0.0001"
        assert conditional.find("OPERATION-MODE").text == "true"

    def test_bare_cluster_emits_short_name_and_empty_wrapper(self):
        parent = _write_ttcan_cluster(_new_cluster("Cluster"))
        ttcan_cluster = parent.find("TTCAN-CLUSTER")

        assert ttcan_cluster.find("SHORT-NAME").text == "Cluster"
        conditional = ttcan_cluster.find("TTCAN-CLUSTER-VARIANTS/TTCAN-CLUSTER-CONDITIONAL")
        assert conditional is not None
        assert len(conditional) == 0

    def test_round_trip_full_through_ttcan_cluster(self):
        parent = _write_ttcan_cluster(_full_cluster())
        reloaded = _new_cluster("Cluster")
        ARXMLParser().readTtcanCluster(_namespaced_first_child(parent), reloaded)

        assert reloaded.getShortName() == "Cluster"
        assert reloaded.getBaudrate().getValue() == 500000
        assert reloaded.getProtocolName().getValue() == "TTCAN"
        assert reloaded.getProtocolVersion().getValue() == "2003"
        assert reloaded.getCanFdBaudrate().getValue() == 2000000

        assert reloaded.getBasicCycleLength().getValue() == 19
        assert reloaded.getNtu().getValue() == 0.0001
        assert reloaded.getOperationMode().getValue() is True

    def test_round_trip_empty_through_ttcan_cluster(self):
        parent = _write_ttcan_cluster(_new_cluster("Cluster"))
        reloaded = _new_cluster("Cluster")
        ARXMLParser().readTtcanCluster(_namespaced_first_child(parent), reloaded)

        assert reloaded.getShortName() == "Cluster"
        assert reloaded.getBaudrate() is None
        assert reloaded.getProtocolName() is None
        assert reloaded.getProtocolVersion() is None
        assert reloaded.getBusOffRecovery() is None
        assert reloaded.getBasicCycleLength() is None
        assert reloaded.getNtu() is None
        assert reloaded.getOperationMode() is None
