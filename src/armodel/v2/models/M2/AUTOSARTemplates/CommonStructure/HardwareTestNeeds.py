from armodel.v2.models.M2.AUTOSARTemplates import ServiceNeeds


class HardwareTestNeeds(ServiceNeeds):
    """
    This meta-class represents the ability to indicate that a software-component
    is interested in the results of the hardware test and will establish a
    PortPrototype to query the hardware test manager.

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::HardwareTestNeeds

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 264, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 841, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
