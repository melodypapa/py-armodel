from typing import List

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class SignalServiceTranslationPropsSet(ARObject):
    """
    Represents a set of signal service translation properties in AUTOSAR.
    Defines a collection of signal service translation property sets.
    """


    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass

    def __init__(self):
        """
        Initializes the SignalServiceTranslationPropsSet with default values.
        """
        super().__init__()
        self.translationProps: List[str] = []

    def addTranslationProp(self, prop: str):
        """
        Adds a translation property to this set.

        Args:
            prop: The translation property to add

        Returns:
            self for method chaining
        """
        self.translationProps.append(prop)
        return self

    def getTranslationProps(self) -> List[str]:
        """
        Gets the list of translation properties.

        Returns:
            List of translation properties
        """
        return self.translationProps
