from typing import List

from .....models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import NameToken, RefType
from .....models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from .....models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import ARElement


class DiagnosticServiceTable(ARElement):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.diagnosticConnectionRefs = []                              # type: List[RefType]
        self.diagnosticServiceInstanceRefs = []                         # type: List[RefType]
        self.ecuInstanceRef = None                                      # type: RefType
        self.protocolKind = None                                        # type: NameToken

    def getDiagnosticConnectionRefs(self):
        return self.diagnosticConnectionRefs

    def addDiagnosticConnectionRef(self, value):
        if value is not None:
            self.diagnosticConnectionRefs.append(value)
        return self

    def getDiagnosticServiceInstanceRefs(self):
        return self.diagnosticServiceInstanceRefs

    def addDiagnosticServiceInstanceRef(self, value):
        if value is not None:
            self.diagnosticServiceInstanceRefs.append(value)
        return self

    def getEcuInstanceRef(self):
        return self.ecuInstanceRef

    def setEcuInstanceRef(self, value):
        if value is not None:
            self.ecuInstanceRef = value
        return self

    def getProtocolKind(self):
        return self.protocolKind

    def setProtocolKind(self, value):
        if value is not None:
            self.protocolKind = value
        return self
