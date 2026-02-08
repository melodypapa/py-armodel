from abc import ABC
from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class ServiceDependency(ARObject, ABC):
    """
    Collects all dependencies of a software module or component on an AUTOSAR
    Service related to a specific item (e.g. an NVRAM Block, a diagnostic event
    etc.). It defines the quality of service (Service Needs) of this item as
    well as (optionally) references to additional elements. This information is
    required for tools in order to generate the related basic software
    configuration and ServiceSwComponentTypes.

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 225, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 609, Classic Platform
      R23-11)
    """
    def __init__(self):
        if type(self) is ServiceDependency:
            raise TypeError("ServiceDependency is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This is the role of the assignment data type in the given context.
        # atpVariation.
        self._assignedData: Optional["RoleBasedDataType"] = None

    @property
    def assigned_data(self) -> Optional["RoleBasedDataType"]:
        """Get assignedData (Pythonic accessor)."""
        return self._assignedData

    @assigned_data.setter
    def assigned_data(self, value: Optional["RoleBasedDataType"]) -> None:
        """
        Set assignedData with validation.

        Args:
            value: The assignedData to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._assignedData = None
            return

        if not isinstance(value, RoleBasedDataType):
            raise TypeError(
                f"assignedData must be RoleBasedDataType or None, got {type(value).__name__}"
            )
        self._assignedData = value
        # If this attribute indicates a relevance for diagnostics then the integrator
                # has a much easier time identifying the the configuration of the diagnostic
                # stack.
        # of mode conditions (e.
        # g.
        # application and BswM) relevant Dcm.
        self._diagnostic: Optional["ServiceDiagnostic"] = None

    @property
    def diagnostic(self) -> Optional["ServiceDiagnostic"]:
        """Get diagnostic (Pythonic accessor)."""
        return self._diagnostic

    @diagnostic.setter
    def diagnostic(self, value: Optional["ServiceDiagnostic"]) -> None:
        """
        Set diagnostic with validation.

        Args:
            value: The diagnostic to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._diagnostic = None
            return

        if not isinstance(value, ServiceDiagnostic):
            raise TypeError(
                f"diagnostic must be ServiceDiagnostic or None, got {type(value).__name__}"
            )
        self._diagnostic = value
        # This attribute can be taken to contribute to the creation of name values.
        self._symbolicName: Optional["SymbolicNameProps"] = None

    @property
    def symbolic_name(self) -> Optional["SymbolicNameProps"]:
        """Get symbolicName (Pythonic accessor)."""
        return self._symbolicName

    @symbolic_name.setter
    def symbolic_name(self, value: Optional["SymbolicNameProps"]) -> None:
        """
        Set symbolicName with validation.

        Args:
            value: The symbolicName to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._symbolicName = None
            return

        if not isinstance(value, SymbolicNameProps):
            raise TypeError(
                f"symbolicName must be SymbolicNameProps or None, got {type(value).__name__}"
            )
        self._symbolicName = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAssignedData(self) -> "RoleBasedDataType":
        """
        AUTOSAR-compliant getter for assignedData.

        Returns:
            The assignedData value

        Note:
            Delegates to assigned_data property (CODING_RULE_V2_00017)
        """
        return self.assigned_data  # Delegates to property

    def setAssignedData(self, value: "RoleBasedDataType") -> "ServiceDependency":
        """
        AUTOSAR-compliant setter for assignedData with method chaining.

        Args:
            value: The assignedData to set

        Returns:
            self for method chaining

        Note:
            Delegates to assigned_data property setter (gets validation automatically)
        """
        self.assigned_data = value  # Delegates to property setter
        return self

    def getDiagnostic(self) -> "ServiceDiagnostic":
        """
        AUTOSAR-compliant getter for diagnostic.

        Returns:
            The diagnostic value

        Note:
            Delegates to diagnostic property (CODING_RULE_V2_00017)
        """
        return self.diagnostic  # Delegates to property

    def setDiagnostic(self, value: "ServiceDiagnostic") -> "ServiceDependency":
        """
        AUTOSAR-compliant setter for diagnostic with method chaining.

        Args:
            value: The diagnostic to set

        Returns:
            self for method chaining

        Note:
            Delegates to diagnostic property setter (gets validation automatically)
        """
        self.diagnostic = value  # Delegates to property setter
        return self

    def getSymbolicName(self) -> "SymbolicNameProps":
        """
        AUTOSAR-compliant getter for symbolicName.

        Returns:
            The symbolicName value

        Note:
            Delegates to symbolic_name property (CODING_RULE_V2_00017)
        """
        return self.symbolic_name  # Delegates to property

    def setSymbolicName(self, value: "SymbolicNameProps") -> "ServiceDependency":
        """
        AUTOSAR-compliant setter for symbolicName with method chaining.

        Args:
            value: The symbolicName to set

        Returns:
            self for method chaining

        Note:
            Delegates to symbolic_name property setter (gets validation automatically)
        """
        self.symbolic_name = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_assigned_data(self, value: Optional["RoleBasedDataType"]) -> "ServiceDependency":
        """
        Set assignedData and return self for chaining.

        Args:
            value: The assignedData to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_assigned_data("value")
        """
        self.assigned_data = value  # Use property setter (gets validation)
        return self

    def with_diagnostic(self, value: Optional["ServiceDiagnostic"]) -> "ServiceDependency":
        """
        Set diagnostic and return self for chaining.

        Args:
            value: The diagnostic to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_diagnostic("value")
        """
        self.diagnostic = value  # Use property setter (gets validation)
        return self

    def with_symbolic_name(self, value: Optional["SymbolicNameProps"]) -> "ServiceDependency":
        """
        Set symbolicName and return self for chaining.

        Args:
            value: The symbolicName to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_symbolic_name("value")
        """
        self.symbolic_name = value  # Use property setter (gets validation)
        return self
