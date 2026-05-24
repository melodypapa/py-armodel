from typing import List

from armodel.models.M2.MSR.Documentation.TextModel.BlockElements import DocumentationBlock
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Integer, RefType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARPositiveInteger
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import FibexElement

class FrameMapping(ARObject):
    """
    A PduToFrameMapping defines the composition of Pdus in each frame.
    """

    def __init__(self):
        super().__init__()

        self.introduction: DocumentationBlock = None
        self.sourceFrameRef: RefType = None
        self.targetFrameRef: RefType = None

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
    """
    Arranges signals transferred by the gateway from one channel to another
    in pairs and defines the mapping between them.
    """

    def __init__(self):
        super().__init__()

        self.introduction: DocumentationBlock = None
        self.sourceSignalRef: RefType = None
        self.targetSignalRef: RefType = None

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
    
class DefaultValueElement(ARObject):
    """
    The default value consists of a number of elements. Each element is one
    byte long and the number of elements is specified by SduLength.
    """

    def __init__(self):
        super().__init__()

        self.elementByteValue: Integer = None
        self.elementPosition: Integer = None

    def getElementByteValue(self):
        return self.elementByteValue

    def setElementByteValue(self, value):
        if value is not None:
            self.elementByteValue = value
        return self

    def getElementPosition(self):
        return self.elementPosition

    def setElementPosition(self, value):
        if value is not None:
            self.elementPosition = value
        return self
    
class PduMappingDefaultValue(ARObject):
    """
    Default value which will be distributed if no I-Pdu has been received
    since last sending.
    """

    def __init__(self):
        super().__init__()

        self.defaultValueElements: List[DefaultValueElement] = []

    def getDefaultValueElements(self):
        return self.defaultValueElements

    def addDefaultValueElements(self, value):
        if value is not None:
            self.defaultValueElements = value
        return self

class TargetIPduRef(ARObject):
    """
    Target destination of the referencing mapping.
    """

    def __init__(self):
        super().__init__()

        self.defaultValue: PduMappingDefaultValue = None
        self.targetIPdu: RefType = None

    def getDefaultValue(self):
        return self.defaultValue

    def setDefaultValue(self, value):
        if value is not None:
            self.defaultValue = value
        return self

    def getTargetIPdu(self):
        return self.targetIPdu

    def setTargetIPdu(self, value):
        if value is not None:
            self.targetIPdu = value
        return self

class IPduMapping(ARObject):
    """
    An ISignalToIPduMapping describes the mapping of ISignals to ISignalIPdus
    and defines the position of the ISignal within an ISignalIPdu.
    """

    def __init__(self):
        super().__init__()

        self.introduction: DocumentationBlock = None
        self.pdurTpChunkSize: ARPositiveInteger = None
        self.sourceIpduRef: RefType = None
        self.targetIPdu: TargetIPduRef = None

    def getIntroduction(self):
        return self.introduction

    def setIntroduction(self, value):
        if value is not None:
            self.introduction = value
        return self

    def getPdurTpChunkSize(self):
        return self.pdurTpChunkSize

    def setPdurTpChunkSize(self, value):
        if value is not None:
            self.pdurTpChunkSize = value
        return self

    def getSourceIpduRef(self):
        return self.sourceIpduRef

    def setSourceIpduRef(self, value):
        if value is not None:
            self.sourceIpduRef = value
        return self

    def getTargetIPdu(self):
        return self.targetIPdu

    def setTargetIPdu(self, value):
        if value is not None:
            self.targetIPdu = value
        return self


    
class Gateway(FibexElement):
    """
    A gateway is an ECU that is connected to two or more clusters and
    performs frame, Pdu, or signal mapping between them.
    """
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.ecuRef: RefType = None
        self.frameMappings: List[FrameMapping] = []
        self.iPduMappings: List[IPduMapping] = []
        self.signalMappings: List[ISignalMapping] = []
    
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

    def addIPduMapping(self, mapping: FrameMapping):
        self.iPduMappings.append(mapping)
        return self

    def getSignalMappings(self) -> List[FrameMapping]:
        return self.signalMappings

    def addSignalMapping(self, mapping: FrameMapping):
        self.signalMappings.append(mapping)
        return self
