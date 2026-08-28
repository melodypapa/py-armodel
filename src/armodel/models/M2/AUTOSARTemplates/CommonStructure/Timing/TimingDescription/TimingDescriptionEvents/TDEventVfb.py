"""
This module contains VFB-level timing description event classes (spec package
CommonStructure::Timing::TimingDescription::TimingDescriptionEvents::TDEventVfb).
"""

from abc import ABC
from typing import Optional

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription import TimingDescriptionEvent
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
    Boolean,
    RefType,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.InstanceRefs import (
    ComponentInCompositionInstanceRef,
)


class TDEventVariableDataPrototypeTypeEnum(AREnum):
    """
    This is used to describe the specific event type of a TDEventVariableDataPrototype
    """

    # TDEventVariableDataPrototypeTypeEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_TimingExtensions.pdf, Table 3.18, p.54
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # (no methods) — enum value form serialized on TDEventVariableDataPrototype.tdEventVariableDataPrototypeType
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    # A point in time where the referenced variable data prototype has been successfully transmitted and is available in the related communication buffer (of the RTE) for the receiving SWC. Tags: atp.EnumerationLiteralIndex=0
    VARIABLE_DATA_PROTOTYPE_RECEIVED = "variableDataPrototypeReceived"

    # A point in time where the referenced variable data prototype has been successfully sent out by the sending SWC, so that it is available in the related communication buffer (of the RTE) for transmission. Tags: atp.EnumerationLiteralIndex=1
    VARIABLE_DATA_PROTOTYPE_SENT = "variableDataPrototypeSent"

    def __init__(self):
        """
        Initializes the TDEventVariableDataPrototypeTypeEnum with valid values.
        """
        super().__init__(
            (
                TDEventVariableDataPrototypeTypeEnum.VARIABLE_DATA_PROTOTYPE_RECEIVED,
                TDEventVariableDataPrototypeTypeEnum.VARIABLE_DATA_PROTOTYPE_SENT,
            )
        )


class TDEventOperationTypeEnum(AREnum):
    """
    This is used to describe the specific event type of a TDEventOperation.
    """

    # TDEventOperationTypeEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_TimingExtensions.pdf, Table 3.20, p.56
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # (no methods) — enum value form serialized on TDEventOperation.tdEventOperationType
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    # A point in time where the referenced operation is called by the client SWC. Tags: atp.EnumerationLiteralIndex=0
    OPERATION_CALLED = "operationCalled"

    # A point in time where the call of the referenced operation is received by the server SWC. Tags: atp.EnumerationLiteralIndex=1
    OPERATION_CALL_RECEIVED = "operationCallReceived"

    # A point in time where the client SWC has received the response of the referenced operation call. Tags: atp.EnumerationLiteralIndex=2
    OPERATION_CALL_RESPONSE_RECEIVED = "operationCallResponseReceived"

    # A point in time where the server SWC has terminated with the execution of the referenced operation, and has sent out a response. Tags: atp.EnumerationLiteralIndex=3
    OPERATION_CALL_RESPONSE_SENT = "operationCallResponseSent"

    def __init__(self):
        """
        Initializes the TDEventOperationTypeEnum with valid values.
        """
        super().__init__(
            (
                TDEventOperationTypeEnum.OPERATION_CALLED,
                TDEventOperationTypeEnum.OPERATION_CALL_RECEIVED,
                TDEventOperationTypeEnum.OPERATION_CALL_RESPONSE_RECEIVED,
                TDEventOperationTypeEnum.OPERATION_CALL_RESPONSE_SENT,
            )
        )


