from typing import List


class CpSoftwareClusterMappingSet(ARElement):
    """
    This meta-class represents the ability to aggregate a collection of CP
    Software Cluster relevant mappings. This is applicable if a CP Software
    Cluster is described besides a concrete System, e.g. a reusable CP Software
    Cluster.

    Package: M2::AUTOSARTemplates::SystemTemplate::SoftwareCluster::CpSoftwareClusterMappingSet

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 285, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # maps a communication resource to CP Software Clusters Stereotypes:
        # atpSplitable; atpVariation Mapping ResourceMapping Tags:.
        self._portElementTo: List["PortElementTo"] = []

    @property
    def port_element_to(self) -> List["PortElementTo"]:
        """Get portElementTo (Pythonic accessor)."""
        return self._portElementTo
        # Maps a Software Cluster resource to an Application Partition to restrict the
                # usage.
        # Stereotypes: atpSplitable; atpVariation Mapping Tags:.
        self._resourceTo: List["CpSoftwareCluster"] = []

    @property
    def resource_to(self) -> List["CpSoftwareCluster"]:
        """Get resourceTo (Pythonic accessor)."""
        return self._resourceTo
        # maps a service resource to CP Software Clusters Stereotypes: atpSplitable;
        # atpVariation Mapping Tags:.
        self._softwareCluster: List["CpSoftwareClusterTo"] = []

    @property
    def software_cluster(self) -> List["CpSoftwareClusterTo"]:
        """Get softwareCluster (Pythonic accessor)."""
        return self._softwareCluster
        # maps SwComponentPrototypes in a CP Software Cluster to ApplicationPartitions
        # atpSplitable; atpVariation Mapping Tags:.
        self._swcTo: List["SwcToApplication"] = []

    @property
    def swc_to(self) -> List["SwcToApplication"]:
        """Get swcTo (Pythonic accessor)."""
        return self._swcTo

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getPortElementTo(self) -> List["PortElementTo"]:
        """
        AUTOSAR-compliant getter for portElementTo.

        Returns:
            The portElementTo value

        Note:
            Delegates to port_element_to property (CODING_RULE_V2_00017)
        """
        return self.port_element_to  # Delegates to property

    def getResourceTo(self) -> List["CpSoftwareCluster"]:
        """
        AUTOSAR-compliant getter for resourceTo.

        Returns:
            The resourceTo value

        Note:
            Delegates to resource_to property (CODING_RULE_V2_00017)
        """
        return self.resource_to  # Delegates to property

    def getSoftwareCluster(self) -> List["CpSoftwareClusterTo"]:
        """
        AUTOSAR-compliant getter for softwareCluster.

        Returns:
            The softwareCluster value

        Note:
            Delegates to software_cluster property (CODING_RULE_V2_00017)
        """
        return self.software_cluster  # Delegates to property

    def getSwcTo(self) -> List["SwcToApplication"]:
        """
        AUTOSAR-compliant getter for swcTo.

        Returns:
            The swcTo value

        Note:
            Delegates to swc_to property (CODING_RULE_V2_00017)
        """
        return self.swc_to  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
