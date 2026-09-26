"""Reader tests for the FMFormulaByFeaturesAndSwSystemconsts group members.

Spec: R23-11 AUTOSAR_FO_TPS_FeatureModelExchangeFormat, Table 7.3, p.63.
XSD 00052 has NO own complexType for the class — it is group-only: group
FM-FORMULA-BY-FEATURES-AND-SW-SYSTEMCONSTS (line 62784) is an unbounded 0..*
choice of FEATURE-REF (DEST FM-FEATURE--SUBTYPES-ENUM, required), 0..1 per the
appinfo pureMM minOccurs=0 / maxOccurs=1.

NOTE: per Rule 0001.7 (abstract XML-bearing bases own reusable helpers) the
class owns readFMFormulaByFeaturesAndSwSystemconsts; the concrete subclass
FMConditionByFeaturesAndSwSystemconsts (Table 7.4, not yet synced) will
compose it — until then the helper is pinned with a concrete test vehicle.
"""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate import FMFormulaByFeaturesAndSwSystemconsts
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


class _ConcreteFormula(FMFormulaByFeaturesAndSwSystemconsts):
    pass


class TestReadFMFormulaByFeaturesAndSwSystemconsts:
    def test_read_feature_ref(self):
        xml = "<FM-COND xmlns='%s'>feature_a<FEATURE-REF DEST='FM-FEATURE'>/FMFeatureModels/Model/FeatureA</FEATURE-REF></FM-COND>" % NS
        element = ET.fromstring(xml)

        formula = ARXMLParser().readFMFormulaByFeaturesAndSwSystemconsts(element, _ConcreteFormula())

        assert formula.getFeatureRef().getValue() == "/FMFeatureModels/Model/FeatureA"
        assert formula.getFeatureRef().getDest() == "FM-FEATURE"

    def test_read_absent_feature_ref(self):
        xml = "<FM-COND xmlns='%s'>feature_a</FM-COND>" % NS
        element = ET.fromstring(xml)

        formula = ARXMLParser().readFMFormulaByFeaturesAndSwSystemconsts(element, _ConcreteFormula())

        assert formula.getFeatureRef() is None
