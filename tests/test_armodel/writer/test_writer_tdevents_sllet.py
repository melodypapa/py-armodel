"""Writer tests for TDEventSLLET (Table D.57)."""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventSLLET import (
    TDEventSLLET,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventSLLETPort import (
    TDEventSLLETPort,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
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


class TestWriteTDEventSLLETPort:
    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def test_write_roundtrip(self):
        parent = self._parent()
        event = TDEventSLLETPort(parent, "SLLETPort1")
        ref = RefType()
        ref.setDest("PORT-PROTOTYPE")
        ref.setValue("/Path/To/Port")
        event.setPortRef(ref)
        element = ET.Element("TD-EVENT-SLLET-PORT", {"xmlns": NS})
        ARXMLWriter().writeTDEventSLLETPort(element, event)
        port_ref_el = element.find("PORT-REF")
        assert port_ref_el is not None
        assert port_ref_el.text == "/Path/To/Port"
        assert port_ref_el.get("DEST") == "PORT-PROTOTYPE"
        reparsed_el = ET.fromstring(ET.tostring(element))
        reparsed = TDEventSLLETPort(parent, "SLLETPort1")
        ARXMLParser().readTDEventSLLETPort(reparsed_el, reparsed)
        assert reparsed.getShortName() == "SLLETPort1"
        assert reparsed.getPortRef() is not None
        assert reparsed.getPortRef().getValue() == "/Path/To/Port"
        assert reparsed.getPortRef().getDest() == "PORT-PROTOTYPE"

    def test_write_empty(self):
        parent = self._parent()
        event = TDEventSLLETPort(parent, "SLLETPort1")
        element = ET.Element("TD-EVENT-SLLET-PORT", {"xmlns": NS})
        ARXMLWriter().writeTDEventSLLETPort(element, event)
        assert element.find("PORT-REF") is None
        reparsed_el = ET.fromstring(ET.tostring(element))
        reparsed = TDEventSLLETPort(parent, "SLLETPort1")
        ARXMLParser().readTDEventSLLETPort(reparsed_el, reparsed)
        assert reparsed.getPortRef() is None
