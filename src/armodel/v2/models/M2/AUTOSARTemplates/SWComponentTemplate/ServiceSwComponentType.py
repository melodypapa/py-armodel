from armodel.v2.models.M2.AUTOSARTemplates import AtomicSwComponentType


class ServiceSwComponentType(AtomicSwComponentType):
    """
    ServiceSwComponentType is used for configuring services for a given ECU.
    Instances of this class are only to be created in ECU Configuration phase
    for the specific purpose of the service configuration.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Components::ServiceSwComponentType

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 336, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 306, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 659, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2056, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
