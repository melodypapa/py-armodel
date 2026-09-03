"""
This module contains classes for representing AUTOSAR RTE events
in software component internal behavior templates.
"""

from abc import ABC
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.VariationPointCapable import VariationPointCapable
from typing import List, Optional
from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior import AbstractEvent
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration import ModeActivationKind
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpStructureElement
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs import RVariableInAtomicSwcInstanceRef, RModeInAtomicSwcInstanceRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs import POperationInAtomicSwcInstanceRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType, TimeValue


class RTEEvent(AtpStructureElement, AbstractEvent, VariationPointCapable, ABC):
    """
    Abstract base class for all RTE-related events.
    """

    # RTEEvent method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getDisabledModeIRefs         [x] impl  [x] docstring  [ ] test
    # [ ] addDisabledModeIRef          [x] impl  [x] docstring  [ ] test
    # [ ] getStartOnEventRef           [x] impl  [x] docstring  [ ] test
    # [ ] setStartOnEventRef           [x] impl  [x] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is RTEEvent:
            raise TypeError("RTEEvent is an abstract class.")
        super().__init__(parent, short_name)

        self.disabledModeIRefs: List["RModeInAtomicSwcInstanceRef"] = []
        self.startOnEventRef: "RefType" = None

    def getDisabledModeIRefs(self):
        """
        Gets the list of disabled mode instance references.

        Returns:
            List[RModeInAtomicSwcInstanceRef]: The disabled mode references
        """
        return self.disabledModeIRefs

    def addDisabledModeIRef(self, value):
        """
        Adds a disabled mode instance reference.

        Args:
            value: The mode instance reference to add

        Returns:
            self for method chaining
        """
        self.disabledModeIRefs.append(value)
        return self

    def getStartOnEventRef(self):
        """
        Gets the reference to the runnable entity started by this event.

        Returns:
            RefType: The start-on-event reference
        """
        return self.startOnEventRef

    def setStartOnEventRef(self, value):
        """
        Sets the reference to the runnable entity started by this event.

        Args:
            value: The start-on-event reference to set

        Returns:
            self for method chaining
        """
        self.startOnEventRef = value
        return self


class AsynchronousServerCallReturnsEvent(RTEEvent):
    """
    This event is raised when an asynchronous server call is finished.
    """

    # AsynchronousServerCallReturnsEvent method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getEventSourceRef            [x] impl  [x] docstring  [ ] test
    # [ ] setEventSourceRef            [x] impl  [x] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.eventSourceRef: RefType = None

    def getEventSourceRef(self):
        """
        Gets the event source reference.

        Returns:
            RefType: The event source reference
        """
        return self.eventSourceRef

    def setEventSourceRef(self, value):
        """
        Sets the event source reference.

        Args:
            value: The event source reference to set

        Returns:
            self for method chaining
        """
        self.eventSourceRef = value
        return self


class DataSendCompletedEvent(RTEEvent):
    """
    This event is raised when the referenced explicit data element has been
    sent or an error occurred.
    """

    # DataSendCompletedEvent method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getEventSourceRef            [x] impl  [x] docstring  [ ] test
    # [ ] setEventSourceRef            [x] impl  [x] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.eventSourceRef: "RefType" = None

    def getEventSourceRef(self):
        """
        Gets the event source reference.

        Returns:
            RefType: The event source reference
        """
        return self.eventSourceRef

    def setEventSourceRef(self, value):
        """
        Sets the event source reference.

        Args:
            value: The event source reference to set

        Returns:
            self for method chaining
        """
        self.eventSourceRef = value
        return self


class DataWriteCompletedEvent(RTEEvent):
    """
    This event is raised when an implicit write access was successful or
    an error occurred.
    """

    # DataWriteCompletedEvent method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getEventSourceRef            [x] impl  [x] docstring  [ ] test
    # [ ] setEventSourceRef            [x] impl  [x] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.eventSourceRef: "RefType" = None

    def getEventSourceRef(self):
        """
        Gets the event source reference.

        Returns:
            RefType: The event source reference
        """
        return self.eventSourceRef

    def setEventSourceRef(self, value):
        """
        Sets the event source reference.

        Args:
            value: The event source reference to set

        Returns:
            self for method chaining
        """
        self.eventSourceRef = value
        return self


