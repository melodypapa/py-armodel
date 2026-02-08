from typing import Union

from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.SignalServiceTranslation.SignalServiceTranslationControlEnum import (
    SignalServiceTranslationControlEnum,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class SignalServiceTranslationProps(ARObject):
    """
    Package: M2::AUTOSARTemplates::CommonStructure::SignalServiceTranslation
    Represents signal service translation properties in AUTOSAR.
    Defines properties for signal service translation.
    """


    def __init__(self) -> None:
        """
        Initializes the SignalServiceTranslationProps with default values.
        """
        super().__init__()
        self.translationControl: Union[Union[SignalServiceTranslationControlEnum, None] , None] = None

    def getTranslationControl(self) -> Union[SignalServiceTranslationControlEnum, None]:
        """
        Gets the translation control type.

        Returns:
            Signal service translation control enum value
        """
        return self.translationControl

    def setTranslationControl(self, value: SignalServiceTranslationControlEnum) -> "SignalServiceTranslationProps":
        """
        Sets the translation control type.

        Args:
            value: Signal service translation control enum value to set

        Returns:
            self for method chaining
        """
        self.translationControl = value
        return self
