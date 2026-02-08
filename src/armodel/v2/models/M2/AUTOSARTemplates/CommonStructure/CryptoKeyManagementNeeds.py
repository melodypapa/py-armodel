from armodel.v2.models.M2.AUTOSARTemplates import ServiceNeeds


class CryptoKeyManagementNeeds(ServiceNeeds):
    """
    This meta-class can be used to indicate a service use case for key
    management.

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::CryptoKeyManagementNeeds

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 745, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
