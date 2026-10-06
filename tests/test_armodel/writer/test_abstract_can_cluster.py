"""Writer round-trip tests for AbstractCanCluster (Table 3.8, p.62).

XML element order per XSD groups COMMUNICATION-CLUSTER-CONTENT + ABSTRACT-CAN-CLUSTER-CONTENT
inside CAN-CLUSTER-CONDITIONAL: BAUDRATE, PHYSICAL-CHANNELS, PROTOCOL-NAME, PROTOCOL-VERSION,
BUS-OFF-RECOVERY, CAN-FD-BAUDRATE, CAN-XL-BAUDRATE.
Coverage runs through the reusable writeAbstractCanCluster helper and the concrete writeCanCluster
entry point (exactly-once guard for the inherited level).
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


def _write_helper(cluster):
    parent = _parent()
    ARXMLWriter().writeAbstractCanCluster(parent, cluster)
    return parent


def _write_can_cluster(cluster):
    parent = _parent()
    ARXMLWriter().writeCanCluster(parent, cluster)
    return parent


def _namespaced_first_child(parent):
    xml_text = ET.tostring(parent, encoding="unicode")
    namespaced = ET.fromstring(xml_text.replace(parent[0].tag, "%s xmlns='%s'" % (parent[0].tag, NS), 1))
    return namespaced[0]


class TestWriteAbstractCanCluster:
    def test_helper_writes_inherited_level_before_own_level_in_xsd_order(self):
        conditional = _write_helper(_full_cluster())
        tags = [child.tag for child in conditional]
        assert tags == XSD_ORDER

    def test_helper_writes_field_values(self):
        conditional = _write_helper(_full_cluster())

        assert conditional.find("BAUDRATE").text == "500000"
        assert conditional.find("PROTOCOL-NAME").text == "CAN"
        assert conditional.find("PROTOCOL-VERSION").text == "1982"

        recovery = conditional.find("BUS-OFF-RECOVERY")
        assert recovery is not None
        assert recovery.find("BOR-COUNTER-L-1-TO-L-2").text == "8"
        assert recovery.find("BOR-TIME-L-1").text == "0.1"

        assert conditional.find("CAN-FD-BAUDRATE").text == "2000000"
        assert conditional.find("CAN-XL-BAUDRATE").text == "10000000"

    def test_helper_writes_nothing_for_bare_cluster(self):
        conditional = _write_helper(_new_cluster("Cluster"))
        assert len(conditional) == 0


class TestWriteCanClusterAbstractLevel:
    def test_entry_point_emits_inherited_and_own_levels_exactly_once(self):
        parent = _write_can_cluster(_full_cluster())
        can_cluster = parent.find("CAN-CLUSTER")
        conditional = can_cluster.find("CAN-CLUSTER-VARIANTS/CAN-CLUSTER-CONDITIONAL")

        tags = [child.tag for child in conditional]
        assert tags == XSD_ORDER
        assert tags.count("BAUDRATE") == 1
        assert tags.count("PROTOCOL-NAME") == 1
        assert tags.count("PROTOCOL-VERSION") == 1

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

        assert reloaded.getBaudrate() is None
        assert reloaded.getProtocolName() is None
        assert reloaded.getProtocolVersion() is None
        assert reloaded.getBusOffRecovery() is None
        assert reloaded.getCanFdBaudrate() is None
        assert reloaded.getCanXlBaudrate() is None
