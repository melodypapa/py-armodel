from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import (
    DiagnosticCapabilityElement,
)


class ObdControlServiceNeeds(DiagnosticCapabilityElement):
    """
    Specifies the abstract needs of a component or module on the configuration
    of OBD Service 08 (request control of on-board system) in relation to a
    particular test-Identifier (TID) supported by this component or module.

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 233, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 796, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
