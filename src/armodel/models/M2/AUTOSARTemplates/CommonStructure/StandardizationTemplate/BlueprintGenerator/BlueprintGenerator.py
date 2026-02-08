from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class BlueprintGenerator(ARObject):
    """
    Represents a blueprint generator in AUTOSAR.
    Defines a generator for creating blueprints from templates.
    """

    def __init__(self):
        """
        Initializes the BlueprintGenerator with default values.
        """
        super().__init__()
        self.generatorName: str = None

    def getGeneratorName(self) -> str:
        """
        Gets the generator name.

        Returns:
            String representing the generator name
        """
        return self.generatorName

    def setGeneratorName(self, value: str):
        """
        Sets the generator name.

        Args:
            value: String value to set

        Returns:
            self for method chaining
        """
        self.generatorName = value
        return self