class TDEventModeDeclarationTypeEnum(AREnum):
    """
    This is used to describe the specific event type of a TDEventModeDeclaration
    """

    # TDEventModeDeclarationTypeEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_TimingExtensions.pdf, Table 3.22, p.57
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # (no methods) — enum value form serialized on TDEventModeDeclaration.tdEventModeDeclarationType
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    # A point in time where the switch to the associated ModeDeclarationGroupPrototype has been completed. Tags: atp.EnumerationLiteralIndex=0
    MODE_DECLARATION_SWITCH_COMPLETED = "modeDeclarationSwitchCompleted"

    # A point in time where the switch to the associated ModeDeclarationGroupPrototype has been initiated. Tags: atp.EnumerationLiteralIndex=1
    MODE_DECLARATION_SWITCH_INITIATED = "modeDeclarationSwitchInitiated"

    def __init__(self):
        """
        Initializes the TDEventModeDeclarationTypeEnum with valid values.
        """
        super().__init__(
            (
                TDEventModeDeclarationTypeEnum.MODE_DECLARATION_SWITCH_COMPLETED,
                TDEventModeDeclarationTypeEnum.MODE_DECLARATION_SWITCH_INITIATED,
            )
        )


class TDEventTriggerTypeEnum(AREnum):
    """
    This is used to describe the specific event type of a TDEventTrigger.
    """

    # TDEventTriggerTypeEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_TimingExtensions.pdf, Table 3.24, p.59
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # (no methods) — enum value form serialized on TDEventTrigger.tdEventTriggerType
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    # A point in time where the referenced trigger has been successfully released and is activating runnable entities of the receiving SW-C. Tags: atp.EnumerationLiteralIndex=0
    TRIGGER_ACTIVATED = "triggerActivated"

    # A point in time where the referenced trigger has been successfully released by the emitting SW-C. Tags: atp.EnumerationLiteralIndex=1
    TRIGGER_RELEASED = "triggerReleased"

    def __init__(self):
        """
        Initializes the TDEventTriggerTypeEnum with valid values.
        """
        super().__init__(
            (
                TDEventTriggerTypeEnum.TRIGGER_ACTIVATED,
                TDEventTriggerTypeEnum.TRIGGER_RELEASED,
            )
        )


__all__ = [
    "TDEventVariableDataPrototypeTypeEnum",
    "TDEventOperationTypeEnum",
    "TDEventModeDeclarationTypeEnum",
    "TDEventTriggerTypeEnum",
    "TDEventVfb",
    "ConcreteTDEventVfb",
    "TDEventVfbReference",
    "TDEventVfbPort",
    "TDEventVariableDataPrototype",
    "TDEventOperation",
    "TDEventModeDeclaration",
    "TDEventTrigger",
]


