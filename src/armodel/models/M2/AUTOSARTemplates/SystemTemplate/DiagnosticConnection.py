from typing import List
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import ARElement

class DiagnosticConnection(ARElement):
    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        self.functionalRequestRefs = []                         # type: List[RefType]
        self.periodicResponseUudtRefs = []                      # type: List[RefType]
        self.physicalRequestRef = None                          # type: RefType
        self.responseRef = None                                 # type: RefType
        self.responseOnEventRef = None                          # type: RefType

    def getFunctionalRequestRefs(self):
        return self.functionalRequestRefs

    def addFunctionalRequestRef(self, value):
        if value is not None:
            self.functionalRequestRefs.append(value)
        return self

    def getPeriodicResponseUudtRefs(self):
        return self.periodicResponseUudtRefs

    def addPeriodicResponseUudtRef(self, value):
        if value is not None:
            self.periodicResponseUudtRefs.append(value)
        return self

    def getPhysicalRequestRef(self):
        return self.physicalRequestRef

    def setPhysicalRequestRef(self, value):
        if value is not None:
            self.physicalRequestRef = value
        return self

    def getResponseRef(self):
        return self.responseRef

    def setResponseRef(self, value):
        if value is not None:
            self.responseRef = value
        return self

    def getResponseOnEventRef(self):
        return self.responseOnEventRef

    def setResponseOnEventRef(self, value):
        if value is not None:
            self.responseOnEventRef = value
        return self


    


