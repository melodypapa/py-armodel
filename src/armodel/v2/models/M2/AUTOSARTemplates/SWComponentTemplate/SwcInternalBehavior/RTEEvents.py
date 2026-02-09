"""
AUTOSAR Package - RTEEvents

Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::RTEEvents
"""

from abc import ABC
from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior import (
    AbstractEvent,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class RTEEvent(AbstractEvent, ABC):
    """
    Abstract base class for all RTE-related events
    
    Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::RTEEvents::RTEEvent
    
    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 327, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 541, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 208, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 238, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is RTEEvent:
            raise TypeError("RTEEvent is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # disabled by: RModeInAtomicSwc.
        self._disabledModeInstanceRef: List["ModeDeclaration"] = []

    @property
    def disabled_mode_instance_ref(self) -> List["ModeDeclaration"]:
        """Get disabledModeInstanceRef (Pythonic accessor)."""
        return self._disabledModeInstanceRef
        # The referenced RunnableEntity starts when the is raised.
        self._startOnEvent: Optional["RunnableEntity"] = None

    @property
    def start_on_event(self) -> Optional["RunnableEntity"]:
        """Get startOnEvent (Pythonic accessor)."""
        return self._startOnEvent

    @start_on_event.setter
    def start_on_event(self, value: Optional["RunnableEntity"]) -> None:
        """
        Set startOnEvent with validation.
        
        Args:
            value: The startOnEvent to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._startOnEvent = None
            return

        if not isinstance(value, RunnableEntity):
            raise TypeError(
                f"startOnEvent must be RunnableEntity or None, got {type(value).__name__}"
            )
        self._startOnEvent = value

    def with_disabled_mode_instance_ref(self, value):
        """
        Set disabled_mode_instance_ref and return self for chaining.

        Args:
            value: The disabled_mode_instance_ref to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_disabled_mode_instance_ref("value")
        """
        self.disabled_mode_instance_ref = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDisabledModeInstanceRef(self) -> List["ModeDeclaration"]:
        """
        AUTOSAR-compliant getter for disabledModeInstanceRef.
        
        Returns:
            The disabledModeInstanceRef value
        
        Note:
            Delegates to disabled_mode_instance_ref property (CODING_RULE_V2_00017)
        """
        return self.disabled_mode_instance_ref  # Delegates to property

    def getStartOnEvent(self) -> "RunnableEntity":
        """
        AUTOSAR-compliant getter for startOnEvent.
        
        Returns:
            The startOnEvent value
        
        Note:
            Delegates to start_on_event property (CODING_RULE_V2_00017)
        """
        return self.start_on_event  # Delegates to property

    def setStartOnEvent(self, value: "RunnableEntity") -> "RTEEvent":
        """
        AUTOSAR-compliant setter for startOnEvent with method chaining.
        
        Args:
            value: The startOnEvent to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to start_on_event property setter (gets validation automatically)
        """
        self.start_on_event = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_start_on_event(self, value: Optional["RunnableEntity"]) -> "RTEEvent":
        """
        Set startOnEvent and return self for chaining.
        
        Args:
            value: The startOnEvent to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_start_on_event("value")
        """
        self.start_on_event = value  # Use property setter (gets validation)
        return self



class WaitPoint(Identifiable):
    """
    This defines a wait-point for which the RunnableEntity can wait.
    
    Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::RTEEvents::WaitPoint
    
    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 550, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Time in seconds before the WaitPoint times out and the call returns with an
        # error indicating the.
        self._timeout: Optional["TimeValue"] = None

    @property
    def timeout(self) -> Optional["TimeValue"]:
        """Get timeout (Pythonic accessor)."""
        return self._timeout

    @timeout.setter
    def timeout(self, value: Optional["TimeValue"]) -> None:
        """
        Set timeout with validation.
        
        Args:
            value: The timeout to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timeout = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"timeout must be TimeValue or None, got {type(value).__name__}"
            )
        self._timeout = value
        self._trigger: Optional["RTEEvent"] = None

    @property
    def trigger(self) -> Optional["RTEEvent"]:
        """Get trigger (Pythonic accessor)."""
        return self._trigger

    @trigger.setter
    def trigger(self, value: Optional["RTEEvent"]) -> None:
        """
        Set trigger with validation.
        
        Args:
            value: The trigger to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._trigger = None
            return

        if not isinstance(value, RTEEvent):
            raise TypeError(
                f"trigger must be RTEEvent or None, got {type(value).__name__}"
            )
        self._trigger = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTimeout(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for timeout.
        
        Returns:
            The timeout value
        
        Note:
            Delegates to timeout property (CODING_RULE_V2_00017)
        """
        return self.timeout  # Delegates to property

    def setTimeout(self, value: "TimeValue") -> "WaitPoint":
        """
        AUTOSAR-compliant setter for timeout with method chaining.
        
        Args:
            value: The timeout to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to timeout property setter (gets validation automatically)
        """
        self.timeout = value  # Delegates to property setter
        return self

    def getTrigger(self) -> "RTEEvent":
        """
        AUTOSAR-compliant getter for trigger.
        
        Returns:
            The trigger value
        
        Note:
            Delegates to trigger property (CODING_RULE_V2_00017)
        """
        return self.trigger  # Delegates to property

    def setTrigger(self, value: "RTEEvent") -> "WaitPoint":
        """
        AUTOSAR-compliant setter for trigger with method chaining.
        
        Args:
            value: The trigger to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to trigger property setter (gets validation automatically)
        """
        self.trigger = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_timeout(self, value: Optional["TimeValue"]) -> "WaitPoint":
        """
        Set timeout and return self for chaining.
        
        Args:
            value: The timeout to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_timeout("value")
        """
        self.timeout = value  # Use property setter (gets validation)
        return self

    def with_trigger(self, value: Optional["RTEEvent"]) -> "WaitPoint":
        """
        Set trigger and return self for chaining.
        
        Args:
            value: The trigger to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_trigger("value")
        """
        self.trigger = value  # Use property setter (gets validation)
        return self



