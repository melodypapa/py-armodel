from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

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
        # This indicates that the relevant objects are specified via a.
        self._collection: RefType = None

    @property
    def collection(self) -> RefType:
        """Get collection (Pythonic accessor)."""
        return self._collection

    @collection.setter
    def collection(self, value: RefType) -> None:
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
        # This association indicates that the considered objects are ones being derived
        # from the associated blueprint.
        self._derivedFrom: List["AtpBlueprint"] = []

    @property
    def derived_from(self) -> List["AtpBlueprint"]:
        """Get derivedFrom (Pythonic accessor)."""
        return self._derivedFrom
        # This indicates an engineering object.
        # The AclPermission relates to all objects in this partial model.
        # implies that the other objects in this set shall be the specified engineering
                # object.
        self._engineering: List["AutosarEngineering"] = []

    @property
    def engineering(self) -> List["AutosarEngineering"]:
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

    def getAclScope(self) -> "AclScopeEnum":
        """
        AUTOSAR-compliant getter for aclScope.
        
        Returns:
            The aclScope value
        
        Note:
            Delegates to acl_scope property (CODING_RULE_V2_00017)
        """
        return self.acl_scope  # Delegates to property

    def setAclScope(self, value: "AclScopeEnum") -> "AclObjectSet":
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

    def setCollection(self, value: RefType) -> "AclObjectSet":
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

    def getDerivedFrom(self) -> List["AtpBlueprint"]:
        """
        AUTOSAR-compliant getter for derivedFrom.
        
        Returns:
            The derivedFrom value
        
        Note:
            Delegates to derived_from property (CODING_RULE_V2_00017)
        """
        return self.derived_from  # Delegates to property

    def getEngineering(self) -> List["AutosarEngineering"]:
        """
        AUTOSAR-compliant getter for engineering.
        
        Returns:
            The engineering value
        
        Note:
            Delegates to engineering property (CODING_RULE_V2_00017)
        """
        return self.engineering  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_acl_scope(self, value: "AclScopeEnum") -> "AclObjectSet":
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

    def with_collection(self, value: Optional[RefType]) -> "AclObjectSet":
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