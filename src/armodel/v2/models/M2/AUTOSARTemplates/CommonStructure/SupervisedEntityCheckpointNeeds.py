from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import (
    ServiceNeeds,
)


class SupervisedEntityCheckpointNeeds(ServiceNeeds):
    """
    Specifies the abstract needs on the configuration of the Watchdog Manager to
    support a Checkpoint for a Supervised Entity.

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 254, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 708, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
