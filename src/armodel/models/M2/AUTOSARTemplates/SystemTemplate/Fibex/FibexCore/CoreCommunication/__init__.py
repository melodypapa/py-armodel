from __future__ import annotations
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.StereotypeMixins import VariationPointCapable

from abc import ABC
from typing import List, Optional, TYPE_CHECKING, cast
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable, Describable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AREnum, ARLiteral, PositiveInteger, Boolean, ByteOrderEnum
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Integer, RefType, String
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import TimeValue, UnlimitedInteger
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import SwDataDefProps
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Filter import DataFilter
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.Timing import (
    TransmissionModeDeclaration,
    TriggerIPduSendCondition,
    AbsoluteTolerance as AbsoluteTolerance,
    RelativeTolerance as RelativeTolerance,
)  # noqa: F401
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore import FibexElement
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import CommConnectorPort
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import PduCollectionTriggerEnum

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.CommonStructure import ValueSpecification
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import HandleOutOfRangeEnum
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import HandleInvalidEnum
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

    def setPackingByteOrder(self, value: Optional[ByteOrderEnum]) -> PduToFrameMapping:
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

    def setPduRef(self, value: Optional[RefType]) -> PduToFrameMapping:
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

    def setStartPosition(self, value: Optional[Integer]) -> PduToFrameMapping:
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

    def setUpdateIndicationBitPosition(self, value: Optional[Integer]) -> PduToFrameMapping:
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

    def setFrameLength(self, value: Optional[Integer]) -> Frame:
        """
        The used length (in bytes) of the referencing frame. Should not be confused with a static byte length reserved for each frame by some platforms (e.g. FlexRay). The frameLength of zero bytes is allowed. Please consider also TPS_SYST_02255.
        A None value is a no-op and does not overwrite an existing frameLength.
        """
        if value is not None:
            self.frameLength = value
        return self

    def createPduToFrameMapping(self, short_name: str) -> PduToFrameMapping:
        if not self.IsReferrableElementExists(short_name, PduToFrameMapping):
            mapping = PduToFrameMapping(self, short_name)
            self.addReferrableElement(mapping)
            self.pduToFrameMappings.append(mapping)
        return cast(PduToFrameMapping, self.getReferrableElement(short_name, PduToFrameMapping))

    def getPduToFrameMappings(self) -> List[PduToFrameMapping]:
        return list(sorted([a for a in self.referrableElements if isinstance(a, PduToFrameMapping)], key=lambda o: o.short_name))


class ContainedIPduCollectionSemanticsEnum(AREnum):
    """
    Defines the collection semantics for ContainedIPdus.
    """

    # ContainedIPduCollectionSemanticsEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.40, p.357 (R23-11)
    # Spec verified: R23-11 (2026-09-26, user 9b confirmation)
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods) — enum value form serialized on ContainedIPduProps.collectionSemantics
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # The ContainedIPdu data will be fetched via TriggerTransmit just before the transmission executes. Tags: atp.EnumerationLiteralIndex=0
    LAST_IS_BEST = "LAST-IS-BEST"

    # The ContainedIPdu data will instantly be stored to the ContainerIPdu in the context of the Transmit API. Tags: atp.EnumerationLiteralIndex=1
    QUEUED = "QUEUED"

    def __init__(self):
        super().__init__([ContainedIPduCollectionSemanticsEnum.LAST_IS_BEST, ContainedIPduCollectionSemanticsEnum.QUEUED])


class ContainerIPduTriggerEnum(AREnum):
    """
    Defines when the transmission of the ContainerIPdu shall be requested.
    """

    # ContainerIPduTriggerEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.36, p.354 (R23-11)
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods) — enum value form serialized on ContainerIPdu.containerTrigger
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # Defines that the transmission of the ContainerIPdu shall be requested when the default trigger conditions apply (e.g. timeout of threshold). Tags: atp.EnumerationLiteralIndex=0
    DEFAULT_TRIGGER = "DEFAULT-TRIGGER"

    # Defines that the transmission of the ContainerIPdu shall be requested right after the first Contained IPdu was put into the ContainerIPdu. Tags: atp.EnumerationLiteralIndex=1
    FIRST_CONTAINED_TRIGGER = "FIRST-CONTAINED-TRIGGER"

    def __init__(self):
        super().__init__([ContainerIPduTriggerEnum.DEFAULT_TRIGGER, ContainerIPduTriggerEnum.FIRST_CONTAINED_TRIGGER])


class ContainerIPduHeaderTypeEnum(AREnum):
    """
    Is used to define the header type and size of ContainerIPdus. The header size includes the header id and the length information.
    """

    # ContainerIPduHeaderTypeEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.37, p.355 (R23-11)
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods) — enum value form serialized on ContainerIPdu.headerType
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # Header size is 64 bit: • Header Id 32 bit • Dlc 32 bit Tags: atp.EnumerationLiteralIndex=0
    LONG_HEADER = "LONG-HEADER"

    # No Header is used and the location of each containedPdu in the ContainerPdu is statically configured. Tags: atp.EnumerationLiteralIndex=2
    NO_HEADER = "NO-HEADER"

    # Header size is 32 bit: • Header Id 24 bit • Dlc 8 bit. Tags: atp.EnumerationLiteralIndex=1
    SHORT_HEADER = "SHORT-HEADER"

    def __init__(self):
        super().__init__([ContainerIPduHeaderTypeEnum.LONG_HEADER, ContainerIPduHeaderTypeEnum.NO_HEADER, ContainerIPduHeaderTypeEnum.SHORT_HEADER])


class RxAcceptContainedIPduEnum(AREnum):
    """
    Defines whether this ContainerIPdu has a fixed set of containedIPdus assigned for reception.
    """

    # RxAcceptContainedIPduEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.38, p.355 (R23-11)
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods) — enum value form serialized on ContainerIPdu.rxAcceptContainedIPdu
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # No fixed set of containedIPdus is defined for reception, any known containedIPdu (based on header Id) shall be expected within this ContainerIPdu. Tags: atp.EnumerationLiteralIndex=0
    ACCEPT_ALL = "ACCEPT-ALL"

    # A fixed set of containedIPdus is defined for reception. Only these assigned containedIPdus (based on headerId) are expected in this ContainerIPdu. If a not assigned containedIPdu is received within this ContainerIPdu this containedIPdu is discarded. Tags: atp.EnumerationLiteralIndex=1
    ACCEPT_CONFIGURED = "ACCEPT-CONFIGURED"

    def __init__(self):
        super().__init__([RxAcceptContainedIPduEnum.ACCEPT_ALL, RxAcceptContainedIPduEnum.ACCEPT_CONFIGURED])


class ContainedIPduProps(ARObject):
    """
    Defines the aspects of an IPdu which can be collected inside a ContainerIPdu.

    [constr_9202] Existence of ContainedIPduProps.collectionSemantics: For each ContainedIPduProps, the attribute collectionSemantics shall exist at the time when the System Description is complete.
    [constr_5268] Existence of ContainedIPduProps.containedPduTriggering reference: If a ContainedIPduProps is aggregated at the ContainerIPdu in the role ContainerIPdu.containedIPduTriggeringProps then the reference ContainedIPduProps.containedPduTriggering shall exist.
    [constr_5269] Exclusion of ContainedIPduProps.containedPduTriggering reference: If a ContainedIPduProps is aggregated at the IPdu in the role IPdu.containedIPduProps then the reference ContainedIPduProps.containedPduTriggering shall NOT exist.
    """

    # ContainedIPduProps method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.39, p.356 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                             [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getCollectionSemantics               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setCollectionSemantics               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getContainedPduTriggeringRef         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setContainedPduTriggeringRef         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getHeaderIdLongHeader                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setHeaderIdLongHeader                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getHeaderIdShortHeader               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setHeaderIdShortHeader               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getOffset                            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setOffset                            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getPriority                          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setPriority                          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTimeout                           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTimeout                           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTrigger                           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTrigger                           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getUpdateIndicationBitPosition       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setUpdateIndicationBitPosition       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # Defines whether this ContainedIPdu shall be collected using a last-is-best or queued semantics.
        self.collectionSemantics: Optional[ContainedIPduCollectionSemanticsEnum] = None

        # Reference to Pdu for which the ContainedIPduProps are valid.
        self.containedPduTriggeringRef: Optional[RefType] = None

        # Defines the header id this IPdu shall have in case this IPdu is put inside a ContainerIPdu with headerType = longHeader.
        self.headerIdLongHeader: Optional[PositiveInteger] = None

        # Defines the header id this IPdu shall have in case this IPdu is put inside a ContainerIPdu with headerType = shortHeader.
        self.headerIdShortHeader: Optional[PositiveInteger] = None

        # Byte offset that describes the location of the ContainedPdu in the ContainerPdu if no header is used.
        self.offset: Optional[PositiveInteger] = None

        # Defines a priority of a ContainedTxPdu. 255 represents the lowest priority and 0 represent the highest priority.
        self.priority: Optional[PositiveInteger] = None

        # Defines a IPdu specific sender timeout which can reduce the ContainerIPdu timer when this containedIPdu is put inside the ContainerIPdu. This attribute is ignored on receiver side.
        self.timeout: Optional[TimeValue] = None

        # Defines whether this IPdu does trigger the sending of the ContainerIPdu. This attribute is ignored on receiver side.
        self.trigger: Optional[PduCollectionTriggerEnum] = None

        # The updateIndicationBit specifies the bit location of ContainedIPdu Update-Bit in the Container PDU. It indicates to the receivers that the ContainedIPdu in the ContainerIPdu was updated.
        self.updateIndicationBitPosition: Optional[PositiveInteger] = None

    def getCollectionSemantics(self) -> Optional[ContainedIPduCollectionSemanticsEnum]:
        """
        Defines whether this ContainedIPdu shall be collected using a last-is-best or queued semantics.
        """
        return self.collectionSemantics

    def setCollectionSemantics(self, value: Optional[ContainedIPduCollectionSemanticsEnum]) -> ContainedIPduProps:
        """
        Defines whether this ContainedIPdu shall be collected using a last-is-best or queued semantics.
        A None value is a no-op and does not overwrite an existing collectionSemantics.
        """
        if value is not None:
            self.collectionSemantics = value
        return self

    def getContainedPduTriggeringRef(self) -> Optional[RefType]:
        """
        Reference to Pdu for which the ContainedIPduProps are valid.
        """
        return self.containedPduTriggeringRef

    def setContainedPduTriggeringRef(self, value: Optional[RefType]) -> ContainedIPduProps:
        """
        Reference to Pdu for which the ContainedIPduProps are valid.
        A None value is a no-op and does not overwrite an existing containedPduTriggeringRef.
        """
        if value is not None:
            self.containedPduTriggeringRef = value
        return self

    def getHeaderIdLongHeader(self) -> Optional[PositiveInteger]:
        """
        Defines the header id this IPdu shall have in case this IPdu is put inside a ContainerIPdu with headerType = longHeader.
        """
        return self.headerIdLongHeader

    def setHeaderIdLongHeader(self, value: Optional[PositiveInteger]) -> ContainedIPduProps:
        """
        Defines the header id this IPdu shall have in case this IPdu is put inside a ContainerIPdu with headerType = longHeader.
        A None value is a no-op and does not overwrite an existing headerIdLongHeader.
        """
        if value is not None:
            self.headerIdLongHeader = value
        return self

    def getHeaderIdShortHeader(self) -> Optional[PositiveInteger]:
        """
        Defines the header id this IPdu shall have in case this IPdu is put inside a ContainerIPdu with headerType = shortHeader.
        """
        return self.headerIdShortHeader

    def setHeaderIdShortHeader(self, value: Optional[PositiveInteger]) -> ContainedIPduProps:
        """
        Defines the header id this IPdu shall have in case this IPdu is put inside a ContainerIPdu with headerType = shortHeader.
        A None value is a no-op and does not overwrite an existing headerIdShortHeader.
        """
        if value is not None:
            self.headerIdShortHeader = value
        return self

    def getOffset(self) -> Optional[PositiveInteger]:
        """
        Byte offset that describes the location of the ContainedPdu in the ContainerPdu if no header is used.
        """
        return self.offset

    def setOffset(self, value: Optional[PositiveInteger]) -> ContainedIPduProps:
        """
        Byte offset that describes the location of the ContainedPdu in the ContainerPdu if no header is used.
        A None value is a no-op and does not overwrite an existing offset.
        """
        if value is not None:
            self.offset = value
        return self

    def getPriority(self) -> Optional[PositiveInteger]:
        """
        Defines a priority of a ContainedTxPdu. 255 represents the lowest priority and 0 represent the highest priority.
        """
        return self.priority

    def setPriority(self, value: Optional[PositiveInteger]) -> ContainedIPduProps:
        """
        Defines a priority of a ContainedTxPdu. 255 represents the lowest priority and 0 represent the highest priority.
        A None value is a no-op and does not overwrite an existing priority.
        """
        if value is not None:
            self.priority = value
        return self

    def getTimeout(self) -> Optional[TimeValue]:
        """
        Defines a IPdu specific sender timeout which can reduce the ContainerIPdu timer when this containedIPdu is put inside the ContainerIPdu. This attribute is ignored on receiver side.
        """
        return self.timeout

    def setTimeout(self, value: Optional[TimeValue]) -> ContainedIPduProps:
        """
        Defines a IPdu specific sender timeout which can reduce the ContainerIPdu timer when this containedIPdu is put inside the ContainerIPdu. This attribute is ignored on receiver side.
        A None value is a no-op and does not overwrite an existing timeout.
        """
        if value is not None:
            self.timeout = value
        return self

    def getTrigger(self) -> Optional[PduCollectionTriggerEnum]:
        """
        Defines whether this IPdu does trigger the sending of the ContainerIPdu. This attribute is ignored on receiver side.
        """
        return self.trigger

    def setTrigger(self, value: Optional[PduCollectionTriggerEnum]) -> ContainedIPduProps:
        """
        Defines whether this IPdu does trigger the sending of the ContainerIPdu. This attribute is ignored on receiver side.
        A None value is a no-op and does not overwrite an existing trigger.
        """
        if value is not None:
            self.trigger = value
        return self

    def getUpdateIndicationBitPosition(self) -> Optional[PositiveInteger]:
        """
        The updateIndicationBit specifies the bit location of ContainedIPdu Update-Bit in the Container PDU. It indicates to the receivers that the ContainedIPdu in the ContainerIPdu was updated.
        """
        return self.updateIndicationBitPosition

    def setUpdateIndicationBitPosition(self, value: Optional[PositiveInteger]) -> ContainedIPduProps:
        """
        The updateIndicationBit specifies the bit location of ContainedIPdu Update-Bit in the Container PDU. It indicates to the receivers that the ContainedIPdu in the ContainerIPdu was updated.
        A None value is a no-op and does not overwrite an existing updateIndicationBitPosition.
        """
        if value is not None:
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

    def setComBasedSignalGroupTransformationRef(self, value: Optional[RefType]) -> ISignalGroup:
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

    def addISignalRef(self, value: RefType) -> ISignalGroup:
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

    def setSystemSignalGroupRef(self, value: Optional[RefType]) -> ISignalGroup:
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

    def addTransformationISignalProps(self, value: TransformationISignalProps) -> ISignalGroup:
        """
        A transformer chain consists of an ordered list of transformers. The ISignalGroup specific configuration properties for each transformer are defined in the TransformationISignalProps class. The transformer configuration properties that are common for all ISignal Groups are described in the TransformationTechnology class. Stereotypes: atpSplitable Tags: atp.Splitkey=transformationISignalProps
        """
        self.transformationISignalProps.append(value)
        return self


