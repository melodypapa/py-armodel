"""V2 base classes copied from ARPackage.py"""

from abc import ABC
from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class ReferenceBase(ARObject):
    """
    Represents a reference base in AUTOSAR models. Reference bases define
    how elements in one package can reference elements in other packages.
    They are used to establish relationships between different AUTOSAR packages.
    """

    def __init__(self):
        """
        Initializes a ReferenceBase instance with default values for
        package reference properties.
        """
        super().__init__()

        # List of global elements that can be referenced
        self.globalElements: List[str] = []
        # List of global references within the package
        self.globalInPackageRefs: List[RefType] = []
        # Flag indicating if this reference base is the default
        self.isDefault: Optional[bool] = None
        # Flag indicating if this reference base is global
        self.isGlobal: Optional[bool] = None
        # Flag indicating if this reference base belongs to the current package
        self.BaseIsThisPackage: Optional[bool] = None
        # List of package references
        self.packageRef: Optional[List[RefType]] = None
        # Short label for this reference base
        self.shortLabel: Optional[str] = None

    def getGlobalElements(self) -> List[str]:
        """
        Returns the list of global elements that can be referenced.

        Returns:
            List of global elements that can be referenced
        """
        return self.globalElements

    def addGlobalElement(self, value: str) -> 'ReferenceBase':
        """
        Adds a global element to the list of referenceable elements.

        Args:
            value: The element to add to the list of global elements

        Returns:
            Reference to this ReferenceBase instance (for method chaining)
        """
        self.globalElements.append(value)
        return self

    def getGlobalInPackageRefs(self) -> List[RefType]:
        """
        Returns the list of global references within the package.

        Returns:
            List of global references within the package
        """
        return self.globalInPackageRefs

    def addGlobalInPackageRef(self, value: RefType) -> 'ReferenceBase':
        """
        Adds a global reference to the package.

        Args:
            value: The reference to add to the list of global in-package references

        Returns:
            Reference to this ReferenceBase instance (for method chaining)
        """
        self.globalInPackageRefs.append(value)
        return self

    def getIsDefault(self) -> Optional[bool]:
        """
        Returns whether this reference base is the default.

        Returns:
            Boolean indicating if this is the default reference base (or None)
        """
        return self.isDefault

    def setIsDefault(self, value: bool) -> 'ReferenceBase':
        """
        Sets whether this reference base is the default.

        Args:
            value: Boolean indicating if this should be the default reference base

        Returns:
            Reference to this ReferenceBase instance (for method chaining)
        """
        self.isDefault = value
        return self

    def getIsGlobal(self) -> Optional[bool]:
        """
        Returns whether this reference base is global.

        Returns:
            Boolean indicating if this is a global reference base (or None)
        """
        return self.isGlobal

    def setIsGlobal(self, value: bool) -> 'ReferenceBase':
        """
        Sets whether this reference base is global.

        Args:
            value: Boolean indicating if this should be a global reference base

        Returns:
            Reference to this ReferenceBase instance (for method chaining)
        """
        self.isGlobal = value
        return self

    def getBaseIsThisPackage(self) -> Optional[bool]:
        """
        Returns whether this reference base belongs to the current package.

        Returns:
            Boolean indicating if this reference base belongs to the current package (or None)
        """
        return self.BaseIsThisPackage

    def setBaseIsThisPackage(self, value: bool) -> 'ReferenceBase':
        """
        Sets whether this reference base belongs to the current package.

        Args:
            value: Boolean indicating if this reference base belongs to the current package

        Returns:
            Reference to this ReferenceBase instance (for method chaining)
        """
        self.BaseIsThisPackage = value
        return self

    def getPackageRef(self) -> Optional[List[RefType]]:
        """
        Returns the list of package references.

        Returns:
            List of package references (or None)
        """
        return self.packageRef

    def setPackageRef(self, value: List[RefType]) -> 'ReferenceBase':
        """
        Sets the list of package references.

        Args:
            value: List of package references to set

        Returns:
            Reference to this ReferenceBase instance (for method chaining)
        """
        self.packageRef = value
        return self

    def getShortLabel(self) -> Optional[str]:
        """
        Returns the short label for this reference base.

        Returns:
            Short label identifier (or None)
        """
        return self.shortLabel

    def setShortLabel(self, value: str) -> 'ReferenceBase':
        """
        Sets the short label for this reference base.

        Args:
            value: The identifier to use as the short label

        Returns:
            Reference to this ReferenceBase instance (for method chaining)
        """
        self.shortLabel = value
        return self
