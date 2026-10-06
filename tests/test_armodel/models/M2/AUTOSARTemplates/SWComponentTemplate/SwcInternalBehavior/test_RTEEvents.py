"""
This module contains comprehensive tests for the RTEEvents module in SWComponentTemplate.SwcInternalBehavior.
Tests cover all classes and methods in the RTEEvents.py file to achieve 100% test coverage.
"""

import inspect
import typing

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior import AbstractEvent
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpStructureElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType, TimeValue
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs import (
    POperationInAtomicSwcInstanceRef,
    RModeInAtomicSwcInstanceRef,
    RTriggerInAtomicSwcInstanceRef,
    RVariableInAtomicSwcInstanceRef,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents import (
    AsynchronousServerCallReturnsEvent,
    BackgroundEvent,
    DataReceivedEvent,
    DataReceiveErrorEvent,
    DataSendCompletedEvent,
    DataWriteCompletedEvent,
    ExternalTriggerOccurredEvent,
    InitEvent,
    InternalTriggerOccurredEvent,
    ModeSwitchedAckEvent,
    OperationInvokedEvent,
    OsTaskExecutionEvent,
    RTEEvent,
    SwcModeSwitchEvent,
    TimingEvent,
    TransformerHardErrorEvent,
    WaitPoint,
)


class TestRTEEvent:
    """Test class for RTEEvent abstract class (Table 7.9)."""

    def test_abstract_class_cannot_be_instantiated(self):
        """Test that RTEEvent abstract class cannot be instantiated directly."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        with pytest.raises(TypeError, match="RTEEvent is an abstract class"):
            RTEEvent(ar_root, "TestRTEEvent")

    def test_initialization(self):
        """Test initialization defaults and inheritance chain via a concrete subclass."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = InitEvent(ar_root, "TestRTEEvent")

        assert event.parent == ar_root
        assert event.short_name == "TestRTEEvent"
        assert event.getDisabledModeIRefs() == []
        assert event.getStartOnEventRef() is None
        assert isinstance(event, AtpStructureElement)
        assert isinstance(event, AbstractEvent)
        assert isinstance(event, Identifiable)

    def test_class_docstring_verbatim(self):
        """Test the class docstring is the spec Note verbatim (Table 7.9)."""
        assert RTEEvent.__doc__.strip() == "Abstract base class for all RTE-related events"

    def test_add_disabled_mode_irefs(self):
        """Test addDisabledModeIRef append order, chaining and None no-op."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = InitEvent(ar_root, "TestRTEEvent")

        iref1 = RModeInAtomicSwcInstanceRef()
        iref2 = RModeInAtomicSwcInstanceRef()
        assert event.addDisabledModeIRef(iref1) is event
        assert event.addDisabledModeIRef(iref2) is event
        assert event.getDisabledModeIRefs() == [iref1, iref2]

        event.addDisabledModeIRef(None)
        assert event.getDisabledModeIRefs() == [iref1, iref2]

    def test_start_on_event_ref_round_trip(self):
        """Test setStartOnEventRef/getStartOnEventRef round-trip and None no-op."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = InitEvent(ar_root, "TestRTEEvent")

        ref = RefType()
        ref.setDest("RUNNABLE-ENTITY")
        ref.setValue("/MyComponents/MySwc_IB/re_event1")
        assert event.setStartOnEventRef(ref) is event
        assert event.getStartOnEventRef() == ref
        assert event.getStartOnEventRef().getDest() == "RUNNABLE-ENTITY"
        assert event.getStartOnEventRef().getValue() == "/MyComponents/MySwc_IB/re_event1"

        event.setStartOnEventRef(None)
        assert event.getStartOnEventRef() == ref


class TestAsynchronousServerCallReturnsEvent:
    """Test class for AsynchronousServerCallReturnsEvent class (Table 7.10)."""

    def test_initialization(self):
        """Test AsynchronousServerCallReturnsEvent initialization defaults."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = AsynchronousServerCallReturnsEvent(ar_root, "TestAsynchronousServerCallReturnsEvent")

        assert event.parent == ar_root
        assert event.short_name == "TestAsynchronousServerCallReturnsEvent"
        assert event.disabledModeIRefs == []
        assert event.startOnEventRef is None
        assert event.eventSourceRef is None
        assert isinstance(event, RTEEvent)

    def test_get_set_eventSourceRef(self):
        """Test setEventSourceRef/getEventSourceRef round-trip and None no-op."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = AsynchronousServerCallReturnsEvent(ar_root, "TestAsynchronousServerCallReturnsEvent")

        ref = RefType()
        ref.setDest("ASYNCHRONOUS-SERVER-CALL-RESULT-POINT")
        ref.setValue("/swc/ib/acp")
        assert event.setEventSourceRef(ref) is event
        assert event.getEventSourceRef() is ref
        assert event.getEventSourceRef().getDest() == "ASYNCHRONOUS-SERVER-CALL-RESULT-POINT"
        assert event.getEventSourceRef().getValue() == "/swc/ib/acp"

        event.setEventSourceRef(None)
        assert event.getEventSourceRef() is ref

    def test_get_type_hints(self):
        """Test spec-typed annotations resolve at runtime (plain get_type_hints)."""
        hints = typing.get_type_hints(AsynchronousServerCallReturnsEvent.setEventSourceRef)
        assert hints.get("value") == typing.Optional[RefType]
        assert hints.get("return") is AsynchronousServerCallReturnsEvent

        assert typing.get_type_hints(AsynchronousServerCallReturnsEvent.getEventSourceRef).get("return") == typing.Optional[RefType]


class TestDataSendCompletedEvent:
    """Test class for DataSendCompletedEvent class (Table 7.11)."""

    def test_initialization(self):
        """Test DataSendCompletedEvent initialization defaults."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = DataSendCompletedEvent(ar_root, "TestDataSendCompletedEvent")

        assert event.parent == ar_root
        assert event.short_name == "TestDataSendCompletedEvent"
        assert event.disabledModeIRefs == []
        assert event.startOnEventRef is None
        assert event.eventSourceRef is None
        assert isinstance(event, RTEEvent)

    def test_get_set_eventSourceRef(self):
        """Test setEventSourceRef/getEventSourceRef round-trip and None no-op."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = DataSendCompletedEvent(ar_root, "TestDataSendCompletedEvent")

        ref = RefType()
        ref.setDest("VARIABLE-ACCESS")
        ref.setValue("/swc/ib/va")
        assert event.setEventSourceRef(ref) is event
        assert event.getEventSourceRef() is ref
        assert event.getEventSourceRef().getDest() == "VARIABLE-ACCESS"
        assert event.getEventSourceRef().getValue() == "/swc/ib/va"

        event.setEventSourceRef(None)
        assert event.getEventSourceRef() is ref

    def test_get_type_hints(self):
        """Test spec-typed annotations resolve at runtime (plain get_type_hints)."""
        hints = typing.get_type_hints(DataSendCompletedEvent.setEventSourceRef)
        assert hints.get("value") == typing.Optional[RefType]
        assert hints.get("return") is DataSendCompletedEvent

        assert typing.get_type_hints(DataSendCompletedEvent.getEventSourceRef).get("return") == typing.Optional[RefType]


class TestDataWriteCompletedEvent:
    """Test class for DataWriteCompletedEvent class (Table 7.12)."""

    def test_docstring_is_spec_note_verbatim(self):
        """The class docstring carries the Table 7.12 Note + constr_1942 verbatim."""
        assert inspect.cleandoc(DataWriteCompletedEvent.__doc__) == (
            "This event is raised when an implicit write access was successful or an error occurred.\n"
            "\n"
            "[constr_1942] Existence of attribute DataWriteCompletedEvent.eventSource: For each DataWriteCompletedEvent, attribute eventSource shall exist at the time when the contract phase generation is executed."
        )

    def test_initialization(self):
        """Test DataWriteCompletedEvent initialization defaults."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = DataWriteCompletedEvent(ar_root, "TestDataWriteCompletedEvent")

        assert event.parent == ar_root
        assert event.short_name == "TestDataWriteCompletedEvent"
        assert event.disabledModeIRefs == []
        assert event.startOnEventRef is None
        assert event.eventSourceRef is None
        assert isinstance(event, RTEEvent)

    def test_get_set_eventSourceRef(self):
        """Test setEventSourceRef/getEventSourceRef round-trip and None no-op."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = DataWriteCompletedEvent(ar_root, "TestDataWriteCompletedEvent")

        ref = RefType()
        ref.setDest("VARIABLE-ACCESS")
        ref.setValue("/swc/ib/va")
        assert event.setEventSourceRef(ref) is event
        assert event.getEventSourceRef() is ref
        assert event.getEventSourceRef().getDest() == "VARIABLE-ACCESS"
        assert event.getEventSourceRef().getValue() == "/swc/ib/va"

        event.setEventSourceRef(None)
        assert event.getEventSourceRef() is ref

    def test_get_type_hints(self):
        """Test spec-typed annotations resolve at runtime (plain get_type_hints)."""
        hints = typing.get_type_hints(DataWriteCompletedEvent.setEventSourceRef)
        assert hints.get("value") == typing.Optional[RefType]
        assert hints.get("return") is DataWriteCompletedEvent

        assert typing.get_type_hints(DataWriteCompletedEvent.getEventSourceRef).get("return") == typing.Optional[RefType]


class TestDataReceivedEvent:
    """Test class for DataReceivedEvent class (Table 7.13)."""

    def test_initialization(self):
        """Test DataReceivedEvent initialization defaults."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = DataReceivedEvent(ar_root, "TestDataReceivedEvent")

        assert event.parent == ar_root
        assert event.short_name == "TestDataReceivedEvent"
        assert event.disabledModeIRefs == []
        assert event.startOnEventRef is None
        assert event.dataIRef is None
        assert isinstance(event, RTEEvent)

    def test_get_set_dataIRef(self):
        """Test setDataIRef/getDataIRef round-trip and None no-op."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = DataReceivedEvent(ar_root, "TestDataReceivedEvent")

        iref = RVariableInAtomicSwcInstanceRef()
        context_ref = RefType()
        context_ref.setDest("R-PORT-PROTOTYPE")
        context_ref.setValue("/swc/rp")
        iref.setContextRPortRef(context_ref)
        target_ref = RefType()
        target_ref.setDest("VARIABLE-DATA-PROTOTYPE")
        target_ref.setValue("/swc/de")
        iref.setTargetDataElementRef(target_ref)
        assert event.setDataIRef(iref) is event
        assert event.getDataIRef() is iref
        assert event.getDataIRef().getContextRPortRef().getValue() == "/swc/rp"
        assert event.getDataIRef().getTargetDataElementRef().getDest() == "VARIABLE-DATA-PROTOTYPE"

        event.setDataIRef(None)
        assert event.getDataIRef() is iref

    def test_get_type_hints(self):
        """Test spec-typed annotations resolve at runtime (plain get_type_hints)."""
        hints = typing.get_type_hints(DataReceivedEvent.setDataIRef)
        assert hints.get("value") == typing.Optional[RVariableInAtomicSwcInstanceRef]
        assert hints.get("return") is DataReceivedEvent

        assert typing.get_type_hints(DataReceivedEvent.getDataIRef).get("return") == typing.Optional[RVariableInAtomicSwcInstanceRef]


class TestSwcModeSwitchEvent:
    """Test class for SwcModeSwitchEvent class (Table 7.17)."""

    def test_class_docstring_is_spec_note_verbatim(self):
        """The class docstring carries the Table 7.17 Note + constr_1946/constr_1947 verbatim."""
        assert inspect.getdoc(SwcModeSwitchEvent) == (
            "This event is raised when the specified mode change occurs."
            "\n\n"
            "[constr_1946] Existence of attribute SwcModeSwitchEvent.activation: For each SwcModeSwitchEvent, attribute activation shall exist at the time when the RTE is generated.\n"  # NOQA E501
            "[constr_1947] Existence of reference SwcModeSwitchEvent.mode: For each SwcModeSwitchEvent, the reference to ModeDeclaration in the role mode shall exist at the time when the RTE is generated."  # NOQA E501
        )

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """Every accessor docstring is the spec Note copied verbatim."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = SwcModeSwitchEvent(ar_root, "TestSwcModeSwitchEvent")

        activation_note = "Specifies if the event is raised on entering or exiting a specific mode or is raised on the transition between two modes."
        mode_note = "The referenced mode or the transition between two modes raises this SwcModeSwitchEvent. InstanceRef implemented by: RModeInAtomicSwcInstanceRef"

        assert inspect.getdoc(event.getActivation) == activation_note
        assert inspect.getdoc(event.setActivation) == activation_note + "\n\nA None value is a no-op and does not overwrite an existing activation."
        assert inspect.getdoc(event.getModeIRefs) == mode_note
        assert inspect.getdoc(event.addModeIRef) == mode_note + "\n\nA None value is a no-op and does not append anything."

    def test_initialization(self):
        """Test SwcModeSwitchEvent initialization defaults (own + inherited)."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = SwcModeSwitchEvent(ar_root, "TestSwcModeSwitchEvent")

        assert event.parent == ar_root
        assert event.short_name == "TestSwcModeSwitchEvent"
        assert event.disabledModeIRefs == []
        assert event.startOnEventRef is None
        assert event.activation is None
        assert event.modeIRefs == []
        assert isinstance(event, RTEEvent)

    def test_get_set_activation(self):
        """setActivation returns self, the value round-trips, None is a no-op."""
        from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration import ModeActivationKind

        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = SwcModeSwitchEvent(ar_root, "TestSwcModeSwitchEvent")

        activation = ModeActivationKind().setValue(ModeActivationKind.ON_ENTRY)
        assert event.setActivation(activation) is event
        assert event.getActivation() == activation
        assert event.getActivation().getValue() == ModeActivationKind.ON_ENTRY

        event.setActivation(None)
        assert event.getActivation() == activation

    def test_add_get_mode_irefs(self):
        """addModeIRef appends in order, returns self, None is a no-op."""
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs import RModeInAtomicSwcInstanceRef

        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = SwcModeSwitchEvent(ar_root, "TestSwcModeSwitchEvent")

        assert event.getModeIRefs() == []
        iref1 = RModeInAtomicSwcInstanceRef()
        iref2 = RModeInAtomicSwcInstanceRef()
        assert event.addModeIRef(iref1) is event
        assert event.addModeIRef(iref2) is event
        assert event.getModeIRefs() == [iref1, iref2]

        event.addModeIRef(None)
        assert event.getModeIRefs() == [iref1, iref2]

    def test_accessor_type_hints(self):
        """Accessors carry the spec-typed annotations (Optional[ModeActivationKind], list of instance refs)."""
        from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration import ModeActivationKind
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs import RModeInAtomicSwcInstanceRef

        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = SwcModeSwitchEvent(ar_root, "TestSwcModeSwitchEvent")

        assert typing.get_type_hints(event.getActivation).get("return") == typing.Optional[ModeActivationKind]
        assert typing.get_type_hints(event.setActivation).get("value") == typing.Optional[ModeActivationKind]
        assert typing.get_type_hints(event.setActivation).get("return") is SwcModeSwitchEvent
        assert typing.get_type_hints(event.getModeIRefs).get("return") == typing.List[RModeInAtomicSwcInstanceRef]
        assert typing.get_type_hints(event.addModeIRef).get("value") == typing.Optional[RModeInAtomicSwcInstanceRef]
        assert typing.get_type_hints(event.addModeIRef).get("return") is SwcModeSwitchEvent


class TestDataReceiveErrorEvent:
    """Test class for DataReceiveErrorEvent class (Table 7.14)."""

    def test_initialization(self):
        """Test DataReceiveErrorEvent initialization defaults."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = DataReceiveErrorEvent(ar_root, "TestDataReceiveErrorEvent")

        assert event.parent == ar_root
        assert event.short_name == "TestDataReceiveErrorEvent"
        assert event.disabledModeIRefs == []
        assert event.startOnEventRef is None
        assert event.dataIRef is None
        assert isinstance(event, RTEEvent)

    def test_get_set_dataIRef(self):
        """Test setDataIRef/getDataIRef round-trip and None no-op."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = DataReceiveErrorEvent(ar_root, "TestDataReceiveErrorEvent")

        iref = RVariableInAtomicSwcInstanceRef()
        context_ref = RefType()
        context_ref.setDest("R-PORT-PROTOTYPE")
        context_ref.setValue("/swc/rp")
        iref.setContextRPortRef(context_ref)
        target_ref = RefType()
        target_ref.setDest("VARIABLE-DATA-PROTOTYPE")
        target_ref.setValue("/swc/de")
        iref.setTargetDataElementRef(target_ref)
        assert event.setDataIRef(iref) is event
        assert event.getDataIRef() is iref
        assert event.getDataIRef().getContextRPortRef().getValue() == "/swc/rp"
        assert event.getDataIRef().getTargetDataElementRef().getDest() == "VARIABLE-DATA-PROTOTYPE"

        event.setDataIRef(None)
        assert event.getDataIRef() is iref

    def test_get_type_hints(self):
        """Test spec-typed annotations resolve at runtime (plain get_type_hints)."""
        hints = typing.get_type_hints(DataReceiveErrorEvent.setDataIRef)
        assert hints.get("value") == typing.Optional[RVariableInAtomicSwcInstanceRef]
        assert hints.get("return") is DataReceiveErrorEvent

        assert typing.get_type_hints(DataReceiveErrorEvent.getDataIRef).get("return") == typing.Optional[RVariableInAtomicSwcInstanceRef]


class TestOperationInvokedEvent:
    """Test class for OperationInvokedEvent class (Table 7.15)."""

    def test_docstring_is_spec_note_verbatim(self):
        """The class docstring carries the Table 7.15 Note + constr_1945 verbatim."""
        assert inspect.cleandoc(OperationInvokedEvent.__doc__) == (
            "This event is raised when the ClientServerOperation referenced in OperationInvokedEvent.operation shall be invoked.\n"
            "\n"
            "[constr_1945] Existence of attribute OperationInvokedEvent.operation: For each OperationInvokedEvent, attribute operation shall exist at the time when the contract phase generation is executed."
        )

    def test_initialization(self):
        """Test OperationInvokedEvent initialization defaults."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = OperationInvokedEvent(ar_root, "TestOperationInvokedEvent")

        assert event.parent == ar_root
        assert event.short_name == "TestOperationInvokedEvent"
        assert event.disabledModeIRefs == []
        assert event.startOnEventRef is None
        assert event.operationIRef is None
        assert isinstance(event, RTEEvent)

    def test_get_set_operationIRef(self):
        """Test setOperationIRef/getOperationIRef round-trip and None no-op."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = OperationInvokedEvent(ar_root, "TestOperationInvokedEvent")

        iref = POperationInAtomicSwcInstanceRef()
        assert event.setOperationIRef(iref) is event
        assert event.getOperationIRef() is iref

        event.setOperationIRef(None)
        assert event.getOperationIRef() is iref

    def test_get_type_hints(self):
        """Test spec-typed annotations resolve at runtime (plain get_type_hints)."""
        hints = typing.get_type_hints(OperationInvokedEvent.setOperationIRef)
        assert hints.get("value") == typing.Optional[POperationInAtomicSwcInstanceRef]
        assert hints.get("return") is OperationInvokedEvent

        assert typing.get_type_hints(OperationInvokedEvent.getOperationIRef).get("return") == typing.Optional[POperationInAtomicSwcInstanceRef]


class TestInitEvent:
    """Test class for InitEvent class."""

    def test_class_docstring_verbatim(self):
        expected = (
            "This RTEEvent is supposed to be used for initialization purposes, i.e. for starting and restarting a partition. "
            "It is not guaranteed that all RunnableEntities referenced by this InitEvent are executed before the 'regular' "
            "RunnableEntities are executed for the first time. The execution order depends on the task mapping."
        )
        assert InitEvent.__doc__.strip() == expected

    def test_init_event_initialization(self):
        """Test InitEvent initialization."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = InitEvent(ar_root, "TestInitEvent")

        assert event.parent == ar_root
        assert event.short_name == "TestInitEvent"
        assert event.disabledModeIRefs == []
        assert event.startOnEventRef is None

        assert isinstance(event, RTEEvent)


class TestTimingEvent:
    """Test class for TimingEvent class."""

    def test_timing_event_initialization(self):
        """Test TimingEvent initialization and methods."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = TimingEvent(ar_root, "TestTimingEvent")

        assert event.parent == ar_root
        assert event.short_name == "TestTimingEvent"
        assert event.disabledModeIRefs == []
        assert event.startOnEventRef is None
        assert event.offset is None
        assert event.period is None

        # Test offset methods
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import TimeValue

        offset = TimeValue()
        offset.setValue(5.0)
        event.setOffset(offset)
        assert event.getOffset() == offset

        # Test period methods
        period = TimeValue()
        period.setValue(10.0)
        event.setPeriod(period)
        assert event.getPeriod() == period

        # Test periodMs property with period >= 0.001 (else block)
        period_large = TimeValue()
        period_large.setValue(100.0)
        event.setPeriod(period_large)
        assert event.periodMs == 100000  # 100.0 * 1000

        # Test periodMs property with None period (return None case)
        event_none = TimingEvent(ar_root, "TimingEventNone")
        assert event_none.periodMs is None

        # Test periodMs property with period < 0.001 (if block)
        period_small = TimeValue()
        period_small.setValue(0.0005)
        event.setPeriod(period_small)
        assert event.periodMs == 0.5  # 0.0005 * 1000

    def test_class_docstring_is_spec_note_verbatim(self):
        """The class docstring carries the Table 7.4 Note + constr_1622 verbatim."""
        assert inspect.getdoc(TimingEvent) == (
            "This event is used to start RunnableEntities that shall be executed periodically."
            "\n\n"
            "[constr_1622] Value of TimingEvent.offset vs. TimingEvent.period: If a value is defined for attribute TimingEvent.offset then this value shall be greater than 0 and less or equal than the value of attribute TimingEvent.period of the respective TimingEvent at the time when the RTE is generated."
        )

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """Every accessor docstring is the spec Note copied verbatim."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = TimingEvent(ar_root, "TestTimingEvent")

        offset_note = "The value makes an assumption about the time offset of the first activation of the RunnableEntity triggered by the mapped TimingEvent relative to the periodic activation of the time base of this TimingEvent. Unit: second."
        period_note = "Period of timing event in seconds. The value of this attribute shall be greater than zero."

        assert inspect.getdoc(event.getOffset) == offset_note
        assert inspect.getdoc(event.setOffset) == offset_note + "\n\nA None value is a no-op and does not overwrite an existing offset."
        assert inspect.getdoc(event.getPeriod) == period_note
        assert inspect.getdoc(event.setPeriod) == period_note + "\n\nA None value is a no-op and does not overwrite an existing period."

    def test_get_set_offset(self):
        """setOffset returns self, the value round-trips, None is a no-op."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = TimingEvent(ar_root, "TestTimingEvent")

        offset = TimeValue()
        offset.setValue(2.5)
        assert event.setOffset(offset) is event
        assert event.getOffset() is offset

        event.setOffset(None)
        assert event.getOffset() is offset

    def test_get_set_period(self):
        """setPeriod returns self, the value round-trips, None is a no-op."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = TimingEvent(ar_root, "TestTimingEvent")

        period = TimeValue()
        period.setValue(10.0)
        assert event.setPeriod(period) is event
        assert event.getPeriod() is period

        event.setPeriod(None)
        assert event.getPeriod() is period

    def test_accessor_type_hints(self):
        """Accessors carry the spec-typed Optional[TimeValue] annotations."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = TimingEvent(ar_root, "TestTimingEvent")

        assert typing.get_type_hints(event.getOffset).get("return") == typing.Optional[TimeValue]
        assert typing.get_type_hints(event.setOffset).get("value") == typing.Optional[TimeValue]
        assert typing.get_type_hints(event.setOffset).get("return") is TimingEvent
        assert typing.get_type_hints(event.getPeriod).get("return") == typing.Optional[TimeValue]
        assert typing.get_type_hints(event.setPeriod).get("value") == typing.Optional[TimeValue]
        assert typing.get_type_hints(event.setPeriod).get("return") is TimingEvent


class TestInternalTriggerOccurredEvent:
    """Test class for InternalTriggerOccurredEvent class (Table 7.21)."""

    def test_docstring_is_spec_note_verbatim(self):
        """The class docstring carries the Table 7.21 Note + constr_1950 verbatim."""
        assert inspect.cleandoc(InternalTriggerOccurredEvent.__doc__) == (
            "This event is raised when the referenced InternalTriggeringPoint has occurred.\n"
            "\n"
            "[constr_1950] Existence of attribute InternalTriggerOccurredEvent.eventSource: For each InternalTriggerOccurredEvent, the attribute eventSource shall exist at the time when the RTE is generated."
        )

    def test_initialization(self):
        """Test InternalTriggerOccurredEvent initialization defaults."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = InternalTriggerOccurredEvent(ar_root, "TestInternalTriggerOccurredEvent")

        assert event.parent == ar_root
        assert event.short_name == "TestInternalTriggerOccurredEvent"
        assert event.disabledModeIRefs == []
        assert event.startOnEventRef is None
        assert event.eventSourceRef is None
        assert isinstance(event, RTEEvent)

    def test_get_set_eventSourceRef(self):
        """Test setEventSourceRef/getEventSourceRef round-trip and None no-op."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = InternalTriggerOccurredEvent(ar_root, "TestInternalTriggerOccurredEvent")

        ref = RefType()
        ref.setDest("INTERNAL-TRIGGERING-POINT")
        ref.setValue("/swc/ib/itp")
        assert event.setEventSourceRef(ref) is event
        assert event.getEventSourceRef() is ref
        assert event.getEventSourceRef().getDest() == "INTERNAL-TRIGGERING-POINT"
        assert event.getEventSourceRef().getValue() == "/swc/ib/itp"

        event.setEventSourceRef(None)
        assert event.getEventSourceRef() is ref

    def test_get_type_hints(self):
        """Test spec-typed annotations resolve at runtime (plain get_type_hints)."""
        hints = typing.get_type_hints(InternalTriggerOccurredEvent.setEventSourceRef)
        assert hints.get("value") == typing.Optional[RefType]
        assert hints.get("return") is InternalTriggerOccurredEvent

        assert typing.get_type_hints(InternalTriggerOccurredEvent.getEventSourceRef).get("return") == typing.Optional[RefType]


class TestModeSwitchedAckEvent:
    """Test class for ModeSwitchedAckEvent class (Table 7.19)."""

    def test_class_docstring_is_spec_note_verbatim(self):
        """The class docstring carries the Table 7.19 Note + constr_1948 verbatim."""
        assert inspect.getdoc(ModeSwitchedAckEvent) == (
            "This event is raised when the referenced ModeSwitchPoint has been processed or an error occurred."
            "\n\n"
            "[constr_1948] Existence of attribute ModeSwitchedAckEvent.eventSource: For each ModeSwitchedAckEvent, attribute eventSource shall exist at the time when the RTE is generated."
        )

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """Every accessor docstring is the spec Note copied verbatim."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = ModeSwitchedAckEvent(ar_root, "TestModeSwitchedAckEvent")

        note = "The referenced ModeSwitchPoint raises this ModeSwitchedAckEvent when the ModeSwitchPoint has been processed."

        assert inspect.getdoc(event.getEventSourceRef) == note
        assert inspect.getdoc(event.setEventSourceRef) == note + "\n\nA None value is a no-op and does not overwrite an existing eventSourceRef."

    def test_mode_switched_ack_event_initialization(self):
        """Test ModeSwitchedAckEvent initialization defaults (own + inherited)."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = ModeSwitchedAckEvent(ar_root, "TestModeSwitchedAckEvent")

        assert event.parent == ar_root
        assert event.short_name == "TestModeSwitchedAckEvent"
        assert event.disabledModeIRefs == []
        assert event.startOnEventRef is None
        assert event.eventSourceRef is None
        assert isinstance(event, RTEEvent)

    def test_get_set_eventSourceRef(self):
        """setEventSourceRef returns self, the value round-trips, None is a no-op."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = ModeSwitchedAckEvent(ar_root, "TestModeSwitchedAckEvent")

        source_ref = RefType()
        source_ref.setDest("MODE-SWITCH-POINT")
        source_ref.setValue("/MyComponents/MySwc_IB/msp_1")
        assert event.setEventSourceRef(source_ref) is event
        assert event.getEventSourceRef() == source_ref
        assert event.getEventSourceRef().getDest() == "MODE-SWITCH-POINT"
        assert event.getEventSourceRef().getValue() == "/MyComponents/MySwc_IB/msp_1"

        event.setEventSourceRef(None)
        assert event.getEventSourceRef() == source_ref

    def test_accessor_type_hints(self):
        """Accessors carry the spec-typed Optional[RefType] annotations."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = ModeSwitchedAckEvent(ar_root, "TestModeSwitchedAckEvent")

        assert typing.get_type_hints(event.getEventSourceRef).get("return") == typing.Optional[RefType]
        assert typing.get_type_hints(event.setEventSourceRef).get("value") == typing.Optional[RefType]
        assert typing.get_type_hints(event.setEventSourceRef).get("return") is ModeSwitchedAckEvent


class TestExternalTriggerOccurredEvent:
    """Test class for ExternalTriggerOccurredEvent class (Table 7.20)."""

    def test_class_docstring_is_spec_note_verbatim(self):
        """The class docstring carries the Table 7.20 Note + constr_1949 verbatim."""
        assert inspect.getdoc(ExternalTriggerOccurredEvent) == (
            "This event is raised when the referenced Trigger has occurred."
            "\n\n"
            "[constr_1949] Existence of attribute ExternalTriggerOccurredEvent.trigger: For each ExternalTriggerOccurredEvent, attribute trigger shall exist at the time when the RTE is generated."
        )

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """Every accessor docstring is the spec Note copied verbatim."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = ExternalTriggerOccurredEvent(ar_root, "TestExternalTriggerOccurredEvent")

        note = "The referenced Trigger raises this ExternalTriggerOccurredEvent. InstanceRef implemented by: RTriggerInAtomicSwcInstanceRef"

        assert inspect.getdoc(event.getTriggerIRef) == note
        assert inspect.getdoc(event.setTriggerIRef) == note + "\n\nA None value is a no-op and does not overwrite an existing triggerIRef."

    def test_initialization(self):
        """Test ExternalTriggerOccurredEvent initialization defaults (own + inherited)."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = ExternalTriggerOccurredEvent(ar_root, "TestExternalTriggerOccurredEvent")

        assert event.parent == ar_root
        assert event.short_name == "TestExternalTriggerOccurredEvent"
        assert event.disabledModeIRefs == []
        assert event.startOnEventRef is None
        assert event.triggerIRef is None
        assert isinstance(event, RTEEvent)

    def test_get_set_trigger_iref(self):
        """setTriggerIRef returns self, the value round-trips, None is a no-op."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = ExternalTriggerOccurredEvent(ar_root, "TestExternalTriggerOccurredEvent")

        iref = RTriggerInAtomicSwcInstanceRef()
        iref.setContextRPortRef(RefType().setValue("/MyComponents/rp_trigger"))
        iref.setTargetTriggerRef(RefType().setValue("/MyComponents/trigger_1"))
        assert event.setTriggerIRef(iref) is event
        assert event.getTriggerIRef() == iref
        assert event.getTriggerIRef().getContextRPortRef().getValue() == "/MyComponents/rp_trigger"
        assert event.getTriggerIRef().getTargetTriggerRef().getValue() == "/MyComponents/trigger_1"

        event.setTriggerIRef(None)
        assert event.getTriggerIRef() == iref

    def test_accessor_type_hints(self):
        """Accessors carry the spec-typed Optional[RTriggerInAtomicSwcInstanceRef] annotations."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = ExternalTriggerOccurredEvent(ar_root, "TestExternalTriggerOccurredEvent")

        assert typing.get_type_hints(event.getTriggerIRef).get("return") == typing.Optional[RTriggerInAtomicSwcInstanceRef]
        assert typing.get_type_hints(event.setTriggerIRef).get("value") == typing.Optional[RTriggerInAtomicSwcInstanceRef]
        assert typing.get_type_hints(event.setTriggerIRef).get("return") is ExternalTriggerOccurredEvent


class TestTransformerHardErrorEvent:
    """Test class for TransformerHardErrorEvent class (Table 7.23)."""

    def test_class_docstring_is_spec_note_verbatim(self):
        """The class docstring carries the Table 7.23 Note + constr_1397 verbatim."""
        assert inspect.getdoc(TransformerHardErrorEvent) == (
            "This event is raised when data are received which should trigger a Client/Server operation or an external Trigger but during transformation of the data a hard transformer error occurred."
            "\n\n"
            "[constr_1397] Existence of attributes of TransformerHardErrorEvent: For any given TransformerHardErrorEvent, either the attribute TransformerHardErrorEvent.operation or TransformerHardErrorEvent.requiredTrigger shall exist at the time when the contract phase generation is executed."
        )

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """Every accessor docstring is the spec Note copied verbatim."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = TransformerHardErrorEvent(ar_root, "TestTransformerHardErrorEvent")

        operation_note = "This represents the ClientServerOperation for which the transformer can raise this TransformerHardErrorEvent. InstanceRef implemented by: POperationInAtomicSwcInstanceRef"
        trigger_note = "This represents the Trigger for which the transformer can raise this TransformerHardErrorEvent. InstanceRef implemented by: RTriggerInAtomicSwcInstanceRef"

        assert inspect.getdoc(event.getOperationIRef) == operation_note
        assert inspect.getdoc(event.setOperationIRef) == operation_note + "\n\nA None value is a no-op and does not overwrite an existing operationIRef."
        assert inspect.getdoc(event.getRequiredTriggerIRef) == trigger_note
        assert inspect.getdoc(event.setRequiredTriggerIRef) == trigger_note + "\n\nA None value is a no-op and does not overwrite an existing requiredTriggerIRef."

    def test_initialization(self):
        """Test TransformerHardErrorEvent initialization defaults (own + inherited)."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = TransformerHardErrorEvent(ar_root, "TestTransformerHardErrorEvent")

        assert event.parent == ar_root
        assert event.short_name == "TestTransformerHardErrorEvent"
        assert event.disabledModeIRefs == []
        assert event.startOnEventRef is None
        assert event.operationIRef is None
        assert event.requiredTriggerIRef is None
        assert isinstance(event, RTEEvent)

    def test_get_set_operation_iref(self):
        """setOperationIRef returns self, the value round-trips, None is a no-op."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = TransformerHardErrorEvent(ar_root, "TestTransformerHardErrorEvent")

        iref = POperationInAtomicSwcInstanceRef()
        iref.setContextPPortRef(RefType().setValue("/MyComponents/pp"))
        iref.setTargetProvidedOperationRef(RefType().setValue("/MyComponents/if/op"))
        assert event.setOperationIRef(iref) is event
        assert event.getOperationIRef() == iref
        assert event.getOperationIRef().getContextPPortRef().getValue() == "/MyComponents/pp"
        assert event.getOperationIRef().getTargetProvidedOperationRef().getValue() == "/MyComponents/if/op"

        event.setOperationIRef(None)
        assert event.getOperationIRef() == iref

    def test_get_set_required_trigger_iref(self):
        """setRequiredTriggerIRef returns self, the value round-trips, None is a no-op."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = TransformerHardErrorEvent(ar_root, "TestTransformerHardErrorEvent")

        iref = RTriggerInAtomicSwcInstanceRef()
        iref.setContextRPortRef(RefType().setValue("/MyComponents/rp"))
        iref.setTargetTriggerRef(RefType().setValue("/MyComponents/trigger_1"))
        assert event.setRequiredTriggerIRef(iref) is event
        assert event.getRequiredTriggerIRef() == iref
        assert event.getRequiredTriggerIRef().getContextRPortRef().getValue() == "/MyComponents/rp"
        assert event.getRequiredTriggerIRef().getTargetTriggerRef().getValue() == "/MyComponents/trigger_1"

        event.setRequiredTriggerIRef(None)
        assert event.getRequiredTriggerIRef() == iref

    def test_accessor_type_hints(self):
        """Accessors carry the spec-typed Optional[...] iref annotations."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = TransformerHardErrorEvent(ar_root, "TestTransformerHardErrorEvent")

        assert typing.get_type_hints(event.getOperationIRef).get("return") == typing.Optional[POperationInAtomicSwcInstanceRef]
        assert typing.get_type_hints(event.setOperationIRef).get("value") == typing.Optional[POperationInAtomicSwcInstanceRef]
        assert typing.get_type_hints(event.setOperationIRef).get("return") is TransformerHardErrorEvent
        assert typing.get_type_hints(event.getRequiredTriggerIRef).get("return") == typing.Optional[RTriggerInAtomicSwcInstanceRef]
        assert typing.get_type_hints(event.setRequiredTriggerIRef).get("value") == typing.Optional[RTriggerInAtomicSwcInstanceRef]
        assert typing.get_type_hints(event.setRequiredTriggerIRef).get("return") is TransformerHardErrorEvent


class TestOsTaskExecutionEvent:
    """Test class for OsTaskExecutionEvent class (Table 7.24)."""

    def test_class_docstring_is_spec_note_verbatim(self):
        """The class docstring carries the Table 7.24 Note + constr_10016 verbatim."""
        assert inspect.getdoc(OsTaskExecutionEvent) == (
            "This RTEEvent is supposed to execute RunnableEntities which have to react on the execution of specific OsTasks. Therefore, this event is unconditionally raised whenever the OsTask on which it is mapped is executed. The main use case for this event is scheduling of Runnables of Complex Drivers which have to react on task executions."
            "\n\n"
            "[constr_10016] Applicability of OsTaskExecutionEvent: An OsTaskExecutionEvent is only applicable for a SwcInternalBehavior in the context of a ComplexDeviceDriverSwComponentType, EcuAbstractionSwComponentType, or ServiceSwComponentType at the time when the contract phase generation is executed."
        )

    def test_initialization(self):
        """Test OsTaskExecutionEvent initialization defaults (own + inherited)."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = OsTaskExecutionEvent(ar_root, "TestOsTaskExecutionEvent")

        assert event.parent == ar_root
        assert event.short_name == "TestOsTaskExecutionEvent"
        assert event.disabledModeIRefs == []
        assert event.startOnEventRef is None
        assert isinstance(event, RTEEvent)


class TestBackgroundEvent:
    """Test class for BackgroundEvent class."""

    def test_background_event_initialization(self):
        """Test BackgroundEvent initialization."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = BackgroundEvent(ar_root, "TestBackgroundEvent")

        assert event.parent == ar_root
        assert event.short_name == "TestBackgroundEvent"
        assert event.disabledModeIRefs == []
        assert event.startOnEventRef is None
        assert isinstance(event, RTEEvent)
        assert BackgroundEvent.__doc__.strip() == "This event is used to start RunnableEntities that are supposed to be executed in the background."


class TestWaitPoint:
    """Test class for WaitPoint class (Table 7.25)."""

    def test_class_docstring_is_spec_note_verbatim(self):
        """The class docstring carries the Table 7.25 Note + constr_1951/constr_1952 verbatim."""
        assert inspect.getdoc(WaitPoint) == (
            "This defines a wait-point for which the RunnableEntity can wait."
            "\n\n"
            "[constr_1951] Existence of attribute WaitPoint.timeout: For each WaitPoint, attribute timeout shall exist at the time when the RTE is generated.\n"  # NOQA E501
            "[constr_1952] Existence of reference WaitPoint.trigger: For each WaitPoint, the reference to RTEEvent in the role trigger shall exist at the time when the contract phase generation is executed."  # NOQA E501
        )

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """Every accessor docstring is the spec Note copied verbatim."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        point = WaitPoint(ar_root, "TestWaitPoint")

        timeout_note = "Time in seconds before the WaitPoint times out and the blocking wait call returns with an error indicating the timeout."
        trigger_note = "This is the RTEEvent this WaitPoint is waiting for."

        assert inspect.getdoc(point.getTimeout) == timeout_note
        assert inspect.getdoc(point.setTimeout) == timeout_note + "\n\nA None value is a no-op and does not overwrite an existing timeout."
        assert inspect.getdoc(point.getTriggerRef) == trigger_note
        assert inspect.getdoc(point.setTriggerRef) == trigger_note + "\n\nA None value is a no-op and does not overwrite an existing triggerRef."

    def test_wait_point_initialization(self):
        """Test WaitPoint initialization defaults and inheritance chain."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        point = WaitPoint(ar_root, "TestWaitPoint")

        assert point.parent == ar_root
        assert point.short_name == "TestWaitPoint"
        assert point.timeout is None
        assert point.triggerRef is None
        assert isinstance(point, Identifiable)

    def test_get_set_timeout(self):
        """setTimeout returns self, the value round-trips, None is a no-op."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        point = WaitPoint(ar_root, "TestWaitPoint")

        timeout = TimeValue()
        timeout.setValue(2.5)
        assert point.setTimeout(timeout) is point
        assert point.getTimeout() is timeout
        assert point.getTimeout().getValue() == 2.5

        point.setTimeout(None)
        assert point.getTimeout() is timeout

    def test_get_set_trigger_ref(self):
        """setTriggerRef returns self, the value round-trips, None is a no-op."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        point = WaitPoint(ar_root, "TestWaitPoint")

        ref = RefType()
        ref.setDest("DATA-RECEIVED-EVENT")
        ref.setValue("/MyComponents/MySwc_IB/dre_1")
        assert point.setTriggerRef(ref) is point
        assert point.getTriggerRef() == ref
        assert point.getTriggerRef().getDest() == "DATA-RECEIVED-EVENT"
        assert point.getTriggerRef().getValue() == "/MyComponents/MySwc_IB/dre_1"

        point.setTriggerRef(None)
        assert point.getTriggerRef() == ref

    def test_accessor_type_hints(self):
        """Accessors carry the spec-typed annotations (Optional[TimeValue], Optional[RefType])."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        point = WaitPoint(ar_root, "TestWaitPoint")

        assert typing.get_type_hints(point.getTimeout).get("return") == typing.Optional[TimeValue]
        assert typing.get_type_hints(point.setTimeout).get("value") == typing.Optional[TimeValue]
        assert typing.get_type_hints(point.setTimeout).get("return") is WaitPoint
        assert typing.get_type_hints(point.getTriggerRef).get("return") == typing.Optional[RefType]
        assert typing.get_type_hints(point.setTriggerRef).get("value") == typing.Optional[RefType]
        assert typing.get_type_hints(point.setTriggerRef).get("return") is WaitPoint
