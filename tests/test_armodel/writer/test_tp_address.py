"""Writer round-trip tests for TpAddress (Table 6.238, p.588).

Serialized through the TP-ADDRESSS wrapper when aggregated by a TpConfig
(XSD group TP-ADDRESS, AUTOSAR_00052.xsd l.125063: TP-ADDRESS INTEGER,
then VARIATION-POINT — emitted by writeIdentifiable when set).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Integer
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols import LinTpConfig, TpAddress
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


def _int(value):
    integer = Integer()
    integer.setValue(str(value))
    return integer


def _with_ns(parent: ET.Element) -> ET.Element:
    return ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))


class TestWriteTpAddress:
    def test_none(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeTpAddress(parent, None)
        assert len(parent) == 0

    def test_empty(self):
        address = TpAddress(MockParent(), "Addr")
        parent = ET.Element("PARENT")
        ARXMLWriter().writeTpAddress(parent, address)

        node = parent.find("TP-ADDRESS")
        assert node is not None
        assert node.find("SHORT-NAME").text == "Addr"
        assert node.find("TP-ADDRESS") is None
        assert node.find("VARIATION-POINT") is None

    def test_full(self):
        address = TpAddress(MockParent(), "Addr")
        address.setTpAddress(_int(2047))
        parent = ET.Element("PARENT")
        ARXMLWriter().writeTpAddress(parent, address)

        node = parent.find("TP-ADDRESS")
        assert node is not None
        assert node.find("SHORT-NAME").text == "Addr"
        assert node.find("TP-ADDRESS").text == "2047"

    def test_round_trip(self):
        address = TpAddress(MockParent(), "Addr")
        address.setTpAddress(_int(2047))
        parent = ET.Element("PARENT")
        ARXMLWriter().writeTpAddress(parent, address)

        reloaded = TpAddress(MockParent(), "Addr")
        ARXMLParser().readTpAddress(_with_ns(parent)[0], reloaded)
        assert reloaded.getTpAddress().getValue() == 2047


class TestWriteLinTpConfigTpAddressesRoundTrip:
    def test_full_round_trip(self):
        config = LinTpConfig(MockParent(), "LinTp")
        addr1 = config.createTpAddress("Addr1")
        addr1.setTpAddress(_int(1))
        addr2 = config.createTpAddress("Addr2")
        addr2.setTpAddress(_int(2))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeLinTpConfigTpAddresses(parent, config)

        wrapper = parent.find("TP-ADDRESSS")
        assert wrapper is not None
        nodes = wrapper.findall("TP-ADDRESS")
        assert len(nodes) == 2
        assert nodes[0].find("SHORT-NAME").text == "Addr1"
        assert nodes[0].find("TP-ADDRESS").text == "1"
        assert nodes[1].find("SHORT-NAME").text == "Addr2"
        assert nodes[1].find("TP-ADDRESS").text == "2"

        reloaded = LinTpConfig(MockParent(), "LinTp")
        ARXMLParser().readLinTpConfigTpAddresses(_with_ns(parent), reloaded)
        addresses = reloaded.getTpAddresses()
        assert len(addresses) == 2
        assert addresses[0].getShortName() == "Addr1"
        assert addresses[0].getTpAddress().getValue() == 1
        assert addresses[1].getShortName() == "Addr2"
        assert addresses[1].getTpAddress().getValue() == 2
