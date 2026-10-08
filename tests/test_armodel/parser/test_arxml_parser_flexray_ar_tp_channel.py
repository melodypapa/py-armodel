"""Tests for the readFlexrayArTpChannel handler (R23-11 FlexrayArTpChannel, Table 6.246, p.602)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import FrArTpAckType, MaximumMessageLengthType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols import FlexrayArTpChannel, FlexrayArTpConfig
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def parser():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    return ARXMLParser()


def _snip(inner: str, root_tag: str = "ROOT") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


class TestReadFlexrayArTpChannel:
    """Tests for readFlexrayArTpChannel (R23-11 FlexrayArTpChannel, Table 6.246, p.602)."""

    def test_read_full_channel(self, parser):
        element = _snip(
            """
                <ACK-TYPE>ACK-WITH-RT</ACK-TYPE>
                <CANCELLATION>true</CANCELLATION>
                <EXTENDED-ADDRESSING>true</EXTENDED-ADDRESSING>
                <MAX-AR>3</MAX-AR>
                <MAX-AS>4</MAX-AS>
                <MAX-BS>8</MAX-BS>
                <MAX-FC-WAIT>2</MAX-FC-WAIT>
                <MAXIMUM-MESSAGE-LENGTH>ISO</MAXIMUM-MESSAGE-LENGTH>
                <MAX-RETRIES>1</MAX-RETRIES>
                <MINIMUM-MULTICAST-SEPERATION-TIME>0.0002</MINIMUM-MULTICAST-SEPERATION-TIME>
                <MINIMUM-SEPARATION-TIME>0.0001</MINIMUM-SEPARATION-TIME>
                <MULTICAST-SEGMENTATION>false</MULTICAST-SEGMENTATION>
                <N-PDU-REFS>
                    <N-PDU-REF DEST="N-PDU">/NPdus/N1</N-PDU-REF>
                    <N-PDU-REF DEST="N-PDU">/NPdus/N2</N-PDU-REF>
                </N-PDU-REFS>
                <TIME-BR>0.01</TIME-BR>
                <TIME-CS>0.02</TIME-CS>
                <TIMEOUT-AR>0.03</TIMEOUT-AR>
                <TIMEOUT-AS>0.04</TIMEOUT-AS>
                <TIMEOUT-BS>0.05</TIMEOUT-BS>
                <TIMEOUT-CR>0.06</TIMEOUT-CR>
            """,
            root_tag="FLEXRAY-AR-TP-CHANNEL",
        )
        channel = FlexrayArTpChannel()
        parser.readFlexrayArTpChannel(element, channel)
        assert channel.getAckType() is not None
        assert isinstance(channel.getAckType(), FrArTpAckType)
        assert channel.getAckType().getValue() == FrArTpAckType.ENUM_ACK_WITH_RT
        assert channel.getCancellation().getValue() is True
        assert channel.getExtendedAddressing().getValue() is True
        assert channel.getMaxAr().getValue() == 3
        assert channel.getMaxAs().getValue() == 4
        assert channel.getMaxBs().getValue() == 8
        assert channel.getMaxFcWait().getValue() == 2
        assert channel.getMaximumMessageLength() is not None
        assert isinstance(channel.getMaximumMessageLength(), MaximumMessageLengthType)
        assert channel.getMaximumMessageLength().getValue() == "ISO"
        assert channel.getMaxRetries().getValue() == 1
        assert channel.getMinimumMulticastSeperationTime().getValue() == 0.0002
        assert channel.getMinimumSeparationTime().getValue() == 0.0001
        assert channel.getMulticastSegmentation().getValue() is False
        refs = channel.getNPduRefs()
        assert len(refs) == 2
        assert refs[0].getValue() == "/NPdus/N1"
        assert refs[1].getValue() == "/NPdus/N2"
        assert channel.getTimeBr().getValue() == 0.01
        assert channel.getTimeCs().getValue() == 0.02
        assert channel.getTimeoutAr().getValue() == 0.03
        assert channel.getTimeoutAs().getValue() == 0.04
        assert channel.getTimeoutBs().getValue() == 0.05
        assert channel.getTimeoutCr().getValue() == 0.06
        assert channel.getTpConnections() == []

    def test_read_channel_with_tp_connections(self, parser):
        element = _snip(
            """
                <TP-CONNECTIONS>
                    <FLEXRAY-AR-TP-CONNECTION>
                        <CONNECTION-PRIO-PDUS>16</CONNECTION-PRIO-PDUS>
                        <SOURCE-REF DEST="FLEXRAY-AR-TP-NODE">/Nodes/Src</SOURCE-REF>
                        <TARGET-REFS>
                            <TARGET-REF DEST="FLEXRAY-AR-TP-NODE">/Nodes/Tgt</TARGET-REF>
                        </TARGET-REFS>
                    </FLEXRAY-AR-TP-CONNECTION>
                </TP-CONNECTIONS>
            """,
            root_tag="FLEXRAY-AR-TP-CHANNEL",
        )
        channel = FlexrayArTpChannel()
        parser.readFlexrayArTpChannel(element, channel)
        connections = channel.getTpConnections()
        assert len(connections) == 1
        assert connections[0].getConnectionPrioPdus().getValue() == 16
        assert connections[0].getSourceRef().getValue() == "/Nodes/Src"
        targets = connections[0].getTargetRefs()
        assert len(targets) == 1
        assert targets[0].getValue() == "/Nodes/Tgt"

    def test_read_empty_channel(self, parser):
        element = _snip("", root_tag="FLEXRAY-AR-TP-CHANNEL")
        channel = FlexrayArTpChannel()
        parser.readFlexrayArTpChannel(element, channel)
        assert channel.getAckType() is None
        assert channel.getNPduRefs() == []
        assert channel.getTpConnections() == []

    def test_read_via_config_dispatch(self, parser):
        element = _snip(
            """
                <SHORT-NAME>Config1</SHORT-NAME>
                <TP-CHANNELS>
                    <FLEXRAY-AR-TP-CHANNEL>
                        <ACK-TYPE>NO-ACK</ACK-TYPE>
                        <MAX-BS>6</MAX-BS>
                    </FLEXRAY-AR-TP-CHANNEL>
                </TP-CHANNELS>
            """,
            root_tag="FLEXRAY-AR-TP-CONFIG",
        )
        package = AUTOSAR.getInstance().createARPackage("TpConfigs")
        config = FlexrayArTpConfig(package, "Config1")
        parser.readFlexrayArTpConfig(element, config)
        channels = config.getTpChannels()
        assert len(channels) == 1
        assert channels[0].getAckType() is not None
        assert channels[0].getAckType().getValue() == FrArTpAckType.ENUM_NO_ACK
        assert channels[0].getMaxBs().getValue() == 6
