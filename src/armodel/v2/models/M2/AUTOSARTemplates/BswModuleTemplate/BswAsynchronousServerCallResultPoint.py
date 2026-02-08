from typing import Optional


class BswAsynchronousServerCallResultPoint(BswModuleCallPoint):
    """
    The callback point for an BswAsynchronousServerCallPoint i.e. the point at
    which the result can be retrieved from the BSW Scheduler.

    Package: M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior::BswAsynchronousServerCallResultPoint

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 80, Classic
      Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The call point invoking the call to which the result belongs.
        self._asynchronous: Optional["BswAsynchronous"] = None

    @property
    def asynchronous(self) -> Optional["BswAsynchronous"]:
        """Get asynchronous (Pythonic accessor)."""
        return self._asynchronous

    @asynchronous.setter
    def asynchronous(self, value: Optional["BswAsynchronous"]) -> None:
        """
        Set asynchronous with validation.

        Args:
            value: The asynchronous to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._asynchronous = None
            return

        if not isinstance(value, BswAsynchronous):
            raise TypeError(
                f"asynchronous must be BswAsynchronous or None, got {type(value).__name__}"
            )
        self._asynchronous = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAsynchronous(self) -> "BswAsynchronous":
        """
        AUTOSAR-compliant getter for asynchronous.

        Returns:
            The asynchronous value

        Note:
            Delegates to asynchronous property (CODING_RULE_V2_00017)
        """
        return self.asynchronous  # Delegates to property

    def setAsynchronous(self, value: "BswAsynchronous") -> "BswAsynchronousServerCallResultPoint":
        """
        AUTOSAR-compliant setter for asynchronous with method chaining.

        Args:
            value: The asynchronous to set

        Returns:
            self for method chaining

        Note:
            Delegates to asynchronous property setter (gets validation automatically)
        """
        self.asynchronous = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_asynchronous(self, value: Optional["BswAsynchronous"]) -> "BswAsynchronousServerCallResultPoint":
        """
        Set asynchronous and return self for chaining.

        Args:
            value: The asynchronous to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_asynchronous("value")
        """
        self.asynchronous = value  # Use property setter (gets validation)
        return self
