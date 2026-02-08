from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription import (
    TDEventSwc,
)


class TDEventSwcInternalBehavior(TDEventSwc):
    """
    This is used to describe timing events related to the SwcInternalBehavior of
    an AtomicSwComponent Type.

    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingDescription::TimingDescription

    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 61, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The scope of this timing event.
        # 277 Document ID 411: AUTOSAR_CP_TPS_TimingExtensions Timing Extensions for
                # Classic R23-11.
        self._runnable: Optional["RunnableEntity"] = None

    @property
    def runnable(self) -> Optional["RunnableEntity"]:
        """Get runnable (Pythonic accessor)."""
        return self._runnable

    @runnable.setter
    def runnable(self, value: Optional["RunnableEntity"]) -> None:
        """
        Set runnable with validation.

        Args:
            value: The runnable to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._runnable = None
            return

        if not isinstance(value, RunnableEntity):
            raise TypeError(
                f"runnable must be RunnableEntity or None, got {type(value).__name__}"
            )
        self._runnable = value
        # The specific type of this timing event.
        self._tdEventSwcBehaviorType: Optional["TDEventSwcInternal"] = None

    @property
    def td_event_swc_behavior_type(self) -> Optional["TDEventSwcInternal"]:
        """Get tdEventSwcBehaviorType (Pythonic accessor)."""
        return self._tdEventSwcBehaviorType

    @td_event_swc_behavior_type.setter
    def td_event_swc_behavior_type(self, value: Optional["TDEventSwcInternal"]) -> None:
        """
        Set tdEventSwcBehaviorType with validation.

        Args:
            value: The tdEventSwcBehaviorType to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tdEventSwcBehaviorType = None
            return

        if not isinstance(value, TDEventSwcInternal):
            raise TypeError(
                f"tdEventSwcBehaviorType must be TDEventSwcInternal or None, got {type(value).__name__}"
            )
        self._tdEventSwcBehaviorType = value
        # The scope of this timing event.
        self._variableAccess: Optional["VariableAccess"] = None

    @property
    def variable_access(self) -> Optional["VariableAccess"]:
        """Get variableAccess (Pythonic accessor)."""
        return self._variableAccess

    @variable_access.setter
    def variable_access(self, value: Optional["VariableAccess"]) -> None:
        """
        Set variableAccess with validation.

        Args:
            value: The variableAccess to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._variableAccess = None
            return

        if not isinstance(value, VariableAccess):
            raise TypeError(
                f"variableAccess must be VariableAccess or None, got {type(value).__name__}"
            )
        self._variableAccess = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getRunnable(self) -> "RunnableEntity":
        """
        AUTOSAR-compliant getter for runnable.

        Returns:
            The runnable value

        Note:
            Delegates to runnable property (CODING_RULE_V2_00017)
        """
        return self.runnable  # Delegates to property

    def setRunnable(self, value: "RunnableEntity") -> "TDEventSwcInternalBehavior":
        """
        AUTOSAR-compliant setter for runnable with method chaining.

        Args:
            value: The runnable to set

        Returns:
            self for method chaining

        Note:
            Delegates to runnable property setter (gets validation automatically)
        """
        self.runnable = value  # Delegates to property setter
        return self

    def getTdEventSwcBehaviorType(self) -> "TDEventSwcInternal":
        """
        AUTOSAR-compliant getter for tdEventSwcBehaviorType.

        Returns:
            The tdEventSwcBehaviorType value

        Note:
            Delegates to td_event_swc_behavior_type property (CODING_RULE_V2_00017)
        """
        return self.td_event_swc_behavior_type  # Delegates to property

    def setTdEventSwcBehaviorType(self, value: "TDEventSwcInternal") -> "TDEventSwcInternalBehavior":
        """
        AUTOSAR-compliant setter for tdEventSwcBehaviorType with method chaining.

        Args:
            value: The tdEventSwcBehaviorType to set

        Returns:
            self for method chaining

        Note:
            Delegates to td_event_swc_behavior_type property setter (gets validation automatically)
        """
        self.td_event_swc_behavior_type = value  # Delegates to property setter
        return self

    def getVariableAccess(self) -> "VariableAccess":
        """
        AUTOSAR-compliant getter for variableAccess.

        Returns:
            The variableAccess value

        Note:
            Delegates to variable_access property (CODING_RULE_V2_00017)
        """
        return self.variable_access  # Delegates to property

    def setVariableAccess(self, value: "VariableAccess") -> "TDEventSwcInternalBehavior":
        """
        AUTOSAR-compliant setter for variableAccess with method chaining.

        Args:
            value: The variableAccess to set

        Returns:
            self for method chaining

        Note:
            Delegates to variable_access property setter (gets validation automatically)
        """
        self.variable_access = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_runnable(self, value: Optional["RunnableEntity"]) -> "TDEventSwcInternalBehavior":
        """
        Set runnable and return self for chaining.

        Args:
            value: The runnable to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_runnable("value")
        """
        self.runnable = value  # Use property setter (gets validation)
        return self

    def with_td_event_swc_behavior_type(self, value: Optional["TDEventSwcInternal"]) -> "TDEventSwcInternalBehavior":
        """
        Set tdEventSwcBehaviorType and return self for chaining.

        Args:
            value: The tdEventSwcBehaviorType to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_td_event_swc_behavior_type("value")
        """
        self.td_event_swc_behavior_type = value  # Use property setter (gets validation)
        return self

    def with_variable_access(self, value: Optional["VariableAccess"]) -> "TDEventSwcInternalBehavior":
        """
        Set variableAccess and return self for chaining.

        Args:
            value: The variableAccess to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_variable_access("value")
        """
        self.variable_access = value  # Use property setter (gets validation)
        return self
