"""Writer tests for TDEventComplex (Table 3.48)."""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventComplex import (
    TDEventComplex,
)
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


class TestWriteTDEventComplex:
    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def test_write_roundtrip(self):
        parent = self._parent()
        event = TDEventComplex(parent, "Complex1")
        element = ET.Element("TD-EVENT-COMPLEX", {"xmlns": NS})
        ARXMLWriter().writeTDEventComplex(element, event)
        reparsed_el = ET.fromstring(ET.tostring(element))
        reparsed = TDEventComplex(parent, "Complex1")
        ARXMLParser().readTDEventComplex(reparsed_el, reparsed)
        assert reparsed.getShortName() == "Complex1"
