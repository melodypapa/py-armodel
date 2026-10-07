"""
Writer/reader round-trip tests for Dhcpv6Props (Table 3.107, p.149).

XML element order per XSD DHCPV-6-PROPS group (emitted as the DHCP-PROPS element —
the instance tag under IPV-6-PROPS; the XSD type is AR:DHCPV-6-PROPS):
TCP-IP-DHCP-V-6-CNF-DELAY-MAX, TCP-IP-DHCP-V-6-CNF-DELAY-MIN,
TCP-IP-DHCP-V-6-INF-DELAY-MAX, TCP-IP-DHCP-V-6-INF-DELAY-MIN,
TCP-IP-DHCP-V-6-SOL-DELAY-MAX, TCP-IP-DHCP-V-6-SOL-DELAY-MIN (unwrapped direct children).
writeIpv6Props dispatches DHCP-PROPS to writeDhcpv6Props since the Dhcpv6Props sync
(Table 3.107) — the child is fully serialized, no longer identity-only.
writeDhcpv6Props calls writeARObject on the DHCP-PROPS element exactly once.
"""

import xml.etree.cElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import String, TimeValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import Dhcpv6Props, Ipv6Props
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"

XSD_ORDER = [
    "TCP-IP-DHCP-V-6-CNF-DELAY-MAX",
    "TCP-IP-DHCP-V-6-CNF-DELAY-MIN",
    "TCP-IP-DHCP-V-6-INF-DELAY-MAX",
    "TCP-IP-DHCP-V-6-INF-DELAY-MIN",
    "TCP-IP-DHCP-V-6-SOL-DELAY-MAX",
    "TCP-IP-DHCP-V-6-SOL-DELAY-MIN",
]


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _full_dhcpv6_props():
    props = Dhcpv6Props()
    props.setTcpIpDhcpV6CnfDelayMax(TimeValue().setValue(100.0))
    props.setTcpIpDhcpV6CnfDelayMin(TimeValue().setValue(1.0))
    props.setTcpIpDhcpV6InfDelayMax(TimeValue().setValue(110.0))
    props.setTcpIpDhcpV6InfDelayMin(TimeValue().setValue(2.0))
    props.setTcpIpDhcpV6SolDelayMax(TimeValue().setValue(120.0))
    props.setTcpIpDhcpV6SolDelayMin(TimeValue().setValue(3.0))
    return props


def _write_dhcpv6_props(props):
    parent = ET.Element("PARENT")
    ARXMLWriter().writeDhcpv6Props(parent, props)
    return parent


def _namespaced_first_child(parent):
    xml_text = ET.tostring(parent, encoding="unicode")
    namespaced = ET.fromstring(xml_text.replace(parent[0].tag, "%s xmlns='%s'" % (parent[0].tag, NS), 1))
    return namespaced[0]


class TestWriteDhcpv6Props:
    def test_members_in_xsd_order(self):
        parent = _write_dhcpv6_props(_full_dhcpv6_props())
        dhcp_props = parent.find("DHCP-PROPS")

        children = [child.tag for child in dhcp_props]
        assert children == XSD_ORDER

    def test_members_written_with_field_values(self):
        parent = _write_dhcpv6_props(_full_dhcpv6_props())
        dhcp_props = parent.find("DHCP-PROPS")

        assert dhcp_props.find("TCP-IP-DHCP-V-6-CNF-DELAY-MAX").text == "100.0"
        assert dhcp_props.find("TCP-IP-DHCP-V-6-CNF-DELAY-MIN").text == "1.0"
        assert dhcp_props.find("TCP-IP-DHCP-V-6-INF-DELAY-MAX").text == "110.0"
        assert dhcp_props.find("TCP-IP-DHCP-V-6-INF-DELAY-MIN").text == "2.0"
        assert dhcp_props.find("TCP-IP-DHCP-V-6-SOL-DELAY-MAX").text == "120.0"
        assert dhcp_props.find("TCP-IP-DHCP-V-6-SOL-DELAY-MIN").text == "3.0"

    def test_bare_props_emits_no_group_children(self):
        parent = _write_dhcpv6_props(Dhcpv6Props())
        dhcp_props = parent.find("DHCP-PROPS")

        assert len(list(dhcp_props)) == 0

    def test_checksum_emitted(self):
        props = Dhcpv6Props()
        checksum = String()
        checksum.setValue("789")
        props.setChecksum(checksum)
        parent = _write_dhcpv6_props(props)

        assert parent.find("DHCP-PROPS").attrib.get("S") == "789"


