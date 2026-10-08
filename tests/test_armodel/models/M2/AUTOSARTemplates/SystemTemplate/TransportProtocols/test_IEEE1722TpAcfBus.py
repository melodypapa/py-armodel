import typing
from inspect import cleandoc
from typing import List, Optional

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import IEEE1722TpAcfBusPart
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    IEEE1722TpAcfCanPart,
    IEEE1722TpAcfLinPart,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.StereotypeMixins import VariationPointCapable
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.IEEE1722TpAcf import IEEE1722TpAcfBus


def _pos_int(value):
    integer = PositiveInteger()
    integer.setValue(value)
    return integer


class TestIEEE1722TpAcfBus:
    def test_docstring_is_spec_note_verbatim(self):
        # Table 6.291, p.657 — class Note verbatim from the markdown
        assert cleandoc(IEEE1722TpAcfBus.__doc__) == "Abstract class to define various busses to be transported over a IEEE1722TP ACF connection. Tags: atp.Status=candidate"

    def test_abstract(self):
        with pytest.raises(TypeError):
            IEEE1722TpAcfBus(None, "AcfBus")

    def test_heritage(self):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable

        assert issubclass(IEEE1722TpAcfBus, Identifiable)
        assert issubclass(IEEE1722TpAcfBus, VariationPointCapable)

    def test_initialization(self):
        class _Bus(IEEE1722TpAcfBus):
            pass

        bus = _Bus(None, "CanBus")
        assert bus.getAcfParts() == []
        assert bus.getBusId() is None
        assert bus.getVariationPoint() is None

    def test_create_acf_parts(self):
        class _Bus(IEEE1722TpAcfBus):
            pass

        bus = _Bus(None, "CanBus")

        can_part = bus.createIEEE1722TpAcfCanPart("CanPart1")
        assert isinstance(can_part, IEEE1722TpAcfCanPart)
        assert can_part.getShortName() == "CanPart1"
        assert bus.getAcfParts() == [can_part]

        lin_part = bus.createIEEE1722TpAcfLinPart("LinPart1")
        assert isinstance(lin_part, IEEE1722TpAcfLinPart)
        assert lin_part.getShortName() == "LinPart1"
        assert bus.getAcfParts() == [can_part, lin_part]

        assert bus.createIEEE1722TpAcfCanPart("CanPart1") is can_part
        assert bus.createIEEE1722TpAcfLinPart("LinPart1") is lin_part
        assert len(bus.getAcfParts()) == 2

    def test_get_set_bus_id(self):
        class _Bus(IEEE1722TpAcfBus):
            pass

        bus = _Bus(None, "CanBus")

        bus_id = _pos_int(7)
        assert bus.setBusId(bus_id) is bus
        assert bus.getBusId() is bus_id
        assert bus.setBusId(None) is bus
        assert bus.getBusId() is bus_id

    def test_variation_point(self):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import VariationPoint

        class _Bus(IEEE1722TpAcfBus):
            pass

        bus = _Bus(None, "CanBus")

        vp = VariationPoint()
        assert bus.setVariationPoint(vp) is bus
        assert bus.getVariationPoint() is vp
        assert bus.setVariationPoint(None) is bus
        assert bus.getVariationPoint() is vp

    def test_annotations(self):
        hints = typing.get_type_hints(IEEE1722TpAcfBus.createIEEE1722TpAcfCanPart)
        assert hints["return"] == IEEE1722TpAcfCanPart
        hints = typing.get_type_hints(IEEE1722TpAcfBus.createIEEE1722TpAcfLinPart)
        assert hints["return"] == IEEE1722TpAcfLinPart
        hints = typing.get_type_hints(IEEE1722TpAcfBus.getAcfParts)
        assert hints["return"] == List[IEEE1722TpAcfBusPart]
        hints = typing.get_type_hints(IEEE1722TpAcfBus.getBusId)
        assert hints["return"] == Optional[PositiveInteger]
        hints = typing.get_type_hints(IEEE1722TpAcfBus.setBusId)
        assert hints["value"] == Optional[PositiveInteger]
        assert hints["return"] == IEEE1722TpAcfBus
