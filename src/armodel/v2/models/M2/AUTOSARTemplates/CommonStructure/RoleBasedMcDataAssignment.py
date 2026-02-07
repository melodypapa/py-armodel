from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class RoleBasedMcDataAssignment(ARObject):
    """
    This meta-class allows to define links that specify logical relationships
    between single McDataInstances. The details on the existence and semantics
    of such links are not standardized. Possible Use Case: Rapid Prototyping
    solutions in which additional communication buffers and switches are
    implemented in the RTE that allow to switch between the usage of the
    original and the bypass buffers. The different buffers and the switch can be
    represented by McDataInstances (in order to be accessed by MC tools) which
    have relationships to each other.
    
    Package: M2::AUTOSARTemplates::CommonStructure::MeasurementCalibrationSupport::RoleBasedMcDataAssignment
    
    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 329, Classic
      Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Determines the executionContext in which the McData describing a local (e.
        # g Task-Local) buffer of a is valid.
        self._execution: List["RptExecutionContext"] = []

    @property
    def execution(self) -> List["RptExecutionContext"]:
        """Get execution (Pythonic accessor)."""
        return self._execution
        # The target of the assignment.
        self._mcDataInstance: List["McDataInstance"] = []

    @property
    def mc_data_instance(self) -> List["McDataInstance"]:
        """Get mcDataInstance (Pythonic accessor)."""
        return self._mcDataInstance
        # Shall be used to specify the role of the assigned data relation to the
        # instance that owns the roles of the RoleBasedMcData are:.
        self._role: Optional["Identifier"] = None

    @property
    def role(self) -> Optional["Identifier"]:
        """Get role (Pythonic accessor)."""
        return self._role

    @role.setter
    def role(self, value: Optional["Identifier"]) -> None:
        """
        Set role with validation.
        
        Args:
            value: The role to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._role = None
            return

        if not isinstance(value, Identifier):
            raise TypeError(
                f"role must be Identifier or None, got {type(value).__name__}"
            )
        self._role = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getExecution(self) -> List["RptExecutionContext"]:
        """
        AUTOSAR-compliant getter for execution.
        
        Returns:
            The execution value
        
        Note:
            Delegates to execution property (CODING_RULE_V2_00017)
        """
        return self.execution  # Delegates to property

    def getMcDataInstance(self) -> List["McDataInstance"]:
        """
        AUTOSAR-compliant getter for mcDataInstance.
        
        Returns:
            The mcDataInstance value
        
        Note:
            Delegates to mc_data_instance property (CODING_RULE_V2_00017)
        """
        return self.mc_data_instance  # Delegates to property

    def getRole(self) -> "Identifier":
        """
        AUTOSAR-compliant getter for role.
        
        Returns:
            The role value
        
        Note:
            Delegates to role property (CODING_RULE_V2_00017)
        """
        return self.role  # Delegates to property

    def setRole(self, value: "Identifier") -> "RoleBasedMcDataAssignment":
        """
        AUTOSAR-compliant setter for role with method chaining.
        
        Args:
            value: The role to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to role property setter (gets validation automatically)
        """
        self.role = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_role(self, value: Optional["Identifier"]) -> "RoleBasedMcDataAssignment":
        """
        Set role and return self for chaining.
        
        Args:
            value: The role to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_role("value")
        """
        self.role = value  # Use property setter (gets validation)
        return self