class OperationInvokedEvent(RTEEvent):
    """
    This event is raised when the ClientServerOperation referenced in
    OperationInvokedEvent.operation shall be invoked.
    
    Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::RTEEvents::OperationInvokedEvent
    
    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 325, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 543, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # by: POperationInAtomicSwc.
        self._operationInstanceRef: Optional["ClientServerOperation"] = None

    @property
    def operation_instance_ref(self) -> Optional["ClientServerOperation"]:
        """Get operationInstanceRef (Pythonic accessor)."""
        return self._operationInstanceRef

    @operation_instance_ref.setter
    def operation_instance_ref(self, value: Optional["ClientServerOperation"]) -> None:
        """
        Set operationInstanceRef with validation.
        
        Args:
            value: The operationInstanceRef to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._operationInstanceRef = None
            return

        if not isinstance(value, ClientServerOperation):
            raise TypeError(
                f"operationInstanceRef must be ClientServerOperation or None, got {type(value).__name__}"
            )
        self._operationInstanceRef = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getOperationInstanceRef(self) -> "ClientServerOperation":
        """
        AUTOSAR-compliant getter for operationInstanceRef.
        
        Returns:
            The operationInstanceRef value
        
        Note:
            Delegates to operation_instance_ref property (CODING_RULE_V2_00017)
        """
        return self.operation_instance_ref  # Delegates to property

    def setOperationInstanceRef(self, value: "ClientServerOperation") -> "OperationInvokedEvent":
        """
        AUTOSAR-compliant setter for operationInstanceRef with method chaining.
        
        Args:
            value: The operationInstanceRef to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to operation_instance_ref property setter (gets validation automatically)
        """
        self.operation_instance_ref = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_operation_instance_ref(self, value: Optional["ClientServerOperation"]) -> "OperationInvokedEvent":
        """
        Set operationInstanceRef and return self for chaining.
        
        Args:
            value: The operationInstanceRef to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_operation_instance_ref("value")
        """
        self.operation_instance_ref = value  # Use property setter (gets validation)
        return self



