"""Parser tests for TDEventSLLET (Table D.57)."""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventSLLET import (
    TDEventSLLET,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventSLLETPort import (
    TDEventSLLETPort,
)
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


class _ConcreteTDEventSLLET(TDEventSLLET):
    pass


class TestReadTDEventSLLET:
    def test_read_full(self):
        AUTOSAR.getInstance().new()
        AUTOSAR.getInstance().setARRelease("R23-11")
        parent = AUTOSAR.getInstance().createARPackage("AUTOSAR")
        event = _ConcreteTDEventSLLET(parent, "SLLET1")
        element = ET.fromstring(
            f"<TD-EVENT-SLLET xmlns='{NS}'>" "<SHORT-NAME>SLLET1</SHORT-NAME>" "</TD-EVENT-SLLET>"
        )
        ARXMLParser().readTDEventSLLET(element, event)
        assert event.getShortName() == "SLLET1"


class TestReadTDEventSLLETPort:
    def test_read_full(self):
        AUTOSAR.getInstance().new()
        AUTOSAR.getInstance().setARRelease("R23-11")
        parent = AUTOSAR.getInstance().createARPackage("AUTOSAR")
        event = TDEventSLLETPort(parent, "SLLETPort1")
        element = ET.fromstring(
            f"<TD-EVENT-SLLET-PORT xmlns='{NS}'>"
            "<SHORT-NAME>SLLETPort1</SHORT-NAME>"
            "<PORT-REF DEST='PORT-PROTOTYPE'>/Path/To/Port</PORT-REF>"
            "</TD-EVENT-SLLET-PORT>"
        )
        ARXMLParser().readTDEventSLLETPort(element, event)
        assert event.getShortName() == "SLLETPort1"
        assert event.getPortRef() is not None
        assert event.getPortRef().getValue() == "/Path/To/Port"
        assert event.getPortRef().getDest() == "PORT-PROTOTYPE"

    def test_read_empty(self):
        AUTOSAR.getInstance().new()
        AUTOSAR.getInstance().setARRelease("R23-11")
        parent = AUTOSAR.getInstance().createARPackage("AUTOSAR")
        event = TDEventSLLETPort(parent, "SLLETPort1")
        element = ET.fromstring(
            f"<TD-EVENT-SLLET-PORT xmlns='{NS}'>" "<SHORT-NAME>SLLETPort1</SHORT-NAME>" "</TD-EVENT-SLLET-PORT>"
        )
        ARXMLParser().readTDEventSLLETPort(element, event)
        assert event.getShortName() == "SLLETPort1"
        assert event.getPortRef() is None
