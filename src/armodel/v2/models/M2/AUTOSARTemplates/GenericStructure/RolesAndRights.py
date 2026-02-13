"""
AUTOSAR Package - RolesAndRights

Package: M2::AUTOSARTemplates::GenericStructure::RolesAndRights
"""


from __future__ import annotations
from abc import ABC
from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.AbstractBlueprintStructure import (
    AtpBlueprint,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.EngineeringObject import (
    AutosarEngineeringObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
    RefType,
    UriString,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    ARElement,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Referrable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
)


class AclPermission(ARElement):
    """
    This meta class represents the ability to represent permissions granted on
    objects in an AUTOSAR model.

    Package: M2::AUTOSARTemplates::GenericStructure::RolesAndRights::AclPermission

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 382, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 159, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute is intended to specify the context under AclPemission is
                # applicable.
        # The values are mutual agreement between the involved the values can be the
                # names of binding.
        self._aclContext: List[NameToken] = []

    @property
    def acl_context(self) -> List[NameToken]:
        """Get aclContext (Pythonic accessor)."""
        return self._aclContext
        # This denotes an object to which the AclPermission.
        self._aclObject: List[RefType] = []

    @property
    def acl_object(self) -> List[RefType]:
        """Get aclObject (Pythonic accessor)."""
        return self._aclObject
        # This denotes an operation which is granted by the given.
        self._aclOperation: List[AclOperation] = []

    @property
    def acl_operation(self) -> List[AclOperation]:
        """Get aclOperation (Pythonic accessor)."""
        return self._aclOperation
        # This denotes the role (individual or even organization) for AclPermission.
        # is granted.
        self._aclRole: List[AclRole] = []

    @property
    def acl_role(self) -> List[AclRole]:
        """Get aclRole (Pythonic accessor)."""
        return self._aclRole
        # This indicates the scope of applied permissions: explicit,.
        self._aclScope: AclScopeEnum = None

    @property
    def acl_scope(self) -> AclScopeEnum:
        """Get aclScope (Pythonic accessor)."""
        return self._aclScope

    @acl_scope.setter
    def acl_scope(self, value: AclScopeEnum) -> None:
        """
        Set aclScope with validation.

        Args:
            value: The aclScope to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, AclScopeEnum):
            raise TypeError(
                f"aclScope must be AclScopeEnum, got {type(value).__name__}"
            )
        self._aclScope = value

    def with_acl_context(self, value):
        """
        Set acl_context and return self for chaining.

        Args:
            value: The acl_context to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_acl_context("value")
        """
        self.acl_context = value  # Use property setter (gets validation)
        return self

    def with_acl_object(self, value):
        """
        Set acl_object and return self for chaining.

        Args:
            value: The acl_object to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_acl_object("value")
        """
        self.acl_object = value  # Use property setter (gets validation)
        return self

    def with_acl_operation(self, value):
        """
        Set acl_operation and return self for chaining.

        Args:
            value: The acl_operation to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_acl_operation("value")
        """
        self.acl_operation = value  # Use property setter (gets validation)
        return self

    def with_acl_role(self, value):
        """
        Set acl_role and return self for chaining.

        Args:
            value: The acl_role to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_acl_role("value")
        """
        self.acl_role = value  # Use property setter (gets validation)
        return self

    def with_acl_object_class(self, value):
        """
        Set acl_object_class and return self for chaining.

        Args:
            value: The acl_object_class to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_acl_object_class("value")
        """
        self.acl_object_class = value  # Use property setter (gets validation)
        return self

    def with_derived_from(self, value):
        """
        Set derived_from and return self for chaining.

        Args:
            value: The derived_from to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_derived_from("value")
        """
        self.derived_from = value  # Use property setter (gets validation)
        return self

    def with_engineering(self, value):
        """
        Set engineering and return self for chaining.

        Args:
            value: The engineering to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_engineering("value")
        """
        self.engineering = value  # Use property setter (gets validation)
        return self

    def with_implied(self, value):
        """
        Set implied and return self for chaining.

        Args:
            value: The implied to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_implied("value")
        """
        self.implied = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAclContext(self) -> List[NameToken]:
        """
        AUTOSAR-compliant getter for aclContext.

        Returns:
            The aclContext value

        Note:
            Delegates to acl_context property (CODING_RULE_V2_00017)
        """
        return self.acl_context  # Delegates to property

    def getAclObject(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for aclObject.

        Returns:
            The aclObject value

        Note:
            Delegates to acl_object property (CODING_RULE_V2_00017)
        """
        return self.acl_object  # Delegates to property

    def getAclOperation(self) -> List[AclOperation]:
        """
        AUTOSAR-compliant getter for aclOperation.

        Returns:
            The aclOperation value

        Note:
            Delegates to acl_operation property (CODING_RULE_V2_00017)
        """
        return self.acl_operation  # Delegates to property

    def getAclRole(self) -> List[AclRole]:
        """
        AUTOSAR-compliant getter for aclRole.

        Returns:
            The aclRole value

        Note:
            Delegates to acl_role property (CODING_RULE_V2_00017)
        """
        return self.acl_role  # Delegates to property

    def getAclScope(self) -> AclScopeEnum:
        """
        AUTOSAR-compliant getter for aclScope.

        Returns:
            The aclScope value

        Note:
            Delegates to acl_scope property (CODING_RULE_V2_00017)
        """
        return self.acl_scope  # Delegates to property

    def setAclScope(self, value: AclScopeEnum) -> AclPermission:
        """
        AUTOSAR-compliant setter for aclScope with method chaining.

        Args:
            value: The aclScope to set

        Returns:
            self for method chaining

        Note:
            Delegates to acl_scope property setter (gets validation automatically)
        """
        self.acl_scope = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_acl_scope(self, value: AclScopeEnum) -> AclPermission:
        """
        Set aclScope and return self for chaining.

        Args:
            value: The aclScope to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_acl_scope("value")
        """
        self.acl_scope = value  # Use property setter (gets validation)
        return self



class AclObjectSet(ARElement):
    """
    that this can also be a reference to a Standard Module Definition. Therefore
    it is stereotyped by atpUri Def. Stereotypes: atpUriDef Table 11.2:
    AclObjectSet

    Package: M2::AUTOSARTemplates::GenericStructure::RolesAndRights::AclObjectSet

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 383, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 158, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This specifies that the considered objects as instances of denoted meta
        # class.
        self._aclObjectClass: List[RefType] = []

    @property
    def acl_object_class(self) -> List[RefType]:
        """Get aclObjectClass (Pythonic accessor)."""
        return self._aclObjectClass
        # this indicates the scope of the referenced objects.
        self._aclScope: AclScopeEnum = None

    @property
    def acl_scope(self) -> AclScopeEnum:
        """Get aclScope (Pythonic accessor)."""
        return self._aclScope

    @acl_scope.setter
    def acl_scope(self, value: AclScopeEnum) -> None:
        """
        Set aclScope with validation.

        Args:
            value: The aclScope to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, AclScopeEnum):
            raise TypeError(
                f"aclScope must be AclScopeEnum, got {type(value).__name__}"
            )
        self._aclScope = value
        self._collection: Optional[RefType] = None

    @property
    def collection(self) -> Optional[RefType]:
        """Get collection (Pythonic accessor)."""
        return self._collection

    @collection.setter
    def collection(self, value: Optional[RefType]) -> None:
        """
        Set collection with validation.

        Args:
            value: The collection to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._collection = None
            return

        self._collection = value
        # from the associated blueprint.
        self._derivedFrom: List[AtpBlueprint] = []

    @property
    def derived_from(self) -> List[AtpBlueprint]:
        """Get derivedFrom (Pythonic accessor)."""
        return self._derivedFrom
        # This indicates an engineering object.
        # The AclPermission relates to all objects in this partial model.
        # implies that the other objects in this set shall be the specified engineering
                # object.
        self._engineering: List[AutosarEngineeringObject] = []

    @property
    def engineering(self) -> List[AutosarEngineeringObject]:
        """Get engineering (Pythonic accessor)."""
        return self._engineering

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAclObjectClass(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for aclObjectClass.

        Returns:
            The aclObjectClass value

        Note:
            Delegates to acl_object_class property (CODING_RULE_V2_00017)
        """
        return self.acl_object_class  # Delegates to property

    def getAclScope(self) -> AclScopeEnum:
        """
        AUTOSAR-compliant getter for aclScope.

        Returns:
            The aclScope value

        Note:
            Delegates to acl_scope property (CODING_RULE_V2_00017)
        """
        return self.acl_scope  # Delegates to property

    def setAclScope(self, value: AclScopeEnum) -> AclObjectSet:
        """
        AUTOSAR-compliant setter for aclScope with method chaining.

        Args:
            value: The aclScope to set

        Returns:
            self for method chaining

        Note:
            Delegates to acl_scope property setter (gets validation automatically)
        """
        self.acl_scope = value  # Delegates to property setter
        return self

    def getCollection(self) -> RefType:
        """
        AUTOSAR-compliant getter for collection.

        Returns:
            The collection value

        Note:
            Delegates to collection property (CODING_RULE_V2_00017)
        """
        return self.collection  # Delegates to property

    def setCollection(self, value: RefType) -> AclObjectSet:
        """
        AUTOSAR-compliant setter for collection with method chaining.

        Args:
            value: The collection to set

        Returns:
            self for method chaining

        Note:
            Delegates to collection property setter (gets validation automatically)
        """
        self.collection = value  # Delegates to property setter
        return self

    def getDerivedFrom(self) -> List[AtpBlueprint]:
        """
        AUTOSAR-compliant getter for derivedFrom.

        Returns:
            The derivedFrom value

        Note:
            Delegates to derived_from property (CODING_RULE_V2_00017)
        """
        return self.derived_from  # Delegates to property

    def getEngineering(self) -> List[AutosarEngineeringObject]:
        """
        AUTOSAR-compliant getter for engineering.

        Returns:
            The engineering value

        Note:
            Delegates to engineering property (CODING_RULE_V2_00017)
        """
        return self.engineering  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_acl_scope(self, value: AclScopeEnum) -> AclObjectSet:
        """
        Set aclScope and return self for chaining.

        Args:
            value: The aclScope to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_acl_scope("value")
        """
        self.acl_scope = value  # Use property setter (gets validation)
        return self

    def with_collection(self, value: Optional[RefType]) -> AclObjectSet:
        """
        Set collection and return self for chaining.

        Args:
            value: The collection to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_collection("value")
        """
        self.collection = value  # Use property setter (gets validation)
        return self



class AtpDefinition(Referrable, ABC):
    """
    This abstract meta class represents "definition"-elements which identify the
    respective values. For example the value of a particular system constant is
    identified by the definition of this system constant.

    Package: M2::AUTOSARTemplates::GenericStructure::RolesAndRights::AtpDefinition

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 383, Foundation
      R23-11)
    """
    def __init__(self):
        if type(self) is AtpDefinition:
            raise TypeError("AtpDefinition is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class AclOperation(ARElement):
    """
    This meta class represents the ability to denote a particular operation
    which may be performed on objects in an AUTOSAR model.

    Package: M2::AUTOSARTemplates::GenericStructure::RolesAndRights::AclOperation

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 384, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 159, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This indicates that the related operations are also implied.
        # the permission is also granted for this.
        self._implied: List[AclOperation] = []

    @property
    def implied(self) -> List[AclOperation]:
        """Get implied (Pythonic accessor)."""
        return self._implied

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getImplied(self) -> List[AclOperation]:
        """
        AUTOSAR-compliant getter for implied.

        Returns:
            The implied value

        Note:
            Delegates to implied property (CODING_RULE_V2_00017)
        """
        return self.implied  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class AclRole(ARElement):
    """
    This meta class represents the ability to specify a particular role which is
    used to grant access rights to AUTOSAR model. The purpose of this meta-class
    is to support the mutual agreements between the involved parties.

    Package: M2::AUTOSARTemplates::GenericStructure::RolesAndRights::AclRole

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 384, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 159, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This is an URL which allows to represent users or the particular role.
        self._ldapUrl: Optional[UriString] = None

    @property
    def ldap_url(self) -> Optional[UriString]:
        """Get ldapUrl (Pythonic accessor)."""
        return self._ldapUrl

    @ldap_url.setter
    def ldap_url(self, value: Optional[UriString]) -> None:
        """
        Set ldapUrl with validation.

        Args:
            value: The ldapUrl to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ldapUrl = None
            return

        if not isinstance(value, UriString):
            raise TypeError(
                f"ldapUrl must be UriString or None, got {type(value).__name__}"
            )
        self._ldapUrl = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getLdapUrl(self) -> UriString:
        """
        AUTOSAR-compliant getter for ldapUrl.

        Returns:
            The ldapUrl value

        Note:
            Delegates to ldap_url property (CODING_RULE_V2_00017)
        """
        return self.ldap_url  # Delegates to property

    def setLdapUrl(self, value: "UriString") -> AclRole:
        """
        AUTOSAR-compliant setter for ldapUrl with method chaining.

        Args:
            value: The ldapUrl to set

        Returns:
            self for method chaining

        Note:
            Delegates to ldap_url property setter (gets validation automatically)
        """
        self.ldap_url = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_ldap_url(self, value: Optional[UriString]) -> AclRole:
        """
        Set ldapUrl and return self for chaining.

        Args:
            value: The ldapUrl to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ldap_url("value")
        """
        self.ldap_url = value  # Use property setter (gets validation)
        return self


class AclScopeEnum(AREnum):
    """
    AclScopeEnum enumeration

This enumerator represents the scope of a definition in context of access control. Aggregated by AclObjectSet.aclScope, AclPermission.aclScope

Package: M2::AUTOSARTemplates::GenericStructure::RolesAndRights
    """
    # This specifies that the AclPermission applies to dependant (in particular referenced) operations / objects as well. Note that this includes the descendant ones.
    dependant = "0"

    # This specifies that the AclPermission applies to descendant operations / objects as well.
    descendant = "1"

    # This is indicates that the AclPermission applies to explicit objects / operations only.
    explicit = "2"
