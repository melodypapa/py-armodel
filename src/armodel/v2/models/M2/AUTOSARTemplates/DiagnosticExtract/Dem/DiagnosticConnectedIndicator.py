from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class DiagnosticConnectedIndicator(Identifiable):
    """
    Description of indicators that are defined per DiagnosticEvent.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dem::DiagnosticEvent::DiagnosticConnectedIndicator

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 166, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Behavior of the linked indicator.
        self._behaviorIndicatorBehaviorEnum: Optional["DiagnosticConnected"] = None

    @property
    def behavior_indicator_behavior_enum(self) -> Optional["DiagnosticConnected"]:
        """Get behaviorIndicatorBehaviorEnum (Pythonic accessor)."""
        return self._behaviorIndicatorBehaviorEnum

    @behavior_indicator_behavior_enum.setter
    def behavior_indicator_behavior_enum(self, value: Optional["DiagnosticConnected"]) -> None:
        """
        Set behaviorIndicatorBehaviorEnum with validation.

        Args:
            value: The behaviorIndicatorBehaviorEnum to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._behaviorIndicatorBehaviorEnum = None
            return

        if not isinstance(value, DiagnosticConnected):
            raise TypeError(
                f"behaviorIndicatorBehaviorEnum must be DiagnosticConnected or None, got {type(value).__name__}"
            )
        self._behaviorIndicatorBehaviorEnum = value
        # This attribute defines the number of healing cycles for the atpVariation.
        self._healingCycle: Optional["PositiveInteger"] = None

    @property
    def healing_cycle(self) -> Optional["PositiveInteger"]:
        """Get healingCycle (Pythonic accessor)."""
        return self._healingCycle

    @healing_cycle.setter
    def healing_cycle(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set healingCycle with validation.

        Args:
            value: The healingCycle to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._healingCycle = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"healingCycle must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._healingCycle = value
        # Reference to the used indicator.
        self._indicator: Optional["DiagnosticIndicator"] = None

    @property
    def indicator(self) -> Optional["DiagnosticIndicator"]:
        """Get indicator (Pythonic accessor)."""
        return self._indicator

    @indicator.setter
    def indicator(self, value: Optional["DiagnosticIndicator"]) -> None:
        """
        Set indicator with validation.

        Args:
            value: The indicator to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._indicator = None
            return

        if not isinstance(value, DiagnosticIndicator):
            raise TypeError(
                f"indicator must be DiagnosticIndicator or None, got {type(value).__name__}"
            )
        self._indicator = value
        # This attribute defines the number of failure cycles for the Please note that
        # this is not relevant for the Adaptive Platform.
        self._indicatorFailure: Optional["PositiveInteger"] = None

    @property
    def indicator_failure(self) -> Optional["PositiveInteger"]:
        """Get indicatorFailure (Pythonic accessor)."""
        return self._indicatorFailure

    @indicator_failure.setter
    def indicator_failure(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set indicatorFailure with validation.

        Args:
            value: The indicatorFailure to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._indicatorFailure = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"indicatorFailure must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._indicatorFailure = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBehaviorIndicatorBehaviorEnum(self) -> "DiagnosticConnected":
        """
        AUTOSAR-compliant getter for behaviorIndicatorBehaviorEnum.

        Returns:
            The behaviorIndicatorBehaviorEnum value

        Note:
            Delegates to behavior_indicator_behavior_enum property (CODING_RULE_V2_00017)
        """
        return self.behavior_indicator_behavior_enum  # Delegates to property

    def setBehaviorIndicatorBehaviorEnum(self, value: "DiagnosticConnected") -> "DiagnosticConnectedIndicator":
        """
        AUTOSAR-compliant setter for behaviorIndicatorBehaviorEnum with method chaining.

        Args:
            value: The behaviorIndicatorBehaviorEnum to set

        Returns:
            self for method chaining

        Note:
            Delegates to behavior_indicator_behavior_enum property setter (gets validation automatically)
        """
        self.behavior_indicator_behavior_enum = value  # Delegates to property setter
        return self

    def getHealingCycle(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for healingCycle.

        Returns:
            The healingCycle value

        Note:
            Delegates to healing_cycle property (CODING_RULE_V2_00017)
        """
        return self.healing_cycle  # Delegates to property

    def setHealingCycle(self, value: "PositiveInteger") -> "DiagnosticConnectedIndicator":
        """
        AUTOSAR-compliant setter for healingCycle with method chaining.

        Args:
            value: The healingCycle to set

        Returns:
            self for method chaining

        Note:
            Delegates to healing_cycle property setter (gets validation automatically)
        """
        self.healing_cycle = value  # Delegates to property setter
        return self

    def getIndicator(self) -> "DiagnosticIndicator":
        """
        AUTOSAR-compliant getter for indicator.

        Returns:
            The indicator value

        Note:
            Delegates to indicator property (CODING_RULE_V2_00017)
        """
        return self.indicator  # Delegates to property

    def setIndicator(self, value: "DiagnosticIndicator") -> "DiagnosticConnectedIndicator":
        """
        AUTOSAR-compliant setter for indicator with method chaining.

        Args:
            value: The indicator to set

        Returns:
            self for method chaining

        Note:
            Delegates to indicator property setter (gets validation automatically)
        """
        self.indicator = value  # Delegates to property setter
        return self

    def getIndicatorFailure(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for indicatorFailure.

        Returns:
            The indicatorFailure value

        Note:
            Delegates to indicator_failure property (CODING_RULE_V2_00017)
        """
        return self.indicator_failure  # Delegates to property

    def setIndicatorFailure(self, value: "PositiveInteger") -> "DiagnosticConnectedIndicator":
        """
        AUTOSAR-compliant setter for indicatorFailure with method chaining.

        Args:
            value: The indicatorFailure to set

        Returns:
            self for method chaining

        Note:
            Delegates to indicator_failure property setter (gets validation automatically)
        """
        self.indicator_failure = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_behavior_indicator_behavior_enum(self, value: Optional["DiagnosticConnected"]) -> "DiagnosticConnectedIndicator":
        """
        Set behaviorIndicatorBehaviorEnum and return self for chaining.

        Args:
            value: The behaviorIndicatorBehaviorEnum to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_behavior_indicator_behavior_enum("value")
        """
        self.behavior_indicator_behavior_enum = value  # Use property setter (gets validation)
        return self

    def with_healing_cycle(self, value: Optional["PositiveInteger"]) -> "DiagnosticConnectedIndicator":
        """
        Set healingCycle and return self for chaining.

        Args:
            value: The healingCycle to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_healing_cycle("value")
        """
        self.healing_cycle = value  # Use property setter (gets validation)
        return self

    def with_indicator(self, value: Optional["DiagnosticIndicator"]) -> "DiagnosticConnectedIndicator":
        """
        Set indicator and return self for chaining.

        Args:
            value: The indicator to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_indicator("value")
        """
        self.indicator = value  # Use property setter (gets validation)
        return self

    def with_indicator_failure(self, value: Optional["PositiveInteger"]) -> "DiagnosticConnectedIndicator":
        """
        Set indicatorFailure and return self for chaining.

        Args:
            value: The indicatorFailure to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_indicator_failure("value")
        """
        self.indicator_failure = value  # Use property setter (gets validation)
        return self
