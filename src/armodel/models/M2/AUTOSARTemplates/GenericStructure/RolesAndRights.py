"""
RolesAndRights module for AUTOSAR M2 models.

Spec package: AUTOSAR Templates::GenericStructure::RolesAndRights. The ARElement
classes below are declared on the import-safe Identifiable base; ARPackage rebinds
their __bases__ to ARElement after its own definition (late-bind pattern, see
BuildActionManifest / Collection).
"""

from __future__ import annotations
from abc import ABC
from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.EngineeringObject import AutosarEngineeringObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable, Referrable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AclScopeEnum,
    NameToken,
    RefType,
    ReferrableSubtypesEnum,
    UriString,
)

__all__ = ["AclObjectSet", "AclOperation", "AclPermission", "AclRole", "AtpDefinition"]


class AtpDefinition(Referrable, ABC):
    """This abstract meta class represents "definition"-elements which identify the respective values. For example the value of a particular system constant is identified by the definition of this system constant."""

    # AtpDefinition method parity checklist:
    # Spec: R23-11/AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 11.3, p.383 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent, short_name: str):
        if type(self) is AtpDefinition:
            raise TypeError("AtpDefinition is an abstract class.")
        super().__init__(parent, short_name)


class AclObjectSet(Identifiable):
    """
    M2::AUTOSARTemplates::GenericStructure::RolesAndRights This meta class represents the ability to denote a set of objects for which roles and rights (access control lists) shall be defined. It basically can define the objects based on • the nature of objects • the involved blueprints • the artifact in which the objects are serialized • the definition of the object (in a definition - value pattern) • individual reference objects
    """

    # AclObjectSet method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 11.2, p.383
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addAclObjectClass            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getAclObjectClasses          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getAclScope                  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setAclScope                  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getCollectionRef             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setCollectionRef             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] addDerivedFromBlueprintRef   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDerivedFromBlueprintRefs  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addEngineeringObject         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getEngineeringObjects        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addObjectRef                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getObjectRefs                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addObjectDefinitionRef       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getObjectDefinitionRefs      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This specifies that the considered objects as instances of the denoted meta class.
        self.aclObjectClasses: List[ReferrableSubtypesEnum] = []

        # this indicates the scope of the referenced objects.
        self.aclScope: Optional[AclScopeEnum] = None

        # This indicates that the relevant objects are specified via a collection.
        self.collectionRef: Optional[RefType] = None

        # This association indicates that the considered objects are the ones being derived from the associated blueprint. Stereotypes: atpUriDef
        self.derivedFromBlueprintRefs: List[RefType] = []

        # This indicates an engineering object. The AclPermission relates to all objects in this partial model. This also implies that the other objects in this set shall be placed in the specified engineering object. Note that semantic constraints apply with respect to <<atpSplitable>>
        self.engineeringObjects: List[AutosarEngineeringObject] = []

        # This association applies a particular (usually small) set of objects (e.g. a singular package). Main usage is, if one does not want to create a collection specifically for access control.
        self.objectRefs: List[RefType] = []

        # This denotes an object by its definition. For example the right to manipulate the value of a particular ecuc parameter is denoted by reference to the definition of the parameter. Note that this can also be a reference to a Standard Module Definition. Therefore it is stereotyped by atpUri Def. Stereotypes: atpUriDef
        self.objectDefinitionRefs: List[RefType] = []

    def addAclObjectClass(self, value: Optional[ReferrableSubtypesEnum]) -> AclObjectSet:
        """
        This specifies that the considered objects as instances of the denoted meta class.
        A None value is a no-op and does not append anything.
        """
        if value is not None:
            self.aclObjectClasses.append(value)
        return self

    def getAclObjectClasses(self) -> List[ReferrableSubtypesEnum]:
        """
        This specifies that the considered objects as instances of the denoted meta class.
        """
        return self.aclObjectClasses

    def getAclScope(self) -> Optional[AclScopeEnum]:
        """
        this indicates the scope of the referenced objects.
        """
        return self.aclScope

    def setAclScope(self, value: Optional[AclScopeEnum]) -> AclObjectSet:
        """
        this indicates the scope of the referenced objects.
        A None value is a no-op and does not overwrite an existing aclScope.
        """
        if value is not None:
            self.aclScope = value
        return self

    def getCollectionRef(self) -> Optional[RefType]:
        """
        This indicates that the relevant objects are specified via a collection.
        """
        return self.collectionRef

    def setCollectionRef(self, value: Optional[RefType]) -> AclObjectSet:
        """
        This indicates that the relevant objects are specified via a collection.
        A None value is a no-op and does not overwrite an existing collectionRef.
        """
        if value is not None:
            self.collectionRef = value
        return self

    def addDerivedFromBlueprintRef(self, value: Optional[RefType]) -> AclObjectSet:
        """
        This association indicates that the considered objects are the ones being derived from the associated blueprint. Stereotypes: atpUriDef
        A None value is a no-op and does not append anything.
        """
        if value is not None:
            self.derivedFromBlueprintRefs.append(value)
        return self

    def getDerivedFromBlueprintRefs(self) -> List[RefType]:
        """
        This association indicates that the considered objects are the ones being derived from the associated blueprint. Stereotypes: atpUriDef
        """
        return self.derivedFromBlueprintRefs

    def addEngineeringObject(self, value: Optional[AutosarEngineeringObject]) -> AclObjectSet:
        """
        This indicates an engineering object. The AclPermission relates to all objects in this partial model. This also implies that the other objects in this set shall be placed in the specified engineering object. Note that semantic constraints apply with respect to <<atpSplitable>>
        A None value is a no-op and does not append anything.
        """
        if value is not None:
            self.engineeringObjects.append(value)
        return self

    def getEngineeringObjects(self) -> List[AutosarEngineeringObject]:
        """
        This indicates an engineering object. The AclPermission relates to all objects in this partial model. This also implies that the other objects in this set shall be placed in the specified engineering object. Note that semantic constraints apply with respect to <<atpSplitable>>
        """
        return self.engineeringObjects

    def addObjectRef(self, value: Optional[RefType]) -> AclObjectSet:
        """
        This association applies a particular (usually small) set of objects (e.g. a singular package). Main usage is, if one does not want to create a collection specifically for access control.
        A None value is a no-op and does not append anything.
        """
        if value is not None:
            self.objectRefs.append(value)
        return self

    def getObjectRefs(self) -> List[RefType]:
        """
        This association applies a particular (usually small) set of objects (e.g. a singular package). Main usage is, if one does not want to create a collection specifically for access control.
        """
        return self.objectRefs

    def addObjectDefinitionRef(self, value: Optional[RefType]) -> AclObjectSet:
        """
        This denotes an object by its definition. For example the right to manipulate the value of a particular ecuc parameter is denoted by reference to the definition of the parameter. Note that this can also be a reference to a Standard Module Definition. Therefore it is stereotyped by atpUri Def. Stereotypes: atpUriDef
        A None value is a no-op and does not append anything.
        """
        if value is not None:
            self.objectDefinitionRefs.append(value)
        return self

    def getObjectDefinitionRefs(self) -> List[RefType]:
        """
        This denotes an object by its definition. For example the right to manipulate the value of a particular ecuc parameter is denoted by reference to the definition of the parameter. Note that this can also be a reference to a Standard Module Definition. Therefore it is stereotyped by atpUri Def. Stereotypes: atpUriDef
        """
        return self.objectDefinitionRefs


