"""Tests for the readDoIpLogicAddress handler (R23-11 DoIpLogicAddress, Table 6.207, p.555)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DoIP import DoIpLogicTargetAddressProps, DoIpLogicTesterAddressProps
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
    package = AUTOSAR.getInstance().createARPackage("DoIpLogicAddresses")
    return DoIpLogicAddress(package, "LogicAddress1")


class TestReadDoIpLogicAddress:
    """Tests for readDoIpLogicAddress handler (R23-11 DoIpLogicAddress, Table 6.207, p.555)."""

    def test_read_doip_logic_address_full_with_target_props(self, parser):
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
        assert address.getShortName() == "LogicAddress1"
        assert address.getAddress().getValue() == 2048
        props = address.getDoIpLogicAddressProps()
        assert isinstance(props, DoIpLogicTargetAddressProps)
        assert props.getShortName() == "TargetProps1"

    def test_read_doip_logic_address_tester_props_with_refs(self, parser):
        element = _snip(
            """
                <SHORT-NAME>LogicAddress1</SHORT-NAME>
                <ADDRESS>4096</ADDRESS>
                <DO-IP-LOGIC-ADDRESS-PROPS>
                    <DO-IP-LOGIC-TESTER-ADDRESS-PROPS>
                        <SHORT-NAME>TesterProps1</SHORT-NAME>
                        <DO-IP-TESTER-ROUTING-ACTIVATION-REFS>
                            <DO-IP-TESTER-ROUTING-ACTIVATION-REF DEST="DO-IP-ROUTING-ACTIVATION">/DoIp/RoutingActivation1</DO-IP-TESTER-ROUTING-ACTIVATION-REF>
                            <DO-IP-TESTER-ROUTING-ACTIVATION-REF DEST="DO-IP-ROUTING-ACTIVATION">/DoIp/RoutingActivation2</DO-IP-TESTER-ROUTING-ACTIVATION-REF>
                        </DO-IP-TESTER-ROUTING-ACTIVATION-REFS>
                    </DO-IP-LOGIC-TESTER-ADDRESS-PROPS>
                </DO-IP-LOGIC-ADDRESS-PROPS>
            """,
            root_tag="DO-IP-LOGIC-ADDRESS",
        )
        address = _address()
        parser.readDoIpLogicAddress(element, address)
        assert address.getAddress().getValue() == 4096
        props = address.getDoIpLogicAddressProps()
        assert isinstance(props, DoIpLogicTesterAddressProps)
        assert props.getShortName() == "TesterProps1"
        refs = props.getDoIpTesterRoutingActivationRefs()
        assert len(refs) == 2
        assert refs[0].getValue() == "/DoIp/RoutingActivation1"
        assert refs[0].getDest() == "DO-IP-ROUTING-ACTIVATION"
        assert refs[1].getValue() == "/DoIp/RoutingActivation2"

    def test_read_doip_logic_address_empty(self, parser):
        element = _snip(
            """
                <SHORT-NAME>LogicAddress1</SHORT-NAME>
            """,
            root_tag="DO-IP-LOGIC-ADDRESS",
        )
        address = _address()
        parser.readDoIpLogicAddress(element, address)
        assert address.getAddress() is None
        assert address.getDoIpLogicAddressProps() is None
