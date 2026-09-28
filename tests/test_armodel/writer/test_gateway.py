"""Writer round-trip tests for Gateway (AUTOSAR_CP_TPS_SystemTemplate Table 8.1, p.837).

Element order per XSD group GATEWAY (00052.xsd L63657): ECU-REF, FRAME-MAPPINGS,
I-PDU-MAPPINGS, SIGNAL-MAPPINGS; complexType = base groups (AR-OBJECT,
REFERRABLE, MULTILANGUAGE-REFERRABLE, IDENTIFIABLE, COLLECTABLE-ELEMENT,
PACKAGEABLE-ELEMENT, FIBEX-ELEMENT) + own group; FIBEX-ELEMENT group is empty
and the complexType carries no VARIATION-POINT capability.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Multiplatform import FrameMapping, Gateway, IPduMapping, ISignalMapping
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _ref(dest, value):
    ref = RefType()
    ref.setDest(dest)
    ref.setValue(value)
    return ref


def _full_gateway() -> Gateway:
    gateway = Gateway(None, "Gateway")
    gateway.setEcuRef(_ref("ECU-INSTANCE", "/EcuTest/GatewayEcu"))

    frame_mapping = FrameMapping()
    frame_mapping.setSourceFrameRef(_ref("FRAME-TRIGGERING", "/Cluster/FrameTriggering_Source"))
    frame_mapping.setTargetFrameRef(_ref("FRAME-TRIGGERING", "/Cluster/FrameTriggering_Target"))
    gateway.addFrameMapping(frame_mapping)

    ipdu_mapping = IPduMapping()
    ipdu_mapping.setSourceIPduRef(_ref("I-SIGNAL-I-PDU", "/Cluster/ISignalIPdu_Source"))
    pdu_max_length = PositiveInteger()
    pdu_max_length.setValue(64)
    ipdu_mapping.setPduMaxLength(pdu_max_length)
    gateway.addIPduMapping(ipdu_mapping)

    signal_mapping = ISignalMapping()
    signal_mapping.setSourceSignalRef(_ref("I-SIGNAL-TRIGGERING", "/Cluster/ISignalTriggering_Source"))
    signal_mapping.setTargetSignalRef(_ref("I-SIGNAL-TRIGGERING", "/Cluster/ISignalTriggering_Target"))
    gateway.addSignalMapping(signal_mapping)
    return gateway


class TestWriteGateway:
    def test_write_full_gateway_wrapper_order(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeGateway(parent, _full_gateway())

        gateway = parent.find("GATEWAY")
        children = [child.tag for child in gateway]
        assert children.index("ECU-REF") < children.index("FRAME-MAPPINGS") < children.index("I-PDU-MAPPINGS") < children.index("SIGNAL-MAPPINGS")

    def test_write_gateway_field_values(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeGateway(parent, _full_gateway())

        gateway = parent.find("GATEWAY")
        ecu_ref = gateway.find("ECU-REF")
        assert ecu_ref.text == "/EcuTest/GatewayEcu"
        assert ecu_ref.attrib["DEST"] == "ECU-INSTANCE"

        frame_mapping = gateway.find("FRAME-MAPPINGS/FRAME-MAPPING")
        assert frame_mapping.find("SOURCE-FRAME-REF").text == "/Cluster/FrameTriggering_Source"
        assert frame_mapping.find("TARGET-FRAME-REF").text == "/Cluster/FrameTriggering_Target"

        ipdu_mapping = gateway.find("I-PDU-MAPPINGS/I-PDU-MAPPING")
        assert ipdu_mapping.find("SOURCE-I-PDU-REF").text == "/Cluster/ISignalIPdu_Source"
        assert ipdu_mapping.find("PDU-MAX-LENGTH").text == "64"

        signal_mapping = gateway.find("SIGNAL-MAPPINGS/I-SIGNAL-MAPPING")
        assert signal_mapping.find("SOURCE-SIGNAL-REF").text == "/Cluster/ISignalTriggering_Source"
        assert signal_mapping.find("TARGET-SIGNAL-REF").text == "/Cluster/ISignalTriggering_Target"

    def test_write_omits_empty_wrappers(self):
        gateway = Gateway(None, "Gateway")
        gateway.setEcuRef(_ref("ECU-INSTANCE", "/EcuTest/GatewayEcu"))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeGateway(parent, gateway)

        gateway_element = parent.find("GATEWAY")
        assert gateway_element.find("FRAME-MAPPINGS") is None
        assert gateway_element.find("I-PDU-MAPPINGS") is None
        assert gateway_element.find("SIGNAL-MAPPINGS") is None

        children = [child.tag for child in gateway_element]
        assert "ECU-REF" in children

    def test_round_trip_mixed_gateway(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeGateway(parent, _full_gateway())
        reparsed = ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))

        gateway = Gateway(None, "Gateway")
        ARXMLParser().readGateway(reparsed.find("{%s}GATEWAY" % NS), gateway)

        assert gateway.getShortName() == "Gateway"
        assert gateway.getEcuRef().getValue() == "/EcuTest/GatewayEcu"
        assert gateway.getEcuRef().getDest() == "ECU-INSTANCE"

        frame_mappings = gateway.getFrameMappings()
        assert len(frame_mappings) == 1
        assert frame_mappings[0].getSourceFrameRef().getValue() == "/Cluster/FrameTriggering_Source"
        assert frame_mappings[0].getTargetFrameRef().getValue() == "/Cluster/FrameTriggering_Target"

        ipdu_mappings = gateway.getIPduMappings()
        assert len(ipdu_mappings) == 1
        assert ipdu_mappings[0].getSourceIPduRef().getValue() == "/Cluster/ISignalIPdu_Source"
        assert ipdu_mappings[0].getPduMaxLength().getValue() == 64

        signal_mappings = gateway.getSignalMappings()
        assert len(signal_mappings) == 1
        assert signal_mappings[0].getSourceSignalRef().getValue() == "/Cluster/ISignalTriggering_Source"
        assert signal_mappings[0].getTargetSignalRef().getValue() == "/Cluster/ISignalTriggering_Target"
