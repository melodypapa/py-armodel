"""Tests for the readDoIpLogicAddressProps handler (R23-11 DoIpLogicTargetAddressProps, Table 6.209, p.556)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DoIP import DoIpLogicTargetAddressProps
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols import DoIpLogicAddress
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test and pin the R23-11 release."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def parser():
    """Fresh ARXMLParser instance running in strict mode."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    return ARXMLParser()


def _snip(inner: str, root_tag: str = "ROOT") -> ET.Element:
    """Wrap an inner XML fragment in a root element bound to the AUTOSAR NS."""
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


def _address() -> DoIpLogicAddress:
    package = AUTOSAR.getInstance().createARPackage("DoIpPkg")
    return DoIpLogicAddress(package, "LogicAddress1")


class TestReadDoIpLogicAddressProps:
    """Tests for the DO-IP-LOGIC-ADDRESS-PROPS dispatch of readDoIpLogicAddress."""

    def test_read_target_address_props(self, parser):
        element = _snip(
            """
                <SHORT-NAME>LogicAddress1</SHORT-NAME>
                <ADDRESS>2048</ADDRESS>
                <DO-IP-LOGIC-ADDRESS-PROPS>
                    <DO-IP-LOGIC-TARGET-ADDRESS-PROPS>
                        <SHORT-NAME>TargetProps1</SHORT-NAME>
                    </DO-IP-LOGIC-TARGET-ADDRESS-PROPS>
                </DO-IP-LOGIC-ADDRESS-PROPS>
            """,
            root_tag="DO-IP-LOGIC-ADDRESS",
        )
        address = _address()
        parser.readDoIpLogicAddress(element, address)
        assert address.getAddress().getValue() == 2048
        props = address.getDoIpLogicAddressProps()
        assert isinstance(props, DoIpLogicTargetAddressProps)
        assert props.getShortName() == "TargetProps1"

    def test_read_without_props(self, parser):
        element = _snip(
            """
                <SHORT-NAME>LogicAddress1</SHORT-NAME>
                <ADDRESS>2048</ADDRESS>
            """,
            root_tag="DO-IP-LOGIC-ADDRESS",
        )
        address = _address()
        parser.readDoIpLogicAddress(element, address)
        assert address.getDoIpLogicAddressProps() is None
