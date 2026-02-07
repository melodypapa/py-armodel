from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class RoleBasedDataAssignment(ARObject):
    """
    This class specifies an assignment of a role to a particular data object in
    either • the SwcInternalBehavior of a software component (or in the
    BswInternalBehavior of a BSW module or BSW cluster) in the context of an
    AUTOSAR Service or • an NvBlockDescriptor to sort out the assignment of
    event-based writing strategies to data elements in a PortPrototype. With
    this assignment, the role of the data can be mapped to a DataPrototype that
    is used in the context of the definition of a specific ServiceNeeds or
    NvBlockDescriptor, so that a tool is able to create the correct access or
    writing strategy.
    
    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::RoleBasedDataAssignment
    
    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 226, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 607, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This is the role of the assigned data in the given context.
        # need to be specified on M1 level.
        # TPS Software Component Template list of applicable roles for various service
                # service use cases in chapter 13 and Service Use Cases" (e.
        # g.
        # , case of the needs for a permanent RAM.
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
        # The VariableDataPrototype used in this role, e.
        # g.
        # Permanent RAM Block of an NVRAM Block which shall the same
                # SwcInternalBehavior or Bsw the role signalBasedDiagnostics it has to refer to
                # a a SenderReceiverInterface or.
        self._usedData: RefType = None

    @property
    def used_data(self) -> RefType:
        """Get usedData (Pythonic accessor)."""
        return self._usedData

    @used_data.setter
    def used_data(self, value: RefType) -> None:
        """
        Set usedData with validation.
        
        Args:
            value: The usedData to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._usedData = None
            return

        self._usedData = value
        # The ParameterDataPrototype used in this role, e.
        # g.
        # ROM Block of an NVRAM Block.
        # It shall belong to the or BswInternalbehavior.
        # the role signalBasedDiagnostics it has to refer to a a ParameterInterface.
        self._usedParameter: RefType = None

    @property
    def used_parameter(self) -> RefType:
        """Get usedParameter (Pythonic accessor)."""
        return self._usedParameter

    @used_parameter.setter
    def used_parameter(self, value: RefType) -> None:
        """
        Set usedParameter with validation.
        
        Args:
            value: The usedParameter to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._usedParameter = None
            return

        self._usedParameter = value
        # The (untyped) PerInstanceMemory used in this role (e.
        # g.
        # Permanent RAM Block for an NVRAM Block).
        self._usedPim: Optional["PerInstanceMemory"] = None

    @property
    def used_pim(self) -> Optional["PerInstanceMemory"]:
        """Get usedPim (Pythonic accessor)."""
        return self._usedPim

    @used_pim.setter
    def used_pim(self, value: Optional["PerInstanceMemory"]) -> None:
        """
        Set usedPim with validation.
        
        Args:
            value: The usedPim to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._usedPim = None
            return

        if not isinstance(value, PerInstanceMemory):
            raise TypeError(
                f"usedPim must be PerInstanceMemory or None, got {type(value).__name__}"
            )
        self._usedPim = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getRole(self) -> "Identifier":
        """
        AUTOSAR-compliant getter for role.
        
        Returns:
            The role value
        
        Note:
            Delegates to role property (CODING_RULE_V2_00017)
        """
        return self.role  # Delegates to property

    def setRole(self, value: "Identifier") -> "RoleBasedDataAssignment":
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

    def getUsedData(self) -> RefType:
        """
        AUTOSAR-compliant getter for usedData.
        
        Returns:
            The usedData value
        
        Note:
            Delegates to used_data property (CODING_RULE_V2_00017)
        """
        return self.used_data  # Delegates to property

    def setUsedData(self, value: RefType) -> "RoleBasedDataAssignment":
        """
        AUTOSAR-compliant setter for usedData with method chaining.
        
        Args:
            value: The usedData to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to used_data property setter (gets validation automatically)
        """
        self.used_data = value  # Delegates to property setter
        return self

    def getUsedParameter(self) -> RefType:
        """
        AUTOSAR-compliant getter for usedParameter.
        
        Returns:
            The usedParameter value
        
        Note:
            Delegates to used_parameter property (CODING_RULE_V2_00017)
        """
        return self.used_parameter  # Delegates to property

    def setUsedParameter(self, value: RefType) -> "RoleBasedDataAssignment":
        """
        AUTOSAR-compliant setter for usedParameter with method chaining.
        
        Args:
            value: The usedParameter to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to used_parameter property setter (gets validation automatically)
        """
        self.used_parameter = value  # Delegates to property setter
        return self

    def getUsedPim(self) -> "PerInstanceMemory":
        """
        AUTOSAR-compliant getter for usedPim.
        
        Returns:
            The usedPim value
        
        Note:
            Delegates to used_pim property (CODING_RULE_V2_00017)
        """
        return self.used_pim  # Delegates to property

    def setUsedPim(self, value: "PerInstanceMemory") -> "RoleBasedDataAssignment":
        """
        AUTOSAR-compliant setter for usedPim with method chaining.
        
        Args:
            value: The usedPim to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to used_pim property setter (gets validation automatically)
        """
        self.used_pim = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_role(self, value: Optional["Identifier"]) -> "RoleBasedDataAssignment":
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

    def with_used_data(self, value: Optional[RefType]) -> "RoleBasedDataAssignment":
        """
        Set usedData and return self for chaining.
        
        Args:
            value: The usedData to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_used_data("value")
        """
        self.used_data = value  # Use property setter (gets validation)
        return self

    def with_used_parameter(self, value: Optional[RefType]) -> "RoleBasedDataAssignment":
        """
        Set usedParameter and return self for chaining.
        
        Args:
            value: The usedParameter to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_used_parameter("value")
        """
        self.used_parameter = value  # Use property setter (gets validation)
        return self

    def with_used_pim(self, value: Optional["PerInstanceMemory"]) -> "RoleBasedDataAssignment":
        """
        Set usedPim and return self for chaining.
        
        Args:
            value: The usedPim to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_used_pim("value")
        """
        self.used_pim = value  # Use property setter (gets validation)
        return self