"""
This module contains classes for representing AUTOSAR RTE events
in software component internal behavior templates.
"""

from __future__ import annotations

from abc import ABC
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.StereotypeMixins import VariationPointCapable
from typing import List, Optional
from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior import AbstractEvent
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration import ModeActivationKind
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpStructureElement
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs import RVariableInAtomicSwcInstanceRef, RModeInAtomicSwcInstanceRef, RTriggerInAtomicSwcInstanceRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs import POperationInAtomicSwcInstanceRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType, TimeValue


class RTEEvent(AtpStructureElement, AbstractEvent, VariationPointCapable, ABC):
    """Abstract base class for all RTE-related events"""

    # RTEEvent method parity checklist:
    # Spec: R23-11/AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 7.9, p.541 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getDisabledModeIRefs    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addDisabledModeIRef     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getStartOnEventRef      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setStartOnEventRef      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is RTEEvent:
            raise TypeError("RTEEvent is an abstract class.")
        super().__init__(parent, short_name)

        # Reference to the Modes that disable the Event.
        self.disabledModeIRefs: List[RModeInAtomicSwcInstanceRef] = []

        # The referenced RunnableEntity starts when the corresponding RTEEvent is raised.
        self.startOnEventRef: Optional[RefType] = None

    def getDisabledModeIRefs(self) -> List[RModeInAtomicSwcInstanceRef]:
        """
        Reference to the Modes that disable the Event.
        """
        return self.disabledModeIRefs

    def addDisabledModeIRef(self, value: Optional[RModeInAtomicSwcInstanceRef]) -> RTEEvent:
        """
        Reference to the Modes that disable the Event.
        A None value is a no-op and does not append anything.
        """
        if value is not None:
            self.disabledModeIRefs.append(value)
        return self

    def getStartOnEventRef(self) -> Optional[RefType]:
        """
        The referenced RunnableEntity starts when the corresponding RTEEvent is raised.
        """
        return self.startOnEventRef

    def setStartOnEventRef(self, value: Optional[RefType]) -> RTEEvent:
        """
        The referenced RunnableEntity starts when the corresponding RTEEvent is raised.
        A None value is a no-op and does not overwrite an existing startOnEventRef.
        """
        if value is not None:
            self.startOnEventRef = value
        return self


