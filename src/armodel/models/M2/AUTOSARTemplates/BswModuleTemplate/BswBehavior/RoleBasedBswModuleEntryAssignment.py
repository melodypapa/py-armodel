"""
This module defines role-based BSW module entry assignment in AUTOSAR.
"""

from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral, RefType


class RoleBasedBswModuleEntryAssignment(ARObject):
    """
    Represents a role-based BSW module entry assignment in AUTOSAR.
    This class defines how BSW module entries are assigned based on their role.
    """

    def __init__(self):
        """
        Initializes the RoleBasedBswModuleEntryAssignment with default values.
        """
        super().__init__()
        self.role: ARLiteral = None
        self.usedModuleEntryRef: RefType = None

    def getRole(self):
        return self.role

    def setRole(self, value):
        self.role = value
        return self

    def getUsedModuleEntryRef(self):
        return self.usedModuleEntryRef

    def setUsedModuleEntryRef(self, value):
        self.usedModuleEntryRef = value
        return self