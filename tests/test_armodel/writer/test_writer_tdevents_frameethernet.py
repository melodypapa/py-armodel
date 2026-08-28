"""Writer tests for TDEventFrameEthernet (Table 3.36)."""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventCom import (
    TDEventFrameEthernet,
    TDEventFrameEthernetTypeEnum,
    TDHeaderIdRange,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
    RefType,
)
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


def _build_event():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    parent = AUTOSAR.getInstance().createARPackage("AUTOSAR")
    event = TDEventFrameEthernet(parent, "Eth1")
    event.setEcuInstanceRef(RefType().setValue("/AUTOSAR/Ecu1").setDest("ECU-INSTANCE"))
    event.setStaticSocketConnectionRef(RefType().setValue("/AUTOSAR/Socket").setDest("STATIC-SOCKET-CONNECTION"))
    enum = TDEventFrameEthernetTypeEnum()
    enum.value = TDEventFrameEthernetTypeEnum.FRAME_ETHERNET_QUEUED_FOR_TRANSMISSION
    event.setTdEventType(enum)
    rng = TDHeaderIdRange()
    rng.setMinHeaderId(Integer().setValue("5"))
    rng.setMaxHeaderId(Integer().setValue("10"))
    event.addTDHeaderIdFilter(rng)
    event.addTdPduTriggeringFilterRef(RefType().setValue("/AUTOSAR/Pdu").setDest("PDU-TRIGGERING"))
    return event


class TestWriteTDEventFrameEthernet:
    def test_write_full(self):
        event = _build_event()
        element = ET.Element("TD-EVENT-FRAME-ETHERNET", xmlns=NS)
        ARXMLWriter().writeTDEventFrameEthernet(element, event)
        out = ET.tostring(element, encoding="unicode")
        assert "STATIC-SOCKET-CONNECTION-REF" in out
        assert "TD-EVENT-TYPE" in out
        assert "TD-HEADER-ID-FILTERS" in out
        assert "TD-HEADER-ID-RANGE" in out
        assert "TD-PDU-TRIGGERING-FILTER-REFS" in out
        assert "frameEthernetQueuedForTransmission" in out

    def test_round_trip(self):
        event = _build_event()
        element = ET.Element("TD-EVENT-FRAME-ETHERNET", xmlns=NS)
        ARXMLWriter().writeTDEventFrameEthernet(element, event)
        reparsed = ET.fromstring(ET.tostring(element, encoding="unicode"))
        read_back = TDEventFrameEthernet(AUTOSAR.getInstance().createARPackage("AUTOSAR"), "tmp")
        ARXMLParser().readTDEventFrameEthernet(reparsed, read_back)
        assert read_back.getStaticSocketConnectionRef().getValue() == "/AUTOSAR/Socket"
        assert read_back.getTdEventType().value == "frameEthernetQueuedForTransmission"
        assert len(read_back.getTdHeaderIdFilter()) == 1
        assert read_back.getTdHeaderIdFilter()[0].getMinHeaderId().getValue() == 5
        assert read_back.getTdHeaderIdFilter()[0].getMaxHeaderId().getValue() == 10
        assert read_back.getTdPduTriggeringFilterRefs()[0].getValue() == "/AUTOSAR/Pdu"
        assert read_back.getEcuInstanceRef().getValue() == "/AUTOSAR/Ecu1"

    def test_write_minimal(self):
        AUTOSAR.getInstance().new()
        AUTOSAR.getInstance().setARRelease("R23-11")
        parent = AUTOSAR.getInstance().createARPackage("AUTOSAR")
        event = TDEventFrameEthernet(parent, "Eth1")
        element = ET.Element("TD-EVENT-FRAME-ETHERNET", xmlns=NS)
        ARXMLWriter().writeTDEventFrameEthernet(element, event)
        out = ET.tostring(element, encoding="unicode")
        assert "STATIC-SOCKET-CONNECTION-REF" not in out
        assert "TD-HEADER-ID-FILTERS" not in out
        assert "TD-PDU-TRIGGERING-FILTER-REFS" not in out
