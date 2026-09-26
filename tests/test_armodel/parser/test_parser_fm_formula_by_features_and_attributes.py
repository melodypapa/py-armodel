"""Reader tests for the FMFormulaByFeaturesAndAttributes group members.

Spec: R23-11 AUTOSAR_FO_TPS_FeatureModelExchangeFormat, Table 7.1, p.61.
XSD 00052 has NO own complexType for the class — it is group-only: group
FM-FORMULA-BY-FEATURES-AND-ATTRIBUTES (line 62746) is an unbounded 0..* choice
of ATTRIBUTE-REF (DEST FM-ATTRIBUTE-DEF--SUBTYPES-ENUM, required) and
FEATURE-REF (DEST FM-FEATURE--SUBTYPES-ENUM, required), each 0..1 per the
appinfo pureMM minOccurs=0 / maxOccurs=1.

NOTE: per Rule 0001.7 (abstract XML-bearing bases own reusable helpers) the
class owns readFMFormulaByFeaturesAndAttributes /
writeFMFormulaByFeaturesAndAttributes; the concrete subclass
FMConditionByFeaturesAndAttributes composes them (its complexType composes the
group), so the composition is pinned here through an FM-COND element too.
"""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate import FMConditionByFeaturesAndAttributes, FMFormulaByFeaturesAndAttributes
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


class TestReadFMFormulaByFeaturesAndAttributes:
    def test_read_both_refs(self):
        xml = (
            "<FM-COND xmlns='%s'>feature_a and attr_b"
            "<ATTRIBUTE-REF DEST='FM-ATTRIBUTE-DEF'>/FMAttributeDefModels/Model/AttributeB</ATTRIBUTE-REF>"
            "<FEATURE-REF DEST='FM-FEATURE'>/FMFeatureModels/Model/FeatureA</FEATURE-REF>"
            "</FM-COND>" % NS
        )
        element = ET.fromstring(xml)

        formula = ARXMLParser().readFMFormulaByFeaturesAndAttributes(element, FMConditionByFeaturesAndAttributes())

        assert isinstance(formula, FMFormulaByFeaturesAndAttributes)
        assert formula.getAttributeRef().getValue() == "/FMAttributeDefModels/Model/AttributeB"
        assert formula.getAttributeRef().getDest() == "FM-ATTRIBUTE-DEF"
        assert formula.getFeatureRef().getValue() == "/FMFeatureModels/Model/FeatureA"
        assert formula.getFeatureRef().getDest() == "FM-FEATURE"

    def test_read_attribute_ref_only(self):
        xml = "<FM-COND xmlns='%s'><ATTRIBUTE-REF DEST='FM-ATTRIBUTE-DEF'>/FMAttributeDefModels/Model/AttributeB</ATTRIBUTE-REF></FM-COND>" % NS
        element = ET.fromstring(xml)

        formula = ARXMLParser().readFMFormulaByFeaturesAndAttributes(element, FMConditionByFeaturesAndAttributes())

        assert formula.getAttributeRef().getValue() == "/FMAttributeDefModels/Model/AttributeB"
        assert formula.getFeatureRef() is None

    def test_read_feature_ref_only(self):
        xml = "<FM-COND xmlns='%s'><FEATURE-REF DEST='FM-FEATURE'>/FMFeatureModels/Model/FeatureA</FEATURE-REF></FM-COND>" % NS
        element = ET.fromstring(xml)

        formula = ARXMLParser().readFMFormulaByFeaturesAndAttributes(element, FMConditionByFeaturesAndAttributes())

        assert formula.getAttributeRef() is None
        assert formula.getFeatureRef().getValue() == "/FMFeatureModels/Model/FeatureA"

    def test_read_no_refs_leaves_both_none(self):
        xml = "<FM-COND xmlns='%s'/>" % NS
        element = ET.fromstring(xml)

        formula = ARXMLParser().readFMFormulaByFeaturesAndAttributes(element, FMConditionByFeaturesAndAttributes())

        assert formula.getAttributeRef() is None
        assert formula.getFeatureRef() is None

    def test_concrete_subclass_composes_group_reader(self):
        """
        The FMConditionByFeaturesAndAttributes complexType composes the
        FM-FORMULA-BY-FEATURES-AND-ATTRIBUTES group — its own helper composes
        the base group reader, so ATTRIBUTE-REF / FEATURE-REF round-trip
        through the subclass element reader.
        """
        xml = "<FM-COND xmlns='%s'>feature_a" "<FEATURE-REF DEST='FM-FEATURE'>/FMFeatureModels/Model/FeatureA</FEATURE-REF>" "</FM-COND>" % NS
        element = ET.fromstring(xml)

        formula = ARXMLParser().readFMConditionByFeaturesAndAttributes(element, FMConditionByFeaturesAndAttributes())

        assert formula.getMixedString() == "feature_a"
        assert formula.getFeatureRef().getValue() == "/FMFeatureModels/Model/FeatureA"
        assert formula.getFeatureRef().getDest() == "FM-FEATURE"
        assert formula.getAttributeRef() is None