class ISignalIPduGroup(FibexElement):
    """
    The AUTOSAR COM Layer is able to start and to stop sending and receiving configurable groups of I-Pdus during runtime. An ISignalIPduGroup contains either ISignalIPdus or ISignalIPduGroups. Tags: atp.recommendedPackage=ISignaliPduGroup
    """

    # ISignalIPduGroup method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.32, p.351 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                         [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getCommunicationDirection        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setCommunicationDirection        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getCommunicationMode             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setCommunicationMode             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getContainedISignalIPduGroupRefs [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addContainedISignalIPduGroupRef  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getISignalIPduRefs               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addISignalIPduRef                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getNmPduRefs                     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addNmPduRef                      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This attribute determines in which direction IPdus that are contained in this IPduGroup will be transmitted (communication direction can be either In or Out).
        self.communicationDirection: Optional[CommunicationDirectionType] = None

        # This attribute defines the use-case for this ISignalIPduGroup (e.g. diagnostic, debugging etc.). For example, in a diagnostic mode all IPdus - which are not involved in diagnostic - are disabled. The use cases are not limited to a fixed enumeration and can be specified as a string.
        self.communicationMode: Optional[String] = None

        # An I-Pdu group can be included in other I-Pdu groups. Contained I-Pdu groups shall not be referenced by the EcuInstance.
        self.containedISignalIPduGroupRefs: List[RefType] = []

        # Reference to a set of Signal I-Pdus, which are contained in the ISignal I-Pdu Group. atpVariation: The content of a ISignal I-Pdu group can vary (->vehicle modes). Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=iSignalIPdu.iSignalIPdu, iSignalIPdu.variationPoint.shortLabel vh.latestBindingTime=postBuild
        self.iSignalIPduRefs: List[RefType] = []

        # Reference to a set of NmPdus with NmUserData, which are contained in the ISignalIPduGroup. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=nmPdu.nmPdu, nmPdu.variationPoint.shortLabel vh.latestBindingTime=postBuild
        self.nmPduRefs: List[RefType] = []

    def getCommunicationDirection(self) -> Optional[CommunicationDirectionType]:
        """
        This attribute determines in which direction IPdus that are contained in this IPduGroup will be transmitted (communication direction can be either In or Out).
        """
        return self.communicationDirection

    def setCommunicationDirection(self, value: Optional[CommunicationDirectionType]) -> ISignalIPduGroup:
        """
        This attribute determines in which direction IPdus that are contained in this IPduGroup will be transmitted (communication direction can be either In or Out).
        A None value is a no-op and does not overwrite an existing communicationDirection.
        """
        if value is not None:
            self.communicationDirection = value
        return self

    def getCommunicationMode(self) -> Optional[String]:
        """
        This attribute defines the use-case for this ISignalIPduGroup (e.g. diagnostic, debugging etc.). For example, in a diagnostic mode all IPdus - which are not involved in diagnostic - are disabled. The use cases are not limited to a fixed enumeration and can be specified as a string.
        """
        return self.communicationMode

    def setCommunicationMode(self, value: Optional[String]) -> ISignalIPduGroup:
        """
        This attribute defines the use-case for this ISignalIPduGroup (e.g. diagnostic, debugging etc.). For example, in a diagnostic mode all IPdus - which are not involved in diagnostic - are disabled. The use cases are not limited to a fixed enumeration and can be specified as a string.
        A None value is a no-op and does not overwrite an existing communicationMode.
        """
        if value is not None:
            self.communicationMode = value
        return self

    def getContainedISignalIPduGroupRefs(self) -> List[RefType]:
        """
        An I-Pdu group can be included in other I-Pdu groups. Contained I-Pdu groups shall not be referenced by the EcuInstance.
        """
        return self.containedISignalIPduGroupRefs

    def addContainedISignalIPduGroupRef(self, value: Optional[RefType]) -> ISignalIPduGroup:
        """
        An I-Pdu group can be included in other I-Pdu groups. Contained I-Pdu groups shall not be referenced by the EcuInstance.
        A None value is a no-op and is not appended to containedISignalIPduGroupRefs.
        """
        if value is not None:
            self.containedISignalIPduGroupRefs.append(value)
        return self

    def getISignalIPduRefs(self) -> List[RefType]:
        """
        Reference to a set of Signal I-Pdus, which are contained in the ISignal I-Pdu Group. atpVariation: The content of a ISignal I-Pdu group can vary (->vehicle modes). Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=iSignalIPdu.iSignalIPdu, iSignalIPdu.variationPoint.shortLabel vh.latestBindingTime=postBuild
        """
        return self.iSignalIPduRefs

    def addISignalIPduRef(self, value: Optional[RefType]) -> ISignalIPduGroup:
        """
        Reference to a set of Signal I-Pdus, which are contained in the ISignal I-Pdu Group. atpVariation: The content of a ISignal I-Pdu group can vary (->vehicle modes). Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=iSignalIPdu.iSignalIPdu, iSignalIPdu.variationPoint.shortLabel vh.latestBindingTime=postBuild
        A None value is a no-op and is not appended to iSignalIPduRefs.
        """
        if value is not None:
            self.iSignalIPduRefs.append(value)
        return self

    def getNmPduRefs(self) -> List[RefType]:
        """
        Reference to a set of NmPdus with NmUserData, which are contained in the ISignalIPduGroup. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=nmPdu.nmPdu, nmPdu.variationPoint.shortLabel vh.latestBindingTime=postBuild
        """
        return self.nmPduRefs

    def addNmPduRef(self, value: Optional[RefType]) -> ISignalIPduGroup:
        """
        Reference to a set of NmPdus with NmUserData, which are contained in the ISignalIPduGroup. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=nmPdu.nmPdu, nmPdu.variationPoint.shortLabel vh.latestBindingTime=postBuild
        A None value is a no-op and is not appended to nmPduRefs.
        """
        if value is not None:
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
        self.hasDynamicLength: Optional[Boolean] = None

        # Pdu length in bytes. In case of dynamic length IPdus (containing a dynamical length signal), this value indicates the maximum data length. It should be noted that in former AUTOSAR releases (Rel 2.1, Rel 3.0, Rel 3.1, Rel 4.0 Rev. 1) this parameter was defined in bits. The Pdu length of zero bytes is allowed.
        self.length: Optional[UnlimitedInteger] = None

    def setHasDynamicLength(self, value: Optional[Boolean]) -> Pdu:
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

    def setLength(self, value: Optional[UnlimitedInteger]) -> Pdu:
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

    def setContainedIPduProps(self, value: Optional[ContainedIPduProps]) -> IPdu:
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

    def setAuthDataFreshnessLength(self, value: Optional[PositiveInteger]) -> SecureCommunicationProps:
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

    def setAuthDataFreshnessStartPosition(self, value: Optional[PositiveInteger]) -> SecureCommunicationProps:
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

    def setAuthenticationBuildAttempts(self, value: Optional[PositiveInteger]) -> SecureCommunicationProps:
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

    def setAuthenticationRetries(self, value: Optional[PositiveInteger]) -> SecureCommunicationProps:
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

    def setDataId(self, value: Optional[PositiveInteger]) -> SecureCommunicationProps:
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

    def setFreshnessValueId(self, value: Optional[PositiveInteger]) -> SecureCommunicationProps:
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

    def setMessageLinkLength(self, value: Optional[PositiveInteger]) -> SecureCommunicationProps:
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

    def setMessageLinkPosition(self, value: Optional[PositiveInteger]) -> SecureCommunicationProps:
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

    def setSecondaryFreshnessValueId(self, value: Optional[PositiveInteger]) -> SecureCommunicationProps:
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

    def setSecuredAreaLength(self, value: Optional[PositiveInteger]) -> SecureCommunicationProps:
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

    def setSecuredAreaOffset(self, value: Optional[PositiveInteger]) -> SecureCommunicationProps:
        """
        This attribute defines the start position (offset in byte) of the area within the payload Pdu which will be secured.
        A None value is a no-op and does not overwrite an existing securedAreaOffset.
        """
        if value is not None:
            self.securedAreaOffset = value
        return self


class SecuredPduHeaderEnum(AREnum):
    """
    Defines the header which will be inserted into the SecuredIPdu.
    """

    # SecuredPduHeaderEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.43, p.369 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods) — enum value form serialized on SecuredIPdu.useSecuredPduHeader
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # No header included in the SecuredPdu. Tags: atp.EnumerationLiteralIndex=0
    NO_HEADER = "NO-HEADER"

    # 8 Bit Secured I-PDU Header included in the Secured I-PDU. Tags: atp.EnumerationLiteralIndex=1
    SECURED_PDU_HEADER08_BIT = "SECURED-PDU-HEADER-08-BIT"

    # 16 Bit Secured I-PDU Header included in the Secured I-PDU. Tags: atp.EnumerationLiteralIndex=2
    SECURED_PDU_HEADER16_BIT = "SECURED-PDU-HEADER-16-BIT"

    # 32 Bit Secured I-PDU Header included in the Secured I-PDU. Tags: atp.EnumerationLiteralIndex=3
    SECURED_PDU_HEADER32_BIT = "SECURED-PDU-HEADER-32-BIT"

    def __init__(self):
        super().__init__([SecuredPduHeaderEnum.NO_HEADER, SecuredPduHeaderEnum.SECURED_PDU_HEADER08_BIT, SecuredPduHeaderEnum.SECURED_PDU_HEADER16_BIT, SecuredPduHeaderEnum.SECURED_PDU_HEADER32_BIT])


