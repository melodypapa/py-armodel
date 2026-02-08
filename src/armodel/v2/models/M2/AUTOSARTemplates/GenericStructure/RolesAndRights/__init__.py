"""
V2 M2::AUTOSARTemplates::GenericStructure::RolesAndRights package.
"""
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.AclObjectSet import AclObjectSet
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.AclOperation import AclOperation
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.AclPermission import AclPermission
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.AclRole import AclRole
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.AtpDefinition import AtpDefinition

__all__ = [
    "AclObjectSet",
    "AclOperation",
    "AclPermission",
    "AclRole",
    "AclScopeEnum",
    "AtpDefinition",
]
