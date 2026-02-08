from typing import Optional
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import DiagnosticCapabilityElement


class DiagnosticIoControlNeeds(DiagnosticCapabilityElement):
    """
    Specifies the general needs on the configuration of the Diagnostic
    Communication Manager (DCM) which are not related to a particular item (e.g.
    a PID). The main use case is the mapping of service ports to the Dcm which
    are not related to a particular item.

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::DiagnosticIoControlNeeds

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 248, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 119, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 781, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to the DiagnosticValueNeeds indicating the the current value via
        # signalBasedDiagnostics.
        self._currentValue: Optional["DiagnosticValueNeeds"] = None

    @property
    def current_value(self) -> Optional["DiagnosticValueNeeds"]:
        """Get currentValue (Pythonic accessor)."""
        return self._currentValue

    @current_value.setter
    def current_value(self, value: Optional["DiagnosticValueNeeds"]) -> None:
        """
        Set currentValue with validation.

        Args:
            value: The currentValue to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._currentValue = None
            return

        if not isinstance(value, DiagnosticValueNeeds):
            raise TypeError(
                f"currentValue must be DiagnosticValueNeeds or None, got {type(value).__name__}"
            )
        self._currentValue = value
        # This attribute determines, if the referenced port supports freezing of I/O
                # value.
        # freeze is not supported if the enclosing aggregated by a Swc [constr_1364].
        self._freezeCurrent: Optional["Boolean"] = None

    @property
    def freeze_current(self) -> Optional["Boolean"]:
        """Get freezeCurrent (Pythonic accessor)."""
        return self._freezeCurrent

    @freeze_current.setter
    def freeze_current(self, value: Optional["Boolean"]) -> None:
        """
        Set freezeCurrent with validation.

        Args:
            value: The freezeCurrent to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._freezeCurrent = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"freezeCurrent must be Boolean or None, got {type(value).__name__}"
            )
        self._freezeCurrent = value
        # This represents a flag for the existence of the ResetTo operation in the
        # service interface.
        self._resetToDefault: Optional["Boolean"] = None

    @property
    def reset_to_default(self) -> Optional["Boolean"]:
        """Get resetToDefault (Pythonic accessor)."""
        return self._resetToDefault

    @reset_to_default.setter
    def reset_to_default(self, value: Optional["Boolean"]) -> None:
        """
        Set resetToDefault with validation.

        Args:
            value: The resetToDefault to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._resetToDefault = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"resetToDefault must be Boolean or None, got {type(value).__name__}"
            )
        self._resetToDefault = value
        # This attribute determines, if the referenced port supports setting of I/O
                # value to a specific value by the diagnostic tester.
        # term adjustment is not supported if the is aggregated by a [constr_1364].
        self._shortTerm: Optional["Boolean"] = None

    @property
    def short_term(self) -> Optional["Boolean"]:
        """Get shortTerm (Pythonic accessor)."""
        return self._shortTerm

    @short_term.setter
    def short_term(self, value: Optional["Boolean"]) -> None:
        """
        Set shortTerm with validation.

        Args:
            value: The shortTerm to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._shortTerm = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"shortTerm must be Boolean or None, got {type(value).__name__}"
            )
        self._shortTerm = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCurrentValue(self) -> "DiagnosticValueNeeds":
        """
        AUTOSAR-compliant getter for currentValue.

        Returns:
            The currentValue value

        Note:
            Delegates to current_value property (CODING_RULE_V2_00017)
        """
        return self.current_value  # Delegates to property

    def setCurrentValue(self, value: "DiagnosticValueNeeds") -> "DiagnosticIoControlNeeds":
        """
        AUTOSAR-compliant setter for currentValue with method chaining.

        Args:
            value: The currentValue to set

        Returns:
            self for method chaining

        Note:
            Delegates to current_value property setter (gets validation automatically)
        """
        self.current_value = value  # Delegates to property setter
        return self

    def getFreezeCurrent(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for freezeCurrent.

        Returns:
            The freezeCurrent value

        Note:
            Delegates to freeze_current property (CODING_RULE_V2_00017)
        """
        return self.freeze_current  # Delegates to property

    def setFreezeCurrent(self, value: "Boolean") -> "DiagnosticIoControlNeeds":
        """
        AUTOSAR-compliant setter for freezeCurrent with method chaining.

        Args:
            value: The freezeCurrent to set

        Returns:
            self for method chaining

        Note:
            Delegates to freeze_current property setter (gets validation automatically)
        """
        self.freeze_current = value  # Delegates to property setter
        return self

    def getResetToDefault(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for resetToDefault.

        Returns:
            The resetToDefault value

        Note:
            Delegates to reset_to_default property (CODING_RULE_V2_00017)
        """
        return self.reset_to_default  # Delegates to property

    def setResetToDefault(self, value: "Boolean") -> "DiagnosticIoControlNeeds":
        """
        AUTOSAR-compliant setter for resetToDefault with method chaining.

        Args:
            value: The resetToDefault to set

        Returns:
            self for method chaining

        Note:
            Delegates to reset_to_default property setter (gets validation automatically)
        """
        self.reset_to_default = value  # Delegates to property setter
        return self

    def getShortTerm(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for shortTerm.

        Returns:
            The shortTerm value

        Note:
            Delegates to short_term property (CODING_RULE_V2_00017)
        """
        return self.short_term  # Delegates to property

    def setShortTerm(self, value: "Boolean") -> "DiagnosticIoControlNeeds":
        """
        AUTOSAR-compliant setter for shortTerm with method chaining.

        Args:
            value: The shortTerm to set

        Returns:
            self for method chaining

        Note:
            Delegates to short_term property setter (gets validation automatically)
        """
        self.short_term = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_current_value(self, value: Optional["DiagnosticValueNeeds"]) -> "DiagnosticIoControlNeeds":
        """
        Set currentValue and return self for chaining.

        Args:
            value: The currentValue to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_current_value("value")
        """
        self.current_value = value  # Use property setter (gets validation)
        return self

    def with_freeze_current(self, value: Optional["Boolean"]) -> "DiagnosticIoControlNeeds":
        """
        Set freezeCurrent and return self for chaining.

        Args:
            value: The freezeCurrent to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_freeze_current("value")
        """
        self.freeze_current = value  # Use property setter (gets validation)
        return self

    def with_reset_to_default(self, value: Optional["Boolean"]) -> "DiagnosticIoControlNeeds":
        """
        Set resetToDefault and return self for chaining.

        Args:
            value: The resetToDefault to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_reset_to_default("value")
        """
        self.reset_to_default = value  # Use property setter (gets validation)
        return self

    def with_short_term(self, value: Optional["Boolean"]) -> "DiagnosticIoControlNeeds":
        """
        Set shortTerm and return self for chaining.

        Args:
            value: The shortTerm to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_short_term("value")
        """
        self.short_term = value  # Use property setter (gets validation)
        return self
