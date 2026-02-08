from typing import Union

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class McSwEmulationMethodSupport(ARObject):
    """
    Package: M2::AUTOSARTemplates::CommonStructure::MeasurementCalibrationSupport
    Represents MC (Measurement and Calibration) software emulation method support in AUTOSAR.
    Defines support for software emulation methods in measurement and calibration.
    """


    def __init__(self) -> None:
        """
        Initializes the McSwEmulationMethodSupport with default values.
        """
        super().__init__()
        self.emulationMethodName: Union[str, None] = None

    def getEmulationMethodName(self) -> Union[str, None]:
        """
        Gets the emulation method name.

        Returns:
            String representing the emulation method name
        """
        return self.emulationMethodName

    def setEmulationMethodName(self, value: str) -> "McSwEmulationMethodSupport":
        """
        Sets the emulation method name.

        Args:
            value: String value to set

        Returns:
            self for method chaining
        """
        self.emulationMethodName = value
        return self
