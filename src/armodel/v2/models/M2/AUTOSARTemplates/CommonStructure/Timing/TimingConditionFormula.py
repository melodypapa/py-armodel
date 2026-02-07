from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class TimingConditionFormula(ARObject):
    """
    A TimingConditionFormula describes a specific dependency. The expression
    shall be a boolean expression addressing modes, variables, arguments, and/or
    events.
    
    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingCondition::TimingConditionFormula
    
    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 35, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This refers to an argument of an operation call.
        self._timingArgumentArgumentInstance: Optional["AutosarOperation"] = None

    @property
    def timing_argument_argument_instance(self) -> Optional["AutosarOperation"]:
        """Get timingArgumentArgumentInstance (Pythonic accessor)."""
        return self._timingArgumentArgumentInstance

    @timing_argument_argument_instance.setter
    def timing_argument_argument_instance(self, value: Optional["AutosarOperation"]) -> None:
        """
        Set timingArgumentArgumentInstance with validation.
        
        Args:
            value: The timingArgumentArgumentInstance to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timingArgumentArgumentInstance = None
            return

        if not isinstance(value, AutosarOperation):
            raise TypeError(
                f"timingArgumentArgumentInstance must be AutosarOperation or None, got {type(value).__name__}"
            )
        self._timingArgumentArgumentInstance = value
        # This refers to a timing condition that is part of an the dependency on a
        # specific.
        self._timingCondition: Optional["TimingCondition"] = None

    @property
    def timing_condition(self) -> Optional["TimingCondition"]:
        """Get timingCondition (Pythonic accessor)."""
        return self._timingCondition

    @timing_condition.setter
    def timing_condition(self, value: Optional["TimingCondition"]) -> None:
        """
        Set timingCondition with validation.
        
        Args:
            value: The timingCondition to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timingCondition = None
            return

        if not isinstance(value, TimingCondition):
            raise TypeError(
                f"timingCondition must be TimingCondition or None, got {type(value).__name__}"
            )
        self._timingCondition = value
        # This refers to a timing event.
        self._timingEvent: Optional["TimingDescriptionEvent"] = None

    @property
    def timing_event(self) -> Optional["TimingDescriptionEvent"]:
        """Get timingEvent (Pythonic accessor)."""
        return self._timingEvent

    @timing_event.setter
    def timing_event(self, value: Optional["TimingDescriptionEvent"]) -> None:
        """
        Set timingEvent with validation.
        
        Args:
            value: The timingEvent to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timingEvent = None
            return

        if not isinstance(value, TimingDescriptionEvent):
            raise TypeError(
                f"timingEvent must be TimingDescriptionEvent or None, got {type(value).__name__}"
            )
        self._timingEvent = value
        # This refers to a mode declaration.
        self._timingMode: Optional["TimingModeInstance"] = None

    @property
    def timing_mode(self) -> Optional["TimingModeInstance"]:
        """Get timingMode (Pythonic accessor)."""
        return self._timingMode

    @timing_mode.setter
    def timing_mode(self, value: Optional["TimingModeInstance"]) -> None:
        """
        Set timingMode with validation.
        
        Args:
            value: The timingMode to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timingMode = None
            return

        if not isinstance(value, TimingModeInstance):
            raise TypeError(
                f"timingMode must be TimingModeInstance or None, got {type(value).__name__}"
            )
        self._timingMode = value
        # This refers to a variable.
        self._timingVariableInstance: Optional["AutosarVariable"] = None

    @property
    def timing_variable_instance(self) -> Optional["AutosarVariable"]:
        """Get timingVariableInstance (Pythonic accessor)."""
        return self._timingVariableInstance

    @timing_variable_instance.setter
    def timing_variable_instance(self, value: Optional["AutosarVariable"]) -> None:
        """
        Set timingVariableInstance with validation.
        
        Args:
            value: The timingVariableInstance to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timingVariableInstance = None
            return

        if not isinstance(value, AutosarVariable):
            raise TypeError(
                f"timingVariableInstance must be AutosarVariable or None, got {type(value).__name__}"
            )
        self._timingVariableInstance = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTimingArgumentArgumentInstance(self) -> "AutosarOperation":
        """
        AUTOSAR-compliant getter for timingArgumentArgumentInstance.
        
        Returns:
            The timingArgumentArgumentInstance value
        
        Note:
            Delegates to timing_argument_argument_instance property (CODING_RULE_V2_00017)
        """
        return self.timing_argument_argument_instance  # Delegates to property

    def setTimingArgumentArgumentInstance(self, value: "AutosarOperation") -> "TimingConditionFormula":
        """
        AUTOSAR-compliant setter for timingArgumentArgumentInstance with method chaining.
        
        Args:
            value: The timingArgumentArgumentInstance to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to timing_argument_argument_instance property setter (gets validation automatically)
        """
        self.timing_argument_argument_instance = value  # Delegates to property setter
        return self

    def getTimingCondition(self) -> "TimingCondition":
        """
        AUTOSAR-compliant getter for timingCondition.
        
        Returns:
            The timingCondition value
        
        Note:
            Delegates to timing_condition property (CODING_RULE_V2_00017)
        """
        return self.timing_condition  # Delegates to property

    def setTimingCondition(self, value: "TimingCondition") -> "TimingConditionFormula":
        """
        AUTOSAR-compliant setter for timingCondition with method chaining.
        
        Args:
            value: The timingCondition to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to timing_condition property setter (gets validation automatically)
        """
        self.timing_condition = value  # Delegates to property setter
        return self

    def getTimingEvent(self) -> "TimingDescriptionEvent":
        """
        AUTOSAR-compliant getter for timingEvent.
        
        Returns:
            The timingEvent value
        
        Note:
            Delegates to timing_event property (CODING_RULE_V2_00017)
        """
        return self.timing_event  # Delegates to property

    def setTimingEvent(self, value: "TimingDescriptionEvent") -> "TimingConditionFormula":
        """
        AUTOSAR-compliant setter for timingEvent with method chaining.
        
        Args:
            value: The timingEvent to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to timing_event property setter (gets validation automatically)
        """
        self.timing_event = value  # Delegates to property setter
        return self

    def getTimingMode(self) -> "TimingModeInstance":
        """
        AUTOSAR-compliant getter for timingMode.
        
        Returns:
            The timingMode value
        
        Note:
            Delegates to timing_mode property (CODING_RULE_V2_00017)
        """
        return self.timing_mode  # Delegates to property

    def setTimingMode(self, value: "TimingModeInstance") -> "TimingConditionFormula":
        """
        AUTOSAR-compliant setter for timingMode with method chaining.
        
        Args:
            value: The timingMode to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to timing_mode property setter (gets validation automatically)
        """
        self.timing_mode = value  # Delegates to property setter
        return self

    def getTimingVariableInstance(self) -> "AutosarVariable":
        """
        AUTOSAR-compliant getter for timingVariableInstance.
        
        Returns:
            The timingVariableInstance value
        
        Note:
            Delegates to timing_variable_instance property (CODING_RULE_V2_00017)
        """
        return self.timing_variable_instance  # Delegates to property

    def setTimingVariableInstance(self, value: "AutosarVariable") -> "TimingConditionFormula":
        """
        AUTOSAR-compliant setter for timingVariableInstance with method chaining.
        
        Args:
            value: The timingVariableInstance to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to timing_variable_instance property setter (gets validation automatically)
        """
        self.timing_variable_instance = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_timing_argument_argument_instance(self, value: Optional["AutosarOperation"]) -> "TimingConditionFormula":
        """
        Set timingArgumentArgumentInstance and return self for chaining.
        
        Args:
            value: The timingArgumentArgumentInstance to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_timing_argument_argument_instance("value")
        """
        self.timing_argument_argument_instance = value  # Use property setter (gets validation)
        return self

    def with_timing_condition(self, value: Optional["TimingCondition"]) -> "TimingConditionFormula":
        """
        Set timingCondition and return self for chaining.
        
        Args:
            value: The timingCondition to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_timing_condition("value")
        """
        self.timing_condition = value  # Use property setter (gets validation)
        return self

    def with_timing_event(self, value: Optional["TimingDescriptionEvent"]) -> "TimingConditionFormula":
        """
        Set timingEvent and return self for chaining.
        
        Args:
            value: The timingEvent to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_timing_event("value")
        """
        self.timing_event = value  # Use property setter (gets validation)
        return self

    def with_timing_mode(self, value: Optional["TimingModeInstance"]) -> "TimingConditionFormula":
        """
        Set timingMode and return self for chaining.
        
        Args:
            value: The timingMode to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_timing_mode("value")
        """
        self.timing_mode = value  # Use property setter (gets validation)
        return self

    def with_timing_variable_instance(self, value: Optional["AutosarVariable"]) -> "TimingConditionFormula":
        """
        Set timingVariableInstance and return self for chaining.
        
        Args:
            value: The timingVariableInstance to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_timing_variable_instance("value")
        """
        self.timing_variable_instance = value  # Use property setter (gets validation)
        return self