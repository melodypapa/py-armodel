"""
Writer/reader round-trip tests for Ipv6FragmentationProps (Table 3.106, p.148).

XML element order per XSD IPV-6-FRAGMENTATION-PROPS group (emitted as the
FRAGMENTATION-PROPS element — the instance tag under IPV-6-PROPS; the XSD type is
AR:IPV-6-FRAGMENTATION-PROPS): TCP-IP-IP-REASSEMBLY-BUFFER-COUNT,
TCP-IP-IP-REASSEMBLY-BUFFER-SIZE, TCP-IP-IP-REASSEMBLY-SEGMENT-COUNT,
TCP-IP-IP-REASSEMBLY-TIMEOUT, TCP-IP-IP-TX-FRAGMENT-BUFFER-COUNT,
TCP-IP-IP-TX-FRAGMENT-BUFFER-SIZE (unwrapped direct children).
writeIpv6Props dispatches FRAGMENTATION-PROPS to writeIpv6FragmentationProps since the
Ipv6FragmentationProps sync (Table 3.106) — the child is fully serialized, no longer
identity-only.
writeIpv6FragmentationProps calls writeARObject on the FRAGMENTATION-PROPS element
exactly once.
"""

import xml.etree.cElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, String, TimeValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import Ipv6FragmentationProps, Ipv6Props
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"

XSD_ORDER = [
    "TCP-IP-IP-REASSEMBLY-BUFFER-COUNT",
    "TCP-IP-IP-REASSEMBLY-BUFFER-SIZE",
    "TCP-IP-IP-REASSEMBLY-SEGMENT-COUNT",
    "TCP-IP-IP-REASSEMBLY-TIMEOUT",
    "TCP-IP-IP-TX-FRAGMENT-BUFFER-COUNT",
    "TCP-IP-IP-TX-FRAGMENT-BUFFER-SIZE",
]


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _full_ipv6_fragmentation_props():
    props = Ipv6FragmentationProps()
    props.setTcpIpIpReassemblyBufferCount(PositiveInteger().setValue(4))
    props.setTcpIpIpReassemblyBufferSize(PositiveInteger().setValue(1500))
    props.setTcpIpIpReassemblySegmentCount(PositiveInteger().setValue(2))
    props.setTcpIpIpReassemblyTimeout(TimeValue().setValue(1.0))
    props.setTcpIpIpTxFragmentBufferCount(PositiveInteger().setValue(5))
    props.setTcpIpIpTxFragmentBufferSize(PositiveInteger().setValue(1500))
    return props


def _write_ipv6_fragmentation_props(props):
    parent = ET.Element("PARENT")
    ARXMLWriter().writeIpv6FragmentationProps(parent, props)
    return parent


def _namespaced_first_child(parent):
    xml_text = ET.tostring(parent, encoding="unicode")
    namespaced = ET.fromstring(xml_text.replace(parent[0].tag, "%s xmlns='%s'" % (parent[0].tag, NS), 1))
    return namespaced[0]


class TestWriteIpv6FragmentationProps:
    def test_members_in_xsd_order(self):
        parent = _write_ipv6_fragmentation_props(_full_ipv6_fragmentation_props())
        fragmentation_props = parent.find("FRAGMENTATION-PROPS")

        children = [child.tag for child in fragmentation_props]
        assert children == XSD_ORDER

    def test_members_written_with_field_values(self):
        parent = _write_ipv6_fragmentation_props(_full_ipv6_fragmentation_props())
        fragmentation_props = parent.find("FRAGMENTATION-PROPS")

        assert fragmentation_props.find("TCP-IP-IP-REASSEMBLY-BUFFER-COUNT").text == "4"
        assert fragmentation_props.find("TCP-IP-IP-REASSEMBLY-BUFFER-SIZE").text == "1500"
        assert fragmentation_props.find("TCP-IP-IP-REASSEMBLY-SEGMENT-COUNT").text == "2"
        assert fragmentation_props.find("TCP-IP-IP-REASSEMBLY-TIMEOUT").text == "1.0"
        assert fragmentation_props.find("TCP-IP-IP-TX-FRAGMENT-BUFFER-COUNT").text == "5"
        assert fragmentation_props.find("TCP-IP-IP-TX-FRAGMENT-BUFFER-SIZE").text == "1500"

    def test_bare_props_emits_no_group_children(self):
        parent = _write_ipv6_fragmentation_props(Ipv6FragmentationProps())
        fragmentation_props = parent.find("FRAGMENTATION-PROPS")

        assert len(list(fragmentation_props)) == 0

    def test_checksum_emitted(self):
        props = Ipv6FragmentationProps()
        checksum = String()
        checksum.setValue("789")
        props.setChecksum(checksum)
        parent = _write_ipv6_fragmentation_props(props)

        assert parent.find("FRAGMENTATION-PROPS").attrib.get("S") == "789"


