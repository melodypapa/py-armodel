from __future__ import annotations
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.VariationPointCapable import VariationPointCapable

from abc import ABC
from typing import List, Optional, TYPE_CHECKING
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable, Describable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AREnum, ARLiteral, ARNumerical, PositiveInteger, Boolean, ByteOrderEnum
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Integer, RefType, String
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import TimeValue, UnlimitedInteger
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import SwDataDefProps
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Filter import DataFilter
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.Timing import TransmissionModeDeclaration, TriggerIPduSendCondition
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore import FibexElement
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import CommConnectorPort

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.CommonStructure import ValueSpecification
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import HandleOutOfRangeEnum
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping import DataTypePolicyEnum
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import TransformationISignalProps


class PduToFrameMapping(Identifiable, VariationPointCapable):
    """
    A PduToFrameMapping defines the composition of Pdus in each frame.
    """

    # PduToFrameMapping method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.29, p.347
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                        [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getPackingByteOrder             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setPackingByteOrder             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getPduRef                       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setPduRef                       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getStartPosition                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setStartPosition                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getUpdateIndicationBitPosition  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setUpdateIndicationBitPosition  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This attribute defines the order of the bytes of the Pdu and the packing into the Frame. Please consider that [constr_3246] and [constr_3222] are restricting the usage of this attribute.
        self.packingByteOrder: Optional[ByteOrderEnum] = None

        # Reference to a I-Pdu, N-Pdu or NmPdu that is transmitted in the Frame.
        self.pduRef: Optional[RefType] = None

        # This attribute describes the bitposition of a Pdu within a Frame. Please note that the absolute position of the Pdu in the Frame is determined by the definition of the packingByteOrder attribute. If Big Endian is specified, the start position indicates the bit position of the most significant bit in the Frame. If Little Endian is specified, the start position indicates the bit position of the least significant bit in the Frame. The bit counting in byte 0 starts with bit 0 (least significant bit). The most significant bit in byte 0 is bit 7. The Pdus are byte aligned in a Frame and only the values 0, 8, 16, 24,... (for little endian) and 7, 15, 23, ... (for big endian) are allowed.
        self.startPosition: Optional[Integer] = None

        # Indication to the receivers that the corresponding Pdu was updated by the sender. This attribute describes the position of the update bit in the frame that aggregates this PDUToFrameMapping. Length is always one bit. Note that the exact bit position of the updateIndicationBitPosition is linked to the value of the attribute packingByteOrder because the method of finding the bit position is different for the values mostSignificantByteFirst and mostSignificantByteLast. This means that if the value of packingByteOrder is changed while the value of updateIndicationBitPosition remains unchanged the exact bit position of updateIndicationBitPosition within the enclosing Frame still undergoes a change. This attribute denotes the least significant bit for "Little Endian" and the most significant bit for "Big Endian".
        self.updateIndicationBitPosition: Optional[Integer] = None

    def getPackingByteOrder(self) -> Optional[ByteOrderEnum]:
        """
        This attribute defines the order of the bytes of the Pdu and the packing into the Frame. Please consider that [constr_3246] and [constr_3222] are restricting the usage of this attribute.
        """
        return self.packingByteOrder

    def setPackingByteOrder(self, value: Optional[ByteOrderEnum]) -> "PduToFrameMapping":
        """
        This attribute defines the order of the bytes of the Pdu and the packing into the Frame. Please consider that [constr_3246] and [constr_3222] are restricting the usage of this attribute.
        A None value is a no-op and does not overwrite an existing packingByteOrder.
        """
        if value is not None:
            self.packingByteOrder = value
        return self

    def getPduRef(self) -> Optional[RefType]:
        """
        Reference to a I-Pdu, N-Pdu or NmPdu that is transmitted in the Frame.
        """
        return self.pduRef

    def setPduRef(self, value: Optional[RefType]) -> "PduToFrameMapping":
        """
        Reference to a I-Pdu, N-Pdu or NmPdu that is transmitted in the Frame.
        A None value is a no-op and does not overwrite an existing pduRef.
        """
        if value is not None:
            self.pduRef = value
        return self

    def getStartPosition(self) -> Optional[Integer]:
        """
        This attribute describes the bitposition of a Pdu within a Frame. Please note that the absolute position of the Pdu in the Frame is determined by the definition of the packingByteOrder attribute. If Big Endian is specified, the start position indicates the bit position of the most significant bit in the Frame. If Little Endian is specified, the start position indicates the bit position of the least significant bit in the Frame. The bit counting in byte 0 starts with bit 0 (least significant bit). The most significant bit in byte 0 is bit 7. The Pdus are byte aligned in a Frame and only the values 0, 8, 16, 24,... (for little endian) and 7, 15, 23, ... (for big endian) are allowed.
        """
        return self.startPosition

    def setStartPosition(self, value: Optional[Integer]) -> "PduToFrameMapping":
        """
        This attribute describes the bitposition of a Pdu within a Frame. Please note that the absolute position of the Pdu in the Frame is determined by the definition of the packingByteOrder attribute. If Big Endian is specified, the start position indicates the bit position of the most significant bit in the Frame. If Little Endian is specified, the start position indicates the bit position of the least significant bit in the Frame. The bit counting in byte 0 starts with bit 0 (least significant bit). The most significant bit in byte 0 is bit 7. The Pdus are byte aligned in a Frame and only the values 0, 8, 16, 24,... (for little endian) and 7, 15, 23, ... (for big endian) are allowed.
        A None value is a no-op and does not overwrite an existing startPosition.
        """
        if value is not None:
            self.startPosition = value
        return self

    def getUpdateIndicationBitPosition(self) -> Optional[Integer]:
        """
        Indication to the receivers that the corresponding Pdu was updated by the sender. This attribute describes the position of the update bit in the frame that aggregates this PDUToFrameMapping. Length is always one bit. Note that the exact bit position of the updateIndicationBitPosition is linked to the value of the attribute packingByteOrder because the method of finding the bit position is different for the values mostSignificantByteFirst and mostSignificantByteLast. This means that if the value of packingByteOrder is changed while the value of updateIndicationBitPosition remains unchanged the exact bit position of updateIndicationBitPosition within the enclosing Frame still undergoes a change. This attribute denotes the least significant bit for "Little Endian" and the most significant bit for "Big Endian".
        """
        return self.updateIndicationBitPosition

    def setUpdateIndicationBitPosition(self, value: Optional[Integer]) -> "PduToFrameMapping":
        """
        Indication to the receivers that the corresponding Pdu was updated by the sender. This attribute describes the position of the update bit in the frame that aggregates this PDUToFrameMapping. Length is always one bit. Note that the exact bit position of the updateIndicationBitPosition is linked to the value of the attribute packingByteOrder because the method of finding the bit position is different for the values mostSignificantByteFirst and mostSignificantByteLast. This means that if the value of packingByteOrder is changed while the value of updateIndicationBitPosition remains unchanged the exact bit position of updateIndicationBitPosition within the enclosing Frame still undergoes a change. This attribute denotes the least significant bit for "Little Endian" and the most significant bit for "Big Endian".
        A None value is a no-op and does not overwrite an existing updateIndicationBitPosition.
        """
        if value is not None:
            self.updateIndicationBitPosition = value
        return self


class Frame(FibexElement, ABC):
    """
    Data frame which is sent over a communication medium. This element describes the pure Layout of a frame sent on a channel.
    Data frame which is sent over a communication medium. This element describes the pure Layout of a frame sent on a channel.
    """

    # Frame method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.78, p.418
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getFrameLength            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setFrameLength            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] createPduToFrameMapping   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getPduToFrameMappings     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is Frame:
            raise TypeError("Frame is an abstract class.")

        super().__init__(parent, short_name)

        # The used length (in bytes) of the referencing frame. Should not be confused with a static byte length reserved for each frame by some platforms (e.g. FlexRay). The frameLength of zero bytes is allowed. Please consider also TPS_SYST_02255.
        self.frameLength: Optional[Integer] = None

        # A frames layout as a sequence of Pdus. atpVariation: The content of a frame can be variable. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=pduToFrameMapping.shortName, pduToFrameMapping.variationPoint.shortLabel vh.latestBindingTime=postBuild
        self.pduToFrameMappings: List[PduToFrameMapping] = []

    def getFrameLength(self) -> Optional[Integer]:
        """
        The used length (in bytes) of the referencing frame. Should not be confused with a static byte length reserved for each frame by some platforms (e.g. FlexRay). The frameLength of zero bytes is allowed. Please consider also TPS_SYST_02255.
        """
        return self.frameLength

    def setFrameLength(self, value: Optional[Integer]) -> "Frame":
        """
        The used length (in bytes) of the referencing frame. Should not be confused with a static byte length reserved for each frame by some platforms (e.g. FlexRay). The frameLength of zero bytes is allowed. Please consider also TPS_SYST_02255.
        A None value is a no-op and does not overwrite an existing frameLength.
        """
        if value is not None:
            self.frameLength = value
        return self

    def createPduToFrameMapping(self, short_name: str) -> PduToFrameMapping:
        if not self.IsElementExists(short_name, PduToFrameMapping):
            mapping = PduToFrameMapping(self, short_name)
            self.addElement(mapping)
            self.pduToFrameMappings.append(mapping)
        return self.getElement(short_name, PduToFrameMapping)

    def getPduToFrameMappings(self) -> List[PduToFrameMapping]:
        return list(sorted(filter(lambda a: isinstance(a, PduToFrameMapping), self.elements), key=lambda o: o.short_name))


class ContainedIPduProps(ARObject):
    """
    Defines properties for contained Interaction Protocol Data Units (IPDUs),
    specifying collection semantics, header IDs, offset, timeout,
    trigger, and update indication bit position properties.
    """

    # ContainedIPduProps method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getCollectionSemantics       [x] impl  [ ] docstring  [ ] test
    # [ ] setCollectionSemantics       [x] impl  [ ] docstring  [ ] test
    # [ ] getHeaderIdLongHeader        [x] impl  [ ] docstring  [ ] test
    # [ ] setHeaderIdLongHeader        [x] impl  [ ] docstring  [ ] test
    # [ ] getHeaderIdShortHeader       [x] impl  [ ] docstring  [ ] test
    # [ ] setHeaderIdShortHeader       [x] impl  [ ] docstring  [ ] test
    # [ ] getOffset                    [x] impl  [ ] docstring  [ ] test
    # [ ] setOffset                    [x] impl  [ ] docstring  [ ] test
    # [ ] getTimeout                   [x] impl  [ ] docstring  [ ] test
    # [ ] setTimeout                   [x] impl  [ ] docstring  [ ] test
    # [ ] getTrigger                   [x] impl  [ ] docstring  [ ] test
    # [ ] setTrigger                   [x] impl  [ ] docstring  [ ] test
    # [ ] getUpdateIndicationBitPosition [x] impl  [ ] docstring  [ ] test
    # [ ] setUpdateIndicationBitPosition [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()

        self.collectionSemantics: ARLiteral = None
        self.headerIdLongHeader: PositiveInteger = None
        self.headerIdShortHeader: PositiveInteger = None
        self.offset: ARNumerical = None
        self.timeout: ARNumerical = None
        self.trigger: ARLiteral = None
        self.updateIndicationBitPosition: ARNumerical = None

    def getCollectionSemantics(self):
        return self.collectionSemantics

    def setCollectionSemantics(self, value):
        self.collectionSemantics = value
        return self

    def getHeaderIdLongHeader(self):
        return self.headerIdLongHeader

    def setHeaderIdLongHeader(self, value):
        self.headerIdLongHeader = value
        return self

    def getHeaderIdShortHeader(self):
        return self.headerIdShortHeader

    def setHeaderIdShortHeader(self, value):
        self.headerIdShortHeader = value
        return self

    def getOffset(self):
        return self.offset

    def setOffset(self, value):
        self.offset = value
        return self

    def getTimeout(self):
        return self.timeout

    def setTimeout(self, value):
        self.timeout = value
        return self

    def getTrigger(self):
        return self.trigger

    def setTrigger(self, value):
        self.trigger = value
        return self

    def getUpdateIndicationBitPosition(self):
        return self.updateIndicationBitPosition

    def setUpdateIndicationBitPosition(self, value):
        self.updateIndicationBitPosition = value
        return self


