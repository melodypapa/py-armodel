"""
This module contains classes for representing AUTOSAR hardware element connectors
in the EcuResourceTemplate module.
"""

from typing import Optional, Union

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Describable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class HwElementConnector(Describable):
    """
    Represents a connection between hardware elements in AUTOSAR hardware descriptions.
    This class defines the connections that can exist between different hardware elements in the model.
    """

    def __init__(self) -> None:
        """
        Initializes the HwElementConnector.
        """
        super().__init__()

        self.hwElementRef: Optional[RefType] = None
        self.hwPinRef: Optional[RefType] = None

    def getHwElementRef(self) -> Optional[RefType]:
        """
        Gets the reference to the connected hardware element.

        Returns:
            RefType representing the hardware element reference, or None if not set
        """
        return self.hwElementRef

    def setHwElementRef(self, value: RefType):
        """
        Sets the reference to the connected hardware element.
        Only sets the value if it is not None.

        Args:
            value: The hardware element reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.hwElementRef = value
        return self

    def getHwPinRef(self) -> Optional[RefType]:
        """
        Gets the reference to the connected hardware pin.

        Returns:
            RefType representing the hardware pin reference, or None if not set
        """
        return self.hwPinRef

    def setHwPinRef(self, value: RefType):
        """
        Sets the reference to the connected hardware pin.
        Only sets the value if it is not None.

        Args:
            value: The hardware pin reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.hwPinRef = value
        return self
