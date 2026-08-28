"""Writer tests for TDEventBswModule (Table 3.44)."""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventBsw import (
    TDEventBswModule,
    TDEventBswModuleTypeEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


class TestWriteTDEventBswModule:
    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def test_write_bsw_module_entry_ref(self):
        parent = self._parent()
        event = TDEventBswModule(parent, "BswModule1")
        event.setBswModuleEntryRef(RefType().setValue("/AUTOSAR/BswModuleEntry1").setDest("BSW-MODULE-ENTRY"))
        element = ET.Element("TD-EVENT-BSW-MODULE")
        ARXMLWriter().writeTDEventBswModule(element, event)
        ref = element.find("BSW-MODULE-ENTRY-REF")
        assert ref is not None
        assert ref.text == "/AUTOSAR/BswModuleEntry1"
        assert ref.attrib["DEST"] == "BSW-MODULE-ENTRY"

    def test_write_td_event_type(self):
        parent = self._parent()
        event = TDEventBswModule(parent, "BswModule1")
        enum = TDEventBswModuleTypeEnum()
        enum.setValue(TDEventBswModuleTypeEnum.BSW_M_ENTRY_CALL_RETURNED)
        event.setTdEventBswModuleType(enum)
        element = ET.Element("TD-EVENT-BSW-MODULE")
        ARXMLWriter().writeTDEventBswModule(element, event)
        type_el = element.find("TD-EVENT-BSW-MODULE-TYPE")
        assert type_el is not None
        assert type_el.text == "bswMEntryCallReturned"

    def test_write_empty(self):
        parent = self._parent()
        event = TDEventBswModule(parent, "BswModule1")
        element = ET.Element("TD-EVENT-BSW-MODULE")
        ARXMLWriter().writeTDEventBswModule(element, event)
        assert element.find("BSW-MODULE-ENTRY-REF") is None
        assert element.find("TD-EVENT-BSW-MODULE-TYPE") is None

    def test_write_roundtrip(self):
        parent = self._parent()
        event = TDEventBswModule(parent, "BswModule1")
        event.setBswModuleEntryRef(RefType().setValue("/AUTOSAR/BswModuleEntry1").setDest("BSW-MODULE-ENTRY"))
        enum = TDEventBswModuleTypeEnum()
        enum.setValue(TDEventBswModuleTypeEnum.BSW_M_ENTRY_CALLED)
        event.setTdEventBswModuleType(enum)
        element = ET.Element("TD-EVENT-BSW-MODULE", {"xmlns": NS})
        ARXMLWriter().writeTDEventBswModule(element, event)
        reparsed_el = ET.fromstring(ET.tostring(element))
        reparsed = TDEventBswModule(parent, "BswModule1")
        ARXMLParser().readTDEventBswModule(reparsed_el, reparsed)
        assert reparsed.getBswModuleEntryRef().getValue() == "/AUTOSAR/BswModuleEntry1"
        assert reparsed.getBswModuleEntryRef().getDest() == "BSW-MODULE-ENTRY"
        assert reparsed.getTdEventBswModuleType().getValue() == "bswMEntryCalled"
