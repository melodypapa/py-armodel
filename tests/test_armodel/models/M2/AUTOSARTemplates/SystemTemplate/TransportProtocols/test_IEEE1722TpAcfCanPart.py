import typing
from inspect import cleandoc
from typing import Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
    RefType,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanCommunication import (
    CanAddressingModeType,
    CanFrameTxBehaviorEnum,
    RxIdentifierRange,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.IEEE1722TpAcf import (
    IEEE1722TpAcfBusPart,
    IEEE1722TpAcfCanPart,
)


def _pos_int(value):
    integer = PositiveInteger()
    integer.setValue(value)
    return integer


def _bool(value):
    boolean = Boolean()
    boolean.setValue(value)
    return boolean


def _enum(enum_cls, value):
    enum = enum_cls()
    enum.setValue(value)
    return enum


class TestIEEE1722TpAcfCanPart:
    def test_docstring_is_spec_note_verbatim(self):
        # Table 6.294, p.661 — class Note verbatim from the markdown
        assert cleandoc(IEEE1722TpAcfCanPart.__doc__) == "Definition of one CAN part (frame or frame range) transported over the IEEE1722Tp channel. Tags: atp.Status=candidate"

    def test_concrete_and_heritage(self):
        part = IEEE1722TpAcfCanPart(None, "CanPart1")
        assert part.getShortName() == "CanPart1"
        assert issubclass(IEEE1722TpAcfCanPart, IEEE1722TpAcfBusPart)

    def test_initialization(self):
        part = IEEE1722TpAcfCanPart(None, "CanPart1")
        assert part.getCanAddressingMode() is None
        assert part.getCanBitRateSwitch() is None
        assert part.getCanFrameTxBehavior() is None
        assert part.getCanIdentifier() is None
        assert part.getCanIdentifierMask() is None
        assert part.getCanIdentifierRange() is None
        assert part.getSduRef() is None
        assert part.getCollectionTrigger() is None
        assert part.getVariationPoint() is None

    def test_get_set_can_addressing_mode(self):
        part = IEEE1722TpAcfCanPart(None, "CanPart1")
        value = _enum(CanAddressingModeType, CanAddressingModeType.ENUM_EXTENDED)
        assert part.setCanAddressingMode(value) is part
        assert part.getCanAddressingMode() is value
        assert part.setCanAddressingMode(None) is part
        assert part.getCanAddressingMode() is value

    def test_get_set_can_bit_rate_switch(self):
        part = IEEE1722TpAcfCanPart(None, "CanPart1")
        value = _bool(True)
        assert part.setCanBitRateSwitch(value) is part
        assert part.getCanBitRateSwitch() is value
        assert part.setCanBitRateSwitch(None) is part
        assert part.getCanBitRateSwitch() is value

    def test_get_set_can_frame_tx_behavior(self):
        part = IEEE1722TpAcfCanPart(None, "CanPart1")
        value = _enum(CanFrameTxBehaviorEnum, CanFrameTxBehaviorEnum.ENUM_CAN_FD)
        assert part.setCanFrameTxBehavior(value) is part
        assert part.getCanFrameTxBehavior() is value
        assert part.setCanFrameTxBehavior(None) is part
        assert part.getCanFrameTxBehavior() is value

    def test_get_set_can_identifier(self):
        part = IEEE1722TpAcfCanPart(None, "CanPart1")
        value = _pos_int(23)
        assert part.setCanIdentifier(value) is part
        assert part.getCanIdentifier() is value
        assert part.setCanIdentifier(None) is part
        assert part.getCanIdentifier() is value

    def test_get_set_can_identifier_mask(self):
        part = IEEE1722TpAcfCanPart(None, "CanPart1")
        value = _pos_int(4095)
        assert part.setCanIdentifierMask(value) is part
        assert part.getCanIdentifierMask() is value
        assert part.setCanIdentifierMask(None) is part
        assert part.getCanIdentifierMask() is value

    def test_get_set_can_identifier_range(self):
        part = IEEE1722TpAcfCanPart(None, "CanPart1")
        value = RxIdentifierRange()
        value.setLowerCanId(_pos_int(0))
        value.setUpperCanId(_pos_int(3000))
        assert part.setCanIdentifierRange(value) is part
        assert part.getCanIdentifierRange() is value
        assert part.getCanIdentifierRange().getUpperCanId().getValue() == 3000
        assert part.setCanIdentifierRange(None) is part
        assert part.getCanIdentifierRange() is value

    def test_get_set_sdu_ref(self):
        part = IEEE1722TpAcfCanPart(None, "CanPart1")
        value = RefType()
        value.setDest("PDU-TRIGGERING-REF")
        value.setValue("/Pkg/PduTriggering")
        assert part.setSduRef(value) is part
        assert part.getSduRef() is value
        assert part.getSduRef().getValue() == "/Pkg/PduTriggering"
        assert part.setSduRef(None) is part
        assert part.getSduRef() is value

    def test_annotations(self):
        hints = typing.get_type_hints(IEEE1722TpAcfCanPart.getCanAddressingMode)
        assert hints["return"] == Optional[CanAddressingModeType]
        hints = typing.get_type_hints(IEEE1722TpAcfCanPart.setCanAddressingMode)
        assert hints["value"] == Optional[CanAddressingModeType]
        assert hints["return"] == IEEE1722TpAcfCanPart
        hints = typing.get_type_hints(IEEE1722TpAcfCanPart.getCanBitRateSwitch)
        assert hints["return"] == Optional[Boolean]
        hints = typing.get_type_hints(IEEE1722TpAcfCanPart.getCanFrameTxBehavior)
        assert hints["return"] == Optional[CanFrameTxBehaviorEnum]
        hints = typing.get_type_hints(IEEE1722TpAcfCanPart.getCanIdentifier)
        assert hints["return"] == Optional[PositiveInteger]
        hints = typing.get_type_hints(IEEE1722TpAcfCanPart.getCanIdentifierMask)
        assert hints["return"] == Optional[PositiveInteger]
        hints = typing.get_type_hints(IEEE1722TpAcfCanPart.getCanIdentifierRange)
        assert hints["return"] == Optional[RxIdentifierRange]
        hints = typing.get_type_hints(IEEE1722TpAcfCanPart.getSduRef)
        assert hints["return"] == Optional[RefType]
        hints = typing.get_type_hints(IEEE1722TpAcfCanPart.setSduRef)
        assert hints["value"] == Optional[RefType]
        assert hints["return"] == IEEE1722TpAcfCanPart
