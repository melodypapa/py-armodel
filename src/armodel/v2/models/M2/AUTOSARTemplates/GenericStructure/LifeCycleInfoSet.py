from typing import (
    List,
    Optional,
)

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    ARElement,
)


class LifeCycleInfoSet(ARElement):
    """
    This meta class represents the ability to attach a life cycle information to
    a particular set of elements. The information can be defined for a
    particular period. This supports the definition of transition plans. If no
    period is specified, the life cycle state applies forever.

    Package: M2::AUTOSARTemplates::GenericStructure::LifeCycles

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 391, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 195, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This denotes the default life cycle state.
        # To be used in all within the LifeCycleInfoSet if no state is stated there
                # explicitly.
        # I.
        # e.
        # the defaultLc be overwritten in LifeCycleInfo elements.
        self._defaultLcState: "LifeCycleState" = None

    @property
    def default_lc_state(self) -> "LifeCycleState":
        """Get defaultLcState (Pythonic accessor)."""
        return self._defaultLcState

    @default_lc_state.setter
    def default_lc_state(self, value: "LifeCycleState") -> None:
        """
        Set defaultLcState with validation.

        Args:
            value: The defaultLcState to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, LifeCycleState):
            raise TypeError(
                f"defaultLcState must be LifeCycleState, got {type(value).__name__}"
            )
        self._defaultLcState = value
        # Default expiry date, i.
        # e.
        # default end point of period for all specified lifeCycleInfo apply.
        # Note that the can be overridden for each lifeCycleInfo.
        self._defaultPeriod: Optional["LifeCyclePeriod"] = None

    @property
    def default_period(self) -> Optional["LifeCyclePeriod"]:
        """Get defaultPeriod (Pythonic accessor)."""
        return self._defaultPeriod

    @default_period.setter
    def default_period(self, value: Optional["LifeCyclePeriod"]) -> None:
        """
        Set defaultPeriod with validation.

        Args:
            value: The defaultPeriod to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._defaultPeriod = None
            return

        if not isinstance(value, LifeCyclePeriod):
            raise TypeError(
                f"defaultPeriod must be LifeCyclePeriod or None, got {type(value).__name__}"
            )
        self._defaultPeriod = value
        # This represents one particular life cycle information.
        self._lifeCycleInfo: List["LifeCycleInfo"] = []

    @property
    def life_cycle_info(self) -> List["LifeCycleInfo"]:
        """Get lifeCycleInfo (Pythonic accessor)."""
        return self._lifeCycleInfo
        # This denotes the life cycle states applicable to the current life cycle info
        # set.
        self._usedLifeCycle: "LifeCycleStateDefinition" = None

    @property
    def used_life_cycle(self) -> "LifeCycleStateDefinition":
        """Get usedLifeCycle (Pythonic accessor)."""
        return self._usedLifeCycle

    @used_life_cycle.setter
    def used_life_cycle(self, value: "LifeCycleStateDefinition") -> None:
        """
        Set usedLifeCycle with validation.

        Args:
            value: The usedLifeCycle to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, LifeCycleStateDefinition):
            raise TypeError(
                f"usedLifeCycle must be LifeCycleStateDefinition, got {type(value).__name__}"
            )
        self._usedLifeCycle = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDefaultLcState(self) -> "LifeCycleState":
        """
        AUTOSAR-compliant getter for defaultLcState.

        Returns:
            The defaultLcState value

        Note:
            Delegates to default_lc_state property (CODING_RULE_V2_00017)
        """
        return self.default_lc_state  # Delegates to property

    def setDefaultLcState(self, value: "LifeCycleState") -> "LifeCycleInfoSet":
        """
        AUTOSAR-compliant setter for defaultLcState with method chaining.

        Args:
            value: The defaultLcState to set

        Returns:
            self for method chaining

        Note:
            Delegates to default_lc_state property setter (gets validation automatically)
        """
        self.default_lc_state = value  # Delegates to property setter
        return self

    def getDefaultPeriod(self) -> "LifeCyclePeriod":
        """
        AUTOSAR-compliant getter for defaultPeriod.

        Returns:
            The defaultPeriod value

        Note:
            Delegates to default_period property (CODING_RULE_V2_00017)
        """
        return self.default_period  # Delegates to property

    def setDefaultPeriod(self, value: "LifeCyclePeriod") -> "LifeCycleInfoSet":
        """
        AUTOSAR-compliant setter for defaultPeriod with method chaining.

        Args:
            value: The defaultPeriod to set

        Returns:
            self for method chaining

        Note:
            Delegates to default_period property setter (gets validation automatically)
        """
        self.default_period = value  # Delegates to property setter
        return self

    def getLifeCycleInfo(self) -> List["LifeCycleInfo"]:
        """
        AUTOSAR-compliant getter for lifeCycleInfo.

        Returns:
            The lifeCycleInfo value

        Note:
            Delegates to life_cycle_info property (CODING_RULE_V2_00017)
        """
        return self.life_cycle_info  # Delegates to property

    def getUsedLifeCycle(self) -> "LifeCycleStateDefinition":
        """
        AUTOSAR-compliant getter for usedLifeCycle.

        Returns:
            The usedLifeCycle value

        Note:
            Delegates to used_life_cycle property (CODING_RULE_V2_00017)
        """
        return self.used_life_cycle  # Delegates to property

    def setUsedLifeCycle(self, value: "LifeCycleStateDefinition") -> "LifeCycleInfoSet":
        """
        AUTOSAR-compliant setter for usedLifeCycle with method chaining.

        Args:
            value: The usedLifeCycle to set

        Returns:
            self for method chaining

        Note:
            Delegates to used_life_cycle property setter (gets validation automatically)
        """
        self.used_life_cycle = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_default_lc_state(self, value: "LifeCycleState") -> "LifeCycleInfoSet":
        """
        Set defaultLcState and return self for chaining.

        Args:
            value: The defaultLcState to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_default_lc_state("value")
        """
        self.default_lc_state = value  # Use property setter (gets validation)
        return self

    def with_default_period(self, value: Optional["LifeCyclePeriod"]) -> "LifeCycleInfoSet":
        """
        Set defaultPeriod and return self for chaining.

        Args:
            value: The defaultPeriod to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_default_period("value")
        """
        self.default_period = value  # Use property setter (gets validation)
        return self

    def with_used_life_cycle(self, value: "LifeCycleStateDefinition") -> "LifeCycleInfoSet":
        """
        Set usedLifeCycle and return self for chaining.

        Args:
            value: The usedLifeCycle to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_used_life_cycle("value")
        """
        self.used_life_cycle = value  # Use property setter (gets validation)
        return self
