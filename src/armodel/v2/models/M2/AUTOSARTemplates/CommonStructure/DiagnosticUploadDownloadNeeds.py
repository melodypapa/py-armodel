from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import DiagnosticCapabilityElement

class DiagnosticUploadDownloadNeeds(DiagnosticCapabilityElement):
    """
    This meta-class represents the ability to specify needs regarding upload and
    download by means of diagnostic services.

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::DiagnosticUploadDownloadNeeds

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 252, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 816, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
