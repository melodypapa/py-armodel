"""
AUTOSAR Package - TimingCondition

Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingCondition
"""

from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class TimingCondition(Identifiable):
    """
    A TimingCondition describes a dependency on a specific condition. The
    element owns an expression which describes the timing condition dependency.
    
    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingCondition::TimingCondition
    
    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 35, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This is the expression describing the dependency on a specific condition.
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

    def with_timing_argument(self, value):
        """
        Set timing_argument and return self for chaining.

        Args:
            value: The timing_argument to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_timing_argument("value")
        """
        self.timing_argument = value  # Use property setter (gets validation)
        return self

    def with_timing_variable(self, value):
        """
        Set timing_variable and return self for chaining.

        Args:
            value: The timing_variable to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_timing_variable("value")
        """
        self.timing_variable = value  # Use property setter (gets validation)
        return self

    def with_context(self, value):
        """
        Set context and return self for chaining.

        Args:
            value: The context to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_context("value")
        """
        self.context = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTimingCondition(self) -> "TimingCondition":
        """
        AUTOSAR-compliant getter for timingCondition.
        
        Returns:
            The timingCondition value
        
        Note:
            Delegates to timing_condition property (CODING_RULE_V2_00017)
        """
        return self.timing_condition  # Delegates to property

    def setTimingCondition(self, value: "TimingCondition") -> "TimingCondition":
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

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_timing_condition(self, value: Optional["TimingCondition"]) -> "TimingCondition":
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



class TimingExtensionResource(Identifiable):
    """
    A TimingExtensionResource provides the capability to contain instance
    references referred from within a timing condition formula.
    
    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingCondition::TimingExtensionResource
    
    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 35, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This refers to an instance reference of an argument of an call.
        # atpVariation 277 Document ID 411: AUTOSAR_CP_TPS_TimingExtensions Timing
                # Extensions for Classic R23-11.
        self._timingArgument: List["AutosarOperation"] = []

    @property
    def timing_argument(self) -> List["AutosarOperation"]:
        """Get timingArgument (Pythonic accessor)."""
        return self._timingArgument
        # This refers to an instance reference of a mode atpVariation.
        self._timingMode: List["TimingModeInstance"] = []

    @property
    def timing_mode(self) -> List["TimingModeInstance"]:
        """Get timingMode (Pythonic accessor)."""
        return self._timingMode
        # This refers to an instance reference of a variable.
        # atpSplitable; atpVariation.
        self._timingVariable: List["AutosarVariable"] = []

    @property
    def timing_variable(self) -> List["AutosarVariable"]:
        """Get timingVariable (Pythonic accessor)."""
        return self._timingVariable

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTimingArgument(self) -> List["AutosarOperation"]:
        """
        AUTOSAR-compliant getter for timingArgument.
        
        Returns:
            The timingArgument value
        
        Note:
            Delegates to timing_argument property (CODING_RULE_V2_00017)
        """
        return self.timing_argument  # Delegates to property

    def getTimingMode(self) -> List["TimingModeInstance"]:
        """
        AUTOSAR-compliant getter for timingMode.
        
        Returns:
            The timingMode value
        
        Note:
            Delegates to timing_mode property (CODING_RULE_V2_00017)
        """
        return self.timing_mode  # Delegates to property

    def getTimingVariable(self) -> List["AutosarVariable"]:
        """
        AUTOSAR-compliant getter for timingVariable.
        
        Returns:
            The timingVariable value
        
        Note:
            Delegates to timing_variable property (CODING_RULE_V2_00017)
        """
        return self.timing_variable  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class TimingModeInstance(Identifiable):
    """
    This class specifies the mode declaration to be checked in a specific
    instance of a mode declaration group. This is used in a timing condition
    formula as an operand of the unary timing function TIMEX_mode Active to
    check whether the mode declaration is active at the point in time this
    expression is evaluated.
    
    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingCondition::TimingModeInstance
    
    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 37, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This refers to a specific mode declaration in the given.
        self._modeInstance: Optional["ModeInSwcBsw"] = None

    @property
    def mode_instance(self) -> Optional["ModeInSwcBsw"]:
        """Get modeInstance (Pythonic accessor)."""
        return self._modeInstance

    @mode_instance.setter
    def mode_instance(self, value: Optional["ModeInSwcBsw"]) -> None:
        """
        Set modeInstance with validation.
        
        Args:
            value: The modeInstance to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._modeInstance = None
            return

        if not isinstance(value, ModeInSwcBsw):
            raise TypeError(
                f"modeInstance must be ModeInSwcBsw or None, got {type(value).__name__}"
            )
        self._modeInstance = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getModeInstance(self) -> "ModeInSwcBsw":
        """
        AUTOSAR-compliant getter for modeInstance.
        
        Returns:
            The modeInstance value
        
        Note:
            Delegates to mode_instance property (CODING_RULE_V2_00017)
        """
        return self.mode_instance  # Delegates to property

    def setModeInstance(self, value: "ModeInSwcBsw") -> "TimingModeInstance":
        """
        AUTOSAR-compliant setter for modeInstance with method chaining.
        
        Args:
            value: The modeInstance to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to mode_instance property setter (gets validation automatically)
        """
        self.mode_instance = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_mode_instance(self, value: Optional["ModeInSwcBsw"]) -> "TimingModeInstance":
        """
        Set modeInstance and return self for chaining.
        
        Args:
            value: The modeInstance to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_mode_instance("value")
        """
        self.mode_instance = value  # Use property setter (gets validation)
        return self



