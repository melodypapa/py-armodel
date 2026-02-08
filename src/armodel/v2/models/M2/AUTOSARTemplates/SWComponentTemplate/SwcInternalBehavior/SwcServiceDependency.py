from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import ServiceDependency

    RefType,
)


class SwcServiceDependency(ServiceDependency):
    """
    Specialization of ServiceDependency in the context of an
    SwcInternalBehavior. It allows to associate ports, port groups and (in
    special cases) data defined for an atomic software component to a given
    ServiceNeeds element. (cid:53) 224 of 719 Document ID 673:
    AUTOSAR_CP_TPS_DiagnosticExtractTemplate Diagnostic Extract Template AUTOSAR
    CP R23-11 (cid:52)

    Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::ServiceMapping::SwcServiceDependency

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 224, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 608, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Defines the role of an associated data object of the same atpVariation.
        self._assignedData: List["RoleBasedData"] = []

    @property
    def assigned_data(self) -> List["RoleBasedData"]:
        """Get assignedData (Pythonic accessor)."""
        return self._assignedData
        # Defines the role of an associated port of the same atpVariation.
        self._assignedPort: List["RoleBasedPort"] = []

    @property
    def assigned_port(self) -> List["RoleBasedPort"]:
        """Get assignedPort (Pythonic accessor)."""
        return self._assignedPort
        # This reference specifies an association between the and a PortGroup, for
                # example to request mode which applies for communication ports.
        # The referred PortGroup shall be local to SWC, but via the links between the
                # Port tool can evaluate this information such that all linked via this port
                # group on the same ECU can.
        self._representedPort: RefType = None

    @property
    def represented_port(self) -> RefType:
        """Get representedPort (Pythonic accessor)."""
        return self._representedPort

    @represented_port.setter
    def represented_port(self, value: RefType) -> None:
        """
        Set representedPort with validation.

        Args:
            value: The representedPort to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._representedPort = None
            return

        self._representedPort = value
        # The associated ServiceNeeds.
        self._serviceNeeds: Optional["ServiceNeeds"] = None

    @property
    def service_needs(self) -> Optional["ServiceNeeds"]:
        """Get serviceNeeds (Pythonic accessor)."""
        return self._serviceNeeds

    @service_needs.setter
    def service_needs(self, value: Optional["ServiceNeeds"]) -> None:
        """
        Set serviceNeeds with validation.

        Args:
            value: The serviceNeeds to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._serviceNeeds = None
            return

        if not isinstance(value, ServiceNeeds):
            raise TypeError(
                f"serviceNeeds must be ServiceNeeds or None, got {type(value).__name__}"
            )
        self._serviceNeeds = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAssignedData(self) -> List["RoleBasedData"]:
        """
        AUTOSAR-compliant getter for assignedData.

        Returns:
            The assignedData value

        Note:
            Delegates to assigned_data property (CODING_RULE_V2_00017)
        """
        return self.assigned_data  # Delegates to property

    def getAssignedPort(self) -> List["RoleBasedPort"]:
        """
        AUTOSAR-compliant getter for assignedPort.

        Returns:
            The assignedPort value

        Note:
            Delegates to assigned_port property (CODING_RULE_V2_00017)
        """
        return self.assigned_port  # Delegates to property

    def getRepresentedPort(self) -> RefType:
        """
        AUTOSAR-compliant getter for representedPort.

        Returns:
            The representedPort value

        Note:
            Delegates to represented_port property (CODING_RULE_V2_00017)
        """
        return self.represented_port  # Delegates to property

    def setRepresentedPort(self, value: RefType) -> "SwcServiceDependency":
        """
        AUTOSAR-compliant setter for representedPort with method chaining.

        Args:
            value: The representedPort to set

        Returns:
            self for method chaining

        Note:
            Delegates to represented_port property setter (gets validation automatically)
        """
        self.represented_port = value  # Delegates to property setter
        return self

    def getServiceNeeds(self) -> "ServiceNeeds":
        """
        AUTOSAR-compliant getter for serviceNeeds.

        Returns:
            The serviceNeeds value

        Note:
            Delegates to service_needs property (CODING_RULE_V2_00017)
        """
        return self.service_needs  # Delegates to property

    def setServiceNeeds(self, value: "ServiceNeeds") -> "SwcServiceDependency":
        """
        AUTOSAR-compliant setter for serviceNeeds with method chaining.

        Args:
            value: The serviceNeeds to set

        Returns:
            self for method chaining

        Note:
            Delegates to service_needs property setter (gets validation automatically)
        """
        self.service_needs = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_represented_port(self, value: Optional[RefType]) -> "SwcServiceDependency":
        """
        Set representedPort and return self for chaining.

        Args:
            value: The representedPort to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_represented_port("value")
        """
        self.represented_port = value  # Use property setter (gets validation)
        return self

    def with_service_needs(self, value: Optional["ServiceNeeds"]) -> "SwcServiceDependency":
        """
        Set serviceNeeds and return self for chaining.

        Args:
            value: The serviceNeeds to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_service_needs("value")
        """
        self.service_needs = value  # Use property setter (gets validation)
        return self
