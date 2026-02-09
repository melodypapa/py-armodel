from typing import Optional

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

    Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::ServiceMapping

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

        if not isinstance(value, Identifier):
            raise TypeError(
                f"role must be Identifier or None, got {type(value).__name__}"
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

    def setRole(self, value: "Identifier") -> "RoleBasedDataTypeAssignment":
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

    def setUsed(self, value: "ImplementationData") -> "RoleBasedDataTypeAssignment":
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

    def with_role(self, value: Optional["Identifier"]) -> "RoleBasedDataTypeAssignment":
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

    def with_used(self, value: Optional["ImplementationData"]) -> "RoleBasedDataTypeAssignment":
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
