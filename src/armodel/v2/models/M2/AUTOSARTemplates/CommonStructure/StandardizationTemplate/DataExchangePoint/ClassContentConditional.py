from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    AbstractCondition,
    AttributeTailoring,
    ConstraintTailoring,
    SdgTailoring,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class ClassContentConditional(Identifiable):
    """
    Specifies the valid content of the class. The content can optionally depend
    on a condition. (E.g. value of attribute ’category’)

    Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::DataExchangePoint::Data::ClassContentConditional

    Sources:
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 103, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Tailorings of the owned and inherited attributes of this Classes.
        self._attribute: List["AttributeTailoring"] = []

    @property
    def attribute(self) -> List["AttributeTailoring"]:
        """Get attribute (Pythonic accessor)."""
        return self._attribute
        # The rules on the content of this class are enabled if the to true.
        self._condition: Optional["AbstractCondition"] = None

    @property
    def condition(self) -> Optional["AbstractCondition"]:
        """Get condition (Pythonic accessor)."""
        return self._condition

    @condition.setter
    def condition(self, value: Optional["AbstractCondition"]) -> None:
        """
        Set condition with validation.

        Args:
            value: The condition to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._condition = None
            return

        if not isinstance(value, AbstractCondition):
            raise TypeError(
                f"condition must be AbstractCondition or None, got {type(value).__name__}"
            )
        self._condition = value
        # Specification of tailorings of Constraints of that are owned this Meta
        # Classes.
        self._constraint: List["ConstraintTailoring"] = []

    @property
    def constraint(self) -> List["ConstraintTailoring"]:
        """Get constraint (Pythonic accessor)."""
        return self._constraint
        # Specification of the applicable Special Data Group.
        self._sdgTailoring: List["SdgTailoring"] = []

    @property
    def sdg_tailoring(self) -> List["SdgTailoring"]:
        """Get sdgTailoring (Pythonic accessor)."""
        return self._sdgTailoring

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAttribute(self) -> List["AttributeTailoring"]:
        """
        AUTOSAR-compliant getter for attribute.

        Returns:
            The attribute value

        Note:
            Delegates to attribute property (CODING_RULE_V2_00017)
        """
        return self.attribute  # Delegates to property

    def getCondition(self) -> "AbstractCondition":
        """
        AUTOSAR-compliant getter for condition.

        Returns:
            The condition value

        Note:
            Delegates to condition property (CODING_RULE_V2_00017)
        """
        return self.condition  # Delegates to property

    def setCondition(self, value: "AbstractCondition") -> "ClassContentConditional":
        """
        AUTOSAR-compliant setter for condition with method chaining.

        Args:
            value: The condition to set

        Returns:
            self for method chaining

        Note:
            Delegates to condition property setter (gets validation automatically)
        """
        self.condition = value  # Delegates to property setter
        return self

    def getConstraint(self) -> List["ConstraintTailoring"]:
        """
        AUTOSAR-compliant getter for constraint.

        Returns:
            The constraint value

        Note:
            Delegates to constraint property (CODING_RULE_V2_00017)
        """
        return self.constraint  # Delegates to property

    def getSdgTailoring(self) -> List["SdgTailoring"]:
        """
        AUTOSAR-compliant getter for sdgTailoring.

        Returns:
            The sdgTailoring value

        Note:
            Delegates to sdg_tailoring property (CODING_RULE_V2_00017)
        """
        return self.sdg_tailoring  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_condition(self, value: Optional["AbstractCondition"]) -> "ClassContentConditional":
        """
        Set condition and return self for chaining.

        Args:
            value: The condition to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_condition("value")
        """
        self.condition = value  # Use property setter (gets validation)
        return self
