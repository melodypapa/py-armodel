from typing import List

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
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
        self._aclContext: List["NameToken"] = []

    @property
    def acl_context(self) -> List["NameToken"]:
        """Get aclContext (Pythonic accessor)."""
        return self._aclContext
        # This denotes an object to which the AclPermission.
        self._aclObject: List[RefType] = []

    @property
    def acl_object(self) -> List[RefType]:
        """Get aclObject (Pythonic accessor)."""
        return self._aclObject
        # This denotes an operation which is granted by the given.
        self._aclOperation: List["AclOperation"] = []

    @property
    def acl_operation(self) -> List["AclOperation"]:
        """Get aclOperation (Pythonic accessor)."""
        return self._aclOperation
        # This denotes the role (individual or even organization) for AclPermission.
        # is granted.
        self._aclRole: List["AclRole"] = []

    @property
    def acl_role(self) -> List["AclRole"]:
        """Get aclRole (Pythonic accessor)."""
        return self._aclRole
        # This indicates the scope of applied permissions: explicit,.
        self._aclScope: "AclScopeEnum" = None

    @property
    def acl_scope(self) -> "AclScopeEnum":
        """Get aclScope (Pythonic accessor)."""
        return self._aclScope

    @acl_scope.setter
    def acl_scope(self, value: "AclScopeEnum") -> None:
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

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAclContext(self) -> List["NameToken"]:
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

    def getAclOperation(self) -> List["AclOperation"]:
        """
        AUTOSAR-compliant getter for aclOperation.

        Returns:
            The aclOperation value

        Note:
            Delegates to acl_operation property (CODING_RULE_V2_00017)
        """
        return self.acl_operation  # Delegates to property

    def getAclRole(self) -> List["AclRole"]:
        """
        AUTOSAR-compliant getter for aclRole.

        Returns:
            The aclRole value

        Note:
            Delegates to acl_role property (CODING_RULE_V2_00017)
        """
        return self.acl_role  # Delegates to property

    def getAclScope(self) -> "AclScopeEnum":
        """
        AUTOSAR-compliant getter for aclScope.

        Returns:
            The aclScope value

        Note:
            Delegates to acl_scope property (CODING_RULE_V2_00017)
        """
        return self.acl_scope  # Delegates to property

    def setAclScope(self, value: "AclScopeEnum") -> "AclPermission":
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

    def with_acl_scope(self, value: "AclScopeEnum") -> "AclPermission":
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
