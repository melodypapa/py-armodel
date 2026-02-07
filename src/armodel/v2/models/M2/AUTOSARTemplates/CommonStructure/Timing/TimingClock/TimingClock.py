from typing import Union

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class TimingClock(ARObject):
    """
    Represents a timing clock in AUTOSAR timing specifications.
    Defines a clock used for timing analysis and synchronization.
    """


    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass

    def __init__(self) -> None:
        """
        Initializes the TimingClock with default values.
        """
        super().__init__()
        self.clockName: Union[str, None] = None
        self.clockType: Union[str, None] = None

    def getClockName(self) -> str:
        """
        Gets the clock name.

        Returns:
            String representing the clock name
        """
        return self.clockName

    def setClockName(self, value: str):
        """
        Sets the clock name.

        Args:
            value: String value to set

        Returns:
            self for method chaining
        """
        self.clockName = value
        return self

    def getClockType(self) -> str:
        """
        Gets the clock type.

        Returns:
            String representing the clock type
        """
        return self.clockType

    def setClockType(self, value: str):
        """
        Sets the clock type.

        Args:
            value: String value to set

        Returns:
            self for method chaining
        """
        self.clockType = value
        return self