class SecuredIPdu(IPdu):
    """
    If useAsCryptographicPdu is not set or set to false this IPdu contains the payload of an Authentic IPdu supplemented by additional Authentication Information (Freshness Counter and an Authenticator). If useAsCryptographicPdu is set to true this IPdu contains the Authenticator for a payload that is transported in a separate message. The separate Authentic IPdu is described by the Pdu that is referenced with the payload reference from this SecuredIPdu. Tags: atp.recommendedPackage=Pdus
    """

    # SecuredIPdu method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.42, p.368 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__            [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getAuthenticationPropsRef       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setAuthenticationPropsRef       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDynamicRuntimeLengthHandling [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDynamicRuntimeLengthHandling [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getFreshnessPropsRef            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setFreshnessPropsRef            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getPayloadRef                   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setPayloadRef                   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSecureCommunicationProps     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSecureCommunicationProps     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getUseAsCryptographicIPdu       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setUseAsCryptographicIPdu       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getUseSecuredPduHeader          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setUseSecuredPduHeader          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Reference to authentication properties that are valid for this SecuredIPdu.
        self.authenticationPropsRef: Optional[RefType] = None

        # Defines whether the length information for handling this SecuredIPdu with SecuredIPdu.useSecuredPdu Header=noHeader is taken from the configuration or from the actually provided length information during runtime. true: SecuredIPdu length information is taken from the actually provided length information during runtime. false: SecuredIPdu length information is taken from the configuration.
        self.dynamicRuntimeLengthHandling: Optional[Boolean] = None

        # Reference to freshness properties that are valid for this SecuredIPdu.
        self.freshnessPropsRef: Optional[RefType] = None

        # Reference to a Pdu that will be protected against unauthorized manipulation and replay attacks.
        self.payloadRef: Optional[RefType] = None

        # Specific configuration properties for this SecuredIPdu.
        self.secureCommunicationProps: Optional[SecureCommunicationProps] = None

        # If this attribute is set to true the SecuredIPdu contains the Authentication Information for an AuthenticIPdu that is transmitted in a separate message. The AuthenticIPdu contains the original payload, i.e. the secured data. If this attribute is set to false this SecuredIPdu contains the payload of an Authentic IPdu supplemented by additional Authentication Information.
        self.useAsCryptographicIPdu: Optional[Boolean] = None

        # This attribute defines the size of the header which is inserted into the SecuredIPdu. If this attribute is set to anything but noHeader, the SecuredIPdu contains the Secured I-PDU Header to indicate the length of the AuthenticIPdu. The AuthenticIPdu contains the original payload, i.e. the secured data.
        self.useSecuredPduHeader: Optional[SecuredPduHeaderEnum] = None

    def getAuthenticationPropsRef(self) -> Optional[RefType]:
        """
        Reference to authentication properties that are valid for this SecuredIPdu.
        """
        return self.authenticationPropsRef

    def setAuthenticationPropsRef(self, value: Optional[RefType]) -> SecuredIPdu:
        """
        Reference to authentication properties that are valid for this SecuredIPdu.
        A None value is a no-op and does not overwrite an existing authenticationPropsRef.
        """
        if value is not None:
            self.authenticationPropsRef = value
        return self

    def getDynamicRuntimeLengthHandling(self) -> Optional[Boolean]:
        """
        Defines whether the length information for handling this SecuredIPdu with SecuredIPdu.useSecuredPdu Header=noHeader is taken from the configuration or from the actually provided length information during runtime. true: SecuredIPdu length information is taken from the actually provided length information during runtime. false: SecuredIPdu length information is taken from the configuration.
        """
        return self.dynamicRuntimeLengthHandling

    def setDynamicRuntimeLengthHandling(self, value: Optional[Boolean]) -> SecuredIPdu:
        """
        Defines whether the length information for handling this SecuredIPdu with SecuredIPdu.useSecuredPdu Header=noHeader is taken from the configuration or from the actually provided length information during runtime. true: SecuredIPdu length information is taken from the actually provided length information during runtime. false: SecuredIPdu length information is taken from the configuration.
        A None value is a no-op and does not overwrite an existing dynamicRuntimeLengthHandling.
        """
        if value is not None:
            self.dynamicRuntimeLengthHandling = value
        return self

    def getFreshnessPropsRef(self) -> Optional[RefType]:
        """
        Reference to freshness properties that are valid for this SecuredIPdu.
        """
        return self.freshnessPropsRef

    def setFreshnessPropsRef(self, value: Optional[RefType]) -> SecuredIPdu:
        """
        Reference to freshness properties that are valid for this SecuredIPdu.
        A None value is a no-op and does not overwrite an existing freshnessPropsRef.
        """
        if value is not None:
            self.freshnessPropsRef = value
        return self

    def getPayloadRef(self) -> Optional[RefType]:
        """
        Reference to a Pdu that will be protected against unauthorized manipulation and replay attacks.
        """
        return self.payloadRef

    def setPayloadRef(self, value: Optional[RefType]) -> SecuredIPdu:
        """
        Reference to a Pdu that will be protected against unauthorized manipulation and replay attacks.
        A None value is a no-op and does not overwrite an existing payloadRef.
        """
        if value is not None:
            self.payloadRef = value
        return self

    def getSecureCommunicationProps(self) -> Optional[SecureCommunicationProps]:
        """
        Specific configuration properties for this SecuredIPdu.
        """
        return self.secureCommunicationProps

    def setSecureCommunicationProps(self, value: Optional[SecureCommunicationProps]) -> SecuredIPdu:
        """
        Specific configuration properties for this SecuredIPdu.
        A None value is a no-op and does not overwrite an existing secureCommunicationProps.
        """
        if value is not None:
            self.secureCommunicationProps = value
        return self

    def getUseAsCryptographicIPdu(self) -> Optional[Boolean]:
        """
        If this attribute is set to true the SecuredIPdu contains the Authentication Information for an AuthenticIPdu that is transmitted in a separate message. The AuthenticIPdu contains the original payload, i.e. the secured data. If this attribute is set to false this SecuredIPdu contains the payload of an Authentic IPdu supplemented by additional Authentication Information.
        """
        return self.useAsCryptographicIPdu

    def setUseAsCryptographicIPdu(self, value: Optional[Boolean]) -> SecuredIPdu:
        """
        If this attribute is set to true the SecuredIPdu contains the Authentication Information for an AuthenticIPdu that is transmitted in a separate message. The AuthenticIPdu contains the original payload, i.e. the secured data. If this attribute is set to false this SecuredIPdu contains the payload of an Authentic IPdu supplemented by additional Authentication Information.
        A None value is a no-op and does not overwrite an existing useAsCryptographicIPdu.
        """
        if value is not None:
            self.useAsCryptographicIPdu = value
        return self

    def getUseSecuredPduHeader(self) -> Optional[SecuredPduHeaderEnum]:
        """
        This attribute defines the size of the header which is inserted into the SecuredIPdu. If this attribute is set to anything but noHeader, the SecuredIPdu contains the Secured I-PDU Header to indicate the length of the AuthenticIPdu. The AuthenticIPdu contains the original payload, i.e. the secured data.
        """
        return self.useSecuredPduHeader

    def setUseSecuredPduHeader(self, value: Optional[SecuredPduHeaderEnum]) -> SecuredIPdu:
        """
        This attribute defines the size of the header which is inserted into the SecuredIPdu. If this attribute is set to anything but noHeader, the SecuredIPdu contains the Secured I-PDU Header to indicate the length of the AuthenticIPdu. The AuthenticIPdu contains the original payload, i.e. the secured data.
        A None value is a no-op and does not overwrite an existing useSecuredPduHeader.
        """
        if value is not None:
            self.useSecuredPduHeader = value
        return self


class TransferPropertyEnum(AREnum):
    """
    Transfer Properties of a Signal.
    """

    # TransferPropertyEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.15, p.327 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods) — enum value form serialized on ISignalToIPduMapping.transferProperty
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # If the signal has the TransferProperty pending, then the function Com_SendSignal shall not perform a transmission of the IPdu associated with the signal. Tags: atp.EnumerationLiteralIndex=0
    PENDING = "PENDING"

    # The signal in the assigned IPdu is updated and a request for the IPdu's transmission is made. Tags: atp.EnumerationLiteralIndex=1
    TRIGGERED = "TRIGGERED"

    # The signal in the assigned IPdu is updated and a request for the IPdus transmission is made only if the signal value is different from the already stored signal value. Tags: atp.EnumerationLiteralIndex=2
    TRIGGERED_ON_CHANGE = "TRIGGERED-ON-CHANGE"

    # The signal in the assigned IPdu is updated and a request for the IPdus transmission is made only if the signal value is different from the already stored signal value. In the DIRECT/N-TIMES or MIXED transmission mode (EventControlledTiming) the IPdu will be transmitted just once without a repetition, independent of the defined NumberOfRepeats. Tags: atp.EnumerationLiteralIndex=3
    TRIGGERED_ON_CHANGE_WITHOUT_REPETITION = "TRIGGERED-ON-CHANGE-WITHOUT-REPETITION"

    # The signal in the assigned IPdu is updated and a request for the IPdu's transmission is made. In the DIRECT/N-TIMES or MIXED transmission mode (EventControlledTiming) the IPdu will be transmitted just once without a repetition, independent of the defined NumberOfRepeats. Tags: atp.EnumerationLiteralIndex=4
    TRIGGERED_WITHOUT_REPETITION = "TRIGGERED-WITHOUT-REPETITION"

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

    def setISignalRef(self, value: Optional[RefType]) -> ISignalToIPduMapping:
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

    def setISignalGroupRef(self, value: Optional[RefType]) -> ISignalToIPduMapping:
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

    def setPackingByteOrder(self, value: Optional[ByteOrderEnum]) -> ISignalToIPduMapping:
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

    def setStartPosition(self, value: Optional[UnlimitedInteger]) -> ISignalToIPduMapping:
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

    def setTransferProperty(self, value: Optional[TransferPropertyEnum]) -> ISignalToIPduMapping:
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

    def setUpdateIndicationBitPosition(self, value: Optional[UnlimitedInteger]) -> ISignalToIPduMapping:
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
        if not self.IsReferrableElementExists(short_name, ISignalToIPduMapping):
            mapping = ISignalToIPduMapping(self, short_name)
            self.addReferrableElement(mapping)
            self.iSignalToIPduMappings.append(mapping)
        return cast(ISignalToIPduMapping, self.getReferrableElement(short_name, ISignalToIPduMapping))

    def getNmDataInformation(self) -> Optional[Boolean]:
        """
        Defines if the Pdu contains NM Data. If the NmPdu does not aggregate any ISignalToIPduMappings it still may contain UserData that is set via Nm_SetUserData(). If the ISignalToIPduMapping exists then the nmDataInformation attribute shall be ignored.
        """
        return self.nmDataInformation

    def setNmDataInformation(self, value: Optional[Boolean]) -> NmPdu:
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

    def setNmVoteInformation(self, value: Optional[Boolean]) -> NmPdu:
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

    def setUnusedBitPattern(self, value: Optional[Integer]) -> NmPdu:
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

        self.diagPduType: Optional[ARLiteral] = None

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

    def setMinimumDelay(self, value: Optional[TimeValue]) -> IPduTiming:
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

    def setTransmissionModeDeclaration(self, value: Optional[TransmissionModeDeclaration]) -> IPduTiming:
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

    def setIPduTimingSpecification(self, value: Optional[IPduTiming]) -> ISignalIPdu:
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
        if not self.IsReferrableElementExists(short_name, ISignalToIPduMapping):
            mapping = ISignalToIPduMapping(self, short_name)
            self.addReferrableElement(mapping)
            self.iSignalToPduMappings.append(mapping)
        return cast(ISignalToIPduMapping, self.getReferrableElement(short_name, ISignalToIPduMapping))

    def getUnusedBitPattern(self) -> Optional[Integer]:
        """
        AUTOSAR COM and AUTOSAR IPDUM are filling not used areas of an IPDU with this bit-pattern. This attribute is mandatory to avoid undefined behavior. This byte-pattern will be repeated throughout the IPdu.
        """
        return self.unusedBitPattern

    def setUnusedBitPattern(self, value: Optional[Integer]) -> ISignalIPdu:
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
    ARRAY = "ARRAY"

    # ISignal shall be interpreted as a primitive type (e.g. UINT_8, SINT_32) Tags: atp.EnumerationLiteralIndex=1
    PRIMITIVE = "PRIMITIVE"

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

    def setHandleOutOfRange(self, value: Optional[HandleOutOfRangeEnum]) -> ISignalProps:
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

    def setDataTransformationRef(self, value: Optional[RefType]) -> ISignal:
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

    def setDataTypePolicy(self, value: Optional[DataTypePolicyEnum]) -> ISignal:
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

    def setInitValue(self, value: Optional[ValueSpecification]) -> ISignal:
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

    def setISignalProps(self, value: Optional[ISignalProps]) -> ISignal:
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

    def setISignalType(self, value: Optional[ISignalTypeEnum]) -> ISignal:
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

    def setLength(self, value: Optional[UnlimitedInteger]) -> ISignal:
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

    def setNetworkRepresentationProps(self, value: Optional[SwDataDefProps]) -> ISignal:
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

    def setSystemSignalRef(self, value: Optional[RefType]) -> ISignal:
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

    def setTimeoutSubstitutionValue(self, value: Optional[ValueSpecification]) -> ISignal:
        """
        Defines and enables the ComTimeoutSubstituition for this ISignal.
        A None value is a no-op and does not overwrite an existing timeoutSubstitutionValue.
        """
        if value is not None:
            self.timeoutSubstitutionValue = value
        return self

    def addTransformationISignalProps(self, value: Optional[TransformationISignalProps]) -> ISignal:
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

    def setIPduRef(self, value: Optional[RefType]) -> PduTriggering:
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

    def addIPduPortRef(self, value: Optional[RefType]) -> PduTriggering:
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

    def addISignalTriggeringRef(self, value: Optional[RefType]) -> PduTriggering:
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

    def setSecOcCryptoMappingRef(self, value: Optional[RefType]) -> PduTriggering:
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

    def addTriggerIPduSendCondition(self, value: Optional[TriggerIPduSendCondition]) -> PduTriggering:
        """
        Defines the trigger for the Com_TriggerIPDUSend API call. Only if all defined TriggerIPduSendConditions evaluate to true (AND associated) the Com_TriggerIPDUSend API shall be called.
        """
        if value is not None:
            self.triggerIPduSendConditions.append(value)
        return self


