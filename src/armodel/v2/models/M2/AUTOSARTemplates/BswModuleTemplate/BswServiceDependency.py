from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    BswService,
    RoleBasedBswModule,
    RoleBasedData,
    ServiceDependency,
    ServiceNeeds,
)


class BswServiceDependency(ServiceDependency):
    """
    Specialization of ServiceDependency in the context of an
    BswInternalBehavior. It allows to associate BswModuleEntries and data
    defined for a BSW module or cluster to a given ServiceNeeds element.

    Package: M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior::BswServiceDependency

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 225, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 225, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 978, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Defines the role of an associated data object (owned by module or cluster) in
        # the context of the ServiceNeeds atpVariation.
        self._assignedData: List["RoleBasedData"] = []

    @property
    def assigned_data(self) -> List["RoleBasedData"]:
        """Get assignedData (Pythonic accessor)."""
        return self._assignedData
        # Defines the role of an associated BswModuleEntry in the context of the
                # ServiceNeeds element.
        # atpVariation.
        self._assignedEntry: List["RoleBasedBswModule"] = []

    @property
    def assigned_entry(self) -> List["RoleBasedBswModule"]:
        """Get assignedEntry (Pythonic accessor)."""
        return self._assignedEntry
        # This adds the ability to become referrable to BswService.
        self._ident: Optional["BswService"] = None

    @property
    def ident(self) -> Optional["BswService"]:
        """Get ident (Pythonic accessor)."""
        return self._ident

    @ident.setter
    def ident(self, value: Optional["BswService"]) -> None:
        """
        Set ident with validation.

        Args:
            value: The ident to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ident = None
            return

        if not isinstance(value, BswService):
            raise TypeError(
                f"ident must be BswService or None, got {type(value).__name__}"
            )
        self._ident = value
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

    def getAssignedEntry(self) -> List["RoleBasedBswModule"]:
        """
        AUTOSAR-compliant getter for assignedEntry.

        Returns:
            The assignedEntry value

        Note:
            Delegates to assigned_entry property (CODING_RULE_V2_00017)
        """
        return self.assigned_entry  # Delegates to property

    def getIdent(self) -> "BswService":
        """
        AUTOSAR-compliant getter for ident.

        Returns:
            The ident value

        Note:
            Delegates to ident property (CODING_RULE_V2_00017)
        """
        return self.ident  # Delegates to property

    def setIdent(self, value: "BswService") -> "BswServiceDependency":
        """
        AUTOSAR-compliant setter for ident with method chaining.

        Args:
            value: The ident to set

        Returns:
            self for method chaining

        Note:
            Delegates to ident property setter (gets validation automatically)
        """
        self.ident = value  # Delegates to property setter
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

    def setServiceNeeds(self, value: "ServiceNeeds") -> "BswServiceDependency":
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

    def with_ident(self, value: Optional["BswService"]) -> "BswServiceDependency":
        """
        Set ident and return self for chaining.

        Args:
            value: The ident to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ident("value")
        """
        self.ident = value  # Use property setter (gets validation)
        return self

    def with_service_needs(self, value: Optional["ServiceNeeds"]) -> "BswServiceDependency":
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
