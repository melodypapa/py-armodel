"""Parser tests for TpAddress (Table 6.238, p.588).

Identifiable aggregated by FlexrayArTpConfig/FlexrayTpConfig/J1939TpConfig/LinTpConfig
.tpAddress through the TP-ADDRESSS wrapper (XSD group TP-ADDRESS,
AUTOSAR_00052.xsd l.125063: TP-ADDRESS INTEGER, then VARIATION-POINT).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
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


def _snip(inner: str) -> ET.Element:
    xml = "<ROOT xmlns='%s'>%s</ROOT>" % (NS, inner)
    return ET.fromstring(xml)


def _with_ns(parent: ET.Element) -> ET.Element:
    return ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))


class TestReadTpAddress:
    def test_read_full(self):
        address = TpAddress(MockParent(), "DiagAddress")
        root = _snip("<TP-ADDRESS><SHORT-NAME>DiagAddress</SHORT-NAME><TP-ADDRESS>2047</TP-ADDRESS></TP-ADDRESS>")
        ARXMLParser().readTpAddress(root[0], address)

        assert address.getShortName() == "DiagAddress"
        assert address.getTpAddress() is not None
        assert address.getTpAddress().getValue() == 2047

    def test_read_empty(self):
        address = TpAddress(MockParent(), "DiagAddress")
        root = _snip("<TP-ADDRESS><SHORT-NAME>DiagAddress</SHORT-NAME></TP-ADDRESS>")
        ARXMLParser().readTpAddress(root[0], address)

        assert address.getTpAddress() is None

    def test_read_variation_point(self):
        address = TpAddress(MockParent(), "DiagAddress")
        root = _snip("<TP-ADDRESS><SHORT-NAME>DiagAddress</SHORT-NAME><TP-ADDRESS>3</TP-ADDRESS><VARIATION-POINT /></TP-ADDRESS>")
        ARXMLParser().readTpAddress(root[0], address)

        assert address.getVariationPoint() is not None


class TestReadLinTpConfigTpAddresses:
    def test_read_via_lin_tp_config(self):
        config = LinTpConfig(MockParent(), "LinTp")
        root = _snip(
            "<LIN-TP-CONFIG>"
            "<SHORT-NAME>LinTp</SHORT-NAME>"
            "<TP-ADDRESSS>"
            "<TP-ADDRESS><SHORT-NAME>Addr1</SHORT-NAME><TP-ADDRESS>1</TP-ADDRESS></TP-ADDRESS>"
            "<TP-ADDRESS><SHORT-NAME>Addr2</SHORT-NAME><TP-ADDRESS>2</TP-ADDRESS></TP-ADDRESS>"
            "</TP-ADDRESSS>"
            "</LIN-TP-CONFIG>"
        )
        ARXMLParser().readLinTpConfigTpAddresses(root[0], config)

        addresses = config.getTpAddresses()
        assert len(addresses) == 2
        assert addresses[0].getShortName() == "Addr1"
        assert addresses[0].getTpAddress().getValue() == 1
        assert addresses[1].getShortName() == "Addr2"
        assert addresses[1].getTpAddress().getValue() == 2

    def test_round_trip_via_lin_tp_config(self):
        config = LinTpConfig(MockParent(), "LinTp")
        root = _snip(
            "<LIN-TP-CONFIG>"
            "<SHORT-NAME>LinTp</SHORT-NAME>"
            "<TP-ADDRESSS>"
            "<TP-ADDRESS><SHORT-NAME>Addr1</SHORT-NAME><TP-ADDRESS>2047</TP-ADDRESS></TP-ADDRESS>"
            "</TP-ADDRESSS>"
            "</LIN-TP-CONFIG>"
        )
        ARXMLParser().readLinTpConfigTpAddresses(root[0], config)

        written = ET.Element("PARENT")
        ARXMLWriter().writeLinTpConfigTpAddresses(written, config)
        reloaded = LinTpConfig(MockParent(), "LinTp")
        ARXMLParser().readLinTpConfigTpAddresses(_with_ns(written), reloaded)

        addresses = reloaded.getTpAddresses()
        assert len(addresses) == 1
        assert addresses[0].getShortName() == "Addr1"
        assert addresses[0].getTpAddress().getValue() == 2047
