from typing import List
from ....M2.MSR.DataDictionary.DataDefProperties import SwDataDefProps
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Identifier
from ....M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AnyInstanceRef
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import ARElement, Identifiable

class FlatInstanceDescriptor(Identifiable):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)
        
        self.ecuExtractReferenceIRef = None                     # type: AnyInstanceRef
        self.role = None                                        # type: Identifier
        self.rtePluginProps = None                              # type: RtePluginProps
        self.swDataDefProps = None                              # type: SwDataDefProps
        self.upstreamReferenceIRef = None                       # type: AnyInstanceRef

    def getEcuExtractReferenceIRef(self):
        return self.ecuExtractReferenceIRef

    def setEcuExtractReferenceIRef(self, value):
        self.ecuExtractReferenceIRef = value
        return self

    def getRole(self):
        return self.role

    def setRole(self, value):
        self.role = value
        return self

    def getRtePluginProps(self):
        return self.rtePluginProps

    def setRtePluginProps(self, value):
        self.rtePluginProps = value
        return self

    def getSwDataDefProps(self):
        return self.swDataDefProps

    def setSwDataDefProps(self, value):
        self.swDataDefProps = value
        return self

    def getUpstreamReferenceIRef(self):
        return self.upstreamReferenceIRef

    def setUpstreamReferenceIRef(self, value):
        self.upstreamReferenceIRef = value
        return self


class FlatMap(ARElement):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.instances = []                                 # type: List[FlatInstanceDescriptor]

    def getInstances(self):
        return list(sorted(filter(lambda a: isinstance(a, FlatInstanceDescriptor), self.elements.values()), key= lambda o:o.short_name))

    def createFlatInstanceDescriptor(self, short_name: str):
        if (short_name not in self.elements):
            element = FlatInstanceDescriptor(self, short_name)
            self.addElement(element)
            self.instances.append(element)
        return self.getElement(short_name)


