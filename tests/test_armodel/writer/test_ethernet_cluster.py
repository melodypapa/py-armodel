"""Writer/reader round-trip tests for EthernetCluster (Table 3.47, p.103).

XML element order per XSD ETHERNET-CLUSTER: heritage groups (SHORT-NAME via
writeIdentifiable) first, then the ETHERNET-CLUSTER group's ETHERNET-CLUSTER-VARIANTS/
ETHERNET-CLUSTER-CONDITIONAL wrapper carrying the inherited COMMUNICATION-CLUSTER content
in sequenceOffset order (BAUDRATE, PHYSICAL-CHANNELS, PROTOCOL-NAME, PROTOCOL-VERSION)
followed by this class's ETHERNET-CLUSTER-CONTENT (COUPLING-PORT-CONNECTIONS,
COUPLING-PORT-STARTUP-ACTIVE-TIME, COUPLING-PORT-SWITCHOFF-DELAY, MAC-MULTICAST-GROUPS).
writeEthernetCluster calls writeIdentifiable on the outer element and the reusable
writeCommunicationCluster helper exactly once on the CONDITIONAL wrapper.
"""

import xml.etree.cElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import MacAddressString, PositiveInteger, PositiveUnlimitedInteger, RefType, String, TimeValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    CouplingPortConnection,
    EthernetCluster,
    MacMulticastGroup,
)
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def writer():
    AUTOSAR.getInstance().new()
    document = AUTOSAR.getInstance()
    document.setARRelease("R23-11")
    return ARXMLWriter()


@pytest.fixture
def parser():
    AUTOSAR.getInstance().new()
    document = AUTOSAR.getInstance()
    document.setARRelease("R23-11")
    return ARXMLParser()


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


class MockPackage(MockParent):
    def getShortName(self):
        return "Pkg"


def _wrap(element: ET.Element) -> ET.Element:
    inner = ET.tostring(element).decode("utf-8")
    return ET.fromstring(f"<AUTOSAR xmlns='{NS}'>{inner}</AUTOSAR>")


class TestWriteEthernetCluster:
    def test_write_timing_and_multicast_groups(self, writer):
        cluster = EthernetCluster(MockPackage(), "EC1")
        startup = TimeValue().setValue(5)
        cluster.setCouplingPortStartupActiveTime(startup)
        switchoff = TimeValue().setValue(10)
        cluster.setCouplingPortSwitchoffDelay(switchoff)
        cluster.createMacMulticastGroup("MMG1")

        parent = ET.Element("ELEMENTS")
        writer.writeEthernetCluster(parent, cluster)

        node = parent.find("ETHERNET-CLUSTER/ETHERNET-CLUSTER-VARIANTS/ETHERNET-CLUSTER-CONDITIONAL")
        assert node is not None
        assert node.find("COUPLING-PORT-STARTUP-ACTIVE-TIME").text == "5.0"
        assert node.find("COUPLING-PORT-SWITCHOFF-DELAY").text == "10.0"
        assert node.find("MAC-MULTICAST-GROUPS/MAC-MULTICAST-GROUP/SHORT-NAME").text == "MMG1"


class TestEthernetClusterRoundTrip:
    def test_round_trip_preserves_all_values(self, writer, parser, tmp_path):
        cluster = EthernetCluster(MockPackage(), "EC1")
        cluster.setCouplingPortStartupActiveTime(TimeValue().setValue(5))
        cluster.setCouplingPortSwitchoffDelay(TimeValue().setValue(10))
        cluster.createMacMulticastGroup("MMG1")

        parent = ET.Element("ELEMENTS")
        writer.writeEthernetCluster(parent, cluster)

        out_file = str(tmp_path / "ethernet_cluster.arxml")
        with open(out_file, "w", encoding="utf-8") as f:
            f.write(ET.tostring(_wrap(parent), encoding="unicode"))

        tree = ET.parse(out_file)
        recovered = EthernetCluster(MockParent(), "EC1")
        parser.readEthernetCluster(tree.getroot()[0][0], recovered)

        assert recovered.getShortName() == "EC1"
        assert recovered.getCouplingPortStartupActiveTime().getValue() == 5
        assert recovered.getCouplingPortSwitchoffDelay().getValue() == 10
        groups = recovered.getMacMulticastGroups()
        assert len(groups) == 1
        assert isinstance(groups[0], MacMulticastGroup)
        assert groups[0].getShortName() == "MMG1"

    def test_reader_empty_fields(self, parser):
        element = ET.fromstring("<ETHERNET-CLUSTER xmlns='%s'><SHORT-NAME>Empty</SHORT-NAME></ETHERNET-CLUSTER>" % NS)
        recovered = EthernetCluster(MockParent(), "Empty")
        parser.readEthernetCluster(element, recovered)

        assert recovered.getMacMulticastGroups() == []
        assert recovered.getCouplingPortStartupActiveTime() is None
        assert recovered.getCouplingPortSwitchoffDelay() is None


