from abc import ABC
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription import TimingDescriptionEvent


class TDEventSLLET(TimingDescriptionEvent, ABC):
    """
    Used to describe SL-LET (System-Level) timing events.

    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingDescription::TimingDescription::TDEventSLLET

    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 251, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is TDEventSLLET:
            raise TypeError("TDEventSLLET is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
