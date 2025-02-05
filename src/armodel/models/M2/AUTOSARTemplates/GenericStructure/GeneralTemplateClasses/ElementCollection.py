from typing import List

from .....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Identifier, NameToken, RefType
from .....M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AnyInstanceRef
from .....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import ARElement


class Collection(ARElement):
    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        self.autoCollect = None                                 # type: AutoCollectEnum
        self.collectedInstances = []                            # type: List[AnyInstanceRef]
        self.collectionSemantics = None                         # type: NameToken
        self.elementRefs = []                                   # type: List[RefType]
        self.elementRole = None                                 # type: Identifier
        self.sourceElementRefs = []                             # type: List[RefType]
        self.sourceInstances = []                               # type: List[AnyInstanceRef]

    def getAutoCollect(self):
        return self.autoCollect

    def setAutoCollect(self, value):
        if value is not None:
            self.autoCollect = value
        return self

    def getCollectedInstances(self):
        return self.collectedInstances

    def setCollectedInstances(self, value):
        if value is not None:
            self.collectedInstances = value
        return self

    def getCollectionSemantics(self):
        return self.collectionSemantics

    def setCollectionSemantics(self, value):
        if value is not None:
            self.collectionSemantics = value
        return self

    def getElementRefs(self):
        return self.elementRefs

    def addElementRef(self, value):
        if value is not None:
            self.elementRefs.append(value)
        return self

    def getElementRole(self):
        return self.elementRole

    def setElementRole(self, value):
        if value is not None:
            self.elementRole = value
        return self

    def getSourceElementRefs(self):
        return self.sourceElementRefs

    def addSourceElementRef(self, value):
        if value is not None:
            self.sourceElementRefs.append(value)
        return self

    def getSourceInstances(self):
        return self.sourceInstances

    def setSourceInstances(self, value):
        if value is not None:
            self.sourceInstances = value
        return self
