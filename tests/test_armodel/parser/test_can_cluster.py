"""Parser tests for CanCluster (Table 3.9, p.62).

XML element order per XSD CAN-CLUSTER: heritage groups (SHORT-NAME via IDENTIFIABLE)
first, then the CAN-CLUSTER group's optional CAN-CLUSTER-VARIANTS/
CAN-CLUSTER-CONDITIONAL wrapper carrying the inherited COMMUNICATION-CLUSTER +
ABSTRACT-CAN-CLUSTER content (BAUDRATE, PHYSICAL-CHANNELS, PROTOCOL-NAME,
PROTOCOL-VERSION, BUS-OFF-RECOVERY, CAN-FD-BAUDRATE, CAN-XL-BAUDRATE).
readCanCluster dispatches the conditional content through the reusable
readAbstractCanCluster helper (exactly once).
"""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology import CanClusterBusOffRecovery
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import CanCluster
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"

FULL_CONDITIONAL = (
    "<BAUDRATE>500000</BAUDRATE>"
    "<PROTOCOL-NAME>CAN</PROTOCOL-NAME>"
    "<PROTOCOL-VERSION>1982</PROTOCOL-VERSION>"
    "<BUS-OFF-RECOVERY>"
    "<BOR-COUNTER-L-1-TO-L-2>8</BOR-COUNTER-L-1-TO-L-2>"
    "<BOR-TIME-L-1>0.1</BOR-TIME-L-1>"
    "</BUS-OFF-RECOVERY>"
    "<CAN-FD-BAUDRATE>2000000</CAN-FD-BAUDRATE>"
    "<CAN-XL-BAUDRATE>10000000</CAN-XL-BAUDRATE>"
)

BARE_CONDITIONAL = ""

FULL_CAN_CLUSTER = (
    "<CAN-CLUSTER>" "<SHORT-NAME>Cluster</SHORT-NAME>" "<CAN-CLUSTER-VARIANTS>" "<CAN-CLUSTER-CONDITIONAL>" + FULL_CONDITIONAL + "</CAN-CLUSTER-CONDITIONAL>" "</CAN-CLUSTER-VARIANTS>" "</CAN-CLUSTER>"
)

BARE_CAN_CLUSTER = (
    "<CAN-CLUSTER>" "<SHORT-NAME>Cluster</SHORT-NAME>" "<CAN-CLUSTER-VARIANTS>" "<CAN-CLUSTER-CONDITIONAL>" + BARE_CONDITIONAL + "</CAN-CLUSTER-CONDITIONAL>" "</CAN-CLUSTER-VARIANTS>" "</CAN-CLUSTER>"
)

WRAPPERLESS_CAN_CLUSTER = "<CAN-CLUSTER>" "<SHORT-NAME>Cluster</SHORT-NAME>" "</CAN-CLUSTER>"


def _new_cluster(name):
    pkg = AUTOSAR.getInstance().createARPackage("Pkg")
    return CanCluster(pkg, name)


def _read_can_cluster(xml):
    root = ET.fromstring("<ROOT xmlns='%s'>%s</ROOT>" % (NS, xml))
    cluster = _new_cluster("Cluster")
    ARXMLParser().readCanCluster(root[0], cluster)
    return cluster


class TestReadCanCluster:
    def test_reads_short_name_and_inherited_levels(self):
        cluster = _read_can_cluster(FULL_CAN_CLUSTER)

        assert cluster.getShortName() == "Cluster"
        assert cluster.getBaudrate().getValue() == 500000
        assert cluster.getProtocolName().getValue() == "CAN"
        assert cluster.getProtocolVersion().getValue() == "1982"

        recovery = cluster.getBusOffRecovery()
        assert isinstance(recovery, CanClusterBusOffRecovery)
        assert recovery.getBorCounterL1ToL2().getValue() == 8
        assert recovery.getBorTimeL1().getValue() == 0.1

        assert cluster.getCanFdBaudrate().getValue() == 2000000
        assert cluster.getCanXlBaudrate().getValue() == 10000000

    def test_reads_empty_conditional_to_none_fields(self):
        cluster = _read_can_cluster(BARE_CAN_CLUSTER)

        assert cluster.getShortName() == "Cluster"
        assert cluster.getBaudrate() is None
        assert cluster.getProtocolName() is None
        assert cluster.getProtocolVersion() is None
        assert cluster.getBusOffRecovery() is None
        assert cluster.getCanFdBaudrate() is None
        assert cluster.getCanXlBaudrate() is None

    def test_reads_cluster_without_variants_wrapper_to_none_fields(self):
        cluster = _read_can_cluster(WRAPPERLESS_CAN_CLUSTER)

        assert cluster.getShortName() == "Cluster"
        assert cluster.getBaudrate() is None
        assert cluster.getProtocolName() is None
        assert cluster.getProtocolVersion() is None
        assert cluster.getBusOffRecovery() is None
        assert cluster.getCanFdBaudrate() is None
        assert cluster.getCanXlBaudrate() is None