class AclOperation(Identifiable):
    """
    This meta class represents the ability to denote a particular operation which may be performed on objects in an AUTOSAR model. Tags: atp.recommendedPackage=AclOperations
    """

    # AclOperation method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 11.4, p.384
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addImpliedOperationRef    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getImpliedOperationRefs   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This indicates that the related operations are also implied. Therefore the permission is also granted for this operation.
        self.impliedOperationRefs: List[RefType] = []

    def addImpliedOperationRef(self, value: Optional[RefType]) -> AclOperation:
        """
        This indicates that the related operations are also implied. Therefore the permission is also granted for this operation.
        A None value is a no-op and does not append anything.
        """
        if value is not None:
            self.impliedOperationRefs.append(value)
        return self

    def getImpliedOperationRefs(self) -> List[RefType]:
        """
        This indicates that the related operations are also implied. Therefore the permission is also granted for this operation.
        """
        return self.impliedOperationRefs


class AclPermission(Identifiable):
    """
    This meta class represents the ability to represent permissions granted on objects in an AUTOSAR model. Tags: atp.recommendedPackage=AclPermissions
    """

    # AclPermission method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 11.1, p.382
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__             [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addAclContext        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getAclContexts       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addAclObjectRef      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getAclObjectRefs     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addAclOperationRef   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getAclOperationRefs  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addAclRoleRef        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getAclRoleRefs       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getAclScope          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setAclScope          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This attribute is intended to specify the context under which the AclPemission is applicable. The values are subject to mutual agreement between the involved stakeholders. For examples the values can be the names of binding times.
        self.aclContexts: List[NameToken] = []

        # This denotes an object to which the AclPermission applies.
        self.aclObjectRefs: List[RefType] = []

        # This denotes an operation which is granted by the given AclPermission.
        self.aclOperationRefs: List[RefType] = []

        # This denotes the role (individual or even organization) for which the AclPermission. is granted.
        self.aclRoleRefs: List[RefType] = []

        # This indicates the scope of applied permissions: explicit, descendant, dependent;
        self.aclScope: Optional[AclScopeEnum] = None

    def addAclContext(self, value: Optional[NameToken]) -> AclPermission:
        """
        This attribute is intended to specify the context under which the AclPemission is applicable. The values are subject to mutual agreement between the involved stakeholders. For examples the values can be the names of binding times.
        A None value is a no-op and does not append anything.
        """
        if value is not None:
            self.aclContexts.append(value)
        return self

    def getAclContexts(self) -> List[NameToken]:
        """
        This attribute is intended to specify the context under which the AclPemission is applicable. The values are subject to mutual agreement between the involved stakeholders. For examples the values can be the names of binding times.
        """
        return self.aclContexts

    def addAclObjectRef(self, value: Optional[RefType]) -> AclPermission:
        """
        This denotes an object to which the AclPermission applies.
        A None value is a no-op and does not append anything.
        """
        if value is not None:
            self.aclObjectRefs.append(value)
        return self

    def getAclObjectRefs(self) -> List[RefType]:
        """
        This denotes an object to which the AclPermission applies.
        """
        return self.aclObjectRefs

    def addAclOperationRef(self, value: Optional[RefType]) -> AclPermission:
        """
        This denotes an operation which is granted by the given AclPermission.
        A None value is a no-op and does not append anything.
        """
        if value is not None:
            self.aclOperationRefs.append(value)
        return self

    def getAclOperationRefs(self) -> List[RefType]:
        """
        This denotes an operation which is granted by the given AclPermission.
        """
        return self.aclOperationRefs

    def addAclRoleRef(self, value: Optional[RefType]) -> AclPermission:
        """
        This denotes the role (individual or even organization) for which the AclPermission. is granted.
        A None value is a no-op and does not append anything.
        """
        if value is not None:
            self.aclRoleRefs.append(value)
        return self

    def getAclRoleRefs(self) -> List[RefType]:
        """
        This denotes the role (individual or even organization) for which the AclPermission. is granted.
        """
        return self.aclRoleRefs

    def getAclScope(self) -> Optional[AclScopeEnum]:
        """
        This indicates the scope of applied permissions: explicit, descendant, dependent;
        """
        return self.aclScope

    def setAclScope(self, value: Optional[AclScopeEnum]) -> AclPermission:
        """
        This indicates the scope of applied permissions: explicit, descendant, dependent;
        A None value is a no-op and does not overwrite an existing aclScope.
        """
        if value is not None:
            self.aclScope = value
        return self


class AclRole(Identifiable):
    """
    This meta class represents the ability to specify a particular role which is used to grant access rights to AUTOSAR model. The purpose of this meta-class is to support the mutual agreements between the involved parties. Tags: atp.recommendedPackage=AclRoles
    """

    # AclRole method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 11.5, p.384
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getLdapUrl  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setLdapUrl  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This is an URL which allows to represent users or organizations taking the particular role.
        self.ldapUrl: Optional[UriString] = None

    def getLdapUrl(self) -> Optional[UriString]:
        """
        This is an URL which allows to represent users or organizations taking the particular role.
        """
        return self.ldapUrl

    def setLdapUrl(self, value: Optional[UriString]) -> AclRole:
        """
        This is an URL which allows to represent users or organizations taking the particular role.
        A None value is a no-op and does not overwrite an existing ldapUrl.
        """
        if value is not None:
            self.ldapUrl = value
        return self
