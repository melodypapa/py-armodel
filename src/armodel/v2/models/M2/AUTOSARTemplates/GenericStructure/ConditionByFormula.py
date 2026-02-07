from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class ConditionByFormula(ARObject):
    """
    This class represents a condition which is computed based on system
    constants according to the specified expression. The expected result is
    considered as boolean value. The result of the expression is interpreted as
    a condition. • "0" represents "false"; • a value other than zero is
    considered "true"
    
    Package: M2::AUTOSARTemplates::GenericStructure::VariantHandling::ConditionByFormula
    
    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 613, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2012, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (Page 73, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 231, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute specifies the point in time when condition evaluated at
                # earliest.
        # At this point in time all constants shall have a value.
        self._bindingTime: "BindingTimeEnum" = None

    @property
    def binding_time(self) -> "BindingTimeEnum":
        """Get bindingTime (Pythonic accessor)."""
        return self._bindingTime

    @binding_time.setter
    def binding_time(self, value: "BindingTimeEnum") -> None:
        """
        Set bindingTime with validation.
        
        Args:
            value: The bindingTime to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, BindingTimeEnum):
            raise TypeError(
                f"bindingTime must be BindingTimeEnum, got {type(value).__name__}"
            )
        self._bindingTime = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBindingTime(self) -> "BindingTimeEnum":
        """
        AUTOSAR-compliant getter for bindingTime.
        
        Returns:
            The bindingTime value
        
        Note:
            Delegates to binding_time property (CODING_RULE_V2_00017)
        """
        return self.binding_time  # Delegates to property

    def setBindingTime(self, value: "BindingTimeEnum") -> "ConditionByFormula":
        """
        AUTOSAR-compliant setter for bindingTime with method chaining.
        
        Args:
            value: The bindingTime to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to binding_time property setter (gets validation automatically)
        """
        self.binding_time = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_binding_time(self, value: "BindingTimeEnum") -> "ConditionByFormula":
        """
        Set bindingTime and return self for chaining.
        
        Args:
            value: The bindingTime to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_binding_time("value")
        """
        self.binding_time = value  # Use property setter (gets validation)
        return self