from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class EcuPartition(Identifiable):
    """
    Partitions are used as error containment regions. They permit the grouping
    of SWCs and resources and allow to describe recovery policies individually
    for each partition. Partitions can be terminated or restarted during
    run-time as a result of a detected error.

    Package: M2::AUTOSARTemplates::SystemTemplate::SWmapping::EcuPartition

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 201, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # A partition can execute either in CPU user mode (execIn = TRUE) or supervisor
                # mode (execInUser FALSE).
        # In user mode, the partition has a limited memory, to memory mapped hardware
                # and to user mode, the partition is mapped to a.
        self._execInUser: Optional["Boolean"] = None

    @property
    def exec_in_user(self) -> Optional["Boolean"]:
        """Get execInUser (Pythonic accessor)."""
        return self._execInUser

    @exec_in_user.setter
    def exec_in_user(self, value: Optional["Boolean"]) -> None:
        """
        Set execInUser with validation.

        Args:
            value: The execInUser to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._execInUser = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"execInUser must be Boolean or None, got {type(value).__name__}"
            )
        self._execInUser = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getExecInUser(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for execInUser.

        Returns:
            The execInUser value

        Note:
            Delegates to exec_in_user property (CODING_RULE_V2_00017)
        """
        return self.exec_in_user  # Delegates to property

    def setExecInUser(self, value: "Boolean") -> "EcuPartition":
        """
        AUTOSAR-compliant setter for execInUser with method chaining.

        Args:
            value: The execInUser to set

        Returns:
            self for method chaining

        Note:
            Delegates to exec_in_user property setter (gets validation automatically)
        """
        self.exec_in_user = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_exec_in_user(self, value: Optional["Boolean"]) -> "EcuPartition":
        """
        Set execInUser and return self for chaining.

        Args:
            value: The execInUser to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_exec_in_user("value")
        """
        self.exec_in_user = value  # Use property setter (gets validation)
        return self
