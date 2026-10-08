import typing
from inspect import cleandoc
from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.StereotypeMixins import VariationPointCapable
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.IEEE1722TpAcf import (
    IEEE1722TpAcfBus,
    IEEE1722TpAcfCan,
    IEEE1722TpAcfCanMessageTypeEnum,
    IEEE1722TpAcfCanPart,
)


def _pos_int(value):
    integer = PositiveInteger()
    integer.setValue(value)
    return integer


class TestIEEE1722TpAcfCan:
    def test_docstring_is_spec_note_verbatim(self):
        # Table 6.293, p.661 — class Note verbatim from the markdown
        assert cleandoc(IEEE1722TpAcfCan.__doc__) == "ACF IEEE1722Tp bus used for CAN transport. Tags: atp.Status=candidate atp.recommendedPackage=IEEE1722TpConnections"

    def test_concrete(self):
        bus = IEEE1722TpAcfCan(None, "CanBus")
        assert bus.getShortName() == "CanBus"

    def test_heritage(self):
        assert issubclass(IEEE1722TpAcfCan, IEEE1722TpAcfBus)
        assert issubclass(IEEE1722TpAcfCan, VariationPointCapable)

    def test_initialization(self):
        bus = IEEE1722TpAcfCan(None, "CanBus")
        assert bus.getMessageType() is None
        assert bus.getAcfParts() == []
        assert bus.getBusId() is None
        assert bus.getVariationPoint() is None

    def test_get_set_message_type(self):
        bus = IEEE1722TpAcfCan(None, "CanBus")

        message_type = IEEE1722TpAcfCanMessageTypeEnum()
        message_type.setValue(IEEE1722TpAcfCanMessageTypeEnum.ENUM_CAN_BRIEF)
        assert bus.setMessageType(message_type) is bus
        assert bus.getMessageType() is message_type
        assert bus.getMessageType().getValue() == "CAN-BRIEF"
        assert bus.setMessageType(None) is bus
        assert bus.getMessageType() is message_type

    def test_create_acf_part_inherited(self):
        bus = IEEE1722TpAcfCan(None, "CanBus")
        part = bus.createIEEE1722TpAcfCanPart("CanPart1")
        assert isinstance(part, IEEE1722TpAcfCanPart)
        assert bus.getAcfParts() == [part]

    def test_annotations(self):
        from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.IEEE1722TpAcf import (
            IEEE1722TpAcfBusPart,
        )

        hints = typing.get_type_hints(IEEE1722TpAcfCan.getMessageType)
        assert hints["return"] == Optional[IEEE1722TpAcfCanMessageTypeEnum]
        hints = typing.get_type_hints(IEEE1722TpAcfCan.setMessageType)
        assert hints["value"] == Optional[IEEE1722TpAcfCanMessageTypeEnum]
        assert hints["return"] == IEEE1722TpAcfCan
        hints = typing.get_type_hints(IEEE1722TpAcfCan.getAcfParts)
        assert hints["return"] == List[IEEE1722TpAcfBusPart]
        hints = typing.get_type_hints(IEEE1722TpAcfCan.getBusId)
        assert hints["return"] == Optional[PositiveInteger]
