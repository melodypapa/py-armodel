"""Writer round-trip tests for CommConnectorPort (Table 6.1)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, TimeValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import (
    CommConnectorPort,
    CommunicationDirectionType,
    FramePort,
    IPduPort,
    IPduSignalProcessingEnum,
)
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


@pytest.fixture(autouse=True)
def reset_autosar():
    from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR

    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def writer():
    return ARXMLWriter()


@pytest.fixture
def parser():
    return ARXMLParser()


def _parent():
    return MockParent()


def _namespaced(element: ET.Element) -> ET.Element:
    xml_text = ET.tostring(element, encoding="unicode")
    return ET.fromstring(xml_text.replace(element.tag, "%s xmlns='%s'" % (element.tag, NS), 1))


def _full_port() -> FramePort:
    port = FramePort(_parent(), "fp")
    direction = CommunicationDirectionType()
    direction.setValue(CommunicationDirectionType.ENUM_IN)
    port.setCommunicationDirection(direction)
    return port


class TestCommConnectorPort:
    def test_inheritance(self):
        parent = _parent()
        port = FramePort(parent, "fp")
        assert isinstance(port, CommConnectorPort)

    def test_write_comm_connector_port(self, writer):
        parent = ET.Element("PARENT")
        writer.writeFramePort(parent, _full_port())

        tag = parent.find("FRAME-PORT")
        assert tag is not None
        assert tag.find("SHORT-NAME") is not None
        assert tag.find("COMMUNICATION-DIRECTION") is not None
        assert tag.find("COMMUNICATION-DIRECTION").text == "in"

    def test_write_comm_connector_port_empty(self, writer):
        parent = ET.Element("PARENT")
        writer.writeFramePort(parent, FramePort(_parent(), "fp"))

        tag = parent.find("FRAME-PORT")
        assert tag is not None
        assert tag.find("COMMUNICATION-DIRECTION") is None

    def test_comm_connector_port_round_trip(self, writer, parser):
        parent = ET.Element("PARENT")
        writer.writeFramePort(parent, _full_port())

        reloaded = FramePort(MockParent(), "fp")
        parser.readFramePort(_namespaced(parent)[0], reloaded)

        assert isinstance(reloaded, CommConnectorPort)
        assert reloaded.getShortName() == "fp"
        assert reloaded.getCommunicationDirection() is not None
        assert reloaded.getCommunicationDirection().getValue() == "in"

    def test_comm_connector_port_round_trip_empty(self, writer, parser):
        parent = ET.Element("PARENT")
        writer.writeFramePort(parent, FramePort(_parent(), "fp"))

        reloaded = FramePort(MockParent(), "fp")
        parser.readFramePort(_namespaced(parent)[0], reloaded)

        assert reloaded.getCommunicationDirection() is None

    def test_ipdu_port_round_trip(self, writer, parser):
        port = IPduPort(MockParent(), "ip")
        direction = CommunicationDirectionType()
        direction.setValue(CommunicationDirectionType.ENUM_OUT)
        port.setCommunicationDirection(direction)
        processing = IPduSignalProcessingEnum()
        processing.setValue(IPduSignalProcessingEnum.ENUM_DEFERRED)
        port.setIPduSignalProcessing(processing)
        rx_security = Boolean()
        rx_security.setValue(True)
        port.setRxSecurityVerification(rx_security)
        window = TimeValue()
        window.setValue("0.05")
        port.setTimestampRxAcceptanceWindow(window)
        use_auth = Boolean()
        use_auth.setValue(False)
        port.setUseAuthDataFreshness(use_auth)

        parent = ET.Element("PARENT")
        writer.writeIPduPort(parent, port)

        reloaded = IPduPort(MockParent(), "ip")
        parser.readIPduPort(_namespaced(parent)[0], reloaded)

        assert isinstance(reloaded, CommConnectorPort)
        assert reloaded.getShortName() == "ip"
        assert reloaded.getCommunicationDirection().getValue() == "out"
        assert reloaded.getIPduSignalProcessing().getValue() == "deferred"
        assert reloaded.getRxSecurityVerification().getValue() is True
        assert float(reloaded.getTimestampRxAcceptanceWindow().getValue()) == 0.05
        assert reloaded.getUseAuthDataFreshness().getValue() is False

    def test_ipdu_port_round_trip_empty(self, writer, parser):
        parent = ET.Element("PARENT")
        writer.writeIPduPort(parent, IPduPort(MockParent(), "ip"))

        tag = parent.find("I-PDU-PORT")
        assert tag.find("COMMUNICATION-DIRECTION") is None
        assert tag.find("I-PDU-SIGNAL-PROCESSING") is None
        assert tag.find("RX-SECURITY-VERIFICATION") is None
        assert tag.find("TIMESTAMP-RX-ACCEPTANCE-WINDOW") is None
        assert tag.find("USE-AUTH-DATA-FRESHNESS") is None

        reloaded = IPduPort(MockParent(), "ip")
        parser.readIPduPort(_namespaced(parent)[0], reloaded)

        assert reloaded.getCommunicationDirection() is None
        assert reloaded.getIPduSignalProcessing() is None
        assert reloaded.getRxSecurityVerification() is None
        assert reloaded.getTimestampRxAcceptanceWindow() is None
        assert reloaded.getUseAuthDataFreshness() is None

    def test_ipdu_port_key_id_not_serialized(self, writer):
        port = IPduPort(MockParent(), "ip")
        assert not hasattr(port, "keyId")

        parent = ET.Element("PARENT")
        writer.writeIPduPort(parent, port)

        xml_text = ET.tostring(parent, encoding="unicode")
        assert "KEY-ID" not in xml_text
