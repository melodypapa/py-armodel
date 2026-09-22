"""Tests for the readDoIpLogicAddressProps handler (R23-11 DoIpLogicTargetAddressProps Table 6.209 p.556, DoIpLogicTesterAddressProps Table 6.210 p.557)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DoIP import (
    DoIpLogicTargetAddressProps,
    DoIpLogicTesterAddressProps,
)
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

    def test_read_tester_address_props(self, parser):
        element = _snip(
            """
                <SHORT-NAME>LogicAddress1</SHORT-NAME>
                <ADDRESS>2048</ADDRESS>
                <DO-IP-LOGIC-ADDRESS-PROPS>
                    <DO-IP-LOGIC-TESTER-ADDRESS-PROPS>
                        <SHORT-NAME>TesterProps1</SHORT-NAME>
                        <DO-IP-TESTER-ROUTING-ACTIVATION-REFS>
                            <DO-IP-TESTER-ROUTING-ACTIVATION-REF DEST="DO-IP-ROUTING-ACTIVATION">/DoIp/DoIpRoutingActivation1</DO-IP-TESTER-ROUTING-ACTIVATION-REF>
                            <DO-IP-TESTER-ROUTING-ACTIVATION-REF DEST="DO-IP-ROUTING-ACTIVATION">/DoIp/DoIpRoutingActivation2</DO-IP-TESTER-ROUTING-ACTIVATION-REF>
                        </DO-IP-TESTER-ROUTING-ACTIVATION-REFS>
                    </DO-IP-LOGIC-TESTER-ADDRESS-PROPS>
                </DO-IP-LOGIC-ADDRESS-PROPS>
            """,
            root_tag="DO-IP-LOGIC-ADDRESS",
        )
        address = _address()
        parser.readDoIpLogicAddress(element, address)
        props = address.getDoIpLogicAddressProps()
        assert isinstance(props, DoIpLogicTesterAddressProps)
        assert props.getShortName() == "TesterProps1"
        refs = props.getDoIpTesterRoutingActivationRefs()
        assert len(refs) == 2
        assert refs[0].getValue() == "/DoIp/DoIpRoutingActivation1"
        assert refs[0].getDest() == "DO-IP-ROUTING-ACTIVATION"
        assert refs[1].getValue() == "/DoIp/DoIpRoutingActivation2"

    def test_read_tester_address_props_without_refs(self, parser):
        element = _snip(
            """
                <DO-IP-LOGIC-ADDRESS-PROPS>
                    <DO-IP-LOGIC-TESTER-ADDRESS-PROPS>
                        <SHORT-NAME>TesterProps1</SHORT-NAME>
                    </DO-IP-LOGIC-TESTER-ADDRESS-PROPS>
                </DO-IP-LOGIC-ADDRESS-PROPS>
            """,
            root_tag="DO-IP-LOGIC-ADDRESS",
        )
        address = _address()
        parser.readDoIpLogicAddress(element, address)
        props = address.getDoIpLogicAddressProps()
        assert isinstance(props, DoIpLogicTesterAddressProps)
        assert props.getDoIpTesterRoutingActivationRefs() == []