XSD_ORDER = [
    "BAUDRATE",
    "PROTOCOL-NAME",
    "PROTOCOL-VERSION",
    "COUPLING-PORT-CONNECTIONS",
    "COUPLING-PORT-STARTUP-ACTIVE-TIME",
    "COUPLING-PORT-SWITCHOFF-DELAY",
    "MAC-MULTICAST-GROUPS",
]


def _pkg():
    return AUTOSAR.getInstance().createARPackage("Pkg")


def _ref(value):
    ref = RefType()
    ref.setValue(value)
    ref.setDest("COUPLING-PORT-REF")
    return ref


def _full_cluster():
    cluster = EthernetCluster(_pkg(), "Cluster")
    cluster.setBaudrate(PositiveUnlimitedInteger().setValue("10000000"))
    cluster.setProtocolName(String().setValue("AUTOSAR Ethernet"))
    cluster.setProtocolVersion(String().setValue("R23-11"))
    connection = CouplingPortConnection()
    connection.setFirstPortRef(_ref("/Pkg/Switch/Cport1"))
    connection.addNodePortRef(_ref("/Pkg/Node/Cport2"))
    connection.setPlcaLocalNodeCount(PositiveInteger().setValue("8"))
    connection.setPlcaTransmitOpportunityTimer(PositiveInteger().setValue("2"))
    connection.setSecondPortRef(_ref("/Pkg/Node/Cport3"))
    cluster.addCouplingPortConnection(connection)
    cluster.setCouplingPortStartupActiveTime(TimeValue().setValue("5"))
    cluster.setCouplingPortSwitchoffDelay(TimeValue().setValue("10"))
    group = cluster.createMacMulticastGroup("MMG1")
    group.setMacMulticastAddress(MacAddressString().setValue("01:00:5E:7F:FF:FF"))
    return cluster


def _write_ethernet_cluster(cluster):
    parent = ET.Element("PARENT")
    ARXMLWriter().writeEthernetCluster(parent, cluster)
    return parent


def _namespaced_first_child(parent):
    xml_text = ET.tostring(parent, encoding="unicode")
    namespaced = ET.fromstring(xml_text.replace(parent[0].tag, "%s xmlns='%s'" % (parent[0].tag, NS), 1))
    return namespaced[0]


