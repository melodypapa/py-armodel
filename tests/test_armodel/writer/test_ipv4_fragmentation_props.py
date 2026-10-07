"""
Writer/reader round-trip tests for Ipv4FragmentationProps (Table 3.104, p.147).

XML element order per XSD IPV-4-FRAGMENTATION-PROPS group (emitted as the
FRAGMENTATION-PROPS element, XSD type AR:IPV-4-FRAGMENTATION-PROPS):
TCP-IP-IP-FRAGMENTATION-RX-ENABLED, TCP-IP-IP-NUM-FRAGMENTS,
TCP-IP-IP-NUM-REASS-DGRAMS, TCP-IP-IP-REASS-TIMEOUT (unwrapped direct children).
writeIpv4Props dispatches FRAGMENTATION-PROPS to writeIpv4FragmentationProps since the
Ipv4FragmentationProps sync (Table 3.104) — the child is fully serialized, no longer
identity-only.
writeIpv4FragmentationProps calls writeARObject on the FRAGMENTATION-PROPS element
exactly once.
"""

import xml.etree.cElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
    String,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import Ipv4FragmentationProps, Ipv4Props
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"

XSD_ORDER = [
    "TCP-IP-IP-FRAGMENTATION-RX-ENABLED",
    "TCP-IP-IP-NUM-FRAGMENTS",
    "TCP-IP-IP-NUM-REASS-DGRAMS",
    "TCP-IP-IP-REASS-TIMEOUT",
]


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _full_ipv4_fragmentation_props():
    props = Ipv4FragmentationProps()
    props.setTcpIpIpFragmentationRxEnabled(Boolean().setValue(True))
    props.setTcpIpIpNumFragments(PositiveInteger().setValue(8))
    props.setTcpIpIpNumReassDgrams(PositiveInteger().setValue(4))
    props.setTcpIpIpReassTimeout(TimeValue().setValue(15.0))
    return props


def _write_ipv4_fragmentation_props(props):
    parent = ET.Element("PARENT")
    ARXMLWriter().writeIpv4FragmentationProps(parent, props)
    return parent


def _namespaced_first_child(parent):
    xml_text = ET.tostring(parent, encoding="unicode")
    namespaced = ET.fromstring(xml_text.replace(parent[0].tag, "%s xmlns='%s'" % (parent[0].tag, NS), 1))
    return namespaced[0]


class TestWriteIpv4FragmentationProps:
    def test_members_in_xsd_order(self):
        parent = _write_ipv4_fragmentation_props(_full_ipv4_fragmentation_props())
        fragmentation_props = parent.find("FRAGMENTATION-PROPS")

        children = [child.tag for child in fragmentation_props]
        assert children == XSD_ORDER

    def test_members_written_with_field_values(self):
        parent = _write_ipv4_fragmentation_props(_full_ipv4_fragmentation_props())
        fragmentation_props = parent.find("FRAGMENTATION-PROPS")

        assert fragmentation_props.find("TCP-IP-IP-FRAGMENTATION-RX-ENABLED").text == "true"
        assert fragmentation_props.find("TCP-IP-IP-NUM-FRAGMENTS").text == "8"
        assert fragmentation_props.find("TCP-IP-IP-NUM-REASS-DGRAMS").text == "4"
        assert fragmentation_props.find("TCP-IP-IP-REASS-TIMEOUT").text == "15.0"

    def test_bare_props_emits_no_group_children(self):
        parent = _write_ipv4_fragmentation_props(Ipv4FragmentationProps())
        fragmentation_props = parent.find("FRAGMENTATION-PROPS")

        assert len(list(fragmentation_props)) == 0

    def test_checksum_emitted(self):
        props = Ipv4FragmentationProps()
        checksum = String()
        checksum.setValue("789")
        props.setChecksum(checksum)
        parent = _write_ipv4_fragmentation_props(props)

        assert parent.find("FRAGMENTATION-PROPS").attrib.get("S") == "789"


