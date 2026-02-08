from armodel.v2.models.M2.AUTOSARTemplates import ServiceNeeds


class SyncTimeBaseMgrUserNeeds(ServiceNeeds):
    """
    Specifies the needs on the configuration of the Synchronized Time-base
    Manager for one time-base. This class currently contains no attributes. An
    instance of this class is used to find out which ports of a
    software-component belong to this time-base in order to group the request
    and response ports of the same time-base. The actual time-base value is
    stored in the PortDefinedArgumentValue of the respective port specification.

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::SyncTimeBaseMgrUserNeeds

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 236, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 818, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
