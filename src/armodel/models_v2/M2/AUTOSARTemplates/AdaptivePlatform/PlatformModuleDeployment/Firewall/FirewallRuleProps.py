from armodel.models_v2.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class FirewallRuleProps(ARObject):
    """
    Represents firewall rule properties in AUTOSAR Adaptive Platform PlatformModuleDeployment.
    Defines properties for firewall rule configuration.
    """

    def __init__(self):
        """
        Initializes the FirewallRuleProps with default values.
        """
        super().__init__()
        self.allowAny: bool = None
        self.direction: str = None
        self.protocol: str = None

    def getAllowAny(self) -> bool:
        """
        Gets the allowAny flag.

        Returns:
            Boolean value indicating if any traffic is allowed
        """
        return self.allowAny

    def setAllowAny(self, value: bool):
        """
        Sets the allowAny flag.

        Args:
            value: Boolean value to set

        Returns:
            self for method chaining
        """
        self.allowAny = value
        return self

    def getDirection(self) -> str:
        """
        Gets the direction of the firewall rule.

        Returns:
            String representing the direction
        """
        return self.direction

    def setDirection(self, value: str):
        """
        Sets the direction of the firewall rule.

        Args:
            value: String value to set

        Returns:
            self for method chaining
        """
        self.direction = value
        return self

    def getProtocol(self) -> str:
        """
        Gets the protocol of the firewall rule.

        Returns:
            String representing the protocol
        """
        return self.protocol

    def setProtocol(self, value: str):
        """
        Sets the protocol of the firewall rule.

        Args:
            value: String value to set

        Returns:
            self for method chaining
        """
        self.protocol = value
        return self
