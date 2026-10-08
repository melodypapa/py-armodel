"""Writer round-trip tests for IPduPort (Table 6.3, p.304).

Element order per XSD complexType I-PDU-PORT: base COMM-CONNECTOR-PORT group
(COMMUNICATION-DIRECTION, VARIATION-POINT last via xml.sequenceOffset="10000") then the
own I-PDU-PORT group (I-PDU-SIGNAL-PROCESSING, RX-SECURITY-VERIFICATION,
TIMESTAMP-RX-ACCEPTANCE-WINDOW, USE-AUTH-DATA-FRESHNESS).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, Identifier, TimeValue
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import VariationPoint
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology import CanCommunicationConnector
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (
    CommunicationDirectionType,
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


def _full_port() -> IPduPort:
    port = IPduPort(_parent(), "ip")
    direction = CommunicationDirectionType()
    direction.setValue(CommunicationDirectionType.IN)
    port.setCommunicationDirection(direction)
    processing = IPduSignalProcessingEnum()
    processing.setValue(IPduSignalProcessingEnum.DEFERRED)
    port.setIPduSignalProcessing(processing)
    port.setRxSecurityVerification(Boolean().setValue(True))
    port.setTimestampRxAcceptanceWindow(TimeValue().setValue(0.05))
    port.setUseAuthDataFreshness(Boolean().setValue(False))
    return port


def _vp(label):
    vp = VariationPoint()
    vp.setShortLabel(Identifier().setValue(label))
    return vp


class TestWriteIPduPort:
    def test_write_ipdu_port_element_order(self, writer):
        # XSD complexType I-PDU-PORT: base group (COMMUNICATION-DIRECTION then
        # VARIATION-POINT last) before the own I-PDU-PORT group children.
        port = _full_port()
        port.setVariationPoint(_vp("VP1"))
        parent = ET.Element("PARENT")
        writer.writeIPduPort(parent, port)

        tag = parent.find("I-PDU-PORT")
        tags = [child.tag for child in tag]
        assert tags == [
            "SHORT-NAME",
            "COMMUNICATION-DIRECTION",
            "VARIATION-POINT",
            "I-PDU-SIGNAL-PROCESSING",
            "RX-SECURITY-VERIFICATION",
            "TIMESTAMP-RX-ACCEPTANCE-WINDOW",
            "USE-AUTH-DATA-FRESHNESS",
        ]
        assert tag.find("VARIATION-POINT/SHORT-LABEL").text == "VP1"

    def test_write_ipdu_port_field_values(self, writer):
        parent = ET.Element("PARENT")
        writer.writeIPduPort(parent, _full_port())

        tag = parent.find("I-PDU-PORT")
        assert tag.find("SHORT-NAME").text == "ip"
        assert tag.find("COMMUNICATION-DIRECTION").text == "IN"
        assert tag.find("I-PDU-SIGNAL-PROCESSING").text == "DEFERRED"
        assert tag.find("RX-SECURITY-VERIFICATION").text == "true"
        assert tag.find("TIMESTAMP-RX-ACCEPTANCE-WINDOW").text == "0.05"
        assert tag.find("USE-AUTH-DATA-FRESHNESS").text == "false"

    def test_write_ipdu_port_empty_fields_emit_no_own_elements(self, writer):
        parent = ET.Element("PARENT")
        writer.writeIPduPort(parent, IPduPort(_parent(), "ip"))

        tag = parent.find("I-PDU-PORT")
        assert tag.find("SHORT-NAME").text == "ip"
        assert tag.find("COMMUNICATION-DIRECTION") is None
        assert tag.find("I-PDU-SIGNAL-PROCESSING") is None
        assert tag.find("RX-SECURITY-VERIFICATION") is None
        assert tag.find("TIMESTAMP-RX-ACCEPTANCE-WINDOW") is None
        assert tag.find("USE-AUTH-DATA-FRESHNESS") is None

    def test_ipdu_port_round_trip(self, writer, parser):
        parent = ET.Element("PARENT")
        writer.writeIPduPort(parent, _full_port())

        reloaded = IPduPort(MockParent(), "ip")
        parser.readIPduPort(_namespaced(parent)[0], reloaded)

        assert reloaded.getShortName() == "ip"
        assert reloaded.getCommunicationDirection().getValue() == "IN"
        assert reloaded.getIPduSignalProcessing().getValue() == "DEFERRED"
        assert reloaded.getRxSecurityVerification().getValue() is True
        assert reloaded.getTimestampRxAcceptanceWindow().getValue() == 0.05
        assert reloaded.getUseAuthDataFreshness().getValue() is False

    def test_ipdu_port_variation_point_round_trip(self, writer, parser):
        port = _full_port()
        port.setVariationPoint(_vp("VP1"))
        parent = ET.Element("PARENT")
        writer.writeIPduPort(parent, port)

        reloaded = IPduPort(MockParent(), "ip")
        parser.readIPduPort(_namespaced(parent)[0], reloaded)

        assert reloaded.getVariationPoint() is not None
        assert reloaded.getVariationPoint().getShortLabel().getValue() == "VP1"
        assert reloaded.getRxSecurityVerification().getValue() is True

    def test_dispatch_writes_ipdu_port(self, writer, parser):
        connector = CanCommunicationConnector(_parent(), "conn")
        port = connector.createIPduPort("ip")
        direction = CommunicationDirectionType()
        direction.setValue(CommunicationDirectionType.OUT)
        port.setCommunicationDirection(direction)
        processing = IPduSignalProcessingEnum()
        processing.setValue(IPduSignalProcessingEnum.IMMEDIATE)
        port.setIPduSignalProcessing(processing)

        parent = ET.Element("PARENT")
        writer.writeCommunicationConnectorEcuCommPortInstances(parent, connector)

        instances_tag = parent.find("ECU-COMM-PORT-INSTANCES")
        assert instances_tag is not None
        port_tag = instances_tag.find("I-PDU-PORT")
        assert port_tag is not None
        assert port_tag.find("SHORT-NAME").text == "ip"
        assert port_tag.find("COMMUNICATION-DIRECTION").text == "OUT"
        assert port_tag.find("I-PDU-SIGNAL-PROCESSING").text == "IMMEDIATE"

        reloaded = CanCommunicationConnector(_parent(), "conn")
        parser.readCommunicationConnectorEcuCommPortInstances(_namespaced(parent), reloaded)
        ports = reloaded.getEcuCommPortInstances()
        assert len(ports) == 1
        assert isinstance(ports[0], IPduPort)
        assert ports[0].getCommunicationDirection().getValue() == "OUT"
        assert ports[0].getIPduSignalProcessing().getValue() == "IMMEDIATE"

    def test_ecu_comm_port_instances_empty_wrapper_not_emitted(self, writer, parser):
        connector = CanCommunicationConnector(_parent(), "conn")

        parent = ET.Element("PARENT")
        writer.writeCommunicationConnectorEcuCommPortInstances(parent, connector)
        assert parent.find("ECU-COMM-PORT-INSTANCES") is None

        reloaded = CanCommunicationConnector(_parent(), "conn")
        parser.readCommunicationConnectorEcuCommPortInstances(_namespaced(parent), reloaded)
        assert reloaded.getEcuCommPortInstances() == []
