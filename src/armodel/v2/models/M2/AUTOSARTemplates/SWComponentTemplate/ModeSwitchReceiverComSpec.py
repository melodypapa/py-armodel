from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import RPortComSpec

    RefType,
)


class ModeSwitchReceiverComSpec(RPortComSpec):
    """
    Communication attributes of RPortPrototypes with respect to mode
    communication

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Communication::ModeSwitchReceiverComSpec

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 191, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This controls the creation of the enhanced mode API that information about
                # the previous mode and the next set to "true" the enhanced mode API is be
                # generated.
        # For more details please refer SWS_RTE.
        self._enhancedMode: Optional["Boolean"] = None

    @property
    def enhanced_mode(self) -> Optional["Boolean"]:
        """Get enhancedMode (Pythonic accessor)."""
        return self._enhancedMode

    @enhanced_mode.setter
    def enhanced_mode(self, value: Optional["Boolean"]) -> None:
        """
        Set enhancedMode with validation.

        Args:
            value: The enhancedMode to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._enhancedMode = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"enhancedMode must be Boolean or None, got {type(value).__name__}"
            )
        self._enhancedMode = value
        # ModeDeclarationGroupPrototype (of the same Port to which these communication
        # attributes apply.
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
        # This attribute controls the behavior of the corresponding with respect to the
                # question whether it deal with asynchronous mode switch requests, i.
        # e.
        # if true, the RPortPrototype is able to deal with an switch request.
        self._supports: Optional["Boolean"] = None

    @property
    def supports(self) -> Optional["Boolean"]:
        """Get supports (Pythonic accessor)."""
        return self._supports

    @supports.setter
    def supports(self, value: Optional["Boolean"]) -> None:
        """
        Set supports with validation.

        Args:
            value: The supports to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._supports = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"supports must be Boolean or None, got {type(value).__name__}"
            )
        self._supports = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getEnhancedMode(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for enhancedMode.

        Returns:
            The enhancedMode value

        Note:
            Delegates to enhanced_mode property (CODING_RULE_V2_00017)
        """
        return self.enhanced_mode  # Delegates to property

    def setEnhancedMode(self, value: "Boolean") -> "ModeSwitchReceiverComSpec":
        """
        AUTOSAR-compliant setter for enhancedMode with method chaining.

        Args:
            value: The enhancedMode to set

        Returns:
            self for method chaining

        Note:
            Delegates to enhanced_mode property setter (gets validation automatically)
        """
        self.enhanced_mode = value  # Delegates to property setter
        return self

    def getModeGroup(self) -> RefType:
        """
        AUTOSAR-compliant getter for modeGroup.

        Returns:
            The modeGroup value

        Note:
            Delegates to mode_group property (CODING_RULE_V2_00017)
        """
        return self.mode_group  # Delegates to property

    def setModeGroup(self, value: RefType) -> "ModeSwitchReceiverComSpec":
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

    def getSupports(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for supports.

        Returns:
            The supports value

        Note:
            Delegates to supports property (CODING_RULE_V2_00017)
        """
        return self.supports  # Delegates to property

    def setSupports(self, value: "Boolean") -> "ModeSwitchReceiverComSpec":
        """
        AUTOSAR-compliant setter for supports with method chaining.

        Args:
            value: The supports to set

        Returns:
            self for method chaining

        Note:
            Delegates to supports property setter (gets validation automatically)
        """
        self.supports = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_enhanced_mode(self, value: Optional["Boolean"]) -> "ModeSwitchReceiverComSpec":
        """
        Set enhancedMode and return self for chaining.

        Args:
            value: The enhancedMode to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_enhanced_mode("value")
        """
        self.enhanced_mode = value  # Use property setter (gets validation)
        return self

    def with_mode_group(self, value: Optional[RefType]) -> "ModeSwitchReceiverComSpec":
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

    def with_supports(self, value: Optional["Boolean"]) -> "ModeSwitchReceiverComSpec":
        """
        Set supports and return self for chaining.

        Args:
            value: The supports to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_supports("value")
        """
        self.supports = value  # Use property setter (gets validation)
        return self
