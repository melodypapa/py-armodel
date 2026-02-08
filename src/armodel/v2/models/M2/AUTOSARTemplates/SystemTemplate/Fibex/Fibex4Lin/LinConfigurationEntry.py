from abc import ABC
from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication import (
    ScheduleTableEntry,
)


class LinConfigurationEntry(ScheduleTableEntry, ABC):
    """
    A ScheduleTableEntry which contains LIN specific assignments.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Lin::LinCommunication

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 434, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is LinConfigurationEntry:
            raise TypeError("LinConfigurationEntry is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The LIN slaves controller who is target of this assignment.
        # in case LinConfigurationEntry.
        # assignedLinSlave.
        self._assigned: Optional["LinSlave"] = None

    @property
    def assigned(self) -> Optional["LinSlave"]:
        """Get assigned (Pythonic accessor)."""
        return self._assigned

    @assigned.setter
    def assigned(self, value: Optional["LinSlave"]) -> None:
        """
        Set assigned with validation.

        Args:
            value: The assigned to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._assigned = None
            return

        if not isinstance(value, LinSlave):
            raise TypeError(
                f"assigned must be LinSlave or None, got {type(value).__name__}"
            )
        self._assigned = value
        # The LIN slave that is target of this assignment.
        # note that this reference is redundant to the Ecu Extract of the LinMaster the
                # LinSlave Ecus shall available.
        # that is described here is necessary in the for the configuration of the
                # LinMaster.
        self._assignedLin: Optional["LinSlaveConfigIdent"] = None

    @property
    def assigned_lin(self) -> Optional["LinSlaveConfigIdent"]:
        """Get assignedLin (Pythonic accessor)."""
        return self._assignedLin

    @assigned_lin.setter
    def assigned_lin(self, value: Optional["LinSlaveConfigIdent"]) -> None:
        """
        Set assignedLin with validation.

        Args:
            value: The assignedLin to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._assignedLin = None
            return

        if not isinstance(value, LinSlaveConfigIdent):
            raise TypeError(
                f"assignedLin must be LinSlaveConfigIdent or None, got {type(value).__name__}"
            )
        self._assignedLin = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAssigned(self) -> "LinSlave":
        """
        AUTOSAR-compliant getter for assigned.

        Returns:
            The assigned value

        Note:
            Delegates to assigned property (CODING_RULE_V2_00017)
        """
        return self.assigned  # Delegates to property

    def setAssigned(self, value: "LinSlave") -> "LinConfigurationEntry":
        """
        AUTOSAR-compliant setter for assigned with method chaining.

        Args:
            value: The assigned to set

        Returns:
            self for method chaining

        Note:
            Delegates to assigned property setter (gets validation automatically)
        """
        self.assigned = value  # Delegates to property setter
        return self

    def getAssignedLin(self) -> "LinSlaveConfigIdent":
        """
        AUTOSAR-compliant getter for assignedLin.

        Returns:
            The assignedLin value

        Note:
            Delegates to assigned_lin property (CODING_RULE_V2_00017)
        """
        return self.assigned_lin  # Delegates to property

    def setAssignedLin(self, value: "LinSlaveConfigIdent") -> "LinConfigurationEntry":
        """
        AUTOSAR-compliant setter for assignedLin with method chaining.

        Args:
            value: The assignedLin to set

        Returns:
            self for method chaining

        Note:
            Delegates to assigned_lin property setter (gets validation automatically)
        """
        self.assigned_lin = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_assigned(self, value: Optional["LinSlave"]) -> "LinConfigurationEntry":
        """
        Set assigned and return self for chaining.

        Args:
            value: The assigned to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_assigned("value")
        """
        self.assigned = value  # Use property setter (gets validation)
        return self

    def with_assigned_lin(self, value: Optional["LinSlaveConfigIdent"]) -> "LinConfigurationEntry":
        """
        Set assignedLin and return self for chaining.

        Args:
            value: The assignedLin to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_assigned_lin("value")
        """
        self.assigned_lin = value  # Use property setter (gets validation)
        return self
