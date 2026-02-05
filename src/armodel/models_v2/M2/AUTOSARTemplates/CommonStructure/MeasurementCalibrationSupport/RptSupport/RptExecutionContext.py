from armodel.models_v2.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.models_v2.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class RptExecutionContext(ARObject):
    """
    Represents an RPT execution context in AUTOSAR.
    Defines the execution context for RPT functionality.
    """

    def __init__(self):
        """
        Initializes the RptExecutionContext with default values.
        """
        super().__init__()
        self.contextRef: RefType = None

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
