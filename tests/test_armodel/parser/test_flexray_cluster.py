"""Parser tests for FlexrayCluster (Table 3.29, p.81).

XML element order per XSD FLEXRAY-CLUSTER: heritage groups (SHORT-NAME via IDENTIFIABLE)
first, then the FLEXRAY-CLUSTER group's optional FLEXRAY-CLUSTER-VARIANTS/
FLEXRAY-CLUSTER-CONDITIONAL wrapper carrying the inherited COMMUNICATION-CLUSTER content
(BAUDRATE, PHYSICAL-CHANNELS, PROTOCOL-NAME, PROTOCOL-VERSION) plus this class's
FLEXRAY-CLUSTER-CONTENT (ACTION-POINT-OFFSET .. WAKEUP-TX-IDLE, 35 elements).
readFlexrayCluster calls readIdentifiable on the outer element and the reusable
readCommunicationCluster helper exactly once on the CONDITIONAL wrapper.
"""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Flexray.FlexrayTopology import FlexrayCluster
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"

OWN_CONDITIONAL = (
    "<ACTION-POINT-OFFSET>2</ACTION-POINT-OFFSET>"
    "<BIT>0.1</BIT>"
    "<CAS-RX-LOW-MAX>10</CAS-RX-LOW-MAX>"
    "<COLD-START-ATTEMPTS>8</COLD-START-ATTEMPTS>"
    "<CYCLE>0.005</CYCLE>"
    "<CYCLE-COUNT-MAX>63</CYCLE-COUNT-MAX>"
    "<DETECT-NIT-ERROR>true</DETECT-NIT-ERROR>"
    "<DYNAMIC-SLOT-IDLE-PHASE>2</DYNAMIC-SLOT-IDLE-PHASE>"
    "<IGNORE-AFTER-TX>5</IGNORE-AFTER-TX>"
    "<LISTEN-NOISE>3</LISTEN-NOISE>"
    "<MACRO-PER-CYCLE>36</MACRO-PER-CYCLE>"
    "<MACROTICK-DURATION>0.001</MACROTICK-DURATION>"
    "<MAX-WITHOUT-CLOCK-CORRECTION-FATAL>2</MAX-WITHOUT-CLOCK-CORRECTION-FATAL>"
    "<MAX-WITHOUT-CLOCK-CORRECTION-PASSIVE>3</MAX-WITHOUT-CLOCK-CORRECTION-PASSIVE>"
    "<MINISLOT-ACTION-POINT-OFFSET>1</MINISLOT-ACTION-POINT-OFFSET>"
    "<MINISLOT-DURATION>10</MINISLOT-DURATION>"
    "<NETWORK-IDLE-TIME>20</NETWORK-IDLE-TIME>"
    "<NETWORK-MANAGEMENT-VECTOR-LENGTH>12</NETWORK-MANAGEMENT-VECTOR-LENGTH>"
    "<NUMBER-OF-MINISLOTS>790</NUMBER-OF-MINISLOTS>"
    "<NUMBER-OF-STATIC-SLOTS>70</NUMBER-OF-STATIC-SLOTS>"
    "<OFFSET-CORRECTION-START>2</OFFSET-CORRECTION-START>"
    "<PAYLOAD-LENGTH-STATIC>16</PAYLOAD-LENGTH-STATIC>"
    "<SAFETY-MARGIN>2</SAFETY-MARGIN>"
    "<SAMPLE-CLOCK-PERIOD>0.05</SAMPLE-CLOCK-PERIOD>"
    "<STATIC-SLOT-DURATION>100</STATIC-SLOT-DURATION>"
    "<SYMBOL-WINDOW>101</SYMBOL-WINDOW>"
    "<SYMBOL-WINDOW-ACTION-POINT-OFFSET>102</SYMBOL-WINDOW-ACTION-POINT-OFFSET>"
    "<SYNC-FRAME-ID-COUNT-MAX>15</SYNC-FRAME-ID-COUNT-MAX>"
    "<TRANCEIVER-STANDBY-DELAY>0.5</TRANCEIVER-STANDBY-DELAY>"
    "<TRANSMISSION-START-SEQUENCE-DURATION>4</TRANSMISSION-START-SEQUENCE-DURATION>"
    "<WAKEUP-RX-IDLE>60</WAKEUP-RX-IDLE>"
    "<WAKEUP-RX-LOW>180</WAKEUP-RX-LOW>"
    "<WAKEUP-RX-WINDOW>300</WAKEUP-RX-WINDOW>"
    "<WAKEUP-TX-ACTIVE>60</WAKEUP-TX-ACTIVE>"
    "<WAKEUP-TX-IDLE>180</WAKEUP-TX-IDLE>"
)

