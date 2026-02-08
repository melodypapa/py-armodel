from armodel.v2.models.M2.AUTOSARTemplates import DiagnosticCapabilityElement


class WarningIndicatorRequestedBitNeeds(DiagnosticCapabilityElement):
    """
    This meta-class represents the ability to explicitly request the existence
    of the WarningIndicator RequestedBit.

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::WarningIndicatorRequestedBitNeeds

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 811, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
