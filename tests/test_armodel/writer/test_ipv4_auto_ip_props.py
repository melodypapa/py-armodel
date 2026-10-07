"""
Writer/reader round-trip tests for Ipv4AutoIpProps (Table 3.103, p.147).

XML element order per XSD IPV-4-AUTO-IP-PROPS group: TCP-IP-AUTO-IP-INIT-TIMEOUT
(unwrapped direct child of AUTO-IP-PROPS).
writeIpv4Props dispatches AUTO-IP-PROPS to writeIpv4AutoIpProps since the
Ipv4AutoIpProps sync (Table 3.103) — the child is fully serialized, no longer
identity-only.
writeIpv4AutoIpProps calls writeARObject on the AUTO-IP-PROPS element exactly once.
"""

import xml.etree.cElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import Ipv4AutoIpProps, Ipv4Props
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"

XSD_ORDER = [
    "TCP-IP-AUTO-IP-INIT-TIMEOUT",
]


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _full_ipv4_auto_ip_props():
    props = Ipv4AutoIpProps()
    props.setTcpIpAutoIpInitTimeout(TimeValue().setValue(3.0))
    return props


def _write_ipv4_auto_ip_props(props):
    parent = ET.Element("PARENT")
    ARXMLWriter().writeIpv4AutoIpProps(parent, props)
    return parent


def _namespaced_first_child(parent):
    xml_text = ET.tostring(parent, encoding="unicode")
    namespaced = ET.fromstring(xml_text.replace(parent[0].tag, "%s xmlns='%s'" % (parent[0].tag, NS), 1))
    return namespaced[0]


class TestWriteIpv4AutoIpProps:
    def test_members_in_xsd_order(self):
        parent = _write_ipv4_auto_ip_props(_full_ipv4_auto_ip_props())
        auto_ip_props = parent.find("AUTO-IP-PROPS")

        children = [child.tag for child in auto_ip_props]
        assert children == XSD_ORDER

    def test_members_written_with_field_values(self):
        parent = _write_ipv4_auto_ip_props(_full_ipv4_auto_ip_props())
        auto_ip_props = parent.find("AUTO-IP-PROPS")

        assert auto_ip_props.find("TCP-IP-AUTO-IP-INIT-TIMEOUT").text == "3.0"

    def test_bare_props_emits_no_group_children(self):
        parent = _write_ipv4_auto_ip_props(Ipv4AutoIpProps())
        auto_ip_props = parent.find("AUTO-IP-PROPS")

        assert len(list(auto_ip_props)) == 0

    def test_checksum_emitted(self):
        props = Ipv4AutoIpProps()
        checksum = String()
        checksum.setValue("456")
        props.setChecksum(checksum)
        parent = _write_ipv4_auto_ip_props(props)

        assert parent.find("AUTO-IP-PROPS").attrib.get("S") == "456"


class TestIpv4AutoIpPropsRoundTrip:
    def test_round_trip_full_through_auto_ip_props(self):
        parent = _write_ipv4_auto_ip_props(_full_ipv4_auto_ip_props())
        reloaded = Ipv4AutoIpProps()
        ARXMLParser().readIpv4AutoIpProps(_namespaced_first_child(parent), reloaded)

        assert reloaded.getTcpIpAutoIpInitTimeout().getValue() == 3.0

    def test_round_trip_empty_through_auto_ip_props(self):
        parent = _write_ipv4_auto_ip_props(Ipv4AutoIpProps())
        reloaded = Ipv4AutoIpProps()
        ARXMLParser().readIpv4AutoIpProps(_namespaced_first_child(parent), reloaded)

        assert reloaded.getTcpIpAutoIpInitTimeout() is None

    def test_round_trip_full_through_ipv4_props_dispatch(self):
        """The upgraded Ipv4Props dispatch fully round-trips the AUTO-IP-PROPS child."""
        ipv4_props = Ipv4Props()
        ipv4_props.setAutoIpProps(_full_ipv4_auto_ip_props())
        parent = ET.Element("PARENT")
        ARXMLWriter().writeIpv4Props(parent, ipv4_props)

        auto_ip_props_element = parent.find("IPV-4-PROPS/AUTO-IP-PROPS")
        xml_text = ET.tostring(parent.find("IPV-4-PROPS"), encoding="unicode")
        namespaced = ET.fromstring(xml_text.replace("IPV-4-PROPS", "IPV-4-PROPS xmlns='%s'" % NS, 1))

        assert auto_ip_props_element.find("TCP-IP-AUTO-IP-INIT-TIMEOUT").text == "3.0"

        reloaded = Ipv4Props()
        ARXMLParser().readIpv4Props(namespaced, reloaded)
        reloaded_auto_ip = reloaded.getAutoIpProps()
        assert isinstance(reloaded_auto_ip, Ipv4AutoIpProps)
        assert reloaded_auto_ip.getTcpIpAutoIpInitTimeout().getValue() == 3.0

    def test_save_reload_round_trip_preserves_all_values(self, tmp_path):
        document = AUTOSAR.getInstance()
        document.setARRelease("R23-11")
        pkg = document.createARPackage("Pkg")
        eth_ip_props = pkg.createEthIpProps("IpProps")
        ipv4_props = Ipv4Props()
        ipv4_props.setAutoIpProps(_full_ipv4_auto_ip_props())
        eth_ip_props.setIpv4Props(ipv4_props)

        out_file = str(tmp_path / "ipv4_auto_ip_props.arxml")
        ARXMLWriter().save(out_file, document)

        reloaded_document = AUTOSAR.getInstance()
        reloaded_document.setARRelease("R23-11")
        ARXMLParser().load(out_file, reloaded_document)

        reloaded_pkg = reloaded_document.getARPackages()[0]
        reloaded_eth_ip_props = [e for e in reloaded_pkg.getReferrableElements() if e.getShortName() == "IpProps"][0]
        reloaded_auto_ip = reloaded_eth_ip_props.getIpv4Props().getAutoIpProps()
        assert isinstance(reloaded_auto_ip, Ipv4AutoIpProps)
        assert reloaded_auto_ip.getTcpIpAutoIpInitTimeout().getValue() == 3.0