class TestDhcpv6PropsRoundTrip:
    def test_round_trip_full_through_dhcp_props(self):
        parent = _write_dhcpv6_props(_full_dhcpv6_props())
        reloaded = Dhcpv6Props()
        ARXMLParser().readDhcpv6Props(_namespaced_first_child(parent), reloaded)

        assert reloaded.getTcpIpDhcpV6CnfDelayMax().getValue() == 100.0
        assert reloaded.getTcpIpDhcpV6CnfDelayMin().getValue() == 1.0
        assert reloaded.getTcpIpDhcpV6InfDelayMax().getValue() == 110.0
        assert reloaded.getTcpIpDhcpV6InfDelayMin().getValue() == 2.0
        assert reloaded.getTcpIpDhcpV6SolDelayMax().getValue() == 120.0
        assert reloaded.getTcpIpDhcpV6SolDelayMin().getValue() == 3.0

    def test_round_trip_empty_through_dhcp_props(self):
        parent = _write_dhcpv6_props(Dhcpv6Props())
        reloaded = Dhcpv6Props()
        ARXMLParser().readDhcpv6Props(_namespaced_first_child(parent), reloaded)

        assert reloaded.getTcpIpDhcpV6CnfDelayMax() is None
        assert reloaded.getTcpIpDhcpV6CnfDelayMin() is None
        assert reloaded.getTcpIpDhcpV6InfDelayMax() is None
        assert reloaded.getTcpIpDhcpV6InfDelayMin() is None
        assert reloaded.getTcpIpDhcpV6SolDelayMax() is None
        assert reloaded.getTcpIpDhcpV6SolDelayMin() is None

    def test_round_trip_full_through_ipv6_props_dispatch(self):
        """The upgraded Ipv6Props dispatch fully round-trips the DHCP-PROPS child."""
        ipv6_props = Ipv6Props()
        ipv6_props.setDhcpProps(_full_dhcpv6_props())
        parent = ET.Element("PARENT")
        ARXMLWriter().writeIpv6Props(parent, ipv6_props)

        dhcp_props_element = parent.find("IPV-6-PROPS/DHCP-PROPS")
        xml_text = ET.tostring(parent.find("IPV-6-PROPS"), encoding="unicode")
        namespaced = ET.fromstring(xml_text.replace("IPV-6-PROPS", "IPV-6-PROPS xmlns='%s'" % NS, 1))

        assert dhcp_props_element.find("TCP-IP-DHCP-V-6-CNF-DELAY-MAX").text == "100.0"
        assert dhcp_props_element.find("TCP-IP-DHCP-V-6-SOL-DELAY-MIN").text == "3.0"

        reloaded = Ipv6Props()
        ARXMLParser().readIpv6Props(namespaced, reloaded)
        reloaded_dhcp = reloaded.getDhcpProps()
        assert isinstance(reloaded_dhcp, Dhcpv6Props)
        assert reloaded_dhcp.getTcpIpDhcpV6CnfDelayMax().getValue() == 100.0
        assert reloaded_dhcp.getTcpIpDhcpV6CnfDelayMin().getValue() == 1.0
        assert reloaded_dhcp.getTcpIpDhcpV6InfDelayMax().getValue() == 110.0
        assert reloaded_dhcp.getTcpIpDhcpV6InfDelayMin().getValue() == 2.0
        assert reloaded_dhcp.getTcpIpDhcpV6SolDelayMax().getValue() == 120.0
        assert reloaded_dhcp.getTcpIpDhcpV6SolDelayMin().getValue() == 3.0

    def test_save_reload_round_trip_preserves_all_values(self, tmp_path):
        document = AUTOSAR.getInstance()
        document.setARRelease("R23-11")
        pkg = document.createARPackage("Pkg")
        eth_ip_props = pkg.createEthIpProps("IpProps")
        ipv6_props = Ipv6Props()
        ipv6_props.setDhcpProps(_full_dhcpv6_props())
        eth_ip_props.setIpv6Props(ipv6_props)

        out_file = str(tmp_path / "dhcpv6_props.arxml")
        ARXMLWriter().save(out_file, document)

        reloaded_document = AUTOSAR.getInstance()
        reloaded_document.setARRelease("R23-11")
        ARXMLParser().load(out_file, reloaded_document)

        reloaded_pkg = reloaded_document.getARPackages()[0]
        reloaded_eth_ip_props = [e for e in reloaded_pkg.getReferrableElements() if e.getShortName() == "IpProps"][0]
        reloaded_dhcp = reloaded_eth_ip_props.getIpv6Props().getDhcpProps()
        assert isinstance(reloaded_dhcp, Dhcpv6Props)
        assert reloaded_dhcp.getTcpIpDhcpV6CnfDelayMax().getValue() == 100.0
        assert reloaded_dhcp.getTcpIpDhcpV6CnfDelayMin().getValue() == 1.0
        assert reloaded_dhcp.getTcpIpDhcpV6InfDelayMax().getValue() == 110.0
        assert reloaded_dhcp.getTcpIpDhcpV6InfDelayMin().getValue() == 2.0
        assert reloaded_dhcp.getTcpIpDhcpV6SolDelayMax().getValue() == 120.0
        assert reloaded_dhcp.getTcpIpDhcpV6SolDelayMin().getValue() == 3.0
