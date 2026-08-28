"""Writer tests for TDEventIPdu (Table 3.32)."""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventCom import (
    TDEventIPdu,
    TDEventIPduTypeEnum,
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
    event = TDEventIPdu(parent, "IPdu1")
    event.setEcuInstanceRef(RefType().setValue("/AUTOSAR/Ecu1").setDest("ECU-INSTANCE"))
    event.setIPduRef(RefType().setValue("/AUTOSAR/IPdu").setDest("I-PDU"))
    event.setPhysicalChannelRef(RefType().setValue("/AUTOSAR/Channel").setDest("PHYSICAL-CHANNEL"))
    enum = TDEventIPduTypeEnum()
    enum.value = TDEventIPduTypeEnum.IPDU_RECEIVED_BY_COM
    event.setTdEventType(enum)
    return event


class TestWriteTDEventIPdu:
    def test_write_full(self):
        event = _build_event()
        element = ET.Element("TD-EVENT-I-PDU", xmlns=NS)
        ARXMLWriter().writeTDEventIPdu(element, event)
        out = ET.tostring(element, encoding="unicode")
        assert "I-PDU-REF" in out
        assert "PHYSICAL-CHANNEL-REF" in out
        assert "TD-EVENT-TYPE" in out
        assert "iPduReceivedByCom" in out

    def test_round_trip(self):
        event = _build_event()
        element = ET.Element("TD-EVENT-I-PDU", xmlns=NS)
        ARXMLWriter().writeTDEventIPdu(element, event)
        reparsed = ET.fromstring(ET.tostring(element, encoding="unicode"))
        read_back = TDEventIPdu(AUTOSAR.getInstance().createARPackage("AUTOSAR"), "tmp")
        ARXMLParser().readTDEventIPdu(reparsed, read_back)
        assert read_back.getIPduRef().getValue() == "/AUTOSAR/IPdu"
        assert read_back.getPhysicalChannelRef().getValue() == "/AUTOSAR/Channel"
        assert read_back.getTdEventType().value == "iPduReceivedByCom"
        assert read_back.getEcuInstanceRef().getValue() == "/AUTOSAR/Ecu1"

    def test_write_minimal(self):
        AUTOSAR.getInstance().new()
        AUTOSAR.getInstance().setARRelease("R23-11")
        parent = AUTOSAR.getInstance().createARPackage("AUTOSAR")
        event = TDEventIPdu(parent, "IPdu1")
        element = ET.Element("TD-EVENT-I-PDU", xmlns=NS)
        ARXMLWriter().writeTDEventIPdu(element, event)
        out = ET.tostring(element, encoding="unicode")
        assert "TD-EVENT-TYPE" not in out
        assert "I-PDU-REF" not in out
