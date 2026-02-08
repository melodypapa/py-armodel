from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class VlanConfig(Identifiable):
    """
    VLAN Configuration attributes

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 106, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # A VLAN is identified by this attribute according to IEEE allowed values range
                # is from 0.
        # 4095.
        self._vlanIdentifier: Optional["PositiveInteger"] = None

    @property
    def vlan_identifier(self) -> Optional["PositiveInteger"]:
        """Get vlanIdentifier (Pythonic accessor)."""
        return self._vlanIdentifier

    @vlan_identifier.setter
    def vlan_identifier(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set vlanIdentifier with validation.

        Args:
            value: The vlanIdentifier to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._vlanIdentifier = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"vlanIdentifier must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._vlanIdentifier = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getVlanIdentifier(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for vlanIdentifier.

        Returns:
            The vlanIdentifier value

        Note:
            Delegates to vlan_identifier property (CODING_RULE_V2_00017)
        """
        return self.vlan_identifier  # Delegates to property

    def setVlanIdentifier(self, value: "PositiveInteger") -> "VlanConfig":
        """
        AUTOSAR-compliant setter for vlanIdentifier with method chaining.

        Args:
            value: The vlanIdentifier to set

        Returns:
            self for method chaining

        Note:
            Delegates to vlan_identifier property setter (gets validation automatically)
        """
        self.vlan_identifier = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_vlan_identifier(self, value: Optional["PositiveInteger"]) -> "VlanConfig":
        """
        Set vlanIdentifier and return self for chaining.

        Args:
            value: The vlanIdentifier to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_vlan_identifier("value")
        """
        self.vlan_identifier = value  # Use property setter (gets validation)
        return self
