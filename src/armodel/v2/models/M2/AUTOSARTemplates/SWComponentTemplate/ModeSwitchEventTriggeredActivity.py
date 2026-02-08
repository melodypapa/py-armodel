from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class ModeSwitchEventTriggeredActivity(ARObject):
    """
    This meta-class defines an activity of the NvBlockSwComponentType for a
    specific NvBlock which is triggered by a ModeSwitchEvent.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::NvBlockComponent

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 675, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute indicates which service of the NvM for the be requested.
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
        # This reference identifies the SwcModeSwitchEvent that the activity.
        self._swcModeSwitch: Optional["SwcModeSwitchEvent"] = None

    @property
    def swc_mode_switch(self) -> Optional["SwcModeSwitchEvent"]:
        """Get swcModeSwitch (Pythonic accessor)."""
        return self._swcModeSwitch

    @swc_mode_switch.setter
    def swc_mode_switch(self, value: Optional["SwcModeSwitchEvent"]) -> None:
        """
        Set swcModeSwitch with validation.

        Args:
            value: The swcModeSwitch to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._swcModeSwitch = None
            return

        if not isinstance(value, SwcModeSwitchEvent):
            raise TypeError(
                f"swcModeSwitch must be SwcModeSwitchEvent or None, got {type(value).__name__}"
            )
        self._swcModeSwitch = value

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

    def setRole(self, value: "Identifier") -> "ModeSwitchEventTriggeredActivity":
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

    def getSwcModeSwitch(self) -> "SwcModeSwitchEvent":
        """
        AUTOSAR-compliant getter for swcModeSwitch.

        Returns:
            The swcModeSwitch value

        Note:
            Delegates to swc_mode_switch property (CODING_RULE_V2_00017)
        """
        return self.swc_mode_switch  # Delegates to property

    def setSwcModeSwitch(self, value: "SwcModeSwitchEvent") -> "ModeSwitchEventTriggeredActivity":
        """
        AUTOSAR-compliant setter for swcModeSwitch with method chaining.

        Args:
            value: The swcModeSwitch to set

        Returns:
            self for method chaining

        Note:
            Delegates to swc_mode_switch property setter (gets validation automatically)
        """
        self.swc_mode_switch = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_role(self, value: Optional["Identifier"]) -> "ModeSwitchEventTriggeredActivity":
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

    def with_swc_mode_switch(self, value: Optional["SwcModeSwitchEvent"]) -> "ModeSwitchEventTriggeredActivity":
        """
        Set swcModeSwitch and return self for chaining.

        Args:
            value: The swcModeSwitch to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_swc_mode_switch("value")
        """
        self.swc_mode_switch = value  # Use property setter (gets validation)
        return self
