from typing import Optional


class ReceiverAnnotation(SenderReceiverAnnotation):
    """
    Annotation of a receiver port, specifying properties of data elements that
    don’t affect communication or generation of the RTE. The given attributes
    are requirements on the required data.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::ApplicationAttributes::ReceiverAnnotation

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 153, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The maximum allowed age of the signal since it was by a sensor.
        # This is a requirement the receiver side.
        self._signalAge: Optional["MultidimensionalTime"] = None

    @property
    def signal_age(self) -> Optional["MultidimensionalTime"]:
        """Get signalAge (Pythonic accessor)."""
        return self._signalAge

    @signal_age.setter
    def signal_age(self, value: Optional["MultidimensionalTime"]) -> None:
        """
        Set signalAge with validation.

        Args:
            value: The signalAge to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._signalAge = None
            return

        if not isinstance(value, MultidimensionalTime):
            raise TypeError(
                f"signalAge must be MultidimensionalTime or None, got {type(value).__name__}"
            )
        self._signalAge = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getSignalAge(self) -> "MultidimensionalTime":
        """
        AUTOSAR-compliant getter for signalAge.

        Returns:
            The signalAge value

        Note:
            Delegates to signal_age property (CODING_RULE_V2_00017)
        """
        return self.signal_age  # Delegates to property

    def setSignalAge(self, value: "MultidimensionalTime") -> "ReceiverAnnotation":
        """
        AUTOSAR-compliant setter for signalAge with method chaining.

        Args:
            value: The signalAge to set

        Returns:
            self for method chaining

        Note:
            Delegates to signal_age property setter (gets validation automatically)
        """
        self.signal_age = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_signal_age(self, value: Optional["MultidimensionalTime"]) -> "ReceiverAnnotation":
        """
        Set signalAge and return self for chaining.

        Args:
            value: The signalAge to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_signal_age("value")
        """
        self.signal_age = value  # Use property setter (gets validation)
        return self
