from typing import Optional


class DelegatedPortAnnotation(GeneralAnnotation):
    """
    Annotation to a "delegated port" to specify the Signal Fan In or Signal Fan
    Out inside the CompositionSw ComponentType.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::ApplicationAttributes::DelegatedPortAnnotation

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 162, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Specifies the Signal Fan In or Signal Fan Out inside the.
        self._signalFan: Optional["SignalFanEnum"] = None

    @property
    def signal_fan(self) -> Optional["SignalFanEnum"]:
        """Get signalFan (Pythonic accessor)."""
        return self._signalFan

    @signal_fan.setter
    def signal_fan(self, value: Optional["SignalFanEnum"]) -> None:
        """
        Set signalFan with validation.

        Args:
            value: The signalFan to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._signalFan = None
            return

        if not isinstance(value, SignalFanEnum):
            raise TypeError(
                f"signalFan must be SignalFanEnum or None, got {type(value).__name__}"
            )
        self._signalFan = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getSignalFan(self) -> "SignalFanEnum":
        """
        AUTOSAR-compliant getter for signalFan.

        Returns:
            The signalFan value

        Note:
            Delegates to signal_fan property (CODING_RULE_V2_00017)
        """
        return self.signal_fan  # Delegates to property

    def setSignalFan(self, value: "SignalFanEnum") -> "DelegatedPortAnnotation":
        """
        AUTOSAR-compliant setter for signalFan with method chaining.

        Args:
            value: The signalFan to set

        Returns:
            self for method chaining

        Note:
            Delegates to signal_fan property setter (gets validation automatically)
        """
        self.signal_fan = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_signal_fan(self, value: Optional["SignalFanEnum"]) -> "DelegatedPortAnnotation":
        """
        Set signalFan and return self for chaining.

        Args:
            value: The signalFan to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_signal_fan("value")
        """
        self.signal_fan = value  # Use property setter (gets validation)
        return self
