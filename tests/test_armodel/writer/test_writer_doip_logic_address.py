"""Tests for the writeDoIpLogicAddress handler (R23-11 DoIpLogicAddress, Table 6.207, p.555)."""

import xml.etree.cElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger
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


class TestWriteDoIpLogicAddress:
    """Tests for the writeDoIpLogicAddress handler (R23-11 DoIpLogicAddress, Table 6.207, p.555)."""

    def test_write_full_in_xsd_order(self, writer):
        package = AUTOSAR.getInstance().createARPackage("DoIpPkg")
        address = DoIpLogicAddress(package, "LogicAddress1")
        address.setAddress(_positive_integer("2048"))
        address.createDoIpLogicTesterAddressProps("TesterProps1")

        parent = _parent()
        writer.writeDoIpLogicAddress(parent, address)
        child = parent.find("DO-IP-LOGIC-ADDRESS")
        assert child is not None
        child_tags = [element.tag for element in child]
        assert child_tags == ["SHORT-NAME", "ADDRESS", "DO-IP-LOGIC-ADDRESS-PROPS"]
        assert child.find("ADDRESS").text == "2048"
        assert child.find("DO-IP-LOGIC-ADDRESS-PROPS/DO-IP-LOGIC-TESTER-ADDRESS-PROPS/SHORT-NAME").text == "TesterProps1"

    def test_write_empty_address_omits_optional_elements(self, writer):
        package = AUTOSAR.getInstance().createARPackage("DoIpPkg")
        address = DoIpLogicAddress(package, "LogicAddress1")

        parent = _parent()
        writer.writeDoIpLogicAddress(parent, address)
        child = parent.find("DO-IP-LOGIC-ADDRESS")
        assert child is not None
        assert child.find("SHORT-NAME").text == "LogicAddress1"
        assert child.find("ADDRESS") is None
        assert child.find("DO-IP-LOGIC-ADDRESS-PROPS") is None

    def test_round_trip_target_props(self, writer, parser):
        package = AUTOSAR.getInstance().createARPackage("DoIpPkg")
        address = DoIpLogicAddress(package, "LogicAddress1")
        address.setAddress(_positive_integer("2048"))
        address.createDoIpLogicTargetAddressProps("TargetProps1")

        parent = _parent()
        writer.writeDoIpLogicAddress(parent, address)
        element = ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))

        package2 = AUTOSAR.getInstance().createARPackage("DoIpPkg2")
        reparsed = DoIpLogicAddress(package2, "LogicAddress1")
        parser.readDoIpLogicAddress(parser.find(element, "DO-IP-LOGIC-ADDRESS"), reparsed)
        assert reparsed.getAddress().getValue() == 2048
        props = reparsed.getDoIpLogicAddressProps()
        assert props.getShortName() == "TargetProps1"
