from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class ModeDeclarationGroupPrototypeMapping(ARObject):
    """
    Defines the mapping of two particular ModeDeclarationGroupPrototypes (in the
    given context) that are unequally named and/or require a reference to a
    ModeDeclarationMappingSet in order to become compatible by definition of
    ModeDeclarationMappings.

    Package: M2::AUTOSARTemplates::CommonStructure::ModeDeclaration

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 130, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # ModeDeclarationGroupPrototype to be mapped.
        self._firstModeGroupPrototype: RefType = None

    @property
    def first_mode_group_prototype(self) -> RefType:
        """Get firstModeGroupPrototype (Pythonic accessor)."""
        return self._firstModeGroupPrototype

    @first_mode_group_prototype.setter
    def first_mode_group_prototype(self, value: RefType) -> None:
        """
        Set firstModeGroupPrototype with validation.

        Args:
            value: The firstModeGroupPrototype to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._firstModeGroupPrototype = None
            return

        self._firstModeGroupPrototype = value
        # This represents the available mappings of Mode Declarations in the context ot
        # this ModeDeclarationGroup.
        self._mode: Optional["ModeDeclaration"] = None

    @property
    def mode(self) -> Optional["ModeDeclaration"]:
        """Get mode (Pythonic accessor)."""
        return self._mode

    @mode.setter
    def mode(self, value: Optional["ModeDeclaration"]) -> None:
        """
        Set mode with validation.

        Args:
            value: The mode to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._mode = None
            return

        if not isinstance(value, ModeDeclaration):
            raise TypeError(
                f"mode must be ModeDeclaration or None, got {type(value).__name__}"
            )
        self._mode = value
        # ModeDeclarationGroupPrototype to be mapped.
        self._secondMode: RefType = None

    @property
    def second_mode(self) -> RefType:
        """Get secondMode (Pythonic accessor)."""
        return self._secondMode

    @second_mode.setter
    def second_mode(self, value: RefType) -> None:
        """
        Set secondMode with validation.

        Args:
            value: The secondMode to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._secondMode = None
            return

        self._secondMode = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getFirstModeGroupPrototype(self) -> RefType:
        """
        AUTOSAR-compliant getter for firstModeGroupPrototype.

        Returns:
            The firstModeGroupPrototype value

        Note:
            Delegates to first_mode_group_prototype property (CODING_RULE_V2_00017)
        """
        return self.first_mode_group_prototype  # Delegates to property

    def setFirstModeGroupPrototype(self, value: RefType) -> "ModeDeclarationGroupPrototypeMapping":
        """
        AUTOSAR-compliant setter for firstModeGroupPrototype with method chaining.

        Args:
            value: The firstModeGroupPrototype to set

        Returns:
            self for method chaining

        Note:
            Delegates to first_mode_group_prototype property setter (gets validation automatically)
        """
        self.first_mode_group_prototype = value  # Delegates to property setter
        return self

    def getMode(self) -> "ModeDeclaration":
        """
        AUTOSAR-compliant getter for mode.

        Returns:
            The mode value

        Note:
            Delegates to mode property (CODING_RULE_V2_00017)
        """
        return self.mode  # Delegates to property

    def setMode(self, value: "ModeDeclaration") -> "ModeDeclarationGroupPrototypeMapping":
        """
        AUTOSAR-compliant setter for mode with method chaining.

        Args:
            value: The mode to set

        Returns:
            self for method chaining

        Note:
            Delegates to mode property setter (gets validation automatically)
        """
        self.mode = value  # Delegates to property setter
        return self

    def getSecondMode(self) -> RefType:
        """
        AUTOSAR-compliant getter for secondMode.

        Returns:
            The secondMode value

        Note:
            Delegates to second_mode property (CODING_RULE_V2_00017)
        """
        return self.second_mode  # Delegates to property

    def setSecondMode(self, value: RefType) -> "ModeDeclarationGroupPrototypeMapping":
        """
        AUTOSAR-compliant setter for secondMode with method chaining.

        Args:
            value: The secondMode to set

        Returns:
            self for method chaining

        Note:
            Delegates to second_mode property setter (gets validation automatically)
        """
        self.second_mode = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_first_mode_group_prototype(self, value: Optional[RefType]) -> "ModeDeclarationGroupPrototypeMapping":
        """
        Set firstModeGroupPrototype and return self for chaining.

        Args:
            value: The firstModeGroupPrototype to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_first_mode_group_prototype("value")
        """
        self.first_mode_group_prototype = value  # Use property setter (gets validation)
        return self

    def with_mode(self, value: Optional["ModeDeclaration"]) -> "ModeDeclarationGroupPrototypeMapping":
        """
        Set mode and return self for chaining.

        Args:
            value: The mode to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_mode("value")
        """
        self.mode = value  # Use property setter (gets validation)
        return self

    def with_second_mode(self, value: Optional[RefType]) -> "ModeDeclarationGroupPrototypeMapping":
        """
        Set secondMode and return self for chaining.

        Args:
            value: The secondMode to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_second_mode("value")
        """
        self.second_mode = value  # Use property setter (gets validation)
        return self
