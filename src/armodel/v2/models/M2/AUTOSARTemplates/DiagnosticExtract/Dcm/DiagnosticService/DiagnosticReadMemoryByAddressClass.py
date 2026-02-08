from armodel.v2.models.M2.AUTOSARTemplates import DiagnosticServiceClass


class DiagnosticReadMemoryByAddressClass(DiagnosticServiceClass):
    """
    This meta-class contains attributes shared by all instances of the "Read
    Memory by Address" diagnostic service.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::MemoryByAddress::DiagnosticReadMemoryByAddressClass

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 142, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
