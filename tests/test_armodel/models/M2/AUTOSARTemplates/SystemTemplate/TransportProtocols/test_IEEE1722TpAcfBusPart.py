import typing
from inspect import cleandoc
from typing import Optional

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.StereotypeMixins import VariationPointCapable
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import PduCollectionTriggerEnum
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.IEEE1722TpAcf import (
    IEEE1722TpAcfBusPart,
    IEEE1722TpAcfCanPart,
    IEEE1722TpAcfLinPart,
)


class TestIEEE1722TpAcfBusPart:
    def test_docstring_is_spec_note_verbatim(self):
        # Table 6.292, p.658 — class Note verbatim from the markdown
        assert cleandoc(IEEE1722TpAcfBusPart.__doc__) == "Definition of one IEEE1722Tp ACF part transported over the IEEE1722Tp channel. Tags: atp.Status=candidate"

    def test_abstract(self):
        with pytest.raises(TypeError):
            IEEE1722TpAcfBusPart(None, "AcfPart")

    def test_heritage(self):
        assert issubclass(IEEE1722TpAcfBusPart, Identifiable)
        assert issubclass(IEEE1722TpAcfBusPart, VariationPointCapable)

    def test_subclasses(self):
        assert issubclass(IEEE1722TpAcfCanPart, IEEE1722TpAcfBusPart)
        assert issubclass(IEEE1722TpAcfLinPart, IEEE1722TpAcfBusPart)

    def test_initialization(self):
        part = IEEE1722TpAcfCanPart(None, "CanPart1")
        assert part.getCollectionTrigger() is None
        assert part.getVariationPoint() is None

    def test_get_set_collection_trigger(self):
        part = IEEE1722TpAcfCanPart(None, "CanPart1")

        trigger = PduCollectionTriggerEnum()
        trigger.setValue(PduCollectionTriggerEnum.ALWAYS)
        assert part.setCollectionTrigger(trigger) is part
        assert part.getCollectionTrigger() is trigger
        assert part.getCollectionTrigger().getValue() == PduCollectionTriggerEnum.ALWAYS
        assert part.setCollectionTrigger(None) is part
        assert part.getCollectionTrigger() is trigger

    def test_variation_point(self):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import VariationPoint

        part = IEEE1722TpAcfLinPart(None, "LinPart1")

        vp = VariationPoint()
        assert part.setVariationPoint(vp) is part
        assert part.getVariationPoint() is vp
        assert part.setVariationPoint(None) is part
        assert part.getVariationPoint() is vp

    def test_annotations(self):
        hints = typing.get_type_hints(IEEE1722TpAcfBusPart.getCollectionTrigger)
        assert hints["return"] == Optional[PduCollectionTriggerEnum]
        hints = typing.get_type_hints(IEEE1722TpAcfBusPart.setCollectionTrigger)
        assert hints["value"] == Optional[PduCollectionTriggerEnum]
        assert hints["return"] == IEEE1722TpAcfBusPart
