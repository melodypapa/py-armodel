"""Parser tests for CommConnectorPort (Table 6.1, p.303).

XML element order per XSD group COMM-CONNECTOR-PORT: COMMUNICATION-DIRECTION,
VARIATION-POINT (xml.sequenceOffset="10000", last). The abstract-level helper
readCommConnectorPort is exercised directly on a FramePort instance (the concrete
subclass used throughout) and through the ECU-COMM-PORT-INSTANCES dispatch on
readCommunicationConnectorEcuCommPortInstances.
"""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology import CanCommunicationConnector
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import CommConnectorPort, FramePort
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


def _port_xml(extra_children: str = "", uuid: str = "") -> ET.Element:
    uuid_attr = " UUID='%s'" % uuid if uuid else ""
    xml = "<FRAME-PORT%s>" "<SHORT-NAME>fp</SHORT-NAME>" "%s" "</FRAME-PORT>" % (uuid_attr, extra_children)
    return ET.fromstring("<ROOT xmlns='%s'>%s</ROOT>" % (NS, xml))[0]


def _dispatch_xml(port_children: str) -> ET.Element:
    xml = "<ECU-COMM-PORT-INSTANCES>" "<FRAME-PORT>" "<SHORT-NAME>fp</SHORT-NAME>" "%s" "</FRAME-PORT>" "</ECU-COMM-PORT-INSTANCES>" % port_children
    return ET.fromstring("<ROOT xmlns='%s'>%s</ROOT>" % (NS, xml))


class TestReadCommConnectorPort:
    def test_read_comm_connector_port_direct_field_values(self):
        element = _port_xml("<COMMUNICATION-DIRECTION>IN</COMMUNICATION-DIRECTION>")
        port = FramePort(MockParent(), "fp")
        ARXMLParser().readCommConnectorPort(element, port)

        assert isinstance(port, CommConnectorPort)
        assert port.getShortName() == "fp"
        assert port.getCommunicationDirection() is not None
        assert port.getCommunicationDirection().getValue() == "IN"

    def test_read_comm_connector_port_without_direction_leaves_field_none(self):
        element = _port_xml()
        port = FramePort(MockParent(), "fp")
        ARXMLParser().readCommConnectorPort(element, port)

        assert port.getCommunicationDirection() is None

    def test_read_comm_connector_port_reads_uuid_attribute(self):
        element = _port_xml("<COMMUNICATION-DIRECTION>OUT</COMMUNICATION-DIRECTION>", uuid="5f2a-uuid")
        port = FramePort(MockParent(), "fp")
        ARXMLParser().readCommConnectorPort(element, port)

        assert port.getUuid() is not None
        assert port.getUuid().getValue() == "5f2a-uuid"
        assert port.getCommunicationDirection().getValue() == "OUT"

    def test_read_comm_connector_port_reads_variation_point(self):
        element = _port_xml("<COMMUNICATION-DIRECTION>IN</COMMUNICATION-DIRECTION>" "<VARIATION-POINT><SHORT-LABEL>VP1</SHORT-LABEL></VARIATION-POINT>")
        port = FramePort(MockParent(), "fp")
        ARXMLParser().readCommConnectorPort(element, port)

        assert port.getVariationPoint() is not None
        assert port.getVariationPoint().getShortLabel().getValue() == "VP1"
        assert port.getCommunicationDirection().getValue() == "IN"

    def test_dispatch_creates_frame_port_with_field_values(self):
        parent = _dispatch_xml("<COMMUNICATION-DIRECTION>OUT</COMMUNICATION-DIRECTION>")
        connector = CanCommunicationConnector(MockParent(), "conn")
        ARXMLParser().readCommunicationConnectorEcuCommPortInstances(parent, connector)

        ports = connector.getEcuCommPortInstances()
        assert len(ports) == 1
        assert isinstance(ports[0], FramePort)
        assert ports[0].getShortName() == "fp"
        assert ports[0].getCommunicationDirection().getValue() == "OUT"

    def test_dispatch_without_wrapper_yields_no_ports(self):
        root = ET.fromstring("<ROOT xmlns='%s'/>" % NS)
        connector = CanCommunicationConnector(MockParent(), "conn")
        ARXMLParser().readCommunicationConnectorEcuCommPortInstances(root, connector)

        assert connector.getEcuCommPortInstances() == []
