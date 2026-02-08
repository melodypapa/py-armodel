from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.SWmapping import MappingConstraint

    RefType,
)


class ComponentClustering(MappingConstraint):
    """
    Constraint that forces the mapping of all referenced SW component instances
    to the same ECU, Core, Partition depending on the defined mappingScope
    attribute. If mappingScope is not specified then mappingScopeEcu shall be
    assumed.

    Package: M2::AUTOSARTemplates::SystemTemplate::SWmapping::ComponentClustering

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 203, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # together.
        # by: ComponentInSystem.
        self._clusteredInstanceRef: List["SwComponent"] = []

    @property
    def clustered_instance_ref(self) -> List["SwComponent"]:
        """Get clusteredInstanceRef (Pythonic accessor)."""
        return self._clusteredInstanceRef
        # This attribute indicates whether the ComponentClustering applies to different
        # ECUs, partitions or this attribute is not specified then mappingScope be
        # assumed.
        self._mappingScope: RefType = None

    @property
    def mapping_scope(self) -> RefType:
        """Get mappingScope (Pythonic accessor)."""
        return self._mappingScope

    @mapping_scope.setter
    def mapping_scope(self, value: RefType) -> None:
        """
        Set mappingScope with validation.

        Args:
            value: The mappingScope to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._mappingScope = None
            return

        self._mappingScope = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getClusteredInstanceRef(self) -> List["SwComponent"]:
        """
        AUTOSAR-compliant getter for clusteredInstanceRef.

        Returns:
            The clusteredInstanceRef value

        Note:
            Delegates to clustered_instance_ref property (CODING_RULE_V2_00017)
        """
        return self.clustered_instance_ref  # Delegates to property

    def getMappingScope(self) -> RefType:
        """
        AUTOSAR-compliant getter for mappingScope.

        Returns:
            The mappingScope value

        Note:
            Delegates to mapping_scope property (CODING_RULE_V2_00017)
        """
        return self.mapping_scope  # Delegates to property

    def setMappingScope(self, value: RefType) -> "ComponentClustering":
        """
        AUTOSAR-compliant setter for mappingScope with method chaining.

        Args:
            value: The mappingScope to set

        Returns:
            self for method chaining

        Note:
            Delegates to mapping_scope property setter (gets validation automatically)
        """
        self.mapping_scope = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_mapping_scope(self, value: Optional[RefType]) -> "ComponentClustering":
        """
        Set mappingScope and return self for chaining.

        Args:
            value: The mappingScope to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_mapping_scope("value")
        """
        self.mapping_scope = value  # Use property setter (gets validation)
        return self
