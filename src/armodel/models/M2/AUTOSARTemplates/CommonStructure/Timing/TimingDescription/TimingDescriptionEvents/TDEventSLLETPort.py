"""
This module contains the SL-LET port timing description event class
(spec package CommonStructure::Timing::TimingDescription::TimingDescriptionEvents::TDEventSLLET).
"""

from typing import Optional

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventSLLET import (
    TDEventSLLET,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class TDEventSLLETPort(TDEventSLLET):
    """
    Used to describe SL-LET timing events on the level of a SWC port. Tags: atp.Status=draft
    """

    # TDEventSLLETPort method parity checklist:
    # Spec: AUTOSAR_CP_TPS_TimingExtensions.pdf, Table 3.49, p.79
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getPortRef   [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] setPortRef   [x] impl  [x] docstring  [x] test  [x] reader  [x] writer

    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        # The originating port of the timing event
        self.portRef: Optional[RefType] = None

    def getPortRef(self) -> Optional[RefType]:
        """The originating port of the timing event"""
        return self.portRef

    def setPortRef(self, value: Optional[RefType]) -> "TDEventSLLETPort":
        """The originating port of the timing event. A None value is a no-op and does not overwrite an existing portRef."""
        if value is not None:
            self.portRef = value
        return self
