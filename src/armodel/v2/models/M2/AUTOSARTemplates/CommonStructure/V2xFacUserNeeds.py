from armodel.v2.models.M2.AUTOSARTemplates import ServiceNeeds


class V2xFacUserNeeds(ServiceNeeds):
    """
    This meta-class represents the ability to define service needs for V2x
    facilities.

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::V2xFacUserNeeds

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 834, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
