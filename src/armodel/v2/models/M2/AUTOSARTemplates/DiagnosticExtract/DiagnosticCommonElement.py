from abc import ABC

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    ARElement,
)


class DiagnosticCommonElement(ARElement, ABC):
    """
    This meta-class represents a common base class for all diagnostic elements.
    It does not contribute any specific functionality other than the ability to
    become the target of a reference.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::CommonDiagnostics::DiagnosticCommonElement

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 32, Classic Platform
      R23-11)
    """
    def __init__(self):
        if type(self) is DiagnosticCommonElement:
            raise TypeError("DiagnosticCommonElement is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
