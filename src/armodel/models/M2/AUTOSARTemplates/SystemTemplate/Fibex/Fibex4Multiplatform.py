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
    # FrameMapping method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getIntroduction              [x] impl  [ ] docstring  [ ] test
    # [ ] setIntroduction              [x] impl  [ ] docstring  [ ] test
    # [ ] getSourceFrameRef            [x] impl  [ ] docstring  [ ] test
    # [ ] setSourceFrameRef            [x] impl  [ ] docstring  [ ] test
    # [ ] getTargetFrameRef            [x] impl  [ ] docstring  [ ] test
    # [ ] setTargetFrameRef            [x] impl  [ ] docstring  [ ] test


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
    # ISignalMapping method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getIntroduction              [x] impl  [ ] docstring  [ ] test
    # [ ] setIntroduction              [x] impl  [ ] docstring  [ ] test
    # [ ] getSourceSignalRef           [x] impl  [ ] docstring  [ ] test
    # [ ] setSourceSignalRef           [x] impl  [ ] docstring  [ ] test
    # [ ] getTargetSignalRef           [x] impl  [ ] docstring  [ ] test
    # [ ] setTargetSignalRef           [x] impl  [ ] docstring  [ ] test


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
    # DefaultValueElement method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getElementByteValue          [x] impl  [ ] docstring  [ ] test
    # [ ] setElementByteValue          [x] impl  [ ] docstring  [ ] test
    # [ ] getElementPosition           [x] impl  [ ] docstring  [ ] test
    # [ ] setElementPosition           [x] impl  [ ] docstring  [ ] test


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
    # PduMappingDefaultValue method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getDefaultValueElements      [x] impl  [ ] docstring  [ ] test
    # [ ] addDefaultValueElements      [x] impl  [ ] docstring  [ ] test


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
    # TargetIPduRef method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getDefaultValue              [x] impl  [ ] docstring  [ ] test
    # [ ] setDefaultValue              [x] impl  [ ] docstring  [ ] test
    # [ ] getTargetIPdu                [x] impl  [ ] docstring  [ ] test
    # [ ] setTargetIPdu                [x] impl  [ ] docstring  [ ] test


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
    # IPduMapping method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getIntroduction              [x] impl  [ ] docstring  [ ] test
    # [ ] setIntroduction              [x] impl  [ ] docstring  [ ] test
    # [ ] getPdurTpChunkSize           [x] impl  [ ] docstring  [ ] test
    # [ ] setPdurTpChunkSize           [x] impl  [ ] docstring  [ ] test
    # [ ] getSourceIpduRef             [x] impl  [ ] docstring  [ ] test
    # [ ] setSourceIpduRef             [x] impl  [ ] docstring  [ ] test
    # [ ] getTargetIPdu                [x] impl  [ ] docstring  [ ] test
    # [ ] setTargetIPdu                [x] impl  [ ] docstring  [ ] test


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
    # Gateway method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getEcuRef                    [x] impl  [ ] docstring  [ ] test
    # [ ] setEcuRef                    [x] impl  [ ] docstring  [ ] test
    # [ ] getFrameMappings             [x] impl  [ ] docstring  [ ] test
    # [ ] addFrameMapping              [x] impl  [ ] docstring  [ ] test
    # [ ] getIPduMappings              [x] impl  [ ] docstring  [ ] test
    # [ ] addIPduMapping               [x] impl  [ ] docstring  [ ] test
    # [ ] getSignalMappings            [x] impl  [ ] docstring  [ ] test
    # [ ] addSignalMapping             [x] impl  [ ] docstring  [ ] test

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
