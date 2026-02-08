from typing import (
    List,
    Optional,
)

from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import (
    ServiceNeeds,
)


class SupervisedEntityNeeds(ServiceNeeds):
    """
    that this value has to be recalculated with respect to the WdgM’s own cycle
    time for ECU configuration. Table 12.12: SupervisedEntityNeeds 234 of 381
    Document ID 89: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate Basic Software
    Module Description Template AUTOSAR CP R23-11

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 234, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 707, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # true/false: supervision activation status of Supervised be enabled/disabled
        # at start.
        self._activateAtStart: Optional["Boolean"] = None

    @property
    def activate_at_start(self) -> Optional["Boolean"]:
        """Get activateAtStart (Pythonic accessor)."""
        return self._activateAtStart

    @activate_at_start.setter
    def activate_at_start(self, value: Optional["Boolean"]) -> None:
        """
        Set activateAtStart with validation.

        Args:
            value: The activateAtStart to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._activateAtStart = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"activateAtStart must be Boolean or None, got {type(value).__name__}"
            )
        self._activateAtStart = value
        # This reference indicates the checkpoints belonging to the Entity.
        # atpVariation.
        self._checkpoints: List["SupervisedEntity"] = []

    @property
    def checkpoints(self) -> List["SupervisedEntity"]:
        """Get checkpoints (Pythonic accessor)."""
        return self._checkpoints
        # true: software-component shall be allowed to deactivate of this
        # SupervisedEntity shall be not allowed to of this SupervisedEntity.
        self._enable: Optional["Boolean"] = None

    @property
    def enable(self) -> Optional["Boolean"]:
        """Get enable (Pythonic accessor)."""
        return self._enable

    @enable.setter
    def enable(self, value: Optional["Boolean"]) -> None:
        """
        Set enable with validation.

        Args:
            value: The enable to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._enable = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"enable must be Boolean or None, got {type(value).__name__}"
            )
        self._enable = value
        # Expected cycle time of alive trigger of this Supervised (in seconds).
        self._expectedAlive: Optional["TimeValue"] = None

    @property
    def expected_alive(self) -> Optional["TimeValue"]:
        """Get expectedAlive (Pythonic accessor)."""
        return self._expectedAlive

    @expected_alive.setter
    def expected_alive(self, value: Optional["TimeValue"]) -> None:
        """
        Set expectedAlive with validation.

        Args:
            value: The expectedAlive to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._expectedAlive = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"expectedAlive must be TimeValue or None, got {type(value).__name__}"
            )
        self._expectedAlive = value
        # Maximum cycle time of alive trigger of this Supervised seconds).
        self._maxAliveCycle: Optional["TimeValue"] = None

    @property
    def max_alive_cycle(self) -> Optional["TimeValue"]:
        """Get maxAliveCycle (Pythonic accessor)."""
        return self._maxAliveCycle

    @max_alive_cycle.setter
    def max_alive_cycle(self, value: Optional["TimeValue"]) -> None:
        """
        Set maxAliveCycle with validation.

        Args:
            value: The maxAliveCycle to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxAliveCycle = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"maxAliveCycle must be TimeValue or None, got {type(value).__name__}"
            )
        self._maxAliveCycle = value
        # Minimum cycle time of alive trigger of this Supervised seconds).
        self._minAliveCycle: Optional["TimeValue"] = None

    @property
    def min_alive_cycle(self) -> Optional["TimeValue"]:
        """Get minAliveCycle (Pythonic accessor)."""
        return self._minAliveCycle

    @min_alive_cycle.setter
    def min_alive_cycle(self, value: Optional["TimeValue"]) -> None:
        """
        Set minAliveCycle with validation.

        Args:
            value: The minAliveCycle to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._minAliveCycle = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"minAliveCycle must be TimeValue or None, got {type(value).__name__}"
            )
        self._minAliveCycle = value
        # Number of consecutive failed alive cycles for this which shall be tolerated
        # until the of the SupervisedEntity is set to SWS WdgM for more.
        self._toleratedFailed: Optional["PositiveInteger"] = None

    @property
    def tolerated_failed(self) -> Optional["PositiveInteger"]:
        """Get toleratedFailed (Pythonic accessor)."""
        return self._toleratedFailed

    @tolerated_failed.setter
    def tolerated_failed(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set toleratedFailed with validation.

        Args:
            value: The toleratedFailed to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._toleratedFailed = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"toleratedFailed must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._toleratedFailed = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getActivateAtStart(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for activateAtStart.

        Returns:
            The activateAtStart value

        Note:
            Delegates to activate_at_start property (CODING_RULE_V2_00017)
        """
        return self.activate_at_start  # Delegates to property

    def setActivateAtStart(self, value: "Boolean") -> "SupervisedEntityNeeds":
        """
        AUTOSAR-compliant setter for activateAtStart with method chaining.

        Args:
            value: The activateAtStart to set

        Returns:
            self for method chaining

        Note:
            Delegates to activate_at_start property setter (gets validation automatically)
        """
        self.activate_at_start = value  # Delegates to property setter
        return self

    def getCheckpoints(self) -> List["SupervisedEntity"]:
        """
        AUTOSAR-compliant getter for checkpoints.

        Returns:
            The checkpoints value

        Note:
            Delegates to checkpoints property (CODING_RULE_V2_00017)
        """
        return self.checkpoints  # Delegates to property

    def getEnable(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for enable.

        Returns:
            The enable value

        Note:
            Delegates to enable property (CODING_RULE_V2_00017)
        """
        return self.enable  # Delegates to property

    def setEnable(self, value: "Boolean") -> "SupervisedEntityNeeds":
        """
        AUTOSAR-compliant setter for enable with method chaining.

        Args:
            value: The enable to set

        Returns:
            self for method chaining

        Note:
            Delegates to enable property setter (gets validation automatically)
        """
        self.enable = value  # Delegates to property setter
        return self

    def getExpectedAlive(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for expectedAlive.

        Returns:
            The expectedAlive value

        Note:
            Delegates to expected_alive property (CODING_RULE_V2_00017)
        """
        return self.expected_alive  # Delegates to property

    def setExpectedAlive(self, value: "TimeValue") -> "SupervisedEntityNeeds":
        """
        AUTOSAR-compliant setter for expectedAlive with method chaining.

        Args:
            value: The expectedAlive to set

        Returns:
            self for method chaining

        Note:
            Delegates to expected_alive property setter (gets validation automatically)
        """
        self.expected_alive = value  # Delegates to property setter
        return self

    def getMaxAliveCycle(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for maxAliveCycle.

        Returns:
            The maxAliveCycle value

        Note:
            Delegates to max_alive_cycle property (CODING_RULE_V2_00017)
        """
        return self.max_alive_cycle  # Delegates to property

    def setMaxAliveCycle(self, value: "TimeValue") -> "SupervisedEntityNeeds":
        """
        AUTOSAR-compliant setter for maxAliveCycle with method chaining.

        Args:
            value: The maxAliveCycle to set

        Returns:
            self for method chaining

        Note:
            Delegates to max_alive_cycle property setter (gets validation automatically)
        """
        self.max_alive_cycle = value  # Delegates to property setter
        return self

    def getMinAliveCycle(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for minAliveCycle.

        Returns:
            The minAliveCycle value

        Note:
            Delegates to min_alive_cycle property (CODING_RULE_V2_00017)
        """
        return self.min_alive_cycle  # Delegates to property

    def setMinAliveCycle(self, value: "TimeValue") -> "SupervisedEntityNeeds":
        """
        AUTOSAR-compliant setter for minAliveCycle with method chaining.

        Args:
            value: The minAliveCycle to set

        Returns:
            self for method chaining

        Note:
            Delegates to min_alive_cycle property setter (gets validation automatically)
        """
        self.min_alive_cycle = value  # Delegates to property setter
        return self

    def getToleratedFailed(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for toleratedFailed.

        Returns:
            The toleratedFailed value

        Note:
            Delegates to tolerated_failed property (CODING_RULE_V2_00017)
        """
        return self.tolerated_failed  # Delegates to property

    def setToleratedFailed(self, value: "PositiveInteger") -> "SupervisedEntityNeeds":
        """
        AUTOSAR-compliant setter for toleratedFailed with method chaining.

        Args:
            value: The toleratedFailed to set

        Returns:
            self for method chaining

        Note:
            Delegates to tolerated_failed property setter (gets validation automatically)
        """
        self.tolerated_failed = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_activate_at_start(self, value: Optional["Boolean"]) -> "SupervisedEntityNeeds":
        """
        Set activateAtStart and return self for chaining.

        Args:
            value: The activateAtStart to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_activate_at_start("value")
        """
        self.activate_at_start = value  # Use property setter (gets validation)
        return self

    def with_enable(self, value: Optional["Boolean"]) -> "SupervisedEntityNeeds":
        """
        Set enable and return self for chaining.

        Args:
            value: The enable to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_enable("value")
        """
        self.enable = value  # Use property setter (gets validation)
        return self

    def with_expected_alive(self, value: Optional["TimeValue"]) -> "SupervisedEntityNeeds":
        """
        Set expectedAlive and return self for chaining.

        Args:
            value: The expectedAlive to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_expected_alive("value")
        """
        self.expected_alive = value  # Use property setter (gets validation)
        return self

    def with_max_alive_cycle(self, value: Optional["TimeValue"]) -> "SupervisedEntityNeeds":
        """
        Set maxAliveCycle and return self for chaining.

        Args:
            value: The maxAliveCycle to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_max_alive_cycle("value")
        """
        self.max_alive_cycle = value  # Use property setter (gets validation)
        return self

    def with_min_alive_cycle(self, value: Optional["TimeValue"]) -> "SupervisedEntityNeeds":
        """
        Set minAliveCycle and return self for chaining.

        Args:
            value: The minAliveCycle to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_min_alive_cycle("value")
        """
        self.min_alive_cycle = value  # Use property setter (gets validation)
        return self

    def with_tolerated_failed(self, value: Optional["PositiveInteger"]) -> "SupervisedEntityNeeds":
        """
        Set toleratedFailed and return self for chaining.

        Args:
            value: The toleratedFailed to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tolerated_failed("value")
        """
        self.tolerated_failed = value  # Use property setter (gets validation)
        return self
