from typing import (
    List,
    Optional,
)

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data import AttributeTailoring

    RefType,
)


class ReferenceTailoring(AttributeTailoring):
    """
    Tailoring of Non-Containment References.

    Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::DataExchangePoint::Data

    Sources:
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 115, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Local class tailoring for content that is referenced by this.
        self._typeTailoring: List["ClassTailoring"] = []

    @property
    def type_tailoring(self) -> List["ClassTailoring"]:
        """Get typeTailoring (Pythonic accessor)."""
        return self._typeTailoring
        # Specifies the severity of unresolved references.
        self._unresolvedRestriction: RefType = None

    @property
    def unresolved_restriction(self) -> RefType:
        """Get unresolvedRestriction (Pythonic accessor)."""
        return self._unresolvedRestriction

    @unresolved_restriction.setter
    def unresolved_restriction(self, value: RefType) -> None:
        """
        Set unresolvedRestriction with validation.

        Args:
            value: The unresolvedRestriction to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._unresolvedRestriction = None
            return

        self._unresolvedRestriction = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTypeTailoring(self) -> List["ClassTailoring"]:
        """
        AUTOSAR-compliant getter for typeTailoring.

        Returns:
            The typeTailoring value

        Note:
            Delegates to type_tailoring property (CODING_RULE_V2_00017)
        """
        return self.type_tailoring  # Delegates to property

    def getUnresolvedRestriction(self) -> RefType:
        """
        AUTOSAR-compliant getter for unresolvedRestriction.

        Returns:
            The unresolvedRestriction value

        Note:
            Delegates to unresolved_restriction property (CODING_RULE_V2_00017)
        """
        return self.unresolved_restriction  # Delegates to property

    def setUnresolvedRestriction(self, value: RefType) -> "ReferenceTailoring":
        """
        AUTOSAR-compliant setter for unresolvedRestriction with method chaining.

        Args:
            value: The unresolvedRestriction to set

        Returns:
            self for method chaining

        Note:
            Delegates to unresolved_restriction property setter (gets validation automatically)
        """
        self.unresolved_restriction = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_unresolved_restriction(self, value: Optional[RefType]) -> "ReferenceTailoring":
        """
        Set unresolvedRestriction and return self for chaining.

        Args:
            value: The unresolvedRestriction to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_unresolved_restriction("value")
        """
        self.unresolved_restriction = value  # Use property setter (gets validation)
        return self
