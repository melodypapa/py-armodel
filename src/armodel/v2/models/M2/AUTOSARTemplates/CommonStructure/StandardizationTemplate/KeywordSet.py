from typing import List

from armodel.v2.models.M2.AUTOSARTemplates import Keyword
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    ARElement,
)


class KeywordSet(ARElement):
    """
    This meta–class represents the ability to collect a set of predefined
    keywords.

    Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::Keyword::KeywordSet

    Sources:
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 194, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This is one particular keyword in the keyword set.
        self._keyword: List["Keyword"] = []

    @property
    def keyword(self) -> List["Keyword"]:
        """Get keyword (Pythonic accessor)."""
        return self._keyword

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getKeyword(self) -> List["Keyword"]:
        """
        AUTOSAR-compliant getter for keyword.

        Returns:
            The keyword value

        Note:
            Delegates to keyword property (CODING_RULE_V2_00017)
        """
        return self.keyword  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