class TDEventVfb(TimingDescriptionEvent, ABC):
    """
    This is the abstract parent class to describe timing events at Virtual Functional Bus (VFB) level.
    """

    # TDEventVfb method parity checklist:
    # Spec: AUTOSAR_CP_TPS_TimingExtensions.pdf, Table 3.14, p.51
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__           [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getComponentIRef   [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] setComponentIRef   [x] impl  [x] docstring  [x] test  [x] reader  [x] writer

    def __init__(self, parent, short_name):
        if type(self) is TDEventVfb:
            raise TypeError("TDEventVfb is an abstract class.")

        super().__init__(parent, short_name)

        # The context for the scope of this timing event. InstanceRef implemented by: ComponentInCompositionInstanceRef
        self.componentIRef: Optional[ComponentInCompositionInstanceRef] = None

    def getComponentIRef(self) -> Optional[ComponentInCompositionInstanceRef]:
        """The context for the scope of this timing event. InstanceRef implemented by: ComponentInCompositionInstanceRef."""
        return self.componentIRef

    def setComponentIRef(self, value: Optional[ComponentInCompositionInstanceRef]) -> "TDEventVfb":
        """The context for the scope of this timing event. InstanceRef implemented by: ComponentInCompositionInstanceRef. A None value is a no-op and does not overwrite an existing componentIRef."""
        if value is not None:
            self.componentIRef = value
        return self


class TDEventVfbReference(TDEventVfb):
    """
    This is used to reference timing description events related to the Virtual Functional Bus (VFB) view which are specified in other timing views.
    """

    # TDEventVfbReference method parity checklist:
    # Spec: AUTOSAR_CP_TPS_TimingExtensions.pdf, Table 3.15, p.52
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                      [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getReferencedTDEventVfbRef    [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] setReferencedTDEventVfbRef    [x] impl  [x] docstring  [x] test  [x] reader  [x] writer

    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        # The referenced timing description event.
        self.referencedTDEventVfbRef: Optional[RefType] = None

    def getReferencedTDEventVfbRef(self) -> Optional[RefType]:
        """The referenced timing description event."""
        return self.referencedTDEventVfbRef

    def setReferencedTDEventVfbRef(self, value: Optional[RefType]) -> "TDEventVfbReference":
        """The referenced timing description event. A None value is a no-op and does not overwrite an existing referencedTDEventVfbRef."""
        if value is not None:
            self.referencedTDEventVfbRef = value
        return self


class TDEventVfbPort(TDEventVfb, ABC):
    """
    This is the abstract parent class to describe specific timing event types at Virtual Functional Bus (VFB) level.
    """

    # TDEventVfbPort method parity checklist:
    # Spec: AUTOSAR_CP_TPS_TimingExtensions.pdf, Table 3.16, p.52
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                        [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getIsExternal                   [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] setIsExternal                   [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] getPortPrototypeBlueprintRef    [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] setPortPrototypeBlueprintRef    [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] getPortRef                      [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] setPortRef                      [x] impl  [x] docstring  [x] test  [x] reader  [x] writer

    def __init__(self, parent, short_name):
        if type(self) is TDEventVfbPort:
            raise TypeError("TDEventVfbPort is an abstract class.")

        super().__init__(parent, short_name)

        # This attribute is used to refer to external events that are related to hardware I/O, like physical sensors and actuators, at Virtual Functional Bus (VFB) level.
        self.isExternal: Optional[Boolean] = None

        # port on which the TimingEvent shall apply
        self.portRef: Optional[RefType] = None

        # port on which the TimingEvent shall apply (in the context of an AUTOSAR blueprint)
        self.portPrototypeBlueprintRef: Optional[RefType] = None

    def getIsExternal(self) -> Optional[Boolean]:
        """This attribute is used to refer to external events that are related to hardware I/O, like physical sensors and actuators, at Virtual Functional Bus (VFB) level."""
        return self.isExternal

    def setIsExternal(self, value: Optional[Boolean]) -> "TDEventVfbPort":
        """This attribute is used to refer to external events that are related to hardware I/O, like physical sensors and actuators, at Virtual Functional Bus (VFB) level. A None value is a no-op and does not overwrite an existing isExternal."""
        if value is not None:
            self.isExternal = value
        return self

    def getPortPrototypeBlueprintRef(self) -> Optional[RefType]:
        """port on which the TimingEvent shall apply (in the context of an AUTOSAR blueprint)"""
        return self.portPrototypeBlueprintRef

    def setPortPrototypeBlueprintRef(self, value: Optional[RefType]) -> "TDEventVfbPort":
        """port on which the TimingEvent shall apply (in the context of an AUTOSAR blueprint). A None value is a no-op and does not overwrite an existing portPrototypeBlueprintRef."""
        if value is not None:
            self.portPrototypeBlueprintRef = value
        return self

    def getPortRef(self) -> Optional[RefType]:
        """port on which the TimingEvent shall apply"""
        return self.portRef

    def setPortRef(self, value: Optional[RefType]) -> "TDEventVfbPort":
        """port on which the TimingEvent shall apply. A None value is a no-op and does not overwrite an existing portRef."""
        if value is not None:
            self.portRef = value
        return self


class TDEventVariableDataPrototype(TDEventVfbPort):
    """
    This is used to describe timing events related to sender-receiver communication at VFB level.
    """

    # TDEventVariableDataPrototype method parity checklist:
    # Spec: AUTOSAR_CP_TPS_TimingExtensions.pdf, Table 3.17, p.54
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                            [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getDataElementRef                   [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] setDataElementRef                   [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] getTdEventVariableDataPrototypeType [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] setTdEventVariableDataPrototypeType [x] impl  [x] docstring  [x] test  [x] reader  [x] writer

    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        # The referenced VariableDataPrototype
        self.dataElementRef: Optional[RefType] = None

        # The specific type of this timing event.
        self.tdEventVariableDataPrototypeType: Optional[TDEventVariableDataPrototypeTypeEnum] = None

    def getDataElementRef(self) -> Optional[RefType]:
        """The referenced VariableDataPrototype"""
        return self.dataElementRef

    def setDataElementRef(self, value: Optional[RefType]) -> "TDEventVariableDataPrototype":
        """The referenced VariableDataPrototype. A None value is a no-op and does not overwrite an existing dataElementRef."""
        if value is not None:
            self.dataElementRef = value
        return self

    def getTdEventVariableDataPrototypeType(self) -> Optional[TDEventVariableDataPrototypeTypeEnum]:
        """The specific type of this timing event."""
        return self.tdEventVariableDataPrototypeType

    def setTdEventVariableDataPrototypeType(self, value: Optional[TDEventVariableDataPrototypeTypeEnum]) -> "TDEventVariableDataPrototype":
        """The specific type of this timing event. A None value is a no-op and does not overwrite an existing tdEventVariableDataPrototypeType."""
        if value is not None:
            self.tdEventVariableDataPrototypeType = value
        return self


class TDEventOperation(TDEventVfbPort):
    """
    This is used to describe timing events related to client-server communication at VFB level.
    """

    # TDEventOperation method parity checklist:
    # Spec: AUTOSAR_CP_TPS_TimingExtensions.pdf, Table 3.19, p.55
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getOperationRef              [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] setOperationRef              [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] getTdEventOperationType      [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] setTdEventOperationType      [x] impl  [x] docstring  [x] test  [x] reader  [x] writer

    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        # The referenced operation.
        self.operationRef: Optional[RefType] = None

        # The specific type of this timing event.
        self.tdEventOperationType: Optional[TDEventOperationTypeEnum] = None

    def getOperationRef(self) -> Optional[RefType]:
        """The referenced operation."""
        return self.operationRef

    def setOperationRef(self, value: Optional[RefType]) -> "TDEventOperation":
        """The referenced operation. A None value is a no-op and does not overwrite an existing operationRef."""
        if value is not None:
            self.operationRef = value
        return self

    def getTdEventOperationType(self) -> Optional[TDEventOperationTypeEnum]:
        """The specific type of this timing event."""
        return self.tdEventOperationType

    def setTdEventOperationType(self, value: Optional[TDEventOperationTypeEnum]) -> "TDEventOperation":
        """The specific type of this timing event. A None value is a no-op and does not overwrite an existing tdEventOperationType."""
        if value is not None:
            self.tdEventOperationType = value
        return self


class TDEventModeDeclaration(TDEventVfbPort):
    """
    This is used to describe timing events related to mode switch communication at VFB level.
    """

    # TDEventModeDeclaration method parity checklist:
    # Spec: AUTOSAR_CP_TPS_TimingExtensions.pdf, Table 3.21, p.57
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                          [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getEntryModeDeclarationRef        [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] setEntryModeDeclarationRef        [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] getExitModeDeclarationRef         [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] setExitModeDeclarationRef         [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] getModeDeclarationRef             [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] setModeDeclarationRef             [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] getTdEventModeDeclarationType     [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] setTdEventModeDeclarationType     [x] impl  [x] docstring  [x] test  [x] reader  [x] writer

    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        # Optional parameter which refines the scope of the TDEventModeDeclaration. If the parameter is set, the event occurs only if the mode declaration group prototype instance shall enter into the referenced ModeDeclaration.
        self.entryModeDeclarationRef: Optional[RefType] = None

        # Optional parameter which refines the scope of the TDEventModeDeclaration. If the parameter is set, the event occurs only if the mode declaration group prototype instance shall exit from the referenced ModeDeclaration.
        self.exitModeDeclarationRef: Optional[RefType] = None

        # The referenced mode declaration group prototype.
        self.modeDeclarationRef: Optional[RefType] = None

        # The specific type of this timing event.
        self.tdEventModeDeclarationType: Optional[TDEventModeDeclarationTypeEnum] = None

    def getEntryModeDeclarationRef(self) -> Optional[RefType]:
        """Optional parameter which refines the scope of the TDEventModeDeclaration. If the parameter is set, the event occurs only if the mode declaration group prototype instance shall enter into the referenced ModeDeclaration."""
        return self.entryModeDeclarationRef

    def setEntryModeDeclarationRef(self, value: Optional[RefType]) -> "TDEventModeDeclaration":
        """Optional parameter which refines the scope of the TDEventModeDeclaration. If the parameter is set, the event occurs only if the mode declaration group prototype instance shall enter into the referenced ModeDeclaration. A None value is a no-op and does not overwrite an existing entryModeDeclarationRef."""
        if value is not None:
            self.entryModeDeclarationRef = value
        return self

    def getExitModeDeclarationRef(self) -> Optional[RefType]:
        """Optional parameter which refines the scope of the TDEventModeDeclaration. If the parameter is set, the event occurs only if the mode declaration group prototype instance shall exit from the referenced ModeDeclaration."""
        return self.exitModeDeclarationRef

    def setExitModeDeclarationRef(self, value: Optional[RefType]) -> "TDEventModeDeclaration":
        """Optional parameter which refines the scope of the TDEventModeDeclaration. If the parameter is set, the event occurs only if the mode declaration group prototype instance shall exit from the referenced ModeDeclaration. A None value is a no-op and does not overwrite an existing exitModeDeclarationRef."""
        if value is not None:
            self.exitModeDeclarationRef = value
        return self

    def getModeDeclarationRef(self) -> Optional[RefType]:
        """The referenced mode declaration group prototype."""
        return self.modeDeclarationRef

    def setModeDeclarationRef(self, value: Optional[RefType]) -> "TDEventModeDeclaration":
        """The referenced mode declaration group prototype. A None value is a no-op and does not overwrite an existing modeDeclarationRef."""
        if value is not None:
            self.modeDeclarationRef = value
        return self

    def getTdEventModeDeclarationType(self) -> Optional[TDEventModeDeclarationTypeEnum]:
        """The specific type of this timing event."""
        return self.tdEventModeDeclarationType

    def setTdEventModeDeclarationType(self, value: Optional[TDEventModeDeclarationTypeEnum]) -> "TDEventModeDeclaration":
        """The specific type of this timing event. A None value is a no-op and does not overwrite an existing tdEventModeDeclarationType."""
        if value is not None:
            self.tdEventModeDeclarationType = value
        return self


class TDEventTrigger(TDEventVfbPort):
    """
    This is used to describe timing events related to triggers at VFB level.
    """

    # TDEventTrigger method parity checklist:
    # Spec: AUTOSAR_CP_TPS_TimingExtensions.pdf, Table 3.23, p.58
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getTdEventTriggerType     [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] setTdEventTriggerType     [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] getTriggerRef             [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] setTriggerRef             [x] impl  [x] docstring  [x] test  [x] reader  [x] writer

    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        # The trigger which is provided (released) or required (activate) in the given context.
        self.triggerRef: Optional[RefType] = None

        # The specific type of this timing event.
        self.tdEventTriggerType: Optional[TDEventTriggerTypeEnum] = None

    def getTriggerRef(self) -> Optional[RefType]:
        """The trigger which is provided (released) or required (activate) in the given context."""
        return self.triggerRef

    def setTriggerRef(self, value: Optional[RefType]) -> "TDEventTrigger":
        """The trigger which is provided (released) or required (activate) in the given context. A None value is a no-op and does not overwrite an existing triggerRef."""
        if value is not None:
            self.triggerRef = value
        return self

    def getTdEventTriggerType(self) -> Optional[TDEventTriggerTypeEnum]:
        """The specific type of this timing event."""
        return self.tdEventTriggerType

    def setTdEventTriggerType(self, value: Optional[TDEventTriggerTypeEnum]) -> "TDEventTrigger":
        """The specific type of this timing event. A None value is a no-op and does not overwrite an existing tdEventTriggerType."""
        if value is not None:
            self.tdEventTriggerType = value
        return self


class ConcreteTDEventVfb(TDEventVfb):
    """Concrete direct-use subclass of the abstract TDEventVfb."""

    pass
