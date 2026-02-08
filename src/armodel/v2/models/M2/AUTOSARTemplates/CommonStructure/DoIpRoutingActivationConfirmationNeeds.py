from typing import Optional


class DoIpRoutingActivationConfirmationNeeds(DoIpServiceNeeds):
    """
    DoIpRoutingActivationConfirmationNeeds indicates that the software-component
    that owns this Service Needs will have a confirmation required for a DoIP
    routing activation service (0x0005) according to ISO 13400-2:2012.

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::DoIpRoutingActivationConfirmationNeeds

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 807, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Describes the length in byte of the additional information RA confirmation
                # that is provided by the software entity.
        # software entity is a software-component the not need to exist as the
                # information is the length of the uint8 Array type.
        # Otherwise software entity is a Complex Driver) this attribute be filled out
                # if additional information is provided.
        self._dataLength: Optional["PositiveInteger"] = None

    @property
    def data_length(self) -> Optional["PositiveInteger"]:
        """Get dataLength (Pythonic accessor)."""
        return self._dataLength

    @data_length.setter
    def data_length(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set dataLength with validation.

        Args:
            value: The dataLength to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dataLength = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"dataLength must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._dataLength = value
        # Describes the ISO 13400-2:2012 "routing activation activation type" which is
                # received via DoIP 0x00 is DEFAULT, 0x01 is WWH-OBD.
        # If the specified values (0x00 or 0x01) is needed shall contain RA_ + hex
                # value representation of value shall be used (i.
        # e: RA_0xE1).
        self._routing: Optional["NameToken"] = None

    @property
    def routing(self) -> Optional["NameToken"]:
        """Get routing (Pythonic accessor)."""
        return self._routing

    @routing.setter
    def routing(self, value: Optional["NameToken"]) -> None:
        """
        Set routing with validation.

        Args:
            value: The routing to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._routing = None
            return

        if not isinstance(value, NameToken):
            raise TypeError(
                f"routing must be NameToken or None, got {type(value).__name__}"
            )
        self._routing = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDataLength(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for dataLength.

        Returns:
            The dataLength value

        Note:
            Delegates to data_length property (CODING_RULE_V2_00017)
        """
        return self.data_length  # Delegates to property

    def setDataLength(self, value: "PositiveInteger") -> "DoIpRoutingActivationConfirmationNeeds":
        """
        AUTOSAR-compliant setter for dataLength with method chaining.

        Args:
            value: The dataLength to set

        Returns:
            self for method chaining

        Note:
            Delegates to data_length property setter (gets validation automatically)
        """
        self.data_length = value  # Delegates to property setter
        return self

    def getRouting(self) -> "NameToken":
        """
        AUTOSAR-compliant getter for routing.

        Returns:
            The routing value

        Note:
            Delegates to routing property (CODING_RULE_V2_00017)
        """
        return self.routing  # Delegates to property

    def setRouting(self, value: "NameToken") -> "DoIpRoutingActivationConfirmationNeeds":
        """
        AUTOSAR-compliant setter for routing with method chaining.

        Args:
            value: The routing to set

        Returns:
            self for method chaining

        Note:
            Delegates to routing property setter (gets validation automatically)
        """
        self.routing = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_data_length(self, value: Optional["PositiveInteger"]) -> "DoIpRoutingActivationConfirmationNeeds":
        """
        Set dataLength and return self for chaining.

        Args:
            value: The dataLength to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_data_length("value")
        """
        self.data_length = value  # Use property setter (gets validation)
        return self

    def with_routing(self, value: Optional["NameToken"]) -> "DoIpRoutingActivationConfirmationNeeds":
        """
        Set routing and return self for chaining.

        Args:
            value: The routing to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_routing("value")
        """
        self.routing = value  # Use property setter (gets validation)
        return self
