from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import ValueSpecification
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class ReferenceValueSpecification(ValueSpecification):
    """
    Specifies a reference to a data prototype to be used as an initial value for
    a pointer in the software.

    Package: M2::AUTOSARTemplates::CommonStructure::Constants::ReferenceValueSpecification

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 436, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The referenced data prototype.
        self._referenceValue: RefType = None

    @property
    def reference_value(self) -> RefType:
        """Get referenceValue (Pythonic accessor)."""
        return self._referenceValue

    @reference_value.setter
    def reference_value(self, value: RefType) -> None:
        """
        Set referenceValue with validation.

        Args:
            value: The referenceValue to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._referenceValue = None
            return

        self._referenceValue = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getReferenceValue(self) -> RefType:
        """
        AUTOSAR-compliant getter for referenceValue.

        Returns:
            The referenceValue value

        Note:
            Delegates to reference_value property (CODING_RULE_V2_00017)
        """
        return self.reference_value  # Delegates to property

    def setReferenceValue(self, value: RefType) -> "ReferenceValueSpecification":
        """
        AUTOSAR-compliant setter for referenceValue with method chaining.

        Args:
            value: The referenceValue to set

        Returns:
            self for method chaining

        Note:
            Delegates to reference_value property setter (gets validation automatically)
        """
        self.reference_value = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_reference_value(self, value: Optional[RefType]) -> "ReferenceValueSpecification":
        """
        Set referenceValue and return self for chaining.

        Args:
            value: The referenceValue to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_reference_value("value")
        """
        self.reference_value = value  # Use property setter (gets validation)
        return self
