"""
AUTOSAR Package - ServiceMapping

Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::ServiceMapping
"""


from __future__ import annotations
from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
    RefType,
)
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import (
    ServiceDependency,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class RoleBasedDataTypeAssignment(ARObject):
    """
    This class specifies an assignment of a role to a particular data type of a
    software component (or in the BswModuleBehavior of a module or cluster) in
    the context of an AUTOSAR Service. With this assignment, the role of the
    data type can be mapped to a specific ServiceNeeds element, so that a tool
    is able to create the correct access.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::ServiceMapping::RoleBasedDataTypeAssignment

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 227, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 610, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This is the role of the associated data type in the given.
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

        if not isinstance(value, (Identifier, str)):
            raise TypeError(
                f"role must be Identifier or str or None, got {type(value).__name__}"
            )
        self._role = value
        self._used: Optional["ImplementationData"] = None

    @property
    def used(self) -> Optional["ImplementationData"]:
        """Get used (Pythonic accessor)."""
        return self._used

    @used.setter
    def used(self, value: Optional["ImplementationData"]) -> None:
        """
        Set used with validation.

        Args:
            value: The used to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._used = None
            return

        if not isinstance(value, ImplementationData):
            raise TypeError(
                f"used must be ImplementationData or None, got {type(value).__name__}"
            )
        self._used = value

    def with_assigned_data(self, value):
        """
        Set assigned_data and return self for chaining.

        Args:
            value: The assigned_data to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_assigned_data("value")
        """
        self.assigned_data = value  # Use property setter (gets validation)
        return self

    def with_assigned_port(self, value):
        """
        Set assigned_port and return self for chaining.

        Args:
            value: The assigned_port to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_assigned_port("value")
        """
        self.assigned_port = value  # Use property setter (gets validation)
        return self

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

    def setRole(self, value: "Identifier") -> RoleBasedDataTypeAssignment:
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

    def getUsed(self) -> "ImplementationData":
        """
        AUTOSAR-compliant getter for used.

        Returns:
            The used value

        Note:
            Delegates to used property (CODING_RULE_V2_00017)
        """
        return self.used  # Delegates to property

    def setUsed(self, value: "ImplementationData") -> RoleBasedDataTypeAssignment:
        """
        AUTOSAR-compliant setter for used with method chaining.

        Args:
            value: The used to set

        Returns:
            self for method chaining

        Note:
            Delegates to used property setter (gets validation automatically)
        """
        self.used = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_role(self, value: Optional["Identifier"]) -> RoleBasedDataTypeAssignment:
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

    def with_used(self, value: Optional["ImplementationData"]) -> RoleBasedDataTypeAssignment:
        """
        Set used and return self for chaining.

        Args:
            value: The used to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_used("value")
        """
        self.used = value  # Use property setter (gets validation)
        return self



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
        self._portPrototype: Optional["RefType"] = None

    @property
    def port_prototype(self) -> Optional["RefType"]:
        """Get portPrototype (Pythonic accessor)."""
        return self._portPrototype

    @port_prototype.setter
    def port_prototype(self, value: Optional["RefType"]) -> None:
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

        if not isinstance(value, (Identifier, str)):
            raise TypeError(
                f"role must be Identifier or str or None, got {type(value).__name__}"
            )
        self._role = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getPortPrototype(self) -> "RefType":
        """
        AUTOSAR-compliant getter for portPrototype.

        Returns:
            The portPrototype value

        Note:
            Delegates to port_prototype property (CODING_RULE_V2_00017)
        """
        return self.port_prototype  # Delegates to property

    def setPortPrototype(self, value: "RefType") -> RoleBasedPortAssignment:
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

    def setRole(self, value: "Identifier") -> RoleBasedPortAssignment:
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

    def with_port_prototype(self, value: Optional[RefType]) -> RoleBasedPortAssignment:
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

    def with_role(self, value: Optional["Identifier"]) -> RoleBasedPortAssignment:
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



class SwcServiceDependency(ServiceDependency):
    """
    Specialization of ServiceDependency in the context of an
    SwcInternalBehavior. It allows to associate ports, port groups and (in
    special cases) data defined for an atomic software component to a given
    ServiceNeeds element. (cid:53) 224 of 719 Document ID 673:
    AUTOSAR_CP_TPS_DiagnosticExtractTemplate Diagnostic Extract Template AUTOSAR
    CP R23-11 (cid:52)

    Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::ServiceMapping::SwcServiceDependency

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 224, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 608, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Defines the role of an associated data object of the same atpVariation.
        self._assignedData: List["RoleBasedData"] = []

    @property
    def assigned_data(self) -> List["RoleBasedData"]:
        """Get assignedData (Pythonic accessor)."""
        return self._assignedData
        # Defines the role of an associated port of the same atpVariation.
        self._assignedPort: List["RoleBasedPort"] = []

    @property
    def assigned_port(self) -> List["RoleBasedPort"]:
        """Get assignedPort (Pythonic accessor)."""
        return self._assignedPort
        # This reference specifies an association between the and a PortGroup, for
                # example to request mode which applies for communication ports.
        # The referred PortGroup shall be local to SWC, but via the links between the
                # Port tool can evaluate this information such that all linked via this port
                # group on the same ECU can.
        self._representedPort: Optional["RefType"] = None

    @property
    def represented_port(self) -> Optional["RefType"]:
        """Get representedPort (Pythonic accessor)."""
        return self._representedPort

    @represented_port.setter
    def represented_port(self, value: Optional["RefType"]) -> None:
        """
        Set representedPort with validation.

        Args:
            value: The representedPort to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._representedPort = None
            return

        self._representedPort = value
        self._serviceNeeds: Optional["ServiceNeeds"] = None

    @property
    def service_needs(self) -> Optional["ServiceNeeds"]:
        """Get serviceNeeds (Pythonic accessor)."""
        return self._serviceNeeds

    @service_needs.setter
    def service_needs(self, value: Optional["ServiceNeeds"]) -> None:
        """
        Set serviceNeeds with validation.

        Args:
            value: The serviceNeeds to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._serviceNeeds = None
            return

        if not isinstance(value, ServiceNeeds):
            raise TypeError(
                f"serviceNeeds must be ServiceNeeds or None, got {type(value).__name__}"
            )
        self._serviceNeeds = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAssignedData(self) -> List["RoleBasedData"]:
        """
        AUTOSAR-compliant getter for assignedData.

        Returns:
            The assignedData value

        Note:
            Delegates to assigned_data property (CODING_RULE_V2_00017)
        """
        return self.assigned_data  # Delegates to property

    def getAssignedPort(self) -> List["RoleBasedPort"]:
        """
        AUTOSAR-compliant getter for assignedPort.

        Returns:
            The assignedPort value

        Note:
            Delegates to assigned_port property (CODING_RULE_V2_00017)
        """
        return self.assigned_port  # Delegates to property

    def getRepresentedPort(self) -> "RefType":
        """
        AUTOSAR-compliant getter for representedPort.

        Returns:
            The representedPort value

        Note:
            Delegates to represented_port property (CODING_RULE_V2_00017)
        """
        return self.represented_port  # Delegates to property

    def setRepresentedPort(self, value: "RefType") -> SwcServiceDependency:
        """
        AUTOSAR-compliant setter for representedPort with method chaining.

        Args:
            value: The representedPort to set

        Returns:
            self for method chaining

        Note:
            Delegates to represented_port property setter (gets validation automatically)
        """
        self.represented_port = value  # Delegates to property setter
        return self

    def getServiceNeeds(self) -> "ServiceNeeds":
        """
        AUTOSAR-compliant getter for serviceNeeds.

        Returns:
            The serviceNeeds value

        Note:
            Delegates to service_needs property (CODING_RULE_V2_00017)
        """
        return self.service_needs  # Delegates to property

    def setServiceNeeds(self, value: "ServiceNeeds") -> SwcServiceDependency:
        """
        AUTOSAR-compliant setter for serviceNeeds with method chaining.

        Args:
            value: The serviceNeeds to set

        Returns:
            self for method chaining

        Note:
            Delegates to service_needs property setter (gets validation automatically)
        """
        self.service_needs = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_represented_port(self, value: Optional[RefType]) -> SwcServiceDependency:
        """
        Set representedPort and return self for chaining.

        Args:
            value: The representedPort to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_represented_port("value")
        """
        self.represented_port = value  # Use property setter (gets validation)
        return self

    def with_service_needs(self, value: Optional["ServiceNeeds"]) -> SwcServiceDependency:
        """
        Set serviceNeeds and return self for chaining.

        Args:
            value: The serviceNeeds to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_service_needs("value")
        """
        self.service_needs = value  # Use property setter (gets validation)
        return self
