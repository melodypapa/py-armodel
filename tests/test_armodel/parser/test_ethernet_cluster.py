"""Parser tests for EthernetCluster (Table 3.47, p.103).

XML element order per XSD ETHERNET-CLUSTER: heritage groups (SHORT-NAME via IDENTIFIABLE)
first, then the ETHERNET-CLUSTER group's optional ETHERNET-CLUSTER-VARIANTS/
ETHERNET-CLUSTER-CONDITIONAL wrapper carrying the inherited COMMUNICATION-CLUSTER content
(BAUDRATE, PHYSICAL-CHANNELS, PROTOCOL-NAME, PROTOCOL-VERSION) plus this class's
ETHERNET-CLUSTER-CONTENT (COUPLING-PORT-CONNECTIONS, COUPLING-PORT-STARTUP-ACTIVE-TIME,
COUPLING-PORT-SWITCHOFF-DELAY, MAC-MULTICAST-GROUPS).
readEthernetCluster calls readIdentifiable on the outer element and the reusable
readCommunicationCluster helper exactly once on the CONDITIONAL wrapper.
"""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import EthernetCluster, MacMulticastGroup
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"

FULL_COUPING_PORT_CONNECTION = (
    "<COUPLING-PORT-CONNECTION>"
    "<SHORT-NAME>Conn</SHORT-NAME>"
    "<FIRST-PORT-REF DEST='COUPLING-PORT-REF'>/Pkg/Switch/Cport1</FIRST-PORT-REF>"
    "<NODE-PORTS>"
    "<COUPLING-PORT-REF-CONDITIONAL>"
    "<COUPLING-PORT-REF DEST='COUPLING-PORT-REF'>/Pkg/Node/Cport2</COUPLING-PORT-REF>"
    "</COUPLING-PORT-REF-CONDITIONAL>"
    "</NODE-PORTS>"
    "<PLCA-LOCAL-NODE-COUNT>8</PLCA-LOCAL-NODE-COUNT>"
    "<PLCA-TRANSMIT-OPPORTUNITY-TIMER>2</PLCA-TRANSMIT-OPPORTUNITY-TIMER>"
    "<SECOND-PORT-REF DEST='COUPLING-PORT-REF'>/Pkg/Node/Cport3</SECOND-PORT-REF>"
    "</COUPLING-PORT-CONNECTION>"
)

FULL_ETHERNET_CLUSTER = (
    "<ETHERNET-CLUSTER>"
    "<SHORT-NAME>Cluster</SHORT-NAME>"
    "<ETHERNET-CLUSTER-VARIANTS>"
    "<ETHERNET-CLUSTER-CONDITIONAL>"
    "<BAUDRATE>10000000</BAUDRATE>"
    "<PROTOCOL-NAME>AUTOSAR Ethernet</PROTOCOL-NAME>"
    "<PROTOCOL-VERSION>R23-11</PROTOCOL-VERSION>"
    "<COUPLING-PORT-CONNECTIONS>" + FULL_COUPING_PORT_CONNECTION + "</COUPLING-PORT-CONNECTIONS>"
    "<COUPLING-PORT-STARTUP-ACTIVE-TIME>5.0</COUPLING-PORT-STARTUP-ACTIVE-TIME>"
    "<COUPLING-PORT-SWITCHOFF-DELAY>10.0</COUPLING-PORT-SWITCHOFF-DELAY>"
    "<MAC-MULTICAST-GROUPS>"
    "<MAC-MULTICAST-GROUP>"
    "<SHORT-NAME>MMG1</SHORT-NAME>"
    "<MAC-MULTICAST-ADDRESS>01:00:5E:7F:FF:FF</MAC-MULTICAST-ADDRESS>"
    "</MAC-MULTICAST-GROUP>"
    "</MAC-MULTICAST-GROUPS>"
    "</ETHERNET-CLUSTER-CONDITIONAL>"
    "</ETHERNET-CLUSTER-VARIANTS>"
    "</ETHERNET-CLUSTER>"
)

