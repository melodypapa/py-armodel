from abc import ABC

from armodel.v2.models.M2.AUTOSARTemplates import DiagnosticServiceInstance


class DiagnosticMemoryByAddress(DiagnosticServiceInstance, ABC):
    """
    This represents an abstract base class for diagnostic services that deal
    with accessing memory by address.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::MemoryByAddress::DiagnosticMemoryByAddress

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 139, Classic Platform
      R23-11)
    """
    def __init__(self):
        if type(self) is DiagnosticMemoryByAddress:
            raise TypeError("DiagnosticMemoryByAddress is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
