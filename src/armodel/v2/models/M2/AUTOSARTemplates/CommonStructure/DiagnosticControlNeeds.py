from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import DiagnosticCapabilityElement

class DiagnosticControlNeeds(DiagnosticCapabilityElement):
    """
    This meta-class indicates a service use-case for reporting the controlled
    status by diagnostic services.

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::DiagnosticControlNeeds

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 812, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