class ISignalGroup(FibexElement):
    """
    SignalGroup of the Interaction Layer. The RTE supports a "signal fan-out" where the same System Signal Group is sent in different SignalIPdus to multiple receivers. An ISignalGroup refers to a set of ISignals that shall always be kept together. A ISignalGroup represents a COM Signal Group. Therefore it is recommended to put the ISignalGroup in the same Package as ISignals (see atp.recommendedPackage) Tags: atp.recommendedPackage=ISignalGroup
    """

    # ISignalGroup method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.12, p.324
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getComBasedSignalGroupTransformationRef [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setComBasedSignalGroupTransformationRef [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getISignalRefs               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addISignalRef                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSystemSignalGroupRef      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSystemSignalGroupRef      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTransformationISignalProps [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addTransformationISignalProps [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        # Optional reference to a DataTransformation which represents the transformer chain that is used to transform the data that shall be placed inside this ISignalGroup based on the COMBasedTransformer approach. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=comBasedSignalGroupTransformation.data Transformation, comBasedSignalGroup Transformation.variationPoint.shortLabel vh.latestBindingTime=codeGenerationTime
        self.comBasedSignalGroupTransformationRef: Optional[RefType] = None

        # Reference to a set of ISignals that shall always be kept together.
        self.iSignalRefs: List[RefType] = []

        # Reference to the SystemSignalGroup that is defined on VFB level and that is supposed to be transmitted in the ISignalGroup.
        self.systemSignalGroupRef: Optional[RefType] = None

        # A transformer chain consists of an ordered list of transformers. The ISignalGroup specific configuration properties for each transformer are defined in the TransformationISignalProps class. The transformer configuration properties that are common for all ISignal Groups are described in the TransformationTechnology class. Stereotypes: atpSplitable Tags: atp.Splitkey=transformationISignalProps
        self.transformationISignalProps: List[TransformationISignalProps] = []

    def getComBasedSignalGroupTransformationRef(self) -> Optional[RefType]:
        """
        Optional reference to a DataTransformation which represents the transformer chain that is used to transform the data that shall be placed inside this ISignalGroup based on the COMBasedTransformer approach. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=comBasedSignalGroupTransformation.data Transformation, comBasedSignalGroup Transformation.variationPoint.shortLabel vh.latestBindingTime=codeGenerationTime
        """
        return self.comBasedSignalGroupTransformationRef

    def setComBasedSignalGroupTransformationRef(self, value: Optional[RefType]) -> "ISignalGroup":
        """
        Optional reference to a DataTransformation which represents the transformer chain that is used to transform the data that shall be placed inside this ISignalGroup based on the COMBasedTransformer approach. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=comBasedSignalGroupTransformation.data Transformation, comBasedSignalGroup Transformation.variationPoint.shortLabel vh.latestBindingTime=codeGenerationTime
        A None value is a no-op and does not overwrite an existing comBasedSignalGroupTransformationRef.
        """
        if value is not None:
            self.comBasedSignalGroupTransformationRef = value
        return self

    def getISignalRefs(self) -> List[RefType]:
        """
        Reference to a set of ISignals that shall always be kept together.
        """
        return self.iSignalRefs

    def addISignalRef(self, value: RefType) -> "ISignalGroup":
        """
        Reference to a set of ISignals that shall always be kept together.
        """
        self.iSignalRefs.append(value)
        return self

    def getSystemSignalGroupRef(self) -> Optional[RefType]:
        """
        Reference to the SystemSignalGroup that is defined on VFB level and that is supposed to be transmitted in the ISignalGroup.
        """
        return self.systemSignalGroupRef

    def setSystemSignalGroupRef(self, value: Optional[RefType]) -> "ISignalGroup":
        """
        Reference to the SystemSignalGroup that is defined on VFB level and that is supposed to be transmitted in the ISignalGroup.
        A None value is a no-op and does not overwrite an existing systemSignalGroupRef.
        """
        if value is not None:
            self.systemSignalGroupRef = value
        return self

    def getTransformationISignalProps(self) -> List[TransformationISignalProps]:
        """
        A transformer chain consists of an ordered list of transformers. The ISignalGroup specific configuration properties for each transformer are defined in the TransformationISignalProps class. The transformer configuration properties that are common for all ISignal Groups are described in the TransformationTechnology class. Stereotypes: atpSplitable Tags: atp.Splitkey=transformationISignalProps
        """
        return self.transformationISignalProps

    def addTransformationISignalProps(self, value: TransformationISignalProps) -> "ISignalGroup":
        """
        A transformer chain consists of an ordered list of transformers. The ISignalGroup specific configuration properties for each transformer are defined in the TransformationISignalProps class. The transformer configuration properties that are common for all ISignal Groups are described in the TransformationTechnology class. Stereotypes: atpSplitable Tags: atp.Splitkey=transformationISignalProps
        """
        self.transformationISignalProps.append(value)
        return self


class ISignalIPduGroup(FibexElement):
    """
    Defines a group of Interaction Protocol Data Units (IPDUs) based on interaction signals,
    specifying communication direction, mode, and references to contained
    IPDU groups and individual IPDUs.
    """

    # ISignalIPduGroup method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getCommunicationDirection    [x] impl  [ ] docstring  [ ] test
    # [ ] setCommunicationDirection    [x] impl  [ ] docstring  [ ] test
    # [ ] getCommunicationMode         [x] impl  [ ] docstring  [ ] test
    # [ ] setCommunicationMode         [x] impl  [ ] docstring  [ ] test
    # [ ] getContainedISignalIPduGroupRefs [x] impl  [ ] docstring  [ ] test
    # [ ] addContainedISignalIPduGroupRef [x] impl  [ ] docstring  [ ] test
    # [ ] getISignalIPduRefs           [x] impl  [ ] docstring  [ ] test
    # [ ] addISignalIPduRef            [x] impl  [ ] docstring  [ ] test
    # [ ] getNmPduRefs                 [x] impl  [ ] docstring  [ ] test
    # [ ] addNmPduRef                  [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        self.communicationDirection = None
        self.communicationMode = None
        self.containedISignalIPduGroupRefs = []
        self.iSignalIPduRefs = []
        self.nmPduRefs = []

    def getCommunicationDirection(self):
        return self.communicationDirection

    def setCommunicationDirection(self, value):
        self.communicationDirection = value
        return self

    def getCommunicationMode(self):
        return self.communicationMode

    def setCommunicationMode(self, value):
        self.communicationMode = value
        return self

    def getContainedISignalIPduGroupRefs(self):
        return self.containedISignalIPduGroupRefs

    def addContainedISignalIPduGroupRef(self, value):
        self.containedISignalIPduGroupRefs.append(value)
        return self

    def getISignalIPduRefs(self):
        return self.iSignalIPduRefs

    def addISignalIPduRef(self, value):
        self.iSignalIPduRefs.append(value)
        return self

    def getNmPduRefs(self):
        return self.nmPduRefs

    def addNmPduRef(self, value):
        self.nmPduRefs.append(value)
        return self


class Pdu(FibexElement, ABC):
    """
    Collection of all Pdus that can be routed through a bus interface.
    """

    # Pdu method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.17, p.340
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] setHasDynamicLength          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getHasDynamicLength          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setLength                    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getLength                    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is Pdu:
            raise TypeError("Pdu is an abstract class.")

        super().__init__(parent, short_name)

        # This attribute defines whether the Pdu has dynamic length (true) or not (false). Please note that the usage of this attribute is restricted by [constr_3448].
        self.hasDynamicLength: Boolean = None

        # Pdu length in bytes. In case of dynamic length IPdus (containing a dynamical length signal), this value indicates the maximum data length. It should be noted that in former AUTOSAR releases (Rel 2.1, Rel 3.0, Rel 3.1, Rel 4.0 Rev. 1) this parameter was defined in bits. The Pdu length of zero bytes is allowed.
        self.length: UnlimitedInteger = None

    def setHasDynamicLength(self, value: Optional[Boolean]) -> "Pdu":
        """
        This attribute defines whether the Pdu has dynamic length (true) or not (false). Please note that the usage of this attribute is restricted by [constr_3448].
        A None value is a no-op and does not overwrite an existing hasDynamicLength.
        """
        if value is not None:
            self.hasDynamicLength = value
        return self

    def getHasDynamicLength(self) -> Optional[Boolean]:
        """
        This attribute defines whether the Pdu has dynamic length (true) or not (false). Please note that the usage of this attribute is restricted by [constr_3448].
        """
        return self.hasDynamicLength

    def setLength(self, value: Optional[UnlimitedInteger]) -> "Pdu":
        """
        Pdu length in bytes. In case of dynamic length IPdus (containing a dynamical length signal), this value indicates the maximum data length. It should be noted that in former AUTOSAR releases (Rel 2.1, Rel 3.0, Rel 3.1, Rel 4.0 Rev. 1) this parameter was defined in bits. The Pdu length of zero bytes is allowed.
        A None value is a no-op and does not overwrite an existing length.
        """
        if value is not None:
            self.length = value
        return self

    def getLength(self) -> Optional[UnlimitedInteger]:
        """
        Pdu length in bytes. In case of dynamic length IPdus (containing a dynamical length signal), this value indicates the maximum data length. It should be noted that in former AUTOSAR releases (Rel 2.1, Rel 3.0, Rel 3.1, Rel 4.0 Rev. 1) this parameter was defined in bits. The Pdu length of zero bytes is allowed.
        """
        return self.length


class IPdu(Pdu, ABC):
    """
    The IPdu (Interaction Layer Protocol Data Unit) element is used to sum up all Pdus that are routed by the PduR.
    """

    # IPdu method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.18, p.341
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getContainedIPduProps     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setContainedIPduProps     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is IPdu:
            raise TypeError("IPdu is an abstract class.")

        super().__init__(parent, short_name)

        # Defines whether this IPdu may be collected inside a ContainerIPdu.
        self.containedIPduProps: Optional[ContainedIPduProps] = None

    def getContainedIPduProps(self) -> Optional[ContainedIPduProps]:
        """
        Defines whether this IPdu may be collected inside a ContainerIPdu.
        """
        return self.containedIPduProps

    def setContainedIPduProps(self, value: Optional[ContainedIPduProps]) -> "IPdu":
        """
        Defines whether this IPdu may be collected inside a ContainerIPdu.
        A None value is a no-op and does not overwrite an existing containedIPduProps.
        """
        if value is not None:
            self.containedIPduProps = value
        return self


class SecureCommunicationProps(ARObject):
    """
    This meta-class contains configuration settings that are specific for an individual SecuredIPdu.
    """

    # SecureCommunicationProps method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.44, p.369
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                               [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getAuthDataFreshnessLength             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setAuthDataFreshnessLength             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getAuthDataFreshnessStartPosition      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setAuthDataFreshnessStartPosition      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getAuthenticationBuildAttempts         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setAuthenticationBuildAttempts         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getAuthenticationRetries               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setAuthenticationRetries               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getDataId                              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setDataId                              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getFreshnessValueId                    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setFreshnessValueId                    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMessageLinkLength                   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMessageLinkLength                   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMessageLinkPosition                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMessageLinkPosition                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSecondaryFreshnessValueId           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSecondaryFreshnessValueId           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSecuredAreaLength                   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSecuredAreaLength                   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSecuredAreaOffset                   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSecuredAreaOffset                   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        """
        Initializes the SecureCommunicationProps.
        """
        super().__init__()

        # This attribute defines the length in bits of the authentic PDU data that is passed to the SWC that verifies and generates the Freshness.
        self.authDataFreshnessLength: Optional[PositiveInteger] = None

        # This value determines the start position in bits of the Authentic PDU that shall be passed on to the SWC that verifies and generates the Freshness. The bit counting is done according to TPS_SYST_01068.
        self.authDataFreshnessStartPosition: Optional[PositiveInteger] = None

        # This attribute specifies the number of authentication build attempts.
        self.authenticationBuildAttempts: Optional[PositiveInteger] = None

        # This attribute defines the additional number of authentication attempts that are to be carried out when the generation of the authentication information failed for a given SecuredIPdu. If zero is set than only one authentication attempt is done.
        self.authenticationRetries: Optional[PositiveInteger] = None

        # This attribute defines a numerical identifier for the Secured I-PDU.
        self.dataId: Optional[PositiveInteger] = None

        # This attribute defines the Id of the Freshness Value. The Freshness Value might be a normal counter or a time value.
        self.freshnessValueId: Optional[PositiveInteger] = None

        # SecOC links an AuthenticIPdu and CryptographicIPdu together by repeating a specific part (Message Linker) of the AuthenticIPdu in the CryptographicIPdu. This attribute defines the length in bits of the messageLinker.
        self.messageLinkLength: Optional[PositiveInteger] = None

        # SecOC links an AuthenticIPdu and CryptographicIPdu together by repeating a specific part (Message Linker) of the AuthenticIPdu in the CryptographicIPdu. This attribute defines the startPosition in bits of the messageLinker.
        self.messageLinkPosition: Optional[PositiveInteger] = None

        # This attribute defines the Id of the Secondary Freshness Value. The Secondary Freshness Value might be a normal counter or a time value. Please note that this attribute is for documentation only to allow the configuration of required freshness value manager and no upstream mapping is defined for it.
        self.secondaryFreshnessValueId: Optional[PositiveInteger] = None

        # This attribute defines the length in bytes of the area within the payload Pdu which will be secured.
        self.securedAreaLength: Optional[PositiveInteger] = None

        # This attribute defines the start position (offset in byte) of the area within the payload Pdu which will be secured.
        self.securedAreaOffset: Optional[PositiveInteger] = None

    def getAuthDataFreshnessLength(self) -> Optional[PositiveInteger]:
        """
        This attribute defines the length in bits of the authentic PDU data that is passed to the SWC that verifies and generates the Freshness.
        """
        return self.authDataFreshnessLength

    def setAuthDataFreshnessLength(self, value: Optional[PositiveInteger]) -> "SecureCommunicationProps":
        """
        This attribute defines the length in bits of the authentic PDU data that is passed to the SWC that verifies and generates the Freshness.
        A None value is a no-op and does not overwrite an existing authDataFreshnessLength.
        """
        if value is not None:
            self.authDataFreshnessLength = value
        return self

    def getAuthDataFreshnessStartPosition(self) -> Optional[PositiveInteger]:
        """
        This value determines the start position in bits of the Authentic PDU that shall be passed on to the SWC that verifies and generates the Freshness. The bit counting is done according to TPS_SYST_01068.
        """
        return self.authDataFreshnessStartPosition

    def setAuthDataFreshnessStartPosition(self, value: Optional[PositiveInteger]) -> "SecureCommunicationProps":
        """
        This value determines the start position in bits of the Authentic PDU that shall be passed on to the SWC that verifies and generates the Freshness. The bit counting is done according to TPS_SYST_01068.
        A None value is a no-op and does not overwrite an existing authDataFreshnessStartPosition.
        """
        if value is not None:
            self.authDataFreshnessStartPosition = value
        return self

    def getAuthenticationBuildAttempts(self) -> Optional[PositiveInteger]:
        """
        This attribute specifies the number of authentication build attempts.
        """
        return self.authenticationBuildAttempts

    def setAuthenticationBuildAttempts(self, value: Optional[PositiveInteger]) -> "SecureCommunicationProps":
        """
        This attribute specifies the number of authentication build attempts.
        A None value is a no-op and does not overwrite an existing authenticationBuildAttempts.
        """
        if value is not None:
            self.authenticationBuildAttempts = value
        return self

    def getAuthenticationRetries(self) -> Optional[PositiveInteger]:
        """
        This attribute defines the additional number of authentication attempts that are to be carried out when the generation of the authentication information failed for a given SecuredIPdu. If zero is set than only one authentication attempt is done.
        """
        return self.authenticationRetries

    def setAuthenticationRetries(self, value: Optional[PositiveInteger]) -> "SecureCommunicationProps":
        """
        This attribute defines the additional number of authentication attempts that are to be carried out when the generation of the authentication information failed for a given SecuredIPdu. If zero is set than only one authentication attempt is done.
        A None value is a no-op and does not overwrite an existing authenticationRetries.
        """
        if value is not None:
            self.authenticationRetries = value
        return self

    def getDataId(self) -> Optional[PositiveInteger]:
        """
        This attribute defines a numerical identifier for the Secured I-PDU.
        """
        return self.dataId

    def setDataId(self, value: Optional[PositiveInteger]) -> "SecureCommunicationProps":
        """
        This attribute defines a numerical identifier for the Secured I-PDU.
        A None value is a no-op and does not overwrite an existing dataId.
        """
        if value is not None:
            self.dataId = value
        return self

    def getFreshnessValueId(self) -> Optional[PositiveInteger]:
        """
        This attribute defines the Id of the Freshness Value. The Freshness Value might be a normal counter or a time value.
        """
        return self.freshnessValueId

    def setFreshnessValueId(self, value: Optional[PositiveInteger]) -> "SecureCommunicationProps":
        """
        This attribute defines the Id of the Freshness Value. The Freshness Value might be a normal counter or a time value.
        A None value is a no-op and does not overwrite an existing freshnessValueId.
        """
        if value is not None:
            self.freshnessValueId = value
        return self

    def getMessageLinkLength(self) -> Optional[PositiveInteger]:
        """
        SecOC links an AuthenticIPdu and CryptographicIPdu together by repeating a specific part (Message Linker) of the AuthenticIPdu in the CryptographicIPdu. This attribute defines the length in bits of the messageLinker.
        """
        return self.messageLinkLength

    def setMessageLinkLength(self, value: Optional[PositiveInteger]) -> "SecureCommunicationProps":
        """
        SecOC links an AuthenticIPdu and CryptographicIPdu together by repeating a specific part (Message Linker) of the AuthenticIPdu in the CryptographicIPdu. This attribute defines the length in bits of the messageLinker.
        A None value is a no-op and does not overwrite an existing messageLinkLength.
        """
        if value is not None:
            self.messageLinkLength = value
        return self

    def getMessageLinkPosition(self) -> Optional[PositiveInteger]:
        """
        SecOC links an AuthenticIPdu and CryptographicIPdu together by repeating a specific part (Message Linker) of the AuthenticIPdu in the CryptographicIPdu. This attribute defines the startPosition in bits of the messageLinker.
        """
        return self.messageLinkPosition

    def setMessageLinkPosition(self, value: Optional[PositiveInteger]) -> "SecureCommunicationProps":
        """
        SecOC links an AuthenticIPdu and CryptographicIPdu together by repeating a specific part (Message Linker) of the AuthenticIPdu in the CryptographicIPdu. This attribute defines the startPosition in bits of the messageLinker.
        A None value is a no-op and does not overwrite an existing messageLinkPosition.
        """
        if value is not None:
            self.messageLinkPosition = value
        return self

    def getSecondaryFreshnessValueId(self) -> Optional[PositiveInteger]:
        """
        This attribute defines the Id of the Secondary Freshness Value. The Secondary Freshness Value might be a normal counter or a time value. Please note that this attribute is for documentation only to allow the configuration of required freshness value manager and no upstream mapping is defined for it.
        """
        return self.secondaryFreshnessValueId

    def setSecondaryFreshnessValueId(self, value: Optional[PositiveInteger]) -> "SecureCommunicationProps":
        """
        This attribute defines the Id of the Secondary Freshness Value. The Secondary Freshness Value might be a normal counter or a time value. Please note that this attribute is for documentation only to allow the configuration of required freshness value manager and no upstream mapping is defined for it.
        A None value is a no-op and does not overwrite an existing secondaryFreshnessValueId.
        """
        if value is not None:
            self.secondaryFreshnessValueId = value
        return self

    def getSecuredAreaLength(self) -> Optional[PositiveInteger]:
        """
        This attribute defines the length in bytes of the area within the payload Pdu which will be secured.
        """
        return self.securedAreaLength

    def setSecuredAreaLength(self, value: Optional[PositiveInteger]) -> "SecureCommunicationProps":
        """
        This attribute defines the length in bytes of the area within the payload Pdu which will be secured.
        A None value is a no-op and does not overwrite an existing securedAreaLength.
        """
        if value is not None:
            self.securedAreaLength = value
        return self

    def getSecuredAreaOffset(self) -> Optional[PositiveInteger]:
        """
        This attribute defines the start position (offset in byte) of the area within the payload Pdu which will be secured.
        """
        return self.securedAreaOffset

    def setSecuredAreaOffset(self, value: Optional[PositiveInteger]) -> "SecureCommunicationProps":
        """
        This attribute defines the start position (offset in byte) of the area within the payload Pdu which will be secured.
        A None value is a no-op and does not overwrite an existing securedAreaOffset.
        """
        if value is not None:
            self.securedAreaOffset = value
        return self


class SecuredIPdu(IPdu):
    """
    Represents a secured Interaction Protocol Data Unit (IPDU) with
    authentication, integrity protection, and other security properties
    for protected communication.
    """

    # SecuredIPdu method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getAuthenticationPropsRef    [x] impl  [ ] docstring  [ ] test
    # [ ] setAuthenticationPropsRef    [x] impl  [ ] docstring  [ ] test
    # [ ] getDynamicRuntimeLengthHandling [x] impl  [ ] docstring  [ ] test
    # [ ] setDynamicRuntimeLengthHandling [x] impl  [ ] docstring  [ ] test
    # [ ] getFreshnessPropsRef         [x] impl  [ ] docstring  [ ] test
    # [ ] setFreshnessPropsRef         [x] impl  [ ] docstring  [ ] test
    # [ ] getPayloadRef                [x] impl  [ ] docstring  [ ] test
    # [ ] setPayloadRef                [x] impl  [ ] docstring  [ ] test
    # [ ] getSecureCommunicationProps  [x] impl  [ ] docstring  [ ] test
    # [ ] setSecureCommunicationProps  [x] impl  [ ] docstring  [ ] test
    # [ ] getUseAsCryptographicIPdu    [x] impl  [ ] docstring  [ ] test
    # [ ] setUseAsCryptographicIPdu    [x] impl  [ ] docstring  [ ] test
    # [ ] getUseSecuredPduHeader       [x] impl  [ ] docstring  [ ] test
    # [ ] setUseSecuredPduHeader       [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.authenticationPropsRef: RefType = None
        self.dynamicRuntimeLengthHandling: Boolean = None
        self.freshnessPropsRef: RefType = None
        self.payloadRef: RefType = None
        self.secureCommunicationProps: SecureCommunicationProps = None
        self.useAsCryptographicIPdu: Boolean = None
        self.useSecuredPduHeader = None

    def getAuthenticationPropsRef(self):
        return self.authenticationPropsRef

    def setAuthenticationPropsRef(self, value):
        if value is not None:
            self.authenticationPropsRef = value
        return self

    def getDynamicRuntimeLengthHandling(self):
        return self.dynamicRuntimeLengthHandling

    def setDynamicRuntimeLengthHandling(self, value):
        if value is not None:
            self.dynamicRuntimeLengthHandling = value
        return self

    def getFreshnessPropsRef(self):
        return self.freshnessPropsRef

    def setFreshnessPropsRef(self, value):
        if value is not None:
            self.freshnessPropsRef = value
        return self

    def getPayloadRef(self):
        return self.payloadRef

    def setPayloadRef(self, value):
        if value is not None:
            self.payloadRef = value
        return self

    def getSecureCommunicationProps(self):
        return self.secureCommunicationProps

    def setSecureCommunicationProps(self, value):
        if value is not None:
            self.secureCommunicationProps = value
        return self

    def getUseAsCryptographicIPdu(self):
        return self.useAsCryptographicIPdu

    def setUseAsCryptographicIPdu(self, value):
        if value is not None:
            self.useAsCryptographicIPdu = value
        return self

    def getUseSecuredPduHeader(self):
        return self.useSecuredPduHeader

    def setUseSecuredPduHeader(self, value):
        if value is not None:
            self.useSecuredPduHeader = value
        return self


class TransferPropertyEnum(AREnum):
    """
    Transfer Properties of a Signal.
    """

    # TransferPropertyEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.15, p.327
    # (no methods)

    # If the signal has the TransferProperty pending, then the function Com_SendSignal shall not perform a transmission of the IPdu associated with the signal. Tags: atp.EnumerationLiteralIndex=0
    PENDING = "pending"

    # The signal in the assigned IPdu is updated and a request for the IPdu's transmission is made. Tags: atp.EnumerationLiteralIndex=1
    TRIGGERED = "triggered"

    # The signal in the assigned IPdu is updated and a request for the IPdus transmission is made only if the signal value is different from the already stored signal value. Tags: atp.EnumerationLiteralIndex=2
    TRIGGERED_ON_CHANGE = "triggeredOnChange"

    # The signal in the assigned IPdu is updated and a request for the IPdus transmission is made only if the signal value is different from the already stored signal value. In the DIRECT/N-TIMES or MIXED transmission mode (EventControlledTiming) the IPdu will be transmitted just once without a repetition, independent of the defined NumberOfRepeats. Tags: atp.EnumerationLiteralIndex=3
    TRIGGERED_ON_CHANGE_WITHOUT_REPETITION = "triggeredOnChangeWithoutRepetition"

    # The signal in the assigned IPdu is updated and a request for the IPdu's transmission is made. In the DIRECT/N-TIMES or MIXED transmission mode (EventControlledTiming) the IPdu will be transmitted just once without a repetition, independent of the defined NumberOfRepeats. Tags: atp.EnumerationLiteralIndex=4
    TRIGGERED_WITHOUT_REPETITION = "triggeredWithoutRepetition"

    def __init__(self):
        super().__init__(
            (
                TransferPropertyEnum.PENDING,
                TransferPropertyEnum.TRIGGERED,
                TransferPropertyEnum.TRIGGERED_ON_CHANGE,
                TransferPropertyEnum.TRIGGERED_ON_CHANGE_WITHOUT_REPETITION,
                TransferPropertyEnum.TRIGGERED_WITHOUT_REPETITION,
            )
        )


class ISignalToIPduMapping(Identifiable, VariationPointCapable):
    """
    An ISignalToIPduMapping describes the mapping of ISignals to ISignalIPdus and defines the position of the ISignal within an ISignalIPdu.
    """

    # ISignalToIPduMapping method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.14, p.326
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getISignalRef                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setISignalRef                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getISignalGroupRef           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setISignalGroupRef           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getPackingByteOrder          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setPackingByteOrder          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getStartPosition             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setStartPosition             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTransferProperty          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setTransferProperty          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getUpdateIndicationBitPosition [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setUpdateIndicationBitPosition [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Reference to a ISignal that is mapped into the ISignal IPdu. Each ISignal contained in the ISignalGroup shall be mapped into an IPdu by an own ISignalToIPduMapping. The references to the ISignal and to the ISignalGroup in an ISignalToIPduMapping are mutually exclusive.
        self.iSignalRef: Optional[RefType] = None

        # Reference to an ISignalGroup that is mapped into the SignalIPdu. If an ISignalToIPduMapping for an ISignal Group is defined, only the UpdateIndicationBitPosition and the transferProperty is relevant. The startPosition and the packingByteOrder shall be ignored. Each ISignal contained in the ISignalGroup shall be mapped into an IPdu by an own ISignalToIPduMapping. The references to the ISignal and to the ISignalGroup in an ISignalToIPduMapping are mutually exclusive.
        self.iSignalGroupRef: Optional[RefType] = None

        # This parameter defines the order of the bytes of the signal and the packing into the SignalIPdu. The byte ordering "Little Endian" (MostSignificantByteLast), "Big Endian" (MostSignificantByteFirst) and "Opaque" can be selected. For opaque data endianness conversion shall be configured to Opaque. The value of this attribute impacts the absolute position of the signal into the SignalIPdu (see the startPosition attribute description). For an ISignalGroup the packingByteOrder is irrelevant and shall be ignored.
        self.packingByteOrder: Optional[ByteOrderEnum] = None

        # This parameter is necessary to describe the bitposition of a signal within an SignalIPdu. It denotes the least significant bit for "Little Endian" and the most significant bit for "Big Endian" packed signals within the IPdu (see the description of the packingByteOrder attribute). In AUTOSAR the bit counting is always set to "sawtooth" and the bit order is set to "Decreasing". The bit counting in byte 0 starts with bit 0 (least significant bit). The most significant bit in byte 0 is bit 7. Please note that the way the bytes will be actually sent on the bus does not impact this representation: they will always be seen by the software as a byte array. If a mapping for the ISignalGroup is defined, this attribute is irrelevant and shall be ignored.
        self.startPosition: Optional[UnlimitedInteger] = None

        # Defines how the referenced ISignal contributes to the send triggering of the ISignalIPdu.
        self.transferProperty: Optional[TransferPropertyEnum] = None

        # The UpdateIndicationBit indicates to the receivers that the signal (or the signal group) was updated by the sender. Length is always one bit. The UpdateIndicationBitPosition attribute describes the position of the update bit within the SignalIPdu. For Signals of a ISignalGroup this attribute is irrelevant and shall be ignored. Note that the exact bit position of the updateIndicationBitPosition is linked to the value of the attribute packingByteOrder because the method of finding the bit position is different for the values mostSignificantByteFirst and mostSignificantByteLast. This means that if the value of packingByteOrder is changed while the value of updateIndicationBitPosition remains unchanged the exact bit position of updateIndicationBitPosition within the enclosing ISignalIPdu still undergoes a change. This attribute denotes the least significant bit for "Little Endian" and the most significant bit for "Big Endian" packed signals within the IPdu (see the description of the packingByteOrder attribute). In AUTOSAR the bit counting is always set to "sawtooth" and the bit order is set to "Decreasing". The bit counting in byte 0 starts with bit 0 (least significant bit). The most significant bit in byte 0 is bit 7.
        self.updateIndicationBitPosition: Optional[UnlimitedInteger] = None

    def getISignalRef(self) -> Optional[RefType]:
        """
        Reference to a ISignal that is mapped into the ISignal IPdu. Each ISignal contained in the ISignalGroup shall be mapped into an IPdu by an own ISignalToIPduMapping. The references to the ISignal and to the ISignalGroup in an ISignalToIPduMapping are mutually exclusive.
        """
        return self.iSignalRef

    def setISignalRef(self, value: Optional[RefType]) -> "ISignalToIPduMapping":
        """
        Reference to a ISignal that is mapped into the ISignal IPdu. Each ISignal contained in the ISignalGroup shall be mapped into an IPdu by an own ISignalToIPduMapping. The references to the ISignal and to the ISignalGroup in an ISignalToIPduMapping are mutually exclusive.
        A None value is a no-op and does not overwrite an existing iSignalRef.
        """
        if value is not None:
            self.iSignalRef = value
        return self

    def getISignalGroupRef(self) -> Optional[RefType]:
        """
        Reference to an ISignalGroup that is mapped into the SignalIPdu. If an ISignalToIPduMapping for an ISignal Group is defined, only the UpdateIndicationBitPosition and the transferProperty is relevant. The startPosition and the packingByteOrder shall be ignored. Each ISignal contained in the ISignalGroup shall be mapped into an IPdu by an own ISignalToIPduMapping. The references to the ISignal and to the ISignalGroup in an ISignalToIPduMapping are mutually exclusive.
        """
        return self.iSignalGroupRef

    def setISignalGroupRef(self, value: Optional[RefType]) -> "ISignalToIPduMapping":
        """
        Reference to an ISignalGroup that is mapped into the SignalIPdu. If an ISignalToIPduMapping for an ISignal Group is defined, only the UpdateIndicationBitPosition and the transferProperty is relevant. The startPosition and the packingByteOrder shall be ignored. Each ISignal contained in the ISignalGroup shall be mapped into an IPdu by an own ISignalToIPduMapping. The references to the ISignal and to the ISignalGroup in an ISignalToIPduMapping are mutually exclusive.
        A None value is a no-op and does not overwrite an existing iSignalGroupRef.
        """
        if value is not None:
            self.iSignalGroupRef = value
        return self

    def getPackingByteOrder(self) -> Optional[ByteOrderEnum]:
        """
        This parameter defines the order of the bytes of the signal and the packing into the SignalIPdu. The byte ordering "Little Endian" (MostSignificantByteLast), "Big Endian" (MostSignificantByteFirst) and "Opaque" can be selected. For opaque data endianness conversion shall be configured to Opaque. The value of this attribute impacts the absolute position of the signal into the SignalIPdu (see the startPosition attribute description). For an ISignalGroup the packingByteOrder is irrelevant and shall be ignored.
        """
        return self.packingByteOrder

    def setPackingByteOrder(self, value: Optional[ByteOrderEnum]) -> "ISignalToIPduMapping":
        """
        This parameter defines the order of the bytes of the signal and the packing into the SignalIPdu. The byte ordering "Little Endian" (MostSignificantByteLast), "Big Endian" (MostSignificantByteFirst) and "Opaque" can be selected. For opaque data endianness conversion shall be configured to Opaque. The value of this attribute impacts the absolute position of the signal into the SignalIPdu (see the startPosition attribute description). For an ISignalGroup the packingByteOrder is irrelevant and shall be ignored.
        A None value is a no-op and does not overwrite an existing packingByteOrder.
        """
        if value is not None:
            self.packingByteOrder = value
        return self

    def getStartPosition(self) -> Optional[UnlimitedInteger]:
        """
        This parameter is necessary to describe the bitposition of a signal within an SignalIPdu. It denotes the least significant bit for "Little Endian" and the most significant bit for "Big Endian" packed signals within the IPdu (see the description of the packingByteOrder attribute). In AUTOSAR the bit counting is always set to "sawtooth" and the bit order is set to "Decreasing". The bit counting in byte 0 starts with bit 0 (least significant bit). The most significant bit in byte 0 is bit 7. Please note that the way the bytes will be actually sent on the bus does not impact this representation: they will always be seen by the software as a byte array. If a mapping for the ISignalGroup is defined, this attribute is irrelevant and shall be ignored.
        """
        return self.startPosition

    def setStartPosition(self, value: Optional[UnlimitedInteger]) -> "ISignalToIPduMapping":
        """
        This parameter is necessary to describe the bitposition of a signal within an SignalIPdu. It denotes the least significant bit for "Little Endian" and the most significant bit for "Big Endian" packed signals within the IPdu (see the description of the packingByteOrder attribute). In AUTOSAR the bit counting is always set to "sawtooth" and the bit order is set to "Decreasing". The bit counting in byte 0 starts with bit 0 (least significant bit). The most significant bit in byte 0 is bit 7. Please note that the way the bytes will be actually sent on the bus does not impact this representation: they will always be seen by the software as a byte array. If a mapping for the ISignalGroup is defined, this attribute is irrelevant and shall be ignored.
        A None value is a no-op and does not overwrite an existing startPosition.
        """
        if value is not None:
            self.startPosition = value
        return self

    def getTransferProperty(self) -> Optional[TransferPropertyEnum]:
        """
        Defines how the referenced ISignal contributes to the send triggering of the ISignalIPdu.
        """
        return self.transferProperty

    def setTransferProperty(self, value: Optional[TransferPropertyEnum]) -> "ISignalToIPduMapping":
        """
        Defines how the referenced ISignal contributes to the send triggering of the ISignalIPdu.
        A None value is a no-op and does not overwrite an existing transferProperty.
        """
        if value is not None:
            self.transferProperty = value
        return self

    def getUpdateIndicationBitPosition(self) -> Optional[UnlimitedInteger]:
        """
        The UpdateIndicationBit indicates to the receivers that the signal (or the signal group) was updated by the sender. Length is always one bit. The UpdateIndicationBitPosition attribute describes the position of the update bit within the SignalIPdu. For Signals of a ISignalGroup this attribute is irrelevant and shall be ignored. Note that the exact bit position of the updateIndicationBitPosition is linked to the value of the attribute packingByteOrder because the method of finding the bit position is different for the values mostSignificantByteFirst and mostSignificantByteLast. This means that if the value of packingByteOrder is changed while the value of updateIndicationBitPosition remains unchanged the exact bit position of updateIndicationBitPosition within the enclosing ISignalIPdu still undergoes a change. This attribute denotes the least significant bit for "Little Endian" and the most significant bit for "Big Endian" packed signals within the IPdu (see the description of the packingByteOrder attribute). In AUTOSAR the bit counting is always set to "sawtooth" and the bit order is set to "Decreasing". The bit counting in byte 0 starts with bit 0 (least significant bit). The most significant bit in byte 0 is bit 7.
        """
        return self.updateIndicationBitPosition

    def setUpdateIndicationBitPosition(self, value: Optional[UnlimitedInteger]) -> "ISignalToIPduMapping":
        """
        The UpdateIndicationBit indicates to the receivers that the signal (or the signal group) was updated by the sender. Length is always one bit. The UpdateIndicationBitPosition attribute describes the position of the update bit within the SignalIPdu. For Signals of a ISignalGroup this attribute is irrelevant and shall be ignored. Note that the exact bit position of the updateIndicationBitPosition is linked to the value of the attribute packingByteOrder because the method of finding the bit position is different for the values mostSignificantByteFirst and mostSignificantByteLast. This means that if the value of packingByteOrder is changed while the value of updateIndicationBitPosition remains unchanged the exact bit position of updateIndicationBitPosition within the enclosing ISignalIPdu still undergoes a change. This attribute denotes the least significant bit for "Little Endian" and the most significant bit for "Big Endian" packed signals within the IPdu (see the description of the packingByteOrder attribute). In AUTOSAR the bit counting is always set to "sawtooth" and the bit order is set to "Decreasing". The bit counting in byte 0 starts with bit 0 (least significant bit). The most significant bit in byte 0 is bit 7.
        A None value is a no-op and does not overwrite an existing updateIndicationBitPosition.
        """
        if value is not None:
            self.updateIndicationBitPosition = value
        return self


class NmPdu(Pdu):
    """
    Network Management Pdu Tags: atp.recommendedPackage=Pdus
    """

    # NmPdu method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.20, p.343
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getISignalToIPduMappings     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] createISignalToIPduMapping   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getNmDataInformation         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setNmDataInformation         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getNmVoteInformation         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setNmVoteInformation         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getUnusedBitPattern          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setUnusedBitPattern          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This optional aggregation is used to describe NmUserData that is transmitted in the NmPdu. The counting of the startPosition starts at the beginning of the NmPdu regardless whether Cbv or Nid are used.
        self.iSignalToIPduMappings: List[ISignalToIPduMapping] = []

        # Defines if the Pdu contains NM Data. If the NmPdu does not aggregate any ISignalToIPduMappings it still may contain UserData that is set via Nm_SetUserData(). If the ISignalToIPduMapping exists then the nmDataInformation attribute shall be ignored.
        self.nmDataInformation: Optional[Boolean] = None

        # Defines if the Pdu contains NM Vote information.
        self.nmVoteInformation: Optional[Boolean] = None

        # AUTOSAR COM is filling not used areas of an Pdu with this bit-pattern. This attribute can only be used if the nmDataInformation attribute is set to true.
        self.unusedBitPattern: Optional[Integer] = None

    def getISignalToIPduMappings(self) -> List[ISignalToIPduMapping]:
        """
        This optional aggregation is used to describe NmUserData that is transmitted in the NmPdu. The counting of the startPosition starts at the beginning of the NmPdu regardless whether Cbv or Nid are used.
        """
        return self.iSignalToIPduMappings

    def createISignalToIPduMapping(self, short_name: str) -> ISignalToIPduMapping:
        """
        This optional aggregation is used to describe NmUserData that is transmitted in the NmPdu. The counting of the startPosition starts at the beginning of the NmPdu regardless whether Cbv or Nid are used.
        """
        if not self.IsElementExists(short_name, ISignalToIPduMapping):
            mapping = ISignalToIPduMapping(self, short_name)
            self.addElement(mapping)
            self.iSignalToIPduMappings.append(mapping)
        return self.getElement(short_name, ISignalToIPduMapping)

    def getNmDataInformation(self) -> Optional[Boolean]:
        """
        Defines if the Pdu contains NM Data. If the NmPdu does not aggregate any ISignalToIPduMappings it still may contain UserData that is set via Nm_SetUserData(). If the ISignalToIPduMapping exists then the nmDataInformation attribute shall be ignored.
        """
        return self.nmDataInformation

    def setNmDataInformation(self, value: Optional[Boolean]) -> "NmPdu":
        """
        Defines if the Pdu contains NM Data. If the NmPdu does not aggregate any ISignalToIPduMappings it still may contain UserData that is set via Nm_SetUserData(). If the ISignalToIPduMapping exists then the nmDataInformation attribute shall be ignored.
        A None value is a no-op and does not overwrite an existing nmDataInformation.
        """
        if value is not None:
            self.nmDataInformation = value
        return self

    def getNmVoteInformation(self) -> Optional[Boolean]:
        """
        Defines if the Pdu contains NM Vote information.
        """
        return self.nmVoteInformation

    def setNmVoteInformation(self, value: Optional[Boolean]) -> "NmPdu":
        """
        Defines if the Pdu contains NM Vote information.
        A None value is a no-op and does not overwrite an existing nmVoteInformation.
        """
        if value is not None:
            self.nmVoteInformation = value
        return self

    def getUnusedBitPattern(self) -> Optional[Integer]:
        """
        AUTOSAR COM is filling not used areas of an Pdu with this bit-pattern. This attribute can only be used if the nmDataInformation attribute is set to true.
        """
        return self.unusedBitPattern

    def setUnusedBitPattern(self, value: Optional[Integer]) -> "NmPdu":
        """
        AUTOSAR COM is filling not used areas of an Pdu with this bit-pattern. This attribute can only be used if the nmDataInformation attribute is set to true.
        A None value is a no-op and does not overwrite an existing unusedBitPattern.
        """
        if value is not None:
            self.unusedBitPattern = value
        return self


class NPdu(IPdu):
    """
    This is a Pdu of the Transport Layer. The main purpose of the TP Layer is to segment and reassemble IPdus. Tags: atp.recommendedPackage=Pdus
    """

    # NPdu method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.21, p.343
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [x] reader  [x] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class DcmIPdu(IPdu):
    """
    Represents a Diagnostic Communication Management Interaction Protocol Data Unit (IPDU)
    used for diagnostic communication in the AUTOSAR system.
    """

    # DcmIPdu method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getDiagPduType               [x] impl  [ ] docstring  [ ] test
    # [ ] setDiagPduType               [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.diagPduType: ARLiteral = None

    def getDiagPduType(self):
        return self.diagPduType

    def setDiagPduType(self, value):
        self.diagPduType = value
        return self


class IPduTiming(Describable, VariationPointCapable):
    """
    AUTOSAR COM provides the possibility to define two different TRANSMISSION MODES for each IPdu. The Transmission Mode of an IPdu that is valid at a specific point in time is selected using the values of the signals that are mapped to this IPdu. For each IPdu a Transmission Mode Selector is defined. The Transmission Mode Selector is calculated by evaluating the conditions for a subset of signals (class TransmissionModeCondition in the System Template). The Transmission Mode Selector is defined to be true, if at least one Condition evaluates to true and is defined to be false, if all Conditions evaluate to false.
    """

    # IPduTiming method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.30, p.348
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getMinimumDelay              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMinimumDelay              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTransmissionModeDeclaration [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setTransmissionModeDeclaration [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # Minimum Delay in seconds between successive transmissions of this I-PDU, independent of the Transmission Mode.
        self.minimumDelay: Optional[TimeValue] = None

        # AUTOSAR COM allows configuring statically two different transmission modes for each I-PDU (True and False). The Transmission Mode Selector evaluates the conditions for a subset of signals and decides the transmission mode. It is possible to switch between the transmission modes during runtime.
        self.transmissionModeDeclaration: Optional[TransmissionModeDeclaration] = None

    def getMinimumDelay(self) -> Optional[TimeValue]:
        """
        Minimum Delay in seconds between successive transmissions of this I-PDU, independent of the Transmission Mode.
        """
        return self.minimumDelay

    def setMinimumDelay(self, value: Optional[TimeValue]) -> "IPduTiming":
        """
        Minimum Delay in seconds between successive transmissions of this I-PDU, independent of the Transmission Mode.
        A None value is a no-op and does not overwrite an existing minimumDelay.
        """
        if value is not None:
            self.minimumDelay = value
        return self

    def getTransmissionModeDeclaration(self) -> Optional[TransmissionModeDeclaration]:
        """
        AUTOSAR COM allows configuring statically two different transmission modes for each I-PDU (True and False). The Transmission Mode Selector evaluates the conditions for a subset of signals and decides the transmission mode. It is possible to switch between the transmission modes during runtime.
        """
        return self.transmissionModeDeclaration

    def setTransmissionModeDeclaration(self, value: Optional[TransmissionModeDeclaration]) -> "IPduTiming":
        """
        AUTOSAR COM allows configuring statically two different transmission modes for each I-PDU (True and False). The Transmission Mode Selector evaluates the conditions for a subset of signals and decides the transmission mode. It is possible to switch between the transmission modes during runtime.
        A None value is a no-op and does not overwrite an existing transmissionModeDeclaration.
        """
        if value is not None:
            self.transmissionModeDeclaration = value
        return self


class ISignalIPdu(IPdu):
    """
    Represents the IPdus handled by Com. The ISignalIPdu assembled and disassembled in AUTOSAR COM consists of one or more signals. In case no multiplexing is performed this IPdu is routed to/from the Interface Layer. A maximum of one dynamic length signal per IPdu is allowed.
    """

    # ISignalIPdu method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.19, p.342
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getIPduTimingSpecification  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setIPduTimingSpecification  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getISignalToPduMappings     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] createISignalToPduMappings  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getUnusedBitPattern         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setUnusedBitPattern         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Timing specification for Com IPdus (Transmission Modes). This information is mandatory for the sender in a System Extract. This information may be omitted on receivers in a System Extract. atpVariation: The timing of a Pdu can vary. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=iPduTimingSpecification, iPduTiming Specification.variationPoint.shortLabel vh.latestBindingTime=postBuild
        self.iPduTimingSpecification: Optional[IPduTiming] = None

        # Definition of SignalToIPduMappings included in the Signal IPdu. atpVariation: The content of a PDU can be variable. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=iSignalToPduMapping.shortName, iSignalTo PduMapping.variationPoint.shortLabel vh.latestBindingTime=postBuild
        self.iSignalToPduMappings: List[ISignalToIPduMapping] = []

        # AUTOSAR COM and AUTOSAR IPDUM are filling not used areas of an IPDU with this bit-pattern. This attribute is mandatory to avoid undefined behavior. This byte-pattern will be repeated throughout the IPdu.
        self.unusedBitPattern: Optional[Integer] = None

    def getIPduTimingSpecification(self) -> Optional[IPduTiming]:
        """
        Timing specification for Com IPdus (Transmission Modes). This information is mandatory for the sender in a System Extract. This information may be omitted on receivers in a System Extract. atpVariation: The timing of a Pdu can vary. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=iPduTimingSpecification, iPduTiming Specification.variationPoint.shortLabel vh.latestBindingTime=postBuild
        """
        return self.iPduTimingSpecification

    def setIPduTimingSpecification(self, value: Optional[IPduTiming]) -> "ISignalIPdu":
        """
        Timing specification for Com IPdus (Transmission Modes). This information is mandatory for the sender in a System Extract. This information may be omitted on receivers in a System Extract. atpVariation: The timing of a Pdu can vary. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=iPduTimingSpecification, iPduTiming Specification.variationPoint.shortLabel vh.latestBindingTime=postBuild
        A None value is a no-op and does not overwrite an existing iPduTimingSpecification.
        """
        if value is not None:
            self.iPduTimingSpecification = value
        return self

    def getISignalToPduMappings(self) -> List[ISignalToIPduMapping]:
        """
        Definition of SignalToIPduMappings included in the Signal IPdu. atpVariation: The content of a PDU can be variable. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=iSignalToPduMapping.shortName, iSignalTo PduMapping.variationPoint.shortLabel vh.latestBindingTime=postBuild
        """
        return self.iSignalToPduMappings

    def createISignalToPduMappings(self, short_name: str) -> ISignalToIPduMapping:
        """
        Definition of SignalToIPduMappings included in the Signal IPdu. atpVariation: The content of a PDU can be variable. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=iSignalToPduMapping.shortName, iSignalTo PduMapping.variationPoint.shortLabel vh.latestBindingTime=postBuild
        """
        if not self.IsElementExists(short_name, ISignalToIPduMapping):
            mapping = ISignalToIPduMapping(self, short_name)
            self.addElement(mapping)
            self.iSignalToPduMappings.append(mapping)
        return self.getElement(short_name, ISignalToIPduMapping)

    def getUnusedBitPattern(self) -> Optional[Integer]:
        """
        AUTOSAR COM and AUTOSAR IPDUM are filling not used areas of an IPDU with this bit-pattern. This attribute is mandatory to avoid undefined behavior. This byte-pattern will be repeated throughout the IPdu.
        """
        return self.unusedBitPattern

    def setUnusedBitPattern(self, value: Optional[Integer]) -> "ISignalIPdu":
        """
        AUTOSAR COM and AUTOSAR IPDUM are filling not used areas of an IPDU with this bit-pattern. This attribute is mandatory to avoid undefined behavior. This byte-pattern will be repeated throughout the IPdu.
        A None value is a no-op and does not overwrite an existing unusedBitPattern.
        """
        if value is not None:
            self.unusedBitPattern = value
        return self


class ISignalTypeEnum(AREnum):
    """
    This enumeration defines ISignal types that are used for derivation of the ComSignalType in the COM configuration.
    """

    # ISignalTypeEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.9, p.322
    # Spec verified: R23-11
    # (no methods)

    # ISignal shall be interpreted as an array (UINT8_N, UINT8_DYN) Tags: atp.EnumerationLiteralIndex=0
    ARRAY = "array"

    # ISignal shall be interpreted as a primitive type (e.g. UINT_8, SINT_32) Tags: atp.EnumerationLiteralIndex=1
    PRIMITIVE = "primitive"

    def __init__(self):
        super().__init__(
            (
                ISignalTypeEnum.ARRAY,
                ISignalTypeEnum.PRIMITIVE,
            )
        )


class ISignalProps(ARObject):
    """
    Additional ISignal properties that may be stored in different files.
    """

    # ISignalProps method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.10, p.323
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                                         [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getHandleOutOfRange                             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setHandleOutOfRange                             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        """
        Initializes the ISignalProps.
        """
        super().__init__()

        # This attribute defines the outOfRangeHandling for received and sent signals.
        self.handleOutOfRange: Optional[HandleOutOfRangeEnum] = None

    def getHandleOutOfRange(self) -> Optional[HandleOutOfRangeEnum]:
        """
        This attribute defines the outOfRangeHandling for received and sent signals.
        """
        return self.handleOutOfRange

    def setHandleOutOfRange(self, value: Optional[HandleOutOfRangeEnum]) -> "ISignalProps":
        """
        This attribute defines the outOfRangeHandling for received and sent signals.
        A None value is a no-op and does not overwrite an existing handleOutOfRange.
        """
        if value is not None:
            self.handleOutOfRange = value
        return self


class ISignal(FibexElement):
    """
    Signal of the Interaction Layer. The RTE supports a "signal fan-out" where the same System Signal is sent in different SignalIPdus to multiple receivers. To support the RTE "signal fan-out" each SignalIPdu contains ISignals. If the same System Signal is to be mapped into several SignalIPdus there is one ISignal needed for each ISignalToIPduMapping. ISignals describe the Interface between the Precompile configured RTE and the potentially Postbuild configured Com Stack (see ECUC Parameter Mapping). In case of the SystemSignalGroup an ISignal shall be created for each SystemSignal contained in the SystemSignalGroup.
    """

    # ISignal method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.7, p.321
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                                         [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getDataTransformationRef                         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setDataTransformationRef                         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getDataTypePolicy                                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setDataTypePolicy                                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getInitValue                                     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setInitValue                                     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getISignalProps                                  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setISignalProps                                  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getISignalType                                   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setISignalType                                   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getLength                                        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setLength                                        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getNetworkRepresentationProps                    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setNetworkRepresentationProps                    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSystemSignalRef                               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSystemSignalRef                               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTimeoutSubstitutionValue                      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setTimeoutSubstitutionValue                      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] addTransformationISignalProps                    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTransformationISignalProps                    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the ISignal.
        """
        super().__init__(parent, short_name)

        # Optional reference to a DataTransformation which represents the transformer chain that is used to transform the data that shall be placed inside this ISignal.
        self.dataTransformationRef: Optional[RefType] = None

        # With the aggregation of SwDataDefProps an ISignal specifies how it is represented on the network. This representation follows a particular policy. Note that this causes some redundancy which is intended and can be used to support flexible development methodology as well as subsequent integrity checks. If the policy "networkRepresentationFromComSpec" is chosen the network representation from the ComSpec that is aggregated by the PortPrototype shall be used. If the "override" policy is chosen the requirements specified in the PortInterface and in the ComSpec are not fulfilled by the networkRepresentationProps. In case the System Description doesn't use a complete Software Component Description (VFB View) the "legacy" policy can be chosen.
        self.dataTypePolicy: Optional[DataTypePolicyEnum] = None

        # Optional definition of a ISignal's initValue in case the System Description doesn't use a complete Software Component Description (VFB View). This supports the inclusion of legacy system signals. This value can be used to configure the Signal's "Init Value". If a full DataMapping exist for the SystemSignal this information may be available from a configured SenderComSpec and ReceiverComSpec. In this case the initvalues in SenderComSpec and/or ReceiverComSpec override this optional value specification. Further restrictions apply from the RTE specification.
        self.initValue: Optional[ValueSpecification] = None

        # Additional optional ISignal properties that may be stored in different files.
        self.iSignalProps: Optional[ISignalProps] = None

        # This attribute defines whether this iSignal is an array that results in a UINT8_N / UINT8_DYN ComSignalType in the COM configuration or a primitive type.
        self.iSignalType: Optional[ISignalTypeEnum] = None

        # Size of the signal in bits. The size needs to be derived from the mapped VariableDataPrototype according to the mapping of primitive DataTypes to BaseTypes as used in the RTE. Indicates maximum size for dynamic length signals. The ISignal length of zero bits is allowed.
        self.length: Optional[UnlimitedInteger] = None

        # Specification of the actual network representation. The usage of SwDataDefProps for this purpose is restricted to the attributes compuMethod and baseType. The optional baseType attributes "memAllignment" and "byteOrder" shall not be used. The attribute "dataTypePolicy" in the SystemTemplate element defines whether this network representation shall be ignored and the information shall be taken over from the network representation of the ComSpec. If "override" is chosen by the system integrator the network representation can violate against the requirements defined in the PortInterface and in the network representation of the ComSpec. In case that the System Description doesn't use a complete Software Component Description (VFB View) this element is used to configure "ComSignalDataInvalidValue" and the Data Semantics.
        self.networkRepresentationProps: Optional[SwDataDefProps] = None

        # Reference to the System Signal that is supposed to be transmitted in the ISignal.
        self.systemSignalRef: Optional[RefType] = None

        # Defines and enables the ComTimeoutSubstituition for this ISignal.
        self.timeoutSubstitutionValue: Optional[ValueSpecification] = None

        # A transformer chain consists of an ordered list of transformers. The ISignal specific configuration properties for each transformer are defined in the TransformationISignalProps class. The transformer configuration properties that are common for all ISignals are described in the TransformationTechnology class.
        self.transformationISignalProps: List[TransformationISignalProps] = []

    def getDataTransformationRef(self) -> Optional[RefType]:
        """
        Optional reference to a DataTransformation which represents the transformer chain that is used to transform the data that shall be placed inside this ISignal.
        """
        return self.dataTransformationRef

    def setDataTransformationRef(self, value: Optional[RefType]) -> "ISignal":
        """
        Optional reference to a DataTransformation which represents the transformer chain that is used to transform the data that shall be placed inside this ISignal.
        A None value is a no-op and does not overwrite an existing dataTransformationRef.
        """
        if value is not None:
            self.dataTransformationRef = value
        return self

    def getDataTypePolicy(self) -> Optional[DataTypePolicyEnum]:
        """
        With the aggregation of SwDataDefProps an ISignal specifies how it is represented on the network. This representation follows a particular policy. Note that this causes some redundancy which is intended and can be used to support flexible development methodology as well as subsequent integrity checks. If the policy "networkRepresentationFromComSpec" is chosen the network representation from the ComSpec that is aggregated by the PortPrototype shall be used. If the "override" policy is chosen the requirements specified in the PortInterface and in the ComSpec are not fulfilled by the networkRepresentationProps. In case the System Description doesn't use a complete Software Component Description (VFB View) the "legacy" policy can be chosen.
        """
        return self.dataTypePolicy

    def setDataTypePolicy(self, value: Optional[DataTypePolicyEnum]) -> "ISignal":
        """
        With the aggregation of SwDataDefProps an ISignal specifies how it is represented on the network. This representation follows a particular policy. Note that this causes some redundancy which is intended and can be used to support flexible development methodology as well as subsequent integrity checks. If the policy "networkRepresentationFromComSpec" is chosen the network representation from the ComSpec that is aggregated by the PortPrototype shall be used. If the "override" policy is chosen the requirements specified in the PortInterface and in the ComSpec are not fulfilled by the networkRepresentationProps. In case the System Description doesn't use a complete Software Component Description (VFB View) the "legacy" policy can be chosen.
        A None value is a no-op and does not overwrite an existing dataTypePolicy.
        """
        if value is not None:
            self.dataTypePolicy = value
        return self

    def getInitValue(self) -> Optional[ValueSpecification]:
        """
        Optional definition of a ISignal's initValue in case the System Description doesn't use a complete Software Component Description (VFB View). This supports the inclusion of legacy system signals. This value can be used to configure the Signal's "Init Value". If a full DataMapping exist for the SystemSignal this information may be available from a configured SenderComSpec and ReceiverComSpec. In this case the initvalues in SenderComSpec and/or ReceiverComSpec override this optional value specification. Further restrictions apply from the RTE specification.
        """
        return self.initValue

    def setInitValue(self, value: Optional[ValueSpecification]) -> "ISignal":
        """
        Optional definition of a ISignal's initValue in case the System Description doesn't use a complete Software Component Description (VFB View). This supports the inclusion of legacy system signals. This value can be used to configure the Signal's "Init Value". If a full DataMapping exist for the SystemSignal this information may be available from a configured SenderComSpec and ReceiverComSpec. In this case the initvalues in SenderComSpec and/or ReceiverComSpec override this optional value specification. Further restrictions apply from the RTE specification.
        A None value is a no-op and does not overwrite an existing initValue.
        """
        if value is not None:
            self.initValue = value
        return self

    def getISignalProps(self) -> Optional[ISignalProps]:
        """
        Additional optional ISignal properties that may be stored in different files.
        """
        return self.iSignalProps

    def setISignalProps(self, value: Optional[ISignalProps]) -> "ISignal":
        """
        Additional optional ISignal properties that may be stored in different files.
        A None value is a no-op and does not overwrite an existing iSignalProps.
        """
        if value is not None:
            self.iSignalProps = value
        return self

    def getISignalType(self) -> Optional[ISignalTypeEnum]:
        """
        This attribute defines whether this iSignal is an array that results in a UINT8_N / UINT8_DYN ComSignalType in the COM configuration or a primitive type.
        """
        return self.iSignalType

    def setISignalType(self, value: Optional[ISignalTypeEnum]) -> "ISignal":
        """
        This attribute defines whether this iSignal is an array that results in a UINT8_N / UINT8_DYN ComSignalType in the COM configuration or a primitive type.
        A None value is a no-op and does not overwrite an existing iSignalType.
        """
        if value is not None:
            self.iSignalType = value
        return self

    def getLength(self) -> Optional[UnlimitedInteger]:
        """
        Size of the signal in bits. The size needs to be derived from the mapped VariableDataPrototype according to the mapping of primitive DataTypes to BaseTypes as used in the RTE. Indicates maximum size for dynamic length signals. The ISignal length of zero bits is allowed.
        """
        return self.length

    def setLength(self, value: Optional[UnlimitedInteger]) -> "ISignal":
        """
        Size of the signal in bits. The size needs to be derived from the mapped VariableDataPrototype according to the mapping of primitive DataTypes to BaseTypes as used in the RTE. Indicates maximum size for dynamic length signals. The ISignal length of zero bits is allowed.
        A None value is a no-op and does not overwrite an existing length.
        """
        if value is not None:
            self.length = value
        return self

    def getNetworkRepresentationProps(self) -> Optional[SwDataDefProps]:
        """
        Specification of the actual network representation. The usage of SwDataDefProps for this purpose is restricted to the attributes compuMethod and baseType. The optional baseType attributes "memAllignment" and "byteOrder" shall not be used. The attribute "dataTypePolicy" in the SystemTemplate element defines whether this network representation shall be ignored and the information shall be taken over from the network representation of the ComSpec. If "override" is chosen by the system integrator the network representation can violate against the requirements defined in the PortInterface and in the network representation of the ComSpec. In case that the System Description doesn't use a complete Software Component Description (VFB View) this element is used to configure "ComSignalDataInvalidValue" and the Data Semantics.
        """
        return self.networkRepresentationProps

    def setNetworkRepresentationProps(self, value: Optional[SwDataDefProps]) -> "ISignal":
        """
        Specification of the actual network representation. The usage of SwDataDefProps for this purpose is restricted to the attributes compuMethod and baseType. The optional baseType attributes "memAllignment" and "byteOrder" shall not be used. The attribute "dataTypePolicy" in the SystemTemplate element defines whether this network representation shall be ignored and the information shall be taken over from the network representation of the ComSpec. If "override" is chosen by the system integrator the network representation can violate against the requirements defined in the PortInterface and in the network representation of the ComSpec. In case that the System Description doesn't use a complete Software Component Description (VFB View) this element is used to configure "ComSignalDataInvalidValue" and the Data Semantics.
        A None value is a no-op and does not overwrite an existing networkRepresentationProps.
        """
        if value is not None:
            self.networkRepresentationProps = value
        return self

    def getSystemSignalRef(self) -> Optional[RefType]:
        """
        Reference to the System Signal that is supposed to be transmitted in the ISignal.
        """
        return self.systemSignalRef

    def setSystemSignalRef(self, value: Optional[RefType]) -> "ISignal":
        """
        Reference to the System Signal that is supposed to be transmitted in the ISignal.
        A None value is a no-op and does not overwrite an existing systemSignalRef.
        """
        if value is not None:
            self.systemSignalRef = value
        return self

    def getTimeoutSubstitutionValue(self) -> Optional[ValueSpecification]:
        """
        Defines and enables the ComTimeoutSubstituition for this ISignal.
        """
        return self.timeoutSubstitutionValue

    def setTimeoutSubstitutionValue(self, value: Optional[ValueSpecification]) -> "ISignal":
        """
        Defines and enables the ComTimeoutSubstituition for this ISignal.
        A None value is a no-op and does not overwrite an existing timeoutSubstitutionValue.
        """
        if value is not None:
            self.timeoutSubstitutionValue = value
        return self

    def addTransformationISignalProps(self, value: Optional[TransformationISignalProps]) -> "ISignal":
        """
        A transformer chain consists of an ordered list of transformers. The ISignal specific configuration properties for each transformer are defined in the TransformationISignalProps class. The transformer configuration properties that are common for all ISignals are described in the TransformationTechnology class.
        """
        if value is not None:
            self.transformationISignalProps.append(value)
        return self

    def getTransformationISignalProps(self) -> List[TransformationISignalProps]:
        """
        A transformer chain consists of an ordered list of transformers. The ISignal specific configuration properties for each transformer are defined in the TransformationISignalProps class. The transformer configuration properties that are common for all ISignals are described in the TransformationTechnology class.
        """
        return self.transformationISignalProps


class PduTriggering(Identifiable, VariationPointCapable):
    """
    The PduTriggering describes on which channel the IPdu is transmitted. The Pdu routing by the PduR is only allowed for subclasses of IPdu. Depending on its relation to entities such channels and clusters it can be unambiguously deduced whether a fan-out is handled by the Pdu router or the Bus Interface. If the fan-out is specified between different clusters it shall be handled by the Pdu Router. If the fan-out is specified between different channels of the same cluster it shall be handled by the Bus Interface.
    """

    # PduTriggering method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.31, p.349
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getIPduRef                   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setIPduRef                   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getIPduPortRefs              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addIPduPortRef               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getISignalTriggeringRefs     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addISignalTriggeringRef      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSecOcCryptoMappingRef     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSecOcCryptoMappingRef     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTriggerIPduSendConditions [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addTriggerIPduSendCondition  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Reference to the Pdu for which the PduTriggering is defined. One I-Pdu can be triggered on different channels (PduR fan-out). The Pdu routing by the PduR is only allowed for subclasses of IPdu. Nevertheless is the reference to the Pdu element necessary since the PduTriggering element is also used to specify the sending and receiving connections to Ecu Ports.
        self.iPduRef: Optional[RefType] = None

        # References to the IPduPort on every ECU of the system which sends and/or receives the I-PDU. References for both the sender and the receiver side shall be included when the system is completely defined.
        self.iPduPortRefs: List[RefType] = []

        # This reference provides the relationship to the ISignalTriggerings that are implemented by the PduTriggering. The reference is optional since no ISignalTriggering can be defined for DCM and Multiplexed Pdus. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=iSignalTriggering.iSignalTriggering, iSignalTriggering.variationPoint.shortLabel vh.latestBindingTime=postBuild
        self.iSignalTriggeringRefs: List[RefType] = []

        # This reference identifies the crypto profile applicable to the usage (send, receive) of the also referenced Secured IPdu. Obviously, this reference is only applicable if the Pdutriggering also references a SecuredIPdu in the role iPdu.
        self.secOcCryptoMappingRef: Optional[RefType] = None

        # Defines the trigger for the Com_TriggerIPDUSend API call. Only if all defined TriggerIPduSendConditions evaluate to true (AND associated) the Com_TriggerIPDUSend API shall be called.
        self.triggerIPduSendConditions: List[TriggerIPduSendCondition] = []

    def getIPduRef(self) -> Optional[RefType]:
        """
        Reference to the Pdu for which the PduTriggering is defined. One I-Pdu can be triggered on different channels (PduR fan-out). The Pdu routing by the PduR is only allowed for subclasses of IPdu. Nevertheless is the reference to the Pdu element necessary since the PduTriggering element is also used to specify the sending and receiving connections to Ecu Ports.
        """
        return self.iPduRef

    def setIPduRef(self, value: Optional[RefType]) -> "PduTriggering":
        """
        Reference to the Pdu for which the PduTriggering is defined. One I-Pdu can be triggered on different channels (PduR fan-out). The Pdu routing by the PduR is only allowed for subclasses of IPdu. Nevertheless is the reference to the Pdu element necessary since the PduTriggering element is also used to specify the sending and receiving connections to Ecu Ports.
        A None value is a no-op and does not overwrite an existing iPduRef.
        """
        if value is not None:
            self.iPduRef = value
        return self

    def getIPduPortRefs(self) -> List[RefType]:
        """
        References to the IPduPort on every ECU of the system which sends and/or receives the I-PDU. References for both the sender and the receiver side shall be included when the system is completely defined.
        """
        return self.iPduPortRefs

    def addIPduPortRef(self, value: Optional[RefType]) -> "PduTriggering":
        """
        References to the IPduPort on every ECU of the system which sends and/or receives the I-PDU. References for both the sender and the receiver side shall be included when the system is completely defined.
        """
        if value is not None:
            self.iPduPortRefs.append(value)
        return self

    def getISignalTriggeringRefs(self) -> List[RefType]:
        """
        This reference provides the relationship to the ISignalTriggerings that are implemented by the PduTriggering. The reference is optional since no ISignalTriggering can be defined for DCM and Multiplexed Pdus. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=iSignalTriggering.iSignalTriggering, iSignalTriggering.variationPoint.shortLabel vh.latestBindingTime=postBuild
        """
        return self.iSignalTriggeringRefs

    def addISignalTriggeringRef(self, value: Optional[RefType]) -> "PduTriggering":
        """
        This reference provides the relationship to the ISignalTriggerings that are implemented by the PduTriggering. The reference is optional since no ISignalTriggering can be defined for DCM and Multiplexed Pdus. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=iSignalTriggering.iSignalTriggering, iSignalTriggering.variationPoint.shortLabel vh.latestBindingTime=postBuild
        """
        if value is not None:
            self.iSignalTriggeringRefs.append(value)
        return self

    def getSecOcCryptoMappingRef(self) -> Optional[RefType]:
        """
        This reference identifies the crypto profile applicable to the usage (send, receive) of the also referenced Secured IPdu. Obviously, this reference is only applicable if the Pdutriggering also references a SecuredIPdu in the role iPdu.
        """
        return self.secOcCryptoMappingRef

    def setSecOcCryptoMappingRef(self, value: Optional[RefType]) -> "PduTriggering":
        """
        This reference identifies the crypto profile applicable to the usage (send, receive) of the also referenced Secured IPdu. Obviously, this reference is only applicable if the Pdutriggering also references a SecuredIPdu in the role iPdu.
        A None value is a no-op and does not overwrite an existing secOcCryptoMappingRef.
        """
        if value is not None:
            self.secOcCryptoMappingRef = value
        return self

    def getTriggerIPduSendConditions(self) -> List[TriggerIPduSendCondition]:
        """
        Defines the trigger for the Com_TriggerIPDUSend API call. Only if all defined TriggerIPduSendConditions evaluate to true (AND associated) the Com_TriggerIPDUSend API shall be called.
        """
        return self.triggerIPduSendConditions

    def addTriggerIPduSendCondition(self, value: Optional[TriggerIPduSendCondition]) -> "PduTriggering":
        """
        Defines the trigger for the Com_TriggerIPDUSend API call. Only if all defined TriggerIPduSendConditions evaluate to true (AND associated) the Com_TriggerIPDUSend API shall be called.
        """
        if value is not None:
            self.triggerIPduSendConditions.append(value)
        return self


class FrameTriggering(Identifiable, VariationPointCapable, ABC):
    """
    Abstract base class for frame triggering mechanisms, defining
    common properties for triggering frame transmission and reception
    including frame references and port references.
    """

    # FrameTriggering method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getFrameRef                  [x] impl  [ ] docstring  [ ] test
    # [ ] setFrameRef                  [x] impl  [ ] docstring  [ ] test
    # [ ] getFramePortRefs             [x] impl  [ ] docstring  [ ] test
    # [ ] addFramePortRef              [x] impl  [ ] docstring  [ ] test
    # [ ] getPduTriggeringRefs         [x] impl  [ ] docstring  [ ] test
    # [ ] addPduTriggeringRef          [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is FrameTriggering:
            raise TypeError("FrameTriggering is an abstract class.")

        super().__init__(parent, short_name)

        # One frame can be triggered several times, e.g. on different channels. If a frame has no frame triggering, it won't be sent at all. A frame triggering has assigned exactly one frame, which it triggers.
        self.frameRef: Optional[RefType] = None

        # References to the FramePort on every ECU of the system which sends and/or receives the frame. References for both the sender and the receiver side shall be included when the system is completely defined.
        self.framePortRefs: List[RefType] = []
        self.pduTriggeringRefs: List[RefType] = []

    def getFrameRef(self) -> Optional[RefType]:
        return self.frameRef

    def setFrameRef(self, value: Optional[RefType]) -> "FrameTriggering":
        # One frame can be triggered several times, e.g. on different channels. If a frame has no frame triggering, it won't be sent at all. A frame triggering has assigned exactly one frame, which it triggers.
        # A None value is a no-op and does not overwrite an existing frameRef.
        if value is not None:
            self.frameRef = value
        return self

    def getFramePortRefs(self) -> List[RefType]:
        return self.framePortRefs

    def addFramePortRef(self, value: RefType):
        self.framePortRefs.append(value)
        return self

    def getPduTriggeringRefs(self) -> RefType:
        return self.pduTriggeringRefs

    def addPduTriggeringRef(self, value: RefType):
        self.pduTriggeringRefs.append(value)
        return self


class SystemSignal(ARElement):
    """
    Represents a system signal in the AUTOSAR system, defining
    dynamic length properties and physical properties for
    system-level signal communication.
    """

    # SystemSignal method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getDynamicLength             [x] impl  [ ] docstring  [ ] test
    # [ ] setDynamicLength             [x] impl  [ ] docstring  [ ] test
    # [ ] getPhysicalProps             [x] impl  [ ] docstring  [ ] test
    # [ ] setPhysicalProps             [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        self.dynamicLength: Boolean = None
        self.physicalProps: SwDataDefProps = None

    def getDynamicLength(self):
        return self.dynamicLength

    def setDynamicLength(self, value):
        self.dynamicLength = value
        return self

    def getPhysicalProps(self):
        return self.physicalProps

    def setPhysicalProps(self, value):
        self.physicalProps = value
        return self


class SystemSignalGroup(ARElement):
    """
    A signal group refers to a set of signals that shall always be kept together. A signal group is used to guarantee the atomic transfer of AUTOSAR composite data types. The SystemSignalGroup defines a signal grouping on VFB level. On cluster level the Signal grouping is described by the ISignalGroup element. Tags: atp.recommendedPackage=SystemSignalGroups
    """

    # SystemSignalGroup method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.13, p.324
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                      [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getSystemSignalRefs           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addSystemSignalRef            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTransformingSystemSignalRef [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setTransformingSystemSignalRef [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Reference to a set of SystemSignals that shall always be kept together.
        self.systemSignalRefs: List[RefType] = []

        # Optional reference to the SystemSignal which shall contain the transformed (linear) data.
        self.transformingSystemSignalRef: Optional[RefType] = None

    def getSystemSignalRefs(self) -> List[RefType]:
        """
        Reference to a set of SystemSignals that shall always be kept together.
        """
        return self.systemSignalRefs

    def addSystemSignalRef(self, value: RefType) -> "SystemSignalGroup":
        """
        Reference to a set of SystemSignals that shall always be kept together.
        """
        self.systemSignalRefs.append(value)
        return self

    def getTransformingSystemSignalRef(self) -> Optional[RefType]:
        """
        Optional reference to the SystemSignal which shall contain the transformed (linear) data.
        """
        return self.transformingSystemSignalRef

    def setTransformingSystemSignalRef(self, value: Optional[RefType]) -> "SystemSignalGroup":
        """
        Optional reference to the SystemSignal which shall contain the transformed (linear) data.
        A None value is a no-op and does not overwrite an existing transformingSystemSignalRef.
        """
        if value is not None:
            self.transformingSystemSignalRef = value
        return self


class ISignalTriggering(Identifiable, VariationPointCapable):
    """
    A ISignalTriggering allows an assignment of ISignals to physical channels.
    """

    # ISignalTriggering method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.16, p.330
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getISignalRef             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setISignalRef             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getISignalGroupRef        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setISignalGroupRef        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] addISignalPortRef         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getISignalPortRefs        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This reference shall be used if an ISignal is transported on the PhysicalChannel. This reference forms an XOR relationship with the ISignalTriggering-ISignalGroup reference.
        self.iSignalRef: Optional[RefType] = None

        # This reference shall be used if an ISignalGroup is transported on the PhysicalChannel. This reference forms an XOR relationship with the ISignal Triggering-ISignal reference.
        self.iSignalGroupRef: Optional[RefType] = None

        # References to the ISignalPort on every ECU of the system which sends and/or receives the ISignal. References for both the sender and the receiver side shall be included when the system is completely defined.
        self.iSignalPortRefs: List[RefType] = []

    def getISignalRef(self) -> Optional[RefType]:
        """
        This reference shall be used if an ISignal is transported on the PhysicalChannel. This reference forms an XOR relationship with the ISignalTriggering-ISignalGroup reference.
        """
        return self.iSignalRef

    def setISignalRef(self, value: Optional[RefType]) -> "ISignalTriggering":
        """
        This reference shall be used if an ISignal is transported on the PhysicalChannel. This reference forms an XOR relationship with the ISignalTriggering-ISignalGroup reference.
        A None value is a no-op and does not overwrite an existing iSignalRef.
        """
        if value is not None:
            self.iSignalRef = value
        return self

    def getISignalGroupRef(self) -> Optional[RefType]:
        """
        This reference shall be used if an ISignalGroup is transported on the PhysicalChannel. This reference forms an XOR relationship with the ISignal Triggering-ISignal reference.
        """
        return self.iSignalGroupRef

    def setISignalGroupRef(self, value: Optional[RefType]) -> "ISignalTriggering":
        """
        This reference shall be used if an ISignalGroup is transported on the PhysicalChannel. This reference forms an XOR relationship with the ISignal Triggering-ISignal reference.
        A None value is a no-op and does not overwrite an existing iSignalGroupRef.
        """
        if value is not None:
            self.iSignalGroupRef = value
        return self

    def addISignalPortRef(self, value: Optional[RefType]) -> "ISignalTriggering":
        """
        References to the ISignalPort on every ECU of the system which sends and/or receives the ISignal. References for both the sender and the receiver side shall be included when the system is completely defined.
        """
        if value is not None:
            self.iSignalPortRefs.append(value)
        return self

    def getISignalPortRefs(self) -> List[RefType]:
        """
        References to the ISignalPort on every ECU of the system which sends and/or receives the ISignal. References for both the sender and the receiver side shall be included when the system is completely defined.
        """
        return self.iSignalPortRefs


class SegmentPosition(ARObject):
    """
    Defines the position of a segment within a communication element,
    specifying byte order, length, and position properties for
    segmented communication.
    """

    # SegmentPosition method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getSegmentByteOrder          [x] impl  [ ] docstring  [ ] test
    # [ ] setSegmentByteOrder          [x] impl  [ ] docstring  [ ] test
    # [ ] getSegmentLength             [x] impl  [ ] docstring  [ ] test
    # [ ] setSegmentLength             [x] impl  [ ] docstring  [ ] test
    # [ ] getSegmentPosition           [x] impl  [ ] docstring  [ ] test
    # [ ] setSegmentPosition           [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()

        self.segmentByteOrder: ByteOrderEnum = None
        self.segmentLength: Integer = None
        self.segmentPosition: Integer = None

    def getSegmentByteOrder(self):
        return self.segmentByteOrder

    def setSegmentByteOrder(self, value):
        if value is not None:
            self.segmentByteOrder = value
        return self

    def getSegmentLength(self):
        return self.segmentLength

    def setSegmentLength(self, value):
        if value is not None:
            self.segmentLength = value
        return self

    def getSegmentPosition(self):
        return self.segmentPosition

    def setSegmentPosition(self, value):
        if value is not None:
            self.segmentPosition = value
        return self


class MultiplexedPart(ARObject, ABC):
    """
    Abstract base class for multiplexed communication parts, defining
    common properties for dynamic and static multiplexed communication
    segments including segment positions.
    """

    # MultiplexedPart method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getSegmentPositions          [x] impl  [ ] docstring  [ ] test
    # [ ] addSegmentPosition           [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        if type(self) is MultiplexedPart:
            raise TypeError("MultiplexedPart is an abstract class.")

        super().__init__()

        self.segmentPositions = []  # type: List[SegmentPosition]

    def getSegmentPositions(self):
        return self.segmentPositions

    def addSegmentPosition(self, value):
        if value is not None:
            self.segmentPositions.append(value)
        return self


class StaticPart(MultiplexedPart, VariationPointCapable):
    """
    Defines a static part of multiplexed communication, specifying
    Interaction Protocol Data Unit (IPDU) references for fixed
    segments in multiplexed communication.
    """

    # StaticPart method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getIPduRef                   [x] impl  [ ] docstring  [ ] test
    # [ ] setIPduRef                   [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()

        self.iPduRef = None  # type: RefType

    def getIPduRef(self):
        return self.iPduRef

    def setIPduRef(self, value):
        if value is not None:
            self.iPduRef = value
        return self


class DynamicPartAlternative(ARObject):
    """
    Defines an alternative for dynamic parts in multiplexed communication,
    specifying selector field codes, initial dynamic part properties,
    and Interaction Protocol Data Unit (IPDU) references.
    """

    # DynamicPartAlternative method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getInitialDynamicPart        [x] impl  [ ] docstring  [ ] test
    # [ ] setInitialDynamicPart        [x] impl  [ ] docstring  [ ] test
    # [ ] getIPduRef                   [x] impl  [ ] docstring  [ ] test
    # [ ] setIPduRef                   [x] impl  [ ] docstring  [ ] test
    # [ ] getSelectorFieldCode         [x] impl  [ ] docstring  [ ] test
    # [ ] setSelectorFieldCode         [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()

        self.initialDynamicPart = None  # type: Boolean
        self.iPduRef = None  # type: RefType
        self.selectorFieldCode = None  # type: Integer

    def getInitialDynamicPart(self):
        return self.initialDynamicPart

    def setInitialDynamicPart(self, value):
        if value is not None:
            self.initialDynamicPart = value
        return self

    def getIPduRef(self):
        return self.iPduRef

    def setIPduRef(self, value):
        if value is not None:
            self.iPduRef = value
        return self

    def getSelectorFieldCode(self):
        return self.selectorFieldCode

    def setSelectorFieldCode(self, value):
        if value is not None:
            self.selectorFieldCode = value
        return self


class DynamicPart(MultiplexedPart, VariationPointCapable):
    """
    Defines a dynamic part of multiplexed communication, specifying
    alternatives for variable segments in multiplexed communication
    based on selector field values.
    """

    # DynamicPart method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getDynamicPartAlternatives   [x] impl  [ ] docstring  [ ] test
    # [ ] addDynamicPartAlternative    [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()

        self.dynamicPartAlternatives = []  # type: List[DynamicPartAlternative]

    def getDynamicPartAlternatives(self):
        return self.dynamicPartAlternatives

    def addDynamicPartAlternative(self, value):
        if value is not None:
            self.dynamicPartAlternatives.append(value)
        return self


class MultiplexedIPdu(IPdu):
    """
    Represents a multiplexed Interaction Protocol Data Unit (IPDU)
    with dynamic and static parts, defining selector field properties
    and trigger modes for multiplexed communication.
    """

    # MultiplexedIPdu method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getDynamicPart               [x] impl  [ ] docstring  [ ] test
    # [ ] setDynamicPart               [x] impl  [ ] docstring  [ ] test
    # [ ] getSelectorFieldByteOrder    [x] impl  [ ] docstring  [ ] test
    # [ ] setSelectorFieldByteOrder    [x] impl  [ ] docstring  [ ] test
    # [ ] getSelectorFieldLength       [x] impl  [ ] docstring  [ ] test
    # [ ] setSelectorFieldLength       [x] impl  [ ] docstring  [ ] test
    # [ ] getSelectorFieldStartPosition [x] impl  [ ] docstring  [ ] test
    # [ ] setSelectorFieldStartPosition [x] impl  [ ] docstring  [ ] test
    # [ ] getStaticPart                [x] impl  [ ] docstring  [ ] test
    # [ ] setStaticPart                [x] impl  [ ] docstring  [ ] test
    # [ ] getTriggerMode               [x] impl  [ ] docstring  [ ] test
    # [ ] setTriggerMode               [x] impl  [ ] docstring  [ ] test
    # [ ] getUnusedBitPattern          [x] impl  [ ] docstring  [ ] test
    # [ ] setUnusedBitPattern          [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        self.dynamicPart = None  # type: DynamicPart
        self.selectorFieldByteOrder = None  # type: ByteOrderEnum
        self.selectorFieldLength = None  # type: Integer
        self.selectorFieldStartPosition = None  # type: Integer
        self.staticPart = None  # type: StaticPart
        self.triggerMode = None  # type: TriggerMode
        self.unusedBitPattern = None  # type: Integer

    def getDynamicPart(self):
        return self.dynamicPart

    def setDynamicPart(self, value):
        if value is not None:
            self.dynamicPart = value
        return self

    def getSelectorFieldByteOrder(self):
        return self.selectorFieldByteOrder

    def setSelectorFieldByteOrder(self, value):
        if value is not None:
            self.selectorFieldByteOrder = value
        return self

    def getSelectorFieldLength(self):
        return self.selectorFieldLength

    def setSelectorFieldLength(self, value):
        if value is not None:
            self.selectorFieldLength = value
        return self

    def getSelectorFieldStartPosition(self):
        return self.selectorFieldStartPosition

    def setSelectorFieldStartPosition(self, value):
        if value is not None:
            self.selectorFieldStartPosition = value
        return self

    def getStaticPart(self):
        return self.staticPart

    def setStaticPart(self, value):
        if value is not None:
            self.staticPart = value
        return self

    def getTriggerMode(self):
        return self.triggerMode

    def setTriggerMode(self, value):
        if value is not None:
            self.triggerMode = value
        return self

    def getUnusedBitPattern(self):
        return self.unusedBitPattern

    def setUnusedBitPattern(self, value):
        if value is not None:
            self.unusedBitPattern = value
        return self


class GeneralPurposePdu(Pdu):
    """
    Represents a general-purpose Protocol Data Unit (PDU) for flexible
    communication patterns that don't fit into specific PDU categories.
    """

    # GeneralPurposePdu method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class GeneralPurposeIPdu(IPdu):
    """
    Represents a general-purpose Interaction Protocol Data Unit (IPDU) for flexible
    interaction-based communication patterns that don't fit into specific IPDU categories.
    """

    # GeneralPurposeIPdu method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class SecureCommunicationPropsSet(FibexElement):
    """
    Collection of properties used to configure SecuredIPdus.
    """

    # SecureCommunicationPropsSet method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.45, p.370
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                                         [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] createSecureCommunicationAuthenticationProps     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getAuthenticationProps                           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] createSecureCommunicationFreshnessProps          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getFreshnessProps                                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the SecureCommunicationPropsSet.
        """
        super().__init__(parent, short_name)

        # Authentication properties used to configure Secured IPdus.
        self.authenticationProps: List[SecureCommunicationAuthenticationProps] = []

        # Freshness properties used to configure SecuredIPdus.
        self.freshnessProps: List[SecureCommunicationFreshnessProps] = []

    def createSecureCommunicationAuthenticationProps(self, short_name: str) -> SecureCommunicationAuthenticationProps:
        """
        Authentication properties used to configure Secured IPdus.
        """
        if not self.IsElementExists(short_name, SecureCommunicationAuthenticationProps):
            props = SecureCommunicationAuthenticationProps(self, short_name)
            self.addElement(props)
            self.authenticationProps.append(props)
        return self.getElement(short_name, SecureCommunicationAuthenticationProps)

    def getAuthenticationProps(self) -> List[SecureCommunicationAuthenticationProps]:
        """
        Authentication properties used to configure Secured IPdus.
        """
        return self.authenticationProps

    def createSecureCommunicationFreshnessProps(self, short_name: str) -> SecureCommunicationFreshnessProps:
        """
        Freshness properties used to configure SecuredIPdus.
        """
        if not self.IsElementExists(short_name, SecureCommunicationFreshnessProps):
            props = SecureCommunicationFreshnessProps(self, short_name)
            self.addElement(props)
            self.freshnessProps.append(props)
        return self.getElement(short_name, SecureCommunicationFreshnessProps)

    def getFreshnessProps(self) -> List[SecureCommunicationFreshnessProps]:
        """
        Freshness properties used to configure SecuredIPdus.
        """
        return self.freshnessProps


class UserDefinedPdu(Pdu):
    """
    Allows to describe PDU-based communication over Complex Communication Drivers.

    If a new BSW module is added above the BusIf (e.g. a new Nm module) then this
    Pdu element shall be used to describe the communication.

    Requirements:
        atp.recommendedPackage=Pdus

    Attributes:
        cddType: Optional attribute that defines the CDD (Complex Device Driver)
            that transmits or receives the UserDefinedPdu. If several CDDs are
            defined this attribute is used to distinguish between them.
    """

    # UserDefinedPdu method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getCddType                   [x] impl  [ ] docstring  [ ] test
    # [ ] setCddType                   [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)
        self.cddType: String = None

    def getCddType(self):
        return self.cddType

    def setCddType(self, value):
        self.cddType = value
        return self


class UserDefinedIPdu(IPdu):
    """
    Represents a user-defined Interaction Protocol Data Unit (IPDU) that allows for custom
    interaction-based communication patterns defined by the user rather than following standard IPDU types.
    """

    # UserDefinedIPdu method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getCddType                   [x] impl  [ ] docstring  [ ] test
    # [ ] setCddType                   [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)
        self.cddType: ARLiteral = None

    def getCddType(self):
        return self.cddType

    def setCddType(self, value):
        self.cddType = value
        return self


class SecureCommunicationAuthenticationProps(Identifiable):
    """
    Authentication properties used to configure SecuredIPdus.
    """

    # SecureCommunicationAuthenticationProps method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.47, p.371
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                       [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getAuthInfoTxLength            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setAuthInfoTxLength            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the SecureCommunicationAuthenticationProps.
        """
        super().__init__(parent, short_name)

        # This attribute defines the length in bits of the authentication code to be included in the payload of the authenticated Pdu.
        self.authInfoTxLength: Optional[PositiveInteger] = None

    def getAuthInfoTxLength(self) -> Optional[PositiveInteger]:
        """
        This attribute defines the length in bits of the authentication code to be included in the payload of the authenticated Pdu.
        """
        return self.authInfoTxLength

    def setAuthInfoTxLength(self, value: Optional[PositiveInteger]) -> "SecureCommunicationAuthenticationProps":
        """
        This attribute defines the length in bits of the authentication code to be included in the payload of the authenticated Pdu.
        A None value is a no-op and does not overwrite an existing authInfoTxLength.
        """
        if value is not None:
            self.authInfoTxLength = value
        return self


class SecureCommunicationFreshnessProps(Identifiable):
    """
    Freshness properties used to configure SecuredIPdus.
    """

    # SecureCommunicationFreshnessProps method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.46, p.371
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                                   [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getFreshnessCounterSyncAttempts            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setFreshnessCounterSyncAttempts            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getFreshnessTimestampTimePeriodFactor      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setFreshnessTimestampTimePeriodFactor      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getFreshnessValueLength                    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setFreshnessValueLength                    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getFreshnessValueTxLength                  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setFreshnessValueTxLength                  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getUseFreshnessTimestamp                   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setUseFreshnessTimestamp                   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the SecureCommunicationFreshnessProps.
        """
        super().__init__(parent, short_name)

        # This attribute defines the number of Freshness Counter re-synchronization attempts when a verification failed for a Secured I-PDU. If the value is zero, there will be no additional verification attempt to synchronize with a potentially better fitting Freshness Counter value. This attribute is only applicable if useFreshnessTimestamp is FALSE.
        self.freshnessCounterSyncAttempts: Optional[PositiveInteger] = None

        # This attribute defines a factor that specifies the time period for the Freshness Timestamp. It holds a multiplication factor that specifies the concrete meaning of a Freshness Timestamp increment by one on basis of microseconds.
        self.freshnessTimestampTimePeriodFactor: Optional[PositiveInteger] = None

        # This attribute defines the complete length in bits of the Freshness Value. As long as the key doesn't change the counter shall not overflow. The length of the counter shall be determined based on the expected life time of the corresponding key and frequency of usage of the counter.
        self.freshnessValueLength: Optional[PositiveInteger] = None

        # This attribute defines the length in bits of the Freshness Value to be included in the payload of the Secured I-PDU. This length is specific to the least significant bits of the complete Freshness Counter. If the attribute is 0 no Freshness Value is included in the Secured I-PDU.
        self.freshnessValueTxLength: Optional[PositiveInteger] = None

        # This attribute specifies whether the Freshness Value is generated through individual Freshness Counters or by a Timestamps. The value is set to TRUE when Timestamps are used.
        self.useFreshnessTimestamp: Optional[Boolean] = None

    def getFreshnessCounterSyncAttempts(self) -> Optional[PositiveInteger]:
        """
        This attribute defines the number of Freshness Counter re-synchronization attempts when a verification failed for a Secured I-PDU. If the value is zero, there will be no additional verification attempt to synchronize with a potentially better fitting Freshness Counter value. This attribute is only applicable if useFreshnessTimestamp is FALSE.
        """
        return self.freshnessCounterSyncAttempts

    def setFreshnessCounterSyncAttempts(self, value: Optional[PositiveInteger]) -> "SecureCommunicationFreshnessProps":
        """
        This attribute defines the number of Freshness Counter re-synchronization attempts when a verification failed for a Secured I-PDU. If the value is zero, there will be no additional verification attempt to synchronize with a potentially better fitting Freshness Counter value. This attribute is only applicable if useFreshnessTimestamp is FALSE.
        A None value is a no-op and does not overwrite an existing freshnessCounterSyncAttempts.
        """
        if value is not None:
            self.freshnessCounterSyncAttempts = value
        return self

    def getFreshnessTimestampTimePeriodFactor(self) -> Optional[PositiveInteger]:
        """
        This attribute defines a factor that specifies the time period for the Freshness Timestamp. It holds a multiplication factor that specifies the concrete meaning of a Freshness Timestamp increment by one on basis of microseconds.
        """
        return self.freshnessTimestampTimePeriodFactor

    def setFreshnessTimestampTimePeriodFactor(self, value: Optional[PositiveInteger]) -> "SecureCommunicationFreshnessProps":
        """
        This attribute defines a factor that specifies the time period for the Freshness Timestamp. It holds a multiplication factor that specifies the concrete meaning of a Freshness Timestamp increment by one on basis of microseconds.
        A None value is a no-op and does not overwrite an existing freshnessTimestampTimePeriodFactor.
        """
        if value is not None:
            self.freshnessTimestampTimePeriodFactor = value
        return self

    def getFreshnessValueLength(self) -> Optional[PositiveInteger]:
        """
        This attribute defines the complete length in bits of the Freshness Value. As long as the key doesn't change the counter shall not overflow. The length of the counter shall be determined based on the expected life time of the corresponding key and frequency of usage of the counter.
        """
        return self.freshnessValueLength

    def setFreshnessValueLength(self, value: Optional[PositiveInteger]) -> "SecureCommunicationFreshnessProps":
        """
        This attribute defines the complete length in bits of the Freshness Value. As long as the key doesn't change the counter shall not overflow. The length of the counter shall be determined based on the expected life time of the corresponding key and frequency of usage of the counter.
        A None value is a no-op and does not overwrite an existing freshnessValueLength.
        """
        if value is not None:
            self.freshnessValueLength = value
        return self

    def getFreshnessValueTxLength(self) -> Optional[PositiveInteger]:
        """
        This attribute defines the length in bits of the Freshness Value to be included in the payload of the Secured I-PDU. This length is specific to the least significant bits of the complete Freshness Counter. If the attribute is 0 no Freshness Value is included in the Secured I-PDU.
        """
        return self.freshnessValueTxLength

    def setFreshnessValueTxLength(self, value: Optional[PositiveInteger]) -> "SecureCommunicationFreshnessProps":
        """
        This attribute defines the length in bits of the Freshness Value to be included in the payload of the Secured I-PDU. This length is specific to the least significant bits of the complete Freshness Counter. If the attribute is 0 no Freshness Value is included in the Secured I-PDU.
        A None value is a no-op and does not overwrite an existing freshnessValueTxLength.
        """
        if value is not None:
            self.freshnessValueTxLength = value
        return self

    def getUseFreshnessTimestamp(self) -> Optional[Boolean]:
        """
        This attribute specifies whether the Freshness Value is generated through individual Freshness Counters or by a Timestamps. The value is set to TRUE when Timestamps are used.
        """
        return self.useFreshnessTimestamp

    def setUseFreshnessTimestamp(self, value: Optional[Boolean]) -> "SecureCommunicationFreshnessProps":
        """
        This attribute specifies whether the Freshness Value is generated through individual Freshness Counters or by a Timestamps. The value is set to TRUE when Timestamps are used.
        A None value is a no-op and does not overwrite an existing useFreshnessTimestamp.
        """
        if value is not None:
            self.useFreshnessTimestamp = value
        return self


class CommunicationDirectionType(AREnum):
    """
    Enumeration defining communication direction types,
    specifying whether communication is inbound or outbound.
    """

    # CommunicationDirectionType method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test

    ENUM_IN = "in"
    ENUM_OUT = "out"

    def __init__(self):
        super().__init__([CommunicationDirectionType.ENUM_IN, CommunicationDirectionType.ENUM_OUT])


class FramePort(CommConnectorPort):
    """
    Represents a frame port for communication connectors,
    handling frame-based communication at the connector level.
    """

    # FramePort method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class IPduSignalProcessingEnum(AREnum):
    """
    Definition of signal processing modes.
    """

    # IPduSignalProcessingEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.4, p.305
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # (no methods) — enum value form serialized on IPduPort.iPduSignalProcessing
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    # The signal indications / confirmations are deferred. Tags: atp.EnumerationLiteralIndex=0
    ENUM_DEFERRED = "deferred"

    # The signal indications / confirmations are performed. Tags: atp.EnumerationLiteralIndex=1
    ENUM_IMMEDIATE = "immediate"

    def __init__(self):
        super().__init__([IPduSignalProcessingEnum.ENUM_DEFERRED, IPduSignalProcessingEnum.ENUM_IMMEDIATE])


class IPduPort(CommConnectorPort):
    """
    Connectors reception or send port on the referenced channel referenced by a PduTriggering.

    [constr_3137] IPduPort.rxSecurityVerification is configurable on the receiver side: The IPduPort.rxSecurityVerification attribute shall only be used in IPduPorts with the communicationDirection = in.
    [constr_3138] IPduPort.rxSecurityVerification validness: The IPduPort.rxSecurityVerification information is only valid for SecuredIPdus.
    [constr_3337] IPduPort.useAuthDataFreshness is configurable on the receiver side: The IPduPort.useAuthDataFreshness attribute shall only be used in IPduPorts with the communicationDirection = in.
    [constr_3338] IPduPort.useAuthDataFreshness validness: The IPduPort.useAuthDataFreshness information is only valid for SecuredIPdus.
    """

    # IPduPort method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.3, p.304
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getIPduSignalProcessing      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setIPduSignalProcessing      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getRxSecurityVerification    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setRxSecurityVerification    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTimestampRxAcceptanceWindow [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setTimestampRxAcceptanceWindow [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getUseAuthDataFreshness      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setUseAuthDataFreshness      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Definition of the two signal processing modes Immediate and Deferred for both Tx and Rx IPdus.
        self.iPduSignalProcessing: Optional[IPduSignalProcessingEnum] = None

        # This attribute defines the bypassing of signature authentication or MAC verification in the receiving ECU. If not defined or set to true the signature authentication or MAC verification shall be performed for the SecuredIPdu. If set to false the signature authentication or MAC verification shall not be performed for the SecuredIPdu.
        self.rxSecurityVerification: Optional[Boolean] = None

        # This attribute is used to define the maximum allowed deviation in seconds from the expected timestamp for which a SecuredIPdu is still deemed authentic. Please note that this attribute is for documentation only to allow the configuration of required freshness value manager and no upstream mapping is defined for it.
        self.timestampRxAcceptanceWindow: Optional[TimeValue] = None

        # This attribute describes whether a part of AuthenticPdu contained in a SecuredIPdu shall be passed on to the SWC that verifies and generates the Freshness. The part of the Authentic-PDU is defined by the authData FreshnessStartPosition and authDataFreshnessLength.
        self.useAuthDataFreshness: Optional[Boolean] = None

    def getIPduSignalProcessing(self) -> Optional[IPduSignalProcessingEnum]:
        """
        Definition of the two signal processing modes Immediate and Deferred for both Tx and Rx IPdus.
        """
        return self.iPduSignalProcessing

    def setIPduSignalProcessing(self, value: Optional[IPduSignalProcessingEnum]) -> "IPduPort":
        """
        Definition of the two signal processing modes Immediate and Deferred for both Tx and Rx IPdus.
        A None value is a no-op and does not overwrite an existing iPduSignalProcessing.
        """
        if value is not None:
            self.iPduSignalProcessing = value
        return self

    def getRxSecurityVerification(self) -> Optional[Boolean]:
        """
        This attribute defines the bypassing of signature authentication or MAC verification in the receiving ECU. If not defined or set to true the signature authentication or MAC verification shall be performed for the SecuredIPdu. If set to false the signature authentication or MAC verification shall not be performed for the SecuredIPdu.
        """
        return self.rxSecurityVerification

    def setRxSecurityVerification(self, value: Optional[Boolean]) -> "IPduPort":
        """
        This attribute defines the bypassing of signature authentication or MAC verification in the receiving ECU. If not defined or set to true the signature authentication or MAC verification shall be performed for the SecuredIPdu. If set to false the signature authentication or MAC verification shall not be performed for the SecuredIPdu.
        A None value is a no-op and does not overwrite an existing rxSecurityVerification.
        """
        if value is not None:
            self.rxSecurityVerification = value
        return self

    def getTimestampRxAcceptanceWindow(self) -> Optional[TimeValue]:
        """
        This attribute is used to define the maximum allowed deviation in seconds from the expected timestamp for which a SecuredIPdu is still deemed authentic. Please note that this attribute is for documentation only to allow the configuration of required freshness value manager and no upstream mapping is defined for it.
        """
        return self.timestampRxAcceptanceWindow

    def setTimestampRxAcceptanceWindow(self, value: Optional[TimeValue]) -> "IPduPort":
        """
        This attribute is used to define the maximum allowed deviation in seconds from the expected timestamp for which a SecuredIPdu is still deemed authentic. Please note that this attribute is for documentation only to allow the configuration of required freshness value manager and no upstream mapping is defined for it.
        A None value is a no-op and does not overwrite an existing timestampRxAcceptanceWindow.
        """
        if value is not None:
            self.timestampRxAcceptanceWindow = value
        return self

    def getUseAuthDataFreshness(self) -> Optional[Boolean]:
        """
        This attribute describes whether a part of AuthenticPdu contained in a SecuredIPdu shall be passed on to the SWC that verifies and generates the Freshness. The part of the Authentic-PDU is defined by the authData FreshnessStartPosition and authDataFreshnessLength.
        """
        return self.useAuthDataFreshness

    def setUseAuthDataFreshness(self, value: Optional[Boolean]) -> "IPduPort":
        """
        This attribute describes whether a part of AuthenticPdu contained in a SecuredIPdu shall be passed on to the SWC that verifies and generates the Freshness. The part of the Authentic-PDU is defined by the authData FreshnessStartPosition and authDataFreshnessLength.
        A None value is a no-op and does not overwrite an existing useAuthDataFreshness.
        """
        if value is not None:
            self.useAuthDataFreshness = value
        return self


class ISignalPort(CommConnectorPort):
    """
    Represents an interaction signal port for communication connectors,
    handling interaction signal communication with filtering,
    timeout, and validity handling properties.
    """

    # ISignalPort method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getDataFilter                [x] impl  [ ] docstring  [ ] test
    # [ ] setDataFilter                [x] impl  [ ] docstring  [ ] test
    # [ ] getDdsQosProfileRef          [x] impl  [ ] docstring  [ ] test
    # [ ] setDdsQosProfileRef          [x] impl  [ ] docstring  [ ] test
    # [ ] getFirstTimeout              [x] impl  [ ] docstring  [ ] test
    # [ ] setFirstTimeout              [x] impl  [ ] docstring  [ ] test
    # [ ] getHandleInvalid             [x] impl  [ ] docstring  [ ] test
    # [ ] setHandleInvalid             [x] impl  [ ] docstring  [ ] test
    # [ ] getTimeout                   [x] impl  [ ] docstring  [ ] test
    # [ ] setTimeout                   [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.dataFilter: DataFilter = None
        self.ddsQosProfileRef: RefType = None
        self.firstTimeout: TimeValue = None
        self.handleInvalid = None
        self.timeout: TimeValue = None

    def getDataFilter(self):
        return self.dataFilter

    def setDataFilter(self, value):
        if value is not None:
            self.dataFilter = value
        return self

    def getDdsQosProfileRef(self):
        return self.ddsQosProfileRef

    def setDdsQosProfileRef(self, value):
        if value is not None:
            self.ddsQosProfileRef = value
        return self

    def getFirstTimeout(self):
        return self.firstTimeout

    def setFirstTimeout(self, value):
        if value is not None:
            self.firstTimeout = value
        return self

    def getHandleInvalid(self):
        return self.handleInvalid

    def setHandleInvalid(self, value):
        if value is not None:
            self.handleInvalid = value
        return self

    def getTimeout(self):
        return self.timeout

    def setTimeout(self, value):
        if value is not None:
            self.timeout = value
        return self
