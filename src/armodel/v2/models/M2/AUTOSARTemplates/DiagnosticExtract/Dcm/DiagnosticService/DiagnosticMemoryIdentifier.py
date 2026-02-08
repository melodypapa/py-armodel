from typing import Optional
from armodel.v2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics import DiagnosticCommonElement


class DiagnosticMemoryIdentifier(DiagnosticCommonElement):
    """
    This meta-class represents the ability to define memory properties from the
    diagnostics point of view.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::MemoryByAddress::DiagnosticMemoryIdentifier

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 140, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents that access permission defined for the specific
        # DiagnosticMemoryIdentifier.
        self._access: Optional["DiagnosticAccess"] = None

    @property
    def access(self) -> Optional["DiagnosticAccess"]:
        """Get access (Pythonic accessor)."""
        return self._access

    @access.setter
    def access(self, value: Optional["DiagnosticAccess"]) -> None:
        """
        Set access with validation.

        Args:
            value: The access to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._access = None
            return

        if not isinstance(value, DiagnosticAccess):
            raise TypeError(
                f"access must be DiagnosticAccess or None, got {type(value).__name__}"
            )
        self._access = value
        # This represents the identification of the memory segment.
        self._id: Optional["PositiveInteger"] = None

    @property
    def id(self) -> Optional["PositiveInteger"]:
        """Get id (Pythonic accessor)."""
        return self._id

    @id.setter
    def id(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set id with validation.

        Args:
            value: The id to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._id = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"id must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._id = value
        # This represents a symbolic label for the upper bound for of the memory
        # segment.
        self._memoryHigh: Optional["String"] = None

    @property
    def memory_high(self) -> Optional["String"]:
        """Get memoryHigh (Pythonic accessor)."""
        return self._memoryHigh

    @memory_high.setter
    def memory_high(self, value: Optional["String"]) -> None:
        """
        Set memoryHigh with validation.

        Args:
            value: The memoryHigh to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._memoryHigh = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"memoryHigh must be String or None, got {type(value).__name__}"
            )
        self._memoryHigh = value
        # This represents a symbolic label for the lower bound for of the memory
        # segment.
        self._memoryLow: Optional["String"] = None

    @property
    def memory_low(self) -> Optional["String"]:
        """Get memoryLow (Pythonic accessor)."""
        return self._memoryLow

    @memory_low.setter
    def memory_low(self, value: Optional["String"]) -> None:
        """
        Set memoryLow with validation.

        Args:
            value: The memoryLow to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._memoryLow = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"memoryLow must be String or None, got {type(value).__name__}"
            )
        self._memoryLow = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAccess(self) -> "DiagnosticAccess":
        """
        AUTOSAR-compliant getter for access.

        Returns:
            The access value

        Note:
            Delegates to access property (CODING_RULE_V2_00017)
        """
        return self.access  # Delegates to property

    def setAccess(self, value: "DiagnosticAccess") -> "DiagnosticMemoryIdentifier":
        """
        AUTOSAR-compliant setter for access with method chaining.

        Args:
            value: The access to set

        Returns:
            self for method chaining

        Note:
            Delegates to access property setter (gets validation automatically)
        """
        self.access = value  # Delegates to property setter
        return self

    def getId(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for id.

        Returns:
            The id value

        Note:
            Delegates to id property (CODING_RULE_V2_00017)
        """
        return self.id  # Delegates to property

    def setId(self, value: "PositiveInteger") -> "DiagnosticMemoryIdentifier":
        """
        AUTOSAR-compliant setter for id with method chaining.

        Args:
            value: The id to set

        Returns:
            self for method chaining

        Note:
            Delegates to id property setter (gets validation automatically)
        """
        self.id = value  # Delegates to property setter
        return self

    def getMemoryHigh(self) -> "String":
        """
        AUTOSAR-compliant getter for memoryHigh.

        Returns:
            The memoryHigh value

        Note:
            Delegates to memory_high property (CODING_RULE_V2_00017)
        """
        return self.memory_high  # Delegates to property

    def setMemoryHigh(self, value: "String") -> "DiagnosticMemoryIdentifier":
        """
        AUTOSAR-compliant setter for memoryHigh with method chaining.

        Args:
            value: The memoryHigh to set

        Returns:
            self for method chaining

        Note:
            Delegates to memory_high property setter (gets validation automatically)
        """
        self.memory_high = value  # Delegates to property setter
        return self

    def getMemoryLow(self) -> "String":
        """
        AUTOSAR-compliant getter for memoryLow.

        Returns:
            The memoryLow value

        Note:
            Delegates to memory_low property (CODING_RULE_V2_00017)
        """
        return self.memory_low  # Delegates to property

    def setMemoryLow(self, value: "String") -> "DiagnosticMemoryIdentifier":
        """
        AUTOSAR-compliant setter for memoryLow with method chaining.

        Args:
            value: The memoryLow to set

        Returns:
            self for method chaining

        Note:
            Delegates to memory_low property setter (gets validation automatically)
        """
        self.memory_low = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_access(self, value: Optional["DiagnosticAccess"]) -> "DiagnosticMemoryIdentifier":
        """
        Set access and return self for chaining.

        Args:
            value: The access to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_access("value")
        """
        self.access = value  # Use property setter (gets validation)
        return self

    def with_id(self, value: Optional["PositiveInteger"]) -> "DiagnosticMemoryIdentifier":
        """
        Set id and return self for chaining.

        Args:
            value: The id to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_id("value")
        """
        self.id = value  # Use property setter (gets validation)
        return self

    def with_memory_high(self, value: Optional["String"]) -> "DiagnosticMemoryIdentifier":
        """
        Set memoryHigh and return self for chaining.

        Args:
            value: The memoryHigh to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_memory_high("value")
        """
        self.memory_high = value  # Use property setter (gets validation)
        return self

    def with_memory_low(self, value: Optional["String"]) -> "DiagnosticMemoryIdentifier":
        """
        Set memoryLow and return self for chaining.

        Args:
            value: The memoryLow to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_memory_low("value")
        """
        self.memory_low = value  # Use property setter (gets validation)
        return self
