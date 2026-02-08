from typing import List

from armodel.v2.models.M2.AUTOSARTemplates import (
    CpSoftwareClusterResource,
    EcucContainerValue,
)


class CpSoftwareClusterServiceResource(CpSoftwareClusterResource):
    """
    Represents a single resource required or provided by a CP Software Cluster
    which relates to the BSW.

    Package: M2::AUTOSARTemplates::SystemTemplate::SoftwareCluster::CpSoftwareClusterServiceResource

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 904, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Refernce(s) to one or multiple EcucContainerValue(s) characteristics of the
        # resource.
        self._resourceNeeds: List["EcucContainerValue"] = []

    @property
    def resource_needs(self) -> List["EcucContainerValue"]:
        """Get resourceNeeds (Pythonic accessor)."""
        return self._resourceNeeds

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getResourceNeeds(self) -> List["EcucContainerValue"]:
        """
        AUTOSAR-compliant getter for resourceNeeds.

        Returns:
            The resourceNeeds value

        Note:
            Delegates to resource_needs property (CODING_RULE_V2_00017)
        """
        return self.resource_needs  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
