"""
This module contains the SoftwareContext class for representing
software execution context information in AUTOSAR resource consumption models.
"""

from typing import Union

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)


class SoftwareContext(ARObject):
    """
    Represents software execution context information in AUTOSAR models.
    This class defines the input conditions and execution state for resource consumption analysis.
    """


    def __init__(self) -> None:
        """
        Initializes the SoftwareContext with default values.
        """
        super().__init__()

        # Input information for this software context
        self.input: Union[Union[String, None] , None] = None
        # Execution state for this software context
        self.state: Union[Union[String, None] , None] = None

    def getInput(self):
        """
        Gets the input information for this software context.

        Returns:
            String: Input information
        """
        return self.input

    def setInput(self, value):
        """
        Sets the input information for this software context.

        Args:
            value: The input information to set

        Returns:
            self for method chaining
        """
        self.input = value
        return self

    def getState(self):
        """
        Gets the execution state for this software context.

        Returns:
            String: Execution state
        """
        return self.state

    def setState(self, value):
        """
        Sets the execution state for this software context.

        Args:
            value: The execution state to set

        Returns:
            self for method chaining
        """
        self.state = value
        return self
