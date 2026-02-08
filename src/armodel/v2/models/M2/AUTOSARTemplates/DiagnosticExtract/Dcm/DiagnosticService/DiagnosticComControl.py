from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService import (
    DiagnosticServiceInstance,
)


class DiagnosticComControl(DiagnosticServiceInstance):
    """
    This represents an instance of the "Communication Control" diagnostic
    service.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::CommunicationControl

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 108, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This reference substantiates that abstract reference in the reference
        # represents the ability to access among all DiagnosticComControl in the.
        self._comControl: Optional["DiagnosticComControl"] = None

    @property
    def com_control(self) -> Optional["DiagnosticComControl"]:
        """Get comControl (Pythonic accessor)."""
        return self._comControl

    @com_control.setter
    def com_control(self, value: Optional["DiagnosticComControl"]) -> None:
        """
        Set comControl with validation.

        Args:
            value: The comControl to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._comControl = None
            return

        if not isinstance(value, DiagnosticComControl):
            raise TypeError(
                f"comControl must be DiagnosticComControl or None, got {type(value).__name__}"
            )
        self._comControl = value
        # This attribute shall be used to define a custom number if none of the
        # standardized values of shall be used.
        self._customSub: Optional["PositiveInteger"] = None

    @property
    def custom_sub(self) -> Optional["PositiveInteger"]:
        """Get customSub (Pythonic accessor)."""
        return self._customSub

    @custom_sub.setter
    def custom_sub(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set customSub with validation.

        Args:
            value: The customSub to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._customSub = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"customSub must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._customSub = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getComControl(self) -> "DiagnosticComControl":
        """
        AUTOSAR-compliant getter for comControl.

        Returns:
            The comControl value

        Note:
            Delegates to com_control property (CODING_RULE_V2_00017)
        """
        return self.com_control  # Delegates to property

    def setComControl(self, value: "DiagnosticComControl") -> "DiagnosticComControl":
        """
        AUTOSAR-compliant setter for comControl with method chaining.

        Args:
            value: The comControl to set

        Returns:
            self for method chaining

        Note:
            Delegates to com_control property setter (gets validation automatically)
        """
        self.com_control = value  # Delegates to property setter
        return self

    def getCustomSub(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for customSub.

        Returns:
            The customSub value

        Note:
            Delegates to custom_sub property (CODING_RULE_V2_00017)
        """
        return self.custom_sub  # Delegates to property

    def setCustomSub(self, value: "PositiveInteger") -> "DiagnosticComControl":
        """
        AUTOSAR-compliant setter for customSub with method chaining.

        Args:
            value: The customSub to set

        Returns:
            self for method chaining

        Note:
            Delegates to custom_sub property setter (gets validation automatically)
        """
        self.custom_sub = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_com_control(self, value: Optional["DiagnosticComControl"]) -> "DiagnosticComControl":
        """
        Set comControl and return self for chaining.

        Args:
            value: The comControl to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_com_control("value")
        """
        self.com_control = value  # Use property setter (gets validation)
        return self

    def with_custom_sub(self, value: Optional["PositiveInteger"]) -> "DiagnosticComControl":
        """
        Set customSub and return self for chaining.

        Args:
            value: The customSub to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_custom_sub("value")
        """
        self.custom_sub = value  # Use property setter (gets validation)
        return self
