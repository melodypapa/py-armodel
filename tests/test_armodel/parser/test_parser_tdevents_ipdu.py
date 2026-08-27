"""Parser tests for TDEventIPdu (Table 3.32)."""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventCom import (
    TDEventIPdu,
)
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


class TestReadTDEventIPdu:
    def test_read_full(self):
        AUTOSAR.getInstance().new()
        AUTOSAR.getInstance().setARRelease("R23-11")
        parent = AUTOSAR.getInstance().createARPackage("AUTOSAR")
        event = TDEventIPdu(parent, "IPdu1")
        element = ET.fromstring(
            f"<TD-EVENT-I-PDU xmlns='{NS}'>"
            "<SHORT-NAME>IPdu1</SHORT-NAME>"
            "<ECU-INSTANCE-REF DEST='ECU-INSTANCE'>/AUTOSAR/Ecu1</ECU-INSTANCE-REF>"
            "<I-PDU-REF DEST='I-PDU'>/AUTOSAR/IPdu</I-PDU-REF>"
            "<PHYSICAL-CHANNEL-REF DEST='PHYSICAL-CHANNEL'>/AUTOSAR/Channel</PHYSICAL-CHANNEL-REF>"
            "<TD-EVENT-TYPE>iPduReceivedByCom</TD-EVENT-TYPE>"
            "</TD-EVENT-I-PDU>"
        )
        ARXMLParser().readTDEventIPdu(element, event)
        assert event.getShortName() == "IPdu1"
        assert event.getEcuInstanceRef().getValue() == "/AUTOSAR/Ecu1"
        assert event.getIPduRef().getValue() == "/AUTOSAR/IPdu"
        assert event.getIPduRef().getDest() == "I-PDU"
        assert event.getPhysicalChannelRef().getValue() == "/AUTOSAR/Channel"
        assert event.getPhysicalChannelRef().getDest() == "PHYSICAL-CHANNEL"
        assert event.getTdEventType().value == "iPduReceivedByCom"

    def test_read_minimal(self):
        AUTOSAR.getInstance().new()
        AUTOSAR.getInstance().setARRelease("R23-11")
        parent = AUTOSAR.getInstance().createARPackage("AUTOSAR")
        event = TDEventIPdu(parent, "IPdu1")
        element = ET.fromstring(f"<TD-EVENT-I-PDU xmlns='{NS}'><SHORT-NAME>IPdu1</SHORT-NAME></TD-EVENT-I-PDU>")
        ARXMLParser().readTDEventIPdu(element, event)
        assert event.getIPduRef() is None
        assert event.getPhysicalChannelRef() is None
        assert event.getTdEventType() is None
