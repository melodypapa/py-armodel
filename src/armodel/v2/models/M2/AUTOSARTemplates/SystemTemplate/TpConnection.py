from abc import ABC
from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import TpConnectionIdent
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class TpConnection(ARObject, ABC):
    """
    TpConnection Base Class.

    Package: M2::AUTOSARTemplates::SystemTemplate::DiagnosticConnection::TpConnection

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 633, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is TpConnection:
            raise TypeError("TpConnection is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This adds the ability to become referrable to Tp.
        self._ident: Optional["TpConnectionIdent"] = None

    @property
    def ident(self) -> Optional["TpConnectionIdent"]:
        """Get ident (Pythonic accessor)."""
        return self._ident

    @ident.setter
    def ident(self, value: Optional["TpConnectionIdent"]) -> None:
        """
        Set ident with validation.

        Args:
            value: The ident to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ident = None
            return

        if not isinstance(value, TpConnectionIdent):
            raise TypeError(
                f"ident must be TpConnectionIdent or None, got {type(value).__name__}"
            )
        self._ident = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getIdent(self) -> "TpConnectionIdent":
        """
        AUTOSAR-compliant getter for ident.

        Returns:
            The ident value

        Note:
            Delegates to ident property (CODING_RULE_V2_00017)
        """
        return self.ident  # Delegates to property

    def setIdent(self, value: "TpConnectionIdent") -> "TpConnection":
        """
        AUTOSAR-compliant setter for ident with method chaining.

        Args:
            value: The ident to set

        Returns:
            self for method chaining

        Note:
            Delegates to ident property setter (gets validation automatically)
        """
        self.ident = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_ident(self, value: Optional["TpConnectionIdent"]) -> "TpConnection":
        """
        Set ident and return self for chaining.

        Args:
            value: The ident to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ident("value")
        """
        self.ident = value  # Use property setter (gets validation)
        return self
