from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import ServiceNeeds

class V2xMUserNeeds(ServiceNeeds):
    """
    This meta-class represents the ability to express service needs for the V2x
    management.

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::V2xMUserNeeds

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 835, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
