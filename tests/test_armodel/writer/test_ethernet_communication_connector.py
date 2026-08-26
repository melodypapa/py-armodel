"""Writer/reader round-trip tests for EthernetCommunicationConnector (Table 3.62, p.117)."""

import xml.etree.cElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, PositiveInteger, RefType, TimeValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import EthernetCommunicationConnector
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def writer():
    AUTOSAR.getInstance().new()
    return ARXMLWriter()


@pytest.fixture
def parser():
    AUTOSAR.getInstance().new()
    return ARXMLParser()


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


def _ref(value):
    ref = RefType()
    ref.setValue(value)
    return ref


def _pos_int(text):
    val = PositiveInteger()
    val.setValue(text)
    return val


def _bool(value):
    b = Boolean()
    b.setValue(value)
    return b


def _timeout():
    t = TimeValue()
    t.setValue(30)
    return t


def _full_connector():
    connector = EthernetCommunicationConnector(MockParent(), "ECCONN1")
    connector.setEthIpPropsRef(_ref("/Ecu/EthIpProps/IP1"))
    connector.setMaximumTransmissionUnit(_pos_int("1500"))
    connector.setNeighborCacheSize(_pos_int("50"))
    connector.setPathMtuEnabled(_bool("true"))
    connector.setPathMtuTimeout(_timeout())
    return connector


class TestWriteEthernetCommunicationConnector:
    def test_write_all_fields(self, writer):
        parent = ET.Element("PARENT")
        writer.writeEthernetCommunicationConnector(parent, _full_connector())

        assert parent.find("ETH-IP-PROPS-REF").text == "/Ecu/EthIpProps/IP1"
        assert parent.find("MAXIMUM-TRANSMISSION-UNIT").text == "1500"
        assert parent.find("NEIGHBOR-CACHE-SIZE").text == "50"
        assert parent.find("PATH-MTU-ENABLED").text == "true"
        assert float(parent.find("PATH-MTU-TIMEOUT").text) == 30.0

    def test_write_empty_fields_omits_optional_tags(self, writer):
        parent = ET.Element("PARENT")
        writer.writeEthernetCommunicationConnector(parent, EthernetCommunicationConnector(MockParent(), "Empty"))
        assert parent.find("ETH-IP-PROPS-REF") is None
        assert parent.find("MAXIMUM-TRANSMISSION-UNIT") is None
        assert parent.find("NEIGHBOR-CACHE-SIZE") is None
        assert parent.find("PATH-MTU-ENABLED") is None
        assert parent.find("PATH-MTU-TIMEOUT") is None


class TestEthernetCommunicationConnectorRoundTrip:
    def test_round_trip_preserves_all_values(self, writer, parser, tmp_path):
        parent = ET.Element("PARENT")
        writer.writeEthernetCommunicationConnector(parent, _full_connector())

        out_file = str(tmp_path / "ecc_conn.arxml")
        with open(out_file, "w", encoding="utf-8") as f:
            inner = ET.tostring(parent).decode("utf-8")
            f.write("<AUTOSAR xmlns='%s'>%s</AUTOSAR>" % (NS, inner))

        tree = ET.parse(out_file)
        recovered = EthernetCommunicationConnector(MockParent(), "ECCONN1")
        parser.readEthernetCommunicationConnector(tree.getroot()[0], recovered)

        assert isinstance(recovered, EthernetCommunicationConnector)
        assert recovered.getEthIpPropsRef().getValue() == "/Ecu/EthIpProps/IP1"
        assert recovered.getMaximumTransmissionUnit().getValue() == 1500
        assert recovered.getNeighborCacheSize().getValue() == 50
        assert recovered.getPathMtuEnabled().getValue() is True
        assert recovered.getPathMtuTimeout().getValue() == 30

    def test_reader_empty_fields(self, parser):
        element = ET.fromstring("<ETHERNET-COMMUNICATION-CONNECTOR xmlns='%s'><SHORT-NAME>Empty</SHORT-NAME></ETHERNET-COMMUNICATION-CONNECTOR>" % NS)
        recovered = EthernetCommunicationConnector(MockParent(), "Empty")
        parser.readEthernetCommunicationConnector(element, recovered)

        assert recovered.getEthIpPropsRef() is None
        assert recovered.getMaximumTransmissionUnit() is None
        assert recovered.getNeighborCacheSize() is None
        assert recovered.getPathMtuEnabled() is None
        assert recovered.getPathMtuTimeout() is None
