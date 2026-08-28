"""Parser tests for TDEventBswInternalBehavior (Table 3.42)."""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventBswInternalBehavior import (
    TDEventBswInternalBehavior,
)
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


class TestReadTDEventBswInternalBehavior:
    def test_read_full(self):
        AUTOSAR.getInstance().new()
        AUTOSAR.getInstance().setARRelease("R23-11")
        parent = AUTOSAR.getInstance().createARPackage("AUTOSAR")
        event = TDEventBswInternalBehavior(parent, "Bsw1")
        element = ET.fromstring(
            f"<TD-EVENT-BSW-INTERNAL-BEHAVIOR xmlns='{NS}'>"
            "<SHORT-NAME>Bsw1</SHORT-NAME>"
            "<BSW-MODULE-ENTITY-REF DEST='BSW-MODULE-ENTITY'>/AUTOSAR/BswModuleEntity1</BSW-MODULE-ENTITY-REF>"
            "<TD-EVENT-BSW-INTERNAL-BEHAVIOR-TYPE>bswModuleEntityActivated</TD-EVENT-BSW-INTERNAL-BEHAVIOR-TYPE>"
            "</TD-EVENT-BSW-INTERNAL-BEHAVIOR>"
        )
        ARXMLParser().readTDEventBswInternalBehavior(element, event)
        assert event.getShortName() == "Bsw1"
        assert event.getBswModuleEntityRef().getValue() == "/AUTOSAR/BswModuleEntity1"
        assert event.getBswModuleEntityRef().getDest() == "BSW-MODULE-ENTITY"
        assert event.getTdEventBswInternalBehaviorType().getValue() == "bswModuleEntityActivated"

    def test_read_minimal(self):
        AUTOSAR.getInstance().new()
        AUTOSAR.getInstance().setARRelease("R23-11")
        parent = AUTOSAR.getInstance().createARPackage("AUTOSAR")
        event = TDEventBswInternalBehavior(parent, "Bsw1")
        element = ET.fromstring(f"<TD-EVENT-BSW-INTERNAL-BEHAVIOR xmlns='{NS}'><SHORT-NAME>Bsw1</SHORT-NAME></TD-EVENT-BSW-INTERNAL-BEHAVIOR>")
        ARXMLParser().readTDEventBswInternalBehavior(element, event)
        assert event.getBswModuleEntityRef() is None
        assert event.getTdEventBswInternalBehaviorType() is None
