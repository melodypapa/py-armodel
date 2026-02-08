from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.Constants import (
    ValueSpecification,
)


class NotAvailableValueSpecification(ValueSpecification):
    """
    This meta-class provides the ability to specify a ValueSpecification to
    state that the respective element is not available. This ability is needed
    to support the existence of ApplicationRecordElements where attribute
    isOptional ist set to the value true.

    Package: M2::AUTOSARTemplates::CommonStructure::Constants

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 440, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The content of this attribute shall be used to initialize gaps memory
                # occupied by a structured data type in the an NotAvailableValueSpecification
                # is used.
        # Note pattern is only applied during initialization!.
        self._defaultPattern: Optional["PositiveInteger"] = None

    @property
    def default_pattern(self) -> Optional["PositiveInteger"]:
        """Get defaultPattern (Pythonic accessor)."""
        return self._defaultPattern

    @default_pattern.setter
    def default_pattern(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set defaultPattern with validation.

        Args:
            value: The defaultPattern to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._defaultPattern = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"defaultPattern must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._defaultPattern = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDefaultPattern(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for defaultPattern.

        Returns:
            The defaultPattern value

        Note:
            Delegates to default_pattern property (CODING_RULE_V2_00017)
        """
        return self.default_pattern  # Delegates to property

    def setDefaultPattern(self, value: "PositiveInteger") -> "NotAvailableValueSpecification":
        """
        AUTOSAR-compliant setter for defaultPattern with method chaining.

        Args:
            value: The defaultPattern to set

        Returns:
            self for method chaining

        Note:
            Delegates to default_pattern property setter (gets validation automatically)
        """
        self.default_pattern = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_default_pattern(self, value: Optional["PositiveInteger"]) -> "NotAvailableValueSpecification":
        """
        Set defaultPattern and return self for chaining.

        Args:
            value: The defaultPattern to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_default_pattern("value")
        """
        self.default_pattern = value  # Use property setter (gets validation)
        return self
