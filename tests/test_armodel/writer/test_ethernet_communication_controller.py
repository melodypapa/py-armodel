"""Writer/reader round-trip tests for EthernetCommunicationController (Table 3.61, p.116)."""

import xml.etree.cElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral, Boolean, Integer, RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    CouplingPort,
    EthernetCommunicationController,
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
    document = AUTOSAR.getInstance()
    document.setARRelease("R23-11")
    return ARXMLWriter()


@pytest.fixture
def parser():
    AUTOSAR.getInstance().new()
    document = AUTOSAR.getInstance()
    document.setARRelease("R23-11")
    return ARXMLParser()


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


def _ref(value):
    ref = RefType()
    ref.setValue(value)
    return ref


def _int(value):
    val = Integer()
    val.setValue(value)
    return val


def _literal(value):
    literal = ARLiteral()
    literal.setValue(value)
    return literal


def _bool(value):
    b = Boolean()
    b.setValue(value)
    return b


def _full_controller():
    controller = EthernetCommunicationController(MockParent(), "ECC1")
    controller.setCanXlConfigRef(_ref("/CanXL/AbstractCanCommController/CAN1"))
    port = controller.createCouplingPort("CP1")
    port.setMacLayerType(_literal("ethernet"))
    controller.setMacLayerType(_literal("ethernet"))
    controller.setMacUnicastAddress(_literal("00:1B:44:11:3A:B7"))
    controller.setMaximumReceiveBufferLength(_int(1500))
    controller.setMaximumTransmitBufferLength(_int(1500))
    controller.setSlaveActAsPassiveCommunicationSlave(_bool("true"))
    return controller


class TestWriteEthernetCommunicationController:
    def test_write_all_fields(self, writer):
        parent = ET.Element("COMM-CONTROLLERS")
        writer.writeEthernetCommunicationController(parent, _full_controller())

        cond = parent.find("ETHERNET-COMMUNICATION-CONTROLLER/ETHERNET-COMMUNICATION-CONTROLLER-VARIANTS/ETHERNET-COMMUNICATION-CONTROLLER-CONDITIONAL")
        assert cond is not None
        assert cond.find("CAN-XL-CONFIG-REF").text == "/CanXL/AbstractCanCommController/CAN1"
        assert cond.find("COUPLING-PORTS/COUPLING-PORT/SHORT-NAME").text == "CP1"
        assert cond.find("MAC-LAYER-TYPE").text == "ethernet"
        assert cond.find("MAC-UNICAST-ADDRESS").text == "00:1B:44:11:3A:B7"
        assert cond.find("MAXIMUM-RECEIVE-BUFFER-LENGTH").text == "1500"
        assert cond.find("MAXIMUM-TRANSMIT-BUFFER-LENGTH").text == "1500"
        assert cond.find("SLAVE-ACT-AS-PASSIVE-COMMUNICATION-SLAVE").text == "true"


class TestEthernetCommunicationControllerRoundTrip:
    def test_round_trip_preserves_all_values(self, writer, parser, tmp_path):
        parent = ET.Element("COMM-CONTROLLERS")
        writer.writeEthernetCommunicationController(parent, _full_controller())

        out_file = str(tmp_path / "ecc.arxml")
        with open(out_file, "w", encoding="utf-8") as f:
            inner = ET.tostring(parent).decode("utf-8")
            f.write("<AUTOSAR xmlns='%s'>%s</AUTOSAR>" % (NS, inner))

        tree = ET.parse(out_file)
        recovered = EthernetCommunicationController(MockParent(), "ECC1")
        parser.readEthernetCommunicationController(tree.getroot()[0][0], recovered)

        assert recovered.getShortName() == "ECC1"
        assert recovered.getCanXlConfigRef().getValue() == "/CanXL/AbstractCanCommController/CAN1"
        ports = recovered.getCouplingPorts()
        assert len(ports) == 1
        assert isinstance(ports[0], CouplingPort)
        assert ports[0].getShortName() == "CP1"
        assert recovered.getMacLayerType().getValue() == "ethernet"
        assert recovered.getMacUnicastAddress().getValue() == "00:1B:44:11:3A:B7"
        assert recovered.getMaximumReceiveBufferLength().getValue() == 1500
        assert recovered.getMaximumTransmitBufferLength().getValue() == 1500
        assert recovered.getSlaveActAsPassiveCommunicationSlave().getValue() is True

    def test_reader_empty_fields(self, parser):
        element = ET.fromstring("<ETHERNET-COMMUNICATION-CONTROLLER xmlns='%s'><SHORT-NAME>Empty</SHORT-NAME></ETHERNET-COMMUNICATION-CONTROLLER>" % NS)
        recovered = EthernetCommunicationController(MockParent(), "Empty")
        parser.readEthernetCommunicationController(element, recovered)

        assert recovered.getCanXlConfigRef() is None
        assert recovered.getCouplingPorts() == []
        assert recovered.getMacLayerType() is None
        assert recovered.getMacUnicastAddress() is None
        assert recovered.getMaximumReceiveBufferLength() is None
        assert recovered.getMaximumTransmitBufferLength() is None