class TestIpv4FragmentationPropsRoundTrip:
    def test_round_trip_full_through_fragmentation_props(self):
        parent = _write_ipv4_fragmentation_props(_full_ipv4_fragmentation_props())
        reloaded = Ipv4FragmentationProps()
        ARXMLParser().readIpv4FragmentationProps(_namespaced_first_child(parent), reloaded)

        assert reloaded.getTcpIpIpFragmentationRxEnabled().getValue() is True
        assert reloaded.getTcpIpIpNumFragments().getValue() == 8
        assert reloaded.getTcpIpIpNumReassDgrams().getValue() == 4
        assert reloaded.getTcpIpIpReassTimeout().getValue() == 15.0

    def test_round_trip_empty_through_fragmentation_props(self):
        parent = _write_ipv4_fragmentation_props(Ipv4FragmentationProps())
        reloaded = Ipv4FragmentationProps()
        ARXMLParser().readIpv4FragmentationProps(_namespaced_first_child(parent), reloaded)

        assert reloaded.getTcpIpIpFragmentationRxEnabled() is None
        assert reloaded.getTcpIpIpNumFragments() is None
        assert reloaded.getTcpIpIpNumReassDgrams() is None
        assert reloaded.getTcpIpIpReassTimeout() is None

    def test_round_trip_full_through_ipv4_props_dispatch(self):
        """The upgraded Ipv4Props dispatch fully round-trips the FRAGMENTATION-PROPS child."""
        ipv4_props = Ipv4Props()
        ipv4_props.setFragmentationProps(_full_ipv4_fragmentation_props())
        parent = ET.Element("PARENT")
        ARXMLWriter().writeIpv4Props(parent, ipv4_props)

        fragmentation_props_element = parent.find("IPV-4-PROPS/FRAGMENTATION-PROPS")
        xml_text = ET.tostring(parent.find("IPV-4-PROPS"), encoding="unicode")
        namespaced = ET.fromstring(xml_text.replace("IPV-4-PROPS", "IPV-4-PROPS xmlns='%s'" % NS, 1))

        assert fragmentation_props_element.find("TCP-IP-IP-FRAGMENTATION-RX-ENABLED").text == "true"
        assert fragmentation_props_element.find("TCP-IP-IP-NUM-FRAGMENTS").text == "8"
        assert fragmentation_props_element.find("TCP-IP-IP-NUM-REASS-DGRAMS").text == "4"
        assert fragmentation_props_element.find("TCP-IP-IP-REASS-TIMEOUT").text == "15.0"

        reloaded = Ipv4Props()
        ARXMLParser().readIpv4Props(namespaced, reloaded)
        reloaded_fragmentation = reloaded.getFragmentationProps()
        assert isinstance(reloaded_fragmentation, Ipv4FragmentationProps)
        assert reloaded_fragmentation.getTcpIpIpFragmentationRxEnabled().getValue() is True
        assert reloaded_fragmentation.getTcpIpIpNumFragments().getValue() == 8
        assert reloaded_fragmentation.getTcpIpIpNumReassDgrams().getValue() == 4
        assert reloaded_fragmentation.getTcpIpIpReassTimeout().getValue() == 15.0

    def test_save_reload_round_trip_preserves_all_values(self, tmp_path):
        document = AUTOSAR.getInstance()
        document.setARRelease("R23-11")
        pkg = document.createARPackage("Pkg")
        eth_ip_props = pkg.createEthIpProps("IpProps")
        ipv4_props = Ipv4Props()
        ipv4_props.setFragmentationProps(_full_ipv4_fragmentation_props())
        eth_ip_props.setIpv4Props(ipv4_props)

        out_file = str(tmp_path / "ipv4_fragmentation_props.arxml")
        ARXMLWriter().save(out_file, document)

        reloaded_document = AUTOSAR.getInstance()
        reloaded_document.setARRelease("R23-11")
        ARXMLParser().load(out_file, reloaded_document)

        reloaded_pkg = reloaded_document.getARPackages()[0]
        reloaded_eth_ip_props = [e for e in reloaded_pkg.getReferrableElements() if e.getShortName() == "IpProps"][0]
        reloaded_fragmentation = reloaded_eth_ip_props.getIpv4Props().getFragmentationProps()
        assert isinstance(reloaded_fragmentation, Ipv4FragmentationProps)
        assert reloaded_fragmentation.getTcpIpIpFragmentationRxEnabled().getValue() is True
        assert reloaded_fragmentation.getTcpIpIpNumFragments().getValue() == 8
        assert reloaded_fragmentation.getTcpIpIpNumReassDgrams().getValue() == 4
        assert reloaded_fragmentation.getTcpIpIpReassTimeout().getValue() == 15.0
