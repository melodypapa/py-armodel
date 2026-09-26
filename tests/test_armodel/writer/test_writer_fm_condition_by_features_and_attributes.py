"""Writer tests for the FMConditionByFeaturesAndAttributes element (FM-COND).

Spec: R23-11 AUTOSAR_FO_TPS_FeatureModelExchangeFormat, Table 7.2, p.62.
XSD 00052 complexType FM-CONDITION-BY-FEATURES-AND-ATTRIBUTES (line 62022):
abstract="false" mixed="true"; Table 7.2 declares no attribute rows, so the
class writes ARObject attributes + the mixed text only.

NOTE: the Aggregated-by consumers (FMFeatureMapCondition.fmCond, FM-COND at XSD
line 62309; FMFeatureRelation.restriction and FMFeatureRestriction.restriction,
RESTRICTION at lines 62523/62560) are all missing from the model — no dispatcher
exists, so this helper is pinned at element level (BlueprintFormula /
PostBuildVariantCriterionValue precedent). The element name follows the
FMFeatureMapCondition.fmCond role (FM-COND); the RESTRICTION roles are covered
via the key parameter.
"""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate import FMConditionByFeaturesAndAttributes
from armodel.writer.arxml_writer import ARXMLWriter


class TestWriteFMConditionByFeaturesAndAttributes:
    def test_write_mixed_text_under_default_fm_cond_key(self):
        formula = FMConditionByFeaturesAndAttributes()
        formula.setMixedString("feature_a and not feature_b")

        element = ET.Element("PARENT")
        ARXMLWriter().writeFMConditionByFeaturesAndAttributes(element, formula)

        written = element.find("FM-COND")
        assert written is not None
        assert written.text == "feature_a and not feature_b"
        assert len(written) == 0

    def test_write_custom_key_for_restriction_role(self):
        formula = FMConditionByFeaturesAndAttributes()
        formula.setMixedString("feature_a")

        element = ET.Element("PARENT")
        ARXMLWriter().writeFMConditionByFeaturesAndAttributes(element, formula, "RESTRICTION")

        assert element.find("RESTRICTION") is not None
        assert element.find("RESTRICTION").text == "feature_a"
        assert element.find("FM-COND") is None

    def test_write_empty_formula_emits_bare_element(self):
        element = ET.Element("PARENT")
        ARXMLWriter().writeFMConditionByFeaturesAndAttributes(element, FMConditionByFeaturesAndAttributes())

        written = element.find("FM-COND")
        assert written is not None
        assert len(written) == 0
        assert written.text is None

    def test_write_none_formula_emits_no_element(self):
        element = ET.Element("PARENT")
        ARXMLWriter().writeFMConditionByFeaturesAndAttributes(element, None)

        assert element.find("FM-COND") is None
