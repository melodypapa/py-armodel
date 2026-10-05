"""Writer round-trip tests for TcpUdpConfig (Table 6.127, p.459) dispatch:
the abstract class's concrete subclasses TcpTp/UdpTp serialize inside the
TP-CONFIGURATION choice (XSD choice members TCP-TP, UDP-TP).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    DateTime,
    PositiveInteger,
    String,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    TcpTp,
    TcpUdpConfig,
    TpPort,
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


def _new_udp_tp():
    tp = UdpTp()
    port = TpPort()
    dynamic = Boolean()
    dynamic.setValue(False)
    port.setDynamicallyAssigned(dynamic)
    number = PositiveInteger()
    number.setValue(30490)
    port.setPortNumber(number)
    port.setChecksum(String().setValue("1234"))
    port.setTimestamp(DateTime().setValue("2024-01-01T00:00:00Z"))
    tp.setUdpTpPort(port)
    tp.setChecksum(String().setValue("9999"))
    tp.setTimestamp(DateTime().setValue("2025-02-02T00:00:00Z"))
    return tp


def _new_tcp_tp():
    tp = TcpTp()
    port = TpPort()
    number = PositiveInteger()
    number.setValue(5000)
    port.setPortNumber(number)
    tp.setTcpTpPort(port)
    keep = Boolean()
    keep.setValue(True)
    tp.setKeepAlives(keep)
    tp.setChecksum(String().setValue("9999"))
    tp.setTimestamp(DateTime().setValue("2025-02-02T00:00:00Z"))
    return tp


class TestTcpUdpConfigDispatch:
    def test_write_udp_tp(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeTransportProtocolConfiguration(parent, _new_udp_tp())
        node = parent.find("TP-CONFIGURATION/UDP-TP")
        assert node is not None
        assert node.find("UDP-TP-PORT/PORT-NUMBER").text == "30490"

    def test_round_trip_preserves_values(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeTransportProtocolConfiguration(parent, _new_udp_tp())
        inner = ET.tostring(parent).decode("utf-8")
        root = ET.fromstring(inner.replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))

        reloaded = ARXMLParser().getTransportProtocolConfiguration(root, "TP-CONFIGURATION")
        assert isinstance(reloaded, TcpUdpConfig)
        assert reloaded.getUdpTpPort().getPortNumber().getValue() == 30490
        assert reloaded.getUdpTpPort().getChecksum().getValue() == "1234"
        assert reloaded.getUdpTpPort().getTimestamp().getValue() == "2024-01-01T00:00:00Z"
        assert reloaded.getChecksum().getValue() == "9999"
        assert reloaded.getTimestamp().getValue() == "2025-02-02T00:00:00Z"

    def test_write_tcp_tp(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeTransportProtocolConfiguration(parent, _new_tcp_tp())
        node = parent.find("TP-CONFIGURATION/TCP-TP")
        assert node is not None
        assert node.find("TCP-TP-PORT/PORT-NUMBER").text == "5000"

    def test_round_trip_tcp_tp_preserves_values(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeTransportProtocolConfiguration(parent, _new_tcp_tp())
        inner = ET.tostring(parent).decode("utf-8")
        root = ET.fromstring(inner.replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))

        reloaded = ARXMLParser().getTransportProtocolConfiguration(root, "TP-CONFIGURATION")
        assert isinstance(reloaded, TcpTp)
        assert reloaded.getTcpTpPort().getPortNumber().getValue() == 5000
        assert reloaded.getKeepAlives().getValue() is True
        assert reloaded.getChecksum().getValue() == "9999"
        assert reloaded.getTimestamp().getValue() == "2025-02-02T00:00:00Z"
