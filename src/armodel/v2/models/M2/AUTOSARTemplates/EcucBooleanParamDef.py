from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

class EcucBooleanParamDef(EcucParameterDef):
    """
    Configuration parameter type for Boolean. Allowed values are true and false.
    
    Package: M2::AUTOSARTemplates::ECUCParameterDefTemplate::EcucBooleanParamDef
    
    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 58, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 183, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Default value of the boolean configuration parameter.
        self._defaultValue: Optional["Boolean"] = None

    @property
    def default_value(self) -> Optional["Boolean"]:
        """Get defaultValue (Pythonic accessor)."""
        return self._defaultValue

    @default_value.setter
    def default_value(self, value: Optional["Boolean"]) -> None:
        """
        Set defaultValue with validation.
        
        Args:
            value: The defaultValue to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._defaultValue = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"defaultValue must be Boolean or None, got {type(value).__name__}"
            )
        self._defaultValue = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDefaultValue(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for defaultValue.
        
        Returns:
            The defaultValue value
        
        Note:
            Delegates to default_value property (CODING_RULE_V2_00017)
        """
        return self.default_value  # Delegates to property

    def setDefaultValue(self, value: "Boolean") -> "EcucBooleanParamDef":
        """
        AUTOSAR-compliant setter for defaultValue with method chaining.
        
        Args:
            value: The defaultValue to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to default_value property setter (gets validation automatically)
        """
        self.default_value = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_default_value(self, value: Optional["Boolean"]) -> "EcucBooleanParamDef":
        """
        Set defaultValue and return self for chaining.
        
        Args:
            value: The defaultValue to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_default_value("value")
        """
        self.default_value = value  # Use property setter (gets validation)
        return self