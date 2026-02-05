# This module contains AUTOSAR System Template classes for diagnostic connections
# It defines connections for diagnostic services and communication between diagnostic entities

from typing import List

from armodel.models_v2.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    ARElement,
)
from armodel.models_v2.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class DiagnosticConnection(ARElement):
    """
    Represents a diagnostic connection in the AUTOSAR system, defining the relationship
    between diagnostic services and their communication endpoints. This class connects
    functional requests, physical requests, and responses within the diagnostic communication
    infrastructure of the system.
    """
    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        self.functionalRequestRefs: List[RefType] = []
        self.periodicResponseUudtRefs: List[RefType] = []
        self.physicalRequestRef: RefType = None
        self.responseRef: RefType = None
        self.responseOnEventRef: RefType = None

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
