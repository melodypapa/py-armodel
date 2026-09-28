"""Reader tests for ISignalMapping (AUTOSAR_CP_TPS_SystemTemplate Table 8.7, p.846).

readISignalMapping reads the XSD group I-SIGNAL-MAPPING (INTRODUCTION,
SOURCE-SIGNAL-REF, TARGET-SIGNAL-REF) after the AR-OBJECT group; getISignalMappings
dispatches SIGNAL-MAPPINGS/I-SIGNAL-MAPPING and readGateway wires it after
I-PDU-MAPPINGS per the GATEWAY group order.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Multiplatform import ISignalMapping
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _i_signal_mapping_element(with_introduction=True):
    xml = """<I-SIGNAL-MAPPING xmlns='%s'>
        %s
        <SOURCE-SIGNAL-REF DEST="I-SIGNAL-TRIGGERING">/Cluster/SourceTriggering</SOURCE-SIGNAL-REF>
        <TARGET-SIGNAL-REF DEST="I-SIGNAL-TRIGGERING">/Cluster/TargetTriggering</TARGET-SIGNAL-REF>
    </I-SIGNAL-MAPPING>""" % (
        NS,
        '<INTRODUCTION><P><L1 L="EN">Signal mapping intro</L1></P></INTRODUCTION>' if with_introduction else "",
    )
    return ET.fromstring(xml)


class TestReadISignalMapping:
    def test_read_all_elements(self):
        mapping = ISignalMapping()
        ARXMLParser().readISignalMapping(_i_signal_mapping_element(), mapping)

        assert mapping.getSourceSignalRef().getValue() == "/Cluster/SourceTriggering"
        assert mapping.getSourceSignalRef().getDest() == "I-SIGNAL-TRIGGERING"
        assert mapping.getTargetSignalRef().getValue() == "/Cluster/TargetTriggering"
        introduction = mapping.getIntroduction()
        assert introduction is not None
        assert len(introduction.getPs()) == 1

    def test_read_absent_elements_to_none(self):
        mapping = ISignalMapping()
        ARXMLParser().readISignalMapping(_i_signal_mapping_element(with_introduction=False), mapping)

        assert mapping.getIntroduction() is None
        assert mapping.getSourceSignalRef().getValue() == "/Cluster/SourceTriggering"
        assert mapping.getTargetSignalRef().getValue() == "/Cluster/TargetTriggering"

    def test_get_i_signal_mappings_dispatch(self):
        gateway_xml = (
            """<GATEWAY xmlns='%s'>
            <ECU-REF DEST="ECU-INSTANCE">/Ecu/Ecu_A</ECU-REF>
            <SIGNAL-MAPPINGS>
                <I-SIGNAL-MAPPING>
                    <SOURCE-SIGNAL-REF DEST="I-SIGNAL-TRIGGERING">/C/S</SOURCE-SIGNAL-REF>
                    <TARGET-SIGNAL-REF DEST="I-SIGNAL-TRIGGERING">/C/T</TARGET-SIGNAL-REF>
                </I-SIGNAL-MAPPING>
                <I-SIGNAL-MAPPING>
                    <SOURCE-SIGNAL-REF DEST="I-SIGNAL-TRIGGERING">/C/S2</SOURCE-SIGNAL-REF>
                    <TARGET-SIGNAL-REF DEST="I-SIGNAL-TRIGGERING">/C/T2</TARGET-SIGNAL-REF>
                </I-SIGNAL-MAPPING>
            </SIGNAL-MAPPINGS>
        </GATEWAY>"""
            % NS
        )
        element = ET.fromstring(gateway_xml)

        mappings = ARXMLParser().getISignalMappings(element)

        assert len(mappings) == 2
        assert mappings[0].getSourceSignalRef().getValue() == "/C/S"
        assert mappings[1].getTargetSignalRef().getValue() == "/C/T2"

    def test_gateway_dispatch_reads_signal_mappings_after_ipdu_mappings(self):
        gateway_xml = (
            """<GATEWAY xmlns='%s'>
            <ECU-REF DEST="ECU-INSTANCE">/Ecu/Ecu_A</ECU-REF>
            <FRAME-MAPPINGS>
                <FRAME-MAPPING>
                    <SOURCE-FRAME-REF DEST="FRAME-TRIGGERING">/C/SF</SOURCE-FRAME-REF>
                    <TARGET-FRAME-REF DEST="FRAME-TRIGGERING">/C/TF</TARGET-FRAME-REF>
                </FRAME-MAPPING>
            </FRAME-MAPPINGS>
            <I-PDU-MAPPINGS>
                <I-PDU-MAPPING>
                    <SOURCE-I-PDU-REF DEST="DCM-I-PDU">/Pdu/Dcm_A</SOURCE-I-PDU-REF>
                </I-PDU-MAPPING>
            </I-PDU-MAPPINGS>
            <SIGNAL-MAPPINGS>
                <I-SIGNAL-MAPPING>
                    <SOURCE-SIGNAL-REF DEST="I-SIGNAL-TRIGGERING">/C/ST</SOURCE-SIGNAL-REF>
                    <TARGET-SIGNAL-REF DEST="I-SIGNAL-TRIGGERING">/C/TT</TARGET-SIGNAL-REF>
                </I-SIGNAL-MAPPING>
            </SIGNAL-MAPPINGS>
        </GATEWAY>"""
            % NS
        )
        element = ET.fromstring(gateway_xml)

        gateway_children = [child.tag.split("}")[-1] for child in element]
        assert gateway_children.index("ECU-REF") < gateway_children.index("FRAME-MAPPINGS") < gateway_children.index("I-PDU-MAPPINGS") < gateway_children.index("SIGNAL-MAPPINGS")

        mappings = ARXMLParser().getISignalMappings(element)
        assert len(mappings) == 1
        assert mappings[0].getSourceSignalRef().getValue() == "/C/ST"
