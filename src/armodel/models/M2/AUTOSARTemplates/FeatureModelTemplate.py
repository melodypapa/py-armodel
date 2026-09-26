from armodel.models.M2.AUTOSARTemplates.GenericStructure.FormulaLanguage import FormulaExpression

__all__ = ["FMConditionByFeaturesAndAttributes"]


class FMConditionByFeaturesAndAttributes(FormulaExpression):
    """A boolean expression that has the syntax of the AUTOSAR formula language but uses only references to features or feature attributes (not system constants) as operands."""

    # FMConditionByFeaturesAndAttributes method parity checklist:
    # Spec: R23-11/AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf, Table 7.2, p.62 (R23-11)
    # (section 7.2.2; R4.3.1 reproduction Table 7.2 has the same rows (p.62, AUTOSAR_TPS_
    # FeatureModelExchangeFormat.md line 1780). XSD 00052 group FM-CONDITION-BY-FEATURES-
    # AND-ATTRIBUTES line 62013 is an empty sequence; complexType line 62022
    # abstract="false" mixed="true" composes AR-OBJECT + FORMULA-EXPRESSION +
    # FM-FORMULA-BY-FEATURES-AND-ATTRIBUTES + the own group. Table 7.2 declares NO
    # attribute rows — the class models zero own members; the parent-group members
    # ATTRIBUTE-REF / FEATURE-REF (group FM-FORMULA-BY-FEATURES-AND-ATTRIBUTES, line
    # 62746) belong to the Table 7.1 base class's own table. The most-derived base
    # FMFormulaByFeaturesAndAttributes (Table 7.1, abstract, group-only in the XSD) is
    # not yet in the model — separate sync row — so the class derives from the nearest
    # available ancestor FormulaExpression. The Aggregated-by consumers
    # (FMFeatureMapCondition.fmCond / FMFeatureRelation.restriction /
    # FMFeatureRestriction.restriction) are all missing from the model — no dispatcher
    # exists, so reader/writer coverage is the class's own helper pair
    # readFMConditionByFeaturesAndAttributes / writeFMConditionByFeaturesAndAttributes,
    # pinned at element level (BlueprintFormula / PostBuildVariantCriterionValue
    # precedent).)
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__       [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # (no methods — Table 7.2 declares no attribute rows; getMixedString / setMixedString
    # provided by the AtpMixedString mixin and get/addAtpReference(s) inherited from
    # FormulaExpression — no spec rows; the class-level reader/writer coverage lives in
    # the own helper pair, test-pinned by
    # tests/test_armodel/parser/test_parser_fm_condition_by_features_and_attributes.py
    # and tests/test_armodel/writer/test_writer_fm_condition_by_features_and_attributes.py)

    def __init__(self):
        super().__init__()
