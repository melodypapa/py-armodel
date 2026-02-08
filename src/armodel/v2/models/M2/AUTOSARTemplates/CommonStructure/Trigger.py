from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    MultidimensionalTime,
    SwImplPolicyEnum,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class Trigger(Identifiable):
    """
    A trigger which is provided (i.e. released) or required (i.e. used to
    activate something) in the given context.

    Package: M2::AUTOSARTemplates::CommonStructure::TriggerDeclaration::Trigger

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 45, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 109, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2076, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 255, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute, when set to value queued, allows for a of Triggers.
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
        # Optional definition of a period in case of a periodically angle) driven
        # external trigger.
        self._triggerPeriod: Optional["MultidimensionalTime"] = None

    @property
    def trigger_period(self) -> Optional["MultidimensionalTime"]:
        """Get triggerPeriod (Pythonic accessor)."""
        return self._triggerPeriod

    @trigger_period.setter
    def trigger_period(self, value: Optional["MultidimensionalTime"]) -> None:
        """
        Set triggerPeriod with validation.

        Args:
            value: The triggerPeriod to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._triggerPeriod = None
            return

        if not isinstance(value, MultidimensionalTime):
            raise TypeError(
                f"triggerPeriod must be MultidimensionalTime or None, got {type(value).__name__}"
            )
        self._triggerPeriod = value

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

    def setSwImplPolicy(self, value: "SwImplPolicyEnum") -> "Trigger":
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

    def getTriggerPeriod(self) -> "MultidimensionalTime":
        """
        AUTOSAR-compliant getter for triggerPeriod.

        Returns:
            The triggerPeriod value

        Note:
            Delegates to trigger_period property (CODING_RULE_V2_00017)
        """
        return self.trigger_period  # Delegates to property

    def setTriggerPeriod(self, value: "MultidimensionalTime") -> "Trigger":
        """
        AUTOSAR-compliant setter for triggerPeriod with method chaining.

        Args:
            value: The triggerPeriod to set

        Returns:
            self for method chaining

        Note:
            Delegates to trigger_period property setter (gets validation automatically)
        """
        self.trigger_period = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_sw_impl_policy(self, value: Optional["SwImplPolicyEnum"]) -> "Trigger":
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

    def with_trigger_period(self, value: Optional["MultidimensionalTime"]) -> "Trigger":
        """
        Set triggerPeriod and return self for chaining.

        Args:
            value: The triggerPeriod to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_trigger_period("value")
        """
        self.trigger_period = value  # Use property setter (gets validation)
        return self
