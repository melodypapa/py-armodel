from abc import ABC

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    ARElement,
)


class IdsCommonElement(ARElement, ABC):
    """
    This meta-class represents a common base class for IDS related elements of
    the Security Extract. It does not contribute any specific functionality
    other than the ability to become the target of a reference.

    Package: M2::AUTOSARTemplates::SecurityExtractTemplate

    Sources:
      - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (Page 62, Foundation R23-11)
    """
    def __init__(self):
        if type(self) is IdsCommonElement:
            raise TypeError("IdsCommonElement is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
