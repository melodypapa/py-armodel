from typing import Optional


class GenericTp(TransportProtocolConfiguration):
    """
    Content Model for a generic transport protocol.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::GenericTp

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 459, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Transport Protocol dependent Address.
        self._tpAddress: Optional["String"] = None

    @property
    def tp_address(self) -> Optional["String"]:
        """Get tpAddress (Pythonic accessor)."""
        return self._tpAddress

    @tp_address.setter
    def tp_address(self, value: Optional["String"]) -> None:
        """
        Set tpAddress with validation.

        Args:
            value: The tpAddress to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tpAddress = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"tpAddress must be String or None, got {type(value).__name__}"
            )
        self._tpAddress = value
        # Name of the used Transport Protocol.
        self._tpTechnology: Optional["String"] = None

    @property
    def tp_technology(self) -> Optional["String"]:
        """Get tpTechnology (Pythonic accessor)."""
        return self._tpTechnology

    @tp_technology.setter
    def tp_technology(self, value: Optional["String"]) -> None:
        """
        Set tpTechnology with validation.

        Args:
            value: The tpTechnology to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tpTechnology = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"tpTechnology must be String or None, got {type(value).__name__}"
            )
        self._tpTechnology = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTpAddress(self) -> "String":
        """
        AUTOSAR-compliant getter for tpAddress.

        Returns:
            The tpAddress value

        Note:
            Delegates to tp_address property (CODING_RULE_V2_00017)
        """
        return self.tp_address  # Delegates to property

    def setTpAddress(self, value: "String") -> "GenericTp":
        """
        AUTOSAR-compliant setter for tpAddress with method chaining.

        Args:
            value: The tpAddress to set

        Returns:
            self for method chaining

        Note:
            Delegates to tp_address property setter (gets validation automatically)
        """
        self.tp_address = value  # Delegates to property setter
        return self

    def getTpTechnology(self) -> "String":
        """
        AUTOSAR-compliant getter for tpTechnology.

        Returns:
            The tpTechnology value

        Note:
            Delegates to tp_technology property (CODING_RULE_V2_00017)
        """
        return self.tp_technology  # Delegates to property

    def setTpTechnology(self, value: "String") -> "GenericTp":
        """
        AUTOSAR-compliant setter for tpTechnology with method chaining.

        Args:
            value: The tpTechnology to set

        Returns:
            self for method chaining

        Note:
            Delegates to tp_technology property setter (gets validation automatically)
        """
        self.tp_technology = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_tp_address(self, value: Optional["String"]) -> "GenericTp":
        """
        Set tpAddress and return self for chaining.

        Args:
            value: The tpAddress to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tp_address("value")
        """
        self.tp_address = value  # Use property setter (gets validation)
        return self

    def with_tp_technology(self, value: Optional["String"]) -> "GenericTp":
        """
        Set tpTechnology and return self for chaining.

        Args:
            value: The tpTechnology to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tp_technology("value")
        """
        self.tp_technology = value  # Use property setter (gets validation)
        return self
