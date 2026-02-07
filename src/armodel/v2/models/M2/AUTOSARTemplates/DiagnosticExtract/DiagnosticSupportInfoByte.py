from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class DiagnosticSupportInfoByte(ARObject):
    """
    This meta-class defines the support information (typically byte A) to
    declare the usability of the Data Elements within the so-called packeted
    PIDs (e.g. PID$68).

    Package: M2::AUTOSARTemplates::DiagnosticExtract::CommonDiagnostics::DiagnosticSupportInfoByte

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 150, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the position of the supportInfo in the PID.
        self._position: Optional["PositiveInteger"] = None

    @property
    def position(self) -> Optional["PositiveInteger"]:
        """Get position (Pythonic accessor)."""
        return self._position

    @position.setter
    def position(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set position with validation.

        Args:
            value: The position to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._position = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"position must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._position = value
        # This represents the size of the supportInfo within the PID.
        self._size: Optional["PositiveInteger"] = None

    @property
    def size(self) -> Optional["PositiveInteger"]:
        """Get size (Pythonic accessor)."""
        return self._size

    @size.setter
    def size(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set size with validation.

        Args:
            value: The size to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._size = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"size must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._size = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getPosition(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for position.

        Returns:
            The position value

        Note:
            Delegates to position property (CODING_RULE_V2_00017)
        """
        return self.position  # Delegates to property

    def setPosition(self, value: "PositiveInteger") -> "DiagnosticSupportInfoByte":
        """
        AUTOSAR-compliant setter for position with method chaining.

        Args:
            value: The position to set

        Returns:
            self for method chaining

        Note:
            Delegates to position property setter (gets validation automatically)
        """
        self.position = value  # Delegates to property setter
        return self

    def getSize(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for size.

        Returns:
            The size value

        Note:
            Delegates to size property (CODING_RULE_V2_00017)
        """
        return self.size  # Delegates to property

    def setSize(self, value: "PositiveInteger") -> "DiagnosticSupportInfoByte":
        """
        AUTOSAR-compliant setter for size with method chaining.

        Args:
            value: The size to set

        Returns:
            self for method chaining

        Note:
            Delegates to size property setter (gets validation automatically)
        """
        self.size = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_position(self, value: Optional["PositiveInteger"]) -> "DiagnosticSupportInfoByte":
        """
        Set position and return self for chaining.

        Args:
            value: The position to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_position("value")
        """
        self.position = value  # Use property setter (gets validation)
        return self

    def with_size(self, value: Optional["PositiveInteger"]) -> "DiagnosticSupportInfoByte":
        """
        Set size and return self for chaining.

        Args:
            value: The size to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_size("value")
        """
        self.size = value  # Use property setter (gets validation)
        return self
