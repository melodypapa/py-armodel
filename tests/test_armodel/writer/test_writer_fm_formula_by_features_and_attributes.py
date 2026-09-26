"""Writer tests for the FMFormulaByFeaturesAndAttributes group members.

Spec: R23-11 AUTOSAR_FO_TPS_FeatureModelExchangeFormat, Table 7.1, p.61.
XSD 00052 has NO own complexType for the class — it is group-only: group
FM-FORMULA-BY-FEATURES-AND-ATTRIBUTES (line 62746) is an unbounded 0..* choice
of ATTRIBUTE-REF (DEST FM-ATTRIBUTE-DEF--SUBTYPES-ENUM, required) and
FEATURE-REF (DEST FM-FEATURE--SUBTYPES-ENUM, required), each 0..1.

NOTE: per Rule 0001.7 (abstract XML-bearing bases own reusable helpers) the
class owns readFMFormulaByFeaturesAndAttributes /
writeFMFormulaByFeaturesAndAttributes; the concrete subclass
FMConditionByFeaturesAndAttributes composes them (its complexType composes the
group), so the composition is pinned here through an FM-COND element too.
"""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate import FMConditionByFeaturesAndAttributes
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.writer.arxml_writer import ARXMLWriter


class TestWriteFMFormulaByFeaturesAndAttributes:
    def test_write_both_refs(self):
        formula = FMConditionByFeaturesAndAttributes()
        attribute_ref = RefType()
        attribute_ref.setDest("FM-ATTRIBUTE-DEF")
        attribute_ref.setValue("/FMAttributeDefModels/Model/AttributeB")
        formula.setAttributeRef(attribute_ref)
        feature_ref = RefType()
        feature_ref.setDest("FM-FEATURE")
        feature_ref.setValue("/FMFeatureModels/Model/FeatureA")
        formula.setFeatureRef(feature_ref)

        element = ET.Element("PARENT")
        ARXMLWriter().writeFMFormulaByFeaturesAndAttributes(element, formula)

        attribute_element = element.find("ATTRIBUTE-REF")
        assert attribute_element is not None
        assert attribute_element.attrib["DEST"] == "FM-ATTRIBUTE-DEF"
        assert attribute_element.text == "/FMAttributeDefModels/Model/AttributeB"
        feature_element = element.find("FEATURE-REF")
        assert feature_element is not None
        assert feature_element.attrib["DEST"] == "FM-FEATURE"
        assert feature_element.text == "/FMFeatureModels/Model/FeatureA"
        assert len(element) == 2

    def test_write_attribute_ref_only_omits_feature_ref(self):
        formula = FMConditionByFeaturesAndAttributes()
        attribute_ref = RefType()
        attribute_ref.setDest("FM-ATTRIBUTE-DEF")
        attribute_ref.setValue("/FMAttributeDefModels/Model/AttributeB")
        formula.setAttributeRef(attribute_ref)

        element = ET.Element("PARENT")
        ARXMLWriter().writeFMFormulaByFeaturesAndAttributes(element, formula)

        assert element.find("ATTRIBUTE-REF") is not None
        assert element.find("FEATURE-REF") is None

    def test_write_no_refs_emits_no_children(self):
        element = ET.Element("PARENT")
        ARXMLWriter().writeFMFormulaByFeaturesAndAttributes(element, FMConditionByFeaturesAndAttributes())

        assert len(element) == 0

    def test_concrete_subclass_composes_group_writer(self):
        """
        The FMConditionByFeaturesAndAttributes complexType composes the
        FM-FORMULA-BY-FEATURES-AND-ATTRIBUTES group — its own helper composes
        the base group writer, so ATTRIBUTE-REF / FEATURE-REF are emitted under
        the subclass element.
        """
        formula = FMConditionByFeaturesAndAttributes()
        formula.setMixedString("feature_a")
        feature_ref = RefType()
        feature_ref.setDest("FM-FEATURE")
        feature_ref.setValue("/FMFeatureModels/Model/FeatureA")
        formula.setFeatureRef(feature_ref)

        element = ET.Element("PARENT")
        ARXMLWriter().writeFMConditionByFeaturesAndAttributes(element, formula)

        written = element.find("FM-COND")
        assert written is not None
        assert written.text == "feature_a"
        feature_element = written.find("FEATURE-REF")
        assert feature_element is not None
        assert feature_element.attrib["DEST"] == "FM-FEATURE"
        assert feature_element.text == "/FMFeatureModels/Model/FeatureA"
