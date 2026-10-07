"""Writer round-trip tests for TransportProtocolConfiguration (Table 6.125, p.459) dispatch:
the TP-CONFIGURATION choice serializes the abstract class's concrete subclasses.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ARLiteral,
    Boolean,
    DateTime,
    PositiveInteger,
    String,
    TimeValue,
    UriString,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    GenericTp,
    HttpTp,
    Ieee1722Tp,
    RequestMethodEnum,
    RtpTp,
    TcpTp,
    TpPort,
    TransportProtocolConfiguration,
    UdpTp,
)
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _literal(text):
    value = ARLiteral()
    value.setValue(text)
    return value


def _new_tp():
    tp = GenericTp()
    tp.setTpAddress(_literal("30490"))
    tp.setTpTechnology(_literal("UDP"))
    tp.setChecksum(String().setValue("1234"))
    tp.setTimestamp(DateTime().setValue("2024-01-01T00:00:00Z"))
    return tp


class TestWriteTransportProtocolConfiguration:
    def test_write_generic_tp(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeTransportProtocolConfiguration(parent, _new_tp())
        node = parent.find("TP-CONFIGURATION/GENERIC-TP")
        assert node is not None
        assert node.find("TP-ADDRESS").text == "30490"
        assert node.find("TP-TECHNOLOGY").text == "UDP"

    def test_write_none_omits_element(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeTransportProtocolConfiguration(parent, None)
        assert parent.find("TP-CONFIGURATION") is None

    def test_round_trip_preserves_values(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeTransportProtocolConfiguration(parent, _new_tp())
        inner = ET.tostring(parent).decode("utf-8")
        root = ET.fromstring(inner.replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))

        reloaded = ARXMLParser().getTransportProtocolConfiguration(root, "TP-CONFIGURATION")
        assert isinstance(reloaded, TransportProtocolConfiguration)
        assert reloaded.getTpAddress().getValue() == "30490"
        assert reloaded.getTpTechnology().getValue() == "UDP"
        assert reloaded.getChecksum().getValue() == "1234"
        assert reloaded.getTimestamp().getValue() == "2024-01-01T00:00:00Z"


def _new_rtp_tp():
    tp = RtpTp()
    tp.setSsrc(PositiveInteger().setValue("1234"))
    udp_tp = UdpTp()
    udp_tp.setUdpTpPort(TpPort().setPortNumber(PositiveInteger().setValue("5004")))
    tp.setTcpUdpConfig(udp_tp)
    return tp


class TestWriteRtpTp:
    def test_write_rtp_tp(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeTransportProtocolConfiguration(parent, _new_rtp_tp())
        node = parent.find("TP-CONFIGURATION/RTP-TP")
        assert node is not None
        assert node.find("SSRC").text == "1234"
        udp_tp = node.find("TCP-UDP-CONFIG/UDP-TP")
        assert udp_tp is not None
        assert udp_tp.find("UDP-TP-PORT/PORT-NUMBER").text == "5004"

    def test_write_rtp_tp_empty_fields_omits_optional_tags(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeTransportProtocolConfiguration(parent, RtpTp())
        node = parent.find("TP-CONFIGURATION/RTP-TP")
        assert node is not None
        assert node.find("SSRC") is None
        assert node.find("TCP-UDP-CONFIG") is None

    def test_round_trip_rtp_tp_preserves_values(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeTransportProtocolConfiguration(parent, _new_rtp_tp())
        inner = ET.tostring(parent).decode("utf-8")
        root = ET.fromstring(inner.replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))

        reloaded = ARXMLParser().getTransportProtocolConfiguration(root, "TP-CONFIGURATION")
        assert isinstance(reloaded, RtpTp)
        assert reloaded.getSsrc().getValue() == 1234
        tcp_udp_config = reloaded.getTcpUdpConfig()
        assert isinstance(tcp_udp_config, UdpTp)
        assert tcp_udp_config.getUdpTpPort().getPortNumber().getValue() == 5004

    def test_round_trip_rtp_tp_tcp_variant(self):
        tp = RtpTp()
        tcp_tp = TcpTp()
        tcp_tp.setTcpTpPort(TpPort().setPortNumber(PositiveInteger().setValue("5005")))
        tp.setTcpUdpConfig(tcp_tp)

        parent = ET.Element("PARENT")
        ARXMLWriter().writeTransportProtocolConfiguration(parent, tp)
        inner = ET.tostring(parent).decode("utf-8")
        root = ET.fromstring(inner.replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))

        reloaded = ARXMLParser().getTransportProtocolConfiguration(root, "TP-CONFIGURATION")
        assert isinstance(reloaded, RtpTp)
        tcp_udp_config = reloaded.getTcpUdpConfig()
        assert isinstance(tcp_udp_config, TcpTp)
        assert tcp_udp_config.getTcpTpPort().getPortNumber().getValue() == 5005


def _new_ieee_1722_tp():
    tp = Ieee1722Tp()
    tp.setRelativeRepresentationTime(TimeValue().setValue("0.5"))
    tp.setStreamIdentifier(PositiveInteger().setValue("1712384"))
    tp.setSubType(PositiveInteger().setValue("0"))
    tp.setVersion(PositiveInteger().setValue("2"))
    return tp


class TestWriteIeee1722Tp:
    def test_write_ieee_1722_tp(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeTransportProtocolConfiguration(parent, _new_ieee_1722_tp())
        node = parent.find("TP-CONFIGURATION/IEEE-1722-TP")
        assert node is not None
        assert node.find("RELATIVE-REPRESENTATION-TIME").text == "0.5"
        assert node.find("STREAM-IDENTIFIER").text == "1712384"
        assert node.find("SUB-TYPE").text == "0"
        assert node.find("VERSION").text == "2"

    def test_write_ieee_1722_tp_empty_fields_omits_optional_tags(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeTransportProtocolConfiguration(parent, Ieee1722Tp())
        node = parent.find("TP-CONFIGURATION/IEEE-1722-TP")
        assert node is not None
        assert node.find("RELATIVE-REPRESENTATION-TIME") is None
        assert node.find("STREAM-IDENTIFIER") is None
        assert node.find("SUB-TYPE") is None
        assert node.find("VERSION") is None

    def test_round_trip_ieee_1722_tp_preserves_values(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeTransportProtocolConfiguration(parent, _new_ieee_1722_tp())
        inner = ET.tostring(parent).decode("utf-8")
        root = ET.fromstring(inner.replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))

        reloaded = ARXMLParser().getTransportProtocolConfiguration(root, "TP-CONFIGURATION")
        assert isinstance(reloaded, Ieee1722Tp)
        assert reloaded.getRelativeRepresentationTime().getValue() == 0.5
        assert reloaded.getStreamIdentifier().getValue() == 1712384
        assert reloaded.getSubType().getValue() == 0
        assert reloaded.getVersion().getValue() == 2


def _new_http_tp():
    tp = HttpTp()
    tp.setContentType(String().setValue("application/soap+xml"))
    tp.setProtocolVersion(String().setValue("1.1"))
    tp.setRequestMethod(RequestMethodEnum().setValue(RequestMethodEnum.POST))
    tcp_tp = TcpTp()
    keep_alives = Boolean()
    keep_alives.setValue(True)
    tcp_tp.setKeepAlives(keep_alives)
    tcp_tp.setTcpTpPort(TpPort().setPortNumber(PositiveInteger().setValue("8080")))
    tp.setTcpTpConfig(tcp_tp)
    tp.setUri(UriString().setValue("http://example.com/Service"))
    return tp


class TestWriteHttpTp:
    def test_write_http_tp(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeTransportProtocolConfiguration(parent, _new_http_tp())
        node = parent.find("TP-CONFIGURATION/HTTP-TP")
        assert node is not None
        assert node.find("CONTENT-TYPE").text == "application/soap+xml"
        assert node.find("PROTOCOL-VERSION").text == "1.1"
        assert node.find("REQUEST-METHOD").text == "POST"
        config_node = node.find("TCP-TP-CONFIG")
        assert config_node is not None
        assert config_node.find("KEEP-ALIVES").text == "true"
        assert config_node.find("TCP-TP-PORT/PORT-NUMBER").text == "8080"
        assert node.find("URI").text == "http://example.com/Service"

    def test_write_http_tp_empty_fields_omits_optional_tags(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeTransportProtocolConfiguration(parent, HttpTp())
        node = parent.find("TP-CONFIGURATION/HTTP-TP")
        assert node is not None
        assert node.find("CONTENT-TYPE") is None
        assert node.find("PROTOCOL-VERSION") is None
        assert node.find("REQUEST-METHOD") is None
        assert node.find("TCP-TP-CONFIG") is None
        assert node.find("URI") is None

    def test_round_trip_http_tp_preserves_values(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeTransportProtocolConfiguration(parent, _new_http_tp())
        inner = ET.tostring(parent).decode("utf-8")
        root = ET.fromstring(inner.replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))

        reloaded = ARXMLParser().getTransportProtocolConfiguration(root, "TP-CONFIGURATION")
        assert isinstance(reloaded, HttpTp)
        assert reloaded.getContentType().getValue() == "application/soap+xml"
        assert reloaded.getProtocolVersion().getValue() == "1.1"
        assert reloaded.getRequestMethod().getValue() == RequestMethodEnum.POST
        tcp_tp_config = reloaded.getTcpTpConfig()
        assert isinstance(tcp_tp_config, TcpTp)
        assert tcp_tp_config.getKeepAlives().getValue() is True
        assert tcp_tp_config.getTcpTpPort().getPortNumber().getValue() == 8080
        assert reloaded.getUri().getValue() == "http://example.com/Service"
