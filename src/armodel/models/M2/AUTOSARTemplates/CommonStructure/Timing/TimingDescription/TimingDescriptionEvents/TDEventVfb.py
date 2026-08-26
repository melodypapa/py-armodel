"""
This module contains VFB-level timing description event classes (spec package
CommonStructure::Timing::TimingDescription::TimingDescriptionEvents::TDEventVfb).
"""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
)


class TDEventVariableDataPrototypeTypeEnum(AREnum):
    """
    This is used to describe the specific event type of a TDEventVariableDataPrototype
    """

    # TDEventVariableDataPrototypeTypeEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_TimingExtensions.pdf, Table 3.18, p.54
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
]
