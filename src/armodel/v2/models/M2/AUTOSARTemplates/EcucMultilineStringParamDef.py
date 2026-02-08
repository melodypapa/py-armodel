from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class EcucMultilineStringParamDef(ARObject):
    """
    Configuration parameter type for multiline Strings (including "carriage
    return").

    Package: M2::AUTOSARTemplates::ECUCParameterDefTemplate::EcucMultilineStringParamDef

    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 64, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
