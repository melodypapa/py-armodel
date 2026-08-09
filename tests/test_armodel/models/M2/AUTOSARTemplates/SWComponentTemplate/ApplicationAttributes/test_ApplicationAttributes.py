"""Tests for the PortPrototype annotation classes (ApplicationAttributes)."""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARBoolean, ARLiteral, RefType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ApplicationAttributes import (
    ClientServerAnnotation,
    DataLimitKindEnum,
    DelegatedPortAnnotation,
    FilterDebouncingEnum,
    IoHwAbstractionServerAnnotation,
    ModePortAnnotation,
    NvDataPortAnnotation,
    ParameterPortAnnotation,
    ProcessingKindEnum,
    PulseTestEnum,
    SenderReceiverAnnotation,
    SignalFanEnum,
    TriggerPortAnnotation,
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
    b = ARBoolean()
    b.setValue("true" if value else "false")
    return b


class TestSenderReceiverAnnotation:
    def test_initialization(self):
        annotation = SenderReceiverAnnotation()
        assert annotation.getComputed() is None
        assert annotation.getDataElementRef() is None
        assert annotation.getLimitKind() is None
        assert annotation.getProcessingKind() is None

    def test_computed_setter_getter(self):
        annotation = SenderReceiverAnnotation()
        value = _bool(True)
        assert annotation.setComputed(value) is annotation
        assert annotation.getComputed() == value

    def test_computed_none_is_noop(self):
        annotation = SenderReceiverAnnotation()
        value = _bool(True)
        annotation.setComputed(value)
        annotation.setComputed(None)
        assert annotation.getComputed() == value

    def test_data_element_ref_setter_getter(self):
        annotation = SenderReceiverAnnotation()
        ref = _ref()
        assert annotation.setDataElementRef(ref) is annotation
        assert annotation.getDataElementRef() == ref

    def test_data_element_ref_none_is_noop(self):
        annotation = SenderReceiverAnnotation()
        ref = _ref()
        annotation.setDataElementRef(ref)
        annotation.setDataElementRef(None)
        assert annotation.getDataElementRef() == ref

    def test_limit_kind_setter_getter(self):
        annotation = SenderReceiverAnnotation()
        value = DataLimitKindEnum().setValue(DataLimitKindEnum.MAX)
        assert annotation.setLimitKind(value) is annotation
        assert annotation.getLimitKind() == value

    def test_processing_kind_setter_getter(self):
        annotation = SenderReceiverAnnotation()
        value = ProcessingKindEnum().setValue(ProcessingKindEnum.FILTERED)
        assert annotation.setProcessingKind(value) is annotation
        assert annotation.getProcessingKind() == value


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


class TestModePortAnnotation:
    def test_initialization(self):
        annotation = ModePortAnnotation()
        assert annotation.getModeGroupRef() is None

    def test_mode_group_ref_setter_getter(self):
        annotation = ModePortAnnotation()
        ref = _ref(dest="MODE-DECLARATION-GROUP-PROTOTYPE")
        assert annotation.setModeGroupRef(ref) is annotation
        assert annotation.getModeGroupRef() == ref

    def test_mode_group_ref_none_is_noop(self):
        annotation = ModePortAnnotation()
        ref = _ref(dest="MODE-DECLARATION-GROUP-PROTOTYPE")
        annotation.setModeGroupRef(ref)
        annotation.setModeGroupRef(None)
        assert annotation.getModeGroupRef() == ref


class TestNvDataPortAnnotation:
    def test_initialization(self):
        annotation = NvDataPortAnnotation()
        assert annotation.getVariableRef() is None

    def test_variable_ref_setter_getter(self):
        annotation = NvDataPortAnnotation()
        ref = _ref()
        assert annotation.setVariableRef(ref) is annotation
        assert annotation.getVariableRef() == ref

    def test_variable_ref_none_is_noop(self):
        annotation = NvDataPortAnnotation()
        ref = _ref()
        annotation.setVariableRef(ref)
        annotation.setVariableRef(None)
        assert annotation.getVariableRef() == ref


class TestParameterPortAnnotation:
    def test_initialization(self):
        annotation = ParameterPortAnnotation()
        assert annotation.getParameterRef() is None

    def test_parameter_ref_setter_getter(self):
        annotation = ParameterPortAnnotation()
        ref = _ref(dest="PARAMETER-DATA-PROTOTYPE")
        assert annotation.setParameterRef(ref) is annotation
        assert annotation.getParameterRef() == ref

    def test_parameter_ref_none_is_noop(self):
        annotation = ParameterPortAnnotation()
        ref = _ref(dest="PARAMETER-DATA-PROTOTYPE")
        annotation.setParameterRef(ref)
        annotation.setParameterRef(None)
        assert annotation.getParameterRef() == ref


class TestTriggerPortAnnotation:
    def test_initialization(self):
        annotation = TriggerPortAnnotation()
        assert annotation.getTriggerRef() is None

    def test_trigger_ref_setter_getter(self):
        annotation = TriggerPortAnnotation()
        ref = _ref(dest="TRIGGER")
        assert annotation.setTriggerRef(ref) is annotation
        assert annotation.getTriggerRef() == ref

    def test_trigger_ref_none_is_noop(self):
        annotation = TriggerPortAnnotation()
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
