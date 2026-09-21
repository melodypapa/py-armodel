"""Tests for the readDoIpRoutingActivation handler (R23-11 DoIpRoutingActivation, Table 6.204, p.553)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DoIP import DoIpRoutingActivation
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


def _activation(short_name: str) -> DoIpRoutingActivation:
    parent = AUTOSAR.getInstance().createARPackage("DoIpRoutingActivationPkg")
    return DoIpRoutingActivation(parent, short_name)


class TestReadDoIpRoutingActivation:
    """Tests for readDoIpRoutingActivation handler (R23-11 DoIpRoutingActivation, Table 6.204, p.553)."""

    def test_read_doip_routing_activation_full(self, parser):
        element = _snip(
            """
                <SHORT-NAME>Activation1</SHORT-NAME>
                <DO-IP-TARGET-ADDRESS-REFS>
                    <DO-IP-TARGET-ADDRESS-REF DEST="DO-IP-LOGIC-TARGET-ADDRESS-PROPS">/DoIp/TargetAddress1</DO-IP-TARGET-ADDRESS-REF>
                    <DO-IP-TARGET-ADDRESS-REF DEST="DO-IP-LOGIC-TARGET-ADDRESS-PROPS">/DoIp/TargetAddress2</DO-IP-TARGET-ADDRESS-REF>
                </DO-IP-TARGET-ADDRESS-REFS>
            """,
            root_tag="DO-IP-ROUTING-ACTIVATION",
        )
        activation = _activation("Activation1")
        parser.readDoIpRoutingActivation(element, activation)
        refs = activation.getDoIpTargetAddressRefs()
        assert len(refs) == 2
        assert refs[0].getValue() == "/DoIp/TargetAddress1"
        assert refs[0].getDest() == "DO-IP-LOGIC-TARGET-ADDRESS-PROPS"
        assert refs[1].getValue() == "/DoIp/TargetAddress2"
        assert refs[1].getDest() == "DO-IP-LOGIC-TARGET-ADDRESS-PROPS"

    def test_read_doip_routing_activation_empty(self, parser):
        element = _snip(
            """
                <SHORT-NAME>Activation1</SHORT-NAME>
            """,
            root_tag="DO-IP-ROUTING-ACTIVATION",
        )
        activation = _activation("Activation1")
        parser.readDoIpRoutingActivation(element, activation)
        assert activation.getDoIpTargetAddressRefs() == []
