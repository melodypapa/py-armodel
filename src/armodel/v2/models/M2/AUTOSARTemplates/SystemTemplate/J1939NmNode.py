from typing import Optional


class J1939NmNode(NmNode):
    """
    J1939 specific NM Node attributes.

    Package: M2::AUTOSARTemplates::SystemTemplate::NetworkManagement::J1939NmNode

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 322, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 691, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Defines the Address Configuration Capability of the J1939NmNode
        # (corresponding to an SAE J1939 Controller Application, CA).
        self._address: Optional["J1939NmAddress"] = None

    @property
    def address(self) -> Optional["J1939NmAddress"]:
        """Get address (Pythonic accessor)."""
        return self._address

    @address.setter
    def address(self, value: Optional["J1939NmAddress"]) -> None:
        """
        Set address with validation.

        Args:
            value: The address to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._address = None
            return

        if not isinstance(value, J1939NmAddress):
            raise TypeError(
                f"address must be J1939NmAddress or None, got {type(value).__name__}"
            )
        self._address = value
        # NodeName configuration.
        self._nodeName: Optional["J1939NodeName"] = None

    @property
    def node_name(self) -> Optional["J1939NodeName"]:
        """Get nodeName (Pythonic accessor)."""
        return self._nodeName

    @node_name.setter
    def node_name(self, value: Optional["J1939NodeName"]) -> None:
        """
        Set nodeName with validation.

        Args:
            value: The nodeName to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nodeName = None
            return

        if not isinstance(value, J1939NodeName):
            raise TypeError(
                f"nodeName must be J1939NodeName or None, got {type(value).__name__}"
            )
        self._nodeName = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAddress(self) -> "J1939NmAddress":
        """
        AUTOSAR-compliant getter for address.

        Returns:
            The address value

        Note:
            Delegates to address property (CODING_RULE_V2_00017)
        """
        return self.address  # Delegates to property

    def setAddress(self, value: "J1939NmAddress") -> "J1939NmNode":
        """
        AUTOSAR-compliant setter for address with method chaining.

        Args:
            value: The address to set

        Returns:
            self for method chaining

        Note:
            Delegates to address property setter (gets validation automatically)
        """
        self.address = value  # Delegates to property setter
        return self

    def getNodeName(self) -> "J1939NodeName":
        """
        AUTOSAR-compliant getter for nodeName.

        Returns:
            The nodeName value

        Note:
            Delegates to node_name property (CODING_RULE_V2_00017)
        """
        return self.node_name  # Delegates to property

    def setNodeName(self, value: "J1939NodeName") -> "J1939NmNode":
        """
        AUTOSAR-compliant setter for nodeName with method chaining.

        Args:
            value: The nodeName to set

        Returns:
            self for method chaining

        Note:
            Delegates to node_name property setter (gets validation automatically)
        """
        self.node_name = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_address(self, value: Optional["J1939NmAddress"]) -> "J1939NmNode":
        """
        Set address and return self for chaining.

        Args:
            value: The address to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_address("value")
        """
        self.address = value  # Use property setter (gets validation)
        return self

    def with_node_name(self, value: Optional["J1939NodeName"]) -> "J1939NmNode":
        """
        Set nodeName and return self for chaining.

        Args:
            value: The nodeName to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_node_name("value")
        """
        self.node_name = value  # Use property setter (gets validation)
        return self