class DataReceivedEvent(RTEEvent):
    """
    This event is raised when the referenced data element is received.
    """

    # DataReceivedEvent method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getDataIRef                  [x] impl  [x] docstring  [ ] test
    # [ ] setDataIRef                  [x] impl  [x] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.dataIRef: "RVariableInAtomicSwcInstanceRef" = None

    def getDataIRef(self):
        """
        Gets the data instance reference.

        Returns:
            RVariableInAtomicSwcInstanceRef: The data instance reference
        """
        return self.dataIRef

    def setDataIRef(self, value):
        """
        Sets the data instance reference.

        Args:
            value: The data instance reference to set

        Returns:
            self for method chaining
        """
        self.dataIRef = value
        return self


class SwcModeSwitchEvent(RTEEvent):
    """
    This event is raised when the specified mode change occurs.
    """

    # SwcModeSwitchEvent method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 7.17, p.544
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__         [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getActivation    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setActivation    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] addModeIRef      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getModeIRefs     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Specifies if the event is raised on entering or exiting a specific mode or is raised on the transition between two modes.
        self.activation: Optional[ModeActivationKind] = None

        # The referenced mode or the transition between two modes raises this SwcModeSwitchEvent. InstanceRef implemented by: RModeInAtomicSwc InstanceRef
        self.modeIRefs: List[RModeInAtomicSwcInstanceRef] = []

    def getActivation(self) -> Optional[ModeActivationKind]:
        """
        Specifies if the event is raised on entering or exiting a specific mode or is raised on the transition between two modes.
        """
        return self.activation

    def setActivation(self, value: Optional[ModeActivationKind]) -> "SwcModeSwitchEvent":
        """
        Specifies if the event is raised on entering or exiting a specific mode or is raised on the transition between two modes.
        A None value is a no-op and does not overwrite an existing activation.
        """
        if value is not None:
            self.activation = value
        return self

    def addModeIRef(self, value: Optional[RModeInAtomicSwcInstanceRef]) -> "SwcModeSwitchEvent":
        """
        The referenced mode or the transition between two modes raises this SwcModeSwitchEvent. InstanceRef implemented by: RModeInAtomicSwc InstanceRef
        A None value is a no-op and does not append anything.
        """
        if value is not None:
            self.modeIRefs.append(value)
        return self

    def getModeIRefs(self) -> List[RModeInAtomicSwcInstanceRef]:
        """
        The referenced mode or the transition between two modes raises this SwcModeSwitchEvent. InstanceRef implemented by: RModeInAtomicSwc InstanceRef
        """
        return self.modeIRefs


class DataReceiveErrorEvent(RTEEvent):
    """
    This event is raised when the Com layer detects and notifies an error
    concerning the reception of the referenced VariableDataPrototype.
    """

    # DataReceiveErrorEvent method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getDataIRef                  [x] impl  [x] docstring  [ ] test
    # [ ] setDataIRef                  [x] impl  [x] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.dataIRef: "RVariableInAtomicSwcInstanceRef" = None

    def getDataIRef(self):
        """
        Gets the data instance reference.

        Returns:
            RVariableInAtomicSwcInstanceRef: The data instance reference
        """
        return self.dataIRef

    def setDataIRef(self, value):
        """
        Sets the data instance reference.

        Args:
            value: The data instance reference to set

        Returns:
            self for method chaining
        """
        self.dataIRef = value
        return self


