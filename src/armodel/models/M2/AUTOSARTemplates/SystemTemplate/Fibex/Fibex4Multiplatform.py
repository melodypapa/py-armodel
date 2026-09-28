from __future__ import annotations
from typing import List, Optional
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.StereotypeMixins import VariationPointCapable

from armodel.models.M2.MSR.Documentation.TextModel.BlockElements import DocumentationBlock
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Integer, RefType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore import FibexElement


class FrameMapping(ARObject, VariationPointCapable):
    """
    The entire source frame is mapped as it is onto the target frame (what in general is only possible inside of a common platform). In this case source and target frame should be the identical object. Each pair consists in a SOURCE and a TARGET referencing to a FrameTriggering. The Frame Mapping is not supported by the Autosar BSW. The existence is optional and has been incorporated into the System Template mainly for compatibility in order to allow interchange between FIBEX and AUTOSAR descriptions.

    [constr_9289] Existence of FrameMapping.sourceFrame: For each FrameMapping, the reference to FrameTriggering in the role sourceFrame shall exist at the time when the System Description is complete.

    [constr_9290] Existence of FrameMapping.targetFrame: For each FrameMapping, the reference to FrameTriggering in the role targetFrame shall exist at the time when the System Description is complete.
    """

    # FrameMapping method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 8.2, p.838
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__             [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getIntroduction      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setIntroduction      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSourceFrameRef    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSourceFrameRef    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTargetFrameRef    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTargetFrameRef    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # This represents introductory documentation about the frame mapping.
        self.introduction: Optional[DocumentationBlock] = None

        # Source destination of the referencing mapping.
        self.sourceFrameRef: Optional[RefType] = None

        # Target destination of the referencing mapping.
        self.targetFrameRef: Optional[RefType] = None

    def getIntroduction(self) -> Optional[DocumentationBlock]:
        """
        This represents introductory documentation about the frame mapping.
        """
        return self.introduction

    def setIntroduction(self, value: Optional[DocumentationBlock]) -> FrameMapping:
        """
        This represents introductory documentation about the frame mapping.
        A None value is a no-op and does not overwrite an existing introduction.
        """
        if value is not None:
            self.introduction = value
        return self

    def getSourceFrameRef(self) -> Optional[RefType]:
        """
        Source destination of the referencing mapping.
        """
        return self.sourceFrameRef

    def setSourceFrameRef(self, value: Optional[RefType]) -> FrameMapping:
        """
        Source destination of the referencing mapping.
        A None value is a no-op and does not overwrite an existing sourceFrameRef.
        """
        if value is not None:
            self.sourceFrameRef = value
        return self

    def getTargetFrameRef(self) -> Optional[RefType]:
        """
        Target destination of the referencing mapping.
        """
        return self.targetFrameRef

    def setTargetFrameRef(self, value: Optional[RefType]) -> FrameMapping:
        """
        Target destination of the referencing mapping.
        A None value is a no-op and does not overwrite an existing targetFrameRef.
        """
        if value is not None:
            self.targetFrameRef = value
        return self


class ISignalMapping(ARObject, VariationPointCapable):
    """
    Arranges those signals (or SignalGroups) that are transferred by the gateway from one channel to the other in pairs and defines the mapping between them. Each pair consists in a source and a target referencing to a ISignalTriggering.

    [constr_9298] Existence of ISignalMapping.sourceSignal: For each ISignalMapping, the reference to ISignalTriggering in the role sourceSignal shall exist at the time when the System Description is complete.

    [constr_9299] Existence of ISignalMapping.targetSignal: For each ISignalMapping, the reference to ISignalTriggering in the role targetSignal shall exist at the time when the System Description is complete.
    """

    # ISignalMapping method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 8.7, p.846
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__              [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getIntroduction       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setIntroduction       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSourceSignalRef    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSourceSignalRef    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTargetSignalRef    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTargetSignalRef    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # This represents introductory documentation about the ISignal mapping.
        self.introduction: Optional[DocumentationBlock] = None

        # Source destination of the referencing mapping.
        self.sourceSignalRef: Optional[RefType] = None

        # Target destination of the referencing mapping.
        self.targetSignalRef: Optional[RefType] = None

    def getIntroduction(self) -> Optional[DocumentationBlock]:
        """
        This represents introductory documentation about the ISignal mapping.
        """
        return self.introduction

    def setIntroduction(self, value: Optional[DocumentationBlock]) -> ISignalMapping:
        """
        This represents introductory documentation about the ISignal mapping.
        A None value is a no-op and does not overwrite an existing introduction.
        """
        if value is not None:
            self.introduction = value
        return self

    def getSourceSignalRef(self) -> Optional[RefType]:
        """
        Source destination of the referencing mapping.
        """
        return self.sourceSignalRef

    def setSourceSignalRef(self, value: Optional[RefType]) -> ISignalMapping:
        """
        Source destination of the referencing mapping.
        A None value is a no-op and does not overwrite an existing sourceSignalRef.
        """
        if value is not None:
            self.sourceSignalRef = value
        return self

    def getTargetSignalRef(self) -> Optional[RefType]:
        """
        Target destination of the referencing mapping.
        """
        return self.targetSignalRef

    def setTargetSignalRef(self, value: Optional[RefType]) -> ISignalMapping:
        """
        Target destination of the referencing mapping.
        A None value is a no-op and does not overwrite an existing targetSignalRef.
        """
        if value is not None:
            self.targetSignalRef = value
        return self


class DefaultValueElement(ARObject):
    """
    The default value consists of a number of elements. Each element is one byte long and the number of elements is specified by SduLength.
    """

    # DefaultValueElement method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 8.6, p.841
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__             [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getElementByteValue  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setElementByteValue  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getElementPosition   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setElementPosition   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # The integer value of a freely defined data byte.
        self.elementByteValue: Optional[Integer] = None

        # This attribute specifies the byte position of the element within the default value
        self.elementPosition: Optional[Integer] = None

    def getElementByteValue(self) -> Optional[Integer]:
        """
        The integer value of a freely defined data byte.
        """
        return self.elementByteValue

    def setElementByteValue(self, value: Optional[Integer]) -> DefaultValueElement:
        """
        The integer value of a freely defined data byte.
        A None value is a no-op and does not overwrite an existing elementByteValue.
        """
        if value is not None:
            self.elementByteValue = value
        return self

    def getElementPosition(self) -> Optional[Integer]:
        """
        This attribute specifies the byte position of the element within the default value
        """
        return self.elementPosition

    def setElementPosition(self, value: Optional[Integer]) -> DefaultValueElement:
        """
        This attribute specifies the byte position of the element within the default value
        A None value is a no-op and does not overwrite an existing elementPosition.
        """
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

    def addDefaultValueElement(self, value: Optional[DefaultValueElement]) -> PduMappingDefaultValue:
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

    [constr_9294] Existence of TargetIPduRef.targetIPdu: For each TargetIPduRef, the reference to PduTriggering in the role targetIPdu shall exist at the time when the System Description is complete.
    """

    # TargetIPduRef method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 8.4, p.841
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__             [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getDefaultValue      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDefaultValue      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTargetIPduRef     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTargetIPduRef     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # If no I-Pdu has been received a default value will be distributed.
        self.defaultValue: Optional[PduMappingDefaultValue] = None

        # IPdu Reference
        self.targetIPduRef: Optional[RefType] = None

    def getDefaultValue(self) -> Optional[PduMappingDefaultValue]:
        """
        If no I-Pdu has been received a default value will be distributed.
        """
        return self.defaultValue

    def setDefaultValue(self, value: Optional[PduMappingDefaultValue]) -> TargetIPduRef:
        """
        If no I-Pdu has been received a default value will be distributed.
        A None value is a no-op and does not overwrite an existing defaultValue.
        """
        if value is not None:
            self.defaultValue = value
        return self

    def getTargetIPduRef(self) -> Optional[RefType]:
        """
        IPdu Reference
        """
        return self.targetIPduRef

    def setTargetIPduRef(self, value: Optional[RefType]) -> TargetIPduRef:
        """
        IPdu Reference
        A None value is a no-op and does not overwrite an existing targetIPduRef.
        """
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

    def setIntroduction(self, value: Optional[DocumentationBlock]) -> IPduMapping:
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

    def setPduMaxLength(self, value: Optional[PositiveInteger]) -> IPduMapping:
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

    def setPdurTpChunkSize(self, value: Optional[PositiveInteger]) -> IPduMapping:
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

    def setSourceIPduRef(self, value: Optional[RefType]) -> IPduMapping:
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

    def setTargetIPdu(self, value: Optional[TargetIPduRef]) -> IPduMapping:
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
