from typing import List, Union

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ARPositiveInteger,
    Integer,
    RefType,
)
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (
    FibexElement,
)
from armodel.v2.models.M2.MSR.Documentation.TextModel.BlockElements import (
    DocumentationBlock,
)


class FrameMapping(ARObject):

    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass

    def __init__(self) -> None:
        super().__init__()

        self.introduction: Union[Union[DocumentationBlock, None] , None] = None
        self.sourceFrameRef: Union[Union[RefType, None] , None] = None
        self.targetFrameRef: Union[Union[RefType, None] , None] = None

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

    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass

    def __init__(self) -> None:
        super().__init__()

        self.introduction: Union[Union[DocumentationBlock, None] , None] = None
        self.sourceSignalRef: Union[Union[RefType, None] , None] = None
        self.targetSignalRef: Union[Union[RefType, None] , None] = None

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

    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass

    def __init__(self) -> None:
        super().__init__()

        self.elementByteValue: Union[Union[Integer, None] , None] = None
        self.elementPosition: Union[Union[Integer, None] , None] = None

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

    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass

    def __init__(self) -> None:
        super().__init__()

        self.defaultValueElements: List[DefaultValueElement] = []

    def getDefaultValueElements(self):
        return self.defaultValueElements

    def addDefaultValueElements(self, value):
        if value is not None:
            self.defaultValueElements = value
        return self

class TargetIPduRef(ARObject):

    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass

    def __init__(self) -> None:
        super().__init__()

        self.defaultValue: Union[Union[PduMappingDefaultValue, None] , None] = None
        self.targetIPdu: Union[Union[RefType, None] , None] = None

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

    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass

    def __init__(self) -> None:
        super().__init__()

        self.introduction: Union[Union[DocumentationBlock, None] , None] = None
        self.pdurTpChunkSize: Union[Union[ARPositiveInteger, None] , None] = None
        self.sourceIpduRef: Union[Union[RefType, None] , None] = None
        self.targetIPdu: Union[Union[TargetIPduRef, None] , None] = None

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
    def __init__(self, parent: ARObject, short_name: str) -> None:
        super().__init__(parent, short_name)

        self.ecuRef: Union[Union[RefType, None] , None] = None
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
