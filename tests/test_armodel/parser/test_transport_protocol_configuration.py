"""Parser tests for TransportProtocolConfiguration (Table 6.125, p.459) dispatch:
the TP-CONFIGURATION choice instantiates the abstract class's concrete subclasses.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import GenericTp, Ieee1722Tp, RtpTp, TcpTp, TransportProtocolConfiguration, UdpTp
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def parser():
    AUTOSAR.getInstance().new()
    return ARXMLParser()


def _snip(inner: str) -> ET.Element:
    return ET.fromstring(f"<ROOT xmlns='{NS}'>{inner}</ROOT>")


def test_read_generic_tp_configuration(parser):
    root = _snip("<TP-CONFIGURATION>" '<GENERIC-TP S="1234" T="2024-01-01T00:00:00Z">' "<TP-ADDRESS>30490</TP-ADDRESS>" "<TP-TECHNOLOGY>UDP</TP-TECHNOLOGY>" "</GENERIC-TP>" "</TP-CONFIGURATION>")
    configuration = parser.getTransportProtocolConfiguration(root, "TP-CONFIGURATION")
    assert isinstance(configuration, GenericTp)
    assert isinstance(configuration, TransportProtocolConfiguration)
    assert configuration.getTpAddress().getValue() == "30490"
    assert configuration.getTpTechnology().getValue() == "UDP"
    assert configuration.getChecksum().getValue() == "1234"
    assert configuration.getTimestamp().getValue() == "2024-01-01T00:00:00Z"


def test_read_rtp_tp_configuration_with_udp_tp(parser):
    root = _snip("<TP-CONFIGURATION><RTP-TP><SSRC>1234</SSRC><TCP-UDP-CONFIG><UDP-TP><UDP-TP-PORT><PORT-NUMBER>5004</PORT-NUMBER></UDP-TP-PORT></UDP-TP></TCP-UDP-CONFIG></RTP-TP></TP-CONFIGURATION>")
    configuration = parser.getTransportProtocolConfiguration(root, "TP-CONFIGURATION")
    assert isinstance(configuration, RtpTp)
    assert isinstance(configuration, TransportProtocolConfiguration)
    assert configuration.getSsrc().getValue() == 1234
    tcp_udp_config = configuration.getTcpUdpConfig()
    assert isinstance(tcp_udp_config, UdpTp)
    assert tcp_udp_config.getUdpTpPort().getPortNumber().getValue() == 5004


def test_read_rtp_tp_configuration_with_tcp_tp(parser):
    root = _snip("<TP-CONFIGURATION><RTP-TP><TCP-UDP-CONFIG><TCP-TP><TCP-TP-PORT><PORT-NUMBER>5005</PORT-NUMBER></TCP-TP-PORT></TCP-TP></TCP-UDP-CONFIG></RTP-TP></TP-CONFIGURATION>")
    configuration = parser.getTransportProtocolConfiguration(root, "TP-CONFIGURATION")
    assert isinstance(configuration, RtpTp)
    tcp_udp_config = configuration.getTcpUdpConfig()
    assert isinstance(tcp_udp_config, TcpTp)
    assert tcp_udp_config.getTcpTpPort().getPortNumber().getValue() == 5005


def test_read_rtp_tp_configuration_without_tcp_udp_config(parser):
    root = _snip("<TP-CONFIGURATION><RTP-TP><SSRC>7</SSRC></RTP-TP></TP-CONFIGURATION>")
    configuration = parser.getTransportProtocolConfiguration(root, "TP-CONFIGURATION")
    assert isinstance(configuration, RtpTp)
    assert configuration.getSsrc().getValue() == 7
    assert configuration.getTcpUdpConfig() is None


def test_read_ieee_1722_tp_configuration(parser):
    root = _snip(
        "<TP-CONFIGURATION><IEEE-1722-TP><RELATIVE-REPRESENTATION-TIME>0.5</RELATIVE-REPRESENTATION-TIME><STREAM-IDENTIFIER>1712384</STREAM-IDENTIFIER><SUB-TYPE>0</SUB-TYPE><VERSION>2</VERSION></IEEE-1722-TP></TP-CONFIGURATION>"
    )
    configuration = parser.getTransportProtocolConfiguration(root, "TP-CONFIGURATION")
    assert isinstance(configuration, Ieee1722Tp)
    assert isinstance(configuration, TransportProtocolConfiguration)
    assert configuration.getRelativeRepresentationTime().getValue() == 0.5
    assert configuration.getStreamIdentifier().getValue() == 1712384
    assert configuration.getSubType().getValue() == 0
    assert configuration.getVersion().getValue() == 2


def test_read_ieee_1722_tp_configuration_empty(parser):
    root = _snip("<TP-CONFIGURATION><IEEE-1722-TP></IEEE-1722-TP></TP-CONFIGURATION>")
    configuration = parser.getTransportProtocolConfiguration(root, "TP-CONFIGURATION")
    assert isinstance(configuration, Ieee1722Tp)
    assert configuration.getRelativeRepresentationTime() is None
    assert configuration.getStreamIdentifier() is None
    assert configuration.getSubType() is None
    assert configuration.getVersion() is None


def test_read_tp_configuration_empty(parser):
    root = _snip("<TP-CONFIGURATION></TP-CONFIGURATION>")
    configuration = parser.getTransportProtocolConfiguration(root, "TP-CONFIGURATION")
    assert configuration is None
