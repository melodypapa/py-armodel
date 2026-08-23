from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ttcan.TtcanCommunication import (
    TtcanAbsolutelyScheduledTiming,
    TtcanTriggerType,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import CycleRepetition


class TestTtcanAbsolutelyScheduledTiming:
    def test_initialization(self):
        timing = TtcanAbsolutelyScheduledTiming()

        assert timing.getCommunicationCycle() is None
        assert timing.getTimeMark() is None
        assert timing.getTrigger() is None

    def test_communicationCycle(self):
        timing = TtcanAbsolutelyScheduledTiming()

        cycle = CycleRepetition()
        timing.setCommunicationCycle(cycle)
        assert timing.getCommunicationCycle() == cycle
        assert timing == timing.setCommunicationCycle(cycle)  # method chaining
        assert timing == timing.setCommunicationCycle(None)  # None no-op
        assert timing.getCommunicationCycle() == cycle  # unchanged

    def test_timeMark(self):
        timing = TtcanAbsolutelyScheduledTiming()

        timing.setTimeMark(16)
        assert timing.getTimeMark() == 16
        assert timing == timing.setTimeMark(16)  # method chaining
        assert timing == timing.setTimeMark(None)  # None no-op
        assert timing.getTimeMark() == 16  # unchanged

    def test_trigger(self):
        timing = TtcanAbsolutelyScheduledTiming()

        trigger = TtcanTriggerType()
        trigger.setValue(TtcanTriggerType.ENUM_RX_TRIGGER)
        timing.setTrigger(trigger)
        assert timing.getTrigger() == trigger
        assert timing.getTrigger().getValue() == "RX-TRIGGER"
        assert timing == timing.setTrigger(trigger)  # method chaining
        assert timing == timing.setTrigger(None)  # None no-op
        assert timing.getTrigger() == trigger  # unchanged


class TestTtcanTriggerType:
    def test_initialization(self):
        trigger_type = TtcanTriggerType()
        assert trigger_type is not None
        trigger_type.setValue(TtcanTriggerType.ENUM_RX_TRIGGER)
        assert trigger_type.getValue() == "RX-TRIGGER"

    def test_literals(self):
        assert TtcanTriggerType.ENUM_RX_TRIGGER == "RX-TRIGGER"
        assert TtcanTriggerType.ENUM_TX_REF_TRIGGER == "TX-REF-TRIGGER"
        assert TtcanTriggerType.ENUM_TX_REF_TRIGGER_GAP == "TX-REF-TRIGGER-GAP"
        assert TtcanTriggerType.ENUM_TX_TRIGGER_MERGED == "TX-TRIGGER-MERGED"
        assert TtcanTriggerType.ENUM_TX_TRIGGER_SINGLE == "TX-TRIGGER-SINGLE"
        assert TtcanTriggerType.ENUM_WATCH_TRIGGER == "WATCH-TRIGGER"
        assert TtcanTriggerType.ENUM_WATCH_TRIGGER_GAP == "WATCH-TRIGGER-GAP"

        enum = TtcanTriggerType()
        assert TtcanTriggerType.ENUM_RX_TRIGGER in enum.getEnumValues()
        assert TtcanTriggerType.ENUM_WATCH_TRIGGER_GAP in enum.getEnumValues()
        assert len(enum.getEnumValues()) == 7
