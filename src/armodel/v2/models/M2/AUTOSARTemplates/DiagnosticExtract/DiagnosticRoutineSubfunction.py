from abc import ABC
from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class DiagnosticRoutineSubfunction(Identifiable, ABC):
    """
    This meta-class acts as an abstract base class to routine subfunctions.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::CommonDiagnostics::DiagnosticRoutineSubfunction

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 121, Classic Platform
      R23-11)
    """
    def __init__(self):
        if type(self) is DiagnosticRoutineSubfunction:
            raise TypeError("DiagnosticRoutineSubfunction is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This reference represents the access permission of the owning routine
        # subfunction.
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

    def setAccess(self, value: "DiagnosticAccess") -> "DiagnosticRoutineSubfunction":
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

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_access(self, value: Optional["DiagnosticAccess"]) -> "DiagnosticRoutineSubfunction":
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
