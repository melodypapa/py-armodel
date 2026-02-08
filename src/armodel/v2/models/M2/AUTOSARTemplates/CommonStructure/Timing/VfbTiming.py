from typing import Optional
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingExtensions import TimingExtension


class VfbTiming(TimingExtension):
    """
    A model element used to define timing descriptions and constraints at VFB
    level. TimingDescriptions aggregated by VfbTiming are restricted to event
    chains referring to events which are derived from the class TDEventVfb.

    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingExtensions::VfbTiming

    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 24, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 223, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This defines the scope of a VfbTiming.
        # All corresponding and constraints shall be defined within.
        self._component: Optional["SwComponentType"] = None

    @property
    def component(self) -> Optional["SwComponentType"]:
        """Get component (Pythonic accessor)."""
        return self._component

    @component.setter
    def component(self, value: Optional["SwComponentType"]) -> None:
        """
        Set component with validation.

        Args:
            value: The component to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._component = None
            return

        if not isinstance(value, SwComponentType):
            raise TypeError(
                f"component must be SwComponentType or None, got {type(value).__name__}"
            )
        self._component = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getComponent(self) -> "SwComponentType":
        """
        AUTOSAR-compliant getter for component.

        Returns:
            The component value

        Note:
            Delegates to component property (CODING_RULE_V2_00017)
        """
        return self.component  # Delegates to property

    def setComponent(self, value: "SwComponentType") -> "VfbTiming":
        """
        AUTOSAR-compliant setter for component with method chaining.

        Args:
            value: The component to set

        Returns:
            self for method chaining

        Note:
            Delegates to component property setter (gets validation automatically)
        """
        self.component = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_component(self, value: Optional["SwComponentType"]) -> "VfbTiming":
        """
        Set component and return self for chaining.

        Args:
            value: The component to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_component("value")
        """
        self.component = value  # Use property setter (gets validation)
        return self
