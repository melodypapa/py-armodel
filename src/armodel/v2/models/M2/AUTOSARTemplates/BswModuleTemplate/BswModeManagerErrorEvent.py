from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
from armodel.v2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior import BswScheduleEvent

    RefType,
)


class BswModeManagerErrorEvent(BswScheduleEvent):
    """
    This represents the ability to react on errors occurring during mode
    handling.

    Package: M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 95, Classic
      Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the ModeDeclarationGroupPrototype for the error behavior of
        # the mode manager applies.
        self._modeGroup: RefType = None

    @property
    def mode_group(self) -> RefType:
        """Get modeGroup (Pythonic accessor)."""
        return self._modeGroup

    @mode_group.setter
    def mode_group(self, value: RefType) -> None:
        """
        Set modeGroup with validation.

        Args:
            value: The modeGroup to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._modeGroup = None
            return

        self._modeGroup = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getModeGroup(self) -> RefType:
        """
        AUTOSAR-compliant getter for modeGroup.

        Returns:
            The modeGroup value

        Note:
            Delegates to mode_group property (CODING_RULE_V2_00017)
        """
        return self.mode_group  # Delegates to property

    def setModeGroup(self, value: RefType) -> "BswModeManagerErrorEvent":
        """
        AUTOSAR-compliant setter for modeGroup with method chaining.

        Args:
            value: The modeGroup to set

        Returns:
            self for method chaining

        Note:
            Delegates to mode_group property setter (gets validation automatically)
        """
        self.mode_group = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_mode_group(self, value: Optional[RefType]) -> "BswModeManagerErrorEvent":
        """
        Set modeGroup and return self for chaining.

        Args:
            value: The modeGroup to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_mode_group("value")
        """
        self.mode_group = value  # Use property setter (gets validation)
        return self
