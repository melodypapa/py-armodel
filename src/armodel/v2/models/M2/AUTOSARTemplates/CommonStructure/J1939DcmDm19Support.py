from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import ServiceNeeds

class J1939DcmDm19Support(ServiceNeeds):
    """
    The software-component provides information about calibration verification
    numbers for inclusion in DM19

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::J1939DcmDm19Support

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 831, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
