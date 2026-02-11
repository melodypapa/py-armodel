"""
AUTOSAR Package - SoftwareCluster

Package: M2::AUTOSARTemplates::SystemTemplate::SoftwareCluster
"""


from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Identifier,
    PositiveInteger,
    RefType,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    ARElement,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
)
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.__init__ import (
    CpSoftwareClusterCommunicationResourceProps,
    CpSoftwareClusterResource,
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

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"globalResource must be PositiveInteger or str or None, got {type(value).__name__}"
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

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"isMandatory must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._isMandatory = value

    def with_dependent(self, value):
        """
        Set dependent and return self for chaining.

        Args:
            value: The dependent to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_dependent("value")
        """
        self.dependent = value  # Use property setter (gets validation)
        return self

    def with_sw_composition(self, value):
        """
        Set sw_composition and return self for chaining.

        Args:
            value: The sw_composition to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sw_composition("value")
        """
        self.sw_composition = value  # Use property setter (gets validation)
        return self

    def with_sw_cluster(self, value):
        """
        Set sw_cluster and return self for chaining.

        Args:
            value: The sw_cluster to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sw_cluster("value")
        """
        self.sw_cluster = value  # Use property setter (gets validation)
        return self

    def with_port_element_to(self, value):
        """
        Set port_element_to and return self for chaining.

        Args:
            value: The port_element_to to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_port_element_to("value")
        """
        self.port_element_to = value  # Use property setter (gets validation)
        return self

    def with_resource_to(self, value):
        """
        Set resource_to and return self for chaining.

        Args:
            value: The resource_to to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_resource_to("value")
        """
        self.resource_to = value  # Use property setter (gets validation)
        return self

    def with_swc_to(self, value):
        """
        Set swc_to and return self for chaining.

        Args:
            value: The swc_to to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_swc_to("value")
        """
        self.swc_to = value  # Use property setter (gets validation)
        return self

    def with_ecu_scope(self, value):
        """
        Set ecu_scope and return self for chaining.

        Args:
            value: The ecu_scope to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ecu_scope("value")
        """
        self.ecu_scope = value  # Use property setter (gets validation)
        return self

    def with_requester(self, value):
        """
        Set requester and return self for chaining.

        Args:
            value: The requester to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_requester("value")
        """
        self.requester = value  # Use property setter (gets validation)
        return self

    def with_resource_needs(self, value):
        """
        Set resource_needs and return self for chaining.

        Args:
            value: The resource_needs to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_resource_needs("value")
        """
        self.resource_needs = value  # Use property setter (gets validation)
        return self

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

    def setGlobalResource(self, value: "PositiveInteger") -> CpSoftwareClusterResource:
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

    def setIsMandatory(self, value: "Boolean") -> CpSoftwareClusterResource:
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

    def with_global_resource(self, value: Optional["PositiveInteger"]) -> CpSoftwareClusterResource:
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

    def with_is_mandatory(self, value: Optional["Boolean"]) -> CpSoftwareClusterResource:
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



class RoleBasedResourceDependency(ARObject):
    """
    This class specifies a dependency between CpSoftwareClusterResources.

    Package: M2::AUTOSARTemplates::SystemTemplate::SoftwareCluster::RoleBasedResourceDependency

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 272, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 902, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to resource for which the dependency is.
        self._resource: Optional[CpSoftwareCluster] = None

    @property
    def resource(self) -> Optional[CpSoftwareCluster]:
        """Get resource (Pythonic accessor)."""
        return self._resource

    @resource.setter
    def resource(self, value: Optional[CpSoftwareCluster]) -> None:
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

        if not isinstance(value, CpSoftwareCluster):
            raise TypeError(
                f"resource must be CpSoftwareCluster or None, got {type(value).__name__}"
            )
        self._resource = value
        # This is attributes characterizes the kind of dependency.
        self._role: Optional["Identifier"] = None

    @property
    def role(self) -> Optional["Identifier"]:
        """Get role (Pythonic accessor)."""
        return self._role

    @role.setter
    def role(self, value: Optional["Identifier"]) -> None:
        """
        Set role with validation.

        Args:
            value: The role to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._role = None
            return

        if not isinstance(value, (Identifier, str)):
            raise TypeError(
                f"role must be Identifier or str or None, got {type(value).__name__}"
            )
        self._role = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getResource(self) -> CpSoftwareCluster:
        """
        AUTOSAR-compliant getter for resource.

        Returns:
            The resource value

        Note:
            Delegates to resource property (CODING_RULE_V2_00017)
        """
        return self.resource  # Delegates to property

    def setResource(self, value: CpSoftwareCluster) -> RoleBasedResourceDependency:
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

    def getRole(self) -> "Identifier":
        """
        AUTOSAR-compliant getter for role.

        Returns:
            The role value

        Note:
            Delegates to role property (CODING_RULE_V2_00017)
        """
        return self.role  # Delegates to property

    def setRole(self, value: "Identifier") -> RoleBasedResourceDependency:
        """
        AUTOSAR-compliant setter for role with method chaining.

        Args:
            value: The role to set

        Returns:
            self for method chaining

        Note:
            Delegates to role property setter (gets validation automatically)
        """
        self.role = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_resource(self, value: Optional[CpSoftwareCluster]) -> RoleBasedResourceDependency:
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

    def with_role(self, value: Optional["Identifier"]) -> RoleBasedResourceDependency:
        """
        Set role and return self for chaining.

        Args:
            value: The role to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_role("value")
        """
        self.role = value  # Use property setter (gets validation)
        return self



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

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"softwareCluster must be PositiveInteger or str or None, got {type(value).__name__}"
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

    def setSoftwareCluster(self, value: "PositiveInteger") -> CpSoftwareCluster:
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

    def with_software_cluster(self, value: Optional["PositiveInteger"]) -> CpSoftwareCluster:
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



class CpSoftwareClusterToEcuInstanceMapping(Identifiable):
    """
    This meta class maps a CpSoftwareCluster to a EcuInstance.

    Package: M2::AUTOSARTemplates::SystemTemplate::SoftwareCluster::CpSoftwareClusterToEcuInstanceMapping

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 283, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to a specific ECU Instance description.
        self._ecuInstance: Optional["EcuInstance"] = None

    @property
    def ecu_instance(self) -> Optional["EcuInstance"]:
        """Get ecuInstance (Pythonic accessor)."""
        return self._ecuInstance

    @ecu_instance.setter
    def ecu_instance(self, value: Optional["EcuInstance"]) -> None:
        """
        Set ecuInstance with validation.

        Args:
            value: The ecuInstance to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ecuInstance = None
            return

        if not isinstance(value, EcuInstance):
            raise TypeError(
                f"ecuInstance must be EcuInstance or None, got {type(value).__name__}"
            )
        self._ecuInstance = value
        # Unique number of the (virtual or physical) machine to Software Cluster is
        # mapped.
        self._machineId: Optional["PositiveInteger"] = None

    @property
    def machine_id(self) -> Optional["PositiveInteger"]:
        """Get machineId (Pythonic accessor)."""
        return self._machineId

    @machine_id.setter
    def machine_id(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set machineId with validation.

        Args:
            value: The machineId to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._machineId = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"machineId must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._machineId = value
        # The mapped CP Software Cluster atpVariation.
        self._swCluster: List[CpSoftwareCluster] = []

    @property
    def sw_cluster(self) -> List[CpSoftwareCluster]:
        """Get swCluster (Pythonic accessor)."""
        return self._swCluster

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getEcuInstance(self) -> "EcuInstance":
        """
        AUTOSAR-compliant getter for ecuInstance.

        Returns:
            The ecuInstance value

        Note:
            Delegates to ecu_instance property (CODING_RULE_V2_00017)
        """
        return self.ecu_instance  # Delegates to property

    def setEcuInstance(self, value: "EcuInstance") -> CpSoftwareClusterToEcuInstanceMapping:
        """
        AUTOSAR-compliant setter for ecuInstance with method chaining.

        Args:
            value: The ecuInstance to set

        Returns:
            self for method chaining

        Note:
            Delegates to ecu_instance property setter (gets validation automatically)
        """
        self.ecu_instance = value  # Delegates to property setter
        return self

    def getMachineId(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for machineId.

        Returns:
            The machineId value

        Note:
            Delegates to machine_id property (CODING_RULE_V2_00017)
        """
        return self.machine_id  # Delegates to property

    def setMachineId(self, value: "PositiveInteger") -> CpSoftwareClusterToEcuInstanceMapping:
        """
        AUTOSAR-compliant setter for machineId with method chaining.

        Args:
            value: The machineId to set

        Returns:
            self for method chaining

        Note:
            Delegates to machine_id property setter (gets validation automatically)
        """
        self.machine_id = value  # Delegates to property setter
        return self

    def getSwCluster(self) -> List[CpSoftwareCluster]:
        """
        AUTOSAR-compliant getter for swCluster.

        Returns:
            The swCluster value

        Note:
            Delegates to sw_cluster property (CODING_RULE_V2_00017)
        """
        return self.sw_cluster  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_ecu_instance(self, value: Optional["EcuInstance"]) -> CpSoftwareClusterToEcuInstanceMapping:
        """
        Set ecuInstance and return self for chaining.

        Args:
            value: The ecuInstance to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ecu_instance("value")
        """
        self.ecu_instance = value  # Use property setter (gets validation)
        return self

    def with_machine_id(self, value: Optional["PositiveInteger"]) -> CpSoftwareClusterToEcuInstanceMapping:
        """
        Set machineId and return self for chaining.

        Args:
            value: The machineId to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_machine_id("value")
        """
        self.machine_id = value  # Use property setter (gets validation)
        return self



class CpSoftwareClusterResourceToApplicationPartitionMapping(Identifiable):
    """
    This meta class maps a Software Cluster resource to an Application Partition
    to restrict the usage.

    Package: M2::AUTOSARTemplates::SystemTemplate::SoftwareCluster::CpSoftwareClusterResourceToApplicationPartitionMapping

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 284, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # ApplicationPartition for which the mapping applies.
        self._application: Optional["ApplicationPartition"] = None

    @property
    def application(self) -> Optional["ApplicationPartition"]:
        """Get application (Pythonic accessor)."""
        return self._application

    @application.setter
    def application(self, value: Optional["ApplicationPartition"]) -> None:
        """
        Set application with validation.

        Args:
            value: The application to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._application = None
            return

        if not isinstance(value, ApplicationPartition):
            raise TypeError(
                f"application must be ApplicationPartition or None, got {type(value).__name__}"
            )
        self._application = value
        # Software Cluster Resource for which the mapping applies.
        self._resource: Optional[CpSoftwareCluster] = None

    @property
    def resource(self) -> Optional[CpSoftwareCluster]:
        """Get resource (Pythonic accessor)."""
        return self._resource

    @resource.setter
    def resource(self, value: Optional[CpSoftwareCluster]) -> None:
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

        if not isinstance(value, CpSoftwareCluster):
            raise TypeError(
                f"resource must be CpSoftwareCluster or None, got {type(value).__name__}"
            )
        self._resource = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getApplication(self) -> "ApplicationPartition":
        """
        AUTOSAR-compliant getter for application.

        Returns:
            The application value

        Note:
            Delegates to application property (CODING_RULE_V2_00017)
        """
        return self.application  # Delegates to property

    def setApplication(self, value: "ApplicationPartition") -> CpSoftwareClusterResourceToApplicationPartitionMapping:
        """
        AUTOSAR-compliant setter for application with method chaining.

        Args:
            value: The application to set

        Returns:
            self for method chaining

        Note:
            Delegates to application property setter (gets validation automatically)
        """
        self.application = value  # Delegates to property setter
        return self

    def getResource(self) -> CpSoftwareCluster:
        """
        AUTOSAR-compliant getter for resource.

        Returns:
            The resource value

        Note:
            Delegates to resource property (CODING_RULE_V2_00017)
        """
        return self.resource  # Delegates to property

    def setResource(self, value: CpSoftwareCluster) -> CpSoftwareClusterResourceToApplicationPartitionMapping:
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

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_application(self, value: Optional["ApplicationPartition"]) -> CpSoftwareClusterResourceToApplicationPartitionMapping:
        """
        Set application and return self for chaining.

        Args:
            value: The application to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_application("value")
        """
        self.application = value  # Use property setter (gets validation)
        return self

    def with_resource(self, value: Optional[CpSoftwareCluster]) -> CpSoftwareClusterResourceToApplicationPartitionMapping:
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
        self._resourceTo: List[CpSoftwareCluster] = []

    @property
    def resource_to(self) -> List[CpSoftwareCluster]:
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

    def getResourceTo(self) -> List[CpSoftwareCluster]:
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



class CpSoftwareClusterToApplicationPartitionMapping(Identifiable):
    """
    This meta class defines ApplicationPartitions that are applicable for the
    CpSoftwareCluster.

    Package: M2::AUTOSARTemplates::SystemTemplate::SoftwareCluster::CpSoftwareClusterToApplicationPartitionMapping

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 287, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Collection of ApplicationPartitions available in the Cp.
        self._application: List["ApplicationPartition"] = []

    @property
    def application(self) -> List["ApplicationPartition"]:
        """Get application (Pythonic accessor)."""
        return self._application
        # Software Cluster Resource for which the mapping applies.
        self._softwareCluster: Optional[CpSoftwareCluster] = None

    @property
    def software_cluster(self) -> Optional[CpSoftwareCluster]:
        """Get softwareCluster (Pythonic accessor)."""
        return self._softwareCluster

    @software_cluster.setter
    def software_cluster(self, value: Optional[CpSoftwareCluster]) -> None:
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

        if not isinstance(value, CpSoftwareCluster):
            raise TypeError(
                f"softwareCluster must be CpSoftwareCluster or None, got {type(value).__name__}"
            )
        self._softwareCluster = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getApplication(self) -> List["ApplicationPartition"]:
        """
        AUTOSAR-compliant getter for application.

        Returns:
            The application value

        Note:
            Delegates to application property (CODING_RULE_V2_00017)
        """
        return self.application  # Delegates to property

    def getSoftwareCluster(self) -> CpSoftwareCluster:
        """
        AUTOSAR-compliant getter for softwareCluster.

        Returns:
            The softwareCluster value

        Note:
            Delegates to software_cluster property (CODING_RULE_V2_00017)
        """
        return self.software_cluster  # Delegates to property

    def setSoftwareCluster(self, value: CpSoftwareCluster) -> CpSoftwareClusterToApplicationPartitionMapping:
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

    def with_software_cluster(self, value: Optional[CpSoftwareCluster]) -> CpSoftwareClusterToApplicationPartitionMapping:
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



class SystemSignalToCommunicationResourceMapping(Identifiable):
    """
    This meta class maps a communication resource to a SystemSignal. This
    mapping can be used in an early process stage in which the DataMapping
    linking the Ports and mapped CpSoftwareCluster CommunicationResource(s) to
    the SystemSignal is not yet available.

    Package: M2::AUTOSARTemplates::SystemTemplate::SoftwareCluster::SystemSignalToCommunicationResourceMapping

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 289, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Communication resource for which the mapping applies.
        self._softwareCluster: Optional[CpSoftwareCluster] = None

    @property
    def software_cluster(self) -> Optional[CpSoftwareCluster]:
        """Get softwareCluster (Pythonic accessor)."""
        return self._softwareCluster

    @software_cluster.setter
    def software_cluster(self, value: Optional[CpSoftwareCluster]) -> None:
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

        if not isinstance(value, CpSoftwareCluster):
            raise TypeError(
                f"softwareCluster must be CpSoftwareCluster or None, got {type(value).__name__}"
            )
        self._softwareCluster = value
        # SystemSignal to which the communication resource is.
        self._systemSignal: Optional["SystemSignal"] = None

    @property
    def system_signal(self) -> Optional["SystemSignal"]:
        """Get systemSignal (Pythonic accessor)."""
        return self._systemSignal

    @system_signal.setter
    def system_signal(self, value: Optional["SystemSignal"]) -> None:
        """
        Set systemSignal with validation.

        Args:
            value: The systemSignal to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._systemSignal = None
            return

        if not isinstance(value, SystemSignal):
            raise TypeError(
                f"systemSignal must be SystemSignal or None, got {type(value).__name__}"
            )
        self._systemSignal = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getSoftwareCluster(self) -> CpSoftwareCluster:
        """
        AUTOSAR-compliant getter for softwareCluster.

        Returns:
            The softwareCluster value

        Note:
            Delegates to software_cluster property (CODING_RULE_V2_00017)
        """
        return self.software_cluster  # Delegates to property

    def setSoftwareCluster(self, value: CpSoftwareCluster) -> SystemSignalToCommunicationResourceMapping:
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

    def getSystemSignal(self) -> "SystemSignal":
        """
        AUTOSAR-compliant getter for systemSignal.

        Returns:
            The systemSignal value

        Note:
            Delegates to system_signal property (CODING_RULE_V2_00017)
        """
        return self.system_signal  # Delegates to property

    def setSystemSignal(self, value: "SystemSignal") -> SystemSignalToCommunicationResourceMapping:
        """
        AUTOSAR-compliant setter for systemSignal with method chaining.

        Args:
            value: The systemSignal to set

        Returns:
            self for method chaining

        Note:
            Delegates to system_signal property setter (gets validation automatically)
        """
        self.system_signal = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_software_cluster(self, value: Optional[CpSoftwareCluster]) -> SystemSignalToCommunicationResourceMapping:
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

    def with_system_signal(self, value: Optional["SystemSignal"]) -> SystemSignalToCommunicationResourceMapping:
        """
        Set systemSignal and return self for chaining.

        Args:
            value: The systemSignal to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_system_signal("value")
        """
        self.system_signal = value  # Use property setter (gets validation)
        return self



class SystemSignalGroupToCommunicationResourceMapping(Identifiable):
    """
    This meta class maps a communication resource to a SystemSignalGroup. This
    mapping can be used in an early process stage in which the DataMapping
    linking the Ports and mapped CpSoftwareCluster CommunicationResource(s) to
    SystemSignals of a SystemSignalGroup is not yet available.

    Package: M2::AUTOSARTemplates::SystemTemplate::SoftwareCluster::SystemSignalGroupToCommunicationResourceMapping

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 290, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Communication resource for which the mapping applies.
        self._softwareCluster: Optional[CpSoftwareCluster] = None

    @property
    def software_cluster(self) -> Optional[CpSoftwareCluster]:
        """Get softwareCluster (Pythonic accessor)."""
        return self._softwareCluster

    @software_cluster.setter
    def software_cluster(self, value: Optional[CpSoftwareCluster]) -> None:
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

        if not isinstance(value, CpSoftwareCluster):
            raise TypeError(
                f"softwareCluster must be CpSoftwareCluster or None, got {type(value).__name__}"
            )
        self._softwareCluster = value
        # SystemSignalGroup to which the communication is assigned.
        self._systemSignal: Optional["RefType"] = None

    @property
    def system_signal(self) -> Optional["RefType"]:
        """Get systemSignal (Pythonic accessor)."""
        return self._systemSignal

    @system_signal.setter
    def system_signal(self, value: Optional["RefType"]) -> None:
        """
        Set systemSignal with validation.

        Args:
            value: The systemSignal to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._systemSignal = None
            return

        self._systemSignal = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getSoftwareCluster(self) -> CpSoftwareCluster:
        """
        AUTOSAR-compliant getter for softwareCluster.

        Returns:
            The softwareCluster value

        Note:
            Delegates to software_cluster property (CODING_RULE_V2_00017)
        """
        return self.software_cluster  # Delegates to property

    def setSoftwareCluster(self, value: CpSoftwareCluster) -> SystemSignalGroupToCommunicationResourceMapping:
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

    def getSystemSignal(self) -> "RefType":
        """
        AUTOSAR-compliant getter for systemSignal.

        Returns:
            The systemSignal value

        Note:
            Delegates to system_signal property (CODING_RULE_V2_00017)
        """
        return self.system_signal  # Delegates to property

    def setSystemSignal(self, value: "RefType") -> SystemSignalGroupToCommunicationResourceMapping:
        """
        AUTOSAR-compliant setter for systemSignal with method chaining.

        Args:
            value: The systemSignal to set

        Returns:
            self for method chaining

        Note:
            Delegates to system_signal property setter (gets validation automatically)
        """
        self.system_signal = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_software_cluster(self, value: Optional[CpSoftwareCluster]) -> SystemSignalGroupToCommunicationResourceMapping:
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

    def with_system_signal(self, value: Optional[RefType]) -> SystemSignalGroupToCommunicationResourceMapping:
        """
        Set systemSignal and return self for chaining.

        Args:
            value: The systemSignal to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_system_signal("value")
        """
        self.system_signal = value  # Use property setter (gets validation)
        return self



class SwComponentPrototypeAssignment(ARObject):
    """
    This meta-class is only required to allow for the variant modeling of an
    instanceRef.

    Package: M2::AUTOSARTemplates::SystemTemplate::SoftwareCluster::SwComponentPrototypeAssignment

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 894, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # CP Software Cluster.
        # This reference is used to belonging SWCs if the CP Software Cluster in the
                # context of a System, by: ComponentInSystem.
        self._swComponent: Optional["SwComponent"] = None

    @property
    def sw_component(self) -> Optional["SwComponent"]:
        """Get swComponent (Pythonic accessor)."""
        return self._swComponent

    @sw_component.setter
    def sw_component(self, value: Optional["SwComponent"]) -> None:
        """
        Set swComponent with validation.

        Args:
            value: The swComponent to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._swComponent = None
            return

        if not isinstance(value, SwComponent):
            raise TypeError(
                f"swComponent must be SwComponent or None, got {type(value).__name__}"
            )
        self._swComponent = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getSwComponent(self) -> "SwComponent":
        """
        AUTOSAR-compliant getter for swComponent.

        Returns:
            The swComponent value

        Note:
            Delegates to sw_component property (CODING_RULE_V2_00017)
        """
        return self.sw_component  # Delegates to property

    def setSwComponent(self, value: "SwComponent") -> SwComponentPrototypeAssignment:
        """
        AUTOSAR-compliant setter for swComponent with method chaining.

        Args:
            value: The swComponent to set

        Returns:
            self for method chaining

        Note:
            Delegates to sw_component property setter (gets validation automatically)
        """
        self.sw_component = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_sw_component(self, value: Optional["SwComponent"]) -> SwComponentPrototypeAssignment:
        """
        Set swComponent and return self for chaining.

        Args:
            value: The swComponent to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sw_component("value")
        """
        self.sw_component = value  # Use property setter (gets validation)
        return self



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
        self._resource: List[CpSoftwareCluster] = []

    @property
    def resource(self) -> List[CpSoftwareCluster]:
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

    def getResource(self) -> List[CpSoftwareCluster]:
        """
        AUTOSAR-compliant getter for resource.

        Returns:
            The resource value

        Note:
            Delegates to resource property (CODING_RULE_V2_00017)
        """
        return self.resource  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class CpSoftwareClusterCommunicationResourceProps(ARObject, ABC):
    """
    Communication properties for cross cluster communication.

    Package: M2::AUTOSARTemplates::SystemTemplate::SoftwareCluster::CpSoftwareClusterCommunicationResourceProps

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 902, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is CpSoftwareClusterCommunicationResourceProps:
            raise TypeError("CpSoftwareClusterCommunicationResourceProps is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class CpSoftwareClusterToResourceMapping(Identifiable):
    """
    This meta class maps a service resource to CP Software Clusters. By this
    mapping it’s specified whether the Software Cluster has to provide or to
    require the resource.

    Package: M2::AUTOSARTemplates::SystemTemplate::SoftwareCluster::CpSoftwareClusterToResourceMapping

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 907, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # CP Software Cluster providing the resource.
        self._provider: Optional[CpSoftwareCluster] = None

    @property
    def provider(self) -> Optional[CpSoftwareCluster]:
        """Get provider (Pythonic accessor)."""
        return self._provider

    @provider.setter
    def provider(self, value: Optional[CpSoftwareCluster]) -> None:
        """
        Set provider with validation.

        Args:
            value: The provider to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._provider = None
            return

        if not isinstance(value, CpSoftwareCluster):
            raise TypeError(
                f"provider must be CpSoftwareCluster or None, got {type(value).__name__}"
            )
        self._provider = value
        # CP Software Cluster requesting the resource.
        self._requester: List[CpSoftwareCluster] = []

    @property
    def requester(self) -> List[CpSoftwareCluster]:
        """Get requester (Pythonic accessor)."""
        return self._requester
        # Service resource for which the mapping applies.
        self._service: Optional[CpSoftwareCluster] = None

    @property
    def service(self) -> Optional[CpSoftwareCluster]:
        """Get service (Pythonic accessor)."""
        return self._service

    @service.setter
    def service(self, value: Optional[CpSoftwareCluster]) -> None:
        """
        Set service with validation.

        Args:
            value: The service to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._service = None
            return

        if not isinstance(value, CpSoftwareCluster):
            raise TypeError(
                f"service must be CpSoftwareCluster or None, got {type(value).__name__}"
            )
        self._service = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getProvider(self) -> CpSoftwareCluster:
        """
        AUTOSAR-compliant getter for provider.

        Returns:
            The provider value

        Note:
            Delegates to provider property (CODING_RULE_V2_00017)
        """
        return self.provider  # Delegates to property

    def setProvider(self, value: CpSoftwareCluster) -> CpSoftwareClusterToResourceMapping:
        """
        AUTOSAR-compliant setter for provider with method chaining.

        Args:
            value: The provider to set

        Returns:
            self for method chaining

        Note:
            Delegates to provider property setter (gets validation automatically)
        """
        self.provider = value  # Delegates to property setter
        return self

    def getRequester(self) -> List[CpSoftwareCluster]:
        """
        AUTOSAR-compliant getter for requester.

        Returns:
            The requester value

        Note:
            Delegates to requester property (CODING_RULE_V2_00017)
        """
        return self.requester  # Delegates to property

    def getService(self) -> CpSoftwareCluster:
        """
        AUTOSAR-compliant getter for service.

        Returns:
            The service value

        Note:
            Delegates to service property (CODING_RULE_V2_00017)
        """
        return self.service  # Delegates to property

    def setService(self, value: CpSoftwareCluster) -> CpSoftwareClusterToResourceMapping:
        """
        AUTOSAR-compliant setter for service with method chaining.

        Args:
            value: The service to set

        Returns:
            self for method chaining

        Note:
            Delegates to service property setter (gets validation automatically)
        """
        self.service = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_provider(self, value: Optional[CpSoftwareCluster]) -> CpSoftwareClusterToResourceMapping:
        """
        Set provider and return self for chaining.

        Args:
            value: The provider to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_provider("value")
        """
        self.provider = value  # Use property setter (gets validation)
        return self

    def with_service(self, value: Optional[CpSoftwareCluster]) -> CpSoftwareClusterToResourceMapping:
        """
        Set service and return self for chaining.

        Args:
            value: The service to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_service("value")
        """
        self.service = value  # Use property setter (gets validation)
        return self



class CpSoftwareClusterCommunicationResource(CpSoftwareClusterResource):
    """
    Represents a single resource required or provided by a CP Software Cluster
    which relates to the port based communication on VFB level.

    Package: M2::AUTOSARTemplates::SystemTemplate::SoftwareCluster::CpSoftwareClusterCommunicationResource

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 902, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This aggregation supports the further qualification of the enclosing
        # CpSoftwareClusterCommunicationRecource by of additional attributes depending
        # on the nature of.
        self._communication: Optional[CpSoftwareCluster] = None

    @property
    def communication(self) -> Optional[CpSoftwareCluster]:
        """Get communication (Pythonic accessor)."""
        return self._communication

    @communication.setter
    def communication(self, value: Optional[CpSoftwareCluster]) -> None:
        """
        Set communication with validation.

        Args:
            value: The communication to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._communication = None
            return

        if not isinstance(value, CpSoftwareCluster):
            raise TypeError(
                f"communication must be CpSoftwareCluster or None, got {type(value).__name__}"
            )
        self._communication = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCommunication(self) -> CpSoftwareCluster:
        """
        AUTOSAR-compliant getter for communication.

        Returns:
            The communication value

        Note:
            Delegates to communication property (CODING_RULE_V2_00017)
        """
        return self.communication  # Delegates to property

    def setCommunication(self, value: CpSoftwareCluster) -> CpSoftwareClusterCommunicationResource:
        """
        AUTOSAR-compliant setter for communication with method chaining.

        Args:
            value: The communication to set

        Returns:
            self for method chaining

        Note:
            Delegates to communication property setter (gets validation automatically)
        """
        self.communication = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_communication(self, value: Optional[CpSoftwareCluster]) -> CpSoftwareClusterCommunicationResource:
        """
        Set communication and return self for chaining.

        Args:
            value: The communication to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_communication("value")
        """
        self.communication = value  # Use property setter (gets validation)
        return self



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



class DataComProps(CpSoftwareClusterCommunicationResourceProps):
    """
    Represents a single resource required or provided by a CP Software Cluster
    which relates to the port based communication on VFB level.

    Package: M2::AUTOSARTemplates::SystemTemplate::SoftwareCluster::DataComProps

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 903, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute defines requirements on the data consistency mechanism in the
        # cross cluster If the attribute is not set, the default value.
        self._data: Optional["DataConsistencyPolicy"] = None

    @property
    def data(self) -> Optional["DataConsistencyPolicy"]:
        """Get data (Pythonic accessor)."""
        return self._data

    @data.setter
    def data(self, value: Optional["DataConsistencyPolicy"]) -> None:
        """
        Set data with validation.

        Args:
            value: The data to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._data = None
            return

        if not isinstance(value, DataConsistencyPolicy):
            raise TypeError(
                f"data must be DataConsistencyPolicy or None, got {type(value).__name__}"
            )
        self._data = value
        # Send indication behavior for last-is-the best data.
        self._sendIndication: Optional[SendIndicationEnum] = None

    @property
    def send_indication(self) -> Optional[SendIndicationEnum]:
        """Get sendIndication (Pythonic accessor)."""
        return self._sendIndication

    @send_indication.setter
    def send_indication(self, value: Optional[SendIndicationEnum]) -> None:
        """
        Set sendIndication with validation.

        Args:
            value: The sendIndication to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sendIndication = None
            return

        if not isinstance(value, SendIndicationEnum):
            raise TypeError(
                f"sendIndication must be SendIndicationEnum or None, got {type(value).__name__}"
            )
        self._sendIndication = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getData(self) -> "DataConsistencyPolicy":
        """
        AUTOSAR-compliant getter for data.

        Returns:
            The data value

        Note:
            Delegates to data property (CODING_RULE_V2_00017)
        """
        return self.data  # Delegates to property

    def setData(self, value: "DataConsistencyPolicy") -> DataComProps:
        """
        AUTOSAR-compliant setter for data with method chaining.

        Args:
            value: The data to set

        Returns:
            self for method chaining

        Note:
            Delegates to data property setter (gets validation automatically)
        """
        self.data = value  # Delegates to property setter
        return self

    def getSendIndication(self) -> SendIndicationEnum:
        """
        AUTOSAR-compliant getter for sendIndication.

        Returns:
            The sendIndication value

        Note:
            Delegates to send_indication property (CODING_RULE_V2_00017)
        """
        return self.send_indication  # Delegates to property

    def setSendIndication(self, value: SendIndicationEnum) -> DataComProps:
        """
        AUTOSAR-compliant setter for sendIndication with method chaining.

        Args:
            value: The sendIndication to set

        Returns:
            self for method chaining

        Note:
            Delegates to send_indication property setter (gets validation automatically)
        """
        self.send_indication = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_data(self, value: Optional["DataConsistencyPolicy"]) -> DataComProps:
        """
        Set data and return self for chaining.

        Args:
            value: The data to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_data("value")
        """
        self.data = value  # Use property setter (gets validation)
        return self

    def with_send_indication(self, value: Optional[SendIndicationEnum]) -> DataComProps:
        """
        Set sendIndication and return self for chaining.

        Args:
            value: The sendIndication to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_send_indication("value")
        """
        self.send_indication = value  # Use property setter (gets validation)
        return self



class ClientServerOperationComProps(CpSoftwareClusterCommunicationResourceProps):
    """
    Defines additional attributes for the implementation of Client Server
    communication between software clusters

    Package: M2::AUTOSARTemplates::SystemTemplate::SoftwareCluster::ClientServerOperationComProps

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 903, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Length of call request queue on the server side.
        # The implemented by the SwCluC.
        # The value shall be equal to 1.
        # Setting the value of queueLength to that incoming requests are rejected while
                # that arrived earlier is being processed.
        self._queueLength: Optional["PositiveInteger"] = None

    @property
    def queue_length(self) -> Optional["PositiveInteger"]:
        """Get queueLength (Pythonic accessor)."""
        return self._queueLength

    @queue_length.setter
    def queue_length(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set queueLength with validation.

        Args:
            value: The queueLength to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._queueLength = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"queueLength must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._queueLength = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getQueueLength(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for queueLength.

        Returns:
            The queueLength value

        Note:
            Delegates to queue_length property (CODING_RULE_V2_00017)
        """
        return self.queue_length  # Delegates to property

    def setQueueLength(self, value: "PositiveInteger") -> ClientServerOperationComProps:
        """
        AUTOSAR-compliant setter for queueLength with method chaining.

        Args:
            value: The queueLength to set

        Returns:
            self for method chaining

        Note:
            Delegates to queue_length property setter (gets validation automatically)
        """
        self.queue_length = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_queue_length(self, value: Optional["PositiveInteger"]) -> ClientServerOperationComProps:
        """
        Set queueLength and return self for chaining.

        Args:
            value: The queueLength to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_queue_length("value")
        """
        self.queue_length = value  # Use property setter (gets validation)
        return self


class DataConsistencyPolicyEnum(AREnum):
    """
    DataConsistencyPolicyEnum enumeration

Defines how data consistency is ensured in the cross cluster communication. Aggregated by DataComProps.dataConsistencyPolicy

Package: M2::AUTOSARTemplates::SystemTemplate::SoftwareCluster
    """
    # In this case the data consistency is ensured by the implementation of the SwClucC module.
    consistencyMechanism = "0"

    # In this case the data consistency is not ensured by the SwClucC module. In this case it has to be Mechanism ensured by scheduling.
    noConsistency = "1"



class SendIndicationEnum(AREnum):
    """
    SendIndicationEnum enumeration

This meta-class provides a way to specify in which way redundancy shall be applied on collection level. Aggregated by DataComProps.sendIndication

Package: M2::AUTOSARTemplates::SystemTemplate::SoftwareCluster
    """
    # Template
    System = "None"

    # CP R23-11
    AUTOSAR = "None"

    # This value represents the requirement that any send operation of the Software Cluster is indicated.
    anySendOperation = "2"

    # This value represents the requirement that send operations of the Software Cluster are not indicated.
    none = "1"


__all__ = [
    CpSoftwareClusterResource,
    RoleBasedResourceDependency,
    CpSoftwareCluster,
    CpSoftwareClusterToEcuInstanceMapping,
    CpSoftwareClusterResourceToApplicationPartitionMapping,
    CpSoftwareClusterMappingSet,
    CpSoftwareClusterToApplicationPartitionMapping,
    SystemSignalToCommunicationResourceMapping,
    SystemSignalGroupToCommunicationResourceMapping,
    SwComponentPrototypeAssignment,
    CpSoftwareClusterResourcePool,
    CpSoftwareClusterCommunicationResourceProps,
    CpSoftwareClusterToResourceMapping,
    CpSoftwareClusterCommunicationResource,
    CpSoftwareClusterServiceResource,
    DataComProps,
    ClientServerOperationComProps,
    DataConsistencyPolicyEnum,
    SendIndicationEnum,
]
