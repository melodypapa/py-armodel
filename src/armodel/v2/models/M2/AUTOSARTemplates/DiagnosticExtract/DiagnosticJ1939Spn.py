from typing import Optional
from armodel.v2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics import DiagnosticCommonElement


class DiagnosticJ1939Spn(DiagnosticCommonElement):
    """
    This meta-class represents the ability to model a J1939 Suspect Parameter
    Number (SPN).

    Package: M2::AUTOSARTemplates::DiagnosticExtract::J1939::DiagnosticJ1939Spn

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 219, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute represents the concrete numerical the enclosing SPN.
        self._spn: Optional["PositiveInteger"] = None

    @property
    def spn(self) -> Optional["PositiveInteger"]:
        """Get spn (Pythonic accessor)."""
        return self._spn

    @spn.setter
    def spn(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set spn with validation.

        Args:
            value: The spn to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._spn = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"spn must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._spn = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getSpn(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for spn.

        Returns:
            The spn value

        Note:
            Delegates to spn property (CODING_RULE_V2_00017)
        """
        return self.spn  # Delegates to property

    def setSpn(self, value: "PositiveInteger") -> "DiagnosticJ1939Spn":
        """
        AUTOSAR-compliant setter for spn with method chaining.

        Args:
            value: The spn to set

        Returns:
            self for method chaining

        Note:
            Delegates to spn property setter (gets validation automatically)
        """
        self.spn = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_spn(self, value: Optional["PositiveInteger"]) -> "DiagnosticJ1939Spn":
        """
        Set spn and return self for chaining.

        Args:
            value: The spn to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_spn("value")
        """
        self.spn = value  # Use property setter (gets validation)
        return self
