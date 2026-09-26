from typing import Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.FormulaLanguage import FormulaExpression
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType

__all__ = ["FMConditionByFeaturesAndAttributes", "FMFormulaByFeaturesAndAttributes"]


class FMFormulaByFeaturesAndAttributes(FormulaExpression):
    """An expression that has the syntax of the AUTOSAR formula language but uses only references to features or feature attributes (not system constants) as operands."""

    # FMFormulaByFeaturesAndAttributes method parity checklist:
    # Spec: R23-11/AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf, Table 7.1, p.61 (R23-11)
    # (section 7.2.1; R4.3.1 reproduction Table 7.1 has the same rows (p.61,
    # AUTOSAR_TPS_FeatureModelExchangeFormat.md line 1757). XSD 00052 has NO own
    # complexType — group-only class: group FM-FORMULA-BY-FEATURES-AND-ATTRIBUTES
    # (line 62746, stereotypes atpMixedString,atpObject) is an unbounded 0..* choice
    # of ATTRIBUTE-REF (DEST FM-ATTRIBUTE-DEF--SUBTYPES-ENUM, required) and
    # FEATURE-REF (DEST FM-FEATURE--SUBTYPES-ENUM, required), each 0..1 per the
    # appinfo pureMM minOccurs=0 / maxOccurs=1. The Table 7.1 attribute rows carry
    # no Note column — the member docstrings are verbatim from the XSD group member
    # documentation. The ref targets FMAttributeDef / FMFeature are not yet in the
    # model — the fields carry RefType (TlvDataIdDefinition precedent). Per Rule
    # 0001.7 (abstract XML-bearing bases own reusable helpers) the class owns the
    # readFMFormulaByFeaturesAndAttributes / writeFMFormulaByFeaturesAndAttributes
    # helpers; the concrete subclass FMConditionByFeaturesAndAttributes (Table 7.2,
    # complexType line 62022 composes this group) calls them via isinstance dispatch
    # (readConditionByFormula / readBlueprintFormula precedent) — no standalone
    # dispatcher exists for the Aggregated-by consumers, coverage is pinned at
    # element level by tests/test_armodel/parser/
    # test_parser_fm_formula_by_features_and_attributes.py and tests/test_armodel/
    # writer/test_writer_fm_formula_by_features_and_attributes.py.)
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__          [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getAttributeRef   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setAttributeRef   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getFeatureRef     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setFeatureRef     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        if type(self) is FMFormulaByFeaturesAndAttributes:
            raise TypeError("FMFormulaByFeaturesAndAttributes is an abstract class.")

        super().__init__()

        # An expression of type FMFormulaByFeaturesAndAttributes may refer to attributes of FMFeatures.
        self.attributeRef: Optional[RefType] = None

        # An expression of type FMFormulaByFeaturesAndAttributes may refer to FMFeatures.
        self.featureRef: Optional[RefType] = None

    def getAttributeRef(self) -> Optional[RefType]:
        """An expression of type FMFormulaByFeaturesAndAttributes may refer to attributes of FMFeatures."""
        return self.attributeRef

    def setAttributeRef(self, value: Optional[RefType]) -> "FMFormulaByFeaturesAndAttributes":
        """An expression of type FMFormulaByFeaturesAndAttributes may refer to attributes of FMFeatures. A None value is a no-op and does not overwrite an existing attributeRef."""
        if value is not None:
            self.attributeRef = value
        return self

    def getFeatureRef(self) -> Optional[RefType]:
        """An expression of type FMFormulaByFeaturesAndAttributes may refer to FMFeatures."""
        return self.featureRef

    def setFeatureRef(self, value: Optional[RefType]) -> "FMFormulaByFeaturesAndAttributes":
        """An expression of type FMFormulaByFeaturesAndAttributes may refer to FMFeatures. A None value is a no-op and does not overwrite an existing featureRef."""
        if value is not None:
            self.featureRef = value
        return self


class FMConditionByFeaturesAndAttributes(FMFormulaByFeaturesAndAttributes):
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
    # 62746) belong to the Table 7.1 base class's own table. Re-base applied 2026-09-26
    # (Rule 0012.3): the most-derived base FMFormulaByFeaturesAndAttributes (Table 7.1,
    # abstract, group-only in the XSD) is now synced — the class re-based from
    # FormulaExpression onto it per the Base row ARObject,
    # FMFormulaByFeaturesAndAttributes, FormulaExpression; the ATTRIBUTE-REF /
    # FEATURE-REF group members are inherited from the base and composed by the
    # reader/writer helpers readFMFormulaByFeaturesAndAttributes /
    # writeFMFormulaByFeaturesAndAttributes. The Aggregated-by consumers
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
    # FormulaExpression — no spec rows; get/setAttributeRef and get/setFeatureRef are
    # inherited from FMFormulaByFeaturesAndAttributes (Table 7.1) — no Table 7.2 rows;
    # the class-level reader/writer coverage lives in the own helper pair, test-pinned by
    # tests/test_armodel/parser/test_parser_fm_condition_by_features_and_attributes.py
    # and tests/test_armodel/writer/test_writer_fm_condition_by_features_and_attributes.py)

    def __init__(self):
        super().__init__()
