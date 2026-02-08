from typing import Union

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class FirewallRuleProps(ARObject):
    """
    Package: M2::AUTOSARTemplates::AdaptivePlatform::PlatformModuleDeployment::Firewall
    Represents firewall rule properties in AUTOSAR Adaptive Platform PlatformModuleDeployment.
    Defines properties for firewall rule configuration.
    """


    def __init__(self) -> None:
        """
        Initializes the FirewallRuleProps with default values.
        """
        super().__init__()
        self.allowAny: Union[bool, None] = None
        self.direction: Union[str, None] = None
        self.protocol: Union[str, None] = None

    def getAllowAny(self) -> Union[bool, None]:
        """
        Gets the allowAny flag.

        Returns:
            Boolean value indicating if any traffic is allowed
        """
        return self.allowAny

    def setAllowAny(self, value: bool) -> "FirewallRuleProps":
        """
        Sets the allowAny flag.

        Args:
            value: Boolean value to set

        Returns:
            self for method chaining
        """
        self.allowAny = value
        return self

    def getDirection(self) -> Union[str, None]:
        """
        Gets the direction of the firewall rule.

        Returns:
            String representing the direction
        """
        return self.direction

    def setDirection(self, value: str) -> "FirewallRuleProps":
        """
        Sets the direction of the firewall rule.

        Args:
            value: String value to set

        Returns:
            self for method chaining
        """
        self.direction = value
        return self

    def getProtocol(self) -> Union[str, None]:
        """
        Gets the protocol of the firewall rule.

        Returns:
            String representing the protocol
        """
        return self.protocol

    def setProtocol(self, value: str) -> "FirewallRuleProps":
        """
        Sets the protocol of the firewall rule.

        Args:
            value: String value to set

        Returns:
            self for method chaining
        """
        self.protocol = value
        return self
