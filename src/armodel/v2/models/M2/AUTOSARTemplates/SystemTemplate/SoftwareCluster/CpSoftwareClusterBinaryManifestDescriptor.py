from typing import List, Optional
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARElement


class CpSoftwareClusterBinaryManifestDescriptor(ARElement):
    """
    This meta-class has the ability to act as a hub for all information related
    to the binary manifest of a given CP software cluster. The manifest is
    subject to integrator work and therefore not a part of the definition of the
    CP software cluster itself.

    Package: M2::AUTOSARTemplates::SystemTemplate::SoftwareCluster::BinaryManifest::CpSoftwareClusterBinaryManifestDescriptor

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 913, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This reference identifies the CpSoftwareCluster to which enclosing
                # CpSoftwareClusterBinaryManifest is an integration phase while the referenced
                # Cp a design element.
        # Therefore, sense to use a reference rather than an the relation of the two
                # meta-classes.
        self._cpSoftware: Optional["CpSoftwareCluster"] = None

    @property
    def cp_software(self) -> Optional["CpSoftwareCluster"]:
        """Get cpSoftware (Pythonic accessor)."""
        return self._cpSoftware

    @cp_software.setter
    def cp_software(self, value: Optional["CpSoftwareCluster"]) -> None:
        """
        Set cpSoftware with validation.

        Args:
            value: The cpSoftware to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._cpSoftware = None
            return

        if not isinstance(value, CpSoftwareCluster):
            raise TypeError(
                f"cpSoftware must be CpSoftwareCluster or None, got {type(value).__name__}"
            )
        self._cpSoftware = value
        # This aggregation identifies the collection of meta-data in the enclosing
        # binary manifest.
        self._metaDataField: List["BinaryManifestMeta"] = []

    @property
    def meta_data_field(self) -> List["BinaryManifestMeta"]:
        """Get metaDataField (Pythonic accessor)."""
        return self._metaDataField
        # This aggregation represents the collection of provided resources in the
        # enclosing binary manifest.
        self._provide: List["BinaryManifestProvide"] = []

    @property
    def provide(self) -> List["BinaryManifestProvide"]:
        """Get provide (Pythonic accessor)."""
        return self._provide
        # This aggregation represents the collection of required resources in the
        # enclosing binary manifest.
        self._require: List["BinaryManifestRequire"] = []

    @property
    def require(self) -> List["BinaryManifestRequire"]:
        """Get require (Pythonic accessor)."""
        return self._require
        # This aggregation represents the collection of binary manifest resource
        # definitions that belong to the enclosing.
        self._resource: List["BinaryManifest"] = []

    @property
    def resource(self) -> List["BinaryManifest"]:
        """Get resource (Pythonic accessor)."""
        return self._resource
        # This attribute represents the value of the id of the CP software cluster.
        # This id is assigned by but may also be copied from CpSoftware available.
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

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCpSoftware(self) -> "CpSoftwareCluster":
        """
        AUTOSAR-compliant getter for cpSoftware.

        Returns:
            The cpSoftware value

        Note:
            Delegates to cp_software property (CODING_RULE_V2_00017)
        """
        return self.cp_software  # Delegates to property

    def setCpSoftware(self, value: "CpSoftwareCluster") -> "CpSoftwareClusterBinaryManifestDescriptor":
        """
        AUTOSAR-compliant setter for cpSoftware with method chaining.

        Args:
            value: The cpSoftware to set

        Returns:
            self for method chaining

        Note:
            Delegates to cp_software property setter (gets validation automatically)
        """
        self.cp_software = value  # Delegates to property setter
        return self

    def getMetaDataField(self) -> List["BinaryManifestMeta"]:
        """
        AUTOSAR-compliant getter for metaDataField.

        Returns:
            The metaDataField value

        Note:
            Delegates to meta_data_field property (CODING_RULE_V2_00017)
        """
        return self.meta_data_field  # Delegates to property

    def getProvide(self) -> List["BinaryManifestProvide"]:
        """
        AUTOSAR-compliant getter for provide.

        Returns:
            The provide value

        Note:
            Delegates to provide property (CODING_RULE_V2_00017)
        """
        return self.provide  # Delegates to property

    def getRequire(self) -> List["BinaryManifestRequire"]:
        """
        AUTOSAR-compliant getter for require.

        Returns:
            The require value

        Note:
            Delegates to require property (CODING_RULE_V2_00017)
        """
        return self.require  # Delegates to property

    def getResource(self) -> List["BinaryManifest"]:
        """
        AUTOSAR-compliant getter for resource.

        Returns:
            The resource value

        Note:
            Delegates to resource property (CODING_RULE_V2_00017)
        """
        return self.resource  # Delegates to property

    def getSoftwareCluster(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for softwareCluster.

        Returns:
            The softwareCluster value

        Note:
            Delegates to software_cluster property (CODING_RULE_V2_00017)
        """
        return self.software_cluster  # Delegates to property

    def setSoftwareCluster(self, value: "PositiveInteger") -> "CpSoftwareClusterBinaryManifestDescriptor":
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

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_cp_software(self, value: Optional["CpSoftwareCluster"]) -> "CpSoftwareClusterBinaryManifestDescriptor":
        """
        Set cpSoftware and return self for chaining.

        Args:
            value: The cpSoftware to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_cp_software("value")
        """
        self.cp_software = value  # Use property setter (gets validation)
        return self

    def with_software_cluster(self, value: Optional["PositiveInteger"]) -> "CpSoftwareClusterBinaryManifestDescriptor":
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
