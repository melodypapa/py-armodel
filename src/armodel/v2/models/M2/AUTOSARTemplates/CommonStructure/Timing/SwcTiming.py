from typing import Optional
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingExtensions import TimingExtension


class SwcTiming(TimingExtension):
    """
    The SwcTiming is used to describe the timing of an atomic software
    component. TimingDescriptions aggregated by SwcTiming are restricted to
    event chains referring to events which are derived from the classes
    TDEventVfb and TDEventSwcInternalBehavior.

    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingExtensions::SwcTiming

    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 25, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This defines the scope of a SwcTiming.
        # All corresponding and constraints shall be defined within reason for the
                # cardinality of 0.
        # 1 is to ensure.
        self._behavior: Optional["SwcInternalBehavior"] = None

    @property
    def behavior(self) -> Optional["SwcInternalBehavior"]:
        """Get behavior (Pythonic accessor)."""
        return self._behavior

    @behavior.setter
    def behavior(self, value: Optional["SwcInternalBehavior"]) -> None:
        """
        Set behavior with validation.

        Args:
            value: The behavior to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._behavior = None
            return

        if not isinstance(value, SwcInternalBehavior):
            raise TypeError(
                f"behavior must be SwcInternalBehavior or None, got {type(value).__name__}"
            )
        self._behavior = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBehavior(self) -> "SwcInternalBehavior":
        """
        AUTOSAR-compliant getter for behavior.

        Returns:
            The behavior value

        Note:
            Delegates to behavior property (CODING_RULE_V2_00017)
        """
        return self.behavior  # Delegates to property

    def setBehavior(self, value: "SwcInternalBehavior") -> "SwcTiming":
        """
        AUTOSAR-compliant setter for behavior with method chaining.

        Args:
            value: The behavior to set

        Returns:
            self for method chaining

        Note:
            Delegates to behavior property setter (gets validation automatically)
        """
        self.behavior = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_behavior(self, value: Optional["SwcInternalBehavior"]) -> "SwcTiming":
        """
        Set behavior and return self for chaining.

        Args:
            value: The behavior to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_behavior("value")
        """
        self.behavior = value  # Use property setter (gets validation)
        return self