class ModeInBswInstanceRef(ARObject):
    """
    Instance reference to be capable of referencing a specific ModeDeclaration
    of a ModeDeclarationGroup Prototype utilized in a BSW module.
    
    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingCondition::ModeInBswInstanceRef
    
    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 38, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Specifies the BSW implementation that manifests the.
        self._contextBsw: Optional["BswImplementation"] = None

    @property
    def context_bsw(self) -> Optional["BswImplementation"]:
        """Get contextBsw (Pythonic accessor)."""
        return self._contextBsw

    @context_bsw.setter
    def context_bsw(self, value: Optional["BswImplementation"]) -> None:
        """
        Set contextBsw with validation.
        
        Args:
            value: The contextBsw to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._contextBsw = None
            return

        if not isinstance(value, BswImplementation):
            raise TypeError(
                f"contextBsw must be BswImplementation or None, got {type(value).__name__}"
            )
        self._contextBsw = value
        # Specifies the mode declaration group prototype that manifests the context.
        # xml.
        # sequenceOffset=20.
        self._contextMode: Optional["RefType"] = None

    @property
    def context_mode(self) -> Optional["RefType"]:
        """Get contextMode (Pythonic accessor)."""
        return self._contextMode

    @context_mode.setter
    def context_mode(self, value: Optional["RefType"]) -> None:
        """
        Set contextMode with validation.
        
        Args:
            value: The contextMode to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._contextMode = None
            return

        self._contextMode = value
        # Specifies the specific mode declaration in the given.
        self._targetMode: Optional["ModeDeclaration"] = None

    @property
    def target_mode(self) -> Optional["ModeDeclaration"]:
        """Get targetMode (Pythonic accessor)."""
        return self._targetMode

    @target_mode.setter
    def target_mode(self, value: Optional["ModeDeclaration"]) -> None:
        """
        Set targetMode with validation.
        
        Args:
            value: The targetMode to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._targetMode = None
            return

        if not isinstance(value, ModeDeclaration):
            raise TypeError(
                f"targetMode must be ModeDeclaration or None, got {type(value).__name__}"
            )
        self._targetMode = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getContextBsw(self) -> "BswImplementation":
        """
        AUTOSAR-compliant getter for contextBsw.
        
        Returns:
            The contextBsw value
        
        Note:
            Delegates to context_bsw property (CODING_RULE_V2_00017)
        """
        return self.context_bsw  # Delegates to property

    def setContextBsw(self, value: "BswImplementation") -> "ModeInBswInstanceRef":
        """
        AUTOSAR-compliant setter for contextBsw with method chaining.
        
        Args:
            value: The contextBsw to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to context_bsw property setter (gets validation automatically)
        """
        self.context_bsw = value  # Delegates to property setter
        return self

    def getContextMode(self) -> "RefType":
        """
        AUTOSAR-compliant getter for contextMode.
        
        Returns:
            The contextMode value
        
        Note:
            Delegates to context_mode property (CODING_RULE_V2_00017)
        """
        return self.context_mode  # Delegates to property

    def setContextMode(self, value: "RefType") -> "ModeInBswInstanceRef":
        """
        AUTOSAR-compliant setter for contextMode with method chaining.
        
        Args:
            value: The contextMode to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to context_mode property setter (gets validation automatically)
        """
        self.context_mode = value  # Delegates to property setter
        return self

    def getTargetMode(self) -> "ModeDeclaration":
        """
        AUTOSAR-compliant getter for targetMode.
        
        Returns:
            The targetMode value
        
        Note:
            Delegates to target_mode property (CODING_RULE_V2_00017)
        """
        return self.target_mode  # Delegates to property

    def setTargetMode(self, value: "ModeDeclaration") -> "ModeInBswInstanceRef":
        """
        AUTOSAR-compliant setter for targetMode with method chaining.
        
        Args:
            value: The targetMode to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to target_mode property setter (gets validation automatically)
        """
        self.target_mode = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_context_bsw(self, value: Optional["BswImplementation"]) -> "ModeInBswInstanceRef":
        """
        Set contextBsw and return self for chaining.
        
        Args:
            value: The contextBsw to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_context_bsw("value")
        """
        self.context_bsw = value  # Use property setter (gets validation)
        return self

    def with_context_mode(self, value: Optional[RefType]) -> "ModeInBswInstanceRef":
        """
        Set contextMode and return self for chaining.
        
        Args:
            value: The contextMode to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_context_mode("value")
        """
        self.context_mode = value  # Use property setter (gets validation)
        return self

    def with_target_mode(self, value: Optional["ModeDeclaration"]) -> "ModeInBswInstanceRef":
        """
        Set targetMode and return self for chaining.
        
        Args:
            value: The targetMode to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_target_mode("value")
        """
        self.target_mode = value  # Use property setter (gets validation)
        return self



