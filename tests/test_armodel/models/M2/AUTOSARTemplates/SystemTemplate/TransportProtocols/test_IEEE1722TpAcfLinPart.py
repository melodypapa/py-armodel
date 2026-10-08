import typing
from inspect import cleandoc
from typing import Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, RefType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.StereotypeMixins import VariationPointCapable
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.IEEE1722TpAcf import (
    IEEE1722TpAcfBusPart,
    IEEE1722TpAcfLinPart,
)


def _pos_int(value):
    integer = PositiveInteger()
    integer.setValue(value)
    return integer


class TestIEEE1722TpAcfLinPart:
    def test_docstring_is_spec_note_verbatim(self):
        # Table 6.297, p.667 — class Note verbatim from the markdown
        assert cleandoc(IEEE1722TpAcfLinPart.__doc__) == "Definition of one LIN part transported over the IEEE1722Tp channel. Tags: atp.Status=candidate"

    def test_concrete_and_heritage(self):
        part = IEEE1722TpAcfLinPart(None, "LinPart1")
        assert part.getShortName() == "LinPart1"
        assert issubclass(IEEE1722TpAcfLinPart, IEEE1722TpAcfBusPart)
        assert issubclass(IEEE1722TpAcfLinPart, VariationPointCapable)

    def test_initialization(self):
        part = IEEE1722TpAcfLinPart(None, "LinPart1")
        assert part.getLinIdentifier() is None
        assert part.getSduRef() is None
        assert part.getCollectionTrigger() is None
        assert part.getVariationPoint() is None

    def test_get_set_lin_identifier(self):
        part = IEEE1722TpAcfLinPart(None, "LinPart1")
        value = _pos_int(63)
        assert part.setLinIdentifier(value) is part
        assert part.getLinIdentifier() is value
        assert part.getLinIdentifier().getValue() == 63
        assert part.setLinIdentifier(None) is part
        assert part.getLinIdentifier() is value

    def test_get_set_sdu_ref(self):
        part = IEEE1722TpAcfLinPart(None, "LinPart1")
        value = RefType()
        value.setDest("PDU-TRIGGERING-REF")
        value.setValue("/Pkg/PduTriggering")
        assert part.setSduRef(value) is part
        assert part.getSduRef() is value
        assert part.getSduRef().getValue() == "/Pkg/PduTriggering"
        assert part.setSduRef(None) is part
        assert part.getSduRef() is value

    def test_annotations(self):
        hints = typing.get_type_hints(IEEE1722TpAcfLinPart.getLinIdentifier)
        assert hints["return"] == Optional[PositiveInteger]
        hints = typing.get_type_hints(IEEE1722TpAcfLinPart.setLinIdentifier)
        assert hints["value"] == Optional[PositiveInteger]
        assert hints["return"] == IEEE1722TpAcfLinPart
        hints = typing.get_type_hints(IEEE1722TpAcfLinPart.getSduRef)
        assert hints["return"] == Optional[RefType]
        hints = typing.get_type_hints(IEEE1722TpAcfLinPart.setSduRef)
        assert hints["value"] == Optional[RefType]
        assert hints["return"] == IEEE1722TpAcfLinPart
