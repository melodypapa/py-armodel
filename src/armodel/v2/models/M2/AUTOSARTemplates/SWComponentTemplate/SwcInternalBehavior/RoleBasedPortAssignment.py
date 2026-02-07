from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class RoleBasedPortAssignment(ARObject):
    """
    This class specifies an assignment of a role to a particular service port
    (RPortPrototype or PPort Prototype) of an AtomicSwComponentType. With this
    assignment, the role of the service port can be mapped to a specific
    ServiceNeeds element, so that a tool is able to create the correct
    connector.
    
    Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::ServiceMapping::RoleBasedPortAssignment
    
    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 329, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 166, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 604, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2050, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Service PortPrototype used in the assigned role.
        # This either belong to the same AtomicSw the SwcInternalBehavior which owns or
                # to the same NvBlockSw the NvBlockDescriptor.
        self._portPrototype: RefType = None

    @property
    def port_prototype(self) -> RefType:
        """Get portPrototype (Pythonic accessor)."""
        return self._portPrototype

    @port_prototype.setter
    def port_prototype(self, value: RefType) -> None:
        """
        Set portPrototype with validation.
        
        Args:
            value: The portPrototype to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._portPrototype = None
            return

        self._portPrototype = value
        # This is the role of the assigned Port in the given context.
        # shall be a shortName of the Blueprint of a Port standardized in the Software
                # Specification of AUTOSAR Service.
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

    def getPortPrototype(self) -> RefType:
        """
        AUTOSAR-compliant getter for portPrototype.
        
        Returns:
            The portPrototype value
        
        Note:
            Delegates to port_prototype property (CODING_RULE_V2_00017)
        """
        return self.port_prototype  # Delegates to property

    def setPortPrototype(self, value: RefType) -> "RoleBasedPortAssignment":
        """
        AUTOSAR-compliant setter for portPrototype with method chaining.
        
        Args:
            value: The portPrototype to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to port_prototype property setter (gets validation automatically)
        """
        self.port_prototype = value  # Delegates to property setter
        return self

    def getRole(self) -> "Identifier":
        """
        AUTOSAR-compliant getter for role.
        
        Returns:
            The role value
        
        Note:
            Delegates to role property (CODING_RULE_V2_00017)
        """
        return self.role  # Delegates to property

    def setRole(self, value: "Identifier") -> "RoleBasedPortAssignment":
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

    def with_port_prototype(self, value: Optional[RefType]) -> "RoleBasedPortAssignment":
        """
        Set portPrototype and return self for chaining.
        
        Args:
            value: The portPrototype to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_port_prototype("value")
        """
        self.port_prototype = value  # Use property setter (gets validation)
        return self

    def with_role(self, value: Optional["Identifier"]) -> "RoleBasedPortAssignment":
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