from abc import ABC

from armodel.v2.models.M2.AUTOSARTemplates import ServiceNeeds


class DoIpServiceNeeds(ServiceNeeds, ABC):
    """
    This represents an abstract base class for ServiceNeeds related to DoIP.

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::DoIpServiceNeeds

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 237, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 805, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2020, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is DoIpServiceNeeds:
            raise TypeError("DoIpServiceNeeds is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
