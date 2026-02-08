from typing import List

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Referrable import (
    Referrable,
)


class ExclusiveAreaNestingOrder(Referrable):
    """
    This meta-class represents the ability to define a nesting order of
    ExclusiveAreas. A nesting order (that may occur in the executable code) is
    formally defined to be able to analyze the resource locking behavior.

    Package: M2::AUTOSARTemplates::CommonStructure::InternalBehavior

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 84, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 554, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents a specific scenario of how Exclusive can be used in terms of
        # the nesting order.
        self._exclusiveArea: List["ExclusiveArea"] = []

    @property
    def exclusive_area(self) -> List["ExclusiveArea"]:
        """Get exclusiveArea (Pythonic accessor)."""
        return self._exclusiveArea

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getExclusiveArea(self) -> List["ExclusiveArea"]:
        """
        AUTOSAR-compliant getter for exclusiveArea.

        Returns:
            The exclusiveArea value

        Note:
            Delegates to exclusive_area property (CODING_RULE_V2_00017)
        """
        return self.exclusive_area  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
