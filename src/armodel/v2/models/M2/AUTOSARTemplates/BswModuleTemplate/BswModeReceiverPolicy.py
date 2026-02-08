from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    RefType,
)


class BswModeReceiverPolicy(ARObject):
    """
    Specifies the details for the reception of a mode switch for the referred
    mode group.

    Package: M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior::BswModeReceiverPolicy

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 103, Classic
      Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This controls the creation of the enhanced mode API that information about
                # the previous mode and the next set to TRUE the enhanced mode API is be
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
        # The required mode group for which the policy is specified.
        self._requiredMode: RefType = None

    @property
    def required_mode(self) -> RefType:
        """Get requiredMode (Pythonic accessor)."""
        return self._requiredMode

    @required_mode.setter
    def required_mode(self, value: RefType) -> None:
        """
        Set requiredMode with validation.

        Args:
            value: The requiredMode to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._requiredMode = None
            return

        self._requiredMode = value
        # Specifies whether the module can handle the reception of asynchronous mode
        # switch (true) or not (false).
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

    def setEnhancedMode(self, value: "Boolean") -> "BswModeReceiverPolicy":
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

    def getRequiredMode(self) -> RefType:
        """
        AUTOSAR-compliant getter for requiredMode.

        Returns:
            The requiredMode value

        Note:
            Delegates to required_mode property (CODING_RULE_V2_00017)
        """
        return self.required_mode  # Delegates to property

    def setRequiredMode(self, value: RefType) -> "BswModeReceiverPolicy":
        """
        AUTOSAR-compliant setter for requiredMode with method chaining.

        Args:
            value: The requiredMode to set

        Returns:
            self for method chaining

        Note:
            Delegates to required_mode property setter (gets validation automatically)
        """
        self.required_mode = value  # Delegates to property setter
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

    def setSupports(self, value: "Boolean") -> "BswModeReceiverPolicy":
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

    def with_enhanced_mode(self, value: Optional["Boolean"]) -> "BswModeReceiverPolicy":
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

    def with_required_mode(self, value: Optional[RefType]) -> "BswModeReceiverPolicy":
        """
        Set requiredMode and return self for chaining.

        Args:
            value: The requiredMode to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_required_mode("value")
        """
        self.required_mode = value  # Use property setter (gets validation)
        return self

    def with_supports(self, value: Optional["Boolean"]) -> "BswModeReceiverPolicy":
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
