"""
This module contains the BSW Internal Behavior level timing description event classes
(spec package CommonStructure::Timing::TimingDescription::TimingDescriptionEvents::TDEventBswInternalBehavior).
"""

from typing import Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
    RefType,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription import (
    TimingDescriptionEvent,
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


class TDEventBswInternalBehavior(TimingDescriptionEvent):
    """
    This is used to describe timing events related to the BswInternalBehavior of a BSW module.
    """

    # TDEventBswInternalBehavior method parity checklist:
    # Spec: AUTOSAR_CP_TPS_TimingExtensions.pdf, Table 3.42, p.73
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                            [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getBswModuleEntityRef              [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] setBswModuleEntityRef              [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] getTdEventBswInternalBehaviorType  [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] setTdEventBswInternalBehaviorType  [x] impl  [x] docstring  [x] test  [x] reader  [x] writer

    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        # The scope of this timing event.
        self.bswModuleEntityRef: Optional[RefType] = None

        # The specific type of this timing event.
        self.tdEventBswInternalBehaviorType: Optional[TDEventBswInternalBehaviorTypeEnum] = None

    def getBswModuleEntityRef(self) -> Optional[RefType]:
        """The scope of this timing event."""
        return self.bswModuleEntityRef

    def setBswModuleEntityRef(self, value: Optional[RefType]) -> "TDEventBswInternalBehavior":
        """The scope of this timing event. A None value is a no-op and does not overwrite an existing bswModuleEntityRef."""
        if value is not None:
            self.bswModuleEntityRef = value
        return self

    def getTdEventBswInternalBehaviorType(self) -> Optional[TDEventBswInternalBehaviorTypeEnum]:
        """The specific type of this timing event."""
        return self.tdEventBswInternalBehaviorType

    def setTdEventBswInternalBehaviorType(self, value: Optional[TDEventBswInternalBehaviorTypeEnum]) -> "TDEventBswInternalBehavior":
        """The specific type of this timing event. A None value is a no-op and does not overwrite an existing tdEventBswInternalBehaviorType."""
        if value is not None:
            self.tdEventBswInternalBehaviorType = value
        return self
