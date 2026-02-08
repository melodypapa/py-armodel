from abc import ABC
from typing import Optional


class DiagnosticAbstractDataIdentifier(DiagnosticCommonElement, ABC):
    """
    This meta-class represents an abstract base class for the modeling of a
    diagnostic data identifier (DID).

    Package: M2::AUTOSARTemplates::DiagnosticExtract::CommonDiagnostics::DiagnosticAbstractDataIdentifier

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 34, Classic Platform
      R23-11)
    """
    def __init__(self):
        if type(self) is DiagnosticAbstractDataIdentifier:
            raise TypeError("DiagnosticAbstractDataIdentifier is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This is the numerical identifier used to identify the the scope of.
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

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getId(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for id.

        Returns:
            The id value

        Note:
            Delegates to id property (CODING_RULE_V2_00017)
        """
        return self.id  # Delegates to property

    def setId(self, value: "PositiveInteger") -> "DiagnosticAbstractDataIdentifier":
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

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_id(self, value: Optional["PositiveInteger"]) -> "DiagnosticAbstractDataIdentifier":
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
