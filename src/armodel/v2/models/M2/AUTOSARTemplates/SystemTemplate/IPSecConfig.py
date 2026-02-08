from typing import (
    List,
    Optional,
)

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class IPSecConfig(ARObject):
    """
    IPsec is a protocol that is designed to provide "end-to-end"
    cryptographically-based security for IP network connections.

    Package: M2::AUTOSARTemplates::SystemTemplate::SecureCommunication

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 571, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Global IPsec configuration settings that are valid for all that are defined
        # on the NetworkEndpoint.
        self._ipSecConfig: Optional["IPSecConfigProps"] = None

    @property
    def ip_sec_config(self) -> Optional["IPSecConfigProps"]:
        """Get ipSecConfig (Pythonic accessor)."""
        return self._ipSecConfig

    @ip_sec_config.setter
    def ip_sec_config(self, value: Optional["IPSecConfigProps"]) -> None:
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

        if not isinstance(value, IPSecConfigProps):
            raise TypeError(
                f"ipSecConfig must be IPSecConfigProps or None, got {type(value).__name__}"
            )
        self._ipSecConfig = value
        # IPSec rules and filters that are defined in the IPSecConfig specific
        # NetworkEndpoint.
        self._ipSecRule: List["IPSecRule"] = []

    @property
    def ip_sec_rule(self) -> List["IPSecRule"]:
        """Get ipSecRule (Pythonic accessor)."""
        return self._ipSecRule

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getIpSecConfig(self) -> "IPSecConfigProps":
        """
        AUTOSAR-compliant getter for ipSecConfig.

        Returns:
            The ipSecConfig value

        Note:
            Delegates to ip_sec_config property (CODING_RULE_V2_00017)
        """
        return self.ip_sec_config  # Delegates to property

    def setIpSecConfig(self, value: "IPSecConfigProps") -> "IPSecConfig":
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

    def getIpSecRule(self) -> List["IPSecRule"]:
        """
        AUTOSAR-compliant getter for ipSecRule.

        Returns:
            The ipSecRule value

        Note:
            Delegates to ip_sec_rule property (CODING_RULE_V2_00017)
        """
        return self.ip_sec_rule  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_ip_sec_config(self, value: Optional["IPSecConfigProps"]) -> "IPSecConfig":
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
