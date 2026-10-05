"""Tests for the PortPrototype annotation classes (ApplicationAttributes)."""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral, Boolean, RefType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ApplicationAttributes import (
    ClientServerAnnotation,
    DelegatedPortAnnotation,
    FilterDebouncingEnum,
    IoHwAbstractionServerAnnotation,
    PulseTestEnum,
    SignalFanEnum,
)


def _ref(value="/Pkg/Elem", dest="VARIABLE-DATA-PROTOTYPE"):
    r = RefType()
    r.setValue(value)
    r.setDest(dest)
    return r


def _literal(text="val"):
    lit = ARLiteral()
    lit.setValue(text)
    return lit


def _bool(value=True):
    b = Boolean()
    b.setValue("true" if value else "false")
    return b


class TestClientServerAnnotation:
    def test_initialization(self):
        annotation = ClientServerAnnotation()
        assert annotation.getOperationRef() is None

    def test_operation_ref_setter_getter(self):
        annotation = ClientServerAnnotation()
        ref = _ref(dest="CLIENT-SERVER-OPERATION")
        assert annotation.setOperationRef(ref) is annotation
        assert annotation.getOperationRef() == ref

    def test_operation_ref_none_is_noop(self):
        annotation = ClientServerAnnotation()
        ref = _ref(dest="CLIENT-SERVER-OPERATION")
        annotation.setOperationRef(ref)
        annotation.setOperationRef(None)
        assert annotation.getOperationRef() == ref


class TestIoHwAbstractionServerAnnotation:
    def test_initialization(self):
        annotation = IoHwAbstractionServerAnnotation()
        assert annotation.getAge() is None
        assert annotation.getArgumentRef() is None
        assert annotation.getBswResolution() is None
        assert annotation.getDataElementRef() is None
        assert annotation.getFailureMonitoringRef() is None
        assert annotation.getFilteringDebouncing() is None
        assert annotation.getPulseTest() is None
        assert annotation.getTriggerRef() is None

    def test_filtering_debouncing_setter_getter(self):
        annotation = IoHwAbstractionServerAnnotation()
        value = FilterDebouncingEnum().setValue(FilterDebouncingEnum.DEBOUNCE_DATA)
        assert annotation.setFilteringDebouncing(value) is annotation
        assert annotation.getFilteringDebouncing() == value

    def test_pulse_test_setter_getter(self):
        annotation = IoHwAbstractionServerAnnotation()
        value = PulseTestEnum().setValue(PulseTestEnum.ENABLE)
        assert annotation.setPulseTest(value) is annotation
        assert annotation.getPulseTest() == value

    def test_trigger_ref_setter_getter(self):
        annotation = IoHwAbstractionServerAnnotation()
        ref = _ref(dest="TRIGGER")
        assert annotation.setTriggerRef(ref) is annotation
        assert annotation.getTriggerRef() == ref

    def test_trigger_ref_none_is_noop(self):
        annotation = IoHwAbstractionServerAnnotation()
        ref = _ref(dest="TRIGGER")
        annotation.setTriggerRef(ref)
        annotation.setTriggerRef(None)
        assert annotation.getTriggerRef() == ref


class TestDelegatedPortAnnotation:
    def test_initialization(self):
        annotation = DelegatedPortAnnotation()
        assert annotation.getSignalFan() is None

    def test_signal_fan_setter_getter(self):
        annotation = DelegatedPortAnnotation()
        value = SignalFanEnum().setValue(SignalFanEnum.SINGLE)
        assert annotation.setSignalFan(value) is annotation
        assert annotation.getSignalFan() == value

    def test_signal_fan_none_is_noop(self):
        annotation = DelegatedPortAnnotation()
        value = SignalFanEnum().setValue(SignalFanEnum.SINGLE)
        annotation.setSignalFan(value)
        annotation.setSignalFan(None)
        assert annotation.getSignalFan() == value
