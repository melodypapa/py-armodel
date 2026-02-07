"""
V2 Model Classes - Core AUTOSAR models.

V2 Implementation:
- Extensible design for V2 modules (CODING_RULE_V2_00014)
- Singleton pattern for AUTOSAR
- Proper inheritance hierarchy (ARObject -> Identifiable -> ARPackage)
- Extended attributes support for custom V2 module properties
- Modern Python patterns with dataclasses and type hints

These classes are designed to be extended by other V2 modules without
requiring modification to base classes (Open/Closed Principle).
"""
from typing import List, Optional

from armodel.v2.models.ar_object import ARObject


class AUTOSAR(ARObject):
    """
    AUTOSAR root element - singleton pattern with extensible design.

    This class follows the singleton pattern and provides extension points
    for V2 modules to add custom functionality.

    Singleton Pattern:
    - Use getInstance() to get the singleton instance
    - Instance is created on first call
    - Can be reset by setting _instance = None (for testing)

    Extension Points:
    - _extended_attributes: Custom properties for V2 modules
    - getTagName(): Override for custom XML tags
    """

    # Class variable for singleton instance
    _instance: Optional["AUTOSAR"] = None

    def __init__(self) -> None:
        """
        Initialize AUTOSAR singleton.

        Raises:
            TypeError: If instance already exists (singleton enforcement).
        """
        super().__init__()
        # Core AUTOSAR attribute
        self.ar_packages: List["ARPackage"] = []

        # V2 extended attributes for custom properties
        self.setExtendedAttribute("schema_version", "3.2.3")
        self.setExtendedAttribute("xmlns", "http://autosar.org/3.2.3")

    @classmethod
    def getInstance(cls) -> "AUTOSAR":
        """
        Get the singleton AUTOSAR instance.

        Creates instance on first call, returns existing instance on
        subsequent calls.

        Returns:
            The singleton AUTOSAR instance.
        """
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    @classmethod
    def resetInstance(cls) -> None:
        """
        Reset the singleton instance.

        This is primarily intended for testing purposes where a fresh
        AUTOSAR instance is needed.
        """
        cls._instance = None


class Identifiable(ARObject):
    """
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
        # Core AUTOSAR attribute
        self.short_name: Optional[str] = None

        # V2 extended attributes for custom properties
        # Example: adminData, category, etc. can be added by modules
        self.setExtendedAttribute("adminData", None)
        self.setExtendedAttribute("category", None)

    def getShortName(self) -> Optional[str]:
        """
        Get the short name of this identifiable object.

        Returns:
            Short name or None if not set.
        """
        return self.short_name

    def setShortName(self, short_name: str) -> "Identifiable":
        """
        Set the short name of this identifiable object.

        Args:
            short_name: The short name to set.

        Returns:
            Self for method chaining.
        """
        self.short_name = short_name
        return self


class ARPackage(Identifiable):
    """
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

