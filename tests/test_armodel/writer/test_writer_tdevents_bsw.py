"""Writer tests for TDEventBsw (Table D.56)."""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventBsw import (
    TDEventBsw,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


class _ConcreteTDEventBsw(TDEventBsw):
    pass


class TestWriteTDEventBsw:
    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def test_write_bsw_module_description_ref(self):
        parent = self._parent()
        event = _ConcreteTDEventBsw(parent, "Bsw1")
        event.setBswModuleDescriptionRef(RefType().setValue("/AUTOSAR/BswModuleDescription1").setDest("BSW-MODULE-DESCRIPTION"))
        element = ET.Element("TD-EVENT-BSW")
        ARXMLWriter().writeTDEventBsw(element, event)
        ref = element.find("BSW-MODULE-DESCRIPTION-REF")
        assert ref is not None
        assert ref.text == "/AUTOSAR/BswModuleDescription1"
        assert ref.attrib["DEST"] == "BSW-MODULE-DESCRIPTION"

    def test_write_empty(self):
        parent = self._parent()
        event = _ConcreteTDEventBsw(parent, "Bsw1")
        element = ET.Element("TD-EVENT-BSW")
        ARXMLWriter().writeTDEventBsw(element, event)
        assert element.find("BSW-MODULE-DESCRIPTION-REF") is None

    def test_write_roundtrip(self):
        parent = self._parent()
        event = _ConcreteTDEventBsw(parent, "Bsw1")
        event.setBswModuleDescriptionRef(RefType().setValue("/AUTOSAR/BswModuleDescription1").setDest("BSW-MODULE-DESCRIPTION"))
        element = ET.Element("TD-EVENT-BSW", {"xmlns": NS})
        ARXMLWriter().writeTDEventBsw(element, event)
        reparsed_el = ET.fromstring(ET.tostring(element))
        reparsed = _ConcreteTDEventBsw(parent, "Bsw1")
        ARXMLParser().readTDEventBsw(reparsed_el, reparsed)
        assert reparsed.getBswModuleDescriptionRef().getValue() == "/AUTOSAR/BswModuleDescription1"
        assert reparsed.getBswModuleDescriptionRef().getDest() == "BSW-MODULE-DESCRIPTION"
