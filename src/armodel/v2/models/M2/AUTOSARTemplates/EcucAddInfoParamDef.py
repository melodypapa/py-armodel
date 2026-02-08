from armodel.v2.models.M2.AUTOSARTemplates import EcucParameterDef


class EcucAddInfoParamDef(EcucParameterDef):
    """
    Configuration Parameter Definition for the specification of formatted text
    in the ECU Configuration Parameter Description.

    Package: M2::AUTOSARTemplates::ECUCParameterDefTemplate::EcucAddInfoParamDef

    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 68, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
