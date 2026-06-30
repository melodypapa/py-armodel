"""
This module contains classes for representing AUTOSAR per-instance memory elements
in software component internal behavior templates.
"""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpStructureElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import SwDataDefProps

class PerInstanceMemory(AtpStructureElement):
    """
    A per-instance memory is a memory block that is allocated separately
    for each instance of an atomic software component.
    """

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.initValue: ARLiteral = None
        self.swDataDefProps: 'SwDataDefProps' = None
        self.type: ARLiteral = None
        self.typeDefinition: ARLiteral = None

    def getInitValue(self):
        """
        Gets the initial value of the per-instance memory.

        Returns:
            ARLiteral: The initial value
        """
        return self.initValue

    def setInitValue(self, value):
        """
        Sets the initial value of the per-instance memory.

        Args:
            value: The initial value to set

        Returns:
            self for method chaining
        """
        self.initValue = value
        return self

    def getSwDataDefProps(self):
        """
        Gets the software data definition properties.

        Returns:
            SwDataDefProps: The software data definition properties
        """
        return self.swDataDefProps

    def setSwDataDefProps(self, value):
        """
        Sets the software data definition properties.

        Args:
            value: The software data definition properties to set

        Returns:
            self for method chaining
        """
        self.swDataDefProps = value
        return self

    def getType(self):
        """
        Gets the type of the per-instance memory.

        Returns:
            ARLiteral: The type
        """
        return self.type

    def setType(self, value):
        """
        Sets the type of the per-instance memory.

        Args:
            value: The type to set

        Returns:
            self for method chaining
        """
        self.type = value
        return self

    def getTypeDefinition(self):
        """
        Gets the type definition of the per-instance memory.

        Returns:
            ARLiteral: The type definition
        """
        return self.typeDefinition

    def setTypeDefinition(self, value):
        """
        Sets the type definition of the per-instance memory.

        Args:
            value: The type definition to set

        Returns:
            self for method chaining
        """
        self.typeDefinition = value
        return self