"""Writer tests for TDEventFrame (Table 3.34)."""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventCom import (
    TDEventFrame,
    TDEventFrameTypeEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


def _build_event():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    parent = AUTOSAR.getInstance().createARPackage("AUTOSAR")
    event = TDEventFrame(parent, "Frame1")
    event.setEcuInstanceRef(RefType().setValue("/AUTOSAR/Ecu1").setDest("ECU-INSTANCE"))
    event.setFrameRef(RefType().setValue("/AUTOSAR/Frame").setDest("FRAME"))
    event.setPhysicalChannelRef(RefType().setValue("/AUTOSAR/Channel").setDest("PHYSICAL-CHANNEL"))
    enum = TDEventFrameTypeEnum()
    enum.value = TDEventFrameTypeEnum.FRAME_QUEUED_FOR_TRANSMISSION
    event.setTdEventType(enum)
    return event


class TestWriteTDEventFrame:
    def test_write_full(self):
        event = _build_event()
        element = ET.Element("TD-EVENT-FRAME", xmlns=NS)
        ARXMLWriter().writeTDEventFrame(element, event)
        out = ET.tostring(element, encoding="unicode")
        assert "FRAME-REF" in out
        assert "PHYSICAL-CHANNEL-REF" in out
        assert "TD-EVENT-TYPE" in out
        assert "frameQueuedForTransmission" in out

    def test_round_trip(self):
        event = _build_event()
        element = ET.Element("TD-EVENT-FRAME", xmlns=NS)
        ARXMLWriter().writeTDEventFrame(element, event)
        reparsed = ET.fromstring(ET.tostring(element, encoding="unicode"))
        read_back = TDEventFrame(AUTOSAR.getInstance().createARPackage("AUTOSAR"), "tmp")
        ARXMLParser().readTDEventFrame(reparsed, read_back)
        assert read_back.getFrameRef().getValue() == "/AUTOSAR/Frame"
        assert read_back.getPhysicalChannelRef().getValue() == "/AUTOSAR/Channel"
        assert read_back.getTdEventType().value == "frameQueuedForTransmission"
        assert read_back.getEcuInstanceRef().getValue() == "/AUTOSAR/Ecu1"

    def test_write_minimal(self):
        AUTOSAR.getInstance().new()
        AUTOSAR.getInstance().setARRelease("R23-11")
        parent = AUTOSAR.getInstance().createARPackage("AUTOSAR")
        event = TDEventFrame(parent, "Frame1")
        element = ET.Element("TD-EVENT-FRAME", xmlns=NS)
        ARXMLWriter().writeTDEventFrame(element, event)
        out = ET.tostring(element, encoding="unicode")
        assert "TD-EVENT-TYPE" not in out
        assert "FRAME-REF" not in out
