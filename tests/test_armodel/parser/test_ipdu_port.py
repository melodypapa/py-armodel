"""Parser tests for IPduPort (Table 6.3, p.304).

XML element order per XSD complexType I-PDU-PORT: the base COMM-CONNECTOR-PORT group
(COMMUNICATION-DIRECTION, VARIATION-POINT last via xml.sequenceOffset="10000") then the
own I-PDU-PORT group (I-PDU-SIGNAL-PROCESSING, RX-SECURITY-VERIFICATION,
TIMESTAMP-RX-ACCEPTANCE-WINDOW, USE-AUTH-DATA-FRESHNESS). KEY-ID is atp.Status="removed"
(4.4.0) and absent from Table 6.3 — the reader tolerates and ignores it.
"""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology import CanCommunicationConnector
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import IPduPort
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


def _port_xml(extra_children: str = "", uuid: str = "") -> ET.Element:
    uuid_attr = " UUID='%s'" % uuid if uuid else ""
    xml = "<I-PDU-PORT%s>" "<SHORT-NAME>ip</SHORT-NAME>" "%s" "</I-PDU-PORT>" % (uuid_attr, extra_children)
    return ET.fromstring("<ROOT xmlns='%s'>%s</ROOT>" % (NS, xml))[0]


def _dispatch_xml(port_children: str) -> ET.Element:
    xml = "<ECU-COMM-PORT-INSTANCES>" "<I-PDU-PORT>" "<SHORT-NAME>ip</SHORT-NAME>" "%s" "</I-PDU-PORT>" "</ECU-COMM-PORT-INSTANCES>" % port_children
    return ET.fromstring("<ROOT xmlns='%s'>%s</ROOT>" % (NS, xml))


def _full_children() -> str:
    return (
        "<COMMUNICATION-DIRECTION>IN</COMMUNICATION-DIRECTION>"
        "<VARIATION-POINT><SHORT-LABEL>VP1</SHORT-LABEL></VARIATION-POINT>"
        "<I-PDU-SIGNAL-PROCESSING>DEFERRED</I-PDU-SIGNAL-PROCESSING>"
        "<RX-SECURITY-VERIFICATION>true</RX-SECURITY-VERIFICATION>"
        "<TIMESTAMP-RX-ACCEPTANCE-WINDOW>0.05</TIMESTAMP-RX-ACCEPTANCE-WINDOW>"
        "<USE-AUTH-DATA-FRESHNESS>false</USE-AUTH-DATA-FRESHNESS>"
    )


class TestReadIPduPort:
    def test_read_ipdu_port_full_field_values(self):
        element = _port_xml(_full_children())
        port = IPduPort(MockParent(), "ip")
        ARXMLParser().readIPduPort(element, port)

        assert port.getShortName() == "ip"
        assert port.getCommunicationDirection() is not None
        assert port.getCommunicationDirection().getValue() == "IN"
        assert port.getIPduSignalProcessing() is not None
        assert port.getIPduSignalProcessing().getValue() == "DEFERRED"
        assert port.getRxSecurityVerification() is not None
        assert port.getRxSecurityVerification().getValue() is True
        assert port.getTimestampRxAcceptanceWindow() is not None
        assert port.getTimestampRxAcceptanceWindow().getValue() == 0.05
        assert port.getUseAuthDataFreshness() is not None
        assert port.getUseAuthDataFreshness().getValue() is False

    def test_read_ipdu_port_without_children_leaves_fields_none(self):
        element = _port_xml()
        port = IPduPort(MockParent(), "ip")
        ARXMLParser().readIPduPort(element, port)

        assert port.getCommunicationDirection() is None
        assert port.getIPduSignalProcessing() is None
        assert port.getRxSecurityVerification() is None
        assert port.getTimestampRxAcceptanceWindow() is None
        assert port.getUseAuthDataFreshness() is None

    def test_read_ipdu_port_reads_base_level_uuid(self):
        element = _port_xml("<RX-SECURITY-VERIFICATION>false</RX-SECURITY-VERIFICATION>", uuid="5f2a-ipdu-port")
        port = IPduPort(MockParent(), "ip")
        ARXMLParser().readIPduPort(element, port)

        assert port.getUuid() is not None
        assert port.getUuid().getValue() == "5f2a-ipdu-port"
        assert port.getRxSecurityVerification().getValue() is False

    def test_read_ipdu_port_reads_variation_point(self):
        element = _port_xml("<VARIATION-POINT><SHORT-LABEL>VP2</SHORT-LABEL></VARIATION-POINT>")
        port = IPduPort(MockParent(), "ip")
        ARXMLParser().readIPduPort(element, port)

        assert port.getVariationPoint() is not None
        assert port.getVariationPoint().getShortLabel().getValue() == "VP2"

    def test_read_ipdu_port_ignores_removed_key_id(self):
        element = _port_xml("<KEY-ID>1</KEY-ID><RX-SECURITY-VERIFICATION>true</RX-SECURITY-VERIFICATION>")
        port = IPduPort(MockParent(), "ip")
        ARXMLParser().readIPduPort(element, port)

        assert port.getRxSecurityVerification().getValue() is True

    def test_dispatch_creates_ipdu_port_with_field_values(self):
        parent = _dispatch_xml("<COMMUNICATION-DIRECTION>OUT</COMMUNICATION-DIRECTION>" "<I-PDU-SIGNAL-PROCESSING>IMMEDIATE</I-PDU-SIGNAL-PROCESSING>")
        connector = CanCommunicationConnector(MockParent(), "conn")
        ARXMLParser().readCommunicationConnectorEcuCommPortInstances(parent, connector)

        ports = connector.getEcuCommPortInstances()
        assert len(ports) == 1
        assert isinstance(ports[0], IPduPort)
        assert ports[0].getShortName() == "ip"
        assert ports[0].getCommunicationDirection().getValue() == "OUT"
        assert ports[0].getIPduSignalProcessing().getValue() == "IMMEDIATE"

    def test_dispatch_without_wrapper_yields_no_ports(self):
        root = ET.fromstring("<ROOT xmlns='%s'/>" % NS)
        connector = CanCommunicationConnector(MockParent(), "conn")
        ARXMLParser().readCommunicationConnectorEcuCommPortInstances(root, connector)

        assert connector.getEcuCommPortInstances() == []
