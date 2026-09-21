"""Writer round-trip tests for TransportProtocolConfiguration (Table 6.125, p.459) dispatch:
the TP-CONFIGURATION choice serializes the abstract class's concrete subclasses.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import GenericTp, TransportProtocolConfiguration
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
