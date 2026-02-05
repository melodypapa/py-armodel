from armodel.models_v2.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject


class RptComponent(ARObject):
    """
    Represents an RPT (Read-Protect-Transform) component in AUTOSAR.
    Defines a component that supports read-protect-transform functionality.
    """

    def __init__(self):
        """
        Initializes the RptComponent with default values.
        """
        super().__init__()
        self.componentRef: str = None
        self.portRef: str = None

    def getComponentRef(self) -> str:
        """
        Gets the component reference.

        Returns:
            String representing the component reference
        """
        return self.componentRef

    def setComponentRef(self, value: str):
        """
        Sets the component reference.

        Args:
            value: String value to set

        Returns:
            self for method chaining
        """
        self.componentRef = value
        return self

    def getPortRef(self) -> str:
        """
        Gets the port reference.

        Returns:
            String representing the port reference
        """
        return self.portRef

    def setPortRef(self, value: str):
        """
        Sets the port reference.

        Args:
            value: String value to set

        Returns:
            self for method chaining
        """
        self.portRef = value
        return self