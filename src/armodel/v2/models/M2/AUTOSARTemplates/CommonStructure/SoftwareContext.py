from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class SoftwareContext(ARObject):
    """
    Specifies the context of the software for this resource consumption.
    
    Package: M2::AUTOSARTemplates::CommonStructure::ResourceConsumption::SoftwareContext
    
    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 163, Classic
      Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Specifies the input vector which is used to provide the.
        self._input: Optional["String"] = None

    @property
    def input(self) -> Optional["String"]:
        """Get input (Pythonic accessor)."""
        return self._input

    @input.setter
    def input(self, value: Optional["String"]) -> None:
        """
        Set input with validation.
        
        Args:
            value: The input to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._input = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"input must be String or None, got {type(value).__name__}"
            )
        self._input = value
        # Specifies the state the software is in when the Execution provided.
        self._state: Optional["String"] = None

    @property
    def state(self) -> Optional["String"]:
        """Get state (Pythonic accessor)."""
        return self._state

    @state.setter
    def state(self, value: Optional["String"]) -> None:
        """
        Set state with validation.
        
        Args:
            value: The state to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._state = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"state must be String or None, got {type(value).__name__}"
            )
        self._state = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getInput(self) -> "String":
        """
        AUTOSAR-compliant getter for input.
        
        Returns:
            The input value
        
        Note:
            Delegates to input property (CODING_RULE_V2_00017)
        """
        return self.input  # Delegates to property

    def setInput(self, value: "String") -> "SoftwareContext":
        """
        AUTOSAR-compliant setter for input with method chaining.
        
        Args:
            value: The input to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to input property setter (gets validation automatically)
        """
        self.input = value  # Delegates to property setter
        return self

    def getState(self) -> "String":
        """
        AUTOSAR-compliant getter for state.
        
        Returns:
            The state value
        
        Note:
            Delegates to state property (CODING_RULE_V2_00017)
        """
        return self.state  # Delegates to property

    def setState(self, value: "String") -> "SoftwareContext":
        """
        AUTOSAR-compliant setter for state with method chaining.
        
        Args:
            value: The state to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to state property setter (gets validation automatically)
        """
        self.state = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_input(self, value: Optional["String"]) -> "SoftwareContext":
        """
        Set input and return self for chaining.
        
        Args:
            value: The input to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_input("value")
        """
        self.input = value  # Use property setter (gets validation)
        return self

    def with_state(self, value: Optional["String"]) -> "SoftwareContext":
        """
        Set state and return self for chaining.
        
        Args:
            value: The state to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_state("value")
        """
        self.state = value  # Use property setter (gets validation)
        return self