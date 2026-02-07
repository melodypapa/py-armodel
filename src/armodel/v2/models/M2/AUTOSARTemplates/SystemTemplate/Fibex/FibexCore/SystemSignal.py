from typing import Optional


class SystemSignal(ARElement):
    """
    The system signal represents the communication system’s view of data
    exchanged between SW components which reside on different ECUs. The system
    signals allow to represent this communication in a flattened structure, with
    exactly one system signal defined for each data element prototype sent and
    received by connected SW component instances.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication::SystemSignal

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 332, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 1009, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 218, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The length of dynamic length signals is variable in a maximum length of such
        # a signal is the configuration (attribute length in ISignal.
        self._dynamicLength: Optional["Boolean"] = None

    @property
    def dynamic_length(self) -> Optional["Boolean"]:
        """Get dynamicLength (Pythonic accessor)."""
        return self._dynamicLength

    @dynamic_length.setter
    def dynamic_length(self, value: Optional["Boolean"]) -> None:
        """
        Set dynamicLength with validation.

        Args:
            value: The dynamicLength to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dynamicLength = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"dynamicLength must be Boolean or None, got {type(value).__name__}"
            )
        self._dynamicLength = value
        # Specification of the physical representation.
        self._physicalProps: Optional["SwDataDefProps"] = None

    @property
    def physical_props(self) -> Optional["SwDataDefProps"]:
        """Get physicalProps (Pythonic accessor)."""
        return self._physicalProps

    @physical_props.setter
    def physical_props(self, value: Optional["SwDataDefProps"]) -> None:
        """
        Set physicalProps with validation.

        Args:
            value: The physicalProps to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._physicalProps = None
            return

        if not isinstance(value, SwDataDefProps):
            raise TypeError(
                f"physicalProps must be SwDataDefProps or None, got {type(value).__name__}"
            )
        self._physicalProps = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDynamicLength(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for dynamicLength.

        Returns:
            The dynamicLength value

        Note:
            Delegates to dynamic_length property (CODING_RULE_V2_00017)
        """
        return self.dynamic_length  # Delegates to property

    def setDynamicLength(self, value: "Boolean") -> "SystemSignal":
        """
        AUTOSAR-compliant setter for dynamicLength with method chaining.

        Args:
            value: The dynamicLength to set

        Returns:
            self for method chaining

        Note:
            Delegates to dynamic_length property setter (gets validation automatically)
        """
        self.dynamic_length = value  # Delegates to property setter
        return self

    def getPhysicalProps(self) -> "SwDataDefProps":
        """
        AUTOSAR-compliant getter for physicalProps.

        Returns:
            The physicalProps value

        Note:
            Delegates to physical_props property (CODING_RULE_V2_00017)
        """
        return self.physical_props  # Delegates to property

    def setPhysicalProps(self, value: "SwDataDefProps") -> "SystemSignal":
        """
        AUTOSAR-compliant setter for physicalProps with method chaining.

        Args:
            value: The physicalProps to set

        Returns:
            self for method chaining

        Note:
            Delegates to physical_props property setter (gets validation automatically)
        """
        self.physical_props = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_dynamic_length(self, value: Optional["Boolean"]) -> "SystemSignal":
        """
        Set dynamicLength and return self for chaining.

        Args:
            value: The dynamicLength to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_dynamic_length("value")
        """
        self.dynamic_length = value  # Use property setter (gets validation)
        return self

    def with_physical_props(self, value: Optional["SwDataDefProps"]) -> "SystemSignal":
        """
        Set physicalProps and return self for chaining.

        Args:
            value: The physicalProps to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_physical_props("value")
        """
        self.physical_props = value  # Use property setter (gets validation)
        return self
