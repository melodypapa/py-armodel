"""
This module contains the SW-C internal behavior timing description event classes
(spec package CommonStructure::Timing::TimingDescription::TimingDescriptionEvents::TDEventSwcInternalBehavior).
"""

from abc import ABC
from typing import Optional

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription import TimingDescriptionEvent
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
    RefType,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.InstanceRefs import (
    ComponentInCompositionInstanceRef,
)


class TDEventSwcInternalBehaviorTypeEnum(AREnum):
    """
    This is used to describe the specific event type of a TDEventSwcInternalBehavior.
    """

    # TDEventSwcInternalBehaviorTypeEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_TimingExtensions.pdf, Table 3.27, p.62
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # (no methods) — enum value form serialized on TDEventSwcInternalBehavior.tdEventSwcInternalBehaviorType
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    # A point in time where the associated RunnableEntity has been activated, which means that it has entered the state "to be started". Tags: atp.EnumerationLiteralIndex=0
    RUNNABLE_ENTITY_ACTIVATED = "runnableEntityActivated"

    # A point in time where the associated RunnableEntity has entered the state "started" after its activation. Tags: atp.EnumerationLiteralIndex=1
    RUNNABLE_ENTITY_STARTED = "runnableEntityStarted"

    # A point in time where the associated RunnableEntity has terminated and entered the state "suspended". Tags: atp.EnumerationLiteralIndex=2
    RUNNABLE_ENTITY_TERMINATED = "runnableEntityTerminated"

    # A point in time where the associated variable is accessed. Tags: atp.EnumerationLiteralIndex=3
    RUNNABLE_ENTITY_VARIABLE_ACCESS = "runnableEntityVariableAccess"

    def __init__(self):
        super().__init__(
            (
                TDEventSwcInternalBehaviorTypeEnum.RUNNABLE_ENTITY_ACTIVATED,
                TDEventSwcInternalBehaviorTypeEnum.RUNNABLE_ENTITY_STARTED,
                TDEventSwcInternalBehaviorTypeEnum.RUNNABLE_ENTITY_TERMINATED,
                TDEventSwcInternalBehaviorTypeEnum.RUNNABLE_ENTITY_VARIABLE_ACCESS,
            )
        )


__all__ = [
    "TDEventSwcInternalBehaviorTypeEnum",
    "TDEventSwc",
    "TDEventSwcInternalBehavior",
    "TDEventSwcInternalBehaviorReference",
]


class TDEventSwc(TimingDescriptionEvent, ABC):
    """
    This is the abstract parent class to describe timing events at Software Component (SW-C) level.
    """

    # TDEventSwc method parity checklist:
    # Spec: AUTOSAR_CP_TPS_TimingExtensions.pdf, Table 3.25, p.60
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__           [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getComponentIRef   [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] setComponentIRef   [x] impl  [x] docstring  [x] test  [x] reader  [x] writer

    def __init__(self, parent, short_name):
        if type(self) is TDEventSwc:
            raise TypeError("TDEventSwc is an abstract class.")

        super().__init__(parent, short_name)

        # The context for the scope of this timing event. InstanceRef implemented by: ComponentInCompositionInstanceRef
        self.componentIRef: Optional[ComponentInCompositionInstanceRef] = None

    def getComponentIRef(self) -> Optional[ComponentInCompositionInstanceRef]:
        """The context for the scope of this timing event. InstanceRef implemented by: ComponentInCompositionInstanceRef."""
        return self.componentIRef

    def setComponentIRef(self, value: Optional[ComponentInCompositionInstanceRef]) -> "TDEventSwc":
        """The context for the scope of this timing event. InstanceRef implemented by: ComponentInCompositionInstanceRef. A None value is a no-op and does not overwrite an existing componentIRef."""
        if value is not None:
            self.componentIRef = value
        return self


class TDEventSwcInternalBehavior(TDEventSwc):
    """
    This is used to describe timing events related to the SwcInternalBehavior of an AtomicSwComponentType.
    """

    # TDEventSwcInternalBehavior method parity checklist:
    # Spec: AUTOSAR_CP_TPS_TimingExtensions.pdf, Table 3.26, p.62
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                            [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getRunnableRef                      [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] setRunnableRef                      [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] getTdEventSwcInternalBehaviorType   [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] setTdEventSwcInternalBehaviorType   [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] getVariableAccessRef                [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] setVariableAccessRef                [x] impl  [x] docstring  [x] test  [x] reader  [x] writer

    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        # The scope of this timing event.
        self.runnableRef: Optional[RefType] = None

        # The specific type of this timing event.
        self.tdEventSwcInternalBehaviorType: Optional[TDEventSwcInternalBehaviorTypeEnum] = None

        # The scope of this timing event.
        self.variableAccessRef: Optional[RefType] = None

    def getRunnableRef(self) -> Optional[RefType]:
        """The scope of this timing event."""
        return self.runnableRef

    def setRunnableRef(self, value: Optional[RefType]) -> "TDEventSwcInternalBehavior":
        """The scope of this timing event. A None value is a no-op and does not overwrite an existing runnableRef."""
        if value is not None:
            self.runnableRef = value
        return self

    def getTdEventSwcInternalBehaviorType(self) -> Optional[TDEventSwcInternalBehaviorTypeEnum]:
        """The specific type of this timing event."""
        return self.tdEventSwcInternalBehaviorType

    def setTdEventSwcInternalBehaviorType(self, value: Optional[TDEventSwcInternalBehaviorTypeEnum]) -> "TDEventSwcInternalBehavior":
        """The specific type of this timing event. A None value is a no-op and does not overwrite an existing tdEventSwcInternalBehaviorType."""
        if value is not None:
            self.tdEventSwcInternalBehaviorType = value
        return self

    def getVariableAccessRef(self) -> Optional[RefType]:
        """The scope of this timing event."""
        return self.variableAccessRef

    def setVariableAccessRef(self, value: Optional[RefType]) -> "TDEventSwcInternalBehavior":
        """The scope of this timing event. A None value is a no-op and does not overwrite an existing variableAccessRef."""
        if value is not None:
            self.variableAccessRef = value
        return self


class TDEventSwcInternalBehaviorReference(TDEventSwc):
    """
    This is used to reference timing description events related to the Software Component (SW-C) view which are specified in other timing views.
    """

    # TDEventSwcInternalBehaviorReference method parity checklist:
    # Spec: AUTOSAR_CP_TPS_TimingExtensions.pdf, Table 3.28, p.63
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                       [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getReferencedTDEventSwcRef     [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] setReferencedTDEventSwcRef     [x] impl  [x] docstring  [x] test  [x] reader  [x] writer

    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        # The referenced timing description event.
        self.referencedTDEventSwcRef: Optional[RefType] = None

    def getReferencedTDEventSwcRef(self) -> Optional[RefType]:
        """The referenced timing description event."""
        return self.referencedTDEventSwcRef

    def setReferencedTDEventSwcRef(self, value: Optional[RefType]) -> "TDEventSwcInternalBehaviorReference":
        """The referenced timing description event. A None value is a no-op and does not overwrite an existing referencedTDEventSwcRef."""
        if value is not None:
            self.referencedTDEventSwcRef = value
        return self
