from abc import ABC
from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    PduActivationRouting,
    TagWithOptionalValue,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    RefType,
)


class AbstractServiceInstance(Identifiable, ABC):
    """
    Provided and Consumed Ethernet Service Instances that are available at the
    ApplicationEndpoint.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::ServiceInstances::AbstractServiceInstance

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 476, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is AbstractServiceInstance:
            raise TypeError("AbstractServiceInstance is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # A sequence of records to store arbitrary name/value pairs additional
        # information about the named atpVariation.
        self._capability: List["TagWithOptionalValue"] = []

    @property
    def capability(self) -> List["TagWithOptionalValue"]:
        """Get capability (Pythonic accessor)."""
        return self._capability
        # Major Version of the ServiceInterface.
        # Value can be set to that represents the Major Version of the service.
        self._majorVersion: Optional["PositiveInteger"] = None

    @property
    def major_version(self) -> Optional["PositiveInteger"]:
        """Get majorVersion (Pythonic accessor)."""
        return self._majorVersion

    @major_version.setter
    def major_version(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set majorVersion with validation.

        Args:
            value: The majorVersion to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._majorVersion = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"majorVersion must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._majorVersion = value
        # The ServiceDiscovery module is able to activate and deactivate the PDU
                # routing for ClientServerOperations methods).
        # atpVariation.
        self._method: Optional["PduActivationRouting"] = None

    @property
    def method(self) -> Optional["PduActivationRouting"]:
        """Get method (Pythonic accessor)."""
        return self._method

    @method.setter
    def method(self, value: Optional["PduActivationRouting"]) -> None:
        """
        Set method with validation.

        Args:
            value: The method to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._method = None
            return

        if not isinstance(value, PduActivationRouting):
            raise TypeError(
                f"method must be PduActivationRouting or None, got {type(value).__name__}"
            )
        self._method = value
        # The ServiceDiscovery module is able to activate and PDU routing from and to
        # TCP/IP-sockets.
        self._routingGroup: List[RefType] = []

    @property
    def routing_group(self) -> List[RefType]:
        """Get routingGroup (Pythonic accessor)."""
        return self._routingGroup

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCapability(self) -> List["TagWithOptionalValue"]:
        """
        AUTOSAR-compliant getter for capability.

        Returns:
            The capability value

        Note:
            Delegates to capability property (CODING_RULE_V2_00017)
        """
        return self.capability  # Delegates to property

    def getMajorVersion(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for majorVersion.

        Returns:
            The majorVersion value

        Note:
            Delegates to major_version property (CODING_RULE_V2_00017)
        """
        return self.major_version  # Delegates to property

    def setMajorVersion(self, value: "PositiveInteger") -> "AbstractServiceInstance":
        """
        AUTOSAR-compliant setter for majorVersion with method chaining.

        Args:
            value: The majorVersion to set

        Returns:
            self for method chaining

        Note:
            Delegates to major_version property setter (gets validation automatically)
        """
        self.major_version = value  # Delegates to property setter
        return self

    def getMethod(self) -> "PduActivationRouting":
        """
        AUTOSAR-compliant getter for method.

        Returns:
            The method value

        Note:
            Delegates to method property (CODING_RULE_V2_00017)
        """
        return self.method  # Delegates to property

    def setMethod(self, value: "PduActivationRouting") -> "AbstractServiceInstance":
        """
        AUTOSAR-compliant setter for method with method chaining.

        Args:
            value: The method to set

        Returns:
            self for method chaining

        Note:
            Delegates to method property setter (gets validation automatically)
        """
        self.method = value  # Delegates to property setter
        return self

    def getRoutingGroup(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for routingGroup.

        Returns:
            The routingGroup value

        Note:
            Delegates to routing_group property (CODING_RULE_V2_00017)
        """
        return self.routing_group  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_major_version(self, value: Optional["PositiveInteger"]) -> "AbstractServiceInstance":
        """
        Set majorVersion and return self for chaining.

        Args:
            value: The majorVersion to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_major_version("value")
        """
        self.major_version = value  # Use property setter (gets validation)
        return self

    def with_method(self, value: Optional["PduActivationRouting"]) -> "AbstractServiceInstance":
        """
        Set method and return self for chaining.

        Args:
            value: The method to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_method("value")
        """
        self.method = value  # Use property setter (gets validation)
        return self
