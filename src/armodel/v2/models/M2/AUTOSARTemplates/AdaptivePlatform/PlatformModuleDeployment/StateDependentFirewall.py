from typing import (
    List,
    Optional,
)

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    ARElement,
)


class StateDependentFirewall(ARElement):
    """
    Firewall rules that are defined in a firewall state

    Package: M2::AUTOSARTemplates::AdaptivePlatform::PlatformModuleDeployment::Firewall

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
        # Collection of firewall rules that apply in the vehicle mode Tags: atp.
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
