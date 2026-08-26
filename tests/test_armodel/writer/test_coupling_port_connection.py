"""Writer/reader round-trip tests for CouplingPortConnection (Table 3.60, p.113)."""

import xml.etree.cElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    CouplingPortConnection,
)
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


def _new_connection():
    connection = CouplingPortConnection()
    connection.setFirstPort(_ref("/Ether/CouplingPort/CP1"))
    connection.addNodePort(_ref("/Ether/CouplingPort/CP3"))
    connection.addNodePort(_ref("/Ether/CouplingPort/CP4"))
    connection.setPlcaLocalNodeCount(_pos_int("4"))
    connection.setPlcaTransmitOpportunityTimer(_pos_int("100"))
    connection.setSecondPort(_ref("/Ether/CouplingPort/CP2"))
    return connection


class TestWriteCouplingPortConnection:
    def test_write_all_fields(self, writer):
        parent = ET.Element("PARENT")
        writer.writeCouplingPortConnection(parent, _new_connection())

        node = parent.find("COUPLING-PORT-CONNECTION")
        assert node is not None
        assert node.find("FIRST-PORT-REF").text == "/Ether/CouplingPort/CP1"
        node_ports = node.findall("NODE-PORTS/COUPLING-PORT-REF-CONDITIONAL/COUPLING-PORT-REF")
        assert len(node_ports) == 2
        assert node.find("PLCA-LOCAL-NODE-COUNT").text == "4"
        assert node.find("PLCA-TRANSMIT-OPPORTUNITY-TIMER").text == "100"
        assert node.find("SECOND-PORT-REF").text == "/Ether/CouplingPort/CP2"


class TestCouplingPortConnectionRoundTrip:
    def test_round_trip_preserves_all_values(self, writer, parser, tmp_path):
        parent = ET.Element("PARENT")
        writer.writeCouplingPortConnection(parent, _new_connection())

        out_file = str(tmp_path / "coupling_port_connection.arxml")
        with open(out_file, "w", encoding="utf-8") as f:
            f.write(ET.tostring(_wrap(parent), encoding="unicode"))

        tree = ET.parse(out_file)
        recovered = CouplingPortConnection()
        parser.readCouplingPortConnection(tree.getroot()[0][0], recovered)

        assert recovered.getFirstPort().getValue() == "/Ether/CouplingPort/CP1"
        assert [r.getValue() for r in recovered.getNodePorts()] == ["/Ether/CouplingPort/CP3", "/Ether/CouplingPort/CP4"]
        assert recovered.getPlcaLocalNodeCount().getValue() == 4
        assert recovered.getPlcaTransmitOpportunityTimer().getValue() == 100
        assert recovered.getSecondPort().getValue() == "/Ether/CouplingPort/CP2"

    def test_reader_empty_fields(self, parser):
        element = ET.fromstring("<COUPLING-PORT-CONNECTION xmlns='%s'></COUPLING-PORT-CONNECTION>" % NS)
        recovered = CouplingPortConnection()
        parser.readCouplingPortConnection(element, recovered)

        assert recovered.getFirstPort() is None
        assert recovered.getNodePorts() == []
        assert recovered.getPlcaLocalNodeCount() is None
        assert recovered.getPlcaTransmitOpportunityTimer() is None
        assert recovered.getSecondPort() is None


def _wrap(element: ET.Element) -> ET.Element:
    inner = ET.tostring(element).decode("utf-8")
    return ET.fromstring(f"<AUTOSAR xmlns='{NS}'>{inner}</AUTOSAR>")
