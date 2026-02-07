from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class AutosarVariableInstance(Identifiable):
    """
    This class represents a reference to a variable instance within AUTOSAR.
    This way it is possible to reference a variable instance in the occurrence
    expression formula. The variable instance can target to one of the following
    variables: • a variable provided via a PortPrototype as whole • an element
    inside of a composite variable provided via a PortPrototype
    
    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingDescription::TimingDescription::AutosarVariableInstance
    
    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 85, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # by: VariableInComponent.
        self._variableInstanceInstanceRef: RefType = None

    @property
    def variable_instance_instance_ref(self) -> RefType:
        """Get variableInstanceInstanceRef (Pythonic accessor)."""
        return self._variableInstanceInstanceRef

    @variable_instance_instance_ref.setter
    def variable_instance_instance_ref(self, value: RefType) -> None:
        """
        Set variableInstanceInstanceRef with validation.
        
        Args:
            value: The variableInstanceInstanceRef to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._variableInstanceInstanceRef = None
            return

        self._variableInstanceInstanceRef = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getVariableInstanceInstanceRef(self) -> RefType:
        """
        AUTOSAR-compliant getter for variableInstanceInstanceRef.
        
        Returns:
            The variableInstanceInstanceRef value
        
        Note:
            Delegates to variable_instance_instance_ref property (CODING_RULE_V2_00017)
        """
        return self.variable_instance_instance_ref  # Delegates to property

    def setVariableInstanceInstanceRef(self, value: RefType) -> "AutosarVariableInstance":
        """
        AUTOSAR-compliant setter for variableInstanceInstanceRef with method chaining.
        
        Args:
            value: The variableInstanceInstanceRef to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to variable_instance_instance_ref property setter (gets validation automatically)
        """
        self.variable_instance_instance_ref = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_variable_instance_instance_ref(self, value: Optional[RefType]) -> "AutosarVariableInstance":
        """
        Set variableInstanceInstanceRef and return self for chaining.
        
        Args:
            value: The variableInstanceInstanceRef to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_variable_instance_instance_ref("value")
        """
        self.variable_instance_instance_ref = value  # Use property setter (gets validation)
        return self