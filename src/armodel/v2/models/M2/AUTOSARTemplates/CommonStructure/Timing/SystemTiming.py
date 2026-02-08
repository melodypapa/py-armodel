from typing import Optional
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingExtensions import TimingExtension


class SystemTiming(TimingExtension):
    """
    A model element used to refine timing descriptions and constraints (from a
    VfbTiming) at System level, utilizing information about topology, software
    deployment, and signal mapping described in the System Template.
    TimingDescriptions aggregated by SystemTiming are restricted to events which
    are derived from the class TDEventVfb, TDEventSwcInternalBehavior and
    TDEventCom.

    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingExtensions::SystemTiming

    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 26, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This defines the scope of a SystemTiming.
        # All descriptions and constraints shall within this scope.
        self._system: Optional["System"] = None

    @property
    def system(self) -> Optional["System"]:
        """Get system (Pythonic accessor)."""
        return self._system

    @system.setter
    def system(self, value: Optional["System"]) -> None:
        """
        Set system with validation.

        Args:
            value: The system to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._system = None
            return

        if not isinstance(value, System):
            raise TypeError(
                f"system must be System or None, got {type(value).__name__}"
            )
        self._system = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getSystem(self) -> "System":
        """
        AUTOSAR-compliant getter for system.

        Returns:
            The system value

        Note:
            Delegates to system property (CODING_RULE_V2_00017)
        """
        return self.system  # Delegates to property

    def setSystem(self, value: "System") -> "SystemTiming":
        """
        AUTOSAR-compliant setter for system with method chaining.

        Args:
            value: The system to set

        Returns:
            self for method chaining

        Note:
            Delegates to system property setter (gets validation automatically)
        """
        self.system = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_system(self, value: Optional["System"]) -> "SystemTiming":
        """
        Set system and return self for chaining.

        Args:
            value: The system to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_system("value")
        """
        self.system = value  # Use property setter (gets validation)
        return self
