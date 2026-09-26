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
PostBuildVariantCriterionValue precedent). The FM-FORMULA-BY-FEATURES-AND-ATTRIBUTES
group members (ATTRIBUTE-REF / FEATURE-REF) belong to the Table 7.1 base class's
own sync row and are deliberately not read here (Rule 0015 — the PDF table wins).
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

    def test_read_tolerates_unmodeled_base_group_children(self):
        """
        ATTRIBUTE-REF / FEATURE-REF belong to the Table 7.1 base class's own table
        (separate sync row) and are not modeled on this class — the reader leaves
        them unread without failing.
        """
        xml = "<FM-COND xmlns='%s'>feature_a" "<FEATURE-REF DEST='FM-FEATURE'>/FMFeatureModels/Model/FeatureA</FEATURE-REF>" "</FM-COND>" % NS
        element = ET.fromstring(xml)

        formula = ARXMLParser().readFMConditionByFeaturesAndAttributes(element, FMConditionByFeaturesAndAttributes())

        assert formula.getMixedString() == "feature_a"
        assert formula.getAtpReferences() == []
