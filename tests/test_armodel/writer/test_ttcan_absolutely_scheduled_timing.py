"""Writer/reader round-trip tests for TtcanAbsolutelyScheduledTiming (Table 6.115, p.450)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DateTime, Integer, String
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ttcan.TtcanCommunication import TtcanAbsolutelyScheduledTiming, TtcanTriggerType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import CycleCounter, CycleRepetition
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def writer():
    AUTOSAR.getInstance().new()
    document = AUTOSAR.getInstance()
    document.setARRelease("R23-11")
    return ARXMLWriter()


@pytest.fixture
def parser():
    AUTOSAR.getInstance().new()
    document = AUTOSAR.getInstance()
    document.setARRelease("R23-11")
    return ARXMLParser()


def _integer(text):
    value = Integer()
    value.setValue(text)
    return value


def _wrap(element: ET.Element) -> ET.Element:
    inner = ET.tostring(element).decode("utf-8")
    return ET.fromstring(f"<AUTOSAR xmlns='{NS}'>{inner}</AUTOSAR>")


class TestTtcanAbsolutelyScheduledTimingRoundTrip:
    def test_round_trip_cycle_counter_preserves_all_values(self, writer, parser, tmp_path):
        timing = TtcanAbsolutelyScheduledTiming()
        cycle = CycleCounter()
        cycle.setCycleCounter(_integer("2"))
        timing.setCommunicationCycle(cycle)
        timing.setTimeMark(_integer("16"))
        trigger = TtcanTriggerType()
        trigger.setValue(TtcanTriggerType.ENUM_TX_TRIGGER_SINGLE)
        timing.setTrigger(trigger)
        timing.setChecksum(String().setValue("a1b2c3d4"))
        timestamp = DateTime()
        timestamp.setValue("2024-01-02T03:04:05+06:00")
        timing.setTimestamp(timestamp)

        parent = ET.Element("ABSOLUTELY-SCHEDULED-TIMINGS")
        writer.writeTtcanAbsolutelyScheduledTiming(parent, timing)

        out_file = str(tmp_path / "ttcan_timing.arxml")
        with open(out_file, "w", encoding="utf-8") as f:
            f.write(ET.tostring(_wrap(parent), encoding="unicode"))

        recovered = TtcanAbsolutelyScheduledTiming()
        tree = ET.parse(out_file)
        parser.readTtcanAbsolutelyScheduledTiming(tree.getroot()[0][0], recovered)

        cycle2 = recovered.getCommunicationCycle()
        assert isinstance(cycle2, CycleCounter)
        assert cycle2.getCycleCounter().getValue() == 2
        assert recovered.getTimeMark().getValue() == 16
        assert recovered.getTrigger().getValue() == TtcanTriggerType.ENUM_TX_TRIGGER_SINGLE
        assert recovered.getChecksum().getValue() == "a1b2c3d4"
        assert recovered.getTimestamp().getValue() == "2024-01-02T03:04:05+06:00"

    def test_round_trip_cycle_repetition_variant(self, writer, parser, tmp_path):
        timing = TtcanAbsolutelyScheduledTiming()
        cycle = CycleRepetition()
        cycle.setBaseCycle(_integer("4"))
        timing.setCommunicationCycle(cycle)

        parent = ET.Element("ABSOLUTELY-SCHEDULED-TIMINGS")
        writer.writeTtcanAbsolutelyScheduledTiming(parent, timing)

        out_file = str(tmp_path / "ttcan_timing_repetition.arxml")
        with open(out_file, "w", encoding="utf-8") as f:
            f.write(ET.tostring(_wrap(parent), encoding="unicode"))

        recovered = TtcanAbsolutelyScheduledTiming()
        tree = ET.parse(out_file)
        parser.readTtcanAbsolutelyScheduledTiming(tree.getroot()[0][0], recovered)

        cycle2 = recovered.getCommunicationCycle()
        assert isinstance(cycle2, CycleRepetition)
        assert cycle2.getBaseCycle().getValue() == 4
        assert recovered.getTimeMark() is None
        assert recovered.getTrigger() is None

    def test_round_trip_empty_omits_optional_elements(self, writer, parser, tmp_path):
        timing = TtcanAbsolutelyScheduledTiming()

        parent = ET.Element("ABSOLUTELY-SCHEDULED-TIMINGS")
        writer.writeTtcanAbsolutelyScheduledTiming(parent, timing)

        out_file = str(tmp_path / "ttcan_timing_empty.arxml")
        with open(out_file, "w", encoding="utf-8") as f:
            f.write(ET.tostring(_wrap(parent), encoding="unicode"))

        tag = ET.parse(out_file).getroot()[0][0]
        assert tag.find("COMMUNICATION-CYCLE") is None
        assert tag.find("TIME-MARK") is None
        assert tag.find("TRIGGER") is None

        recovered = TtcanAbsolutelyScheduledTiming()
        parser.readTtcanAbsolutelyScheduledTiming(tag, recovered)
        assert recovered.getCommunicationCycle() is None
        assert recovered.getTimeMark() is None
        assert recovered.getTrigger() is None
