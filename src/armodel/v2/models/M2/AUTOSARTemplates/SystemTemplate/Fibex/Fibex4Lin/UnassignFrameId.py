from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class UnassignFrameId(LinConfigurationEntry):
    """
    Schedule entry for an Unassign Frame Id master request where the protected
    identifier is assigned the value 0x40. This will disable
    reception/transmission of a previously dynamically assigned frame
    identifier.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Lin::LinCommunication::UnassignFrameId

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 436, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The frame whose identifier is reset by this assignment.
        self._unassigned: RefType = None

    @property
    def unassigned(self) -> RefType:
        """Get unassigned (Pythonic accessor)."""
        return self._unassigned

    @unassigned.setter
    def unassigned(self, value: RefType) -> None:
        """
        Set unassigned with validation.

        Args:
            value: The unassigned to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._unassigned = None
            return

        self._unassigned = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getUnassigned(self) -> RefType:
        """
        AUTOSAR-compliant getter for unassigned.

        Returns:
            The unassigned value

        Note:
            Delegates to unassigned property (CODING_RULE_V2_00017)
        """
        return self.unassigned  # Delegates to property

    def setUnassigned(self, value: RefType) -> "UnassignFrameId":
        """
        AUTOSAR-compliant setter for unassigned with method chaining.

        Args:
            value: The unassigned to set

        Returns:
            self for method chaining

        Note:
            Delegates to unassigned property setter (gets validation automatically)
        """
        self.unassigned = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_unassigned(self, value: Optional[RefType]) -> "UnassignFrameId":
        """
        Set unassigned and return self for chaining.

        Args:
            value: The unassigned to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_unassigned("value")
        """
        self.unassigned = value  # Use property setter (gets validation)
        return self
