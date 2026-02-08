from typing import (
    List,
    Optional,
)

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    ARElement,
)


class FirewallRule(ARElement):
    """
    Firewall Rule that defines the control information in individual packets.

    Package: M2::AUTOSARTemplates::AdaptivePlatform::PlatformModuleDeployment::Firewall

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 584, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute defines the capacity of the queue for rate Algorithm).
        # 2090 Document ID 63: AUTOSAR_CP_TPS_SystemTemplate R23-11.
        self._bucketSize: Optional["PositiveInteger"] = None

    @property
    def bucket_size(self) -> Optional["PositiveInteger"]:
        """Get bucketSize (Pythonic accessor)."""
        return self._bucketSize

    @bucket_size.setter
    def bucket_size(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set bucketSize with validation.

        Args:
            value: The bucketSize to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._bucketSize = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"bucketSize must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._bucketSize = value
        # Configuration of rules on the Data Link Layer atp.
        # Status=candidate.
        self._dataLinkLayer: Optional["DataLinkLayerRule"] = None

    @property
    def data_link_layer(self) -> Optional["DataLinkLayerRule"]:
        """Get dataLinkLayer (Pythonic accessor)."""
        return self._dataLinkLayer

    @data_link_layer.setter
    def data_link_layer(self, value: Optional["DataLinkLayerRule"]) -> None:
        """
        Set dataLinkLayer with validation.

        Args:
            value: The dataLinkLayer to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dataLinkLayer = None
            return

        if not isinstance(value, DataLinkLayerRule):
            raise TypeError(
                f"dataLinkLayer must be DataLinkLayerRule or None, got {type(value).__name__}"
            )
        self._dataLinkLayer = value
        # Configuration of firewall rules for DDS.
        self._ddsRule: Optional["DdsRule"] = None

    @property
    def dds_rule(self) -> Optional["DdsRule"]:
        """Get ddsRule (Pythonic accessor)."""
        return self._ddsRule

    @dds_rule.setter
    def dds_rule(self, value: Optional["DdsRule"]) -> None:
        """
        Set ddsRule with validation.

        Args:
            value: The ddsRule to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ddsRule = None
            return

        if not isinstance(value, DdsRule):
            raise TypeError(
                f"ddsRule must be DdsRule or None, got {type(value).__name__}"
            )
        self._ddsRule = value
        # Configuration of firewall rules for DoIP messages.
        self._doIpRule: Optional["DoIpRule"] = None

    @property
    def do_ip_rule(self) -> Optional["DoIpRule"]:
        """Get doIpRule (Pythonic accessor)."""
        return self._doIpRule

    @do_ip_rule.setter
    def do_ip_rule(self, value: Optional["DoIpRule"]) -> None:
        """
        Set doIpRule with validation.

        Args:
            value: The doIpRule to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._doIpRule = None
            return

        if not isinstance(value, DoIpRule):
            raise TypeError(
                f"doIpRule must be DoIpRule or None, got {type(value).__name__}"
            )
        self._doIpRule = value
        # Configuration of rules on the Network Layer atp.
        # Status=candidate.
        self._networkLayer: Optional["NetworkLayerRule"] = None

    @property
    def network_layer(self) -> Optional["NetworkLayerRule"]:
        """Get networkLayer (Pythonic accessor)."""
        return self._networkLayer

    @network_layer.setter
    def network_layer(self, value: Optional["NetworkLayerRule"]) -> None:
        """
        Set networkLayer with validation.

        Args:
            value: The networkLayer to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._networkLayer = None
            return

        if not isinstance(value, NetworkLayerRule):
            raise TypeError(
                f"networkLayer must be NetworkLayerRule or None, got {type(value).__name__}"
            )
        self._networkLayer = value
        # Configuration of generic firewall rules Tags: atp.
        # Status=candidate.
        self._payloadByte: List["PayloadBytePattern"] = []

    @property
    def payload_byte(self) -> List["PayloadBytePattern"]:
        """Get payloadByte (Pythonic accessor)."""
        return self._payloadByte
        # This attribute defines the output rate that describes how leave the queue per
        # second (leaky-bucket.
        self._refillAmount: Optional["PositiveInteger"] = None

    @property
    def refill_amount(self) -> Optional["PositiveInteger"]:
        """Get refillAmount (Pythonic accessor)."""
        return self._refillAmount

    @refill_amount.setter
    def refill_amount(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set refillAmount with validation.

        Args:
            value: The refillAmount to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._refillAmount = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"refillAmount must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._refillAmount = value
        # Configuration of firewall rules for SOME/IP messages.
        self._someipRule: Optional["SomeipProtocolRule"] = None

    @property
    def someip_rule(self) -> Optional["SomeipProtocolRule"]:
        """Get someipRule (Pythonic accessor)."""
        return self._someipRule

    @someip_rule.setter
    def someip_rule(self, value: Optional["SomeipProtocolRule"]) -> None:
        """
        Set someipRule with validation.

        Args:
            value: The someipRule to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._someipRule = None
            return

        if not isinstance(value, SomeipProtocolRule):
            raise TypeError(
                f"someipRule must be SomeipProtocolRule or None, got {type(value).__name__}"
            )
        self._someipRule = value
        # Configuration of firewall rules for SOME/IP Service.
        self._someipSdRule: Optional["SomeipSdRule"] = None

    @property
    def someip_sd_rule(self) -> Optional["SomeipSdRule"]:
        """Get someipSdRule (Pythonic accessor)."""
        return self._someipSdRule

    @someip_sd_rule.setter
    def someip_sd_rule(self, value: Optional["SomeipSdRule"]) -> None:
        """
        Set someipSdRule with validation.

        Args:
            value: The someipSdRule to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._someipSdRule = None
            return

        if not isinstance(value, SomeipSdRule):
            raise TypeError(
                f"someipSdRule must be SomeipSdRule or None, got {type(value).__name__}"
            )
        self._someipSdRule = value
        # Configuration of rules on the Transport Layer atp.
        # Status=candidate.
        self._transportLayer: Optional["TransportLayerRule"] = None

    @property
    def transport_layer(self) -> Optional["TransportLayerRule"]:
        """Get transportLayer (Pythonic accessor)."""
        return self._transportLayer

    @transport_layer.setter
    def transport_layer(self, value: Optional["TransportLayerRule"]) -> None:
        """
        Set transportLayer with validation.

        Args:
            value: The transportLayer to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._transportLayer = None
            return

        if not isinstance(value, TransportLayerRule):
            raise TypeError(
                f"transportLayer must be TransportLayerRule or None, got {type(value).__name__}"
            )
        self._transportLayer = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBucketSize(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for bucketSize.

        Returns:
            The bucketSize value

        Note:
            Delegates to bucket_size property (CODING_RULE_V2_00017)
        """
        return self.bucket_size  # Delegates to property

    def setBucketSize(self, value: "PositiveInteger") -> "FirewallRule":
        """
        AUTOSAR-compliant setter for bucketSize with method chaining.

        Args:
            value: The bucketSize to set

        Returns:
            self for method chaining

        Note:
            Delegates to bucket_size property setter (gets validation automatically)
        """
        self.bucket_size = value  # Delegates to property setter
        return self

    def getDataLinkLayer(self) -> "DataLinkLayerRule":
        """
        AUTOSAR-compliant getter for dataLinkLayer.

        Returns:
            The dataLinkLayer value

        Note:
            Delegates to data_link_layer property (CODING_RULE_V2_00017)
        """
        return self.data_link_layer  # Delegates to property

    def setDataLinkLayer(self, value: "DataLinkLayerRule") -> "FirewallRule":
        """
        AUTOSAR-compliant setter for dataLinkLayer with method chaining.

        Args:
            value: The dataLinkLayer to set

        Returns:
            self for method chaining

        Note:
            Delegates to data_link_layer property setter (gets validation automatically)
        """
        self.data_link_layer = value  # Delegates to property setter
        return self

    def getDdsRule(self) -> "DdsRule":
        """
        AUTOSAR-compliant getter for ddsRule.

        Returns:
            The ddsRule value

        Note:
            Delegates to dds_rule property (CODING_RULE_V2_00017)
        """
        return self.dds_rule  # Delegates to property

    def setDdsRule(self, value: "DdsRule") -> "FirewallRule":
        """
        AUTOSAR-compliant setter for ddsRule with method chaining.

        Args:
            value: The ddsRule to set

        Returns:
            self for method chaining

        Note:
            Delegates to dds_rule property setter (gets validation automatically)
        """
        self.dds_rule = value  # Delegates to property setter
        return self

    def getDoIpRule(self) -> "DoIpRule":
        """
        AUTOSAR-compliant getter for doIpRule.

        Returns:
            The doIpRule value

        Note:
            Delegates to do_ip_rule property (CODING_RULE_V2_00017)
        """
        return self.do_ip_rule  # Delegates to property

    def setDoIpRule(self, value: "DoIpRule") -> "FirewallRule":
        """
        AUTOSAR-compliant setter for doIpRule with method chaining.

        Args:
            value: The doIpRule to set

        Returns:
            self for method chaining

        Note:
            Delegates to do_ip_rule property setter (gets validation automatically)
        """
        self.do_ip_rule = value  # Delegates to property setter
        return self

    def getNetworkLayer(self) -> "NetworkLayerRule":
        """
        AUTOSAR-compliant getter for networkLayer.

        Returns:
            The networkLayer value

        Note:
            Delegates to network_layer property (CODING_RULE_V2_00017)
        """
        return self.network_layer  # Delegates to property

    def setNetworkLayer(self, value: "NetworkLayerRule") -> "FirewallRule":
        """
        AUTOSAR-compliant setter for networkLayer with method chaining.

        Args:
            value: The networkLayer to set

        Returns:
            self for method chaining

        Note:
            Delegates to network_layer property setter (gets validation automatically)
        """
        self.network_layer = value  # Delegates to property setter
        return self

    def getPayloadByte(self) -> List["PayloadBytePattern"]:
        """
        AUTOSAR-compliant getter for payloadByte.

        Returns:
            The payloadByte value

        Note:
            Delegates to payload_byte property (CODING_RULE_V2_00017)
        """
        return self.payload_byte  # Delegates to property

    def getRefillAmount(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for refillAmount.

        Returns:
            The refillAmount value

        Note:
            Delegates to refill_amount property (CODING_RULE_V2_00017)
        """
        return self.refill_amount  # Delegates to property

    def setRefillAmount(self, value: "PositiveInteger") -> "FirewallRule":
        """
        AUTOSAR-compliant setter for refillAmount with method chaining.

        Args:
            value: The refillAmount to set

        Returns:
            self for method chaining

        Note:
            Delegates to refill_amount property setter (gets validation automatically)
        """
        self.refill_amount = value  # Delegates to property setter
        return self

    def getSomeipRule(self) -> "SomeipProtocolRule":
        """
        AUTOSAR-compliant getter for someipRule.

        Returns:
            The someipRule value

        Note:
            Delegates to someip_rule property (CODING_RULE_V2_00017)
        """
        return self.someip_rule  # Delegates to property

    def setSomeipRule(self, value: "SomeipProtocolRule") -> "FirewallRule":
        """
        AUTOSAR-compliant setter for someipRule with method chaining.

        Args:
            value: The someipRule to set

        Returns:
            self for method chaining

        Note:
            Delegates to someip_rule property setter (gets validation automatically)
        """
        self.someip_rule = value  # Delegates to property setter
        return self

    def getSomeipSdRule(self) -> "SomeipSdRule":
        """
        AUTOSAR-compliant getter for someipSdRule.

        Returns:
            The someipSdRule value

        Note:
            Delegates to someip_sd_rule property (CODING_RULE_V2_00017)
        """
        return self.someip_sd_rule  # Delegates to property

    def setSomeipSdRule(self, value: "SomeipSdRule") -> "FirewallRule":
        """
        AUTOSAR-compliant setter for someipSdRule with method chaining.

        Args:
            value: The someipSdRule to set

        Returns:
            self for method chaining

        Note:
            Delegates to someip_sd_rule property setter (gets validation automatically)
        """
        self.someip_sd_rule = value  # Delegates to property setter
        return self

    def getTransportLayer(self) -> "TransportLayerRule":
        """
        AUTOSAR-compliant getter for transportLayer.

        Returns:
            The transportLayer value

        Note:
            Delegates to transport_layer property (CODING_RULE_V2_00017)
        """
        return self.transport_layer  # Delegates to property

    def setTransportLayer(self, value: "TransportLayerRule") -> "FirewallRule":
        """
        AUTOSAR-compliant setter for transportLayer with method chaining.

        Args:
            value: The transportLayer to set

        Returns:
            self for method chaining

        Note:
            Delegates to transport_layer property setter (gets validation automatically)
        """
        self.transport_layer = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_bucket_size(self, value: Optional["PositiveInteger"]) -> "FirewallRule":
        """
        Set bucketSize and return self for chaining.

        Args:
            value: The bucketSize to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_bucket_size("value")
        """
        self.bucket_size = value  # Use property setter (gets validation)
        return self

    def with_data_link_layer(self, value: Optional["DataLinkLayerRule"]) -> "FirewallRule":
        """
        Set dataLinkLayer and return self for chaining.

        Args:
            value: The dataLinkLayer to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_data_link_layer("value")
        """
        self.data_link_layer = value  # Use property setter (gets validation)
        return self

    def with_dds_rule(self, value: Optional["DdsRule"]) -> "FirewallRule":
        """
        Set ddsRule and return self for chaining.

        Args:
            value: The ddsRule to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_dds_rule("value")
        """
        self.dds_rule = value  # Use property setter (gets validation)
        return self

    def with_do_ip_rule(self, value: Optional["DoIpRule"]) -> "FirewallRule":
        """
        Set doIpRule and return self for chaining.

        Args:
            value: The doIpRule to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_do_ip_rule("value")
        """
        self.do_ip_rule = value  # Use property setter (gets validation)
        return self

    def with_network_layer(self, value: Optional["NetworkLayerRule"]) -> "FirewallRule":
        """
        Set networkLayer and return self for chaining.

        Args:
            value: The networkLayer to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_network_layer("value")
        """
        self.network_layer = value  # Use property setter (gets validation)
        return self

    def with_refill_amount(self, value: Optional["PositiveInteger"]) -> "FirewallRule":
        """
        Set refillAmount and return self for chaining.

        Args:
            value: The refillAmount to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_refill_amount("value")
        """
        self.refill_amount = value  # Use property setter (gets validation)
        return self

    def with_someip_rule(self, value: Optional["SomeipProtocolRule"]) -> "FirewallRule":
        """
        Set someipRule and return self for chaining.

        Args:
            value: The someipRule to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_someip_rule("value")
        """
        self.someip_rule = value  # Use property setter (gets validation)
        return self

    def with_someip_sd_rule(self, value: Optional["SomeipSdRule"]) -> "FirewallRule":
        """
        Set someipSdRule and return self for chaining.

        Args:
            value: The someipSdRule to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_someip_sd_rule("value")
        """
        self.someip_sd_rule = value  # Use property setter (gets validation)
        return self

    def with_transport_layer(self, value: Optional["TransportLayerRule"]) -> "FirewallRule":
        """
        Set transportLayer and return self for chaining.

        Args:
            value: The transportLayer to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_transport_layer("value")
        """
        self.transport_layer = value  # Use property setter (gets validation)
        return self
