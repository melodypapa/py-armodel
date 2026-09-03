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


class TestVariationPointCapabilityMatrix:
    def test_pr_port_capable_via_port_prototype(self):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.VariationPointCapable import VariationPointCapable
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components import PRPortPrototype

        assert issubclass(PRPortPrototype, VariationPointCapable)

    def test_ar_package_capable(self):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARPackage
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.VariationPointCapable import VariationPointCapable

        assert issubclass(ARPackage, VariationPointCapable)

    def test_structured_req_capable(self):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.VariationPointCapable import VariationPointCapable
        from armodel.models.M2.MSR.Documentation.BlockElements.RequirementsTracing import StructuredReq

        assert issubclass(StructuredReq, VariationPointCapable)

    def test_post_build_variant_criterion_not_capable(self):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.VariationPointCapable import VariationPointCapable
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import PostBuildVariantCriterion

        assert not issubclass(PostBuildVariantCriterion, VariationPointCapable)