class ModeInSwcInstanceRef(ARObject):
    """
    Instance reference to be capable of referencing a ModeDeclaration at a
    specific Mode Switch Port of a SW-C.
    
    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingCondition::ModeInSwcInstanceRef
    
    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 38, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Specifies the SW component representing the base of the.
        self._base: Optional["SwComponentType"] = None

    @property
    def base(self) -> Optional["SwComponentType"]:
        """Get base (Pythonic accessor)."""
        return self._base

    @base.setter
    def base(self, value: Optional["SwComponentType"]) -> None:
        """
        Set base with validation.
        
        Args:
            value: The base to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._base = None
            return

        if not isinstance(value, SwComponentType):
            raise TypeError(
                f"base must be SwComponentType or None, got {type(value).__name__}"
            )
        self._base = value
        # Specifies the SW component prototype representing the context.
        self._context: List["SwComponent"] = []

    @property
    def context(self) -> List["SwComponent"]:
        """Get context (Pythonic accessor)."""
        return self._context
        # Specifies the mode declaration group prototype that manifests the context.
        # xml.
        # sequenceOffset=40.
        self._contextMode: Optional["RefType"] = None

    @property
    def context_mode(self) -> Optional["RefType"]:
        """Get contextMode (Pythonic accessor)."""
        return self._contextMode

    @context_mode.setter
    def context_mode(self, value: Optional["RefType"]) -> None:
        """
        Set contextMode with validation.
        
        Args:
            value: The contextMode to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._contextMode = None
            return

        self._contextMode = value
        # Specifies the port prototype representing the context.
        # 277 Document ID 411: AUTOSAR_CP_TPS_TimingExtensions Timing Extensions for
                # Classic R23-11.
        self._contextPort: Optional["RefType"] = None

    @property
    def context_port(self) -> Optional["RefType"]:
        """Get contextPort (Pythonic accessor)."""
        return self._contextPort

    @context_port.setter
    def context_port(self, value: Optional["RefType"]) -> None:
        """
        Set contextPort with validation.
        
        Args:
            value: The contextPort to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._contextPort = None
            return

        self._contextPort = value
        # Specifies the specific mode declaration in the given.
        self._targetMode: Optional["ModeDeclaration"] = None

    @property
    def target_mode(self) -> Optional["ModeDeclaration"]:
        """Get targetMode (Pythonic accessor)."""
        return self._targetMode

    @target_mode.setter
    def target_mode(self, value: Optional["ModeDeclaration"]) -> None:
        """
        Set targetMode with validation.
        
        Args:
            value: The targetMode to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._targetMode = None
            return

        if not isinstance(value, ModeDeclaration):
            raise TypeError(
                f"targetMode must be ModeDeclaration or None, got {type(value).__name__}"
            )
        self._targetMode = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBase(self) -> "SwComponentType":
        """
        AUTOSAR-compliant getter for base.
        
        Returns:
            The base value
        
        Note:
            Delegates to base property (CODING_RULE_V2_00017)
        """
        return self.base  # Delegates to property

    def setBase(self, value: "SwComponentType") -> "ModeInSwcInstanceRef":
        """
        AUTOSAR-compliant setter for base with method chaining.
        
        Args:
            value: The base to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to base property setter (gets validation automatically)
        """
        self.base = value  # Delegates to property setter
        return self

    def getContext(self) -> List["SwComponent"]:
        """
        AUTOSAR-compliant getter for context.
        
        Returns:
            The context value
        
        Note:
            Delegates to context property (CODING_RULE_V2_00017)
        """
        return self.context  # Delegates to property

    def getContextMode(self) -> "RefType":
        """
        AUTOSAR-compliant getter for contextMode.
        
        Returns:
            The contextMode value
        
        Note:
            Delegates to context_mode property (CODING_RULE_V2_00017)
        """
        return self.context_mode  # Delegates to property

    def setContextMode(self, value: "RefType") -> "ModeInSwcInstanceRef":
        """
        AUTOSAR-compliant setter for contextMode with method chaining.
        
        Args:
            value: The contextMode to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to context_mode property setter (gets validation automatically)
        """
        self.context_mode = value  # Delegates to property setter
        return self

    def getContextPort(self) -> "RefType":
        """
        AUTOSAR-compliant getter for contextPort.
        
        Returns:
            The contextPort value
        
        Note:
            Delegates to context_port property (CODING_RULE_V2_00017)
        """
        return self.context_port  # Delegates to property

    def setContextPort(self, value: "RefType") -> "ModeInSwcInstanceRef":
        """
        AUTOSAR-compliant setter for contextPort with method chaining.
        
        Args:
            value: The contextPort to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to context_port property setter (gets validation automatically)
        """
        self.context_port = value  # Delegates to property setter
        return self

    def getTargetMode(self) -> "ModeDeclaration":
        """
        AUTOSAR-compliant getter for targetMode.
        
        Returns:
            The targetMode value
        
        Note:
            Delegates to target_mode property (CODING_RULE_V2_00017)
        """
        return self.target_mode  # Delegates to property

    def setTargetMode(self, value: "ModeDeclaration") -> "ModeInSwcInstanceRef":
        """
        AUTOSAR-compliant setter for targetMode with method chaining.
        
        Args:
            value: The targetMode to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to target_mode property setter (gets validation automatically)
        """
        self.target_mode = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_base(self, value: Optional["SwComponentType"]) -> "ModeInSwcInstanceRef":
        """
        Set base and return self for chaining.
        
        Args:
            value: The base to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_base("value")
        """
        self.base = value  # Use property setter (gets validation)
        return self

    def with_context_mode(self, value: Optional[RefType]) -> "ModeInSwcInstanceRef":
        """
        Set contextMode and return self for chaining.
        
        Args:
            value: The contextMode to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_context_mode("value")
        """
        self.context_mode = value  # Use property setter (gets validation)
        return self

    def with_context_port(self, value: Optional[RefType]) -> "ModeInSwcInstanceRef":
        """
        Set contextPort and return self for chaining.
        
        Args:
            value: The contextPort to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_context_port("value")
        """
        self.context_port = value  # Use property setter (gets validation)
        return self

    def with_target_mode(self, value: Optional["ModeDeclaration"]) -> "ModeInSwcInstanceRef":
        """
        Set targetMode and return self for chaining.
        
        Args:
            value: The targetMode to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_target_mode("value")
        """
        self.target_mode = value  # Use property setter (gets validation)
        return self
