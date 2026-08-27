"""Writer tests for TDEventISignal (Table 3.30)."""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventCom import (
    TDEventISignal,
    TDEventISignalTypeEnum,
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
    event = TDEventISignal(parent, "ISig1")
    event.setEcuInstanceRef(RefType().setValue("/AUTOSAR/Ecu1").setDest("ECU-INSTANCE"))
    event.setISignalRef(RefType().setValue("/AUTOSAR/ISig").setDest("I-SIGNAL"))
    event.setPhysicalChannelRef(RefType().setValue("/AUTOSAR/Channel").setDest("PHYSICAL-CHANNEL"))
    enum = TDEventISignalTypeEnum()
    enum.value = TDEventISignalTypeEnum.ISIGNAL_AVAILABLE_FOR_RTE
    event.setTdEventType(enum)
    return event


class TestWriteTDEventISignal:
    def test_write_full(self):
        event = _build_event()
        element = ET.Element("TD-EVENT-I-SIGNAL", xmlns=NS)
        ARXMLWriter().writeTDEventISignal(element, event)
        out = ET.tostring(element, encoding="unicode")
        assert "I-SIGNAL-REF" in out
        assert "PHYSICAL-CHANNEL-REF" in out
        assert "TD-EVENT-TYPE" in out
        assert "iSignalAvailableForRte" in out

    def test_round_trip(self):
        event = _build_event()
        element = ET.Element("TD-EVENT-I-SIGNAL", xmlns=NS)
        ARXMLWriter().writeTDEventISignal(element, event)
        reparsed = ET.fromstring(ET.tostring(element, encoding="unicode"))
        read_back = TDEventISignal(AUTOSAR.getInstance().createARPackage("AUTOSAR"), "tmp")
        ARXMLParser().readTDEventISignal(reparsed, read_back)
        assert read_back.getISignalRef().getValue() == "/AUTOSAR/ISig"
        assert read_back.getPhysicalChannelRef().getValue() == "/AUTOSAR/Channel"
        assert read_back.getTdEventType().value == "iSignalAvailableForRte"
        assert read_back.getEcuInstanceRef().getValue() == "/AUTOSAR/Ecu1"

    def test_write_minimal(self):
        AUTOSAR.getInstance().new()
        AUTOSAR.getInstance().setARRelease("R23-11")
        parent = AUTOSAR.getInstance().createARPackage("AUTOSAR")
        event = TDEventISignal(parent, "ISig1")
        element = ET.Element("TD-EVENT-I-SIGNAL", xmlns=NS)
        ARXMLWriter().writeTDEventISignal(element, event)
        out = ET.tostring(element, encoding="unicode")
        assert "TD-EVENT-TYPE" not in out
        assert "I-SIGNAL-REF" not in out
