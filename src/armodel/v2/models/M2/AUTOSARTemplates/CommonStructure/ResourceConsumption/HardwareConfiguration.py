"""
This module contains the HardwareConfiguration class for representing
hardware-specific configuration information in AUTOSAR resource consumption models.
"""

from typing import Union

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)


class HardwareConfiguration(ARObject):
    """
    Represents hardware configuration information in AUTOSAR models.
    This class defines specific hardware properties that may affect resource consumption.
    """


    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass

    def __init__(self) -> None:
        """
        Initializes the HardwareConfiguration with default values.
        """
        super().__init__()

        # Additional information about the hardware configuration
        self.additionalInformation: Union[Union[String, None] , None] = None
        # Processor mode setting for this hardware configuration
        self.processorMode: Union[Union[String, None] , None] = None
        # Processor speed for this hardware configuration
        self.processorSpeed: Union[Union[String, None] , None] = None

    def getAdditionalInformation(self):
        """
        Gets the additional information about the hardware configuration.

        Returns:
            String: Additional hardware configuration information
        """
        return self.additionalInformation

    def setAdditionalInformation(self, value):
        """
        Sets the additional information about the hardware configuration.

        Args:
            value: The additional information to set

        Returns:
            self for method chaining
        """
        self.additionalInformation = value
        return self

    def getProcessorMode(self):
        """
        Gets the processor mode setting for this hardware configuration.

        Returns:
            String: Processor mode setting
        """
        return self.processorMode

    def setProcessorMode(self, value):
        """
        Sets the processor mode setting for this hardware configuration.

        Args:
            value: The processor mode to set

        Returns:
            self for method chaining
        """
        self.processorMode = value
        return self

    def getProcessorSpeed(self):
        """
        Gets the processor speed for this hardware configuration.

        Returns:
            String: Processor speed setting
        """
        return self.processorSpeed

    def setProcessorSpeed(self, value):
        """
        Sets the processor speed for this hardware configuration.

        Args:
            value: The processor speed to set

        Returns:
            self for method chaining
        """
        self.processorSpeed = value
        return self

