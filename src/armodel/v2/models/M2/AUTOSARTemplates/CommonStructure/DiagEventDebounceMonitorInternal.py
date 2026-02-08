from armodel.v2.models.M2.AUTOSARTemplates import DiagEventDebounceAlgorithm


class DiagEventDebounceMonitorInternal(DiagEventDebounceAlgorithm):
    """
    This meta-class represents the ability to indicate that no Dem pre-debounce
    algorithm shall be used for this diagnostic monitor. The SWC might implement
    an internal debouncing algorithm and report qualified (debounced) results to
    the Dem/DM.

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::DiagEventDebounceMonitorInternal

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 260, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 199, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 758, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