class TimingEvent(RTEEvent):
    """
    This event is used to start RunnableEntities that shall be executed
    periodically.
    
    Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::RTEEvents::TimingEvent
    
    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 532, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 254, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The value makes an assumption about the time offset of activation of the
                # RunnableEntity triggered by the relative to the periodic activation of base
                # of this TimingEvent.
        # Unit: second.
        self._offset: Optional["TimeValue"] = None

    @property
    def offset(self) -> Optional["TimeValue"]:
        """Get offset (Pythonic accessor)."""
        return self._offset

    @offset.setter
    def offset(self, value: Optional["TimeValue"]) -> None:
        """
        Set offset with validation.
        
        Args:
            value: The offset to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._offset = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"offset must be TimeValue or None, got {type(value).__name__}"
            )
        self._offset = value
        # The value of this be greater than zero.
        self._period: Optional["TimeValue"] = None

    @property
    def period(self) -> Optional["TimeValue"]:
        """Get period (Pythonic accessor)."""
        return self._period

    @period.setter
    def period(self, value: Optional["TimeValue"]) -> None:
        """
        Set period with validation.
        
        Args:
            value: The period to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._period = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"period must be TimeValue or None, got {type(value).__name__}"
            )
        self._period = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getOffset(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for offset.
        
        Returns:
            The offset value
        
        Note:
            Delegates to offset property (CODING_RULE_V2_00017)
        """
        return self.offset  # Delegates to property

    def setOffset(self, value: "TimeValue") -> "TimingEvent":
        """
        AUTOSAR-compliant setter for offset with method chaining.
        
        Args:
            value: The offset to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to offset property setter (gets validation automatically)
        """
        self.offset = value  # Delegates to property setter
        return self

    def getPeriod(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for period.
        
        Returns:
            The period value
        
        Note:
            Delegates to period property (CODING_RULE_V2_00017)
        """
        return self.period  # Delegates to property

    def setPeriod(self, value: "TimeValue") -> "TimingEvent":
        """
        AUTOSAR-compliant setter for period with method chaining.
        
        Args:
            value: The period to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to period property setter (gets validation automatically)
        """
        self.period = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_offset(self, value: Optional["TimeValue"]) -> "TimingEvent":
        """
        Set offset and return self for chaining.
        
        Args:
            value: The offset to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_offset("value")
        """
        self.offset = value  # Use property setter (gets validation)
        return self

    def with_period(self, value: Optional["TimeValue"]) -> "TimingEvent":
        """
        Set period and return self for chaining.
        
        Args:
            value: The period to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_period("value")
        """
        self.period = value  # Use property setter (gets validation)
        return self



class AsynchronousServerCallReturnsEvent(RTEEvent):
    """
    This event is raised when an asynchronous server call is finished.
    
    Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::RTEEvents::AsynchronousServerCallReturnsEvent
    
    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 541, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The referenced AsynchronousServerCallResultPoint this
        # AsynchronousServerCallReturnsEvent when server call returns.
        self._eventSource: Optional["AsynchronousServer"] = None

    @property
    def event_source(self) -> Optional["AsynchronousServer"]:
        """Get eventSource (Pythonic accessor)."""
        return self._eventSource

    @event_source.setter
    def event_source(self, value: Optional["AsynchronousServer"]) -> None:
        """
        Set eventSource with validation.
        
        Args:
            value: The eventSource to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._eventSource = None
            return

        if not isinstance(value, AsynchronousServer):
            raise TypeError(
                f"eventSource must be AsynchronousServer or None, got {type(value).__name__}"
            )
        self._eventSource = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getEventSource(self) -> "AsynchronousServer":
        """
        AUTOSAR-compliant getter for eventSource.
        
        Returns:
            The eventSource value
        
        Note:
            Delegates to event_source property (CODING_RULE_V2_00017)
        """
        return self.event_source  # Delegates to property

    def setEventSource(self, value: "AsynchronousServer") -> "AsynchronousServerCallReturnsEvent":
        """
        AUTOSAR-compliant setter for eventSource with method chaining.
        
        Args:
            value: The eventSource to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to event_source property setter (gets validation automatically)
        """
        self.event_source = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_event_source(self, value: Optional["AsynchronousServer"]) -> "AsynchronousServerCallReturnsEvent":
        """
        Set eventSource and return self for chaining.
        
        Args:
            value: The eventSource to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_event_source("value")
        """
        self.event_source = value  # Use property setter (gets validation)
        return self



class DataSendCompletedEvent(RTEEvent):
    """
    This event is raised when the referenced explicit data element has been sent
    or an error occurred.
    
    Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::RTEEvents::DataSendCompletedEvent
    
    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 542, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The referenced VariableAccess raises this DataSend the explicit write access
        # was an error occurred.
        self._eventSource: Optional["VariableAccess"] = None

    @property
    def event_source(self) -> Optional["VariableAccess"]:
        """Get eventSource (Pythonic accessor)."""
        return self._eventSource

    @event_source.setter
    def event_source(self, value: Optional["VariableAccess"]) -> None:
        """
        Set eventSource with validation.
        
        Args:
            value: The eventSource to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._eventSource = None
            return

        if not isinstance(value, VariableAccess):
            raise TypeError(
                f"eventSource must be VariableAccess or None, got {type(value).__name__}"
            )
        self._eventSource = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getEventSource(self) -> "VariableAccess":
        """
        AUTOSAR-compliant getter for eventSource.
        
        Returns:
            The eventSource value
        
        Note:
            Delegates to event_source property (CODING_RULE_V2_00017)
        """
        return self.event_source  # Delegates to property

    def setEventSource(self, value: "VariableAccess") -> "DataSendCompletedEvent":
        """
        AUTOSAR-compliant setter for eventSource with method chaining.
        
        Args:
            value: The eventSource to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to event_source property setter (gets validation automatically)
        """
        self.event_source = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_event_source(self, value: Optional["VariableAccess"]) -> "DataSendCompletedEvent":
        """
        Set eventSource and return self for chaining.
        
        Args:
            value: The eventSource to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_event_source("value")
        """
        self.event_source = value  # Use property setter (gets validation)
        return self



class DataWriteCompletedEvent(RTEEvent):
    """
    This event is raised when an implicit write access was successful or an
    error occurred.
    
    Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::RTEEvents::DataWriteCompletedEvent
    
    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 542, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The referenced VariableAccess raises this DataWrite the implicit write access
        # was an error occurred.
        self._eventSource: Optional["VariableAccess"] = None

    @property
    def event_source(self) -> Optional["VariableAccess"]:
        """Get eventSource (Pythonic accessor)."""
        return self._eventSource

    @event_source.setter
    def event_source(self, value: Optional["VariableAccess"]) -> None:
        """
        Set eventSource with validation.
        
        Args:
            value: The eventSource to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._eventSource = None
            return

        if not isinstance(value, VariableAccess):
            raise TypeError(
                f"eventSource must be VariableAccess or None, got {type(value).__name__}"
            )
        self._eventSource = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getEventSource(self) -> "VariableAccess":
        """
        AUTOSAR-compliant getter for eventSource.
        
        Returns:
            The eventSource value
        
        Note:
            Delegates to event_source property (CODING_RULE_V2_00017)
        """
        return self.event_source  # Delegates to property

    def setEventSource(self, value: "VariableAccess") -> "DataWriteCompletedEvent":
        """
        AUTOSAR-compliant setter for eventSource with method chaining.
        
        Args:
            value: The eventSource to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to event_source property setter (gets validation automatically)
        """
        self.event_source = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_event_source(self, value: Optional["VariableAccess"]) -> "DataWriteCompletedEvent":
        """
        Set eventSource and return self for chaining.
        
        Args:
            value: The eventSource to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_event_source("value")
        """
        self.event_source = value  # Use property setter (gets validation)
        return self



class DataReceivedEvent(RTEEvent):
    """
    This event is raised when the referenced data element is received.
    
    Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::RTEEvents::DataReceivedEvent
    
    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 542, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # the data has been received.
        # by: RVariableInAtomicSwc.
        self._data: Optional["RefType"] = None

    @property
    def data(self) -> Optional["RefType"]:
        """Get data (Pythonic accessor)."""
        return self._data

    @data.setter
    def data(self, value: Optional["RefType"]) -> None:
        """
        Set data with validation.
        
        Args:
            value: The data to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._data = None
            return

        self._data = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getData(self) -> "RefType":
        """
        AUTOSAR-compliant getter for data.
        
        Returns:
            The data value
        
        Note:
            Delegates to data property (CODING_RULE_V2_00017)
        """
        return self.data  # Delegates to property

    def setData(self, value: "RefType") -> "DataReceivedEvent":
        """
        AUTOSAR-compliant setter for data with method chaining.
        
        Args:
            value: The data to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to data property setter (gets validation automatically)
        """
        self.data = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_data(self, value: Optional[RefType]) -> "DataReceivedEvent":
        """
        Set data and return self for chaining.
        
        Args:
            value: The data to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_data("value")
        """
        self.data = value  # Use property setter (gets validation)
        return self



class DataReceiveErrorEvent(RTEEvent):
    """
    This event is raised when the Com layer detects and notifies an error
    concerning the reception of the referenced VariableDataPrototype.
    
    Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::RTEEvents::DataReceiveErrorEvent
    
    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 543, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # there was an error during the by: RVariableInAtomicSwc.
        self._data: Optional["RefType"] = None

    @property
    def data(self) -> Optional["RefType"]:
        """Get data (Pythonic accessor)."""
        return self._data

    @data.setter
    def data(self, value: Optional["RefType"]) -> None:
        """
        Set data with validation.
        
        Args:
            value: The data to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._data = None
            return

        self._data = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getData(self) -> "RefType":
        """
        AUTOSAR-compliant getter for data.
        
        Returns:
            The data value
        
        Note:
            Delegates to data property (CODING_RULE_V2_00017)
        """
        return self.data  # Delegates to property

    def setData(self, value: "RefType") -> "DataReceiveErrorEvent":
        """
        AUTOSAR-compliant setter for data with method chaining.
        
        Args:
            value: The data to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to data property setter (gets validation automatically)
        """
        self.data = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_data(self, value: Optional[RefType]) -> "DataReceiveErrorEvent":
        """
        Set data and return self for chaining.
        
        Args:
            value: The data to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_data("value")
        """
        self.data = value  # Use property setter (gets validation)
        return self



class BackgroundEvent(RTEEvent):
    """
    This event is used to start RunnableEntities that are supposed to be
    executed in the background.
    
    Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::RTEEvents::BackgroundEvent
    
    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 544, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class SwcModeSwitchEvent(RTEEvent):
    """
    This event is raised when the specified mode change occurs.
    
    Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::RTEEvents::SwcModeSwitchEvent
    
    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 544, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Specifies if the event is raised on entering or exiting a or is raised on the
                # transition between two ModeDeclaration 0.
        # 2 iref The referenced mode or the transition between two this
                # SwcModeSwitchEvent.
        # by: RModeInAtomicSwc.
        self._activation: Optional["ModeActivationKind"] = None

    @property
    def activation(self) -> Optional["ModeActivationKind"]:
        """Get activation (Pythonic accessor)."""
        return self._activation

    @activation.setter
    def activation(self, value: Optional["ModeActivationKind"]) -> None:
        """
        Set activation with validation.
        
        Args:
            value: The activation to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._activation = None
            return

        if not isinstance(value, ModeActivationKind):
            raise TypeError(
                f"activation must be ModeActivationKind or None, got {type(value).__name__}"
            )
        self._activation = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getActivation(self) -> "ModeActivationKind":
        """
        AUTOSAR-compliant getter for activation.
        
        Returns:
            The activation value
        
        Note:
            Delegates to activation property (CODING_RULE_V2_00017)
        """
        return self.activation  # Delegates to property

    def setActivation(self, value: "ModeActivationKind") -> "SwcModeSwitchEvent":
        """
        AUTOSAR-compliant setter for activation with method chaining.
        
        Args:
            value: The activation to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to activation property setter (gets validation automatically)
        """
        self.activation = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_activation(self, value: Optional["ModeActivationKind"]) -> "SwcModeSwitchEvent":
        """
        Set activation and return self for chaining.
        
        Args:
            value: The activation to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_activation("value")
        """
        self.activation = value  # Use property setter (gets validation)
        return self



class ModeSwitchedAckEvent(RTEEvent):
    """
    This event is raised when the referenced ModeSwitchPoint has been processed
    or an error occurred.
    
    Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::RTEEvents::ModeSwitchedAckEvent
    
    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 545, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The referenced ModeSwitchPoint raises this Mode the ModeSwitchPoint has been.
        self._eventSource: Optional["ModeSwitchPoint"] = None

    @property
    def event_source(self) -> Optional["ModeSwitchPoint"]:
        """Get eventSource (Pythonic accessor)."""
        return self._eventSource

    @event_source.setter
    def event_source(self, value: Optional["ModeSwitchPoint"]) -> None:
        """
        Set eventSource with validation.
        
        Args:
            value: The eventSource to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._eventSource = None
            return

        if not isinstance(value, ModeSwitchPoint):
            raise TypeError(
                f"eventSource must be ModeSwitchPoint or None, got {type(value).__name__}"
            )
        self._eventSource = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getEventSource(self) -> "ModeSwitchPoint":
        """
        AUTOSAR-compliant getter for eventSource.
        
        Returns:
            The eventSource value
        
        Note:
            Delegates to event_source property (CODING_RULE_V2_00017)
        """
        return self.event_source  # Delegates to property

    def setEventSource(self, value: "ModeSwitchPoint") -> "ModeSwitchedAckEvent":
        """
        AUTOSAR-compliant setter for eventSource with method chaining.
        
        Args:
            value: The eventSource to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to event_source property setter (gets validation automatically)
        """
        self.event_source = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_event_source(self, value: Optional["ModeSwitchPoint"]) -> "ModeSwitchedAckEvent":
        """
        Set eventSource and return self for chaining.
        
        Args:
            value: The eventSource to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_event_source("value")
        """
        self.event_source = value  # Use property setter (gets validation)
        return self



class ExternalTriggerOccurredEvent(RTEEvent):
    """
    This event is raised when the referenced Trigger has occurred.
    
    Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::RTEEvents::ExternalTriggerOccurredEvent
    
    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 545, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # by: RTriggerInAtomicSwc.
        self._triggerInstanceRef: Optional["RefType"] = None

    @property
    def trigger_instance_ref(self) -> Optional["RefType"]:
        """Get triggerInstanceRef (Pythonic accessor)."""
        return self._triggerInstanceRef

    @trigger_instance_ref.setter
    def trigger_instance_ref(self, value: Optional["RefType"]) -> None:
        """
        Set triggerInstanceRef with validation.
        
        Args:
            value: The triggerInstanceRef to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._triggerInstanceRef = None
            return

        self._triggerInstanceRef = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTriggerInstanceRef(self) -> "RefType":
        """
        AUTOSAR-compliant getter for triggerInstanceRef.
        
        Returns:
            The triggerInstanceRef value
        
        Note:
            Delegates to trigger_instance_ref property (CODING_RULE_V2_00017)
        """
        return self.trigger_instance_ref  # Delegates to property

    def setTriggerInstanceRef(self, value: "RefType") -> "ExternalTriggerOccurredEvent":
        """
        AUTOSAR-compliant setter for triggerInstanceRef with method chaining.
        
        Args:
            value: The triggerInstanceRef to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to trigger_instance_ref property setter (gets validation automatically)
        """
        self.trigger_instance_ref = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_trigger_instance_ref(self, value: Optional[RefType]) -> "ExternalTriggerOccurredEvent":
        """
        Set triggerInstanceRef and return self for chaining.
        
        Args:
            value: The triggerInstanceRef to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_trigger_instance_ref("value")
        """
        self.trigger_instance_ref = value  # Use property setter (gets validation)
        return self



class InternalTriggerOccurredEvent(RTEEvent):
    """
    This event is raised when the referenced InternalTriggeringPoint has
    occurred.
    
    Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::RTEEvents::InternalTriggerOccurredEvent
    
    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 546, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The referenced InternalTriggeringPoint raises this Internal.
        self._eventSource: Optional["RefType"] = None

    @property
    def event_source(self) -> Optional["RefType"]:
        """Get eventSource (Pythonic accessor)."""
        return self._eventSource

    @event_source.setter
    def event_source(self, value: Optional["RefType"]) -> None:
        """
        Set eventSource with validation.
        
        Args:
            value: The eventSource to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._eventSource = None
            return

        self._eventSource = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getEventSource(self) -> "RefType":
        """
        AUTOSAR-compliant getter for eventSource.
        
        Returns:
            The eventSource value
        
        Note:
            Delegates to event_source property (CODING_RULE_V2_00017)
        """
        return self.event_source  # Delegates to property

    def setEventSource(self, value: "RefType") -> "InternalTriggerOccurredEvent":
        """
        AUTOSAR-compliant setter for eventSource with method chaining.
        
        Args:
            value: The eventSource to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to event_source property setter (gets validation automatically)
        """
        self.event_source = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_event_source(self, value: Optional[RefType]) -> "InternalTriggerOccurredEvent":
        """
        Set eventSource and return self for chaining.
        
        Args:
            value: The eventSource to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_event_source("value")
        """
        self.event_source = value  # Use property setter (gets validation)
        return self



class InitEvent(RTEEvent):
    """
    This RTEEvent is supposed to be used for initialization purposes, i.e. for
    starting and restarting a partition. It is not guaranteed that all
    RunnableEntities referenced by this InitEvent are executed before the
    ’regular’ RunnableEntities are executed for the first time. The execution
    order depends on the task mapping.
    
    Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::RTEEvents::InitEvent
    
    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 546, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class TransformerHardErrorEvent(RTEEvent):
    """
    This event is raised when data are received which should trigger a
    Client/Server operation or an external Trigger but during transformation of
    the data a hard transformer error occurred.
    
    Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::RTEEvents::TransformerHardErrorEvent
    
    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 546, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # raise this TransformerHardErrorEvent.
        # by: POperationInAtomicSwc.
        self._operation: Optional["ClientServerOperation"] = None

    @property
    def operation(self) -> Optional["ClientServerOperation"]:
        """Get operation (Pythonic accessor)."""
        return self._operation

    @operation.setter
    def operation(self, value: Optional["ClientServerOperation"]) -> None:
        """
        Set operation with validation.
        
        Args:
            value: The operation to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._operation = None
            return

        if not isinstance(value, ClientServerOperation):
            raise TypeError(
                f"operation must be ClientServerOperation or None, got {type(value).__name__}"
            )
        self._operation = value
        # by: RTriggerInAtomicSwc.
        self._requiredTrigger: Optional["RefType"] = None

    @property
    def required_trigger(self) -> Optional["RefType"]:
        """Get requiredTrigger (Pythonic accessor)."""
        return self._requiredTrigger

    @required_trigger.setter
    def required_trigger(self, value: Optional["RefType"]) -> None:
        """
        Set requiredTrigger with validation.
        
        Args:
            value: The requiredTrigger to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._requiredTrigger = None
            return

        self._requiredTrigger = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getOperation(self) -> "ClientServerOperation":
        """
        AUTOSAR-compliant getter for operation.
        
        Returns:
            The operation value
        
        Note:
            Delegates to operation property (CODING_RULE_V2_00017)
        """
        return self.operation  # Delegates to property

    def setOperation(self, value: "ClientServerOperation") -> "TransformerHardErrorEvent":
        """
        AUTOSAR-compliant setter for operation with method chaining.
        
        Args:
            value: The operation to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to operation property setter (gets validation automatically)
        """
        self.operation = value  # Delegates to property setter
        return self

    def getRequiredTrigger(self) -> "RefType":
        """
        AUTOSAR-compliant getter for requiredTrigger.
        
        Returns:
            The requiredTrigger value
        
        Note:
            Delegates to required_trigger property (CODING_RULE_V2_00017)
        """
        return self.required_trigger  # Delegates to property

    def setRequiredTrigger(self, value: "RefType") -> "TransformerHardErrorEvent":
        """
        AUTOSAR-compliant setter for requiredTrigger with method chaining.
        
        Args:
            value: The requiredTrigger to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to required_trigger property setter (gets validation automatically)
        """
        self.required_trigger = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_operation(self, value: Optional["ClientServerOperation"]) -> "TransformerHardErrorEvent":
        """
        Set operation and return self for chaining.
        
        Args:
            value: The operation to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_operation("value")
        """
        self.operation = value  # Use property setter (gets validation)
        return self

    def with_required_trigger(self, value: Optional[RefType]) -> "TransformerHardErrorEvent":
        """
        Set requiredTrigger and return self for chaining.
        
        Args:
            value: The requiredTrigger to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_required_trigger("value")
        """
        self.required_trigger = value  # Use property setter (gets validation)
        return self



class OsTaskExecutionEvent(RTEEvent):
    """
    This RTEEvent is supposed to execute RunnableEntities which have to react on
    the execution of specific OsTasks. Therefore, this event is unconditionally
    raised whenever the OsTask on which it is mapped is executed. The main use
    case for this event is scheduling of Runnables of Complex Drivers which have
    to react on task executions.
    
    Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::RTEEvents::OsTaskExecutionEvent
    
    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 547, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class SwcModeManagerErrorEvent(RTEEvent):
    """
    This event is raised when an error occurred during the handling of the
    referenced ModeDeclarationGroup Prototype.
    
    Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::RTEEvents::SwcModeManagerErrorEvent
    
    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 637, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # this SwcModeManagerErrorEvent is raised in case error.
        # by: PModeGroupInAtomic.
        self._modeGroup: Optional["RefType"] = None

    @property
    def mode_group(self) -> Optional["RefType"]:
        """Get modeGroup (Pythonic accessor)."""
        return self._modeGroup

    @mode_group.setter
    def mode_group(self, value: Optional["RefType"]) -> None:
        """
        Set modeGroup with validation.
        
        Args:
            value: The modeGroup to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._modeGroup = None
            return

        self._modeGroup = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getModeGroup(self) -> "RefType":
        """
        AUTOSAR-compliant getter for modeGroup.
        
        Returns:
            The modeGroup value
        
        Note:
            Delegates to mode_group property (CODING_RULE_V2_00017)
        """
        return self.mode_group  # Delegates to property

    def setModeGroup(self, value: "RefType") -> "SwcModeManagerErrorEvent":
        """
        AUTOSAR-compliant setter for modeGroup with method chaining.
        
        Args:
            value: The modeGroup to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to mode_group property setter (gets validation automatically)
        """
        self.mode_group = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_mode_group(self, value: Optional[RefType]) -> "SwcModeManagerErrorEvent":
        """
        Set modeGroup and return self for chaining.
        
        Args:
            value: The modeGroup to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_mode_group("value")
        """
        self.mode_group = value  # Use property setter (gets validation)
        return self
