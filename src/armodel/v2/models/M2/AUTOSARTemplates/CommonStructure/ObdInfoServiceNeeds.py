from armodel.v2.models.M2.AUTOSARTemplates import DiagnosticCapabilityElement


class ObdInfoServiceNeeds(DiagnosticCapabilityElement):
    """
    Specifies the abstract needs of a component or module on the configuration
    of OBD Services in relation to a given InfoType (OBD Service 09) which is
    supported by this component or module.

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::ObdInfoServiceNeeds

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 324, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 233, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 797, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
