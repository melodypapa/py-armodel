from abc import ABC

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class DiagnosticServiceMappingDiagTarget(ARObject, ABC):
    """
    This meta-class serves as a base class for diagnostics-related targets of
    subclasses of DiagnosticSw Mapping

    Package: M2::AUTOSARTemplates::DiagnosticExtract::DiagnosticMapping::ServiceMapping

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 234, Classic Platform
      R23-11)
    """
    def __init__(self):
        if type(self) is DiagnosticServiceMappingDiagTarget:
            raise TypeError("DiagnosticServiceMappingDiagTarget is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
