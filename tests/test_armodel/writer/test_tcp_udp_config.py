"""Writer round-trip tests for TcpUdpConfig (Table 6.127, p.459) dispatch:
the abstract class's concrete subclasses TcpTp/UdpTp serialize inside the
TP-CONFIGURATION choice (XSD choice members TCP-TP, UDP-TP).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import TcpUdpConfig, UdpTp
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _new_udp_tp():
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import TpPort

    tp = UdpTp()
    port = TpPort()
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, PositiveInteger

    dynamic = Boolean()
    dynamic.setValue(False)
    port.setDynamicallyAssigned(dynamic)
    number = PositiveInteger()
    number.setValue(30490)
    port.setPortNumber(number)
    tp.setUdpTpPort(port)
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
