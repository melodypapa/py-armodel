"""Reader tests for FrameMapping (AUTOSAR_CP_TPS_SystemTemplate Table 8.2, p.838).

readFrameMapping reads the XSD group FRAME-MAPPING (INTRODUCTION,
SOURCE-FRAME-REF, TARGET-FRAME-REF) after the AR-OBJECT group; getFrameMappings
dispatches FRAME-MAPPINGS/FRAME-MAPPING and readGateway wires it between
ECU-REF and I-PDU-MAPPINGS per the GATEWAY group order.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Multiplatform import FrameMapping
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _frame_mapping_element(with_introduction=True):
    xml = """<FRAME-MAPPING xmlns='%s'>
        %s
        <SOURCE-FRAME-REF DEST="FRAME-TRIGGERING">/Cluster/SourceTriggering</SOURCE-FRAME-REF>
        <TARGET-FRAME-REF DEST="FRAME-TRIGGERING">/Cluster/TargetTriggering</TARGET-FRAME-REF>
    </FRAME-MAPPING>""" % (
        NS,
        '<INTRODUCTION><P><L1 L="EN">Gateway intro</L1></P></INTRODUCTION>' if with_introduction else "",
    )
    return ET.fromstring(xml)


class TestReadFrameMapping:
    def test_read_all_elements(self):
        mapping = FrameMapping()
        ARXMLParser().readFrameMapping(_frame_mapping_element(), mapping)

        assert mapping.getSourceFrameRef().getValue() == "/Cluster/SourceTriggering"
        assert mapping.getSourceFrameRef().getDest() == "FRAME-TRIGGERING"
        assert mapping.getTargetFrameRef().getValue() == "/Cluster/TargetTriggering"
        introduction = mapping.getIntroduction()
        assert introduction is not None
        assert len(introduction.getPs()) == 1

    def test_read_absent_elements_to_none(self):
        mapping = FrameMapping()
        ARXMLParser().readFrameMapping(_frame_mapping_element(with_introduction=False), mapping)

        assert mapping.getIntroduction() is None
        assert mapping.getSourceFrameRef().getValue() == "/Cluster/SourceTriggering"

    def test_get_frame_mappings_dispatch(self):
        gateway_xml = (
            """<GATEWAY xmlns='%s'>
            <ECU-REF DEST="ECU-INSTANCE">/Ecu/Ecu_A</ECU-REF>
            <FRAME-MAPPINGS>
                <FRAME-MAPPING>
                    <SOURCE-FRAME-REF DEST="FRAME-TRIGGERING">/C/S</SOURCE-FRAME-REF>
                    <TARGET-FRAME-REF DEST="FRAME-TRIGGERING">/C/T</TARGET-FRAME-REF>
                </FRAME-MAPPING>
                <FRAME-MAPPING>
                    <SOURCE-FRAME-REF DEST="FRAME-TRIGGERING">/C/S2</SOURCE-FRAME-REF>
                    <TARGET-FRAME-REF DEST="FRAME-TRIGGERING">/C/T2</TARGET-FRAME-REF>
                </FRAME-MAPPING>
            </FRAME-MAPPINGS>
        </GATEWAY>"""
            % NS
        )
        element = ET.fromstring(gateway_xml)

        mappings = ARXMLParser().getFrameMappings(element)

        assert len(mappings) == 2
        assert mappings[0].getSourceFrameRef().getValue() == "/C/S"
        assert mappings[1].getTargetFrameRef().getValue() == "/C/T2"
