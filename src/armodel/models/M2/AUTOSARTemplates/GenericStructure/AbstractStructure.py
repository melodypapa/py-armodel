
from abc import ABCMeta
from typing import List
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import ARElement, Identifiable
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject


class AtpInstanceRef(ARObject, metaclass=ABCMeta):
    def __init__(self):

        if type(self) == AtpInstanceRef:
            raise NotImplementedError("AtpInstanceRef is an abstract class.")

        super().__init__()

        self.atpBaseRef = None                  # type: RefType
        self.atpContextElementRefs = []         # type: List[RefType]
        self.atpTargetRef = None                # type: RefType

    def getAtpBaseRef(self):
        return self.atpBaseRef

    def setAtpBaseRef(self, value):
        self.atpBaseRef = value
        return self

    def getAtpContextElementRefs(self):
        return self.atpContextElementRefs

    def addAtpContextElementRef(self, value):
        self.atpContextElementRefs.append(value)
        return self

    def getAtpTargetRef(self):
        return self.atpTargetRef

    def setAtpTargetRef(self, value):
        self.atpTargetRef = value
        return self


class AnyInstanceRef(ARObject):
    def __init__(self):
        super().__init__()

        self.baseRef = None                             # type: RefType
        self.contextElementRefs = []                    # type: List[RefType]
        self.targetRef = None                           # type: RefType

    def getBaseRef(self) -> RefType:
        return self.baseRef

    def setBaseRef(self, value: RefType):
        self.baseRef = value
        return self

    def getContextElementRefs(self) -> List[RefType]:
        return self.contextElementRefs

    def addContextElementRef(self, value: RefType):
        self.contextElementRefs.append(value)
        return self

    def getTargetRef(self) -> RefType:
        return self.targetRef

    def setTargetRef(self, value: RefType):
        self.targetRef = value
        return self


class AtpFeature(Identifiable, metaclass=ABCMeta):
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is AtpFeature:
            raise TypeError("AtpFeature is an abstract class.")
        super().__init__(parent, short_name)


class AtpStructureElement(AtpFeature, metaclass=ABCMeta):
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is AtpFeature:
            raise TypeError("AtpStructureElement is an abstract class.")
        super().__init__(parent, short_name)


class AtpType(ARElement, metaclass=ABCMeta):
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is AtpType:
            raise TypeError("AtpType is an abstract class.")

        super().__init__(parent, short_name)
