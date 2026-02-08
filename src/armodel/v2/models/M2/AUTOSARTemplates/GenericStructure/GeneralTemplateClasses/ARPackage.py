"""
AUTOSAR AR Package - extensible container for AUTOSAR elements.

Package: M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::ARPackage
"""
from typing import List

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class ARPackage(Identifiable):
    """
    Package: M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::ARPackage
    AUTOSAR AR Package - extensible container for AUTOSAR elements.

    This class represents an AUTOSAR package which can contain
    sub-packages and AUTOSAR elements.

    Extension Points:
    - ar_packages: List of sub-packages
    - elements: List of AUTOSAR elements
    - _extended_attributes: Custom properties for V2 modules
    - Can be extended for package-specific metadata
    """

    def __init__(self) -> None:
        """Initialize ARPackage with extensible structure."""
        super().__init__()
        # Core AUTOSAR attributes
        self.ar_packages: List["ARPackage"] = []
        self.elements: List[ARObject] = []

        # V2 extended attributes for custom properties
        # Example: package metadata, vendor info, etc.
        self.setExtendedAttribute("vendor", None)
        self.setExtendedAttribute("description", None)

    def addARPackage(self, package: "ARPackage") -> None:
        """
        Add a sub-package to this package.

        Args:
            package: The ARPackage to add.
        """
        self.ar_packages.append(package)
        package.parent = self

    def addElement(self, element: ARObject) -> None:
        """
        Add an AUTOSAR element to this package.

        Args:
            element: The ARObject element to add.
        """
        self.elements.append(element)
        element.parent = self

    def getARPackages(self) -> List["ARPackage"]:
        """
        Get all sub-packages in this package.

        Returns:
            List of ARPackage objects.
        """
        return self.ar_packages

    def getElements(self) -> List[ARObject]:
        """
        Get all elements in this package.

        Returns:
            List of ARObject elements.
        """
        return self.elements

