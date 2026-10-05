"""Parser tests for TtcanCluster (Table 3.24, p.76).

XML element order per XSD TTCAN-CLUSTER: heritage groups (SHORT-NAME via IDENTIFIABLE)
first, then the TTCAN-CLUSTER group's optional TTCAN-CLUSTER-VARIANTS/
TTCAN-CLUSTER-CONDITIONAL wrapper carrying the inherited COMMUNICATION-CLUSTER +
ABSTRACT-CAN-CLUSTER content (BAUDRATE, PHYSICAL-CHANNELS, PROTOCOL-NAME,
PROTOCOL-VERSION, BUS-OFF-RECOVERY, CAN-FD-BAUDRATE, CAN-XL-BAUDRATE) plus this
class's TTCAN-CLUSTER-CONTENT (BASIC-CYCLE-LENGTH, NTU, OPERATION-MODE).
readTtcanCluster dispatches the conditional content through the reusable
readAbstractCanCluster helper (exactly once) and reads its own attributes after it.
"""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import TtcanCluster
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"

OWN_CONDITIONAL = "<BASIC-CYCLE-LENGTH>19</BASIC-CYCLE-LENGTH>" "<NTU>0.0001</NTU>" "<OPERATION-MODE>true</OPERATION-MODE>"

BARE_CONDITIONAL = ""

FULL_TTCAN_CLUSTER = (
    "<TTCAN-CLUSTER>"
    "<SHORT-NAME>Cluster</SHORT-NAME>"
    "<TTCAN-CLUSTER-VARIANTS>"
    "<TTCAN-CLUSTER-CONDITIONAL>"
    "<BAUDRATE>500000</BAUDRATE>"
    "<PROTOCOL-NAME>TTCAN</PROTOCOL-NAME>"
    "<PROTOCOL-VERSION>2003</PROTOCOL-VERSION>"
    "<CAN-FD-BAUDRATE>2000000</CAN-FD-BAUDRATE>" + OWN_CONDITIONAL + "</TTCAN-CLUSTER-CONDITIONAL>"
    "</TTCAN-CLUSTER-VARIANTS>"
    "</TTCAN-CLUSTER>"
)

BARE_TTCAN_CLUSTER = (
    "<TTCAN-CLUSTER>"
    "<SHORT-NAME>Cluster</SHORT-NAME>"
    "<TTCAN-CLUSTER-VARIANTS>"
    "<TTCAN-CLUSTER-CONDITIONAL>" + BARE_CONDITIONAL + "</TTCAN-CLUSTER-CONDITIONAL>"
    "</TTCAN-CLUSTER-VARIANTS>"
    "</TTCAN-CLUSTER>"
)

WRAPPERLESS_TTCAN_CLUSTER = "<TTCAN-CLUSTER>" "<SHORT-NAME>Cluster</SHORT-NAME>" "</TTCAN-CLUSTER>"


def _new_cluster(name):
    pkg = AUTOSAR.getInstance().createARPackage("Pkg")
    return TtcanCluster(pkg, name)


def _read_ttcan_cluster(xml):
    root = ET.fromstring("<ROOT xmlns='%s'>%s</ROOT>" % (NS, xml))
    cluster = _new_cluster("Cluster")
    ARXMLParser().readTtcanCluster(root[0], cluster)
    return cluster


class TestReadTtcanCluster:
    def test_reads_short_name_and_inherited_levels(self):
        cluster = _read_ttcan_cluster(FULL_TTCAN_CLUSTER)

        assert cluster.getShortName() == "Cluster"
        assert cluster.getBaudrate().getValue() == 500000
        assert cluster.getProtocolName().getValue() == "TTCAN"
        assert cluster.getProtocolVersion().getValue() == "2003"
        assert cluster.getCanFdBaudrate().getValue() == 2000000

    def test_reads_own_field_values(self):
        cluster = _read_ttcan_cluster(FULL_TTCAN_CLUSTER)

        assert cluster.getBasicCycleLength().getValue() == 19
        assert cluster.getNtu().getValue() == 0.0001
        assert cluster.getOperationMode().getValue() is True

    def test_reads_empty_conditional_to_none_fields(self):
        cluster = _read_ttcan_cluster(BARE_TTCAN_CLUSTER)

        assert cluster.getShortName() == "Cluster"
        assert cluster.getBaudrate() is None
        assert cluster.getProtocolName() is None
        assert cluster.getProtocolVersion() is None
        assert cluster.getBusOffRecovery() is None
        assert cluster.getCanFdBaudrate() is None
        assert cluster.getCanXlBaudrate() is None
        assert cluster.getBasicCycleLength() is None
        assert cluster.getNtu() is None
        assert cluster.getOperationMode() is None

    def test_reads_cluster_without_variants_wrapper_to_none_fields(self):
        cluster = _read_ttcan_cluster(WRAPPERLESS_TTCAN_CLUSTER)

        assert cluster.getShortName() == "Cluster"
        assert cluster.getBaudrate() is None
        assert cluster.getProtocolName() is None
        assert cluster.getProtocolVersion() is None
        assert cluster.getBusOffRecovery() is None
        assert cluster.getBasicCycleLength() is None
        assert cluster.getNtu() is None
        assert cluster.getOperationMode() is None
