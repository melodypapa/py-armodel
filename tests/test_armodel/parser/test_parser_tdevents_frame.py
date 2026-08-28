"""Parser tests for TDEventFrame (Table 3.34)."""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventCom import (
    TDEventFrame,
)
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


class TestReadTDEventFrame:
    def test_read_full(self):
        AUTOSAR.getInstance().new()
        AUTOSAR.getInstance().setARRelease("R23-11")
        parent = AUTOSAR.getInstance().createARPackage("AUTOSAR")
        event = TDEventFrame(parent, "Frame1")
        element = ET.fromstring(
            f"<TD-EVENT-FRAME xmlns='{NS}'>"
            "<SHORT-NAME>Frame1</SHORT-NAME>"
            "<ECU-INSTANCE-REF DEST='ECU-INSTANCE'>/AUTOSAR/Ecu1</ECU-INSTANCE-REF>"
            "<FRAME-REF DEST='FRAME'>/AUTOSAR/Frame</FRAME-REF>"
            "<PHYSICAL-CHANNEL-REF DEST='PHYSICAL-CHANNEL'>/AUTOSAR/Channel</PHYSICAL-CHANNEL-REF>"
            "<TD-EVENT-TYPE>frameQueuedForTransmission</TD-EVENT-TYPE>"
            "</TD-EVENT-FRAME>"
        )
        ARXMLParser().readTDEventFrame(element, event)
        assert event.getShortName() == "Frame1"
        assert event.getEcuInstanceRef().getValue() == "/AUTOSAR/Ecu1"
        assert event.getFrameRef().getValue() == "/AUTOSAR/Frame"
        assert event.getFrameRef().getDest() == "FRAME"
        assert event.getPhysicalChannelRef().getValue() == "/AUTOSAR/Channel"
        assert event.getPhysicalChannelRef().getDest() == "PHYSICAL-CHANNEL"
        assert event.getTdEventType().value == "frameQueuedForTransmission"

    def test_read_minimal(self):
        AUTOSAR.getInstance().new()
        AUTOSAR.getInstance().setARRelease("R23-11")
        parent = AUTOSAR.getInstance().createARPackage("AUTOSAR")
        event = TDEventFrame(parent, "Frame1")
        element = ET.fromstring(f"<TD-EVENT-FRAME xmlns='{NS}'><SHORT-NAME>Frame1</SHORT-NAME></TD-EVENT-FRAME>")
        ARXMLParser().readTDEventFrame(element, event)
        assert event.getFrameRef() is None
        assert event.getPhysicalChannelRef() is None
        assert event.getTdEventType() is None
