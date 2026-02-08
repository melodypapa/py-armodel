from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data import AttributeCondition

    RefType,
)


class ReferenceCondition(AttributeCondition):
    """
    The ReferenceCondition evaluates to true, if the referenced reference is
    accepted by all rules of this condition.

    Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::DataExchangePoint::Data

    Sources:
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 104, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The reference that has to be accepted by the restrictions ReferenceCondition.
        self._reference: RefType = None

    @property
    def reference(self) -> RefType:
        """Get reference (Pythonic accessor)."""
        return self._reference

    @reference.setter
    def reference(self, value: RefType) -> None:
        """
        Set reference with validation.

        Args:
            value: The reference to set

        Raises:
            TypeError: If value type is incorrect
        """
        self._reference = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getReference(self) -> RefType:
        """
        AUTOSAR-compliant getter for reference.

        Returns:
            The reference value

        Note:
            Delegates to reference property (CODING_RULE_V2_00017)
        """
        return self.reference  # Delegates to property

    def setReference(self, value: RefType) -> "ReferenceCondition":
        """
        AUTOSAR-compliant setter for reference with method chaining.

        Args:
            value: The reference to set

        Returns:
            self for method chaining

        Note:
            Delegates to reference property setter (gets validation automatically)
        """
        self.reference = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_reference(self, value: RefType) -> "ReferenceCondition":
        """
        Set reference and return self for chaining.

        Args:
            value: The reference to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_reference("value")
        """
        self.reference = value  # Use property setter (gets validation)
        return self
