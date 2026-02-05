from armodel.models_v2.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.models_v2.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class TimingModeInstance(ARObject):
    """
    Represents a timing mode instance in AUTOSAR.
    Defines a mode instance used in timing specifications.
    """

    def __init__(self):
        """
        Initializes the TimingModeInstance with default values.
        """
        super().__init__()
        self.modeRef: RefType = None
        self.modeValue: str = None

    def getModeRef(self) -> RefType:
        """
        Gets the mode reference.

        Returns:
            Reference to the mode
        """
        return self.modeRef

    def setModeRef(self, value: RefType):
        """
        Sets the mode reference.

        Args:
            value: The mode reference to set

        Returns:
            self for method chaining
        """
        self.modeRef = value
        return self

    def getModeValue(self) -> str:
        """
        Gets the mode value.

        Returns:
            String representing the mode value
        """
        return self.modeValue

    def setModeValue(self, value: str):
        """
        Sets the mode value.

        Args:
            value: String value to set

        Returns:
            self for method chaining
        """
        self.modeValue = value
        return self