class ContainerIPdu(IPdu):
    """
    Allows to collect several IPdus in one ContainerIPdu based on the headerType. Tags: atp.recommendedPackage=Pdus
    """

    # ContainerIPdu method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.35, p.354 (R23-11)
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                          [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addContainedIPduTriggeringProps   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getContainedIPduTriggeringProps   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addContainedPduTriggeringRef      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getContainedPduTriggeringRefs     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getContainerTimeout               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setContainerTimeout               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getContainerTrigger               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setContainerTrigger               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getHeaderType                     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setHeaderType                     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getMinimumRxContainerQueueSize    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setMinimumRxContainerQueueSize    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getMinimumTxContainerQueueSize    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setMinimumTxContainerQueueSize    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getRxAcceptContainedIPdu          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setRxAcceptContainedIPdu          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getThresholdSize                  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setThresholdSize                  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getUnusedBitPattern               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setUnusedBitPattern               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Defines properties for an IPdu that is part of the ContainerIPdu.
        self.containedIPduTriggeringProps: List[ContainedIPduProps] = []

        # This PduTriggering shall be collected inside the Container IPdu.
        self.containedPduTriggeringRefs: List[RefType] = []

        # When this timeout expires the ContainerIPdu is sent out. The respective timer is started when the first Ipdu is put into the ContainerIPdu. This attribute is ignored on receiver side.
        self.containerTimeout: Optional[TimeValue] = None

        # Defines if the transmission of the ContainerIPdu shall be requested right after the first ContainedIPdu was put into it. This attribute shall be ignored on receiver side.
        self.containerTrigger: Optional[ContainerIPduTriggerEnum] = None

        # Defines whether and which header type is used (header id and length).
        self.headerType: Optional[ContainerIPduHeaderTypeEnum] = None

        # This attribute defines the minimum queue size for received containers.
        self.minimumRxContainerQueueSize: Optional[PositiveInteger] = None

        # This attribute defines the minimum queue size for transmitted containers.
        self.minimumTxContainerQueueSize: Optional[PositiveInteger] = None

        # Defines whether this ContainerIPdu has a fixed set of containedIPdus assigned for reception.
        self.rxAcceptContainedIPdu: Optional[RxAcceptContainedIPduEnum] = None

        # Defines the size threshold which, when exceeded, triggers the sending of the ContainerIPdu although the maximum Pdu size has not been reached yet. Unit: byte.
        self.thresholdSize: Optional[PositiveInteger] = None

        # IPduM fills not updated areas of the ContainerPdu with this byte-pattern.
        self.unusedBitPattern: Optional[PositiveInteger] = None

    def addContainedIPduTriggeringProps(self, value: Optional[ContainedIPduProps]) -> ContainerIPdu:
        """
        Defines properties for an IPdu that is part of the ContainerIPdu.
        A None value is a no-op and does not add to containedIPduTriggeringProps.
        """
        if value is not None:
            self.containedIPduTriggeringProps.append(value)
        return self

    def getContainedIPduTriggeringProps(self) -> List[ContainedIPduProps]:
        """
        Defines properties for an IPdu that is part of the ContainerIPdu.
        """
        return self.containedIPduTriggeringProps

    def addContainedPduTriggeringRef(self, value: Optional[RefType]) -> ContainerIPdu:
        """
        This PduTriggering shall be collected inside the Container IPdu.
        A None value is a no-op and does not add to containedPduTriggeringRefs.
        """
        if value is not None:
            self.containedPduTriggeringRefs.append(value)
        return self

    def getContainedPduTriggeringRefs(self) -> List[RefType]:
        """
        This PduTriggering shall be collected inside the Container IPdu.
        """
        return self.containedPduTriggeringRefs

    def getContainerTimeout(self) -> Optional[TimeValue]:
        """
        When this timeout expires the ContainerIPdu is sent out. The respective timer is started when the first Ipdu is put into the ContainerIPdu. This attribute is ignored on receiver side.
        """
        return self.containerTimeout

    def setContainerTimeout(self, value: Optional[TimeValue]) -> ContainerIPdu:
        """
        When this timeout expires the ContainerIPdu is sent out. The respective timer is started when the first Ipdu is put into the ContainerIPdu. This attribute is ignored on receiver side.
        A None value is a no-op and does not overwrite an existing containerTimeout.
        """
        if value is not None:
            self.containerTimeout = value
        return self

    def getContainerTrigger(self) -> Optional[ContainerIPduTriggerEnum]:
        """
        Defines if the transmission of the ContainerIPdu shall be requested right after the first ContainedIPdu was put into it. This attribute shall be ignored on receiver side.
        """
        return self.containerTrigger

    def setContainerTrigger(self, value: Optional[ContainerIPduTriggerEnum]) -> ContainerIPdu:
        """
        Defines if the transmission of the ContainerIPdu shall be requested right after the first ContainedIPdu was put into it. This attribute shall be ignored on receiver side.
        A None value is a no-op and does not overwrite an existing containerTrigger.
        """
        if value is not None:
            self.containerTrigger = value
        return self

    def getHeaderType(self) -> Optional[ContainerIPduHeaderTypeEnum]:
        """
        Defines whether and which header type is used (header id and length).
        """
        return self.headerType

    def setHeaderType(self, value: Optional[ContainerIPduHeaderTypeEnum]) -> ContainerIPdu:
        """
        Defines whether and which header type is used (header id and length).
        A None value is a no-op and does not overwrite an existing headerType.
        """
        if value is not None:
            self.headerType = value
        return self

    def getMinimumRxContainerQueueSize(self) -> Optional[PositiveInteger]:
        """
        This attribute defines the minimum queue size for received containers.
        """
        return self.minimumRxContainerQueueSize

    def setMinimumRxContainerQueueSize(self, value: Optional[PositiveInteger]) -> ContainerIPdu:
        """
        This attribute defines the minimum queue size for received containers.
        A None value is a no-op and does not overwrite an existing minimumRxContainerQueueSize.
        """
        if value is not None:
            self.minimumRxContainerQueueSize = value
        return self

    def getMinimumTxContainerQueueSize(self) -> Optional[PositiveInteger]:
        """
        This attribute defines the minimum queue size for transmitted containers.
        """
        return self.minimumTxContainerQueueSize

    def setMinimumTxContainerQueueSize(self, value: Optional[PositiveInteger]) -> ContainerIPdu:
        """
        This attribute defines the minimum queue size for transmitted containers.
        A None value is a no-op and does not overwrite an existing minimumTxContainerQueueSize.
        """
        if value is not None:
            self.minimumTxContainerQueueSize = value
        return self

    def getRxAcceptContainedIPdu(self) -> Optional[RxAcceptContainedIPduEnum]:
        """
        Defines whether this ContainerIPdu has a fixed set of containedIPdus assigned for reception.
        """
        return self.rxAcceptContainedIPdu

    def setRxAcceptContainedIPdu(self, value: Optional[RxAcceptContainedIPduEnum]) -> ContainerIPdu:
        """
        Defines whether this ContainerIPdu has a fixed set of containedIPdus assigned for reception.
        A None value is a no-op and does not overwrite an existing rxAcceptContainedIPdu.
        """
        if value is not None:
            self.rxAcceptContainedIPdu = value
        return self

    def getThresholdSize(self) -> Optional[PositiveInteger]:
        """
        Defines the size threshold which, when exceeded, triggers the sending of the ContainerIPdu although the maximum Pdu size has not been reached yet. Unit: byte.
        """
        return self.thresholdSize

    def setThresholdSize(self, value: Optional[PositiveInteger]) -> ContainerIPdu:
        """
        Defines the size threshold which, when exceeded, triggers the sending of the ContainerIPdu although the maximum Pdu size has not been reached yet. Unit: byte.
        A None value is a no-op and does not overwrite an existing thresholdSize.
        """
        if value is not None:
            self.thresholdSize = value
        return self

    def getUnusedBitPattern(self) -> Optional[PositiveInteger]:
        """
        IPduM fills not updated areas of the ContainerPdu with this byte-pattern.
        """
        return self.unusedBitPattern

    def setUnusedBitPattern(self, value: Optional[PositiveInteger]) -> ContainerIPdu:
        """
        IPduM fills not updated areas of the ContainerPdu with this byte-pattern.
        A None value is a no-op and does not overwrite an existing unusedBitPattern.
        """
        if value is not None:
            self.unusedBitPattern = value
        return self


class PdurIPduGroup(FibexElement):
    """
    The AUTOSAR PduR will enable and disable the sending of configurable groups of IPdus during runtime according to the AUTOSAR PduR specification. Tags: atp.recommendedPackage=PdurIPduGroups
    """

    # PdurIPduGroup method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.34, p.352
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getCommunicationMode    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setCommunicationMode    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] addIPduRef              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getIPduRefs             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This attribute defines the use-case for this PduRIPduGroup. For example, in a diagnostic mode all IPdus - which are not involved in diagnostic - are disabled. The use cases are not limited to a fixed enumeration and can be specified as a string.
        self.communicationMode: Optional[String] = None

        # Reference to a set of IPdus, which are contained in the PduR I-Pdu Group. If an IPdu is routed by the PduR to different destinations (PduR fan-out) than an PduTriggering for each destination is created in the System Template. To enable/disable a specific destination the PdurIPduGroup refers to the PduTriggering. atpVariation: The content of a PduR I-Pdu group can vary (->vehicle modes).
        self.iPduRefs: List[RefType] = []

    def getCommunicationMode(self) -> Optional[String]:
        """
        This attribute defines the use-case for this PduRIPduGroup. For example, in a diagnostic mode all IPdus - which are not involved in diagnostic - are disabled. The use cases are not limited to a fixed enumeration and can be specified as a string.
        """
        return self.communicationMode

    def setCommunicationMode(self, value: Optional[String]) -> PdurIPduGroup:
        """
        This attribute defines the use-case for this PduRIPduGroup. For example, in a diagnostic mode all IPdus - which are not involved in diagnostic - are disabled. The use cases are not limited to a fixed enumeration and can be specified as a string.
        A None value is a no-op and does not overwrite an existing communicationMode.
        """
        if value is not None:
            self.communicationMode = value
        return self

    def addIPduRef(self, value: Optional[RefType]) -> PdurIPduGroup:
        """
        Reference to a set of IPdus, which are contained in the PduR I-Pdu Group. If an IPdu is routed by the PduR to different destinations (PduR fan-out) than an PduTriggering for each destination is created in the System Template. To enable/disable a specific destination the PdurIPduGroup refers to the PduTriggering. atpVariation: The content of a PduR I-Pdu group can vary (->vehicle modes).
        A None value is a no-op and does not add to iPduRefs.
        """
        if value is not None:
            self.iPduRefs.append(value)
        return self

    def getIPduRefs(self) -> List[RefType]:
        """
        Reference to a set of IPdus, which are contained in the PduR I-Pdu Group. If an IPdu is routed by the PduR to different destinations (PduR fan-out) than an PduTriggering for each destination is created in the System Template. To enable/disable a specific destination the PdurIPduGroup refers to the PduTriggering. atpVariation: The content of a PduR I-Pdu group can vary (->vehicle modes).
        """
        return self.iPduRefs


