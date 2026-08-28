"""Writer tests for TDEventSLLET (Table D.57)."""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventSLLET import (
    TDEventSLLET,
)
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


class _ConcreteTDEventSLLET(TDEventSLLET):
    pass


class TestWriteTDEventSLLET:
    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def test_write_roundtrip(self):
        parent = self._parent()
        event = _ConcreteTDEventSLLET(parent, "SLLET1")
        element = ET.Element("TD-EVENT-SLLET", {"xmlns": NS})
        ARXMLWriter().writeTDEventSLLET(element, event)
        reparsed_el = ET.fromstring(ET.tostring(element))
        reparsed = _ConcreteTDEventSLLET(parent, "SLLET1")
        ARXMLParser().readTDEventSLLET(reparsed_el, reparsed)
        assert reparsed.getShortName() == "SLLET1"
