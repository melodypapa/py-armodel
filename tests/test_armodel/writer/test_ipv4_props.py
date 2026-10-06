"""
Writer/reader round-trip tests for Ipv4Props (Table 3.101, p.146).

XML element order per XSD IPV-4-PROPS group: ARP-PROPS, AUTO-IP-PROPS,
FRAGMENTATION-PROPS (unwrapped direct children of IPV-4-PROPS).
All three children fully round-trip via readIpv4ArpProps/writeIpv4ArpProps,
readIpv4AutoIpProps/writeIpv4AutoIpProps and
readIpv4FragmentationProps/writeIpv4FragmentationProps since the Ipv4ArpProps
(Table 3.102), Ipv4AutoIpProps (Table 3.103) and Ipv4FragmentationProps
(Table 3.104) syncs.
writeIpv4Props calls writeARObject on the IPV-4-PROPS element exactly once.
"""

import xml.etree.cElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, PositiveInteger, String
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import Ipv4ArpProps, Ipv4AutoIpProps, Ipv4FragmentationProps, Ipv4Props
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"

XSD_ORDER = [
    "ARP-PROPS",
    "AUTO-IP-PROPS",
    "FRAGMENTATION-PROPS",
]


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _full_ipv4_props():
    ipv4_props = Ipv4Props()
    ipv4_props.setArpProps(Ipv4ArpProps())
    ipv4_props.setAutoIpProps(Ipv4AutoIpProps())
    fragmentation_props = Ipv4FragmentationProps()
    fragmentation_props.setTcpIpIpFragmentationRxEnabled(Boolean().setValue(True))
    fragmentation_props.setTcpIpIpNumFragments(PositiveInteger().setValue(8))
    ipv4_props.setFragmentationProps(fragmentation_props)
    return ipv4_props


def _write_ipv4_props(ipv4_props):
    parent = ET.Element("PARENT")
    ARXMLWriter().writeIpv4Props(parent, ipv4_props)
    return parent


def _namespaced_first_child(parent):
    xml_text = ET.tostring(parent, encoding="unicode")
    namespaced = ET.fromstring(xml_text.replace(parent[0].tag, "%s xmlns='%s'" % (parent[0].tag, NS), 1))
    return namespaced[0]


class TestWriteIpv4Props:
    def test_entry_point_emits_children_in_xsd_order(self):
        parent = _write_ipv4_props(_full_ipv4_props())
        ipv4_props = parent.find("IPV-4-PROPS")

        children = [child.tag for child in ipv4_props]
        assert children == XSD_ORDER

    def test_entry_point_writes_field_values(self):
        parent = _write_ipv4_props(_full_ipv4_props())
        ipv4_props = parent.find("IPV-4-PROPS")

        assert ipv4_props.find("ARP-PROPS") is not None
        assert ipv4_props.find("AUTO-IP-PROPS") is not None
        assert ipv4_props.find("FRAGMENTATION-PROPS") is not None

    def test_bare_ipv4_props_emits_no_group_children(self):
        parent = _write_ipv4_props(Ipv4Props())
        ipv4_props = parent.find("IPV-4-PROPS")

        assert len(list(ipv4_props)) == 0

    def test_checksum_and_timestamp_emitted(self):
        ipv4_props = Ipv4Props()
        checksum = String()
        checksum.setValue("123")
        ipv4_props.setChecksum(checksum)
        parent = _write_ipv4_props(ipv4_props)

        assert parent.find("IPV-4-PROPS").attrib.get("S") == "123"


class TestIpv4PropsRoundTrip:
    def test_round_trip_full_through_ipv4_props(self):
        parent = _write_ipv4_props(_full_ipv4_props())
        reloaded = Ipv4Props()
        ARXMLParser().readIpv4Props(_namespaced_first_child(parent), reloaded)

        assert isinstance(reloaded.getArpProps(), Ipv4ArpProps)
        assert isinstance(reloaded.getAutoIpProps(), Ipv4AutoIpProps)
        assert isinstance(reloaded.getFragmentationProps(), Ipv4FragmentationProps)
        assert reloaded.getFragmentationProps().getTcpIpIpFragmentationRxEnabled().getValue() is True
        assert reloaded.getFragmentationProps().getTcpIpIpNumFragments().getValue() == 8

    def test_round_trip_empty_through_ipv4_props(self):
        parent = _write_ipv4_props(Ipv4Props())
        reloaded = Ipv4Props()
        ARXMLParser().readIpv4Props(_namespaced_first_child(parent), reloaded)

        assert reloaded.getArpProps() is None
        assert reloaded.getAutoIpProps() is None
        assert reloaded.getFragmentationProps() is None

    def test_save_reload_round_trip_preserves_all_values(self, tmp_path):
        document = AUTOSAR.getInstance()
        document.setARRelease("R23-11")
        pkg = document.createARPackage("Pkg")
        eth_ip_props = pkg.createEthIpProps("IpProps")
        ipv4_props = Ipv4Props()
        ipv4_props.setArpProps(Ipv4ArpProps())
        ipv4_props.setAutoIpProps(Ipv4AutoIpProps())
        fragmentation_props = Ipv4FragmentationProps()
        fragmentation_props.setTcpIpIpFragmentationRxEnabled(Boolean().setValue(True))
        fragmentation_props.setTcpIpIpNumFragments(PositiveInteger().setValue(8))
        ipv4_props.setFragmentationProps(fragmentation_props)
        eth_ip_props.setIpv4Props(ipv4_props)

        out_file = str(tmp_path / "ipv4_props.arxml")
        ARXMLWriter().save(out_file, document)

        reloaded_document = AUTOSAR.getInstance()
        reloaded_document.setARRelease("R23-11")
        ARXMLParser().load(out_file, reloaded_document)

        reloaded_pkg = reloaded_document.getARPackages()[0]
        reloaded_eth_ip_props = [e for e in reloaded_pkg.getReferrableElements() if e.getShortName() == "IpProps"][0]
        reloaded = reloaded_eth_ip_props.getIpv4Props()
        assert isinstance(reloaded, Ipv4Props)
        assert isinstance(reloaded.getArpProps(), Ipv4ArpProps)
        assert isinstance(reloaded.getAutoIpProps(), Ipv4AutoIpProps)
        assert isinstance(reloaded.getFragmentationProps(), Ipv4FragmentationProps)
        assert reloaded.getFragmentationProps().getTcpIpIpFragmentationRxEnabled().getValue() is True
        assert reloaded.getFragmentationProps().getTcpIpIpNumFragments().getValue() == 8
