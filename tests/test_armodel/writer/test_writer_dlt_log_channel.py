"""Tests for the writeDltLogChannel handler (R23-11 DltLogChannel, Table 6.336, p.723)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    RefType,
    String,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Dlt import DltDefaultTraceStateEnum, DltLogChannel, LogTraceDefaultLogLevelEnum
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

XSD_CHILD_ORDER = [
    "SHORT-NAME",
    "APPLICATION-CONTEXT-REFS",
    "DEFAULT-TRACE-STATE",
    "DLT-MESSAGE-REFS",
    "LOG-CHANNEL-ID",
    "LOG-TRACE-DEFAULT-LOG-THRESHOLD",
    "NON-VERBOSE-MODE",
    "RX-PDU-TRIGGERING-REF",
    "SEGMENTATION-SUPPORTED",
    "TX-PDU-TRIGGERING-REF",
]

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def writer():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    return ARXMLWriter()


@pytest.fixture
def parser():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    return ARXMLParser()


def _parent():
    return ET.Element("PARENT")


def _string(value: str) -> String:
    text = String()
    text.setValue(value)
    return text


def _ref(value: str, dest: str) -> RefType:
    ref = RefType()
    ref.setValue(value)
    ref.setDest(dest)
    return ref


def _boolean(value: str) -> Boolean:
    boolean = Boolean()
    boolean.setValue(value)
    return boolean


def _fill(channel: DltLogChannel) -> DltLogChannel:
    channel.addApplicationContextRef(_ref("/LogAndTrace/DltContexts/Context1", "DLT-CONTEXT"))
    channel.addApplicationContextRef(_ref("/LogAndTrace/DltContexts/Context2", "DLT-CONTEXT"))
    channel.setDefaultTraceState(DltDefaultTraceStateEnum().setValue("DEFAULT-TRACE-STATE-ENABLED"))
    channel.addDltMessageRef(_ref("/LogAndTrace/DltMessages/Message1", "DLT-MESSAGE"))
    channel.addDltMessageRef(_ref("/LogAndTrace/DltMessages/Message2", "DLT-MESSAGE"))
    channel.setLogChannelId(_string("LOG1"))
    channel.setLogTraceDefaultLogThreshold(LogTraceDefaultLogLevelEnum().setValue("WARN"))
    channel.setNonVerboseMode(_boolean("true"))
    channel.setRxPduTriggeringRef(_ref("/Topology/Cluster/PhysicalChannel/RxTriggering", "PDU-TRIGGERING"))
    channel.setSegmentationSupported(_boolean("false"))
    channel.setTxPduTriggeringRef(_ref("/Topology/Cluster/PhysicalChannel/TxTriggering", "PDU-TRIGGERING"))
    return channel


class TestWriteDltLogChannel:
    """Tests for writeDltLogChannel handler (R23-11 DltLogChannel, Table 6.336, p.723)."""

    def test_children_in_xsd_order(self, writer):
        parent = _parent()
        writer.writeDltLogChannel(parent, _fill(DltLogChannel(None, "channel_one")))
        child = parent.find("DLT-LOG-CHANNEL")
        assert child is not None
        child_tags = [element.tag for element in child]
        assert child_tags == XSD_CHILD_ORDER
        assert child.find("SHORT-NAME").text == "channel_one"
        context_refs_element = child.find("APPLICATION-CONTEXT-REFS")
        context_refs = context_refs_element.findall("APPLICATION-CONTEXT-REF")
        assert len(context_refs) == 2
        assert context_refs[0].text == "/LogAndTrace/DltContexts/Context1"
        assert context_refs[0].get("DEST") == "DLT-CONTEXT"
        assert context_refs[1].text == "/LogAndTrace/DltContexts/Context2"
        assert child.find("DEFAULT-TRACE-STATE").text == "DEFAULT-TRACE-STATE-ENABLED"
        message_refs_element = child.find("DLT-MESSAGE-REFS")
        message_refs = message_refs_element.findall("DLT-MESSAGE-REF")
        assert len(message_refs) == 2
        assert message_refs[0].text == "/LogAndTrace/DltMessages/Message1"
        assert message_refs[0].get("DEST") == "DLT-MESSAGE"
        assert child.find("LOG-CHANNEL-ID").text == "LOG1"
        assert child.find("LOG-TRACE-DEFAULT-LOG-THRESHOLD").text == "WARN"
        assert child.find("NON-VERBOSE-MODE").text == "true"
        rx_ref = child.find("RX-PDU-TRIGGERING-REF")
        assert rx_ref.text == "/Topology/Cluster/PhysicalChannel/RxTriggering"
        assert rx_ref.get("DEST") == "PDU-TRIGGERING"
        assert child.find("SEGMENTATION-SUPPORTED").text == "false"
        tx_ref = child.find("TX-PDU-TRIGGERING-REF")
        assert tx_ref.text == "/Topology/Cluster/PhysicalChannel/TxTriggering"
        assert tx_ref.get("DEST") == "PDU-TRIGGERING"

    def test_empty_wrapper_list_omitted(self, writer):
        parent = _parent()
        writer.writeDltLogChannel(parent, DltLogChannel(None, "channel_empty"))
        child = parent.find("DLT-LOG-CHANNEL")
        assert child is not None
        assert child.find("APPLICATION-CONTEXT-REFS") is None
        assert child.find("DEFAULT-TRACE-STATE") is None
        assert child.find("DLT-MESSAGE-REFS") is None
        assert child.find("LOG-CHANNEL-ID") is None
        assert child.find("LOG-TRACE-DEFAULT-LOG-THRESHOLD") is None
        assert child.find("NON-VERBOSE-MODE") is None
        assert child.find("RX-PDU-TRIGGERING-REF") is None
        assert child.find("SEGMENTATION-SUPPORTED") is None
        assert child.find("TX-PDU-TRIGGERING-REF") is None

    def test_round_trip_write_then_read(self, writer, parser):
        parent = _parent()
        writer.writeDltLogChannel(parent, _fill(DltLogChannel(None, "channel_one")))
        child = parent.find("DLT-LOG-CHANNEL")
        fragment = ET.tostring(child, encoding="unicode")

        reloaded = ET.fromstring(f"<ROOT xmlns='{NS}'>{fragment}</ROOT>")
        parsed = DltLogChannel(None, "channel_one")
        parser.readDltLogChannel(reloaded.find(f"{{{NS}}}DLT-LOG-CHANNEL"), parsed)
        assert parsed.getShortName() == "channel_one"
        context_refs = parsed.getApplicationContextRefs()
        assert len(context_refs) == 2
        assert context_refs[0].getValue() == "/LogAndTrace/DltContexts/Context1"
        assert context_refs[0].getDest() == "DLT-CONTEXT"
        assert context_refs[1].getValue() == "/LogAndTrace/DltContexts/Context2"
        assert parsed.getDefaultTraceState().getValue() == "DEFAULT-TRACE-STATE-ENABLED"
        message_refs = parsed.getDltMessageRefs()
        assert len(message_refs) == 2
        assert message_refs[0].getValue() == "/LogAndTrace/DltMessages/Message1"
        assert message_refs[0].getDest() == "DLT-MESSAGE"
        assert message_refs[1].getValue() == "/LogAndTrace/DltMessages/Message2"
        assert parsed.getLogChannelId().getValue() == "LOG1"
        assert parsed.getLogTraceDefaultLogThreshold().getValue() == "WARN"
        assert parsed.getNonVerboseMode().getValue() is True
        assert parsed.getRxPduTriggeringRef().getValue() == "/Topology/Cluster/PhysicalChannel/RxTriggering"
        assert parsed.getRxPduTriggeringRef().getDest() == "PDU-TRIGGERING"
        assert parsed.getSegmentationSupported().getValue() is False
        assert parsed.getTxPduTriggeringRef().getValue() == "/Topology/Cluster/PhysicalChannel/TxTriggering"
        assert parsed.getTxPduTriggeringRef().getDest() == "PDU-TRIGGERING"
