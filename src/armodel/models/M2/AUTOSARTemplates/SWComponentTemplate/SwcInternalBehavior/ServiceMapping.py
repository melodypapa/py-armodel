from ....AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from ....AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType

class RoleBasedPortAssignment(ARObject):
    def __init__(self):
        super().__init__()

        self.portPrototypeRef = None            # type: RefType
        self.role = None                        # type: Identifier

    def getPortPrototypeRef(self):
        return self.portPrototypeRef

    def setPortPrototypeRef(self, value):
        self.portPrototypeRef = value
        return self

    def getRole(self):
        return self.role

    def setRole(self, value):
        self.role = value
        return self
