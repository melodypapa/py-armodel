from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    DiagnosticFunction,
    DiagnosticIumpr,
    DiagnosticMapping,
)


class DiagnosticIumprToFunctionIdentifierMapping(DiagnosticMapping):
    """
    This meta-class represents the ability to associate a
    DiagnosticFunctionIdentifier with a DiagnosticIumpr.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::DiagnosticMapping::DiagnosticIumprToFunctionIdentifierMapping

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 265, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This reference identifies the applicable Diagnostic FunctionIdentifier.
        self._function: Optional["DiagnosticFunction"] = None

    @property
    def function(self) -> Optional["DiagnosticFunction"]:
        """Get function (Pythonic accessor)."""
        return self._function

    @function.setter
    def function(self, value: Optional["DiagnosticFunction"]) -> None:
        """
        Set function with validation.

        Args:
            value: The function to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._function = None
            return

        if not isinstance(value, DiagnosticFunction):
            raise TypeError(
                f"function must be DiagnosticFunction or None, got {type(value).__name__}"
            )
        self._function = value
        # This reference identifies the applicable DiagnosticIumpr.
        self._iumpr: Optional["DiagnosticIumpr"] = None

    @property
    def iumpr(self) -> Optional["DiagnosticIumpr"]:
        """Get iumpr (Pythonic accessor)."""
        return self._iumpr

    @iumpr.setter
    def iumpr(self, value: Optional["DiagnosticIumpr"]) -> None:
        """
        Set iumpr with validation.

        Args:
            value: The iumpr to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._iumpr = None
            return

        if not isinstance(value, DiagnosticIumpr):
            raise TypeError(
                f"iumpr must be DiagnosticIumpr or None, got {type(value).__name__}"
            )
        self._iumpr = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getFunction(self) -> "DiagnosticFunction":
        """
        AUTOSAR-compliant getter for function.

        Returns:
            The function value

        Note:
            Delegates to function property (CODING_RULE_V2_00017)
        """
        return self.function  # Delegates to property

    def setFunction(self, value: "DiagnosticFunction") -> "DiagnosticIumprToFunctionIdentifierMapping":
        """
        AUTOSAR-compliant setter for function with method chaining.

        Args:
            value: The function to set

        Returns:
            self for method chaining

        Note:
            Delegates to function property setter (gets validation automatically)
        """
        self.function = value  # Delegates to property setter
        return self

    def getIumpr(self) -> "DiagnosticIumpr":
        """
        AUTOSAR-compliant getter for iumpr.

        Returns:
            The iumpr value

        Note:
            Delegates to iumpr property (CODING_RULE_V2_00017)
        """
        return self.iumpr  # Delegates to property

    def setIumpr(self, value: "DiagnosticIumpr") -> "DiagnosticIumprToFunctionIdentifierMapping":
        """
        AUTOSAR-compliant setter for iumpr with method chaining.

        Args:
            value: The iumpr to set

        Returns:
            self for method chaining

        Note:
            Delegates to iumpr property setter (gets validation automatically)
        """
        self.iumpr = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_function(self, value: Optional["DiagnosticFunction"]) -> "DiagnosticIumprToFunctionIdentifierMapping":
        """
        Set function and return self for chaining.

        Args:
            value: The function to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_function("value")
        """
        self.function = value  # Use property setter (gets validation)
        return self

    def with_iumpr(self, value: Optional["DiagnosticIumpr"]) -> "DiagnosticIumprToFunctionIdentifierMapping":
        """
        Set iumpr and return self for chaining.

        Args:
            value: The iumpr to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_iumpr("value")
        """
        self.iumpr = value  # Use property setter (gets validation)
        return self