class FrameTriggering(Identifiable, VariationPointCapable, ABC):
    """
    The FrameTriggering describes the instance of a frame sent on a channel and defines the manner of triggering (timing information) and identification of a frame on the channel, on which it is sent. For the same frame, if FrameTriggerings exist on more than one channel of the same cluster the fan-out/in is handled by the Bus interface.

    [constr_9131] Existence of FrameTriggering.frame: For each FrameTriggering, the reference to Frame in the role frame shall exist at the time when the System Description is complete.
    """

    # FrameTriggering method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.79, p.418 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__              [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getFrameRef           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setFrameRef           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] addFramePortRef       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getFramePortRefs      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addPduTriggeringRef   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getPduTriggeringRefs  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is FrameTriggering:
            raise TypeError("FrameTriggering is an abstract class.")

        super().__init__(parent, short_name)

        # One frame can be triggered several times, e.g. on different channels. If a frame has no frame triggering, it won't be sent at all. A frame triggering has assigned exactly one frame, which it triggers.
        self.frameRef: Optional[RefType] = None

        # References to the FramePort on every ECU of the system which sends and/or receives the frame. References for both the sender and the receiver side shall be included when the system is completely defined.
        self.framePortRefs: List[RefType] = []

        # This reference provides the relationship to the Pdu Triggerings that are implemented by the FrameTriggering. The reference is optional since no PduTriggering can be defined for NmPdus and XCP Pdus. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=pduTriggering.pduTriggering, pdu Triggering.variationPoint.shortLabel vh.latestBindingTime=postBuild
        self.pduTriggeringRefs: List[RefType] = []

    def getFrameRef(self) -> Optional[RefType]:
        """
        One frame can be triggered several times, e.g. on different channels. If a frame has no frame triggering, it won't be sent at all. A frame triggering has assigned exactly one frame, which it triggers.
        """
        return self.frameRef

    def setFrameRef(self, value: Optional[RefType]) -> FrameTriggering:
        """
        One frame can be triggered several times, e.g. on different channels. If a frame has no frame triggering, it won't be sent at all. A frame triggering has assigned exactly one frame, which it triggers.
        A None value is a no-op and does not overwrite an existing frameRef.
        """
        if value is not None:
            self.frameRef = value
        return self

    def addFramePortRef(self, value: Optional[RefType]) -> FrameTriggering:
        """
        References to the FramePort on every ECU of the system which sends and/or receives the frame. References for both the sender and the receiver side shall be included when the system is completely defined.
        """
        if value is not None:
            self.framePortRefs.append(value)
        return self

    def getFramePortRefs(self) -> List[RefType]:
        """
        References to the FramePort on every ECU of the system which sends and/or receives the frame. References for both the sender and the receiver side shall be included when the system is completely defined.
        """
        return self.framePortRefs

    def addPduTriggeringRef(self, value: Optional[RefType]) -> FrameTriggering:
        """
        This reference provides the relationship to the Pdu Triggerings that are implemented by the FrameTriggering. The reference is optional since no PduTriggering can be defined for NmPdus and XCP Pdus. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=pduTriggering.pduTriggering, pdu Triggering.variationPoint.shortLabel vh.latestBindingTime=postBuild
        """
        if value is not None:
            self.pduTriggeringRefs.append(value)
        return self

    def getPduTriggeringRefs(self) -> List[RefType]:
        """
        This reference provides the relationship to the Pdu Triggerings that are implemented by the FrameTriggering. The reference is optional since no PduTriggering can be defined for NmPdus and XCP Pdus. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=pduTriggering.pduTriggering, pdu Triggering.variationPoint.shortLabel vh.latestBindingTime=postBuild
        """
        return self.pduTriggeringRefs


