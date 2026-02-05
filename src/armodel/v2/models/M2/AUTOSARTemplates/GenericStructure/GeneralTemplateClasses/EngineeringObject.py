"""
This module contains classes for representing AUTOSAR engineering objects
in the GenericStructure module.
"""

from abc import ABC
from typing import Any, Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ARLiteral,
)


class EngineeringObject(ARObject, ABC):
    """
    Abstract class for AUTOSAR engineering objects.
    This class defines the basic structure for engineering objects in AUTOSAR models.
    """

    def __init__(self):
        if type(self) == EngineeringObject:
            raise TypeError("EngineeringObject is an abstract class.")

        super().__init__()

        self.category: Optional[ARLiteral] = None
        self.domain: Optional[ARLiteral] = None
        self.revision_label: Optional[ARLiteral] = None
        self.short_label: Optional[ARLiteral] = None

    def setCategory(self, category: Any):
        """
        Sets the category for this engineering object.
        If the category is not an ARLiteral, it will be converted to one.
        
        Args:
            category: The category to set
            
        Returns:
            self for method chaining
        """
        if isinstance(category, ARLiteral):
            self.category = category
        else:
            self.category = ARLiteral()
            self.category.setValue(str(category))
        return self

    def getCategory(self) -> Optional[ARLiteral]:
        """
        Gets the category for this engineering object.
        
        Returns:
            ARLiteral representing the category, or None if not set
        """
        return self.category

    def setDomain(self, domain: ARLiteral):
        """
        Sets the domain for this engineering object.
        
        Args:
            domain: The domain to set
            
        Returns:
            self for method chaining
        """
        self.domain = domain
        return self

    def getDomain(self) -> Optional[ARLiteral]:
        """
        Gets the domain for this engineering object.
        
        Returns:
            ARLiteral representing the domain, or None if not set
        """
        return self.domain

    def setRevisionLabel(self, revision_label: ARLiteral):
        """
        Sets the revision label for this engineering object.
        
        Args:
            revision_label: The revision label to set
            
        Returns:
            self for method chaining
        """
        self.revision_label = revision_label
        return self

    def getRevisionLabel(self) -> Optional[ARLiteral]:
        """
        Gets the revision label for this engineering object.
        
        Returns:
            ARLiteral representing the revision label, or None if not set
        """
        return self.revision_label

    def setShortLabel(self, label: ARLiteral):
        """
        Sets the short label for this engineering object.
        
        Args:
            label: The short label to set
            
        Returns:
            self for method chaining
        """
        self.short_label = label
        return self

    def getShortLabel(self) -> Optional[ARLiteral]:
        """
        Gets the short label for this engineering object.
        
        Returns:
            ARLiteral representing the short label, or None if not set
        """
        return self.short_label


class AutosarEngineeringObject(EngineeringObject):
    """
    Represents an AUTOSAR engineering object.
    This class extends EngineeringObject with AUTOSAR-specific functionality.
    """

    def __init__(self):
        super().__init__()
