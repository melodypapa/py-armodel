"""Parser tests for TDEventBswModule (Table 3.44)."""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventBsw import (
    TDEventBswModule,
)
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


class TestReadTDEventBswModule:
    def test_read_full(self):
        AUTOSAR.getInstance().new()
        AUTOSAR.getInstance().setARRelease("R23-11")
        parent = AUTOSAR.getInstance().createARPackage("AUTOSAR")
        event = TDEventBswModule(parent, "BswModule1")
        element = ET.fromstring(
            f"<TD-EVENT-BSW-MODULE xmlns='{NS}'>"
            "<SHORT-NAME>BswModule1</SHORT-NAME>"
            "<BSW-MODULE-ENTRY-REF DEST='BSW-MODULE-ENTRY'>/AUTOSAR/BswModuleEntry1</BSW-MODULE-ENTRY-REF>"
            "<TD-EVENT-BSW-MODULE-TYPE>bswMEntryCalled</TD-EVENT-BSW-MODULE-TYPE>"
            "</TD-EVENT-BSW-MODULE>"
        )
        ARXMLParser().readTDEventBswModule(element, event)
        assert event.getShortName() == "BswModule1"
        assert event.getBswModuleEntryRef().getValue() == "/AUTOSAR/BswModuleEntry1"
        assert event.getBswModuleEntryRef().getDest() == "BSW-MODULE-ENTRY"
        assert event.getTdEventBswModuleType().getValue() == "bswMEntryCalled"

    def test_read_minimal(self):
        AUTOSAR.getInstance().new()
        AUTOSAR.getInstance().setARRelease("R23-11")
        parent = AUTOSAR.getInstance().createARPackage("AUTOSAR")
        event = TDEventBswModule(parent, "BswModule1")
        element = ET.fromstring(f"<TD-EVENT-BSW-MODULE xmlns='{NS}'><SHORT-NAME>BswModule1</SHORT-NAME></TD-EVENT-BSW-MODULE>")
        ARXMLParser().readTDEventBswModule(element, event)
        assert event.getBswModuleEntryRef() is None
        assert event.getTdEventBswModuleType() is None
