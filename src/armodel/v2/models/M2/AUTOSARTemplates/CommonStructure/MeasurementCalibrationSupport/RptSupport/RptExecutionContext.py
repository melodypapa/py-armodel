from typing import Union

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class RptExecutionContext(ARObject):
    """
    Represents an RPT execution context in AUTOSAR.
    Defines the execution context for RPT functionality.
    """


    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass

    def __init__(self) -> None:
        """
        Initializes the RptExecutionContext with default values.
        """
        super().__init__()
        self.contextRef: Union[Union[RefType, None] , None] = None

    def getContextRef(self) -> RefType:
        """
        Gets the context reference.

        Returns:
            Reference to the context
        """
        return self.contextRef

    def setContextRef(self, value: RefType):
        """
        Sets the context reference.

        Args:
            value: The context reference to set

        Returns:
            self for method chaining
        """
        self.contextRef = value
        return self