class SystemSignal(ARElement):
    """
    The system signal represents the communication system's view of data exchanged between SW components which reside on different ECUs. The system signals allow to represent this communication in a flattened structure, with exactly one system signal defined for each data element prototype sent and received by connected SW component instances. Tags: atp.recommendedPackage=SystemSignals
    """

    # SystemSignal method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 5.23, p.218 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__          [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getDynamicLength  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDynamicLength  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getPhysicalProps  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setPhysicalProps  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # The length of dynamic length signals is variable in run-time. Only a maximum length of such a signal is specified in the configuration (attribute length in ISignal element).
        self.dynamicLength: Optional[Boolean] = None

        # Specification of the physical representation. Stereotypes: atpSplitable Tags: atp.Splitkey=physicalProps
        self.physicalProps: Optional[SwDataDefProps] = None

    def getDynamicLength(self) -> Optional[Boolean]:
        """
        The length of dynamic length signals is variable in run-time. Only a maximum length of such a signal is specified in the configuration (attribute length in ISignal element).
        """
        return self.dynamicLength

    def setDynamicLength(self, value: Optional[Boolean]) -> SystemSignal:
        """
        The length of dynamic length signals is variable in run-time. Only a maximum length of such a signal is specified in the configuration (attribute length in ISignal element).
        A None value is a no-op and does not overwrite an existing dynamicLength.
        """
        if value is not None:
            self.dynamicLength = value
        return self

    def getPhysicalProps(self) -> Optional[SwDataDefProps]:
        """
        Specification of the physical representation. Stereotypes: atpSplitable Tags: atp.Splitkey=physicalProps
        """
        return self.physicalProps

    def setPhysicalProps(self, value: Optional[SwDataDefProps]) -> SystemSignal:
        """
        Specification of the physical representation. Stereotypes: atpSplitable Tags: atp.Splitkey=physicalProps
        A None value is a no-op and does not overwrite an existing physicalProps.
        """
        if value is not None:
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

    def addSystemSignalRef(self, value: RefType) -> SystemSignalGroup:
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

    def setTransformingSystemSignalRef(self, value: Optional[RefType]) -> SystemSignalGroup:
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

    def setISignalRef(self, value: Optional[RefType]) -> ISignalTriggering:
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

    def setISignalGroupRef(self, value: Optional[RefType]) -> ISignalTriggering:
        """
        This reference shall be used if an ISignalGroup is transported on the PhysicalChannel. This reference forms an XOR relationship with the ISignal Triggering-ISignal reference.
        A None value is a no-op and does not overwrite an existing iSignalGroupRef.
        """
        if value is not None:
            self.iSignalGroupRef = value
        return self

    def addISignalPortRef(self, value: Optional[RefType]) -> ISignalTriggering:
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
    The StaticPart and the DynamicPart can be separated in multiple segments within the multiplexed PDU. The ISignalIPdus are copied bit by bit into the MultiplexedIPdu. If the space of the first segment is 5 bits large than the first 5 bits of the ISignalIPdu are copied into this first segment and so on.
    """

    # SegmentPosition method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.77, p.412 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__            [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getSegmentByteOrder [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSegmentByteOrder [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSegmentLength    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSegmentLength    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSegmentPosition  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSegmentPosition  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # This attribute defines the order of the bytes of the segment and the packing into the MultiplexedIPdu. Please consider that [constr_3247] and [constr_3224] are restricting the usage of this attribute.
        self.segmentByteOrder: Optional[ByteOrderEnum] = None

        # Data Length of the segment in bits.
        self.segmentLength: Optional[Integer] = None

        # Segments bit position relatively to the beginning of a multiplexed IPdu. Note that the absolute position of the segment in the MultiplexedIPdu is determined by the definition of the segmentByteOrder attribute of the SegmentPosition. If Big Endian is specified, the start position indicates the bit position of the most significant bit in the IPdu. If Little Endian is specified, the start position indicates the bit position of the least significant bit in the IPdu. In AUTOSAR the bit counting is always set to "sawtooth" and the bit order is set to "Decreasing". The bit counting in byte 0 starts with bit 0 (least significant bit). The most significant bit in byte 0 is bit 7.
        self.segmentPosition: Optional[Integer] = None

    def getSegmentByteOrder(self) -> Optional[ByteOrderEnum]:
        """
        This attribute defines the order of the bytes of the segment and the packing into the MultiplexedIPdu. Please consider that [constr_3247] and [constr_3224] are restricting the usage of this attribute.
        """
        return self.segmentByteOrder

    def setSegmentByteOrder(self, value: Optional[ByteOrderEnum]) -> SegmentPosition:
        """
        This attribute defines the order of the bytes of the segment and the packing into the MultiplexedIPdu. Please consider that [constr_3247] and [constr_3224] are restricting the usage of this attribute.
        A None value is a no-op and does not overwrite an existing segmentByteOrder.
        """
        if value is not None:
            self.segmentByteOrder = value
        return self

    def getSegmentLength(self) -> Optional[Integer]:
        """
        Data Length of the segment in bits.
        """
        return self.segmentLength

    def setSegmentLength(self, value: Optional[Integer]) -> SegmentPosition:
        """
        Data Length of the segment in bits.
        A None value is a no-op and does not overwrite an existing segmentLength.
        """
        if value is not None:
            self.segmentLength = value
        return self

    def getSegmentPosition(self) -> Optional[Integer]:
        """
        Segments bit position relatively to the beginning of a multiplexed IPdu. Note that the absolute position of the segment in the MultiplexedIPdu is determined by the definition of the segmentByteOrder attribute of the SegmentPosition. If Big Endian is specified, the start position indicates the bit position of the most significant bit in the IPdu. If Little Endian is specified, the start position indicates the bit position of the least significant bit in the IPdu. In AUTOSAR the bit counting is always set to "sawtooth" and the bit order is set to "Decreasing". The bit counting in byte 0 starts with bit 0 (least significant bit). The most significant bit in byte 0 is bit 7.
        """
        return self.segmentPosition

    def setSegmentPosition(self, value: Optional[Integer]) -> SegmentPosition:
        """
        Segments bit position relatively to the beginning of a multiplexed IPdu. Note that the absolute position of the segment in the MultiplexedIPdu is determined by the definition of the segmentByteOrder attribute of the SegmentPosition. If Big Endian is specified, the start position indicates the bit position of the most significant bit in the IPdu. If Little Endian is specified, the start position indicates the bit position of the least significant bit in the IPdu. In AUTOSAR the bit counting is always set to "sawtooth" and the bit order is set to "Decreasing". The bit counting in byte 0 starts with bit 0 (least significant bit). The most significant bit in byte 0 is bit 7.
        A None value is a no-op and does not overwrite an existing segmentPosition.
        """
        if value is not None:
            self.segmentPosition = value
        return self


class MultiplexedPart(ARObject, ABC):
    """
    The StaticPart and the DynamicPart have common properties. Both can be separated in multiple segments within the multiplexed PDU.

    [constr_9181] Existence of MultiplexedPart.segmentPosition: For each MultiplexedPart the aggregation of SegmentPosition in role segmentPosition shall exist at the time when the System Description is complete.
    """

    # MultiplexedPart method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.76, p.411 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__             [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getSegmentPositions  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addSegmentPosition   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        if type(self) is MultiplexedPart:
            raise TypeError("MultiplexedPart is an abstract class.")

        super().__init__()

        # The StaticPart and the DynamicPart can be separated in multiple segments within the multiplexed PDU. Therefore the StaticPart and the DynamicPart can contain multiple SegmentPositions.
        self.segmentPositions: List[SegmentPosition] = []

    def getSegmentPositions(self) -> List[SegmentPosition]:
        """
        The StaticPart and the DynamicPart can be separated in multiple segments within the multiplexed PDU. Therefore the StaticPart and the DynamicPart can contain multiple SegmentPositions.
        """
        return self.segmentPositions

    def addSegmentPosition(self, value: Optional[SegmentPosition]) -> MultiplexedPart:
        """
        The StaticPart and the DynamicPart can be separated in multiple segments within the multiplexed PDU. Therefore the StaticPart and the DynamicPart can contain multiple SegmentPositions.
        A None value is a no-op and is not appended to segmentPositions.
        """
        if value is not None:
            self.segmentPositions.append(value)
        return self


class StaticPart(MultiplexedPart, VariationPointCapable):
    """
    Some parts/signals of the I-PDU may be the same regardless of the selector field. Such a part is called static part. The static part is optional.

    [constr_9176] Existence of StaticPart.iPdu: For each StaticPart, the reference to ISignalIPdu in role iPdu shall exist at the time when the System Description is complete.
    """

    # StaticPart method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.73, p.410 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getIPduRef   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setIPduRef   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # Reference to a Com IPdu which is routed to the IPduM module and is combined to a multiplexedPdu.
        self.iPduRef: Optional[RefType] = None

    def getIPduRef(self) -> Optional[RefType]:
        """
        Reference to a Com IPdu which is routed to the IPduM module and is combined to a multiplexedPdu.
        """
        return self.iPduRef

    def setIPduRef(self, value: Optional[RefType]) -> StaticPart:
        """
        Reference to a Com IPdu which is routed to the IPduM module and is combined to a multiplexedPdu.
        A None value is a no-op and does not overwrite an existing iPduRef.
        """
        if value is not None:
            self.iPduRef = value
        return self


class DynamicPartAlternative(ARObject):
    """
    One of the Com IPdu alternatives that are transmitted in the Dynamic Part of the MultiplexedIPdu. The selectorFieldCode specifies which Com IPdu is contained in the DynamicPart within a certain transmission of a multiplexed PDU.

    [constr_9178] Existence of DynamicPartAlternative.initialDynamicPart: For each DynamicPartAlternative the attribute initialDynamicPart shall exist at the time when the System Description is complete.

    [constr_9179] Existence of DynamicPartAlternative.iPdu: For each DynamicPartAlternative, the reference to ISignalIPdu in role iPdu shall exist at the time when the System Description is complete.

    [constr_9180] Existence of DynamicPartAlternative.selectorFieldCode: For each DynamicPartAlternative, the attribute selectorFieldCode shall exist at the time when the System Description is complete.
    """

    # DynamicPartAlternative method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.75, p.411 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getInitialDynamicPart   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setInitialDynamicPart   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getIPduRef              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setIPduRef              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSelectorFieldCode    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSelectorFieldCode    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # Dynamic part that shall be used to initialize this multiplexed IPdu. Constraint: Only one "DynamicPartAlternative" in a "DynamicPart" shall be the initialDynamicPart.
        self.initialDynamicPart: Optional[Boolean] = None

        # Reference to a Com IPdu which is routed to the IPduM module and is combined to a multiplexedPdu.
        self.iPduRef: Optional[RefType] = None

        # The selector field is part of a multiplexed IPdu. It consists of contiguous bits. The value of the selector field selects the layout of the multiplexed part of the IPdu.
        self.selectorFieldCode: Optional[Integer] = None

    def getInitialDynamicPart(self) -> Optional[Boolean]:
        """
        Dynamic part that shall be used to initialize this multiplexed IPdu. Constraint: Only one "DynamicPartAlternative" in a "DynamicPart" shall be the initialDynamicPart.
        """
        return self.initialDynamicPart

    def setInitialDynamicPart(self, value: Optional[Boolean]) -> DynamicPartAlternative:
        """
        Dynamic part that shall be used to initialize this multiplexed IPdu. Constraint: Only one "DynamicPartAlternative" in a "DynamicPart" shall be the initialDynamicPart.
        A None value is a no-op and does not overwrite an existing initialDynamicPart.
        """
        if value is not None:
            self.initialDynamicPart = value
        return self

    def getIPduRef(self) -> Optional[RefType]:
        """
        Reference to a Com IPdu which is routed to the IPduM module and is combined to a multiplexedPdu.
        """
        return self.iPduRef

    def setIPduRef(self, value: Optional[RefType]) -> DynamicPartAlternative:
        """
        Reference to a Com IPdu which is routed to the IPduM module and is combined to a multiplexedPdu.
        A None value is a no-op and does not overwrite an existing iPduRef.
        """
        if value is not None:
            self.iPduRef = value
        return self

    def getSelectorFieldCode(self) -> Optional[Integer]:
        """
        The selector field is part of a multiplexed IPdu. It consists of contiguous bits. The value of the selector field selects the layout of the multiplexed part of the IPdu.
        """
        return self.selectorFieldCode

    def setSelectorFieldCode(self, value: Optional[Integer]) -> DynamicPartAlternative:
        """
        The selector field is part of a multiplexed IPdu. It consists of contiguous bits. The value of the selector field selects the layout of the multiplexed part of the IPdu.
        A None value is a no-op and does not overwrite an existing selectorFieldCode.
        """
        if value is not None:
            self.selectorFieldCode = value
        return self


class DynamicPart(MultiplexedPart, VariationPointCapable):
    """
    Dynamic part of a multiplexed I-Pdu. Reserved space which is used to transport varying SignalIPdus at the same position, controlled by the corresponding selectorFieldCode.
    """

    # DynamicPart method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.74, p.410 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getDynamicPartAlternatives  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addDynamicPartAlternative   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # Com IPdu alternatives that are transmitted in the Dynamic Part of the MultiplexedIPdu.
        self.dynamicPartAlternatives: List[DynamicPartAlternative] = []

    def getDynamicPartAlternatives(self) -> List[DynamicPartAlternative]:
        """
        Com IPdu alternatives that are transmitted in the Dynamic Part of the MultiplexedIPdu.
        """
        return self.dynamicPartAlternatives

    def addDynamicPartAlternative(self, value: Optional[DynamicPartAlternative]) -> DynamicPart:
        """
        Com IPdu alternatives that are transmitted in the Dynamic Part of the MultiplexedIPdu.
        A None value is a no-op and is not appended to dynamicPartAlternatives.
        """
        if value is not None:
            self.dynamicPartAlternatives.append(value)
        return self


class TriggerMode(AREnum):
    """
    IPduM can be configured to send a transmission request for the new multiplexed I-PDU to the PDU-Router because of conditions/ modes.
    """

    # TriggerMode method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.71, p.408 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods) — enum value form serialized on MultiplexedIPdu.triggerMode
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # IPduM sends a transmission request to the PduR if a dynamic part is received. Tags: atp.EnumerationLiteralIndex=0
    DYNAMIC_PART_TRIGGER = "DYNAMIC-PART-TRIGGER"

    # IPduM does not trigger transmission because of receiving anything of this IPdu in case of Trigger Transmit. Tags: atp.EnumerationLiteralIndex=1
    NONE = "NONE"

    # IPduM sends a transmission request to the PduR if a static or dynamic part is received. Tags: atp.EnumerationLiteralIndex=2
    STATIC_OR_DYNAMIC_PART_TRIGGER = "STATIC-OR-DYNAMIC-PART-TRIGGER"

    # IPduM sends a transmission request to the PduR if a static part is received. Tags: atp.EnumerationLiteralIndex=3
    STATIC_PART_TRIGGER = "STATIC-PART-TRIGGER"

    def __init__(self):
        super().__init__([TriggerMode.DYNAMIC_PART_TRIGGER, TriggerMode.NONE, TriggerMode.STATIC_OR_DYNAMIC_PART_TRIGGER, TriggerMode.STATIC_PART_TRIGGER])


class MultiplexedIPdu(IPdu):
    """
    A MultiplexedPdu (i.e. NOT a COM I-PDU) contains a DynamicPart, an optional StaticPart and a selector Field. In case of multiplexing this IPdu is routed between the Pdu Multiplexer and the Interface Layer. A multiplexer is used to define variable parts within an IPdu that may carry different signals. The receivers of such a IPdu can determine which signalPdus are transmitted by evaluating the selector field, which carries a unique selector code for each sub-part. Tags: atp.recommendedPackage=Pdus

    """

    # MultiplexedIPdu method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.72, p.410 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__       [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getDynamicPart         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDynamicPart         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSelectorFieldByteOrder [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSelectorFieldByteOrder [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSelectorFieldLength [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSelectorFieldLength [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSelectorFieldStartPosition [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSelectorFieldStartPosition [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getStaticPart          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setStaticPart          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTriggerMode         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTriggerMode         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getUnusedBitPattern    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setUnusedBitPattern    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # According to the value of the selector field some parts of the IPdu have a different layout. In a complete System Description a MultiplexedIPdu shall contain a Dynamic Part. The following use cases support the multiplicity to be 0..1: • If a MultiplexedIPdu is received by a Pdu Gateway and is not delivered to the IPduM but routed directly to a bus interface then the content of the MulitplexedIPdu doesn't need to be described in the System Extract/ Ecu Extract. • If a MultiplexedIPdu is received by an ECU which is only interested in the static part of the MultiplexedIPdu then the dynamicPart does not need to be described in the System Extract/Ecu Extract. atpVariation: Content of a multiplexed PDU can vary. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=dynamicPart, dynamicPart.variation Point.shortLabel vh.latestBindingTime=postBuild

        self.dynamicPart: Optional[DynamicPart] = None

        # This attribute defines the order of the bytes of the selector Field and the packing into the MultiplexedIPdu. Please consider that [constr_3247] and [constr_3223] are restricting the usage of this attribute. In a complete System Description this attribute is mandatory. If a MultiplexedPdu is received by a Pdu Gateway and is not delivered to the IPduM but routed directly to a bus interface then the content of the MulitplexedPdu doesn't need to be described in the System Extract/Ecu Extract. To support this use case the multiplicity is set to 0..1.

        self.selectorFieldByteOrder: Optional[ByteOrderEnum] = None

        # The size in bits of the selector field shall be configurable in a range of 1-16 bits. In a complete System Description this attribute is mandatory. If a MultiplexedPdu is received by a Pdu Gateway and is not delivered to the IPduM but routed directly to a bus interface then the content of the MulitplexedPdu doesn't need to be described in the System Extract/Ecu Extract. To support this use case the multiplicity is set to 0..1.

        self.selectorFieldLength: Optional[Integer] = None

        # This parameter is necessary to describe the position of the selector field within the IPdu. Note that the absolute position of the selectorField in the MultiplexedIPdu is determined by the definition of the selectorFieldByteOrder attribute of the Multiplexed Pdu. If Big Endian is specified, the start position indicates the bit position of the most significant bit in the IPdu. If Little Endian is specified, the start position indicates the bit position of the least significant bit in the IPdu. In AUTOSAR the bit counting is always set to "sawtooth" and the bit order is set to "Decreasing". The bit counting in byte 0 starts with bit 0 (least significant bit). The most significant bit in byte 0 is bit 7. In a complete System Description this attribute is mandatory. If a MultiplexedPdu is received by a Pdu Gateway and is not delivered to the IPduM but routed directly to a bus interface then the content of the MulitplexedPdu doesn't need to be described in the System Extract/Ecu Extract. To support this use case the multiplicity is set to 0..1.

        self.selectorFieldStartPosition: Optional[Integer] = None

        # The static part of the multiplexed IPdu is the same regardless of the selector field. The static part is optional. atpVariation: Content of a multiplexed PDU can vary. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=staticPart, staticPart.variationPoint.short Label vh.latestBindingTime=postBuild

        self.staticPart: Optional[StaticPart] = None

        # IPduM can be configured to send a transmission request for the new multiplexed IPdu to the PDU-Router because of the trigger conditions/ modes that are described in the TriggerMode enumeration. In a complete System Description this attribute is mandatory. If a MultiplexedPdu is received by a Pdu Gateway and is not delivered to the IPduM but routed directly to a bus interface then the content of the MulitplexedPdu doesn't need to be described in the System Extract/Ecu Extract. To support this use case the multiplicity is set to 0..1.

        self.triggerMode: Optional[TriggerMode] = None

        # AUTOSAR COM and AUTOSAR IPDUM are filling not used areas of an IPdu with this bit-pattern. This attribute is mandatory to avoid undefined behavior. This byte-pattern will be repeated throughout the IPdu. In a complete System Description this attribute is mandatory. If a MultiplexedPdu is received by a Pdu Gateway and is not delivered to the IPduM but routed directly to a bus interface then the content of the MulitplexedPdu doesn't need to be described in the System Extract/Ecu Extract. To support this use case the multiplicity is set to 0..1.

        self.unusedBitPattern: Optional[Integer] = None

    def getDynamicPart(self) -> Optional[DynamicPart]:
        """
        According to the value of the selector field some parts of the IPdu have a different layout. In a complete System Description a MultiplexedIPdu shall contain a Dynamic Part. The following use cases support the multiplicity to be 0..1: • If a MultiplexedIPdu is received by a Pdu Gateway and is not delivered to the IPduM but routed directly to a bus interface then the content of the MulitplexedIPdu doesn't need to be described in the System Extract/ Ecu Extract. • If a MultiplexedIPdu is received by an ECU which is only interested in the static part of the MultiplexedIPdu then the dynamicPart does not need to be described in the System Extract/Ecu Extract. atpVariation: Content of a multiplexed PDU can vary. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=dynamicPart, dynamicPart.variation Point.shortLabel vh.latestBindingTime=postBuild

        """
        return self.dynamicPart

    def setDynamicPart(self, value: Optional[DynamicPart]) -> MultiplexedIPdu:
        """
        According to the value of the selector field some parts of the IPdu have a different layout. In a complete System Description a MultiplexedIPdu shall contain a Dynamic Part. The following use cases support the multiplicity to be 0..1: • If a MultiplexedIPdu is received by a Pdu Gateway and is not delivered to the IPduM but routed directly to a bus interface then the content of the MulitplexedIPdu doesn't need to be described in the System Extract/ Ecu Extract. • If a MultiplexedIPdu is received by an ECU which is only interested in the static part of the MultiplexedIPdu then the dynamicPart does not need to be described in the System Extract/Ecu Extract. atpVariation: Content of a multiplexed PDU can vary. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=dynamicPart, dynamicPart.variation Point.shortLabel vh.latestBindingTime=postBuild

        A None value is a no-op and does not overwrite an existing dynamicPart.
        """
        if value is not None:
            self.dynamicPart = value
        return self

    def getSelectorFieldByteOrder(self) -> Optional[ByteOrderEnum]:
        """
        This attribute defines the order of the bytes of the selector Field and the packing into the MultiplexedIPdu. Please consider that [constr_3247] and [constr_3223] are restricting the usage of this attribute. In a complete System Description this attribute is mandatory. If a MultiplexedPdu is received by a Pdu Gateway and is not delivered to the IPduM but routed directly to a bus interface then the content of the MulitplexedPdu doesn't need to be described in the System Extract/Ecu Extract. To support this use case the multiplicity is set to 0..1.

        """
        return self.selectorFieldByteOrder

    def setSelectorFieldByteOrder(self, value: Optional[ByteOrderEnum]) -> MultiplexedIPdu:
        """
        This attribute defines the order of the bytes of the selector Field and the packing into the MultiplexedIPdu. Please consider that [constr_3247] and [constr_3223] are restricting the usage of this attribute. In a complete System Description this attribute is mandatory. If a MultiplexedPdu is received by a Pdu Gateway and is not delivered to the IPduM but routed directly to a bus interface then the content of the MulitplexedPdu doesn't need to be described in the System Extract/Ecu Extract. To support this use case the multiplicity is set to 0..1.

        A None value is a no-op and does not overwrite an existing selectorFieldByteOrder.
        """
        if value is not None:
            self.selectorFieldByteOrder = value
        return self

    def getSelectorFieldLength(self) -> Optional[Integer]:
        """
        The size in bits of the selector field shall be configurable in a range of 1-16 bits. In a complete System Description this attribute is mandatory. If a MultiplexedPdu is received by a Pdu Gateway and is not delivered to the IPduM but routed directly to a bus interface then the content of the MulitplexedPdu doesn't need to be described in the System Extract/Ecu Extract. To support this use case the multiplicity is set to 0..1.

        """
        return self.selectorFieldLength

    def setSelectorFieldLength(self, value: Optional[Integer]) -> MultiplexedIPdu:
        """
        The size in bits of the selector field shall be configurable in a range of 1-16 bits. In a complete System Description this attribute is mandatory. If a MultiplexedPdu is received by a Pdu Gateway and is not delivered to the IPduM but routed directly to a bus interface then the content of the MulitplexedPdu doesn't need to be described in the System Extract/Ecu Extract. To support this use case the multiplicity is set to 0..1.

        A None value is a no-op and does not overwrite an existing selectorFieldLength.
        """
        if value is not None:
            self.selectorFieldLength = value
        return self

    def getSelectorFieldStartPosition(self) -> Optional[Integer]:
        """
        This parameter is necessary to describe the position of the selector field within the IPdu. Note that the absolute position of the selectorField in the MultiplexedIPdu is determined by the definition of the selectorFieldByteOrder attribute of the Multiplexed Pdu. If Big Endian is specified, the start position indicates the bit position of the most significant bit in the IPdu. If Little Endian is specified, the start position indicates the bit position of the least significant bit in the IPdu. In AUTOSAR the bit counting is always set to "sawtooth" and the bit order is set to "Decreasing". The bit counting in byte 0 starts with bit 0 (least significant bit). The most significant bit in byte 0 is bit 7. In a complete System Description this attribute is mandatory. If a MultiplexedPdu is received by a Pdu Gateway and is not delivered to the IPduM but routed directly to a bus interface then the content of the MulitplexedPdu doesn't need to be described in the System Extract/Ecu Extract. To support this use case the multiplicity is set to 0..1.

        """
        return self.selectorFieldStartPosition

    def setSelectorFieldStartPosition(self, value: Optional[Integer]) -> MultiplexedIPdu:
        """
        This parameter is necessary to describe the position of the selector field within the IPdu. Note that the absolute position of the selectorField in the MultiplexedIPdu is determined by the definition of the selectorFieldByteOrder attribute of the Multiplexed Pdu. If Big Endian is specified, the start position indicates the bit position of the most significant bit in the IPdu. If Little Endian is specified, the start position indicates the bit position of the least significant bit in the IPdu. In AUTOSAR the bit counting is always set to "sawtooth" and the bit order is set to "Decreasing". The bit counting in byte 0 starts with bit 0 (least significant bit). The most significant bit in byte 0 is bit 7. In a complete System Description this attribute is mandatory. If a MultiplexedPdu is received by a Pdu Gateway and is not delivered to the IPduM but routed directly to a bus interface then the content of the MulitplexedPdu doesn't need to be described in the System Extract/Ecu Extract. To support this use case the multiplicity is set to 0..1.

        A None value is a no-op and does not overwrite an existing selectorFieldStartPosition.
        """
        if value is not None:
            self.selectorFieldStartPosition = value
        return self

    def getStaticPart(self) -> Optional[StaticPart]:
        """
        The static part of the multiplexed IPdu is the same regardless of the selector field. The static part is optional. atpVariation: Content of a multiplexed PDU can vary. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=staticPart, staticPart.variationPoint.short Label vh.latestBindingTime=postBuild

        """
        return self.staticPart

    def setStaticPart(self, value: Optional[StaticPart]) -> MultiplexedIPdu:
        """
        The static part of the multiplexed IPdu is the same regardless of the selector field. The static part is optional. atpVariation: Content of a multiplexed PDU can vary. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=staticPart, staticPart.variationPoint.short Label vh.latestBindingTime=postBuild

        A None value is a no-op and does not overwrite an existing staticPart.
        """
        if value is not None:
            self.staticPart = value
        return self

    def getTriggerMode(self) -> Optional[TriggerMode]:
        """
        IPduM can be configured to send a transmission request for the new multiplexed IPdu to the PDU-Router because of the trigger conditions/ modes that are described in the TriggerMode enumeration. In a complete System Description this attribute is mandatory. If a MultiplexedPdu is received by a Pdu Gateway and is not delivered to the IPduM but routed directly to a bus interface then the content of the MulitplexedPdu doesn't need to be described in the System Extract/Ecu Extract. To support this use case the multiplicity is set to 0..1.

        """
        return self.triggerMode

    def setTriggerMode(self, value: Optional[TriggerMode]) -> MultiplexedIPdu:
        """
        IPduM can be configured to send a transmission request for the new multiplexed IPdu to the PDU-Router because of the trigger conditions/ modes that are described in the TriggerMode enumeration. In a complete System Description this attribute is mandatory. If a MultiplexedPdu is received by a Pdu Gateway and is not delivered to the IPduM but routed directly to a bus interface then the content of the MulitplexedPdu doesn't need to be described in the System Extract/Ecu Extract. To support this use case the multiplicity is set to 0..1.

        A None value is a no-op and does not overwrite an existing triggerMode.
        """
        if value is not None:
            self.triggerMode = value
        return self

    def getUnusedBitPattern(self) -> Optional[Integer]:
        """
        AUTOSAR COM and AUTOSAR IPDUM are filling not used areas of an IPdu with this bit-pattern. This attribute is mandatory to avoid undefined behavior. This byte-pattern will be repeated throughout the IPdu. In a complete System Description this attribute is mandatory. If a MultiplexedPdu is received by a Pdu Gateway and is not delivered to the IPduM but routed directly to a bus interface then the content of the MulitplexedPdu doesn't need to be described in the System Extract/Ecu Extract. To support this use case the multiplicity is set to 0..1.

        """
        return self.unusedBitPattern

    def setUnusedBitPattern(self, value: Optional[Integer]) -> MultiplexedIPdu:
        """
        AUTOSAR COM and AUTOSAR IPDUM are filling not used areas of an IPdu with this bit-pattern. This attribute is mandatory to avoid undefined behavior. This byte-pattern will be repeated throughout the IPdu. In a complete System Description this attribute is mandatory. If a MultiplexedPdu is received by a Pdu Gateway and is not delivered to the IPduM but routed directly to a bus interface then the content of the MulitplexedPdu doesn't need to be described in the System Extract/Ecu Extract. To support this use case the multiplicity is set to 0..1.

        A None value is a no-op and does not overwrite an existing unusedBitPattern.
        """
        if value is not None:
            self.unusedBitPattern = value
        return self


class GeneralPurposePdu(Pdu):
    """
    This element is used for AUTOSAR Pdus without additional attributes that are routed by a bus interface. Please note that the category name of such Pdus is standardized in the AUTOSAR System Template. Tags: atp.recommendedPackage=Pdus

    [constr_3081] Value of category in GeneralPurposePdu: The attribute category of GeneralPurposePdu can have the following values: SD (Service Discovery), GLOBAL_TIME, DoIP
    """

    # GeneralPurposePdu method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.25, p.344 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class GeneralPurposeIPdu(IPdu):
    """
    This element is used for AUTOSAR Pdus without attributes that are routed by the PduR. Please note that the category name of such Pdus is standardized in the AUTOSAR System Template. Tags: atp.recommendedPackage=Pdus

    [constr_3082] Value of category in GeneralPurposeIPdu: The attribute category of GeneralPurposeIPdu can have the following values: XCP, SOMEIP_SEGMENTED_IPDU, DLT, IDS
    """

    # GeneralPurposeIPdu method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.26, p.345 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

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
        if not self.IsReferrableElementExists(short_name, SecureCommunicationAuthenticationProps):
            props = SecureCommunicationAuthenticationProps(self, short_name)
            self.addReferrableElement(props)
            self.authenticationProps.append(props)
        return cast(SecureCommunicationAuthenticationProps, self.getReferrableElement(short_name, SecureCommunicationAuthenticationProps))

    def getAuthenticationProps(self) -> List[SecureCommunicationAuthenticationProps]:
        """
        Authentication properties used to configure Secured IPdus.
        """
        return self.authenticationProps

    def createSecureCommunicationFreshnessProps(self, short_name: str) -> SecureCommunicationFreshnessProps:
        """
        Freshness properties used to configure SecuredIPdus.
        """
        if not self.IsReferrableElementExists(short_name, SecureCommunicationFreshnessProps):
            props = SecureCommunicationFreshnessProps(self, short_name)
            self.addReferrableElement(props)
            self.freshnessProps.append(props)
        return cast(SecureCommunicationFreshnessProps, self.getReferrableElement(short_name, SecureCommunicationFreshnessProps))

    def getFreshnessProps(self) -> List[SecureCommunicationFreshnessProps]:
        """
        Freshness properties used to configure SecuredIPdus.
        """
        return self.freshnessProps


class UserDefinedPdu(Pdu):
    """
    UserDefinedPdu allows to describe PDU-based communication over Complex Drivers. If a new BSW module is added above the BusIf (e.g. a new Nm module) then this Pdu element shall be used to describe the communication. Tags: atp.recommendedPackage=Pdus
    """

    # UserDefinedPdu method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.27, p.345 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getCddType   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setCddType   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This attribute defines the CDD that transmits or receives the UserDefinedIPdu. If several CDDs are defined this attribute is used to distinguish between them.
        self.cddType: Optional[String] = None

    def getCddType(self) -> Optional[String]:
        """
        This attribute defines the CDD that transmits or receives the UserDefinedIPdu. If several CDDs are defined this attribute is used to distinguish between them.
        """
        return self.cddType

    def setCddType(self, value: Optional[String]) -> UserDefinedPdu:
        """
        This attribute defines the CDD that transmits or receives the UserDefinedIPdu. If several CDDs are defined this attribute is used to distinguish between them.
        A None value is a no-op and does not overwrite an existing cddType.
        """
        if value is not None:
            self.cddType = value
        return self


class UserDefinedIPdu(IPdu):
    """
    UserDefinedIPdu allows to describe PDU-based communication over Complex Drivers. If a new BSW module is added above the PduR (e.g. a Diagnostic Service ) then this IPdu element shall be used to describe the communication. Tags: atp.recommendedPackage=Pdus
    """

    # UserDefinedIPdu method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.28, p.346 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getCddType   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setCddType   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This attribute defines the CDD that transmits or receives the UserDefinedPdu. If several CDDs are defined this attribute is used to distinguish between them.
        self.cddType: Optional[String] = None

    def getCddType(self) -> Optional[String]:
        """
        This attribute defines the CDD that transmits or receives the UserDefinedPdu. If several CDDs are defined this attribute is used to distinguish between them.
        """
        return self.cddType

    def setCddType(self, value: Optional[String]) -> UserDefinedIPdu:
        """
        This attribute defines the CDD that transmits or receives the UserDefinedPdu. If several CDDs are defined this attribute is used to distinguish between them.
        A None value is a no-op and does not overwrite an existing cddType.
        """
        if value is not None:
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

    def setAuthInfoTxLength(self, value: Optional[PositiveInteger]) -> SecureCommunicationAuthenticationProps:
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

    def setFreshnessCounterSyncAttempts(self, value: Optional[PositiveInteger]) -> SecureCommunicationFreshnessProps:
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

    def setFreshnessTimestampTimePeriodFactor(self, value: Optional[PositiveInteger]) -> SecureCommunicationFreshnessProps:
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

    def setFreshnessValueLength(self, value: Optional[PositiveInteger]) -> SecureCommunicationFreshnessProps:
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

    def setFreshnessValueTxLength(self, value: Optional[PositiveInteger]) -> SecureCommunicationFreshnessProps:
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

    def setUseFreshnessTimestamp(self, value: Optional[Boolean]) -> SecureCommunicationFreshnessProps:
        """
        This attribute specifies whether the Freshness Value is generated through individual Freshness Counters or by a Timestamps. The value is set to TRUE when Timestamps are used.
        A None value is a no-op and does not overwrite an existing useFreshnessTimestamp.
        """
        if value is not None:
            self.useFreshnessTimestamp = value
        return self


class CommunicationDirectionType(AREnum):
    """
    Describes the communication direction.
    """

    # CommunicationDirectionType method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.33, p.351 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods) — enum value form serialized on CommConnectorPort.communicationDirection, IEEE1722TpConnection.communicationDirection, IPSecRule.direction, ISignalIPduGroup.communicationDirection
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # Reception (Input) Tags: atp.EnumerationLiteralIndex=0
    IN = "IN"

    # Transmission (Output) Tags: atp.EnumerationLiteralIndex=1
    OUT = "OUT"

    def __init__(self):
        super().__init__([CommunicationDirectionType.IN, CommunicationDirectionType.OUT])


class FramePort(CommConnectorPort):
    """
    Connectors reception or send port on the referenced channel referenced by a FrameTriggering.
    """

    # FramePort method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.2, p.304 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class IPduSignalProcessingEnum(AREnum):
    """
    Definition of signal processing modes.
    """

    # IPduSignalProcessingEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.4, p.305
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods) — enum value form serialized on IPduPort.iPduSignalProcessing
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # The signal indications / confirmations are deferred. Tags: atp.EnumerationLiteralIndex=0
    DEFERRED = "DEFERRED"

    # The signal indications / confirmations are performed. Tags: atp.EnumerationLiteralIndex=1
    IMMEDIATE = "IMMEDIATE"

    def __init__(self):
        super().__init__([IPduSignalProcessingEnum.DEFERRED, IPduSignalProcessingEnum.IMMEDIATE])


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
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                       [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getIPduSignalProcessing        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setIPduSignalProcessing        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getRxSecurityVerification      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setRxSecurityVerification      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTimestampRxAcceptanceWindow [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTimestampRxAcceptanceWindow [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getUseAuthDataFreshness        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setUseAuthDataFreshness        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

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

    def setIPduSignalProcessing(self, value: Optional[IPduSignalProcessingEnum]) -> IPduPort:
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

    def setRxSecurityVerification(self, value: Optional[Boolean]) -> IPduPort:
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

    def setTimestampRxAcceptanceWindow(self, value: Optional[TimeValue]) -> IPduPort:
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

    def setUseAuthDataFreshness(self, value: Optional[Boolean]) -> IPduPort:
        """
        This attribute describes whether a part of AuthenticPdu contained in a SecuredIPdu shall be passed on to the SWC that verifies and generates the Freshness. The part of the Authentic-PDU is defined by the authData FreshnessStartPosition and authDataFreshnessLength.
        A None value is a no-op and does not overwrite an existing useAuthDataFreshness.
        """
        if value is not None:
            self.useAuthDataFreshness = value
        return self


class ISignalPort(CommConnectorPort):
    """
    Connectors reception or send port on the referenced channel referenced by an ISignalTriggering. If different timeouts or DataFilters for ISignals need to be specified several ISignalPorts may be created.
    """

    # ISignalPort method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.5, p.306 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__            [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getDataFilter       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDataFilter       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDdsQosProfileRef [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDdsQosProfileRef [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getFirstTimeout     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setFirstTimeout     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getHandleInvalid    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setHandleInvalid    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTimeout          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTimeout          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Optional specification of a signal COM filter at the receiver side in case that the System Description doesn't use a complete Software Component Description (VFB View). This supports the inclusion of legacy system signals. If a full DataMapping exist for the SystemSignal this information may be available from a configured ReceiverComSpec. In this case the ReceiverComSpec overrides this optional specification.
        self.dataFilter: Optional[DataFilter] = None

        # Reference to the DDS Qos profile used for this ISignal. Tags: atp.Status=candidate
        self.ddsQosProfileRef: Optional[RefType] = None

        # • ISignalPort with communicationDirection = in: Optional first timeout value in seconds for the reception of the ISignal. • ISignalPort with communicationDirection = out: Optional first timeout value in seconds for transmission deadline monitoring.
        self.firstTimeout: Optional[TimeValue] = None

        # This attribute defines how invalidation is applied to the ISignals received in the context of this ISignalPort.
        self.handleInvalid: Optional[HandleInvalidEnum] = None

        # • ISignalPort with communicationDirection = in: Optional timeout value in seconds for the reception of the ISignal. The attribute value is used to configure the Com Timeout in the COM module. The RTE ignores this attribute. The timeout can also be specified with the NonqueuedReceiverComSpec.aliveTimeout attribute. If a full DataMapping exists for the SystemSignal and the value is available in the configured ReceiverComSpec, then the timeout value in the ReceiverComSpec overrides this optional timeout specification during the creation of the Base Ecu Configuration of the COM module. • ISignalPort with communicationDirection = out: Optional timeout value in seconds for the transmission of the ISignal. The attribute value is used to configure the ComTimeout in the COM module. The RTE ignores this attribute. The timeout can also be specified with the ender ComSpec.transmissionAcknowledge.timeout attribute. If a full DataMapping exists for the SystemSignal and the value is available in the configured SenderComSpec, then the timeout value in the SenderComSpec overrides this optional timeout specification during the creation of the Base Ecu Configuration of the COM module. This attribute can be used in the following cases: • legacy signal where the System Description doesn't use a complete Software Component Description (VFB View) and where the DataMapping is missing. • bus monitoring use cases in which the DataMapping is ignored.
        self.timeout: Optional[TimeValue] = None

    def getDataFilter(self) -> Optional[DataFilter]:
        """
        Optional specification of a signal COM filter at the receiver side in case that the System Description doesn't use a complete Software Component Description (VFB View). This supports the inclusion of legacy system signals. If a full DataMapping exist for the SystemSignal this information may be available from a configured ReceiverComSpec. In this case the ReceiverComSpec overrides this optional specification.
        """
        return self.dataFilter

    def setDataFilter(self, value: Optional[DataFilter]) -> ISignalPort:
        """
        Optional specification of a signal COM filter at the receiver side in case that the System Description doesn't use a complete Software Component Description (VFB View). This supports the inclusion of legacy system signals. If a full DataMapping exist for the SystemSignal this information may be available from a configured ReceiverComSpec. In this case the ReceiverComSpec overrides this optional specification.
        A None value is a no-op and does not overwrite an existing dataFilter.
        """
        if value is not None:
            self.dataFilter = value
        return self

    def getDdsQosProfileRef(self) -> Optional[RefType]:
        """
        Reference to the DDS Qos profile used for this ISignal. Tags: atp.Status=candidate
        """
        return self.ddsQosProfileRef

    def setDdsQosProfileRef(self, value: Optional[RefType]) -> ISignalPort:
        """
        Reference to the DDS Qos profile used for this ISignal. Tags: atp.Status=candidate
        A None value is a no-op and does not overwrite an existing ddsQosProfileRef.
        """
        if value is not None:
            self.ddsQosProfileRef = value
        return self

    def getFirstTimeout(self) -> Optional[TimeValue]:
        """
        • ISignalPort with communicationDirection = in: Optional first timeout value in seconds for the reception of the ISignal. • ISignalPort with communicationDirection = out: Optional first timeout value in seconds for transmission deadline monitoring.
        """
        return self.firstTimeout

    def setFirstTimeout(self, value: Optional[TimeValue]) -> ISignalPort:
        """
        • ISignalPort with communicationDirection = in: Optional first timeout value in seconds for the reception of the ISignal. • ISignalPort with communicationDirection = out: Optional first timeout value in seconds for transmission deadline monitoring.
        A None value is a no-op and does not overwrite an existing firstTimeout.
        """
        if value is not None:
            self.firstTimeout = value
        return self

    def getHandleInvalid(self) -> Optional[HandleInvalidEnum]:
        """
        This attribute defines how invalidation is applied to the ISignals received in the context of this ISignalPort.
        """
        return self.handleInvalid

    def setHandleInvalid(self, value: Optional[HandleInvalidEnum]) -> ISignalPort:
        """
        This attribute defines how invalidation is applied to the ISignals received in the context of this ISignalPort.
        A None value is a no-op and does not overwrite an existing handleInvalid.
        """
        if value is not None:
            self.handleInvalid = value
        return self

    def getTimeout(self) -> Optional[TimeValue]:
        """
        • ISignalPort with communicationDirection = in: Optional timeout value in seconds for the reception of the ISignal. The attribute value is used to configure the Com Timeout in the COM module. The RTE ignores this attribute. The timeout can also be specified with the NonqueuedReceiverComSpec.aliveTimeout attribute. If a full DataMapping exists for the SystemSignal and the value is available in the configured ReceiverComSpec, then the timeout value in the ReceiverComSpec overrides this optional timeout specification during the creation of the Base Ecu Configuration of the COM module. • ISignalPort with communicationDirection = out: Optional timeout value in seconds for the transmission of the ISignal. The attribute value is used to configure the ComTimeout in the COM module. The RTE ignores this attribute. The timeout can also be specified with the ender ComSpec.transmissionAcknowledge.timeout attribute. If a full DataMapping exists for the SystemSignal and the value is available in the configured SenderComSpec, then the timeout value in the SenderComSpec overrides this optional timeout specification during the creation of the Base Ecu Configuration of the COM module. This attribute can be used in the following cases: • legacy signal where the System Description doesn't use a complete Software Component Description (VFB View) and where the DataMapping is missing. • bus monitoring use cases in which the DataMapping is ignored.
        """
        return self.timeout

    def setTimeout(self, value: Optional[TimeValue]) -> ISignalPort:
        """
        • ISignalPort with communicationDirection = in: Optional timeout value in seconds for the reception of the ISignal. The attribute value is used to configure the Com Timeout in the COM module. The RTE ignores this attribute. The timeout can also be specified with the NonqueuedReceiverComSpec.aliveTimeout attribute. If a full DataMapping exists for the SystemSignal and the value is available in the configured ReceiverComSpec, then the timeout value in the ReceiverComSpec overrides this optional timeout specification during the creation of the Base Ecu Configuration of the COM module. • ISignalPort with communicationDirection = out: Optional timeout value in seconds for the transmission of the ISignal. The attribute value is used to configure the ComTimeout in the COM module. The RTE ignores this attribute. The timeout can also be specified with the ender ComSpec.transmissionAcknowledge.timeout attribute. If a full DataMapping exists for the SystemSignal and the value is available in the configured SenderComSpec, then the timeout value in the SenderComSpec overrides this optional timeout specification during the creation of the Base Ecu Configuration of the COM module. This attribute can be used in the following cases: • legacy signal where the System Description doesn't use a complete Software Component Description (VFB View) and where the DataMapping is missing. • bus monitoring use cases in which the DataMapping is ignored.
        A None value is a no-op and does not overwrite an existing timeout.
        """
        if value is not None:
            self.timeout = value
        return self


class EthernetFrameTriggering(FrameTriggering):
    pass


class J1939DcmIPdu(IPdu):
    pass
