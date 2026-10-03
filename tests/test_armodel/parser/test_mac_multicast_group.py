"""
Reader tests for the MacMulticastGroup child of EthernetCluster (AUTOSAR_CP_TPS_SystemTemplate,
Table 3.48, p.104).

macMulticastAddress is spec type MacAddressString (0..1, attr): the reader must materialize
a MacAddressString, not the generic ARLiteral (Rule 0013.2).

Round-trip counterpart: the writer keeps setChildElementOptionalLiteral, which accepts
ARLiteral subclasses.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import MacAddressString
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import MacMulticastGroup
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str) -> ET.Element:
    return ET.fromstring(f"<MAC-MULTICAST-GROUP xmlns='{NS}'>{inner}</MAC-MULTICAST-GROUP>")


def _group() -> MacMulticastGroup:
    return MacMulticastGroup(AUTOSAR.getInstance().createARPackage("AUTOSAR"), "Group1")


class TestReadMacMulticastGroup:
    def test_read_mac_multicast_address_typed(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip("<SHORT-NAME>Group1</SHORT-NAME>" "<MAC-MULTICAST-ADDRESS>01:80:C2:00:00:0E</MAC-MULTICAST-ADDRESS>")
        group = _group()
        parser.readMacMulticastGroup(element, group)

        address = group.getMacMulticastAddress()
        assert isinstance(address, MacAddressString)
        assert address.getValue() == "01:80:C2:00:00:0E"

    def test_read_absent_mac_multicast_address(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip("<SHORT-NAME>Group1</SHORT-NAME>")
        group = _group()
        parser.readMacMulticastGroup(element, group)

        assert group.getMacMulticastAddress() is None

    def test_read_empty_mac_multicast_group_element(self):
        parser = ARXMLParser(options={"warning": True})
        element = ET.fromstring(f"<MAC-MULTICAST-GROUP xmlns='{NS}'/>")
        group = _group()
        parser.readMacMulticastGroup(element, group)

        assert group.getMacMulticastAddress() is None
