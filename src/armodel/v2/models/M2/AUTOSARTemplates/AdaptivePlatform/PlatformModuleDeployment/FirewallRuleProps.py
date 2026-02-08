from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates import FirewallActionEnum
from armodel.v2.models.M2.AUTOSARTemplates.AdaptivePlatform.PlatformModuleDeployment.Firewall.FirewallRule import (
    FirewallRule,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


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
        # This element defines an egress rule expression against which the network
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
