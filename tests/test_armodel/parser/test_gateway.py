"""Reader tests for Gateway (AUTOSAR_CP_TPS_SystemTemplate Table 8.1, p.837).

readGateway reads the XSD group GATEWAY (00052.xsd L63657) in order:
ECU-REF (REF + DEST ECU-INSTANCE), FRAME-MAPPINGS, I-PDU-MAPPINGS,
SIGNAL-MAPPINGS — after the base groups; the GATEWAY group and its
complexType carry no trailing VARIATION-POINT.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Multiplatform import Gateway
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _gateway_element(full=True):
    wrappers = (
        """<ECU-REF DEST="ECU-INSTANCE">/EcuTest/GatewayEcu</ECU-REF>
        <FRAME-MAPPINGS>
            <FRAME-MAPPING>
                <SOURCE-FRAME-REF DEST="FRAME-TRIGGERING">/Cluster/FT_Source</SOURCE-FRAME-REF>
                <TARGET-FRAME-REF DEST="FRAME-TRIGGERING">/Cluster/FT_Target</TARGET-FRAME-REF>
            </FRAME-MAPPING>
        </FRAME-MAPPINGS>
        <I-PDU-MAPPINGS>
            <I-PDU-MAPPING>
                <PDU-MAX-LENGTH>128</PDU-MAX-LENGTH>
                <SOURCE-I-PDU-REF DEST="I-SIGNAL-I-PDU">/Cluster/IPdu_Source</SOURCE-I-PDU-REF>
                <TARGET-I-PDU>
                    <TARGET-I-PDU-REF DEST="PDU-TRIGGERING">/Cluster/PT_Target</TARGET-I-PDU-REF>
                </TARGET-I-PDU>
            </I-PDU-MAPPING>
        </I-PDU-MAPPINGS>
        <SIGNAL-MAPPINGS>
            <I-SIGNAL-MAPPING>
                <SOURCE-SIGNAL-REF DEST="I-SIGNAL-TRIGGERING">/Cluster/IST_Source</SOURCE-SIGNAL-REF>
                <TARGET-SIGNAL-REF DEST="I-SIGNAL-TRIGGERING">/Cluster/IST_Target</TARGET-SIGNAL-REF>
            </I-SIGNAL-MAPPING>
        </SIGNAL-MAPPINGS>"""
        if full
        else ""
    )
    xml = """<ROOT xmlns='%s'><GATEWAY>
        <SHORT-NAME>Gateway</SHORT-NAME>
        %s
    </GATEWAY></ROOT>""" % (
        NS,
        wrappers,
    )
    return ET.fromstring(xml)


class TestReadGateway:
    def test_read_full_gateway(self):
        gateway = Gateway(None, "Gateway")
        ARXMLParser().readGateway(_gateway_element().find("{%s}GATEWAY" % NS), gateway)

        assert gateway.getShortName() == "Gateway"
        ecu_ref = gateway.getEcuRef()
        assert ecu_ref.getValue() == "/EcuTest/GatewayEcu"
        assert ecu_ref.getDest() == "ECU-INSTANCE"

        frame_mappings = gateway.getFrameMappings()
        assert len(frame_mappings) == 1
        assert frame_mappings[0].getSourceFrameRef().getValue() == "/Cluster/FT_Source"
        assert frame_mappings[0].getTargetFrameRef().getValue() == "/Cluster/FT_Target"

        ipdu_mappings = gateway.getIPduMappings()
        assert len(ipdu_mappings) == 1
        assert ipdu_mappings[0].getPduMaxLength().getValue() == 128
        assert ipdu_mappings[0].getSourceIPduRef().getValue() == "/Cluster/IPdu_Source"
        assert ipdu_mappings[0].getTargetIPdu().getTargetIPduRef().getValue() == "/Cluster/PT_Target"

        signal_mappings = gateway.getSignalMappings()
        assert len(signal_mappings) == 1
        assert signal_mappings[0].getSourceSignalRef().getValue() == "/Cluster/IST_Source"
        assert signal_mappings[0].getTargetSignalRef().getValue() == "/Cluster/IST_Target"

    def test_read_gateway_without_members(self):
        gateway = Gateway(None, "Gateway")
        ARXMLParser().readGateway(_gateway_element(full=False).find("{%s}GATEWAY" % NS), gateway)

        assert gateway.getShortName() == "Gateway"
        assert gateway.getEcuRef() is None
        assert gateway.getFrameMappings() == []
        assert gateway.getIPduMappings() == []
        assert gateway.getSignalMappings() == []
