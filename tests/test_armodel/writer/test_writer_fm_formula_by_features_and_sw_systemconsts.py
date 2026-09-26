"""Writer tests for the FMFormulaByFeaturesAndSwSystemconsts group members.

Spec: R23-11 AUTOSAR_FO_TPS_FeatureModelExchangeFormat, Table 7.3, p.63.
XSD 00052 has NO own complexType for the class — it is group-only: group
FM-FORMULA-BY-FEATURES-AND-SW-SYSTEMCONSTS (line 62784) is an unbounded 0..*
choice of FEATURE-REF (DEST FM-FEATURE--SUBTYPES-ENUM, required), 0..1 per the
appinfo pureMM minOccurs=0 / maxOccurs=1.

NOTE: per Rule 0001.7 (abstract XML-bearing bases own reusable helpers) the
class owns writeFMFormulaByFeaturesAndSwSystemconsts; the concrete subclass
FMConditionByFeaturesAndSwSystemconsts (Table 7.4, not yet synced) will
compose it — until then the helper is pinned with a concrete test vehicle.
"""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate import FMFormulaByFeaturesAndSwSystemconsts
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.writer.arxml_writer import ARXMLWriter


class _ConcreteFormula(FMFormulaByFeaturesAndSwSystemconsts):
    pass


class TestWriteFMFormulaByFeaturesAndSwSystemconsts:
    def test_write_feature_ref(self):
        formula = _ConcreteFormula()
        feature_ref = RefType()
        feature_ref.setDest("FM-FEATURE")
        feature_ref.setValue("/FMFeatureModels/Model/FeatureA")
        formula.setFeatureRef(feature_ref)

        element = ET.Element("PARENT")
        ARXMLWriter().writeFMFormulaByFeaturesAndSwSystemconsts(element, formula)

        feature_element = element.find("FEATURE-REF")
        assert feature_element is not None
        assert feature_element.attrib["DEST"] == "FM-FEATURE"
        assert feature_element.text == "/FMFeatureModels/Model/FeatureA"
        assert len(element) == 1

    def test_write_no_feature_ref_emits_no_children(self):
        element = ET.Element("PARENT")
        ARXMLWriter().writeFMFormulaByFeaturesAndSwSystemconsts(element, _ConcreteFormula())

        assert len(element) == 0
