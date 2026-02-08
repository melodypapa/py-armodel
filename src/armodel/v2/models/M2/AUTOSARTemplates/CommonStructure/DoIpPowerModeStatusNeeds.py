from armodel.v2.models.M2.AUTOSARTemplates import DoIpServiceNeeds


class DoIpPowerModeStatusNeeds(DoIpServiceNeeds):
    """
    The DoIpPowerModeStatusNeeds indicates that the software-component owning
    this ServiceNeeds is providing the PowerModeStatus for the DoIP service
    0x4003 according to ISO 13400-2:2012.

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::DoIpPowerModeStatusNeeds

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 806, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2019, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
