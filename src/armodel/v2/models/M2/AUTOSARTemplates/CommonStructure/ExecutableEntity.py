from abc import ABC
from typing import (
    List,
    Optional,
)

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class ExecutableEntity(Identifiable, ABC):
    """
    Abstraction of executable code.

    Package: M2::AUTOSARTemplates::CommonStructure::InternalBehavior

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 70, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 538, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2024, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 222, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is ExecutableEntity:
            raise TypeError("ExecutableEntity is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # If the ExecutableEntity provides at least one activation Reason element the
                # RTE resp.
        # BSW Scheduler shall to read the activation vector of this execution.
        # activationReason element is provided the feature of to determine the
                # activating RTEEvent is this ExecutableEntity.
        self._activation: List["ExecutableEntity"] = []

    @property
    def activation(self) -> List["ExecutableEntity"]:
        """Get activation (Pythonic accessor)."""
        return self._activation
        # This means that the executable entity can enter/leave the area through
                # explicit API calls.
        # atpVariation.
        self._canEnter: List["ExclusiveArea"] = []

    @property
    def can_enter(self) -> List["ExclusiveArea"]:
        """Get canEnter (Pythonic accessor)."""
        return self._canEnter
        # This represents the set of ExclusiveAreaNestingOrders recognized by this
        # ExecutableEntity.
        self._exclusiveArea: List["ExclusiveAreaNesting"] = []

    @property
    def exclusive_area(self) -> List["ExclusiveAreaNesting"]:
        """Get exclusiveArea (Pythonic accessor)."""
        return self._exclusiveArea
        # Specifies the time in seconds by which two consecutive of an ExecutableEntity
        # are guaranteed to be.
        self._minimumStart: Optional["TimeValue"] = None

    @property
    def minimum_start(self) -> Optional["TimeValue"]:
        """Get minimumStart (Pythonic accessor)."""
        return self._minimumStart

    @minimum_start.setter
    def minimum_start(self, value: Optional["TimeValue"]) -> None:
        """
        Set minimumStart with validation.

        Args:
            value: The minimumStart to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._minimumStart = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"minimumStart must be TimeValue or None, got {type(value).__name__}"
            )
        self._minimumStart = value
        # The reentrancy level of this ExecutableEntity.
        # See the the enumeration type ReentrancyLevel details.
        # that nonReentrant interfaces can have also multicoreReentrant
                # implementations, and can also have multicoreReentrant.
        self._reentrancyLevel: Optional["ReentrancyLevelEnum"] = None

    @property
    def reentrancy_level(self) -> Optional["ReentrancyLevelEnum"]:
        """Get reentrancyLevel (Pythonic accessor)."""
        return self._reentrancyLevel

    @reentrancy_level.setter
    def reentrancy_level(self, value: Optional["ReentrancyLevelEnum"]) -> None:
        """
        Set reentrancyLevel with validation.

        Args:
            value: The reentrancyLevel to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._reentrancyLevel = None
            return

        if not isinstance(value, ReentrancyLevelEnum):
            raise TypeError(
                f"reentrancyLevel must be ReentrancyLevelEnum or None, got {type(value).__name__}"
            )
        self._reentrancyLevel = value
        # The executable entity runs completely inside the area.
        # atpVariation.
        self._runsInside: List["ExclusiveArea"] = []

    @property
    def runs_inside(self) -> List["ExclusiveArea"]:
        """Get runsInside (Pythonic accessor)."""
        return self._runsInside
        # Addressing method related to this code entity.
        # Via an the same SwAddrMethod, it can be several code entities (even of
                # different components) shall be located in the same already specifying the
                # memory section.
        self._swAddrMethod: Optional["SwAddrMethod"] = None

    @property
    def sw_addr_method(self) -> Optional["SwAddrMethod"]:
        """Get swAddrMethod (Pythonic accessor)."""
        return self._swAddrMethod

    @sw_addr_method.setter
    def sw_addr_method(self, value: Optional["SwAddrMethod"]) -> None:
        """
        Set swAddrMethod with validation.

        Args:
            value: The swAddrMethod to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._swAddrMethod = None
            return

        if not isinstance(value, SwAddrMethod):
            raise TypeError(
                f"swAddrMethod must be SwAddrMethod or None, got {type(value).__name__}"
            )
        self._swAddrMethod = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getActivation(self) -> List["ExecutableEntity"]:
        """
        AUTOSAR-compliant getter for activation.

        Returns:
            The activation value

        Note:
            Delegates to activation property (CODING_RULE_V2_00017)
        """
        return self.activation  # Delegates to property

    def getCanEnter(self) -> List["ExclusiveArea"]:
        """
        AUTOSAR-compliant getter for canEnter.

        Returns:
            The canEnter value

        Note:
            Delegates to can_enter property (CODING_RULE_V2_00017)
        """
        return self.can_enter  # Delegates to property

    def getExclusiveArea(self) -> List["ExclusiveAreaNesting"]:
        """
        AUTOSAR-compliant getter for exclusiveArea.

        Returns:
            The exclusiveArea value

        Note:
            Delegates to exclusive_area property (CODING_RULE_V2_00017)
        """
        return self.exclusive_area  # Delegates to property

    def getMinimumStart(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for minimumStart.

        Returns:
            The minimumStart value

        Note:
            Delegates to minimum_start property (CODING_RULE_V2_00017)
        """
        return self.minimum_start  # Delegates to property

    def setMinimumStart(self, value: "TimeValue") -> "ExecutableEntity":
        """
        AUTOSAR-compliant setter for minimumStart with method chaining.

        Args:
            value: The minimumStart to set

        Returns:
            self for method chaining

        Note:
            Delegates to minimum_start property setter (gets validation automatically)
        """
        self.minimum_start = value  # Delegates to property setter
        return self

    def getReentrancyLevel(self) -> "ReentrancyLevelEnum":
        """
        AUTOSAR-compliant getter for reentrancyLevel.

        Returns:
            The reentrancyLevel value

        Note:
            Delegates to reentrancy_level property (CODING_RULE_V2_00017)
        """
        return self.reentrancy_level  # Delegates to property

    def setReentrancyLevel(self, value: "ReentrancyLevelEnum") -> "ExecutableEntity":
        """
        AUTOSAR-compliant setter for reentrancyLevel with method chaining.

        Args:
            value: The reentrancyLevel to set

        Returns:
            self for method chaining

        Note:
            Delegates to reentrancy_level property setter (gets validation automatically)
        """
        self.reentrancy_level = value  # Delegates to property setter
        return self

    def getRunsInside(self) -> List["ExclusiveArea"]:
        """
        AUTOSAR-compliant getter for runsInside.

        Returns:
            The runsInside value

        Note:
            Delegates to runs_inside property (CODING_RULE_V2_00017)
        """
        return self.runs_inside  # Delegates to property

    def getSwAddrMethod(self) -> "SwAddrMethod":
        """
        AUTOSAR-compliant getter for swAddrMethod.

        Returns:
            The swAddrMethod value

        Note:
            Delegates to sw_addr_method property (CODING_RULE_V2_00017)
        """
        return self.sw_addr_method  # Delegates to property

    def setSwAddrMethod(self, value: "SwAddrMethod") -> "ExecutableEntity":
        """
        AUTOSAR-compliant setter for swAddrMethod with method chaining.

        Args:
            value: The swAddrMethod to set

        Returns:
            self for method chaining

        Note:
            Delegates to sw_addr_method property setter (gets validation automatically)
        """
        self.sw_addr_method = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_minimum_start(self, value: Optional["TimeValue"]) -> "ExecutableEntity":
        """
        Set minimumStart and return self for chaining.

        Args:
            value: The minimumStart to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_minimum_start("value")
        """
        self.minimum_start = value  # Use property setter (gets validation)
        return self

    def with_reentrancy_level(self, value: Optional["ReentrancyLevelEnum"]) -> "ExecutableEntity":
        """
        Set reentrancyLevel and return self for chaining.

        Args:
            value: The reentrancyLevel to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_reentrancy_level("value")
        """
        self.reentrancy_level = value  # Use property setter (gets validation)
        return self

    def with_sw_addr_method(self, value: Optional["SwAddrMethod"]) -> "ExecutableEntity":
        """
        Set swAddrMethod and return self for chaining.

        Args:
            value: The swAddrMethod to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sw_addr_method("value")
        """
        self.sw_addr_method = value  # Use property setter (gets validation)
        return self
