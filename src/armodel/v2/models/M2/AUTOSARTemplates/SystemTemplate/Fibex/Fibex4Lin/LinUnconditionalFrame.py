from armodel.v2.models.M2.AUTOSARTemplates import LinFrame


class LinUnconditionalFrame(LinFrame):
    """
    Unconditional frames carry signals. The master sends a frame header in a
    scheduled frame slot and the designated slave node fills the frame with
    data.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Lin::LinCommunication::LinUnconditionalFrame

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 429, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