class TestIpv6FragmentationPropsRoundTrip:
    def test_round_trip_full_through_fragmentation_props(self):
        parent = _write_ipv6_fragmentation_props(_full_ipv6_fragmentation_props())
        reloaded = Ipv6FragmentationProps()
        ARXMLParser().readIpv6FragmentationProps(_namespaced_first_child(parent), reloaded)

        assert reloaded.getTcpIpIpReassemblyBufferCount().getValue() == 4
        assert reloaded.getTcpIpIpReassemblyBufferSize().getValue() == 1500
        assert reloaded.getTcpIpIpReassemblySegmentCount().getValue() == 2
        assert reloaded.getTcpIpIpReassemblyTimeout().getValue() == 1.0
        assert reloaded.getTcpIpIpTxFragmentBufferCount().getValue() == 5
        assert reloaded.getTcpIpIpTxFragmentBufferSize().getValue() == 1500

    def test_round_trip_empty_through_fragmentation_props(self):
        parent = _write_ipv6_fragmentation_props(Ipv6FragmentationProps())
        reloaded = Ipv6FragmentationProps()
        ARXMLParser().readIpv6FragmentationProps(_namespaced_first_child(parent), reloaded)

        assert reloaded.getTcpIpIpReassemblyBufferCount() is None
        assert reloaded.getTcpIpIpReassemblyBufferSize() is None
        assert reloaded.getTcpIpIpReassemblySegmentCount() is None
        assert reloaded.getTcpIpIpReassemblyTimeout() is None
        assert reloaded.getTcpIpIpTxFragmentBufferCount() is None
        assert reloaded.getTcpIpIpTxFragmentBufferSize() is None

    def test_round_trip_full_through_ipv6_props_dispatch(self):
        """The upgraded Ipv6Props dispatch fully round-trips the FRAGMENTATION-PROPS child."""
        ipv6_props = Ipv6Props()
        ipv6_props.setFragmentationProps(_full_ipv6_fragmentation_props())
        parent = ET.Element("PARENT")
        ARXMLWriter().writeIpv6Props(parent, ipv6_props)

        fragmentation_props_element = parent.find("IPV-6-PROPS/FRAGMENTATION-PROPS")
        xml_text = ET.tostring(parent.find("IPV-6-PROPS"), encoding="unicode")
        namespaced = ET.fromstring(xml_text.replace("IPV-6-PROPS", "IPV-6-PROPS xmlns='%s'" % NS, 1))

        assert fragmentation_props_element.find("TCP-IP-IP-REASSEMBLY-BUFFER-COUNT").text == "4"
        assert fragmentation_props_element.find("TCP-IP-IP-TX-FRAGMENT-BUFFER-SIZE").text == "1500"

        reloaded = Ipv6Props()
        ARXMLParser().readIpv6Props(namespaced, reloaded)
        reloaded_fragmentation = reloaded.getFragmentationProps()
        assert isinstance(reloaded_fragmentation, Ipv6FragmentationProps)
        assert reloaded_fragmentation.getTcpIpIpReassemblyBufferCount().getValue() == 4
        assert reloaded_fragmentation.getTcpIpIpReassemblyBufferSize().getValue() == 1500
        assert reloaded_fragmentation.getTcpIpIpReassemblySegmentCount().getValue() == 2
        assert reloaded_fragmentation.getTcpIpIpReassemblyTimeout().getValue() == 1.0
        assert reloaded_fragmentation.getTcpIpIpTxFragmentBufferCount().getValue() == 5
        assert reloaded_fragmentation.getTcpIpIpTxFragmentBufferSize().getValue() == 1500

    def test_save_reload_round_trip_preserves_all_values(self, tmp_path):
        document = AUTOSAR.getInstance()
        document.setARRelease("R23-11")
        pkg = document.createARPackage("Pkg")
        eth_ip_props = pkg.createEthIpProps("IpProps")
        ipv6_props = Ipv6Props()
        ipv6_props.setFragmentationProps(_full_ipv6_fragmentation_props())
        eth_ip_props.setIpv6Props(ipv6_props)

        out_file = str(tmp_path / "ipv6_fragmentation_props.arxml")
        ARXMLWriter().save(out_file, document)

        reloaded_document = AUTOSAR.getInstance()
        reloaded_document.setARRelease("R23-11")
        ARXMLParser().load(out_file, reloaded_document)

        reloaded_pkg = reloaded_document.getARPackages()[0]
        reloaded_eth_ip_props = [e for e in reloaded_pkg.getReferrableElements() if e.getShortName() == "IpProps"][0]
        reloaded_fragmentation = reloaded_eth_ip_props.getIpv6Props().getFragmentationProps()
        assert isinstance(reloaded_fragmentation, Ipv6FragmentationProps)
        assert reloaded_fragmentation.getTcpIpIpReassemblyBufferCount().getValue() == 4
        assert reloaded_fragmentation.getTcpIpIpReassemblyBufferSize().getValue() == 1500
        assert reloaded_fragmentation.getTcpIpIpReassemblySegmentCount().getValue() == 2
        assert reloaded_fragmentation.getTcpIpIpReassemblyTimeout().getValue() == 1.0
        assert reloaded_fragmentation.getTcpIpIpTxFragmentBufferCount().getValue() == 5
        assert reloaded_fragmentation.getTcpIpIpTxFragmentBufferSize().getValue() == 1500
