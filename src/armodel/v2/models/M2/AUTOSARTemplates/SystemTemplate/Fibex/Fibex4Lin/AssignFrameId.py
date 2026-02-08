from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class AssignFrameId(LinConfigurationEntry):
    """
    Schedule entry for an Assign Frame Id master request.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Lin::LinCommunication::AssignFrameId

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 436, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The frame whose identifier is set by this assignment.
        self._assignedFrame: RefType = None

    @property
    def assigned_frame(self) -> RefType:
        """Get assignedFrame (Pythonic accessor)."""
        return self._assignedFrame

    @assigned_frame.setter
    def assigned_frame(self, value: RefType) -> None:
        """
        Set assignedFrame with validation.

        Args:
            value: The assignedFrame to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._assignedFrame = None
            return

        self._assignedFrame = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAssignedFrame(self) -> RefType:
        """
        AUTOSAR-compliant getter for assignedFrame.

        Returns:
            The assignedFrame value

        Note:
            Delegates to assigned_frame property (CODING_RULE_V2_00017)
        """
        return self.assigned_frame  # Delegates to property

    def setAssignedFrame(self, value: RefType) -> "AssignFrameId":
        """
        AUTOSAR-compliant setter for assignedFrame with method chaining.

        Args:
            value: The assignedFrame to set

        Returns:
            self for method chaining

        Note:
            Delegates to assigned_frame property setter (gets validation automatically)
        """
        self.assigned_frame = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_assigned_frame(self, value: Optional[RefType]) -> "AssignFrameId":
        """
        Set assignedFrame and return self for chaining.

        Args:
            value: The assignedFrame to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_assigned_frame("value")
        """
        self.assigned_frame = value  # Use property setter (gets validation)
        return self
