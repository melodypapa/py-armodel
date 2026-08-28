"""Parser tests for TDEventBswModeDeclaration (Table 3.46)."""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventBsw import (
    TDEventBswModeDeclaration,
)
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


class TestReadTDEventBswModeDeclaration:
    def test_read_full(self):
        AUTOSAR.getInstance().new()
        AUTOSAR.getInstance().setARRelease("R23-11")
        parent = AUTOSAR.getInstance().createARPackage("AUTOSAR")
        event = TDEventBswModeDeclaration(parent, "BswMode1")
        element = ET.fromstring(
            f"<TD-EVENT-BSW-MODE-DECLARATION xmlns='{NS}'>"
            "<SHORT-NAME>BswMode1</SHORT-NAME>"
            "<ENTRY-MODE-DECLARATION-REF DEST='MODE-DECLARATION'>/AUTOSAR/EntryMode</ENTRY-MODE-DECLARATION-REF>"
            "<EXIT-MODE-DECLARATION-REF DEST='MODE-DECLARATION'>/AUTOSAR/ExitMode</EXIT-MODE-DECLARATION-REF>"
            "<MODE-DECLARATION-REF DEST='MODE-DECLARATION-GROUP-PROTOTYPE'>/AUTOSAR/ModeGroup</MODE-DECLARATION-REF>"
            "<TD-EVENT-BSW-MODE-DECLARATION-TYPE>modeDeclarationRequested</TD-EVENT-BSW-MODE-DECLARATION-TYPE>"
            "</TD-EVENT-BSW-MODE-DECLARATION>"
        )
        ARXMLParser().readTDEventBswModeDeclaration(element, event)
        assert event.getShortName() == "BswMode1"
        assert event.getEntryModeDeclarationRef().getValue() == "/AUTOSAR/EntryMode"
        assert event.getExitModeDeclarationRef().getValue() == "/AUTOSAR/ExitMode"
        assert event.getModeDeclarationRef().getValue() == "/AUTOSAR/ModeGroup"
        assert event.getModeDeclarationRef().getDest() == "MODE-DECLARATION-GROUP-PROTOTYPE"
        assert event.getTdEventBswModeDeclarationType().getValue() == "modeDeclarationRequested"

    def test_read_minimal(self):
        AUTOSAR.getInstance().new()
        AUTOSAR.getInstance().setARRelease("R23-11")
        parent = AUTOSAR.getInstance().createARPackage("AUTOSAR")
        event = TDEventBswModeDeclaration(parent, "BswMode1")
        element = ET.fromstring(f"<TD-EVENT-BSW-MODE-DECLARATION xmlns='{NS}'><SHORT-NAME>BswMode1</SHORT-NAME></TD-EVENT-BSW-MODE-DECLARATION>")
        ARXMLParser().readTDEventBswModeDeclaration(element, event)
        assert event.getEntryModeDeclarationRef() is None
        assert event.getExitModeDeclarationRef() is None
        assert event.getModeDeclarationRef() is None
        assert event.getTdEventBswModeDeclarationType() is None
