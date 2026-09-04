"""
This module contains comprehensive tests for the RTEEvents module in SWComponentTemplate.SwcInternalBehavior.
Tests cover all classes and methods in the RTEEvents.py file to achieve 100% test coverage.
"""

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior import AbstractEvent
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpStructureElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs import RModeInAtomicSwcInstanceRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents import (
    AsynchronousServerCallReturnsEvent,
    BackgroundEvent,
    DataReceivedEvent,
    DataReceiveErrorEvent,
    DataSendCompletedEvent,
    DataWriteCompletedEvent,
    InitEvent,
    InternalTriggerOccurredEvent,
    ModeSwitchedAckEvent,
    OperationInvokedEvent,
    RTEEvent,
    SwcModeSwitchEvent,
    TimingEvent,
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
    """Test class for AsynchronousServerCallReturnsEvent class."""

    def test_asynchronous_server_call_returns_event_initialization(self):
        """Test AsynchronousServerCallReturnsEvent initialization and methods."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = AsynchronousServerCallReturnsEvent(ar_root, "TestAsynchronousServerCallReturnsEvent")

        assert event.parent == ar_root
        assert event.short_name == "TestAsynchronousServerCallReturnsEvent"
        assert event.disabledModeIRefs == []
        assert event.startOnEventRef is None
        assert event.eventSourceRef is None

        # Test eventSourceRef methods
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType

        source_ref = RefType()
        source_ref.setValue("/Source/Ref")
        event.setEventSourceRef(source_ref)
        assert event.getEventSourceRef() == source_ref


class TestDataSendCompletedEvent:
    """Test class for DataSendCompletedEvent class."""

    def test_data_send_completed_event_initialization(self):
        """Test DataSendCompletedEvent initialization and methods."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = DataSendCompletedEvent(ar_root, "TestDataSendCompletedEvent")

        assert event.parent == ar_root
        assert event.short_name == "TestDataSendCompletedEvent"
        assert event.disabledModeIRefs == []
        assert event.startOnEventRef is None
        assert event.eventSourceRef is None

        # Test eventSourceRef methods
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType

        source_ref = RefType()
        source_ref.setValue("/Source/Ref")
        event.setEventSourceRef(source_ref)
        assert event.getEventSourceRef() == source_ref


class TestDataWriteCompletedEvent:
    """Test class for DataWriteCompletedEvent class."""

    def test_data_write_completed_event_initialization(self):
        """Test DataWriteCompletedEvent initialization and methods."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = DataWriteCompletedEvent(ar_root, "TestDataWriteCompletedEvent")

        assert event.parent == ar_root
        assert event.short_name == "TestDataWriteCompletedEvent"
        assert event.disabledModeIRefs == []
        assert event.startOnEventRef is None
        assert event.eventSourceRef is None

        # Test eventSourceRef methods
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType

        source_ref = RefType()
        source_ref.setValue("/Source/Ref")
        event.setEventSourceRef(source_ref)
        assert event.getEventSourceRef() == source_ref


class TestDataReceivedEvent:
    """Test class for DataReceivedEvent class."""

    def test_data_received_event_initialization(self):
        """Test DataReceivedEvent initialization and methods."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = DataReceivedEvent(ar_root, "TestDataReceivedEvent")

        assert event.parent == ar_root
        assert event.short_name == "TestDataReceivedEvent"
        assert event.disabledModeIRefs == []
        assert event.startOnEventRef is None
        assert event.dataIRef is None

        # Test dataIRef methods
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs import RVariableInAtomicSwcInstanceRef

        iref = RVariableInAtomicSwcInstanceRef()
        event.setDataIRef(iref)
        assert event.getDataIRef() == iref


class TestSwcModeSwitchEvent:
    """Test class for SwcModeSwitchEvent class."""

    def test_initialization(self):
        """Test SwcModeSwitchEvent initialization defaults."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = SwcModeSwitchEvent(ar_root, "TestSwcModeSwitchEvent")

        assert event.parent == ar_root
        assert event.short_name == "TestSwcModeSwitchEvent"
        assert event.activation is None
        assert event.modeIRefs == []

    def test_get_set_activation(self):
        """Test getActivation/setActivation round-trip and None no-op."""
        from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration import ModeActivationKind

        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = SwcModeSwitchEvent(ar_root, "TestSwcModeSwitchEvent")

        activation = ModeActivationKind().setValue(ModeActivationKind.ON_ENTRY)
        assert event.setActivation(activation) is event
        assert event.getActivation() == activation

        event.setActivation(None)
        assert event.getActivation() == activation

    def test_add_get_mode_irefs(self):
        """Test addModeIRef/getModeIRefs append, return value and None no-op."""
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs import RModeInAtomicSwcInstanceRef

        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = SwcModeSwitchEvent(ar_root, "TestSwcModeSwitchEvent")

        assert event.getModeIRefs() == []
        iref = RModeInAtomicSwcInstanceRef()
        assert event.addModeIRef(iref) is event
        assert event.getModeIRefs() == [iref]

        event.addModeIRef(None)
        assert event.getModeIRefs() == [iref]


class TestDataReceiveErrorEvent:
    """Test class for DataReceiveErrorEvent class."""

    def test_data_receive_error_event_initialization(self):
        """Test DataReceiveErrorEvent initialization and methods."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = DataReceiveErrorEvent(ar_root, "TestDataReceiveErrorEvent")

        assert event.parent == ar_root
        assert event.short_name == "TestDataReceiveErrorEvent"
        assert event.disabledModeIRefs == []
        assert event.startOnEventRef is None
        assert event.dataIRef is None

        # Test dataIRef methods
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs import RVariableInAtomicSwcInstanceRef

        iref = RVariableInAtomicSwcInstanceRef()
        event.setDataIRef(iref)
        assert event.getDataIRef() == iref


class TestOperationInvokedEvent:
    """Test class for OperationInvokedEvent class."""

    def test_operation_invoked_event_initialization(self):
        """Test OperationInvokedEvent initialization and methods."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = OperationInvokedEvent(ar_root, "TestOperationInvokedEvent")

        assert event.parent == ar_root
        assert event.short_name == "TestOperationInvokedEvent"
        assert event.disabledModeIRefs == []
        assert event.startOnEventRef is None
        assert event.operationIRef is None

        # Test operationIRef methods
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs import POperationInAtomicSwcInstanceRef

        iref = POperationInAtomicSwcInstanceRef()
        event.setOperationIRef(iref)
        assert event.getOperationIRef() == iref


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


class TestInternalTriggerOccurredEvent:
    """Test class for InternalTriggerOccurredEvent class."""

    def test_internal_trigger_occurred_event_initialization(self):
        """Test InternalTriggerOccurredEvent initialization and methods."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = InternalTriggerOccurredEvent(ar_root, "TestInternalTriggerOccurredEvent")

        assert event.parent == ar_root
        assert event.short_name == "TestInternalTriggerOccurredEvent"
        assert event.disabledModeIRefs == []
        assert event.startOnEventRef is None
        assert event.eventSourceRef is None

        # Test eventSourceRef methods
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType

        source_ref = RefType()
        source_ref.setValue("/Source/Ref")
        event.setEventSourceRef(source_ref)
        assert event.getEventSourceRef() == source_ref


class TestModeSwitchedAckEvent:
    """Test class for ModeSwitchedAckEvent class."""

    def test_mode_switched_ack_event_initialization(self):
        """Test ModeSwitchedAckEvent initialization and methods."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = ModeSwitchedAckEvent(ar_root, "TestModeSwitchedAckEvent")

        assert event.parent == ar_root
        assert event.short_name == "TestModeSwitchedAckEvent"
        assert event.disabledModeIRefs == []
        assert event.startOnEventRef is None
        assert event.eventSourceRef is None

        # Test eventSourceRef methods
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType

        source_ref = RefType()
        source_ref.setValue("/Source/Ref")
        event.setEventSourceRef(source_ref)
        assert event.getEventSourceRef() == source_ref


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


class TestWaitPoint:
    """Test class for WaitPoint class."""

    def test_wait_point_initialization(self):
        """Test WaitPoint initialization."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        point = WaitPoint(ar_root, "TestWaitPoint")

        assert point.parent == ar_root
        assert point.short_name == "TestWaitPoint"
        assert point.getTimeout() is None
        assert point.getTriggerRef() is None

    def test_get_set_timeout(self):
        """Test setTimeout/getTimeout round-trip."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        point = WaitPoint(ar_root, "TestWaitPoint")

        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import TimeValue

        timeout = TimeValue()
        timeout.setValue(5.0)
        result = point.setTimeout(timeout)
        assert result is point
        assert point.getTimeout() == timeout

    def test_set_timeout_none_noop(self):
        """Test setTimeout(None) is a no-op."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        point = WaitPoint(ar_root, "TestWaitPoint")

        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import TimeValue

        timeout = TimeValue()
        timeout.setValue(5.0)
        point.setTimeout(timeout)
        result = point.setTimeout(None)
        assert result is point
        assert point.getTimeout() == timeout

    def test_get_set_trigger_ref(self):
        """Test setTriggerRef/getTriggerRef round-trip."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        point = WaitPoint(ar_root, "TestWaitPoint")

        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType

        trigger_ref = RefType()
        trigger_ref.setDest("RTEEvent")
        trigger_ref.setValue("/Event")
        result = point.setTriggerRef(trigger_ref)
        assert result is point
        assert point.getTriggerRef() == trigger_ref

    def test_set_trigger_ref_none_noop(self):
        """Test setTriggerRef(None) is a no-op."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        point = WaitPoint(ar_root, "TestWaitPoint")

        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType

        trigger_ref = RefType()
        trigger_ref.setDest("RTEEvent")
        trigger_ref.setValue("/Event")
        point.setTriggerRef(trigger_ref)
        result = point.setTriggerRef(None)
        assert result is point
        assert point.getTriggerRef() == trigger_ref
