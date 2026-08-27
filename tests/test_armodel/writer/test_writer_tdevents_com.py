"""Writer tests for TDEventCom (abstract COM timing event base, Table 3.29)."""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventCom import (
    TDEventCom,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


class ConcreteTDEventCom(TDEventCom):
    pass


class TestWriteTDEventCom:
    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def test_write_with_ecu_instance_ref(self):
        parent = self._parent()
        event = ConcreteTDEventCom(parent, "Com1")
        event.setEcuInstanceRef(RefType().setValue("/AUTOSAR/Ecu1").setDest("ECU-INSTANCE"))
        element = ET.Element("TD-EVENT-COM")
        ARXMLWriter().writeTDEventCom(element, event)
        ref = element.find("ECU-INSTANCE-REF")
        assert ref is not None
        assert ref.text == "/AUTOSAR/Ecu1"
        assert ref.attrib["DEST"] == "ECU-INSTANCE"

    def test_write_roundtrip(self):
        parent = self._parent()
        event = ConcreteTDEventCom(parent, "Com1")
        event.setEcuInstanceRef(RefType().setValue("/AUTOSAR/Ecu1").setDest("ECU-INSTANCE"))
        element = ET.Element("TD-EVENT-COM", {"xmlns": NS})
        ARXMLWriter().writeTDEventCom(element, event)
        reparsed_el = ET.fromstring(ET.tostring(element))
        reparsed = ConcreteTDEventCom(parent, "Com1")
        ARXMLParser().readTDEventCom(reparsed_el, reparsed)
        assert reparsed.getEcuInstanceRef().getValue() == "/AUTOSAR/Ecu1"
        assert reparsed.getEcuInstanceRef().getDest() == "ECU-INSTANCE"

    def test_write_empty(self):
        parent = self._parent()
        event = ConcreteTDEventCom(parent, "Com1")
        element = ET.Element("TD-EVENT-COM")
        ARXMLWriter().writeTDEventCom(element, event)
        assert element.find("ECU-INSTANCE-REF") is None
