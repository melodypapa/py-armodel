"""
This module contains the BSW Internal Behavior level timing description event classes
(spec package CommonStructure::Timing::TimingDescription::TimingDescriptionEvents::TDEventBswInternalBehavior).
"""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
)


class TDEventBswInternalBehaviorTypeEnum(AREnum):
    """
    This is used to describe the specific event type of a TDEventBswInternalBehavior.
    """

    # TDEventBswInternalBehaviorTypeEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_TimingExtensions.pdf, Table 3.43, p.74
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # (no methods) — enum value form serialized on TDEventBswInternalBehavior.tdEventBswInternalBehaviorType
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    # A point in time where the associated BswModuleEntity has been activated, which means that it has entered the state "to be started". Tags: atp.EnumerationLiteralIndex=0
    BSW_MODULE_ENTITY_ACTIVATED = "bswModuleEntityActivated"

    # A point in time where the associated BswModuleEntity has entered the state "started" after its activation. Tags: atp.EnumerationLiteralIndex=1
    BSW_MODULE_ENTITY_STARTED = "bswModuleEntityStarted"

    # A point in time where the associated BswModuleEntity has terminated and entered the state "suspended" Tags: atp.EnumerationLiteralIndex=2
    BSW_MODULE_ENTITY_TERMINATED = "bswModuleEntityTerminated"

    def __init__(self):
        """
        Initializes the TDEventBswInternalBehaviorTypeEnum with valid values.
        """
        super().__init__(
            (
                TDEventBswInternalBehaviorTypeEnum.BSW_MODULE_ENTITY_ACTIVATED,
                TDEventBswInternalBehaviorTypeEnum.BSW_MODULE_ENTITY_STARTED,
                TDEventBswInternalBehaviorTypeEnum.BSW_MODULE_ENTITY_TERMINATED,
            )
        )
