
from abc import ABCMeta
from typing import List

from ....ar_ref import RefType
from ....ar_object import ARObject


class AtpInstanceRef(ARObject, metaclass = ABCMeta):
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
        self.contextElementRef = None                   # type: RefType
        self.targetRef = None                           # type: RefType

    def getBaseRef(self) -> RefType:
        return self.baseRef

    def setBaseRef(self, value: RefType):
        self.baseRef = value
        return self

    def getContextElementRef(self) -> RefType:
        return self.contextElementRef

    def setContextElementRef(self, value: RefType):
        self.contextElementRef = value
        return self

    def getTargetRef(self) -> RefType:
        return self.targetRef

    def setTargetRef(self, value:RefType):
        self.targetRef = value
        return self
