"""Parser tests for LinCluster (Table 3.36, p.93).

XML element order per XSD LIN-CLUSTER (AUTOSAR_00052.xsd line 76922): heritage groups
(SHORT-NAME via IDENTIFIABLE) first, then the LIN-CLUSTER group's optional
LIN-CLUSTER-VARIANTS/LIN-CLUSTER-CONDITIONAL wrapper carrying the inherited
COMMUNICATION-CLUSTER content (BAUDRATE, PHYSICAL-CHANNELS, PROTOCOL-NAME,
PROTOCOL-VERSION); LIN-CLUSTER-CONTENT is an empty sequence.
readLinCluster calls readIdentifiable on the outer element and the reusable
readCommunicationCluster helper exactly once on the CONDITIONAL wrapper.
"""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinTopology import LinCluster
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"

FULL_LIN_CLUSTER = (
    "<LIN-CLUSTER>"
    "<SHORT-NAME>Cluster</SHORT-NAME>"
    "<LIN-CLUSTER-VARIANTS>"
    "<LIN-CLUSTER-CONDITIONAL>"
    "<BAUDRATE>19200</BAUDRATE>"
    "<PROTOCOL-NAME>LIN</PROTOCOL-NAME>"
    "<PROTOCOL-VERSION>2.2</PROTOCOL-VERSION>"
    "</LIN-CLUSTER-CONDITIONAL>"
    "</LIN-CLUSTER-VARIANTS>"
    "</LIN-CLUSTER>"
)

BARE_LIN_CLUSTER = "<LIN-CLUSTER>" "<SHORT-NAME>Cluster</SHORT-NAME>" "<LIN-CLUSTER-VARIANTS>" "<LIN-CLUSTER-CONDITIONAL>" "</LIN-CLUSTER-CONDITIONAL>" "</LIN-CLUSTER-VARIANTS>" "</LIN-CLUSTER>"

WRAPPERLESS_LIN_CLUSTER = "<LIN-CLUSTER>" "<SHORT-NAME>Cluster</SHORT-NAME>" "</LIN-CLUSTER>"


def _new_cluster(name):
    pkg = AUTOSAR.getInstance().createARPackage("Pkg")
    return LinCluster(pkg, name)


def _read_lin_cluster(xml):
    root = ET.fromstring("<ROOT xmlns='%s'>%s</ROOT>" % (NS, xml))
    cluster = _new_cluster("Cluster")
    ARXMLParser().readLinCluster(root[0], cluster)
    return cluster


class TestReadLinCluster:
    def test_reads_short_name_and_inherited_levels(self):
        cluster = _read_lin_cluster(FULL_LIN_CLUSTER)

        assert cluster.getShortName() == "Cluster"
        assert cluster.getBaudrate().getValue() == 19200
        assert cluster.getProtocolName().getValue() == "LIN"
        assert cluster.getProtocolVersion().getValue() == "2.2"

    def test_reads_no_own_conditional_content(self):
        cluster = _read_lin_cluster(FULL_LIN_CLUSTER)

        assert cluster.getPhysicalChannels() == []

    def test_reads_empty_conditional_to_none_fields(self):
        cluster = _read_lin_cluster(BARE_LIN_CLUSTER)

        assert cluster.getShortName() == "Cluster"
        assert cluster.getBaudrate() is None
        assert cluster.getProtocolName() is None
        assert cluster.getProtocolVersion() is None
        assert cluster.getPhysicalChannels() == []

    def test_reads_cluster_without_variants_wrapper_to_none_fields(self):
        cluster = _read_lin_cluster(WRAPPERLESS_LIN_CLUSTER)

        assert cluster.getShortName() == "Cluster"
        assert cluster.getBaudrate() is None
        assert cluster.getProtocolName() is None
        assert cluster.getProtocolVersion() is None
        assert cluster.getPhysicalChannels() == []
