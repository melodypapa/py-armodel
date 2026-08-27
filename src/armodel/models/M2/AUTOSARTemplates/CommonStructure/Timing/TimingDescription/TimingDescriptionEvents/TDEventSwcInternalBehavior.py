"""
This module contains the SW-C internal behavior timing description event classes
(spec package CommonStructure::Timing::TimingDescription::TimingDescriptionEvents::TDEventSwcInternalBehavior).
"""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
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
        """
        Initializes the TDEventSwcInternalBehaviorTypeEnum with valid values.
        """
        super().__init__(
            (
                TDEventSwcInternalBehaviorTypeEnum.RUNNABLE_ENTITY_ACTIVATED,
                TDEventSwcInternalBehaviorTypeEnum.RUNNABLE_ENTITY_STARTED,
                TDEventSwcInternalBehaviorTypeEnum.RUNNABLE_ENTITY_TERMINATED,
                TDEventSwcInternalBehaviorTypeEnum.RUNNABLE_ENTITY_VARIABLE_ACCESS,
            )
        )
