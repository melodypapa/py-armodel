import typing

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Integer
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ttcan.TtcanCommunication import (
    TtcanAbsolutelyScheduledTiming,
    TtcanTriggerType,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import CommunicationCycle, CycleCounter, CycleRepetition


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

    def test_communicationCycle_cycleCounter_variant(self):
        timing = TtcanAbsolutelyScheduledTiming()

        cycle = CycleCounter()
        timing.setCommunicationCycle(cycle)
        assert isinstance(timing.getCommunicationCycle(), CycleCounter)

    def test_timeMark(self):
        timing = TtcanAbsolutelyScheduledTiming()

        value = Integer().setValue("16")
        timing.setTimeMark(value)
        assert timing.getTimeMark() is value
        assert timing.getTimeMark().getValue() == 16
        assert timing == timing.setTimeMark(value)  # method chaining
        assert timing == timing.setTimeMark(None)  # None no-op
        assert timing.getTimeMark() is value  # unchanged

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

    def test_type_hints_pin(self):
        assert typing.get_type_hints(TtcanAbsolutelyScheduledTiming.setCommunicationCycle)["return"] is TtcanAbsolutelyScheduledTiming
        assert typing.get_type_hints(TtcanAbsolutelyScheduledTiming.setTimeMark)["return"] is TtcanAbsolutelyScheduledTiming
        assert typing.get_type_hints(TtcanAbsolutelyScheduledTiming.setTrigger)["return"] is TtcanAbsolutelyScheduledTiming
        assert typing.get_type_hints(TtcanAbsolutelyScheduledTiming.setTimeMark)["value"] == typing.Optional[Integer]
        assert typing.get_type_hints(TtcanAbsolutelyScheduledTiming.getCommunicationCycle)["return"] == typing.Optional[CommunicationCycle]


class TestTtcanTriggerType:
    """Test cases for TtcanTriggerType (Table 6.116)."""

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

    def test_facet_order(self):
        assert list(TtcanTriggerType().getEnumValues()) == [
            TtcanTriggerType.ENUM_RX_TRIGGER,
            TtcanTriggerType.ENUM_TX_REF_TRIGGER,
            TtcanTriggerType.ENUM_TX_REF_TRIGGER_GAP,
            TtcanTriggerType.ENUM_TX_TRIGGER_MERGED,
            TtcanTriggerType.ENUM_TX_TRIGGER_SINGLE,
            TtcanTriggerType.ENUM_WATCH_TRIGGER,
            TtcanTriggerType.ENUM_WATCH_TRIGGER_GAP,
        ]
