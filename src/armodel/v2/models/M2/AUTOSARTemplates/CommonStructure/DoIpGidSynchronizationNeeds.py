from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import (
    DoIpServiceNeeds,
)


class DoIpGidSynchronizationNeeds(DoIpServiceNeeds):
    """
    The DoIpGidSynchronizationNeeds indicates that the software-component owning
    this ServiceNeeds is triggered by the DoIP entity to start a synchronization
    of the GID (Group Identification) on the DoIP service 0x0001, 0x0002, 0x0003
    or before announcement via service 0x0004 according to ISO 13400-2:2012 if
    necessary. Note that this need is only relevant for DoIP synchronization
    masters.

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 805, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2019, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
