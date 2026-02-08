from typing import (
    List,
    Optional,
)

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    ARElement,
)


class CpSoftwareClusterBinaryManifestDescriptor(ARElement):
    """
    This meta-class has the ability to act as a hub for all information related
    to the binary manifest of a given CP software cluster. The manifest is
    subject to integrator work and therefore not a part of the definition of the
    CP software cluster itself.

    Package: M2::AUTOSARTemplates::SystemTemplate::SoftwareCluster::BinaryManifest

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

from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.BinaryManifest import (
    BinaryManifestResource,
)


class BinaryManifestProvideResource(BinaryManifestResource):
    """
    This meta-class represents a provided resource in the binary manifest.

    Package: M2::AUTOSARTemplates::SystemTemplate::SoftwareCluster::BinaryManifest

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 914, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute provides an upper limit for the number of for this resource.
        self._numberOf: Optional["PositiveInteger"] = None

    @property
    def number_of(self) -> Optional["PositiveInteger"]:
        """Get numberOf (Pythonic accessor)."""
        return self._numberOf

    @number_of.setter
    def number_of(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set numberOf with validation.

        Args:
            value: The numberOf to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._numberOf = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"numberOf must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._numberOf = value
        # This attribute indicates whether the enclosing Binary supports multiple
        # notifiers sets.
        self._supports: Optional["Boolean"] = None

    @property
    def supports(self) -> Optional["Boolean"]:
        """Get supports (Pythonic accessor)."""
        return self._supports

    @supports.setter
    def supports(self, value: Optional["Boolean"]) -> None:
        """
        Set supports with validation.

        Args:
            value: The supports to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._supports = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"supports must be Boolean or None, got {type(value).__name__}"
            )
        self._supports = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getNumberOf(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for numberOf.

        Returns:
            The numberOf value

        Note:
            Delegates to number_of property (CODING_RULE_V2_00017)
        """
        return self.number_of  # Delegates to property

    def setNumberOf(self, value: "PositiveInteger") -> "BinaryManifestProvideResource":
        """
        AUTOSAR-compliant setter for numberOf with method chaining.

        Args:
            value: The numberOf to set

        Returns:
            self for method chaining

        Note:
            Delegates to number_of property setter (gets validation automatically)
        """
        self.number_of = value  # Delegates to property setter
        return self

    def getSupports(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for supports.

        Returns:
            The supports value

        Note:
            Delegates to supports property (CODING_RULE_V2_00017)
        """
        return self.supports  # Delegates to property

    def setSupports(self, value: "Boolean") -> "BinaryManifestProvideResource":
        """
        AUTOSAR-compliant setter for supports with method chaining.

        Args:
            value: The supports to set

        Returns:
            self for method chaining

        Note:
            Delegates to supports property setter (gets validation automatically)
        """
        self.supports = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_number_of(self, value: Optional["PositiveInteger"]) -> "BinaryManifestProvideResource":
        """
        Set numberOf and return self for chaining.

        Args:
            value: The numberOf to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_number_of("value")
        """
        self.number_of = value  # Use property setter (gets validation)
        return self

    def with_supports(self, value: Optional["Boolean"]) -> "BinaryManifestProvideResource":
        """
        Set supports and return self for chaining.

        Args:
            value: The supports to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_supports("value")
        """
        self.supports = value  # Use property setter (gets validation)
        return self

from abc import ABC
from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class BinaryManifestResource(Identifiable, ABC):
    """
    This meta-class acts as an abstract base class for specializations.

    Package: M2::AUTOSARTemplates::SystemTemplate::SoftwareCluster::BinaryManifest

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

from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.BinaryManifest import (
    BinaryManifestResource,
)


class BinaryManifestRequireResource(BinaryManifestResource):
    """
    This meta-class represents a required resource in the binary manifest.

    Package: M2::AUTOSARTemplates::SystemTemplate::SoftwareCluster::BinaryManifest

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 916, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute indicates whether the connection of the BinaryManifestResource
        # is mandatory.
        self._connectionIs: Optional["Boolean"] = None

    @property
    def connection_is(self) -> Optional["Boolean"]:
        """Get connectionIs (Pythonic accessor)."""
        return self._connectionIs

    @connection_is.setter
    def connection_is(self, value: Optional["Boolean"]) -> None:
        """
        Set connectionIs with validation.

        Args:
            value: The connectionIs to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._connectionIs = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"connectionIs must be Boolean or None, got {type(value).__name__}"
            )
        self._connectionIs = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getConnectionIs(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for connectionIs.

        Returns:
            The connectionIs value

        Note:
            Delegates to connection_is property (CODING_RULE_V2_00017)
        """
        return self.connection_is  # Delegates to property

    def setConnectionIs(self, value: "Boolean") -> "BinaryManifestRequireResource":
        """
        AUTOSAR-compliant setter for connectionIs with method chaining.

        Args:
            value: The connectionIs to set

        Returns:
            self for method chaining

        Note:
            Delegates to connection_is property setter (gets validation automatically)
        """
        self.connection_is = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_connection_is(self, value: Optional["Boolean"]) -> "BinaryManifestRequireResource":
        """
        Set connectionIs and return self for chaining.

        Args:
            value: The connectionIs to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_connection_is("value")
        """
        self.connection_is = value  # Use property setter (gets validation)
        return self

from typing import List

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class BinaryManifestResourceDefinition(Identifiable):
    """
    This meta-class represents the ability to specify a resource definition that
    provides information that can be shared by all resources that refer to the
    respective resource definition.

    Package: M2::AUTOSARTemplates::SystemTemplate::SoftwareCluster::BinaryManifest

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 917, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This aggregation specifies the collection of handle definitions in the
        # context of the enclosing binary manifest.
        self._itemDefinition: List["BinaryManifestItem"] = []

    @property
    def item_definition(self) -> List["BinaryManifestItem"]:
        """Get itemDefinition (Pythonic accessor)."""
        return self._itemDefinition

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getItemDefinition(self) -> List["BinaryManifestItem"]:
        """
        AUTOSAR-compliant getter for itemDefinition.

        Returns:
            The itemDefinition value

        Note:
            Delegates to item_definition property (CODING_RULE_V2_00017)
        """
        return self.item_definition  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

from typing import (
    List,
    Optional,
)

from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.BinaryManifest import (
    BinaryManifestAddressableObject,
)


class BinaryManifestItem(BinaryManifestAddressableObject):
    """
    This meta-class represents the ability to describe a specific handle or
    auxiliary field in the context of binary manifest resource.

    Package: M2::AUTOSARTemplates::SystemTemplate::SoftwareCluster::BinaryManifest

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 919, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This aggregation is used to define structured Binary.
        self._auxiliaryField: List["BinaryManifestItem"] = []

    @property
    def auxiliary_field(self) -> List["BinaryManifestItem"]:
        """Get auxiliaryField (Pythonic accessor)."""
        return self._auxiliaryField
        # This aggregation represents the definition of a default for a binary manifest
                # handle or an auxiliaryField.
        # shall be taken if no connection for this possible.
        self._defaultValue: Optional["BinaryManifestItem"] = None

    @property
    def default_value(self) -> Optional["BinaryManifestItem"]:
        """Get defaultValue (Pythonic accessor)."""
        return self._defaultValue

    @default_value.setter
    def default_value(self, value: Optional["BinaryManifestItem"]) -> None:
        """
        Set defaultValue with validation.

        Args:
            value: The defaultValue to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._defaultValue = None
            return

        if not isinstance(value, BinaryManifestItem):
            raise TypeError(
                f"defaultValue must be BinaryManifestItem or None, got {type(value).__name__}"
            )
        self._defaultValue = value
        # If true, the handle or auxiliary field in the context of binary relates to an
        # optional BinaryManifest is not used.
        self._isUnused: Optional["Boolean"] = None

    @property
    def is_unused(self) -> Optional["Boolean"]:
        """Get isUnused (Pythonic accessor)."""
        return self._isUnused

    @is_unused.setter
    def is_unused(self, value: Optional["Boolean"]) -> None:
        """
        Set isUnused with validation.

        Args:
            value: The isUnused to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._isUnused = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"isUnused must be Boolean or None, got {type(value).__name__}"
            )
        self._isUnused = value
        # This aggregation represents the definition of a value for a manifest handle
                # or an auxiliaryField.
        # shall be taken to establish a connection.
        self._value: Optional["BinaryManifestItem"] = None

    @property
    def value(self) -> Optional["BinaryManifestItem"]:
        """Get value (Pythonic accessor)."""
        return self._value

    @value.setter
    def value(self, value: Optional["BinaryManifestItem"]) -> None:
        """
        Set value with validation.

        Args:
            value: The value to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._value = None
            return

        if not isinstance(value, BinaryManifestItem):
            raise TypeError(
                f"value must be BinaryManifestItem or None, got {type(value).__name__}"
            )
        self._value = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAuxiliaryField(self) -> List["BinaryManifestItem"]:
        """
        AUTOSAR-compliant getter for auxiliaryField.

        Returns:
            The auxiliaryField value

        Note:
            Delegates to auxiliary_field property (CODING_RULE_V2_00017)
        """
        return self.auxiliary_field  # Delegates to property

    def getDefaultValue(self) -> "BinaryManifestItem":
        """
        AUTOSAR-compliant getter for defaultValue.

        Returns:
            The defaultValue value

        Note:
            Delegates to default_value property (CODING_RULE_V2_00017)
        """
        return self.default_value  # Delegates to property

    def setDefaultValue(self, value: "BinaryManifestItem") -> "BinaryManifestItem":
        """
        AUTOSAR-compliant setter for defaultValue with method chaining.

        Args:
            value: The defaultValue to set

        Returns:
            self for method chaining

        Note:
            Delegates to default_value property setter (gets validation automatically)
        """
        self.default_value = value  # Delegates to property setter
        return self

    def getIsUnused(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for isUnused.

        Returns:
            The isUnused value

        Note:
            Delegates to is_unused property (CODING_RULE_V2_00017)
        """
        return self.is_unused  # Delegates to property

    def setIsUnused(self, value: "Boolean") -> "BinaryManifestItem":
        """
        AUTOSAR-compliant setter for isUnused with method chaining.

        Args:
            value: The isUnused to set

        Returns:
            self for method chaining

        Note:
            Delegates to is_unused property setter (gets validation automatically)
        """
        self.is_unused = value  # Delegates to property setter
        return self

    def getValue(self) -> "BinaryManifestItem":
        """
        AUTOSAR-compliant getter for value.

        Returns:
            The value value

        Note:
            Delegates to value property (CODING_RULE_V2_00017)
        """
        return self.value  # Delegates to property

    def setValue(self, value: "BinaryManifestItem") -> "BinaryManifestItem":
        """
        AUTOSAR-compliant setter for value with method chaining.

        Args:
            value: The value to set

        Returns:
            self for method chaining

        Note:
            Delegates to value property setter (gets validation automatically)
        """
        self.value = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_default_value(self, value: Optional["BinaryManifestItem"]) -> "BinaryManifestItem":
        """
        Set defaultValue and return self for chaining.

        Args:
            value: The defaultValue to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_default_value("value")
        """
        self.default_value = value  # Use property setter (gets validation)
        return self

    def with_is_unused(self, value: Optional["Boolean"]) -> "BinaryManifestItem":
        """
        Set isUnused and return self for chaining.

        Args:
            value: The isUnused to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_is_unused("value")
        """
        self.is_unused = value  # Use property setter (gets validation)
        return self

    def with_value(self, value: Optional["BinaryManifestItem"]) -> "BinaryManifestItem":
        """
        Set value and return self for chaining.

        Args:
            value: The value to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_value("value")
        """
        self.value = value  # Use property setter (gets validation)
        return self

from typing import (
    List,
    Optional,
)

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class BinaryManifestItemDefinition(Identifiable):
    """
    This meta-class provides the ability to define the handle definition or an
    auxiliary field of a binary manifest resource.

    Package: M2::AUTOSARTemplates::SystemTemplate::SoftwareCluster::BinaryManifest

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 920, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This aggregation is used to define structured Binary ManifestItemDefinitions.
        self._auxiliaryField: List["BinaryManifestItem"] = []

    @property
    def auxiliary_field(self) -> List["BinaryManifestItem"]:
        """Get auxiliaryField (Pythonic accessor)."""
        return self._auxiliaryField
        # If true, the handle definition or auxiliary field of a binary is optional and
        # may not be used in all to this BinaryManifest.
        self._isOptional: Optional["Boolean"] = None

    @property
    def is_optional(self) -> Optional["Boolean"]:
        """Get isOptional (Pythonic accessor)."""
        return self._isOptional

    @is_optional.setter
    def is_optional(self, value: Optional["Boolean"]) -> None:
        """
        Set isOptional with validation.

        Args:
            value: The isOptional to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._isOptional = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"isOptional must be Boolean or None, got {type(value).__name__}"
            )
        self._isOptional = value
        # This attribute provides the ability to specify the size of the.
        self._size: Optional["PositiveInteger"] = None

    @property
    def size(self) -> Optional["PositiveInteger"]:
        """Get size (Pythonic accessor)."""
        return self._size

    @size.setter
    def size(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set size with validation.

        Args:
            value: The size to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._size = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"size must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._size = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAuxiliaryField(self) -> List["BinaryManifestItem"]:
        """
        AUTOSAR-compliant getter for auxiliaryField.

        Returns:
            The auxiliaryField value

        Note:
            Delegates to auxiliary_field property (CODING_RULE_V2_00017)
        """
        return self.auxiliary_field  # Delegates to property

    def getIsOptional(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for isOptional.

        Returns:
            The isOptional value

        Note:
            Delegates to is_optional property (CODING_RULE_V2_00017)
        """
        return self.is_optional  # Delegates to property

    def setIsOptional(self, value: "Boolean") -> "BinaryManifestItemDefinition":
        """
        AUTOSAR-compliant setter for isOptional with method chaining.

        Args:
            value: The isOptional to set

        Returns:
            self for method chaining

        Note:
            Delegates to is_optional property setter (gets validation automatically)
        """
        self.is_optional = value  # Delegates to property setter
        return self

    def getSize(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for size.

        Returns:
            The size value

        Note:
            Delegates to size property (CODING_RULE_V2_00017)
        """
        return self.size  # Delegates to property

    def setSize(self, value: "PositiveInteger") -> "BinaryManifestItemDefinition":
        """
        AUTOSAR-compliant setter for size with method chaining.

        Args:
            value: The size to set

        Returns:
            self for method chaining

        Note:
            Delegates to size property setter (gets validation automatically)
        """
        self.size = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_is_optional(self, value: Optional["Boolean"]) -> "BinaryManifestItemDefinition":
        """
        Set isOptional and return self for chaining.

        Args:
            value: The isOptional to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_is_optional("value")
        """
        self.is_optional = value  # Use property setter (gets validation)
        return self

    def with_size(self, value: Optional["PositiveInteger"]) -> "BinaryManifestItemDefinition":
        """
        Set size and return self for chaining.

        Args:
            value: The size to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_size("value")
        """
        self.size = value  # Use property setter (gets validation)
        return self

from abc import ABC
from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class BinaryManifestAddressableObject(Identifiable, ABC):
    """
    This meta-class acts as an abstract base class for addressable objects in
    the context of the binary manifest of a CP software cluster.

    Package: M2::AUTOSARTemplates::SystemTemplate::SoftwareCluster::BinaryManifest

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 920, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is BinaryManifestAddressableObject:
            raise TypeError("BinaryManifestAddressableObject is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute specifies the address of the enclosing.
        self._address: Optional["Address"] = None

    @property
    def address(self) -> Optional["Address"]:
        """Get address (Pythonic accessor)."""
        return self._address

    @address.setter
    def address(self, value: Optional["Address"]) -> None:
        """
        Set address with validation.

        Args:
            value: The address to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._address = None
            return

        if not isinstance(value, Address):
            raise TypeError(
                f"address must be Address or None, got {type(value).__name__}"
            )
        self._address = value
        # This attribute specifies the symbol of the addressable.
        self._symbol: Optional["SymbolString"] = None

    @property
    def symbol(self) -> Optional["SymbolString"]:
        """Get symbol (Pythonic accessor)."""
        return self._symbol

    @symbol.setter
    def symbol(self, value: Optional["SymbolString"]) -> None:
        """
        Set symbol with validation.

        Args:
            value: The symbol to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._symbol = None
            return

        if not isinstance(value, SymbolString):
            raise TypeError(
                f"symbol must be SymbolString or None, got {type(value).__name__}"
            )
        self._symbol = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAddress(self) -> "Address":
        """
        AUTOSAR-compliant getter for address.

        Returns:
            The address value

        Note:
            Delegates to address property (CODING_RULE_V2_00017)
        """
        return self.address  # Delegates to property

    def setAddress(self, value: "Address") -> "BinaryManifestAddressableObject":
        """
        AUTOSAR-compliant setter for address with method chaining.

        Args:
            value: The address to set

        Returns:
            self for method chaining

        Note:
            Delegates to address property setter (gets validation automatically)
        """
        self.address = value  # Delegates to property setter
        return self

    def getSymbol(self) -> "SymbolString":
        """
        AUTOSAR-compliant getter for symbol.

        Returns:
            The symbol value

        Note:
            Delegates to symbol property (CODING_RULE_V2_00017)
        """
        return self.symbol  # Delegates to property

    def setSymbol(self, value: "SymbolString") -> "BinaryManifestAddressableObject":
        """
        AUTOSAR-compliant setter for symbol with method chaining.

        Args:
            value: The symbol to set

        Returns:
            self for method chaining

        Note:
            Delegates to symbol property setter (gets validation automatically)
        """
        self.symbol = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_address(self, value: Optional["Address"]) -> "BinaryManifestAddressableObject":
        """
        Set address and return self for chaining.

        Args:
            value: The address to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_address("value")
        """
        self.address = value  # Use property setter (gets validation)
        return self

    def with_symbol(self, value: Optional["SymbolString"]) -> "BinaryManifestAddressableObject":
        """
        Set symbol and return self for chaining.

        Args:
            value: The symbol to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_symbol("value")
        """
        self.symbol = value  # Use property setter (gets validation)
        return self

from abc import ABC

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class BinaryManifestItemValue(ARObject, ABC):
    """
    This meta-class has the ability to act as an abstract base class for values
    of binary manifest item.

    Package: M2::AUTOSARTemplates::SystemTemplate::SoftwareCluster::BinaryManifest

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 922, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is BinaryManifestItemValue:
            raise TypeError("BinaryManifestItemValue is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.BinaryManifest import (
    BinaryManifestItemValue,
)


class BinaryManifestItemNumericalValue(BinaryManifestItemValue):
    """
    This meta-class has the ability to provide a numerical value for a binary
    manifest item.

    Package: M2::AUTOSARTemplates::SystemTemplate::SoftwareCluster::BinaryManifest

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 922, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute specifies the actual numerical value to be the binary manifest
        # handle.
        self._value: Optional["Numerical"] = None

    @property
    def value(self) -> Optional["Numerical"]:
        """Get value (Pythonic accessor)."""
        return self._value

    @value.setter
    def value(self, value: Optional["Numerical"]) -> None:
        """
        Set value with validation.

        Args:
            value: The value to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._value = None
            return

        if not isinstance(value, Numerical):
            raise TypeError(
                f"value must be Numerical or None, got {type(value).__name__}"
            )
        self._value = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getValue(self) -> "Numerical":
        """
        AUTOSAR-compliant getter for value.

        Returns:
            The value value

        Note:
            Delegates to value property (CODING_RULE_V2_00017)
        """
        return self.value  # Delegates to property

    def setValue(self, value: "Numerical") -> "BinaryManifestItemNumericalValue":
        """
        AUTOSAR-compliant setter for value with method chaining.

        Args:
            value: The value to set

        Returns:
            self for method chaining

        Note:
            Delegates to value property setter (gets validation automatically)
        """
        self.value = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_value(self, value: Optional["Numerical"]) -> "BinaryManifestItemNumericalValue":
        """
        Set value and return self for chaining.

        Args:
            value: The value to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_value("value")
        """
        self.value = value  # Use property setter (gets validation)
        return self

from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.BinaryManifest import (
    BinaryManifestItemValue,
)


class BinaryManifestItemPointerValue(BinaryManifestItemValue):
    """
    This meta-class has the ability to provide a value for a pointer in the
    context of a binary manifest item.

    Package: M2::AUTOSARTemplates::SystemTemplate::SoftwareCluster::BinaryManifest

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 922, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute represents the address value of the value.
        self._address: Optional["Address"] = None

    @property
    def address(self) -> Optional["Address"]:
        """Get address (Pythonic accessor)."""
        return self._address

    @address.setter
    def address(self, value: Optional["Address"]) -> None:
        """
        Set address with validation.

        Args:
            value: The address to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._address = None
            return

        if not isinstance(value, Address):
            raise TypeError(
                f"address must be Address or None, got {type(value).__name__}"
            )
        self._address = value
        # This attribute represents the symbol associated with the handle.
        self._symbol: Optional["SymbolString"] = None

    @property
    def symbol(self) -> Optional["SymbolString"]:
        """Get symbol (Pythonic accessor)."""
        return self._symbol

    @symbol.setter
    def symbol(self, value: Optional["SymbolString"]) -> None:
        """
        Set symbol with validation.

        Args:
            value: The symbol to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._symbol = None
            return

        if not isinstance(value, SymbolString):
            raise TypeError(
                f"symbol must be SymbolString or None, got {type(value).__name__}"
            )
        self._symbol = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAddress(self) -> "Address":
        """
        AUTOSAR-compliant getter for address.

        Returns:
            The address value

        Note:
            Delegates to address property (CODING_RULE_V2_00017)
        """
        return self.address  # Delegates to property

    def setAddress(self, value: "Address") -> "BinaryManifestItemPointerValue":
        """
        AUTOSAR-compliant setter for address with method chaining.

        Args:
            value: The address to set

        Returns:
            self for method chaining

        Note:
            Delegates to address property setter (gets validation automatically)
        """
        self.address = value  # Delegates to property setter
        return self

    def getSymbol(self) -> "SymbolString":
        """
        AUTOSAR-compliant getter for symbol.

        Returns:
            The symbol value

        Note:
            Delegates to symbol property (CODING_RULE_V2_00017)
        """
        return self.symbol  # Delegates to property

    def setSymbol(self, value: "SymbolString") -> "BinaryManifestItemPointerValue":
        """
        AUTOSAR-compliant setter for symbol with method chaining.

        Args:
            value: The symbol to set

        Returns:
            self for method chaining

        Note:
            Delegates to symbol property setter (gets validation automatically)
        """
        self.symbol = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_address(self, value: Optional["Address"]) -> "BinaryManifestItemPointerValue":
        """
        Set address and return self for chaining.

        Args:
            value: The address to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_address("value")
        """
        self.address = value  # Use property setter (gets validation)
        return self

    def with_symbol(self, value: Optional["SymbolString"]) -> "BinaryManifestItemPointerValue":
        """
        Set symbol and return self for chaining.

        Args:
            value: The symbol to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_symbol("value")
        """
        self.symbol = value  # Use property setter (gets validation)
        return self

from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.BinaryManifest import (
    BinaryManifestAddressableObject,
)


class BinaryManifestMetaDataField(BinaryManifestAddressableObject):
    """
    This meta-class provides the ability to define a meta-data field for the
    binary manifest descriptor.

    Package: M2::AUTOSARTemplates::SystemTemplate::SoftwareCluster::BinaryManifest

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 923, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The value of this attribute represents the size of the in bytes.
        self._size: Optional["PositiveInteger"] = None

    @property
    def size(self) -> Optional["PositiveInteger"]:
        """Get size (Pythonic accessor)."""
        return self._size

    @size.setter
    def size(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set size with validation.

        Args:
            value: The size to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._size = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"size must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._size = value
        # This attribute specifies the value of the meta-data field.
        self._value: Optional["VerbatimString"] = None

    @property
    def value(self) -> Optional["VerbatimString"]:
        """Get value (Pythonic accessor)."""
        return self._value

    @value.setter
    def value(self, value: Optional["VerbatimString"]) -> None:
        """
        Set value with validation.

        Args:
            value: The value to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._value = None
            return

        if not isinstance(value, VerbatimString):
            raise TypeError(
                f"value must be VerbatimString or None, got {type(value).__name__}"
            )
        self._value = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getSize(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for size.

        Returns:
            The size value

        Note:
            Delegates to size property (CODING_RULE_V2_00017)
        """
        return self.size  # Delegates to property

    def setSize(self, value: "PositiveInteger") -> "BinaryManifestMetaDataField":
        """
        AUTOSAR-compliant setter for size with method chaining.

        Args:
            value: The size to set

        Returns:
            self for method chaining

        Note:
            Delegates to size property setter (gets validation automatically)
        """
        self.size = value  # Delegates to property setter
        return self

    def getValue(self) -> "VerbatimString":
        """
        AUTOSAR-compliant getter for value.

        Returns:
            The value value

        Note:
            Delegates to value property (CODING_RULE_V2_00017)
        """
        return self.value  # Delegates to property

    def setValue(self, value: "VerbatimString") -> "BinaryManifestMetaDataField":
        """
        AUTOSAR-compliant setter for value with method chaining.

        Args:
            value: The value to set

        Returns:
            self for method chaining

        Note:
            Delegates to value property setter (gets validation automatically)
        """
        self.value = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_size(self, value: Optional["PositiveInteger"]) -> "BinaryManifestMetaDataField":
        """
        Set size and return self for chaining.

        Args:
            value: The size to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_size("value")
        """
        self.size = value  # Use property setter (gets validation)
        return self

    def with_value(self, value: Optional["VerbatimString"]) -> "BinaryManifestMetaDataField":
        """
        Set value and return self for chaining.

        Args:
            value: The value to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_value("value")
        """
        self.value = value  # Use property setter (gets validation)
        return self
