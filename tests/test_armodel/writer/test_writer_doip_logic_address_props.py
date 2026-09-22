"""Tests for the writeDoIpLogicAddressProps handler (R23-11 DoIpLogicTargetAddressProps Table 6.209 p.556, DoIpLogicTesterAddressProps Table 6.210 p.557)."""

import xml.etree.cElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DoIP import DoIpLogicTargetAddressProps, DoIpLogicTesterAddressProps
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols import DoIpLogicAddress
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


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


@pytest.fixture
def parser():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    return ARXMLParser()


def _parent():
    return ET.Element("PARENT")


def _positive_integer(value):
    integer = PositiveInteger()
    integer.setValue(value)
    return integer


def _filled_address() -> DoIpLogicAddress:
    package = AUTOSAR.getInstance().createARPackage("DoIpPkg")
    address = DoIpLogicAddress(package, "LogicAddress1")
    address.setAddress(_positive_integer("2048"))
    props = DoIpLogicTargetAddressProps(address, "TargetProps1")
    address.setDoIpLogicAddressProps(props)
    return address


def _ref(value, dest=None):
    ref = RefType()
    ref.setValue(value)
    if dest is not None:
        ref.setDest(dest)
    return ref


def _filled_tester_address() -> DoIpLogicAddress:
    package = AUTOSAR.getInstance().createARPackage("DoIpPkg")
    address = DoIpLogicAddress(package, "LogicAddress1")
    address.setAddress(_positive_integer("4096"))
    props = DoIpLogicTesterAddressProps(address, "TesterProps1")
    props.addDoIpTesterRoutingActivationRef(_ref("/DoIp/DoIpRoutingActivation1", "DO-IP-ROUTING-ACTIVATION"))
    props.addDoIpTesterRoutingActivationRef(_ref("/DoIp/DoIpRoutingActivation2", "DO-IP-ROUTING-ACTIVATION"))
    address.setDoIpLogicAddressProps(props)
    return address


class TestWriteDoIpLogicAddressProps:
    """Tests for the DO-IP-LOGIC-ADDRESS-PROPS handling of writeDoIpLogicAddress."""

    def test_write_target_address_props_in_xsd_order(self, writer):
        address = _filled_address()

        parent = _parent()
        writer.writeDoIpLogicAddress(parent, address)
        child = parent.find("DO-IP-LOGIC-ADDRESS")
        assert child is not None
        child_tags = [element.tag for element in child]
        assert child_tags == ["SHORT-NAME", "ADDRESS", "DO-IP-LOGIC-ADDRESS-PROPS"]
        assert child.find("ADDRESS").text == "2048"
        props_element = child.find("DO-IP-LOGIC-ADDRESS-PROPS/DO-IP-LOGIC-TARGET-ADDRESS-PROPS")
        assert props_element is not None
        assert props_element.find("SHORT-NAME").text == "TargetProps1"

    def test_write_without_props_omits_element(self, writer):
        package = AUTOSAR.getInstance().createARPackage("DoIpPkg")
        address = DoIpLogicAddress(package, "LogicAddress1")

        parent = _parent()
        writer.writeDoIpLogicAddress(parent, address)
        child = parent.find("DO-IP-LOGIC-ADDRESS")
        assert child.find("DO-IP-LOGIC-ADDRESS-PROPS") is None

    def test_round_trip_target_address_props(self, writer, parser):
        address = _filled_address()

        parent = _parent()
        writer.writeDoIpLogicAddress(parent, address)
        element = ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))

        package = AUTOSAR.getInstance().createARPackage("DoIpPkg2")
        reparsed = DoIpLogicAddress(package, "LogicAddress1")
        parser.readDoIpLogicAddress(parser.find(element, "DO-IP-LOGIC-ADDRESS"), reparsed)
        assert reparsed.getAddress().getValue() == 2048
        props = reparsed.getDoIpLogicAddressProps()
        assert isinstance(props, DoIpLogicTargetAddressProps)
        assert props.getShortName() == "TargetProps1"

    def test_write_tester_address_props_in_xsd_order(self, writer):
        address = _filled_tester_address()

        parent = _parent()
        writer.writeDoIpLogicAddress(parent, address)
        child = parent.find("DO-IP-LOGIC-ADDRESS")
        assert child is not None
        child_tags = [element.tag for element in child]
        assert child_tags == ["SHORT-NAME", "ADDRESS", "DO-IP-LOGIC-ADDRESS-PROPS"]
        props_element = child.find("DO-IP-LOGIC-ADDRESS-PROPS/DO-IP-LOGIC-TESTER-ADDRESS-PROPS")
        assert props_element is not None
        assert props_element.find("SHORT-NAME").text == "TesterProps1"
        child_tags = [element.tag for element in props_element]
        assert child_tags == ["SHORT-NAME", "DO-IP-TESTER-ROUTING-ACTIVATION-REFS"]
        refs = props_element.findall("DO-IP-TESTER-ROUTING-ACTIVATION-REFS/DO-IP-TESTER-ROUTING-ACTIVATION-REF")
        assert len(refs) == 2
        assert refs[0].text == "/DoIp/DoIpRoutingActivation1"
        assert refs[0].get("DEST") == "DO-IP-ROUTING-ACTIVATION"
        assert refs[1].text == "/DoIp/DoIpRoutingActivation2"

    def test_write_tester_address_props_without_refs_omits_wrapper(self, writer):
        package = AUTOSAR.getInstance().createARPackage("DoIpPkg")
        address = DoIpLogicAddress(package, "LogicAddress1")
        props = DoIpLogicTesterAddressProps(address, "TesterProps1")
        address.setDoIpLogicAddressProps(props)

        parent = _parent()
        writer.writeDoIpLogicAddress(parent, address)
        props_element = parent.find("DO-IP-LOGIC-ADDRESS/DO-IP-LOGIC-ADDRESS-PROPS/DO-IP-LOGIC-TESTER-ADDRESS-PROPS")
        assert props_element is not None
        assert props_element.find("DO-IP-TESTER-ROUTING-ACTIVATION-REFS") is None

    def test_round_trip_tester_address_props(self, writer, parser):
        address = _filled_tester_address()

        parent = _parent()
        writer.writeDoIpLogicAddress(parent, address)
        element = ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))

        package = AUTOSAR.getInstance().createARPackage("DoIpPkg2")
        reparsed = DoIpLogicAddress(package, "LogicAddress1")
        parser.readDoIpLogicAddress(parser.find(element, "DO-IP-LOGIC-ADDRESS"), reparsed)
        assert reparsed.getAddress().getValue() == 4096
        props = reparsed.getDoIpLogicAddressProps()
        assert isinstance(props, DoIpLogicTesterAddressProps)
        assert props.getShortName() == "TesterProps1"
        refs = props.getDoIpTesterRoutingActivationRefs()
        assert len(refs) == 2
        assert refs[0].getValue() == "/DoIp/DoIpRoutingActivation1"
        assert refs[0].getDest() == "DO-IP-ROUTING-ACTIVATION"
        assert refs[1].getValue() == "/DoIp/DoIpRoutingActivation2"
