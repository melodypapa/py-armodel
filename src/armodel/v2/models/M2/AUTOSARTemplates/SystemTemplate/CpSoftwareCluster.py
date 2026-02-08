from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    CompositionSw,
    SwComponent,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    ARElement,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class CpSoftwareCluster(ARElement):
    """
    This meta class provides the ability to define a CP Software Cluster. Each
    CP Software Cluster can be integrated and build individually. It defines the
    sub-set of hierarchical tree(s) of Software Components belonging to this CP
    Software Cluster. Resources required or provided by this CP Software Cluster
    are given in the according mappings.

    Package: M2::AUTOSARTemplates::SystemTemplate::SoftwareCluster::CpSoftwareCluster

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 309, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 893, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 221, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute represents the value of the id of the CP software cluster.
        self._softwareCluster: Optional["PositiveInteger"] = None

    @property
    def software_cluster(self) -> Optional["PositiveInteger"]:
        """Get softwareCluster (Pythonic accessor)."""
        return self._softwareCluster

    @software_cluster.setter
    def software_cluster(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set softwareCluster with validation.

        Args:
            value: The softwareCluster to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._softwareCluster = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"softwareCluster must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._softwareCluster = value
        # This is the collection of SwComponentPrototype Assignments atpVariation.
        self._swComponent: List["SwComponent"] = []

    @property
    def sw_component(self) -> List["SwComponent"]:
        """Get swComponent (Pythonic accessor)."""
        return self._swComponent
        # Software Components in the context of a CompositionSw belonging to this CP
                # Software Cluster.
        # can be used to describe the belonging the CP Software Cluster is described
                # out of of a System, e.
        # g.
        # reusable CP Software atpVariation.
        self._swComposition: List["CompositionSw"] = []

    @property
    def sw_composition(self) -> List["CompositionSw"]:
        """Get swComposition (Pythonic accessor)."""
        return self._swComposition

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getSoftwareCluster(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for softwareCluster.

        Returns:
            The softwareCluster value

        Note:
            Delegates to software_cluster property (CODING_RULE_V2_00017)
        """
        return self.software_cluster  # Delegates to property

    def setSoftwareCluster(self, value: "PositiveInteger") -> "CpSoftwareCluster":
        """
        AUTOSAR-compliant setter for softwareCluster with method chaining.

        Args:
            value: The softwareCluster to set

        Returns:
            self for method chaining

        Note:
            Delegates to software_cluster property setter (gets validation automatically)
        """
        self.software_cluster = value  # Delegates to property setter
        return self

    def getSwComponent(self) -> List["SwComponent"]:
        """
        AUTOSAR-compliant getter for swComponent.

        Returns:
            The swComponent value

        Note:
            Delegates to sw_component property (CODING_RULE_V2_00017)
        """
        return self.sw_component  # Delegates to property

    def getSwComposition(self) -> List["CompositionSw"]:
        """
        AUTOSAR-compliant getter for swComposition.

        Returns:
            The swComposition value

        Note:
            Delegates to sw_composition property (CODING_RULE_V2_00017)
        """
        return self.sw_composition  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_software_cluster(self, value: Optional["PositiveInteger"]) -> "CpSoftwareCluster":
        """
        Set softwareCluster and return self for chaining.

        Args:
            value: The softwareCluster to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_software_cluster("value")
        """
        self.software_cluster = value  # Use property setter (gets validation)
        return self
