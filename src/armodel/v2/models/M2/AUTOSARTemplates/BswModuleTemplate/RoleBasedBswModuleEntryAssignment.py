from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    BswModuleEntry,
    Identifier,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class RoleBasedBswModuleEntryAssignment(ARObject):
    """
    This class specifies an assignment of a role to a particular BswModuleEntry
    (usually a configurable callback). With this assignment, the role of the
    callback is mapped to a specific ServiceNeeds element, so that a tool is
    able to create appropriate configuration values for the module that
    implements the AUTOSAR Service.

    Package: M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior::RoleBasedBswModuleEntryAssignment

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 226, Classic
      Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The assigned entry.
        # It should be an implementedEntry or the module or cluster that requires the.
        self._assignedEntry: Optional["BswModuleEntry"] = None

    @property
    def assigned_entry(self) -> Optional["BswModuleEntry"]:
        """Get assignedEntry (Pythonic accessor)."""
        return self._assignedEntry

    @assigned_entry.setter
    def assigned_entry(self, value: Optional["BswModuleEntry"]) -> None:
        """
        Set assignedEntry with validation.

        Args:
            value: The assignedEntry to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._assignedEntry = None
            return

        if not isinstance(value, BswModuleEntry):
            raise TypeError(
                f"assignedEntry must be BswModuleEntry or None, got {type(value).__name__}"
            )
        self._assignedEntry = value
        # This is the role of the assigned BswModuleEntry in the The attribute is
                # required (for example) kind of callbacks may be associated same ServiceNeeds
                # (e.
        # g.
        # end-notification vs.
        # shall be the role name of a configurable (usually a callback) as standardized
                # in the of the related AUTOSAR Service.
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

    def getAssignedEntry(self) -> "BswModuleEntry":
        """
        AUTOSAR-compliant getter for assignedEntry.

        Returns:
            The assignedEntry value

        Note:
            Delegates to assigned_entry property (CODING_RULE_V2_00017)
        """
        return self.assigned_entry  # Delegates to property

    def setAssignedEntry(self, value: "BswModuleEntry") -> "RoleBasedBswModuleEntryAssignment":
        """
        AUTOSAR-compliant setter for assignedEntry with method chaining.

        Args:
            value: The assignedEntry to set

        Returns:
            self for method chaining

        Note:
            Delegates to assigned_entry property setter (gets validation automatically)
        """
        self.assigned_entry = value  # Delegates to property setter
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

    def setRole(self, value: "Identifier") -> "RoleBasedBswModuleEntryAssignment":
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

    def with_assigned_entry(self, value: Optional["BswModuleEntry"]) -> "RoleBasedBswModuleEntryAssignment":
        """
        Set assignedEntry and return self for chaining.

        Args:
            value: The assignedEntry to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_assigned_entry("value")
        """
        self.assigned_entry = value  # Use property setter (gets validation)
        return self

    def with_role(self, value: Optional["Identifier"]) -> "RoleBasedBswModuleEntryAssignment":
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
