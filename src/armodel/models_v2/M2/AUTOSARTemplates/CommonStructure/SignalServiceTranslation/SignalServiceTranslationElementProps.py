from armodel.models_v2.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class SignalServiceTranslationElementProps(ARObject):
    """
    Represents signal service translation element properties in AUTOSAR.
    Defines properties for signal service translation elements.
    """

    def __init__(self):
        """
        Initializes the SignalServiceTranslationElementProps with default values.
        """
        super().__init__()
        self.elementRef: str = None

    def getElementRef(self) -> str:
        """
        Gets the element reference.

        Returns:
            String representing the element reference
        """
        return self.elementRef

    def setElementRef(self, value: str):
        """
        Sets the element reference.

        Args:
            value: String value to set

        Returns:
            self for method chaining
        """
        self.elementRef = value
        return self
