from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class BswInternalTriggeringPoint(Identifiable):
    """
    Represents the activation point for one or more
    BswInternalTriggerOccurredEvents.

    Package: M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior::BswInternalTriggeringPoint

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 91, Classic
      Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute, when set to value queued, specifies a of the internal trigger
        # event.
        self._swImplPolicy: Optional["SwImplPolicyEnum"] = None

    @property
    def sw_impl_policy(self) -> Optional["SwImplPolicyEnum"]:
        """Get swImplPolicy (Pythonic accessor)."""
        return self._swImplPolicy

    @sw_impl_policy.setter
    def sw_impl_policy(self, value: Optional["SwImplPolicyEnum"]) -> None:
        """
        Set swImplPolicy with validation.

        Args:
            value: The swImplPolicy to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._swImplPolicy = None
            return

        if not isinstance(value, SwImplPolicyEnum):
            raise TypeError(
                f"swImplPolicy must be SwImplPolicyEnum or None, got {type(value).__name__}"
            )
        self._swImplPolicy = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getSwImplPolicy(self) -> "SwImplPolicyEnum":
        """
        AUTOSAR-compliant getter for swImplPolicy.

        Returns:
            The swImplPolicy value

        Note:
            Delegates to sw_impl_policy property (CODING_RULE_V2_00017)
        """
        return self.sw_impl_policy  # Delegates to property

    def setSwImplPolicy(self, value: "SwImplPolicyEnum") -> "BswInternalTriggeringPoint":
        """
        AUTOSAR-compliant setter for swImplPolicy with method chaining.

        Args:
            value: The swImplPolicy to set

        Returns:
            self for method chaining

        Note:
            Delegates to sw_impl_policy property setter (gets validation automatically)
        """
        self.sw_impl_policy = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_sw_impl_policy(self, value: Optional["SwImplPolicyEnum"]) -> "BswInternalTriggeringPoint":
        """
        Set swImplPolicy and return self for chaining.

        Args:
            value: The swImplPolicy to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sw_impl_policy("value")
        """
        self.sw_impl_policy = value  # Use property setter (gets validation)
        return self
