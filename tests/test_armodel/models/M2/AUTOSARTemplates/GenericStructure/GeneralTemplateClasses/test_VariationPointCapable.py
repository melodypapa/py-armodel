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

    def test_post_build_variant_criterion_capable_via_packageable_element(self):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.VariationPointCapable import VariationPointCapable
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import PostBuildVariantCriterion

        # ARPackage.element carries atpVariation (GST Table 4.1, [TPS_GST_00199]):
        # every PackageableElement genuinely aggregates a VariationPoint. The XSD
        # hoists the slot into the PACKAGEABLE-ELEMENT group (Applicable for:
        # ARPackage.element), so POST-BUILD-VARIANT-CRITERION inherits it via the
        # group ref - the same mechanism as P-PORT-PROTOTYPE via PORT-PROTOTYPE.
        assert issubclass(PostBuildVariantCriterion, VariationPointCapable)

    def test_post_build_variant_condition_not_capable(self):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.VariationPointCapable import VariationPointCapable
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import PostBuildVariantCondition

        assert not issubclass(PostBuildVariantCondition, VariationPointCapable)

    def test_identifiable_not_capable(self):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.VariationPointCapable import VariationPointCapable

        assert not issubclass(Identifiable, VariationPointCapable)
