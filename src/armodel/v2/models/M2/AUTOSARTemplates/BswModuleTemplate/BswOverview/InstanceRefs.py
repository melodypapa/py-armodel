"""
AUTOSAR Package - InstanceRefs

Package: M2::AUTOSARTemplates::BswModuleTemplate::BswOverview::InstanceRefs
"""


from __future__ import annotations
from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class ModeInBswModuleDescriptionInstanceRef(ARObject):
    """

    Package: M2::AUTOSARTemplates::BswModuleTemplate::BswOverview::InstanceRefs::ModeInBswModuleDescriptionInstanceRef

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 323, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Stereotypes: atpDerived.
        self._base: Optional["BswModuleDescription"] = None

    @property
    def base(self) -> Optional["BswModuleDescription"]:
        """Get base (Pythonic accessor)."""
        return self._base

    @base.setter
    def base(self, value: Optional["BswModuleDescription"]) -> None:
        """
        Set base with validation.

        Args:
            value: The base to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._base = None
            return

        if not isinstance(value, BswModuleDescription):
            raise TypeError(
                f"base must be BswModuleDescription or None, got {type(value).__name__}"
            )
        self._base = value
        # sequenceOffset=20.
        self._contextModeGroup: Optional["RefType"] = None

    @property
    def context_mode_group(self) -> Optional["RefType"]:
        """Get contextModeGroup (Pythonic accessor)."""
        return self._contextModeGroup

    @context_mode_group.setter
    def context_mode_group(self, value: Optional["RefType"]) -> None:
        """
        Set contextModeGroup with validation.

        Args:
            value: The contextModeGroup to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._contextModeGroup = None
            return

        self._contextModeGroup = value
        # sequenceOffset=30.
        self._targetMode: Optional["ModeDeclaration"] = None

    @property
    def target_mode(self) -> Optional["ModeDeclaration"]:
        """Get targetMode (Pythonic accessor)."""
        return self._targetMode

    @target_mode.setter
    def target_mode(self, value: Optional["ModeDeclaration"]) -> None:
        """
        Set targetMode with validation.

        Args:
            value: The targetMode to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._targetMode = None
            return

        if not isinstance(value, ModeDeclaration):
            raise TypeError(
                f"targetMode must be ModeDeclaration or None, got {type(value).__name__}"
            )
        self._targetMode = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBase(self) -> "BswModuleDescription":
        """
        AUTOSAR-compliant getter for base.

        Returns:
            The base value

        Note:
            Delegates to base property (CODING_RULE_V2_00017)
        """
        return self.base  # Delegates to property

    def setBase(self, value: "BswModuleDescription") -> ModeInBswModuleDescriptionInstanceRef:
        """
        AUTOSAR-compliant setter for base with method chaining.

        Args:
            value: The base to set

        Returns:
            self for method chaining

        Note:
            Delegates to base property setter (gets validation automatically)
        """
        self.base = value  # Delegates to property setter
        return self

    def getContextModeGroup(self) -> "RefType":
        """
        AUTOSAR-compliant getter for contextModeGroup.

        Returns:
            The contextModeGroup value

        Note:
            Delegates to context_mode_group property (CODING_RULE_V2_00017)
        """
        return self.context_mode_group  # Delegates to property

    def setContextModeGroup(self, value: "RefType") -> ModeInBswModuleDescriptionInstanceRef:
        """
        AUTOSAR-compliant setter for contextModeGroup with method chaining.

        Args:
            value: The contextModeGroup to set

        Returns:
            self for method chaining

        Note:
            Delegates to context_mode_group property setter (gets validation automatically)
        """
        self.context_mode_group = value  # Delegates to property setter
        return self

    def getTargetMode(self) -> "ModeDeclaration":
        """
        AUTOSAR-compliant getter for targetMode.

        Returns:
            The targetMode value

        Note:
            Delegates to target_mode property (CODING_RULE_V2_00017)
        """
        return self.target_mode  # Delegates to property

    def setTargetMode(self, value: "ModeDeclaration") -> ModeInBswModuleDescriptionInstanceRef:
        """
        AUTOSAR-compliant setter for targetMode with method chaining.

        Args:
            value: The targetMode to set

        Returns:
            self for method chaining

        Note:
            Delegates to target_mode property setter (gets validation automatically)
        """
        self.target_mode = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_base(self, value: Optional["BswModuleDescription"]) -> ModeInBswModuleDescriptionInstanceRef:
        """
        Set base and return self for chaining.

        Args:
            value: The base to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_base("value")
        """
        self.base = value  # Use property setter (gets validation)
        return self

    def with_context_mode_group(self, value: Optional[RefType]) -> ModeInBswModuleDescriptionInstanceRef:
        """
        Set contextModeGroup and return self for chaining.

        Args:
            value: The contextModeGroup to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_context_mode_group("value")
        """
        self.context_mode_group = value  # Use property setter (gets validation)
        return self

    def with_target_mode(self, value: Optional["ModeDeclaration"]) -> ModeInBswModuleDescriptionInstanceRef:
        """
        Set targetMode and return self for chaining.

        Args:
            value: The targetMode to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_target_mode("value")
        """
        self.target_mode = value  # Use property setter (gets validation)
        return self
