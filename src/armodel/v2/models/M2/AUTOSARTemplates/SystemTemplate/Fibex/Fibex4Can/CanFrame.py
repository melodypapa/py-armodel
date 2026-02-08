from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (
    Frame,
)


class CanFrame(Frame):
    """
    CAN specific Frame element. This element shall also be used for TTCan.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Can::CanCommunication

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 442, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
