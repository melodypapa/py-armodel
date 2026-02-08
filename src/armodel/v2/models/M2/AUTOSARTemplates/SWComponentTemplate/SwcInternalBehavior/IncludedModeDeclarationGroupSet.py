from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates import Identifier
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class IncludedModeDeclarationGroupSet(ARObject):
    """
    An IncludedModeDeclarationGroupSet declares that a set of
    ModeDeclarationGroups used by the software component for its implementation
    and consequently these ModeDeclarationGroups become part of the contract.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::ModeDeclarationGroup::IncludedModeDeclarationGroupSet

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 601, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the referenced ModeDeclarationGroup.
        self._mode: List[RefType] = []

    @property
    def mode(self) -> List[RefType]:
        """Get mode (Pythonic accessor)."""
        return self._mode
        # The prefix shall be used by the RTE generator as a prefix creation of symbols
        # related to the referenced RTE_TRANSITION_<Mode.
        self._prefix: Optional["Identifier"] = None

    @property
    def prefix(self) -> Optional["Identifier"]:
        """Get prefix (Pythonic accessor)."""
        return self._prefix

    @prefix.setter
    def prefix(self, value: Optional["Identifier"]) -> None:
        """
        Set prefix with validation.

        Args:
            value: The prefix to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._prefix = None
            return

        if not isinstance(value, Identifier):
            raise TypeError(
                f"prefix must be Identifier or None, got {type(value).__name__}"
            )
        self._prefix = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getMode(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for mode.

        Returns:
            The mode value

        Note:
            Delegates to mode property (CODING_RULE_V2_00017)
        """
        return self.mode  # Delegates to property

    def getPrefix(self) -> "Identifier":
        """
        AUTOSAR-compliant getter for prefix.

        Returns:
            The prefix value

        Note:
            Delegates to prefix property (CODING_RULE_V2_00017)
        """
        return self.prefix  # Delegates to property

    def setPrefix(self, value: "Identifier") -> "IncludedModeDeclarationGroupSet":
        """
        AUTOSAR-compliant setter for prefix with method chaining.

        Args:
            value: The prefix to set

        Returns:
            self for method chaining

        Note:
            Delegates to prefix property setter (gets validation automatically)
        """
        self.prefix = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_prefix(self, value: Optional["Identifier"]) -> "IncludedModeDeclarationGroupSet":
        """
        Set prefix and return self for chaining.

        Args:
            value: The prefix to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_prefix("value")
        """
        self.prefix = value  # Use property setter (gets validation)
        return self
