from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class McDataAccessDetails(ARObject):
    """
    Represents MC (Measurement and Calibration) data access details in AUTOSAR.
    Defines details about how MC data can be accessed.
    """


    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass

    def __init__(self) -> None:
        """
        Initializes the McDataAccessDetails with default values.
        """
        super().__init__()
        self.accessType: str = None
        self.address: str = None

    def getAccessType(self) -> str:
        """
        Gets the access type.

        Returns:
            String representing the access type
        """
        return self.accessType

    def setAccessType(self, value: str):
        """
        Sets the access type.

        Args:
            value: String value to set

        Returns:
            self for method chaining
        """
        self.accessType = value
        return self

    def getAddress(self) -> str:
        """
        Gets the address.

        Returns:
            String representing the address
        """
        return self.address

    def setAddress(self, value: str):
        """
        Sets the address.

        Args:
            value: String value to set

        Returns:
            self for method chaining
        """
        self.address = value
        return self
