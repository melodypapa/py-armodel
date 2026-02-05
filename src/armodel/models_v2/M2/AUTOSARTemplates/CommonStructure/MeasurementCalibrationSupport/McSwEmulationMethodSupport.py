from armodel.models_v2.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject


class McSwEmulationMethodSupport(ARObject):
    """
    Represents MC (Measurement and Calibration) software emulation method support in AUTOSAR.
    Defines support for software emulation methods in measurement and calibration.
    """

    def __init__(self):
        """
        Initializes the McSwEmulationMethodSupport with default values.
        """
        super().__init__()
        self.emulationMethodName: str = None

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