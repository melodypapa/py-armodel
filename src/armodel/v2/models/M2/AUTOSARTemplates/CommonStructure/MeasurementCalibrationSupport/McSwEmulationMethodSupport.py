from typing import Union

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class McSwEmulationMethodSupport(ARObject):
    """
    Represents MC (Measurement and Calibration) software emulation method support in AUTOSAR.
    Defines support for software emulation methods in measurement and calibration.
    """


    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass

    def __init__(self) -> None:
        """
        Initializes the McSwEmulationMethodSupport with default values.
        """
        super().__init__()
        self.emulationMethodName: Union[str, None] = None

    def getEmulationMethodName(self) -> str:
        """
        Gets the emulation method name.

        Returns:
            String representing the emulation method name
        """
        return self.emulationMethodName

    def setEmulationMethodName(self, value: str):
        """
        Sets the emulation method name.

        Args:
            value: String value to set

        Returns:
            self for method chaining
        """
        self.emulationMethodName = value
        return self
