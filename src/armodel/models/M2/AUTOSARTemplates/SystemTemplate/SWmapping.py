# This module contains AUTOSAR System Template classes for software component mapping
# It defines mappings between software components and their implementations or partitions

from typing import List
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from ....M2.AUTOSARTemplates.SystemTemplate.InstanceRefs import ComponentInSystemInstanceRef


class SwcToImplMapping(Identifiable):
    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        self.componentIRefs: List[ComponentInSystemInstanceRef] = []
        self.componentImplementationRef: RefType = None

    def getComponentIRefs(self):
        return self.componentIRefs

    def addComponentIRef(self, value):
        if value is not None:
            self.componentIRefs.append(value)
        return self

    def getComponentImplementationRef(self):
        return self.componentImplementationRef

    def setComponentImplementationRef(self, value):
        if value is not None:
            self.componentImplementationRef = value
        return self


class ApplicationPartitionToEcuPartitionMapping(Identifiable):
    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        self.applicationPartitionRefs: List[RefType] = []
        self.ecuPartitionRef: RefType = None

    def getApplicationPartitionRefs(self):
        return self.applicationPartitionRefs

    def addApplicationPartitionRef(self, value):
        if value is not None:
            self.applicationPartitionRefs.append(value)
        return self

    def getEcuPartitionRef(self):
        return self.ecuPartitionRef

    def setEcuPartitionRef(self, value):
        if value is not None:
            self.ecuPartitionRef = value
        return self