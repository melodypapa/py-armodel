from typing import Union

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class TimingModeInstance(ARObject):
    """
    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingCondition
    Represents a timing mode instance in AUTOSAR.
    Defines a mode instance used in timing specifications.
    """


    def __init__(self) -> None:
        """
        Initializes the TimingModeInstance with default values.
        """
        super().__init__()
        self.modeRef: Union[Union[RefType, None] , None] = None
        self.modeValue: Union[str, None] = None

    def getModeRef(self) -> Union[RefType, None]:
        """
        Gets the mode reference.

        Returns:
            Reference to the mode
        """
        return self.modeRef

    def setModeRef(self, value: RefType) -> "TimingModeInstance":
        """
        Sets the mode reference.

        Args:
            value: The mode reference to set

        Returns:
            self for method chaining
        """
        self.modeRef = value
        return self

    def getModeValue(self) -> Union[str, None]:
        """
        Gets the mode value.

        Returns:
            String representing the mode value
        """
        return self.modeValue

    def setModeValue(self, value: str) -> "TimingModeInstance":
        """
        Sets the mode value.

        Args:
            value: String value to set

        Returns:
            self for method chaining
        """
        self.modeValue = value
        return self
