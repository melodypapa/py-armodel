from typing import Optional
from armodel.v2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.MemoryByAddress import DiagnosticMemoryAddressableRangeAccess


class DiagnosticReadMemoryByAddress(DiagnosticMemoryAddressableRangeAccess):
    """
    This represents an instance of the "Read Memory by Address" diagnostic
    service.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::MemoryByAddress::DiagnosticReadMemoryByAddress

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 141, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This reference substantiates that abstract reference in the serviceClass for
                # this specific concrete class.
        # reference represents the ability to access among all DiagnosticReadMemoryBy
                # the given context.
        self._readClass: Optional["DiagnosticReadMemory"] = None

    @property
    def read_class(self) -> Optional["DiagnosticReadMemory"]:
        """Get readClass (Pythonic accessor)."""
        return self._readClass

    @read_class.setter
    def read_class(self, value: Optional["DiagnosticReadMemory"]) -> None:
        """
        Set readClass with validation.

        Args:
            value: The readClass to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._readClass = None
            return

        if not isinstance(value, DiagnosticReadMemory):
            raise TypeError(
                f"readClass must be DiagnosticReadMemory or None, got {type(value).__name__}"
            )
        self._readClass = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getReadClass(self) -> "DiagnosticReadMemory":
        """
        AUTOSAR-compliant getter for readClass.

        Returns:
            The readClass value

        Note:
            Delegates to read_class property (CODING_RULE_V2_00017)
        """
        return self.read_class  # Delegates to property

    def setReadClass(self, value: "DiagnosticReadMemory") -> "DiagnosticReadMemoryByAddress":
        """
        AUTOSAR-compliant setter for readClass with method chaining.

        Args:
            value: The readClass to set

        Returns:
            self for method chaining

        Note:
            Delegates to read_class property setter (gets validation automatically)
        """
        self.read_class = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_read_class(self, value: Optional["DiagnosticReadMemory"]) -> "DiagnosticReadMemoryByAddress":
        """
        Set readClass and return self for chaining.

        Args:
            value: The readClass to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_read_class("value")
        """
        self.read_class = value  # Use property setter (gets validation)
        return self
