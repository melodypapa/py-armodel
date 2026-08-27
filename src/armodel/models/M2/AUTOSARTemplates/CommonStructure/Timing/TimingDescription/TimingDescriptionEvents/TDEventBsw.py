"""
This module contains the BSW Module level timing description event classes
(spec package CommonStructure::Timing::TimingDescription::TimingDescriptionEvents::TDEventBsw).
"""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
)


class TDEventBswModuleTypeEnum(AREnum):
    """
    This is used to describe the specific event type of a TDEventBswModule.
    """

    # TDEventBswModuleTypeEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_TimingExtensions.pdf, Table 3.45, p.76
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # (no methods) — enum value form serialized on TDEventBswModule.tdEventBswModuleType
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    # A point in time where the associated BswModuleEntry has been called. Tags: atp.EnumerationLiteralIndex=0
    BSW_M_ENTRY_CALLED = "bswMEntryCalled"

    # A point in time where the call of the associated BswModuleEntry has returned. Tags: atp.EnumerationLiteralIndex=1
    BSW_M_ENTRY_CALL_RETURNED = "bswMEntryCallReturned"

    def __init__(self):
        """
        Initializes the TDEventBswModuleTypeEnum with valid values.
        """
        super().__init__(
            (
                TDEventBswModuleTypeEnum.BSW_M_ENTRY_CALLED,
                TDEventBswModuleTypeEnum.BSW_M_ENTRY_CALL_RETURNED,
            )
        )
