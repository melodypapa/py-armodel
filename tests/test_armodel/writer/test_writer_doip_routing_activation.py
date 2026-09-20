"""Tests for the writeDoIpRoutingActivation handler (R23-11 DoIpRoutingActivation, Table 6.204, p.553)."""

import xml.etree.cElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DoIP import DoIpRoutingActivation
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def writer():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    return ARXMLWriter()


def _parent():
    return ET.Element("PARENT")


def _ref(value, dest=None):
    ref = RefType()
    ref.setValue(value)
    if dest is not None:
        ref.setDest(dest)
    return ref


def _activation(short_name: str) -> DoIpRoutingActivation:
    parent = AUTOSAR.getInstance().createARPackage("DoIpRoutingActivationPkg")
    return DoIpRoutingActivation(parent, short_name)


class TestWriteDoIpRoutingActivation:
    """Tests for writeDoIpRoutingActivation handler (R23-11 DoIpRoutingActivation, Table 6.204, p.553)."""

    def test_children_in_xsd_order(self, writer):
        activation = _activation("Activation1")
        activation.addDoIpTargetAddressRef(_ref("/DoIp/TargetAddress1", "DO-IP-LOGIC-TARGET-ADDRESS-PROPS"))
        activation.addDoIpTargetAddressRef(_ref("/DoIp/TargetAddress2", "DO-IP-LOGIC-TARGET-ADDRESS-PROPS"))

        parent = _parent()
        writer.writeDoIpRoutingActivation(parent, activation)
        child = parent.find("DO-IP-ROUTING-ACTIVATION")
        assert child is not None
        assert child.find("SHORT-NAME").text == "Activation1"
        refs_wrapper = child.find("DO-IP-TARGET-ADDRESS-REFS")
        assert refs_wrapper is not None
        ref_tags = refs_wrapper.findall("DO-IP-TARGET-ADDRESS-REF")
        assert len(ref_tags) == 2
        assert ref_tags[0].text == "/DoIp/TargetAddress1"
        assert ref_tags[0].get("DEST") == "DO-IP-LOGIC-TARGET-ADDRESS-PROPS"
        assert ref_tags[1].text == "/DoIp/TargetAddress2"
        assert ref_tags[1].get("DEST") == "DO-IP-LOGIC-TARGET-ADDRESS-PROPS"

    def test_empty_children_omitted(self, writer):
        activation = _activation("Activation1")
        parent = _parent()
        writer.writeDoIpRoutingActivation(parent, activation)
        child = parent.find("DO-IP-ROUTING-ACTIVATION")
        assert child is not None
        assert child.find("DO-IP-TARGET-ADDRESS-REFS") is None
