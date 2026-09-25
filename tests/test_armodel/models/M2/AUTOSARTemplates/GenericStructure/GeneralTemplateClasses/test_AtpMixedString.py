from abc import ABC

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.StereotypeMixins import AtpMixedString


class _Mixed(AtpMixedString):
    pass


class TestAtpMixedStringInterface:
    def test_interface_level_mixin(self):
        assert issubclass(AtpMixedString, ABC)
        assert not issubclass(AtpMixedString, ARObject)

    def test_probe_needs_no_init(self):
        m = _Mixed()
        assert isinstance(m, AtpMixedString)
        assert m.getMixedString() is None

    def test_default_none_and_round_trip(self):
        m = _Mixed()
        assert m.setMixedString("A and\n B ").getMixedString() == "A and\n B "

    def test_none_noop_and_chaining(self):
        m = _Mixed()
        m.setMixedString("keep")
        assert m.setMixedString(None) is m
        assert m.getMixedString() == "keep"

    def test_whitespace_only_stored_verbatim(self):
        m = _Mixed()
        m.setMixedString(" ")
        assert m.getMixedString() == " "


class TestAtpMixedStringCapabilityMatrix:
    def test_variation_point_family_capable(self):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling.AttributeValueVariationPoints import (
            AttributeValueVariationPoint,
            NumericalValueVariationPoint,
        )

        assert issubclass(AttributeValueVariationPoint, AtpMixedString)
        assert issubclass(NumericalValueVariationPoint, AtpMixedString)

    def test_condition_by_formula_capable(self):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import ConditionByFormula

        assert issubclass(ConditionByFormula, AtpMixedString)
        assert issubclass(ConditionByFormula, ARObject)

    def test_timing_formulas_capable(self):
        from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingCondition import TimingConditionFormula
        from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventOccurrenceExpression import (
            TDEventOccurrenceExpressionFormula,
        )

        assert issubclass(TimingConditionFormula, AtpMixedString)
        assert issubclass(TDEventOccurrenceExpressionFormula, AtpMixedString)

    def test_documentation_family_not_capable(self):
        from armodel.models.M2.MSR.Documentation.TextModel.BlockElements import DocumentationBlock
        from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel import LParagraph
        from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import MultiLanguageParagraph

        assert not issubclass(DocumentationBlock, AtpMixedString)
        assert not issubclass(LParagraph, AtpMixedString)
        assert not issubclass(MultiLanguageParagraph, AtpMixedString)
