"""
This module contains comprehensive tests for the RTEEvents module in SWComponentTemplate.SwcInternalBehavior.
Tests cover all classes and methods in the RTEEvents.py file to achieve 100% test coverage.
"""

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
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
)


class TestRTEEvent:
    """Test class for RTEEvent abstract class."""

    def test_abstract_class_cannot_be_instantiated(self):
        """Test that RTEEvent abstract class cannot be instantiated directly."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        with pytest.raises(TypeError, match="RTEEvent is an abstract class"):
            RTEEvent(ar_root, "TestRTEEvent")

    def test_concrete_subclass_initialization(self):
        """Test that a concrete subclass of RTEEvent can be instantiated."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        rte_event = InitEvent(ar_root, "TestRTEEvent")

        assert rte_event.parent == ar_root
        assert rte_event.short_name == "TestRTEEvent"
        assert rte_event.disabledModeIRefs == []
        assert rte_event.startOnEventRef is None

        # Test disabledModeIRefs methods
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs import (
            RModeInAtomicSwcInstanceRef,
        )
        iref = RModeInAtomicSwcInstanceRef()
        rte_event.addDisabledModeIRef(iref)
        assert iref in rte_event.getDisabledModeIRefs()

        # Test startOnEventRef methods
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
            RefType,
        )
        event_ref = RefType()
        event_ref.setValue("/Event/Ref")
        rte_event.setStartOnEventRef(event_ref)
        assert rte_event.getStartOnEventRef() == event_ref


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
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
            RefType,
        )
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
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
            RefType,
        )
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
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
            RefType,
        )
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
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs import (
            RVariableInAtomicSwcInstanceRef,
        )
        iref = RVariableInAtomicSwcInstanceRef()
        event.setDataIRef(iref)
        assert event.getDataIRef() == iref


class TestSwcModeSwitchEvent:
    """Test class for SwcModeSwitchEvent class."""

    def test_swc_mode_switch_event_initialization(self):
        """Test SwcModeSwitchEvent initialization and methods."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = SwcModeSwitchEvent(ar_root, "TestSwcModeSwitchEvent")

        assert event.parent == ar_root
        assert event.short_name == "TestSwcModeSwitchEvent"
        assert event.disabledModeIRefs == []
        assert event.startOnEventRef is None
        assert event.activation is None
        assert event.modeIRefs == []

        # Test activation methods
        activation = "test_activation"
        event.setActivation(activation)
        assert event.getActivation() == activation

        # Test modeIRefs methods
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs import (
            RModeInAtomicSwcInstanceRef,
        )
        iref = RModeInAtomicSwcInstanceRef()
        event.addModeIRef(iref)
        assert iref in event.getModeIRefs()


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
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs import (
            RVariableInAtomicSwcInstanceRef,
        )
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
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs import (
            POperationInAtomicSwcInstanceRef,
        )
        iref = POperationInAtomicSwcInstanceRef()
        event.setOperationIRef(iref)
        assert event.getOperationIRef() == iref


class TestInitEvent:
    """Test class for InitEvent class."""

    def test_init_event_initialization(self):
        """Test InitEvent initialization."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        event = InitEvent(ar_root, "TestInitEvent")

        assert event.parent == ar_root
        assert event.short_name == "TestInitEvent"
        assert event.disabledModeIRefs == []
        assert event.startOnEventRef is None


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
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
            TimeValue,
        )
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
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
            RefType,
        )
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
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
            RefType,
        )
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