class TestWriteEthernetClusterXsd:
    def test_entry_point_emits_short_name_and_wrapper(self):
        parent = _write_ethernet_cluster(_full_cluster())
        ethernet_cluster = parent.find("ETHERNET-CLUSTER")

        assert ethernet_cluster.find("SHORT-NAME").text == "Cluster"
        assert ethernet_cluster.find("ETHERNET-CLUSTER-VARIANTS/ETHERNET-CLUSTER-CONDITIONAL") is not None

    def test_entry_point_writes_inherited_levels_in_xsd_order_exactly_once(self):
        parent = _write_ethernet_cluster(_full_cluster())
        ethernet_cluster = parent.find("ETHERNET-CLUSTER")
        conditional = ethernet_cluster.find("ETHERNET-CLUSTER-VARIANTS/ETHERNET-CLUSTER-CONDITIONAL")

        assert [child.tag for child in conditional] == XSD_ORDER

        all_tags = [child.tag for child in ethernet_cluster.iter()]
        for tag in XSD_ORDER:
            assert all_tags.count(tag) == 1, tag

    def test_entry_point_writes_field_values(self):
        parent = _write_ethernet_cluster(_full_cluster())
        conditional = parent.find("ETHERNET-CLUSTER/ETHERNET-CLUSTER-VARIANTS/ETHERNET-CLUSTER-CONDITIONAL")

        assert conditional.find("BAUDRATE").text == "10000000"
        assert conditional.find("PROTOCOL-NAME").text == "AUTOSAR Ethernet"
        assert conditional.find("PROTOCOL-VERSION").text == "R23-11"
        assert conditional.find("COUPLING-PORT-CONNECTIONS/COUPLING-PORT-CONNECTION/FIRST-PORT-REF").text == "/Pkg/Switch/Cport1"
        assert conditional.find("COUPLING-PORT-CONNECTIONS/COUPLING-PORT-CONNECTION/NODE-PORTS/COUPLING-PORT-REF-CONDITIONAL/COUPLING-PORT-REF").text == "/Pkg/Node/Cport2"
        assert conditional.find("COUPLING-PORT-CONNECTIONS/COUPLING-PORT-CONNECTION/PLCA-LOCAL-NODE-COUNT").text == "8"
        assert conditional.find("COUPLING-PORT-CONNECTIONS/COUPLING-PORT-CONNECTION/PLCA-TRANSMIT-OPPORTUNITY-TIMER").text == "2"
        assert conditional.find("COUPLING-PORT-CONNECTIONS/COUPLING-PORT-CONNECTION/SECOND-PORT-REF").text == "/Pkg/Node/Cport3"
        assert conditional.find("COUPLING-PORT-STARTUP-ACTIVE-TIME").text == "5"
        assert conditional.find("COUPLING-PORT-SWITCHOFF-DELAY").text == "10"
        assert conditional.find("MAC-MULTICAST-GROUPS/MAC-MULTICAST-GROUP/SHORT-NAME").text == "MMG1"
        assert conditional.find("MAC-MULTICAST-GROUPS/MAC-MULTICAST-GROUP/MAC-MULTICAST-ADDRESS").text == "01:00:5E:7F:FF:FF"

    def test_bare_cluster_emits_short_name_and_empty_wrapper(self):
        parent = _write_ethernet_cluster(EthernetCluster(_pkg(), "Cluster"))
        ethernet_cluster = parent.find("ETHERNET-CLUSTER")

        assert ethernet_cluster.find("SHORT-NAME").text == "Cluster"
        conditional = ethernet_cluster.find("ETHERNET-CLUSTER-VARIANTS/ETHERNET-CLUSTER-CONDITIONAL")
        assert conditional is not None
        assert len(conditional) == 0

    def test_round_trip_full_through_ethernet_cluster(self):
        parent = _write_ethernet_cluster(_full_cluster())
        reloaded = EthernetCluster(_pkg(), "Cluster")
        ARXMLParser().readEthernetCluster(_namespaced_first_child(parent), reloaded)

        assert reloaded.getShortName() == "Cluster"
        assert reloaded.getBaudrate().getValue() == 10000000
        assert reloaded.getProtocolName().getValue() == "AUTOSAR Ethernet"
        assert reloaded.getProtocolVersion().getValue() == "R23-11"
        connections = reloaded.getCouplingPortConnections()
        assert len(connections) == 1
        assert connections[0].getFirstPortRef().getValue() == "/Pkg/Switch/Cport1"
        assert connections[0].getNodePortRefs()[0].getValue() == "/Pkg/Node/Cport2"
        assert connections[0].getPlcaLocalNodeCount().getValue() == 8
        assert connections[0].getPlcaTransmitOpportunityTimer().getValue() == 2
        assert connections[0].getSecondPortRef().getValue() == "/Pkg/Node/Cport3"
        assert reloaded.getCouplingPortStartupActiveTime().getValue() == 5.0
        assert reloaded.getCouplingPortSwitchoffDelay().getValue() == 10.0
        groups = reloaded.getMacMulticastGroups()
        assert len(groups) == 1
        assert isinstance(groups[0], MacMulticastGroup)
        assert groups[0].getShortName() == "MMG1"
        assert groups[0].getMacMulticastAddress().getValue() == "01:00:5E:7F:FF:FF"

    def test_round_trip_empty_through_ethernet_cluster(self):
        parent = _write_ethernet_cluster(EthernetCluster(_pkg(), "Cluster"))
        reloaded = EthernetCluster(_pkg(), "Cluster")
        ARXMLParser().readEthernetCluster(_namespaced_first_child(parent), reloaded)

        assert reloaded.getShortName() == "Cluster"
        assert reloaded.getBaudrate() is None
        assert reloaded.getProtocolName() is None
        assert reloaded.getProtocolVersion() is None
        assert reloaded.getCouplingPortConnections() == []
        assert reloaded.getCouplingPortStartupActiveTime() is None
        assert reloaded.getCouplingPortSwitchoffDelay() is None
        assert reloaded.getMacMulticastGroups() == []
