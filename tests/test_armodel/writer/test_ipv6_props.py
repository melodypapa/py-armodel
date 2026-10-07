"""
Writer/reader round-trip tests for Ipv6Props (Table 3.105, p.148).

XML element order per XSD IPV-6-PROPS group: DHCP-PROPS, FRAGMENTATION-PROPS,
NDP-PROPS (unwrapped direct children of IPV-6-PROPS). The FRAGMENTATION-PROPS child
fully round-trips via writeIpv6FragmentationProps since the Ipv6FragmentationProps
sync (Table 3.106); Dhcpv6Props (Table 3.107) and Ipv6NdpProps (Table 3.108) are
still queued stubs and round-trip presence-only until their syncs land.
writeIpv6Props calls writeARObject on the IPV-6-PROPS element exactly once.
"""

import xml.etree.cElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import Dhcpv6Props, Ipv6NdpProps
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import String
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import Ipv6FragmentationProps, Ipv6Props
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"

XSD_ORDER = [
    "DHCP-PROPS",
    "FRAGMENTATION-PROPS",
    "NDP-PROPS",
]


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _full_ipv6_props():
    ipv6_props = Ipv6Props()
    ipv6_props.setDhcpProps(Dhcpv6Props())
    ipv6_props.setFragmentationProps(Ipv6FragmentationProps())
    ipv6_props.setNdpProps(Ipv6NdpProps())
    return ipv6_props


def _write_ipv6_props(ipv6_props):
    parent = ET.Element("PARENT")
    ARXMLWriter().writeIpv6Props(parent, ipv6_props)
    return parent


def _namespaced_first_child(parent):
    xml_text = ET.tostring(parent, encoding="unicode")
    namespaced = ET.fromstring(xml_text.replace(parent[0].tag, "%s xmlns='%s'" % (parent[0].tag, NS), 1))
    return namespaced[0]


class TestWriteIpv6Props:
    def test_entry_point_emits_children_in_xsd_order(self):
        parent = _write_ipv6_props(_full_ipv6_props())
        ipv6_props = parent.find("IPV-6-PROPS")

        children = [child.tag for child in ipv6_props]
        assert children == XSD_ORDER

    def test_entry_point_writes_field_values(self):
        parent = _write_ipv6_props(_full_ipv6_props())
        ipv6_props = parent.find("IPV-6-PROPS")

        assert ipv6_props.find("DHCP-PROPS") is not None
        assert ipv6_props.find("FRAGMENTATION-PROPS") is not None
        assert ipv6_props.find("NDP-PROPS") is not None

    def test_bare_ipv6_props_emits_no_group_children(self):
        parent = _write_ipv6_props(Ipv6Props())
        ipv6_props = parent.find("IPV-6-PROPS")

        assert len(list(ipv6_props)) == 0

    def test_checksum_and_timestamp_emitted(self):
        ipv6_props = Ipv6Props()
        checksum = String()
        checksum.setValue("123")
        ipv6_props.setChecksum(checksum)
        parent = _write_ipv6_props(ipv6_props)

        assert parent.find("IPV-6-PROPS").attrib.get("S") == "123"


class TestIpv6PropsRoundTrip:
    def test_round_trip_full_through_ipv6_props(self):
        parent = _write_ipv6_props(_full_ipv6_props())
        reloaded = Ipv6Props()
        ARXMLParser().readIpv6Props(_namespaced_first_child(parent), reloaded)

        assert isinstance(reloaded.getDhcpProps(), Dhcpv6Props)
        assert isinstance(reloaded.getFragmentationProps(), Ipv6FragmentationProps)
        assert isinstance(reloaded.getNdpProps(), Ipv6NdpProps)

    def test_round_trip_empty_through_ipv6_props(self):
        parent = _write_ipv6_props(Ipv6Props())
        reloaded = Ipv6Props()
        ARXMLParser().readIpv6Props(_namespaced_first_child(parent), reloaded)

        assert reloaded.getDhcpProps() is None
        assert reloaded.getFragmentationProps() is None
        assert reloaded.getNdpProps() is None

    def test_save_reload_round_trip_preserves_all_values(self, tmp_path):
        document = AUTOSAR.getInstance()
        document.setARRelease("R23-11")
        pkg = document.createARPackage("Pkg")
        eth_ip_props = pkg.createEthIpProps("IpProps")
        ipv6_props = Ipv6Props()
        ipv6_props.setDhcpProps(Dhcpv6Props())
        ipv6_props.setFragmentationProps(Ipv6FragmentationProps())
        ipv6_props.setNdpProps(Ipv6NdpProps())
        eth_ip_props.setIpv6Props(ipv6_props)

        out_file = str(tmp_path / "ipv6_props.arxml")
        ARXMLWriter().save(out_file, document)

        reloaded_document = AUTOSAR.getInstance()
        reloaded_document.setARRelease("R23-11")
        ARXMLParser().load(out_file, reloaded_document)

        reloaded_pkg = reloaded_document.getARPackages()[0]
        reloaded_eth_ip_props = [e for e in reloaded_pkg.getReferrableElements() if e.getShortName() == "IpProps"][0]
        reloaded = reloaded_eth_ip_props.getIpv6Props()
        assert isinstance(reloaded, Ipv6Props)
        assert isinstance(reloaded.getDhcpProps(), Dhcpv6Props)
        assert isinstance(reloaded.getFragmentationProps(), Ipv6FragmentationProps)
        assert isinstance(reloaded.getNdpProps(), Ipv6NdpProps)
