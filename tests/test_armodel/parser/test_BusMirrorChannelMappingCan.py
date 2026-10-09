"""Reader tests for BusMirrorChannelMappingCan (SystemTemplate TPS Table 6.328, p.701).

readBusMirrorChannelMappingCan calls the base readBusMirrorChannelMapping and
reads the three wrapper lists (CAN-ID-RANGE-MAPPINGS, CAN-ID-TO-CAN-ID-MAPPINGS,
LIN-PID-TO-CAN-ID-MAPPINGS) then the two scalars, per the XSD group
BUS-MIRROR-CHANNEL-MAPPING-CAN (AUTOSAR_00052.xsd).
"""

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.BusMirror import BusMirrorChannelMappingCan
from tests.test_armodel.parser._helpers import _snip


class TestBusMirrorChannelMappingCanReader:
    def test_read_full_field_values(self, parser):
        mapping = BusMirrorChannelMappingCan(None, "CanMapping")
        element = _snip(
            """
            <SHORT-NAME>CanMapping</SHORT-NAME>
            <MIRRORING-PROTOCOL>VERSION-1</MIRRORING-PROTOCOL>
            <SOURCE-CHANNEL>
                <BUS-MIRROR-NETWORK-ID>1</BUS-MIRROR-NETWORK-ID>
            </SOURCE-CHANNEL>
            <TARGET-CHANNEL>
                <BUS-MIRROR-NETWORK-ID>2</BUS-MIRROR-NETWORK-ID>
            </TARGET-CHANNEL>
            <TARGET-PDU-TRIGGERINGS>
                <PDU-TRIGGERING-REF-CONDITIONAL>
                    <PDU-TRIGGERING-REF DEST="PDU-TRIGGERING">/Fibex/PduTriggering</PDU-TRIGGERING-REF>
                </PDU-TRIGGERING-REF-CONDITIONAL>
            </TARGET-PDU-TRIGGERINGS>
            <CAN-ID-RANGE-MAPPINGS>
                <BUS-MIRROR-CAN-ID-RANGE-MAPPING>
                    <DESTINATION-BASE-ID>16</DESTINATION-BASE-ID>
                    <SOURCE-CAN-ID-CODE>40</SOURCE-CAN-ID-CODE>
                    <SOURCE-CAN-ID-MASK>7</SOURCE-CAN-ID-MASK>
                </BUS-MIRROR-CAN-ID-RANGE-MAPPING>
            </CAN-ID-RANGE-MAPPINGS>
            <CAN-ID-TO-CAN-ID-MAPPINGS>
                <BUS-MIRROR-CAN-ID-TO-CAN-ID-MAPPING>
                    <REMAPPED-CAN-ID>512</REMAPPED-CAN-ID>
                    <SOUCE-CAN-ID-REF DEST="CAN-FRAME-TRIGGERING">/Can/FrameTriggering</SOUCE-CAN-ID-REF>
                </BUS-MIRROR-CAN-ID-TO-CAN-ID-MAPPING>
            </CAN-ID-TO-CAN-ID-MAPPINGS>
            <LIN-PID-TO-CAN-ID-MAPPINGS>
                <BUS-MIRROR-LIN-PID-TO-CAN-ID-MAPPING>
                    <REMAPPED-CAN-ID>768</REMAPPED-CAN-ID>
                    <SOURCE-LIN-PID-REF DEST="LIN-FRAME-TRIGGERING">/Lin/FrameTriggering</SOURCE-LIN-PID-REF>
                </BUS-MIRROR-LIN-PID-TO-CAN-ID-MAPPING>
            </LIN-PID-TO-CAN-ID-MAPPINGS>
            <MIRROR-SOURCE-LIN-TO-CAN-RANGE-BASE-ID>512</MIRROR-SOURCE-LIN-TO-CAN-RANGE-BASE-ID>
            <MIRROR-STATUS-CAN-ID>2048</MIRROR-STATUS-CAN-ID>
            """,
            root_tag="BUS-MIRROR-CHANNEL-MAPPING-CAN",
        )

        parser.readBusMirrorChannelMappingCan(element, mapping)

        assert mapping.getShortName() == "CanMapping"
        assert mapping.getMirroringProtocol().getValue() == "VERSION-1"
        assert mapping.getSourceChannel() is not None
        assert mapping.getTargetChannel() is not None
        assert len(mapping.getTargetPduTriggeringRefs()) == 1

        range_mappings = mapping.getCanIdRangeMappings()
        assert len(range_mappings) == 1
        assert range_mappings[0].getDestinationBaseId().getValue() == 16
        assert range_mappings[0].getSourceCanIdCode().getValue() == 40
        assert range_mappings[0].getSourceCanIdMask().getValue() == 7

        id_mappings = mapping.getCanIdToCanIdMappings()
        assert len(id_mappings) == 1
        assert id_mappings[0].getRemappedCanId().getValue() == 512
        assert id_mappings[0].getSouceCanIdRef().getValue() == "/Can/FrameTriggering"

        lin_mappings = mapping.getLinPidToCanIdMappings()
        assert len(lin_mappings) == 1
        assert lin_mappings[0].getRemappedCanId().getValue() == 768
        assert lin_mappings[0].getSourceLinPidRef().getValue() == "/Lin/FrameTriggering"

        assert mapping.getMirrorSourceLinToCanRangeBaseId().getValue() == 512
        assert mapping.getMirrorStatusCanId().getValue() == 2048

    def test_read_empty(self, parser):
        mapping = BusMirrorChannelMappingCan(None, "CanMapping")
        element = _snip(
            """
            <SHORT-NAME>CanMapping</SHORT-NAME>
            """,
            root_tag="BUS-MIRROR-CHANNEL-MAPPING-CAN",
        )

        parser.readBusMirrorChannelMappingCan(element, mapping)

        assert mapping.getMirroringProtocol() is None
        assert mapping.getSourceChannel() is None
        assert mapping.getTargetChannel() is None
        assert mapping.getTargetPduTriggeringRefs() == []
        assert mapping.getCanIdRangeMappings() == []
        assert mapping.getCanIdToCanIdMappings() == []
        assert mapping.getLinPidToCanIdMappings() == []
        assert mapping.getMirrorSourceLinToCanRangeBaseId() is None
        assert mapping.getMirrorStatusCanId() is None
