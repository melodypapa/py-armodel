"""Writer round-trip tests for CanCluster (Table 3.9, p.62).

XML element order per XSD CAN-CLUSTER: heritage groups (SHORT-NAME via
writeIdentifiable) first, then the CAN-CLUSTER group's CAN-CLUSTER-VARIANTS/
CAN-CLUSTER-CONDITIONAL wrapper carrying the inherited COMMUNICATION-CLUSTER +
ABSTRACT-CAN-CLUSTER content in sequenceOffset order (BAUDRATE, PHYSICAL-CHANNELS,
PROTOCOL-NAME, PROTOCOL-VERSION, BUS-OFF-RECOVERY, CAN-FD-BAUDRATE, CAN-XL-BAUDRATE).
writeCanCluster calls the writeAbstractCanCluster helper exactly once.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, PositiveUnlimitedInteger, String, TimeValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology import CanClusterBusOffRecovery
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import CanCluster
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"

XSD_ORDER = ["BAUDRATE", "PROTOCOL-NAME", "PROTOCOL-VERSION", "BUS-OFF-RECOVERY", "CAN-FD-BAUDRATE", "CAN-XL-BAUDRATE"]


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _parent():
    return ET.Element("PARENT")


def _pos_int(text):
    value = PositiveInteger()
    value.setValue(text)
    return value


def _unlimited_int(text):
    value = PositiveUnlimitedInteger()
    value.setValue(text)
    return value


def _time(text):
    value = TimeValue()
    value.setValue(text)
    return value


def _new_recovery():
    recovery = CanClusterBusOffRecovery()
    recovery.setBorCounterL1ToL2(_pos_int("8"))
    recovery.setBorTimeL1(_time("0.1"))
    return recovery


def _new_cluster(name):
    pkg = AUTOSAR.getInstance().createARPackage("Pkg")
    return CanCluster(pkg, name)


def _full_cluster():
    cluster = _new_cluster("Cluster")
    cluster.setBaudrate(_unlimited_int("500000"))
    cluster.setProtocolName(String().setValue("CAN"))
    cluster.setProtocolVersion(String().setValue("1982"))
    cluster.setBusOffRecovery(_new_recovery())
    cluster.setCanFdBaudrate(_unlimited_int("2000000"))
    cluster.setCanXlBaudrate(_unlimited_int("10000000"))
    return cluster


def _write_can_cluster(cluster):
    parent = _parent()
    ARXMLWriter().writeCanCluster(parent, cluster)
    return parent


def _namespaced_first_child(parent):
    xml_text = ET.tostring(parent, encoding="unicode")
    namespaced = ET.fromstring(xml_text.replace(parent[0].tag, "%s xmlns='%s'" % (parent[0].tag, NS), 1))
    return namespaced[0]


class TestWriteCanCluster:
    def test_entry_point_emits_short_name_and_wrapper(self):
        parent = _write_can_cluster(_full_cluster())
        can_cluster = parent.find("CAN-CLUSTER")

        assert can_cluster.find("SHORT-NAME").text == "Cluster"
        assert can_cluster.find("CAN-CLUSTER-VARIANTS/CAN-CLUSTER-CONDITIONAL") is not None

    def test_entry_point_writes_inherited_levels_in_xsd_order_exactly_once(self):
        parent = _write_can_cluster(_full_cluster())
        can_cluster = parent.find("CAN-CLUSTER")
        conditional = can_cluster.find("CAN-CLUSTER-VARIANTS/CAN-CLUSTER-CONDITIONAL")

        assert [child.tag for child in conditional] == XSD_ORDER

        all_tags = [child.tag for child in can_cluster.iter()]
        for tag in XSD_ORDER:
            assert all_tags.count(tag) == 1, tag

    def test_entry_point_writes_field_values(self):
        parent = _write_can_cluster(_full_cluster())
        conditional = parent.find("CAN-CLUSTER/CAN-CLUSTER-VARIANTS/CAN-CLUSTER-CONDITIONAL")

        assert conditional.find("BAUDRATE").text == "500000"
        assert conditional.find("PROTOCOL-NAME").text == "CAN"
        assert conditional.find("PROTOCOL-VERSION").text == "1982"

        recovery = conditional.find("BUS-OFF-RECOVERY")
        assert recovery is not None
        assert recovery.find("BOR-COUNTER-L-1-TO-L-2").text == "8"
        assert recovery.find("BOR-TIME-L-1").text == "0.1"

        assert conditional.find("CAN-FD-BAUDRATE").text == "2000000"
        assert conditional.find("CAN-XL-BAUDRATE").text == "10000000"

    def test_bare_cluster_emits_short_name_and_empty_wrapper(self):
        parent = _write_can_cluster(_new_cluster("Cluster"))
        can_cluster = parent.find("CAN-CLUSTER")

        assert can_cluster.find("SHORT-NAME").text == "Cluster"
        conditional = can_cluster.find("CAN-CLUSTER-VARIANTS/CAN-CLUSTER-CONDITIONAL")
        assert conditional is not None
        assert len(conditional) == 0

    def test_round_trip_full_through_can_cluster(self):
        parent = _write_can_cluster(_full_cluster())
        reloaded = _new_cluster("Cluster")
        ARXMLParser().readCanCluster(_namespaced_first_child(parent), reloaded)

        assert reloaded.getShortName() == "Cluster"
        assert reloaded.getBaudrate().getValue() == 500000
        assert reloaded.getProtocolName().getValue() == "CAN"
        assert reloaded.getProtocolVersion().getValue() == "1982"

        recovery = reloaded.getBusOffRecovery()
        assert isinstance(recovery, CanClusterBusOffRecovery)
        assert recovery.getBorCounterL1ToL2().getValue() == 8
        assert recovery.getBorTimeL1().getValue() == 0.1

        assert reloaded.getCanFdBaudrate().getValue() == 2000000
        assert reloaded.getCanXlBaudrate().getValue() == 10000000

    def test_round_trip_empty_through_can_cluster(self):
        parent = _write_can_cluster(_new_cluster("Cluster"))
        reloaded = _new_cluster("Cluster")
        ARXMLParser().readCanCluster(_namespaced_first_child(parent), reloaded)

        assert reloaded.getShortName() == "Cluster"
        assert reloaded.getBaudrate() is None
        assert reloaded.getProtocolName() is None
        assert reloaded.getProtocolVersion() is None
        assert reloaded.getBusOffRecovery() is None
        assert reloaded.getCanFdBaudrate() is None
        assert reloaded.getCanXlBaudrate() is None
