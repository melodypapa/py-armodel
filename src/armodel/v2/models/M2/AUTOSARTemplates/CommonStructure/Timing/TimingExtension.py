from abc import ABC
from typing import List, Optional


class TimingExtension(ARElement, ABC):
    """
    The abstract parent class of the different template specific timing
    extensions. Depending on the specific timing extension the timing
    descriptions and timing constraints, that can be used to specify the timing
    behavior, are restricted.

    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingExtensions::TimingExtension

    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 254, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is TimingExtension:
            raise TypeError("TimingExtension is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # A list of accuracies - which may be used to specify synchronizations from one
        # model clock to another model atpVariation.
        self._timingClock: List["TimingClockSync"] = []

    @property
    def timing_clock(self) -> List["TimingClockSync"]:
        """Get timingClock (Pythonic accessor)."""
        return self._timingClock
        # The timing condition specifies a specific condition.
        # atpVariation 277 Document ID 411: AUTOSAR_CP_TPS_TimingExtensions Timing
                # Extensions for Classic R23-11.
        self._timingCondition: List["TimingCondition"] = []

    @property
    def timing_condition(self) -> List["TimingCondition"]:
        """Get timingCondition (Pythonic accessor)."""
        return self._timingCondition
        # The timing constraints that belong to a specific timing in the role of a
                # timing requirement.
        # to support different timing constraint variants timing specification, the
                # aggregation is marked stereotype "atpVariation".
        # atpVariation.
        self._timing: List["TimingConstraint"] = []

    @property
    def timing(self) -> List["TimingConstraint"]:
        """Get timing (Pythonic accessor)."""
        return self._timing
        # The timing resource contains all instance references from within a timing
        # condition formula of a timing.
        self._timingResource: Optional["TimingExtension"] = None

    @property
    def timing_resource(self) -> Optional["TimingExtension"]:
        """Get timingResource (Pythonic accessor)."""
        return self._timingResource

    @timing_resource.setter
    def timing_resource(self, value: Optional["TimingExtension"]) -> None:
        """
        Set timingResource with validation.

        Args:
            value: The timingResource to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timingResource = None
            return

        if not isinstance(value, TimingExtension):
            raise TypeError(
                f"timingResource must be TimingExtension or None, got {type(value).__name__}"
            )
        self._timingResource = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTimingClock(self) -> List["TimingClockSync"]:
        """
        AUTOSAR-compliant getter for timingClock.

        Returns:
            The timingClock value

        Note:
            Delegates to timing_clock property (CODING_RULE_V2_00017)
        """
        return self.timing_clock  # Delegates to property

    def getTimingCondition(self) -> List["TimingCondition"]:
        """
        AUTOSAR-compliant getter for timingCondition.

        Returns:
            The timingCondition value

        Note:
            Delegates to timing_condition property (CODING_RULE_V2_00017)
        """
        return self.timing_condition  # Delegates to property

    def getTiming(self) -> List["TimingConstraint"]:
        """
        AUTOSAR-compliant getter for timing.

        Returns:
            The timing value

        Note:
            Delegates to timing property (CODING_RULE_V2_00017)
        """
        return self.timing  # Delegates to property

    def getTimingResource(self) -> "TimingExtension":
        """
        AUTOSAR-compliant getter for timingResource.

        Returns:
            The timingResource value

        Note:
            Delegates to timing_resource property (CODING_RULE_V2_00017)
        """
        return self.timing_resource  # Delegates to property

    def setTimingResource(self, value: "TimingExtension") -> "TimingExtension":
        """
        AUTOSAR-compliant setter for timingResource with method chaining.

        Args:
            value: The timingResource to set

        Returns:
            self for method chaining

        Note:
            Delegates to timing_resource property setter (gets validation automatically)
        """
        self.timing_resource = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_timing_resource(self, value: Optional["TimingExtension"]) -> "TimingExtension":
        """
        Set timingResource and return self for chaining.

        Args:
            value: The timingResource to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_timing_resource("value")
        """
        self.timing_resource = value  # Use property setter (gets validation)
        return self
