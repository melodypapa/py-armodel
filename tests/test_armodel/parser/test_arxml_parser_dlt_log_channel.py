"""Tests for the readDltLogChannel handler (R23-11 DltLogChannel, Table 6.336, p.723)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Dlt import DltLogChannel
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test and pin the R23-11 release."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def parser():
    """Fresh ARXMLParser instance running in strict mode."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    return ARXMLParser()


def _snip(inner: str, root_tag: str = "ROOT") -> ET.Element:
    """Wrap an inner XML fragment in a root element bound to the AUTOSAR NS."""
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


class TestReadDltLogChannel:
    """Tests for readDltLogChannel handler (R23-11 DltLogChannel, Table 6.336, p.723)."""

    def test_read_dlt_log_channel_full(self, parser):
        element = _snip(
            """
                <SHORT-NAME>channel_one</SHORT-NAME>
                <APPLICATION-CONTEXT-REFS>
                    <APPLICATION-CONTEXT-REF DEST="DLT-CONTEXT">/LogAndTrace/DltContexts/Context1</APPLICATION-CONTEXT-REF>
                    <APPLICATION-CONTEXT-REF DEST="DLT-CONTEXT">/LogAndTrace/DltContexts/Context2</APPLICATION-CONTEXT-REF>
                </APPLICATION-CONTEXT-REFS>
                <DEFAULT-TRACE-STATE>DEFAULT-TRACE-STATE-ENABLED</DEFAULT-TRACE-STATE>
                <DLT-MESSAGE-REFS>
                    <DLT-MESSAGE-REF DEST="DLT-MESSAGE">/LogAndTrace/DltMessages/Message1</DLT-MESSAGE-REF>
                    <DLT-MESSAGE-REF DEST="DLT-MESSAGE">/LogAndTrace/DltMessages/Message2</DLT-MESSAGE-REF>
                </DLT-MESSAGE-REFS>
                <LOG-CHANNEL-ID>LOG1</LOG-CHANNEL-ID>
                <LOG-TRACE-DEFAULT-LOG-THRESHOLD>WARN</LOG-TRACE-DEFAULT-LOG-THRESHOLD>
                <NON-VERBOSE-MODE>true</NON-VERBOSE-MODE>
                <RX-PDU-TRIGGERING-REF DEST="PDU-TRIGGERING">/Topology/Cluster/PhysicalChannel/RxTriggering</RX-PDU-TRIGGERING-REF>
                <SEGMENTATION-SUPPORTED>false</SEGMENTATION-SUPPORTED>
                <TX-PDU-TRIGGERING-REF DEST="PDU-TRIGGERING">/Topology/Cluster/PhysicalChannel/TxTriggering</TX-PDU-TRIGGERING-REF>
            """,
            root_tag="DLT-LOG-CHANNEL",
        )
        channel = DltLogChannel(None, "channel_one")
        parser.readDltLogChannel(element, channel)
        assert channel.getShortName() == "channel_one"
        context_refs = channel.getApplicationContextRefs()
        assert len(context_refs) == 2
        assert context_refs[0].getValue() == "/LogAndTrace/DltContexts/Context1"
        assert context_refs[0].getDest() == "DLT-CONTEXT"
        assert context_refs[1].getValue() == "/LogAndTrace/DltContexts/Context2"
        assert channel.getDefaultTraceState().getValue() == "DEFAULT-TRACE-STATE-ENABLED"
        message_refs = channel.getDltMessageRefs()
        assert len(message_refs) == 2
        assert message_refs[0].getValue() == "/LogAndTrace/DltMessages/Message1"
        assert message_refs[0].getDest() == "DLT-MESSAGE"
        assert message_refs[1].getValue() == "/LogAndTrace/DltMessages/Message2"
        assert channel.getLogChannelId().getValue() == "LOG1"
        assert channel.getLogTraceDefaultLogThreshold().getValue() == "WARN"
        assert channel.getNonVerboseMode().getValue() is True
        assert channel.getRxPduTriggeringRef().getValue() == "/Topology/Cluster/PhysicalChannel/RxTriggering"
        assert channel.getRxPduTriggeringRef().getDest() == "PDU-TRIGGERING"
        assert channel.getSegmentationSupported().getValue() is False
        assert channel.getTxPduTriggeringRef().getValue() == "/Topology/Cluster/PhysicalChannel/TxTriggering"
        assert channel.getTxPduTriggeringRef().getDest() == "PDU-TRIGGERING"

    def test_read_dlt_log_channel_empty(self, parser):
        element = _snip(
            """
            """,
            root_tag="DLT-LOG-CHANNEL",
        )
        channel = DltLogChannel(None, "channel_empty")
        parser.readDltLogChannel(element, channel)
        assert channel.getApplicationContextRefs() == []
        assert channel.getDefaultTraceState() is None
        assert channel.getDltMessageRefs() == []
        assert channel.getLogChannelId() is None
        assert channel.getLogTraceDefaultLogThreshold() is None
        assert channel.getNonVerboseMode() is None
        assert channel.getRxPduTriggeringRef() is None
        assert channel.getSegmentationSupported() is None
        assert channel.getTxPduTriggeringRef() is None
