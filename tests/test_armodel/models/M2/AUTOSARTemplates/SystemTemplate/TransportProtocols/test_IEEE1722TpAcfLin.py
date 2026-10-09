import typing
from inspect import cleandoc
from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, PositiveInteger
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.StereotypeMixins import VariationPointCapable
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.IEEE1722TpAcf import (
    IEEE1722TpAcfBus,
    IEEE1722TpAcfBusPart,
    IEEE1722TpAcfLin,
    IEEE1722TpAcfLinPart,
)


def _pos_int(value):
    integer = PositiveInteger()
    integer.setValue(value)
    return integer


def _bool(value):
    boolean = Boolean()
    boolean.setValue(value)
    return boolean


class TestIEEE1722TpAcfLin:
    def test_docstring_is_spec_note_verbatim(self):
        # Table 6.296, p.667 — class Note verbatim from the markdown
        assert cleandoc(IEEE1722TpAcfLin.__doc__) == "ACF IEEE1722Tp bus used for LIN transport. Tags: atp.Status=candidate atp.recommendedPackage=IEEE1722TpConnections"

    def test_concrete(self):
        bus = IEEE1722TpAcfLin(None, "LinBus")
        assert bus.getShortName() == "LinBus"

    def test_heritage(self):
        assert issubclass(IEEE1722TpAcfLin, IEEE1722TpAcfBus)
        assert issubclass(IEEE1722TpAcfLin, VariationPointCapable)

    def test_initialization(self):
        bus = IEEE1722TpAcfLin(None, "LinBus")
        assert bus.getBaseFrequency() is None
        assert bus.getFrameSyncEnabled() is None
        assert bus.getTimestampInterval() is None
        assert bus.getAcfParts() == []
        assert bus.getBusId() is None
        assert bus.getVariationPoint() is None

    def test_get_set_base_frequency(self):
        bus = IEEE1722TpAcfLin(None, "LinBus")
        value = _pos_int(48000)
        assert bus.setBaseFrequency(value) is bus
        assert bus.getBaseFrequency() is value
        assert bus.getBaseFrequency().getValue() == 48000
        assert bus.setBaseFrequency(None) is bus
        assert bus.getBaseFrequency() is value

    def test_get_set_frame_sync_enabled(self):
        bus = IEEE1722TpAcfLin(None, "LinBus")
        value = _bool(True)
        assert bus.setFrameSyncEnabled(value) is bus
        assert bus.getFrameSyncEnabled() is value
        assert bus.setFrameSyncEnabled(None) is bus
        assert bus.getFrameSyncEnabled() is value

    def test_get_set_timestamp_interval(self):
        bus = IEEE1722TpAcfLin(None, "LinBus")
        value = _pos_int(4)
        assert bus.setTimestampInterval(value) is bus
        assert bus.getTimestampInterval() is value
        assert bus.getTimestampInterval().getValue() == 4
        assert bus.setTimestampInterval(None) is bus
        assert bus.getTimestampInterval() is value

    def test_create_acf_part_inherited(self):
        bus = IEEE1722TpAcfLin(None, "LinBus")
        part = bus.createIEEE1722TpAcfLinPart("LinPart1")
        assert isinstance(part, IEEE1722TpAcfLinPart)
        assert bus.getAcfParts() == [part]

    def test_annotations(self):
        hints = typing.get_type_hints(IEEE1722TpAcfLin.getBaseFrequency)
        assert hints["return"] == Optional[PositiveInteger]
        hints = typing.get_type_hints(IEEE1722TpAcfLin.setBaseFrequency)
        assert hints["value"] == Optional[PositiveInteger]
        assert hints["return"] == IEEE1722TpAcfLin
        hints = typing.get_type_hints(IEEE1722TpAcfLin.getFrameSyncEnabled)
        assert hints["return"] == Optional[Boolean]
        hints = typing.get_type_hints(IEEE1722TpAcfLin.setFrameSyncEnabled)
        assert hints["value"] == Optional[Boolean]
        assert hints["return"] == IEEE1722TpAcfLin
        hints = typing.get_type_hints(IEEE1722TpAcfLin.getTimestampInterval)
        assert hints["return"] == Optional[PositiveInteger]
        hints = typing.get_type_hints(IEEE1722TpAcfLin.setTimestampInterval)
        assert hints["value"] == Optional[PositiveInteger]
        assert hints["return"] == IEEE1722TpAcfLin
        hints = typing.get_type_hints(IEEE1722TpAcfLin.getAcfParts)
        assert hints["return"] == List[IEEE1722TpAcfBusPart]
        hints = typing.get_type_hints(IEEE1722TpAcfLin.getBusId)
        assert hints["return"] == Optional[PositiveInteger]
