"""Reader tests for the FMConditionByFeaturesAndAttributes element (FM-COND).

Spec: R23-11 AUTOSAR_FO_TPS_FeatureModelExchangeFormat, Table 7.2, p.62.
XSD 00052 complexType FM-CONDITION-BY-FEATURES-AND-ATTRIBUTES (line 62022):
abstract="false" mixed="true", unbounded choice of AR-OBJECT / FORMULA-EXPRESSION /
FM-FORMULA-BY-FEATURES-AND-ATTRIBUTES / own (empty) group; Table 7.2 declares no
attribute rows, so the class reads ARObject attributes + the mixed text only.

NOTE: the Aggregated-by consumers (FMFeatureMapCondition.fmCond, FM-COND at XSD
line 62309; FMFeatureRelation.restriction and FMFeatureRestriction.restriction,
RESTRICTION at lines 62523/62560) are all missing from the model — no dispatcher
exists, so this helper is pinned at element level (BlueprintFormula /
PostBuildVariantCriterionValue precedent). Re-base applied 2026-09-26 (Rule
0012.3): the class now derives from the synced FMFormulaByFeaturesAndAttributes
(Table 7.1) and its reader composes the base group reader, so the group members
ATTRIBUTE-REF / FEATURE-REF round-trip too (covered in
test_parser_fm_formula_by_features_and_attributes.py).
"""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate import FMConditionByFeaturesAndAttributes
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


class TestReadFMConditionByFeaturesAndAttributes:
    def test_read_text_only(self):
        xml = "<FM-COND xmlns='%s'>feature_a and not feature_b</FM-COND>" % NS
        element = ET.fromstring(xml)

        formula = ARXMLParser().readFMConditionByFeaturesAndAttributes(element, FMConditionByFeaturesAndAttributes())

        assert isinstance(formula, FMConditionByFeaturesAndAttributes)
        assert formula.getMixedString() == "feature_a and not feature_b"
        assert formula.getAtpReferences() == []
        assert formula.getAtpStringReferences() == []

    def test_read_empty_element_leaves_text_none(self):
        xml = "<FM-COND xmlns='%s'/>" % NS
        element = ET.fromstring(xml)

        formula = ARXMLParser().readFMConditionByFeaturesAndAttributes(element, FMConditionByFeaturesAndAttributes())

        assert isinstance(formula, FMConditionByFeaturesAndAttributes)
        assert formula.getMixedString() is None

    def test_read_whitespace_only_text_is_not_set(self):
        xml = "<FM-COND xmlns='%s'>   </FM-COND>" % NS
        element = ET.fromstring(xml)

        formula = ARXMLParser().readFMConditionByFeaturesAndAttributes(element, FMConditionByFeaturesAndAttributes())

        assert formula.getMixedString() is None

    def test_read_composes_base_group_children(self):
        """
        Re-base applied 2026-09-26 (Rule 0012.3): the ATTRIBUTE-REF / FEATURE-REF
        members belong to the Table 7.1 base class's own table — the reader now
        composes the base group reader and populates the inherited ref fields.
        """
        xml = "<FM-COND xmlns='%s'>feature_a" "<FEATURE-REF DEST='FM-FEATURE'>/FMFeatureModels/Model/FeatureA</FEATURE-REF>" "</FM-COND>" % NS
        element = ET.fromstring(xml)

        formula = ARXMLParser().readFMConditionByFeaturesAndAttributes(element, FMConditionByFeaturesAndAttributes())

        assert formula.getMixedString() == "feature_a"
        assert formula.getFeatureRef().getValue() == "/FMFeatureModels/Model/FeatureA"
        assert formula.getAtpReferences() == []