BARE_ETHERNET_CLUSTER = (
    "<ETHERNET-CLUSTER>"
    "<SHORT-NAME>Cluster</SHORT-NAME>"
    "<ETHERNET-CLUSTER-VARIANTS>"
    "<ETHERNET-CLUSTER-CONDITIONAL>"
    "</ETHERNET-CLUSTER-CONDITIONAL>"
    "</ETHERNET-CLUSTER-VARIANTS>"
    "</ETHERNET-CLUSTER>"
)

WRAPPERLESS_ETHERNET_CLUSTER = "<ETHERNET-CLUSTER>" "<SHORT-NAME>Cluster</SHORT-NAME>" "</ETHERNET-CLUSTER>"


def _new_cluster(name):
    pkg = AUTOSAR.getInstance().createARPackage("Pkg")
    return EthernetCluster(pkg, name)


def _read_ethernet_cluster(xml):
    root = ET.fromstring("<ROOT xmlns='%s'>%s</ROOT>" % (NS, xml))
    cluster = _new_cluster("Cluster")
    ARXMLParser().readEthernetCluster(root[0], cluster)
    return cluster


class TestReadEthernetCluster:
    def test_reads_short_name_and_inherited_levels(self):
        cluster = _read_ethernet_cluster(FULL_ETHERNET_CLUSTER)

        assert cluster.getShortName() == "Cluster"
        assert cluster.getBaudrate().getValue() == 10000000
        assert cluster.getProtocolName().getValue() == "AUTOSAR Ethernet"
        assert cluster.getProtocolVersion().getValue() == "R23-11"

    def test_reads_own_field_values(self):
        cluster = _read_ethernet_cluster(FULL_ETHERNET_CLUSTER)

        assert cluster.getCouplingPortStartupActiveTime().getValue() == 5.0
        assert cluster.getCouplingPortSwitchoffDelay().getValue() == 10.0

    def test_reads_coupling_port_connection_values(self):
        cluster = _read_ethernet_cluster(FULL_ETHERNET_CLUSTER)

        connections = cluster.getCouplingPortConnections()
        assert len(connections) == 1
        connection = connections[0]
        assert connection.getFirstPortRef().getValue() == "/Pkg/Switch/Cport1"
        assert connection.getFirstPortRef().getDest() == "COUPLING-PORT-REF"
        node_port_refs = connection.getNodePortRefs()
        assert len(node_port_refs) == 1
        assert node_port_refs[0].getValue() == "/Pkg/Node/Cport2"
        assert connection.getPlcaLocalNodeCount().getValue() == 8
        assert connection.getPlcaTransmitOpportunityTimer().getValue() == 2
        assert connection.getSecondPortRef().getValue() == "/Pkg/Node/Cport3"

    def test_reads_mac_multicast_group_values(self):
        cluster = _read_ethernet_cluster(FULL_ETHERNET_CLUSTER)

        groups = cluster.getMacMulticastGroups()
        assert len(groups) == 1
        assert isinstance(groups[0], MacMulticastGroup)
        assert groups[0].getShortName() == "MMG1"
        assert groups[0].getMacMulticastAddress().getValue() == "01:00:5E:7F:FF:FF"

    def test_reads_empty_conditional_to_none_and_empty_fields(self):
        cluster = _read_ethernet_cluster(BARE_ETHERNET_CLUSTER)

        assert cluster.getShortName() == "Cluster"
        assert cluster.getBaudrate() is None
        assert cluster.getProtocolName() is None
        assert cluster.getProtocolVersion() is None
        assert cluster.getCouplingPortConnections() == []
        assert cluster.getCouplingPortStartupActiveTime() is None
        assert cluster.getCouplingPortSwitchoffDelay() is None
        assert cluster.getMacMulticastGroups() == []

    def test_reads_cluster_without_variants_wrapper_to_none_fields(self):
        cluster = _read_ethernet_cluster(WRAPPERLESS_ETHERNET_CLUSTER)

        assert cluster.getShortName() == "Cluster"
        assert cluster.getBaudrate() is None
        assert cluster.getProtocolName() is None
        assert cluster.getProtocolVersion() is None
        assert cluster.getCouplingPortConnections() == []
        assert cluster.getCouplingPortStartupActiveTime() is None
        assert cluster.getCouplingPortSwitchoffDelay() is None
        assert cluster.getMacMulticastGroups() == []
