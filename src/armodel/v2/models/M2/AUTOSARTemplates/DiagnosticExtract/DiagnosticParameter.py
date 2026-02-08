from typing import Optional
from armodel.v2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics import DiagnosticAbstractParameter


class DiagnosticParameter(DiagnosticAbstractParameter):
    """
    This meta-class represents the ability to describe information relevant for
    the execution of a specific diagnostic service, i.e. it can be taken to
    parameterize the service.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::CommonDiagnostics::DiagnosticParameter

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 36, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The aggregation in the role ident provides the ability to the
                # DiagnosticAbstractParameter identifiable.
        # semantical point of view, the AbstractDiagnostic considered a first-class
                # Identifiable and aggregation in the role ident shall always it may be
                # possible to let AbstractDiagnostic inherit from Identifiable).
        self._ident: Optional["DiagnosticParameter"] = None

    @property
    def ident(self) -> Optional["DiagnosticParameter"]:
        """Get ident (Pythonic accessor)."""
        return self._ident

    @ident.setter
    def ident(self, value: Optional["DiagnosticParameter"]) -> None:
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

        if not isinstance(value, DiagnosticParameter):
            raise TypeError(
                f"ident must be DiagnosticParameter or None, got {type(value).__name__}"
            )
        self._ident = value
        # This attribute represents the ability to define which bit of support info
        # byte is representing this part of the PID.
        self._supportInfo: Optional["DiagnosticParameter"] = None

    @property
    def support_info(self) -> Optional["DiagnosticParameter"]:
        """Get supportInfo (Pythonic accessor)."""
        return self._supportInfo

    @support_info.setter
    def support_info(self, value: Optional["DiagnosticParameter"]) -> None:
        """
        Set supportInfo with validation.

        Args:
            value: The supportInfo to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._supportInfo = None
            return

        if not isinstance(value, DiagnosticParameter):
            raise TypeError(
                f"supportInfo must be DiagnosticParameter or None, got {type(value).__name__}"
            )
        self._supportInfo = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getIdent(self) -> "DiagnosticParameter":
        """
        AUTOSAR-compliant getter for ident.

        Returns:
            The ident value

        Note:
            Delegates to ident property (CODING_RULE_V2_00017)
        """
        return self.ident  # Delegates to property

    def setIdent(self, value: "DiagnosticParameter") -> "DiagnosticParameter":
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

    def getSupportInfo(self) -> "DiagnosticParameter":
        """
        AUTOSAR-compliant getter for supportInfo.

        Returns:
            The supportInfo value

        Note:
            Delegates to support_info property (CODING_RULE_V2_00017)
        """
        return self.support_info  # Delegates to property

    def setSupportInfo(self, value: "DiagnosticParameter") -> "DiagnosticParameter":
        """
        AUTOSAR-compliant setter for supportInfo with method chaining.

        Args:
            value: The supportInfo to set

        Returns:
            self for method chaining

        Note:
            Delegates to support_info property setter (gets validation automatically)
        """
        self.support_info = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_ident(self, value: Optional["DiagnosticParameter"]) -> "DiagnosticParameter":
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

    def with_support_info(self, value: Optional["DiagnosticParameter"]) -> "DiagnosticParameter":
        """
        Set supportInfo and return self for chaining.

        Args:
            value: The supportInfo to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_support_info("value")
        """
        self.support_info = value  # Use property setter (gets validation)
        return self
