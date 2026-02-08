from typing import List

from armodel.v2.models.M2.AUTOSARTemplates import (
    CpSoftwareCluster,
    EcuInstance,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    ARElement,
)


class CpSoftwareClusterResourcePool(ARElement):
    """
    Represents the pool of resources which can be provided or required by CP
    Software Clusters.

    Package: M2::AUTOSARTemplates::SystemTemplate::SoftwareCluster::CpSoftwareClusterResourcePool

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 901, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This reference identifies the EcuInstance in which the is defined.
        self._ecuScope: List["EcuInstance"] = []

    @property
    def ecu_scope(self) -> List["EcuInstance"]:
        """Get ecuScope (Pythonic accessor)."""
        return self._ecuScope
        # This aggregation represents the collection of resources in enclosing resource
        # pool.
        self._resource: List["CpSoftwareCluster"] = []

    @property
    def resource(self) -> List["CpSoftwareCluster"]:
        """Get resource (Pythonic accessor)."""
        return self._resource

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getEcuScope(self) -> List["EcuInstance"]:
        """
        AUTOSAR-compliant getter for ecuScope.

        Returns:
            The ecuScope value

        Note:
            Delegates to ecu_scope property (CODING_RULE_V2_00017)
        """
        return self.ecu_scope  # Delegates to property

    def getResource(self) -> List["CpSoftwareCluster"]:
        """
        AUTOSAR-compliant getter for resource.

        Returns:
            The resource value

        Note:
            Delegates to resource property (CODING_RULE_V2_00017)
        """
        return self.resource  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
