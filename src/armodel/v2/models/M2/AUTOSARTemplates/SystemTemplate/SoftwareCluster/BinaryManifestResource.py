from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class BinaryManifestResource(Identifiable, ABC):
    """
    This meta-class acts as an abstract base class for specializations.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::SoftwareCluster::BinaryManifest::BinaryManifestResource
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 915, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is BinaryManifestResource:
            raise TypeError("BinaryManifestResource is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # A unique identifiers per resource used for the connection The identifier is
                # required to be unique in the a single machine.
        # If software clusters are be reused on multiple machines the applies for all
                # the intended BinaryManifestItem * aggr This aggregation represents the
                # collection of binary owned by the enclosing binary manifest.
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
        # this reference identifies the definition of the Binary ManifestResource.
        # The definition provides configuration is shared among all BinaryManifest
                # refer to the BinaryManifestResource.
        self._resource: Optional["BinaryManifest"] = None

    @property
    def resource(self) -> Optional["BinaryManifest"]:
        """Get resource (Pythonic accessor)."""
        return self._resource

    @resource.setter
    def resource(self, value: Optional["BinaryManifest"]) -> None:
        """
        Set resource with validation.
        
        Args:
            value: The resource to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._resource = None
            return

        if not isinstance(value, BinaryManifest):
            raise TypeError(
                f"resource must be BinaryManifest or None, got {type(value).__name__}"
            )
        self._resource = value
        # This attribute specifies the guard value of the enclosing manifest resource.
        self._resourceGuard: Optional["String"] = None

    @property
    def resource_guard(self) -> Optional["String"]:
        """Get resourceGuard (Pythonic accessor)."""
        return self._resourceGuard

    @resource_guard.setter
    def resource_guard(self, value: Optional["String"]) -> None:
        """
        Set resourceGuard with validation.
        
        Args:
            value: The resourceGuard to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._resourceGuard = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"resourceGuard must be String or None, got {type(value).__name__}"
            )
        self._resourceGuard = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getGlobalResource(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for globalResource.
        
        Returns:
            The globalResource value
        
        Note:
            Delegates to global_resource property (CODING_RULE_V2_00017)
        """
        return self.global_resource  # Delegates to property

    def setGlobalResource(self, value: "PositiveInteger") -> "BinaryManifestResource":
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

    def getResource(self) -> "BinaryManifest":
        """
        AUTOSAR-compliant getter for resource.
        
        Returns:
            The resource value
        
        Note:
            Delegates to resource property (CODING_RULE_V2_00017)
        """
        return self.resource  # Delegates to property

    def setResource(self, value: "BinaryManifest") -> "BinaryManifestResource":
        """
        AUTOSAR-compliant setter for resource with method chaining.
        
        Args:
            value: The resource to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to resource property setter (gets validation automatically)
        """
        self.resource = value  # Delegates to property setter
        return self

    def getResourceGuard(self) -> "String":
        """
        AUTOSAR-compliant getter for resourceGuard.
        
        Returns:
            The resourceGuard value
        
        Note:
            Delegates to resource_guard property (CODING_RULE_V2_00017)
        """
        return self.resource_guard  # Delegates to property

    def setResourceGuard(self, value: "String") -> "BinaryManifestResource":
        """
        AUTOSAR-compliant setter for resourceGuard with method chaining.
        
        Args:
            value: The resourceGuard to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to resource_guard property setter (gets validation automatically)
        """
        self.resource_guard = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_global_resource(self, value: Optional["PositiveInteger"]) -> "BinaryManifestResource":
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

    def with_resource(self, value: Optional["BinaryManifest"]) -> "BinaryManifestResource":
        """
        Set resource and return self for chaining.
        
        Args:
            value: The resource to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_resource("value")
        """
        self.resource = value  # Use property setter (gets validation)
        return self

    def with_resource_guard(self, value: Optional["String"]) -> "BinaryManifestResource":
        """
        Set resourceGuard and return self for chaining.
        
        Args:
            value: The resourceGuard to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_resource_guard("value")
        """
        self.resource_guard = value  # Use property setter (gets validation)
        return self