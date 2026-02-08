from armodel.v2.models.M2.AUTOSARTemplates import ServiceNeeds


class IdsMgrCustomTimestampNeeds(ServiceNeeds):
    """
    This meta-class is used to indicate that the enclosing SwcServiceDependency
    represents a service use case for the retrieval of a custom timestamp by the
    Intrusion Detection System Manager.

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::IdsMgrCustomTimestampNeeds

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 842, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
