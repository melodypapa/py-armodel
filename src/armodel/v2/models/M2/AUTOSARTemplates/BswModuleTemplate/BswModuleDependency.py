from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class BswModuleDependency(Identifiable):
    """
    This class collects the dependencies of a BSW module or cluster on a certain
    other BSW module.

    Package: M2::AUTOSARTemplates::BswModuleTemplate::BswInterfaces

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 47, Classic
      Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # AUTOSAR identifier of the target module of which the defined.
        # is optional, because the target module be identified by targetModuleRef.
        # 381 Document ID 89: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate Module
                # Description Template R23-11.
        self._targetModuleId: Optional["PositiveInteger"] = None

    @property
    def target_module_id(self) -> Optional["PositiveInteger"]:
        """Get targetModuleId (Pythonic accessor)."""
        return self._targetModuleId

    @target_module_id.setter
    def target_module_id(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set targetModuleId with validation.

        Args:
            value: The targetModuleId to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._targetModuleId = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"targetModuleId must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._targetModuleId = value
        # Reference to the target module.
        # It is an <<atpUriDef>> the reference shall be used to identify the target
                # actually needing the description of that atpUriDef; atpVariation.
        self._targetModule: Optional["BswModuleDescription"] = None

    @property
    def target_module(self) -> Optional["BswModuleDescription"]:
        """Get targetModule (Pythonic accessor)."""
        return self._targetModule

    @target_module.setter
    def target_module(self, value: Optional["BswModuleDescription"]) -> None:
        """
        Set targetModule with validation.

        Args:
            value: The targetModule to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._targetModule = None
            return

        if not isinstance(value, BswModuleDescription):
            raise TypeError(
                f"targetModule must be BswModuleDescription or None, got {type(value).__name__}"
            )
        self._targetModule = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTargetModuleId(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for targetModuleId.

        Returns:
            The targetModuleId value

        Note:
            Delegates to target_module_id property (CODING_RULE_V2_00017)
        """
        return self.target_module_id  # Delegates to property

    def setTargetModuleId(self, value: "PositiveInteger") -> "BswModuleDependency":
        """
        AUTOSAR-compliant setter for targetModuleId with method chaining.

        Args:
            value: The targetModuleId to set

        Returns:
            self for method chaining

        Note:
            Delegates to target_module_id property setter (gets validation automatically)
        """
        self.target_module_id = value  # Delegates to property setter
        return self

    def getTargetModule(self) -> "BswModuleDescription":
        """
        AUTOSAR-compliant getter for targetModule.

        Returns:
            The targetModule value

        Note:
            Delegates to target_module property (CODING_RULE_V2_00017)
        """
        return self.target_module  # Delegates to property

    def setTargetModule(self, value: "BswModuleDescription") -> "BswModuleDependency":
        """
        AUTOSAR-compliant setter for targetModule with method chaining.

        Args:
            value: The targetModule to set

        Returns:
            self for method chaining

        Note:
            Delegates to target_module property setter (gets validation automatically)
        """
        self.target_module = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_target_module_id(self, value: Optional["PositiveInteger"]) -> "BswModuleDependency":
        """
        Set targetModuleId and return self for chaining.

        Args:
            value: The targetModuleId to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_target_module_id("value")
        """
        self.target_module_id = value  # Use property setter (gets validation)
        return self

    def with_target_module(self, value: Optional["BswModuleDescription"]) -> "BswModuleDependency":
        """
        Set targetModule and return self for chaining.

        Args:
            value: The targetModule to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_target_module("value")
        """
        self.target_module = value  # Use property setter (gets validation)
        return self
