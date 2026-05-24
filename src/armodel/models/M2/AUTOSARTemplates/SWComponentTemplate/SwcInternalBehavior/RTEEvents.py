"""
This module contains classes for representing AUTOSAR RTE events
in software component internal behavior templates.
"""

from abc import ABC
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpStructureElement
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs import RVariableInAtomicSwcInstanceRef, RModeInAtomicSwcInstanceRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.InstanceRefs import POperationInAtomicSwcInstanceRef
from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior import AbstractEvent
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType, TimeValue
from typing import List


class RTEEvent(AtpStructureElement, ABC):
    """
    Abstract base class for all RTE-related events.
    """

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is RTEEvent:
            raise TypeError("RTEEvent is an abstract class.")
        super().__init__(parent, short_name)

        self.disabledModeIRefs: List['RModeInAtomicSwcInstanceRef'] = []
        self.startOnEventRef: 'RefType' = None

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

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.eventSourceRef: 'RefType' = None

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

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.eventSourceRef: 'RefType' = None

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

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.dataIRef: 'RVariableInAtomicSwcInstanceRef' = None

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

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.activation = None
        self.modeIRefs: List['RModeInAtomicSwcInstanceRef'] = []

    def getActivation(self):
        """
        Gets the activation setting.

        Returns:
            The activation setting
        """
        return self.activation

    def setActivation(self, value):
        """
        Sets the activation setting.

        Args:
            value: The activation setting to set

        Returns:
            self for method chaining
        """
        self.activation = value
        return self

    def getModeIRefs(self):
        """
        Gets the list of mode instance references.

        Returns:
            List[RModeInAtomicSwcInstanceRef]: The mode instance references
        """
        return self.modeIRefs

    def addModeIRef(self, value):
        """
        Adds a mode instance reference.

        Args:
            value: The mode instance reference to add

        Returns:
            self for method chaining
        """
        self.modeIRefs.append(value)
        return self


class DataReceiveErrorEvent(RTEEvent):
    """
    This event is raised when the Com layer detects and notifies an error
    concerning the reception of the referenced VariableDataPrototype.
    """

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.dataIRef: 'RVariableInAtomicSwcInstanceRef' = None

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

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.operationIRef: 'POperationInAtomicSwcInstanceRef' = None

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

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class TimingEvent(RTEEvent):
    """
    This event is used to start RunnableEntities that shall be executed
    periodically.
    """

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.offset: 'TimeValue' = None
        self.period: 'TimeValue' = None

    @property
    def periodMs(self):
        if self.period is None:
            return None
        else:
            period_value = self.period.getValue() if hasattr(self.period, 'getValue') else self.period
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

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.eventSourceRef: 'RefType' = None

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

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class ModeSwitchedAckEvent(RTEEvent):
    """
    This event is raised when the referenced ModeSwitchPoint has been
    processed or an error occurred.
    """

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
