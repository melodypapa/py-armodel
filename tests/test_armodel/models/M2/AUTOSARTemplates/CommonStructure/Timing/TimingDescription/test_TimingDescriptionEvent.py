import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription import (
    TimingDescription,
    TimingDescriptionEvent,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class ConcreteTimingDescriptionEvent(TimingDescriptionEvent):
    pass


class TestTimingDescriptionEvent:
    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def test_abstract_class_cannot_be_instantiated(self):
        parent = self._parent()
        with pytest.raises(TypeError, match="TimingDescriptionEvent is an abstract class"):
            TimingDescriptionEvent(parent, "TDEvent1")

    def test_base_is_timing_description(self):
        assert issubclass(TimingDescriptionEvent, TimingDescription)
        assert issubclass(TimingDescriptionEvent, Identifiable)

    def test_initialization_defaults(self):
        event = ConcreteTimingDescriptionEvent(self._parent(), "TDEvent1")
        assert event.getShortName() == "TDEvent1"
        assert event.getClockReferenceRef() is None
        assert event.getOccurrenceExpression() is None

    def test_get_set_clock_reference_ref(self):
        event = ConcreteTimingDescriptionEvent(self._parent(), "TDEvent1")
        ref = RefType().setValue("/AUTOSAR/Clock1").setDest("TIMING-CLOCK")
        assert event.setClockReferenceRef(ref) is event
        assert event.getClockReferenceRef() is ref
        assert event.getClockReferenceRef().getValue() == "/AUTOSAR/Clock1"
        assert event.getClockReferenceRef().getDest() == "TIMING-CLOCK"

    def test_set_clock_reference_ref_none_is_no_op(self):
        event = ConcreteTimingDescriptionEvent(self._parent(), "TDEvent1")
        ref = RefType().setValue("/AUTOSAR/Clock1").setDest("TIMING-CLOCK")
        event.setClockReferenceRef(ref)
        event.setClockReferenceRef(None)
        assert event.getClockReferenceRef() is ref

    def test_get_set_occurrence_expression(self):
        from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventOccurrenceExpression import (
            TDEventOccurrenceExpression,
        )

        event = ConcreteTimingDescriptionEvent(self._parent(), "TDEvent1")
        expression = TDEventOccurrenceExpression()
        assert event.setOccurrenceExpression(expression) is event
        assert event.getOccurrenceExpression() is expression

    def test_set_occurrence_expression_none_is_no_op(self):
        from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventOccurrenceExpression import (
            TDEventOccurrenceExpression,
        )

        event = ConcreteTimingDescriptionEvent(self._parent(), "TDEvent1")
        expression = TDEventOccurrenceExpression()
        event.setOccurrenceExpression(expression)
        event.setOccurrenceExpression(None)
        assert event.getOccurrenceExpression() is expression
