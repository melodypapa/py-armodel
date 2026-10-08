"""Reader tests for PduTriggering (Table 6.31, p.349).

XML group PDU-TRIGGERING (AUTOSAR_00052.xsd l.88762): I-PDU-PORT-REFS wrapper,
I-PDU-REF, I-SIGNAL-TRIGGERINGS wrapper (I-SIGNAL-TRIGGERING-REF-CONDITIONAL items),
SEC-OC-CRYPTO-MAPPING-REF, TRIGGER-I-PDU-SEND-CONDITIONS wrapper, VARIATION-POINT
last (sequenceOffset 10000), after the inherited IDENTIFIABLE group.
Aggregated by PhysicalChannel.pduTriggering.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology import CanPhysicalChannel
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import PduTriggering, TriggerIPduSendCondition
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


FULL_XML = """
<PDU-TRIGGERING xmlns="%s" UUID="11111111-2222-3333-4444-555555555555">
    <SHORT-NAME>PT1</SHORT-NAME>
    <I-PDU-PORT-REFS>
        <I-PDU-PORT-REF DEST="I-PDU-PORT">/Cluster/Ecu1/Port1</I-PDU-PORT-REF>
        <I-PDU-PORT-REF DEST="I-PDU-PORT">/Cluster/Ecu2/Port2</I-PDU-PORT-REF>
    </I-PDU-PORT-REFS>
    <I-PDU-REF DEST="PDU">/Cluster/Pdus/Ipdu1</I-PDU-REF>
    <I-SIGNAL-TRIGGERINGS>
        <I-SIGNAL-TRIGGERING-REF-CONDITIONAL>
            <I-SIGNAL-TRIGGERING-REF DEST="I-SIGNAL-TRIGGERING">/Cluster/ST1</I-SIGNAL-TRIGGERING-REF>
        </I-SIGNAL-TRIGGERING-REF-CONDITIONAL>
        <I-SIGNAL-TRIGGERING-REF-CONDITIONAL>
            <I-SIGNAL-TRIGGERING-REF DEST="I-SIGNAL-TRIGGERING">/Cluster/ST2</I-SIGNAL-TRIGGERING-REF>
        </I-SIGNAL-TRIGGERING-REF-CONDITIONAL>
    </I-SIGNAL-TRIGGERINGS>
    <SEC-OC-CRYPTO-MAPPING-REF DEST="SEC-OC-CRYPTO-SERVICE-MAPPING">/SecOc/CryptoMapping1</SEC-OC-CRYPTO-MAPPING-REF>
    <TRIGGER-I-PDU-SEND-CONDITIONS>
        <TRIGGER-I-PDU-SEND-CONDITION>
            <MODE-DECLARATION-REFS>
                <MODE-DECLARATION-REF DEST="MODE-DECLARATION">/Md/ModeDcl1</MODE-DECLARATION-REF>
            </MODE-DECLARATION-REFS>
        </TRIGGER-I-PDU-SEND-CONDITION>
    </TRIGGER-I-PDU-SEND-CONDITIONS>
    <VARIATION-POINT>
        <SHORT-LABEL>vpPt</SHORT-LABEL>
    </VARIATION-POINT>
</PDU-TRIGGERING>
""" % NS


class TestReadPduTriggering:
    def test_read_full(self):
        element = _parse(FULL_XML)
        triggering = PduTriggering(None, "PT1")
        ARXMLParser().readPduTriggering(element, triggering)

        assert triggering.getUuid() is not None
        assert triggering.getUuid().getValue() == "11111111-2222-3333-4444-555555555555"

        port_refs = triggering.getIPduPortRefs()
        assert [ref.getValue() for ref in port_refs] == ["/Cluster/Ecu1/Port1", "/Cluster/Ecu2/Port2"]
        assert port_refs[0].getDest() == "I-PDU-PORT"

        assert triggering.getIPduRef() is not None
        assert triggering.getIPduRef().getValue() == "/Cluster/Pdus/Ipdu1"
        assert triggering.getIPduRef().getDest() == "PDU"

        isignal_refs = triggering.getISignalTriggeringRefs()
        assert [ref.getValue() for ref in isignal_refs] == ["/Cluster/ST1", "/Cluster/ST2"]
        assert isignal_refs[0].getDest() == "I-SIGNAL-TRIGGERING"

        assert triggering.getSecOcCryptoMappingRef() is not None
        assert triggering.getSecOcCryptoMappingRef().getValue() == "/SecOc/CryptoMapping1"
        assert triggering.getSecOcCryptoMappingRef().getDest() == "SEC-OC-CRYPTO-SERVICE-MAPPING"

        conditions = triggering.getTriggerIPduSendConditions()
        assert len(conditions) == 1
        assert isinstance(conditions[0], TriggerIPduSendCondition)
        mode_refs = conditions[0].getModeDeclarationRefs()
        assert [ref.getValue() for ref in mode_refs] == ["/Md/ModeDcl1"]
        assert mode_refs[0].getDest() == "MODE-DECLARATION"

        assert triggering.getVariationPoint() is not None
        assert triggering.getVariationPoint().getShortLabel() is not None
        assert triggering.getVariationPoint().getShortLabel().getValue() == "vpPt"

    def test_read_empty(self):
        xml = '<PDU-TRIGGERING xmlns="%s"><SHORT-NAME>PT1</SHORT-NAME></PDU-TRIGGERING>' % NS
        element = _parse(xml)
        triggering = PduTriggering(None, "PT1")
        ARXMLParser().readPduTriggering(element, triggering)

        assert triggering.getIPduRef() is None
        assert triggering.getIPduPortRefs() == []
        assert triggering.getISignalTriggeringRefs() == []
        assert triggering.getSecOcCryptoMappingRef() is None
        assert triggering.getTriggerIPduSendConditions() == []
        assert triggering.getVariationPoint() is None

    def test_read_via_physical_channel_dispatch(self):
        xml = """
        <CAN-PHYSICAL-CHANNEL xmlns="%s">
            <SHORT-NAME>CanCh</SHORT-NAME>
            <PDU-TRIGGERINGS>
                <PDU-TRIGGERING>
                    <SHORT-NAME>PT1</SHORT-NAME>
                    <I-PDU-REF DEST="PDU">/Cluster/Pdus/Ipdu1</I-PDU-REF>
                </PDU-TRIGGERING>
            </PDU-TRIGGERINGS>
        </CAN-PHYSICAL-CHANNEL>
        """ % NS
        element = _parse(xml)
        channel = CanPhysicalChannel(None, "CanCh")
        ARXMLParser().readPhysicalChannelPduTriggerings(element, channel)

        triggerings = channel.getPduTriggerings()
        assert len(triggerings) == 1
        assert triggerings[0].getShortName() == "PT1"
        assert triggerings[0].getIPduRef() is not None
        assert triggerings[0].getIPduRef().getValue() == "/Cluster/Pdus/Ipdu1"
