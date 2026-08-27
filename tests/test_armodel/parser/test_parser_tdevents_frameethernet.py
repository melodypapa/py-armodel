"""Parser tests for TDEventFrameEthernet (Table 3.36)."""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventCom import (
    TDEventFrameEthernet,
)
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


class TestReadTDEventFrameEthernet:
    def test_read_full(self):
        AUTOSAR.getInstance().new()
        AUTOSAR.getInstance().setARRelease("R23-11")
        parent = AUTOSAR.getInstance().createARPackage("AUTOSAR")
        event = TDEventFrameEthernet(parent, "Eth1")
        element = ET.fromstring(
            f"<TD-EVENT-FRAME-ETHERNET xmlns='{NS}'>"
            "<SHORT-NAME>Eth1</SHORT-NAME>"
            "<ECU-INSTANCE-REF DEST='ECU-INSTANCE'>/AUTOSAR/Ecu1</ECU-INSTANCE-REF>"
            "<STATIC-SOCKET-CONNECTION-REF DEST='STATIC-SOCKET-CONNECTION'>/AUTOSAR/Socket</STATIC-SOCKET-CONNECTION-REF>"
            "<TD-EVENT-TYPE>frameEthernetQueuedForTransmission</TD-EVENT-TYPE>"
            "<TD-HEADER-ID-FILTERS>"
            "<TD-HEADER-ID-RANGE><MIN-HEADER-ID>5</MIN-HEADER-ID><MAX-HEADER-ID>10</MAX-HEADER-ID></TD-HEADER-ID-RANGE>"
            "</TD-HEADER-ID-FILTERS>"
            "<TD-PDU-TRIGGERING-FILTER-REFS>"
            "<TD-PDU-TRIGGERING-FILTER-REF DEST='PDU-TRIGGERING'>/AUTOSAR/Pdu</TD-PDU-TRIGGERING-FILTER-REF>"
            "</TD-PDU-TRIGGERING-FILTER-REFS>"
            "</TD-EVENT-FRAME-ETHERNET>"
        )
        ARXMLParser().readTDEventFrameEthernet(element, event)
        assert event.getShortName() == "Eth1"
        assert event.getEcuInstanceRef().getValue() == "/AUTOSAR/Ecu1"
        assert event.getStaticSocketConnectionRef().getValue() == "/AUTOSAR/Socket"
        assert event.getStaticSocketConnectionRef().getDest() == "STATIC-SOCKET-CONNECTION"
        assert event.getTdEventType().value == "frameEthernetQueuedForTransmission"
        assert len(event.getTdHeaderIdFilter()) == 1
        assert event.getTdHeaderIdFilter()[0].getMinHeaderId().getValue() == 5
        assert event.getTdHeaderIdFilter()[0].getMaxHeaderId().getValue() == 10
        assert len(event.getTdPduTriggeringFilterRefs()) == 1
        assert event.getTdPduTriggeringFilterRefs()[0].getValue() == "/AUTOSAR/Pdu"

    def test_read_minimal(self):
        AUTOSAR.getInstance().new()
        AUTOSAR.getInstance().setARRelease("R23-11")
        parent = AUTOSAR.getInstance().createARPackage("AUTOSAR")
        event = TDEventFrameEthernet(parent, "Eth1")
        element = ET.fromstring(f"<TD-EVENT-FRAME-ETHERNET xmlns='{NS}'><SHORT-NAME>Eth1</SHORT-NAME></TD-EVENT-FRAME-ETHERNET>")
        ARXMLParser().readTDEventFrameEthernet(element, event)
        assert event.getStaticSocketConnectionRef() is None
        assert event.getTdEventType() is None
        assert event.getTdHeaderIdFilter() == []
        assert event.getTdPduTriggeringFilterRefs() == []
