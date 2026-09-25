from typing import List, Optional
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.StereotypeMixins import VariationPointCapable

from armodel.models.M2.MSR.Documentation.TextModel.BlockElements import DocumentationBlock
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Integer, RefType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore import FibexElement


class FrameMapping(ARObject, VariationPointCapable):
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


class ISignalMapping(ARObject, VariationPointCapable):
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
    """Default Value which will be distributed if no I-Pdu has been received since last sending."""

    # PduMappingDefaultValue method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 8.5, p.841
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getDefaultValueElements     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addDefaultValueElement      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # The default value consists of a number of elements. Each default value element is represented by the element and the position in an array.
        self.defaultValueElements: List[DefaultValueElement] = []

    def getDefaultValueElements(self) -> List[DefaultValueElement]:
        """
        The default value consists of a number of elements. Each default value element is represented by the element and the position in an array.
        """
        return self.defaultValueElements

    def addDefaultValueElement(self, value: Optional[DefaultValueElement]) -> "PduMappingDefaultValue":
        """
        The default value consists of a number of elements. Each default value element is represented by the element and the position in an array.
        A None value is a no-op and does not extend the defaultValueElements list.
        """
        if value is not None:
            self.defaultValueElements.append(value)
        return self


class TargetIPduRef(ARObject):
    """
    Target destination of the referencing mapping.
    """

    # TargetIPduRef method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getDefaultValue              [x] impl  [ ] docstring  [ ] test
    # [ ] setDefaultValue              [x] impl  [ ] docstring  [ ] test
    # [ ] getTargetIPduRef             [x] impl  [ ] docstring  [ ] test
    # [ ] setTargetIPduRef             [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()

        self.defaultValue: PduMappingDefaultValue = None
        self.targetIPduRef: RefType = None

    def getDefaultValue(self):
        return self.defaultValue

    def setDefaultValue(self, value):
        if value is not None:
            self.defaultValue = value
        return self

    def getTargetIPduRef(self):
        return self.targetIPduRef

    def setTargetIPduRef(self, value):
        if value is not None:
            self.targetIPduRef = value
        return self


class IPduMapping(ARObject, VariationPointCapable):
    """Arranges those IPdus that are transferred by the gateway from one channel to the other in pairs and defines the mapping between them."""

    # IPduMapping method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 8.3, p.840
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                 [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getIntroduction          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setIntroduction          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getPduMaxLength          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setPduMaxLength          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getPdurTpChunkSize       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setPdurTpChunkSize       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSourceIPduRef         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSourceIPduRef         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTargetIPdu            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTargetIPdu            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # This represents introductory documentation about the IPdu mapping.
        self.introduction: Optional[DocumentationBlock] = None

        # Define the maximum length in bytes which limits the length of the Pdu during gateway operation if the runtime length of the received Pdu exceeds this limit.
        self.pduMaxLength: Optional[PositiveInteger] = None

        # Optionally defines the to be configured Pdu Router Tp ChunkSize for this routing relation.
        self.pdurTpChunkSize: Optional[PositiveInteger] = None

        # Source destination of the referencing mapping.
        self.sourceIPduRef: Optional[RefType] = None

        # Target destination of the referencing mapping.
        self.targetIPdu: Optional[TargetIPduRef] = None

    def getIntroduction(self) -> Optional[DocumentationBlock]:
        """
        This represents introductory documentation about the IPdu mapping.
        """
        return self.introduction

    def setIntroduction(self, value: Optional[DocumentationBlock]) -> "IPduMapping":
        """
        This represents introductory documentation about the IPdu mapping.
        A None value is a no-op and does not overwrite an existing introduction.
        """
        if value is not None:
            self.introduction = value
        return self

    def getPduMaxLength(self) -> Optional[PositiveInteger]:
        """
        Define the maximum length in bytes which limits the length of the Pdu during gateway operation if the runtime length of the received Pdu exceeds this limit.
        """
        return self.pduMaxLength

    def setPduMaxLength(self, value: Optional[PositiveInteger]) -> "IPduMapping":
        """
        Define the maximum length in bytes which limits the length of the Pdu during gateway operation if the runtime length of the received Pdu exceeds this limit.
        A None value is a no-op and does not overwrite an existing pduMaxLength.
        """
        if value is not None:
            self.pduMaxLength = value
        return self

    def getPdurTpChunkSize(self) -> Optional[PositiveInteger]:
        """
        Optionally defines the to be configured Pdu Router Tp ChunkSize for this routing relation.
        """
        return self.pdurTpChunkSize

    def setPdurTpChunkSize(self, value: Optional[PositiveInteger]) -> "IPduMapping":
        """
        Optionally defines the to be configured Pdu Router Tp ChunkSize for this routing relation.
        A None value is a no-op and does not overwrite an existing pdurTpChunkSize.
        """
        if value is not None:
            self.pdurTpChunkSize = value
        return self

    def getSourceIPduRef(self) -> Optional[RefType]:
        """
        Source destination of the referencing mapping.
        """
        return self.sourceIPduRef

    def setSourceIPduRef(self, value: Optional[RefType]) -> "IPduMapping":
        """
        Source destination of the referencing mapping.
        A None value is a no-op and does not overwrite an existing sourceIPduRef.
        """
        if value is not None:
            self.sourceIPduRef = value
        return self

    def getTargetIPdu(self) -> Optional[TargetIPduRef]:
        """
        Target destination of the referencing mapping.
        """
        return self.targetIPdu

    def setTargetIPdu(self, value: Optional[TargetIPduRef]) -> "IPduMapping":
        """
        Target destination of the referencing mapping.
        A None value is a no-op and does not overwrite an existing targetIPdu.
        """
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
