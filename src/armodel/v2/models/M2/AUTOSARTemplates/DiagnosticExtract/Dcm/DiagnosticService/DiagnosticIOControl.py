from typing import List, Optional


class DiagnosticIOControl(DiagnosticServiceInstance):
    """
    This represents an instance of the "I/O Control" diagnostic service.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::IOControl::DiagnosticIOControl

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 118, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This aggregation represents the control mask record consisting of single
        # bits.
        self._controlEnable: List["DiagnosticControl"] = []

    @property
    def control_enable(self) -> List["DiagnosticControl"]:
        """Get controlEnable (Pythonic accessor)."""
        return self._controlEnable
        # This represents the corresponding DiagnosticData.
        self._dataIdentifierIdentifier: Optional["DiagnosticDataIdentifier"] = None

    @property
    def data_identifier_identifier(self) -> Optional["DiagnosticDataIdentifier"]:
        """Get dataIdentifierIdentifier (Pythonic accessor)."""
        return self._dataIdentifierIdentifier

    @data_identifier_identifier.setter
    def data_identifier_identifier(self, value: Optional["DiagnosticDataIdentifier"]) -> None:
        """
        Set dataIdentifierIdentifier with validation.

        Args:
            value: The dataIdentifierIdentifier to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dataIdentifierIdentifier = None
            return

        if not isinstance(value, DiagnosticDataIdentifier):
            raise TypeError(
                f"dataIdentifierIdentifier must be DiagnosticDataIdentifier or None, got {type(value).__name__}"
            )
        self._dataIdentifierIdentifier = value
        # Setting this attribute to true represents the ability of the to execute a
        # freezeCurrentState.
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
        # This reference substantiates that abstract reference in the reference
        # represents the ability to access among all DiagnosticIOControl in the.
        self._ioControlClass: Optional["DiagnosticIoControl"] = None

    @property
    def io_control_class(self) -> Optional["DiagnosticIoControl"]:
        """Get ioControlClass (Pythonic accessor)."""
        return self._ioControlClass

    @io_control_class.setter
    def io_control_class(self, value: Optional["DiagnosticIoControl"]) -> None:
        """
        Set ioControlClass with validation.

        Args:
            value: The ioControlClass to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ioControlClass = None
            return

        if not isinstance(value, DiagnosticIoControl):
            raise TypeError(
                f"ioControlClass must be DiagnosticIoControl or None, got {type(value).__name__}"
            )
        self._ioControlClass = value
        # Setting this attribute to true represents the ability of the execute a
        # resetToDefault.
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
        # Setting this attribute to true represents the ability of the to execute a
        # shortTermAdjustment.
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

    def getControlEnable(self) -> List["DiagnosticControl"]:
        """
        AUTOSAR-compliant getter for controlEnable.

        Returns:
            The controlEnable value

        Note:
            Delegates to control_enable property (CODING_RULE_V2_00017)
        """
        return self.control_enable  # Delegates to property

    def getDataIdentifierIdentifier(self) -> "DiagnosticDataIdentifier":
        """
        AUTOSAR-compliant getter for dataIdentifierIdentifier.

        Returns:
            The dataIdentifierIdentifier value

        Note:
            Delegates to data_identifier_identifier property (CODING_RULE_V2_00017)
        """
        return self.data_identifier_identifier  # Delegates to property

    def setDataIdentifierIdentifier(self, value: "DiagnosticDataIdentifier") -> "DiagnosticIOControl":
        """
        AUTOSAR-compliant setter for dataIdentifierIdentifier with method chaining.

        Args:
            value: The dataIdentifierIdentifier to set

        Returns:
            self for method chaining

        Note:
            Delegates to data_identifier_identifier property setter (gets validation automatically)
        """
        self.data_identifier_identifier = value  # Delegates to property setter
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

    def setFreezeCurrent(self, value: "Boolean") -> "DiagnosticIOControl":
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

    def getIoControlClass(self) -> "DiagnosticIoControl":
        """
        AUTOSAR-compliant getter for ioControlClass.

        Returns:
            The ioControlClass value

        Note:
            Delegates to io_control_class property (CODING_RULE_V2_00017)
        """
        return self.io_control_class  # Delegates to property

    def setIoControlClass(self, value: "DiagnosticIoControl") -> "DiagnosticIOControl":
        """
        AUTOSAR-compliant setter for ioControlClass with method chaining.

        Args:
            value: The ioControlClass to set

        Returns:
            self for method chaining

        Note:
            Delegates to io_control_class property setter (gets validation automatically)
        """
        self.io_control_class = value  # Delegates to property setter
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

    def setResetToDefault(self, value: "Boolean") -> "DiagnosticIOControl":
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

    def setShortTerm(self, value: "Boolean") -> "DiagnosticIOControl":
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

    def with_data_identifier_identifier(self, value: Optional["DiagnosticDataIdentifier"]) -> "DiagnosticIOControl":
        """
        Set dataIdentifierIdentifier and return self for chaining.

        Args:
            value: The dataIdentifierIdentifier to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_data_identifier_identifier("value")
        """
        self.data_identifier_identifier = value  # Use property setter (gets validation)
        return self

    def with_freeze_current(self, value: Optional["Boolean"]) -> "DiagnosticIOControl":
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

    def with_io_control_class(self, value: Optional["DiagnosticIoControl"]) -> "DiagnosticIOControl":
        """
        Set ioControlClass and return self for chaining.

        Args:
            value: The ioControlClass to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_io_control_class("value")
        """
        self.io_control_class = value  # Use property setter (gets validation)
        return self

    def with_reset_to_default(self, value: Optional["Boolean"]) -> "DiagnosticIOControl":
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

    def with_short_term(self, value: Optional["Boolean"]) -> "DiagnosticIOControl":
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
