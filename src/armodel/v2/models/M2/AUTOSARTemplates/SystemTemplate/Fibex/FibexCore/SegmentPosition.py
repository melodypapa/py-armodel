from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    ByteOrderEnum,
    Integer,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class SegmentPosition(ARObject):
    """
    that the absolute position of the segment in the MultiplexedIPdu is
    determined by the definition of the segmentByteOrder attribute of the
    SegmentPosition. If Big Endian is specified, the start position indicates
    the bit position of the most significant bit in the IPdu. If Little Endian
    is specified, the start position indicates the bit position of the least
    significant bit in the IPdu. In AUTOSAR the bit counting is always set to
    "sawtooth" and the bit order is set to "Decreasing". The bit counting in
    byte 0 starts with bit 0 (least significant bit). The most significant bit
    in byte 0 is bit 7. Table 6.77: SegmentPosition [constr_9182] Existence of
    SegmentPosition.segmentByteOrder (cid:100)For each SegmentPosition, the
    attribute segmentByteOrder shall exist at the time when the System
    Description is complete.(cid:99)() [constr_9183] Existence of
    SegmentPosition.segmentLength (cid:100)For each Seg- mentPosition, the
    attribute segmentLength shall exist at the time when the System Description
    is complete.(cid:99)() [constr_9184] Existence of
    SegmentPosition.segmentPosition (cid:100)For each SegmentPosition, the
    attribute segmentPosition shall exist at the time when the System
    Description is complete.(cid:99)() [constr_3247] Byte order mix within a
    MultiplexedIPdu is not allowed (cid:100)The segmentByteOrder of all
    SegmentPositions and the selectorFieldByte- Order shall have the same value
    in the MultiplexedIPdu.(cid:99)() [constr_3223] No ByteOrderEnum.opaque
    allowed for MultiplexedIPdu.se- lectorFieldByteOrder (cid:100)The values of
    MultiplexedIPdu.selectorFieldBy- teOrder are restricted to
    ByteOrderEnum.mostSignificantByteFirst and
    ByteOrderEnum.mostSignificantByteLast. I.e. the value ByteOrderEnum. opaque
    is not allowed.(cid:99)() [constr_3224] No ByteOrderEnum.opaque allowed for
    SegmentPosition.seg- mentByteOrder. (cid:100)The values of
    SegmentPosition.segmentByteOrder are re- stricted to
    ByteOrderEnum.mostSignificantByteFirst and ByteOrderEnum. 412 of 2090
    Document ID 63: AUTOSAR_CP_TPS_SystemTemplate System Template AUTOSAR CP
    R23-11 mostSignificantByteLast. I.e. the value ByteOrderEnum.opaque is not
    al- lowed.(cid:99)() Figure 6.26 shows an example of an IPdu Multiplexer.
    The static part of the multiplexed IPdu contains ComIPduA. The value of the
    selector field in the dynamic part decides which content is transmitted.
    ComIPduB is transmitted if the selector field value is "0". ComIPduC is
    transmitted if the selector field value is "1". The static and the dynamic
    part can consist of more than one element. These sub parts of the static or
    dynamic parts are called segments. In Figure 6.26 the dynamic Part is
    segmented into two parts. More details can be found in [23]. MuxPdu:
    MultiplexedIPdu selectorFieldLength = 1 length = 64
    selectorFieldStartPosition = 0 staticSegment: SegmentPosition :StaticPart
    segmentLength = 16 segmentPosition = 32 :DynamicPart dynamicSegment1:
    SegmentPosition segmentLength = 31 segmentPosition = 1 PduA: ISignalIPdu
    dynamicSegment2: SegmentPosition segmentLength = 16 segmentPosition = 48
    PduC: ISignalIPdu alternative1: DynamicPartAlternative selectorFieldCode = 1
    PduB: ISignalIPdu alternative2: DynamicPartAlternative selectorFieldCode = 0
    Figure 6.26: I-Pdu Multiplexer Example Each of the following figures shows
    an example with an allowed IPduM configuration. Please note that the AUTOSAR
    IPduM module does not shift any part (static or dy- namic) IPdu and just
    merges the payload. ISignalIPdus that are referenced by the different
    DynamicPartAlternatives in one MultiplexedIPdu shall always have the same
    length. A configuration may be optimized with respect to unused data at end
    of a StaticPart ISignalIPdu. This is shown in figure 6.27 where the
    ISignalIPdu that is referenced by the StaticPart is shorter than the Multi-
    plexedIPdu. An optimization with respect to unused data at end of
    DynamicPar- tAlternative ISignalIPdus is shown in figure 6.28. 413 of 2090
    Document ID 63: AUTOSAR_CP_TPS_SystemTemplate System Template AUTOSAR CP
    R23-11 0 48 64 MultiplexedPdu: Switch DynamicPart StaticPart DynamicPart
    All(cid:2)dynamic part Referenced ISignalIPdus:(cid:2)(cid:2)
    alternatives(cid:2)have the 0 8 same(cid:2)size,(cid:2)even if
    alternatives(cid:2)contain DynamicPartAlternative: 1 Signal1 Signal2 unused
    areas. 0 8 DynamicPartAlternative: 2 Signal3 Signal4 Signal5 0 8
    DynamicPartAlternative: 3 Signal3 Signal4 Signal6 0 The(cid:2)static
    StaticPart: Signal6 part may be shorter Figure 6.27: Multiplexer
    configuration example optimized with respect to unused data at end of static
    part Pdu 0 48 64 MultiplexedPdu: Switch DynamicPart StaticPart Referenced
    ISignalIPdus:(cid:2)(cid:2) 0 8 DynamicPartAlternative: 1 Signal1 Signal2
    All(cid:2)dynamic part The(cid:2)dynamic alternatives(cid:2)have the parts
    may be same(cid:2)size,(cid:2)even if 0 8 alternatives(cid:2)contain shorter
    than the static part unused areas. DynamicPartAlternative: 2 Signal3 Signal4
    0 8 DynamicPartAlternative: 3 Signal3 Signal4 Signal5 0 48 StaticPart:
    Signal6 Figure 6.28: Multiplexer configuration example optimized with
    respect to unused data at end of dynamic part Pdus 414 of 2090 Document ID
    63: AUTOSAR_CP_TPS_SystemTemplate System Template AUTOSAR CP R23-11 6.5.1
    I-Pdu Multiplexer in System Extract/ECU Extract The processing in the ECU
    determines the description of MultiplexedIPdus in the System Extract/Ecu
    Extract. In case that a Gateway ECU only routes a Multi- plexedIPdu without
    being interested in the content leads to a reduced description in the System
    Extract/ECU Extract. The following items describe the different scenar- ios
    and the consequences for the System Extract/ECU Extract description. A
    complete System Description contains all information. [TPS_SYST_01080]
    Sending or receiving of a MultiplexedIPdu in System Ex- tract/ECU Extract
    (cid:100) • all attributes of the MultiplexedIPdu are mandatory • aggregated
    DynamicPart with associated ISignalIPdus is mandatory in case – of sending –
    of receiving if at least one DynamicPartAlternative is received by one Ecu
    of the Extract. • a PduTriggering shall be defined for the MultiplexedIPdu •
    a PduTriggering shall be defined for all included ISignalIPdus in the Dy-
    namicPart and StaticPart (cid:99)() The initial ECU Configuration Generator
    configures COM, PduR, IpduM and lower lay- ers with the information from the
    System Extract/ECU Extract. [TPS_SYST_01081] Gatewaying of a MultiplexedIPdu
    in System Extract/ECU Extract (cid:100) • StaticPart and DynamicPart
    definitions shall be omitted, thus no ISig- nalIPdu description shall be
    included • all attributes of the MultiplexedIPdu shall be omitted. • a
    PduTriggering shall be defined only for the gatewayed MultiplexedIPdu • an
    IPduMapping between the source and the target PduTriggerings shall be
    defined (cid:99)() The initial ECU Configuration Generator configures PduR
    and lower layers with the information from the System Extract/ECU Extract.
    [TPS_SYST_01082] Receiving and gatewaying of a MultiplexedIPdu in System
    Extract/ECU Extract (cid:100) • all attributes of the MultiplexedIPdu are
    mandatory 415 of 2090 Document ID 63: AUTOSAR_CP_TPS_SystemTemplate System
    Template AUTOSAR CP R23-11 • aggregated DynamicPart with associated
    ISignalIPdus is mandatory in case at least one DynamicPartAlternative is
    received by one Ecu of the Extract. • a PduTriggering shall be defined for
    the MultiplexedIPdu • an IPduMapping between the source and the target
    PduTriggerings shall be defined • a PduTriggering shall be defined for all
    included ISignalIPdus in the Dy- namicPart and StaticPart (cid:99)() The
    initial ECU Configuration Generator configures Com, PduR, IpduM and lower
    lay- ers with the information from the System Extract/ECU Extract. 416 of
    2090 Document ID 63: AUTOSAR_CP_TPS_SystemTemplate System Template AUTOSAR
    CP R23-11 6.6 Frames Identifiable PhysicalChannel Identifiable
    FrameTriggering FibexElement Frame + frameLength: Integer [0..1]
    Identifiable «atpPrototype» FibexElement PduToFrameMapping
    UploadableDesignElement Pdu + packingByteOrder: ByteOrderEnum [0..1] +
    startPosition: Integer [0..1] + hasDynamicLength: Boolean [0..1] +
    updateIndicationBitPosition: Integer [0..1] + length: UnlimitedInteger
    [0..1] (cid:1) (cid:16) (cid:4) (cid:23) (cid:14) (cid:2) (cid:17) (cid:8)
    (cid:24) (cid:3) (cid:4) (cid:18) (cid:19) (cid:14) (cid:23) (cid:5) (cid:2)
    (cid:3) (cid:3) (cid:21) (cid:3) (cid:18) (cid:29) (cid:20) (cid:26)
    (cid:30) (cid:2) (cid:25) (cid:6) (cid:7) (cid:2) (cid:14) (cid:3) (cid:21)
    (cid:7) (cid:19) (cid:22) (cid:14) (cid:20) (cid:1) (cid:16) (cid:4) (cid:3)
    (cid:7) (cid:3) (cid:6) (cid:2) (cid:17) (cid:8) (cid:7) (cid:8) (cid:9)
    (cid:7) (cid:27) (cid:3) (cid:4) (cid:18) (cid:19) (cid:14) (cid:9) (cid:22)
    (cid:3) (cid:2) (cid:3) (cid:7) (cid:12) (cid:5) (cid:3) (cid:21) (cid:10)
    (cid:9) (cid:20) (cid:8) (cid:2) (cid:25) (cid:12) (cid:13) (cid:28) (cid:6)
    (cid:7) (cid:14) (cid:3) (cid:7) (cid:19) (cid:2) (cid:12) (cid:3) (cid:2)
    (cid:21) (cid:22) (cid:13) (cid:7) (cid:23) (cid:2) (cid:9) (cid:3) (cid:7)
    (cid:8) (cid:7) (cid:9) (cid:14) (cid:15) (cid:20) (cid:22) (cid:9) (cid:22)
    (cid:2) (cid:10) (cid:7) (cid:9) (cid:24) (cid:6) (cid:22) (cid:12) (cid:13)
    (cid:2) (cid:12) (cid:13) (cid:7) (cid:23) (cid:14) (cid:15) (cid:20)
    (cid:24) +managedPhysicalChannel 0..* «atpVariation,atpSplitable»
    +frameTriggering 0..* +frame 0..1 «atpVariation,atpSplitable»
    +pduToFrameMapping 0..* +pdu 0..1 Figure 6.29: Frame Overview (FibexCore:
    FrameOverview) [TPS_SYST_01083] Frame (cid:100)A Frame represents a general
    design object that is used to describe the layout of the included Pdus as a
    reusable asset.(cid:99)() [TPS_SYST_01084] FrameTriggering (cid:100)The
    FrameTriggering implements the reusable definition of a Frame within a
    concrete context and thus defines a Frame’s send behavior and identification
    on a certain PhysicalChannel.(cid:99)() [TPS_SYST_02255] Frame.frameLength
    usage for FlexrayFrames and Can- Frames (cid:100)The frameLength for a
    FlexrayFrame shall be equal or larger than the combined length of all Pdus
    that are mapped to the frame. The frameLength for a CanFrame is used to
    describe the minimum length of a re- ceived L-PDU to be accepted by a data
    length check. Therefore, it is possible to configure a frameLength which is
    smaller than the mapped Pdu to this frame. If data length check is not
    needed the frameLength of a CanFrame may be left unde- fined. The reason for
    that is that if the CanFrame.frameLength is larger than the Pdu.length of
    the mapped Pdu and data length check is used, a received Pdu will always be
    discarded due to a failing minimum length check.(cid:99)() 417 of 2090
    Document ID 63: AUTOSAR_CP_TPS_SystemTemplate System Template AUTOSAR CP
    R23-11

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication::SegmentPosition

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 412, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute defines the order of the bytes of the and the packing into the
                # MultiplexedIPdu.
        # that [constr_3247] and [constr_3224] are usage of this attribute.
        self._segmentByte: Optional["ByteOrderEnum"] = None

    @property
    def segment_byte(self) -> Optional["ByteOrderEnum"]:
        """Get segmentByte (Pythonic accessor)."""
        return self._segmentByte

    @segment_byte.setter
    def segment_byte(self, value: Optional["ByteOrderEnum"]) -> None:
        """
        Set segmentByte with validation.

        Args:
            value: The segmentByte to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._segmentByte = None
            return

        if not isinstance(value, ByteOrderEnum):
            raise TypeError(
                f"segmentByte must be ByteOrderEnum or None, got {type(value).__name__}"
            )
        self._segmentByte = value
        # Data Length of the segment in bits.
        self._segmentLength: Optional["Integer"] = None

    @property
    def segment_length(self) -> Optional["Integer"]:
        """Get segmentLength (Pythonic accessor)."""
        return self._segmentLength

    @segment_length.setter
    def segment_length(self, value: Optional["Integer"]) -> None:
        """
        Set segmentLength with validation.

        Args:
            value: The segmentLength to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._segmentLength = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"segmentLength must be Integer or None, got {type(value).__name__}"
            )
        self._segmentLength = value
        # Segments bit position relatively to the beginning of a IPdu.
        self._segment: Optional["Integer"] = None

    @property
    def segment(self) -> Optional["Integer"]:
        """Get segment (Pythonic accessor)."""
        return self._segment

    @segment.setter
    def segment(self, value: Optional["Integer"]) -> None:
        """
        Set segment with validation.

        Args:
            value: The segment to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._segment = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"segment must be Integer or None, got {type(value).__name__}"
            )
        self._segment = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getSegmentByte(self) -> "ByteOrderEnum":
        """
        AUTOSAR-compliant getter for segmentByte.

        Returns:
            The segmentByte value

        Note:
            Delegates to segment_byte property (CODING_RULE_V2_00017)
        """
        return self.segment_byte  # Delegates to property

    def setSegmentByte(self, value: "ByteOrderEnum") -> "SegmentPosition":
        """
        AUTOSAR-compliant setter for segmentByte with method chaining.

        Args:
            value: The segmentByte to set

        Returns:
            self for method chaining

        Note:
            Delegates to segment_byte property setter (gets validation automatically)
        """
        self.segment_byte = value  # Delegates to property setter
        return self

    def getSegmentLength(self) -> "Integer":
        """
        AUTOSAR-compliant getter for segmentLength.

        Returns:
            The segmentLength value

        Note:
            Delegates to segment_length property (CODING_RULE_V2_00017)
        """
        return self.segment_length  # Delegates to property

    def setSegmentLength(self, value: "Integer") -> "SegmentPosition":
        """
        AUTOSAR-compliant setter for segmentLength with method chaining.

        Args:
            value: The segmentLength to set

        Returns:
            self for method chaining

        Note:
            Delegates to segment_length property setter (gets validation automatically)
        """
        self.segment_length = value  # Delegates to property setter
        return self

    def getSegment(self) -> "Integer":
        """
        AUTOSAR-compliant getter for segment.

        Returns:
            The segment value

        Note:
            Delegates to segment property (CODING_RULE_V2_00017)
        """
        return self.segment  # Delegates to property

    def setSegment(self, value: "Integer") -> "SegmentPosition":
        """
        AUTOSAR-compliant setter for segment with method chaining.

        Args:
            value: The segment to set

        Returns:
            self for method chaining

        Note:
            Delegates to segment property setter (gets validation automatically)
        """
        self.segment = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_segment_byte(self, value: Optional["ByteOrderEnum"]) -> "SegmentPosition":
        """
        Set segmentByte and return self for chaining.

        Args:
            value: The segmentByte to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_segment_byte("value")
        """
        self.segment_byte = value  # Use property setter (gets validation)
        return self

    def with_segment_length(self, value: Optional["Integer"]) -> "SegmentPosition":
        """
        Set segmentLength and return self for chaining.

        Args:
            value: The segmentLength to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_segment_length("value")
        """
        self.segment_length = value  # Use property setter (gets validation)
        return self

    def with_segment(self, value: Optional["Integer"]) -> "SegmentPosition":
        """
        Set segment and return self for chaining.

        Args:
            value: The segment to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_segment("value")
        """
        self.segment = value  # Use property setter (gets validation)
        return self