class AsynchronousServerCallReturnsEvent(RTEEvent):
    """
    This event is raised when an asynchronous server call is finished.

    [constr_1940] Existence of attribute AsynchronousServerCallReturnsEvent.eventSource: For each AsynchronousServerCallReturnsEvent, attribute eventSource shall exist at the time when the contract phase generation is executed.
    """

    # AsynchronousServerCallReturnsEvent method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 7.10, p.541
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__          [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getEventSourceRef [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setEventSourceRef [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # The referenced AsynchronousServerCallResultPoint raises this AsynchronousServerCallReturnsEvent when the asynchronous server call returns.
        self.eventSourceRef: Optional[RefType] = None

    def getEventSourceRef(self) -> Optional[RefType]:
        """
        The referenced AsynchronousServerCallResultPoint raises this AsynchronousServerCallReturnsEvent when the asynchronous server call returns.
        """
        return self.eventSourceRef

    def setEventSourceRef(self, value: Optional[RefType]) -> AsynchronousServerCallReturnsEvent:
        """
        The referenced AsynchronousServerCallResultPoint raises this AsynchronousServerCallReturnsEvent when the asynchronous server call returns.
        A None value is a no-op and does not overwrite an existing eventSourceRef.
        """
        if value is not None:
            self.eventSourceRef = value
        return self


class DataSendCompletedEvent(RTEEvent):
    """
    This event is raised when the referenced explicit data element has been sent or an error occurred.

    [constr_1941] Existence of attribute DataSendCompletedEvent.eventSource: For each DataSendCompletedEvent, attribute eventSource shall exist at the time when the contract phase generation is executed.
    """

    # DataSendCompletedEvent method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 7.11, p.542
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__          [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getEventSourceRef [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setEventSourceRef [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # The referenced VariableAccess raises this DataSendCompletedEvent when the explicit write access was successful or an error occurred.
        self.eventSourceRef: Optional[RefType] = None

    def getEventSourceRef(self) -> Optional[RefType]:
        """
        The referenced VariableAccess raises this DataSendCompletedEvent when the explicit write access was successful or an error occurred.
        """
        return self.eventSourceRef

    def setEventSourceRef(self, value: Optional[RefType]) -> DataSendCompletedEvent:
        """
        The referenced VariableAccess raises this DataSendCompletedEvent when the explicit write access was successful or an error occurred.
        A None value is a no-op and does not overwrite an existing eventSourceRef.
        """
        if value is not None:
            self.eventSourceRef = value
        return self


class DataWriteCompletedEvent(RTEEvent):
    """
    This event is raised when an implicit write access was successful or an error occurred.

    [constr_1942] Existence of attribute DataWriteCompletedEvent.eventSource: For each DataWriteCompletedEvent, attribute eventSource shall exist at the time when the contract phase generation is executed.
    """

    # DataWriteCompletedEvent method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 7.12, p.542
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__          [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getEventSourceRef [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setEventSourceRef [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # The referenced VariableAccess raises this DataWriteCompletedEvent when the implicit write access was successful or an error occurred.
        self.eventSourceRef: Optional[RefType] = None

    def getEventSourceRef(self) -> Optional[RefType]:
        """The referenced VariableAccess raises this DataWriteCompletedEvent when the implicit write access was successful or an error occurred."""
        return self.eventSourceRef

    def setEventSourceRef(self, value: Optional[RefType]) -> DataWriteCompletedEvent:
        """
        The referenced VariableAccess raises this DataWriteCompletedEvent when the implicit write access was successful or an error occurred.
        A None value is a no-op and does not overwrite an existing eventSourceRef.
        """
        if value is not None:
            self.eventSourceRef = value
        return self


class DataReceivedEvent(RTEEvent):
    """
    This event is raised when the referenced data element is received.

    [constr_1943] Existence of attribute DataReceivedEvent.data: For each DataReceivedEvent, attribute data shall exist at the time when the contract phase generation is executed.
    """

    # DataReceivedEvent method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 7.13, p.542
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getDataIRef  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDataIRef  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # The referenced VariableDataPrototype raises this DataReceivedEvent when the data has been received. InstanceRef implemented by: RVariableInAtomicSwcInstanceRef
        self.dataIRef: Optional[RVariableInAtomicSwcInstanceRef] = None

    def getDataIRef(self) -> Optional[RVariableInAtomicSwcInstanceRef]:
        """
        The referenced VariableDataPrototype raises this DataReceivedEvent when the data has been received. InstanceRef implemented by: RVariableInAtomicSwcInstanceRef
        """
        return self.dataIRef

    def setDataIRef(self, value: Optional[RVariableInAtomicSwcInstanceRef]) -> DataReceivedEvent:
        """
        The referenced VariableDataPrototype raises this DataReceivedEvent when the data has been received. InstanceRef implemented by: RVariableInAtomicSwcInstanceRef
        A None value is a no-op and does not overwrite an existing dataIRef.
        """
        if value is not None:
            self.dataIRef = value
        return self


class SwcModeSwitchEvent(RTEEvent):
    """
    This event is raised when the specified mode change occurs.

    [constr_1946] Existence of attribute SwcModeSwitchEvent.activation: For each SwcModeSwitchEvent, attribute activation shall exist at the time when the RTE is generated.
    [constr_1947] Existence of reference SwcModeSwitchEvent.mode: For each SwcModeSwitchEvent, the reference to ModeDeclaration in the role mode shall exist at the time when the RTE is generated.
    """

    # SwcModeSwitchEvent method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 7.17, p.544
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__      [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getActivation [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setActivation [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] addModeIRef   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getModeIRefs  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Specifies if the event is raised on entering or exiting a specific mode or is raised on the transition between two modes.
        self.activation: Optional[ModeActivationKind] = None

        # The referenced mode or the transition between two modes raises this SwcModeSwitchEvent. InstanceRef implemented by: RModeInAtomicSwcInstanceRef
        self.modeIRefs: List[RModeInAtomicSwcInstanceRef] = []

    def getActivation(self) -> Optional[ModeActivationKind]:
        """
        Specifies if the event is raised on entering or exiting a specific mode or is raised on the transition between two modes.
        """
        return self.activation

    def setActivation(self, value: Optional[ModeActivationKind]) -> SwcModeSwitchEvent:
        """
        Specifies if the event is raised on entering or exiting a specific mode or is raised on the transition between two modes.

        A None value is a no-op and does not overwrite an existing activation.
        """
        if value is not None:
            self.activation = value
        return self

    def addModeIRef(self, value: Optional[RModeInAtomicSwcInstanceRef]) -> SwcModeSwitchEvent:
        """
        The referenced mode or the transition between two modes raises this SwcModeSwitchEvent. InstanceRef implemented by: RModeInAtomicSwcInstanceRef

        A None value is a no-op and does not append anything.
        """
        if value is not None:
            self.modeIRefs.append(value)
        return self

    def getModeIRefs(self) -> List[RModeInAtomicSwcInstanceRef]:
        """
        The referenced mode or the transition between two modes raises this SwcModeSwitchEvent. InstanceRef implemented by: RModeInAtomicSwcInstanceRef
        """
        return self.modeIRefs


class DataReceiveErrorEvent(RTEEvent):
    """
    This event is raised when the Com layer detects and notifies an error concerning the reception of the referenced VariableDataPrototype.

    [constr_1944] Existence of attribute DataReceiveErrorEvent.data: For each DataReceiveErrorEvent, attribute data shall exist at the time when the contract phase generation is executed.
    """

    # DataReceiveErrorEvent method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 7.14, p.543
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getDataIRef  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDataIRef  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # The referenced VariableDataPrototype raises this DataReceiveErrorEvent when there was an error during the reception. InstanceRef implemented by: RVariableInAtomicSwcInstanceRef
        self.dataIRef: Optional[RVariableInAtomicSwcInstanceRef] = None

    def getDataIRef(self) -> Optional[RVariableInAtomicSwcInstanceRef]:
        """
        The referenced VariableDataPrototype raises this DataReceiveErrorEvent when there was an error during the reception. InstanceRef implemented by: RVariableInAtomicSwcInstanceRef
        """
        return self.dataIRef

    def setDataIRef(self, value: Optional[RVariableInAtomicSwcInstanceRef]) -> DataReceiveErrorEvent:
        """
        The referenced VariableDataPrototype raises this DataReceiveErrorEvent when there was an error during the reception. InstanceRef implemented by: RVariableInAtomicSwcInstanceRef
        A None value is a no-op and does not overwrite an existing dataIRef.
        """
        if value is not None:
            self.dataIRef = value
        return self


class OperationInvokedEvent(RTEEvent):
    """
    This event is raised when the ClientServerOperation referenced in OperationInvokedEvent.operation shall be invoked.

    [constr_1945] Existence of attribute OperationInvokedEvent.operation: For each OperationInvokedEvent, attribute operation shall exist at the time when the contract phase generation is executed.
    """

    # OperationInvokedEvent method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 7.15, p.543
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__          [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getOperationIRef  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setOperationIRef  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This represents the ClientServerOperation which shall be invoked.
        self.operationIRef: Optional[POperationInAtomicSwcInstanceRef] = None

    def getOperationIRef(self) -> Optional[POperationInAtomicSwcInstanceRef]:
        """This represents the ClientServerOperation which shall be invoked."""
        return self.operationIRef

    def setOperationIRef(self, value: Optional[POperationInAtomicSwcInstanceRef]) -> OperationInvokedEvent:
        """
        This represents the ClientServerOperation which shall be invoked.
        A None value is a no-op and does not overwrite an existing operationIRef.
        """
        if value is not None:
            self.operationIRef = value
        return self


class InitEvent(RTEEvent):
    """
    This RTEEvent is supposed to be used for initialization purposes, i.e. for starting and restarting a partition. It is not guaranteed that all RunnableEntities referenced by this InitEvent are executed before the 'regular' RunnableEntities are executed for the first time. The execution order depends on the task mapping.
    """

    # InitEvent method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 7.22, p.546 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class TimingEvent(RTEEvent):
    """
    This event is used to start RunnableEntities that shall be executed periodically.

    [constr_1622] Value of TimingEvent.offset vs. TimingEvent.period: If a value is defined for attribute TimingEvent.offset then this value shall be greater than 0 and less or equal than the value of attribute TimingEvent.period of the respective TimingEvent at the time when the RTE is generated.
    """

    # TimingEvent method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 7.4, p.532
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__   [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] periodMs   [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getOffset  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setOffset  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getPeriod  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setPeriod  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # The value makes an assumption about the time offset of the first activation of the RunnableEntity triggered by the mapped TimingEvent relative to the periodic activation of the time base of this TimingEvent. Unit: second.
        self.offset: Optional[TimeValue] = None

        # Period of timing event in seconds. The value of this attribute shall be greater than zero.
        self.period: Optional[TimeValue] = None

    @property
    def periodMs(self):
        """
        The period of the event in milliseconds (read-only convenience property derived from period; no spec row — added convenience property).
        """
        if self.period is None:
            return None
        else:
            period_value = self.period.getValue() if hasattr(self.period, "getValue") else self.period
            if period_value < 0.001:
                return period_value * 1000
            else:
                return (int)(period_value * 1000)

    def getOffset(self) -> Optional[TimeValue]:
        """
        The value makes an assumption about the time offset of the first activation of the RunnableEntity triggered by the mapped TimingEvent relative to the periodic activation of the time base of this TimingEvent. Unit: second.
        """

        return self.offset

    def setOffset(self, value: Optional[TimeValue]) -> TimingEvent:
        """
        The value makes an assumption about the time offset of the first activation of the RunnableEntity triggered by the mapped TimingEvent relative to the periodic activation of the time base of this TimingEvent. Unit: second.

        A None value is a no-op and does not overwrite an existing offset.
        """

        if value is not None:
            self.offset = value
        return self

    def getPeriod(self) -> Optional[TimeValue]:
        """
        Period of timing event in seconds. The value of this attribute shall be greater than zero.
        """

        return self.period

    def setPeriod(self, value: Optional[TimeValue]) -> TimingEvent:
        """
        Period of timing event in seconds. The value of this attribute shall be greater than zero.

        A None value is a no-op and does not overwrite an existing period.
        """

        if value is not None:
            self.period = value
        return self


class InternalTriggerOccurredEvent(RTEEvent):
    """
    This event is raised when the referenced InternalTriggeringPoint has occurred.

    [constr_1950] Existence of attribute InternalTriggerOccurredEvent.eventSource: For each InternalTriggerOccurredEvent, the attribute eventSource shall exist at the time when the RTE is generated.
    """

    # InternalTriggerOccurredEvent method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 7.21, p.546
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__          [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getEventSourceRef [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setEventSourceRef [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # The referenced InternalTriggeringPoint raises this InternalTriggerOccurredEvent.
        self.eventSourceRef: Optional[RefType] = None

    def getEventSourceRef(self) -> Optional[RefType]:
        """The referenced InternalTriggeringPoint raises this InternalTriggerOccurredEvent."""
        return self.eventSourceRef

    def setEventSourceRef(self, value: Optional[RefType]) -> InternalTriggerOccurredEvent:
        """
        The referenced InternalTriggeringPoint raises this InternalTriggerOccurredEvent.
        A None value is a no-op and does not overwrite an existing eventSourceRef.
        """
        if value is not None:
            self.eventSourceRef = value
        return self


class BackgroundEvent(RTEEvent):
    """
    This event is used to start RunnableEntities that are supposed to be executed in the background.
    """

    # BackgroundEvent method parity checklist:
    # Spec: R23-11/AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 7.16, p.544 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class ModeSwitchedAckEvent(RTEEvent):
    """
    This event is raised when the referenced ModeSwitchPoint has been processed or an error occurred.

    [constr_1948] Existence of attribute ModeSwitchedAckEvent.eventSource: For each ModeSwitchedAckEvent, attribute eventSource shall exist at the time when the RTE is generated.
    """

    # ModeSwitchedAckEvent method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 7.19, p.545
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__           [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getEventSourceRef  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setEventSourceRef  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # The referenced ModeSwitchPoint raises this ModeSwitchedAckEvent when the ModeSwitchPoint has been processed.
        self.eventSourceRef: Optional[RefType] = None

    def getEventSourceRef(self) -> Optional[RefType]:
        """
        The referenced ModeSwitchPoint raises this ModeSwitchedAckEvent when the ModeSwitchPoint has been processed.
        """
        return self.eventSourceRef

    def setEventSourceRef(self, value: Optional[RefType]) -> ModeSwitchedAckEvent:
        """
        The referenced ModeSwitchPoint raises this ModeSwitchedAckEvent when the ModeSwitchPoint has been processed.

        A None value is a no-op and does not overwrite an existing eventSourceRef.
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

    def setTimeout(self, value: Optional[TimeValue]) -> WaitPoint:
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

    def setTriggerRef(self, value: Optional[RefType]) -> WaitPoint:
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


class ExternalTriggerOccurredEvent(RTEEvent):
    """
    This event is raised when the referenced Trigger has occurred.

    [constr_1949] Existence of attribute ExternalTriggerOccurredEvent.trigger: For each ExternalTriggerOccurredEvent, attribute trigger shall exist at the time when the RTE is generated.
    """

    # ExternalTriggerOccurredEvent method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 7.20, p.545
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__         [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getTriggerIRef   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTriggerIRef   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # The referenced Trigger raises this ExternalTriggerOccurredEvent. InstanceRef implemented by: RTriggerInAtomicSwcInstanceRef
        self.triggerIRef: Optional[RTriggerInAtomicSwcInstanceRef] = None

    def getTriggerIRef(self) -> Optional[RTriggerInAtomicSwcInstanceRef]:
        """
        The referenced Trigger raises this ExternalTriggerOccurredEvent. InstanceRef implemented by: RTriggerInAtomicSwcInstanceRef
        """
        return self.triggerIRef

    def setTriggerIRef(self, value: Optional[RTriggerInAtomicSwcInstanceRef]) -> ExternalTriggerOccurredEvent:
        """
        The referenced Trigger raises this ExternalTriggerOccurredEvent. InstanceRef implemented by: RTriggerInAtomicSwcInstanceRef

        A None value is a no-op and does not overwrite an existing triggerIRef.
        """
        if value is not None:
            self.triggerIRef = value
        return self


class OsTaskExecutionEvent(RTEEvent):
    """
    This RTEEvent is supposed to execute RunnableEntities which have to react on the execution of specific OsTasks. Therefore, this event is unconditionally raised whenever the OsTask on which it is mapped is executed. The main use case for this event is scheduling of Runnables of Complex Drivers which have to react on task executions.

    [constr_10016] Applicability of OsTaskExecutionEvent: An OsTaskExecutionEvent is only applicable for a SwcInternalBehavior in the context of a ComplexDeviceDriverSwComponentType, EcuAbstractionSwComponentType, or ServiceSwComponentType at the time when the contract phase generation is executed.
    """

    # OsTaskExecutionEvent method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 7.24, p.547
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class TransformerHardErrorEvent(RTEEvent):
    """
    This event is raised when data are received which should trigger a Client/Server operation or an external Trigger but during transformation of the data a hard transformer error occurred.

    [constr_1397] Existence of attributes of TransformerHardErrorEvent: For any given TransformerHardErrorEvent, either the attribute TransformerHardErrorEvent.operation or TransformerHardErrorEvent.requiredTrigger shall exist at the time when the contract phase generation is executed.
    """

    # TransformerHardErrorEvent method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 7.23, p.546
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__               [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getOperationIRef       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setOperationIRef       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getRequiredTriggerIRef [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setRequiredTriggerIRef [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This represents the ClientServerOperation for which the transformer can raise this TransformerHardErrorEvent. InstanceRef implemented by: POperationInAtomicSwcInstanceRef
        self.operationIRef: Optional[POperationInAtomicSwcInstanceRef] = None

        # This represents the Trigger for which the transformer can raise this TransformerHardErrorEvent. InstanceRef implemented by: RTriggerInAtomicSwcInstanceRef
        self.requiredTriggerIRef: Optional[RTriggerInAtomicSwcInstanceRef] = None

    def getOperationIRef(self) -> Optional[POperationInAtomicSwcInstanceRef]:
        """
        This represents the ClientServerOperation for which the transformer can raise this TransformerHardErrorEvent. InstanceRef implemented by: POperationInAtomicSwcInstanceRef
        """
        return self.operationIRef

    def setOperationIRef(self, value: Optional[POperationInAtomicSwcInstanceRef]) -> TransformerHardErrorEvent:
        """
        This represents the ClientServerOperation for which the transformer can raise this TransformerHardErrorEvent. InstanceRef implemented by: POperationInAtomicSwcInstanceRef

        A None value is a no-op and does not overwrite an existing operationIRef.
        """
        if value is not None:
            self.operationIRef = value
        return self

    def getRequiredTriggerIRef(self) -> Optional[RTriggerInAtomicSwcInstanceRef]:
        """
        This represents the Trigger for which the transformer can raise this TransformerHardErrorEvent. InstanceRef implemented by: RTriggerInAtomicSwcInstanceRef
        """
        return self.requiredTriggerIRef

    def setRequiredTriggerIRef(self, value: Optional[RTriggerInAtomicSwcInstanceRef]) -> TransformerHardErrorEvent:
        """
        This represents the Trigger for which the transformer can raise this TransformerHardErrorEvent. InstanceRef implemented by: RTriggerInAtomicSwcInstanceRef

        A None value is a no-op and does not overwrite an existing requiredTriggerIRef.
        """
        if value is not None:
            self.requiredTriggerIRef = value
        return self
