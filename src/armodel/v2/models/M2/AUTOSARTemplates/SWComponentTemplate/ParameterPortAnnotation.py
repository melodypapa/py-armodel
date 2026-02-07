from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

class ParameterPortAnnotation(GeneralAnnotation):
    """
    Annotation to a port used for calibration regarding a certain
    ParameterDataPrototype.
    
    Package: M2::AUTOSARTemplates::SWComponentTemplate::ApplicationAttributes::ParameterPortAnnotation
    
    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 158, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The instance of annotated ParameterDataPrototype.
        self._parameterPrototype: Optional["ParameterData"] = None

    @property
    def parameter_prototype(self) -> Optional["ParameterData"]:
        """Get parameterPrototype (Pythonic accessor)."""
        return self._parameterPrototype

    @parameter_prototype.setter
    def parameter_prototype(self, value: Optional["ParameterData"]) -> None:
        """
        Set parameterPrototype with validation.
        
        Args:
            value: The parameterPrototype to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._parameterPrototype = None
            return

        if not isinstance(value, ParameterData):
            raise TypeError(
                f"parameterPrototype must be ParameterData or None, got {type(value).__name__}"
            )
        self._parameterPrototype = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getParameterPrototype(self) -> "ParameterData":
        """
        AUTOSAR-compliant getter for parameterPrototype.
        
        Returns:
            The parameterPrototype value
        
        Note:
            Delegates to parameter_prototype property (CODING_RULE_V2_00017)
        """
        return self.parameter_prototype  # Delegates to property

    def setParameterPrototype(self, value: "ParameterData") -> "ParameterPortAnnotation":
        """
        AUTOSAR-compliant setter for parameterPrototype with method chaining.
        
        Args:
            value: The parameterPrototype to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to parameter_prototype property setter (gets validation automatically)
        """
        self.parameter_prototype = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_parameter_prototype(self, value: Optional["ParameterData"]) -> "ParameterPortAnnotation":
        """
        Set parameterPrototype and return self for chaining.
        
        Args:
            value: The parameterPrototype to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_parameter_prototype("value")
        """
        self.parameter_prototype = value  # Use property setter (gets validation)
        return self