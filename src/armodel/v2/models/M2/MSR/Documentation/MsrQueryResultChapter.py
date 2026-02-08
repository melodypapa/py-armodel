from typing import List

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class MsrQueryResultChapter(ARObject):
    """
    This metaclass represents the result of an msrquery which is a set of
    chapters.

    Package: M2::MSR::Documentation::MsrQuery

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 344, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This is one particular chapter in the query result.
        self._chapter: List["Chapter"] = []

    @property
    def chapter(self) -> List["Chapter"]:
        """Get chapter (Pythonic accessor)."""
        return self._chapter

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getChapter(self) -> List["Chapter"]:
        """
        AUTOSAR-compliant getter for chapter.

        Returns:
            The chapter value

        Note:
            Delegates to chapter property (CODING_RULE_V2_00017)
        """
        return self.chapter  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
