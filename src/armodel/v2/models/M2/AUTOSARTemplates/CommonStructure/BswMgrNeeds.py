from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import ServiceNeeds

class BswMgrNeeds(ServiceNeeds):
    """
    Specifies the abstract needs on the configuration of the Basic Software
    Manager for one "user".

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::BswMgrNeeds

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 716, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
