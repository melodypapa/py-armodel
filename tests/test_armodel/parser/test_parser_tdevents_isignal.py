"""Parser tests for TDEventISignal (Table 3.30)."""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventCom import (
    TDEventISignal,
)
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


class TestReadTDEventISignal:
    def test_read_full(self):
        AUTOSAR.getInstance().new()
        AUTOSAR.getInstance().setARRelease("R23-11")
        parent = AUTOSAR.getInstance().createARPackage("AUTOSAR")
        event = TDEventISignal(parent, "ISig1")
        element = ET.fromstring(
            f"<TD-EVENT-I-SIGNAL xmlns='{NS}'>"
            "<SHORT-NAME>ISig1</SHORT-NAME>"
            "<ECU-INSTANCE-REF DEST='ECU-INSTANCE'>/AUTOSAR/Ecu1</ECU-INSTANCE-REF>"
            "<I-SIGNAL-REF DEST='I-SIGNAL'>/AUTOSAR/ISig</I-SIGNAL-REF>"
            "<PHYSICAL-CHANNEL-REF DEST='PHYSICAL-CHANNEL'>/AUTOSAR/Channel</PHYSICAL-CHANNEL-REF>"
            "<TD-EVENT-TYPE>iSignalAvailableForRte</TD-EVENT-TYPE>"
            "</TD-EVENT-I-SIGNAL>"
        )
        ARXMLParser().readTDEventISignal(element, event)
        assert event.getShortName() == "ISig1"
        assert event.getEcuInstanceRef().getValue() == "/AUTOSAR/Ecu1"
        assert event.getISignalRef().getValue() == "/AUTOSAR/ISig"
        assert event.getISignalRef().getDest() == "I-SIGNAL"
        assert event.getPhysicalChannelRef().getValue() == "/AUTOSAR/Channel"
        assert event.getPhysicalChannelRef().getDest() == "PHYSICAL-CHANNEL"
        assert event.getTdEventType().value == "iSignalAvailableForRte"

    def test_read_minimal(self):
        AUTOSAR.getInstance().new()
        AUTOSAR.getInstance().setARRelease("R23-11")
        parent = AUTOSAR.getInstance().createARPackage("AUTOSAR")
        event = TDEventISignal(parent, "ISig1")
        element = ET.fromstring(f"<TD-EVENT-I-SIGNAL xmlns='{NS}'><SHORT-NAME>ISig1</SHORT-NAME></TD-EVENT-I-SIGNAL>")
        ARXMLParser().readTDEventISignal(element, event)
        assert event.getISignalRef() is None
        assert event.getPhysicalChannelRef() is None
        assert event.getTdEventType() is None
