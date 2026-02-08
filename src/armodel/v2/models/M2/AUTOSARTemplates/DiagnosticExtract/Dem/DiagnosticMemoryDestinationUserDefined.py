from typing import List, Optional


class DiagnosticMemoryDestinationUserDefined(DiagnosticMemoryDestination):
    """
    This represents a user-defined memory for a diagnostic event.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dem::DiagnosticMemoryDestination::DiagnosticMemoryDestinationUserDefined

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 184, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This reference identifies the collection of applicable.
        self._authRole: List["DiagnosticAuthRole"] = []

    @property
    def auth_role(self) -> List["DiagnosticAuthRole"]:
        """Get authRole (Pythonic accessor)."""
        return self._authRole
        # This represents the identifier of the user-defined memory.
        self._memoryId: Optional["PositiveInteger"] = None

    @property
    def memory_id(self) -> Optional["PositiveInteger"]:
        """Get memoryId (Pythonic accessor)."""
        return self._memoryId

    @memory_id.setter
    def memory_id(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set memoryId with validation.

        Args:
            value: The memoryId to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._memoryId = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"memoryId must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._memoryId = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAuthRole(self) -> List["DiagnosticAuthRole"]:
        """
        AUTOSAR-compliant getter for authRole.

        Returns:
            The authRole value

        Note:
            Delegates to auth_role property (CODING_RULE_V2_00017)
        """
        return self.auth_role  # Delegates to property

    def getMemoryId(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for memoryId.

        Returns:
            The memoryId value

        Note:
            Delegates to memory_id property (CODING_RULE_V2_00017)
        """
        return self.memory_id  # Delegates to property

    def setMemoryId(self, value: "PositiveInteger") -> "DiagnosticMemoryDestinationUserDefined":
        """
        AUTOSAR-compliant setter for memoryId with method chaining.

        Args:
            value: The memoryId to set

        Returns:
            self for method chaining

        Note:
            Delegates to memory_id property setter (gets validation automatically)
        """
        self.memory_id = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_memory_id(self, value: Optional["PositiveInteger"]) -> "DiagnosticMemoryDestinationUserDefined":
        """
        Set memoryId and return self for chaining.

        Args:
            value: The memoryId to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_memory_id("value")
        """
        self.memory_id = value  # Use property setter (gets validation)
        return self
