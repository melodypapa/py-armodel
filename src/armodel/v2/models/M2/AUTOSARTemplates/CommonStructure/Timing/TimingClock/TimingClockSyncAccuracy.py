from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class TimingClockSyncAccuracy(ARObject):
    """
    Represents timing clock synchronization accuracy in AUTOSAR.
    Defines the accuracy of clock synchronization.
    """


    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass

    def __init__(self) -> None:
        """
        Initializes the TimingClockSyncAccuracy with default values.
        """
        super().__init__()
        self.accuracy: Union[str, None] = None
        self.unit: Union[str, None] = None

    def getAccuracy(self) -> str:
        """
        Gets the accuracy value.

        Returns:
            String representing the accuracy
        """
        return self.accuracy

    def setAccuracy(self, value: str):
        """
        Sets the accuracy value.

        Args:
            value: String value to set

        Returns:
            self for method chaining
        """
        self.accuracy = value
        return self

    def getUnit(self) -> str:
        """
        Gets the unit.

        Returns:
            String representing the unit
        """
        return self.unit

    def setUnit(self, value: str):
        """
        Sets the unit.

        Args:
            value: String value to set

        Returns:
            self for method chaining
        """
        self.unit = value
        return self
