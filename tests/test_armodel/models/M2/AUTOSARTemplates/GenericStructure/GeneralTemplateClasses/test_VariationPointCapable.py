import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import VariationPoint


class TestVariationPointCapable:
    def test_default_is_none(self):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.VariationPointCapable import VariationPointCapable

        class Probe(VariationPointCapable):
            pass

        assert Probe().getVariationPoint() is None

    def test_round_trip_and_none_noop(self):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.VariationPointCapable import VariationPointCapable

        class Probe(VariationPointCapable):
            pass

        probe = Probe()
        vp = VariationPoint()
        assert probe.setVariationPoint(vp) is probe
        assert probe.getVariationPoint() is vp
        probe.setVariationPoint(None)
        assert probe.getVariationPoint() is vp