FULL_FLEXRAY_CLUSTER = (
    "<FLEXRAY-CLUSTER>"
    "<SHORT-NAME>Cluster</SHORT-NAME>"
    "<FLEXRAY-CLUSTER-VARIANTS>"
    "<FLEXRAY-CLUSTER-CONDITIONAL>"
    "<BAUDRATE>500000</BAUDRATE>"
    "<PROTOCOL-NAME>FLEXRAY</PROTOCOL-NAME>"
    "<PROTOCOL-VERSION>10.0</PROTOCOL-VERSION>" + OWN_CONDITIONAL + "</FLEXRAY-CLUSTER-CONDITIONAL>"
    "</FLEXRAY-CLUSTER-VARIANTS>"
    "</FLEXRAY-CLUSTER>"
)

BARE_FLEXRAY_CLUSTER = (
    "<FLEXRAY-CLUSTER>"
    "<SHORT-NAME>Cluster</SHORT-NAME>"
    "<FLEXRAY-CLUSTER-VARIANTS>"
    "<FLEXRAY-CLUSTER-CONDITIONAL>"
    "</FLEXRAY-CLUSTER-CONDITIONAL>"
    "</FLEXRAY-CLUSTER-VARIANTS>"
    "</FLEXRAY-CLUSTER>"
)

WRAPPERLESS_FLEXRAY_CLUSTER = "<FLEXRAY-CLUSTER>" "<SHORT-NAME>Cluster</SHORT-NAME>" "</FLEXRAY-CLUSTER>"


def _new_cluster(name):
    pkg = AUTOSAR.getInstance().createARPackage("Pkg")
    return FlexrayCluster(pkg, name)


def _read_flexray_cluster(xml):
    root = ET.fromstring("<ROOT xmlns='%s'>%s</ROOT>" % (NS, xml))
    cluster = _new_cluster("Cluster")
    ARXMLParser().readFlexrayCluster(root[0], cluster)
    return cluster


