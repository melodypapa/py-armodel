"""
This module contains tests for the EOCExecutableEntityRefGroup class in the
AUTOSAR CommonStructure.Timing.TimingConstraint.ExecutionOrderConstraint module.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.ExecutionOrderConstraint import (
    EOCExecutableEntityRefGroup,
    LetDataExchangeParadigmEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
    PositiveInteger,
    RefType,
)


class TestEOCExecutableEntityRefGroup:
    """
    Test class for EOCExecutableEntityRefGroup functionality.
    """

    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def test_initialization(self):
        parent = self._parent()
        group = EOCExecutableEntityRefGroup(parent, "Group1")
        assert isinstance(group, EOCExecutableEntityRefGroup)
        assert group.getShortName() == "Group1"
        assert group.getLetDataExchangeParadigm() is None
        assert group.getLetIntervalRefs() == []
        assert group.getMaxCycleRepetitions() is None
        assert group.getMaxCycles() is None
        assert group.getMaxSlots() is None
        assert group.getMaxSlotsPerCycle() is None
        assert group.getNestedElementRefs() == []
        assert group.getSuccessorRefs() == []
        assert group.getTriggeringEventRef() is None

    def test_get_set_let_data_exchange_paradigm(self):
        parent = self._parent()
        group = EOCExecutableEntityRefGroup(parent, "Group1")

        paradigm = LetDataExchangeParadigmEnum().setValue(LetDataExchangeParadigmEnum.INTRA_LET_EOC)
        assert group.setLetDataExchangeParadigm(paradigm) is group
        assert group.getLetDataExchangeParadigm() is paradigm

        group.setLetDataExchangeParadigm(None)
        assert group.getLetDataExchangeParadigm() is paradigm

    def test_add_get_let_interval_refs(self):
        parent = self._parent()
        group = EOCExecutableEntityRefGroup(parent, "Group1")

        assert group.addLetIntervalRef(RefType().setValue("/AUTOSAR/LetChain1").setDest("TIMING-DESCRIPTION-EVENT-CHAIN")) is group
        assert group.addLetIntervalRef(RefType().setValue("/AUTOSAR/LetChain2").setDest("TIMING-DESCRIPTION-EVENT-CHAIN")) is group

        refs = group.getLetIntervalRefs()
        assert len(refs) == 2
        assert refs[0].getValue() == "/AUTOSAR/LetChain1"
        assert refs[1].getValue() == "/AUTOSAR/LetChain2"

        group.addLetIntervalRef(None)
        assert len(group.getLetIntervalRefs()) == 2

    def test_get_set_max_cycle_repetitions(self):
        parent = self._parent()
        group = EOCExecutableEntityRefGroup(parent, "Group1")

        repetitions = PositiveInteger().setValue("4")
        assert group.setMaxCycleRepetitions(repetitions) is group
        assert group.getMaxCycleRepetitions() is repetitions
        assert group.getMaxCycleRepetitions().getValue() == 4

        group.setMaxCycleRepetitions(None)
        assert group.getMaxCycleRepetitions() is repetitions

    def test_get_set_max_cycles(self):
        parent = self._parent()
        group = EOCExecutableEntityRefGroup(parent, "Group1")

        cycles = Integer().setValue("12")
        assert group.setMaxCycles(cycles) is group
        assert group.getMaxCycles() is cycles
        assert group.getMaxCycles().getValue() == 12

        group.setMaxCycles(None)
        assert group.getMaxCycles() is cycles

    def test_get_set_max_slots(self):
        parent = self._parent()
        group = EOCExecutableEntityRefGroup(parent, "Group1")

        slots = Integer().setValue("3")
        assert group.setMaxSlots(slots) is group
        assert group.getMaxSlots() is slots
        assert group.getMaxSlots().getValue() == 3

        group.setMaxSlots(None)
        assert group.getMaxSlots() is slots

    def test_get_set_max_slots_per_cycle(self):
        parent = self._parent()
        group = EOCExecutableEntityRefGroup(parent, "Group1")

        slots_per_cycle = PositiveInteger().setValue("2")
        assert group.setMaxSlotsPerCycle(slots_per_cycle) is group
        assert group.getMaxSlotsPerCycle() is slots_per_cycle
        assert group.getMaxSlotsPerCycle().getValue() == 2

        group.setMaxSlotsPerCycle(None)
        assert group.getMaxSlotsPerCycle() is slots_per_cycle

    def test_add_get_nested_element_refs(self):
        parent = self._parent()
        group = EOCExecutableEntityRefGroup(parent, "Group1")

        assert group.addNestedElementRef(RefType().setValue("/AUTOSAR/Entity1").setDest("EOC-EXECUTABLE-ENTITY-REF")) is group
        assert group.addNestedElementRef(RefType().setValue("/AUTOSAR/Group2").setDest("EOC-EXECUTABLE-ENTITY-REF-GROUP")) is group

        refs = group.getNestedElementRefs()
        assert len(refs) == 2
        assert refs[0].getValue() == "/AUTOSAR/Entity1"
        assert refs[0].getDest() == "EOC-EXECUTABLE-ENTITY-REF"
        assert refs[1].getValue() == "/AUTOSAR/Group2"

        group.addNestedElementRef(None)
        assert len(group.getNestedElementRefs()) == 2

    def test_add_get_successor_refs(self):
        parent = self._parent()
        group = EOCExecutableEntityRefGroup(parent, "Group1")

        assert group.addSuccessorRef(RefType().setValue("/AUTOSAR/Successor1").setDest("EOC-EXECUTABLE-ENTITY-REF")) is group

        refs = group.getSuccessorRefs()
        assert len(refs) == 1
        assert refs[0].getValue() == "/AUTOSAR/Successor1"

        group.addSuccessorRef(None)
        assert len(group.getSuccessorRefs()) == 1

    def test_get_set_triggering_event_ref(self):
        parent = self._parent()
        group = EOCExecutableEntityRefGroup(parent, "Group1")

        ref = RefType().setValue("/AUTOSAR/TimingEvent").setDest("TIMING-DESCRIPTION-EVENT")
        assert group.setTriggeringEventRef(ref) is group
        assert group.getTriggeringEventRef() is ref

        group.setTriggeringEventRef(None)
        assert group.getTriggeringEventRef() is ref
