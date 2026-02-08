from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import PortInterfaceMapping

    RefType,
)


class ModeInterfaceMapping(PortInterfaceMapping):
    """
    Defines the mapping of ModeDeclarationGroupPrototypes in context of two
    different ModeInterfaces.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::PortInterface

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 130, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Mapping of two ModeDeclarationGroupPrototypes in two ModeInterfaces.
        self._modeMapping: RefType = None

    @property
    def mode_mapping(self) -> RefType:
        """Get modeMapping (Pythonic accessor)."""
        return self._modeMapping

    @mode_mapping.setter
    def mode_mapping(self, value: RefType) -> None:
        """
        Set modeMapping with validation.

        Args:
            value: The modeMapping to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._modeMapping = None
            return

        self._modeMapping = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getModeMapping(self) -> RefType:
        """
        AUTOSAR-compliant getter for modeMapping.

        Returns:
            The modeMapping value

        Note:
            Delegates to mode_mapping property (CODING_RULE_V2_00017)
        """
        return self.mode_mapping  # Delegates to property

    def setModeMapping(self, value: RefType) -> "ModeInterfaceMapping":
        """
        AUTOSAR-compliant setter for modeMapping with method chaining.

        Args:
            value: The modeMapping to set

        Returns:
            self for method chaining

        Note:
            Delegates to mode_mapping property setter (gets validation automatically)
        """
        self.mode_mapping = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_mode_mapping(self, value: Optional[RefType]) -> "ModeInterfaceMapping":
        """
        Set modeMapping and return self for chaining.

        Args:
            value: The modeMapping to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_mode_mapping("value")
        """
        self.mode_mapping = value  # Use property setter (gets validation)
        return self
