"""Parser tests for TDEventCom (abstract COM timing event base, Table 3.29)."""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventCom import (
    TDEventCom,
    TDEventCycleStart,
    TDEventFrClusterCycleStart,
)
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


class ConcreteTDEventCom(TDEventCom):
    pass


class ConcreteTDEventCycleStart(TDEventCycleStart):
    pass


class TestReadTDEventCom:
    def test_read_full(self):
        AUTOSAR.getInstance().new()
        AUTOSAR.getInstance().setARRelease("R23-11")
        parent = AUTOSAR.getInstance().createARPackage("AUTOSAR")
        event = ConcreteTDEventCom(parent, "Com1")
        element = ET.fromstring(f"<TD-EVENT-COM xmlns='{NS}'>" "<SHORT-NAME>Com1</SHORT-NAME>" "<ECU-INSTANCE-REF DEST='ECU-INSTANCE'>/AUTOSAR/Ecu1</ECU-INSTANCE-REF>" "</TD-EVENT-COM>")
        ARXMLParser().readTDEventCom(element, event)
        assert event.getShortName() == "Com1"
        assert event.getEcuInstanceRef().getValue() == "/AUTOSAR/Ecu1"
        assert event.getEcuInstanceRef().getDest() == "ECU-INSTANCE"

    def test_read_minimal(self):
        AUTOSAR.getInstance().new()
        AUTOSAR.getInstance().setARRelease("R23-11")
        parent = AUTOSAR.getInstance().createARPackage("AUTOSAR")
        event = ConcreteTDEventCom(parent, "Com1")
        element = ET.fromstring(f"<TD-EVENT-COM xmlns='{NS}'><SHORT-NAME>Com1</SHORT-NAME></TD-EVENT-COM>")
        ARXMLParser().readTDEventCom(element, event)
        assert event.getEcuInstanceRef() is None


class TestReadTDEventCycleStart:
    def test_read_cycle_repetition(self):
        AUTOSAR.getInstance().new()
        AUTOSAR.getInstance().setARRelease("R23-11")
        parent = AUTOSAR.getInstance().createARPackage("AUTOSAR")
        event = ConcreteTDEventCycleStart(parent, "Cyc1")
        element = ET.fromstring(f"<TD-EVENT-CYCLE-START xmlns='{NS}'>" "<SHORT-NAME>Cyc1</SHORT-NAME>" "<CYCLE-REPETITION>4</CYCLE-REPETITION>" "</TD-EVENT-CYCLE-START>")
        ARXMLParser().readTDEventCycleStart(element, event)
        assert event.getShortName() == "Cyc1"
        assert event.getCycleRepetition().getValue() == 4

    def test_read_minimal(self):
        AUTOSAR.getInstance().new()
        AUTOSAR.getInstance().setARRelease("R23-11")
        parent = AUTOSAR.getInstance().createARPackage("AUTOSAR")
        event = ConcreteTDEventCycleStart(parent, "Cyc1")
        element = ET.fromstring(f"<TD-EVENT-CYCLE-START xmlns='{NS}'><SHORT-NAME>Cyc1</SHORT-NAME></TD-EVENT-CYCLE-START>")
        ARXMLParser().readTDEventCycleStart(element, event)
        assert event.getCycleRepetition() is None


class TestReadTDEventFrClusterCycleStart:
    def test_read_full(self):
        AUTOSAR.getInstance().new()
        AUTOSAR.getInstance().setARRelease("R23-11")
        parent = AUTOSAR.getInstance().createARPackage("AUTOSAR")
        event = TDEventFrClusterCycleStart(parent, "FrCyc1")
        element = ET.fromstring(
            f"<TD-EVENT-FR-CLUSTER-CYCLE-START xmlns='{NS}'>"
            "<SHORT-NAME>FrCyc1</SHORT-NAME>"
            "<CYCLE-REPETITION>4</CYCLE-REPETITION>"
            "<FR-CLUSTER-REF DEST='FLEXRAY-CLUSTER'>/AUTOSAR/FrCluster1</FR-CLUSTER-REF>"
            "</TD-EVENT-FR-CLUSTER-CYCLE-START>"
        )
        ARXMLParser().readTDEventFrClusterCycleStart(element, event)
        assert event.getShortName() == "FrCyc1"
        assert event.getCycleRepetition().getValue() == 4
        assert event.getFrClusterRef().getValue() == "/AUTOSAR/FrCluster1"
        assert event.getFrClusterRef().getDest() == "FLEXRAY-CLUSTER"

    def test_read_minimal(self):
        AUTOSAR.getInstance().new()
        AUTOSAR.getInstance().setARRelease("R23-11")
        parent = AUTOSAR.getInstance().createARPackage("AUTOSAR")
        event = TDEventFrClusterCycleStart(parent, "FrCyc1")
        element = ET.fromstring(f"<TD-EVENT-FR-CLUSTER-CYCLE-START xmlns='{NS}'><SHORT-NAME>FrCyc1</SHORT-NAME></TD-EVENT-FR-CLUSTER-CYCLE-START>")
        ARXMLParser().readTDEventFrClusterCycleStart(element, event)
        assert event.getFrClusterRef() is None
