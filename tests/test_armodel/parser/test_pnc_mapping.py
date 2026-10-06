"""Reader tests for PncMapping (Table 5.45, p.266).

XML group PNC-MAPPING (AUTOSAR_00052.xsd l.91575) after the inherited
AR-OBJECT / DESCRIBABLE groups: DYNAMIC-PNC-MAPPING-PDU-GROUP-REFS, IDENT,
PHYSICAL-CHANNEL-REFS, PNC-CONSUMED-PROVIDED-SERVICE-INSTANCE-GROUPS,
PNC-GROUP-REFS, PNC-IDENTIFIER, PNC-PDUR-GROUP-REFS, PNC-WAKEUP-ENABLE,
RELEVANT-FOR-DYNAMIC-PNC-MAPPING-REFS, SHORT-LABEL, VFC-IREFS,
WAKEUP-FRAME-REFS, VARIATION-POINT.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate import System
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.PncMapping import PncMapping, PncMappingIdent
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _parse(xml: str) -> ET.Element:
    return ET.fromstring(xml)


class TestReadPncMapping:
    def test_read_full(self):
        xml = (
            """
        <PNC-MAPPING xmlns="%s">
            <SHORT-NAME>Pnc1</SHORT-NAME>
            <DESC><L-2 L="FOR-ALL">A partial network</L-2></DESC>
            <DYNAMIC-PNC-MAPPING-PDU-GROUP-REFS>
                <DYNAMIC-PNC-MAPPING-PDU-GROUP-REF DEST="I-SIGNAL-I-PDU-GROUP">/Groups/DynGroup1</DYNAMIC-PNC-MAPPING-PDU-GROUP-REF>
            </DYNAMIC-PNC-MAPPING-PDU-GROUP-REFS>
            <IDENT>
                <SHORT-NAME>PncIdent1</SHORT-NAME>
            </IDENT>
            <PHYSICAL-CHANNEL-REFS>
                <PHYSICAL-CHANNEL-REF DEST="CAN-PHYSICAL-CHANNEL">/Topology/Can1</PHYSICAL-CHANNEL-REF>
            </PHYSICAL-CHANNEL-REFS>
            <PNC-CONSUMED-PROVIDED-SERVICE-INSTANCE-GROUPS>
                <CONSUMED-PROVIDED-SERVICE-INSTANCE-GROUP-REF-CONDITIONAL>
                    <CONSUMED-PROVIDED-SERVICE-INSTANCE-GROUP-REF DEST="CONSUMED-PROVIDED-SERVICE-INSTANCE-GROUP">/ServiceInstances/Group1</CONSUMED-PROVIDED-SERVICE-INSTANCE-GROUP-REF>
                </CONSUMED-PROVIDED-SERVICE-INSTANCE-GROUP-REF-CONDITIONAL>
            </PNC-CONSUMED-PROVIDED-SERVICE-INSTANCE-GROUPS>
            <PNC-GROUP-REFS>
                <PNC-GROUP-REF DEST="I-SIGNAL-I-PDU-GROUP">/Groups/PncGroup1</PNC-GROUP-REF>
            </PNC-GROUP-REFS>
            <PNC-IDENTIFIER>8</PNC-IDENTIFIER>
            <PNC-PDUR-GROUP-REFS>
                <PNC-PDUR-GROUP-REF DEST="PDUR-I-PDU-GROUP">/Groups/PdurGroup1</PNC-PDUR-GROUP-REF>
            </PNC-PDUR-GROUP-REFS>
            <PNC-WAKEUP-ENABLE>true</PNC-WAKEUP-ENABLE>
            <RELEVANT-FOR-DYNAMIC-PNC-MAPPING-REFS>
                <RELEVANT-FOR-DYNAMIC-PNC-MAPPING-REF DEST="ECU-INSTANCE">/Ecu/Gateway1</RELEVANT-FOR-DYNAMIC-PNC-MAPPING-REF>
            </RELEVANT-FOR-DYNAMIC-PNC-MAPPING-REFS>
            <SHORT-LABEL>PNC_1</SHORT-LABEL>
            <VFC-IREFS>
                <VFC-IREF>
                    <BASE-REF DEST="PORT-GROUP">/System/PortGroup1</BASE-REF>
                </VFC-IREF>
            </VFC-IREFS>
            <WAKEUP-FRAME-REFS>
                <WAKEUP-FRAME-REF DEST="CAN-FRAME-TRIGGERING">/Frames/Frame1</WAKEUP-FRAME-REF>
            </WAKEUP-FRAME-REFS>
        </PNC-MAPPING>
        """
            % NS
        )
        element = _parse(xml)
        mapping = PncMapping()
        ARXMLParser().readPncMapping(element, mapping)

        pdu_refs = mapping.getDynamicPncMappingPduGroupRefs()
        assert len(pdu_refs) == 1
        assert pdu_refs[0].getValue() == "/Groups/DynGroup1"
        ident = mapping.getIdent()
        assert isinstance(ident, PncMappingIdent)
        assert ident.getShortName() == "PncIdent1"
        assert mapping.getPhysicalChannelRefs()[0].getValue() == "/Topology/Can1"
        cpsig_refs = mapping.getPncConsumedProvidedServiceInstanceGroupRefs()
        assert len(cpsig_refs) == 1
        assert cpsig_refs[0].getValue() == "/ServiceInstances/Group1"
        assert mapping.getPncGroupRefs()[0].getValue() == "/Groups/PncGroup1"
        assert mapping.getPncIdentifier().getValue() == 8
        assert mapping.getPncPdurGroupRefs()[0].getValue() == "/Groups/PdurGroup1"
        assert mapping.getPncWakeupEnable().getValue() is True
        assert mapping.getRelevantForDynamicPncMappingRefs()[0].getValue() == "/Ecu/Gateway1"
        assert mapping.getShortLabel().getValue() == "PNC_1"
        vfc_irefs = mapping.getVfcIRefs()
        assert len(vfc_irefs) == 1
        assert vfc_irefs[0].getBaseRef().getValue() == "/System/PortGroup1"
        assert mapping.getWakeupFrameRefs()[0].getValue() == "/Frames/Frame1"
        assert mapping.getDesc() is not None

    def test_read_empty(self):
        xml = '<PNC-MAPPING xmlns="%s"/>' % NS
        element = _parse(xml)
        mapping = PncMapping()
        ARXMLParser().readPncMapping(element, mapping)

        assert mapping.getDynamicPncMappingPduGroupRefs() == []
        assert mapping.getIdent() is None
        assert mapping.getPncIdentifier() is None
        assert mapping.getVfcIRefs() == []

    def test_read_via_system_mapping(self):
        xml = (
            """
        <PARENT xmlns="%s">
            <PNC-MAPPINGS>
                <PNC-MAPPING>
                    <SHORT-LABEL>PNC_2</SHORT-LABEL>
                </PNC-MAPPING>
            </PNC-MAPPINGS>
        </PARENT>
        """
            % NS
        )
        element = _parse(xml)
        system = System(parent=None, short_name="sys")
        mapping = system.createSystemMapping("sm")
        ARXMLParser().readSystemMappingPncMappings(element, mapping)

        pnc_mappings = mapping.getPncMappings()
        assert len(pnc_mappings) == 1
        assert isinstance(pnc_mappings[0], PncMapping)
        assert pnc_mappings[0].getShortLabel().getValue() == "PNC_2"