class OperationInvokedEvent(RTEEvent):
    """
    This event is raised when the ClientServerOperation referenced in
    OperationInvokedEvent.operation shall be invoked.
    """

    # OperationInvokedEvent method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getOperationIRef             [x] impl  [x] docstring  [ ] test
    # [ ] setOperationIRef             [x] impl  [x] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.operationIRef: "POperationInAtomicSwcInstanceRef" = None

    def getOperationIRef(self):
        """
        Gets the operation instance reference.

        Returns:
            POperationInAtomicSwcInstanceRef: The operation instance reference
        """
        return self.operationIRef

    def setOperationIRef(self, value):
        """
        Sets the operation instance reference.

        Args:
            value: The operation instance reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.operationIRef = value
        return self


class InitEvent(RTEEvent):
    """
    This RTEEvent is used for initialization purposes, i.e. for starting and
    restarting a partition. It is not guaranteed that all RunnableEntities
    referenced by this InitEvent are executed before the 'regular'
    RunnableEntities are executed for the first time.
    """

    # InitEvent method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class TimingEvent(RTEEvent):
    """
    This event is used to start RunnableEntities that shall be executed
    periodically.
    """

    # TimingEvent method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] periodMs                     [x] impl  [ ] docstring  [ ] test
    # [ ] getOffset                    [x] impl  [x] docstring  [ ] test
    # [ ] setOffset                    [x] impl  [x] docstring  [ ] test
    # [ ] getPeriod                    [x] impl  [x] docstring  [ ] test
    # [ ] setPeriod                    [x] impl  [x] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.offset: "TimeValue" = None
        self.period: "TimeValue" = None

    @property
    def periodMs(self):
        if self.period is None:
            return None
        else:
            period_value = self.period.getValue() if hasattr(self.period, "getValue") else self.period
            if period_value < 0.001:
                return period_value * 1000
            else:
                return (int)(period_value * 1000)

    def getOffset(self):
        """
        Gets the offset before the first event firing.

        Returns:
            TimeValue: The offset
        """
        return self.offset

    def setOffset(self, value):
        """
        Sets the offset before the first event firing.

        Args:
            value: The offset to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.offset = value
        return self

    def getPeriod(self):
        """
        Gets the period between event firings.

        Returns:
            TimeValue: The period
        """
        return self.period

    def setPeriod(self, value):
        """
        Sets the period between event firings.

        Args:
            value: The period to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.period = value
        return self


class InternalTriggerOccurredEvent(RTEEvent):
    """
    This event is raised when the referenced InternalTriggeringPoint has
    occurred.
    """

    # InternalTriggerOccurredEvent method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getEventSourceRef            [x] impl  [x] docstring  [ ] test
    # [ ] setEventSourceRef            [x] impl  [x] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.eventSourceRef: "RefType" = None

    def getEventSourceRef(self):
        """
        Gets the event source reference.

        Returns:
            RefType: The event source reference
        """
        return self.eventSourceRef

    def setEventSourceRef(self, value):
        """
        Sets the event source reference.

        Args:
            value: The event source reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.eventSourceRef = value
        return self


class BackgroundEvent(RTEEvent):
    """
    This event is used to start RunnableEntities that are supposed to be
    executed in the background.
    """

    # BackgroundEvent method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class ModeSwitchedAckEvent(RTEEvent):
    """
    This event is raised when the referenced ModeSwitchPoint has been
    processed or an error occurred.
    """

    # ModeSwitchedAckEvent method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getEventSourceRef            [x] impl  [x] docstring  [ ] test
    # [ ] setEventSourceRef            [x] impl  [x] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.eventSourceRef: RefType = None

    def getEventSourceRef(self):
        """
        Gets the event source reference.

        Returns:
            RefType: The event source reference
        """
        return self.eventSourceRef

    def setEventSourceRef(self, value):
        """
        Sets the event source reference.

        Args:
            value: The event source reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.eventSourceRef = value
        return self


class WaitPoint(Identifiable):
    """
    This defines a wait-point for which the RunnableEntity can wait.
    """

    # WaitPoint method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 7.25, p.550
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getTimeout                   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setTimeout                   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTriggerRef                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setTriggerRef                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Time in seconds before the WaitPoint times out and the blocking wait call returns with an error indicating the timeout.
        self.timeout: Optional[TimeValue] = None

        # This is the RTEEvent this WaitPoint is waiting for.
        self.triggerRef: Optional[RefType] = None

    def getTimeout(self) -> Optional[TimeValue]:
        """
        Time in seconds before the WaitPoint times out and the blocking wait call returns with an error indicating the timeout.

        Returns:
            Optional[TimeValue]: The timeout, or None if not set
        """
        return self.timeout

    def setTimeout(self, value: Optional[TimeValue]) -> "WaitPoint":
        """
        Time in seconds before the WaitPoint times out and the blocking wait call returns with an error indicating the timeout.
        A None value is a no-op and does not overwrite an existing timeout.

        Args:
            value: The timeout to set

        Returns:
            WaitPoint: self for method chaining
        """
        if value is not None:
            self.timeout = value
        return self

    def getTriggerRef(self) -> Optional[RefType]:
        """
        This is the RTEEvent this WaitPoint is waiting for.

        Returns:
            Optional[RefType]: The trigger reference, or None if not set
        """
        return self.triggerRef

    def setTriggerRef(self, value: Optional[RefType]) -> "WaitPoint":
        """
        This is the RTEEvent this WaitPoint is waiting for.
        A None value is a no-op and does not overwrite an existing triggerRef.

        Args:
            value: The trigger reference to set

        Returns:
            WaitPoint: self for method chaining
        """
        if value is not None:
            self.triggerRef = value
        return self
