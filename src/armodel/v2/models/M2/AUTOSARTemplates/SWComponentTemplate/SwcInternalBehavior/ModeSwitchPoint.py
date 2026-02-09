from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.AccessCount import (
    AbstractAccessPoint,
)

    RefType,
)


class ModeSwitchPoint(AbstractAccessPoint):
    """
    A ModeSwitchPoint is required by a RunnableEntity owned a Mode Manager. Its
    semantics implies the ability to initiate a mode switch.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::ModeDeclarationGroup

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 323, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 633, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # by: PModeGroupInAtomic.
        self._modeGroupSwcInstanceRef: RefType = None

    @property
    def mode_group_swc_instance_ref(self) -> RefType:
        """Get modeGroupSwcInstanceRef (Pythonic accessor)."""
        return self._modeGroupSwcInstanceRef

    @mode_group_swc_instance_ref.setter
    def mode_group_swc_instance_ref(self, value: RefType) -> None:
        """
        Set modeGroupSwcInstanceRef with validation.

        Args:
            value: The modeGroupSwcInstanceRef to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._modeGroupSwcInstanceRef = None
            return

        self._modeGroupSwcInstanceRef = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getModeGroupSwcInstanceRef(self) -> RefType:
        """
        AUTOSAR-compliant getter for modeGroupSwcInstanceRef.

        Returns:
            The modeGroupSwcInstanceRef value

        Note:
            Delegates to mode_group_swc_instance_ref property (CODING_RULE_V2_00017)
        """
        return self.mode_group_swc_instance_ref  # Delegates to property

    def setModeGroupSwcInstanceRef(self, value: RefType) -> "ModeSwitchPoint":
        """
        AUTOSAR-compliant setter for modeGroupSwcInstanceRef with method chaining.

        Args:
            value: The modeGroupSwcInstanceRef to set

        Returns:
            self for method chaining

        Note:
            Delegates to mode_group_swc_instance_ref property setter (gets validation automatically)
        """
        self.mode_group_swc_instance_ref = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_mode_group_swc_instance_ref(self, value: Optional[RefType]) -> "ModeSwitchPoint":
        """
        Set modeGroupSwcInstanceRef and return self for chaining.

        Args:
            value: The modeGroupSwcInstanceRef to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_mode_group_swc_instance_ref("value")
        """
        self.mode_group_swc_instance_ref = value  # Use property setter (gets validation)
        return self
