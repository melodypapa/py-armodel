from typing import Optional


class IdsMgrNeeds(ServiceNeeds):
    """
    This meta-class is used to indicate that the enclosing SwcServiceDependency
    represents a service use case for the Intrusion Detection System Manager.

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::IdsMgrNeeds

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 842, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute controls whether the reporting of the event shall be done by
        # means of the smart.
        self._useSmart: Optional["Boolean"] = None

    @property
    def use_smart(self) -> Optional["Boolean"]:
        """Get useSmart (Pythonic accessor)."""
        return self._useSmart

    @use_smart.setter
    def use_smart(self, value: Optional["Boolean"]) -> None:
        """
        Set useSmart with validation.

        Args:
            value: The useSmart to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._useSmart = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"useSmart must be Boolean or None, got {type(value).__name__}"
            )
        self._useSmart = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getUseSmart(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for useSmart.

        Returns:
            The useSmart value

        Note:
            Delegates to use_smart property (CODING_RULE_V2_00017)
        """
        return self.use_smart  # Delegates to property

    def setUseSmart(self, value: "Boolean") -> "IdsMgrNeeds":
        """
        AUTOSAR-compliant setter for useSmart with method chaining.

        Args:
            value: The useSmart to set

        Returns:
            self for method chaining

        Note:
            Delegates to use_smart property setter (gets validation automatically)
        """
        self.use_smart = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_use_smart(self, value: Optional["Boolean"]) -> "IdsMgrNeeds":
        """
        Set useSmart and return self for chaining.

        Args:
            value: The useSmart to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_use_smart("value")
        """
        self.use_smart = value  # Use property setter (gets validation)
        return self
