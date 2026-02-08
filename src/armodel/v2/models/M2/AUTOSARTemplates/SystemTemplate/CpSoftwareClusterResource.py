from abc import ABC
from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates import RoleBasedResource
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)


class CpSoftwareClusterResource(Identifiable, ABC):
    """
    Represents a single resource required or provided by a CP Software Cluster.

    Package: M2::AUTOSARTemplates::SystemTemplate::SoftwareCluster::CpSoftwareClusterResource

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 271, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 901, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is CpSoftwareClusterResource:
            raise TypeError("CpSoftwareClusterResource is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Link to a resource which depends on this resource to implement them.
        self._dependent: List["RoleBasedResource"] = []

    @property
    def dependent(self) -> List["RoleBasedResource"]:
        """Get dependent (Pythonic accessor)."""
        return self._dependent
        # A unique identifiers per resource used for the connection The identifier is
                # required to be unique in the a single machine.
        # If software clusters are be reused on multiple machines the applies for all
                # the intended.
        self._globalResource: Optional["PositiveInteger"] = None

    @property
    def global_resource(self) -> Optional["PositiveInteger"]:
        """Get globalResource (Pythonic accessor)."""
        return self._globalResource

    @global_resource.setter
    def global_resource(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set globalResource with validation.

        Args:
            value: The globalResource to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._globalResource = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"globalResource must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._globalResource = value
        # This attribute indicates, that the resource is mandatory to Software Cluster.
        # If the resource is not the machine the connection process of any requiring
                # this resource gets aborted.
        self._isMandatory: Optional["Boolean"] = None

    @property
    def is_mandatory(self) -> Optional["Boolean"]:
        """Get isMandatory (Pythonic accessor)."""
        return self._isMandatory

    @is_mandatory.setter
    def is_mandatory(self, value: Optional["Boolean"]) -> None:
        """
        Set isMandatory with validation.

        Args:
            value: The isMandatory to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._isMandatory = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"isMandatory must be Boolean or None, got {type(value).__name__}"
            )
        self._isMandatory = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDependent(self) -> List["RoleBasedResource"]:
        """
        AUTOSAR-compliant getter for dependent.

        Returns:
            The dependent value

        Note:
            Delegates to dependent property (CODING_RULE_V2_00017)
        """
        return self.dependent  # Delegates to property

    def getGlobalResource(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for globalResource.

        Returns:
            The globalResource value

        Note:
            Delegates to global_resource property (CODING_RULE_V2_00017)
        """
        return self.global_resource  # Delegates to property

    def setGlobalResource(self, value: "PositiveInteger") -> "CpSoftwareClusterResource":
        """
        AUTOSAR-compliant setter for globalResource with method chaining.

        Args:
            value: The globalResource to set

        Returns:
            self for method chaining

        Note:
            Delegates to global_resource property setter (gets validation automatically)
        """
        self.global_resource = value  # Delegates to property setter
        return self

    def getIsMandatory(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for isMandatory.

        Returns:
            The isMandatory value

        Note:
            Delegates to is_mandatory property (CODING_RULE_V2_00017)
        """
        return self.is_mandatory  # Delegates to property

    def setIsMandatory(self, value: "Boolean") -> "CpSoftwareClusterResource":
        """
        AUTOSAR-compliant setter for isMandatory with method chaining.

        Args:
            value: The isMandatory to set

        Returns:
            self for method chaining

        Note:
            Delegates to is_mandatory property setter (gets validation automatically)
        """
        self.is_mandatory = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_global_resource(self, value: Optional["PositiveInteger"]) -> "CpSoftwareClusterResource":
        """
        Set globalResource and return self for chaining.

        Args:
            value: The globalResource to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_global_resource("value")
        """
        self.global_resource = value  # Use property setter (gets validation)
        return self

    def with_is_mandatory(self, value: Optional["Boolean"]) -> "CpSoftwareClusterResource":
        """
        Set isMandatory and return self for chaining.

        Args:
            value: The isMandatory to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_is_mandatory("value")
        """
        self.is_mandatory = value  # Use property setter (gets validation)
        return self
