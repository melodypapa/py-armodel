from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Referrable import Referrable

class BswVariableAccess(Referrable):
    """
    The presence of a BswVariableAccess implies that a BswModuleEntity needs
    access to a VariableData Prototype via the BSW Scheduler. The kind of access
    is specified by the role in which the class is used.
    
    Package: M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior::BswVariableAccess
    
    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 81, Classic
      Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The data accessed via the BSW Scheduler.
        self._accessedVariable: RefType = None

    @property
    def accessed_variable(self) -> RefType:
        """Get accessedVariable (Pythonic accessor)."""
        return self._accessedVariable

    @accessed_variable.setter
    def accessed_variable(self, value: RefType) -> None:
        """
        Set accessedVariable with validation.
        
        Args:
            value: The accessedVariable to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._accessedVariable = None
            return

        self._accessedVariable = value
        # The existence of this reference indicates that the variable is received resp.
        # sent only in the context of the referred.
        self._context: List["BswDistinguished"] = []

    @property
    def context(self) -> List["BswDistinguished"]:
        """Get context (Pythonic accessor)."""
        return self._context

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAccessedVariable(self) -> RefType:
        """
        AUTOSAR-compliant getter for accessedVariable.
        
        Returns:
            The accessedVariable value
        
        Note:
            Delegates to accessed_variable property (CODING_RULE_V2_00017)
        """
        return self.accessed_variable  # Delegates to property

    def setAccessedVariable(self, value: RefType) -> "BswVariableAccess":
        """
        AUTOSAR-compliant setter for accessedVariable with method chaining.
        
        Args:
            value: The accessedVariable to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to accessed_variable property setter (gets validation automatically)
        """
        self.accessed_variable = value  # Delegates to property setter
        return self

    def getContext(self) -> List["BswDistinguished"]:
        """
        AUTOSAR-compliant getter for context.
        
        Returns:
            The context value
        
        Note:
            Delegates to context property (CODING_RULE_V2_00017)
        """
        return self.context  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_accessed_variable(self, value: Optional[RefType]) -> "BswVariableAccess":
        """
        Set accessedVariable and return self for chaining.
        
        Args:
            value: The accessedVariable to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_accessed_variable("value")
        """
        self.accessed_variable = value  # Use property setter (gets validation)
        return self