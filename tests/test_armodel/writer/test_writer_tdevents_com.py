"""Writer tests for TDEventCom (abstract COM timing event base, Table 3.29)."""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventCom import (
    TDEventCom,
    TDEventCycleStart,
    TDEventFrClusterCycleStart,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
    RefType,
)
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


class ConcreteTDEventCom(TDEventCom):
    pass


class ConcreteTDEventCycleStart(TDEventCycleStart):
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


class TestWriteTDEventCycleStart:
    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def test_write_cycle_repetition(self):
        parent = self._parent()
        event = ConcreteTDEventCycleStart(parent, "Cyc1")
        event.setCycleRepetition(Integer().setValue(4))
        element = ET.Element("TD-EVENT-CYCLE-START")
        ARXMLWriter().writeTDEventCycleStart(element, event)
        rep = element.find("CYCLE-REPETITION")
        assert rep is not None
        assert rep.text == "4"

    def test_write_roundtrip(self):
        parent = self._parent()
        event = ConcreteTDEventCycleStart(parent, "Cyc1")
        event.setCycleRepetition(Integer().setValue(4))
        element = ET.Element("TD-EVENT-CYCLE-START", {"xmlns": NS})
        ARXMLWriter().writeTDEventCycleStart(element, event)
        reparsed_el = ET.fromstring(ET.tostring(element))
        reparsed = ConcreteTDEventCycleStart(parent, "Cyc1")
        ARXMLParser().readTDEventCycleStart(reparsed_el, reparsed)
        assert reparsed.getCycleRepetition().getValue() == 4

    def test_write_empty(self):
        parent = self._parent()
        event = ConcreteTDEventCycleStart(parent, "Cyc1")
        element = ET.Element("TD-EVENT-CYCLE-START")
        ARXMLWriter().writeTDEventCycleStart(element, event)
        assert element.find("CYCLE-REPETITION") is None


class TestWriteTDEventFrClusterCycleStart:
    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def test_write_fr_cluster_ref(self):
        parent = self._parent()
        event = TDEventFrClusterCycleStart(parent, "FrCyc1")
        event.setFrClusterRef(RefType().setValue("/AUTOSAR/FrCluster1").setDest("FLEXRAY-CLUSTER"))
        element = ET.Element("TD-EVENT-FR-CLUSTER-CYCLE-START")
        ARXMLWriter().writeTDEventFrClusterCycleStart(element, event)
        ref = element.find("FR-CLUSTER-REF")
        assert ref is not None
        assert ref.text == "/AUTOSAR/FrCluster1"
        assert ref.attrib["DEST"] == "FLEXRAY-CLUSTER"

    def test_write_inherited_cycle_repetition(self):
        parent = self._parent()
        event = TDEventFrClusterCycleStart(parent, "FrCyc1")
        event.setCycleRepetition(Integer().setValue(4))
        element = ET.Element("TD-EVENT-FR-CLUSTER-CYCLE-START")
        ARXMLWriter().writeTDEventFrClusterCycleStart(element, event)
        assert element.find("CYCLE-REPETITION").text == "4"

    def test_write_roundtrip(self):
        parent = self._parent()
        event = TDEventFrClusterCycleStart(parent, "FrCyc1")
        event.setFrClusterRef(RefType().setValue("/AUTOSAR/FrCluster1").setDest("FLEXRAY-CLUSTER"))
        event.setCycleRepetition(Integer().setValue(4))
        element = ET.Element("TD-EVENT-FR-CLUSTER-CYCLE-START", {"xmlns": NS})
        ARXMLWriter().writeTDEventFrClusterCycleStart(element, event)
        reparsed_el = ET.fromstring(ET.tostring(element))
        reparsed = TDEventFrClusterCycleStart(parent, "FrCyc1")
        ARXMLParser().readTDEventFrClusterCycleStart(reparsed_el, reparsed)
        assert reparsed.getFrClusterRef().getValue() == "/AUTOSAR/FrCluster1"
        assert reparsed.getFrClusterRef().getDest() == "FLEXRAY-CLUSTER"
        assert reparsed.getCycleRepetition().getValue() == 4

    def test_write_empty(self):
        parent = self._parent()
        event = TDEventFrClusterCycleStart(parent, "FrCyc1")
        element = ET.Element("TD-EVENT-FR-CLUSTER-CYCLE-START")
        ARXMLWriter().writeTDEventFrClusterCycleStart(element, event)
        assert element.find("FR-CLUSTER-REF") is None
