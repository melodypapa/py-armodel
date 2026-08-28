"""Parser tests for TDEventComplex (Table 3.48)."""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventComplex import (
    TDEventComplex,
)
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


class TestReadTDEventComplex:
    def test_read_full(self):
        AUTOSAR.getInstance().new()
        AUTOSAR.getInstance().setARRelease("R23-11")
        parent = AUTOSAR.getInstance().createARPackage("AUTOSAR")
        event = TDEventComplex(parent, "Complex1")
        element = ET.fromstring(f"<TD-EVENT-COMPLEX xmlns='{NS}'>" "<SHORT-NAME>Complex1</SHORT-NAME>" "</TD-EVENT-COMPLEX>")
        ARXMLParser().readTDEventComplex(element, event)
        assert event.getShortName() == "Complex1"