class TestReadFlexrayCluster:
    def test_reads_short_name_and_inherited_levels(self):
        cluster = _read_flexray_cluster(FULL_FLEXRAY_CLUSTER)

        assert cluster.getShortName() == "Cluster"
        assert cluster.getBaudrate().getValue() == 500000
        assert cluster.getProtocolName().getValue() == "FLEXRAY"
        assert cluster.getProtocolVersion().getValue() == "10.0"

    def test_reads_own_field_values(self):
        cluster = _read_flexray_cluster(FULL_FLEXRAY_CLUSTER)

        assert cluster.getActionPointOffset().getValue() == 2
        assert cluster.getBit().getValue() == 0.1
        assert cluster.getCasRxLowMax().getValue() == 10
        assert cluster.getColdStartAttempts().getValue() == 8
        assert cluster.getCycle().getValue() == 0.005
        assert cluster.getCycleCountMax().getValue() == 63
        assert cluster.getDetectNitError().getValue() is True
        assert cluster.getDynamicSlotIdlePhase().getValue() == 2
        assert cluster.getIgnoreAfterTx().getValue() == 5
        assert cluster.getListenNoise().getValue() == 3
        assert cluster.getMacroPerCycle().getValue() == 36
        assert cluster.getMacrotickDuration().getValue() == 0.001
        assert cluster.getMaxWithoutClockCorrectionFatal().getValue() == 2
        assert cluster.getMaxWithoutClockCorrectionPassive().getValue() == 3
        assert cluster.getMinislotActionPointOffset().getValue() == 1
        assert cluster.getMinislotDuration().getValue() == 10
        assert cluster.getNetworkIdleTime().getValue() == 20
        assert cluster.getNetworkManagementVectorLength().getValue() == 12
        assert cluster.getNumberOfMinislots().getValue() == 790
        assert cluster.getNumberOfStaticSlots().getValue() == 70
        assert cluster.getOffsetCorrectionStart().getValue() == 2
        assert cluster.getPayloadLengthStatic().getValue() == 16
        assert cluster.getSafetyMargin().getValue() == 2
        assert cluster.getSampleClockPeriod().getValue() == 0.05
        assert cluster.getStaticSlotDuration().getValue() == 100
        assert cluster.getSymbolWindow().getValue() == 101
        assert cluster.getSymbolWindowActionPointOffset().getValue() == 102
        assert cluster.getSyncFrameIdCountMax().getValue() == 15
        assert cluster.getTranceiverStandbyDelay().getValue() == 0.5
        assert cluster.getTransmissionStartSequenceDuration().getValue() == 4
        assert cluster.getWakeupRxIdle().getValue() == 60
        assert cluster.getWakeupRxLow().getValue() == 180
        assert cluster.getWakeupRxWindow().getValue() == 300
        assert cluster.getWakeupTxActive().getValue() == 60
        assert cluster.getWakeupTxIdle().getValue() == 180

    def test_reads_empty_conditional_to_none_fields(self):
        cluster = _read_flexray_cluster(BARE_FLEXRAY_CLUSTER)

        assert cluster.getShortName() == "Cluster"
        assert cluster.getBaudrate() is None
        assert cluster.getProtocolName() is None
        assert cluster.getProtocolVersion() is None
        assert cluster.getActionPointOffset() is None
        assert cluster.getBit() is None
        assert cluster.getCasRxLowMax() is None
        assert cluster.getColdStartAttempts() is None
        assert cluster.getCycle() is None
        assert cluster.getCycleCountMax() is None
        assert cluster.getDetectNitError() is None
        assert cluster.getDynamicSlotIdlePhase() is None
        assert cluster.getIgnoreAfterTx() is None
        assert cluster.getListenNoise() is None
        assert cluster.getMacroPerCycle() is None
        assert cluster.getMacrotickDuration() is None
        assert cluster.getMaxWithoutClockCorrectionFatal() is None
        assert cluster.getMaxWithoutClockCorrectionPassive() is None
        assert cluster.getMinislotActionPointOffset() is None
        assert cluster.getMinislotDuration() is None
        assert cluster.getNetworkIdleTime() is None
        assert cluster.getNetworkManagementVectorLength() is None
        assert cluster.getNumberOfMinislots() is None
        assert cluster.getNumberOfStaticSlots() is None
        assert cluster.getOffsetCorrectionStart() is None
        assert cluster.getPayloadLengthStatic() is None
        assert cluster.getSafetyMargin() is None
        assert cluster.getSampleClockPeriod() is None
        assert cluster.getStaticSlotDuration() is None
        assert cluster.getSymbolWindow() is None
        assert cluster.getSymbolWindowActionPointOffset() is None
        assert cluster.getSyncFrameIdCountMax() is None
        assert cluster.getTranceiverStandbyDelay() is None
        assert cluster.getTransmissionStartSequenceDuration() is None
        assert cluster.getWakeupRxIdle() is None
        assert cluster.getWakeupRxLow() is None
        assert cluster.getWakeupRxWindow() is None
        assert cluster.getWakeupTxActive() is None
        assert cluster.getWakeupTxIdle() is None

    def test_reads_cluster_without_variants_wrapper_to_none_fields(self):
        cluster = _read_flexray_cluster(WRAPPERLESS_FLEXRAY_CLUSTER)

        assert cluster.getShortName() == "Cluster"
        assert cluster.getBaudrate() is None
        assert cluster.getProtocolName() is None
        assert cluster.getProtocolVersion() is None
        assert cluster.getActionPointOffset() is None
        assert cluster.getCycle() is None
        assert cluster.getMacroPerCycle() is None
        assert cluster.getWakeupTxIdle() is None
