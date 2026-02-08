from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class EcucLinkerSymbolDef(ARObject):
    """
    Configuration parameter type for Linker Symbol Names like those used to
    specify memory locations of variables and constants.

    Package: M2::AUTOSARTemplates::ECUCParameterDefTemplate::EcucLinkerSymbolDef

    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 65, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
