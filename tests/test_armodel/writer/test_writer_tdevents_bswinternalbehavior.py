"""Writer tests for TDEventBswInternalBehavior (Table 3.42)."""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventBswInternalBehavior import (
    TDEventBswInternalBehavior,
    TDEventBswInternalBehaviorTypeEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


class TestWriteTDEventBswInternalBehavior:
    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def test_write_bsw_module_entity_ref(self):
        parent = self._parent()
        event = TDEventBswInternalBehavior(parent, "Bsw1")
        event.setBswModuleEntityRef(RefType().setValue("/AUTOSAR/BswModuleEntity1").setDest("BSW-MODULE-ENTITY"))
        element = ET.Element("TD-EVENT-BSW-INTERNAL-BEHAVIOR")
        ARXMLWriter().writeTDEventBswInternalBehavior(element, event)
        ref = element.find("BSW-MODULE-ENTITY-REF")
        assert ref is not None
        assert ref.text == "/AUTOSAR/BswModuleEntity1"
        assert ref.attrib["DEST"] == "BSW-MODULE-ENTITY"

    def test_write_td_event_type(self):
        parent = self._parent()
        event = TDEventBswInternalBehavior(parent, "Bsw1")
        enum = TDEventBswInternalBehaviorTypeEnum()
        enum.setValue(TDEventBswInternalBehaviorTypeEnum.BSW_MODULE_ENTITY_TERMINATED)
        event.setTdEventBswInternalBehaviorType(enum)
        element = ET.Element("TD-EVENT-BSW-INTERNAL-BEHAVIOR")
        ARXMLWriter().writeTDEventBswInternalBehavior(element, event)
        type_el = element.find("TD-EVENT-BSW-INTERNAL-BEHAVIOR-TYPE")
        assert type_el is not None
        assert type_el.text == "bswModuleEntityTerminated"

    def test_write_roundtrip(self):
        parent = self._parent()
        event = TDEventBswInternalBehavior(parent, "Bsw1")
        event.setBswModuleEntityRef(RefType().setValue("/AUTOSAR/BswModuleEntity1").setDest("BSW-MODULE-ENTITY"))
        enum = TDEventBswInternalBehaviorTypeEnum()
        enum.setValue(TDEventBswInternalBehaviorTypeEnum.BSW_MODULE_ENTITY_STARTED)
        event.setTdEventBswInternalBehaviorType(enum)
        element = ET.Element("TD-EVENT-BSW-INTERNAL-BEHAVIOR", {"xmlns": NS})
        ARXMLWriter().writeTDEventBswInternalBehavior(element, event)
        reparsed_el = ET.fromstring(ET.tostring(element))
        reparsed = TDEventBswInternalBehavior(parent, "Bsw1")
        ARXMLParser().readTDEventBswInternalBehavior(reparsed_el, reparsed)
        assert reparsed.getBswModuleEntityRef().getValue() == "/AUTOSAR/BswModuleEntity1"
        assert reparsed.getBswModuleEntityRef().getDest() == "BSW-MODULE-ENTITY"
        assert reparsed.getTdEventBswInternalBehaviorType().getValue() == "bswModuleEntityStarted"

    def test_write_empty(self):
        parent = self._parent()
        event = TDEventBswInternalBehavior(parent, "Bsw1")
        element = ET.Element("TD-EVENT-BSW-INTERNAL-BEHAVIOR")
        ARXMLWriter().writeTDEventBswInternalBehavior(element, event)
        assert element.find("BSW-MODULE-ENTITY-REF") is None
        assert element.find("TD-EVENT-BSW-INTERNAL-BEHAVIOR-TYPE") is None
