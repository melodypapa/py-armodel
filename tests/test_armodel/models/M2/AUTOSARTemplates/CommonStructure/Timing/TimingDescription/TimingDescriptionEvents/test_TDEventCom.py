from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription import (
    TimingDescriptionEvent,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventCom import (
    TDEventCom,
    TDEventCycleStart,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
    RefType,
)


class _TDEventComImpl(TDEventCom):
    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)


class _TDEventCycleStartImpl(TDEventCycleStart):
    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)


class TestTDEventCom:
    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def test_abstract_guard(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        raised = False
        try:
            TDEventCom(None, "X")
        except TypeError:
            raised = True
        assert raised, "TDEventCom should be abstract"

    def test_base_is_timing_description_event(self):
        assert issubclass(TDEventCom, TimingDescriptionEvent)

    def test_defaults(self):
        parent = self._parent()
        event = _TDEventComImpl(parent, "E1")
        assert event.getEcuInstanceRef() is None

    def test_set_get_ecu_instance_ref(self):
        parent = self._parent()
        event = _TDEventComImpl(parent, "E1")
        ref = RefType()
        ref.setValue("/Path/To/EcuInstance")
        assert event.setEcuInstanceRef(ref) is event
        assert event.getEcuInstanceRef() is ref

    def test_set_ecu_instance_ref_none_noop(self):
        parent = self._parent()
        event = _TDEventComImpl(parent, "E1")
        ref = RefType()
        ref.setValue("/Path/To/EcuInstance")
        event.setEcuInstanceRef(ref)
        event.setEcuInstanceRef(None)
        assert event.getEcuInstanceRef() is ref


class TestTDEventCycleStart:
    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def test_abstract_guard(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        raised = False
        try:
            TDEventCycleStart(None, "X")
        except TypeError:
            raised = True
        assert raised, "TDEventCycleStart should be abstract"

    def test_base_is_tdevent_com(self):
        assert issubclass(TDEventCycleStart, TDEventCom)

    def test_defaults(self):
        parent = self._parent()
        event = _TDEventCycleStartImpl(parent, "E1")
        assert event.getCycleRepetition() is None

    def test_set_get_cycle_repetition(self):
        parent = self._parent()
        event = _TDEventCycleStartImpl(parent, "E1")
        value = Integer()
        value.setValue(2)
        assert event.setCycleRepetition(value) is event
        assert event.getCycleRepetition() is value

    def test_set_cycle_repetition_none_noop(self):
        parent = self._parent()
        event = _TDEventCycleStartImpl(parent, "E1")
        value = Integer()
        value.setValue(2)
        event.setCycleRepetition(value)
        event.setCycleRepetition(None)
        assert event.getCycleRepetition() is value
