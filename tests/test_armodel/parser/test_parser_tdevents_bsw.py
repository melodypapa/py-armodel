"""Parser tests for TDEventBsw (Table D.56)."""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventBsw import (
    TDEventBsw,
)
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


class _ConcreteTDEventBsw(TDEventBsw):
    pass


class TestReadTDEventBsw:
    def test_read_full(self):
        AUTOSAR.getInstance().new()
        AUTOSAR.getInstance().setARRelease("R23-11")
        parent = AUTOSAR.getInstance().createARPackage("AUTOSAR")
        event = _ConcreteTDEventBsw(parent, "Bsw1")
        element = ET.fromstring(
            f"<TD-EVENT-BSW xmlns='{NS}'>"
            "<SHORT-NAME>Bsw1</SHORT-NAME>"
            "<BSW-MODULE-DESCRIPTION-REF DEST='BSW-MODULE-DESCRIPTION'>/AUTOSAR/BswModuleDescription1</BSW-MODULE-DESCRIPTION-REF>"
            "</TD-EVENT-BSW>"
        )
        ARXMLParser().readTDEventBsw(element, event)
        assert event.getShortName() == "Bsw1"
        assert event.getBswModuleDescriptionRef().getValue() == "/AUTOSAR/BswModuleDescription1"
        assert event.getBswModuleDescriptionRef().getDest() == "BSW-MODULE-DESCRIPTION"

    def test_read_minimal(self):
        AUTOSAR.getInstance().new()
        AUTOSAR.getInstance().setARRelease("R23-11")
        parent = AUTOSAR.getInstance().createARPackage("AUTOSAR")
        event = _ConcreteTDEventBsw(parent, "Bsw1")
        element = ET.fromstring(f"<TD-EVENT-BSW xmlns='{NS}'><SHORT-NAME>Bsw1</SHORT-NAME></TD-EVENT-BSW>")
        ARXMLParser().readTDEventBsw(element, event)
        assert event.getBswModuleDescriptionRef() is None
