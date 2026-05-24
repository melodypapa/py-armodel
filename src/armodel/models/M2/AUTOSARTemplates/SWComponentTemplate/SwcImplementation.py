"""
This module contains classes for representing AUTOSAR software component implementation
elements in software component templates.
"""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType, String
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Implementation import Implementation

class SwcImplementation(Implementation):
    """
    Implementation of an atomic software component defining the behavior
    reference, per-instance memory sizes, and required RTE vendor.
    """

    def __init__(self, parent: ARObject, short_name: str) -> None:
        super().__init__(parent, short_name)

        self.behaviorRef: RefType = None
        self.perInstanceMemorySizes = []
        self.requiredRTEVendor: String = None

    def getBehaviorRef(self):
        """
        Gets the reference to the internal behavior.

        Returns:
            RefType: The behavior reference
        """
        return self.behaviorRef

    def setBehaviorRef(self, value):
        """
        Sets the reference to the internal behavior.

        Args:
            value: The behavior reference to set

        Returns:
            self for method chaining
        """
        self.behaviorRef = value
        return self

    def getPerInstanceMemorySizes(self):
        """
        Gets the list of per-instance memory sizes.

        Returns:
            The list of per-instance memory sizes
        """
        return self.perInstanceMemorySizes

    def addPerInstanceMemorySize(self, value):
        """
        Adds a per-instance memory size.

        Args:
            value: The per-instance memory size to add

        Returns:
            self for method chaining
        """
        self.perInstanceMemorySizes.append(value)
        return self

    def getRequiredRTEVendor(self):
        """
        Gets the required RTE vendor.

        Returns:
            String: The required RTE vendor
        """
        return self.requiredRTEVendor

    def setRequiredRTEVendor(self, value):
        """
        Sets the required RTE vendor.

        Args:
            value: The required RTE vendor to set

        Returns:
            self for method chaining
        """
        self.requiredRTEVendor = value
        return self
