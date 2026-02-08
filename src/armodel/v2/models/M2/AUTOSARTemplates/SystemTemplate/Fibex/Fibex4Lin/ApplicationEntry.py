from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import ScheduleTableEntry
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class ApplicationEntry(ScheduleTableEntry):
    """
    Schedule table entry for application messages.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Lin::LinCommunication::ApplicationEntry

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 433, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Specifies the LinFrame that will be transmitted in this.
        self._frameTriggering: RefType = None

    @property
    def frame_triggering(self) -> RefType:
        """Get frameTriggering (Pythonic accessor)."""
        return self._frameTriggering

    @frame_triggering.setter
    def frame_triggering(self, value: RefType) -> None:
        """
        Set frameTriggering with validation.

        Args:
            value: The frameTriggering to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._frameTriggering = None
            return

        self._frameTriggering = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getFrameTriggering(self) -> RefType:
        """
        AUTOSAR-compliant getter for frameTriggering.

        Returns:
            The frameTriggering value

        Note:
            Delegates to frame_triggering property (CODING_RULE_V2_00017)
        """
        return self.frame_triggering  # Delegates to property

    def setFrameTriggering(self, value: RefType) -> "ApplicationEntry":
        """
        AUTOSAR-compliant setter for frameTriggering with method chaining.

        Args:
            value: The frameTriggering to set

        Returns:
            self for method chaining

        Note:
            Delegates to frame_triggering property setter (gets validation automatically)
        """
        self.frame_triggering = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_frame_triggering(self, value: Optional[RefType]) -> "ApplicationEntry":
        """
        Set frameTriggering and return self for chaining.

        Args:
            value: The frameTriggering to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_frame_triggering("value")
        """
        self.frame_triggering = value  # Use property setter (gets validation)
        return self
