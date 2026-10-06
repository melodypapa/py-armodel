"""
Writer/reader round-trip tests for EthIpProps (Table 3.100, p.146).

XML element order per XSD ETH-IP-PROPS group: IPV-4-PROPS, IPV-6-PROPS.
The IPV-4-PROPS child fully round-trips via readIpv4Props/writeIpv4Props since
the Ipv4Props sync (Table 3.101); the member type Ipv6Props is queued separately
(Table 3.105), so until its sync lands the IPV-6-PROPS child round-trips
presence-only (empty element).
writeEthIpProps calls writeIdentifiable on the ETH-IP-PROPS element exactly once.
"""

import xml.etree.cElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import Ipv6Props
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import EthIpProps, Ipv4ArpProps, Ipv4AutoIpProps, Ipv4FragmentationProps, Ipv4Props
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"

XSD_ORDER = [
    "IPV-4-PROPS",
    "IPV-6-PROPS",
]


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _pkg():
    AUTOSAR.getInstance().setARRelease("R23-11")
    return AUTOSAR.getInstance().createARPackage("Pkg")


def _full_eth_ip_props():
    eth_ip_props = EthIpProps(_pkg(), "IpProps")
    eth_ip_props.setIpv4Props(Ipv4Props())
    eth_ip_props.setIpv6Props(Ipv6Props())
    return eth_ip_props


def _write_eth_ip_props(eth_ip_props):
    parent = ET.Element("PARENT")
    ARXMLWriter().writeEthIpProps(parent, eth_ip_props)
    return parent


def _namespaced_first_child(parent):
    xml_text = ET.tostring(parent, encoding="unicode")
    namespaced = ET.fromstring(xml_text.replace(parent[0].tag, "%s xmlns='%s'" % (parent[0].tag, NS), 1))
    return namespaced[0]


class TestWriteEthIpProps:
    def test_entry_point_emits_short_name_and_group_in_xsd_order(self):
        parent = _write_eth_ip_props(_full_eth_ip_props())
        eth_ip_props = parent.find("ETH-IP-PROPS")

        assert eth_ip_props.find("SHORT-NAME").text == "IpProps"
        children = [child.tag for child in eth_ip_props]
        assert children == ["SHORT-NAME"] + XSD_ORDER

    def test_entry_point_writes_field_values(self):
        parent = _write_eth_ip_props(_full_eth_ip_props())
        eth_ip_props = parent.find("ETH-IP-PROPS")

        assert eth_ip_props.find("IPV-4-PROPS") is not None
        assert eth_ip_props.find("IPV-6-PROPS") is not None

    def test_bare_eth_ip_props_emits_no_group_children(self):
        parent = _write_eth_ip_props(EthIpProps(_pkg(), "IpProps"))
        eth_ip_props = parent.find("ETH-IP-PROPS")

        assert eth_ip_props.find("SHORT-NAME").text == "IpProps"
        for tag in XSD_ORDER:
            assert eth_ip_props.find(tag) is None, tag


class TestEthIpPropsRoundTrip:
    def test_round_trip_full_through_eth_ip_props(self):
        parent = _write_eth_ip_props(_full_eth_ip_props())
        reloaded = EthIpProps(_pkg(), "IpProps")
        ARXMLParser().readEthIpProps(_namespaced_first_child(parent), reloaded)

        assert reloaded.getShortName() == "IpProps"
        assert isinstance(reloaded.getIpv4Props(), Ipv4Props)
        assert isinstance(reloaded.getIpv6Props(), Ipv6Props)

    def test_round_trip_nested_ipv4_props_children(self):
        eth_ip_props = EthIpProps(_pkg(), "IpProps")
        ipv4_props = Ipv4Props()
        ipv4_props.setArpProps(Ipv4ArpProps())
        ipv4_props.setAutoIpProps(Ipv4AutoIpProps())
        ipv4_props.setFragmentationProps(Ipv4FragmentationProps())
        eth_ip_props.setIpv4Props(ipv4_props)

        parent = _write_eth_ip_props(eth_ip_props)
        reloaded = EthIpProps(_pkg(), "IpProps")
        ARXMLParser().readEthIpProps(_namespaced_first_child(parent), reloaded)

        reloaded_ipv4_props = reloaded.getIpv4Props()
        assert isinstance(reloaded_ipv4_props, Ipv4Props)
        assert isinstance(reloaded_ipv4_props.getArpProps(), Ipv4ArpProps)
        assert isinstance(reloaded_ipv4_props.getAutoIpProps(), Ipv4AutoIpProps)
        assert isinstance(reloaded_ipv4_props.getFragmentationProps(), Ipv4FragmentationProps)

    def test_round_trip_empty_through_eth_ip_props(self):
        parent = _write_eth_ip_props(EthIpProps(_pkg(), "IpProps"))
        reloaded = EthIpProps(_pkg(), "IpProps")
        ARXMLParser().readEthIpProps(_namespaced_first_child(parent), reloaded)

        assert reloaded.getShortName() == "IpProps"
        assert reloaded.getIpv4Props() is None
        assert reloaded.getIpv6Props() is None

    def test_save_reload_round_trip_preserves_all_values(self, tmp_path):
        document = AUTOSAR.getInstance()
        document.setARRelease("R23-11")
        pkg = document.createARPackage("Pkg")
        eth_ip_props = pkg.createEthIpProps("IpProps")
        eth_ip_props.setIpv4Props(Ipv4Props())
        eth_ip_props.setIpv6Props(Ipv6Props())

        out_file = str(tmp_path / "eth_ip_props.arxml")
        ARXMLWriter().save(out_file, document)

        reloaded_document = AUTOSAR.getInstance().new()
        reloaded_document = AUTOSAR.getInstance()
        reloaded_document.setARRelease("R23-11")
        ARXMLParser().load(out_file, reloaded_document)

        reloaded_pkg = reloaded_document.getARPackages()[0]
        reloaded = [e for e in reloaded_pkg.getReferrableElements() if isinstance(e, EthIpProps)]
        assert len(reloaded) == 1
        reloaded = reloaded[0]
        assert reloaded.getShortName() == "IpProps"
        assert isinstance(reloaded.getIpv4Props(), Ipv4Props)
        assert isinstance(reloaded.getIpv6Props(), Ipv6Props)
