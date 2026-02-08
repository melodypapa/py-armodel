from abc import ABC

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class AbstractSecurityEventFilter(Identifiable, ABC):
    """
    This meta-class acts as a base class for security event filters.

    Package: M2::AUTOSARTemplates::SecurityExtractTemplate

    Sources:
      - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (Page 21, Foundation R23-11)
    """
    def __init__(self):
        if type(self) is AbstractSecurityEventFilter:
            raise TypeError("AbstractSecurityEventFilter is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
