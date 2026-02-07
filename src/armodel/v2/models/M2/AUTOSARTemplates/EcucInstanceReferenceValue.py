from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

class EcucInstanceReferenceValue(EcucAbstractReferenceValue):
    """
    InstanceReference representation in the ECU Configuration.
    
    Package: M2::AUTOSARTemplates::ECUCDescriptionTemplate::EcucInstanceReferenceValue
    
    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 134, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # by: AnyInstanceRef.
        self._value: Optional["AtpFeature"] = None

    @property
    def value(self) -> Optional["AtpFeature"]:
        """Get value (Pythonic accessor)."""
        return self._value

    @value.setter
    def value(self, value: Optional["AtpFeature"]) -> None:
        """
        Set value with validation.
        
        Args:
            value: The value to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._value = None
            return

        if not isinstance(value, AtpFeature):
            raise TypeError(
                f"value must be AtpFeature or None, got {type(value).__name__}"
            )
        self._value = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getValue(self) -> "AtpFeature":
        """
        AUTOSAR-compliant getter for value.
        
        Returns:
            The value value
        
        Note:
            Delegates to value property (CODING_RULE_V2_00017)
        """
        return self.value  # Delegates to property

    def setValue(self, value: "AtpFeature") -> "EcucInstanceReferenceValue":
        """
        AUTOSAR-compliant setter for value with method chaining.
        
        Args:
            value: The value to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to value property setter (gets validation automatically)
        """
        self.value = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_value(self, value: Optional["AtpFeature"]) -> "EcucInstanceReferenceValue":
        """
        Set value and return self for chaining.
        
        Args:
            value: The value to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_value("value")
        """
        self.value = value  # Use property setter (gets validation)
        return self