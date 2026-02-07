from typing import Optional


class IndicatorStatusNeeds(ServiceNeeds):
    """
    This meta-class shall be taken to signal a service use case that affects the
    indicator status.

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::IndicatorStatusNeeds

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 766, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Defines the type of the indicator.
        self._typeEnum: Optional["DiagnosticIndicatorType"] = None

    @property
    def type_enum(self) -> Optional["DiagnosticIndicatorType"]:
        """Get typeEnum (Pythonic accessor)."""
        return self._typeEnum

    @type_enum.setter
    def type_enum(self, value: Optional["DiagnosticIndicatorType"]) -> None:
        """
        Set typeEnum with validation.

        Args:
            value: The typeEnum to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._typeEnum = None
            return

        if not isinstance(value, DiagnosticIndicatorType):
            raise TypeError(
                f"typeEnum must be DiagnosticIndicatorType or None, got {type(value).__name__}"
            )
        self._typeEnum = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTypeEnum(self) -> "DiagnosticIndicatorType":
        """
        AUTOSAR-compliant getter for typeEnum.

        Returns:
            The typeEnum value

        Note:
            Delegates to type_enum property (CODING_RULE_V2_00017)
        """
        return self.type_enum  # Delegates to property

    def setTypeEnum(self, value: "DiagnosticIndicatorType") -> "IndicatorStatusNeeds":
        """
        AUTOSAR-compliant setter for typeEnum with method chaining.

        Args:
            value: The typeEnum to set

        Returns:
            self for method chaining

        Note:
            Delegates to type_enum property setter (gets validation automatically)
        """
        self.type_enum = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_type_enum(self, value: Optional["DiagnosticIndicatorType"]) -> "IndicatorStatusNeeds":
        """
        Set typeEnum and return self for chaining.

        Args:
            value: The typeEnum to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_type_enum("value")
        """
        self.type_enum = value  # Use property setter (gets validation)
        return self
