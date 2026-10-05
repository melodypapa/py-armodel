"""Parser tests for CanClusterBusOffRecovery (Table 3.10, p.63).

XML element order per XSD group CAN-CLUSTER-BUS-OFF-RECOVERY: BOR-COUNTER-L-1-TO-L-2,
BOR-TIME-L-1, BOR-TIME-L-2, BOR-TIME-TX-ENSURED, MAIN-FUNCTION-PERIOD.
Coverage runs through the BUS-OFF-RECOVERY wrapper dispatch on readAbstractCanCluster.
"""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, TimeValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology import CanClusterBusOffRecovery
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import CanCluster
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"

FULL_RECOVERY = (
    '<BUS-OFF-RECOVERY S="1234" T="2024-01-01T00:00:00Z">'
    "<BOR-COUNTER-L-1-TO-L-2>8</BOR-COUNTER-L-1-TO-L-2>"
    "<BOR-TIME-L-1>0.1</BOR-TIME-L-1>"
    "<BOR-TIME-L-2>1.5</BOR-TIME-L-2>"
    "<BOR-TIME-TX-ENSURED>0.2</BOR-TIME-TX-ENSURED>"
    "<MAIN-FUNCTION-PERIOD>0.01</MAIN-FUNCTION-PERIOD>"
    "</BUS-OFF-RECOVERY>"
)


def _read_into_cluster(inner):
    root = ET.fromstring("<ROOT xmlns='%s'>%s</ROOT>" % (NS, inner))
    pkg = AUTOSAR.getInstance().createARPackage("Pkg")
    cluster = CanCluster(pkg, "Cluster")
    ARXMLParser().readAbstractCanCluster(root, cluster)
    return cluster


class TestReadCanClusterBusOffRecovery:
    def test_returns_none_when_bus_off_recovery_absent(self, parser):
        cluster = _read_into_cluster("<CAN-FD-BAUDRATE>2000000</CAN-FD-BAUDRATE>")
        assert cluster.getBusOffRecovery() is None

    def test_reads_all_five_fields_with_values_and_types(self, parser):
        cluster = _read_into_cluster(FULL_RECOVERY)
        recovery = cluster.getBusOffRecovery()
        assert isinstance(recovery, CanClusterBusOffRecovery)

        counter = recovery.getBorCounterL1ToL2()
        assert isinstance(counter, PositiveInteger)
        assert counter.getValue() == 8

        bor_time_l1 = recovery.getBorTimeL1()
        assert isinstance(bor_time_l1, TimeValue)
        assert bor_time_l1.getValue() == 0.1

        bor_time_l2 = recovery.getBorTimeL2()
        assert isinstance(bor_time_l2, TimeValue)
        assert bor_time_l2.getValue() == 1.5

        bor_time_tx_ensured = recovery.getBorTimeTxEnsured()
        assert isinstance(bor_time_tx_ensured, TimeValue)
        assert bor_time_tx_ensured.getValue() == 0.2

        main_function_period = recovery.getMainFunctionPeriod()
        assert isinstance(main_function_period, TimeValue)
        assert main_function_period.getValue() == 0.01

        assert recovery.getChecksum().getValue() == "1234"
        assert recovery.getTimestamp().getValue() == "2024-01-01T00:00:00Z"

    def test_reads_empty_recovery_wrapper_to_none_fields(self, parser):
        cluster = _read_into_cluster("<BUS-OFF-RECOVERY/>")
        recovery = cluster.getBusOffRecovery()
        assert isinstance(recovery, CanClusterBusOffRecovery)
        assert recovery.getBorCounterL1ToL2() is None
        assert recovery.getBorTimeL1() is None
        assert recovery.getBorTimeL2() is None
        assert recovery.getBorTimeTxEnsured() is None
        assert recovery.getMainFunctionPeriod() is None
