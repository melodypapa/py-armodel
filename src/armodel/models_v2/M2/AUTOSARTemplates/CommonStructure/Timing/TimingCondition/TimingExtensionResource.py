from armodel.models_v2.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class TimingExtensionResource(ARObject):
    """
    Represents a timing extension resource in AUTOSAR.
    Defines resources used for timing extensions.
    """

    def __init__(self):
        """
        Initializes the TimingExtensionResource with default values.
        """
        super().__init__()
        self.resourceName: str = None
        self.resourceType: str = None

    def getResourceName(self) -> str:
        """
        Gets the resource name.

        Returns:
            String representing the resource name
        """
        return self.resourceName

    def setResourceName(self, value: str):
        """
        Sets the resource name.

        Args:
            value: String value to set

        Returns:
            self for method chaining
        """
        self.resourceName = value
        return self

    def getResourceType(self) -> str:
        """
        Gets the resource type.

        Returns:
            String representing the resource type
        """
        return self.resourceType

    def setResourceType(self, value: str):
        """
        Sets the resource type.

        Args:
            value: String value to set

        Returns:
            self for method chaining
        """
        self.resourceType = value
        return self
