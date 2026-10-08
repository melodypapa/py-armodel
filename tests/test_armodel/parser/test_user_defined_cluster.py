"""Parser tests for UserDefinedCluster (Table 3.129, p.179).

XML element order per XSD USER-DEFINED-CLUSTER (AUTOSAR_00052.xsd line 128538):
heritage groups (SHORT-NAME via IDENTIFIABLE) first, then the USER-DEFINED-CLUSTER
group's optional USER-DEFINED-CLUSTER-VARIANTS/USER-DEFINED-CLUSTER-CONDITIONAL
wrapper carrying the inherited COMMUNICATION-CLUSTER content (BAUDRATE,
PHYSICAL-CHANNELS, PROTOCOL-NAME, PROTOCOL-VERSION); USER-DEFINED-CLUSTER-CONTENT
is an empty sequence.
readUserDefinedCluster calls readIdentifiable on the outer element and the reusable
readCommunicationCluster helper exactly once on the CONDITIONAL wrapper.
"""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.CddSupport import UserDefinedCluster
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"

FULL_USER_DEFINED_CLUSTER = (
    "<USER-DEFINED-CLUSTER>"
    "<SHORT-NAME>Cluster</SHORT-NAME>"
    "<USER-DEFINED-CLUSTER-VARIANTS>"
    "<USER-DEFINED-CLUSTER-CONDITIONAL>"
    "<BAUDRATE>500000</BAUDRATE>"
    "<PROTOCOL-NAME>USER-DEFINED</PROTOCOL-NAME>"
    "<PROTOCOL-VERSION>1.0</PROTOCOL-VERSION>"
    "</USER-DEFINED-CLUSTER-CONDITIONAL>"
    "</USER-DEFINED-CLUSTER-VARIANTS>"
    "</USER-DEFINED-CLUSTER>"
)

BARE_USER_DEFINED_CLUSTER = (
    "<USER-DEFINED-CLUSTER>"
    "<SHORT-NAME>Cluster</SHORT-NAME>"
    "<USER-DEFINED-CLUSTER-VARIANTS>"
    "<USER-DEFINED-CLUSTER-CONDITIONAL>"
    "</USER-DEFINED-CLUSTER-CONDITIONAL>"
    "</USER-DEFINED-CLUSTER-VARIANTS>"
    "</USER-DEFINED-CLUSTER>"
)

WRAPPERLESS_USER_DEFINED_CLUSTER = "<USER-DEFINED-CLUSTER>" "<SHORT-NAME>Cluster</SHORT-NAME>" "</USER-DEFINED-CLUSTER>"


def _new_cluster(name):
    pkg = AUTOSAR.getInstance().createARPackage("Pkg")
    return UserDefinedCluster(pkg, name)


def _read_user_defined_cluster(xml):
    root = ET.fromstring("<ROOT xmlns='%s'>%s</ROOT>" % (NS, xml))
    cluster = _new_cluster("Cluster")
    ARXMLParser().readUserDefinedCluster(root[0], cluster)
    return cluster


class TestReadUserDefinedCluster:
    def test_reads_short_name_and_inherited_levels(self):
        cluster = _read_user_defined_cluster(FULL_USER_DEFINED_CLUSTER)

        assert cluster.getShortName() == "Cluster"
        assert cluster.getBaudrate().getValue() == 500000
        assert cluster.getProtocolName().getValue() == "USER-DEFINED"
        assert cluster.getProtocolVersion().getValue() == "1.0"

    def test_reads_no_own_conditional_content(self):
        cluster = _read_user_defined_cluster(FULL_USER_DEFINED_CLUSTER)

        assert cluster.getPhysicalChannels() == []

    def test_reads_empty_conditional_to_none_fields(self):
        cluster = _read_user_defined_cluster(BARE_USER_DEFINED_CLUSTER)

        assert cluster.getShortName() == "Cluster"
        assert cluster.getBaudrate() is None
        assert cluster.getProtocolName() is None
        assert cluster.getProtocolVersion() is None
        assert cluster.getPhysicalChannels() == []

    def test_reads_cluster_without_variants_wrapper_to_none_fields(self):
        cluster = _read_user_defined_cluster(WRAPPERLESS_USER_DEFINED_CLUSTER)

        assert cluster.getShortName() == "Cluster"
        assert cluster.getBaudrate() is None
        assert cluster.getProtocolName() is None
        assert cluster.getProtocolVersion() is None
        assert cluster.getPhysicalChannels() == []
