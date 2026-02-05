from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.SignalServiceTranslationControlEnum import SignalServiceTranslationControlEnum


class SignalServiceTranslationProps(ARObject):
    """
    Represents signal service translation properties in AUTOSAR.
    Defines properties for signal service translation.
    """

    def __init__(self):
        """
        Initializes the SignalServiceTranslationProps with default values.
        """
        super().__init__()
        self.translationControl: SignalServiceTranslationControlEnum = None

    def getTranslationControl(self) -> SignalServiceTranslationControlEnum:
        """
        Gets the translation control type.

        Returns:
            Signal service translation control enum value
        """
        return self.translationControl

    def setTranslationControl(self, value: SignalServiceTranslationControlEnum):
        """
        Sets the translation control type.

        Args:
            value: Signal service translation control enum value to set

        Returns:
            self for method chaining
        """
        self.translationControl = value
        return self