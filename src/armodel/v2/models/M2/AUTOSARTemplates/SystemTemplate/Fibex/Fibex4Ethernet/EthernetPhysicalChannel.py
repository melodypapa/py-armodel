from typing import List, Optional
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import PhysicalChannel


class EthernetPhysicalChannel(PhysicalChannel):
    """
    The EthernetPhysicalChannel represents a VLAN or an untagged channel. An
    untagged channel is modeled as an EthernetPhysicalChannel without an
    aggregated VLAN.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::EthernetPhysicalChannel

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 314, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 105, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Collection of NetworkEndpoints that are used in the VLan.
        # atpSplitable.
        self._network: List["NetworkEndpoint"] = []

    @property
    def network(self) -> List["NetworkEndpoint"]:
        """Get network (Pythonic accessor)."""
        return self._network
        # SoAd Configuration for one specific Physical Channel.
        self._soAdConfig: Optional["SoAdConfig"] = None

    @property
    def so_ad_config(self) -> Optional["SoAdConfig"]:
        """Get soAdConfig (Pythonic accessor)."""
        return self._soAdConfig

    @so_ad_config.setter
    def so_ad_config(self, value: Optional["SoAdConfig"]) -> None:
        """
        Set soAdConfig with validation.

        Args:
            value: The soAdConfig to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._soAdConfig = None
            return

        if not isinstance(value, SoAdConfig):
            raise TypeError(
                f"soAdConfig must be SoAdConfig or None, got {type(value).__name__}"
            )
        self._soAdConfig = value
        # VLAN Configuration.
        self._vlan: Optional["VlanConfig"] = None

    @property
    def vlan(self) -> Optional["VlanConfig"]:
        """Get vlan (Pythonic accessor)."""
        return self._vlan

    @vlan.setter
    def vlan(self, value: Optional["VlanConfig"]) -> None:
        """
        Set vlan with validation.

        Args:
            value: The vlan to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._vlan = None
            return

        if not isinstance(value, VlanConfig):
            raise TypeError(
                f"vlan must be VlanConfig or None, got {type(value).__name__}"
            )
        self._vlan = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getNetwork(self) -> List["NetworkEndpoint"]:
        """
        AUTOSAR-compliant getter for network.

        Returns:
            The network value

        Note:
            Delegates to network property (CODING_RULE_V2_00017)
        """
        return self.network  # Delegates to property

    def getSoAdConfig(self) -> "SoAdConfig":
        """
        AUTOSAR-compliant getter for soAdConfig.

        Returns:
            The soAdConfig value

        Note:
            Delegates to so_ad_config property (CODING_RULE_V2_00017)
        """
        return self.so_ad_config  # Delegates to property

    def setSoAdConfig(self, value: "SoAdConfig") -> "EthernetPhysicalChannel":
        """
        AUTOSAR-compliant setter for soAdConfig with method chaining.

        Args:
            value: The soAdConfig to set

        Returns:
            self for method chaining

        Note:
            Delegates to so_ad_config property setter (gets validation automatically)
        """
        self.so_ad_config = value  # Delegates to property setter
        return self

    def getVlan(self) -> "VlanConfig":
        """
        AUTOSAR-compliant getter for vlan.

        Returns:
            The vlan value

        Note:
            Delegates to vlan property (CODING_RULE_V2_00017)
        """
        return self.vlan  # Delegates to property

    def setVlan(self, value: "VlanConfig") -> "EthernetPhysicalChannel":
        """
        AUTOSAR-compliant setter for vlan with method chaining.

        Args:
            value: The vlan to set

        Returns:
            self for method chaining

        Note:
            Delegates to vlan property setter (gets validation automatically)
        """
        self.vlan = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_so_ad_config(self, value: Optional["SoAdConfig"]) -> "EthernetPhysicalChannel":
        """
        Set soAdConfig and return self for chaining.

        Args:
            value: The soAdConfig to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_so_ad_config("value")
        """
        self.so_ad_config = value  # Use property setter (gets validation)
        return self

    def with_vlan(self, value: Optional["VlanConfig"]) -> "EthernetPhysicalChannel":
        """
        Set vlan and return self for chaining.

        Args:
            value: The vlan to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_vlan("value")
        """
        self.vlan = value  # Use property setter (gets validation)
        return self
