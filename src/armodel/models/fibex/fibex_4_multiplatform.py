from typing import List

from ..m2.msr.documentation.block_elements import DocumentationBlock
from ..ar_ref import RefType
from ..ar_object import ARObject, ARPositiveInteger
from .fibex_core.core_communication import FibexElement

class FrameMapping(ARObject):
    def __init__(self):
        super().__init__()

        self.introduction = None            # type: DocumentationBlock
        self.sourceFrameRef = None          # type: RefType
        self.targetFrameRef = None          # type: RefType

    def getIntroduction(self):
        return self.introduction

    def setIntroduction(self, value):
        self.introduction = value
        return self

    def getSourceFrameRef(self):
        return self.sourceFrameRef

    def setSourceFrameRef(self, value):
        self.sourceFrameRef = value
        return self

    def getTargetFrameRef(self):
        return self.targetFrameRef

    def setTargetFrameRef(self, value):
        self.targetFrameRef = value
        return self

class ISignalMapping(ARObject):
    def __init__(self):
        super().__init__()

        self.introduction = None         # type: DocumentationBlock
        self.sourceSignalRef = None      # type: RefType
        self.targetSignalRef = None      # type: RefType

    def getIntroduction(self):
        return self.introduction

    def setIntroduction(self, value):
        self.introduction = value
        return self

    def getSourceSignalRef(self):
        return self.sourceSignalRef

    def setSourceSignalRef(self, value):
        self.sourceSignalRef = value
        return self

    def getTargetSignalRef(self):
        return self.targetSignalRef

    def setTargetSignalRef(self, value):
        self.targetSignalRef = value
        return self

class IPduMapping(ARObject):
    def __init__(self):
        super().__init__()

        self.introduction = None            # type: DocumentationBlock
        self.pdurTpChunkSize = None         # type: ARPositiveInteger
        self.sourceIpduRef = None           # type: RefType
        self.targetIpduRef = None           # type: RefType

    def getIntroduction(self):
        return self.introduction

    def setIntroduction(self, value):
        self.introduction = value
        return self

    def getPdurTpChunkSize(self):
        return self.pdurTpChunkSize

    def setPdurTpChunkSize(self, value):
        self.pdurTpChunkSize = value
        return self

    def getSourceIpduRef(self):
        return self.sourceIpduRef

    def setSourceIpduRef(self, value):
        self.sourceIpduRef = value
        return self

    def getTargetIpduRef(self):
        return self.targetIpduRef

    def setTargetIpduRef(self, value):
        self.targetIpduRef = value
        return self

class Gateway(FibexElement):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.ecuRef = None                # type: RefType
        self.frameMappings = []           # type: List[FrameMapping]
        self.iPduMappings = []            # type: List[IPduMapping]
        self.signalMappings = []          # type: List[ISignalMapping]
    
    def getEcuRef(self):
        return self.ecuRef

    def setEcuRef(self, value):
        self.ecuRef = value
        return self

    def getFrameMappings(self) -> List[FrameMapping]:
        return self.frameMappings

    def addFrameMapping(self, mapping: FrameMapping):
        self.frameMappings.append(mapping)
        return self

    def getIPduMappings(self) -> List[FrameMapping]:
        return self.iPduMappings

    def addIPduMappings(self, mapping: FrameMapping):
        self.iPduMappings.append(mapping)
        return self

    def getSignalMappings(self) -> List[FrameMapping]:
        return self.signalMappings

    def addSignalMapping(self, mapping: FrameMapping):
        self.signalMappings.append(mapping)
        return self
