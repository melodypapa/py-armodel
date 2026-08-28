"""Writer tests for TDEventBswModeDeclaration (Table 3.46)."""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventBsw import (
    TDEventBswModeDeclaration,
    TDEventBswModeDeclarationTypeEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


class TestWriteTDEventBswModeDeclaration:
    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def test_write_refs(self):
        parent = self._parent()
        event = TDEventBswModeDeclaration(parent, "BswMode1")
        event.setEntryModeDeclarationRef(RefType().setValue("/AUTOSAR/EntryMode").setDest("MODE-DECLARATION"))
        event.setExitModeDeclarationRef(RefType().setValue("/AUTOSAR/ExitMode").setDest("MODE-DECLARATION"))
        event.setModeDeclarationRef(RefType().setValue("/AUTOSAR/ModeGroup").setDest("MODE-DECLARATION-GROUP-PROTOTYPE"))
        element = ET.Element("TD-EVENT-BSW-MODE-DECLARATION")
        ARXMLWriter().writeTDEventBswModeDeclaration(element, event)
        assert element.find("ENTRY-MODE-DECLARATION-REF").text == "/AUTOSAR/EntryMode"
        assert element.find("EXIT-MODE-DECLARATION-REF").text == "/AUTOSAR/ExitMode"
        mode_ref = element.find("MODE-DECLARATION-REF")
        assert mode_ref.text == "/AUTOSAR/ModeGroup"
        assert mode_ref.attrib["DEST"] == "MODE-DECLARATION-GROUP-PROTOTYPE"

    def test_write_td_event_type(self):
        parent = self._parent()
        event = TDEventBswModeDeclaration(parent, "BswMode1")
        enum = TDEventBswModeDeclarationTypeEnum()
        enum.setValue(TDEventBswModeDeclarationTypeEnum.MODE_DECLARATION_SWITCH_INITIATED)
        event.setTdEventBswModeDeclarationType(enum)
        element = ET.Element("TD-EVENT-BSW-MODE-DECLARATION")
        ARXMLWriter().writeTDEventBswModeDeclaration(element, event)
        type_el = element.find("TD-EVENT-BSW-MODE-DECLARATION-TYPE")
        assert type_el is not None
        assert type_el.text == "modeDeclarationSwitchInitiated"

    def test_write_empty(self):
        parent = self._parent()
        event = TDEventBswModeDeclaration(parent, "BswMode1")
        element = ET.Element("TD-EVENT-BSW-MODE-DECLARATION")
        ARXMLWriter().writeTDEventBswModeDeclaration(element, event)
        assert element.find("ENTRY-MODE-DECLARATION-REF") is None
        assert element.find("EXIT-MODE-DECLARATION-REF") is None
        assert element.find("MODE-DECLARATION-REF") is None
        assert element.find("TD-EVENT-BSW-MODE-DECLARATION-TYPE") is None

    def test_write_roundtrip(self):
        parent = self._parent()
        event = TDEventBswModeDeclaration(parent, "BswMode1")
        event.setEntryModeDeclarationRef(RefType().setValue("/AUTOSAR/EntryMode").setDest("MODE-DECLARATION"))
        event.setModeDeclarationRef(RefType().setValue("/AUTOSAR/ModeGroup").setDest("MODE-DECLARATION-GROUP-PROTOTYPE"))
        enum = TDEventBswModeDeclarationTypeEnum()
        enum.setValue(TDEventBswModeDeclarationTypeEnum.MODE_DECLARATION_REQUESTED)
        event.setTdEventBswModeDeclarationType(enum)
        element = ET.Element("TD-EVENT-BSW-MODE-DECLARATION", {"xmlns": NS})
        ARXMLWriter().writeTDEventBswModeDeclaration(element, event)
        reparsed_el = ET.fromstring(ET.tostring(element))
        reparsed = TDEventBswModeDeclaration(parent, "BswMode1")
        ARXMLParser().readTDEventBswModeDeclaration(reparsed_el, reparsed)
        assert reparsed.getEntryModeDeclarationRef().getValue() == "/AUTOSAR/EntryMode"
        assert reparsed.getModeDeclarationRef().getDest() == "MODE-DECLARATION-GROUP-PROTOTYPE"
        assert reparsed.getTdEventBswModeDeclarationType().getValue() == "modeDeclarationRequested"
