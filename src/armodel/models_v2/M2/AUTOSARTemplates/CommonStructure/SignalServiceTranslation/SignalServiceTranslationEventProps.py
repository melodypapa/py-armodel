from armodel.models_v2.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class SignalServiceTranslationEventProps(ARObject):
    """
    Represents signal service translation event properties in AUTOSAR.
    Defines properties for signal service translation events.
    """

    def __init__(self):
        """
        Initializes the SignalServiceTranslationEventProps with default values.
        """
        super().__init__()
        self.eventRef: str = None

    def getEventRef(self) -> str:
        """
        Gets the event reference.

        Returns:
            String representing the event reference
        """
        return self.eventRef

    def setEventRef(self, value: str):
        """
        Sets the event reference.

        Args:
            value: String value to set

        Returns:
            self for method chaining
        """
        self.eventRef = value
        return self
