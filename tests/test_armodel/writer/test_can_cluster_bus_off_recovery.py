"""Writer round-trip tests for CanClusterBusOffRecovery (Table 3.10, p.63).

XML element order per XSD group CAN-CLUSTER-BUS-OFF-RECOVERY: BOR-COUNTER-L-1-TO-L-2,
BOR-TIME-L-1, BOR-TIME-L-2, BOR-TIME-TX-ENSURED, MAIN-FUNCTION-PERIOD.
Coverage runs through the BUS-OFF-RECOVERY wrapper dispatch on writeAbstractCanCluster.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, TimeValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology import CanClusterBusOffRecovery
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import CanCluster
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


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


def _time(text):
    value = TimeValue()
    value.setValue(text)
    return value


def _new_recovery():
    recovery = CanClusterBusOffRecovery()
    recovery.setBorCounterL1ToL2(_pos_int("8"))
    recovery.setBorTimeL1(_time("0.1"))
    recovery.setBorTimeL2(_time("1.5"))
    recovery.setBorTimeTxEnsured(_time("0.2"))
    recovery.setMainFunctionPeriod(_time("0.01"))
    return recovery


class TestWriteCanClusterBusOffRecovery:
    def test_write_none_recovery_omits_wrapper(self):
        parent = _parent()
        ARXMLWriter().setCanClusterBusOffRecovery(parent, "BUS-OFF-RECOVERY", None)
        assert len(parent) == 0

    def test_write_all_five_fields_in_xsd_order(self):
        parent = _parent()
        ARXMLWriter().setCanClusterBusOffRecovery(parent, "BUS-OFF-RECOVERY", _new_recovery())
        tag = parent.find("BUS-OFF-RECOVERY")
        assert tag is not None
        tags = [child.tag for child in tag]
        assert tags == ["BOR-COUNTER-L-1-TO-L-2", "BOR-TIME-L-1", "BOR-TIME-L-2", "BOR-TIME-TX-ENSURED", "MAIN-FUNCTION-PERIOD"]

    def test_write_field_values(self):
        parent = _parent()
        ARXMLWriter().setCanClusterBusOffRecovery(parent, "BUS-OFF-RECOVERY", _new_recovery())
        tag = parent.find("BUS-OFF-RECOVERY")
        assert tag.find("BOR-COUNTER-L-1-TO-L-2").text == "8"
        assert tag.find("BOR-TIME-L-1").text == "0.1"
        assert tag.find("BOR-TIME-L-2").text == "1.5"
        assert tag.find("BOR-TIME-TX-ENSURED").text == "0.2"
        assert tag.find("MAIN-FUNCTION-PERIOD").text == "0.01"

    def test_write_empty_recovery_omits_child_tags(self):
        parent = _parent()
        ARXMLWriter().setCanClusterBusOffRecovery(parent, "BUS-OFF-RECOVERY", CanClusterBusOffRecovery())
        tag = parent.find("BUS-OFF-RECOVERY")
        assert tag is not None
        assert len(tag) == 0

    def test_round_trip_preserves_all_values(self):
        pkg = AUTOSAR.getInstance().createARPackage("Pkg")
        cluster = CanCluster(pkg, "Cluster")
        cluster.setBusOffRecovery(_new_recovery())

        parent = _parent()
        ARXMLWriter().writeAbstractCanCluster(parent, cluster)
        inner = ET.tostring(parent).decode("utf-8")
        root = ET.fromstring("<ROOT xmlns='%s'>%s</ROOT>" % (NS, inner))

        parsed_pkg = AUTOSAR.getInstance().createARPackage("Parsed")
        parsed_cluster = CanCluster(parsed_pkg, "Cluster")
        ARXMLParser().readAbstractCanCluster(root[0], parsed_cluster)

        recovery = parsed_cluster.getBusOffRecovery()
        assert isinstance(recovery, CanClusterBusOffRecovery)
        assert recovery.getBorCounterL1ToL2().getValue() == 8
        assert recovery.getBorTimeL1().getValue() == 0.1
        assert recovery.getBorTimeL2().getValue() == 1.5
        assert isinstance(recovery.getBorTimeTxEnsured(), TimeValue)
        assert recovery.getBorTimeTxEnsured().getValue() == 0.2
        assert isinstance(recovery.getMainFunctionPeriod(), TimeValue)
        assert recovery.getMainFunctionPeriod().getValue() == 0.01
