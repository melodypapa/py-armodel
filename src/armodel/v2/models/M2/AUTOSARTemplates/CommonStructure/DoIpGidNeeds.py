
class DoIpGidNeeds(DoIpServiceNeeds):
    """
    The DoIpGidNeeds indicates that the software-component owning this
    ServiceNeeds is providing the GID number either after a GID Synchronisation
    or by other means like e.g. flashed EEPROM parameter. This need can be used
    independent from DoIpGidSynchronizationNeeds and is necessary if the GID can
    not be provided out of the DoIP configuration options.

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::DoIpGidNeeds

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
