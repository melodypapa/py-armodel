from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class NetworkEndpoint(Identifiable):
    """
    The network endpoint defines the network addressing (e.g. IP-Address or MAC
    multicast address).
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::NetworkEndpoint
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 463, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Defines the fully qualified domain name (FQDN) e.
        # g.
        self._fullyQualified: Optional["String"] = None

    @property
    def fully_qualified(self) -> Optional["String"]:
        """Get fullyQualified (Pythonic accessor)."""
        return self._fullyQualified

    @fully_qualified.setter
    def fully_qualified(self, value: Optional["String"]) -> None:
        """
        Set fullyQualified with validation.
        
        Args:
            value: The fullyQualified to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._fullyQualified = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"fullyQualified must be String or None, got {type(value).__name__}"
            )
        self._fullyQualified = value
        # Defines the network infrastructure services provided or.
        self._infrastructure: Optional["InfrastructureServices"] = None

    @property
    def infrastructure(self) -> Optional["InfrastructureServices"]:
        """Get infrastructure (Pythonic accessor)."""
        return self._infrastructure

    @infrastructure.setter
    def infrastructure(self, value: Optional["InfrastructureServices"]) -> None:
        """
        Set infrastructure with validation.
        
        Args:
            value: The infrastructure to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._infrastructure = None
            return

        if not isinstance(value, InfrastructureServices):
            raise TypeError(
                f"infrastructure must be InfrastructureServices or None, got {type(value).__name__}"
            )
        self._infrastructure = value
        # Optional IPSec configuration that provides security IP packets.
        self._ipSecConfig: Optional["IPSecConfig"] = None

    @property
    def ip_sec_config(self) -> Optional["IPSecConfig"]:
        """Get ipSecConfig (Pythonic accessor)."""
        return self._ipSecConfig

    @ip_sec_config.setter
    def ip_sec_config(self, value: Optional["IPSecConfig"]) -> None:
        """
        Set ipSecConfig with validation.
        
        Args:
            value: The ipSecConfig to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ipSecConfig = None
            return

        if not isinstance(value, IPSecConfig):
            raise TypeError(
                f"ipSecConfig must be IPSecConfig or None, got {type(value).__name__}"
            )
        self._ipSecConfig = value
        # Definition of a Network Address.
        # Tags: xml.
        # name Address Plural=NETWORK-ENDPOINT-ADDRESSES.
        self._network: List["NetworkEndpoint"] = []

    @property
    def network(self) -> List["NetworkEndpoint"]:
        """Get network (Pythonic accessor)."""
        return self._network
        # Defines the frame priority where values from 0 (best 7 (highest) are allowed.
        self._priority: Optional["PositiveInteger"] = None

    @property
    def priority(self) -> Optional["PositiveInteger"]:
        """Get priority (Pythonic accessor)."""
        return self._priority

    @priority.setter
    def priority(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set priority with validation.
        
        Args:
            value: The priority to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._priority = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"priority must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._priority = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getFullyQualified(self) -> "String":
        """
        AUTOSAR-compliant getter for fullyQualified.
        
        Returns:
            The fullyQualified value
        
        Note:
            Delegates to fully_qualified property (CODING_RULE_V2_00017)
        """
        return self.fully_qualified  # Delegates to property

    def setFullyQualified(self, value: "String") -> "NetworkEndpoint":
        """
        AUTOSAR-compliant setter for fullyQualified with method chaining.
        
        Args:
            value: The fullyQualified to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to fully_qualified property setter (gets validation automatically)
        """
        self.fully_qualified = value  # Delegates to property setter
        return self

    def getInfrastructure(self) -> "InfrastructureServices":
        """
        AUTOSAR-compliant getter for infrastructure.
        
        Returns:
            The infrastructure value
        
        Note:
            Delegates to infrastructure property (CODING_RULE_V2_00017)
        """
        return self.infrastructure  # Delegates to property

    def setInfrastructure(self, value: "InfrastructureServices") -> "NetworkEndpoint":
        """
        AUTOSAR-compliant setter for infrastructure with method chaining.
        
        Args:
            value: The infrastructure to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to infrastructure property setter (gets validation automatically)
        """
        self.infrastructure = value  # Delegates to property setter
        return self

    def getIpSecConfig(self) -> "IPSecConfig":
        """
        AUTOSAR-compliant getter for ipSecConfig.
        
        Returns:
            The ipSecConfig value
        
        Note:
            Delegates to ip_sec_config property (CODING_RULE_V2_00017)
        """
        return self.ip_sec_config  # Delegates to property

    def setIpSecConfig(self, value: "IPSecConfig") -> "NetworkEndpoint":
        """
        AUTOSAR-compliant setter for ipSecConfig with method chaining.
        
        Args:
            value: The ipSecConfig to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to ip_sec_config property setter (gets validation automatically)
        """
        self.ip_sec_config = value  # Delegates to property setter
        return self

    def getNetwork(self) -> List["NetworkEndpoint"]:
        """
        AUTOSAR-compliant getter for network.
        
        Returns:
            The network value
        
        Note:
            Delegates to network property (CODING_RULE_V2_00017)
        """
        return self.network  # Delegates to property

    def getPriority(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for priority.
        
        Returns:
            The priority value
        
        Note:
            Delegates to priority property (CODING_RULE_V2_00017)
        """
        return self.priority  # Delegates to property

    def setPriority(self, value: "PositiveInteger") -> "NetworkEndpoint":
        """
        AUTOSAR-compliant setter for priority with method chaining.
        
        Args:
            value: The priority to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to priority property setter (gets validation automatically)
        """
        self.priority = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_fully_qualified(self, value: Optional["String"]) -> "NetworkEndpoint":
        """
        Set fullyQualified and return self for chaining.
        
        Args:
            value: The fullyQualified to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_fully_qualified("value")
        """
        self.fully_qualified = value  # Use property setter (gets validation)
        return self

    def with_infrastructure(self, value: Optional["InfrastructureServices"]) -> "NetworkEndpoint":
        """
        Set infrastructure and return self for chaining.
        
        Args:
            value: The infrastructure to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_infrastructure("value")
        """
        self.infrastructure = value  # Use property setter (gets validation)
        return self

    def with_ip_sec_config(self, value: Optional["IPSecConfig"]) -> "NetworkEndpoint":
        """
        Set ipSecConfig and return self for chaining.
        
        Args:
            value: The ipSecConfig to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_ip_sec_config("value")
        """
        self.ip_sec_config = value  # Use property setter (gets validation)
        return self

    def with_priority(self, value: Optional["PositiveInteger"]) -> "NetworkEndpoint":
        """
        Set priority and return self for chaining.
        
        Args:
            value: The priority to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_priority("value")
        """
        self.priority = value  # Use property setter (gets validation)
        return self