"""
Tests for parsing ETH-IP-PROPS elements (EthIpProps, Table 3.100, p.146).

Round-trip counterpart: tests/test_armodel/writer/test_eth_ip_props.py
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import Ipv6Props
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import EthIpProps, Ipv4ArpProps, Ipv4AutoIpProps, Ipv4FragmentationProps, Ipv4Props
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def parser():
    """Create ARXML parser instance."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    return ARXMLParser()


def _make_eth_ip_props() -> EthIpProps:
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    ar_root = AUTOSAR.getInstance().createARPackage("AUTOSAR")
    return ar_root.createEthIpProps("IpProps")


class TestReadEthIpProps:
    """Test readEthIpProps (EthIpProps, Table 3.100)."""

    def test_read_all_members(self, parser):
        """Every ETH-IP-PROPS group element populates its model field."""
        eth_ip_props = _make_eth_ip_props()
        element = ET.fromstring(
            f"""<ETH-IP-PROPS xmlns='{NS}'>
                <SHORT-NAME>IpProps</SHORT-NAME>
                <IPV-4-PROPS/>
                <IPV-6-PROPS/>
            </ETH-IP-PROPS>"""
        )

        parser.readEthIpProps(element, eth_ip_props)

        assert eth_ip_props.getShortName() == "IpProps"
        assert isinstance(eth_ip_props.getIpv4Props(), Ipv4Props)
        assert isinstance(eth_ip_props.getIpv6Props(), Ipv6Props)

    def test_read_identifiable_levels(self, parser):
        """The identifiable levels (CATEGORY etc.) are populated via readIdentifiable."""
        eth_ip_props = _make_eth_ip_props()
        element = ET.fromstring(
            f"""<ETH-IP-PROPS xmlns='{NS}'>
                <SHORT-NAME>IpProps</SHORT-NAME>
                <CATEGORY>myCategory</CATEGORY>
                <IPV-4-PROPS/>
            </ETH-IP-PROPS>"""
        )

        parser.readEthIpProps(element, eth_ip_props)

        assert eth_ip_props.getCategory() is not None
        assert eth_ip_props.getCategory().getValue() == "myCategory"
        assert isinstance(eth_ip_props.getIpv4Props(), Ipv4Props)
        assert eth_ip_props.getIpv6Props() is None

    def test_read_nested_ipv4_props_children(self, parser):
        """The IPV-4-PROPS child dispatches to readIpv4Props (Ipv4Props, Table 3.101)."""
        eth_ip_props = _make_eth_ip_props()
        element = ET.fromstring(
            f"""<ETH-IP-PROPS xmlns='{NS}'>
                <SHORT-NAME>IpProps</SHORT-NAME>
                <IPV-4-PROPS>
                    <ARP-PROPS/>
                    <AUTO-IP-PROPS/>
                    <FRAGMENTATION-PROPS/>
                </IPV-4-PROPS>
            </ETH-IP-PROPS>"""
        )

        parser.readEthIpProps(element, eth_ip_props)

        ipv4_props = eth_ip_props.getIpv4Props()
        assert isinstance(ipv4_props, Ipv4Props)
        assert isinstance(ipv4_props.getArpProps(), Ipv4ArpProps)
        assert isinstance(ipv4_props.getAutoIpProps(), Ipv4AutoIpProps)
        assert isinstance(ipv4_props.getFragmentationProps(), Ipv4FragmentationProps)

    def test_read_absent_optional_members(self, parser):
        """Absent optional members leave the fields untouched (empty case)."""
        eth_ip_props = _make_eth_ip_props()
        element = ET.fromstring(
            f"""<ETH-IP-PROPS xmlns='{NS}'>
                <SHORT-NAME>IpProps</SHORT-NAME>
            </ETH-IP-PROPS>"""
        )

        parser.readEthIpProps(element, eth_ip_props)

        assert eth_ip_props.getIpv4Props() is None
        assert eth_ip_props.getIpv6Props() is None

    def test_load_via_ar_package(self, parser):
        """Test that the ARPackage ELEMENTS dispatch reads an ETH-IP-PROPS."""
        content = f"""<?xml version="1.0" encoding="utf-8"?>
<AUTOSAR xmlns="{NS}" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="{NS} AUTOSAR_00052.xsd">
    <AR-PACKAGES>
        <AR-PACKAGE>
            <SHORT-NAME>AUTOSAR</SHORT-NAME>
            <ELEMENTS>
                <ETH-IP-PROPS>
                    <SHORT-NAME>IpProps</SHORT-NAME>
                    <IPV-4-PROPS/>
                </ETH-IP-PROPS>
            </ELEMENTS>
        </AR-PACKAGE>
    </AR-PACKAGES>
</AUTOSAR>"""
        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)

            document = AUTOSAR.getInstance()
            document.clear()
            parser.load(file_path, document)

            pkg = document.getARPackages()[0]
            eth_ip_props = [e for e in pkg.getReferrableElements() if isinstance(e, EthIpProps)]
            assert len(eth_ip_props) == 1
            assert eth_ip_props[0].getShortName() == "IpProps"
            assert isinstance(eth_ip_props[0].getIpv4Props(), Ipv4Props)
            assert eth_ip_props[0].getIpv6Props() is None
        finally:
            os.remove(file_path)
