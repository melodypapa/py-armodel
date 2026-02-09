"""
AUTOSAR Package - Firewall

Package: M2::AUTOSARTemplates::AdaptivePlatform::PlatformModuleDeployment::Firewall
"""

from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    ARElement,
)


class StateDependentFirewall(ARElement):
    """
    Firewall rules that are defined in a firewall state
    
    Package: M2::AUTOSARTemplates::AdaptivePlatform::PlatformModuleDeployment::Firewall::StateDependentFirewall
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 583, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute defines a defaultAction in case that the not yet set.
        self._defaultAction: Optional["FirewallActionEnum"] = None

    @property
    def default_action(self) -> Optional["FirewallActionEnum"]:
        """Get defaultAction (Pythonic accessor)."""
        return self._defaultAction

    @default_action.setter
    def default_action(self, value: Optional["FirewallActionEnum"]) -> None:
        """
        Set defaultAction with validation.
        
        Args:
            value: The defaultAction to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._defaultAction = None
            return

        if not isinstance(value, FirewallActionEnum):
            raise TypeError(
                f"defaultAction must be FirewallActionEnum or None, got {type(value).__name__}"
            )
        self._defaultAction = value
        # Status=candidate.
        self._firewallRule: List["FirewallRuleProps"] = []

    @property
    def firewall_rule(self) -> List["FirewallRuleProps"]:
        """Get firewallRule (Pythonic accessor)."""
        return self._firewallRule
        # Reference to firewall states in which the Firewall is active.
        # one of the referenced ModeDeclarations is the current state then the firewall
                # rule shall be considered as.
        self._firewallState: List["ModeDeclaration"] = []

    @property
    def firewall_state(self) -> List["ModeDeclaration"]:
        """Get firewallState (Pythonic accessor)."""
        return self._firewallState

    def with_firewall_rule(self, value):
        """
        Set firewall_rule and return self for chaining.

        Args:
            value: The firewall_rule to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_firewall_rule("value")
        """
        self.firewall_rule = value  # Use property setter (gets validation)
        return self

    def with_firewall_state(self, value):
        """
        Set firewall_state and return self for chaining.

        Args:
            value: The firewall_state to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_firewall_state("value")
        """
        self.firewall_state = value  # Use property setter (gets validation)
        return self

    def with_matching_egress(self, value):
        """
        Set matching_egress and return self for chaining.

        Args:
            value: The matching_egress to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_matching_egress("value")
        """
        self.matching_egress = value  # Use property setter (gets validation)
        return self

    def with_matching(self, value):
        """
        Set matching and return self for chaining.

        Args:
            value: The matching to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_matching("value")
        """
        self.matching = value  # Use property setter (gets validation)
        return self

    def with_payload_byte(self, value):
        """
        Set payload_byte and return self for chaining.

        Args:
            value: The payload_byte to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_payload_byte("value")
        """
        self.payload_byte = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDefaultAction(self) -> "FirewallActionEnum":
        """
        AUTOSAR-compliant getter for defaultAction.
        
        Returns:
            The defaultAction value
        
        Note:
            Delegates to default_action property (CODING_RULE_V2_00017)
        """
        return self.default_action  # Delegates to property

    def setDefaultAction(self, value: "FirewallActionEnum") -> "StateDependentFirewall":
        """
        AUTOSAR-compliant setter for defaultAction with method chaining.
        
        Args:
            value: The defaultAction to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to default_action property setter (gets validation automatically)
        """
        self.default_action = value  # Delegates to property setter
        return self

    def getFirewallRule(self) -> List["FirewallRuleProps"]:
        """
        AUTOSAR-compliant getter for firewallRule.
        
        Returns:
            The firewallRule value
        
        Note:
            Delegates to firewall_rule property (CODING_RULE_V2_00017)
        """
        return self.firewall_rule  # Delegates to property

    def getFirewallState(self) -> List["ModeDeclaration"]:
        """
        AUTOSAR-compliant getter for firewallState.
        
        Returns:
            The firewallState value
        
        Note:
            Delegates to firewall_state property (CODING_RULE_V2_00017)
        """
        return self.firewall_state  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_default_action(self, value: Optional["FirewallActionEnum"]) -> "StateDependentFirewall":
        """
        Set defaultAction and return self for chaining.
        
        Args:
            value: The defaultAction to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_default_action("value")
        """
        self.default_action = value  # Use property setter (gets validation)
        return self



class FirewallRuleProps(ARObject):
    """
    Firewall rule that is defined by an action that is performed if the
    referenced pattern matches.
    
    Package: M2::AUTOSARTemplates::AdaptivePlatform::PlatformModuleDeployment::Firewall::FirewallRuleProps
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 584, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Action that is performed by the firewall if the matching fulfilled.
        self._action: Optional["FirewallActionEnum"] = None

    @property
    def action(self) -> Optional["FirewallActionEnum"]:
        """Get action (Pythonic accessor)."""
        return self._action

    @action.setter
    def action(self, value: Optional["FirewallActionEnum"]) -> None:
        """
        Set action with validation.
        
        Args:
            value: The action to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._action = None
            return

        if not isinstance(value, FirewallActionEnum):
            raise TypeError(
                f"action must be FirewallActionEnum or None, got {type(value).__name__}"
            )
        self._action = value
        # traffic is matched.
        self._matchingEgress: List["FirewallRule"] = []

    @property
    def matching_egress(self) -> List["FirewallRule"]:
        """Get matchingEgress (Pythonic accessor)."""
        return self._matchingEgress
        # This element defines an ingress rule expression against the network traffic
                # is matched.
        # atp.
        # Status=candidate.
        self._matching: List["FirewallRule"] = []

    @property
    def matching(self) -> List["FirewallRule"]:
        """Get matching (Pythonic accessor)."""
        return self._matching

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAction(self) -> "FirewallActionEnum":
        """
        AUTOSAR-compliant getter for action.
        
        Returns:
            The action value
        
        Note:
            Delegates to action property (CODING_RULE_V2_00017)
        """
        return self.action  # Delegates to property

    def setAction(self, value: "FirewallActionEnum") -> "FirewallRuleProps":
        """
        AUTOSAR-compliant setter for action with method chaining.
        
        Args:
            value: The action to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to action property setter (gets validation automatically)
        """
        self.action = value  # Delegates to property setter
        return self

    def getMatchingEgress(self) -> List["FirewallRule"]:
        """
        AUTOSAR-compliant getter for matchingEgress.
        
        Returns:
            The matchingEgress value
        
        Note:
            Delegates to matching_egress property (CODING_RULE_V2_00017)
        """
        return self.matching_egress  # Delegates to property

    def getMatching(self) -> List["FirewallRule"]:
        """
        AUTOSAR-compliant getter for matching.
        
        Returns:
            The matching value
        
        Note:
            Delegates to matching property (CODING_RULE_V2_00017)
        """
        return self.matching  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_action(self, value: Optional["FirewallActionEnum"]) -> "FirewallRuleProps":
        """
        Set action and return self for chaining.
        
        Args:
            value: The action to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_action("value")
        """
        self.action = value  # Use property setter (gets validation)
        return self



class FirewallRule(ARElement):
    """
    Firewall Rule that defines the control information in individual packets.
    
    Package: M2::AUTOSARTemplates::AdaptivePlatform::PlatformModuleDeployment::Firewall::FirewallRule
    
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

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"bucketSize must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._bucketSize = value
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

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"refillAmount must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._refillAmount = value
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
