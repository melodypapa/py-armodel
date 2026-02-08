from armodel.v2.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucAbstractConfigurationClass

class EcucMultiplicityConfigurationClass(EcucAbstractConfigurationClass):
    """
    Specifies the MultiplicityConfigurationClass of a parameter/reference or a
    container for each ConfigurationVariant of the EcucModuleDef.

    Package: M2::AUTOSARTemplates::ECUCParameterDefTemplate::EcucMultiplicityConfigurationClass

    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 52, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
