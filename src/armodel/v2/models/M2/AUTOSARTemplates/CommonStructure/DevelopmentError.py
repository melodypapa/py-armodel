from armodel.v2.models.M2.AUTOSARTemplates import TracedFailure


class DevelopmentError(TracedFailure):
    """
    The reported failure is classified as development error.

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::DevelopmentError

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 263, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 832, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
