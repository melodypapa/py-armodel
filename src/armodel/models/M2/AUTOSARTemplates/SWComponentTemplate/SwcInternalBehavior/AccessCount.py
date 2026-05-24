"""
This module contains classes for representing AUTOSAR access count elements
in software component internal behavior templates.
"""

from abc import ABC

from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpStructureElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class AbstractAccessPoint(AtpStructureElement, ABC):
    """
    Abstract class indicating an access point from an ExecutableEntity.
    """

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) == AbstractAccessPoint:
            raise TypeError("ARObject is an abstract class.")

        super().__init__(parent, short_name)

        self.returnValueProvision = None

    def getReturnValueProvision(self):
        """
        Gets the return value provision.

        Returns:
            The return value provision
        """
        return self.returnValueProvision

    def setReturnValueProvision(self, value):
        """
        Sets the return value provision.
        Only sets the value if it is not None.

        Args:
            value: The return value provision to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.returnValueProvision = value
        return self
