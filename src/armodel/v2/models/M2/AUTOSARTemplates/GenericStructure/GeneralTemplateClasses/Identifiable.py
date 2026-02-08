"""
Identifiable AUTOSAR object - extensible for V2 modules.

Package: M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::Identifiable
"""
from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class Identifiable(ARObject):
    """
    Package: M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::Identifiable
    Identifiable AUTOSAR object - extensible for V2 modules.

    This class represents AUTOSAR objects that have a short name identifier.
    It serves as a base class for most AUTOSAR model elements.

    Extension Points:
    - short_name: Core AUTOSAR identifier
    - _extended_attributes: Custom properties for V2 modules
    - Can be extended by subclasses for module-specific attributes
    """

    def __init__(self) -> None:
        """Initialize Identifiable with short name and extensible attributes."""
        super().__init__()
        # Core AUTOSAR attribute (private)
        self._short_name: Optional[str] = None

        # V2 extended attributes for custom properties
        # Example: adminData, category, etc. can be added by modules
        self.setExtendedAttribute("adminData", None)
        self.setExtendedAttribute("category", None)

    @property
    def short_name(self) -> Optional[str]:
        """
        Get the short name of this identifiable object (Pythonic accessor).

        Returns:
            Short name or None if not set.
        """
        return self._short_name

    @short_name.setter
    def short_name(self, short_name: str) -> None:
        """
        Set the short name of this identifiable object (Pythonic setter).

        Args:
            short_name: The short name to set.
        """
        self._short_name = short_name

    def getShortName(self) -> Optional[str]:
        """
        Get the short name of this identifiable object (AUTOSAR-compatible method).

        Returns:
            Short name or None if not set.
        """
        return self._short_name

    def setShortName(self, short_name: str) -> "Identifiable":
        """
        Set the short name of this identifiable object (AUTOSAR-compatible method).

        Args:
            short_name: The short name to set.

        Returns:
            Self for method chaining.
        """
        self._short_name = short_name
        return self


